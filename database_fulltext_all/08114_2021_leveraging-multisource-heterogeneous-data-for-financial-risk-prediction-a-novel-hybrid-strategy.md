---
otero_id: 8114
otero_key: "8SEKVCDT"
title: "Leveraging Multisource Heterogeneous Data for Financial Risk Prediction: A Novel Hybrid-Strategy-Based Self-Adaptive Method"
authors: "Gang Wang; Gang Chen; Huimin Zhao; Feng Zhang; Shanlin Yang; Tian Lu"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/16118"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# LEVERAGING MULTISOURCE HETEROGENEOUS DATA FOR FINANCIAL RISK PREDICTION: A NOVEL HYBRID-STRATEGY-BASED SELF-ADAPTIVE METHOD<sup>1</sup>

Gang Wang School of Management, Hefei University of Technology, Hefei, Anhui, CHINA {wgedison@hfut.edu.cn}

Gang Chen School of Management, Fudan University, Shanghai, CHINA {chengang050970@foxmail.com}

Huimin Zhao Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee, Milwaukee, WI, U.S.A. {hzhao@uwm.edu}

Feng Zhang School of Management, Hefei University of Technology, Hefei, Anhui, CHINA {zhangfeng@mail.hfut.edu.cn}

Shanlin Yang School of Management, Hefei University of Technology, Hefei, Anhui, CHINA {yangsl@hfut.edu.cn}

Tian Lu Heinz College, Carnegie Mellon University, Pittsburgh, PA, U.S.A. {lutiansteven@gmail.com}

Emerging phenomena of ubiquitous multisource data offer promising avenues for making breakthroughs in financial risk prediction. While most existing methods for financial risk prediction are based on a single information source, which may not adequately capture various complex factors that jointly influence financial risks, we propose a hybrid-strategy-based self-adaptive method to effectively leverage heterogeneous soft information drawn from a variety of sources. The method uses a proposed new featuresparsity learning method to adaptively integrate multisource heterogeneous soft features with hard features and a proposed improved evidential reasoning rule to adaptively aggregate base classifier predictions, thereby alleviating both the declarative bias and the procedural bias of the learning process. Evaluation in two cases at the individual level (concerning borrowers at a P2P lending platform) and the company level (concerning listed companies in the Chinese stock market) showed that, compared with relying solely on hard features, effectively incorporating multisource heterogeneous soft features using our proposed method enabled earlier prediction of financial risks with desirable performance.

Keywords: Financial risk prediction, soft information, ensemble learning, hybrid learning strategy, adaptive integration, adaptive aggregation

## Introduction

Recent years have witnessed the rapid popularization of internet finance (e.g., internet insurance, peer-to-peer (P2P) lending, and consumer finance) in response to the demand for new financial services with higher efficiency and convenience (Butler et al. 2016; Wei and Lin 2016). This raises again, in the new context of fintech, the core issue of financial risk management, which has prevailed in the financial industry and has also been a hot research topic (Ge et al. 2017; Gomber et al. 2018). Generally, financial risks<sup>2</sup> cause damage to various stakeholders and may even weaken the stability and sustainability of the overall economy (Abbasi et al. 2012; Chen et al. 2016). For instance, financial risks are associated with such adverse effects as economic losses, reduction of revenues, increases in spending, unemployment, and government deficits (Karanikolos et al. 2013). Financial risk prediction (FRP), as an important instrument for taking precautions against losses due to financial risks, has been a focus of research for decades (Alfaro et al. 2008; Iyer et al. 2015). It is expected that FRP will be able to reveal potential financial risks in the near future, thus providing early warning signals and supporting related decision-making. Accordingly, extensive efforts, in both industry practice and academic research, have been devoted to FRP (Mild et al. 2015; Sun et al. 2018).

Generally, there are two important types of financial entities in financial markets: individual lenders and borrowers, who affect the microfinance market, and listed companies, which are associated with the stock market. At the individual level, the financial risk with respect to an individual’s default has attracted considerable concerns from government, industry, and researchers (Zhang and Liu 2012). Specifically, the sustainability and widespread popularity of P2P lending platforms, which operate fully online without the involvement of any financial institution, largely depend on the reliability of individual borrowers (Zhao et al. 2017). From a profit perspective, assessing a borrower’s default probability is critical for both the asset safety of lenders and the sustainability of the P2P lending market (Xia et al. 2017). Accordingly, there has been an upsurge of research on default risk prediction (DRP) in the emerging P2P lending context intended to guide nonprofessional lenders in making profitable investment decisions (Cai et al. 2016; Lin et al. 2013; Tan et al. 2018).

At the company level, the risk regarding a company’s financial distress has attracted continual attention since the 1960s (Altman 1968; Beaver 1966). Great losses resulting from a company’s financial distress pose a considerable threat to companies, investors, and government regulators (Lin et al. 2012). In extreme cases, such losses adversely affect the whole economic system and society (Kirkos 2015). In order to secure sufficient time and opportunity to correct or adjust business strategies in advance to minimize potential losses, efforts have been continually devoted to financial distress prediction (FDP) (Alfaro et al. 2008; Psillaki et al. 2010).

In summary, DRP at the individual level and FDP at the company level are two important representatives of financial risk prediction. Both problems have great implications for financial risk management. However, both DRP and FDP studies have long relied predominantly on a single information source for feature extraction, leading to homogeneous features and the incomplete evaluation of financial risks. DRP studies commonly use basic personal information, such as age, education, household, income, and loans (Guo et al. 2016; Serrano-Cinca and Gutiérrez-Nieto 2016), while financial ratios derived from a company’s disclosed accounting information are conventionally and continually used in FDP (Serrano-Cinca and GutiéRrez-Nieto 2013; Zhou et al. 2016).

In terms of methodology, similar methods have been applied to DRP and FDP. Some statistical methods used earlier for building FDP models include discriminant analysis (Altman 1968; Karels and Prakash 1987), logit regression analysis (Martin 1977; Ohlson 1980), and factor analysis (West 1985). Recently, machine learning methods have been more widely used in FDP (Barboza et al. 2017), with decision tree (Olson et al. 2012; Sun et al. 2018), artificial neural network (Geng et al. 2015; Zhou et al. 2016), and support vector machine (SVM) (du Jardin 2018; Liang et al. 2016) representing some examples. Methods used for DRP include linear regression (Iyer et al. 2015), logistic regression (Cai et al. 2016; Ge et al. 2017), decision tree (Serrano-Cinca and Gutiérrez-Nieto 2016), and artificial neural network (Byanjankar et al. 2015). Moreover, there is now a trend of using ensemble methods to improve prediction performance over single classifiers in both FDP (Alfaro et al. 2008; Geng et al. 2015) and DRP (Wang et al. 2017; Xia et al. 2017).

Despite the extensive existing research on FRP, the big data era now offers new opportunities for further improvement by leveraging a variety of information sources unavailable before. While basic predictive information has shown considerable ability to reveal financial risks directly (Burtch et al. 2014; Zhang and Liu 2012), the increasing popularity of online platforms and social media (e.g., blogs, tweets, microblogs, and social news) is resulting in more and more heterogeneous sources of predictive information, including both hard information and soft information, hence introducing new possibilities (Dong et al. 2018; Li et al. 2018; Lu et al. 2019). By leveraging the characteristics of big data, such as high variety and high volume, learning from multisource heterogeneous soft information has the potential to lead to further improvements in FRP performance (Cecchini et al. 2010; Ge et al. 2017).

Unfortunately, existing FRP methods designed to deal with homogeneous predictive information sources are not easily adaptable to new scenarios with multisource heterogeneous information. Such scenarios present some new challenges, such as heterogeneous feature sources, heterogeneous feature structures, heterogeneous feature implications, and feature interactions. Since certain feature sources or feature structures naturally have their own unique predictive abilities, indiscriminately superposing or simply selecting multisource features may not fully capture their potential and may even hurt prediction performance (Zhao et al. 2015). This new phenomenon calls for a mechanism that can make effective use of valuable information available from heterogeneous sources by appropriately tackling the new challenges they pose.

To fill these gaps, we strive to develop a new FRP method that can effectively leverage multisource information with heterogeneous structures. We extract multiple types of features with heterogeneous structures based on data from a rich set of information sources and make multiple methodological contributions at different levels. We propose a novel hybrid-strategy-based self-adaptive method, named HSB\_RS (for hybrid-strategy-based random subspace), which adaptively integrates the multisource heterogeneous features and adaptively aggregates the predictions of a set of diverse base classifiers, thereby alleviating both the declarative bias and the procedural bias (Abbasi et al. 2012) of the learning process. Our HSB\_RS fundamentally adopts the framework of random subspace (RS) (Ho 1998) and further leverages the strengths of two new methods we propose specifically within HSB\_RS. One is a new feature-sparsity learning method called WFAL\_GW (i.e., weight-fused adaptive lasso incorporating group weighting) for adaptively integrating multisource heterogeneous features. The other is an improved evidential reasoning (ER) rule (Yang and Xu 2013) instantiated in and tailored to the context of classification called AER (i.e., adaptive ER) for adaptively aggregating the predictions of diverse base classifiers.

We empirically evaluated our proposed HSB\_RS using real data. Our experiments cover both FDP at the company level and DRP at the individual level. The FDP case concerns listed companies in the Chinese stock market, while the DRP case concerns borrowers on a Chinese P2P lending platform. Data available in the FDP case include both quantitative financial data and qualitative textual data, such as annual reports and financial news, from three independent sources. Five data sources are available in the DRP case, with some sources providing quantitative data, some providing qualitative textual data, and some providing both. Our experimental results in both cases demonstrate the effectiveness of our proposed method for FRP in leveraging multisource heterogeneous information, and its superiority over state-of-the-art methods in terms of prediction performance (compared with SVM using solely hard features, the proposed method, which leverages multisource heterogeneous data, improved the prediction AUC by up to 10.2% and 31.2%, respectively), providing evidence for the robustness of our proposed method.

## Literature Review

Financial risk analytics regarding different economic entities has attracted sustained attention for a long time as it can provide important implications and insights for stakeholders (e.g., managers, investors, regulators, borrowers, and lenders) (Zhang and Liu 2012; Zhao et al. 2017). Table A1 and Table A2 (in Appendix A) summarize existing relevant studies relating to DRP and FDP, respectively. The key differences across the studies relate to the information they used and the models they constructed, which are among the most important aspects that influence the performance of FRP (Chen et al. 2016; Kirkos 2015). Therefore, we focus our review of FRP research on relevant features and methods.

## Features for Financial Risk Prediction

Previous studies have commonly extracted features based on specific domain knowledge using disclosed data from public information platforms (Guo et al. 2016; Liu et al. 2015). For example, to examine rational herding among lenders in the P2P lending market, Zhang and Liu (2012) derived 16 basic features based on data from a microloan market. Liu et al. (2015) extracted basic features, such as a lender’s age, gender, education level, and prior bids, to investigate how friendship relationships affect a P2P lending site. Such domain-specific information has also been used in many other recent DRP studies (Butler et al. 2016; Cai et al. 2016).

Domain-specific basic features typically used in FDP are financial features, e.g., financial ratios derived from accounting data (Olson et al. 2012; Serrano-Cinca and GutiéRrez-Nieto 2013). Financial features, providing insights for understanding the financial prospect of a company, are conventionally used and are universally deemed to play a dominant role in FDP (du Jardin 2015; Liang et al. 2016). Their predictive abilities have been verified by numerous studies (du Jardin 2018; Sun et al. 2018). Kirkos (2015) reviewed research using financial ratios as financial distress predictors and found that both previous and recent studies relied solely on financial ratios.

The flourishing of online media, e.g., social media, has, in recent years, provided a variety of new information sources potentially useful for enhancing FRP performance. In light of this new phenomenon, Ge et al. (2017) predicted default in P2P lending by supplementing basic features with social media information. Burtch et al. (2014) evaluated the effects of cultural differences and geography on online prosocial lending using common language, immigration, diversity of ethnicity, and so on.

In the context of DRP, Iyer et al. (2015) categorized features into two types: hard and soft. Standard financial features (i.e., hard features) are based on hard essential information and are commonly used, while nonstandard features (i.e., soft features) can capture soft information, which comprises information difficult to quantify, as well as information that is quantifiable but has not been conventionally adopted. In this paper, for the convenience of discussion, we borrow the terms hard features and soft features to refer to standard and nonstandard features, respectively, in both DRP and FDP.

In the field of FDP, researchers have also become aware of the deficiencies of taking only hard financial features as inputs for FDP, such as their homogeneity, limited predictive power, and lack of reflection of external environments (Loughran and McDonald 2011; Tetlock et al. 2008). Beyond hard features, soft features have been explored for financial event detection (Cecchini et al. 2010).

## Methods for Financial Risk Prediction

Statistical and machine learning methods have been commonly used to predict financial risks (Chen et al. 2016; Kirkos 2015). Some widely used methods for DRP include logistic regression (Cai et al. 2016; Ge et al. 2017), decision tree (Serrano-Cinca and Gutiérrez-Nieto 2016), and artificial neural network (Byanjankar et al. 2015). Similar methods have also been applied to FDP (Alaka et al. 2017; Lin et al. 2012). Kumar and Ravi (2007) provided a comprehensive review of statistical and machine learning methods used in FDP and concluded that the interest and confidence in machine learning methods have grown enormously in recent years due to their promising performance. Chen et al. (2016) summarized recent studies on FDP, showing overwhelming evidence that machine learning methods, without relying on restrictive assumptions, can improve prediction performance over statistical methods.

Using ensemble methods to evaluate financial risks is now becoming a trend. For example, Wang et al. (2017) used an ensemble mixture random forest to identify a borrower’s default risk and empirically verified that their random forest outperformed a single tree. In a survey of FDP studies, Kirkos (2015) reported that building ensemble classifiers is a current trend. In a recent study, du Jardin (2018) suggested that the superior performance of ensemble models is associated with the way they capture a variety of financial distress situations.

## Research Gaps

Our literature review reveals some gaps in the existing FRP research. Regarding features, while domain-specific basic features have dominated FRP for a long time, recent studies have recognized the significance of soft features. However, applications of soft information have so far been limited to a certain homogeneous data source, far from exploiting the full potential of big data analytics (Ge et al. 2017; Iyer et al. 2015). For example, Ge et al. (2017) supplemented basic features with social media information in DRP in P2P lending, but they only explored quantitative indicators from the Weibo content whereas textual expressions were neglected.

Regarding methods, while many previous studies have run into difficulties in enhancing their homogeneous feature-based models, the boom of multisource data sheds light on new possibilities for further improving the performance of FRP models (Ge et al. 2017; Iyer et al. 2015). However, recent attempts to apply multisource heterogeneous features for FRP indiscriminately superposed the features (Iyer et al. 2015; Li et al. 2016; Lu et al. 2019), which not only cripples the predictive abilities of individual features but also restricts the integrative power of multisource heterogeneous features. Overall, the full potential of abundant soft data available for FRP remains to be exploited. It is imperative to explore effective ways to better leverage multisource heterogeneous features for FRP.

## Research Objective, Research Questions, and Research Design

Motivated by the aforementioned research gaps in the existing literature, our research objective in this study is to better leverage valuable multisource heterogeneous information for FRP, assuming data from the various sources have been collected and merged. This raises two research questions. First, it seems reasonable to expect the potential usefulness of multisource information for FRP. Prior research has shown that FRP on entities in a financial market is rooted in multiple factors (Iyer et al. 2015). Microfinance theory suggests that social networks can help reduce information asymmetry in P2P lending (Chen and Han 2012). Moreover, in the face of the vast variety of new information sources that are emerging, it is reasonable to anticipate that enhancing FRP performance by exploring more valuable information is a promising direction. We thus raise our first research question: What information sources, in addition to conventional sources of hard information, may be useful for enhancing FRP performance?

To answer this question, we examined existing studies that focus on FRP with new information sources to identify potentially useful sources. Social network information has been shown to help understanding borrowers’ default risks because borrowers are deterred from default due to potential social stigma costs (Ge et al. 2017). For example, phone usage data can reflect one’s purchase habits and natural characteristics and hence help to indicate borrowers’ repayment patterns (Ma et al. 2018). Meanwhile, the theory of financial risk suggests that externalities of risk are fundamental to understanding financial crisis (Estrada 2011). For example, textual information in annual reports and financial news has been found to be useful for revealing a company’s external environment (Cecchini et al. 2010). When textual social media content is leveraged for a company’s product defect discovery, distinctive terms and semantic factors embedded in texts turned out to be powerful predictors (Abrahams et al. 2015). Overall, financial risks should be understood from multiple perspectives. Quantifying the impacts of various information sources enables a better understanding of financial risks and provides decision makers with more comprehensive inputs for FRP (Li et al. 2018).

However, better leveraging multisource information intrinsically requires an effective mechanism that can consolidate the heterogeneous predictive capabilities. Hence, we endeavor to address our second research question: How is it possible to effectively leverage valuable multisource information for FRP?

In response to this question, we performed an in-depth analysis of the challenges (summarized in Table 1). To tackle all of these challenges, we first drew guidelines from the machine learning bias theory for our method design. Generally, there are two main types of bias in a machine learning process (Granger and Ramanathan 1984). The declarative (or representational) bias affects the representation of the hypothesis space and can be altered by adjusting the dimensionality and quality of the feature space, whereas the procedural bias depends on the way that classifiers explore the best hypotheses from the hypothesis space, with certain constraints. To alleviate these two types of bias, we propose a new hybrid learning strategy combining a data-driven strategy and a reasoning-driven strategy.

The data-driven strategy ensures that the integration of multisource features adheres to the features’ intrinsic characteristics (listed in Table 1), so that the declarative bias can be alleviated by a comprehensive feature space derived from multisource information. Following this strategy, we considered existing feature selection methods, with a focus on state-of-the-art lasso-based methods, in terms of their applicability and deficiencies. Feature selection methods can be broadly categorized into three types: filter, wrapper, and embedded (Gui et al. 2016). Both filter methods and wrapper methods take feature subsets for evaluation, so they are incapable of dealing with the challenges in the context of multisource heterogeneous feature integration (Table 1). Instead, lasso-based (embedded) methods can learn feature structures from an overall perspective and have several advantages over other feature selection methods (Gui et al. 2016). Lasso-based methods are founded on the basis of well-grounded theories and share some useful properties in the process of feature selection and model estimation. The criteria of lasso-based methods for feature selection are open to adaptation and redesign, thus allowing us to extend existing methods to more thoroughly address the new challenges (Table 1) that FRP is facing.

While there are several state-of-the-art lasso-based methods, none of them can fully tackle all the challenges (Table 1). For example, by incorporating a weighted fusion mechanism into lasso, weight fused lasso (WFL) was proposed to cope with redundancy among interrelated features (Daye and Jeng 2009). Nevertheless, this method treats all features equally while neglecting feature heterogeneity. As for the popular group lasso (GL) and sparse group lasso (SGL), they realize a feature selection process with feature grouping, which is potentially helpful for dealing with heterogeneous feature structures (Simon et al. 2013). In particular, SGL accommodates both group-wise and within-group sparsity and is more appropriate for our method design, since addressing the challenges (Table 1) intrinsically requires differentiating the predictive roles of both individual features and heterogeneous feature groups. However, it only takes preset feature structures into consideration, does not deal with feature interactions, and does not accommodate adaptability, which is addressed in adaptive lasso (AL) (Zou 2006). Therefore, we design a new method by synthesizing the strengths of these methods (i.e., AL, WFL, and SGL). On the other hand, it is a current trend to use ensemble methods to obtain more accurate results for FRP (du Jardin 2016).

<table><tr><td colspan="4">Table 1. New Challenges Posed by Multisource Information for FRP</td></tr><tr><td>Challenge</td><td>Description</td><td>Impact</td><td>Our solution</td></tr><tr><td>High dimensionality</td><td>Various types of features derived from multiple sources form a high-dimensional feature space.</td><td>Prediction models may be prone to overfitting in a high-dimensional feature space.</td><td>Repeatedly sampling feature subspaces based on feature importance.</td></tr><tr><td>Heterogeneous sources</td><td>Different feature properties and distributions.</td><td>Features from different sources hold unique predictive abilities.</td><td>Grouping and discriminating features by their sources.</td></tr><tr><td>Heterogeneous structures</td><td>Mutual complementarity and interference of heterogeneous features.</td><td>Features with heterogeneous structures need to be distinguished and coordinated.</td><td>Grouping and discriminating features by their structures.</td></tr><tr><td>Heterogeneous implications</td><td>Distinct implications of various types of features.</td><td>Features with heterogeneous implications help to reflect financial risks in different ways.a</td><td>Grouping and discriminating features by their implications.</td></tr><tr><td>Interactionsb</td><td>The predictive role of a feature interacts with those of other features.</td><td>Feature interactions weaken the stability of prediction models.</td><td>Learning from feature correlations when integrating features for use.</td></tr><tr><td>Need for adaptability</td><td>Adapting the selection bias on important multisource features.</td><td>Feature heterogeneity calls for different selection criteria.</td><td>Setting distinct adjustment for the weighting process on each feature.</td></tr><tr><td>Diverse prediction models</td><td>Multisource heterogeneous features result in diverse prediction models.</td><td>Weak models are overused or strong models are underused.</td><td>Incorporating the global weight and individual reliability of each prediction model.</td></tr><tr><td colspan="4">aFor example, positive and negative affections, as well as financial ratios from different accounting aspects, contribute to the predictive ability</td></tr></table>

<sup>a</sup> For example, positive and negative affections, as well as financial ratios from different accounting aspects, contribute to the predictive ability of FRP differently.  
<sup>b</sup> Winkler (1981) revealed that multisource information is intrinsically accompanied by the possibility of stochastic dependence, which provides a powerful argument for the necessity of dealing with interacting multisource features when integrating them for use.

By combining a set of base classifiers, ensemble methods often produce superior prediction results over single classifiers (Kirkos 2015). A commonly used result aggregation approach of ensemble methods is majority voting (Windeatt and Ardeshir 2004). However, since different base classifiers generated from multisource features possess different knowledge about the same given prediction task, useful information from classifiers relating to the minority class is more likely to be lost with a voting process. We posit that it is necessary to simultaneously assess the individual as well as collective effects of diverse base classifiers. We thus propose a reasoning-driven strategy to alleviate the procedural bias by adaptively aggregating the predictions of diverse and complementary base classifiers, such that the ensemble model’s performance can be robustly improved.

There is a long history of research on expert aggregation. Morris (1977) presented a Bayesian inference-based framework for aggregating independent experts’ decisions. In obtaining linear combinations of multiple prediction results, Granger and Ramanathan (1984) demonstrated that it is improper to restrict the weights of integrated units. After providing an overview of extensive research on multiple expert aggregation, Genest and Zidek (1986) summarized that the Bayesian paradigm tends to be the only satisfactory method for synthesizing conflicting decision results when an external decision maker is involved.

Jacobs (1995) emphasized that the key challenge for combining experts’ probability assessments is the high correlation among them. Overall, it is a sensible way to ensure independence across multiple probability distributions and aggregate them within a Bayesian inference process with a proper weighting scheme. All of these conclusions bring our attention to the evidential reasoning (ER) rule, which can combine a set of probability distributions conjunctively with weights and reliabilities (Yang and Xu 2013). Reliability helps to measure a classifier’s inherent predictive ability; weight reflects a classifier’s relative importance from a global view. With a mechanism based on weight and reliability, the ER rule potentially provides more rational aggregation of prediction models than conventional voting and averaging strategies.

Previous studies that introduced the ER rule into classification problems have encountered some difficulties. For example, Xu et al. (2017) took each feature as a piece of evidence and obtained the prediction result by manipulating features within an evidential reasoning process. However, such a practice becomes infeasible if heterogeneous and high-dimensional features are involved. Zhou et al. (2017a) used the ER rule for aggregating base classifiers in an ensemble. They defined the reliability of a base classifier as its similarity with others in terms of their predictions, whereas the weight of a base classifier is specified during the process of model training.

<table><tr><td colspan="9">Table 2. Comparison of WFAL_GW and Existing Lasso-Based Methods</td></tr><tr><td>Study</td><td>Method</td><td>Within-group sparse effect</td><td>Automatic grouping</td><td>Presupposed grouping</td><td>Within-group adaptation</td><td>Group-wise adaptation</td><td>Consistency in feature selection</td><td>Asymptotic normality</td></tr><tr><td>Genest and Zidek 1986</td><td>Lasso</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Yuan and Lin 2006</td><td>GL</td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Gui et al. 2016</td><td>WFL</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Zou 2006</td><td>AL</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td><td>√</td></tr><tr><td>Simon et al. 2013</td><td>SGL</td><td>√</td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Wang and Leng 2008</td><td>AGL</td><td></td><td></td><td>√</td><td></td><td>√</td><td>√</td><td>√</td></tr><tr><td>This study</td><td>WFAL_GW</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

Note: AGL: adaptive group lasso

<table><tr><td colspan="3">Table 3. Comparison of AER and Existing ER-Based Classification Methods</td></tr><tr><td>Study</td><td>Combination strategy for classification</td><td>Deficiency/solution</td></tr><tr><td>Polikar 2006</td><td>Dempster-Shafer theory</td><td>Led to counterintuitive results when used to combine highly conflicting evidence.</td></tr><tr><td>Bi et al. 2008</td><td>Evidential reasoning approach</td><td>Cannot effectively combine multiple pieces of evidence that are fully reliable individually but highly conflicting with each other.</td></tr><tr><td>Denceux and Masson 2012</td><td>Dempster-Shafer framework with linearly ordered frame of discernment</td><td>Without any consideration of evidence reliability.</td></tr><tr><td>Xu et al. 2017</td><td>ER rule</td><td>A scheme that takes features as evidence is infeasible in the face of high-dimensional feature spaces.</td></tr><tr><td>Zhou et al. 2017a</td><td>ER rule</td><td>The weight interacts with a model&#x27;s parameters, while the reliability is essentially determined by a voting process, which causes information loss.</td></tr><tr><td>This study</td><td>AER</td><td>Reliabilities are obtained through training, while weights are simultaneously derived through optimization.</td></tr></table>

This definition scheme for the ER rule also faces multiple drawbacks. First, its defined reliability is essentially a result of majority voting, which is incapable of reflecting the prediction ability of the model itself. Second, the weight determination and model construction are performed simultaneously, contradicting the independence requirement on evidence. Third, assigning weights to models before they are constructed fails to capture real intermodel dependencies.

Our analysis of the applicability and deficiencies of existing methods reveals that the focal context of this study fundamentally calls for a new feature selection method and a new model aggregation method, which can more effectively address the new challenges (Table 1) than existing methods. Guided by the data-driven strategy, we propose a new method WFAL\_GW (presented in the next section), which can tackle the challenges from the feature aspect. Guided by the reasoning-driven strategy, we propose a new aggregation method AER (presented in the next section), which enables the selection of a proper weight for each base classifier through training, meeting the need for making adaptive and full use of diverse predictions. In Table 2 and Table 3, we compare our WFAL\_GW and AER with existing relevant methods, respectively.

Overall, we propose a general framework for a hybrid-strategybased self-adaptive method for FRP (outlined in Figure 1). Based on multiple heterogeneous information sources, it first extracts both hard and soft features. Then, it divides the multisource features into groups by exploring their inherent heterogeneous structures. Next, following a data-driven strategy, it adaptively integrates multisource heterogeneous features to alleviate the declarative bias. Finally, following a reasoning-driven strategy, it adaptively aggregates the predictions of diverse base classifiers based on the integrated multisource heterogeneous features, thereby alleviating the procedural bias. We then instantiate this general framework and propose a concrete method (presented in the next section), which synthesizes the strengths of WFAL\_GW and AER.

![](/api/attachments/8SEKVCDT/fulltext/images/1345d24004b140d29e9e7d65863956dfd98a8d6d73d77aa8ad51997d8d35d9dc.jpg)  
Figure 1. Framework for a Hybrid-Strategy-Based Self-Adaptive Method

## Proposed Method

## Feature Extraction and Grouping

Features are extracted using data acquired from multiple sources. Basic hard features, e.g., financial ratios (du Jardin 2018; Sun et al. 2018), can be directly derived or indirectly calculated based on domain knowledge. While there is no universal guideline for properly selecting basic hard features, Alfaro et al. (2008) suggested three criteria: the selected features should be (1) commonly used, (2) available and computable, and (3) based on preliminary trials. For our proposed FRP method, we select basic hard features that have been frequently used and empirically verified as effective in previous studies.

A soft information source may contain both quantitative and qualitative data. For example, quantitative indicators extracted from a microblogging site have been demonstrated to be useful for indicating default risks (Ge et al. 2017). Meanwhile, the textual content of a microblog may also be useful (Li et al. 2016; Loughran and McDonald 2011). Several approaches, such as sentiment analysis (Loughran and McDonald 2011), bag-of-words (Zhang et al. 2011), and deep learning (Kraus and Feuerriegel 2017), can be used to assess the information embedded in textual narratives. In the context of product defect discovery, Abrahams et al. (2015) proposed an integrated framework for extracting features (lexical, stylistic, social, sentiment, and semantic features) from user-generated content, some of which are also applicable in FRP.

Two kinds of features are extracted from soft qualitative information in our method. First, metafeatures (e.g., sentiment) are extracted. Second, due to the insufficiency of metafeatures for FRP (Wang et al. 2018), we also use lowlevel lexical features. While the conventional bag-of-words approach loses context-specific information without considering word order, deep learning can preserve word order and context and, moreover, can capture nonlinear relationships among features (LeCun et al. 2015). Like Kraus et al. (2017), we adopt the long short-term memory (LSTM) network, which has been successfully applied to process sequential data with long dependencies in many fields, to generate qualitative lexical features.

In order to deal with the heterogeneity of features, we first divide all features into different groups according to their heterogeneous data sources, data structures, and implications (as described in Table 1) based on domain knowledge. Specifically, in FRP, quantitative features (e.g., financial ratios) naturally fall into different groups as they reflect different aspects (e.g., profitability, development capacity, solvency, operational capabilities, capital expansion capacity, and finance structure) of a company’s financial status (du Jardin 2016; Geng et al. 2015). We therefore map quantitative features into heterogeneous groups according to the domainspecific knowledge they hold. Metafeatures also fall into different groups. For example, sentiment features can be grouped into three typical polarities, i.e., positive, negative, and neutral (Wu and Cui 2018). Lexical features are typically high-dimensional without natural grouping structures. With the use of LSTM, lexical features are projected into a new feature space via nonlinear transformations, and by optimizing the activation functions of the gates and the target function in the last feedforward layer, lexical features are cast into a unified representation, rendering them homogeneous for the given prediction task (Kraus and Feuerriegel 2017). However, intrinsic heterogeneous structures may still be embedded in lexical features in correlative ways (e.g., multicollinearity), which may affect prediction performance (Zhao et al. 2015). We bestow the ability to automatically group correlated features on our proposed method WFAL\_GW to further tackle the multicollinearity problem resulting from the implicit heterogeneous structures.

## Hybrid Strategy-Based Random Subspace

Ensemble methods typically used for FRP include bagging, boosting, and random subspace (du Jardin 2016; du Jardin 2018). As our goal, multisource heterogeneous feature integration naturally requires a method or mechanism for feature space manipulation. Random subspace, which is based on feature space partitioning such that better base classifiers can be achieved in random subspaces rather than in the original feature space with redundant or irrelevant features (Ho 1998), shows its better fitness and an apparent advantage over bagging and boosting in this context. In this vein, we propose an ensemble method called hybrid strategy-based random subspace (HSB\_RS) to enhance the standard random subspace method, following our hybrid strategy.

As outlined in Figure 2, HSB\_RS consists of three main steps. It starts with adaptive feature integration using WFA\_GW (Step 1). WFA\_GW first uses SGL to weight multisource heterogeneous features at group-wise and within-group levels and then takes the obtained adaptive weight vector to learn the final feature weights by considering feature correlations. Taking the final feature weights as sampling probabilities, several feature subsets are generated by probabilistically resampling the features. The step for base classifier construction (Step 2) is straightforward and any classification method can be used. Once base classifiers are constructed on the feature subsets, they are adaptively aggregated using AER (Step 3), which specifies a reliability score vector and trains an adaptive weight vector for base classifiers to reflect their individual and global roles for aggregation.

## Data-Driven Strategy: Adaptive Integration of Multisource Heterogeneous Features

In light of the strengths and shortcomings of the aforementioned lasso-based methods, we propose a novel data-driven sparse method called weight-fused adaptive lasso incorporating group weighting (WFAL\_GW) to adaptively integrate multisource heterogeneous features. Our WFAL\_GW synthesizes the strengths of AL, WFL, and SGL. As mentioned before, regularized sparse models can share some useful properties, which are crucial for a good feature selection process (Daye and Jeng 2009). Oracle properties (i.e., asymptotic normality and consistency of estimation; Zou 2006) of WFAL\_GW with their proofs are provided in Appendix B, demonstrating its feasibility and effectiveness for integrating multisource heterogeneous features. Appendix B also shows the grouping effects of WFAL\_GW, which contribute to improving the feature quality by tackling implicit interrelationships.

Consider an FRP problem as a binary classification problem based on features, andp $y _ { i } \in \left\{ - 1 , 1 \right\}$ is the class to be predicted. Denote the grouped feature space as ${ \bf X } = [ { \bf x } _ { 1 } ^ { ( 1 ) } , { \bf x } _ { 2 } ^ { ( 1 ) } , . . . , { \bf x } _ { p _ { 1 } } ^ { ( 1 ) } , { \bf x } _ { 1 } ^ { ( 2 ) } , { \bf x } _ { 2 } ^ { ( 2 ) } , . . . , { \bf x } _ { p _ { 2 } } ^ { ( 2 ) } , . . . , { \bf x } _ { 1 } ^ { ( J ) } , { \bf x } _ { 2 } ^ { ( J ) } , . . . , { \bf x } _ { p _ { J } } ^ { ( J ) } ]$ where the superscript denotes the order of heterogeneous feature groups and the subscript denotes the order of features within a feature group.

![](/api/attachments/8SEKVCDT/fulltext/images/2dd4f6c77a3b93a1098167a26097dfb5e6c198a116276072fcc63ff7c9a1a3e2.jpg)  
Figure 2. Outline of the Proposed HSB\_RS

Let $\mathbf { u } = ( u _ { 1 } , u _ { 2 } , . . . , u _ { p } ) ^ { T } \in R _ { + } ^ { p }$ denote the nonnegative adaptive feature weight vector generated by SGL (Simon et al. 2013) and $\mathbf { v } = ( \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { p } ) ^ { T } \in R _ { + } ^ { p }$ denote the final feature weight vector generated by WFAL\_GW. To use regularized sparse models, the typical linear regression model is denoted as $y = \beta _ { 0 } + \sum _ { i = 1 } ^ { p } \beta _ { i } x _ { i } + e$ , where $\beta _ { i } \in R$ is the regression coefficient associated with feature $x _ { i }$ Without loss of generality, we assume that only $p _ { \mathrm { 0 } } \ ( \mathrm { \Delta } p _ { \mathrm { 0 } } < p$ ) features are relevant and ${ \frac { 1 } { n } } \mathbf { X } \mathbf { X } ^ { T } = \mathbf { B } ^ { n }  \mathbf { B }$ , where $\ddot { }  \{ \pmb { \mathscr { s } } \} $ is the limit operator that converges with probability one and B is a positive definite matrix. Further suppose that $\mathbf { B } = \left[ \begin{array} { l l } { \mathbf { b } _ { 1 1 } } & { \mathbf { b } _ { 1 2 } } \\ { \mathbf { b } _ { 2 1 } } & { \mathbf { b } _ { 2 2 } } \end{array} \right]$ , where ${ \bf b } _ { 1 1 }$ is a $p _ { 0 } \times p _ { 0 }$ matrix corresponding

to the $p _ { 0 }$ relevant features. Besides, refers to the∣∣ $L _ { \mathrm { 1 } }$ norm of a vector, and $\left. \cdot \right. _ { 2 }$ refers to the $L _ { 2 }$ norm of a vector. For asymptotic analysis, assume that the error term ise independent and identically distributed with zero mean and variance $\sigma ^ { 2 }$ . Moreover, each feature $\mathbf { X } _ { j }$ is normalized as $\underline { { x _ { i j } - \mu _ { j } } }$ , where $\mu _ { j }$ and $\sigma _ { j }$ are the mean and standard $\sigma _ { j }$ deviation of $\mathbf { X } _ { j }$ , respectively (Yuan and Lin 2006).

As shown in Figure 2, WFAL\_GW consists of two steps: SGL and WFAL (for weight fused adaptive lasso). In the first step, the extracted feature groups are superposed, and an initial weight vector is obtained by conducting SGL. The SGLu estimation can be characterized as<sup>3</sup>:

$$
\overline {{{{\boldsymbol {\gamma}}}}} ^ {*} = \arg \min _ {\boldsymbol {\gamma}} \left\{\frac {1}{2} \| \mathbf {y} - \mathbf {X} \boldsymbol {\gamma} \| _ {2} ^ {2} + \lambda (1 - \alpha) \sum_ {j = 1} ^ {J} \left\| \boldsymbol {\gamma} ^ {(j)} \right\| _ {2} + \lambda \alpha | \boldsymbol {\gamma} | \right\}.\tag{1}
$$

SGL takes into account distinctions among both feature groups and individual features, allowing both group-wise and within-group sparsity, through the two regularization terms. To construct proper adaptive penalties, WFAL\_GW takes the regression coefficients obtained by SGL as feature importance and adds the smoothing term $1 / { \sqrt { n } }$ to all weights in case some coefficients may be compressed to zero, following Zou (2006). This results in a novel adaptive penalty term $u _ { i } = \frac { 1 } { \mid \gamma _ { i } \mid + 1 / \sqrt { n } }$ . The first step is adjusted by

the parameter $\alpha \in [ 0 , 1 ]$ for desired effect of group-wise and within-group sparsity. $\alpha = 0$ and provide GL =1 and lasso as special cases, respectively. Besides, simultaneously adjusts the shrinkage on group-wise and within-group sparsity, and larger is associated with stronger shrinkage on features.

In the second step, the proposed WFAL, which takes asu the adaptive weight vector, is performed to get the final feature weight vector . In WFAL estimation, twov regularized constraints are imposed on the regression coefficients when minimizing residual sum of squares. It can be defined as the following optimization problem:

$$
\overline {{{\boldsymbol {\beta}}}} ^ {*} = \arg \min _ {\boldsymbol {\beta}} \left\{\frac {1}{2} \| \mathbf {y} - \mathbf {X} \boldsymbol {\beta} \| _ {2} ^ {2} + \lambda_ {1} \sum_ {i = 1} ^ {p} u _ {i} | \beta_ {i} | + \frac {\lambda_ {2}}{p} \sum_ {i, j = 1; i <   j} ^ {p} a _ {i j} \left(\beta_ {i} - s _ {i j} \beta_ {j}\right) ^ {2} \right\}\tag{2}
$$

where $a _ { i j } = \frac { \left| \rho _ { i j } \right| } { 1 - \left| \rho _ { i j } \right| }$ , and $s _ { i j } = \mathrm { s g n } ( \rho _ { i j } ^ { } ) = \left\{ { + 1 , \rho _ { i j } ^ { } > 0 } \right.$ . Here, the Pearson correlation coefficient is adopted to measure the $\rho _ { i j }$ correlation between two features $\mathbf { X } _ { i }$ and $\mathbf { X } _ { j }$ . The penalty term $\lambda _ { 1 } \sum _ { i = 1 } ^ { p } u _ { i } \mid \beta _ { i } \mid$ is imposed to induce an adaptive sparse solution for the feature vector . Meanwhile, the penaltyX term $\frac { \lambda _ { 2 } } { p } \sum _ { i , j = 1 ; i < j } ^ { p } a _ { i j } ( \beta _ { i } - s _ { i j } \beta _ { j } ) ^ { 2 }$ of weighted fusion, which penalizes pairwise differences of coefficients via correlationdriven weights, is introduced to deal with interrelated features, such that highly correlated features can be treated somewhat similarly, thereby suppressing arbitrary selection from a group of highly correlated features and underrepresentation of potentially valuable features (Daye and Jeng 2009). Overall, the proposed penalty can be regarded as a convex combination of the adaptive lasso and weight-fused lasso, with two parameters $\lambda _ { \mathfrak { i } }$ and $\lambda _ { 2 } \cdot \lambda _ { 1 }$ controls the scale of shrinkage on features. $\lambda _ { 2 }$ determines the penalty shrinkage degree imposed on the pairwise differences of features. Given the regression coefficient vector $\mathbf { \beta }$ estimated by Equation (2), we normalize its absolute values

$$
\mathbf {v}, \text {i.e.,} v _ {i} = \frac {\left| \beta_ {i} ^ {*} \right|}{\sum_ {j = 1} ^ {p} \left| \beta_ {j} ^ {*} \right|} \text {and} \sum_ {i = 1} ^ {p} v _ {i} = 1.
$$

Having derived , it is assigned to the feature vector .v x Subsequently, taking the weight vector as samplingv probabilities, feature subsets,N $\left\{ \mathbf { D } _ { s u b } ^ { 1 } , \mathbf { D } _ { s u b } ^ { 2 } , . . . , \mathbf { D } _ { s u b } ^ { N } \right\}$ , can be generated by probabilistically resampling the features. The subspace rate of random subspace is the samplingr proportion of a feature subset from the original features, so the probabilistically resampling process is adjusted by .r The feature subsets are then used to train baseN N classifiers.

## Reasoning-Driven Strategy: Adaptive Aggregation of Base Classifier Predictions

For the reasoning process of the ER rule in the context of ensemble learning, the evidence should be independent while the weight and reliability need to be defined in advance (Yang and Xu 2013). Xu et al. (2017) proposed acquiring evidence from the features, but this idea is not applicable to classification tasks with high-dimensional feature spaces. Considering individual classifiers as pieces of evidence, Zhou et al. (2017b) demonstrated independence among them—that is, their outputs are independent from each other, so the ER rule can be effectively used in result aggregation of an ensemble. In addition, we propose to define the reliability of an individual classifier as its classification performance. As FRP applications typically involve severe class imbalance and loss asymmetry, we use an aggregate performance measure, such as the widely used AUC (Bradley 1997), which depends solely on the outputs of a classifier (and not on the decision threshold), as a classifier’s reliability. Further, in order to ensure that results can be aggregated adaptively, we construct an optimal function for weight training purpose.

Assume there are base classifiers involved, with theN weight vector and the reliability vector of base classifiers denoted $\begin{array} { r l r l r } { \mathrm { a s } } & { { } } & { \mathbf { w } = ( w _ { 1 } , w _ { 2 } , . . . , w _ { N } ) ^ { T } \in R _ { + } ^ { N } } \end{array}$ and $\mathbf { R } = ( R _ { 1 } , R _ { 2 } , . . . , R _ { N } ) ^ { T } \in R _ { + } ^ { N }$ respectively. In the binary classification context of this study, each base classifier is deemed as an expert (evidence producer) and its predicted probability distribution on an instance corresponds to a piece of evidence. For a target instance that needs to be predicted, AER adaptively aggregates the predictions of the baseN classifiers to make the final prediction.

First, evidence $E _ { i }$ is profiled as

$$
E _ {i} = \{(\theta , p _ {\theta , i}) | \theta \subseteq \Theta , \sum_ {\theta \subseteq \Theta} p _ {\theta , i} = 1 \},\tag{3}
$$

where $\Theta = \{ - 1 , 1 \}$ is the set of mutually exclusive and collectively exhaustive hypotheses (binary classes). $( \theta , p _ { \theta , i } )$ is an element of evidence $E _ { i }$ , indicating that the evidence supports the class $\theta$ to the degree of $p _ { \theta , i }$ Evidence aggregation is performed by using a weighted belief distribution $m _ { i }$ with reliability (Yang and Xu 2013).

<sub>Specifically,</sub> <sub>reflects</sub> <sub>the</sub> <sub>support</sub> <sub>degree</sub> <sub>of</sub>m <sub>,i</sub> $E _ { i }$ for $\theta$ with consideration of weight and reliability.

$$
m _ {\theta , i} = c _ {R w, i} m _ {\theta , i},\tag{4}
$$

where $m _ { \theta , i } = \ * w _ { i } p _ { \theta , i }$ and $c _ { R w , i } = \frac { 1 } { 1 + w _ { i } - R _ { i } }$ . Then, without

consideration of the local ignorance of independentN classifiers, the joint support of the first two pieces of evidence $E _ { 1 }$ and $E _ { 2 }$ to the proposition can be calculated as follows.

$$
m _ {\theta , E (2)} = [ (1 - R _ {2}) m _ {\theta , 1} + (1 - R _ {1}) m _ {\theta , 2} ] + m _ {\theta , 1} m _ {\theta , 2}.\tag{5}
$$

By recursive calculation, the joint support of all pieces ofN evidence to $\theta$ can be derived. The combined evidence based on the first pieces of evidence is symbolized asC E C( )

$$
m _ {\theta , E (C)} = \left[ \left(1 - R _ {C}\right) m _ {\theta , E (C - 1)} + m _ {_ {P (\Theta)}, E (C - 1)} m _ {\theta , C} \right] + m _ {\theta , E (C - 1)} m _ {\theta , C};\tag{6}
$$

$$
P _ {\theta , E (C)} = \frac {m _ {\theta , E (C)}}{\sum_ {\theta \subseteq \Theta} m _ {\theta , E (C)}}.\tag{7}
$$

The final normalized result over N classifiers is represented as

$$
p _ {\theta , E (N)} = \frac {m _ {\theta , E (N)}}{1 - m _ {p (\Theta) , E (N)}},\tag{8}
$$

where $m _ { p ( \Theta ) , E ( N ) }$ is residual support of N classifiers.

$$
m _ {p (\Theta), E (N)} = (1 - R _ {i}) m _ {p (\Theta), E (N - 1)} \mathrm{and}
$$

$$
m _ {p (\Theta), E _ {i}} = c _ {R w, i} \left(1 - R _ {i}\right).
$$

Since the reliability has been specified, AER trains the weight vector by optimizing the following proposed objective function with a genetic simulated annealing algorithm.

$$
\mathbf {w} ^ {*} = \underset {\mathbf {w}} {\arg \min} \sum_ {i = 1} ^ {n} \left| y _ {i} - \operatorname{sgn} (p _ {\theta 1} ^ {(i)} - p _ {\theta 2} ^ {(i)}) \right| ^ {2}, \mathbf {w} \in (0, 1),\tag{9}
$$

where $p _ { \theta 1 } ^ { ( i ) }$ and $p _ { \theta 2 } ^ { ( i ) }$ denote the supports of base classifiers to the two classes (1 and -1) of instance .i

Pseudo-code: Figure 3 presents the pseudo-code for HSB\_RS, which comprises modules of adaptive feature weighting and feature subset sampling, base classifier construction, and prediction result reasoning and aggregation.

## Empirical Evaluation

We empirically evaluated the proposed HSB\_RS in two real cases at different levels (i.e., individual and company), involving DRP on borrowers at a major Chinese P2P lending platform and FDP on listed companies in the Chinese stock market, respectively.

## Data

## DRP Data

We collaborated with the P2P lending platform and collected data from five information sources (data descriptions are available in Appendix C). Since basic hard information has been deemed essential for DRP (Burtch et al. 2014; Liu et al. 2015), we first collected some basic data, including 14 hard features, about borrowers from the focal P2P lending platform.

As social media information may also be valuable to reveal one’s default risk, we crawled disclosed social media data of these borrowers from Weibo.com. Following but not limited to Ge et al. (2017), we extracted four quantitative features, i.e., numbers of followers, friends, fans, and messages. We also derived social interaction features based on the numbers of likes, forwards, and comments that each of a borrower’s messages had received. In addition, we merged the Weibo messages of each borrower and then extracted sentiment and lexical features from the merged text.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
HSB_RS (D,  $\alpha$ ,  $\lambda_{2}$ , r, J, N, CLF)

Input: Data set D;
SGL parameter  $\alpha$ ;
Weight-fused penalty parameter  $\lambda_{2}$ ;
Random subspace rate r;
Number of feature groups J;
Number of feature subsets N;
Base learner CLF.

Output: The final prediction result

1. Define the adaptive feature vector as  $u_{i} = \frac{1}{|\gamma_{i}| + 1/\sqrt{n}}$ 

2. Perform SGL with a preset  $\alpha$  and derive U

3. Convert Equation (2) using the Cholesky decomposition with a specified  $\lambda_{2}$ 

4. Conduct the WFAL_GW estimation and get V

5. Take V as sampling probability  $\varepsilon$ 

6.  $\left\{\mathbf{D}_{sub}^{1}, \mathbf{D}_{sub}^{2}, \ldots, \mathbf{D}_{sub}^{N}\right\} = RS(\mathbf{D}, r, \varepsilon)$ 

7. For  $i = 1, 2, \cdots, N$ 

8.  $h_{t} = CLF(\mathbf{D}_{sub}^{i})$ 

9. End For

10. Calculate the N base classifiers' reliability vector R with AUC

11. Train the N base classifiers' weight vector W

12. Adaptively aggregate the predictions of the N base classifiers ( $h_{i}, i = 1, 2, \cdots, N$ ) using AER

13. Return the aggregated result
</div>

## Figure 3. Pseudo-Code of HSB\_RS

Following Loughran and McDonald (2011), we extracted multiple sentiment features, corresponding to the counts and frequencies of words regarding positive sentiment, negative sentiment, strong modal, weak modal, and uncertainty, respectively. We used the positive and negative categories of the Chinese HowNet sentiment lexicons, <sup>4</sup> and used the “extreme/most,” “very,” “more,” and “over” categories as strong modal and the “-ish” and “insufficiently” categories as weak modal. We used the original uncertainty lexicon published by Loughran and McDonald (2011) and asked three doctoral students in a management school to translate uncertainty terms into Chinese.<sup>5</sup> Consistent with Kraus and Feuerriegel (2017), we extracted lexical features using LSTM. Specifically, we first used word2vec to convert textual data into word vectors in an embedding space and then trained an LSTM model on the word vectors to predict the class (default or not). Using the trained LSTM model as a prediction model, we took the outputs of the final hidden units of the last LSTM cell as lexical features. We used the word2vec module from genism, which is published by Google, and the Python module TensorFlow for LSTM. To explore how the predictive power of soft features from social media evolves over time, we divided the Weibo data into two parts based on the time when the loans took place, namely, T-1 (before loan start date) and T-0 (after loan start date).

Since it has been reported and empirically demonstrated that one’s contacts and social interactions through telecommunications can reflect one’s economic status (Ma et al. 2018), we collected call statistics of the borrowers in mobile communication. The statistics covered the number and total duration of calls to each of six types of contacts (i.e., spouse, parents, siblings, colleagues, classmates, and friends), as well as whether the registered name and ID were real.

Finally, we collected the borrowers’ online consumption statistics from Alipay (Zhifubao in Chinese), one of the largest third-party payment platforms, and online shopping data from Taobao, one of the most popular electronic retailing platforms globally. We posited that such online consumption and shopping data are internally linked to personal economic situations since online shopping and online payment have become increasingly prevalent in China. Our experiment results provide some evidence supporting this association. The data from these two sources include a large number of quantitative features. The Taobao data also include lexical features based on borrowers’ purchase records.

Other than the data crawled from Weibo.com, all of the data were derived through collaboration with the P2P lending platform and de-identified to preserve privacy. For the mobile call and Alipay data, we only received statistics without detailed data on individual calls or transactions. We collected data about loans that had a one-year term and were granted in 2016. For each loan, we collected data from all of the sources within the same time period as its loan term, using a rolling-window approach. The data collection periods for different loans were generally different because they started on different dates, but we collected one year of data for all the loans. Overall, there were 440 features in total in the DRP case.

The dataset consisted of 8,056 instances. Following previous DRP studies, we deemed a borrower whose loan was overdue for more than 120 days as a positive instance (i.e., default) (Ge et al. 2017). There were 1,844 positive and 6,212 negative instances, respectively.

Subsequently, we grouped quantitative features according to their sources and grouped sentiment features derived from Weibo data into three groups as they expressed different sentiment polarities (positive, neutral, and negative). Specifically, the positive group covered positive and strong modal words, the negative sentiment group covered negative and weak modal words, and the neutral group covered uncertainty words.

We conducted some exploratory analysis on the features (see Appendix E for details). First, we used the bag-of-words approach (unigrams) with TF-IDF and information gain to identify important terms reflecting blog content from Weibo.com. Then, we used WFAL\_GW to identify important features.

## FDP Data

We collected data about the 2,000 companies in the Shenzhen Stock Exchange and Shanghai Stock Exchange of China. Because there lacks consensus on the definition of financial distress, we used the special treatment (ST) warning mechanism as a symbol of financial distress, following a large number of previous studies (Geng et al. 2015; Zhou et al. 2016). Based on ST, there were 144 positive instances and 1,856 negative instances of financial distress in 2016. Financial distress is commonly predicted with data going back at least three years because whether a company is specially treated (ST) depends heavily on its previous financial performance in two consecutive years (Geng et al. 2015). To examine the effect of prediction time, we collected financial data from three years (T-3), four years (T-4), and five years (T-5) prior to the benchmark year (i.e., 2016), consistent with Geng et al. (2015).

Based on Alfaro et al.’s (2008) criteria, we extracted 39 financial ratios from CSMAR (China Security Market Accounting Research). We divided the financial ratios into six groups, according to the financial condition aspects they reflect, i.e., profitability, development capacity, solvency, operational capabilities, capital expansion capacity, and finance structure (Geng et al. 2015). For nonfinancial features, we extracted the annual reports (Cecchini et al. 2010; Hajek et al. 2014) from the official websites of the two exchanges and crawled financial news from Eastmoney,<sup>6</sup> one of the largest and most influential financial portals in China. We then extracted sentiment features and lexical features similarly as in the DRP case. In the FDP case, we also used a litigious lexicon in extracting sentiment features (Loughran and McDonald 2011), which were included in the negative sentiment group, because litigious terms are more likely to occur in reports of companies that appear to be involved in negative events and prospects. We used the litigious lexicon from Sougou,<sup>7</sup> one of the most popular input method-based lexicons in China. Overall, there were 319 features in total in the FDP case. Data descriptions and exploratory analysis are available in Appendix D and Appendix F, respectively.

## Experimental Procedure

We examined the effects of three factors—the learning method, the features used, and the prediction time—on prediction performance in both cases. First, we compared our proposed HSB\_RS to nine baselines: SVM, bagging (Serrano-Cinca and GutiéRrez-Nieto 2013; Sun et al. 2018), boosting (Alfaro et al. 2008; Zhou et al. 2016), random subspace (RS), random subspace incorporating lasso (Lasso\_RS) (du Jardin 2018), random subspace incorporating a standard ER rule (ER\_RS), PBM\_RS (du Jardin 2016), XGBoost (Chen and Guestrin 2016), and multilayer perceptron (MLP). We selected SVM as a baseline and the base learning method in all of the general ensemble methods, as our pilot examination showed its competency in performance and stability against other base classification methods (e.g., decision tree, artificial neural network, logistic regression, naive Bayes, and k-nearest neighbor) in both cases. We tested standard ensemble methods (i.e., bagging, boosting, and RS). To examine the effects of the two major inspirations for our method (i.e., lasso and ER rule), we included Lasso\_RS and ER\_RS as baselines. In ER\_RS, we used an equal weight for base classifiers and AUC as the measure of reliability. We tested a state-of-theart method proposed for FDP (i.e., PBM\_RS). Finally, we included XGBoost and MLP as representatives of advanced boosting and deep neural network methods. For the proposed HSB\_RS, we implemented the WFAL\_GW component in R based on a public lasso toolkit<sup>8</sup> and a public SGL toolkit,<sup>9</sup> and implemented the AER component in Java. We used standard modules in Weka, scikit-learn of Python 3.6, and R for most of the baselines, and implemented PBM\_RS in Java. For a fair comparison, all methods received the same inputs.

For each method, we tested its performance with hard features, soft features, and both, respectively, to examine the usefulness of incorporating multisource heterogeneous information. We also tested the effect of the prediction time. In the DRP case, we tested the two parts of Weibo data (i.e., T-1 and T-0). In the FDP case, we tested the three time spans (i.e., T-3, T-4, and T-5). Under each setting (i.e., combination of learning method, features used, and prediction time), we estimated the prediction performance using ten independent 10-fold crossvalidations, with each testing fold providing one performance estimate, thus resulting in 10\*10=100 performance estimates. We used AUC as an aggregate performance measure (Lin et al. 2017) (we also used other metrics, such as the Kolmogorov–Smirnov statistic [KS], Gini, and F1-score). Parameter setting and sensitivity analysis results are available in Appendices G and H.

## Results

Tables 4 and 5 summarize the results in terms of AUC (results in terms of KS, Gini, and F1-score are available in Appendix J) in the two cases, respectively. Overall, the results show similar patterns across the two cases.

HSB\_RS incorporating multisource heterogeneous features achieved the best performance (about 95% in mean AUC) under every time span in both cases. This demonstrates the superiority of our proposed FRP method over the baselines.

Compared to a single SVM classifier based solely on hard features, our proposed method improved the prediction performance by up to 10.2% (from 86.13% to 95.22%) and 31.2% (from 72.65% to 95.28% at T-5) in the DRP and FDP cases, respectively. This demonstrates the advantage of our method, which is designed based on a hybrid strategy adaptively integrating heterogeneous information drawn from a variety of sources and adaptively aggregating base classifier predictions.

## Effect of Incorporating Multisource Heterogeneous Features

Incorporating soft features improved performance for every method in both cases, showing that the performance improvement due to the use of multisource heterogeneous features was robust. The performance improvement ranged from 0.7% to 5.3% and from 0.7% to 7.0% in the DRP and FDP cases, respectively.

Although it is unrealistic to build practical prediction models with solely soft features, we included this setting in the experiment for completeness. The models with both hard and soft features always outperformed the corresponding models with soft features only. In the FDP case, the models with just hard features performed substantially better than the corresponding models with just soft features, showing that hard features are more informative and fundamental than the soft features extracted from annual reports and financial news. In the DRP case, however, the models with soft features were comparable to and often even better than the corresponding models with hard features, showing that the soft features based on social media, telecommunication, online shopping, and online consumption data can be very valuable.

While most of the existing studies (du Jardin 2016; Geng et al. 2015) rely on a single information source, our results show the value of multisource heterogeneous information in improving FRP performance and suggest that it is important to exploit soft features’ supplemental effect over conventional hard features. Soft information from a variety of sources reflecting various aspects about the target is especially important in scenarios (e.g., P2P lending) where many conventional hard features are not really verified and hence not particularly “hard.” Our findings shed light on the potential introduced by the vast variety of new information sources that are emerging.

<table><tr><td colspan="6">Table 4. Mean (Standard Deviation) of AUC (%) in the DRP Case</td></tr><tr><td rowspan="2">Method</td><td rowspan="2">Hard features</td><td colspan="2">Soft features</td><td colspan="2">Integrated features</td></tr><tr><td>T-1</td><td>T-0</td><td>T-1</td><td>T-0</td></tr><tr><td>SVM</td><td>86.13 (2.78)</td><td>86.11 (2.16)</td><td>86.17 (2.47)</td><td>90.90 (1.53)</td><td>89.96 (1.85)</td></tr><tr><td>Bagging</td><td>90.34 (2.17)</td><td>90.36 (1.91)</td><td>90.55 (1.86)</td><td>92.55 (0.65)</td><td>92.40 (0.91)</td></tr><tr><td>Boosting</td><td>90.54 (1.88)</td><td>90.28 (1.64)</td><td>90.10 (1.77)</td><td>91.59 (0.69)</td><td>90.98 (0.97)</td></tr><tr><td>RS</td><td>90.42 (2.25)</td><td>91.24 (1.19)</td><td>91.50 (1.18)</td><td>93.13 (0.51)</td><td>93.05 (0.56)</td></tr><tr><td>XGBoost</td><td>90.75 (2.07)</td><td>92.21 (1.06)</td><td>92.13 (1.04)</td><td>93.15 (0.78)</td><td>93.13 (0.76)</td></tr><tr><td>MLP</td><td>89.68 (2.28)</td><td>90.61 (1.56)</td><td>90.28 (1.78)</td><td>91.55 (1.39)</td><td>91.41 (1.41)</td></tr><tr><td>ER_RS</td><td>90.44 (2.51)</td><td>92.05 (0.89)</td><td>92.17 (0.92)</td><td>93.49 (0.35)</td><td>93.38 (0.41)</td></tr><tr><td>Lasso_RS</td><td>91.02 (2.01)</td><td>92.35 (0.41)</td><td>92.42 (0.48)</td><td>94.06 (0.14)</td><td>94.07 (0.21)</td></tr><tr><td>PBM_RS</td><td>90.63 (1.66)</td><td>92.35 (1.25)</td><td>92.87 (1.19)</td><td>93.94 (0.17)</td><td>93.97 (0.19)</td></tr><tr><td>HSB_RS</td><td>91.27 (1.94)</td><td>93.62 (0.37)</td><td>93.64 (0.33)</td><td>95.22 (0.13)</td><td>95.21 (0.11)</td></tr></table>

Table 5. Mean (Standard Deviation) of AUC (%) in the FDP Case

<table><tr><td rowspan="2">Method</td><td colspan="3">Hard features</td><td colspan="3">Soft features</td><td colspan="3">Integrated features</td></tr><tr><td>T-3</td><td>T-4</td><td>T-5</td><td>T-3</td><td>T-4</td><td>T-5</td><td>T-3</td><td>T-4</td><td>T-5</td></tr><tr><td>SVM</td><td>82.57(1.94)</td><td>74.55(1.31)</td><td>72.65(1.16)</td><td>70.38(4.39)</td><td>70.40(5.35)</td><td>71.36(4.58)</td><td>83.65(7.30)</td><td>75.05(7.23)</td><td>77.76(6.43)</td></tr><tr><td>Bagging</td><td>88.69(2.96)</td><td>84.32(3.99)</td><td>80.84(3.18)</td><td>72.40(5.35)</td><td>73.90(6.46)</td><td>72.63(6.32)</td><td>89.84(5.27)</td><td>86.48(7.44)</td><td>83.35(6.28)</td></tr><tr><td>Boosting</td><td>89.10(5.37)</td><td>88.30(5.32)</td><td>87.60(6.42)</td><td>77.76(4.39)</td><td>81.59(4.81)</td><td>80.81(4.01)</td><td>90.13(4.73)</td><td>89.21(4.79)</td><td>92.25(4.37)</td></tr><tr><td>RS</td><td>90.15(5.55)</td><td>90.13(5.76)</td><td>89.55(5.87)</td><td>80.34(3.51)</td><td>81.37(4.39)</td><td>81.63(3.97)</td><td>92.06(2.25)</td><td>92.47(3.24)</td><td>93.16(2.99)</td></tr><tr><td>XGBoost</td><td>90.14(4.73)</td><td>90.03(4.54)</td><td>89.18(5.81)</td><td>80.96(2.61)</td><td>81.45(4.51)</td><td>81.71(3.16)</td><td>92.04(1.96)</td><td>92.25(2.94)</td><td>92.95(2.60)</td></tr><tr><td>MLP</td><td>88.68(5.87)</td><td>87.53(6.78)</td><td>86.17(6.47)</td><td>77.24(4.28)</td><td>78.23(5.48)</td><td>78.50(4.98)</td><td>90.73(4.55)</td><td>90.22(4.37)</td><td>91.91(4.08)</td></tr><tr><td>ER_RS</td><td>90.24(5.56)</td><td>90.14(5.75)</td><td>89.59(5.88)</td><td>80.47(3.08)</td><td>81.47(3.60)</td><td>81.71(3.36)</td><td>92.11(2.24)</td><td>92.60(3.24)</td><td>93.21(2.91)</td></tr><tr><td>Lasso_RS</td><td>91.09(5.93)</td><td>90.81(5.80)</td><td>90.79(5.60)</td><td>81.15(3.22)</td><td>81.63(3.64)</td><td>81.29(3.60)</td><td>93.12(2.96)</td><td>93.97(3.77)</td><td>95.08(3.11)</td></tr><tr><td>PBM_RS</td><td>90.53(6.73)</td><td>90.26(7.28)</td><td>90.11(6.39)</td><td>79.47(4.84)</td><td>78.95(4.63)</td><td>80.71(4.09)</td><td>92.43(3.76)</td><td>92.93(4.35)</td><td>93.32(3.13)</td></tr><tr><td>HSB_RS</td><td>92.36(5.25)</td><td>91.51(5.24)</td><td>91.60(5.29)</td><td>82.38(2.90)</td><td>83.12(3.49)</td><td>82.40(2.64)</td><td>95.36(2.41)</td><td>94.47(3.43)</td><td>95.28(2.85)</td></tr></table>

## Effect of Learning Method

We focus the comparison of learning methods on the settings that incorporate multisource heterogeneous features (i.e., with both hard and soft features), as the previous analysis has established their superiority over relying on hard features alone. First, standard ensemble learning methods (i.e., bagging, boosting, and RS) improved performance over a single classifier in both cases. This finding is consistent with several previous studies (du Jardin 2018), which also found the usefulness of combining multiple classifiers.

Among the standard ensemble methods, RS outperformed bagging and boosting in both cases. This implies the advantage of methods based on feature splitting, such as RS, over instance partitioning or weighting-based methods like bagging and boosting, in dealing with high-dimensional feature spaces (Ho 1998). The multiple heterogeneous information sources used in our cases led to feature spaces with very high dimensionalities, rendering RS more effective than bagging and boosting.

Extending RS with lasso and the ER rule appears to have been useful; Lasso\_RS and ER\_RS outperformed RS in both cases. This shows the usefulness of feature weighting with regularized sparse model and result aggregation with the ER rule approach. The RS variant PBM\_RS (du Jardin 2016) also slightly improved the performance over the standard RS.

Our HSB\_RS further outperformed all RS variants, including the standard RS, Lasso\_RS, ER\_RS, and PBM\_RS. This shows the effectiveness of incorporating a two-stage adaptive process to adaptively integrate features and adaptively aggregate base classifier predictions using the proposed WFAL\_GW and AER. Finally, Our HSB\_RS also outperformed XGBoost and MLP. Statistical testing results comparing HSB\_RS and the baselines are available in Appendix I.

## Effect of Prediction Time

Having established the superiority of our HSB\_RS using all available multisource heterogeneous features, we focus the examination of the prediction time on such settings. In the DRP case, because of the limitations in data collection, only soft features from Weibo.com were extracted at different time spans (i.e., T-1 and T-0). There was almost no difference in performance between the two time spans. This is consistent with a previous study (Ma et al. 2018), which divided raw data into two sets in chronological order and achieved roughly the same results. Our results indicate that the predictive power of the information from a microblogging site, such as Weibo.com, can be quite stable over time. Users’ microblogs can reflect their inherent personality and characteristics, which are not subject to frequent changes, and may be correlated with individual risk preferences. By manually examining the Weibo content, we found that it is indeed rather prevalent for a borrower to express personal moods and habits on the platform (see Table E1). Different disclosure patterns reflect borrowers’ different personalities, which inherently connect to their default tendencies.

In the FDP case, all features were extracted during three time spans (i.e., T-3, T-4, and T-5), allowing for a more complete examination of the prediction time. With a simple method and limited information, such as SVM with hard features only, the prediction performance deteriorated substantially when moving the prediction earlier (i.e., from T-3 to T-4 to T-5). This finding is consistent with Geng et al. (2015) and explains why most previous studies (Alfaro et al. 2008; du Jardin 2015; Olson et al. 2012; Serrano-Cinca and GutiéRrez-Nieto 2013) did not attempt long-term prediction beyond T-3. However, with our proposed HSB\_RS, which incorporates multisource heterogeneous features, the prediction performance remained largely unchanged (no noticeable difference) when moving from T-3 to T-4 to T-5. This reveals the possibility of achieving accurate prediction earlier by capitalizing on soft features from a variety of sources. The main reason behind this phenomenon is that nonfinancial soft predictive information inherently implies an enduring predictive effect for FRP. Specifically, by manually checking the annual reports, we found that they contain descriptive information regarding a company’s longterm development, business plan, and strategy adjustment in such sections as important matters, business discussion, and company governance (see Table F1). Such contents help to reflect the external environment and long-term planning of a company, thus having more long-term effects on prediction than quantitative financial information. Our exploratory analysis also showed that a longer time interval led to smaller weights on financial features but larger weights on nonfinancial features (see Table F3). From this point of view, soft information facilitates the trade-off between prediction performance and promptness and allows for earlier forecasting of financial risks.

## Contributions, Implications, and Limitations

This study makes several contributions to the literature. First, it contributes to the design science paradigm of IS by proposing a novel artifact, a hybrid-strategy-based self-adaptive method (HSB\_RS) for FRP to better leverage heterogeneous multisource data that are becoming increasingly prevalent. By adaptively integrating heterogeneous multisource features and adaptively aggregating the predictions of multiple base classifiers through two proposed algorithms (i.e., WFAL\_GW and AER), HSB\_RS alleviates both the declarative bias and the procedural bias in a machine learning process (Abbasi et al. 2012). Although HSB\_RS was designed specifically for FRP, the hybrid learning strategy is more general and may be adapted to design effective prediction methods in other contexts, where heterogeneous data sources are emerging, posing a variety of challenges (summarized in Table 1) on effective consolidation of the heterogeneous predictive capabilities of such data sources. Some possible examples include electronic medical records and medical imaging data for health monitoring and various modes of business-customer interaction data (e.g., textual, audio, and video chat) for customer demand forecasting. Furthermore, we make multiple methodological contributions at different levels. While we designed HSB\_RS with two particular component methods (WFAL\_GW and AER), the hybrid-strategy-based self-adaptive framework underlying HSB\_RS provides a meta-ensemble method, allowing other appropriate component methods to be plugged in, replacing WFAL\_GW and AER. On the other hand, while we designed WFAL\_GW and AER specifically within HSB\_RS, they are also quite general and may become useful components of other ensemble learners.

Second, this study provides a general method for predicting financial risks at different levels, e.g., FDP at the company level and DRP at the individual level. Such unification provides inspiration for researchers to enrich their methodologies toward broader applicability.

Third, this study takes into account multisource heterogeneous information, including both hard information and soft information. It empirically demonstrates the usefulness of some emerging sources of data, thus broadening our knowledge about useful predictors for financial risks.

The performance improvement achieved by our proposed method has practical implications for various stakeholders (e.g., P2P lending platforms and lenders in DRP, and stockholders, executives, and regulators in FDP) affected by financial risks. More accurate predictions allow for better decision-making among these stakeholders. Furthermore, our empirical evaluation shows that predictions with comparable performance can be made earlier when qualitative soft information, which better reflects long-term financial prospects, is incorporated, thus providing more time and opportunities for stakeholders to react to potential financial risks. We provide some practical guidelines, including a roadmap for deploying our method in practice and a pipeline of data extraction, preparation, and processing, in Appendix K and Appendix L, respectively.

Our proposed method presents a new way for practitioners to achieve improved risk predictions by leveraging a variety of data sources. It may be further applied to emerging phenomena, e.g., predicting financial risks associated with the recently flourishing P2P lending platforms themselves (besides borrowers), which has practical implications on the investment decisions of lenders. It may even be adapted to other practical contexts, e.g., financial fraud detection (Abbasi et al. 2012) and customer churn prediction.

Our work also has some limitations. First, while our empirical evaluation demonstrated the advantage of our method over various baselines in terms of prediction performance, there is “no free lunch” and the performance improvement inevitably comes at a cost. Our goal was to predict rather than to explain (Shmueli 2010). Our proposed method produces predictive models but not explanatory models. The increased model complexity certainly reduces model interpretability. When explanations are required, our complex model gives way to parsimonious and interpretable alternatives. Another limitation is the small sample size (144 positives and 1,856 negatives) in the FDP case of our empirical evaluation. While this sample size is comparable to those of many recent studies on FDP (see Table A2), which also investigate the risk for financial distress of Chinese listed companies, future research should examine a much larger sample by expanding to nonlisted companies, thereby enhancing generalizability.

## Conclusion

In response to the variety of data sources emerging in the big data era, we propose a novel FRP method (HSB\_RS) guided by a hybrid learning strategy. The method adaptively integrates heterogeneous features drawn from a variety of sources and adaptively aggregates the predictions of multiple base classifiers through two proposed algorithms, WFAL\_GW and AER. Empirical evaluation at both the individual level (concerning borrowers at a P2P lending platform) and the company level (concerning listed companies in the Chinese stock market) demonstrated the utility of our proposed method.

Our work opens up several avenues for future research. First, while we evaluated the proposed method in DRP regarding borrowers in P2P lending and FDP regarding listed companies, the generalizability of the method may be further validated. For example, there has been an upsurge of P2P lending platforms in recent years. As of 2018, there were over 6,000 P2P lending platforms in China alone, with more than half of them being classified as “problematic platforms” according to P2PEye.com. Hence, predicting the financial risk associated with a platform is an important new problem. Second, while we examined several information sources, future research could expand to a wider range of sources (e.g., discussion forums, social media and social networks, Google trend data, policies, public opinions, and import/export data) that are becoming increasingly available. Third, because of the limitations in data collection in the DRP case, we examined the temporal effect of soft features from Weibo.com only. The temporal effects of other types of features could be examined in future research.

## Acknowledgments

The authors would like to express their sincere gratitude to the senior editor, associate editor, and three anonymous reviewers for their constructive feedback, which has helped to improve the quality of this paper significantly. The first three authors contributed equally to this work. This work was supported in part by the National Natural Science Foundation of China (grant numbers 72071062, 71690230, 71521001, 71971067, 91546104, 71872050, 71531006).

## References

Abbasi, A., Albrecht, C., Vance, A., and Hansen, J. 2012. “Metafraud: A Meta-Learning Framework for Detecting Financial Fraud,” MIS Quarterly (36:4), pp. 1293-1327.

Abrahams, A. S., Fan, W., Wang, G. A., Zhang, Z., and Jiao, J. 2015. “An Integrated Text Analytic Framework for Product Defect Discovery,” Production Operations Management (24:6), pp. 975-990.

Alaka, H. A., Oyedele, L. O., Owolabi, H. A., Kumar, V., Ajayi, S. O., Akinade, O. O., and Bilal, M. 2017. “Systematic Review of Bankruptcy Prediction Models: Towards a Framework for Tool Selection,“ Expert Systems with Applications (94), pp. 164- 184.

Alfaro, E., García, N., Gámez, M., and Elizondo, D. 2008. “Bankruptcy Forecasting: An Empirical Comparison of Adaboost and Neural Networks,” Decision Support Systems (45:1), pp. 110-122.

Altman, E. I. 1968. “Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy,” The Journal of Finance (23:4), pp. 589-609.

Barboza, F., Kimura, H., and Altman, E. 2017. “Machine Learning Models and Bankruptcy Prediction,“ Expert Systems with Applications (83), pp. 405-417.

Beaver, W. H. 1966. “Financial Ratios as Predictors of Failure,” Journal of Accounting Research (4), pp. 71-111.

Bi, Y., Guan, J., and Bell, D. 2008. “The Combination of Multiple Classifiers Using an Evidential Reasoning Approach,” Artificial Intelligence (172:15), pp. 1731-1751.

Bradley, A. P. 1997. “The Use of the Area under the ROC Curve in the Evaluation of Machine Learning Algorithms,” Pattern Recognition (30:7), pp. 1145-1159.

Burtch, G., Ghose, A., and Wattal, S. 2014. “Cultural Differences and Geography as Determinants of Online Prosocial Lending,” MIS Quarterly (38:3), pp. 773-794.

Butler, A. W., Cornaggia, J., and Gurun, U. G. 2016. “Do Local Capital Market Conditions Affect Consumers’ Borrowing Decisions?” Management Science (63:12), pp. 4175-4187.

Byanjankar, A., Heikkilä, M., and Mezei, J. 2015. “Predicting Credit Risk in Peer-to-Peer Lending: A Neural Network Approach,” 2015 IEEE Symposium Series on Computational Intelligence: IEEE, pp. 719-725.

Cai, S., Lin, X., Xu, D., and Fu, X. 2016. “Judging Online Peer-to-Peer Lending Behavior: A Comparison of First-Time and Repeated Borrowing Requests,” Information & Management (53:7), pp. 857-867.

Cecchini, M., Aytug, H., Koehler, G. J., and Pathak, P. 2010. “Making Words Work: Using Financial Text as a Predictor of Financial Events,” Decision Support Systems (50:1), pp. 164- 175.

Chen, D. and Han, C. 2012. “A Comparative Study of Online P2P Lending in the USA and China,” Journal of Internet Banking and Commerce (17:2), pp. 1-15.

Chen, N., Ribeiro, B., and Chen, A. 2016. “Financial Credit Risk Assessment: A Recent Review,” Artificial Intelligence Review (45:1), pp. 1-23.

Chen, T. and Guestrin, C. 2016. “Xgboost: A Scalable Tree Boosting System,” Proceedings of the 22nd ACM Sigkdd International Conference on Knowledge Discovery and Data Mining, pp. 785-794.

Daye, Z. J. and Jeng, X. J. 2009. “Shrinkage and Model Selection with Correlated Variables Via Weighted Fusion,” Computational Statistics & Data Analysis (53:4), pp. 1284- 1298.

Denœux, T. and Masson, M.-H. 2012. “Evidential Reasoning in Large Partially Ordered Sets,” Annals of Operations Research (195:1), pp. 135-161.

Dong, W., Liao, S., and Zhang, Z. 2018. “Leveraging Financial Social Media Data for Corporate Fraud Detection,” Journal of Management Information Systems (35:2), pp. 461-487.

du Jardin, P. 2015. “Bankruptcy Prediction Using Terminal Failure Processes,” European Journal of Operational Research (242:1), pp. 286-303.

du Jardin, P. 2016. “A Two-Stage Classification Technique for Bankruptcy Prediction,” European Journal of Operational Research (254:1), pp. 236-252.

du Jardin, P. 2018. “Failure Pattern-Based Ensembles Applied to Bankruptcy Forecasting,” Decision Support Systems (107), pp. 64-77.

Estrada, F. 2011. “Theory of Financial Risk,” MPRA Paper 29665, University Library of Munich (https://mpra.ub.unimuenchen.de/29665/1/MPRA\_paper\_29665.pdf).

Ge, R., Feng, J., Gu, B., and Zhang, P. 2017. “Predicting and Deterring Default with Social Media Information in Peer-to-Peer Lending,” Journal of Management Information Systems (34:2), pp. 401-424.

Genest, C. and Zidek, J. 1986. “Combining Probability Distributions: A Critique and an Annotated Bibliography,” Statistical Science (1:1), pp. 114-135.

Geng, R., Bose, I., and Chen, X. 2015. “Prediction of Financial Distress: An Empirical Study of Listed Chinese Companies Using Data Mining,” European Journal of Operational Research (241:1), pp. 236-247.

Gomber, P., Kauffman, R. J., Parker, C., and Weber, B. W. 2018. “On the Fintech Revolution: Interpreting the Forces of Innovation, Disruption, and Transformation in Financial Services,” Journal of Management Information Systems (35:1), pp. 220-265.

Granger, C. W., and Ramanathan, R. 1984. “Improved Methods of Combining Forecasts,” Journal of Forecasting (3:2), pp. 197- 204.

Gui, J., Sun, Z., Ji, S., Tao, D., and Tan, T. 2016. “Feature Selection Based on Structured Sparsity: A Comprehensive Study,” IEEE Transactions on Neural Networks Learning Systems (28:7), pp. 1490-1507.

Guo, Y., Zhou, W., Luo, C., Liu, C., and Xiong, H. 2016. “Instance-Based Credit Risk Assessment for Investment Decisions in P2p Lending,” European Journal of Operational Research (249:2), pp. 417-426.

Hajek, P., Olej, V., and Myskova, R. 2014. “Forecasting Corporate Financial Performance Using Sentiment in Annual Reports for Stakeholders’ Decision-Making,” Technological and Economic Development of Economy (20:4), pp. 721-738.

Ho, T. K. 1998. “The Random Subspace Method for Constructing Decision Forests,” IEEE Transactions on Pattern Analysis and Machine Intelligence (20:8), pp. 832-844.

Iyer, R., Khwaja, A. I., Luttmer, E. F., and Shue, K. 2015. “Screening Peers Softly: Inferring the Quality of Small Borrowers,” Management Science (62:6), pp. 1554-1577.

Jacobs, R. A. 1995. “Methods for Combining Experts’ Probability Assessments,” Neural Computation (7:5), pp. 867-888.

Karanikolos, M., Mladovsky, P., Cylus, J., Thomson, S., Basu, S., Stuckler, D., Mackenbach, J. P., and McKee, M. 2013. “Financial Crisis, Austerity, and Health in Europe,” The Lancet (381:9874), pp. 1323-1331.

Karels, G. V. and Prakash, A. J. 1987. “Multivariate Normality and Forecasting of Business Bankruptcy,” Journal of Business Finance & Accounting (14:4), pp. 573-593.

Kirkos, E. 2015. “Assessing Methodologies for Intelligent Bankruptcy Prediction,” Artificial Intelligence Review (43:1), pp. 83-123.

Kraus, M. and Feuerriegel, S. 2017. “Decision Support from Financial Disclosures with Deep Neural Networks and Transfer Learning,” Decision Support Systems (104), pp. 38- 48.

Kumar, P. R., and Ravi, V. 2007. “Bankruptcy Prediction in Banks and Firms Via Statistical and Intelligent Techniques–a Review,” European Journal of Operational Research (180:1), pp. 1-28.

LeCun, Y., Bengio, Y., and Hinton, G. 2015. “Deep Learning,” Nature (521), pp. 436-444.

Li, Q., Chen, Y., Jiang, L. L., Li, P., and Chen, H. 2016. “A Tensor-Based Information Framework for Predicting the Stock Market,” ACM Transactions on Information Systems (34:2), Article 11.

Li, Q., Chen, Y., Wang, J., Chen, Y., and Chen, H. 2018. “Web Media and Stock Markets: A Survey and Future Directions from a Big Data Perspective,” IEEE Transactions on Knowledge and Data Engineering (30:2), pp. 381-399.

Liang, D., Lu, C.-C., Tsai, C.-F., and Shih, G.-A. 2016. “Financial Ratios and Corporate Governance Indicators in Bankruptcy Prediction: A Comprehensive Study,” European Journal of Operational Research (252:2), pp. 561-572.

Lin, M., Prabhala, N. R., and Viswanathan, S. 2013. “Judging Borrowers by the Company They Keep: Friendship Networks and Information Asymmetry in Online Peer-to-Peer Lending,” Management Science (59:1), pp. 17-35.

Lin, W.-Y., Hu, Y.-H., and Tsai, C.-F. 2012. “Machine Learning in Financial Crisis Prediction: A Survey,” IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) (42:4), pp. 421-436.

Lin, Y.-K., Chen, H., Brown, R. A., Li, S.-H., and Yang, H.-J. 2017. “Healthcare Predictive Analytics for Risk Profiling in Chronic Care: A Bayesian Multitask Learning Approach,” MIS Quarterly (41:2), 473-495.

Liu, D., Brass, D. J., Lu, Y., and Chen, D. 2015. “Friendships in Online Peer-to-Peer Lending: Pipes, Prisms, and Relational Herding,” MIS Quarterly (39:3), pp. 729-742.

Loughran, T. and McDonald, B. 2011. “When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10‐Ks,” The Journal of Finance (66:1), pp. 35-65.

Lu, T., Zhang, Y., and Li, B. 2019. “The Value of Alternative Data in Credit Risk Prediction: Evidence from a Large Field Experiment,” in Proceedings of the 40<sup>th</sup> International Conference on Information Systems, Munich, Germany.

Ma, L., Zhao, X., Zhou, Z., and Liu, Y. 2018. “A New Aspect on P2P Online Lending Default Prediction Using Meta-Level Phone Usage Data in China,” Decision Support Systems (111), pp. 60-71.

Martin, D. 1977. “Early Warning of Bank Failure: A Logit Regression Approach,” Journal of Banking & Finance (1:3), pp. 249-276.

Mild, A., Waitz, M., and Wöckl, J. 2015. “How Low Can You Go?—Overcoming the Inability of Lenders to Set Proper

Interest Rates on Unsecured Peer-to-Peer Lending Markets,” Journal of Business Research (68:6), pp. 1291-1305.

Morris, P. A. 1977. “Combining Expert Judgments: A Bayesian Approach,” Management Science (23:7), pp. 679-693.

Ohlson, J. A. 1980. “Financial Ratios and the Probabilistic Prediction of Bankruptcy,” Journal of Accounting Research (18:1), pp. 109-131.

Olson, D. L., Delen, D., and Meng, Y. 2012. “Comparative Analysis of Data Mining Methods for Bankruptcy Prediction,” Decision Support Systems (52:2), pp. 464-473.

Polikar, R. 2006. “Ensemble Based Systems in Decision Making,” IEEE Circuits Systems Magazine (6:3), pp. 21-45.

Psillaki, M., Tsolas, I. E., and Margaritis, D. 2010. “Evaluation of Credit Risk Based on Firm Performance,” European Journal of Operational Research (201:3), pp. 873-881.

Serrano-Cinca, C. and GutiéRrez-Nieto, B. 2013. “Partial Least Square Discriminant Analysis for Bankruptcy Prediction,” Decision Support Systems (54:3), pp. 1245-1255.

Serrano-Cinca, C. and Gutiérrez-Nieto, B. 2016. “The Use of Profit Scoring as an Alternative to Credit Scoring Systems in Peer-to-Peer (P2P) Lending,” Decision Support Systems (89), pp. 113- 122.

Shmueli, G. 2010. “To Explain or to Predict?,” Statistical Science (25:3), pp. 289-310.

Simon, N., Friedman, J., Hastie, T., and Tibshirani, R. 2013. “A Sparse-Group Lasso,” Journal of Computational and Graphical Statistics (22:2), pp. 231-245.

Sun, J., Lang, J., Fujita, H., and Li, H. 2018. “Imbalanced Enterprise Credit Evaluation with DTE-SBD: Decision Tree Ensemble Based on SMOTE and Bagging with Differentiated Sampling Rates,” Information Sciences (425), pp. 76-91.

Tan, F., Hou, X., Zhang, J., Wei, Z., and Yan, Z. 2018. “A Deep Learning Approach to Competing Risks Representation in Peerto-Peer Lending,” IEEE Transactions on Neural Networks Learning Systems (30:5), pp. 1565-1574.

Tetlock, P. C., Saar-Tsechansky, M., and Macskassy, S. 2008. “More Than Words: Quantifying Language to Measure Firms' Fundamentals,” The Journal of Finance (63:3), pp. 1437-1467.

Wang, G., Chen, G., and Chu, Y. 2018. “A New Random Subspace Method Incorporating Sentiment and Textual Information for Financial Distress Prediction,” Electronic Commerce Research and Applications (29), pp. 30-49.

Wang, H. and Leng, C. 2008. “A Note on Adaptive Group Lasso,” Computational Statistics Data Analysis (52:12), pp. 5277-5286.

Wang, Z., Jiang, C., Ding, Y., Lv, X., and Liu, Y. 2017. “A Novel Behavioral Scoring Model for Estimating Probability of Default over Time in Peer-to-Peer Lending,” Electronic Commerce Research and Applications (27), pp. 74-82.

Wei, Z. and Lin, M. 2016. “Market Mechanisms in Online Peer-to-Peer Lending,” Management Science (63:12), pp. 4236-4257.

West, R. C. 1985. “A Factor-Analytic Approach to Bank Condition,” Journal of Banking & Finance (9:2), pp. 253-266.

Windeatt, T. and Ardeshir, G. 2004. “Decision Tree Simplification for Classifier Ensembles,” International Journal of Pattern Recognition and Artificial Intelligence (18:05), pp. 749-776.

Winkler, R. L. 1981. “Combining Probability Distributions from Dependent Information Sources,” Management Science (27:4), pp. 479-488.

Wu, D. and Cui, Y. 2018. “Disaster Early Warning and Damage Assessment Analysis Using Social Media Data and Geo-

Location Information,” Decision Support Systems (111), pp. 48- 59.

Xia, Y., Liu, C., and Liu, N. 2017. “Cost-Sensitive Boosted Tree for Loan Evaluation in Peer-to-Peer Lending,” Electronic Commerce Research and Applications (24), pp. 30-49.

Xu, X., Zheng, J., Yang, J.-B., Xu, D.-l., and Chen, Y.-w. 2017. “Data Classification Using Evidence Reasoning Rule,” Knowledge-Based Systems (116), pp. 144-151.

Yang, J.-B. and Xu, D.-L. 2013. “Evidential Reasoning Rule for Evidence Combination,” Artificial Intelligence (205), pp. 1-29.

Yuan, M. and Lin, Y. 2006. “Model Selection and Estimation in Regression with Grouped Variables,” Journal of the Royal Statistical Society: Series B (68:1), pp. 49-67.

Zhang, J. and Liu, P. 2012. “Rational Herding in Microloan Markets,” Management Science (58:5), pp. 892-912.

Zhang, Y., Dang, Y., and Chen, H. 2011. “Gender Classification for Web Forums,” IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans (41:4), pp. 668-677.

Zhao, H., Liu, Q., Zhu, H., Ge, Y., Chen, E., Zhu, Y., and Du, J. 2017. “A Sequential Approach to Market State Modeling and Analysis in Online P2P Lending,” IEEE Transactions on Systems, Man, and Cybernetics: Systems (48:1), pp. 21-33.

Zhao, L., Hu, Q., and Wang, W. 2015. “Heterogeneous Feature Selection with Multi-Modal Deep Neural Networks and Sparse Group Lasso,” IEEE Transactions on Multimedia (17:11), pp. 1936-1948.

Zhou, L., Tam, K. P., and Fujita, H. 2016. “Predicting the Listing Status of Chinese Listed Companies with Multi-Class Classification Models,” Information Sciences (328), pp. 222- 236.

Zhou, Z., Zhou, Z.-J., Hao, H., Li, S., Chen, X., Zhang, Y., Folkert, M., and Wang, J. 2017a. “Constructing Multi-Modality and Multi-Classifier Radiomics Predictive Models through Reliable Classifier Fusion,” arXiv preprint arXiv:.01614).

Zhou, Z., Zhou, Z.-J., Hao, H., Li, S., Chen, X., Zhang, Y., Folkert, M., and Wang, J. 2017b. “Constructing Multi-Modality and Multi-Classifier Radiomics Predictive Models through Reliable Classifier Fusion” (https://arxiv.org/ftp/arxiv/papers/1710/ 1710.01614.pdf).

Zou, H. 2006. “The Adaptive Lasso and Its Oracle Properties,” Journal of the American Statistical Association (101:476), pp. 1418-1429.

## About the Authors

Gang Wang is a professor at the School of Management, Hefei University of Technology. He received his Ph.D. degree in Management Science and Engineering from the School of Management, Fudan University. His current research interests include business analytics, machine learning, fintech, and industrial big data analytics. His work has been published in such journals as Decision Support Systems, Information Processing and Management, IEEE Transactions on Instrumentation and Measurement, IEEE Transactions on Systems, Man, and Cybernetics: Systems, and IEEE Intelligent Systems, and in the proceedings of such conferences as the International Conference on Information Systems (ICIS), Pacific Asia Conference on Information Systems (PACIS), and Hawaii

International Conference on System Sciences (HICSS). He serves as an associate editor for Decision Support Systems

Gang Chen is a Ph.D. student in management science and engineering at Fudan University. His research interests include fintech, social media analytics, and multimodal deep learning. His work has appeared in such journals as IEEE Intelligent Systems, Electronic Commerce Research and Applications, and Applied Soft Computing, and in the proceedings of such conferences as the Pacific Asia Conference on Information Systems (PACIS) and Workshop on Information Technologies and Systems (WITS).

Huimin Zhao is a professor of information technology management at the Lubar School of Business, University of Wisconsin-Milwaukee. He received B.E. and M.E. degrees in automation from Tsinghua University, China and a Ph.D. degree in management information systems from the University of Arizona, U.S.A. His current research interests include data mining and healthcare informatics. He has published in such journals as MIS Quarterly, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Journal of Management Information Systems, Journal of the Association for Information Systems, and Decision Support Systems. He serves as a senior editor for Decision Support Systems, an associate editor for Information Systems Research, and an associate editor for the Journal of Business Analytics, and has served as an associate editor for MIS Quarterly. He served as a co-chair of the 19th Workshop on Information Technologies and Systems, the 5th INFORMS Workshop on Data Mining and Health Informatics, and the 9th China Summer Workshop on Information Management.

Feng Zhang is a Ph.D. student in management science and engineering at Hefei University of Technology. His research interests include industrial big data analytics, multi-view data mining, and machine learning. His work has appeared in the Journal of Intelligent Manufacturing.

Shanlin Yang is a member of the Chinese Academy of Engineering and the leading professor in management science and information systems at the School of Management, Hefei University of Technology. He is the director of the academic board of Hefei University of Technology and the director of the National-Local Joint Engineering Research Center of Intelligent Decision and Information Systems. He has won two second-class prizes for the State Scientific and Technological Progress Award and six first-class prizes for provincial- and ministerial-level science and technology awards. His research interests include information systems, cloud computing, and artificial intelligence.

Tian Lu is a postdoctoral fellow in the Heinz College at Carnegie Mellon University. He received his Ph.D. in management science and engineering from Fudan University. His work has appeared in such journals as Management Science, Journal of the Association for Information Systems, and Information & Management, and in the proceedings of such conferences as the International Conference on Information Systems (ICIS) and Hawaii International Conference on System Sciences (HICSS). His research interests include fintech, internet finance, ecommerce, and social media.

Related Studies

## Appendix A

<table><tr><td colspan="6">Table A1. Previous Studies on Individual Financial Risk Assessment in P2P Lending</td></tr><tr><td>Study</td><td>Features</td><td>Method(s)</td><td>Data source</td><td>Sample size</td><td>Best result(s)/ Conclusions</td></tr><tr><td>Zhang and Liu 2012</td><td>16 hard features</td><td>Dynamic generalized method of moments</td><td>Prosper.com</td><td>49,693</td><td>Found evidence of rational herding among lenders.</td></tr><tr><td>Chen and Han 2012</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Lenders in China rely more on “soft” information than lenders in America.</td></tr><tr><td>Yum et al. 2012</td><td>22 hard features</td><td>Logistic regression</td><td>Popfunding.com</td><td>5,211</td><td>Lenders seek the wisdom of crowds when information on creditworthiness is extremely limited.</td></tr><tr><td>Burtch et al. 2014</td><td>10 hard features</td><td>Poisson pseudo-maximum likelihood</td><td>Kiva.org</td><td>165,452</td><td>Lenders do prefer culturally similar and geographically proximate borrowers.</td></tr><tr><td>Lin et al. 2013</td><td>34 hard features</td><td>Cox proportional hazards</td><td>Prosper.com</td><td>56,584</td><td>Friendships increase the probability of successful funding.</td></tr><tr><td>Liu et al. 2015</td><td>29 hard features</td><td>Logit model</td><td>Chinese PPDAI</td><td>12,514</td><td>Friendships affect economic decisions.</td></tr><tr><td>Emekter et al. 2015</td><td>30 hard features</td><td>Logistic regression, Step-wise regression</td><td>Lending Club</td><td>61,451</td><td>A borrower's high FICO score and high income are associated with low default risk.</td></tr><tr><td>Iyer et al. 2015</td><td>18 hard features &amp; 11 soft features</td><td>Linear regression, ROC curve</td><td>Prosper.com</td><td>194,033</td><td>AUC: 75.43%</td></tr><tr><td>Malekipirbazari and Aksakalli 2015</td><td>30 hard features</td><td>RF, SVM, logistic regression, kNN</td><td>Lending Club</td><td>14,012/54,240</td><td>AUC: 71%, TP Rate: 0.88, FP Rate: 0.74:</td></tr><tr><td>Byanjankar et al. 2015</td><td>14 hard features</td><td>ANN, logistic regression</td><td>European Bondora</td><td>2,529/13,508</td><td>TP Rate: 74.39%, TN Rate: 62.71%</td></tr><tr><td>Guo et al. 2016</td><td>5 hard features</td><td>Instance-based method</td><td>Lending Club, Prosper</td><td>2,016/4,128</td><td>Sharpe ratio: 1.9976</td></tr><tr><td>Serrano-Cinca and Gutiérrez-Nieto 2016</td><td>19 hard features</td><td>Linear regression, DT</td><td>Lending Club</td><td>4,800/36,101</td><td>IRR: 2.30%-18.87%</td></tr><tr><td>Cai et al. 2016</td><td>10 hard features</td><td>Logistic regression</td><td>Chinese PPDAI</td><td>5,069</td><td>Confirmed the signals' power from the borrowing request.</td></tr><tr><td>Wei and Lin 2016</td><td>36 hard features</td><td>Game-theoretic model</td><td>Prosper.com</td><td>13,017</td><td>Auctions are not necessarily inferior in terms of overall social welfare.</td></tr><tr><td>Butler et al. 2016</td><td>35 hard features</td><td>OLS regression</td><td>Prosper.com</td><td>5,069</td><td>Borrowers who reside in areas with good access to bank finance request loans with lower interest rates.</td></tr><tr><td>Ge et al. 2017</td><td>8 hard features &amp; 4 soft features</td><td>Logistic regression</td><td>A Chinese P2P platform</td><td>35,457</td><td>AUC: 65.7%</td></tr><tr><td>Xia et al. 2017</td><td>15 hard features</td><td>Cost-sensitive XGBoost</td><td>Lending Club, We.com</td><td>448/4,798</td><td>AUC: 74.85%</td></tr><tr><td>Zhao et al. 2017</td><td>Segment intervals</td><td>Bayesian hidden Markov model</td><td>Prosper.com</td><td>4,243</td><td>Market state modeling can be applied to bidding prediction and herding detection.</td></tr><tr><td>Wang et al. 2017</td><td>26 hard features</td><td>RF</td><td>A Chinese P2P platform</td><td>6,079/52,573</td><td>AUC: 75.1%</td></tr><tr><td>Xia et al. 2018</td><td>17 hard features</td><td>SVM, RF, XGBoost, Bagging, Stacking</td><td>Lending Club, We.com</td><td>349/1072</td><td>AUC: 89.47%</td></tr><tr><td>Ma et al. 2018</td><td>90 soft features</td><td>AdaBoost</td><td>A Chinese P2P platform</td><td>1,111/1,916</td><td>AUC: 72%, TP Rate: 71.0%, TN Rate: 47.0%</td></tr><tr><td>Lu et al., 2019</td><td>117 hard and soft features</td><td>SVM, Logistic regression, RF, XGBoost, kNN, MLP</td><td>A Chinese P2P platform</td><td>2083/3101</td><td>Multisource data help enhance DRP and alleviate inequality in financial service markets</td></tr></table>

Note: kNN—k-nearest neighbors; DT—decision tree; SVM—support vector machine; ANN—artificial neural network; RF— random forests; TP—true positive; TN—true negative; FP—false positive; MLP—multi-layer perceptron. “/” in the sample size column divides instances into with default risk class (the former) and without default risk class. Note that accuracy is not an informative performance indicator when the classes (positive and negative) are largely imbalanced and the costs of the two types of misclassification errors (false positives and false negatives) are largely asymmetric.

Table A2. Studies on Financial Distress Prediction in the Past Decade (2008-2018)

<table><tr><td>Study</td><td>Time span</td><td>Features</td><td>Method(s)</td><td>Data source</td><td>Sample size</td><td>Best result(s)</td></tr><tr><td>Alfaro et al. 2008</td><td>T-1</td><td>16 financial features</td><td>ANN, boosting</td><td>SABI database of Bureau Van Dijk</td><td>590/590</td><td>Error rate: 8.9%</td></tr><tr><td>Peng et al. 2011</td><td>-</td><td>13 financial features</td><td>DT, NB, SVM, Ensemble</td><td>Korean bankruptcy dataset</td><td>65/130</td><td>AUC: 90.26%</td></tr><tr><td>Olson et al. 2012</td><td>T-1</td><td>18 financial features</td><td>DT, ANN, SVM</td><td>The LexisNexis database &amp; the Compustat database</td><td>100/100</td><td>Accuracy: 91.4%</td></tr><tr><td>Zhou et al. 2012</td><td>T-1</td><td>32 financial features</td><td>kNN, DT, NB, ANN, SVM, Boosting</td><td>Wharton Research Data Service &amp; ShenZhen and Shanghai stock markets</td><td>417/417</td><td>TP Rate: 70.4%, TN Rate: 53.1%, AUC: 79.7%</td></tr><tr><td>Sun and Li 2012</td><td>T-2</td><td>29 financial features</td><td>SVM</td><td>China Stock Market and Accounting Research Database</td><td>135/135</td><td>Accuracy: 91.67%</td></tr><tr><td>Serrano-Cinca and Gutiérrez-Nieto 2013</td><td>T-1,T-2</td><td>17 financial features</td><td>kNN, DT, NB, ANN, SVM, Bagging, Boosting</td><td>Database from the Federal Deposit Insurance Corporation</td><td>320/7,973</td><td>Type-I error: 36.11%, Type-II error: 4.26%</td></tr><tr><td>Geng et al. 2015</td><td>T-3,T-4,T-5</td><td>31 financial features</td><td>DT, ANN, SVM</td><td>China Security Market Accounting Research Database</td><td>107/107</td><td>Recall: 83.4%, Precision: 79.3%</td></tr><tr><td>du Jardin 2015</td><td>T-1,T-2,T-3</td><td>50 financial features</td><td>Logistic regression, ANN</td><td>French Diane</td><td>9,310/9,310</td><td>Accuracy: 85.1%</td></tr><tr><td>Zhou et al. 2016</td><td>T-1</td><td>164 financial features</td><td>kNN, DT, ANN, SVM, Boosting</td><td>China Stock Market and Accounting Research Database</td><td>18,551</td><td>Accuracy: 91.78%</td></tr><tr><td>du Jardin 2016</td><td>T-1</td><td>35 financial features</td><td>DT, ANN, Bagging, Boosting, Random Subspace</td><td>French Diane</td><td>110/110</td><td>Accuracy: 84.9%</td></tr><tr><td>Liang et al. 2016</td><td>-</td><td>190 financial features</td><td>kNN, DT, NB, SVM</td><td>Taiwan Economic Journal</td><td>239/239</td><td>Type-I error: 18.1%, Type-II error: 25.9%</td></tr><tr><td>du Jardin 2018</td><td>T-1</td><td>30 financial features</td><td>Logistic regression, DT, SVM, Bagging, Boosting, Random Subspace</td><td>French Diane</td><td>120/6,000</td><td>AUC: 83.7%, Type-I error: 23.08%, Type-II error: 16.66%</td></tr><tr><td>Sun et al. 2018</td><td>T-2</td><td>57 financial features</td><td>DT, Bagging</td><td>China Stock Market and Accounting Research Database</td><td>138/414</td><td>F-measure: 68.49%</td></tr><tr><td>Cecchini et al. 2010</td><td>T-1</td><td>Lexical features</td><td>SVM</td><td>Accounting and Auditing Enforcement Releases (AAERs) from the SEC website</td><td>78/78</td><td>Type-I error: 19.23%, Type-II error: 20.51%</td></tr><tr><td>Hajek et al. 2014</td><td>T-2</td><td>11 sentiment features</td><td>DT, ANN, SVM</td><td>Annual reports of U.S. companies</td><td>172/199</td><td>TP Rate: 86.9%, FP Rate:6.8%,</td></tr><tr><td>Hájek and Olej 2015</td><td>T-3</td><td>36 sentiment features</td><td>DT, ANN, SVM, Random Subspace</td><td>Annual reports (10-Ks filings) from U.S. SEC EDGAR System</td><td>386/386</td><td>TP Rate: 95.7%, FP Rate:8.3%,</td></tr><tr><td>Li et al. 2016</td><td>-</td><td>Financial features, sentiment features</td><td>Tensor-based model</td><td>China Stock Market and Accounting Research Database</td><td>100</td><td>Directional accuracy: 60%</td></tr></table>

Note: “-” in the time span column indicates that the adopted time span(s) are unknown. NB—Naive Bayesian. Only the largest sample size is listed if a study employed multiple datasets.

## Appendix B

## Properties of WFAL\_GW

## Theorem 1 (Oracle Properties)

Given data set $\mathbf { D } { = } \left[ \mathbf { X } , \mathbf { y } \right]$ , where $\mathbf X = \left[ \mathbf x _ { 1 } , \mathbf x _ { 2 } , . . . , \mathbf x _ { p } \right]$ , with $\mathbf { X } _ { i }$ standardized and centered. Supposey $\lambda _ { _ { \mathrm { n } } } / \sqrt { n }  _ { _ { p } } 0$ and $\lambda _ { \mathrm { n } } { \sqrt { n } }  \infty$ , where $\to _ { p }$ denotes convergence in probability. Let $ _ { d }$ denote convergence in distribution. Then, the WFAL\_GW estimate must satisfy the oracle properties, namely,

(1) Consistency in feature selection: $\operatorname* { l i m } _ { n \to \infty } ( \mathbf { \beta } - \mathbf { \beta } ) = \mathbf { O } _ { p } ( { \sqrt { n } } )$

(2) Asymptotic normality: $\sqrt { n } ( \mathbf { \substack { \{ \pmb { \beta } } - \pmb { \beta } \} } )  _ { d } N ( 0 , \sigma ^ { 2 } \mathbf { \mathbf { B } } _ { 1 1 } ^ { - 1 } )$

## Theorem 2 (Grouping Effect)

Given data set $\mathbf { D } { = } \left[ \mathbf { X } , \mathbf { y } \right]$ , where $\mathbf X = \left[ \mathbf x _ { 1 } , \mathbf x _ { 2 } , . . . , \mathbf x _ { p } \right]$ , with $\mathbf { X } _ { i }$ standardized and centered. Supposey $\lambda _ { 1 } \neq 0 , \lambda _ { 2 } \neq 0$ , and $\overline { { a } } _ { i } = \frac { 1 } { p } et { } { ' } \sum _ { m = 1 } a _ { i m }$ . Then, for $\beta _ { { \scriptscriptstyle i } } \beta _ { { \scriptscriptstyle i } } > 0$

$$
\begin{array}{l} \left| \overline {{\beta}} _ {i} - \overline {{\beta}} _ {j} \right| \leq \frac {\left\| \mathbf {y} \right\| _ {2} \sqrt {2 (1 - \rho_ {i j})} + \frac {\lambda_ {1}}{2} \left| u _ {i} - u _ {j} \right|}{\lambda_ {2} \overline {{a _ {i}}}} \\ \quad + (\left\| \mathbf {y} \right\| _ {2} + \frac {\lambda_ {1}}{2} u _ {j}) \left| \frac {1}{\lambda_ {2} \overline {{a _ {i}}}} - \frac {1}{\lambda_ {2} \overline {{a _ {j}}}} \right| \cdot \\ \quad + \frac {\lambda_ {2}}{p} \sum_ {m = 1} ^ {p} | (\frac {s _ {i m} a _ {i m}}{\lambda_ {2} \overline {{a _ {i}}}} + \frac {s _ {j m} a _ {j m}}{\lambda_ {2} \overline {{a _ {j}}}}) \overline {{\beta}} _ {m} | \end{array}\tag{B1}
$$

If $\rho _ { i j }  1 , \overline { { a _ { i } } }  1$ , then $| \beta _ { i } - \beta _ { { \mathrm { \ } } _ { j } } | \to 0$ . Accordingly, WFAL\_GW has grouping effects for interrelated features.

## Proof of Theorem 1

Let be defined as:Q

$$
\mathbf {Q} = \frac {1}{p} \left[ \begin{array}{c c c c} \sum_ {j \neq 1} a _ {1 j} & - s _ {1 2} a _ {1 2} & \dots & - s _ {1 p} a _ {1 p} \\ - s _ {1 2} a _ {1 2} & \sum_ {j \neq 2} a _ {2 j} & \dots & \vdots \\ \vdots & \vdots & \ddots & - s _ {(p - 1) p} a _ {(p - 1) p} \\ - s _ {1 p} a _ {1 p} & \dots & - s _ {(p - 1) p} a _ {(p - 1) p} & \sum_ {j \neq p} a _ {p j} \end{array} \right].\tag{B2}
$$

Wang et al. / Leveraging Multisource Heterogeneous Data for Financial Risk Prediction

Then, Equation (2) can be converted into:

$$
\boldsymbol {\beta} ^ {*} = \arg \min _ {\boldsymbol {\beta}} \left\{\frac {1}{2} \left\| \mathbf {y} - \mathbf {X} \boldsymbol {\beta} \right\| _ {2} ^ {2} + \lambda_ {1} \sum_ {i = 1} ^ {p} u _ {i} | \beta_ {i} | + \lambda_ {2} \boldsymbol {\beta} ^ {T} \mathbf {Q} \boldsymbol {\beta} \right\}.\tag{B3}
$$

Since $\mathbf { Q }$ is positive semi-definite, following Daye et al. (Daye and Jeng 2009), the Cholesky decomposition can be performed to derive decomposition $\mathbf { Q } = \mathbf { M } \mathbf { M } ^ { T }$ . Let $\mathbf { y } ^ { * } = { \left( \begin{array} { l } { \mathbf { y } } \\ { 0 } \end{array} \right) }$ and $\mathbf { X } ^ { * } = \left( \begin{array} { c } { \mathbf { X } } \\ { \sqrt { \lambda _ { 2 } } \mathbf { M } } \end{array} \right)$ , then Equation (B3) can be reformulated as:

$$
\boldsymbol {\beta} ^ {*} = \arg \min _ {\boldsymbol {\beta}} \left\{\frac {1}{2} \left\| \mathbf {y} ^ {*} - \mathbf {X} ^ {*} \boldsymbol {\beta} \right\| _ {2} ^ {2} + \lambda_ {1} \sum_ {i = 1} ^ {p} u _ {i} | \beta_ {i} | \right\}.\tag{B4}
$$

The form of Equation (B4) is consistent with that of adaptive lasso (Zou 2006), which defines the adaptive weight vector as ${ \bf w } = \left| \beta \right| ^ { - \gamma }$ and $\beta$ is estimated by performing the ordinary least squares. Here, we replace it with $u _ { i } = \frac { 1 } { \mid \gamma _ { i } [ S G L ] \mid + 1 / \sqrt { n } }  _ { p }  \gamma _ { i } [ S G L ]  ^ { - 1 }$ . According to the1 Theorem $^ 2$ in (Zou 2006), we can conclude that $\mathrm { W F A L \_ G W }$ satisfies oracle properties, namely, asymptotic normality and consistency of estimation.

## Proof of Theorem 2

Construct objective function $L$ as:

$$
L (\hat {\boldsymbol {\beta}}, \lambda_ {1}, \lambda_ {2}) = \left\| \mathbf {y} - \mathbf {X} \boldsymbol {\beta} \right\| _ {2} ^ {2} + \lambda_ {1} \sum_ {i = 1} ^ {p} u _ {i} | \beta_ {i} | + \frac {\lambda_ {2}}{p} \sum_ {i, j = 1; i <   j} ^ {p} a _ {i j} \left(\beta_ {i} - s _ {i j} \beta_ {j}\right) ^ {2}.\tag{B5}
$$

Note that $\beta _ { i } \beta _ { j } > 0 ~ ( \mathrm { i . e . , } ~ \beta _ { i }$ and $\beta _ { j }$ share a common sign). By seeking partial derivatives of $\beta _ { i }$ and $\beta _ { j }$ , we have

$$
\begin{array}{l} \frac {\partial L (\boldsymbol {\beta} , \lambda_ {1} , \lambda_ {2})}{\partial \beta_ {i}} = - 2 \mathbf {X} ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) + \lambda_ {1} u _ {i} \operatorname{sgn} (\beta_ {i}) \\ \qquad + \frac {2 \lambda_ {2}}{p} (\beta_ {i} \sum_ {m = 1} ^ {p} a _ {i m} - \sum_ {m = 1} ^ {p} s _ {i m} a _ {i m} \beta_ {m}) \end{array} ,\tag{B6}
$$

$$
\begin{array}{l} \frac {\partial L (\boldsymbol {\beta} , \lambda_ {1} , \lambda_ {2})}{\partial \beta_ {j}} = - 2 \mathbf {X} ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) + \lambda_ {1} u _ {i} \operatorname{sgn} (\beta_ {j}) \\ \qquad + \frac {2 \lambda_ {2}}{p} (\beta_ {j} \sum_ {m = 1} ^ {p} a _ {i m} - \sum_ {m = 1} ^ {p} s _ {i m} a _ {i m} \beta_ {m}) \end{array} .\tag{B7}
$$

Setting $\frac { \partial L ( \Bumpeq , \lambda _ { 1 } , \lambda _ { 2 } ) } { \partial \beta _ { i } } = 0$ and $\frac { \partial L ( \mathbf { \boldsymbol { \mathsf { \beta } } } , \lambda _ { 1 } , \lambda _ { 2 } ) } { \partial \beta _ { i } } = 0$ , respectively, we find the following solutions

$$
\beta_ {i} = \frac {2 \mathbf {X} ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) - \lambda_ {1} u _ {i} \operatorname{sgn} \left(\beta_ {i}\right) + \frac {2 \lambda_ {2}}{p} \sum_ {m = 1} ^ {p} s _ {i m} a _ {i m} \beta_ {m}}{2 \lambda_ {2} \bar {a _ {i}}},\tag{B8}
$$

$$
\beta_ {j} = \frac {2 \mathbf {X} ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) - \lambda_ {1} u _ {i} \operatorname{sgn} \left(\beta_ {j}\right) + \frac {2 \lambda_ {2}}{p} \sum_ {m = 1} ^ {p} s _ {j m} a _ {j m} \beta_ {m}}{2 \lambda_ {2} \overline {{{a _ {i}}}}}.\tag{B9}
$$

Assume

$$
B = \left| \frac {2 \mathbf {X} ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) - \frac {\lambda_ {1}}{2} u _ {i} \operatorname{sgn} \left(\beta_ {i}\right)}{\lambda_ {2} \overline {{a _ {i}}}} - \frac {2 \mathbf {X} ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) - \frac {\lambda_ {1}}{2} u _ {j} \operatorname{sgn} \left(\beta_ {j}\right)}{\lambda_ {2} \overline {{a _ {j}}}} \right|.\tag{B10}
$$

Then,

$$
\left| \beta_ {i} - \beta_ {j} \right| \leq B + \frac {\lambda_ {2}}{p} \sum_ {m = 1} ^ {p} \left| (\frac {s _ {i m} a _ {i m}}{\lambda_ {2} \overline {{a _ {i}}}} - \frac {s _ {j m} a _ {j m}}{\lambda_ {2} \overline {{a _ {j}}}}) \beta_ {m} \right|.\tag{B11}
$$

$$
\text { It   is   known   that } \left| \frac {a}{b} - \frac {c}{d} \right| \leq \left| \frac {a - c}{b} \right| + | c | \left| \frac {1}{b} - \frac {1}{d} \right| \tag {DayeandJeng2009}. S o,
$$

$$
B \leq \left| \frac {\left(\mathbf {x} _ {i} - \mathbf {x} _ {j}\right) ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) - \frac {\lambda_ {1}}{2} \left(u _ {i} \operatorname{sgn} \left(\beta_ {i}\right) + u _ {j} \operatorname{sgn} \left(\beta_ {j}\right)\right)}{\lambda_ {2} \overline {{a _ {i}}}} \right| + \left| \mathbf {x} _ {j} ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) - \frac {\lambda_ {1}}{2} u _ {j} \operatorname{sgn} \left(\beta_ {j}\right) \right| \left| \frac {1}{\lambda_ {2} \overline {{a _ {i}}}} - \frac {1}{\lambda_ {2} \overline {{a _ {j}}}} \right| \tag {B12}
$$

For WFAL\_GW, we derive

$$
L (\boldsymbol {\beta}, \lambda_ {1}, \lambda_ {2}) \leq L (\boldsymbol {\beta} = 0, \lambda_ {1}, \lambda_ {2}) = \| \mathbf {y} \| _ {2},\tag{B13}
$$

and

$$
\left| \left(\mathbf {x} _ {i} - \mathbf {x} _ {j}\right) ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) \right| \leq \left\| \mathbf {x} _ {i} - \mathbf {x} _ {j} \right\| _ {2} \left\| \mathbf {y} - \mathbf {X} \boldsymbol {\beta} \right\| _ {2} \leq \left\| \mathbf {y} \right\| _ {2} \sqrt {2 (1 - \rho_ {i j})}.\tag{B14}
$$

Further,

$$
\left| \left(\mathbf {x} _ {i} - \mathbf {x} _ {j}\right) ^ {T} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) - \frac {\lambda_ {1}}{2} u _ {j} \operatorname{sgn} \left(\beta_ {j}\right) \right| \leq \left\| \mathbf {y} \right\| _ {2} + \frac {\lambda_ {1}}{2} u _ {j}.\tag{B15}
$$

Overall,

$$
B \leq \frac {\left\| \mathbf {y} \right\| _ {2} \sqrt {2 \left(1 - \rho_ {i j}\right)} + \frac {\lambda_ {1}}{2} \left| u _ {i} - u _ {j} \right|}{\lambda_ {2} \overline {{a _ {i}}}} + \left(\left\| \mathbf {y} \right\| _ {2} + \frac {\lambda_ {1}}{2} u _ {j}\right) \left| \frac {1}{\lambda_ {2} \overline {{a _ {i}}}} - \frac {1}{\lambda_ {2} \overline {{a _ {j}}}} \right|.\tag{B16}
$$

Finally, by adding Inequality (B11) and Inequality (B16), we can derive Inequality (B1).

## Appendix C

## Description of Data in the DRP (P2P Lending) Case

<table><tr><td colspan="2">Table C1. Hard Features</td></tr><tr><td>Feature</td><td>Description</td></tr><tr><td>Gender</td><td>-</td></tr><tr><td>Age</td><td>-</td></tr><tr><td>District</td><td>-</td></tr><tr><td>Zodiac sign</td><td>-</td></tr><tr><td>Ethnic group</td><td>-</td></tr><tr><td>Educational degree</td><td>-</td></tr><tr><td>Educational system</td><td>Standard duration (in years) for the highest degree</td></tr><tr><td># of contacts</td><td>The number of contacts between the borrower and the platform</td></tr><tr><td># of active contacts</td><td>The number of times that the borrower has contacted the platform</td></tr><tr><td># of passive contacts</td><td>The number of times that the platform has contacted the borrower</td></tr><tr><td>Is multi-loan</td><td>Whether the borrower has borrowed money from multiple platforms</td></tr><tr><td># of platforms contacted</td><td>The number of platforms the borrower has contacted</td></tr><tr><td># of platforms registered</td><td>The number of platforms the borrower has registered on</td></tr><tr><td># of platforms engaged</td><td>The number of platforms from which the borrower has borrowed money</td></tr></table>

<table><tr><td colspan="2">Table C2. Call Data-Based Soft Features</td></tr><tr><td>Feature</td><td>Description</td></tr><tr><td>If_Name_match</td><td>Whether the registered name matches the real one</td></tr><tr><td>If_ID_match_1</td><td>Whether the registered ID matches the real one</td></tr><tr><td># of calls_1</td><td>The number of times that the borrower has called their spouse</td></tr><tr><td># of calls_2</td><td>The number of times that the borrower has called their parents</td></tr><tr><td># of calls_3</td><td>The number of times that the borrower has called their siblings</td></tr><tr><td># of calls_4</td><td>The number of times that the borrower has called their colleagues</td></tr><tr><td># of calls_5</td><td>The number of times that the borrower has called their classmates</td></tr><tr><td># of calls_6</td><td>The number of times that the borrower has called their friends</td></tr><tr><td>Duration of calls_1</td><td>The total duration of the borrower&#x27;s calls with their spouse</td></tr><tr><td>Duration of calls_2</td><td>The total duration of the borrower&#x27;s calls with their parents</td></tr><tr><td>Duration of calls_3</td><td>The total duration of the borrower&#x27;s calls with their siblings</td></tr><tr><td>Duration of calls_4</td><td>The total duration of the borrower&#x27;s calls with their colleagues</td></tr><tr><td>Duration of calls_5</td><td>The total duration of the borrower&#x27;s calls with their classmates</td></tr><tr><td>Duration of calls_6</td><td>The total duration of the borrower&#x27;s calls with their friends</td></tr></table>

<table><tr><td colspan="2">Table C3. Alipay Data-Based Soft Features</td></tr><tr><td>Feature</td><td>Description</td></tr><tr><td>If_ID_match_2</td><td>Whether the registered ID at Alipay matches the real one</td></tr><tr><td># of binding cards</td><td>The number of bank cards binding with Alipay</td></tr><tr><td>Alipay balance</td><td>The balance of the borrower's Alipay account</td></tr><tr><td>Yu Ebao balance</td><td>The balance of the borrower's Yu Ebao account</td></tr><tr><td>Ant Check Later line</td><td>The borrower's credit line at Ant Check Later</td></tr><tr><td>Ant Check Later balance</td><td>The borrower's balance at Ant Check Later</td></tr><tr><td>Available borrowing amount</td><td>Available borrowing amount from Alipay</td></tr><tr><td>Remaining borrowing amount</td><td>Remaining available borrowing amount from Alipay</td></tr><tr><td>Expenditure</td><td>Expenditure amounts on 41 items</td></tr><tr><td>Expenditure ratio</td><td>Expenditure ratios (over the total expenditure) of 41 items</td></tr><tr><td>Income</td><td>Income amounts on 16 items</td></tr><tr><td>Income ratio</td><td>Income ratios (over the total income) on 16 items</td></tr><tr><td colspan="2">Table C4. Taobao Data-Based Soft Features</td></tr><tr><td>Feature</td><td>Description</td></tr><tr><td># of products</td><td>The number of products purchased by the borrower</td></tr><tr><td># of orders</td><td>The number of orders placed by the borrower</td></tr><tr><td>Consumption</td><td>The total consumption amount of the borrower</td></tr><tr><td>Average price</td><td>The average price of the purchased products</td></tr><tr><td>Average consumption</td><td>The average amount per consumption</td></tr><tr><td>Max consumption</td><td>The maximum consumption amount</td></tr><tr><td>Purchased items</td><td>Purchased items are represented by lexical features</td></tr></table>

Table C5. Weibo Data-Based Soft Features

<table><tr><td>Feature group</td><td colspan="4">Feature</td></tr><tr><td rowspan="4">Basic group</td><td># of followers</td><td># of friends</td><td># of fans</td><td># of messages</td></tr><tr><td>Max # of comments</td><td>Min # of comments</td><td>Mean # of comments</td><td>Std # of comments</td></tr><tr><td>Max # of likes</td><td>Min # of likes</td><td>Mean # of likes</td><td>Std # of likes</td></tr><tr><td>Max # of forwards</td><td>Min # of forwards</td><td>Mean # of forwards</td><td>Std # of forwards</td></tr><tr><td>Positive sentiment group</td><td># of positive words</td><td>Frequency of positive words</td><td># of strong modal words</td><td>Frequency of strong modal words</td></tr><tr><td>Negative sentiment group</td><td># of negative words</td><td>Frequency of negative words</td><td># of weak modal words</td><td>Frequency of weak modal words</td></tr><tr><td>Neutral sentiment group</td><td># of uncertainty words</td><td>Frequency of uncertainty words</td><td></td><td></td></tr><tr><td>Lexicon group</td><td>Lexical features</td><td></td><td></td><td></td></tr></table>

Note: The Max/Min/Mean/Std # of comments/likes/forwards are social interaction features. For each borrower, we collected the numbers of likes, forwards, and comments that each of the borrower’s messages had received on the Weibo platform. Then, we used the statistics (max, min, mean, and standard deviation) of these numbers as social interaction features.

<table><tr><td colspan="9">Table C6. Summary Statistics for Weibo-Based Sentiment Features</td></tr><tr><td rowspan="2">Sentiment feature</td><td colspan="4">T-1</td><td colspan="4">T-0</td></tr><tr><td>Max</td><td>Min</td><td>Mean</td><td>Std</td><td>Max</td><td>Min</td><td>Mean</td><td>Std</td></tr><tr><td># of positive words</td><td>10,255</td><td>0</td><td>415.74</td><td>494.25</td><td>9,647</td><td>0</td><td>417.04</td><td>481.54</td></tr><tr><td># of negative words</td><td>7,936</td><td>0</td><td>263.78</td><td>337.69</td><td>7,218</td><td>0</td><td>262.57</td><td>321.08</td></tr><tr><td># of strong modal words</td><td>1,170</td><td>0</td><td>47.06</td><td>60.49</td><td>1,131</td><td>0</td><td>47.11</td><td>59.32</td></tr><tr><td># of weak modal words</td><td>194</td><td>0</td><td>9.98</td><td>12.31</td><td>178</td><td>0</td><td>9.95</td><td>12.42</td></tr><tr><td># of uncertainty words</td><td>524</td><td>0</td><td>12.79</td><td>19.07</td><td>341</td><td>0</td><td>12.59</td><td>16.44</td></tr><tr><td>Frequency of positive words</td><td>0.253</td><td>0</td><td>0.076</td><td>0.021</td><td>0.250</td><td>0</td><td>0.077</td><td>0.022</td></tr><tr><td>Frequency of strong modal words</td><td>0.071</td><td>0</td><td>0.008</td><td>0.005</td><td>0.333</td><td>0</td><td>0.048</td><td>0.020</td></tr><tr><td>Frequency of negative words</td><td>0.300</td><td>0</td><td>0.047</td><td>0.017</td><td>0.100</td><td>0</td><td>0.009</td><td>0.006</td></tr><tr><td>Frequency of weak modal words</td><td>0.032</td><td>0</td><td>0.002</td><td>0.002</td><td>0.050</td><td>0</td><td>0.002</td><td>0.002</td></tr><tr><td>Frequency of uncertainty words</td><td>0.040</td><td>0</td><td>0.002</td><td>0.002</td><td>0.043</td><td>0</td><td>0.002</td><td>0.002</td></tr></table>

Table C7. Expenditure and Income Items at Alipay

<table><tr><td colspan="4">Expenditure items</td><td colspan="2">Income items</td></tr><tr><td>Chinese</td><td>English</td><td>Chinese</td><td>English</td><td>Chinese</td><td>English</td></tr><tr><td>提现</td><td>Cash withdrawal</td><td>珠宝</td><td>Jewelry</td><td>转账</td><td>Account-to-account transfer</td></tr><tr><td>服饰</td><td>Clothes &amp; accessories</td><td>借条还款</td><td>IOU repayment</td><td>借贷收入</td><td>Borrowing &amp; lending income</td></tr><tr><td>非借条还款</td><td>Non-IOU repayment</td><td>运动休闲</td><td>Sports &amp; leisure</td><td>支付宝充值</td><td>Alipay refill</td></tr><tr><td>理财</td><td>Financing</td><td>贷款还款</td><td>Loan repayment</td><td>非借条收入</td><td>Non-IOU income</td></tr><tr><td>转账</td><td>Account-to-account transfer</td><td>网络消费</td><td>Network consumption</td><td>理财</td><td>Financing</td></tr><tr><td>话费充值</td><td>Call fee prepay</td><td>彩票</td><td>Lottery</td><td>卖家收入</td><td>Seller income</td></tr><tr><td>出行旅游</td><td>Travel</td><td>物流</td><td>Logistics</td><td>个人红包</td><td>Personal red packet</td></tr><tr><td>护肤彩妆</td><td>Toiletry</td><td>线下消费</td><td>Offline consumption</td><td>劳动收入</td><td>Labor income</td></tr><tr><td>家装建材</td><td>Decorative material</td><td>医疗保健</td><td>Health care</td><td>消费退款</td><td>Consumption refund</td></tr><tr><td>食品</td><td>Food</td><td>其他红包</td><td>Other red packet</td><td>其他红包</td><td>Other red packet</td></tr><tr><td>母婴儿童</td><td>Maternal &amp; child supplies</td><td>教育培训</td><td>Education and training</td><td>保险理赔</td><td>Insurance claim</td></tr><tr><td>手机数码</td><td>Mobile phone &amp; digital product</td><td>生活服务</td><td>Living service</td><td>群红包</td><td>Group red packet</td></tr><tr><td>汽车消费</td><td>Vehicle-related consumption</td><td>群红包</td><td>Group red packet</td><td>活动收入</td><td>Event income</td></tr><tr><td>家居百货</td><td>Home furnishing</td><td>批发类消费</td><td>Wholesale consumption</td><td>彩票收入</td><td>Lottery income</td></tr><tr><td>游戏</td><td>Computer game</td><td>办公学习用品</td><td>Office supplies</td><td>保证金退回</td><td>Deposit refund</td></tr><tr><td>信用卡还款</td><td>Credit card repayment</td><td>公益基金</td><td>Public interest fund</td><td>其他</td><td>Other</td></tr><tr><td>餐饮</td><td>Catering</td><td>虚拟物品</td><td>Virtual goods</td><td></td><td></td></tr><tr><td>卖家消费</td><td>Seller consumption</td><td>信贷还款</td><td>Credit repayment</td><td></td><td></td></tr><tr><td>缴费</td><td>Payment</td><td>购物卡</td><td>Shopping card</td><td></td><td></td></tr><tr><td>个人红包</td><td>Personal red packet</td><td>其他</td><td>Other</td><td></td><td></td></tr><tr><td>保险</td><td>Insurance</td><td></td><td></td><td></td><td></td></tr></table>

## Appendix D

## Description of Data in the FDP (Listed Companies) Case

In order to distinguish sentiment features based on different data sources, we use “R\_” and “N\_” to indicate annual report-based sentiment features and financial news-based sentiment features, respectively, and “#” and “\*” to represent the count and the frequency of a sentiment type. In addition, sentiment types are symbolized by capitalized first letters, i.e., P (positive), N (negative), S (strong modal), W (weak modal), L (litigious), and U (uncertainty).

<table><tr><td colspan="6">Table D1. Grouped Financial Features</td></tr><tr><td>Category</td><td></td><td>Feature</td><td>Category</td><td></td><td>Feature</td></tr><tr><td rowspan="7">Profitability</td><td>A1</td><td>(Sales revenue - sales cost)/sales revenue</td><td rowspan="7">Operational capabilities</td><td>A21</td><td>Main business income/average total assets</td></tr><tr><td>A2</td><td>Net profit/sales revenue</td><td>A22</td><td>Sales revenue/average fixed assets</td></tr><tr><td>A3</td><td>Earnings before income tax/average total assets</td><td>A23</td><td>Main business cost/average inventory</td></tr><tr><td>A4</td><td>Net profit/average total assets</td><td>A24</td><td>Main business income/average balance of accounts receivable</td></tr><tr><td>A5</td><td>Net profit/average current assets</td><td>A25</td><td>Sales revenue/average current assets</td></tr><tr><td>A6</td><td>Net profit/average fixed assets</td><td>A26</td><td>Cost of sales/average payable accounts</td></tr><tr><td>A7</td><td>Net profit/average shareholders&#x27; equity</td><td>A27</td><td>Sales revenue/average working capital</td></tr><tr><td rowspan="4">Development capacity</td><td>A8</td><td>Main business income of this year/main business income of last year</td><td rowspan="4">Capital expansion capacity</td><td>A28</td><td>Net increase in cash and cash equivalents/number of ordinary shares</td></tr><tr><td>A9</td><td>Net profit of this year/net profit of last year</td><td>A29</td><td>Net assets/number of ordinary shares</td></tr><tr><td>A10</td><td>Total assets of this year/total assets of last year</td><td>A30</td><td>Net profit/number of ordinary shares</td></tr><tr><td>A11</td><td>Net assets of this year/net assets of last year</td><td>A31</td><td>Capital reserves/number of ordinary shares</td></tr><tr><td rowspan="9">Solvency</td><td>A12</td><td>Total liabilities/total assets</td><td rowspan="9">Finance structure</td><td>A32</td><td>Current assets/total assets</td></tr><tr><td>A13</td><td>Current assets/current liabilities</td><td>A33</td><td>Fixed assets/total assets</td></tr><tr><td>A14</td><td>(Current assets - inventory)/current liabilities</td><td>A34</td><td>Shareholders&#x27; equity/fixed assets</td></tr><tr><td>A15</td><td>Total liabilities/total shareholders&#x27; equity</td><td>A35</td><td>Current liabilities/total liabilities</td></tr><tr><td>A16</td><td>Current liabilities/total assets</td><td>A36</td><td>Cash flow/total assets</td></tr><tr><td>A17</td><td>Earnings before interest and tax (EBIT)/interest expense</td><td>A37</td><td>Accounts receivable/total liabilities</td></tr><tr><td>A18</td><td>Net operating cash flow/current liabilities</td><td>A38</td><td>Current liabilities/shareholders&#x27; equity</td></tr><tr><td>A19</td><td>Non-current liabilities/non-current liabilities + owners&#x27; equity)</td><td>A39</td><td>Working capital/total assets</td></tr><tr><td>A20</td><td>Net operating cash flow/total liabilities</td><td></td><td></td></tr></table>

Table D2. Grouped Annual Report-Based Sentiment Features

<table><tr><td rowspan="2">Span</td><td rowspan="2">Polarity feature</td><td colspan="4">Positive sentiment group</td><td colspan="6">Negative sentiment group</td><td colspan="2">Neutral group</td></tr><tr><td>R_#_P</td><td>R_#_S</td><td>R_*_P</td><td>R_*_S</td><td>R_#_N</td><td>R_#_W</td><td>R_#_L</td><td>R_*_N</td><td>R_*_W</td><td>R_*_L</td><td>R_#_U</td><td>R_*_U</td></tr><tr><td rowspan="4">T-3</td><td>Max</td><td>14,153</td><td>816</td><td>0.2160</td><td>0.0238</td><td>4,358</td><td>238</td><td>11,473</td><td>0.0932</td><td>0.0071</td><td>0.1733</td><td>927</td><td>0.0204</td></tr><tr><td>Min</td><td>494</td><td>15</td><td>0.0720</td><td>0.0006</td><td>95</td><td>1</td><td>266</td><td>0.0233</td><td>0.0000</td><td>0.0289</td><td>28</td><td>0.0006</td></tr><tr><td>Mean</td><td>5,480.69</td><td>100.33</td><td>0.1601</td><td>0.0029</td><td>2,114.34</td><td>14.81</td><td>4,670.72</td><td>0.0623</td><td>0.0004</td><td>0.1371</td><td>262.80</td><td>0.0078</td></tr><tr><td>Std</td><td>1,431.11</td><td>71.08</td><td>0.0142</td><td>0.0020</td><td>453.10</td><td>12.13</td><td>1,068.45</td><td>0.0065</td><td>0.0003</td><td>0.0107</td><td>68.84</td><td>0.0014</td></tr><tr><td rowspan="4">T-4</td><td>Max</td><td>27,757</td><td>2,516</td><td>0.2754</td><td>0.0384</td><td>9,465</td><td>349</td><td>12,859</td><td>0.0927</td><td>0.0054</td><td>0.1662</td><td>961</td><td>0.0150</td></tr><tr><td>Min</td><td>78</td><td>4</td><td>0.0976</td><td>0.0039</td><td>15</td><td>2</td><td>19</td><td>0.0301</td><td>0.0001</td><td>0.0412</td><td>0</td><td>0.0000</td></tr><tr><td>Mean</td><td>10,906.17</td><td>598.33</td><td>0.2010</td><td>0.0110</td><td>3,444.13</td><td>78.60</td><td>5,312.16</td><td>0.0638</td><td>0.0015</td><td>0.0983</td><td>303.47</td><td>0.0056</td></tr><tr><td>Std</td><td>2,901.68</td><td>213.19</td><td>0.0210</td><td>0.0029</td><td>868.75</td><td>29.22</td><td>1,249.43</td><td>0.0076</td><td>0.0004</td><td>0.0081</td><td>82.66</td><td>0.0010</td></tr><tr><td rowspan="3">T-5</td><td>Max</td><td>24,995</td><td>1,946</td><td>0.2690</td><td>0.0361</td><td>8,140</td><td>265</td><td>12,589</td><td>0.0987</td><td>0.0049</td><td>0.1215</td><td>961</td><td>0.0150</td></tr><tr><td>Min</td><td>2,067</td><td>70</td><td>0.0886</td><td>0.0039</td><td>711</td><td>16</td><td>989</td><td>0.0301</td><td>0.0005</td><td>0.0403</td><td>61</td><td>0.0013</td></tr><tr><td>Mean</td><td>10,226.02</td><td>566.48</td><td>0.2003</td><td>0.0111</td><td>3,248.83</td><td>74.66</td><td>4,959.47</td><td>0.0639</td><td>0.0015</td><td>0.0976</td><td>286.11</td><td>0.0056</td></tr><tr><td></td><td>Std</td><td>2,687.09</td><td>194.32</td><td>0.0210</td><td>0.0029</td><td>819.03</td><td>27.09</td><td>1,158.61</td><td>0.0078</td><td>0.0004</td><td>0.0078</td><td>79.68</td><td>0.0010</td></tr></table>

Table D3. Grouped Financial News-Based Sentiment Features

<table><tr><td rowspan="2">Span</td><td rowspan="2">Polarity feature</td><td colspan="4">Positive sentiment group</td><td colspan="6">Negative sentiment group</td><td colspan="2">Neutral group</td></tr><tr><td>N_#_P</td><td>N_#_S</td><td>N_*_P</td><td>N_*_S</td><td>N_#_N</td><td>N_#_W</td><td>N_#_L</td><td>N_*_N</td><td>N_*_W</td><td>N_*_L</td><td>N_#_U</td><td>N_*_U</td></tr><tr><td rowspan="4">T-3</td><td>Max</td><td>3,950</td><td>9,820</td><td>0.0194</td><td>0.0157</td><td>51,379</td><td>243</td><td>7,764</td><td>0.0655</td><td>0.0013</td><td>0.0200</td><td>64,776</td><td>0.1734</td></tr><tr><td>Min</td><td>0</td><td>11</td><td>0.0000</td><td>0.0007</td><td>63</td><td>0</td><td>18</td><td>0.0028</td><td>0.0000</td><td>0.0008</td><td>257</td><td>0.0648</td></tr><tr><td>Mean</td><td>389.64</td><td>721.82</td><td>0.0044</td><td>0.0086</td><td>3,272.08</td><td>12.48</td><td>657.51</td><td>0.0376</td><td>0.0001</td><td>0.0081</td><td>8,063.25</td><td>0.1083</td></tr><tr><td>Std</td><td>530.73</td><td>994.58</td><td>0.0026</td><td>0.0027</td><td>4,791.98</td><td>22.93</td><td>831.40</td><td>0.0114</td><td>0.0002</td><td>0.0030</td><td>7,704.26</td><td>0.0234</td></tr><tr><td rowspan="4">T-4</td><td>Max</td><td>5,081</td><td>4,996</td><td>0.0222</td><td>0.0204</td><td>16,829</td><td>84</td><td>3,420</td><td>0.0698</td><td>0.0007</td><td>0.0245</td><td>33,167</td><td>0.1597</td></tr><tr><td>Min</td><td>6</td><td>13</td><td>0.0010</td><td>0.0017</td><td>100</td><td>0</td><td>13</td><td>0.0088</td><td>0.0000</td><td>0.0015</td><td>609</td><td>0.0647</td></tr><tr><td>Mean</td><td>468.65</td><td>670.57</td><td>0.0050</td><td>0.0078</td><td>3,279.38</td><td>11.68</td><td>698.44</td><td>0.0371</td><td>0.0001</td><td>0.0081</td><td>8,678.81</td><td>0.1073</td></tr><tr><td>Std</td><td>601.13</td><td>645.13</td><td>0.0034</td><td>0.0029</td><td>3,052.14</td><td>13.63</td><td>622.35</td><td>0.0106</td><td>0.0001</td><td>0.0027</td><td>6,139.52</td><td>0.0191</td></tr><tr><td rowspan="3">T-5</td><td>Max</td><td>3,208</td><td>7,887</td><td>0.0191</td><td>0.0199</td><td>25,687</td><td>134</td><td>5,753</td><td>0.0769</td><td>0.0048</td><td>0.0162</td><td>50,474</td><td>0.1542</td></tr><tr><td>Min</td><td>1</td><td>2</td><td>0.0011</td><td>0.0028</td><td>15</td><td>0</td><td>1</td><td>0.0096</td><td>0.0000</td><td>0.0032</td><td>9</td><td>0.0431</td></tr><tr><td>Mean</td><td>404.29</td><td>705.26</td><td>0.0045</td><td>0.0077</td><td>3,418.02</td><td>12.36</td><td>834.60</td><td>0.0364</td><td>0.0002</td><td>0.0088</td><td>8,530.40</td><td>0.1000</td></tr><tr><td></td><td>Std</td><td>486.91</td><td>881.09</td><td>0.0022</td><td>0.0026</td><td>4,028.47</td><td>18.16</td><td>966.69</td><td>0.0107</td><td>0.0003</td><td>0.0026</td><td>8,077.55</td><td>0.0177</td></tr></table>

## Appendix E

## Exploratory Analysis on Features in the DRP (P2P Lending) Case

We conducted some exploratory analysis on features. First, since the lexical features derived by the deep learning approach (i.e., LSTM) are not comprehensible, we used the bag-of-words approach with TF-IDF to extract unigrams and sorted them in descending order by their information gain, so as to reveal the main blog content from Weibo.com. Then, to provide some insights into informative features that contribute to the predictive power in DRP, important features identified by WFAL\_GW—the weights of these features sum up to more than 50%—are listed in Table E2 and contrasted in Figure E1.

Based on Table E2, many hard features, such as “# of platforms contacted”, “educational level”, and “# of platforms registered”, were identified to be particularly important, thus confirming their fundamental role for DRP and explaining why priority has been constantly given to them in previous studies (Burtch et al. 2014; Iyer et al. 2015; Lin et al. 2013). Meanwhile, the results provide support for the usefulness of phone usage data-based features for DRP, in line with a prior study that reported that the total number of calls is a positive indicator of economic status (Ma et al. 2018). Moreover, friendships appeared to have more predictive ability than other relationships. For example, the weight of “# of friends” was larger than those of “# of followers” and “# of fans”, while the weight of “# of calls\_6” was larger than those of “# of calls\_4”, “# of calls\_2”, and “# of calls\_5”. These findings are consistent with some previous studies, which deemed the friendship relationship as a key determinant of one’s behavior in P2P lending (Ge et al. 2017; Liu et al. 2015).

Table E1. Top 30 Representative Weibo-Specific Words

<table><tr><td colspan="4">T-1</td><td colspan="4">T-0</td></tr><tr><td>Chinese</td><td>English</td><td>Chinese</td><td>English</td><td>Chinese</td><td>English</td><td>Chinese</td><td>English</td></tr><tr><td>希望</td><td>Hope</td><td>真心</td><td>Sincere</td><td>表情</td><td>Expression</td><td>怀念</td><td>Miss</td></tr><tr><td>越来越</td><td>More and more</td><td>强大</td><td>Powerful</td><td>鼓掌</td><td>Applause</td><td>轻松</td><td>Relaxed</td></tr><tr><td>感动</td><td>Moved</td><td>电影</td><td>Film</td><td>开心</td><td>Happy</td><td>努力</td><td>Effort</td></tr><tr><td>工作</td><td>Work</td><td>表情</td><td>Expression</td><td>真心</td><td>Sincere</td><td>分享</td><td>Share</td></tr><tr><td>梦想</td><td>Dream</td><td>时代</td><td>Era</td><td>希望</td><td>Hope</td><td>挑战</td><td>Challenge</td></tr><tr><td>完美</td><td>Perfect</td><td>忘记</td><td>Forget</td><td>漂亮</td><td>Pretty</td><td>仔细</td><td>Careful</td></tr><tr><td>可爱</td><td>Lovely</td><td>可怜</td><td>Pity</td><td>朋友</td><td>Friend</td><td>机会</td><td>Chance</td></tr><tr><td>第一</td><td>The first</td><td>喜欢</td><td>Like</td><td>爱情</td><td>Love</td><td>感动</td><td>Moved</td></tr><tr><td>朋友</td><td>Friend</td><td>快乐</td><td>Happiness</td><td>灵魂</td><td>Soul</td><td>成功</td><td>Success</td></tr><tr><td>人生</td><td>Life</td><td>力量</td><td>Power</td><td>第一</td><td>The first</td><td>明白</td><td>Clear</td></tr><tr><td>加油</td><td>Cheer</td><td>新闻</td><td>News</td><td>工作</td><td>Work</td><td>伤害</td><td>Harm</td></tr><tr><td>期待</td><td>Expect</td><td>成功</td><td>Success</td><td>能量</td><td>Energy</td><td>力量</td><td>Power</td></tr><tr><td>感受</td><td>Feeling</td><td>努力</td><td>Effort</td><td>生活</td><td>Life</td><td>接受</td><td>Accept</td></tr><tr><td>支持</td><td>Support</td><td>勇敢</td><td>Brave</td><td>快乐</td><td>Happiness</td><td>现实</td><td>Reality</td></tr><tr><td>挑战</td><td>Challenge</td><td>负责</td><td>Responsible</td><td>特别</td><td>Special</td><td>追求</td><td>Pursuit</td></tr></table>

<table><tr><td colspan="6">Table E2. Important Features Identified by WFAL_GW in the DRP Case</td></tr><tr><td>Order</td><td>Feature</td><td>Weight</td><td>Order</td><td>Feature</td><td>Weight</td></tr><tr><td>1</td><td># of platforms contacted</td><td>0.0912</td><td>16</td><td># of calls_6</td><td>0.0012</td></tr><tr><td>2</td><td>Educational degree</td><td>0.0736</td><td>17</td><td>If_Name_match</td><td>0.0010</td></tr><tr><td>3</td><td>Age</td><td>0.0592</td><td>18</td><td># of messages</td><td>0.0010</td></tr><tr><td>4</td><td>Educational system</td><td>0.0543</td><td>19</td><td># of products</td><td>0.0010</td></tr><tr><td>5</td><td># of platforms registered</td><td>0.0463</td><td>20</td><td>Average consumption</td><td>0.0009</td></tr><tr><td>6</td><td>Ethnic group</td><td>0.0355</td><td>21</td><td># of calls_4</td><td>0.0009</td></tr><tr><td>7</td><td>Gender</td><td>0.0342</td><td>22</td><td>Max # of likes</td><td>0.0008</td></tr><tr><td>8</td><td>Is multi-loan</td><td>0.0293</td><td>23</td><td># of calls_2</td><td>0.0008</td></tr><tr><td>9</td><td>Zodiac sign</td><td>0.0239</td><td>24</td><td>Consumption</td><td>0.0007</td></tr><tr><td>10</td><td># of passive contacts</td><td>0.0092</td><td>25</td><td># of fans</td><td>0.0006</td></tr><tr><td>11</td><td># of contacts</td><td>0.0085</td><td>26</td><td>Expenditure</td><td>0.0005</td></tr><tr><td>12</td><td>District</td><td>0.0073</td><td>27</td><td>If_ID_match_1</td><td>0.0004</td></tr><tr><td>13</td><td># of orders</td><td>0.0061</td><td>28</td><td># of calls_5</td><td>0.0004</td></tr><tr><td>14</td><td># of active contacts</td><td>0.0055</td><td>29</td><td>Mean # of forwards</td><td>0.0004</td></tr><tr><td>15</td><td>Mean # of comments</td><td>0.0051</td><td>30</td><td># of negative words</td><td>0.0003</td></tr></table>

![](/api/attachments/8SEKVCDT/fulltext/images/821bef77f0d6cba1c8eca066120bea7838e677d7bae5576a795385355a2a694e.jpg)

Figure E1. Pareto Chart of Feature Weights in the DRP Case

## Appendix F

Exploratory Analysis on Features in the FDP (Listed Companies) Case

<table><tr><td colspan="6">Table F1. Top 20 Representative Annual Report-Specific Words</td></tr><tr><td colspan="2">T-3</td><td colspan="2">T-4</td><td colspan="2">T-5</td></tr><tr><td>Chinese</td><td>English</td><td>Chinese</td><td>English</td><td>Chinese</td><td>English</td></tr><tr><td>股票交易</td><td>Stock exchange</td><td>偿还</td><td>Repay</td><td>知情人</td><td>Insider</td></tr><tr><td>竞争力</td><td>Competitiveness</td><td>票据</td><td>Bill</td><td>贷方</td><td>Credit</td></tr><tr><td>公司债</td><td>Corporate bonds</td><td>知情人</td><td>Insider</td><td>使用权</td><td>Usage right</td></tr><tr><td>衍生品</td><td>Derivative</td><td>解除</td><td>Relieve</td><td>经理</td><td>Manager</td></tr><tr><td>道德规范</td><td>Ethics</td><td>事务所</td><td>Office</td><td>偿还</td><td>Repay</td></tr><tr><td>涉嫌</td><td>Suspected</td><td>管理层</td><td>Management layer</td><td>所有权</td><td>Ownership</td></tr><tr><td>交易日</td><td>Trading day</td><td>使用权</td><td>Usage right</td><td>管理层</td><td>Management layer</td></tr><tr><td>毛利率</td><td>Gross interest rate</td><td>等价物</td><td>Equivalents</td><td>票据</td><td>Bill</td></tr><tr><td>核心技术</td><td>Core technology</td><td>总经理</td><td>CEO</td><td>会计师</td><td>Accountant</td></tr><tr><td>保荐人</td><td>Sponsor</td><td>资本</td><td>Capital</td><td>固定资产</td><td>Fixed asset</td></tr><tr><td>知情人</td><td>Insider</td><td>固定资产</td><td>Fixed asset</td><td>董事会</td><td>Board of directors</td></tr><tr><td>非流通股</td><td>Non-tradable shares</td><td>会计师</td><td>Accountant</td><td>所得税</td><td>Income tax</td></tr><tr><td>合伙</td><td>Partnership</td><td>所得税</td><td>Income tax</td><td>交易所</td><td>Exchange</td></tr><tr><td>派发</td><td>Distribute</td><td>监事会</td><td>Supervisory board</td><td>事务所</td><td>Office</td></tr><tr><td>证券监管</td><td>Security supervision</td><td>董事会</td><td>Board of directors</td><td>房地产</td><td>Real estate</td></tr><tr><td>总体方案</td><td>Overall scheme</td><td>聘任</td><td>Appointment</td><td>有限公司</td><td>Limited company</td></tr><tr><td>回顾总结</td><td>Review</td><td>借款</td><td>Loan</td><td>监事会</td><td>Supervisory board</td></tr><tr><td>发展战略</td><td>Development strategy</td><td>交易所</td><td>Exchange</td><td>营业执照</td><td>Business license</td></tr><tr><td>管理方式</td><td>Management style</td><td>依法</td><td>According to the law</td><td>公益金</td><td>Public fund</td></tr><tr><td>财务制度</td><td>Financial system</td><td>房地产</td><td>Real estate</td><td>合同</td><td>Contract</td></tr></table>

<table><tr><td colspan="6">Table F2. Top 20 Representative Financial News-Specific Words</td></tr><tr><td colspan="2">T-3</td><td colspan="2">T-4</td><td colspan="2">T-5</td></tr><tr><td>Chinese</td><td>English</td><td>Chinese</td><td>English</td><td>Chinese</td><td>English</td></tr><tr><td>上市公司</td><td>Listed company</td><td>上市公司</td><td>Listed company</td><td>上半年</td><td>First half of the year</td></tr><tr><td>上涨</td><td>Rise</td><td>上涨</td><td>Rise</td><td>上市公司</td><td>Listed company</td></tr><tr><td>下跌</td><td>Fall</td><td>下降</td><td>Fall</td><td>上涨</td><td>Rise</td></tr><tr><td>净流入</td><td>Net inflow</td><td>业绩</td><td>Performance</td><td>下跌</td><td>Fall</td></tr><tr><td>投资</td><td>Invest</td><td>个股</td><td>Individual stock</td><td>业绩</td><td>Performance</td></tr><tr><td>业绩</td><td>Performance</td><td>涨幅</td><td>Increase range</td><td>个股</td><td>Individual stock</td></tr><tr><td>个股</td><td>Individual stock</td><td>买入</td><td>Buy in</td><td>交易</td><td>Transaction</td></tr><tr><td>政策</td><td>Policy</td><td>交易</td><td>Transaction</td><td>买入</td><td>Buy in</td></tr><tr><td>买入</td><td>Buy in</td><td>价格</td><td>Price</td><td>产品</td><td>Product</td></tr><tr><td>交易</td><td>Transaction</td><td>余量</td><td>Margin</td><td>估值</td><td>Valuation</td></tr><tr><td>产业</td><td>Industry</td><td>停牌</td><td>Suspend</td><td>偿还</td><td>Repay</td></tr><tr><td>增持</td><td>Increase holding</td><td>偿还</td><td>Repay</td><td>减持</td><td>Reduce holding</td></tr><tr><td>价格</td><td>Price</td><td>公告</td><td>Notice</td><td>净利润</td><td>Net profit</td></tr><tr><td>估值</td><td>Valuation</td><td>净利润</td><td>Net profit</td><td>净流入</td><td>Net inflow</td></tr><tr><td>跌幅</td><td>Drop range</td><td>减持</td><td>Reduce holding</td><td>创业板</td><td>GEM</td></tr><tr><td>融资</td><td>Financing</td><td>基金</td><td>Fund</td><td>基金</td><td>Fund</td></tr><tr><td>证券</td><td>Security</td><td>增持</td><td>Increase holding</td><td>增持</td><td>Increase holding</td></tr><tr><td>创业板</td><td>GEM</td><td>成交</td><td>Clinch a deal</td><td>市值</td><td>Market value</td></tr><tr><td>减持</td><td>Reduce holding</td><td>持股</td><td>Share holding</td><td>涨停</td><td>Limit up</td></tr><tr><td>控股</td><td>Hold controlling interest</td><td>收购</td><td>Acquire</td><td>重组</td><td>Reorganization</td></tr></table>

<table><tr><td colspan="8">Table F3. Important Features Identified by WFAL_GW in the FDP Case</td></tr><tr><td rowspan="2">Order</td><td colspan="2">T-3</td><td>T-4</td><td></td><td></td><td>T-5</td><td></td></tr><tr><td>Feature</td><td>Weight</td><td>Feature</td><td>Weight</td><td></td><td>Feature</td><td>Weight</td></tr><tr><td>1</td><td>N_*_S</td><td>0.0262</td><td>N_T</td><td>0.0506</td><td></td><td>N_T</td><td>0.0372</td></tr><tr><td>2</td><td>A12</td><td>0.0261</td><td>R_T</td><td>0.0453</td><td></td><td>N_T</td><td>0.0314</td></tr><tr><td>3</td><td>N_*_P</td><td>0.0259</td><td>A13</td><td>0.0426</td><td></td><td>R_T</td><td>0.0313</td></tr><tr><td>4</td><td>R_*_N</td><td>0.0258</td><td>A16</td><td>0.0390</td><td></td><td>R_T</td><td>0.0303</td></tr><tr><td>5</td><td>R_T</td><td>0.0243</td><td>R_*_P</td><td>0.0355</td><td></td><td>N_*_U</td><td>0.0255</td></tr><tr><td>6</td><td>A13</td><td>0.0230</td><td>A1</td><td>0.0315</td><td></td><td>N_*_S</td><td>0.0245</td></tr><tr><td>7</td><td>A16</td><td>0.0214</td><td>N_T</td><td>0.0314</td><td></td><td>A16</td><td>0.0235</td></tr><tr><td>8</td><td>N_*_N</td><td>0.0212</td><td>A5</td><td>0.0241</td><td></td><td>R_*_W</td><td>0.0233</td></tr><tr><td>9</td><td>N_T</td><td>0.0207</td><td>R_T</td><td>0.0229</td><td></td><td>A13</td><td>0.0194</td></tr><tr><td>10</td><td>R_T</td><td>0.0199</td><td>N_T</td><td>0.0223</td><td></td><td>R_T</td><td>0.0184</td></tr><tr><td>11</td><td>R_T</td><td>0.0195</td><td>A36</td><td>0.0221</td><td></td><td>A1</td><td>0.0180</td></tr><tr><td>12</td><td>A1</td><td>0.0194</td><td>A21</td><td>0.0219</td><td></td><td>R_*_P</td><td>0.0173</td></tr><tr><td>13</td><td>A11</td><td>0.0183</td><td>A22</td><td>0.0213</td><td></td><td>A8</td><td>0.0168</td></tr><tr><td>14</td><td>N_T</td><td>0.0178</td><td>A32</td><td>0.0200</td><td></td><td>R_T</td><td>0.0167</td></tr><tr><td>15</td><td>A14</td><td>0.0176</td><td>N #_W</td><td>0.0194</td><td></td><td>N_*_N</td><td>0.0162</td></tr><tr><td>16</td><td>N_*_U</td><td>0.0168</td><td>N_T</td><td>0.0193</td><td></td><td>R_*_S</td><td>0.0154</td></tr><tr><td>17</td><td>N_T</td><td>0.0167</td><td>R_T</td><td>0.0185</td><td></td><td>N_T</td><td>0.0153</td></tr><tr><td>18</td><td>R_T</td><td>0.0162</td><td>N_T</td><td>0.0175</td><td></td><td>R_T</td><td>0.0150</td></tr><tr><td>19</td><td>R_T</td><td>0.0161</td><td>A8</td><td>0.0169</td><td></td><td>N_*_W</td><td>0.0140</td></tr><tr><td>20</td><td>R_T</td><td>0.0159</td><td>R_T</td><td>0.0165</td><td></td><td>A31</td><td>0.0128</td></tr><tr><td>21</td><td>R_*_W</td><td>0.0150</td><td>R_T</td><td>0.0155</td><td></td><td>N_T</td><td>0.0128</td></tr><tr><td>22</td><td>N_T</td><td>0.0146</td><td>N_T</td><td>0.0150</td><td></td><td>N_T</td><td>0.0127</td></tr><tr><td>23</td><td>A29</td><td>0.0142</td><td>R #_W</td><td>0.0144</td><td></td><td>R_T</td><td>0.0125</td></tr><tr><td>24</td><td>A5</td><td>0.0125</td><td>R_T</td><td>0.0141</td><td></td><td>R_T</td><td>0.0124</td></tr><tr><td>25</td><td>N_T</td><td>0.0124</td><td>R #_P</td><td>0.0138</td><td></td><td>R_T</td><td>0.0124</td></tr><tr><td>26</td><td>R_*_P</td><td>0.0120</td><td>N_T</td><td>0.0132</td><td></td><td>N_*_P</td><td>0.0124</td></tr><tr><td>27</td><td>A21</td><td>0.0120</td><td>R_T</td><td>0.0128</td><td></td><td>R_*_L</td><td>0.0121</td></tr><tr><td>28</td><td>A10</td><td>0.0115</td><td>N_T</td><td>0.0127</td><td></td><td>R_T</td><td>0.0116</td></tr><tr><td>29</td><td>R_T</td><td>0.0113</td><td>R_T</td><td>0.0118</td><td></td><td>R #_S</td><td>0.0116</td></tr><tr><td>30</td><td>N_T</td><td>0.0110</td><td>A9</td><td>0.0117</td><td></td><td>A18</td><td>0.0115</td></tr><tr><td>31</td><td>R #_N</td><td>0.0105</td><td>N_T</td><td>0.0116</td><td></td><td>N_T</td><td>0.0111</td></tr><tr><td>32</td><td>R #_W</td><td>0.0105</td><td>R_T</td><td>0.0116</td><td></td><td>R_T</td><td>0.0110</td></tr><tr><td>33</td><td>A31</td><td>0.0099</td><td>R_T</td><td>0.0115</td><td></td><td>R #_N</td><td>0.0107</td></tr><tr><td>34</td><td>R_T</td><td>0.0091</td><td>N_T</td><td>0.0113</td><td></td><td>R_T</td><td>0.0097</td></tr><tr><td>35</td><td>R_*_S</td><td>0.0087</td><td>N_T</td><td>0.0111</td><td></td><td>R_T</td><td>0.0096</td></tr><tr><td>36</td><td>A27</td><td>0.0086</td><td>A24</td><td>0.0106</td><td></td><td>R_T</td><td>0.0093</td></tr><tr><td>37</td><td>N_T</td><td>0.0086</td><td>N_T</td><td>0.0106</td><td></td><td>N_T</td><td>0.0091</td></tr><tr><td>38</td><td>R_T</td><td>0.0083</td><td>R_T</td><td>0.0101</td><td></td><td>A29</td><td>0.0091</td></tr><tr><td>39</td><td>A32</td><td>0.0083</td><td>N_T</td><td>0.0099</td><td></td><td>R #_W</td><td>0.0089</td></tr><tr><td>40</td><td>R_T</td><td>0.0083</td><td>A38</td><td>0.0095</td><td></td><td>R *_N</td><td>0.0086</td></tr><tr><td>Sum</td><td></td><td>0.6261</td><td></td><td>0.7814</td><td></td><td></td><td>0.6414</td></tr></table>

Note: R\_T—lexical features extracted by LSTM from annual reports; N\_T—lexical features extracted by LSTM from financial news. The serial numbers of the lexical features are not informative and hence omitted. All of the three information sources appeared to be useful for FDP.

## Appendix G

## Parameter Setting in the Experiment

<table><tr><td colspan="3">Table G1. Parameter Setting of Model Construction</td></tr><tr><td>Parameter</td><td>Setting</td><td>Description</td></tr><tr><td>Kernel</td><td>Polynomial kernel</td><td>The kernel of SVM</td></tr><tr><td>N</td><td>10</td><td>The number of base classifiers</td></tr><tr><td>r</td><td>From 0.1 to 0.9 in increment of 0.1</td><td>Subspace rate of RS</td></tr><tr><td>λ</td><td> $\lambda_{\min} = 0.01\lambda_{\max}$ </td><td>Optimized through cross-validation</td></tr><tr><td> $\lambda_1$ </td><td> $\lambda_{1\min} = 0.01\lambda_{1\max}$ </td><td>Optimized through cross-validation</td></tr><tr><td> $\lambda_2$ </td><td>0.0001, 0.001, 0.01, 0.1, 1</td><td>Parameter of weighted fusion in WFAL_GW</td></tr><tr><td>α</td><td>0.1, 0.3, 0.5, 0.7, 0.9</td><td>Parameter of SGL</td></tr><tr><td>R</td><td>AUC</td><td>Reliability of AER</td></tr></table>

<table><tr><td colspan="4">Table G2. Parameter Setting of Lexical Feature Extraction</td></tr><tr><td>Module</td><td>Parameter</td><td>Setting</td><td>Description</td></tr><tr><td rowspan="14">LSTM</td><td>units</td><td>128</td><td>Dimensionality of the output space</td></tr><tr><td>activation</td><td>tanh</td><td>Activation function to use</td></tr><tr><td>dropout</td><td>0.1</td><td>Fraction of the units to drop for the linear transformation of the inputs</td></tr><tr><td>return_sequences</td><td>False</td><td>Whether to return the last output</td></tr><tr><td>return_state</td><td>False</td><td>Whether to return the last state in addition to the output</td></tr><tr><td>input_dim</td><td>100</td><td>Dimensionality of the input feature space</td></tr><tr><td>input_length</td><td>500</td><td>Size of the input sequence</td></tr><tr><td>batch_size</td><td>32</td><td>Number of samples per gradient update</td></tr><tr><td>epochs</td><td>100</td><td>Number of epochs to train the model</td></tr><tr><td>loss</td><td>binary_crossentropy</td><td>Loss function of the network</td></tr><tr><td>optimizer</td><td>adam</td><td>Optimization approach of the network</td></tr><tr><td>lr</td><td>0.01</td><td>Learning rate</td></tr><tr><td>momentum</td><td>0</td><td>Parameter updating momentum</td></tr><tr><td>Decay</td><td>0</td><td>Learning rate decay over each update</td></tr><tr><td rowspan="7">Word2Vec</td><td>size</td><td>100</td><td>Dimensionality of the word vectors</td></tr><tr><td>window</td><td>5</td><td>Maximum distance between the current word and the predicted word within a sentence</td></tr><tr><td>min_count</td><td>5</td><td>Ignores all words with total frequency lower than this</td></tr><tr><td>hs</td><td>0</td><td>Hierarchical softmax is used for model training</td></tr><tr><td>sg</td><td>1</td><td>Skip-gram as training algorithm</td></tr><tr><td>negative</td><td>5</td><td>Size of noise words for negative sampling</td></tr><tr><td>alpha</td><td>0.025</td><td>The initial learning rate</td></tr><tr><td colspan="4">Table G3. Parameter Setting of Baseline Methods</td></tr><tr><td>Baseline method</td><td>Parameter</td><td>Setting</td><td>Description</td></tr><tr><td rowspan="6">XGBoost</td><td>booster</td><td>gbtree</td><td>Use tree-based models or linear functions to boost</td></tr><tr><td>nthread</td><td>default</td><td>Number of parallel threads used to run XGBoost</td></tr><tr><td>eta</td><td>0.3</td><td>Learning rate</td></tr><tr><td>max_depth</td><td>6</td><td>Maximum depth of a tree</td></tr><tr><td>lambda</td><td>0.1</td><td>L2 regularization term on weights</td></tr><tr><td>alpha</td><td>0.01</td><td>L1 regularization term on weights</td></tr><tr><td>Multi-layer perceptron</td><td>loss_func_name</td><td>Binary_log_loss</td><td>Loss function used</td></tr><tr><td></td><td>alpha</td><td>0.0001</td><td>L2 penalty term</td></tr><tr><td></td><td>hidden_layer_sizes</td><td>5</td><td>Number of hidden layers</td></tr><tr><td></td><td>solver</td><td>adam</td><td>The method for weight optimization</td></tr><tr><td></td><td>activation</td><td>relu</td><td>Activation function for the hidden layer</td></tr><tr><td></td><td>batch_size</td><td>200</td><td>The size of one batch</td></tr><tr><td></td><td>learning rate</td><td>constant</td><td>Learning rate schedule for weight updating</td></tr><tr><td></td><td>Learning_rate_init</td><td>0.001</td><td>The initial learning rate used</td></tr><tr><td></td><td>max_iter</td><td>200</td><td>Maximum number of iterations</td></tr></table>

![](/api/attachments/8SEKVCDT/fulltext/images/bc382086b4cf22af0eacd8047093676443b3ecf97a49c7d4395334da0c7c31c9.jpg)  
(1) RS

![](/api/attachments/8SEKVCDT/fulltext/images/d9473b2b3491fbf535222ff97ab978f46e334272d4a342c3f74e2920134caeb9.jpg)  
(2) HSB\_RS

As shown in Figure H1, in the DRP case, the AUC of RS increased gradually as increased, and reached the highest values of 0.9305 (T-r 0) and 0.9313 (T-1), respectively, at $r = 0 . 7$ . For HSB\_RS, the highest AUCs were about 0.9521 and 0.9522 for T-0 and T-1 respectively, and the optimal was 0.3 for both T-0 and T-1. As shown in Figure H2, in the FDP case, the highest AUC values attained by RS arer 0.9206 with T-3 and , 0.9247 with T-4 and , and 0.9316 with T-5 and . The highest AUC values obtained byr = 0.5 r = 0.3 r = 0.7 HSB\_RS are 0.9536 with T-3 and $r = 0 . 3 , 0 . 9 4 4 7$ with T-4 and , and 0.9528 with T-5 andr = 0.3 $r = 0 . 7$

Figure H3 and Figure H4 show the results of sensitivity analysis regarding the $\alpha$ and $\lambda _ { 2 }$ of HSB\_RS with the complete multisource heterogeneous feature set.

![](/api/attachments/8SEKVCDT/fulltext/images/a0d5c8d401dadf091107d5caeb31efeb38f40af8d44877d03bb2951b7cb4fc46.jpg)  
(a) r=0.3

![](/api/attachments/8SEKVCDT/fulltext/images/8d350e9a2f94ca5ce0009eb7685a0ec609f974528c4248f9e62c928a7b9e75ba.jpg)  
(b) r=0.5

![](/api/attachments/8SEKVCDT/fulltext/images/8b2137f1d4fe6f88a1313b5aa1054c98aa5c1385bdd3eba0037155bf1df0ebfd.jpg)  
(c) r=0.7

(1) T-0  
![](/api/attachments/8SEKVCDT/fulltext/images/2616e56a9d2ff8523c13fc885ea4edc7f4c42f624ad612c86ab7553f70df0f94.jpg)

![](/api/attachments/8SEKVCDT/fulltext/images/6339a230542071955bda649e4b5b68ec2bca02a70c8c9181c723f4dda9605649.jpg)  
(b) r=0.5

![](/api/attachments/8SEKVCDT/fulltext/images/e8c1c6f843a407f5554cd8db633b03ee8ed9a9eedc58cf69ffb3a5bdb29035bc.jpg)  
(2) T-1

(b) r=0.5

![](/api/attachments/8SEKVCDT/fulltext/images/aaae9e5b9516b6a76414f14bd6843943540b16087468ca4bf307efbad64c3732.jpg)  
(1)T-3

![](/api/attachments/8SEKVCDT/fulltext/images/24745b377262d08f6a2824e0d1d494ab4a59ff71d8b6caa551102b887d8c9108.jpg)

![](/api/attachments/8SEKVCDT/fulltext/images/607b87790713232eedb904bd59958095873e5e85eb507b370f5d533eff3bce25.jpg)

![](/api/attachments/8SEKVCDT/fulltext/images/6967638317951d6e2e261917110f8d67d12a633706113b487d73e71ead79e5e1.jpg)  
(2) T-4

![](/api/attachments/8SEKVCDT/fulltext/images/e71b23ac6550722e22be7fee785916d4e9250f32733f5c48ec52aafd9d75ce12.jpg)

![](/api/attachments/8SEKVCDT/fulltext/images/ddbd2136cf5363b01831ef8d3b006346104e2845a184911a291b6e3de78e08af.jpg)

![](/api/attachments/8SEKVCDT/fulltext/images/1a1b80bcf235e8e127435cd8cdc43de4fc91cc7fa621e33f70f7df9d7278124d.jpg)  
(3) T-5

![](/api/attachments/8SEKVCDT/fulltext/images/a8c14c8fc18dda1b5364d2a49efe3ee7077137b846c55bc665f79f16e08e9ca7.jpg)  
(b) r=0.5

![](/api/attachments/8SEKVCDT/fulltext/images/47d3ddc6ab813f31e2e02ff32ac7b32444fc56efac9c524f373923a193b24a9c.jpg)

## Appendix I

## Statistical Analysis

We used ANOVA with Tukey-Kramer post hoc pairwise comparison to compare the proposed method with the nine baselines in terms of prediction performance (AUC). Tables I1 and I2 present the Tukey-Kramer test results for the DRP and FDP cases with all features under T-1 and T-3, respectively. Figures I1 and I2 present the corresponding box-whisker charts (the names of Bagging, Boosting, Random Subspace, XGBoost, Multi-layer Preceptron, ER\_RS, Lasso\_RS, PBM\_RS, and HSB\_RS are respectively abbreviated as shown).

Table I1. Tukey-Kramer Test Result (t and p) in the DRP Case

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>2</td><td>20.917***</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>8.813***</td><td>12.103***</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>28.313***</td><td>7.397***</td><td>19.500***</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>28.576***</td><td>7.660***</td><td>19.763***</td><td>0.263</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>8.288***</td><td>12.629***</td><td>0.525</td><td>20.025***</td><td>20.288***</td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>32.962***</td><td>12.045***</td><td>24.149***</td><td>4.649*</td><td>4.386</td><td>24.674***</td><td></td><td></td><td></td></tr><tr><td>8</td><td>40.176***</td><td>19.259***</td><td>31.363***</td><td>11.863***</td><td>11.600***</td><td>31.888***</td><td>7.214***</td><td></td><td></td></tr><tr><td>9</td><td>38.620***</td><td>17.703***</td><td>29.806***</td><td>10.306***</td><td>10.043***</td><td>30.332***</td><td>5.658**</td><td>1.556</td><td></td></tr><tr><td>10</td><td>54.839***</td><td>33.923***</td><td>46.026***</td><td>26.526***</td><td>26.263***</td><td>46.551***</td><td>21.877***</td><td>14.664***</td><td>16.220***</td></tr></table>

Note: 1-SVM, 2-Bagging, 3-Boosting, 4-Random Subspace, 5-XGBoost, 6-Multi-layer Perceptron, 7-ER\_RS, 8-Lasso\_RS, 9-PBM\_RS, 10- HSB\_RS.  
\*\*\* Significant at the 0.001 level.  
\*\* Significant at the 0.01 level.  
\* Significant at the 0.05 level.

<table><tr><td colspan="10">Table I2. Tukey-Kramer Test Result (t and p) in the FDP Case</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>2</td><td>15.131***</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>15.855***</td><td>0.724</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>20.562***</td><td>5.431**</td><td>4.708*</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>20.527***</td><td>5.395**</td><td>4.672*</td><td>0.036</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>17.326***</td><td>2.195</td><td>1.471</td><td>3.236</td><td>3.201</td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>20.703***</td><td>5.572**</td><td>4.848*</td><td>0.141</td><td>0.177</td><td>3.377</td><td></td><td></td><td></td></tr><tr><td>8</td><td>23.164***</td><td>8.033***</td><td>7.310***</td><td>2.602</td><td>2.638</td><td>5.838**</td><td>2.461</td><td></td><td></td></tr><tr><td>9</td><td>21.476***</td><td>6.344***</td><td>5.621**</td><td>0.913</td><td>0.949</td><td>4.150</td><td>0.773</td><td>1.689</td><td></td></tr><tr><td>10</td><td>28.650***</td><td>13.519***</td><td>12.795***</td><td>8.088***</td><td>8.123***</td><td>11.324***</td><td>7.947***</td><td>5.486**</td><td>7.174***</td></tr></table>

Note: 1-SVM, 2-Bagging, 3-Boosting, 4-Random Subspace, 5-XGBoost, 6-Multi-layer Perceptron, 7-ER\_RS, 8-Lasso\_RS, 9-PBM\_RS, 10- HSB\_RS.  
\*\*\* Significant at the 0.001 level.  
\*\* Significant at the 0.01 level.  
\* Significant at the 0.05 level.

![](/api/attachments/8SEKVCDT/fulltext/images/568d17d73b445e1f5f5c51e02e99c291d92398695deb5bf6c44aae33fadeb15e.jpg)  
Figure I1. Box-Whisker Chart for the DRP Case

![](/api/attachments/8SEKVCDT/fulltext/images/17f4a8e9c52a438eee2510cbdb7b8a6727755800764a1d7fc5ec5edf37c0d560.jpg)

## Appendix J

## Evaluation Results in Terms of Other Metrics

In addition to AUC, we also evaluated our proposed method (HSB\_RS) and the baselines with Kolmogorov–Smirnov (KS) statistic, Gini, and F1-score. Tables J1 and J2, J3 and J4, and J5 and J6 summarize the KS, Gini, and F1-score results based on integrated features in the two cases, respectively. Note that unlike AUC, KS, and Gini, which are aggregate performance metrics, F1-score needs to be measured under a chosen decision threshold on the predicted conditional probability of the class. The F1-score results reported here are based on the default threshold of 0.5.

<table><tr><td colspan="3">Table J1. Mean (Standard Deviation) of KS (%) in the DRP Case</td></tr><tr><td>Method</td><td>T-1</td><td>T-0</td></tr><tr><td>SVM</td><td>59.15 (3.48)</td><td>56.30 (4.09)</td></tr><tr><td>Bagging</td><td>63.16 (2.81)</td><td>62.03 (3.45)</td></tr><tr><td>Boosting</td><td>61.65 (2.95)</td><td>58.50 (3.06)</td></tr><tr><td>RS</td><td>63.91 (2.94)</td><td>63.58 (2.96)</td></tr><tr><td>XGBoost</td><td>64.87 (2.86)</td><td>64.75 (2.31)</td></tr><tr><td>MLP</td><td>60.69 (3.41)</td><td>59.95 (3.38)</td></tr><tr><td>ER_RS</td><td>65.17 (1.35)</td><td>65.05 (1.42)</td></tr><tr><td>Lasso_RS</td><td>65.97 (0.94)</td><td>65.82 (1.01)</td></tr><tr><td>PBM_RS</td><td>65.69 (0.95)</td><td>65.66 (0.99)</td></tr><tr><td>HSB_RS</td><td>69.13 (0.77)</td><td>68.63 (0.61)</td></tr></table>

<table><tr><td colspan="4">Table J2. Mean (Standard Deviation) of KS (%) in the FDP Case</td></tr><tr><td>Method</td><td>T-3</td><td>T-4</td><td>T-5</td></tr><tr><td>SVM</td><td>57.27 (8.12)</td><td>41.15 (8.05)</td><td>45.01 (7.98)</td></tr><tr><td>Bagging</td><td>59.82 (6.48)</td><td>56.73 (8.44)</td><td>56.74 (7.65)</td></tr><tr><td>Boosting</td><td>62.94 (6.81)</td><td>61.13 (6.92)</td><td>64.89 (5.09)</td></tr><tr><td>RS</td><td>65.68 (3.84)</td><td>67.87 (4.98)</td><td>66.87 (4.59)</td></tr><tr><td>XGBoost</td><td>64.75 (4.78)</td><td>67.02 (4.13)</td><td>66.76 (3.63)</td></tr><tr><td>MLP</td><td>64.34 (6.54)</td><td>62.81 (5.91)</td><td>64.91 (5.62)</td></tr><tr><td>ER_RS</td><td>67.11 (3.75)</td><td>68.13 (4.68)</td><td>68.93 (3.99)</td></tr><tr><td>Lasso_RS</td><td>69.22 (3.25)</td><td>70.87 (4.04)</td><td>72.33 (3.89)</td></tr><tr><td>PBM_RS</td><td>67.13 (5.66)</td><td>68.36 (5.94)</td><td>69.21 (4.08)</td></tr><tr><td>HSB_RS</td><td>73.33 (3.18)</td><td>72.02 (4.05)</td><td>73.38 (3.64)</td></tr></table>

<table><tr><td colspan="3">Table J3. Mean (Standard Deviation) of Gini (%) in the DRP Case</td></tr><tr><td>Method</td><td>T-1</td><td>T-0</td></tr><tr><td>SVM</td><td>81.80 (3.06)</td><td>79.92 (3.70)</td></tr><tr><td>Bagging</td><td>85.10 (1.30)</td><td>84.80 (1.82)</td></tr><tr><td>Boosting</td><td>83.18 (1.38)</td><td>81.96 (1.94)</td></tr><tr><td>RS</td><td>86.26 (1.02)</td><td>86.10 (1.12)</td></tr><tr><td>XGBoost</td><td>86.30 (1.56)</td><td>86.26 (1.52)</td></tr><tr><td>MLP</td><td>83.10 (1.90)</td><td>82.82 (1.86)</td></tr><tr><td>ER_RS</td><td>86.98 (0.70)</td><td>86.76 (0.82)</td></tr><tr><td>Lasso_RS</td><td>88.12 (0.28)</td><td>88.14 (0.42)</td></tr><tr><td>PBM_RS</td><td>87.88 (0.34)</td><td>87.94 (0.38)</td></tr><tr><td>HSB_RS</td><td>90.44 (0.28)</td><td>90.42 (0.22)</td></tr></table>

<table><tr><td colspan="4">Table J4. Mean (Standard Deviation) of Gini (%) in the FDP Case</td></tr><tr><td>Method</td><td>T-3</td><td>T-4</td><td>T-5</td></tr><tr><td>SVM</td><td>67.30 (14.60)</td><td>50.10 (14.46)</td><td>55.52 (12.86)</td></tr><tr><td>Bagging</td><td>79.68 (10.54)</td><td>72.96 (14.88)</td><td>66.70 (12.56)</td></tr><tr><td>Boosting</td><td>80.26 (9.46)</td><td>78.42 (9.58)</td><td>84.50 (8.74)</td></tr><tr><td>RS</td><td>84.12 (4.50)</td><td>84.94 (6.48)</td><td>86.32 (5.98)</td></tr><tr><td>XGBoost</td><td>84.08 (3.92)</td><td>84.50 (5.88)</td><td>85.90 (5.20)</td></tr><tr><td>MLP</td><td>81.46 (9.10)</td><td>80.44 (8.74)</td><td>83.82 (8.16)</td></tr><tr><td>ER_RS</td><td>84.22 (4.48)</td><td>85.20 (6.48)</td><td>86.42 (5.82)</td></tr><tr><td>Lasso_RS</td><td>86.24 (5.92)</td><td>87.94 (7.54)</td><td>90.16 (6.22)</td></tr><tr><td>PBM_RS</td><td>84.86 (7.52)</td><td>85.86 (8.70)</td><td>86.64 (6.26)</td></tr><tr><td>HSB_RS</td><td>90.72 (4.82)</td><td>88.94 (6.86)</td><td>90.56 (5.70)</td></tr></table>

<table><tr><td colspan="5">Table J5. Mean (Standard Deviation) of Class-Wise F1-Score (%) in the DRP Case</td></tr><tr><td rowspan="2">Method</td><td colspan="2">T-1</td><td colspan="2">T-0</td></tr><tr><td>Risk</td><td>Non-risk</td><td>Risk</td><td>Non-risk</td></tr><tr><td>SVM</td><td>66.51 (2.80)</td><td>87.32 (1.05)</td><td>65.59 (2.97)</td><td>87.28 (1.06)</td></tr><tr><td>Bagging</td><td>67.98 (2.01)</td><td>88.76 (0.97)</td><td>66.55 (2.45)</td><td>88.64 (1.02)</td></tr><tr><td>Boosting</td><td>70.60 (2.30)</td><td>88.66 (1.02)</td><td>70.21 (2.60)</td><td>88.22 (1.45)</td></tr><tr><td>RS</td><td>73.00 (2.11)</td><td>89.95 (0.96)</td><td>73.45 (2.34)</td><td>89.57 (0.89)</td></tr><tr><td>XGBoost</td><td>73.52 (2.75)</td><td>90.36 (0.99)</td><td>74.08 (2.16)</td><td>90.12 (0.94)</td></tr><tr><td>MLP</td><td>70.43 (3.01)</td><td>88.61 (1.06)</td><td>71.02 (2.99)</td><td>88.43 (1.21)</td></tr><tr><td>ER_RS</td><td>74.10 (2.08)</td><td>90.51 (0.71)</td><td>74.17 (2.36)</td><td>90.49 (0.87)</td></tr><tr><td>Lasso_RS</td><td>77.81 (1.63)</td><td>91.42 (0.51)</td><td>77.66 (1.89)</td><td>91.67 (0.51)</td></tr><tr><td>PBM_RS</td><td>77.45 (2.25)</td><td>91.07 (0.69)</td><td>77.64 (2.89)</td><td>91.11 (0.58)</td></tr><tr><td>HSB_RS</td><td>79.09 (1.56)</td><td>93.82 (0.45)</td><td>78.94 (1.23)</td><td>93.60 (0.35)</td></tr></table>

<table><tr><td colspan="7">Table J6. Mean (Standard Deviation) of Class-Wise F1-Score (%) in the FDP Case</td></tr><tr><td rowspan="2">Method</td><td colspan="2">T-3</td><td colspan="2">T-4</td><td colspan="2">T-5</td></tr><tr><td>Risk</td><td>Non-risk</td><td>Risk</td><td>Non-risk</td><td>Risk</td><td>Non-risk</td></tr><tr><td>SVM</td><td>63.13 (9.09)</td><td>93.28(0.83)</td><td>62.65(12.47)</td><td>92.95(0.68)</td><td>67.00(9.22)</td><td>93.71(0.64)</td></tr><tr><td>Bagging</td><td>66.05(8.56)</td><td>94.63(0.85)</td><td>66.50(11.89)</td><td>94.43(0.69)</td><td>70.41(8.79)</td><td>94.02(0.64)</td></tr><tr><td>Boosting</td><td>66.69(7.18)</td><td>94.87(0.93)</td><td>67.28(9.59)</td><td>94.49(0.73)</td><td>71.80(9.10)</td><td>94.73(0.83)</td></tr><tr><td>RS</td><td>66.93(7.32)</td><td>95.03(0.83)</td><td>69.72(7.36)</td><td>95.29(0.84)</td><td>73.91(7.35)</td><td>95.33(0.83)</td></tr><tr><td>XGBoost</td><td>66.91(7.24)</td><td>95.07(0.70)</td><td>69.71(7.31)</td><td>95.26(0.71)</td><td>73.43(6.97)</td><td>95.29(0.67)</td></tr><tr><td>MLP</td><td>66.74(7.91)</td><td>94.82(0.89)</td><td>68.34(7.83)</td><td>94.91(0.88)</td><td>71.72(7.71)</td><td>94.72(0.86)</td></tr><tr><td>ER_RS</td><td>68.20(5.93)</td><td>96.06(0.80)</td><td>69.83(6.69)</td><td>95.78(0.83)</td><td>74.29(5.94)</td><td>95.44(0.81)</td></tr><tr><td>Lasso_RS</td><td>68.55(6.01)</td><td>96.24(0.77)</td><td>70.87(6.74)</td><td>95.68(0.82)</td><td>74.91(6.32)</td><td>96.38(0.76)</td></tr><tr><td>PBM_RS</td><td>68.15(7.72)</td><td>96.03(0.84)</td><td>70.01(7.96)</td><td>95.04(0.85)</td><td>73.59(7.69)</td><td>95.81(0.80)</td></tr><tr><td>HSB_RS</td><td>72.04(5.48)</td><td>97.70(0.69)</td><td>73.66(6.11)</td><td>97.32(0.73)</td><td>77.66(5.90)</td><td>98.05(0.71)</td></tr></table>

## Appendix K

## Roadmap for Deployment

Figure K1 outlines a roadmap for deploying our method in practice, which is in line with the DSR roadmap established in prior research (Alturki, et al., 2011). Below, we further elucidate the four main interrelated components: requirement definition, multisource data collection, model deployment, and coordination.

![](/api/attachments/8SEKVCDT/fulltext/images/71be1b549a3c9bc13909d32a5eef527dbaf20f95bd2860ae4b40447fd5088263.jpg)  
Figure K1. Roadmap for Deploying HSB\_RS in Practice

## 1. Requirement definition

A variety of stakeholders potentially affected by financial risks are in need of effective FRP tools like our proposed method. At the individual level, P2P lenders and lending platforms need to accurately assess borrowers’ default risks. At the company level, both internal executives and external investors (e.g., banks and stockholders) of a company need to keep a close eye on early signs of potential financial distress. Besides, regulators from the government are deeply concerned with the dire (both tangible and intangible) consequences of severe financial risks at both individual and company levels. Given the FRP requirements of these stakeholders, HSB\_RS can be deployed to support their related decisionmaking.

## 2. Multisource data collection

As inputs to HSB\_RS, multisource heterogeneous data can be collected from various data providers, such as social media platforms, e-commerce platforms, mobile communication operators, and the government’s open data platforms. Although data collaboration may give rise to serious concerns regarding data privacy, data security, and data value, multisource data can still be acquired with the help of secure multi-party computation mechanisms, including homomorphic encryption (Gentry, 2009), differential privacy (Dwork and Roth, 2014), and federated learning (Yang et al., 2019). Such mechanisms ensure multisource data to be fully leveraged without jeopardizing security and privacy.

## 3. Model Deployment

Once the inputs are ready, the deployment of HSB\_RS is relatively straightforward. As computing resources are becoming commodities nowadays, the running environment of HSB\_RS can be easily configured. Once deployed, HSB\_RS can be reused with limited extra cost.

## 4. Coordination

The functioning of an HSB\_RS based FRP system and the reconcilement among its components can be maintained by a coordinator. Any party (government regulators, financial institutions, companies, and third parties) with sufficient credibility and competency can fill in the coordinator role.

Below, we further discuss whether, by whom, and how our method could be deployed effectively in practice. Along the way, we use the two cases in our evaluation as illustrative examples.

## Whether:

With respect to “whether” HSB\_RS would be practically feasible and helpful, our two cases demonstrate that it is indeed feasible for most stakeholders to obtain data from multiple heterogeneous sources and thereby benefit from the performance improvement. In our FRP case, the financial ratios (from CSMAR), annual reports (from two stock exchanges), and financial news (from Eastmoney) are all publicly accessible. In our DRP case, we acquired some of the data in collaboration with the P2P lending platform and crawled publicly disclosed social media data from Weibo.com by ourselves. The loan application-related information borrowers submit to the platform is publicly accessible. The data regarding mobile communication, online consumption, and online shopping are collected by the platform through its proprietary channels. The platform is able to obtain all the data we used.

## By Whom:

With respect to “by whom” HSB\_RS would be helpful, a variety of stakeholders (e.g., P2P lending platforms and lenders in DRP, and stockholders, executives, and regulators in FDP) would be interested in it to better predict default risk or financial distress. For some technically less competent stakeholders (e.g., individual investors on the P2P lending platform), other more competent parties (e.g., the P2P lending platform) can deploy our method and provide its prediction results as a kind of recommendation service (e.g., like a credit scoring service).

## How:

With respect to “how” HSB\_RS or one like it could be deployed, we believe that the expected benefits would well exceed the costs of data acquisition and model building. Financial risks often incur dire, both tangible and intangible, consequences to a variety of stakeholders. The variety of data sources emerging in recent years are providing promising avenues for making breakthroughs in FRP. The incremental improvement of our method over the state of the art (represented by some of the baselines in our evaluation) has real value to stakeholders. While we used just a few data sources in our evaluation, much more can be added in practice, and the advantage of our method over existing simpler alternatives will be further pronounced.

The improvement of our more complex method does come with a cost of extra computing works. However, as computing resources are nowadays becoming commodities with continuously increased computing power and lowered cost, the cost for the extra computing works will become negligible compared to the gain in performance improvement. In the long run, the benefit (tangible and intangible losses saved by improved performance in repeated predictions) would be well worth the cost (extra computing resources consumed in periodic model refreshing).

## Appendix L

Pipeline of Data Extraction, Preparation, and Processing

![](/api/attachments/8SEKVCDT/fulltext/images/342303d8977d2ed37a980e7cda25ecc4e378868d9c9f329de051ae16a899c6a6.jpg)

Figure L1. Pipeline of Data Extraction, Preparation, and Processing

Figure L1 outlines a pipeline of data extraction, preparation, and processing for using our method. Below, we use the two cases in our evaluation to illustrate the steps in this pipeline.

1. Data Acquisition: Acquire data from multiple heterogeneous sources.

DRP:

P2P lending, mobile communication, online consumption, and online payment data were acquired through collaboration with the P2P lending platform.

• Social media data were crawled from Weibo.com.

## FDP:

Financial data were obtained from CSMAR.

• Annual reports were downloaded from the official websites of the Shenzhen Stock Exchange and Shanghai Stock Exchange of China.

• Financial news data were crawled from Eastmoney.

## 2. Feature Extraction: Extract hard and soft features from the acquired data.

## DRP:

Conventional hard features were taken from the basic data from the platform.

• Call statistics, online consumption statistics, and online shopping statistics were derived.

Social media statistics were extracted from the Weibo data.

• Social interaction features were derived based on the numbers of likes, forwards, and comments each Weibo message had received.

• Sentiment features were derived from merged Weibo messages based on the Chinese HowNet sentiment lexicons.

• Lexical features were derived from merged Weibo messages using word2vec and LSTM.

## FDP:

• Conventional financial ratios were derived from the CSMAR data.

• Sentiment features and lexical features were derived from annual reports and financial news similarly as in the DRP case.

• Additional sentiment features were derived based on the litigious lexicon from Sougou.

3. Feature Grouping: Group the features according to their heterogeneous data sources, structures, and implications based on domain knowledge.

## DRP:

• Features from different sources were placed in different groups.

• The hard features were placed in one group.

• The quantitative social media features were placed in one group.

• The lexical features were placed in one group.

• The sentiment features were placed in three groups: positive, neutral, and negative.

## FDP:

• Features from different sources were placed in different groups.

• The financial ratios were placed in six groups: profitability, development capacity, solvency, operational capabilities, capital expansion capacity, and finance structure.

• The lexical features from each source were placed in one group.

• The sentiment features from each source were placed in three groups: positive, neutral, and negative.

4. Model Training: Train prediction models using HSB\_RS based on the grouped features.

## Appendix References

Alturki, A., Gable, G. G., and Bandara, W. 2011. “A Design Science Research Roadmap,” in Proceedings of the International Conference on Design Science Research in Information Systems, pp. 107-123.

Dwork, C. and Roth, A. 2014. “The Algorithmic Foundations of Differential Privacy,” Foundations and Trends in Theoretical Computer Science, (9:3), pp. 211-407.

Emekter, R., Tu, Y., Jirasakuldech, B., and Lu, M. 2015. “Evaluating Credit Risk and Loan Performance in Online Peer-to-Peer (P2P) Lending,” Applied Economics (47:1), pp. 54-70.

Gentry, C. 2009. “Fully Homomorphic Encryption Using Ideal Lattices,” in Proceedings of the 41st Annual ACM Symposium on Theory of Computing, pp. 169-178.

Hájek, P. and Olej, V. 2015. “Word Categorization of Corporate Annual Reports for Bankruptcy Prediction by Machine Learning Methods,” in Proceedings of the International Conference on Text, Speech, and Dialogue, pp. 122-130.

Malekipirbazari, M. and Aksakalli, V. 2015. “Risk Assessment in Social Lending Via Random Forests,” Expert Systems with Applications, (42:10), pp. 4621-4631.

Peng, Y., Wang, G., Kou, G., and Shi, Y. 2011. “An Empirical Study of Classification Algorithm Evaluation for Financial Risk Prediction,” Applied Soft Computing (11:2), pp. 2906-2915.

Sun, J. and Li, H. 2012. “Financial Distress Prediction Using Support Vector Machines: Ensemble Vs. Individual,” Applied Soft Computing, (12:8), pp. 2254-2265.

Xia, Y., Liu, C., Da, B., and Xie, F. 2018. “A Novel Heterogeneous Ensemble Credit Scoring Model Based on Bstacking Approach,” Expert Systems with Applications (93) pp. 182-199.

Yang, Q., Liu, Y., Chen, T., and Tong, Y. 2019. “Federated Machine Learning: Concept and Applications,” ACM Transactions on Intelligent Systems and Technology (10:2), pp. 1-19.

Yum, H., Lee, B., and Chae, M. 2012. “From the Wisdom of Crowds to My Own Judgment in Microfinance through Online Peer-to-Peer Lending Platforms,” Electronic Commerce Research and Applications, (11:5), pp. 469-483.

Zhou, L., Lai, K. K., and Yen, J. 2012. “Empirical Models Based on Features Ranking Techniques for Corporate Financial Distress Prediction,” Computers & Mathematics with Applications, (64:8), pp. 2484-2496.
