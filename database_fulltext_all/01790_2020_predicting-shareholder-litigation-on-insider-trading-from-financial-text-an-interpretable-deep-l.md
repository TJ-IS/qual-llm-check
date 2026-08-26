---
otero_id: 1790
otero_key: "TJYGNSJB"
title: "Predicting shareholder litigation on insider trading from financial text: An interpretable deep learning approach"
authors: "Rong Liu; Feng Mai; Zhe Shan; Ying Wu"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103387"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Journal Pre-proof

Predicting shareholder litigation on insider trading from financial text: An interpretable deep learning approach

Rong Liu, Feng Mai, Zhe Shan, Ying Wu

![](/api/attachments/TJYGNSJB/fulltext/images/1985e536e6fc449e7b46c88b33726b841c7b849eb7a889dd5f46bd24dc4809bd.jpg)

PII: S0378-7206(20)30325-6

DOI: https://doi.org/10.1016/j.im.2020.103387

Reference: INFMAN 103387

To appear in: Information & Management

Received Date: 9 March 2020

Revised Date: 5 October 2020

Accepted Date: 7 October 2020

Please cite this article as: doi: https://doi.org/

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# Predicting Shareholder Litigation on Insider Trading from Financial Text: An Interpretable Deep Learning Approach

Rong Liu School of Business Stevens Institute of Technology 1 Castle Point Terrace, Hoboken, NJ 07030, USA Email: rong.liu@stevens.edu Phone: +1 (201)-216-5028

Feng Mai School of Business Stevens Institute of Technology 1 Castle Point Terrace, Hoboken, NJ 07030, USA Email: feng.mai@stevens.edu Phone: +1 (201)-216-3815

Zhe Shan\* Department of Information Systems and Analytics Farmer School of Business Miami University Oxford, OH 45056, USA Email: jayshan@miamioh.edu Phone: +1 (513)-529-4940

Ying Wu School of Business Stevens Institute of Technology 1 Castle Point Terrace, Hoboken, NJ 07030, USA Email: ying.wu@stevens.edu Phone: +1 (201)-216-3510

\* Corresponding author. Declarations of interest: none.

## Abstract

The detrimental effects of insider trading on the financial markets and the economy are well documented. However, resource-constrained regulators face a great challenge in detecting insider trading and enforcing insider trading laws. We develop a text analytics framework that uses machine learning to predict ex-ante potentially opportunistic insider trading, using actual insider trading allegation by shareholders as the proxy,

from corporate textual disclosures. Distinct from typical black-box neural network models, which have difficulty tracing a prediction back to key features, our approach combines the predictive power of deep learning with attention mechanisms to provide interpretability to the model. Further, our model utilizes representations from a business proximity network and incorporates the temporal variations of a firm’s financial disclosures. The empirical results offer new insights into insider trading and provide practical implications. Overall, we contribute to the literature by reconciling performance and interpretability in predictive analytics. Our study also informs the practice by proposing a new method for regulators to examine a large amount of text in order to monitor and predict financial misconduct.

Keywords: Insider Trading, Predictive Analytics, Deep Learning, Attention Models, Text Mining

## 1 INTRODUCTION

Insider trading refers to the buying or selling of a public company’s securities based on material, nonpublic information. Corporate executives have access to private information about public companies and thus possess a significant advantage over the majority of investors. By making perfectly timed trades based on nonpublic information, insiders can yield millions in profit. Insider trading based on private information clearly compromises the fairness and integrity of the capital markets. If left unchecked, it has dire and long-term consequences such as damaging investor confidence, raising the cost of capital [1], impeding innovation [2], and hurting financial market stability [3]. Because of the high economic and social costs, in the U.S. and many other countries, it is illegal to trade while in possession of material nonpublic information about a security.

Yet, despite the laws and regulations in place, their efficacy in restraining insider trading is limited. Prosecution and conviction of insider trading cases are difficult. According to the study by [4], insider trading laws exist in more than 80% of countries that have the stock market, but prosecutions have taken place in only about 40% of them. Making things worse, the duty of policing insider trading violations largely falls on the shoulders of market regulators such as the Securities and Exchange Commission (SEC) in the U.S. These agencies are severely resource-constrained and must rely on staff discretion to select cases to pursue [5].

Given the challenges faced by regulators and policymakers, we propose a novel analytics framework that uses machine learning models to learn from historical data and to predict the likelihood of future insider trading violations. Predictive analytics can hold great practical value while also generating new theoretical insights [6,7]. Analytical technology for regulatory considerations (a.k.a. regtech) is especially relevant for information systems (IS) research in the age of fintech, as policymakers and regulators are in need of modern tools and frameworks to keep up with technology-driven changes in the field [8]. Currently, regulators must wait passively for a whistleblower or a large suspicious trade to make a case [9]. With a prediction model, regulators could actively target future investigation and enforcement efforts. In addition, the ability to detect potential illegal insider trading could provide beneficial deterrent effects.

##

However, building a prediction model for potentially illegal insider trading is a challenging task for several reasons. First, there are many economic, behavioral, and contextual factors that influence the probability of financial misconduct [10,11]. It is difficult to capture these factors by numeric information alone from the company’s financial statement. As such, it is an open question whether informative and opportunistic insider trades that violate regulations can be predicted. Second, the antecedents of corporate financial misconducts include not only a firm’s own current conditions, but also its competitive environment [12] and changes in historical financial reports [13]. Incorporating these elements in a prediction model is difficult as they entail high dimensional features. In addition, because the environment is “in a state of constant change” [14], we need to capture the dynamic competitive relationship between firms. Third, for regulatory agencies to justify their actions, the prediction model needs to be more than a black box. Many machine learning methods are not well received among criminal justice agencies because they lack clear logic or explanation for their decisions [15]. Demoulin and Coussement (2020) show that interpretability is a key antecedent for organizational acceptance of a text mining system [16]. High interpretability, therefore, is crucial for machine learning models to reach their full potential in assisting regulators and policymakers.

To address these challenges, we propose an interpretable deep learning framework to automatically extract patterns for prediction from a large corpus of firms’ annual reports (10-K’s), which is known to contain important information about firm-related issues [17]. Deep learning is a machine learning paradigm that combines multiple layers of neural networks to learn representations of data with multiple levels of abstraction [18]. Despite its ubiquity, effective integration of text data in financial models remains a challenging mission due to the difficulty in both obtaining and quantifying textual data. We show that the deep learning model is suitable for such tasks by condensing the sparsely encoded information in the financial text. We compare the predictive performance of the deep learning models to several benchmark models and show that deep learning models have superior out-of-sample performance.

We map our model design to the logic of the problem by making three adaptations to a typical deep text classification model. First, we add hierarchical attention mechanisms to the deep learning model. The

##

attention mechanisms automatically assign context-dependent weights to words and paragraphs during the model training process, thus allowing us to decode which part of the data the neural network is paying attention to. This is important for regulatory considerations because the trained neural network is directly interpretable. Second, we use a graph-based machine learning approach to represent firms’ dynamic context in a network. Specifically, we extract business description sections from the 10-K’s and construct a business proximity network [19,20] using a novel text similarity measure. The network supports the intuition that two competing firms usually have similar product descriptions. We then use a neural network to represent each firm’s position on the network with a low-dimensional vector. This graph-based definition of the environmental context can capture competition across industry boundaries; it is also inherently dynamic because the competitive relationships are updated along with the annual filings. We encode this environmental context learned from textual data using Gated Recurrent Units (GRUs), a type of recurrent neural network. Third and finally, we measure changes in historical financial reports and encode the sequence of temporal variations of a firm’s reports with GRUs to extract patterns indicative of insider trading.

Overall, this study contributes to the IS literature in several ways. First, most prior literature focuses on how big data analytics can help achieve organizational success such as agility, innovation, and competitive performance [21]. We add to the literature by offering a new set of predictive analytics tools for market regulators to detect corporate misconduct, namely, insider trading. We show that textual disclosure is relevant for its ability to reflect information cues that are missing in quantitative variables. In particular, our textual model can identify a coherent set of meaningful words and topics that are resonant with relevant economic and behavioral theories. In addition, our empirical findings shed light on theoretical tensions in prior studies regarding the effects of the competitive environment and temporal differences of filing documents on risks of insider trading. The prediction framework can potentially be used for detecting other financial misconduct and corporate wrongdoing.

Second, we contribute to IS methodology by designing an attention-based deep learning approach that integrates multiple inputs from textual, numerical, and relational data. Recently, deep learning has shown promising results in many areas of IS research including user-generated content [22–25], process analytics [26,27], and healthcare analytics [28,29], thanks to its ability to extract features from high-dimensional, unstructured data. We add to this growing stream of analytics literature by (1) showing how attention-based models can strike a balance between the better performance of neural networks and the higher interpretability of linear models, which is crucial for potential applications of such systems [16,30], and (2) extending the work of [19] and [20] by proposing a deep learning model to construct and to learn features from a business proximity network, thereby capturing information about firms’ competitive environment to enhance prediction.

Third, we show that predictive analytics for insider trading is an important and viable research topic for IS researchers. To the best of our knowledge, only a few studies looked at insider trading from a computational perspective and existing works are mostly exploratory [31]. We demonstrate, theoretically and empirically, that alleged insider trading cases are predictable from publicly available archival data. With the integrity of the modern financial market at stake, this is an area where IS researchers can make a significant contribution by informing other disciplines.

## 2 BACKGROUND AND RELATED WORK

We review three strands of related literature: (1) insider trading and its costs, (2) predictive analytics for regulators, and (3) deep learning methods in IS research. We also discuss how our work fills gaps in the prior literature.

## 2.1 Insider Trading and Its Costs

The trades of corporate insiders are among the most widely scrutinized activities in the stock market [32]. The social costs of insider trading are well documented. Easley et al. [33] show that a change of 10% in the probability of insider trades increases the cost of equity by 2.5% per year. Easley and O’Hara argue that information asymmetry associated with insider trading is a systematic risk that cannot be diversified away [1]. Although laws and regulations governing insider trading are implemented in many countries, they are not always effective. Using data from 52 countries, Bris reports a surprising finding: the intensity of insider trading and profitability increases after new laws are enforced [34]. U.S. law requires corporate insiders—defined as directors, officers, or owners of more than 10% of the company stock—to report transactions to the SEC.<sup>1</sup> Still, based on the abnormal returns of these reported transactions, it is clear that insiders take advantage of their information to make profitable trades [35].

While many scholars studied the factors behind the variation of insider trading activities [3,10,35], few have looked at the predictability of illegal insider trading. Cohen et al. show that only routine trades with zero abnormal returns are predictable, which has limited value for regulators’ enforcement actions [32]. Tamersoy et al. conduct a large-scale analysis of insiders’ trades using the Form 4 filings [31]. They extract distinctive temporal patterns in insiders’ trades that may be explained by regulations, policies, and other factors. However, the study is exploratory and does not address the predictability of the trades.

Our study fills a critical gap in the literature by providing evidence on the predictability of illegal insider trades. We use the alleged insider trading as the proxy on illegal insider trading because studies have documented that the activity of insider trading increases the probability of stockholder litigation if the valuations exploited by the insider trading activity are achieved using what can be alleged to be false or misleading information. Our focus is not to identify insider trading using ex-post insider trading records but rather to predict ex-ante potentially opportunistic insider trading by investigating the intent of insiders to benefit from their trading and how they face the trade-offs between financial benefits and potential costs.

## 2.2 Predictive Analytics for Regulatory Enforcement and Fraud Detection

In many domains, predictive analytics can be as, if not more, valuable as explanation [36]. Law enforcement is one of these domains. Predictive analytics allows enforcement agencies to stay ahead of the computational methods to detect financial fraud. We refer readers to Refs. [38–41] for reviews of these techniques. Our work is inspired by recent IS studies that use machine learning to detect financial statement fraud. Abbasi et al. propose a business intelligence framework that detects fraud from publicly available financial information [42]. Text mining methods have been used to identify SEC investigations [43,44]. Siering et al. use content-based and linguistic cues for online crowdfunding fraud detection [45]. Dong et al. use financial ratios and language-based features from social media data for corporate fraud prediction [46].

Our study adds to this stream of literature by focusing on the prediction of insider trading cases using text. We design our model to work with a much larger sample size (more than 90,000 observations, compared with the range between 122 and 652 in prior studies [43–46]). Further, although several studies consider textual features, they rely on different feature engineering methods. We propose an end-to-end deep learning model, in which the learning algorithm goes directly from the raw textual input to the prediction. As will be discussed later, the training of such end-to-end model can be more efficient, given a large amount of input data. Lastly, prior approaches mainly utilize case-specific features and do not consider relational data (i.e., firms’ relationship to its peers and its own past). The inclusion of a temporal component for individual firms would be an important extension to these methods [44]. Leveraging new methods to learn from relational data is also much needed in a networked business environment [19].

## 2.3 Deep Learning for Textual Data

Firms’ text disclosure plays an important role in how financial information is conveyed to the public. Studies have demonstrated that qualitative corporate filings contain valuable information about credit risk [47] and financial statement frauds [43]. However, many prior text analytics studies rely on simple text summarization techniques such as word count, sentiment, and readability [48,49]. The information in financial text goes well beyond these measures [50]. To leverage the full value of the textual disclosures, there is a need for more efficient algorithms to extract information from textual data.

In the past decade, artificial neural network has been used as an important tool in IS research (see, e.g., Refs. [27,51,52]). Built on classical neural network theories, deep learning models [18] add additional processing layers that can transform raw inputs into higher-level representations. For textual data, a deep learning model maps discrete words or phrases into continuous representations in a vector space. This allows the model to operate on the semantics of raw inputs and circumvent the dimensionality problem in text classification. Several recent IS studies successfully leverage deep learning models such as recurrent neural network and word embeddings for prediction tasks in healthcare domains and online reviews [22,23,28,29,53].

Despite their remarkable predictive capabilities, deep learning models have been criticized for being black boxes with low interpretability. As machine learning models penetrate critical areas such as financial markets and medicine, there is increased anxiety about whether they can be trusted if they cannot be understood. New regulations from the European Union propose that individuals affected by algorithmic decisions have a right to explanation [54]. Law enforcement agencies especially require high interpretability of machine learning models since they must defend their decisions [15]. To address the issue of interpretability, we introduce attention mechanisms. Attention mechanism [55] is a novel technique in deep learning that allows a neural network model to focus dynamically on a subset of an input based on a given context to enhance pattern recognition. We show that hierarchical attention mechanisms allow our model to achieve both high prediction accuracy and interpretability.

## 3 THEORETICAL FOUNDATION

## 3.1 Predictability of Insider Trading

Before discussing the details of the prediction model, we need to answer the following question: why do we believe that future insider trades are predictable in the first place? To justify the prediction models, we note that findings from both behavioral psychology and corporate finance lend support to our approach. To begin with, behavioral experiments have shown that unethical behaviors such as informed insider trading are not random. Various economic and psychological causes—such as external and internal reward [56], the probability of punishment [57], and saliency of dishonesty [58]—can trigger or curtail acts of cheating. In other words, having knowledge of environmental cues makes future dishonest actions predictable.

At the firm level, the financial reports and market performance often disclose the environmental factors that elicit insider trading. Several specific channels can contribute to the predictability of insider trading behavior. First, financial documents contain cues about managers’ personal incentives that can often foretell their actions. The quality of managerial disclosure can reveal subsequent insider trading decisions [59]. A lower quality disclosure is associated with future insider purchasing, as managers wish to maintain their information advantage. Second, financial reports may disclose weaknesses in internal control, such that certain actions and policies of the firm management can lead to an unethical work environment [60]. Moreover, certain business cultures are more likely to weaken the honesty norm and promote dishonest behavior [61], and a firm’s ethical culture can be reflected in its financial report [62]. Lastly, corporate insiders, for their own incentives, have the propensity to engage in trading prior to material events such as bankruptcy [63]; these material events are known to be predictable using machine learning models [44,64]. Taken together, just as how lab experiments and empirical studies can estimate the causal effects of an isolated factor, a machine learning model should be able to derive patterns from historical data prior to opportunistic insider trading behavior.

## 3.2 Utility of Financial Text

We propose that financial text, corporate annual filings in particular, can be used as an important source of information for a machine learning model. Theoretically, the information manipulation theory [65] argues that insiders who tend to conduct opportunistic trading will have incentives to withhold relevant information so that investors are more likely to make incorrect inferences. Meanwhile, once the insider has chosen to commit opportunistic insider trading, he or she has incentives to engage in a type of word “shell game”, which grandstands certain aspects of performance to deflect attention away from the economic events that precipitated the insider trading [66]. Given such subtle motives, highly aggregated variables such as document tone are limited by their low dimensionality. For example, an opportunistic insider might have incentives to be abnormally positive on one topic, but abnormally negative on another, washing away any signal in aggregate tone. A deep learning model has the potential to learn new representations from the raw text—a high dimensional data structure—to identify both effects.

Specifically, the Management Discussions and Analysis (MD&A) section of the 10-Ks can contribute significant prediction power for three reasons. First, while most of financial statements are numeric summary of historical performance, the purpose of MD&A is to provide a management perspective not only on their firms’ past performance and current financial positions, but also their future prospects. Second, public text information provides a setting that is more consistent with the argument of limited investor rationality and investor attention developed in recent literature [67]. In contrast, numerical data extracted from financial statements or the stock market are less likely to be subject to simple limited investor attention. Finally, managers tend to have more freedom in writing the texts of the annual report rather than of the numbers, since the latter are subject to generally accepted accounting principles or other applicable accounting rules. Therefore, MD&As can shed light on more nuanced managerial behaviors and strategic intent.

Other than the MD&A section, two additional sources of information from 10-Ks can add predictive power. The business description section can capture firms’ competitive environment [68], which may either encourage or restrain insider trading. On the one hand, because insiders’ potential profit depends on the information asymmetry, they are less likely to extract rents in highly competitive environments closely monitored by analysts and peers [69]. On the other hand, a complex environment—partly embodied by competitive pressures from peers [70]—creates opportunities for insiders to exploit their information advantage. This can be due to the lapse of ex-ante preventive measures [12]. Or, firms with similar descriptions are more likely to engage in mergers and acquisition (M&A) deals because of product market synergies. Informed insider trading is prevalent ahead of these M&A announcements [71].

Further, firms’ changes in the filings also carry valuable information. Cohen et al. [13] present the “lazy prices” phenomenon: changes to the 10-Ks predict future earnings, news announcement, and most importantly, insider selling activities. This is because the public digest these changes with a lag, but the insiders hold material information on why these changes took place. Therefore, we contend that the temporal differences of filing documents for individual firms can also add value to a prediction model.<sup>2</sup>

## 4 DATA AND PREPROCESSING

We construct our insider trading database by merging four data sources: class action lawsuit data from

##

Stanford Securities Class Action Clearinghouse (SCAC), textual disclosure data from 10-K annual filings to the SEC’s Electronic Data Gathering, Analysis, and Retrieval (EDGAR) system, accounting data from Compustat North America, and equity trading data from Center for Research in Security Prices (CRSP). Our initial sample consists of the entire population of publicly traded companies in the U.S. from Compustat during the period of 1996–2015 with no missing data for the main numerical variables used in the analysis. We then match our sample with the CRSP database for trading data on the exchanges and exclude firms that CRSP does not cover. Next, we match this sample with the SEC’s EDGAR system, which provides the most comprehensive and accurate textual disclosure data on the 10-K, as well as its variants, annual filings. After the match, we then identify a sample of firms that are subject to class action lawsuits by collecting litigation data from SCAC, which has all securities class actions filed in U.S. federal court since the passage of the Private Securities Litigation Reform Act (PSLRA) of 1995. To the best of our knowledge, our final sample covers all publicly traded domestic firms in the U.S., which were the subject of the class action suit identified for the period of 1996–2015. Figure 1 summarizes our analysis procedure, including database construction, data preprocessing, feature extraction, and model training and evaluation. Next, we describe each dataset and analysis procedure in detail.

## 4.1 Insider Trading Indicator

Our sample begins with the firms that were the subject of a class action lawsuit identified through the SCAC.<sup>3</sup> The SCAC provides detailed information regarding the filing date, class period (i.e., the period over which the alleged fraudulent behavior occurred), nature of the complaint, and settlement terms. We examine security class-action suits occurring after passage of the PSLRA with filing dates between 1996 and 2015. Figure 2 provides several excerpts from the lawsuit filings.

![](/api/attachments/TJYGNSJB/fulltext/images/32efa4a9907160fe0f0eaaa2dd59cf5cde4323606a409ea9e3f98e52aa9b192f.jpg)

Figure 1: Research Framework  
![](/api/attachments/TJYGNSJB/fulltext/images/fe6621ac7214adf8713ee018f453d33472f4f84d8187a87d5113f6df1bae86a8.jpg)  
Figure 2: Excerpts from Insider Trading Class-Action Lawsuits

Since not all the cases in SCAC are insider trading, we identify cases violating any law or rule related to insider trading. The Securities Exchange Act of 1934 was the first law against insider trading. The Act grants the SEC the authority to set the rules. Section 20A of the Act provides a private right of action against persons engaged in insider trading. SEC has also enacted Rule 10b5-1 to deter insiders from trading on private information. Thus, within all case summaries, we search for keywords mentioning this law or this rule using regular expressions. If either Section 20A or Rule 10b5-1 is mentioned in a case summary, then the case is annotated as positive. From our original sample of 4,903 security-related cases, we are able to identify 1,151 cases that are related to insider trading. For each identified positive case, we further assign it to the corresponding fiscal year of the firm based on its filing date.<sup>4</sup> Note that, typically, a legal case may last for many years and some may be dismissed at the end. To make the problem more tractable, the classification target is identified based only on the initial filing status of cases.

We acknowledge, of course, that the insider trading allegation by shareholders is an imperfect proxy for all illegal insider trading behavior. Insider trading can be alleged by other government institutes such as SEC, which puts illegal insider trading as a high priority area. That being said, the objective of this study is not to study how the regulators enforced insider trading laws in the past, but rather to provide them complementary support to detect additional illegal insider trading from publicly available archival data. As such, we intentionally do not base our prediction on the SEC enforcement cases but rather on the shareholder class action litigations which are expected to have significant impacts on the stock market participants overall. Despite its potential limitation as an instrument, a distinct advantage of our response variable is its simplicity and availability.

## 4.2 Numerical Financial Predictors

For numerical inputs, we compile eight firm-level predictor variables based on the literature on insider trading. When predicting financial misbehavior, it is common to consider the accounting information and up-to-date market information that may reflect the company’s liability, liquidity, and profitability status. Table 1 lists these variables and the rationale for including them. In our study, all variables are obtained by merging annual accounting data from Compustat North America with equity data from CRSP. To avoid recording errors or outliers, we further winsorize all the numerical predictor variables at 1% and 99% by replacing values that are lower than 1% with the variable’s first percentile and higher than the 99% with its 99th percentile. In addition, we include the Fama-French 12-industry classification as a categorical predictor. Table 2 provides the summary statistics of the numerical variables.

## 4.3 Textual Predictors

A key innovation of our study is that we consider an untapped textual data source to predict insider trading. The SEC requires all public firms to file a 10-K form at the end of each fiscal year. A complete 10- K consists of 14 items that provide a comprehensive yearly summary of a company’s business. Common items include business (description), financial performance, organization structure, executive compensation, and equity, among others.

Our prediction model focuses on the Business (Item 1) and the MD&A (Item 7) sections of 10-K. These two sections serve three different purposes in our prediction model. First, according to the theory of insider used to build a business proximity network each year (akin to [19,20]). The network captures firms’ dynamic relatedness with each other in terms of product, market, and technology. Our model then uses a firm’s structural position on the business proximity network—which represents the organizational environment of the firm—for prediction. Finally, we encode the temporal differences of the MD&A section to capture the recent changes in the firm.

Table 1: Description of Numerical Variables

<table><tr><td>Variable</td><td>Description</td><td>Rationale and References</td></tr><tr><td>LOGAT</td><td>Log (Total Assets)</td><td>Size is an important determinant for abnormal returns from informed insider trading. Insiders from smaller firms are more likely to have greater abnormal returns. A possible reason is that smaller firms have greater information asymmetry, as they are less closely monitored by institutional investors and analysts [72].</td></tr><tr><td>RSIZE</td><td>Relative market capitalization of the firm. Calculated using the log market capitalization of the firm divided by the market value of all securities</td><td>We follow [72] and consider the relative size (along with the absolute size) of the firm to the market.</td></tr><tr><td>SIGMA</td><td>Stock volatility. Calculated as the standard deviation of the daily stock return observed over the previous three months</td><td>Informed trading in options market is prevalent. Acharya and Johnson (2007) show that insiders could also profit from the credit derivatives markets. Activities on these markets are associated with asset price volatility [73]. When the firm is in a more volatile condition or has higher default risk, the risk of insider trading also rises. The effect, however, could be the opposite for insiders with limited capital as they are unable to diversify away risk.</td></tr><tr><td>EXCESS_RETURN</td><td>The firm&#x27;s log excess return on its equity relative to that on the S&amp;P 500 index</td><td>A widespread form of insider trading is accompanied by earnings management [10]. For example, managers can inflate stock prices through misstating earnings before selling their stock holdings. Literature also documents that insiders exhibit “buy low and sell high” behavior. Following negative excess return compared to the market, insiders purchase stocks and intend to sell high based on future bullish private information.</td></tr><tr><td>LTAT</td><td>Total Liabilities / Total Assets</td><td>Managers in highly leveraged firms are more likely to undertake risky projects, thereby raising the volatility of the stock price, which can induce insider trading on the derivatives market. Leverage could also be associated with leveraged buyouts and wider credit spread on the CDS markets, both providing lucrative trading opportunities for insiders [74].</td></tr><tr><td>LOGSALE</td><td>Log (Sale)</td><td>Similar rationale to LOGAT.</td></tr><tr><td>MB</td><td>Market-to-Book Ratio. Calculated using the ratio of the market equity to the adjusted book equity to which we add a 10% difference between the market equity and book equity</td><td>MB measures if a firm is over or undervalued by the stock market relative to its accounting value. Insider trading is usually positively related to the MB ratio. Such behavior reflects insiders&#x27; recognition of market mis-valuation based on past performance and insiders&#x27; superior knowledge of the real potential of future performance [75].</td></tr><tr><td>INDUSTRY</td><td>Fama-French 12-industry classification (dummy coded)</td><td>Insider trading can be affected by industry-wide information flow, through channels such as suppliers sharing information from common customers [76].</td></tr></table>

We download all 10-K forms and its variants, 10-K405, 10KSB, and 10KSB40, from the SEC EDGAR system. We link 10-K forms to CRSP and the Compustat database using the Central Index Key (CIK). For each linked 10-K filing, we transform the file to plain text by removing the HTML tags, tables, and exhibits. We then extract the Business and MD&A sections using regular expressions. These two sections usually appear as Item 1 and Item 7 respectively.<sup>5</sup> The raw corpus is preprocessed in four steps. (1) We tokenize documents into individual words using spaCy, an open-source library for natural language processing (NLP). (2) We also use spaCy to lemmatize words to remove the inflectional forms of words and return them to basic forms. (3) We remove the common stop words, numeric, and punctuation marks. (4) Since some phrases have meanings that are not captured by simply summing up the individual words, we use the method recommended by [77] to find common phrases in the text and treat them as single words.

Table 2: Summary Statistics of Numerical Variables

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Median</td><td>Max</td></tr><tr><td>LOGAT</td><td>5.89</td><td>2.14</td><td>-6.91</td><td>5.86</td><td>14.99</td></tr><tr><td>RSIZE</td><td>-10.88</td><td>1.97</td><td>-17.2</td><td>-10.97</td><td>-3.46</td></tr><tr><td>SIGMA</td><td>0.03</td><td>0.12</td><td>0</td><td>0.01</td><td>15.19</td></tr><tr><td>EXCESS_RETURN</td><td>-0.02</td><td>0.27</td><td>-0.82</td><td>-0.03</td><td>3.74</td></tr><tr><td>LTAT</td><td>0.57</td><td>4.73</td><td>0</td><td>0.54</td><td>1410.5</td></tr><tr><td>LOGSALE</td><td>5.21</td><td>2.29</td><td>-6.91</td><td>5.21</td><td>12.98</td></tr><tr><td>MB</td><td>2.03</td><td>43.17</td><td>-4907.93</td><td>1.59</td><td>8803.86</td></tr></table>

We then merge numerical predictors with all the textual predictors based on Compustat identifier (GVKEY) and fiscal year to get our primary samples, which include all the firms from 1996 to 2015. For each firm-year combination, we identify whether the firm has at least one lawsuit related to insider trading in the following year as a binary indicator. Out of the 1,151 cases identified from the SCAC database, only 846 firm-years are annotated as positives due to missing 10-K reports or multiple charges within one year for some firms. This binary indicator becomes our prediction target. We lag the textual and numeric predictors by one year and use them to predict the insider trading cases. For the sake of efficiency, we remove words with few frequencies in the entire corpus and include only 45,000 most frequent words. Such a filtering procedure is a common practice in NLP. In total, our data include 11,612 firms and 90,152 firmyears with no missing observations. It is also extremely imbalanced with only 0.94% positive samples. Table 3 provides a yearly distribution of insider trading cases in the sample.

Using these numerical and textual predictors, we create deep learning models with attention mechanisms to predict insider trading. We also compare deep learning models with baseline models for benchmarking purposes (see Figure 1). We describe these models in the next section.

## 5 METHOD

Figure 3 presents the deep learning model architecture. Modules for processing different inputs are shown using different colors. These modules, annotated as A-F in the figure, are introduced one by one as follows.

Table 3: Distribution of Insider Trading Cases by Year (846 cases in total)

<table><tr><td>Year</td><td>Total Firms</td><td>Insider Cases</td><td>Trading</td><td>Year</td><td>Total Firms</td><td>Insider Cases</td><td>Trading</td></tr><tr><td>1996</td><td>3112</td><td>6</td><td></td><td>2006</td><td>4365</td><td>37</td><td></td></tr><tr><td>1997</td><td>5688</td><td>28</td><td></td><td>2007</td><td>4322</td><td>43</td><td></td></tr><tr><td>1998</td><td>5850</td><td>33</td><td></td><td>2008</td><td>4289</td><td>51</td><td></td></tr><tr><td>1999</td><td>5743</td><td>49</td><td></td><td>2009</td><td>4108</td><td>20</td><td></td></tr><tr><td>2000</td><td>5595</td><td>56</td><td></td><td>2010</td><td>3921</td><td>21</td><td></td></tr><tr><td>2001</td><td>5362</td><td>167</td><td></td><td>2011</td><td>3839</td><td>42</td><td></td></tr><tr><td>2002</td><td>4969</td><td>62</td><td></td><td>2012</td><td>3755</td><td>21</td><td></td></tr><tr><td>2003</td><td>4696</td><td>58</td><td></td><td>2013</td><td>3718</td><td>15</td><td></td></tr><tr><td>2004</td><td>4451</td><td>64</td><td></td><td>2014</td><td>3795</td><td>5</td><td></td></tr><tr><td>2005</td><td>4413</td><td>60</td><td></td><td>2015</td><td>3937</td><td>8</td><td></td></tr></table>

## 5.1 Word Embedding (Module A)

In the first layer of the model, we learn vectorized representations of words from the documents. The goal is to represent each word as a vec tor of p dimensions (p = 100 in our experiments). This layer addresses the “curse of dimensionality” problem in the commonly used bag-of-words model. The bag-of-words model treats each unique word as a feature, which can increase the dimensionality of input features to over tens of thousands (the size of vocabulary). Dimension reduction on the inputs usually improves the out-of-sample performance of the model. Moreover, with a dense, vectorized presentation of the words, the prediction model makes use of the semantics rather than the syntax of the text.

![](/api/attachments/TJYGNSJB/fulltext/images/8503adea913c7e21e918e69ad90f0b32384279bceb57efe3f7c5cf1edb9d7f8e.jpg)  
Figure 3: Deep Learning Model Architecture  
There are two ways to obtain word vectors. Their first steps are the same. We start by observing that

each unique word ?? can be naturally expressed using a one-hot binary vector of size n, where n is the size of the vocabulary. Formally, let ?? denote the set of n unique words in total in the corpus, $C =$ $\left[ w _ { 1 } , w _ { 2 } , \dots , w _ { n } \right]$ . The one-hot encoding of word $w = [ x _ { 1 } , x _ { 2 } , \dots , x _ { n } ]$ , where $x _ { j } = { \left\{ \begin{array} { l l } { 1 , ~ i f ~ w = w _ { j } } \\ { 0 , o t h e r w i s e } \end{array} \right. }$ . For example, the fourth word in the vocabulary can be expressed as $[ 0 , 0 , 0 , 1 , 0 , . . . , 0 ]$ . The one-hot vector is a very sparse representation because there are n-1 zeros in the vector. Then the neural network uses the corpus to learn an embedding matrix, ??, with dimension $n \times p$ . The matrix ?? projects the one-hot vector of the j-th word to a vector $e _ { j }$ in $\mathbb { R } ^ { p }$ , where $e _ { j }$ is the corresponding row in W. We use $e _ { j }$ vector representation of the word. The vector $e _ { j }$ is a dense vector with a much lower dimension.

The difference between these two ways is how to complete the feed-forward neural network for training. The first way is using the skip-gram model proposed in Ref. [77] to pre-train word vectors. It uses an unsupervised approach to learning word embedding vectors from a large corpus. The skip-gram model summarizes the contextual information of each word by predicting its surrounding words using a neural $e _ { j }$ $e _ { j }$ probability of observing each context word surrounding the j-th word. The second way is optimizing the parameter matrix ?? directly in a supervised model. In this approach, word vectors are initialized randomly and then learned as a part of the prediction. As a result, word vectors are tuned toward the learning target of the model. We experimented with both approaches and found that a hybrid approach renders better prediction performance. In this approach, we first train word vectors using the skip-gram model with our 10-K corpus, these word vectors are then used to initialize the embedding matrix ?? in our deep learning model, and ?? is further tuned during training the deep learning model.

## 5.2 Word Attention (Module B) and Paragraph Representations

Motivated by the human visual attention system, attention mechanisms have been actively used in image recognition models to find the focal points in images. This technique has recently been introduced to NLP and achieved excellent performance in many tasks [55,78]. Traditional NLP models (such as bag-of-words and deep learning models built solely on word embeddings) learn a fixed weight for the same input feature.

For example, a word is assumed to be equally informative throughout a document. The essence of attention is that the feature weight can change according to context, so the model can dynamically focus on the most relevant input features for prediction. Moreover, a significant advantage of attention is that it provides interpretability to the model based on the context-dependent weights of words and paragraphs.

We adopt the hierarchical attention network structure [78] and include two layers of attention mechanisms in our model. The first layer generates paragraph representations based on words, and the second layer generates document representations based on paragraphs. Such design allows us to interpret the model both at the local (paragraph) level and at the global (document) level. We introduce the first layer in this subsection and the second layer later in section 5.4.

In the first layer, attention is allocated to words within each paragraph. Previous studies show that specific words or topics in financial documents carry important information about firms. Yet, a word can have different meanings depending on the paragraph context. For instance, the word “extraordinary” can be used to describe the excellent performance of the firm; it can also mean extraordinary circumstances in which an abnormal course of action is warranted. Attention mechanisms can learn important words based on the local context and aggregate these informative words to form a representation of the paragraph.

Formally, a document with ?? paragraphs is denoted as $d = [ s _ { 1 } , s _ { 2 } , \ldots , s _ { m } ]$ , where the j-th paragraph $s _ { j } = [ x _ { j , 1 } , x _ { j , 2 } , \ldots , x _ { j , h } ] , x _ { j , i } ( i = 1 , 2 , \ldots , h )$ is the one-hot encoding vector of the i-th word in paragraph ??<sub>??</sub>, and h is the number of words in a paragraph. However, each of our MD&A document is very large, with about 200 natural paragraphs and 8,000 words. It would be difficult for recurrent neural networks such as LSTM or GRU to handle long dependencies in such a long sequence of words or paragraphs. Previous work has shown that LSTM and GRU models have a limited ability to search through memories far in the past to access information needed for making a prediction [79]. Hence, we divided each document into 40 paragraph blocks (?? = 40) by combining neighboring paragraphs (for simplicity, we just call such a block a “paragraph” thereafter). Similarly, we truncate long paragraphs and pad shorter ones so that each paragraph has a uniform length ℎ = 200. Let W denote the n × p embedding matrix for all word, where p is the embedding dimension. The first attention layer generates a representation for paragraph ??<sub>??</sub> through Equations (1)–(4):

$$
e _ {j} = s _ {j} W\tag{1}
$$

$$
u _ {j} = \tanh (e _ {j} W _ {a} + b)\tag{2}
$$

$$
a _ {j} = \frac {\exp (u _ {j} U _ {a} ^ {T})}{\sum \exp (u _ {j} U _ {a} ^ {T})}\tag{3}
$$

$$
z _ {j} = a _ {j} \circ e _ {j}\tag{4}
$$

Equation (1) returns a word embedding matrix $\boldsymbol { e } _ { j } ( \boldsymbol { e } _ { j } \in \mathbb { R } ^ { h \times p } )$ for all words in paragraph ??<sub>??</sub>. Equations (2)–(4) describe the attention mechanism. In Equation (2), through a q-unit hidden layer with weights $W _ { \mathrm { a } }$ and bias b, we get a hidden representation of $e _ { j } .$ , denoted as $u _ { j }$ $( u _ { j } \in \mathbb { R } ^ { h \times q } )$ , where $W _ { a } \in \mathbb { R } ^ { p \times q }$ $b \in \mathbb { R } ^ { 1 \times q }$ Moreover, the attention mechanism introduces another parameter, $U _ { a } \in \mathbb { R } ^ { 1 \times q }$ We can consider $U _ { a }$ as a context vector representing a query “should the model pay attention to a vector of $u _ { j } ? ^ { \dag }$ Then, in Equation (3), the cosine similarity between $u _ { j }$ and $U _ { \mathrm { a } }$ is calculated as the attention weight. The weight $( a _ { j } \in \mathbb { R } ^ { h } )$ is further normalized over all words in $s _ { j } .$ . Finally, as shown in Equation (4), the dot product of attention weight $a _ { j }$ and $e _ { j }$ , i.e., the weighted sum of the word embedding vectors in $s _ { j }$ , produces the paragraph presentation $\boldsymbol { z } _ { j } \in \mathbb { R } ^ { 1 \times p }$ . In this attention mechanism, $W _ { a } , b$ , and $U _ { a }$ are the parameters to be learned.

## 5.3 Business Proximity Network and Node Embedding (Module C)

As argued earlier, a firm’s competitive environment provides important contextual information for predicting insider behaviors. We adopt a social network approach to define a firm’s environment. In each year, we use the business description sections in the 10-K filings to construct a business proximity network [19,20,68]. Each firm is a node in the network. Two firms are connected if they have high product, market, or technology overlap, as measured by document similarity of their business descriptions. Then, we use a node embedding model to represent each firm as a 100-dimensional vector that summarizes the firm’s structural position in the network [80].

We use a document similarity algorithm built upon word embeddings, called Word Mover’s Distance (WMD), to calculate the dyadic proximity between firms [81]. Intuitively, when measuring the similarity of two documents ?? and $d ^ { \prime }$ , WMD captures the “total costs” of mapping each word in ?? to its closest synonym in $d ^ { \prime } . ^ { 6 }$ The mapping is less costly if two words are similar in meanings; the cost is zero if the same word appears in both documents. Formally, for a pair of documents ?? and $d ^ { \prime }$ both with length ??, we use embedding vectors to represent all the nouns, i.e., $d = [ e _ { 1 } , e _ { 2 } , \dots , e _ { l } ]$ and $d ^ { \prime } = [ e _ { 1 } ^ { \prime } , ~ e _ { 2 } ^ { \prime } , \ldots , e _ { l } ^ { \prime } ]$ . Let $c ( i , j ) = \left\| e _ { i } - e _ { j } ^ { \prime } \right\| _ { 2 }$ be the Euclidean distance of word vectors $e _ { i }$ and $e _ { j } ^ { \prime } .$ . Then the WMD between ?? and $d ^ { \prime }$ can be calculated as $\begin{array} { r } { r = \sum _ { i , j = 1 } ^ { l } T _ { i j } c ( i , j ) } \end{array}$ , where $T _ { i j }$ is the optimal solution to the optimization problem: min $\begin{array} { r } { \sum _ { i , j = 1 } ^ { l } T _ { i j } c ( i , j ) } \end{array}$ , subject to $\begin{array} { r } { \sum _ { j = 1 } ^ { l } T _ { i j } = e _ { i } , \sum _ { i = 1 } ^ { l } T _ { i j } = e _ { j } ^ { \prime } } \end{array}$ , and $T _ { i j } \geq 0$ , for $\forall i , j \in [ 1 , 2 , \ldots , l ]$ . This problem is essentially a transportation problem: the words in ?? are the sources and the words in $d ^ { \prime }$ are the destinations; the costs are the semantic distances between pairs of words.

After we calculate the pairwise proximity between firms using WMD, we follow Ref. [68] and define the network by adding edges between the top 2.05% of the most similar firm pairs. The threshold resembles the granularity of the Standard Industrial Classification (SIC) code at the three-digit level (2.05% firm pairs belong to the same SIC-3 industry). Because we use the word embedding technique to measure the similarity between firms, our approach is a deep learning alternative to the text-based business proximity networks proposed by recent literature [19,20,68]. Compared with the cosine similarity approach in [68], our method is robust to synonymy—firms sometimes use different words to describe the same product. Compared with the topic modeling approach used in [19], our approach naturally fits into the deep learning framework and does not entail estimating a Bayesian model.

Given the business proximity network, we need to find useful features in the network to represent firms’ environments. Traditional social network analysis relies on hand-picked features such as node degrees, centralities, and local communities to represent the nodes. By contrast, node2vec can automatically learn low-dimensional vector representations of nodes based on their network positions [80]. The idea behind the node2vec algorithm is conceptually similar to that of a skip-gram model, i.e., we can learn a word’s meaning from its neighbors. In a network, a node’s neighbors determine its role and position. The algorithm thus takes two steps. First, it learns each node’s neighbors by simulating r random walks of fixed length l starting from each node.<sup>7</sup> In the second step, it applies the skip-gram model on the traces of random walks (sequences of nodes) as if they were a text corpus. The nodes are treated as words, and each walk is treated as a sentence. In essence, node2vec uses a neural network to predict a node’s neighborhood defined by the random walks. Finally, because we construct one network each year, we align the yearly dimensions of node vectors using the orthogonal Procrustes method [82].

## 5.4 Paragraph Attention (Module D) and Document Representation

Now we turn to the second layer in the hierarchical attention model. This layer generates a representation of each document. It learns the meaning of a paragraph based on the global context, which consists of the preceding paragraphs and the firm’s competitive environment. In the previous subsection, we describe how a node vector encodes a firm’s structural position in a business network. Following the sequence-tosequence learning techniques [18], we use $\mathrm { G R U ^ { 8 } }$ to generate a document presentation from paragraph representations concatenated with the node vector at the beginning as a “preface”. This is to emulate how humans typically process the information in an MD&A document: first, understanding the firm’s overall business context and selecting useful information from the context into memory, then in a sequential manner, utilizing the memory to interpret each paragraph in the document, updating the memory with the most important information extracted from the paragraph, and finally generating a new representation of the paragraph. As shown in Figure 3, final representations, denoted as $Z ^ { \prime } = [ n v ^ { \prime } , z _ { 1 } ^ { \prime } , z _ { 2 } ^ { \prime } , \ldots , z _ { m } ^ { \prime } ]$ , are generated for the node vector and the paragraphs after the GRU.

While the first word-level attention layer identifies informative words in a paragraph, the second paragraph-level attention layer identifies important paragraphs when constructing a document representation. Note that the node vector also receives an attention score to indicate its importance. With a different set of parameters $W _ { a . }$ , ??, and $U _ { a } .$ , we treat $Z ^ { \prime }$ as $s _ { j }$ when applying the same attention mechanism described by Equations (2)–(4). This paragraph attention layer assigns an attention weight to each paragraph (Equation (3)), and generates a document representation as the weighted sum of the node vector and the paragraph representations (Equation (4)).

## 5.5 Temporal Variation of MD&A (Module E)

The temporal variation of a firm’s MD&A documents is another textual input of our model. The temporal variation of firm i’s MD&A document at period ?? is represented as a sequence $R _ { t } ^ { ( i ) } =$ $[ r _ { ( t - k , ~ t - k + 1 ) } , ~ r _ { ( t - k + 1 , ~ t - k + 2 ) } , \ldots , r _ { ( t - 1 , ~ t ) } ]$ , where $r _ { ( t _ { 1 } , t _ { 2 } ) }$ is the WMD of a pair of MD&A documents at consecutive periods $t _ { I }$ and $t _ { 2 } .$ . We set $k = 5$ in our experiment, i.e., the model considers the extent of changes in a five-year window. In order to generate a final representation of $R _ { t } ^ { ( i ) }$ that can capture patterns of temporal variations, we pass the sequence through a bidirectional GRU so that each element is linked with both its preceding and succeeding elements in the sequence.

So far, we have processed all textual predictors. As shown in Figure 3, the final presentations of node vectors, MD&A documents, and temporal variations are concatenated and sent to another dense layer to allow interactions among them.

## 5.6 Numerical Financial Indicator Predictors (Module F)

As the final input of our model, the numerical predictors first enter a dense layer to allow interactions among the predictors. Then the output of this hidden layer is merged with the textual predictors in another dense hidden layer to generate the final features for prediction. These features enter a single neuron with a sigmoid activation function to predict inside trading probabilities in accordance with prior neural network literature.

## 5.7 Comparison with Baselines Models

We now compare the attention-based deep learning model with a set of standard baseline models that use the bag-of-words representation of text documents. The bag-of-words model has been used in many

##

other IS studies that use text as predictors (e.g., [43,45]). While the bag-of-words model is conceptually simple with good interpretability, our deep learning framework has two advantages. First, the word embedding layer learns the semantics of the words and represents them in a low-dimension space. Although singular value decomposition (SVD) on a document-term matrix can achieve the same goal (e.g., Zhou et al., 2018, [22]), SVD is computationally expensive $( O ( \operatorname* { m i n } \{ m n ^ { 2 } , m ^ { 2 } n \} )$ for an ?? × ?? matrix). Moreover, SVD requires the entire document-term matrix to be fit into the memory. These hurdles make SVD impractical for a large corpus. A deep learning model, on the other hand, can leverage the parallel computing power of Graphics Processing Units (GPUs). It also supports mini-batch training, whereby the model can be trained using a stream of small subsets of the data. Therefore, our model is easily scalable.

The second advantage of our framework is that models using bag-of-words representations allocate the same weight to a word within all samples, while an attention mechanism assigns context-dependent weights locally to features within a sample. The context can be general semantics, as determined by surrounding words and sentences. The context can also be specific to the problem itself, such as the position of the firm in the business proximity network. Moreover, as shown in our hierarchical attention network, attention mechanisms can be flexibly applied to any layer in the deep learning architecture. This allows the model to be interpretable at different levels of granularity.

Empirically, we use two common baseline algorithms based on the bag-of-words model: support vector machine (SVM) and Naïve Bayes. In a text classification problem, common baseline algorithms include Naïve Bayes, k-nearest neighbors (kNN), SVM, logistic regression, and decision tree [83,84]. We exclude kNN, decision tree, and logistic regression because they yield poor performance in our experiment. Distance-based algorithms such as kNN fail because the MD&A documents from the same firm are usually more similar to each other than to those from other firms. As a result, the nearest neighbors are usually historic documents of the same firm. Also, in our end-to-end approach (in contrast to the feature engineering approaches as in prior work [85,86], the models learn directly from the bag-of-words representations. Without careful regularization, logistic regression and decision tree tend to overfit the bag-of-words inputs, as it is possible to find a subset of words that fits every training sample perfectly (complete separation).

##

Therefore, we follow prior work and use Naïve Bayes and SVM as baseline algorithms because of their ability to generalize well in large feature spaces [42,46,84].

In addition, we compare our model to two neural network architectures based on the word embedding layer: average embedding, doc2vec [87], and convolutional neural network (CNN) [88]. Note that in general RNN does not apply for sequences with 8,000 time steps. The average embedding model computes the column mean of the word vectors for each document and yields a p-100 dimensional dense feature vector, which is then fed into a dense layer with 32 units and an output layer. The doc2vec model extends the word2vec model that we use to pre-train the word embedding matrix; a 100-dimensional document vector is trained along with the word vectors to predict all the words in each document. The document vector is used as the feature vector for each document and connects to the dense and output layer. The CNN model applies one-dimensional convolution of three different kernel sizes (f = 3, 4, and 5) to the word vectors in a document. For each kernel size h, we use $5 0 f { \times } p$ filters to transform each window of f consecutive word vectors into a scalar; a max-pooling layer then finds the maximum value of the scalars produced by each filter. The 150-dimensional feature vector is connected to a dense layer and an output layer.

Finally, we consider four baseline models with only numerical predictors: a logistic regression, a decision tree, a SVM with Gaussian kernel, and a neural network model. The neural network model is similar to Module F in Figure 3, except that the output of the hidden layer is not merged with the textual features, but enters a single neuron with a sigmoid activation function to produce predictions.

## 6 EMPIRICAL RESULTS

## 6.1 Model Implementation and Evaluation

In this section, we present the results of our experiments with attention models and compare their performance with baseline models. All models are trained on an Ubuntu 14.04 server with a Xeon E5-2620 v4 CPU, 64 GB of memory, and a GTX 1080 GPU.

To measure model performance, we apply stratified five-fold cross-validation and report the average

AUC obtained from test sets.<sup>9</sup> Because insider trading cases are rare, using the classification accuracy to measure a model’s performance can be misleading. This is because the accuracy score assumes that Type I and Type II errors are equally costly. For regulators, however, prevention and deterrence are less costly than enforcement and punishment [89]. In other words, the cost of false negatives is higher than that of false positives. Although it is possible to assign a higher cost to the false negatives in the model’s objective function, such an assignment would be arbitrary. Moreover, regulators are interested in more than a mere dichotomous prediction of positive or negative case. An accurate assessment of the relative risk of a firm, as evaluated by AUC, can provide better guidance for resource allocation.

Hence, we use AUC as a more flexible performance measure. AUC calculates the trade-off between the false positive rate and the true positive rate as the decision criterion (cutoff probability) varies. It can be used to evaluate a model’s overall ability without assuming a relative cost structure. The AUC score ranges from 0.5 to 1, with 0.5 indicating a baseline of random assignment of class labels, and 1 suggesting a perfect classification. We also report the averaged decile-ranking table on the test sets. We rank the company’s predicted insider trading probabilities into deciles, where the top decile contains the companies with the highest risk and the bottom decile contains firms with the lowest risk. The decile table is constructed by tabulating the cumulative percentage of actual insider trading firms in each decile. A high percentage in the high deciles implies better out-of-sample prediction accuracy.

We implement our baseline models using scikit-learn, an open-source library for Python. All neural network models are implemented using Keras, a Python API built on top of Google’s TensorFlow library. As discussed earlier, for the word-embedding layer, we initialize the word-embedding matrix W with pretrained word vectors and then train it as a part of the models. The embedding dimension (p) is set to 100. We obtain pre-training word vectors with the entire text corpus using the skip-gram model [77]. The context vector $U _ { a }$ used in the attention layers is also set to 100 dimensions (q). The GRU for encoding paragraphs is configured with 100 cells. The bidirectional GRU for temporal variations has three cells to produce an output with six numbers. All hidden dense layers have 64 units and use ReLU activation function. In addition, to prevent overfitting, we apply a combination of L1 and L2 regularizations in all layers. Also, we apply batch normalization to each hidden layer to increase the stability of our model. Since our dataset is imbalanced, we incorporate class weights into the binary cross-entropy cost function.

## 6.2 Model Performance

Table 4 reports the model performance for all the baseline models. When using numerical predictors (Panel A), the best-performing model is the neural network model (denoted as Model D in Panel A) with an AUC of 78.95%. As shown in Figure 3, the hidden layer with 64 units can allow the eight numerical variables to have sufficient interactions with each other. As a result, it outperforms the logistic regression, which can be considered as a single neuron. When using text data (Panel B), the Naïve Bayes and SVM models perform equivalently, with an AUC around 70%. The average embedding model out-performs the bag-of-words models with an AUC of 72.51%. The doc2vec model performs worse than the average embedding model with an AUC of 68.03%. This is not surprising, as the document embeddings are only pre-trained and are not tuned to the firm outcomes. However, CNN has worse performance than simple bag-of-words models. We have also considered using LSTM to model each MD&A document as a long sequence of 8,000 words. Unsurprisingly, this model achieved very poor performance due to its difficulties in tracking memory through extremely long sequences [79]. This result is consistent with past studies that use textual disclosures to predict financial events [64] and highlights the challenge of applying CNN on long documents.

Now we turn to the performance of our attention-based deep learning models as shown in Table 5. First, with only the text (word embeddings) as the input, the model achieves AUC of 75.75%, 5% higher than Naïve Bayes and SVM baselines. Then we add other predictors to this model one at a time to examine the incremental effectiveness of each predictor. With the temporal variations added, the model performance increases to 76.19%. Similarly, incorporating the node vectors also improves the AUC. With all the textual predictors, the model (denoted as Model K in table 5) achieves a decent AUC score of 76.81%. Overall, we find 10-K textual disclosures have high predictive power for insider trading.

Table 4: Performance of Baseline Models

<table><tr><td colspan="5">Panel A: Baseline Models for Numerical Inputs</td></tr><tr><td>Models</td><td>(A) Logistic Regression</td><td>(B) Decision Tree</td><td>(C) SVM</td><td>(D) Neural Network</td></tr><tr><td>AUC (%)</td><td>76.84</td><td>76.63</td><td>78.55</td><td>78.95</td></tr><tr><td></td><td colspan="4">Deciles (%)</td></tr><tr><td>1</td><td>37.94</td><td>37.70</td><td>39.71</td><td>43.62</td></tr><tr><td>2</td><td>17.26</td><td>18.32</td><td>19.03</td><td>15.01</td></tr><tr><td>3</td><td>15.60</td><td>13.83</td><td>12.06</td><td>15.13</td></tr><tr><td>4</td><td>6.97</td><td>10.17</td><td>10.40</td><td>7.56</td></tr><tr><td>5</td><td>8.75</td><td>6.38</td><td>7.45</td><td>5.56</td></tr><tr><td>≥ 6</td><td>13.47</td><td>13.60</td><td>11.35</td><td>13.12</td></tr></table>

<table><tr><td colspan="6">Panel B: Baseline Models for Textual Inputs</td></tr><tr><td>Models</td><td>(E) Naïve Bayes</td><td>(F) SVM</td><td>(G) Average Embedding</td><td>(H) doc2vec</td><td>(I) CNN</td></tr><tr><td>AUC (%)</td><td>70.38</td><td>70.80</td><td>72.51</td><td>68.03</td><td>68.90</td></tr><tr><td></td><td colspan="5">Deciles (%)</td></tr><tr><td>1</td><td>31.21</td><td>33.57</td><td>37.71</td><td>31.32</td><td>30.61</td></tr><tr><td>2</td><td>14.42</td><td>15.61</td><td>15.60</td><td>13.12</td><td>13.12</td></tr><tr><td>3</td><td>12.76</td><td>11.35</td><td>11.23</td><td>11.82</td><td>12.53</td></tr><tr><td>4</td><td>10.40</td><td>8.39</td><td>7.45</td><td>9.34</td><td>9.81</td></tr><tr><td>5</td><td>7.69</td><td>6.97</td><td>5.55</td><td>7.09</td><td>8.04</td></tr><tr><td>≥ 6</td><td>23.52</td><td>24.11</td><td>22.46</td><td>27.31</td><td>25.89</td></tr></table>

Finally, when both textual and numerical predictors are included in the model (Model O), the AUC is further increased by more than 4% to reach 81.22%. This model also outperforms the best baseline model (Model D) by more than 2%. The DeLong test [90] for comparing ROC curves confirms that the AUC of Model O is significantly higher than Model D with a p-value 0.024. When comparing the decile table, this model has the highest 1st decile performance (45.63%). This means that if the regulators target the top 10% of the firms with the highest predicted insider trading probability, 45.63% of the positive cases will be included. Also, the sum of 1st and 2nd deciles in this model reaches 67.5%, exceeding the best baseline

model (Model D) by 10%.

Table 5: Performance of Deep Learning Models

<table><tr><td></td><td colspan="5">Deep Learning Models with Attention</td></tr><tr><td>Predictors</td><td>(K) Text only</td><td>(L) Text + Temporal Variation</td><td>(M) Text + Node Vector</td><td>(N) Text + Temporal Variation + Node Vector</td><td>(O) Text + Temporal Variation + Node Vector + Numerical</td></tr><tr><td>AUC (%)</td><td>75.75</td><td>76.19</td><td>75.96</td><td>76.81</td><td>81.22</td></tr><tr><td></td><td colspan="5">Deciles (%)</td></tr><tr><td>1</td><td>40.31</td><td>41.61</td><td>39.25</td><td>41.50</td><td>45.63</td></tr><tr><td>2</td><td>16.32</td><td>16.31</td><td>16.31</td><td>14.77</td><td>21.87</td></tr><tr><td>3</td><td>11.70</td><td>9.69</td><td>12.29</td><td>12.65</td><td>10.16</td></tr><tr><td>4</td><td>7.68</td><td>8.15</td><td>7.44</td><td>8.75</td><td>6.38</td></tr><tr><td>5</td><td>6.15</td><td>5.55</td><td>9.34</td><td>7.33</td><td>5.67</td></tr><tr><td>≥ 6</td><td>17.84</td><td>18.68</td><td>15.37</td><td>15.01</td><td>10.28</td></tr></table>

So far we have demonstrated that different constructs in our models have improved performance. A further question is whether these constructs can be configured differently to achieve even better performance. We conducted extensive experiments to search for optimal configurations. In one experiment, we created a number of different configurations based on Model M (Text + Node Vector), and tested their performance as shown in Table 6. First, in the original Model M, node vectors are treated as “preface” concatenated with paragraphs, and they can selectively inject useful information to the GRU state. Another option is to use node vectors directly as the initial state of GRU (Model M1). Although intuitive, this configuration has a potential risk that node vectors, which encode the market position of a firm, can bring unnecessary noise and may not act as an ideal initial state for processing paragraphs. This may explain that Model M1 achieves an average testing AUC of 74.33%, lower than that of Model M (75.96%). In contrast, in another configuration (Model M2), we capture the dependencies between node vectors and paragraphs only by self-attention without GRU. The average AUC achieved by this configuration is 75.49%, slightly lower than the original Model M.

Yet in another configuration (Model M3), we can further emphasize the dependencies between node vectors and paragraphs by using a bidirectional GRU, as suggested in Ref. [79]. However, since each paragraph in our dataset is a long sequence with 200 words, due to the limited capability of GRU in processing long sequences [79], we choose not to use a bidirectional GRU at the word level but only at the paragraph level. Model M3 is more computation-intensive due to the bidirectional GRU and it obtains an AUC of 75.46%, slightly underperforming the original Model M. Since an MD&A document serves as a critical source for investors to understand a firm through the eyes of management, each paragraph is usually made self-contained and seldomly dependent on subsequent paragraphs in order to provide great clarity. This may explain why the bidirectional GRU brings little gain. Further, another configuration (Model M4) can be created by using a Bidirectional GRU to process paragraphs with node vectors as initial states. This model achieves an AUC of 73.23%.

Table 6: Addition Configurations Created from Deep Learning Model (M)

<table><tr><td>Models</td><td>(M1) Node vectors as initial states of GRU to process paragraphs</td><td>(M2) Node vectors catenated with paragraphs without GRU</td><td>(M3) BiGRU processing concatenated node vectors and paragraphs</td><td>(M4) Node vectors as initial states of BiGRU to process paragraphs</td><td>(M5) Node vectors paralleled with document representation without influencing paragraph processing</td></tr><tr><td>AUC (%)</td><td>74.33</td><td>75.49</td><td>75.46</td><td>73.23</td><td>71.02</td></tr><tr><td colspan="6">Deciles (%)</td></tr><tr><td>1</td><td>37.00</td><td>40.42</td><td>40.77</td><td>35.22</td><td>29.08</td></tr><tr><td>2</td><td>17.38</td><td>14.54</td><td>16.20</td><td>15.25</td><td>17.13</td></tr><tr><td>3</td><td>11.94</td><td>11.23</td><td>10.40</td><td>12.53</td><td>13.83</td></tr><tr><td>4</td><td>8.16</td><td>9.58</td><td>6.98</td><td>11.11</td><td>10.28</td></tr><tr><td>5</td><td>5.67</td><td>6.98</td><td>6.62</td><td>5.44</td><td>7.92</td></tr><tr><td>≥ 6</td><td>19.86</td><td>17.26</td><td>19.03</td><td>20.45</td><td>21.75</td></tr></table>

Finally, we can create a configuration to completely disregard node vectors during the processing of paragraphs by GRU. In this configuration (Model M5), the paragraphs are first processed through GRU and the attention layer to obtain a document representation without the involvement of node vectors. Then a firm’s node vector is concatenated with the document representation, and the concatenated representation is sent to the dense layer for final prediction. The AUC of this model is 71.02%, significantly lower than the previous configurations. Our experiments suggest that node vectors have a positive impact on information extraction from paragraphs. In a similar vein, we also experimented with a number of variations for other models in Table 6, but they cannot outperform our original models in Figure 3 in terms of AUC performance. Due to space limitations, we omit their details. With these extensive experiments, we believe that our architecture shown in Figure 3 is reasonably good.

## 6.3 Insights from Error Analysis

We further analyze the prediction errors made by the best model with numerical predictors (Model D) and the deep learning model with all textual predictors (Model N) to determine if numerical and textual predictors are complementary or substitutable. Using a decision threshold of 0.5, we plot the recall rate of each class in Figure 4, i.e., the percentage of positive or negative samples that are successfully recovered. The left chart shows that about 46% of positive samples can be correctly identified by both models. The numerical model can recognize 25.65% of insider trading cases that are missed by the textual model, whereas the textual model recovers 11.82% of cases that cannot be identified by the numerical model. This seems to indicate that the numerical variables alone are more effective in recognizing positive cases. Yet it comes at the expense of a high false-positive rate, as shown by the right pie chart. The numerical model misidentifies 19.15% negative samples as positives, but these samples can be correctly identified by the textual model. In comparison, the textual model has about 8% fewer false positives. Overall, we conclude that textual and numerical predictors are complementary because 1) the model with both inputs (Model O) outperforms all other models, and 2) each input can help identify a portion of cases that otherwise would be missed by the other.

## 6.4 Interpreting Attentions on Text

A key feature of attention models is their interpretability, which allows us to understand why the model functions as it does. After the attention models have been trained, we retrieved all attention weights of Model N on the testing dataset to understand how a prediction of a specific sample is reached. These weights offer a new way to analyze the context-specific attention on individual words. To illustrate, we use a firm’s industry sector as the context. We first categorize the firms using the Fama-French 12 industry classification. Then, we select the top 25% cases based on their predicted probability, among which Finance, Healthcare, and Wholesale & Retail industries contain a large number of cases. For these three industry sectors, we collected the top 25% high-attention paragraphs and then the top 25% high-attention words. There are 157 unique words. As shown in Table 7, these three sectors share 49 common high-attention words.

Positive Samples

![](/api/attachments/TJYGNSJB/fulltext/images/e763b6799ded3c8283a95cc3c932e0bf24222647b9b65725b24c04d229d5ec9c.jpg)  
Negative Samples

![](/api/attachments/TJYGNSJB/fulltext/images/855d9a32790301532e6fffa7a4446148d2de6109cffcefbf2ae12a4bdbdfd0df.jpg)  
Figure 4: Error Analysis of Predictive Models with Different Inputs

First, the attention model quantifies a coherent set of words that captures the underlying incentives when managers plan to trade on their private information. Theory offers two hypotheses regarding managers’ disclosure [59]. On the one hand, managers may provide informative disclosure in advance of their transactions to reduce litigation risk. On the other hand, to maintain their advantage, they may exercise considerable discretion over specific facts and their interpretation of these facts. Many of the words shown in Table 7 are associated with these two hypotheses. When discussing the outlook of firms, insider managers are more likely to use negative language (loss, reduction, discontinue, or decrease) and uncertainty terms (change, issue, or defer), which may reduce the risk of private lawsuits. In particular, more emphasis on risk factors in the financial operation (issuance, repurchase, maturity, fund, exposure, instrument) and accounting management (tax, amortization, defer, balance sheet, SFAS, and repayment) may temper investor expectation and provide less ammunition for them to file lawsuits. Second, there is evidence of managers exercising discretion over disclosure quality. By providing words such as recognize, realize, believe, estimate, managers may attempt to convince investors and regulators that they are obeying the regulations while using their discretion to protect their private information. Overall, Table 7 provides realworld examples of how insiders strive to balance the “revealing” or “concealing” choice.

Table 7: Industry-Dependent High-Attention Words

<table><tr><td>Industry</td><td>Industry-Specific Words</td><td>Common Words</td></tr><tr><td>Finance</td><td>loan, policy, trading, mortgage, gain, hold, shareholder, client, allowance, transaction, portfolio, derivative, origination, income, consider, collateral, unrealized, reserve, manage, specific, default, prepayment, summary, guarantee, classify, present, residual, collect, strategy, adjustment, economic</td><td rowspan="3">recognize, loss, reflect, change, purpose, condition, tax, reduction, amortization, issuance, impact, repurchase, balance sheet, position, adopt, recognition, contract, issue, discussion, sfas, realize, require, maturity, discontinue, estimate, settlement, write, decrease, contractual, implement, review, fund, extent, company, determine, exposure, repayment, record, accounting, previously, instrument, continue, recent, believe, number, defer, accordingly, result, repay, accordance</td></tr><tr><td>Healthcare, Medical Equipment, and Drugs</td><td>delay, potential, inception, payment, milestone, collaboration, announce, progress, commence, likely, private placement, research development, commercialization, limitation, hospital, eliminate, research, eitf, intend</td></tr><tr><td>Wholesale, Retail, and Some Services (Laundries, Repair Shops)</td><td>open, initiative, improve, fiscal, integration, goodwill intangible, rent, reduce, customer, closure, delivery, earning, statement, method, negatively impact</td></tr></table>

\* Words are listed in decreasing order of their attention weights.

To further identify the amount of discretion that managers choose to exercise, we use the attention model to explore how it varies by context (industry sectors). As shown in Table 7, the high-attention words in the finance section suggest some risk factors are industry-specific, such as loan, trading, mortgage, portfolio, derivative, and pre-payment. For the healthcare industry, the focus is more related to innovation and commercialization. Firms in the wholesale and retail industry have higher attention on customer, operations, and logistics, e.g., customer, open, closure, integration, rent, reduce, and delivery. The finding confirms the importance of identifying industry-specific factors related to insider trading.

As we add hierarchical attention to the model, we can study how the model zooms in and out of a document. The model offers regulators the convenience of focusing their limited capacity on those highattention paragraphs. In Appendix A (in the companion file), we provide a case study in which the model highlighted two specific paragraphs in a positive case. We also use topic modeling to provide a bird’s-eye view of all the paragraphs that the model highlights. Prior research [17,19,91] has shown that latent Dirichlet allocation (LDA) is able to quantify the main themes in a firm’s textual disclosure. We first train a ten-topic LDA model using all the paragraphs in the entire sample. Appendix B (in the companion file) contains the word cloud of the high-probability words in each topic. We assign the following labels to the ten topics: Liability, Accounting, Production, Regulation, Operation, Hedging, Economy, Clinical, Proper, Plant and Equipment (PP&E), and Partnership. We then calculate the valence of topics as their mixture percentage in the entire sample. For example, overall the MD&A sections have 23% of the discussions on Liability, and 15% on Accounting-related issues. Finally, we use the LDA model trained from the full sample to infer the topic mixtures in the highlighted paragraphs (top ten high-attention paragraphs from each positive sample).

Figure 5 compares the topic proportions from the full sample with the proportions in the high-attention paragraphs. Consistent with the motive to avoid ex-post-facto shareholder litigation, insider managers are more likely to emphasize future liability risk and regulatory risks in the MD&A section. In addition, we consider two hypotheses derived from communication and psychology literature. First, consistent with the Information Manipulation Theory, it is clear from Figure 5 that high-attention paragraphs do under-report details from the internal aspects, such as accounting, production, and PP&E. The second hypothesis is derived from the finding in Ref. [92] that insider managers avoid references to themselves because they wish to minimize personal responsibility if the fraud and illegal insider trading are discovered. We find consistent evidence in support of this hypothesis from Figure 5. These insider managers do reduce the discussion in the MD&A on how they have evolved in the firm partnership management, in particular, using fewer words like partnership, advisory, affiliated, membership, and advisor.

## 6.5 Interpreting Node Embedding and Temporal Variations

Recall that we presented two competing theories about the effect of competitive environment: one suggests that competitors distract preventive measures and create more insider trading opportunities around M&As; the other suggests that competition erodes insiders’ information advantage. Attentions on node embedding vectors may offer a resolution. We examine network statistics for those firms with both high attention weights on node vectors and high prediction probability (both in top decile). In Figure 6, we plot a probability distribution of these firms’ node degrees, i.e., the number of competitors with similar products. We compare the degree distribution of high attention firms with that of all the firms in our sample. Figure 6 suggests that the high attention firms with possible insider trading activities have greater node degrees than an average firm. In other words, firms with more competitors are worth paying attention to.

![](/api/attachments/TJYGNSJB/fulltext/images/6a8b2ff536aea1951a3acc4766dcb90bd6efdb17ab55c592269a6d0f9037592e.jpg)  
Figure 5: Comparison of Topic Mixture (All Documents vs. High-Attention Paragraphs)

Next, we examine the effect of temporal variations on the prediction of insider trading, again with Model N. Our hypothesis is that if temporal variations contribute to the prediction of insider trading, their patterns should be different in the predicted positive cases than in the other cases. To verify this hypothesis, we divide our samples into two groups: cases with top one decile prediction probability (containing 41.50% true positive cases) and all the others. For each firm-year, the temporal variation is represented as a sequence of moving similarities of the firm’s MD&A in the past 5 years (see Section 5.5). Figure 7 shows the average similarities of the sequence over the samples in each group. The differences between these two groups are substantial: 0.08, 0.11, 0.10, 0.10, and 0.08 for the past 1–5 years respectively. All of the differences are statistically significant at the 1% level. Therefore, we conclude that our prediction model captures the impact of temporal variations on the possibility of illegal insider trading. Our experiment result supports the proposal that temporal variations would allow researchers to better understand how firm changes are manifest in financial texts [44].

![](/api/attachments/TJYGNSJB/fulltext/images/224db3e40dc6814758b6b1f4e2f50ee2c8892f6ab4bb6292c2dfd3d832c95931.jpg)  
Figure 6: Number of Competitors and Firm Attentions

![](/api/attachments/TJYGNSJB/fulltext/images/e7c9a3e301d539c79671d507aff8036ec498475d367b3ab0861f4a957330fcd4.jpg)  
Figure 7: Effect of Temporal Variations on Insider Trading Prediction

## 7 DISCUSSION AND CONCLUSION

Before Equifax, Inc., announced its data breach that affected 145 million consumers to the public in September 2017, three senior executives unloaded \$1.8 million of company shares [93]. Such insider trading instances led to public and media outcry, but financial regulatory agencies often failed to prosecute offenders due to limited resources. In this paper, we propose a machine learning framework to predict illegal insider trading, which the actual insider trading allegations by shareholders are used as the proxy. By combining a unique dataset of shareholders’ class-action lawsuits against insider trading with U.S. public firms’ financial reports, we conduct a comprehensive analysis to predict whether a firm will be the target of litigation. Our key methodological contribution is that we develop an interpretable deep learning model to extract information from the textual disclosures for both prediction and interpretation. We find that text is a useful information source for insider trading prediction. We also find models with both numerical features and financial text can give stronger out-of-sample prediction accuracy than the former alone. Moreover, we find that as theory predicts, contextual information extracted from a business proximity network and temporal changes of the documents adds predictive power. We interpret the model b identifying context-specific words and topics that are informative using the attention mechanisms.

## 7.1 Implications for Literature

Our study offers several implications for IS literature and knowledge base. First, from a design science perspective [94], we create an innovative artifact that is relevant for both practitioners and researchers. We design our framework specifically for regulatory considerations by achieving high predictability, interpretability, and scalability. We develop a deep learning method for text by considering a much larger corpus than is the case with existing methods. Overall, we demonstrate that deep learning is a valuable tool for text-based predictive analytics in IS research.

Second, both qualitative and quantitative IS researchers are increasingly using textual data to generate new theory [95]. For theory development, being able to “zoom in and out” of data is crucial because it enables a richer understanding of both the details and the broad patterns [96]. The hierarchical attention mechanism introduced in this study lends itself well to such tasks. By design, an attention-based model provides a principled approach to learn the broad predictive relationship between the text and dependent variable while also supporting zooming in and out of either informative words or paragraphs that support the predictions. In addition, the business proximity network constructed from text and the attention weights associated with node embedding vectors can provide fresh theoretical insights on the growing networked economy.

Third, we explore a new fintech research opportunity with profound societal implications. Gomber et al.

recognized the “one problem, one data set, one publication” problem in fintech research that may hinder the collaboration between academic researchers and practitioners [8]. To this end, our response variable and the predictor variables are publicly available. The availability of such “ground truth” and large data sources provides a common ground for a continuing conversation between the IS academia and regulators who have an interest in data-driven approaches.

## 7.2 Implications for Practice

The predictability of insider trading allows regulators to target future prevention, enforcement, and investigation efforts. Regulators are currently resigned to waiting for a trader to execute a trade of a size and timing precision that would warrant investigative work. Predictive models are much needed for resource-constrained regulatory agencies to flag and monitor highly probable firms. For example, the SEC took an initiative to develop software to examine language use in financial reports for signs of fraud [97]. Our work represents a novel development in this front. To the best of our knowledge, very few published studies use deep learning techniques to help financial regulators and policymakers streamline and automate the process of curbing illegal insider trading. Our framework takes an end-to-end approach, uses publicly available data without time-consuming feature engineering, and achieves superior performance. Moreover, attention mechanisms applied in our framework provide interpretability of predictions. The high-attention features have high face validity and corroborate recent high-profile insider trading cases. For example, industry-specific high-attention words reveal insider trading risks are associated with drug approval.<sup>10</sup> The attention on node vectors suggests that insider trading is more likely in the highly competitive industries where M&A activities take place.<sup>11</sup> The features highlighted by attentions allow regulators to reason and validate high-risk cases while proactively carrying out preventative interventions on targeted firms or individuals.

Apart from offering a decision support system for regulators, the mere existence of a prediction model could deter future opportunistic insider trading. According to Becker’s classical economic theory of crime [98], one would weigh the costs and benefits before making the choice of whether to commit an offense. It follows that there are two ways to deter illegal insider trading by swaying a would-be offender’s expected utility: raising the severity of punishment and increasing the certainty of detection. The results from behavioral experiments suggest that the certainty of detection has an even stronger effect than severe punishment [57]. On this basis, we believe that because a prediction model can result in swifter and more certain enforcement actions, the accompanying deterrence effect could indirectly benefit social welfare.

Predicting insider trades can also help expose other forms of corporate fraud. Research has shown that opportunistic insider trading goes hand-in-hand with other forms of corporate misbehavior such as earnings management [10]. The magnitude of insider trading often reflects the gravity of other problems—many insiders brazenly trade on a fraud that they or their colleagues committed. Together, these misbehaviors can pose even greater threats to shareholders and result in enormous welfare loss in the entire economy. Therefore, being able to predict opportunistic insider trading provides a glimpse of ongoing and future corporate fraud.

## 7.3 Limitations and Future Research

Our study has several limitations. First, we predicted only whether a firm faces insider trading litigation; we did not consider the severity of the case as well as SEC enforcement cases on insider trading. Future research could consider alternative targets such as the amount of abnormal return. Second, we conduct a firm-level analysis on insider trading. An individual-level analysis is also possible using executives’ individual characteristics from corporate governance databases. Third, our research used a single textual data source (10-K). Our methodology can be combined with other data sources such as social media (e.g., [46]) or earnings call transcripts to improve prediction accuracy. Our work can foster future research in this important area. Finally, although our model is trained with a comprehensive dataset, as new 10-K filings are added, the model may need to be fine-tuned to fit the changing corpus. How to create an adaptive deep learning framework (in the same vein as Metafraud [42]) is another interesting topic for future work.

## AuthorStatement

I herewith submit for your consideration the revised manuscript “Predicting Shareholder Litigation on Insider Trading from Financial Text – An Interpretable Deep Learning Approach” for publication in the Information and Management as a research article.

We would like to thank you for offering us the opportunity to revise this manuscript and the encouraging comments from the reviewer team. Following AE’s inputs, we have made several minor revisions in this version.

We thank you again for your effort to help us improve our paper. We hope you will find our revision to be satisfactory.

## REFERENCES

[1] D. Easley, M. O’Hara, Information and the cost of capital, J. Finance. 59 (2004) 1553–1583. https://doi.org/10.1111/j.1540-6261.2004.00672.x.

[2] R. Levine, C. Lin, L. Wei, Insider trading and innovation, J. Law Econ. 60 (2017) 749–800.

[3] V. Khanna, E.H. Kim, Y. Lu, CEO Connectedness and Corporate Fraud, J. Finance. 70 (2015) 1203–1252. https://doi.org/10.1111/jofi.12243.

[4] U. Bhattacharya, H. Daouk, The world price of insider trading, J. Finance. 57 (2002) 75–108.

[5] M.M. Correia, Political connections and SEC enforcement, J. Account. Econ. 57 (2014) 241–262.

[6] A. Abbasi, S. Sarker, R.H.L. Chiang, Big data research in information systems: Toward an inclusive research agenda, J. Assoc. Inf. Syst. 17 (2016) 3.

[7] G. Shmueli, O. Koppius, Predictive Analytics in Information Systems Research, MIS Q. 35 (2011) 553–572. https://doi.org/10.2139/ssrn.1606674.

[8] P. Gomber, R.J. Kauffman, C. Parker, B.W. Weber, On the Fintech Revolution: Interpreting the Forces of Innovation, Disruption, and Transformation in Financial Services, J. Manag. Inf. Syst. 35 (2018) 220–265. https://doi.org/10.1080/07421222.2018.1440766.

[9] B.J. Adams, T. Perry, C. Mahoney, The Challenges of Detection and Enforcement of Insider Trading, J. Bus. Ethics. 153 (2018) 375–388. https://doi.org/10.1007/s10551-016-3403-4.

[10] A. Agrawal, T. Cooper, Insider trading before accounting scandals, J. Corp. Financ. 34 (2015) 169–190. https://doi.org/10.1016/j.jcorpfin.2015.07.005.

[11] A.D. Jagolinzer, D.F. Larcker, D.J. Taylor, Corporate governance and the information content of insider trades J. Account. Res. 49 (2011) 1249–1274. https://doi.org/10.1111/j.1475-679X.2011.00424.x.

[12] L.L. Hansen, Corporate financial crime: social diagnosis and treatment, J. Financ. Crime. 16 (2009) 28–40. https://doi.org/10.1108/13590790910924948.

[13] L. Cohen, C. Malloy, Q. Nguyen, Lazy prices, 2018. https://doi.org/10.3386/w25084.

https://doi.org/10.1002/smj.4250121008.

[15] T. Brennan, W.L. Oliver, The Emergence of Machine Learning Techniques in Criminology, Criminol. Public Policy. 12 (2013) 551–562. https://doi.org/10.1111/1745-9133.12055.

[16] N.T.M. Demoulin, K. Coussement, Acceptance of text-mining systems: The signaling role of information quality, Inf. Manag. 57 (2020) 103120. https://doi.org/10.1016/j.im.2018.10.006.

[17] N. Pröllochs, S. Feuerriegel, Business analytics for strategic management: Identifying and assessing corporate challenges via topic modeling, Inf. Manag. 57 (2020) 103070. https://doi.org/10.1016/j.im.2018.05.003.

[18] Y. Lecun, Y. Bengio, G. https://doi.org/10.1038/nature14539.

[19] Z.M. Shi, G.M. Lee, A.B. Whinston, Toward a better measure of business proximity: Topic modeling for industry intelligence, MIS Q. 40 (2016) 1035–1056. https://doi.org/10.25300/MISQ/2016/40.4.11.

[20] S.Y. Yang, F.C. Liu, X. Zhu, D.C. Yen, A Graph Mining Approach to Identify Financial Reporting Patterns: An Empirical Examination of Industry Classifications, Decis. Sci. 50 (2019) 847–876. https://doi.org/10.1111/deci.12345.

[21] P. Mikalef, I.O. Pappas, J. Krogstie, P.A. Pavlou, Big data and business analytics: A research agenda for realizing business value, Inf. Manag. 57 (2020). https://doi.org/10.1016/j.im.2019.103237.

[22] S. Zhou, Z. Qiao, Q. Du, G.A. Wang, W. Fan, X. Yan, Measuring Customer Agility from Online Reviews Using Big Data Text Analytics, J. Manag. Inf. Syst. 35 (2018) 510–539. https://doi.org/10.1080/07421222.2018.1451956.

[23] D. Shin, S. He, G.M. Lee, A.B. Whinston, S. Cetintas, K.-C. Lee, Enhancing Social Media Analysis with Visual Analytics: A Deep Learning Approach, MIS Q. Forthcomin (2019) 1–67. https://doi.org/10.2139/ssrn.2830377.

[24] J. Guo, W. Zhang, W. Fan, W. Li, Combining Geographical and Social Influences with Deep Learning for Personalized Point-of-Interest Recommendation, J. Manag. Inf. Syst. 35 (2018) 1121–1153.

[25] F. Ahmad, A. Abbasi, J. Li, D.G. Dobolyi, R.G. Netemeyer, G.D. Clifford, H. Chen, A deep learning architecture for psychometric natural language processing, ACM Trans. Inf. Syst. 38 (2020) 1–29. https://doi.org/10.1145/3365211.

[26] J. Evermann, J.-R. Rehse, P. Fettke, Predicting process behaviour using deep learning, Decis. Support Syst. 100 (2017) 129–140. https://doi.org/10.1016/j.dss.2017.04.003.

[27] S. Fan, N. Ilk, A text analytics framework for automated communication pattern analysis, Inf. Manag. (2020).

https://doi.org/10.1016/j.im.2019.103219.

[28] J. Xie, X. Liu, D.D. Zeng, X. Fang, Understanding Medication Nonadherence from Social Media: A Sentiment-Enriched Deep Learning Approach, SSRN Electron. J. (2017). https://doi.org/10.2139/ssrn.3091923.

[29] X. Liu, B. Zhang, A. Susarla, R. Padman, Go to YouTube and See Me Tomorrow: Social Media and Self-Care of Chronic Conditions, MIS Q. Forthcomin (2019) 1–47. https://doi.org/10.2139/ssrn.3061149.

[30] I. Seeber, E. Bittner, R.O. Briggs, T. de Vreede, G.J. de Vreede, A. Elkins, R. Maier, A.B. Merz, S. Oeste-Reiß, N. Randrup, G. Schwabe, M. Söllner, Machines as teammates: A research agenda on AI in team collaboration, Inf. Manag. 57 (2020) 103174. https://doi.org/10.1016/j.im.2019.103174.

[31] A. Tamersoy, E. Khalil, B. Xie, S.L. Lenkey, B.R. Routledge, D.H. Chau, S.B. Navathe, Large-scale insider trading analysis: patterns and discoveries, Soc. Netw. Anal. Min. 4 (2014) 1–17. https://doi.org/10.1007/s13278-014-0201-9.

[32] L. Cohen, C. Malloy, L. Pomorski, Decoding inside information, J. Finance. 67 (2012) 1009–1043. https://doi.org/10.1111/j.1540-6261.2012.01740.x.

[33] D. Easley, S. Hvidkjaer, M. O’Hara, Is information risk a determinant of asset returns?, J. Finance. 57 (2002) 2185–2221. https://doi.org/10.1111/1540-6261.00493.

[34] A. Bris, Do insider trading laws work?, Eur. Financ. Manag. 11 (2005) 267–312. https://doi.org/10.1111/j.1354-7798.2005.00285.x.

[35] a. D. Jagolinzer, SEC Rule 10b5-1 and Insiders’ Strategic Trade, Manage. Sci. 55 (2009) 224–239. https://doi.org/10.1287/mnsc.1080.0928.

[36] R. Agarwal, V. Dhar, Big data, data science, and analytics: The opportunity and challenge for IS research, Inf. Syst. Res. 25 (2014) 443–448. https://doi.org/10.1287/isre.2014.0546.

[37] M.S. Gerber, Predicting crime using Twitter and kernel density estimation, Decis. Support Syst. 61 (2014) 115–125. https://doi.org/10.1016/j.dss.2014.02.003.

[38] R.J. Bolton, D.J. Hand, Statistical Fraud Detection: A Review, Stat. Sci. 17 (2002) 235–249. https://doi.org/10.2307/3182781.

[39] E.W.T. Ngai, Y. Hu, Y.H. Wong, Y. Chen, X. Sun, The application of data mining techniques in financial fraud detection: A classification framework and an academic review of literature, Decis. Support Syst. 50 (2011) 559–569. https://doi.org/10.1016/j.dss.2010.08.006.

[40] J. West, M. Bhattacharya, Intelligent financial fraud detection: A comprehensive review, Comput. Secur. 57 (2016) 47–66. https://doi.org/10.1016/j.cose.2015.09.005.

[41] M. Cecchini, H. Aytug, G.J. Koehler, P. Pathak, Detecting management fraud in public companies, Manage. Sci. 56 (2010) 1146–1160. https://doi.org/10.1287/mnsc.1100.1174.

[42] A. Abbasi, C. Albrecht, A. Vance, J. Hansen, Metafraud: A meta-learning framework for detecting financial fraud, MIS Q. 36 (2012) 1293–1327. https://doi.org/https://www.researchgate.net/profile/James\_Hansen7/publication/262403570\_MetaFraud\_A\_ meta-learning\_framework\_for\_detecting\_financial\_fraud/links/55ec5f2208aeb6516268c516/MetaFraud-Ameta-learning-framework-for-detecting-financial-fraud.pdf.

[43] F.H. Glancy, S.B. Yadav, A computational model for financial reporting fraud detection, Decis. Support Syst. 50 (2011) 595–601. https://doi.org/10.1016/j.dss.2010.08.010.

[44] M. Cecchini, H. Aytug, G.J. Koehler, P. Pathak, Making words work: Using financial text as a predictor of financial events, Decis. Support Syst. 50 (2010) 164–175. https://doi.org/10.1016/J.DSS.2010.07.012.

[45] M. Siering, J.A. Koch, A. V. Deokar, Detecting Fraudulent Behavior on Crowdfunding Platforms: The Role of Linguistic and Content-Based Cues in Static and Dynamic Contexts, J. Manag. Inf. Syst. 33 (2016) 421– 455. https://doi.org/10.1080/07421222.2016.1205930.

[46] W. Dong, S. Liao, Z. Zhang, Leveraging financial social media data for corporate fraud detection, J. Manag. Inf. Syst. 35 (2018) 461–487. https://doi.org/10.1080/07421222.2018.1451954.

[47] T. Loughran, B. McDonald, When is a liability not a liability? Textual analysis, dictionaries, and 10‐Ks, J. Finance. 66 (2011) 35–65.

[48] S.T. Li, T.T. Pham, H.C. Chuang, Do reviewers’ words affect predicting their helpfulness ratings? Locating helpful reviewers by linguistics styles, Inf. Manag. 56 (2019) 28–38. https://doi.org/10.1016/j.im.2018.06.002.

[49] W. Chung, D. Zeng, Dissecting emotion and user influence in social media communities: An interaction modeling approach, Inf. Manag. 57 (2020) 103108. https://doi.org/10.1016/j.im.2018.09.008.

[50] Z. Bozanic, M. Thevenot, Qualitative Disclosure and Changes in Sell‐Side Financial Analysts’ Information Environment, Contemp. Account. Res. 32 (2015) 1595–1616.

[51] X.B. Li, S. Sarkar, Protecting privacy against record linkage disclosure: A bounded swapping approach for

numeric data, Inf. Syst. Res. 22 (2011) 774–789. https://doi.org/10.1287/isre.1100.0289.

[52] G. Pant, P. Srinivasan, Predicting Web page status, Inf. Syst. Res. 21 (2010) 345–364. https://doi.org/10.1287/isre.1080.0231.

[53] H.M. Zolbanin, B. Davazdahemami, D. Delen, A.H. Zadeh, Data Analytics for the Sustainable Use of Resources in Hospitals: Predicting the Length of Stay for Patients with Chronic Diseases, Inf. Manag. (2020) 103282. https://doi.org/10.1016/j.im.2020.103282.

[54] B. Goodman, S. Flaxman, European Union regulations on algorithmic decision-making and a “right to explanation,” ArXiv Prepr. ArXiv1606.08813. (2016). https://doi.org/10.1609/aimag.v38i3.2741.

[55] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A.N. Gomez, L. Kaiser, I. Polosukhin, Attention Is All You Need, in: Adv. Neural Inf. Process. Syst., 2017: pp. 5998–6008. https://doi.org/10.1017/S0140525X16001837.

[56] O. Amir, D. Ariely, A. Cooke, D. Dunning, N. Epley, U. Gneezy, B. Koszegi, D. Lichtenstein, N. Mazar, S. Mullainathan, Psychology, behavioral economics, and public policy, Mark. Lett. 16 (2005) 443–454.

[57] D.S. Nagin, G. Pogarsky, An experimental investigation of deterrence: Cheating, self‐serving bias, and impulsivity, Criminology. 41 (2003) 167–194.

[58] F. Gino, S. Ayal, D. Ariely, Contagion and differentiation in unethical behavior: The effect of one bad apple on the barrel, Psychol. Sci. 20 (2009) 393–398. https://doi.org/10.1111/j.1467-9280.2009.02306.x.

[59] J.L. Rogers, Disclosure quality and management trading incentives, J. Account. Res. 46 (2008) 1265–1296. https://doi.org/10.1111/j.1475-679X.2008.00308.x.

[60] H.A. Skaife, D. Veenman, D. Wangerin, Internal control over financial reporting and managerial rent extraction: Evidence from the profitability of insider trading, J. Account. Econ. 55 (2013) 91–110. https://doi.org/10.1016/j.jacceco.2012.07.005.

[61] A. Cohn, E. Fehr, M.A. Maréchal, Business culture and dishonesty in the banking industry, Nature. 516 (2014) 86–89.

[62] J.M. Swales, P.S. Rogers, Discourse and the projection of corporate culture: The mission statement, Discourse Soc. 6 (1995) 223–242.

[63] H.N. Seyhun, M. Bradley, Corporate Bankruptcy and Insider Trading, J. Bus. 70 (1997) 189–216. https://doi.org/10.1086/209715.

[64] F. Mai, S. Tian, C. Lee, L. Ma, Deep learning models for bankruptcy prediction using textual disclosures, Eur. J. Oper. Res. 274 (2019) 743–758. https://doi.org/10.1016/J.EJOR.2018.10.024.

[65] S.A. McCornack, Information manipulation theory, Commun. Monogr. 59 (1992) 1–16. https://doi.org/10.1080/03637759209376245.

[66] G. Hoberg, C. Lewis, Do fraudulent firms produce abnormal disclosure?, J. Corp. Financ. 43 (2017) 58–85. https://doi.org/10.1016/j.jcorpfin.2016.12.007.

[67] D. Hirshleifer, S.H. Teoh, Limited attention, information disclosure, and financial reporting, J. Account. Econ. 36 (2003) 337–386. https://doi.org/10.1016/j.jacceco.2003.10.002.

[68] G. Hoberg, G. Phillips, Text-based network industries and endogenous product differentiation, J. Polit. Econ. 124 (2016) 1423–1465.

[69] J. Peress, Product market competition, insider trading, and stock market efficiency, J. Finance. 65 (2010) 1– 43. https://doi.org/10.1111/j.1540-6261.2009.01522.x.

[70] L. Xue, G. Ray, B. Gu, Environmental uncertainty and IT infrastructure governance: A curvilinear relationship, Inf. Syst. Res. 22 (2011) 389–399. https://doi.org/10.1287/isre.1090.0269.

[71] P. Augustin, M. Brenner, M.G. Subrahmanyam, Informed options trading prior to takeover announcements: Insider trading?, Manage. Sci. 65 (2019) 5697–5720. https://doi.org/10.1287/mnsc.2018.3122.

[72] J.-C. Lin, J.S. Howe, Insider trading in the OTC market, J. Finance. 45 (1990) 1273–1284. https://doi.org/10.1111/j.1540-6261.1990.tb02436.x.

[73] V. V. Acharya, T.C. Johnson, Insider trading in credit derivatives, J. Financ. Econ. 84 (2007) 110–141. https://doi.org/10.1016/J.JFINECO.2006.05.003.

[74] V. V. Acharya, T.C. Johnson, More insiders, more insider trading: Evidence from private-equity buyouts, J. Financ. Econ. 98 (2010) 500–523. https://doi.org/10.1016/J.JFINECO.2010.08.002.

[75] R.M. Bushman, J.D. Piotroski, A.J. Smith, Insider trading restrictions and analysts’ incentives to follow firms, J. Finance. 60 (2005) 35–66. https://doi.org/10.1111/j.1540-6261.2005.00724.x.

[76] D.M. Alldredge, D.C. Cicero, Attentive insider trading, J. Financ. Econ. 115 (2015) 84–101. https://doi.org/10.1016/j.jfineco.2014.09.005.

[77] T. Mikolov, I. Sutskever, K. Chen, G. Corrado, J. Dean, Distributed Representations of Words and Phrases and their Compositionality, 2013. https://doi.org/10.1162/jmlr.2003.3.4-5.951.

[78] Z. Yang, D. Yang, C. Dyer, X. He, A. Smola, E. Hovy, Hierarchical attention networks for document classification, in: Proc. 2016 Conf. North Am. Chapter Assoc. Comput. Linguist. Hum. Lang. Technol., 2016: pp. 1480–1489. https://doi.org/10.18653/v1/N16-1174.

[79] C. Gulcehre, S. Chandar, Y. Bengio, Memory Augmented Neural Networks with Wormhole Connections, (2017). http://arxiv.org/abs/1701.08718 (accessed June 16, 2020).

[80] A. Grover, J. Leskovec, node2vec: Scalable Feature Learning for Networks, in: Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., ACM Press, New York, New York, USA, 2016: pp. 855–864. https://doi.org/10.1145/2939672.2939754.

[81] M.J. Kusner, Y. Sun, N.I. Kolkin, K.Q. Weinberger, From Word Embeddings to Document Distances, in: Proc. 32nd Int. Conf. Mach. Learn., 2015: pp. 957–966. https://doi.org/10.1080/03019233.2016.1218198.

[82] W.L. Hamilton, J. Leskovec, D. Jurafsky, Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change, ArXiv Prepr. arXiv:1605 (2016). http://arxiv.org/abs/1605.09096.

[83] S. Deng, Y. Zhou, P. Zhang, A. Abbasi, Using discussion logic in analyzing online group discussions: A text mining approach, Inf. Manag. 56 (2019) 536–551. https://doi.org/10.1016/j.im.2018.09.013.

[84] I. Kim, G. Pant, Predicting web site audience demographics using content and design cues, Inf. Manag. 56 (2019) 718–730. https://doi.org/10.1016/j.im.2018.11.005.

[85] N. Kumar, D. Venugopal, L. Qiu, S. Kumar, Detecting Review Manipulation on Online Platforms with Hierarchical Supervised Learning, J. Manag. Inf. Syst. 35 (2018) 350–380. https://doi.org/10.1080/07421222.2018.1440758.

[86] S.M. Ho, J.T. Hancock, C. Booth, X. Liu, Computer-Mediated Deception: Strategies Revealed by Language-Action Cues in Spontaneous Communication, J. Manag. Inf. Syst. 33 (2016) 393–420. https://doi.org/10.1080/07421222.2016.1205924.

[87] Q. Le, T. Mikolov, Distributed representations of sentences and documents, in: 31st Int. Conf. Mach. Learn. ICML 2014, 2014.

[88] Y. Kim, Convolutional neural networks for sentence classification, in: EMNLP 2014 - 2014 Conf. Empir. Methods Nat. Lang. Process. Proc. Conf., 2014. https://doi.org/10.3115/v1/d14-1181.

[89] G.J. Stigler, The Optimum Enforcement of Laws, J. Polit. Econ. 78 (1970) 526–536. https://doi.org/10.1086/259646.

[90] E.R. DeLong, D.M. DeLong, D.L. Clarke-Pearson, Comparing the Areas under Two or More Correlated Receiver Operating Characteristic Curves: A Nonparametric Approach, Biometrics. 44 (1988) 837. https://doi.org/10.2307/2531595.

[91] Y. Bao, A. Datta, Simultaneously Discovering and Quantifying Risk Types from Textual Risk Disclosures, Manage. Sci. 60 (2014) 1371–1391. https://doi.org/10.1287/mnsc.2014.1930.

[92] N. Burns, S. Kedia, Executive option exercises and financial misreporting, J. Bank. Financ. 32 (2008) 845– 857. https://doi.org/10.1016/j.jbankfin.2007.06.004.

[93] CBS/AP, Equifax executives sold \$1.8 million in stock after breach, (2017). https://www.cbsnews.com/news/equifax-breach-executives-sold-1-8-million-in-stock/.

[94] A.R. Hevner, S.T. March, J. Park, S. Ram, Design Science in Information Systems Research, MIS Q. 28 (2004) 75–105. https://doi.org/10.2307/25148625.

[95] N. Berente, S. Seidel, H. Safadi, Research Commentary—Data-Driven Computationally Intensive Theory Development, Inf. Syst. Res. 30 (2019) 50–64. https://doi.org/10.1287/isre.2018.0774.

[96] J. Gaskin, N. Berente, K. Lyytinen, Y. Yoo, Toward Generalizable Sociomaterial Inquiry: A Computational Approach for Zooming In and Out of Sociomaterial Routines, MIS Q. 38 (2014) 849–871. https://doi.org/10.25300/MISQ/2014/38.3.10.

[97] J. Eaglesham, Accounting fraud targeted: With crisis-related enforcement ebbing, SEC is turning back to Main Street., Wall Str. J. (2013). https://www.wsj.com/articles/SB10001424127887324125504578509241215284044

[98] G.S. Becker, Crime and punishment: An economic approach, in: Econ. Dimens. Crime, Springer, 1968: pp. 13–68.

[99] I. Kim, D.J. Skinner, Measuring securities litigation risk, J. Account. Econ. 53 (2012) 290–310. https://doi.org/10.1016/J.JACCECO.2011.09.005.

## Authors’ Bios:

Rong Liu (rong.liu@stevens.edu) is Associate Professor of Information Systems in the school of business at Stevens Institute of Technology. Before joining Stevens, she was a Research Staff Member at IBM’s T. J. Watson Research Center. She received her Ph.D. in Business Administration from The Pennsylvania State University. Her research interests include machine learning, business analytics, and business process management.

Feng Mai (feng.mai@stevens.edu) is Assistant Professor of Information Systems in the School of Business at Stevens Institute of Technology. He received his Ph.D. from the University of Cincinnati. His research interests include social media, electronic commerce, and business analytics.

Zhe (Jay) Shan (jayshan@miamioh.edu) is Assistant Professor, Department of Information Systems and Analytics, Farmer School of Business, Miami University. He earned his Ph.D. in Business Administration and Operations Research from Penn State University Smeal College of Business in 2011. His research interests include FinTech innovation, information security management, patient-center healthcare, and business process analytics.

Ying Wu (ying.wu@stevens.edu) is Assistant Professor of Economics and Finance in the School of Business at Stevens Institute of Technology. She received her Ph.D. from Cornell University. Her research interests include asset pricing, international finance, and financial econometrics.
