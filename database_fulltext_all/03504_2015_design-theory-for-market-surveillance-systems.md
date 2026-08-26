---
otero_id: 3504
otero_key: "CMJ8U2AN"
title: "Design Theory for Market Surveillance Systems"
authors: "Xin Li; Sherry X. Sun; Kun Chen; Terrance Fung; Huaiqing Wang"
year: "2015"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2015.1063312"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design Theory for Market Surveillance Systems

Xin Li, Sherry X. Sun, Kun Chen, Terrance Fung & Huaiqing Wang

To cite this article: Xin Li, Sherry X. Sun, Kun Chen, Terrance Fung & Huaiqing Wang (2015) Design Theory for Market Surveillance Systems, Journal of Management Information Systems, 32:2, 278-313, DOI: 10.1080/07421222.2015.1063312

To link to this article: https://doi.org/10.1080/07421222.2015.1063312

![](/api/attachments/CMJ8U2AN/fulltext/images/a357bf46462105690b53fa0d4d1c012df6cf3b330bb827aa7263e2df112b5e1a.jpg)

Published online: 28 Aug 2015.

![](/api/attachments/CMJ8U2AN/fulltext/images/24ff3ef6c0b1cf62d49c95e8006bb7a2c53760cd09e20996fa0ac7d8aab0a795.jpg)

Submit your article to this journal

![](/api/attachments/CMJ8U2AN/fulltext/images/bdf8ed01c2394b9f81d7dc394400b4122e6679c2eb2c182163258160c7d10bfb.jpg)

Article views: 344

![](/api/attachments/CMJ8U2AN/fulltext/images/3cf6e9d22128b801bdec18f7518394cdf78650aeea1a096c0cc05f61fe2dcb8c.jpg)

View related articles

![](/api/attachments/CMJ8U2AN/fulltext/images/1c69e0790638197d9e1ff2ce72098e9ae16a5627a4cb14e4fdc4bb177cc46fc4.jpg)

View Crossmark data

![](/api/attachments/CMJ8U2AN/fulltext/images/05d8f2ff5d8fc1274468474d1b691371760297f1b9e29781e9790f2c1c670697.jpg)

Citing articles: 1 View citing articles

# Design Theory for Market Surveillance Systems

XIN LI, SHERRY X. SUN, KUN CHEN, TERRANCE FUNG, AND HUAIQING WANG

XIN LI is an assistant professor in the Department of Information Systems at the City University of Hong Kong. He received his Ph.D. in Management Information Systems from the University of Arizona, and his Bachelor’s and Master’s degrees from the Department of Automation at Tsinghua University, China. His research interests include business intelligence and knowledge discovery, social network analysis, social media, and e-commerce. His work has appeared in the Journal of Management Information Systems, Decision Support Systems, ACM Transactions on Management Information Systems, Journal of the American Society for Information Science and Technology, and various IEEE Transactions, among other venues.

SHERRY X. SUN holds a Ph.D. degree in management and an M.S. degree in management information systems from the University of Arizona. Her research focuses on the construction of computational methodologies and tools for the management of enterprise information systems. She has published in journals such as Information Systems Research, IEEE Transactions on Systems, Man, and Cybernetics, Information Sciences, Information Systems Frontier, and others.

KUN CHEN (corresponding author; chenk@sustc.edu.cn) is an assistant professor in the Department of Financial Mathematics and Financial Engineering at South University of Science and Technology of China in Shenzhen. She received her Ph.D. from the Department of Information Systems at the City University of Hong Kong.

TERRANCE FUNG works for the Securities and Futures Commission of Hong Kong. He received his Ph.D. from the Department of Information Systems at the City University of Hong Kong.

HUAIQING WANG is a professor in the Department of Financial Mathematics and Financial Engineering at South University of Science and Technology of China, in Shenzhen. He is also the honorary dean and a guest professor in the School of Information Engineering, Wuhan University of Technology, China. He received his Ph.D. from the University of Manchester, UK. He specializes in the research of financial intelligence and intelligent systems, such as intelligent financial systems, intelligent learning systems, business process management systems, knowledge management systems, and conceptual modeling and ontology. He has published more than 70 papers in well-known scholarly journals.

ABSTRACT: Market surveillance systems (MSSs) are information systems that monitor financial markets to combat market abuses. Existing MSSs focus mainly on analyzing trading activities and are often developed through a trial-and-error approach by screening data mining algorithms and features. The void of theoretical direction limits the effectiveness of MSSs and calls for the development of a design theory based on a thorough examination of the meta-requirements of MSSs. Based on the efficient market hypothesis and text understanding theory, this paper argues that market information analysis should be incorporated into MSSs and commonsense knowledge should be employed to connect related events to transactions and provide reference concepts for understanding market context and assessing transaction risk. We show the effectiveness of this proposed design theory through developing and evaluating a prototype system in the context of a real-world stock exchange market. By taking a theory-driven approach, this research shows the possibility and provides guidelines on the use of market information analysis to alleviate the market surveillance problem, which has significant implications for financial markets and the economy given the explosive growth of illegal trading activities worldwide.

KEY WORDS AND PHRASES: design theory, market surveillance systems, text mining, financial markets, efficient market hypothesis, text understanding theory.

Financial markets are the basis of the modern global economy. It is critical to ensure that people trade in a fair manner so that the markets function properly. However, there have always been attempts to impair market integrity for economic profit, such as illegal insider trading and market manipulation. In this research, we refer to the abusive, manipulative, or illegal trading practices in financial markets as market abuses. Among such market abuses, illegal insider trading activities employ information gained in capacities where the law prohibits its use for trading advantage. Market manipulation intends to move prices in a direction that is inconsistent with traders’ beliefs through disseminating false news or executing deceptive trading transactions. By making use of hidden information or generating false information, market abuses affect the market’s proper response to market information, cause price deviation from the true value of trading objects, and ruin the integrity of the price discovery process as well as investors’ confidence. Consequently, market liquidity dries up and the financial markets no longer function efficiently.

In order to tackle the challenge of market abuses, financial markets worldwide employ market surveillance systems (MSSs) [10, 42] to oversee trader behaviors and identify market abuses [9, 16]. MSSs helped us to identify some high impact market abuse cases in recent years. For example, in 2009, the Galleon Group was charged with insider trading and eventually closed [24] . Part of the evidence leading to the investigation of this biggest hedge fund insider trading scandal in history involved abnormal activities on the New York Stock Exchange. However, the need for MSSs is far more than identifying the revealed cases. Augustin et al. [4] showed that about 25 percnet of the merger and acquisition deals between 1996 and 2012 in the United States were related to unusual activities on equity options markets 30 days before the deal announcement. The high volume of suspicious activities reinforces the need for MSSs in practice. The need for MSSs has gone beyond the direct need of government regulatory bodies. After the 2008 economic crisis and several trading misconduct cases, in which some traders caused their companies huge financial losses, financial firms have been eager to incorporate MSSs to monitor internal activities for risk mitigation [58].

Despite the important application of MSSs, there have been limited efforts on a design theory to direct effective design. To the best of our knowledge, existing MSSs are often developed in a trial-and-error manner, using various data mining techniques, for example, outlier detection techniques, on market activities (price, volume, or profit of transactions) [55] to find out the ones that can lead to best detection performance. The MSS development process lacks theoretical direction and it is not clear whether existing analysis is sufficient for surveillance.

This paper argues that market information, such as public news, announcements, financial reports, and rumors, is a critical component of market surveillance. In finance, the efficient market hypothesis asserts that financial markets react to public information in an efficient manner [26]. Information on the market, including all past public information, current public information, or even private information, is quickly reflected in market price (i.e., the weak form, the semistrong form, and the strong form of the efficient market hypothesis). In general, market activities should be temporally consistent with publicly available market information if the financial market runs smoothly. When dishonest traders employ hidden information in trading (i.e., insider trading) or intentionally bring false information into a market (i.e., market manipulation), their trading activities may no longer behave in accordance with public market information. Such inconsistency can be a cue for surveillance. In supervisory agencies, suspicious transactions identified through market activity analysis are always subject to manual inspection. Surveillance specialists employ public news to interpret the rationale behind transactions and identify high-risk transactions for further investigation [25]. However, from the design theory perspective, the role of market information has not been fully utilized in MSSs [15].

Noticing this limitation, this paper proposes a design theory for MSSs according to the framework in Walls et al. [70]. In this design theory, we employ the efficient market hypothesis to justify the incorporation of market information analysis with market activity analysis in the design product. Moreover, the design process component of the design theory explores how market information analysis should be conducted. Rooted in text understanding theory from cognitive psychology, we argue that commonsense knowledge should be employed in the design method. It can help exploit intertwined relations between market information and transactions, and understand subtle meanings of the textual market information to assess suspicious transaction risk. The design product and the design process are integrated in our design theory. The use of commonsense knowledge (as suggested by the text understanding theory) is the key to enable text mining in MSSs in our design theory.

Following the design science paradigm [32], we instantiate our design theory in a prototypical system, MarketWatch. The system employs news to analyze transaction risk with the help of machine learning classifiers and then presents transactionrelated news in a graph visualization according to the commonsense knowledge. We evaluate the effectiveness of the proposed approach with experiments on a realworld data set and through interviews with surveillance specialists. We find that an effective market information analysis module for MSSs significantly eases surveillance specialists’ work by providing additional evidence on abnormal transactions.

## Background

## Market Surveillance

Market integrity is the fundamental requirement of financial markets. However, there have always been attempts to impair market integrity for economic profit. To prevent such market abuses requires the joint efforts of scholars, practitioners, and regulators. Due to the complexity of financial markets, theoretically sound and robust assessments of illegal trading are difficult. Thus, practitioners rely on MSSs [42] to scrutinize financial markets for suspicious transactions with the help of statistical and machine learning techniques. Most financial markets around the world are now equipped with MSSs. Among these systems, SMARTS (Securities Markets Automated Research Trading and Surveillance) is one of the leading solutions [63]. Established in 1994, over 80 clients across 30 markets now use SMARTS, including the Hong Kong Stock Exchange. In 2010, SMARTS was acquired by NASDAQ. AWACS (Advanced Warning and Control System) specializes in realtime multiexchanges activities [5]. SONAR (Securities Observation, News Analysis, and Regulation system) was adopted by FINRA (Financial Industry Regulatory Authority) in 2001 [25].

Table 1 compares the key functionalities of major existing MSSs, which are classified as two types: market activity analysis and market information analysis. In general, most existing MSSs take a similar approach characterized by the analysis of market activities, such as unusual price change, trading volume, profit for transactions, and so on [56]. Patterns of market abuses can be summarized from surveillance specialists’ experience and implemented as rule-based systems [42] or through statistical analysis [49].

For the rule-based approach, Lucas [42] reported on a rule-based expert system for surveillance, in which patterns of illegal trading activities were summarized from interviews with surveillance specialists. There were approximately 160 rules, each of which suggests a prediction with a confidence value. All rule suggestions are aggregated to derive the final prediction. Kirkland et al. [39] also employed a rule-based approach to build surveillance systems, where the rules were discovered from association rule mining and decision trees.

Table 1. Key Functionalities of Major Existing Market Surveillance Systems

<table><tr><td></td><td>SMARTS[63]</td><td>Scila[61]</td><td>AWACS[5]</td><td>SONAR[25]</td></tr><tr><td colspan="5">Market activity analysis</td></tr><tr><td colspan="5">Data</td></tr><tr><td>Transactions</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Ask/bid orders</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td colspan="5">Analytics</td></tr><tr><td>Activity query</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Activity statistics</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Prebuilt risk assessment models</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Customizable assessment models</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td colspan="5">Presentation</td></tr><tr><td>Financial trend charts</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Alert overlay on trend charts</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td colspan="5">Market information analysis</td></tr><tr><td colspan="5">Data</td></tr><tr><td>News</td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>Financial reports</td><td></td><td></td><td></td><td>√</td></tr><tr><td colspan="5">Analytics</td></tr><tr><td>Event query</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Event extraction from text</td><td></td><td></td><td></td><td>√</td></tr><tr><td colspan="5">Presentation</td></tr><tr><td>List view of events</td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>Event overlay on financial charts</td><td>√</td><td></td><td></td><td>√</td></tr></table>

In statistical analysis, market activity-based surveillance is usually framed as an outlier detection problem [19]. Time-series models have been employed to predict normal market trends and reflect abnormal changes. Pirrong [55] used regression and error correction models with features on price and volume change to detect manipulation in soybean futures markets. Qu et al. [57] employed Voronoi diagram-based clustering to find outliers in stock price time series, which may indicate market abuses. Furthermore, machine learning algorithms can be applied on timeseries features to find abnormal transactions. Ogut et al. [49] applied neural network and Support Vector Machine (SVM) on variables to detect stock price manipulation, including the difference between stock and index’s average daily return, average daily change in volume, and average daily volatility. They found that the data mining algorithms have better performance than discriminant analysis and logit regression. Palshikar and Apte [51] devised a graph clustering algorithm based on timing and transaction characteristics to detect circular trading. These techniques for market activity analysis characterize the MSSs that have been widely used in major markets worldwide.

![](/api/attachments/CMJ8U2AN/fulltext/images/f65b20aa9a103d7e58512fb3f1e9c0baedaccaf978cd3dae85681556a824065e.jpg)  
Figure 1. The Market Surveillance Process in Agencies

However, market surveillance in practice is not limited to these market activity analyses. Figure 1 summarizes the generic market surveillance process using MSSs. In daily operations, the market activity-based surveillance algorithms report anomalous transactions. Surveillance specialists then manually inspect the identified transactions according to the market trend and public news appearing around the transaction time identified from internal/external search engines. After the manual inspection, suspicious transactions that cannot be explained by news events are reported to senior officials, leading to formal legal investigations. The manually identified suspicious transactions are also reported to the model development team as training data. The modelers are responsible for developing machine learning models, tuning their parameters based on the identified suspicious transactions, and updating the market activity-based surveillance algorithms used in daily operations.

In the surveillance process, specialists’ inspection and digestion of market information play a very important role. Some systems, such as SMARTS and SONAR (Table 1), partially support the use of market information. They generally support news search and presentation with financial charts to aid surveillance specialists. SONAR supports event extraction and can align events with a transaction timeline as evidence for risk assessment [25]. It also codes news to different topic categories to aid specialists’ comprehension and provide predefined rules to specify if certain events are of concern. SMARTS can also classify whether a news article may cause a stock price change based on its linguistic features [45]. However, directly assessing transaction risk with the help of news contents in existing MSSs is still very primitive. It is mostly up to the surveillance specialists to understand news content and determine whether it is related to trading activities. Due to the primitive textual analysis capabilities of the current generation of

MSSs, many surveillance specialists even resort to general-purpose search engines, such as Google, to manually retrieve relevant news events. To reduce specialists’ workload, it is necessary to develop more effective systems that can explore news-transaction relations and directly assess transaction risk with the help of news articles.

## Why a New Design Theory Is Needed for Market Surveillance

Even though many surveillance specialists rely on news search engines and laborintensive manual digestion of news to support their work, practitioners still underestimate the significance of text mining in MSSs (partially due to their past unsatisfactory experience with text mining solutions). In the MSS context, existing research focuses on the use of data mining techniques to detect suspicious transactions. It is not clear whether existing market activity-based designs are sufficient for market surveillance. There is a need for theoretical justification and guidelines on the use of text mining in MSSs to direct practices and support MSS development. Once the theoretical necessity and practical effectiveness of text miningbased solutions are shown, the demand for text mining solutions from practitioners should increase. Thus, this research focuses on developing a design theory for MSSs.

Design theory is the output of design science research [27, 52], which seeks to understand important information systems development problems [48] and to offer solutions through building and evaluating innovative information technology (IT) artifacts [32]. In the process of searching for solutions, design science research has the potential to validate previous theoretical findings as well as lead to more in-depth theoretical explorations [44, 70]. The developed design theory is validated through a rigorous development-evaluation process and can direct future design and development. This research follows the design science paradigm in building a design theory for MSSs.

## A Design Theory for Market Surveillance Systems

We propose a design theory for developing effective and functional MSSs considering both market activities and market information. Multiple theory frameworks exist for theorizing the design of IT artifacts (i.e., systems, models, etc.). Walls et al. propose that it is necessary to delineate both the design product and the design process in a design theory [69, 70]. From the design product aspect, a design theory needs to draw meta-requirements of the artifact from its governing kernel theories rooted in natural or social sciences. The meta-requirements are fulfilled in a metadesign and validated through testable design product hypotheses. From the design process aspect, the design method and procedure to construct the artifact are also governed by kernel theories (which can be different from design product kernel theories) and need to be validated through testable design process hypotheses. There also exist simpler frameworks, such as Markus et al. [44], that focus on the design product in building the design theory.

![](/api/attachments/CMJ8U2AN/fulltext/images/437d0062deb767b198f3885f4eef56c8beeeb24cd3e3f6f2703507670a3c7f40.jpg)  
Figure 2. A Design Theory for Market Surveillance Systems

After carefully examining existing theory frameworks, we choose to use Walls et al.’s framework [70] to build our design theory because our proposed design theory characterizes both the design product and the design process of MSSs. As shown in Figure 2, the design product of the design theory explains why market information should be included in MSSs, and the design process of the design theory explains how to enable the use of text mining in MSSs (with the help of commonsense knowledge). The design product meta-requirements are drawn from the efficient market hypothesis. Naturally derived from this theory, effective MSS must be able to analyze not only market activities but also market information, of which textual market information is a major portion. This meta-requirement drives the MSS design process. Directed by the text understanding theory [67], we propose a design method that incorporates commonsense knowledge [37] with text mining for market information understanding and analysis, especially to assess the connections between suspicious transactions and public market information. The text understanding theory provides strong support for the use of commonsense knowledge in the design method. Through this design method, the meta-design delineates features of effective MSSs that combine market information and market activity analysis in the design product.

## The Design Product: Market Surveillance Systems

The design product part of our design theory characterizes the structure of an effective MSS that can meet the requirements of a market surveillance task.

## Kernel Theories

In a financial market, traders actively collect market information, generate interpretations of market conditions, and make trading decisions to maximize their profit. Their collective activities determine market movements. Because traders exploit market information, the efficient market hypothesis [18] asserts that financial markets will respond to market information in an efficient manner. There are three forms of efficient market hypothesis (the weak form, the semistrong form, and the strong form), which differ in the information that can be captured in a market (historical public information, current public information, and hidden information). If changes on historical public information are reflected in a market, the market is in the weak form of efficiency market. If current public information is reflected in the market, it is in the semistrong form. If hidden information is further reflected in the market, it is in the strong form.

Many studies have been conducted to empirically test the efficient market hypothesis in different contexts. For example, Khan [36] showed that the grain futures market indicated semistrong efficiency after large traders’ position information is released. Samuelson argued that the stock market is “micro efficient” but not “macro efficient” [59]. That is, the efficient markets hypothesis works much better for individual stocks than it does for the aggregate stock market. This dictum is also strongly supported by follow-up empirical studies [35].

The efficient market hypothesis is widely used in financial practices. It has become a common practice in automated trading to develop algorithms and inspect market information to generate trading decisions [46, 62]. In market regulation, the efficient market hypothesis has also been accepted by the Supreme Court of the United States in judging securities fraud claims [47].

In this research, we employ the efficient market hypothesis as the kernel theory of our design product to direct MSS design. Based on this theory, security prices should accurately reflect publicly available information and respond rapidly to new public information. So, when dishonest traders employ hidden information (through insider trading) or intentionally bring false information into a market (through market manipulation), market efficiency will dissipate [1] and trading activities may no longer closely follow public market information. Market movements that cannot be explained in the context of market information should raise surveillance specialists’ suspicion. In fact, previous studies have empirically found evidence that illegal trading activities make use of information before it appears on the market as publication information [11], which supports this rationale to detect market abuse. Therefore, we argue that effective financial market surveillance should integrate news and other market information with market activities.

## Meta-Requirements

In light of the efficient market hypothesis, effective MSSs should take into account not only market activities but also market information, which is the first metarequirement in our design theory in Figure 2. The use of manual news search in supervisory agencies reflects practitioners’ empirical sensing of the need for market information analysis in market surveillance. However, such efforts need to be formalized and automated in MSSs.

The analysis of market information raises several challenges in MSS design. As we know, there is a huge amount of market information depicting various financial events every day. This raises an information overload problem for human processing and digestion. In this research, we focus on textual market information such as news, which is the largest portion of market information. An effective MSS should alleviate the information overload problem by enabling automatic processing of textual market information [68]. (Other forms of market information, including multimedia information or quantitative information, is much less than the textual information. We leave the exploitation of such market information to future research.)

Automatic analysis of textual market information, such as news [60] and online discussions [13, 43, 66], has been previously applied in several finance-related applications. For example, Peramunetilleke and Wong [53] predicted currency exchange rates based on news headlines. Oh and Sheng [50] predicted stock price by using micoblog sentiments. However, these studies focus mainly on deriving the collective effect of market information on market indexes. In market surveillance, we need to assess the rationale behind individual transactions. Thus, textual analysis models adopted in MSSs need to have the capability to connect transactions with their possible related market information for risk assessment. The ability to automatically process a large amount of textual information corresponding to transactions is the second meta-requirement of our design theory in Figure 2.

Furthermore, the connections between market information and transactions are subtle and complicated. Although there is a great amount of market news, a very limited amount of such information directly mentions companies in each transaction. For this reason, traditional event extraction methods based on named entity matching [25] may not provide sufficient context information to determine the incentive behind a transaction. An effective MSS needs to have deep text comprehension capability to enable understanding of subtle messages embedded in news articles and identify indirect connections for news-driven market transactions to make an inference. It is also necessary to appropriately present such subtle messages and indirect connections to surveillance specialists to help them understand the market status and make a decision. This is the third meta-requirement of our design theory in Figure 2.

Text mining has been used in understanding financial textual content in previous studies. However, existing financial text mining studies [46] usually directly apply machine learning methods on linguistic features, such as bag of words [20, 23] and n-grams [62], to build classifiers. There have been efforts to enrich those basic features through using noun phrases, name entities [60], and sentiment lexicons [13, 64]. Those features focus on understanding individual documents. They do not directly address the concern of assessing individual transactions based on their connections with market information as is needed in market surveillance. As a result, the second and third meta-requirements of our design theory require innovative design in the design method part of the design process.

## Meta-Design

Given the meta-requirements derived from the kernel theories, the meta-design describes a class of artifacts hypothesized to satisfy the meta-requirements. In Figure 3, we present our meta-design for the basic components to be included in an effective MSS.

As suggested by the first meta-requirement, we use market activity analysis in conjunction with market information analysis in our proposed meta-design. For practical concerns, the two modules can be put in a sequential order, that is, first identify transactions not following regular trading patterns through market activity analysis, and then apply market information analysis to assess the risk associated with those transactions. This architectural design can reduce the computational capacity needed for processing market information, which also benefits the second meta-requirement. By filtering out a majority of normal transactions using market activity analysis, the design allows us to focus on those abnormal transactions for analysis.

In our meta-design, the market information analysis module is the major architectural improvement. Per the second and third meta-requirements, we propose to use text mining methods to analyze market information that can be connected with the suspicious transactions identified though market activity analysis, which is the first meta-design of the design theory. To enable efficient processing and deep text understanding, a machine learning approach can be employed to extract predictive features as surveillance cues to build risk classification models. As compared with other methods, such as rule-based methods, the machine learning approach requires less effort than generalizing heuristic rules from free-text. It can also evolve with the accumulation of training cases, which is done in supervisory agencies every day. As a result, this is one of the most popular approaches being applied in financial text mining studies [46] and in existing MSSs (for market activity analysis).

![](/api/attachments/CMJ8U2AN/fulltext/images/20ef3780b4437fe9298e749d3b5f58d541de852cb0220edb438fb1284d3d6709.jpg)  
Figure 3. A Meta-Design for Market Surveillance Systems

Furthermore, to address the third meta-requirement, the surveillance cues extracted by machine learning models, especially relations between market information and transactions, should be presented to surveillance specialists. This is the second metadesign of our design theory. Appropriate visualization will make it easier for surveillance specialists to understand reasons for model predictions. More important, visualizing prediction evidence makes surveillance specialists aware of the market context, which may help their entire work process. Note that MSSs always play a supporting role to surveillance specialists in market surveillance. It is the surveillance specialists’ final judgment based on many (subtle) factors that really matters. In practice, surveillance cue presentation is critical to the success of market surveillance tasks.

## Testable Design Product Hypotheses

Testable hypotheses are intended to assess whether the meta-design satisfies the meta-requirements [70]. From the design product perspective, the key issue to evaluate in our design theory is whether market information analysis is an indispensible component of MSSs.

In our meta-design, text mining is applied to assess the market information that can be associated with suspicious transactions identified from market activity analysis. From an information processing perspective, employing market information in MSSs provides more evidence to assess the risk of transactions. It would better to understand the relevant context and reasons for a suspicious transaction. For decision making in general and for text mining in particular, such extra evidence from textual market information would make it easier to identify market abuses. The richer evidence would also provide more detailed understanding of the transactions and more accurate risk assessments. Thus, we conjecture that incorporating market information analysis with market activity analysis can lead to more accurate assessment of transaction risk than using market activity measures alone.

In addition to providing overall risk assessments, the presentation of surveillance cues obtained from market information in our meta-design reduces surveillance specialists’ efforts in searching for and digesting news. By bringing together different aspects of information in the presentation, surveillance specialists can make their final judgments more easily. We conjecture that an integrated presentation of surveillance cues extracted from market information better meets users’ information requirements and improves system usability and surveillance effectiveness.

## The Design Process: Commonsense Knowledge-enhanced Textual Analysis

Since market activity analysis has been studied in several previous studies [12, 42], we focus on how market information analysis should be designed in the design process part, which we consider a more important part of our design theory. As pointed out by the meta-requirements (Figure 2), textual analysis for market surveillance requires deep text understanding abilities. In this section, we explore how to strengthen text understanding for market surveillance.

## Kernel Theories

In a financial market, market information influences transactions through traders. Traders’ decisions are based on their interpretation of the market information. Cognitive science has developed text understanding theory to explain humans’ text understanding process [54, 67], which sheds light on how we can model the processing of market information.

According to text understanding theory, the understanding of text happens at multiple levels [37, 38]. First, a person recognizes individual words, extracts basic meanings from sentences, and composes content semantics into a text model. Then, since there is often significant implicit or missing information in text, people use their prior knowledge to connect related information and construct a situation model to make inferences on what the text refers to [37].

In the text understanding process, prior knowledge plays an important role. People tend to match unfamiliar concepts and statements to familiar ones when processing new information. Matching prior knowledge assists humans’ text understanding both in connecting individual experiences with the situation model [22, 37] and decoding the information present in text for its semantic meanings. In fact, scientists have found biological evidence from electroencephalogram data on parallel integration of term semantics and prior knowledge reasoning when interpreting a sentence [29].

In a financial market, traders not only have their unique prior knowledge but also share a significant amount of common facts, information, rationales, and rules. In artificial intelligence studies, this prior knowledge an ordinary person is expected to have is conceptualized as commonsense knowledge [40]. In a financial market, commonsense knowledge shared by investors determines their collective understanding of market information and the regular trading decisions most people may make. Thus, commonsense knowledge should be beneficial in modeling normal financial market outputs and can help differentiate abnormal transactions from normal ones in MSSs. This process should be conducted following the two levels of the human text understanding process.

## Design Method

According to the meta-requirements of MSSs, it is necessary to make connections between a transaction and its relevant market information to better assess transaction risk. The text understanding theory suggests that commonsense knowledge can be employed to enrich such connections by improving understanding of market information at the situation and semantics levels. Thus, we propose mechanisms that match the two levels of roles played by commonsense knowledge in text understanding as the first two design methods.

To model the role of commonsense knowledge in two levels of text understanding, we take the most commonly used semistructured representation of commonsense knowledge, where commonsense concepts, facts, and their relations are represented as a graph structure (i.e., ontology). Concepts and entities (i.e., instances of concepts) are represented as nodes and commonsense relations between concepts/entities are represented as links in this graph. We suggest building a comprehensive knowledge base on previously developed commonsense knowledge bases to approximate the commonsense knowledge of traders used in financial markets.

As the first design method, we suggest using commonsense knowledge to enrich links between news articles and transactions, which is aligned with the role of commonsense knowledge in building a situation model for text understanding. This allows us to provide a complete picture of the transaction’s context. In news articles, commonsense concepts and entities may be discussed in various circumstances. Following the graph structure of commonsense knowledge, we will be able to identify their (indirectly) related concepts that may eventually connect to a transaction. From a transaction perspective, such a design can pull together multiple news articles talking about events related to the transaction. By explicating the intertwined relationship among different pieces of news articles and transactions, more textual features and surveillance cues can be developed to set up the inference context and aid both automatic and manual transaction risk assessment.

As the second design method, we suggest using commonsense knowledge to enrich the reference concepts related to words in news articles, which is aligned with the role of commonsense knowledge in decoding the semantics of sentences in text. By revealing reference concepts to words/terms in news articles, one can better understand the embedded subtle message the articles contain. For the commonsense concepts/entities in news articles, we can find more generic or specific concepts in commonsense ontologies to use as reference concepts. Including these reference concepts allows better understanding of the subtle messages in news articles.

The dual role of commonsense knowledge in a human’s cognitive process that is used to derive our two design methods has been used in several different applications. In terms of creating a comprehensive situation model, Lieberman et al. employed commonsense knowledge to understand the context of communications and provide smarter interactive interfaces [41]. In terms of understanding semantics of objects/words/sentences, a semantic smoothing approach has been developed to enrich linguistic features using hypernymy, hyponymy, meronymy, and holonymythe relations in WordNet for text classification and clustering [8, 34, 71]. Similar techniques were also applied on entities extracted from Wikipedia [21, 28] and Yago [7] for text mining.

The third design method we propose is to model and present the features generated using news–transactions relations and reference concepts with the help of commonsense knowledge bases. In general, machine learning models can be built to classify risks of transactions based on these features, which need to properly model the graph structure of commonsense knowledge. Furthermore, we suggest taking advantage of the graph presentation of commonsense knowledge to present the machine learning features to consumers. Since the features are generated upon commonsense ontology, it is straightforward to organize them (normally in the form of strings) to a commonsense ontology. Since the commonsense knowledge ontology was built to mimic human reasoning logic, it should be easy for surveillance specialist to understand its semantic links. The machine learning prediction and the graph presentations can ease surveillance specialists’ workload in understanding market information and risk assessment.

## Testable Design Process Hypotheses

With the enhancement of commonsense knowledge, we expect that market information analysis would be helpful to market surveillance. In this section, we present research hypotheses to evaluate the proposed design method principles.

Commonsense knowledge can help to capture the intertwined relationships between news articles and transactions. The impact of news articles on transactions may depend on their semantic relations with the transactions. For example, industry news would have a different impact as compared with company news. Thus, capturing the relationships can facilitate the assessment of market status and thus assist the disclosure of reasons for market activities. We conjecture that exploiting news–transaction relationships using commonsense knowledge will improve suspicious transaction identification performance.

Commonsense knowledge can assist in decoding terms and sentences in the news by providing reference concepts that are implied in text. As shown in previous text mining research, the richer set of features and reference concepts can help to decipher terms in each single piece of news, thus improving the understanding of news article contents. Therefore, we conjecture that providing reference concepts would assist suspicious transaction assessment.

Because identifying news–transaction relations provides a bigger picture and exploiting reference concepts improves comprehension of news, the two mechanisms may complement each other. We conjecture that combining them will cause an overall performance increase.

In practice, surveillance specialists often conduct market information analysis by searching in search engines. However, they still need to manually digest the news and infer its (indirect) impact on transactions. If the news–transaction relationships are extracted automatically, selected by their importance, and explicated by their logic, it will be easier for specialists to process information and judge transaction risk. In our proposed design methods, the graph presentation of features selected by machine learning models fulfills the requirements for information extraction, selection, and explication. Compared with traditional search engine methods, we conjecture that it can reduce human workload in searching and digestion, and improve surveillance effectiveness.

## An Instantiation of the Design Theory

As part of the design theory development process, we instantiate a prototypical system, MarketWatch, that manifests the proposed design principles for the design process and the design product. Figure 4 shows the system architecture of an MSS that considers public news as market information. The system supplements the existing industrial market activity analysis module with market information analysis to assess the risk of suspicious transactions. The system ranks suspicious transactions and reports the most risky ones for follow-up investigation. In practice, there is an expectation that high-risk transactions are accurately reported so that investigators can identify the real market abuses. The system incorporates commonsense knowledge to interpret relations between news and transactions and enrich features of the news articles. News associated with a suspicious transaction is used to assess the transaction’s risk. Since the influence of news on the market only lasts for a short time period, we just consider news from the last market close time to transaction time. As is done in many text mining studies, we take a feature-based approach to process news. We convert news features to transaction features and build classifiers for risk prediction.

![](/api/attachments/CMJ8U2AN/fulltext/images/54aeabc13e9ffa47331cb564d739234bdf35586f68097da51582590bad603c97.jpg)  
Figure 4. A System Architecture for News-aware Market Surveillance Systems

Our implementation of the MarketWatch system targets surveillance of the Hong Kong stock market. We incorporated three commonsense knowledge bases: OpenCyc (v2.0) [40]; DBpedia (v3.5) [3]; and the company profiles of the 1,361 companies on the HKEx, including company name, key person, location, industry, and so on. (We consider such information commonsense to Hong Kong stock market investors.) We connect these knowledge bases through OpenCyc-DBpedia links and manual matches between HKEx company profiles and DBpedia.

For our evaluation of the MarketWatch system, we adopt two major news sources (other news sources can be easily included when necessary). Bloomberg News covers major worldwide events and is widely used by investors when making decisions. Standard News is a local Hong Kong newspaper that began publishing news online in July 2008. Our system contains 104,455 articles published on Bloomberg’s Website in 2008 that are indexed by Google and 10,848 breaking news and 8,242 others news articles published online by Standard News between July and December 2008. To support further analysis, we derive linguistic features from news articles. We develop a parser program using LingPipe API [2] to extract n-gram features from news articles and remove stop words. We apply Porter’s algorithm for stemming. We conduct a small-scale experiment,<sup>2</sup> and choose 2-gram representation of each news article to balance between performance and computational cost.

In our design process, the major challenge is to enrich news features and assemble them to transaction features describing each transaction. We employ commonsense knowledge to address this problem. First, we connect news articles with transactions. Previously, such a connection was often made through company name matching. In this research, following the design methods of our design theory, we find connections between suspicious transactions and news through semantic links in commonsense knowledge bases. These connections with different lengths and through different types of links have different semantic meanings. For example, the link from the transaction company to its industry sector brings industry sector news into the model. A longer connection to another company in the same industry brings in competitor news to inspect suspicious transactions. We convert the semantic links to prefixes and attach them to news linguistic features to create transactional features describing suspicious transactions.

Second, we enrich news features by incorporating reference concepts in commonsense knowledge that are relevant to terms/words in news. Commonsense knowledge connects concepts and terms to more general and more specific concepts. In this research, we choose to use only upper-level relations indicating more general related concepts and sibling-level relations (alias) when enriching features since these semantic relations are reported to be more informative in previous research [71]. Similar to linguistic features, the reference concepts are attached to the semantic links between news–transaction connections to generate transactional features.

In the two methods, we limit the number of semantic links between news and transactions and between news terms and reference concepts to two for computational efficiency.

After feature generation, we apply information-gain-based feature selection using the Weka package [30]. We experiment with different machine learning algorithms, including SVM, decision tree, and Naive Bayes, and choose to implement Naive Bayes with the help of Weka due to its performance advantages in the small-scale tests.

At the final presentation step, the predictions generated by the machine learning classifier are presented together with the supporting evidence, that is, the most informative surveillance cues identified by the feature selection algorithm. We take advantage of the commonsense knowledge structure and develop a graph representation of surveillance cues to support surveillance specialists’ judgments. The interface is composed of five components (Figure 5). The upper panel lists suspicious transactions identified by market activity-based tools. Users (surveillance specialists) can choose to focus on certain types of transactions based on stock code and transaction time. When selecting a transaction, the system analyzes its associated news and assesses its risk level. The prediction result, reported below the upper panel, is read as ‘No Further Action’ in this example. In the left panel, the system shows a list of news articles and the market trend (in a line chart) around transaction time. The left panel provides the most basic contextual information for surveillance specialists’ convenience. In the right panel, the system visualizes the relationships between focal suspicious transactions and related news in a graph, connected by commonsense concepts and relations. It should be noted that the relations shown are only the most informative ones after feature selection. To keep the graph easy to understand, we do not directly visualize features on the graph. Instead, we provide news titles and contents in float windows. The relations among news and transactions combined with the system’s predictions can help surveillance specialists judge whether a suspicious transaction needs further investigation.

![](/api/attachments/CMJ8U2AN/fulltext/images/63dc499e2952c12182a77e330b764c863212453a7f5232271af0a0e374eaed16.jpg)  
Figure 5. MarketWatch System Interface

As compared with the news analysis functionalities in existing MSSs, the major advantage of MarketWatch is that it explicates the relations between news and transactions using common-sense knowledge to enrich transaction features. Extracted and selected by machine learning methods, such features are richer and more flexible than predefined rules such as those used in SONAR. Moreover, MarketWatch provides assessments of transaction risks as well as presenting the transaction features in a graph presentation. The graph presentation will also reduce surveillance specialists’ digestion effort. We intend to present all information in the five components to support surveillance specialists’ judgment.

## Validation of the Design Theory

Evaluating the hypotheses on our design product and design process require different efforts. On the design process side, the evaluation focuses on whether our proposed design methods are effective as compared with existing text mining approaches. On the design product side, the evaluation focuses on whether market information is effective as compared with using only market activity analysis in MSSs. Table 2 illustrates our evaluation on the two sides of the design theory. We conduct computational experiments to examine the performance of the classifier for transaction risk assessment and collect user comments from surveillance specialists to assess the perceived usability of the MarketWatch system design.

## Evaluation Framework

## Experiment Evaluation Framework

MSS performance is usually measured based on the ability to differentiate normal transactions from illegal/high-risk ones. Since our research focuses on the market information analysis module conducted after market activity analysis, the experiment evaluation calculates the ability of this module to assess risk of suspicious transactions detected by market activity analysis. In a supervisory agency, predicted highrisk transactions will be subject to further investigation.

For evaluation purposes, we mimicked a regular market activity investigation process and compiled a data set of suspicious transactions in the Hong Kong stock market from July 13, 2008, to December 31, 2008. Focusing on 700 companies that claimed to have unusual price movements on the HKEx Website during that time, we identified 1,913 suspicious transactions with the help of a domain expert from the Hong Kong stock market’s supervisory agency using a state-of-the-art surveillance system. The domain expert manually inspected these suspicious transactions and coded them as either normal or illegal/high-risk based on his experience, public news, and other available information. The result is 1,352 normal transactions and 561 high-risk ones (which need further investigation). The domain expert’s coding is considered as the gold standard. We then evaluate MSS performance by checking whether their predictions are the same as the domain expert’s judgment.

Table 2. An Overview of the Evaluation Process

<table><tr><td></td><td>Design process</td><td>Design product</td></tr><tr><td>Experiment</td><td>Performance of two feature enrichment mechanisms over traditional text miningRepresentative textual surveillance cues</td><td>ROC curve comparison using only market activity analysis</td></tr><tr><td>User comments</td><td>Subjective assessment of surveillance cue graph presentation</td><td>Subjective assessment of the entire system</td></tr><tr><td colspan="3">Note: ROC—receiver operating characteristic.</td></tr></table>

For the design process evaluation, we adopt precision, recall, and F-measure as performance evaluation metrics for the suspicious transaction classification task, where we consider high\_risk transactions as positive. Precision measures the proportion of correctly predicted high\_risk transactions (Equation [1]). Recall measures the coverage of predicted high\_risk transactions (Equation [2]) in the entire data set. To effectively combat market abuses, we need high recall to avoid mistaking illegal activities as normal ones. To reduce unnecessary follow-up investigations, high precision is needed to avoid mistaking normal activities as illegal ones. In automatic classification, precision and recall usually conflict with each other. Thus, we use the F-measure, which combines the two measures (Equation [3]), as an overall evaluation metric. In general, a higher F-measure indicates better performance.

$$
P r e c i s i o n = \frac {\text { Number   of   Correctly   Predicted   High\_risk   Transactions }}{\text { Total   Number   of   Predicted   High\_risk   Transactions }}\tag{1}
$$

$$
\text { Recall } = \frac {\text { Number   of   Correctly   Predicted   High\_risk   Transactions }}{\text { Total   Number   of   High\_risk   Transactions }}\tag{2}
$$

$$
F = \frac {2 * P r e c i s i o n * R e c a l l}{P r e c i s i o n + R e c a l l}.\tag{3}
$$

To evaluate the design product, we need to compare MSSs with, versus without, a market information analysis module. Note that the data are postmarket activity analysis. Therefore, we rank suspicious transactions according to our system’s predicted risk level and compare it with market activity-based ranking, which is often used in supervisory agencies to shortlist suspicious transactions due to their resource limitations. We use the receiver operating characteristic (ROC) curve to compare how the two types of rankings differ when varying the number of suspicious transactions. The ROC curve is created by plotting the true positive (correctly classified high-risk transactions) rate against the false positive (incorrectly classified high-risk transactions) rate by assuming a different number of highly ranked transactions as illegal according to prediction confidence. Since people prefer a higher true positive rate given the same false positive rate, an ROC curve closer to the upper left corner indicates better performance. The best possible ROC curve goes through the upper left corner of the ROC space, representing that the model will never make any false negatives or false positives. A completely random guess would show as a diagonal line (from the bottom left to the top right corners) on the diagram, where the percentages of false negatives and false positives are equal.

## User-based Evaluation

In addition to the computational experiments, we invite human subjects from supervisory agencies to evaluate the system. There is only a small group of surveillance specialists in the supervisory agencies; they have a unique skill set that is not representable by other groups, say, graduate students. Thus, we cannot conduct a large-scale user study or survey (and cannot provide statistical hypotheses testing on this perspective). We made an effort to invite surveillance specialists at different ranks and with firsthand experience of daily surveillance operations to give a meaningful and relevant assessment of the system. (It is also possible to conduct evaluations with surveillance specialists in multiple supervisory agencies. However, due to the sensitive nature of market surveillance, there are practical difficulties in doing so and we have not achieved that. We leave cross-evaluation with multiple supervisory agencies to future research.) We interviewed four specialists, including a senior director (no longer involved in daily alert inspection), a senior manager (occasionally involved in daily alert inspection), a manager (partially involved in daily alert inspection), and an assistant manager (involved in daily alert inspection). Although the size of the subject pool is small, given these subjects’ experience and expertise, we believe that their comments are valuable and meaningful to practice.

## Evaluation of the Design Process

## Experimental Procedure

The state of the art in market information analysis uses name matching to find news and employs linguistics features for the analysis. This is the baseline (BL) for our research. In our design, we propose two feature enrichment mechanisms: identifying news–transaction relations (NTR) and reference concepts (RC) with the help of commonsense knowledge. We also combine the two mechanisms (CB) to enrich the feature set. We conduct feature selection and build the binary classifier using these four feature sets. We conduct 10-fold cross validation 30 times for (fold-level) pairwise t-tests.

With the specified evaluation metrics and four feature sets, we can operationalize the performance-related hypotheses on the design process of our design theory as follows:

PROC-1: Utilizing commonsense knowledge to exploit news–transaction relations (i.e., NTR) in market information analysis will result in higher suspicious transaction classification F-measures than not using such relations (i.e., BL).

PROC-2: Utilizing commonsense knowledge to exploit reference concepts (i.e., RC) in market information analysis will result in higher suspicious transaction classification F-measures than not using such information (i.e., BL).

PROC-3: Utilizing commonsense knowledge to explore both news–transaction relations and reference concepts (i.e., CB) in market information analysis will lead to higher suspicious transaction classification F-measures than using one type of mechanism (i.e., NTR and RC).

## Performance over Traditional Text Mining

Table 3 reports our experimental results. When using the baseline features, only 24 instances are classifiable, with an average of 6 instances classified as normal and exempted from human investigation. Although these predictions were 100 percent correct, this does not help surveillance specialists much, since they still need to manually screen the other transactions. When employing news–transaction relations to enrich features (NTR), we notice a significant improvement of recall (71.30 percent) and F-measure (53.87 percent), although the precision is reduced to 43.29 percent. When we employ reference concepts (RC) to enrich features, there is only a slight increase of recall and F-measure (and a slight decrease) as compared with the BL. It classified only about 8 instances as high-risk among the 39 classifiable instances. If we combine the two feature enrichment mechanisms, the prediction performance has a joint advantage on precision, but reduced recall a little bit. In pairwise t-test results based on 30 rounds of experiments, most hypotheses are supported at the 99 percent confidence interval. Specifically, the features enhanced by news–transaction relations (NTR in PROC-1) or reference concepts (RC in PROC-2) were all significantly better than the baseline model (BL); combining the two feature enrichment mechanisms (CB in PROC-3) resulted in an improved prediction performance over RC but not over NTR.

Obviously, exploring the relationship between news articles and transactions through commonsense knowledge provides us with a richer set of features to better judge suspicious transactions’ risk. Our results show that it is the most important factor of the success of text mining in market surveillance. Without such enrichment, suggested by the text understanding theory, we can only show the value of text mining in MSSs. In practice, articles directly referring to transactions’ companies are sparse. Using commonsense knowledge can help in recognizing indirectly related news articles, which could help interpret investors’ decisions. For market information-based analysis, the recall reaches a much higher level while precision is acceptable. Supervisory agencies could confidently allocate less effort in dealing with the transactions predicted to be normal. In general, considering commonsense knowledge in the design process of our design theory is an important innovation and is a venue with high potential to alleviate the market surveillance problem.

Table 3. Transaction Risk Prediction Performance (n = 1,913)

<table><tr><td>Model</td><td>Precision, %</td><td>Recall, %</td><td>F-measure, %</td></tr><tr><td>Name matching (BL)</td><td>100.00</td><td>1.07</td><td>2.12</td></tr><tr><td>News–transaction relation (NTR)</td><td>43.48</td><td>71.16</td><td>53.97</td></tr><tr><td>Reference concept (RC)</td><td>88.89</td><td>1.43</td><td>2.81</td></tr><tr><td>Combined (CB)</td><td>43.97</td><td>68.00</td><td>53.41</td></tr></table>

## Representative Textual Surveillance Cues

We investigate CB surveillance cues used in suspicious transaction assessment. Table 4 summarizes these features. If we only inspect news with a company’s identity, that is, if the news has a direct connection with the transaction, there are only a small number of features (19) related to a small number of suspicious transactions (24). In the example in Table 4, the news directly referring to PCCW contains some words, such as lose, reduce, plunge, sell, earn, and so on, that can be modeled by text mining algorithms for the transaction’s risk assessment.

When there is one semantic link connecting news with transactions, most features are related to industry, location, and personnel of the suspicious transaction’s company. Among these features, the ones from industry-related news are the most prominent, contributing more than 18,000 features that can connect 1,546 suspicious transactions to news articles. For example, the features related to “AAC Acoustic Technologies Holdings Inc.” through the “Company → Industry” relationship are news about “Hardware,” the company’s industry. In our data set, this news contains words such as plunge, decline, and loss, which can be modeled by text mining algorithms. Consistent with our intuition, industry sector news provides significant implications for trading activities related to companies in the industry. If a suspicious transaction shows a different pattern from the industry’s news trends, there is good reason to suspect its purpose. We also notice that key company personnel can provide a unique perspective for surveillance. Although there are only 265 suspicious transactions with such information, incorporating key company personnel provides about 8,000 features to support our analysis.

Table 4. Example Textual Surveillance Cues

<table><tr><td>Cue category</td><td>Instances</td><td>Features</td><td>Examples</td></tr><tr><td colspan="4">Directly connected news and transaction</td></tr><tr><td>Company</td><td>24</td><td>19</td><td>(PCCW) lose, reduce, plunge, sell, earn ...</td></tr><tr><td colspan="4">One semantic link between news and transaction</td></tr><tr><td>Company → Industry</td><td>1,546</td><td>18,588</td><td>(AAC Acoustic Technologies Holdings Inc. → Hardware) plunge, decline, loss ...</td></tr><tr><td>Company → Location</td><td>1,547</td><td>9,135</td><td>(AviChina Industry &amp; Technology Co. Ltd → Beijing) drop, slump, shrink ...</td></tr><tr><td>Company → Person</td><td>265</td><td>8,313</td><td>(Esprit → John Poon) success, hire, resign ...</td></tr><tr><td colspan="4">Two semantic links between news and transaction</td></tr><tr><td>Company → Parent company → Key person</td><td>22</td><td>6,432</td><td>(Hutchison Harbour Ring Ltd. → Hutchison Whampoa → Sir Li Ka-shing) increase, stake ...</td></tr><tr><td>Company → Parent company → Location</td><td>13</td><td>6,078</td><td>(Cathay Pacific Airways → Dragonair → Hong Kong) improve, fell, lowest ...</td></tr><tr><td>Company → Region served → Largest city</td><td>145</td><td>961</td><td>(Hutchison Telecommunications International Ltd. → Sri Lanka → Colombo) attack, damage ...</td></tr></table>

When there are two semantic links between news and transactions, the semantic meanings of cues increase significantly, while the number of features of each type decreases. Among all those features, the “Company → Parent company → Key person” relationship, that is, influential person in the industry, provides 6,432 features. They obviously influence decisions on their related 22 transactions. News related to the location of a company and its parent company also plays a role in determining the risk of suspicious transactions.

## Subjective Assessment of Surveillance Cues Presentation

Table 5 presents our excerpted interview results (on both design process and design product). In general, the assistant manager was the most positive about using the system while the senior manager was the most conservative.

For the subjective assessment of our design process, we focus on the effect of the graph presentation of cues for surveillance specialists. Following previous research [14, 33], we check whether the interface provides them with relevant information that makes their judgment more efficient than a news list. We also verify whether the graph presentation is easier to understand and use than news query tools such as a search engine.

After testing the system, all subjects felt that the shortlisted news on the graph (with the help of commonsense knowledge) is a useful functionality. It provides “more targeted” information than a full list of news and can be used as “a quick reference,” while the full list of news can help “look for . . . other related information.” They stated that the graph presentation “is easier to see” and “saves . . . time and effort in searching for relevant news.” While keyword-based searching is more flexible and “can be controlled by the user,” “the shortlisted news in a graph provides what requires a few searches and would save some effort.” The graph presentation “is useful as a first screening.” They agree that they can “get similar results by keyword search sometimes.”

In terms of the ease of use of the interface, although “sometimes [the interface] gets too crowded,” all subjects agreed that the graph presentation “is understandable” and explicating the commonsense relations between news and transactions “reduce[s] the [mental] effort needed” to reason. One manager stated, “If the links [between news and transactions] are accurate,” then they can save us time in understanding the impact of news events.” The subjects feel the graph presentation “is certainly easier to use” than keyword search (with a list view) “since [they] don’t have to actively search for relevant news.”

<sub>.</sub> <sub>Assess</sub>m<sup>ent</sup> <sup>by</sup> <sup>Human</sup> <sup>S</sup>

<table><tr><td rowspan="2">Position</td><td>Subject 1</td><td>Subject 2</td><td>Subject 3</td><td>Subject 4</td></tr><tr><td>Assistant manager</td><td>Manager</td><td>Senior manager</td><td>Senior director</td></tr><tr><td>Clearing Alerts</td><td>Regularly</td><td>Sometimes</td><td>Used to</td><td>Used to</td></tr><tr><td>Aspects</td><td colspan="4">Major Comments</td></tr><tr><td colspan="4">Design process (News Graph Presentation)Useful to provide relevant infoThe graph is better [than list view] as it is more targeted.It saves me time and effort.Keyword-based searching is useful when user needs to target specific articles and the shortlisted news [i.e., graph presentation] is useful as a first screening.I could get similar results by keyword search sometimes.It is useful overall. The way it presents the news graphically is convenient.I think the shortlisted news in graph provides what requires a few searches and would save some effort.It does reduce the effort needed.But it is lacking in search capability. It is generally useful.The graph is good for a quick reference. The full list is useful when we need to look for other news that tells us, for instance, the broad market environment and other related information.Keyword-based searching is more targeted and can be controlled by the user. But presenting the news that the system guessed is related would help at the very first stage.(continues)</td><td></td></tr></table>

<table><tr><td rowspan="2">Position</td><td>Subject 1</td><td>Subject 2</td><td>Subject 3</td><td>Subject 4</td></tr><tr><td>Assistant manager</td><td>Manager</td><td>Senior manager</td><td>Senior director</td></tr><tr><td>Clearing Alerts</td><td>Regularly</td><td>Sometimes</td><td>Used to</td><td>Used to</td></tr><tr><td>Aspects</td><td colspan="4">Major Comments</td></tr><tr><td>Ease of use (than news search)</td><td>Of course it is easier, since I don&#x27;t have to actively search for relevant news.I think the interface is quite intuitive.</td><td>It is certainly easier to use. But it will only be effective if it is also accurate in presenting the relations between those news.Sometimes it gets too crowded.</td><td>Yes, it is easier to see.It seems easy to use.</td><td>It does reduce the effort needed.The graph is understandable.I would say graph presentation is easy to use compared to list view.</td></tr><tr><td colspan="5">Design product (The Integrated System)</td></tr><tr><td>Useful for risk assessment</td><td>It will help in identifying suspicious activities.I like how news and price information are displayed together so that it is easier to judge alerts according to prevailing news events.</td><td>Yes, to a certain extent, but human verification is still needed.</td><td>I don&#x27;t think we will rely on that to make a judgment. We have to assess the alerts based on transaction details, market news, and our experiences and expertise.</td><td>I would say that the idea to incorporate news content in automating alerts generation is useful, if the risk assessment is indeed accurate.The best aspect would be the incorporation of news content and their relationship with each other.</td></tr><tr><td>User information satisfaction</td><td>I think it meets the needs when taking a first glance at the alerts, although further investigation in the transaction details is needed to reach conclusions.</td><td>Yes, definitely [meets our information need]. In fact, information from news is routinely used in conjunction with market activities information in daily investigation and surveillance.</td><td>Yes it does [meet our information need].</td><td>Yes of course [meets our information need]. We have always used news together with transaction data, this system is just an attempt to partially automate the news analysis part.</td></tr></table>

The user comments indicate that the graph presentation of the surveillance cues (mainly intertwined relations between news and transactions) is useful and is easy to use.

## Evaluation of the Design Product

## Performance Compared to Market Activity Only

To assess the benefit of incorporating market information analysis into MSSs, we compare the performances of using, versus not using, market information analysis in ranking the risk of suspicious transactions.<sup>3</sup> In practice, surveillance specialists usually filter the suspicious transactions based on price change rate or transaction volume and focus more on transactions with a higher trading volume or a bigger price change. Given that market information analysis brings more context information into risk assessment, we conjecture that our proposed market information analysis has better ROC curves than those rules-of-thumb.

Figure 6 compares the CB method in our MarketWatch prototype with the two dominant ranking methods in practice. Obviously, the CB method incorporating market information analysis provides a more accurate assessment of the transaction risk ranking. Market information analysis has the potential to help surveillance specialists better allocate their time on different transactions. It is interesting to note that the ROC curve of price-based ranking is close to a random ranking, indicating that the price change rate is not very helpful in the risk assessment stage. The ROC curve of transaction volume-based ranking is more accurate than price-based ranking. However, it is still much worse than a market informationbased solution. This result provides strong support for incorporating market information analysis into MSS.

![](/api/attachments/CMJ8U2AN/fulltext/images/a4f936d3bb69b197e81ce9b0c6052f384afb5759e64586751b1c0e7547899096.jpg)  
Figure 6. Performance Improvement using Market Information Analysis

## Subjective Assessments of Market Information Analysis in MSSs

To assess surveillance specialists’ opinions on the role of market information analysis in MSSs, we collected comments on perceived usefulness and user (information) satisfaction [14] on our system. Specifically, we assess whether the prediction results from market information analysis are useful for final assessment and whether the market information analysis module meets surveillance specialists’ information need in their work. In light of the kernel theories, we conjecture that incorporating market information analysis in MSSs improves their usability.

In interviews, the subjects commented that market information analysis is a useful module that “help[s] in identifying suspicious activities.” Although “human verification is still needed,” “the idea to incorporate news content in automating alerts generation is useful, if the risk assessment is indeed accurate.” They feel the most helpful part of the system is “the incorporation of news content and their relationship with each other.” Furthermore, “news and price information are displayed together so that it is easier to judge alerts according to prevailing news events.”

In terms of user (information) satisfaction, all subjects agreed that the system is able to help them fulfill their information requirements in their daily work. They comment that “information from news is routinely used in conjunction [with] market activities information in [their] daily investigation and surveillance”; “the use of news is always a crucial part in identifying suspicious activities”; “[they] have always used news together with transaction data”; and the system is “an attempt to partially automate the news analysis part.” The system meets the need of their job responsibilities “when taking a first glance at the alerts, although further investigation in the transaction details is needed to reach conclusions.”

In general, comments from the surveillance specialists show that market information analysis should be used together with market activities analysis in MSSs to provide a more comprehensive assessment of suspicious transactions and (partially) automate surveillance specialists’ work. It should be noted that this conclusion is based on the design process part of our design theory. In interviews, we also noted that several managers consider their existing semi-manual processing of news search and digestion as a type of market information analysis.

## Discussion

In the experiments, our prototypical system illustrates significant performance improvement on the recall of suspicious transactions. If we use only the features on news identified through name entity matching, market information analysis can capture only a handful of suspicious transactions. After incorporating the two feature enrichment mechanisms suggested by our design theory, market information analysis can identify about 70 percent of the suspicious transactions with a reasonable level of noise, which shows the possibility of automating tedious manual process in market surveillance. The performance improvement is mainly attributed to the identified relationships between news and transactions.

In addition to the assessment of transaction risk, the MarketWatch system uses the graph structure of commonsense knowledge to visualize surveillance cues selected by machine learning algorithms. Such a presentation can facilitate surveillance specialists’ understanding of a transaction’s situation. According to user comments, the graph presentation makes it easy for surveillance specialists to comprehend surveillance cues. The graph structure highlights the relations between transactions and news, hides some less important features, and improves surveillance specialists judgments by providing a complete picture of the market.

Collectively, the evaluation results of the MarketWatch system lend credence to the notion that market information analysis could help alleviate the market surveillance problem if equipped with commonsense knowledge-enhanced text mining tools. The approach that uses both market information and activity analyses has better ROC than that solely relying on market activity analysis. The integration of market information analysis into MSS improves user perceived usefulness and user (information) satisfaction with the MSS.

## Implications

From a theoretical perspective, our paper follows the full structure of Walls et al.’s framework [69, 70], which allows us to assess both the design product and the design process in one integrated design theory and enables the examination of three related aspects of MSS design: information, feature, and presentation. Our research provides an instantiation of this framework, showing the possibility of using this comprehensive framework to develop theories. Through the development and evaluation of the design theory, our paper leads to the following design principles along with a manifestation of their feasibility [32]:

1. Both market activity analysis and market information should be included in MSS. Omitting market information is theoretically problematic and practically less effective.

2. When conducting market information analysis, it is beneficial to leverage commonsense knowledge to (a) develop a comprehensive picture of intertwined relations between news and transactions, and (b) capture subtle messages of news through semantically relating concepts embedded in news.

3. A presentation that uses the graph structure of commonsense ontology to organize surveillance cues increases the interpretability of the text mining results.

From a practical perspective, our derived design guidelines have significant implications for financial investors, researchers, and surveillance agencies who work on MSS research. Our research provides justifications for leveraging market information in the market surveillance task. As shown in our experiments, the MarketWatch system is able to identify the risk associated with suspicious transactions efficiently and effectively. Using the theoretical arguments and practical examples, we hope practitioners can put more focus on the use of textual analysis in market surveillance. Given the critical role that financial markets play in the global economy and the explosive growth of illegal trading activities, adding effective market information analysis functions to market surveillance with the help of commonsense knowledge has significant economic impact. As shown in previous research, the improvements to MSSs can also improve market efficiency [31], which has a deep impact on investors and the economy.

## Limitations

This study has some limitations. First, in this research we mainly inspect the role of commonsense knowledge in text mining-based market surveillance. Other design mechanisms may exist that can be used to tackle the market surveillance problem. There may also be other design elements that need to be considered. For example, in this paper, we use relatively simple text mining algorithms to illustrate our design theory. There is room to improve the text mining model and develop more complicated text mining solutions for this problem following our proposed design theory. In addition, we use news articles to exemplify our design theory. Other types of market information, such as financial statements, online discussions, and governmental reports, may also influence the market and can be integrated into our framework. Further, the experiments show a relatively small performance improvement when combining the two mechanisms (NTR and RC) together. It is worth studying the reasons for this in the future.

Second, as in other data mining studies, the improvement on recall is achieved at the cost of lower precision (and a waste of case investigation resources). Although the ROC curve shows an overall improvement of our approach over existing practices, it is worthwhile to assess supervisory agencies’ preferences on the two aspects for better setup of MSSs. Moreover, as the users of other decision support systems [17], surveillance specialists’ behaviors may be changed by MSSs, which will further change the design of MSSs in future.

Third, the evaluation of our design theory is based mainly on one stock market. It is possible to extend the application and evaluation of our design theory to other supervisory agencies, which can improve the generalizability of our proposed design theory.

## Conclusions

In this research, we develop a design theory for MSSs. Based on the kernel theory of efficient market hypothesis, we propose to incorporate market information analysis with market activity analysis to create an effective MSS. Based on the kernel theory of text understanding theory, we propose two mechanisms regarding effective market information analysis in MSSs, namely, using commonsense knowledge, (1) to identify the intertwined relationships among news articles and transactions so as to understand the transaction’s context, and (2) to reveal reference concepts to words/terms in news articles so as to understand the news more accurately. Our design theory suggests modeling these two mechanisms in MSSs.

Following the design science paradigm, we developed a prototypical system, MarketWatch, to evaluate the effectiveness of the proposed design theory in the context of the Hong Kong stock market. Both computational experiments and human subject assessments show the effectiveness of our proposed design theory as compared with existing practices. In particular, we found that the identified relationships between news and transactions play an important role in helping to address the surveillance task in our framework. Our design theory can reduce surveillance specialists’ workload and support their judgments in surveillance. Collectively, this research lends credence to the notion that market information analysis could help alleviate the market surveillance problem if equipped with commonsense knowledge-enhanced text mining tools.

The paper instantiates the full structure of Walls et al.’s framework [69, 70], which assesses both the design product and the design process in building a design theory of MSSs. The developed design theory highlights the synergy of commonsense knowledge-supported text understanding in addressing the market surveillance problem, which, to the best of our knowledge, is the first in the literature. Through this research, we intend to promote studies examining the role of text mining in market surveillance.

Practically, the design theory we built up can help in identifying the risk associated with suspicious transactions efficiently and effectively. Given the critical role that financial markets play in the global economy and the explosive growth of illegal trading activities, advances in MSSs have significant impacts on financial markets, investors, and the economy.

In the future, we will continue to explore the theoretical and practical issues of the design theory of MSSs. We will explore other design mechanisms, improve the text mining models, incorporate other types of market information, and strengthen the applications and evaluations of our framework . We will continue to strengthen our design theory and improve its generalizability in our future research.

## NOTES

1. Since news is the major influential market information, we use news and market information interchangeably.

2. We also experimented with POS features using the Stanford POS tagger [65], sentiment features using SentiWordNet [6], and features from different parts of news, such as news title or news content as in previous financial text mining studies [42]. These features do not provide significant performance difference. We thus use the basic representation in this paper.

3. We do not do binary classification since we do not know the threshold used in industry in market activity analysis.

## REFERENCES

1. Aggarwal, R.K., and Wu, G. Stock market manipulations. Journal of Business, 79, 4 (2006), 1915–1953.

2. Alias-i. 2015. http://alias-i.Com/lingpipe. (accessed April 20, 2015).

3. Auer, S.; Bizer, C.; Lehmann, J.; Kobilarov, G.; Cyganiak, R.; and Ives, Z. Dbpedia: A nucleus for a web of open data. In 6th International Semantic Web Conference. Busan, Korea: LNCS, Springer, 2007, pp. 722–735.

4. Augustin, P.; Brenner, M.; and Subrahmanyam, M.G. Informed options trading prior to M&A announcements: Insider trading? 2014. http://ssrn.com/abstract=2441606. (accessed April 20, 2015).

5. AWACS. 2015. http://www.3i-infotech.Com/content/capital\_market/stock\_exchange\_ surveillance\_system.Aspx. (accessed April 20, 2015).

6. Baccianella, S.; Esuli, A.; and Sebastiani, F. Sentiwordnet 3.0: An enhanced lexical resource for sentiment analysis and opinion mining. In 7th Conference on International Language Resources and Evaluation, Valletta, Malta: European Language Resources Association (ELRA), 2010, pp. 19–21.

7. Baralis, E.; Cagliero, L.; Jabeen, S.; Fiori, A.; and Shah, S. Multi-document summarization based on the Yago ontology. Expert Systems with Applications, 40, 17 (2013), 6976–6984.

8. Bloehdorn, S.; Hotho, A.; and Staab, S. An ontology-based framework for text mining. LDV Forum: GLDV Journal for Computational Linguistics and Language Technology, 20, 1 (2005), 87–112.

9. Caruthers, R. NYSE to switch its market surveillance from FINRA to NYSE regulation subsidiary. FierceFinanceIT, 2014. http://www.fiercefinanceit.com/story/nyse-switch-its-mar ket-surveillance-finra-nyse-regulation-subsidiary/2014-10-07 (accessed April 20, 2015).

10. Comerton-Forde, C., and Rydge, J. Market integrity and surveillance effort. Journal of Financial Servies Research, 29 (2006), 149–172.

11. Cornell, B., and Sirri, E.R. The reaction of investors and stock-prices to insider trading. Journal of Finance, 47, 3 (1992), 1031–1059.

12. Cumming, D., and Johan, S. Global market surveillance. American Law and Economics Review, 10, 2 (2008), 454–506.

13. Das, S.R., and Chen, M.Y. Yahoo! For Amazon: Sentiment extraction from small talk on the web. Management Science, 53, 9 (2007), 1375–1388.

14. DeLone, W.H., and McLean, E.R. The DeLone and McLean model of information systems success: A ten-year update. Journal of Management Information Systems, 19, 4 (2003), 9–30.

15. Diaz, D.; Theodoulidis, B.; and Sampaio, P. A unified framework for financial market monitoring systems. 2010. http://ssrn.com/abstract=1561663 (accessed April 20, 2015).

16. Drummond, M. Asic targets insider traders with new \$44m surveillance system. AFR Weekend, 2013. http://www.afr.com/news/asic-targets-insider-traders-with-new-44m-surveil lance-system-20131124-iysqv (accessed April 20, 2015).

17. Elkins, A.C.; Dunbar, N.E.; Adame, B.; and Nunamaker, J.F. Are users threatened by credibility assessment systems? Journal of Management Information Systems, 29, 4 (2013), 249–261.

18. Fama, E. Efficient capital markets: A review of theory and empirical work. Journal of Finance, 25, 2 (1970), 383–417.

19. Frisen, M. Methods and evaluations for surveillance in industry, business, finance, and public health. Quality and Reliability Engineering International, 27, 5 (2011), 611–621.

20. Fung, G.P.C.; Yu, J.X.; and Lam, W. News sensitive stock trend prediction. In 6th Pacific-Asia Conference on Knowledge Discovery and Data Mining. Taipei, 2002, pp. 481–493.

21. Gabrilovich, E., and Markovitch, S. Feature generation for text categorization using world knowledge. International Joint Conferences on Artificial Intelligence, Edinburgh, Scotland: AAAI Press, 2005, pp. 1048–1053.

22. Gerrig, R., and McKoon, G. The readiness is all: The functionality of memory-based text processing. Discourse Processes, 26, 2–3 (1998), 67–86.

23. Gidofalvi, G. Using news articles to predict stock price movements. Technical Report, Department of Computer Science and Engineering, University of California, 2003.

24. Glovin, D., and Voris, B.V. Rajaratnam guilty on all counts in U.S. insider-trading case. Bloomberg, 2011. http://www.bloomberg.com/news/articles/2011-05-11/rajaratnam-is-foundguilty-of-all-counts-in-galleon-insider-trading-trial. (accessed April 20, 2015).

25. Goldberg, H.; Kirkland, J.; Lee, D.; Shyr, P.; and Thakker, D. The NASD securities observation, news analysis & regulation system. In Conference on Innovative Applications of Artificial Intelligence. Acapulco, Mexico, 2003, pp. 11–18.

26. Green, T. Economic news and the impact of trading on bond prices. Journal of Finance, 59, 3 (2004), 1203–1234.

27. Gregor, S., and Hevner, A.R. Positioning and presenting design science research for maximum impact. MIS Quarterly, 37, 2 (2013), 337–355.

28. Gupta, R., and Ratinov, L. Text categorization with knowledge transfer from heterogeneous data sources. In 23rd AAAI Conference on Artificial Intelligence. Chicago, 2008, pp. 842–847.

29. Hagoort, P.; Hald, L.; Bastiaansen, M.; and Petersson, K.M. Integration of word meaning and world knowledge in language comprehension. Science, 304, 5669 (2004), 438–441.

30. Hall, M.; Frank, E.; Holmes, G.; Pfahringer, B.; Reutemann, P.; and Witten, I.H. The Weka data mining software: An update. SIGKDD Explorations, 11, 1 (2009), 10–18.

31. Harris, F.H.D.; Aitken, M.J.; and Ji, S. Trade-based manipulation and market efficiency after the introduction of real-time surveillance: A cross-market comparison. 2011. http://ssrn. com/abstract=1890928 (accessed April 20, 2015).

32. Hevner, A.R.; March, S.T.; Park, J.; and Ram, S. Design science in information systems research. MIS Quarterly, 28, 1 (2004), 75–105.

33. Hu, P.J.H.; Zeng, D.; Chen, H.C.; Larson, C.; Chang, W.; Tseng, C.J.; and Ma, J. System for infectious disease information sharing and analysis: Design and evaluation. IEEE Transactions on Information Technology in Biomedicine, 11, 4 (2007), 483–492.

34. Hung, C.L.; Wermter, S.; and Smith, P. Hybrid neural document clustering using guided self-organization and wordnet. IEEE Intelligent Systems, 19, 2 (2004), 68–77.

35. Jeeman, J., and Robert, S. Samuelson’s dictum and the stock market. Economic Inquiry, 43, 2 (2005), 221–228.

36. Khan, A.M. Conformity with large speculators: A test of efficiency in the grain futures market. Atlantic Economic Journal, 14, 3 (1986), 51–55.

37. Kintsch, W. The role of knowledge in discourse processing: A construction-integration model. Psychological Review, 95, 2 (1988), 163–182.

38. Kintsch, W., and Vandijk, T.A. Toward a model of text comprehension and production. Psychological Review, 85, 5 (1978), 363–394.

39. Kirkland, J.D.; Senator, T.E.; Hayden, J.J.; Dybala, T.; Goldberg, H.G.; and Shyr, P. The nasd regulation advanced-detection system (ads). AI Magazine, 20, 1 (1999), 55–67.

40. Lenat, D.B., and Guha, R.V. Building Large Knowledge-based Systems: Representation and Inference in the Cyc Project. Boston: Addison-Wesley Longman, 1989.

41. Lieberman, H.; Liu, H.; Singh, P.; and Barry, B. Beating common sense into interactive applications. AI Magazine, 25, 4 (2004), 63–76.

42. Lucas, H.C. Market expert surveillance system. Communications of the ACM, 36, 12 (1993), 27–34.

43. Luo, X.M., and Zhang, J. How do consumer buzz and traffic in social media marketing predict the value of the firm? Journal of Management Information Systems, 30, 2 (2013), 213–238.

44. Markus, M.L.; Majchrzak, A.; and Gasser, L. A design theory for systems that support emergent knowledge processes. MIS Quarterly, 26, 3 (2002), 179–212.

45. Milosavljevic, M.J.-Y.D.; Hachey, B.; Arunasalam, B.; Radford, W.; and Curran, J.R. Automating financial surveillance. Lecture Notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering, 40 (2010), 305–311.

46. Mittermayer, M.-A., and Knolmayer, G.F. Newscats: A news categorization and trading system. In International Conference in Data Mining. Hong Kong, 2006, pp. 1002–1007.

47. Muir, D.M., and Schipani, C.A. The use of efficient market hypothesis: Beyond sox. Michigan Law Review, 105, 8 (2007), 1941–1980.

48. Nunamaker, J.F.J.; Chen, M.; and Purdin, T.D.M. Systems development in information systems research. Journal of Management Information Systems, 7, 3 (1990), 89–106.

49. Ogut, H.; Doganay, M.M.; and Aktas, R. Detecting stock-price manipulation in an emerging market: The case of turkey. Expert Systems with Applications, 36, 9 (2009), 11944–11949.

50. Oh, C., and Sheng, O. Investigating predictive power of stock micro blog sentiment in forecasting future stock price directional movement. In International Conference on Informaiton Systems. Shanghai: Association for Information Systems, 2011, 17.

51. Palshikar, G.K., and Apte, M.M. Collusion set detection using graph clustering. Data Mining and Knowledge Discovery, 16, 2 (2008), 135–164.

52. Peffers, K.; Rothenberger, T.T.M.A.; and Chatterjee, S. A design science research methodology for information systems research. Journal of Management Information Systems, 24, 3 (2007), 45–77.

53. Peramunetilleke, D., and Wong, R.K. Currency exchange rate forecasting from news headlines. In Australasian Database Conference. Melbourne, 2002, pp. 131–139.

54. Perfetti, C.A. Comprehending written language: A blueprint of the reader. In C.M. Brown and P. Hagoort (eds.), The Neurocognition of Language Processing. London: Oxford University Press, 1999, pp. 167–208.

55. Pirrong, C. Detecting manipulation in futures markets: The Ferruzzi soybean episode. American Law and Economics Review, 6, 1 (2004), 28–71.

56. Punniyamoorthy, M., and Thoppan, J.J. ANN-GA based model for stock market surveillance. Journal of Financial Crime, 20, 1 (2013), 52–66.

57. Qu, J.; Qin, W.; Feng, Y.; and Sai, Y. An outlier detection method based on Voronoi diagram for financial surveillance. In International Workshop on Intelligent Systems and Applications. Wuhan, China: IEEE, 2009, pp. 1–4.

58. Rodier, M. Insider fraud: Watch out, your bank could be the next one to lose billions Wall Street & Technology. 2011. http://www.wallstreetandtech.com/risk-manage ment/insider-fraud-watch-out-your-bank-could-be-the-next-one-to-lose-billions/d/d-id/ 1265313 (accessed April 20, 2015).

59. Samuelson, P.A. Summing upon business cycles: Opening address. In J.C. Fuhrer and S. Schuh (eds.), Beyond Shocks: What Causes Business Cycles. Federal Reserve Bank of Boston, 1998, pp. 33–36.

60. Schumaker, R.P., and Chen, H.C. Textual analysis of stock market prediction using breaking financial news: The AZFinText system. ACM Transactions on Information Systems, 27, 2 (2009), 12.

61. Scila. 2015. http://www.Cinnober.Com/cinnober%c2%ae-surveillance (accessed April 20, 2015).

62. Seo, Y.W.; Giampapa, J.A.; and Sycara, K.P. Financial news analysis for intelligent portfolio management. Technical Report, CMU-RI-TR-04-04, Robotics Institute, Carnegie Mellon University, Pittsburgh, 2004.

63. SMARTS. 2015. http://www.Nasdaqomx.Com/technology/marketplacesolutions/surveil lancecompliance (accessed April 20, 2015).

64. Tetlock, P.C. Does public financial news resolve asymmetric information? Review of Financial Studies, 23, 9 (2010), 3520–3557.

65. Toutanova, K.; Klein, D.; Manning, C.; and Singer, Y. Feature-rich part-of-speech tagging with a cyclic dependency network. In Conference of the North American Chapter of the Association for Computational Linguistics on Human Language Technology. Edmonton, Canada: Association for Computational Linguistics, 2003, pp. 173–180.

66. Tumarkin, R., and Whitelaw, R.F. News or noise? Internet postings and stock prices. Financial Analysts Journal, 57, 3 (2001), 41–51.

67. Verhoeven, L., and Perfetti, C. Advances in text comprehension: Model, process and development. Applied Cognitive Psychology, 22, 3 (2008), 293–301.

68. Vlas, R.E., and Robinson, W.N. Two rule-based natural language strategies for requirements discovery and classification in open source software development projects. Journal of Management Information Systems, 28, 4 (2012), 11–38.

69. Walls, J.; Widmeyer, G.; and El Sawy, O. Assessing information system design theory in perspective: How useful was our 1992 initial rendition. Journal of Information Technology Theory and Application, 6, 2 (2004), 43–58.

70. Walls, J.G.; Widmeyer, G.R.; and El Sawy, O.A. Building an information system design theory for vigilant EIS. Information Systems Research, 3, 1 (1992), 36–59.

71. Zheng, H.T.; Kang, B.Y.; and Kim, H.G. Exploiting noun phrases and semantic relationships for text document clustering. Information Sciences, 179, 13 (2009), 2249–2262.
