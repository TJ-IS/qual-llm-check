---
otero_id: 14390
otero_key: "JQF7N3FX"
title: "Leveraging Financial Social Media Data for Corporate Fraud Detection"
authors: "Wei Dong; Shaoyi Liao; Zhongju Zhang"
year: "2018"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2018.1451954"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Leveraging Financial Social Media Data for Corporate Fraud Detection

Wei Dong, Shaoyi Liao & Zhongju Zhang

To cite this article: Wei Dong, Shaoyi Liao & Zhongju Zhang (2018) Leveraging Financial Social Media Data for Corporate Fraud Detection, Journal of Management Information Systems, 35:2, 461-487, DOI: 10.1080/07421222.2018.1451954

To link to this article: https://doi.org/10.1080/07421222.2018.1451954

![](/api/attachments/JQF7N3FX/fulltext/images/013b969964a6aaf4dd6238ed9315d8e786bc2fc3a3fa887546c8eb85558f0da2.jpg)

View supplementary material

![](/api/attachments/JQF7N3FX/fulltext/images/6c66e5e96547972d9014a8fda02eff21e94cd4d26a3abedd7df48cf2e35dfbc3.jpg)

Published online: 15 May 2018.

![](/api/attachments/JQF7N3FX/fulltext/images/4f6ac414b71b4eebdbc443e2979c29eeff2bb30c6de517b0c8e3b422cb63883c.jpg)

Submit your article to this journal

![](/api/attachments/JQF7N3FX/fulltext/images/11c5a29a1ff63f4454a0f2aae5d599d0c2bbe005b461de557f7bef1ba0d8b3d1.jpg)

Article views: 23

![](/api/attachments/JQF7N3FX/fulltext/images/7cff2185f28471659bd7da5816e3705dc675283f9ce6f326c51b4aa2d9aa885f.jpg)

View related articles

![](/api/attachments/JQF7N3FX/fulltext/images/3c8ed430bacc141d3ab18fe1ee33070a01f76cab6998c57aeffac6a80d6738c9.jpg)

View Crossmark data

# Leveraging Financial Social Media Data for Corporate Fraud Detection

WEI DONG, SHAOYI LIAO, AND ZHONGJU ZHANG

WEI DONG (weidong1@mail.ustc.edu.cn) is a Ph.D. candidate in management science and engineering at the School of Management, University of Science and Technology of China. He is in a joint doctoral program with City University of Hong Kong. His research interests include social media, text mining, and business intelligence. He has published in European Journal of Operational Research.

SHAOYI LIAO (issliao@cityu.edu.hk) is a professor in the Department of Information Systems, City University of Hong Kong. He obtained his Ph.D. in information systems from the Aix-Marseille University, France. His research is focused on artificial intelligence, business intelligence, and social media analytics. He has published in MIS Quarterly, INFORMS Journal on Computing, Decision Support Systems, and ACM Transactions on Management Information Systems, among others.

ZHONGJU ZHANG (Zhongju.Zhang@asu.edu; corresponding author) is codirector of the Actionable Analytics Lab and an associate professor of information systems at the W. P. Carey School of Business, Arizona State University. His research focuses on how information technology and data analytics impact consumer behavior and decision making, create business value, and transform business models. His work has appeared in the leading academic journals including Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Production and Operations Management, INFORMS Journal on Computing, and others. He has won numerous research and teaching awards.

ABSTRACT: Corporate fraud can lead to significant financial losses and cause immeasurable damage to investor confidence and the overall economy. Detection of such frauds is a time-consuming and challenging task. Traditionally, researchers have been relying on financial data and/or textual content from financial statements to detect corporate fraud. Guided by systemic functional linguistics (SFL) theory, we propose an analytic framework that taps into unstructured data from financial social media platforms to assess the risk of corporate fraud. We assemble a unique data set including 64 fraudulent firms and a matched sample of 64 nonfraudulent firms, as well as the social media data prior to the firm’s alleged fraud violation in Accounting and Auditing Enforcement Releases (AAERs). Our framework automatically extracts signals such as sentiment features, emotion features, topic features, lexical features, and social network features, which are then fed into machine learning classifiers for fraud detection. We evaluate and compare the performance of our algorithm against baseline approaches using only financial ratios and language-based features respectively. We further validate the robustness of our algorithm by detecting leaked information and rumors, testing the algorithm on a new data set, and conducting an applicability check. Our results demonstrate the value of financial social media data and serve as a proof of concept of using such data to complement traditional fraud detection methods.

KEY WORDS AND PHRASES: corporate fraud, financial social media, fraud detection, social media platform, systemic functional linguistics theory, text analytics.

Financial fraud is a serious commercial problem worldwide and has many different types, including corporate fraud, securities and commodities fraud, health-care fraud, financial institution fraud, mortgage fraud, and others [24]. Corporate fraud continues to be one of the FBI’s highest criminal priorities, and is defined as a “deliberate fraud committed by management that injures investors and creditors through misleading financial statements” [22, p. 28]. Even though the number of corporate fraud cases is relatively lower than that of other kinds of frauds, the financial losses associated with corporate fraud can be devastating once it happens. For example, the Enron scandal cost shareholders \$74 billion while the WorldCom fraud led to 30,000 lost jobs and \$180 billion in losses for investors. In addition to the tremendous financial losses, corporate fraud also has the potential to cause immeasurable damage to the overall economy and investor confidence. Therefore, corporate fraud risk assessment and detection before the U.S. Securities and Exchange Commission (SEC) disclosure have received significant attention from both practitioners and academic research.

Existing analytical procedures for corporate fraud investigation highly rely on auditing accountants and regulators, who analyze complex financial records and documents including financial statements. Financial statements, however, can be out of date upon release. They usually discuss a company’s past operations and performances for the previous quarter, if not earlier. While useful to identify fraudulent and nonfraudulent activities, data contained in a financial statement are often not appropriate to detect corporate fraud in a timely manner. According to Liou [40], approaches using financial statements often result in an average time lag of around three years from fraud inception to detection of the fraud. Additionally, financial statements may contain misleading and fictitious information; thus, further in-depth research is needed to assess the validity and risks of material misstatement in these documents [34].

In recent years, financial social media platforms for investment research have burgeoned. In addition to the fundamental research and broad in-depth coverage of various equities, these platforms allow registered users to participate in discussions, offer insights and alternative perspectives, and point out risks or flaws through an interactive forum/commentary mechanism. The user base of the platform is diverse. Besides investors, industry experts, and financial analysts, the platform also has a large readership including money managers, business leaders, journalists, bloggers, and the public. The opinions and views expressed in the analysis and discussions of these platforms have been shown to contain value-relevant information and have been used to predict future stock returns and earnings surprises [17]. Dyck et al. [21] also recognize the power of nontraditional players (such as employees, media outlets, and public investors) as whistleblowers about a potential violation of federal laws and regulations that has occurred, is ongoing, or is about to occur.

We believe the user-generated content (UGC) on financial social media platforms can be useful in assessing the potential risk of corporate fraud. Anecdotal evidence seems to support this idea. Take NQ Mobile (a Chinese mobile security company) as an example. Muddy Water Research (a market research and short-selling firm) released a harsh assessment citing “a massive fraud” of NQ Mobile on October 24, 2013. The news led to a 47 percent drop in the NQ stock price overnight. It is, however, worth noting that a Xueqiu (major Chinese social media platform for financial investors) user named “kankan123” had released a series of analysis reports questioning NQ Mobile’s fraud behavior at the beginning of 2013 (detailed information can be found at http://xueqiu.com/S/NQ/25820468), which is more than six months before the report from Muddy Water Research. An analytic framework that takes advantage of such UGC can thus help audit firms, government regulators, securities agencies, and investors to achieve their strategic goals by providing an early and effective fraud detection algorithm to protect public interests. These stakeholders can leverage the framework to better estimate the fraud risk associated with each target firm so as to make informed decisions, such as minimizing exposure to fraudulent firms and determining how to allocate resources to investigate target firms.

In this study, we seek to examine how to extract useful features from UGC on social media platforms and develop a text analytic framework to automatically detect corporate fraud. Our framework is grounded in systemic functional linguistics (SFL) theory [29], which provides foundations for our feature sets such as sentiment features, emotion features, topic features, lexical weights features, and social network features. We evaluate the performance of our algorithm using data from two platforms: SeekingAlpha and Yahoo Finance. Our extensive analyses demonstrate the efficacy of our algorithm as well as the leading effects of social media content on early corporate fraud detection. Additionally, we validate the practical contributions and implications of our algorithm by conducting an applicability check with four focus groups (each with three domain knowledge experts). The applicability check shows that major stakeholders in the financial industry feel that our approach is a helpful auxiliary tool, providing further evidence of the value of our framework. To the best of our knowledge, this is one of the first studies to use textual data from social media platforms for corporate fraud detection.

## Literature Review

Financial fraud and fraud detection has been an important topic in both the accounting and the finance literature. It is relatively understudied in the information systems literature. Here, we review existing literature about different types of financial fraud and the various methods that have been proposed to detect it. We highlight what might be missing and what we can add to further improve the existing methods.

Financial fraud can happen at both the firm and community levels. Communitylevel fraud usually involves a focal firm as well as external parties (such as customers and/or clients) related to the firm [54]. At the firm level, Ngai et al. [49] provided a detailed literature review on detecting financial fraud via data mining methods. Among different types of financial fraud, corporate fraud consists of activities undertaken by an individual (usually top management) to deliberately mislead investors, creditors, and the public so as to gain an unfair advantage. When facing market-driven pressures due to predicament or asset misappropriation because of personal affairs, firm managers tend to “overstate assets, sales and profit, or understate liabilities, expenses or losses” [69, p. 5519] and disclose unreal growth opportunities in financial statements. With these conceited misrepresentations, Wall Street analysts and public investors will raise their expectations and earnings projections about this company. Likewise, in order to meet the new expectations and projections of the market, the management will have to make another misleading financial statement for the next quarter or fiscal year. This cycle constitutes the business process map of corporate fraud.

In order to improve financial reporting, the American Institute of Certified Public Accountants has established standard accounting principles. To fight corporate fraud, several auditing guidelines have been issued that auditors need to consider in identifying the risk of material misstatement in financial statements. Typically, financial statements for a business include income statements, balance sheets, statement of retained earnings, and cash flows. These contents can be broadly classified into structured (e.g., numeric financial variable and ratios, quantitative descriptions of operating conditions) and unstructured data (e.g., management discussion and analysis). Table 1 presents a sample of representative studies that use structured and unstructured data for corporate fraud detection. These studies are conventional fraud detection methods that tap into only traditional data sources such as financial statements and earnings conference calls.

From a methodology perspective, conventional auditing practices rely primarily on statistical analysis of structured financial data [15]. Kaminski et al. [34], however, argued that financial ratios provide limited ability to detect fraud because management can create fictitious numbers. Hence some researchers, for example, Brazel et al. [10], examined the effectiveness of nonfinancial variables on the risk of corporate fraud. With the development of natural language processing (NLP) techniques, researchers have begun to glean the textual contents and signals from financial statements and examine whether they can provide additional sources of information to predict fraud. Table 2 summarizes a list of studies that seek to detect fraud using text mining techniques (either a rule-based dictionary approach or statistical approach) [38]. Most of the studies in Table 2 used the management discussion and analysis (MD&A) section of financial reports, which is usually well-written by a firm’s management team in formal business language.

Table 1. Representative Studies of Corporate Fraud Detection and Data Sources

<table><tr><td>Data type</td><td>Indicators</td><td>Literature</td><td>Data source</td></tr><tr><td rowspan="3">Structured data</td><td>Numerical financial variables</td><td>Cecchini et al. [15]</td><td>Financial statements</td></tr><tr><td>Financial ratios</td><td>Summers and Sweeney [64]; Dechow et al. [19]; Abbasi et al. [1]</td><td>Financial statements</td></tr><tr><td>Nonfinancial variables</td><td>Brazel et al. [10]</td><td>Financial statements</td></tr><tr><td rowspan="4">Unstructured data</td><td rowspan="2">Features from language-based textual content</td><td>Larcker and Zakolyukina [36]</td><td>Earnings conference calls</td></tr><tr><td>Purda and Skillicorn [55]</td><td>MD&amp;A section from financial statements</td></tr><tr><td>Features from vocal speech</td><td>Hobson et al. [30]</td><td>Earnings conference calls</td></tr><tr><td>Social media features</td><td>Current study</td><td>Financial social media platform, for example, SeekingAlpha</td></tr></table>

Table 2. Text-based Methods of Corporate Fraud Detection

<table><tr><td>Technique</td><td>Literature</td><td>Source of text</td></tr><tr><td rowspan="3">Dictionary-based method</td><td>Purda and Skillicorn [55]</td><td>MD&amp;A section from both annual and quarterly reports</td></tr><tr><td>Larcker and Zakolyukina [36]</td><td>Earnings conference calls</td></tr><tr><td>Humpherys et al. [31]</td><td>MD&amp;A section of the 10-K report</td></tr><tr><td rowspan="2">Statistical method</td><td>Cecchini et al. [16]; Glancy and Yadav [26]; Moffitt et al. [47]</td><td>MD&amp;A section of the 10-K report</td></tr><tr><td>Goel and Gangolly [27]; Goel et al. [28]</td><td>The entire text of the 10-K report</td></tr></table>

Additionally, the MD&A section has a fairly rigid content structure, such as discussion of financial conditions, results of operations, and forward-looking statements for the company.

Data sources such as financial statements and earnings conference calls are usually well-planned and prepared in advance. Liou [40] found that detection methods using financial statements tend to result in a time lag from fraud inception to detection. More importantly, financial statements and earnings conference calls do not capture opinions and insights from other stakeholders such as public investors and analysts. Dyck et al. [21] and Cecchini et al. [16] argued the potential strategic value of using this new source of information—user-generated content from employees, media outlets, and public investors—to predict corporate fraud. Financial social media platforms such as SeekingAlpha are natural venues that aggregate such user-generated content online, and thus merit further study to examine their impacts on corporate fraud detection. It should be noted that the process of analyzing unstructured textual data from financial social media platforms is drastically different from that using only the structured data and/or the MD&A section from financial statements. Dictionary-based text analysis methods would also not be appropriate here since the contributors of this social media content are not the management team of a firm. It is therefore difficult to construct a context-aware dictionary.

## Theoretical Foundation for Social Media-Based Corporate Fraud Detection

To capture the salient features from UGC and to understand how users on social media platforms use language to express their opinions about a company’s operations and performances, we refer to systemic functional linguistics (SFL) theory [29, p. 15]. SFL argues that language is a system of choices/options that writers use to achieve certain goals. The meaning of a text is dependent on those choices within a language system [65]. The term “systemic” views language as “a network of systems or interrelated sets of options for making meaning.” The term “functional” indicates that the approach is concerned with contextualized and practical uses.

SFL theory includes three interrelated functions: ideational, interpersonal, and textual. Ideational function states that language is about construing ideas [29]. Interpersonal function refers to language as a medium for interaction, and it is the means for creating and maintaining our interpersonal relations. These two functions are interlinked via the textual function, which determines how information is organized and presented to create a coherent flow of discourse. In other words, ideational and textual functions focus on the content of messages, while interpersonal function deals with interaction structures.

## Ideational Function

The ideational function can be represented by topics, opinions, and emotions [2]. Textual documents usually exhibit multiple topics [8]. Brown et al. [11] found that these thematic topics are informative in predicting intentional financial statement misreporting. We believe that topics discussed in the social media data of a fraudulent firm can differ from those of a legitimate firm and are thus useful in classifying firms. We adopt latent Dirichlet allocation (LDA) [8], a widely used topic model, to extract thematic topics from social media data. Opinions are sentiment polarities (e.g., positive, neutral, and negative) about a particular entity [52]. According to Buller and Burgoon [13], deceivers (e.g., fraudulent firms) tend to engage in more strategic activity (information, behavior and image management) designed to project a positive image. We adopt the sentiment words dictionary in the financial domain created by Loughran and

McDonald [41] to measure sentimental opinions expressed by users on financial social media platforms. Emotions consist of various affects such as happiness, sadness, horror, and anger [2]. Newman et al. [48] found that linguistic styles (such as hate, sadness, anger) can predict deception. In this study, we use the emotional categories defined in the Linguistic Inquiry and Word Count dictionary [53] to measure “assent,” “anxiety,” “anger,” “swear,” and “sadness” emotions [36].

Additionally, according to cognitive theory, cognitive appraisal is a component of emotion [37]. Cognitive appraisal in the context of corporate fraud refers to how an individual views a firm’s operations condition. We measure cognitive appraisal by (1) overall description of the fraudulent situation; (2) detailed analysis of the fraudulent behavior; and (3) legal judgments and sanctions. Three separate word lists are developed to capture each of the above three components. The synonyms of fraud word list contains 120 words that are widely used in the Accounting and Auditing Enforcement Releases (AAERs), such as “phony,” “fake,” “sham,” and “deceptive.” The fraudulent behavior word list contains 136 words such as “mislead,” “conceal,” “fabricate,” and “detect.” The legal judgment word list contains 32 words such as “jurisdiction,” “crime,” “forfeiture,” and “sanction.” Table 3 summarizes the opinion and emotional features as well as their measurements.

Table 3. Measures of Opinions and Emotion Related Features

<table><tr><td>Type</td><td>Feature</td><td>Measurement</td></tr><tr><td rowspan="2">Opinions</td><td>Ratio of positive sentiment</td><td>Total number of positive words divided by total number of words*</td></tr><tr><td>Ratio of negative sentiment</td><td>Total number of negative words divided by total number of words</td></tr><tr><td rowspan="8">Emotions</td><td>Ratio of assent words</td><td>Total number of assent words divided by total number of words</td></tr><tr><td>Ratio of anxiety words</td><td>Total number of anxiety words divided by total number of words</td></tr><tr><td>Ratio of anger words</td><td>Total number of anger words divided by total number of words</td></tr><tr><td>Ratio of swear words</td><td>Total number of swear words divided by total number of words</td></tr><tr><td>Ratio of sadness words</td><td>Total number of sadness words divided by total number of words</td></tr><tr><td>Ratio of fraud synonyms words</td><td>Total number of synonyms of fraud divided by total number of words</td></tr><tr><td>Ratio of fraud analysis words</td><td>Total number of fraud analysis words divided by total number of words</td></tr><tr><td>Ratio of legal judgments words</td><td>Total number of legal judgments words divided by total number of words</td></tr><tr><td colspan="3">*Total number of words is the number of words ignoring stop words.</td></tr></table>

## Textual Function

The major element of the textual function is thematic structure. It shows the progression of what is going on and carries the writer’s ideology, which to tells people what the writer is really concerned about in his mind [29]. Textual function can be conceptualized into three information types: writing styles, genres, and vernaculars [2, 5]. Writing styles and vernaculars are not applicable in our context since users on social media platforms do not follow a unified writing style and user vernaculars.

Genres in a document represent how writers typically use language to respond to recurring situations [32]. Merkl-Davies and Brennan [45] found that corporate narratives can be regarded as an identifiable genre for business communication with distinctive linguistic properties. Genres can be distinguished by genre analysis using word frequencies based on corpus linguistics [60]. We adopt a modified word frequency, term frequency-inverse document frequency (TF-IDF) [58], for genre classification. TF-IDF assumes that only terms with a high term frequency in a given document but a low document frequency in the whole collection of documents are important in classifying documents. TF-IDF scheme represents a collection of documents by document-term vectors, of which each element is the weight of a term in a document.

## Interpersonal Function

Interpersonal function refers to the fact that “language is a medium of exchange between people” [2, 61, p. 75]. It is generally represented by social interaction/ structure that can be built through the reply-to relationships between messages [25]. Abbasi and Chen[2] found that employees’ social network structure presented in inner-firm e-mails changed after the Enron fraud. Pak and Zhou [51] provided new evidence that deception is a strategic activity where the deceiver juggles between the dual goals of promoting deceptive ideas and avoiding detection. They found that social structural characteristics can be used to delineate deception in computermediated communication. Numbers of messages, posts, and/or comments have been used to capture social structure in UGC [3, 4]. In this study, we track the number of Analysis reports (AR), the number of Breaking news (BN), and the number of StockTalk messages (SM) as well as the number of comments to those contents for each firm. In addition, we consider the number of distinctive authors who post AR and SM and the number of posts per author. Finally we track the number of users who follow the news related to a firm. Table 4 summarizes the measures of the features related to interpersonal function.

Based on the above discussions, in Figure 1, we propose a text analytic framework to predict corporate fraud using financial social media data. Since the dimensionality of the TF-IDF term weights vector is often huge, we employ a dimension reduction technique (principal component analysis) for the TF-IDF feature selection. Reduced dimension of TF-IDF features lowers the training time of classifiers and avoids potential overfitting problems. We use support vector machine (SVM) for document classification. SVM has been shown to be successful in working with large feature space and small sample set [16], and is capable of handling large sparse data [33]. For comparison purposes, we also implement logistic regression (LR), neural networks (NN), and decision tree (DT) in this study. We use accuracy, recall, F1 score, and the area under the receiver operating characteristic (ROC) curve (AUC), which are standard information retrieval metrics [43], to mathematically evaluate the quality of trained classifiers. A tenfold cross-validation technique is employed to assess how the model results generalize to independent test data.

Table 4. Measures of Interpersonal Function-Related Features

<table><tr><td>Type</td><td>Feature and measurement</td><td>No. of features</td></tr><tr><td rowspan="5">Social interaction structure</td><td>Number of Analysis reports (AR), Breaking news (BN), or StockTalk messages (SM)</td><td>3</td></tr><tr><td>Number of comments to AR, BN, or SM</td><td>3</td></tr><tr><td>Numbers of distinctive authors for AR, or SM</td><td>2</td></tr><tr><td>Numbers of AR or SM per author</td><td>2</td></tr><tr><td>Number of followers</td><td>1</td></tr></table>

![](/api/attachments/JQF7N3FX/fulltext/images/38c382c27eeacebe327b6b64be75a07200bdfc9bf4890f34270ab15d5042c2bd.jpg)  
Figure 1. An SFL-Based Framework for Corporate Fraud Detection

## Data Collection

Our data came from a few sources. We selected SeekingAlpha (http://seekingalpha. com) as the source to collect financial social media data. SeekingAlpha is a crowdsourced content service platform for investment research, with broad coverage of stocks, asset classes, exchange traded funds (ETFs), and investment strategy. Since its inception in early 2004, SeekingAlpha has grown to be the top destination for stock market opinion and analysis on the Internet with 4 million registered users. Additionally, in contrast to other equity research platforms, insights on SeekingAlpha are provided by investors and industry experts from the buy-side rather than the sell-side [17]. Off-topic discussions are moderated by the 24-hour inhouse moderation team at SeekingAlpha: posts on the bulletin boards are categorized by a ticker symbol, and only topic-related posts can be published due to the site’s “optional post” feature. For each firm, there are five types of information content: Analysis reports, Breaking news, Earning call transcripts, StockTalk, and Videos. Analysis reports are created by analysts and platform contributors; Breaking news are created by SeekingAlpha editors, thus can be considered trustworthy [62]; Earning call transcripts come from the firm’s conference call each quarter; StockTalk is organized as discussion forums; Videos are short video clips discussing the focal firm.

We crawled all the contents (including all comments) under the Analysis reports, Breaking news, and StockTalk sections, together with the social network structures for each firm in our sample. Since a fraudulent firm may be disclosed as committing financial fraud in several announcements of the SEC at different times, we considered only the time of the first announcement and extracted only social media data prior to that point. Note that not all fraudulent firms have data on SeekingAlpha prior to their fraud disclosure time. As shown in Figure 2(a), SeekingAlpha had not been established at the time when the firm’s fraudulent behavior was disclosed.

![](/api/attachments/JQF7N3FX/fulltext/images/f119a9e81ffba900a98f509609dbbb175ca6f3ba7d575d735f84aa48a0cb5cf8.jpg)

(a) Fraudulent behavior is disclosed before the establishment of SeekingAlpha  
![](/api/attachments/JQF7N3FX/fulltext/images/1145474f4070cc651de12477795a83ed74cf95526ccb1bffe472e660de424c29.jpg)  
(b) Fraudulent behavior is disclosed after the establishment of SeekingAlpha  
Figure 2. Timeline of Fraud Period and Establishment of SeekingAlpha

Hence, we did not include firms whose fraudulent behavior is disclosed before the establishment of SeekingAlpha.

In addition to the social media data, we also collected the financial ratios and the textual contents of the MD&A section from the annual financial statements of the firm. These data are used to compare the performance of our algorithm against baseline methods. Based on the literature, financial ratios in the first year of the fraudulent time period (called the first fraud year) for a fraudulent firm are always selected to represent the firm’s operation performance [7, 20]. The financial ratios of the first fraud year for a firm are selected from a database of global public companies called Compustat. The financial statements of the first fraud year are obtained from the SEC’s official company file system—the EDGAR database.

## Sample Selection

We used public traded companies in the U.S. stock market to test the performance of the proposed approach. First, all fraudulent public firms were identified and labeled. We used AAERs to screen companies that are involved in financial frauds. The SEC has been issuing AAERs since 1982 to investigate a company or other related parties for alleged accounting misconducts. These releases provide varying degrees of details about the nature of the accounting and/or auditing misconduct in financial statements. Dechow et al. [19] developed a comprehensive database containing 936 firms (and the misstatement events that affect at least one of the firms’ quarterly or annual financial statements from May 17, 1982, to October 19, 2013) after a thorough analysis of 3,490 AAERs.

We discarded the firms with only quarterly misstatement events because quarterly statements are unaudited [10]. This resulted in 804 companies with annual fraudulent events. Among these, 38 of the firms were accused of wrongdoing that is unrelated to financial misstatements, such as auditor issues, bribes or disclosure-related issues, and others [19]. We removed those 38 firms from our sample. For each of the remaining 766 companies, we tried to find the SIC (Standard Industry Classification) code from the EDGAR database and the stock symbol from the Compustat database. The SIC code is used to check whether a company is a financial firm, such as banks, insurance companies, and CPA firms, for which the SIC ranges from 6000 to 6999. The stock symbol is the unique identifier we used to extract social media data for the company from SeekingAlpha. Companies that cannot be found in these two databases and SeekingAlpha are dropped.

Following previous research, we also excluded financial firms whose SICs start with number 6 [6]. On one hand, the SEC’s industry guidelines require specific disclosures for financial companies such as real estate partnerships, property and casualty insurance, and bank holding companies [55]. Additionally, accounting rules, asset valuations, and other characteristics for financial companies are different from those for other types of companies [23]. Finally, we discarded 22 companies whose financial data was missing during the fraud period in the Compustat database, and 29 firms whose fraudulent behavior was disclosed before the establishment of SeekingAlpha. We also dropped another 56 fraudulent firms that lacked sufficient social media data (less than 500 words excluding stop words) during the period from the establishment of SeekingAlpha to the first disclosure time. Table 5 details our sample selection process.

Table 5. Sample Selection Process

<table><tr><td>Distinct companies</td><td>Number</td></tr><tr><td>Companies with accounting misconducts in Dechow et al. [19] data set</td><td>936</td></tr><tr><td>Less: companies with only quarterly fraudulent events</td><td>132</td></tr><tr><td>Subtotal (companies with annual fraudulent events)</td><td>804</td></tr><tr><td>Less: companies with auditor, bribes, disclosure, no dates, and other issues</td><td>38</td></tr><tr><td>Subtotal (companies with annual corporate fraud)</td><td>766</td></tr><tr><td>Less: Companies that cannot be found in SEC EDGAR database</td><td>111</td></tr><tr><td>Less: Companies that cannot be found in Compustat database</td><td>38</td></tr><tr><td>Less: Companies that cannot be found in SeekingAlpha</td><td>343</td></tr><tr><td>Less: Financial companies: Banks &amp; Insurance (SIC 6000-6999)</td><td>103</td></tr><tr><td>Less: Companies&#x27; financial data in fraud years cannot be found in Compustat database</td><td>22</td></tr><tr><td>Less: Companies that are disclosed before the establishment of SeekingAlpha</td><td>29</td></tr><tr><td>Less: Companies that do not have enough social media data</td><td>56</td></tr><tr><td>Total</td><td>64</td></tr></table>

We matched each fraudulent firm with a control firm (nonfraudulent) for classification purposes [64]. This is an oversampling strategy, which is appropriate for handling rare events [3]. Random sampling in this case would result in an extremely high percentage of nonfraudulent firms in the sample, thus making attempts to investigate significant features for predicting corporate fraud not meaningful. Nonfraudulent firms are selected based on two criteria. First, we tried to find a direct match by using the Compustat database on the basis of the fraud year, firm size, and industry; see Dong et al. [20] for detailed descriptions of the matching process. Additionally, each nonfraudulent firm should have enough textual data (at least 500 words excluding stop words) on SeekingAlpha. If many firms meet the selection criteria, one of them will be randomly chosen. The above sampling strategy leads to a 1:1 ratio for fraudulent and nonfraudulent firms. For a robustness check, we also examined the case when the sample is not balanced—that is, the ratio of fraudulent and nonfraudulent firms is not 1:1. Note that social media data for nonfraudulent firms are collected up to August 31, 2015, when this study started. In summary, our final data set includes 64 fraudulent firms together with a corresponding 64 matched nonfraudulent firms.

## Data Preprocessing

For textual social media and MD&A content, we used the Stanford CoreNLP toolkit [44] to implement sentence segmentation and word tokenization. Punctuation marks, hyperlinks, numerical digits, and special symbols are removed after tokenization. Furthermore, we removed the stop words developed for the financial industry by

Table 6. Description of the Data Set

<table><tr><td>Dataset (128 firms)</td><td>No. of Analysis reports</td><td>No. of Breaking news</td><td>No. of StockTalk messages</td><td>No. of sentences</td><td>No. of words</td><td>No. of financial ratios</td></tr><tr><td>Social media data</td><td>3,981(31.10)</td><td>2,251(17.59)</td><td>1,672(13.06)</td><td>184,356(1,440.28)</td><td>2,613,362(20,416.89)</td><td>—</td></tr><tr><td>MD&amp;A data</td><td>—</td><td>—</td><td>—</td><td>92,712(724.31)</td><td>902,940(7,054.22)</td><td>—</td></tr><tr><td>Financial ratios</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>84</td></tr></table>

Loughran and McDonald [41]. Words that appear only once in the entire corpus were also dropped in this study [66] because rare words are usually noninformative and most likely to be just noise [68]. The last important step in data preprocessing is stemming. Stemming refers to reducing a word to its base, which helps to discern the importance of specific words within the text. We adopted Wordnet Stemmer [46] in this study. Wordnet Stemmer keeps the morphology of a word form, such as nouns, adjectives, adverbs, and verbs. It also better retains the stem of a word; for example, the word “sharper” (instead of “sharp”), which could mean a fraud, will be retained by Wordnet Stemmer.

For financial ratios, we adopted a rich set of 84 yearly financial ratios (see Table 2 in the online Appendix). This feature set includes 12 annual financial ratios, 24 industry-collaboration contextual features, 24 industry-competition contextual features, and 24 organization contextual features. Among the 12 annual financial ratios (R1 to R12), seven of them, AQI, DSIR, DEPI, GMI, LEV, SG, and SGEE, come from Beneish [7] who discussed in detail why these ratios are related to financial fraud. The equation of CFED is derived from Dechow [18]. The other financial ratios are obtained from Abbasi et al. [1]. The industry and organization contextual features are generated based on year-to-year changes of accounting items retrieved from the Compustat database. If there are missing data or zero denominator during the computation, we used the techniques introduced in Beneish [7].

Table 6 describes the summary statistics of our data set; the numbers in parentheses are the average value.

## Analysis and Evaluation

We perform comprehensive analysis to systematically evaluate the efficacy of our proposed algorithm. As discussed earlier, four classifiers (SVM, NN, DT, and LR) are used to predict corporate fraud. We iteratively include each of the three categories of input features (financial ratio, MD&A, social media data) to evaluate their effects on fraud detection. To further evaluate robustness, we test the predictive power of our model on a separate holdout sample as well as using data from another financial social media platform Yahoo Finance.

## Fraud Detection Using Only Social Media Data

The input variables here are the features (discussed in the Theoretical Foundation Section) extracted from social media data. There are 2 sentiment features, 8 emotion features, and 11 social network features. Principal component analysis yields 127 lexical features. Following the topic model by Blei et al. [8], we compute the perplexity scores for different number of topics ranging from 20 to 1,000. In the end, the 100 topic feature model (with a minimum perplexity value of 1,239.77) is selected. Statistical descriptions for sentiment, emotion, and social network features are shown in Table 1 of the online Appendix.

Table 7 reports the average classification performance of the four classifiers. It can be seen that the SVM model achieves the best testing performance among all classifiers. By contrast, the LR model obtains the worst performance. Using priordisclosure information from SeekingAlpha, we can predict fraud with 75.50 percent accuracy in the test data set. Since all the social media data are prior to the first fraud disclosure time point, we can develop a fraud detection warning system by closely monitoring and extracting useful features from the social media platform, thus reducing the time lag between financial misstatements and fraud disclosure.

Using the SVM model with the best performance, we investigate each set of social media features independently. Average performances of the model with only social network features, topic features, sentiment and emotion features, and lexical features are shown in Figure 3. We find that topic features are most predicative of fraud. Comparing social network and lexical features, we note that lexical features are helpful in the training data while social network features do better in the testing data. Classification abilities of sentiment and emotion features are not as good as the other features in both the training and testing data.

The results of our model using the SVM classifier on imbalanced data with different ratios are presented in Figure 4. We note that as the ratio of fraudulent to

Table 7. Performance of Classification Using Only Social Media Features

<table><tr><td colspan="2"></td><td>Average accuracy</td><td>Average recall</td><td>Average F1 score</td><td>Average AUC</td></tr><tr><td rowspan="2">SVM</td><td>Training</td><td>99.66</td><td>99.50</td><td>99.66</td><td>99.94</td></tr><tr><td>Testing</td><td>75.50</td><td>81.56</td><td>76.50</td><td>86.32</td></tr><tr><td rowspan="2">NN</td><td>Training</td><td>100.00</td><td>100.00</td><td>100.00</td><td>98.26</td></tr><tr><td>Testing</td><td>63.17</td><td>68.05</td><td>62.18</td><td>53.71</td></tr><tr><td rowspan="2">DT</td><td>Training</td><td>98.52</td><td>98.30</td><td>98.52</td><td>96.44</td></tr><tr><td>Testing</td><td>63.10</td><td>66.54</td><td>64.93</td><td>43.34</td></tr><tr><td rowspan="2">LR</td><td>Training</td><td>50.27</td><td>87.04</td><td>59.96</td><td>46.42</td></tr><tr><td>Testing</td><td>54.50</td><td>87.75</td><td>60.98</td><td>43.70</td></tr></table>

![](/api/attachments/JQF7N3FX/fulltext/images/c648efeb3df22b0a78b964e2ed00793d45b57b75e6f46a5fa824075f08a88cba.jpg)  
Figure 3. Performance of Classification Using Each Set of Social Media Features

![](/api/attachments/JQF7N3FX/fulltext/images/85cad27f345523d7a7c970d06a740f27e08f4a83f4d8196cb4f59afaaa1e1be5.jpg)  
Figure 4. Performance of SVM on Imbalanced Data

nonfraudulent firms decreases, the recalls and AUCs decrease slightly while the accuracy of the model increases. F1 scores, however, drop significantly as the data set becomes more imbalanced. The reason is that more nonfraudulent firms in the sample will train the classifier to classify firms as nonfraudulent as much as possible to increase classification accuracy. In other words, the ability for the classifier to detect fraud becomes low, which results in low values of recall and precision. Hence, the F1 score, which is the combination of recall and precision, drops quickly. The overall performances of the model on the imbalanced data set still look good.

## Comparison with Baseline Methods

In this section, we compare the performance of our model against methods using only structured financial ratios and language-based features from textual MD&A contents.

## Baseline Method Using Only Financial Ratios

Table 8 documents the average performances of the four classifiers using only financial ratio data. Again, the SVM model achieves the best performance. The average testing accuracy, however, is only 56.17 percent, much lower than the model performance using the social media data. Note that the baseline model performance is lower than that of Abbasi et al. [1] using the same financial ratios. This may have to do with treatment of missing values in the data sample.

The performance of the baseline method using financial ratios supports the findings by Kaminski et al. [34] and Dechow et al. [19] that a firm’s financial numbers do not change dramatically between the fraudulent periods and the surrounding truthful years. Thus financial ratios of first fraud year would not be good indicators for discerning fraudulent or nonfraudulent cases. On the contrary, Purda and Skillicorn [55] found that word choice may raise red flags from truthful years to fraudulent periods. This explains why classification performances using features from social media data in the previous section are much better than the results using only financial ratios.

Table 8. Performance of Baseline Method Using Only Financial Ratios

<table><tr><td colspan="2"></td><td>Average accuracy</td><td>Average recall</td><td>Average F1 score</td><td>Average AUC</td></tr><tr><td rowspan="2">SVM</td><td>Training</td><td>99.39</td><td>98.77</td><td>99.37</td><td>99.96</td></tr><tr><td>Testing</td><td>56.17</td><td>77.74</td><td>63.37</td><td>49.29</td></tr><tr><td rowspan="2">NN</td><td>Training</td><td>76.58</td><td>69.60</td><td>74.72</td><td>73.09</td></tr><tr><td>Testing</td><td>48.83</td><td>42.39</td><td>43.71</td><td>41.75</td></tr><tr><td rowspan="2">DT</td><td>Training</td><td>97.41</td><td>96.75</td><td>97.37</td><td>95.34</td></tr><tr><td>Testing</td><td>41.17</td><td>42.08</td><td>40.09</td><td>36.02</td></tr><tr><td rowspan="2">LR</td><td>Training</td><td>54.69</td><td>60.31</td><td>56.88</td><td>51.94</td></tr><tr><td>Testing</td><td>54.67</td><td>60.00</td><td>54.54</td><td>43.58</td></tr></table>

## Baseline Method Using Only Language-Based Features in MD&A

We replicate the procedure by Purda and Skillicorn [55] to analyze the MD&A section of firms’ financial statements. The most common 1,100 words are used. The fraction of in-bag observations is set to 75 percent. A random forest of 3,000 trees is created based on these in-bag documents and tested on another 25 percent out-bag documents. The top 200 words most predictive of fraud are found and used as language-based input features for classification. Performances of the four classifiers are presented in Table 9.

Here, the LR model achieves the best performance in terms of average accuracy (70.33 percent), recall (71.90 percent), and F1 score (70.10 percent) while SVM has the highest average AUC (69.82 percent). Comparing the numbers in Table 7, Table 8, and Table 9, we demonstrate that our proposed algorithm using social media features outperforms the baseline methods using financial ratios and language-based features. We also note that the performance of the model using language-based features from the MD&A sections is better than that of the method using financial ratios.

## Incremental Effect of Combined Feature Sets

To test the incremental effect of each category of data, we gradually add languagebased features and then social media features into financial ratios. The classification performance using three types of feature sets—(1) only financial ratios, (2) a combination of financial ratios and language-based features, and (3) a full combination of financial ratios, language-based features, and social features—are investigated. The performances of the four classifiers using these three types of feature sets are recorded in Tables 10–13.

Considering the performances of the SVM classifier in Table 10, it is clear that the performance of the combined financial ratios and language-based features is better than that using only financial ratios. Moreover, the performance of the fully combined feature set is better than that using the combination of financial ratios

Table 9. Performance of Baseline Method Using Only Language-based Features from MD&A Contents

<table><tr><td colspan="2"></td><td>Average accuracy</td><td>Average recall</td><td>Average F1 score</td><td>Average AUC</td></tr><tr><td rowspan="2">SVM</td><td>Training</td><td>97.29</td><td>97.01</td><td>97.28</td><td>99.50</td></tr><tr><td>Testing</td><td>66.67</td><td>66.02</td><td>64.25</td><td>69.82</td></tr><tr><td rowspan="2">NN</td><td>Training</td><td>100.00</td><td>100.00</td><td>100.00</td><td>98.26</td></tr><tr><td>Testing</td><td>66.33</td><td>62.19</td><td>64.69</td><td>52.09</td></tr><tr><td rowspan="2">DT</td><td>Training</td><td>99.14</td><td>98.81</td><td>99.10</td><td>97.57</td></tr><tr><td>Testing</td><td>52.78</td><td>50.83</td><td>54.98</td><td>54.14</td></tr><tr><td rowspan="2">LR</td><td>Training</td><td>100.00</td><td>100.00</td><td>100.00</td><td>98.26</td></tr><tr><td>Testing</td><td>70.33</td><td>71.90</td><td>70.10</td><td>58.96</td></tr></table>

Table 10. Performance of SVM Classifier Using Combined Features

<table><tr><td>SVM</td><td></td><td>Average accuracy</td><td>Average recall</td><td>Average F1 score</td><td>Average AUC</td></tr><tr><td rowspan="2">Financial ratios</td><td>Training</td><td>99.39</td><td>98.77</td><td>99.37</td><td>99.96</td></tr><tr><td>Testing</td><td>56.17</td><td>77.74</td><td>63.37</td><td>49.29</td></tr><tr><td rowspan="2">Financial ratios and language-based features</td><td>Training</td><td>98.71</td><td>98.60</td><td>98.72</td><td>99.83</td></tr><tr><td>Testing</td><td>70.83</td><td>68.54</td><td>69.31</td><td>71.78</td></tr><tr><td rowspan="2">Fully combination of features</td><td>Training</td><td>100.00</td><td>100.00</td><td>100.00</td><td>100.00</td></tr><tr><td>Testing</td><td>80.00</td><td>83.04</td><td>79.80</td><td>85.03</td></tr></table>

Table 11. Performance of NN Classifier Using Combined Features

<table><tr><td>NN</td><td></td><td>Average accuracy</td><td>Average recall</td><td>Average F1 score</td><td>Average AUC</td></tr><tr><td rowspan="2">Financial ratios</td><td>Training</td><td>76.58</td><td>69.60</td><td>74.72</td><td>73.09</td></tr><tr><td>Testing</td><td>48.83</td><td>42.39</td><td>43.71</td><td>41.75</td></tr><tr><td rowspan="2">Financial ratios and language-based features</td><td>Training</td><td>100.00</td><td>100.00</td><td>100.00</td><td>98.26</td></tr><tr><td>Testing</td><td>62.33</td><td>69.48</td><td>63.91</td><td>50.75</td></tr><tr><td rowspan="2">Fully combination of features</td><td>Training</td><td>100.00</td><td>100.00</td><td>100.00</td><td>98.26</td></tr><tr><td>Testing</td><td>66.17</td><td>79.96</td><td>69.80</td><td>55.07</td></tr></table>

Table 12. Performance of DT Classifier Using Combined Features

<table><tr><td>DT</td><td></td><td>Average accuracy</td><td>Average recall</td><td>Average F1 score</td><td>Average AUC</td></tr><tr><td rowspan="2">Financial ratios</td><td>Training</td><td>97.41</td><td>96.75</td><td>97.37</td><td>95.34</td></tr><tr><td>Testing</td><td>41.17</td><td>42.08</td><td>40.09</td><td>36.02</td></tr><tr><td rowspan="2">Financial ratios and language-based features</td><td>Training</td><td>97.99</td><td>98.60</td><td>98.03</td><td>96.33</td></tr><tr><td>Testing</td><td>52.78</td><td>52.92</td><td>46.88</td><td>47.25</td></tr><tr><td rowspan="2">Full combination of features</td><td>Training</td><td>98.28</td><td>99.29</td><td>98.36</td><td>96.67</td></tr><tr><td>Testing</td><td>52.38</td><td>49.18</td><td>45.58</td><td>39.35</td></tr></table>

and language-based features. Performance is improved when more features are added. The same can be said of the NN model. This result shows that there is indeed incremental value of these three sources of information for fraud detection.

In the DT classifier, the performance combining financial ratios and languagebased features is better than that using only financial ratios. But the performance using all the features is slightly worse than that using combined financial ratios and language-based features. In the LR classifier, when adding more features, the final performance decreases. This demonstrates that more features are not necessarily better when classifying fraud. Including all features could lead to overfitted models (very high performance on the training data set), resulting in decreased model performance in the test data set.

Table 13. Performance of LR Classifier Using Combined Features

<table><tr><td>LR</td><td></td><td>Average accuracy</td><td>Average recall</td><td>Average F1 score</td><td>Average AUC</td></tr><tr><td rowspan="2">Financial ratios</td><td>Training</td><td>54.69</td><td>60.31</td><td>56.88</td><td>51.94</td></tr><tr><td>Testing</td><td>54.67</td><td>60.00</td><td>54.54</td><td>43.58</td></tr><tr><td rowspan="2">Financial ratios and language-based features</td><td>Training</td><td>54.33</td><td>61.34</td><td>56.93</td><td>51.22</td></tr><tr><td>Testing</td><td>53.00</td><td>56.35</td><td>53.09</td><td>48.97</td></tr><tr><td rowspan="2">Full combination of features</td><td>Training</td><td>98.28</td><td>99.29</td><td>98.36</td><td>96.67</td></tr><tr><td>Testing</td><td>52.38</td><td>49.18</td><td>45.58</td><td>39.35</td></tr></table>

From Tables 10–13, we note that the SVM model using a combination of financial ratios, language-based features, and social media features achieves the best model performance. The average accuracy, recall, F1 measure, and AUC on the test data set are around 80 percent, consistently higher than those in the previous literature. Overall, our extensive analysis demonstrates not only the efficacy of using social media features for corporate fraud detection but also the incremental value of social media features to existing methods using only financial ratios and/or textual features of MD&A.

## Robustness Check

Social media have the duality of social reporting and a collective rumor mill [50]. A rumor is defined as a statement whose truth value is undefined or deliberately false [56]. Rumors and leaked information may be spread by insiders (such as company managers or directors) or by outsiders (such as investment institutions, professional speculators, or financial journalists). Rumors may eventually turn out to be true or false [39]. Too many false rumors in SeekingAlpha can cause issues in data quality and lead to imprecise classification of fraudulent and nonfraudulent firms. To address this issue and determine how sensitive our algorithm is to leaked information and rumors, we first propose an approach to identify leaked information or rumor from our data set and then reassess the performance of the model by removing those rumors and/or leaked information from our data set.

We assume that if a fraudulent company’s misconduct is mentioned in a post before the first fraud disclosure time, then the post is regarded as leaked information [12]. Analogously, if a post discusses the misconducts of a current legitimate company, then it will be classified as a rumor. The detailed processes to identify leaked information and rumors are discussed in online Appendix. Sixteen features, inspired by Castillo et al. [14] and Yang et al. [67], are developed for our rumor detection model. Overall, 22.75% of the posts for fraudulent firms are identified as leaked information and 15.80 percent of the posts for nonfraudulent firms are rumors. We remove the leaked information for fraudulent firms and rumors for nonfraudulent firms sequentially and obtain three new data sets: the first one has no rumors, the second has no leaked information, and the third has neither rumors nor leaked information. The performances of the SVM classifier on these three data sets are presented in Table 14.

Table 14. Performance of Classification on Data Sets Without Rumors and Leaked Information

<table><tr><td colspan="2">SVM</td><td>Average accuracy</td><td>Average recall</td><td>Average F1 score</td><td>Average AUC</td></tr><tr><td rowspan="2">No rumor only</td><td>Training</td><td>98.97</td><td>98.96</td><td>98.97</td><td>99.78</td></tr><tr><td>Testing</td><td>78.33</td><td>74.20</td><td>76.08</td><td>84.13</td></tr><tr><td rowspan="2">No leaked information only</td><td>Training</td><td>95.69</td><td>93.45</td><td>95.49</td><td>99.25</td></tr><tr><td>Testing</td><td>76.17</td><td>73.27</td><td>74.11</td><td>84.59</td></tr><tr><td rowspan="2">No rumor and no leaked information</td><td>Training</td><td>98.19</td><td>97.76</td><td>98.15</td><td>99.61</td></tr><tr><td>Testing</td><td>77.00</td><td>72.26</td><td>74.94</td><td>80.94</td></tr></table>

Comparing Table 10 and Table 14, we notice that the model performance decreases about 2–10 percent after removing the rumors and leaked information. These results to a certain extent provide further evidence of the robustness of our proposed algorithm. Since leaked information discusses a firm’s misconduct ahead of the fraud disclosure time, it is valuable for the prediction of the firm’s fraudulent behavior. Therefore, performance decreases much more when discarding leaked information from the data set.

## Generalizability Check

Here we test the prediction and generalizability of our best model (SVM with all features) on a separate holdout sample of firms. We extend Dechow et al.’s [19] study period to December 31, 2014, and carefully examine the companies that appear in AAERs from AAER 3491 to 3618. Working together, two graduate students majoring in accounting check whether each AAER stated the annual acts of misconduct of a focal company. The value of Cohen’s kappa, which measures the agreement between two raters, was 0.78. After another round of discussion, they reach an agreement about the classification of these 127 new AAERs and found 13 of them fraudulent. Five of the 13 companies, however, do not have data in SeekingAlpha and/or in Compustat for the corresponding years, and one of them is a financial company. Hence our holdout sample contains 7 fraudulent firms. We also randomly choose 7 nonfraudulent firms to match the fraudulent ones based on firm size and industry. The average accuracy, recall, F1 measure, and AUC of our model on this holdout sample are 71.43 percent, 57.14 percent, 66.67 percent, and 69.39 percent, respectively.

Table 15. Performance of Classification Using Data from Yahoo Finance

<table><tr><td></td><td></td><td>Average accuracy</td><td>Average recall</td><td>Average F1 score</td><td>Average AUC</td></tr><tr><td rowspan="2">SVM model with combined features</td><td>Training</td><td>98.21</td><td>98.62</td><td>98.24</td><td>99.99</td></tr><tr><td>Testing</td><td>65.63</td><td>88.75</td><td>71.52</td><td>69.90-</td></tr></table>

To further assess the generalizability of our algorithm, we assemble a new data set from another social media platform, Yahoo Finance. Of all the fraudulent firms in our data set, 35 have data on Yahoo Finance. We again match the 35 fraudulent with 35 nonfraudulent firms. Online Appendix 3 provides details of the data collection process. We test the performance of our algorithm on this new data set. Due to the limitation of the sample size, a fivefold cross validation technique is used. The results of the SVM classifier using Yahoo Finance data are presented in Table 15.

While the performance of the classification is lower than that using data from SeekingAlpha, our algorithm is still effective in detecting fraudulent firms. The main reason for the decrease in performance, in our view, can be attributed to the lack of analysis reports on Yahoo Finance. Kothari et al. [35] argued that professional analysts usually repackage and interpret the information in corporate disclosures and business press news into in-depth analysis reports. The analysis reports, along with stock market opinions and discussions from general investors and industry experts, contain significant cues that can be leveraged for corporate fraud detection. These cues, however, are lacking in the Yahoo Finance platform.

## Applicability Check

An important question for academic researchers is how our proposed algorithm can be trusted and actually used in practice. To address the issue of practical contributions in more depth, we conducted an applicability check of our proposed framework as well as how people might actually use it. The applicability check also helps to avoid Type III errors [57] by verifying that the research problem formulated is correct. The details of our applicability check process are presented in Online Appendix 4. Here we provide a synopsis of the process.

We recruited four focus groups for the applicability check. Two groups consist of experts in corporate investment, and the other two groups consist of experts in financial accounting. Each group has three domain knowledge experts so betweengroup and within-group comparison can be made. Following the guidelines of Rosemann and Vessey [59], we designed a set of open-ended interview questions. We performed a pilot test of the interview with two accounting Ph.D. students and one accounting practitioner before conducting the formal interviews. During the focus group interviews, the interviewees were first fully exposed to the research objectives, methodologies, and findings of this study. The interviewees were subsequently asked to specify their professional background, answer how to determine if a company is fraudulent or not, and clarify whether they would use our framework to detect fraud. The interviewees were allowed to discuss and exchange opinions during the interviews. The first author of this study served as the moderator and answered any related questions. Each focus group interview lasted about an hour.

The focus group subjects believed that the characteristics of an industry can lead to a different set of financial indicators for corporate fraud assessment. Conventionally, the primary approach for corporate fraud detection was to analyze financial reports and compare the abnormal financial data of the target firm with the data of other companies in the same industry. Additionally, some stakeholders may manually search online financial news to get a better understanding of the target firm, watch video interviews of top management, and listen to company conference calls to look for signals/cues by informally analyzing facial expressions, talk speed, words used, and other types of body language. During the process, the experience played an important role in fraud risk assessment. Furthermore, on-the-spot due diligence research and investigation could be performed to make an informed decision.

Our analyses from the interviews show that the subjects in our focus groups generally welcome new techniques to help them determine whether a corporation is involved in fraudulent behavior. Additionally, the approach proposed in this study represents a new source of information to senior major stakeholders in the financial industry. While these major stakeholders feel that our approach may not entirely replace the analysis based on a financial report, it does provide them a helpful auxiliary tool and is largely welcomed by financial and accounting practitioners.

From the interview, we also discovered a few interesting results. One focus group (with corporate investment background) believed that social media platforms contain inaccurate information such as rumors. The focus group members indicate, however, that they would use our algorithm if the issue of the data quality is addressed. As discussed earlier, our proposed algorithm is still effective in detecting fraudulent firms after removing leaked information and rumors from the data. In addition, some investment experts indicated that they were very likely to use the social media-based analytic tool if they were personal investors. They would also use the proposed algorithm if the focal company in their investment decision involved extensive research. When evaluating a large target company, investment experts also preferred our algorithm over personal experiences. Financial accountants in general believed that financial reports were still the most valuable information in detecting fraud. Overall, these findings of applicability check provide further evidence that we developed an appropriate method to solve a practical question.

## Discussion and Conclusions

Corporate fraud is a serious issue in modern corporate risk management. This study used social media data from financial platforms and proposed a text analytic framework, rooted in the SFL theory, which aims to extract signals/cues to detect early signs of fraud. Social media are unique in their ability to generate and disseminate information by the general public, which traditional media lack [42]. Social media platforms, such as SeekingAlpha, contain various information about a firm, including new product announcements, merger and acquisition, return on investment, and even conjectures about managements’ inside trading behaviors and other misconduct.

We show that the latent features derived from financial social media data have a leading effect for fraud detection. In addition, we benchmark the performance of our model against those that use just the financial ratios and/or language-based features from MD&A sections, and demonstrate that social media features perform better in our data set. By integrating financial ratios, language-based features, and social media features together, our algorithm leads to an 80 percent prediction accuracy. Finally we conduct an applicability check of our algorithm. These findings not only demonstrate the efficacy of social media features for fraud detection but also verify that a social media-based method can supplement existing corporate fraud detection approaches. We note that the five sets of latent features proposed in our study can be extracted from other types of social media data and applied to domains such as product defect discovery [3], fraudulent behavior detection on crowdfunding platforms [63], and fake online reviews detection [70].

Our study serves as proof of a concept to develop a system that can be used by government regulators, securities agencies, company research institutes, and other stakeholders for early fraud detection and prevention. We propose three main components for the system. First, it needs to periodically collect data from social media platforms, such as SeekingAlpha and Yahoo Finance, and automatically derive latent features such as those discussed in the study. Second, the latent social media features along with financial ratios (accessible via Compustat) and languagebased features (obtainable from the Compustat and SEC EDGAR databases) from the MD&A will feed into a machine learning module to classify fraudulent and nonfraudulent firms. Third, the final learned model can be used to monitor and predict the likelihood that a potential firm may be involved in fraudulent behavior.

The proposed fraud detection system has the potential to significantly shorten the time lag from fraud inception to fraud disclosure, thus significantly preventing financial losses to broad shareholders and financial turbulence to the economic system. Three stakeholders, in particular, investors, audit firms, and government regulators and policymakers can benefit from such a system [1, 15]. Investors (including individuals, institutional investors, rating agencies, and others) are often easily influenced by misleading reports. Early fraud detection will help investors make informed investment decisions. For auditors, the new method will help them better assess the risk of material misstatement during their planning phase so as to reduce instances of fraudulent financial statements. For government regulators, an efficient and effective fraud detection system can help them focus primarily on suspicious ones. Finally, the base standard on Analytical Procedures (e.g., SAS No. 56) was issued a quarter of a century ago, long before the emergence of business intelligence, social media, big data, and other technological advances. Now is the time for policymakers to reexamine and update the Audit Standards.

This study has several limitations. The sample size is small since financial social media platforms are relatively new. Fraudulent firms prior to the establishment of these platforms were not used in our study. We used all prior-disclosure information to predict fraud. It is possible that more recent social media data incorporate all relevant information. If that is the case, then it is an interesting exercise to examine the appropriate time window to extract social media data. In addition, when extracting social media features, we captured only the centrality degree of the social interactions. The main reason is that there are no interactions between the focal firm itself and platform users on SeekingAlpha. If we consider contents and comments released by official accounts of firms on Facebook or Twitter, other patterns of social network structure can be investigated as suggested by Borgatti and Foster [9], such as centrality, betweenness, and closeness. Note that if these social media platforms, such as SeekingAlpha, change their website designs, we need to reprogram the data crawl process in order to retrieve the latest data.

Experts in the focus group provided some interesting questions that are valuable for future research. They held that different corporate frauds have different impacts on investors, auditors, and regulators. Detecting and categorizing specific corporate frauds will be an interesting exercise. Domain knowledge experts also believed that supervision regime change could lead to the establishment of new policies, which can have a significant influence on the effectiveness of fraud detection methods.

## Supplemental File

Supplemental data for this article can be accessed on the publisher’s website at DOI: https://doi.org/10.1080/07421222.2018.1451954

## Funding

This work was supported by the National Science-Technology Support Plan of China (2015BAK18B02), a development grant from Shenzhen Science, Technology and Innovation Commission (JCYJ20160229165300897), and a Hong Kong GRF grant (193213).

## REFERENCES

1. Abbasi, A.; Albrecht, C.; Vance, A.; and Hansen, J. Metafraud: A meta-learning framework for detecting financial fraud. MIS Quarterly, 36, 4 (2012), 1293–1327.

2. Abbasi, A.; and Chen, H. CyberGate: A design framework and system for text analysis of computer-mediated communication. MIS Quarterly, 32, 4 (2008), 811–837.

3. Abrahams, A.S.; Fan, W.; Wang, G.A.; Zhang, Z.; and Jiao, J. An integrated text analytic framework for product defect discovery. Production and Operations Management, 24, 6 (2015), 975–990.

4. Antweiler, W.; and Frank, M.Z. Is all that talk just noise? The information content of Internet stock message boards. Journal of Finance, 59, 3 (2004), 1259–1294.

5. Argamon, S.; Whitelaw, C.; Chase, P.; Hota, S.R.; Garg, N.; and Levitan, S. Stylistic text classification using functional lexical features. Journal of the American Society for Information Science and Technology, 58, 6 (2007), 802–822.

6. Beneish, M.D. Detecting GAAP violation: Implications for assessing earnings management among firms with extreme financial performance. Journal of Accounting and Public Policy, 16, 3 (1997), 271–309.

7. Beneish, M.D. The detection of earnings manipulation. Financial Analysts Journal, 55, 5 (1999), 24–36.

8. Blei, D.M.; Ng, A.Y.; Jordan, M.I.; and Lafferty, J. Latent dirichlet allocation. Journal of Machine Learning Research, 3, 4/5 (2003), 993–1022.

9. Borgatti, S.P.; and Foster, P.C. The network paradigm in organizational research: A review and typology. Journal of Management, 29, 6 (2003), 991–1013.

10. Brazel, J.F.; Jones, K.L.; and Zimbelman, M.F. Using nonfinancial measures to assess fraud risk. Journal of Accounting Research, 47, 5 (2009), 1135–1166.

11. Brown, N.C.; Crowley, R.M.; and Elliott, W.B. What are you saying? Using topic to detect financial misreporting. In P. Mohanram and L. Yang (eds.), Proceedings of the 27th Annual Conference on Financial Economics and Accounting Paper. Toronto, 2016, pp. 1–67.

12. Brunnermeier, M.K. Information leakage and market efficiency. Review of Financial Studies, 18, 2 (2005), 417–457.

13. Buller, D.B.; and Burgoon, J.K. Interpersonal deception theory. Communication Theory, 6, 3 (1996), 203–242.

14. Castillo, C.; Mendoza, M.; and Poblete, B. Information credibility on twitter. In S. Sadagopan, K. Ramamritham, A. Kumar, and M. P. Ravindra (eds.), Proceedings of the 20th International Conference on World Wide Web. Hyderabad, 2011, pp. 675–684.

15. Cecchini, M.; Aytug, H.; Koehler, G.J.; and Pathak, P. Detecting management fraud in public companies. Management Science, 56, 7 (2010), 1146–1160.

16. Cecchini, M.; Aytug, H.; Koehler, G.J.; and Pathak, P. Making words work: Using financial text as a predictor of financial events. Decision Support Systems, 50, 1 (2010), 164– 175.

17. Chen, H.; De, P.; Hu, Y.; and Hwang, B.-H. Wisdom of crowds: The value of stock opinions transmitted through social media. Review of Financial Studies, 27, 5 (2014), 1367– 1403.

18. Dechow, P.M. Accounting earnings and cash flows as measures of firm performance: The role of accounting accruals. Journal of Accounting and Economics, 18, 1 (1994), 3–42.

19. Dechow, P.M.; Ge, W.; Larson, C.R.; and Sloan, R.G. Predicting material accounting misstatements. Contemporary Accounting Research, 28, 1 (2011), 17–82.

20. Dong, W.; Liao, S.; Fang, B.; Cheng, X.; Chen, Z.; and Fan, W. The detection of fraudulent financial statements: An integrated language model. In K. Siau, Q. Li, and X. Guo (eds.), Proceedings of the 18th Pacific Asia Conference on Information Systems. Chengdu, 2014, pp. 1–15.

21. Dyck, A.; Morse, A.; and Zingales; L. Who blows the whistle on corporate fraud?. The Journal of Finance, 65, 6 (2010), 2213–2253.

22. Elliott, R. K.; and Willingham, J. J. Management fraud: Detection and deterrence. New York: Petrocelli Books, 1980.

23. Fanning, K.M.; and Cogger, K.O. Neural network detection of management fraud using published financial data. International Journal of Intelligent Systems in Accounting, Finance and Management, 7, 1 (1998), 21–41.

24. Federal Bureau of Investigation (FBI). Financial crimes report to the public (Fiscal years 2010–2011). 2012. https://www.fbi.gov/stats-services/publications/financial-crimes-report-2010- 2011.

25. Fu, T.; Abbasi, A.; and Chen, H. A hybrid approach to Web forum interactional coherence analysis. Journal of the American Society for Information Science and Technology, 59, 8 (2008), 1195–1209.

26. Glancy, F.H.; and Yadav, S.B. A computational model for financial reporting fraud detection. Decision Support Systems, 50, 3 (2011), 595–601.

27. Goel, S.; and Gangolly, J. Beyond the numbers: Mining the annual reports for hidden cues indicative of financial statement fraud. Intelligent Systems in Accounting, Finance and Management, 19, 2 (2012), 75–89.

28. Goel, S.; Gangolly, J.; Faerman, S.R.; and Uzuner, O. Can linguistic predictors detect fraudulent financial filings? Journal of Emerging Technologies in Accounting, 7, 1 (2010), 25–46.

29. Halliday, M.; Matthiessen, C.M.; and Matthiessen, C. An Introduction to Functional Grammar. London: Hodder Education, 2004.

30. Hobson, J.L.; Mayew, W.J.; and Venkatachalam, M. Analyzing speech to detect financial misreporting. Journal of Accounting Research, 50, 2 (2012), 349–392.

31. Humpherys, S.L.; Moffitt, K.C.; Burns, M.B.; Burgoon, J.K.; and Felix, W.F. Identification of fraudulent financial statements using linguistic credibility analysis. Decision Support Systems, 50, 3 (2011), 585–594.

32. Hyland, K. Genre and Second Language Writing. Ann Arbor: University of Michigan Press, 2004.

33. Joachims, T. Training linear SVMs in linear time. In L. Ungar (ed.), Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. Philadelphia, 2006, pp. 217–226.

34. Kaminski, K.A.; Wetzel, T.S.; and Guan, L. Can financial ratios detect fraudulent financial reporting? Managerial Auditing Journal, 19, 1 (2004), 15–28.

35. Kothari, S.; Li, X.; and Short, J.E. The effect of disclosures by management, analysts, and business press on cost of capital, return volatility, and analyst forecasts: A study using content analysis. Accounting Review, 84, 5 (2009), 1639–1670.

36. Larcker, D.F.; and Zakolyukina, A.A. Detecting deceptive discussions in conference calls. Journal of Accounting Research, 50, 2 (2012), 495–540.

37. Lazarus, R. S. Thoughts on the relations between emotion and cognition. American Psychologist, 37, 9 (1982), 1019–1024.

38. Li, F. Textual analysis of corporate disclosures: A survey of the literature. Journal of Accounting Literature, 29 (2010), 143–165.

39. Li, Q.; Liu, X.; Fang, R.; Nourbakhsh, A.; and Shah, S. User behaviors in newsworthy rumors: A case study of Twitter. In K. P. Gummadi and M. Strohmaier (eds.), Proceedings of the 10th International AAAI Conference on Web and Social Media. Cologne, 2016, pp. 627–630.

40. Liou, F.-M. Fraudulent financial reporting detection and business failure prediction models: A comparison. Managerial Auditing Journal, 23, 7 (2008), 650–662.

41. Loughran, T. I. M.; and McDonald, B. When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. The Journal of Finance, 66, 1 (2011), 35–65.

42. Luo, X.; Zhang, J.; and Duan, W. Social media and firm equity value. Information Systems Research, 24, 1 (2013), 146–163.

43. Manning, C.D.; Raghavan, P.; and Schütze, H. Introduction to Information Retrieval. Cambridge: Cambridge University Press, 2008.

44. Manning, C.D.; Surdeanu, M.; Bauer, J.; Finkel, J.; Bethard, S.J., and McClosky, D. The Stanford CoreNLP natural language processing toolkit. In K. Bontcheva and Z. Jingbo (eds.), Proceedings of 52nd Annual Meeting of the Association for Computational Linguistics System Demonstrations. Baltimore, 2014, pp. 55–60.

45. Merkl-Davies, D. M., and Brennan, N. Discretionary disclosure strategies in corporate narratives: incremental information or impression management?. Journal of Accounting Literature, 26, (2007), 116–196.

46. Miller, G.A.; Beckwith, R.; Fellbaum, C.; Gross, D.; and Miller, K.J. Introduction to WordNet: An on-line lexical database. International Journal of Lexicography, 3, 4 (1990), 235–244.

47. Moffitt, K.; Felix, W.; and Burgoon, J.K. Using lexical bundles to discriminate between fraudulent and non-fraudulent financial reports. In C. Ferran (ed.), Proceedings of the SIG-ASYS Pre-ICIS 2010 workshop. St. Louis, MO, 2010, pp. 1–22.

48. Newman, M.L.; Pennebaker, J.W.; Berry, D.S.; and Richards, J.M. Lying words: Predicting deception from linguistic styles. Personality and Social Psychology Bulletin, 29, 5 (2003), 665–675.

49. Ngai, E.; Hu, Y.; Wong, Y.; Chen, Y.; and Sun, X. The application of data mining techniques in financial fraud detection: A classification framework and an academic review of literature. Decision Support Systems, 50, 3 (2011), 559–569.

50. Oh, O.; Agrawal, M.; and Rao, H.R. Community intelligence and social media services: A rumor theoretic analysis of tweets during social crises. MIS Quarterly, 37, 2 (2013), 407–426.

51. Pak, J.; and Zhou, L. Social structural behavior of deception in computer-mediated communication. Decision Support Systems, 63 (2014), 95–103.

52. Pang, B.; and Lee, L. Opinion mining and sentiment analysis. Foundations and Trends in Information Retrieval, 2, 1–2 (2008), 1–135.

53. Pennebaker, J.W.; Francis, M.E.; and Booth, R.J. Linguistic Inquiry and Word Count (LIWC): A Computerized Text Analysis Program. Austin: LIWC.net, 2001.

54. Phua, C.; Lee, V.; Smith, K.; and Gayler, R. A comprehensive survey of data miningbased fraud detection research. 2010. https://arxiv.org/abs/1009.6119.

55. Purda, L.; and Skillicorn, D. Accounting variables, deception, and a bag of words: Assessing the tools of fraud detection. Contemporary Accounting Research, 32, 3 (2014), 1193–1223.

56. Qazvinian, V.; Rosengren, E.; Radev, D.R.; and Mei, Q. Rumor has it: Identifying misinformation in microblogs. In P. Merlo (ed.), Proceedings of the Conference on Empirical Methods in Natural Language Processing. Edinburgh, 2011, pp. 1589–1599.

57. Rai, A. Editor’s comments: Avoiding Type III errors: Formulating IS research problems that matter. MIS Quarterly, 41, 2 (2017), iii–vii.

58. Rajaraman, A.; Ullman, J.D.; Rajaraman, A.; and Ullman, J.D. Data Mining of Massive Datasets. Cambridge: Cambridge University Press, 2011.

59. Rosemann, M., and Vessey, I. Toward improving the relevance of information systems research to practice: The role of applicability checks. MIS Quarterly, 32, 1 (2008), 1–22.

60. Rutherford, B.A. Genre analysis of corporate annual report narratives a corpus linguistics–based approach. Journal of Business Communication, 42, 4 (2005), 349–378.

61. Sack, W. Conversation map: An interface for very large-scale conversations. Journal of Management Information Systems, 17, 3 (2000), 73–92.

62. Schumaker, R.P.; Zhang, Y.; Huang, C.-N.; and Chen, H. Evaluating sentiment in financial news articles. Decision Support Systems, 53, 3 (2012), 458–464.

63. Siering, M.; Koch, J.-A.; and Deokar, A. V. Detecting fraudulent behavior on crowdfunding platforms: The role of linguistic and content-based cues in static and dynamic contexts. Journal of Management Information Systems, 33, 2 (2016), 421–455.

64. Summers, S.L.; and Sweeney, J.T. Fraudulently misstated financial statements and insider trading: An empirical analysis. Accounting Review, 73, 1 (1998), 131–146.

65. Teo, P. Racism in the news: A critical discourse analysis of news reporting in two Australian newspapers. Discourse and Society, 11, 1 (2000), 7–49.

66. Williamson, S.; Wang, C.; Heller, K.A., and Blei, D.M. The IBP compound Dirichlet process and its application to focused topic modeling. In S. Wrobel (ed.), Proceedings of the 27th International Conference on Machine Learning. Haifa, 2010, pp. 1151–1158.

67. Yang, F.; Liu, Y.; Yu, X.; and Yang, M. Automatic detection of rumor on Sina Weibo. In Y. Ding, J. Han, J. Tang, and P. Yu (eds.), Proceedings of the ACM SIGKDD Workshop on Mining Data Semantics. Beijing, 2012, pp. 1–7.

68. Yang, Y.; and Pedersen, J.O. A comparative study on feature selection in text categorization. In D. H. Fisher (ed.) Proceedings of the 14th International Conference on Machine Learning. Nashville, TN, 1997, pp. 412–420.

69. Yue, D.; Wu, X.; Wang, Y.; Li, Y.; and Chu, C.-H. A review of data mining-based financial fraud detection research. In L. Cuthbert, W. Huang, and C. Rubenstein (eds.), Proceedings of the International Conference on Wireless Communications, Networking and Mobile Computing. Shanghai, 2007, pp. 5519–5522.

70. Zhang, D.; Zhou, L.; Kehoe, J.L.; and Kilic, I.Y. What online reviewer behaviors really matter? Effects of verbal and nonverbal behaviors on detection of fake online reviews. Journal of Management Information Systems, 33, 2 (2016), 456–481.
