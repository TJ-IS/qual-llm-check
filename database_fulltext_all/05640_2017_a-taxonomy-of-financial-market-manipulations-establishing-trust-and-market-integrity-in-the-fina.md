---
otero_id: 5640
otero_key: "D24FR4JM"
title: "A Taxonomy of Financial Market Manipulations: Establishing Trust and Market Integrity in the Financialized Economy through Automated Fraud Detection"
authors: "Michael Siering; Benjamin Clapham; Oliver Engel; Peter Gomber"
year: "2017"
journal: "Journal of Information Technology"
doi: "10.1057/s41265-016-0029-z"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research Article

# A taxonomy of financial market manipulations: establishing trust and market integrity in the financialized economy through automated fraud detection

Michael Siering<sup>1</sup>, Benjamin Clapham<sup>1</sup>, Oliver Engel<sup>1</sup>, Peter Gomber<sup>1</sup>

<sup>1</sup>Goethe University Frankfurt, Theodor-W.-Adorno-Platz 4, 60323 Frankfurt, Germany

Correspondence:

M Siering, Goethe University Frankfurt, Theodor-W.-Adorno-Platz 4, 60323 Frankfurt, Germany.

Tel: +49 (0)69 798 34683;

Fax: +49 (0)69 798 35007;

E-mail: siering@wiwi.uni-frankfurt.de

## Abstract

Financial market manipulations represent a major threat to trust and market integrity in capital markets. Manipulations contribute to mispricing, market imperfections and an increase in transaction costs for market participants and in costs of capital for issuers. Manipulations are facilitated by increased transaction velocity, speculative trading and abusive usage of new trading technologies, i.e., they are directly linked to financial sector changes that drive financialization. Research at the intersection of financialization and IS might support regulatory authorities and market operators in improving market surveillance and helping to detect fraudulent activities. However, confusing terminology is prevalent on financial markets with respect to different manipulation techniques and their characteristics, which hampers efficient fraud detection. Furthermore, recognizing manipulations is challenging given the large number of information sources and the vast number of trades occurring not least because of high-frequency traders. Therefore, automated market surveillance tools require a comprehensive taxonomy of financial market manipulations as a basis for appropriate configuration. Based on a cluster analysis of SEC litigation releases, a review of the latest market abuse regulation and academic studies, we develop a taxonomy of manipulations that structures and details existing manipulation techniques and reveals how these techniques differ along several dimensions. In a case study, we show how the taxonomy can be utilized to guide the development of appropriate decision support systems for fraud detection. Journal of Information Technology (2017). doi:10.1057/s41265-016-0029-z

Keywords: financial market manipulation; market surveillance; taxonomy; fraud detection; decision support

## Introduction

T he financial crisis triggered an intensive debate about international economies. There is widespread agreement that weaknesses in financial regulation and supervision contributed to the crisis and that the strongly increased financial activity does not fulfill its main purpose, i.e., to serve the needs of the real economy by providing efficient financial products and services. Financial activities are viewed as an end in itself to enable financial players to generate excessive profits based on highly complex financial products (e.g., over-the-counter (OTC) derivatives) and a tremendous increase in turnover on financial markets. These trends are mirrored in the term financialization, which is defined as ‘‘the increasing dominance of financial actors, markets, practices, measurements and narratives, at various scales, resulting in a structural transformation of economies, firms (including financial institutions), states and households’’ (Aalbers, 2016: 3). Key drivers of financialization are deregulation, the focus on the shareholder value concept and, last but not least, the proliferation of information technology (IT) (Lagoarde-Segot, 2016). New trading technologies such as algorithmic trading and high-frequency trading (HFT) lead to massive increases in turnover velocity on financial markets because they enable sophisticated market participants to generate significant total profits based on small profits per trade and to instantaneously react to profitable situations in a highly complex and fragmented trading environment (Gomber et al., 2016).

Furthermore, since financial markets have existed, market participants try to generate profits from deceiving others (Leinweber and Madhavan, 2001). For instance, stock prices are manipulated to pretend a trend (Comerton-Forde and Putnins, 2011), or false and misleading information is disseminated to cause market reactions and to profit from other market participants’ actions. However, in recent years, the magnitude of financial market manipulations and their effect has increased continuously. Technology-savvy market participants, such as HFTs, are perceived to exploit their technological advantage to perform deceptive tactics (Biais and Woolley, 2011; Cumming et al., 2012) at the expense of other market participants or to contribute to extreme and unexpected market price fluctuations as witnessed in the May 6, 2010, Flash Crash (Easley et al., 2011). This event brought these new trading technologies to the forefront of the financialization debate and triggered far-reaching regulatory initiatives both in the USA and in Europe to monitor or even curb this form of speculative trading, which is accused of focusing solely on market microstructure noise rather than contributing to market efficiency by incorporating relevant information into asset prices.

In addition to this increased risk of speculative mispricing and potential market manipulation due to new technologies, numerous concrete scandals and accusations in the context of market abuse and manipulation were recently uncovered. The manipulation of the fixings in the foreign exchange markets over several years (Financial Conduct Authority (FCA), 2014) and the Libor rate manipulation scandal (Financial Services Authority (FSA), 2012) revealed massive rigging activities in the area of financial benchmarks that led to fines of more than \$10 billion until 2016 (Vaughan, 2016). Politicians, regulators and the public thus push for increased transparency and massive efforts in the area of surveillance to curb market abuse and manipulation and to re-establish trust in the financial sector.

Due to the massive increase in transactions triggered by speculative trading, an enormous amount of data must be analyzed to generate alerts based on overnight-batch processes that can be investigated in detail to identify potential and actual market manipulations. Because order and trading data can hardly be analyzed manually, automated fraud detection systems are required that provide alerts of potential market manipulations. Previous research has already shown that appropriate information systems (IS) can help to identify fraudulent content (Abbasi et al., 2010; Zahedi et al., 2015) and communication behavior (Zhou et al., 2004). Nevertheless, although the necessity of decision support systems (DSSs) that support market surveillance authorities in the field of financial fraud detection appears obvious, few academic studies exist in this particular context.

One essential prerequisite for building DSSs that are able to assist with the identification of potentially fraudulent behavior is an in-depth domain and data understanding (Fayyad et al., 1996) that prevents improper system configurations and might lead to the discovery of wrong and invalid patterns.

Although a clear distinction between different manipulation techniques is a prerequisite for efficient market surveillance, confusing terminology is prevalent with respect to manipulation techniques and their main characteristics; existing classifications (e.g., Allen and Gale, 1992) neither provide a comprehensive view of differences and similarities nor cover the newly emerging forms of manipulation in conjunction with HFT. Furthermore, they do not link to the configuration of fraud detection systems.

To close this research gap and to follow the call of Ngai et al. (2011) concerning the automated detection of fraud in the field of financial markets, we develop a novel and comprehensive taxonomy of market manipulations by (1) analyzing current cases of prosecuted market manipulations based on a cluster analysis of litigation releases published by the US Securities and Exchange Commission (SEC), (2) performing a structured literature review to include all manipulation techniques studied by academics and (3) completing the taxonomy based on an analysis of current financial market regulation. That is, we include the European Market Abuse Regulation (MAR) for multi-country coverage of market manipulations. Thus, we follow the methodology proposed by Nickerson et al. (2013) and build a taxonomy of market manipulations, considering both the differences and similarities of various market manipulation techniques and new types of manipulations related to HFT strategies in particular.

We contribute to research at the interface of financialization and IS by (1) systematically documenting and organizing new and established forms of market manipulation that are based on traditional and new (potentially speculative) trading technologies, such as HFT, in a market manipulation taxonomy and (2) evaluating this taxonomy for the automated detection of market manipulations based on sophisticated information systems. Furthermore, we provide specific guidelines on how to derive a DSS configuration to detect fraudulent market behavior based on a systematically derived taxonomy, thereby contributing to research in IS. The results are highly relevant for regulators and market surveillance authorities because the systematic and automated detection of market manipulation prevents abusive behavior and contributes to re-establishing trust in financial markets.

This paper is structured as follows. Section ‘‘Research context: financial market manipulations and their detection presents related work on financial market manipulations and fraud detection. Section ‘‘General research approach’’ briefly explains the general research methodology including the taxonomy approach. Section ‘‘Analysis of financial market manipulations based on SEC litigation releases’’ provides first insights into market manipulations based on a cluster analysis of litigation releases. Insights into our structured literature and regulatory review are provided in section ‘‘European market abuse regulation and literature review’’. Section ‘‘Developing a taxonomy of financial market manipulations’’ presents the taxonomy development. Section ‘‘Evaluation of the taxonomy’ evaluates our taxonomy and shows in a case study how the taxonomy can be applied in the field of fraud detection. Finally, section ‘‘Conclusion’’ summarizes our findings.

## Research context: financial market manipulations and their detection

Manipulation of financial markets is as old as the markets themselves and has been studied extensively in the academic literature both from an economic and from a legal perspective. To avoid manipulative actions and to ensure capital markets’ integrity, exchanges and regulatory authorities engage in market surveillance to detect manipulative behavior (Leinweber and Madhavan, 2001).

Because manipulations can occur in different forms and categories, there is no generally accepted definition of financial market manipulation or financial fraud (we do not distinguish between market fraud and manipulation, and both terms are used interchangeably in the following). Therefore, we follow a broad definition of financial market manipulations; first, market manipulations encompass the manipulation of financial disclosures accompanied by large accounting scandals such as Enron and Worldcom, because such scandals hamper the efficient functioning of markets (Akhigbe et al., 2005; Jones, 2011). Second, investor confidence is impeded by investment manipulations such as the Ponzi scheme set up by Bernard Madoff (Pozza et al., 2009; Rapoport, 2012). Third, insider trading is another form of market manipulation, drawing on information asymmetries (Arshadi, 1998; Allen and Ramanan, 1995). Fourth, there is a variety of different fraudulent trading activities aiming at financial market manipulation that we also consolidate under this umbrella term. According to Cumming and Johan (2008: 456), such ‘‘trading practices … distort prices and enable market manipulators to profit at the expense of other participants, creating information asymmetries’’. Forms of such market manipulations are, for example, ‘‘Pump and Dump’’ techniques in which the manipulator releases falsepositive information concerning a company to profit from the subsequent price increase (Sabherwal et al., 2011) or ‘‘Marking the Close’’ in which the fraudster tries to manipulate the closing price of a stock (Hillion and Suominen, 2004). These manipulations have a severe effect on trust in financial markets and on investors, who can lose substantial parts of their investment, e.g., due to ‘‘Pump and Dump’ fraud (Hanke and Hauser, 2008). A detailed overview of market manipulations addressed in academic studies and of international market abuse regulation is provided in our literature and regulatory review (‘‘European market abuse regulation and literature review’’ section).

Due to the increasing utilization of IT in particular, which is also one main driver of financialization (Lagoarde-Segot, 2016), the risk of market manipulations increases due to novel forms of manipulation arising from technologies such as HFT. Furthermore, the chance of manually detecting market manipulations is lowered due to increasing amounts of data to be analyzed. To increase trust, the prevention of market manipulations is of high importance, which requires appropriate IS for fraud detection. Research on IS indicates that automated detection systems are able to find patterns in datasets to identify fraudulent Web content (Abbasi et al., 2010; Zahedi et al., 2015). Additionally, related classification methods might be used to detect deceptive content in computer-mediated communication (Zhou et al., 2004). Nevertheless, previous research has also shown that an indepth domain understanding is essential for finding an appropriate system configuration (Fayyad et al., 1996).

In the field of financial market manipulations, Allen and Gale (1992) are among the first who provide a structured overview and categorization. They differentiate between actions that manipulate the actual or perceived value of an asset (action-based manipulation), the release of false or misleading information to move stock prices in the desired direction (information-based manipulation) and attempts to manipulate by buying and selling a stock in a specific manner (trade-based manipulation). However, the taxonomy developed by Allen and Gale (1992) is not sufficiently detailed for use as an input for an automated market surveillance system because it does not address a potential system configuration. Moreover, due to technological enhancements, new forms of manipulation have evolved that are not covered by this taxonomy. For example, algorithmic traders and in particular the subset of HFTs might try to manipulate stock prices based on order submissions and their subsequent deletions to profit from their low-latency access to markets and market data.

Manipulation is a serious threat to the efficiency and liquidity of trading venues and undermines the trust of market participants (Kyle and Viswanathan, 2008). Therefore, detection of market manipulation/financial fraud is essential to ensure the orderly function of markets and to provide a level playing field for all participants. Distinguishing fraudulent financial data from authentic data is one of the most difficult tasks regulators face (Ngai et al., 2011). In the USA, the SEC is responsible for market manipulation detection and prosecution. Self-regulatory (non-governmental) institutions such as the Financial Industry Regulatory Authority (Davis, 2007) are also active in this field. In the European Union (EU), the MAR, which has been in force since 2014 and has been applied since July 2016, lists activities that are defined as financial market manipulation.

There are a variety of tools that can be used by regulators to detect market manipulation (Wheeler and Aitken, 2000). Of special interest for this study is the use of intelligent systems for decision support to identify suspicious behavior (Baker, 2005; Humpherys et al., 2011). Although there is a large research stream about the empirical evidence of manipulations and their effects on financial markets, little research addresses the detection of financial market fraud by using an automated DSS (Comerton-Forde and Putnins, 2011).

One approach to detecting manipulation is proposed by Aggarwal and Wu (2006), who analyze 142 cases of stock market manipulation. They find that potentially informed parties and market makers are likely to be manipulators and show that prices of manipulated stocks rise through the manipulation period and fall thereafter. Comerton-Forde and Putnins (2011) developed a measure of the probability of closing price manipulation in a given market for a stock. Furthermore, Ledgerwood and Carpenter (2012) derived a theoretical framework for classification and detection of market manipulation. Other work focuses on peer group analyses using unsupervised learning to detect suspicious behavior (Kim and Sohn, 2012) or data mining techniques to detect fraudulent financial statements (Kirkos et al., 2007). However, no generally accepted basis for the development of an automated financial fraud detection system exists. Furthermore, none of the mentioned approaches contains a means to detect market manipulation conducted by HFTs or other market participants using a low-latency infrastructure. With this study, we therefore respond to the call for research by Ngai et al. (2011) and contribute to the scarce literature on financial fraud detection by proposing a taxonomy of market manipulations that is of fundamental importance to configure automated fraud detection systems.

## General research approach

The primary goal of this study is to develop a taxonomy of financial market manipulations. Taxonomy development has been studied intensively in the social sciences. A detailed overview is provided by Bailey (1984). We apply the methodology developed by Nickerson et al. (2013), which is accepted in the field of IS, and adapt it by including different sources for input, i.e., currently existing market manipulations, as shown in Figure 1.

We identify market manipulation techniques based on three sources from academia and international regulation: SEC litigation releases to determine fraudulent financial market activities that are prosecuted in the USA, manipulation techniques that are described in the MAR and a structured literature review on financial market manipulations. Additionally, we rely on the European Benchmark Regulation (European Parliament and Council, 2016) as a source for fraudulent actions aimed at the manipulation of market benchmarks. As a result, we determine the different forms of market manipulation which are then used together with a first taxonomy developed by Allen and Gale (1992) as a starting point to derive our taxonomy, which shows mutually exclusive and collectively exhaustive characteristics. The already existing dimensions included in the taxonomy are determined based upon established category definitions in the academic literature. New dimensions are built drawing on insights from the structured literature review and international market abuse regulation. An evaluation and discussion of the proposed taxonomy follows.

1) US SEC Litigation Releases

2) European Market Abuse Regulation

3) Structured Literature Review

Figure 1 General research approach for taxonomy development.

## Analysis of financial market manipulations based on SEC litigation releases

## SEC litigation releases and dataset acquisition

Litigation releases (LRs) report the enforcement actions of the SEC. Among other information, a release can include arraignments, a subpoena (e.g., defendants in a civil court explain themselves), an announcement of investigation, a final judgment (e.g., penalty or disgorgement payments are announced), a trading halt (e.g., to protect the unsuspecting public from manipulation) or public service announcements. LRs represent a prominent source to analyze market manipulations that are prosecuted by the SEC.

We downloaded all LRs from the SEC homepage from December 29, 1995, to July 22, 2013, resulting in 8093 releases. To avoid data inconsistency and noise, we cleaned the obtained dataset by excluding years that were only partly covered due to the introduction of the database in 1995/1996 (and the incomplete year 2013), LRs that did not refer to Rule 10b-5 of the SEC, which covers the ‘‘employment of manipulative and deceptive devices,’’ and large scandals and Ponzi schemes because they tend to involve large numbers of defendants, claimants, and different courts, which leads to redundancy in the dataset and might influence the clustering process (Coffee, 2005). Nevertheless, Ponzi schemes are later included in the taxonomy because they represent a form of financial market manipulation. Table 1 depicts the data processing in detail.

Our final dataset covers 4340 releases. Table 2 provides summary statistics for the documents in the total raw dataset and for the documents that are used for the analysis.

## Clustering approach

To derive insights into which general categories of manipulative behavior are prosecuted by the SEC, the LRs are clustered. Therefore, the raw data must be transformed in a form that is readable and processable by an unsupervised clustering algorithm (Rokach and Maimon, 2005). The objective behind the unsupervised clustering approach is to reveal novel patterns and to explore an unknown database without the requirement of specific knowledge about the particular structure of the LRs.

The documents are preprocessed before the clustering algorithm is applied. Therefore, they are reduced to their fundamental parts, and a term frequency measure is applied to create a word vector of the documents. First, the documents are tokenized by applying a split after every non-letter character (e.g., commas, semicolons and spaces) (Rehman et al., 2013). After that, uppercase letters are

Taxonomy of Financial Market Manipulations

transformed into lowercase letters to homogenize the words. Next, one-letter tokens and stop-words are excluded from the list of tokens. These exclusions are non-informative tokens such as articles, pronouns and adverbs (Fatudimu et al., 2008). To enhance the meaningfulness of the individual tokens, a Porter-Stemmer is used (Porter, 2006). By reducing tokens to their common stem, the total number of different tokens is reduced, which also reduces computational complexity. The advantage of this algorithm is context awareness and simplicity of the suffix removal rules (Willett, 2006). In the last step, we calculate TF-IDF scores for every token (Jones, 1972), and every token is assigned a number that determines its weight in the document (term frequency) and in the overall corpus of documents (inverse document frequency).

Following the pre-processing, we apply a clustering algorithm. Clustering is the assignment of objects to groups with high intra-similarity and low inter-similarity; many algorithms exist to solve this optimization problem, each having its own specific field of application (Tabrizi et al., 2013). The LRs are expressed in natural unstructured language, which has important consequences for usable algorithms and measures because LRs have different lengths and content structures (Losiewicz et al., 2000). Therefore, algorithms must be used that can process high-dimensional datasets and normalize the documents to avoid ambiguous results (Ye, 2011). For the task of finding patterns in highdimensional datasets, the k-means algorithm combined with a suitable similarity measure is the algorithm of choice (Willett, 1988). The k-means algorithm divides a population of N-Dimensional Objects (here LRs) into k sets by optimizing the within-class variance and calculating the means of the attributes (centroids) within the cluster (MacQueen, 1967). Practically, k random vectors are created, and the similarity to the objects is measured, with the most similar objects being grouped together. This process is repeated until the within-class variance is optimized or the predefined maximum number of iterations is reached. The assignment of a mean vector (centroid) to every cluster makes this algorithm especially useful for document clustering because the mean vector can easily be interpreted and applied by human reasoning (MacQueen, 1967).

Table 1 Excluded documents from the raw litigation release database

<table><tr><td>Cleansing measure</td><td>Number of excluded documents</td></tr><tr><td>Filter 1995,1996 and 2013</td><td>722</td></tr><tr><td>No 10b-5 reference</td><td>1845</td></tr><tr><td>Filter Ponzi schemes</td><td>632</td></tr><tr><td>Filter scandals (e.g., Enron, Worldcom)</td><td>554</td></tr><tr><td>Final database</td><td>4340</td></tr></table>

Clustering process and evaluation of the different cluster models We calculate 15 different models with numbers of clusters from 2 to 16. There is no commonly agreed evaluation technique or measure for determining the most suitable number of clusters and clustering model (Aliguliyev, 2009). Clustering always requires both quantitative (e.g., performance measures) and qualitative (e.g., human reasoning or expert knowledge) criteria to determine the true number of clusters and to evaluate the found patterns (Frank, 1994). Therefore, we apply both qualitative criteria and the X-means algorithm to find the optimal number of clusters (Bouwman, 1983; Pelleg and Moore, 2000).

Table 3 shows an excerpt of the results of the clustering algorithm for the optimal cluster number of four. The table presents the twelve top scoring tokens for each cluster together with the corresponding cosine similarity (TF-IDF value). In comparison with the other models developed, the reported cluster model with four clusters appears to be the most suitable from a qualitative point of view. Different from the models with fewer clusters, there is an information gain by adding up to four clusters to describe the dataset. Furthermore, four categories of market manipulation are revealed: financial instrument manipulation, accounting fraud, investment fraud and insider trading. Each fraudulent activity is characterized by the respective relevant keywords that appear most often within a cluster as shown in Table 3.

Because the tokens ‘‘stock’’ and ‘‘manipul’’ are of high importance for the first cluster, it is labeled the cluster of financial instrument manipulation (Allen and Gale, 1992). The other tokens in this cluster fit to financial instrument manipulation, e.g., penny stocks are common targets of manipulative actions (see token ‘‘penni’’) (Bartels, 2000), and several manipulation techniques such as ‘‘Pump and Dump’ depend upon the Internet (see token ‘‘internet’’) to disseminate false messages (Sabherwal et al., 2011). The second cluster is determined to represent accounting fraud because it clearly includes LRs that cover the misstatement or overstatement of accounting figures such as revenue (see token ‘‘revenu’’) or financial figures (see token ‘‘financi’’) (Gerety and Lehn, 1997). This statement also holds true for the other tokens in this cluster such as ‘‘audit,’’ ‘‘fiscal’’ and ‘‘report.’’ Cluster 3 covers manipulation with respect to funds of investors (see token ‘‘fund’’ and ‘‘investor’’) and is named investment fraud cluster (Carroll, 2006). Investment fraud is regularly conducted by asset managers or financial advisors (see tokens ‘‘asset,’’ ‘‘manag’’ and ‘‘advis’’) using the legal form of a limited liability company (see token ‘‘llc’’) and deceiving clients by disbursing false returns (see tokens ‘‘client’’ and ‘‘return’’) (Ionescu, 2010). The last cluster indicates that the most relevant technique for the cluster is insider trading (see tokens ‘‘insid’’ and ‘‘trade’’) (Roddenberry and Bacon, 2011). Insider trading often occurs around mergers and acquisitions (see tokens ‘‘merger’’ and ‘‘acquisit’’); the manipulator tries to profit from non-public information (see tokens ‘‘profit’’ and ‘nonpubl’’) (Allen and Ramanan, 1995).

Table 2 Summary statistics for the analyzed litigation releases

<table><tr><td rowspan="2">Measure</td><td colspan="2">Documents per year</td><td colspan="2">Word count</td></tr><tr><td>Raw</td><td>Cleaned</td><td>Raw</td><td>Cleaned</td></tr><tr><td>Average</td><td>425</td><td>271</td><td>3694</td><td>1678</td></tr><tr><td>Median</td><td>438</td><td>274</td><td>3363</td><td>1537</td></tr><tr><td>Minimum</td><td>122</td><td>208</td><td>819</td><td>406</td></tr><tr><td>Maximum</td><td>619</td><td>371</td><td>48306</td><td>7767</td></tr><tr><td>SD</td><td>120</td><td>41</td><td>1721</td><td>700</td></tr></table>

Table 3 Result of the clustering process with four centroid vectors (k = 4) showing tokens, corresponding ranks, TF-IDF scores and a representative litigation release for each cluster

<table><tr><td rowspan="3">Rank</td><td colspan="2">Cluster 1</td><td colspan="2">Cluster 2</td><td colspan="2">Cluster 3</td><td colspan="2">Cluster 4</td></tr><tr><td colspan="2">Financial instrument manipulation (1283 LRs)</td><td colspan="2">Accounting fraud (840 LRs)</td><td colspan="2">Investment fraud (1351 LRs)</td><td colspan="2">Insider trading (866 LRs)</td></tr><tr><td>Token</td><td>TF-IDF</td><td>Token</td><td>TF-IDF</td><td>Token</td><td>TF-IDF</td><td>Token</td><td>TF-IDF</td></tr><tr><td>1</td><td>Stock</td><td>0.039</td><td>Revenu</td><td>0.050</td><td>Fund</td><td>0.064</td><td>Insid</td><td>0.065</td></tr><tr><td>2</td><td>Judgment</td><td>0.030</td><td>Report</td><td>0.045</td><td>Invest</td><td>0.059</td><td>Trade</td><td>0.056</td></tr><tr><td>3</td><td>Internet</td><td>0.027</td><td>Record</td><td>0.041</td><td>Investor</td><td>0.053</td><td>Tip</td><td>0.043</td></tr><tr><td>4</td><td>Manipul</td><td>0.027</td><td>Audit</td><td>0.040</td><td>Advis</td><td>0.040</td><td>Option</td><td>0.040</td></tr><tr><td>5</td><td>Florida</td><td>0.024</td><td>Quarter</td><td>0.039</td><td>Llc</td><td>0.036</td><td>Share</td><td>0.040</td></tr><tr><td>6</td><td>Penni</td><td>0.024</td><td>Fiscal</td><td>0.037</td><td>Client</td><td>0.035</td><td>Profit</td><td>0.037</td></tr><tr><td>7</td><td>Offer</td><td>0.023</td><td>Financi</td><td>0.034</td><td>Capit</td><td>0.032</td><td>Acquisit</td><td>0.036</td></tr><tr><td>8</td><td>Defend</td><td>0.023</td><td>Account</td><td>0.034</td><td>Asset</td><td>0.031</td><td>Purchas</td><td>0.034</td></tr><tr><td>9</td><td>Share</td><td>0.022</td><td>Auditor</td><td>0.030</td><td>Manag</td><td>0.030</td><td>Stock</td><td>0.033</td></tr><tr><td>10</td><td>Final</td><td>0.022</td><td>Aid</td><td>0.030</td><td>Defend</td><td>0.025</td><td>Merger</td><td>0.033</td></tr><tr><td>11</td><td>Investor</td><td>0.020</td><td>Year</td><td>0.029</td><td>Return</td><td>0.024</td><td>Nonpubl</td><td>0.032</td></tr><tr><td>12</td><td>Enter</td><td>0.020</td><td>Offic</td><td>0.029</td><td>Bank</td><td>0.023</td><td>Illeg</td><td>0.030</td></tr><tr><td>LR</td><td>LR 21423 (2010)</td><td></td><td colspan="2">LR 17346 (2002)</td><td colspan="2">LR 22545 (2012)</td><td colspan="2">LR 17645 (2002)</td></tr></table>

Three tokens, i.e., ‘‘investor,’’ ‘‘stock’’ and ‘‘share,’’ appear in two of the four clusters. However, this appearance does not harm the validity of the clustering process because both financial instrument manipulation and investment fraud are conducted either by investors or to deceive investors. Likewise, financial instrument manipulation aims at the manipulation of stock, respectively, share prices while market participants conducting insider trading try to benefit from changes in stock (share) prices based on non-public information.

Because these four clusters are meaningfully distinguishable, a minimum number of four clusters appears appropriate. By adding one more cluster, the investment fraud cluster is split. This split, however, does not help to describe the dataset better but instead creates fuzzy assignments because five of the twelve tokens assigned to cluster three (see Table 3) are also relevant for the new cluster of the model, making it difficult to find a clear and distinguishable label for both clusters. This finding and the analysis of the rest of the centroid vectors (six to fifteen) leads to the conclusion that k = 4 is the optimal number of clusters from a qualitative information gain standpoint (Bouwman, 1983).

After having analyzed the optimal cluster number from a qualitative standpoint, a k-means algorithm is applied as a quantitative measure. Specifically, we apply the X-means algorithm that computes all cluster models (similar to the kmeans approach) from a predefined upper to lower boundary and assigns scores based on the Bayesian Information Criterion to every model (Pelleg and Moore, 2000). When a score is computed for every model in the predefined range, the model with the best score determines the optimal number of clusters to partition the dataset from an information criterion point of view. The quantitative approach supports the chosen model of four clusters.

In addition to the four clusters of financial market manipulations that we identified based on SEC LRs, a deeper analysis of the centroid vector for the cluster of financial instrument manipulations reveals more fine-grained manipulative actions such as ‘‘Pump and Dump’’ (indicated by the token ‘‘pump’’ on rank 47 of the centroid vector). A more detailed analysis of different manipulation techniques is provided in the ‘‘European market abuse regulation and literature review’’ section to enhance and complete the taxonomy as described in the ‘‘Developing a taxonomy of financial market manipulations’’ section.

## European market abuse regulation and literature review

## Analysis of European regulation

With our taxonomy of financial market manipulations, we want to provide a comprehensive, multi-country overview on fraudulent behavior in financial markets. Therefore, we rely on not only US legislation but also inclusion of manipulation techniques that are considered in the MAR. By examining both US and European jurisdictions, we have considered all manipulations in the two largest financial markets. Different from the LRs, no in-depth textual analysis is necessary for the MAR because manipulation techniques can be extracted from the articles defined in the regulation.

The MAR is intended to ensure the integrity and smooth functioning of European financial markets with the goal of increasing investor confidence (European Parliament and

Council, 2014). The regulation precisely describes different activities that are considered manipulative behavior in Articles 8 and 12. Furthermore, we determined abusive activities related to market benchmarks from the European Benchmark Regulation, effective as of 2016 (European Parliament and Council, 2016). The list of market manipulations extracted from the MAR and the European Benchmark Regulation is presented together with the additional manipulation techniques found in academic studies in Table 5 (see next section).

## Literature review of financial market manipulations

In addition to incorporating regulation and prosecution of market manipulations, we conduct a systematic literature review to identify manipulations that might not yet be considered in regulatory documents.

A systematic literature review shall provide a comprehensive view on the topic in question (Denney and Tewksbury, 2013) and exhaustively include all related studies to reveal the current state of knowledge in the research field under investigation (Rowley and Slack, 2004). In this context, an effective literature search relies on meaningful keywords and backward and forward reference searches (Levy and Ellis, 2006) that are especially fruitful because the keyword search is rather unlikely to fully yield all relevant literature concerning the topic (Webster and Watson, 2002).

We applied both techniques to find all manipulation techniques that are addressed in academic research. We searched in peer-reviewed journals in reputable databases for scientific publications from 1990 onwards, as shown in Table 4. Keywords in our search were ‘‘stock market manipulation’’, ‘‘stock market fraud’’, ‘‘financial market manipulation’’ and ‘‘financial market fraud’’. Applying backward and forward reference searches, we manually added additional relevant publications not found in the keywords search.

Table 5 presents all of the financial market manipulations that we identified based on SEC LRs, the European MAR and the systematic literature review. We only included manipulation techniques mentioned in at least two sources, and we categorized the different fraudulent activities according to clusters based on the analysis of SEC LRs.

Table 4 Results of the systematic literature review

<table><tr><td>Database</td><td>Number of hits in the database</td><td>Publications explicitly covering financial market manipulations</td></tr><tr><td>ABI/INFORM database ProQuest</td><td>125</td><td>3</td></tr><tr><td>ACM</td><td>35</td><td>3</td></tr><tr><td>AIS library</td><td>14</td><td>0</td></tr><tr><td>Business Source Premier</td><td>252</td><td>19</td></tr><tr><td>Emerald Fulltext</td><td>18</td><td>6</td></tr><tr><td>IEEE Xplore Digital Library</td><td>3</td><td>2</td></tr><tr><td>Science Direct</td><td>43</td><td>14</td></tr><tr><td>Springer-Link journals</td><td>53</td><td>4</td></tr><tr><td>JSTOR</td><td>65</td><td>6</td></tr><tr><td>Manually added</td><td>17</td><td>17</td></tr><tr><td>Total</td><td>625</td><td>74</td></tr></table>

## Developing a taxonomy of financial market manipulations

## Taxonomy development methodology

Developing a suitable taxonomy is important for almost every discipline to understand the underlying mechanics and to break down complex topics into smaller parts (Miller and Roth, 1994). The emphasis when developing a taxonomy of manipulation techniques should be on awareness of the effects on the market and the identification of touch points with the market environment (Kumar and Langberg, 2009). This emphasis leads to the development of effective countermeasures or detection techniques that help to make financial markets more efficient and less likely to be manipulated (Cumming and Johan, 2008). To achieve this goal, comprehensibility and extendibility are highly important so that the taxonomy can be adapted to changing market conditions and new manipulation techniques (Ngai et al., 2011).

To the knowledge of the authors, no concise, robust, comprehensive, extendible and explanatory taxonomy of manipulation techniques can be found in the financial market manipulation literature (Nickerson et al., 2013; Kyle and Viswanathan, 2008). There only exist simple taxonomies for market manipulations. For instance, Allen and Gale (1992) distinguished action-, information- and trade-based manipulation.

Our taxonomy development is based on the method proposed by Nickerson et al. (2013). Nickerson et al. (2013: 338) define taxonomies as ‘‘[…] systems for grouping objects of interest in a domain based on common characteristics. The algorithm follows an iterative approach. Objects are discovered and grouped according to defined characteristics and dimensions.

For the taxonomy, the objects are the manipulation techniques, and the characteristics should be related to our meta-characteristic, the market environment, also encompassing the interaction of the manipulation with the market environment. This interaction involves both market participants (issuers, intermediaries and investors) and market information such as prices and trading volumes (Ledgerwood and Carpenter, 2012; Hellwig, 1980).

The algorithm starts with the most comprehensive characteristic, and each (sub) characteristic should be a logical consequence (Nickerson et al., 2013). After each iteration, a taxonomy table (see Table 6) and a taxonomy formula [see Eq. (1)] are derived until the ending conditions are met.

$$
T _ {m} = \left\{D _ {i}, i = 1, \dots , n | D _ {i} = \left[ C _ {i j}, j = 1, \dots , k _ {i}; \quad k _ {i} \geq 2 \right] \right\}\tag{1}
$$

$T _ { m }$ is the taxonomy after iteration m with a set of n dimensions $D _ { i } ,$ each consisting of $k _ { i }$ mutually exclusive and collectively exhaustive characteristics $C _ { i j } .$ . The markers (‘‘X’’) in the table indicate the classification of the objects. The exemplary taxonomy shown in Table 6 is described by the following Eq. (2):

Table 5 Identified market manipulation techniques

<table><tr><td>Cluster (SEC LRs)</td><td>Manipulation technique</td><td>Description</td><td>References</td></tr><tr><td>Accounting fraud</td><td>Fraudulent financial statements</td><td>Accounting fraud means the willful misrepresentation of the financial health of a firm by disclosure violations and improper accounting. There exist different types of accounting fraud (e.g., earnings inflation, fictitious transactions and accounts payable fraud).</td><td>Gerety and Lehn (1997), Bonner et al. (1998), Pagano and Immordino (2012)</td></tr><tr><td rowspan="3">Investment fraud</td><td>Benchmark manipulation (with official fixing)</td><td>Collusion of banks or other intermediaries to influence and manipulate fundamental reference prices or interest rates that are officially fixed at a certain point in time (e.g., LIBOR manipulation).</td><td>Abrantes-Metz et al. (2012), Fouquau and Spieser (2015), MAR Art. 12 (1)(d), European Parliament and Council (2016)</td></tr><tr><td>Benchmark manipulation (no official fixing)</td><td>Collusion of banks or other intermediaries aimed at the manipulation of fundamental reference prices or interest rates (e.g., commodity benchmarks such as oil or gold prices).</td><td>MAR Art. 12 (1)(d), European Parliament and Council (2016)</td></tr><tr><td>Ponzi scheme</td><td>A Ponzi scheme is a fraudulent investment operation in which the operator, an individual or organization, consecutively raises external funds and pays returns to investors from new capital raised from later investors, thereby creating an illusion of high returns.</td><td>Shleifer and Vishny (1997), Ionescu (2010), Rapoport (2012)</td></tr><tr><td>Insider trading</td><td>Insider trading</td><td>Insider trading means that investment decisions are based on relevant non-public information (e.g., executives trading before dividend announcements).</td><td>Roddenberry and Bacon (2011), Arshadi (1998), Allen and Ramanan (1995), MAR Art. 8 (1)</td></tr><tr><td rowspan="5">Financial instrument manipulation</td><td>Pump and dump</td><td>The fraudster buys relatively unknown or low-valued stocks, disseminates false-positive information to lure other investors into buying the stock, which leads to increasing stock prices (the “pump”). In the next step, the fraudster sells the shares to realize substantial profits before the stock price reverts to its normal low level (the “dump”).</td><td>Sabherwal et al. (2011), Bartels (2000), MAR Art. 12 (1)(c), MAR Art. 12 (2)(d)</td></tr><tr><td>Short and distort</td><td>Short and distort describes the manipulation technique of an investor entering a short position in a specific company’s stock, disseminating wrong negative information about the company and buying back the stock after its decline, thereby making substantial profits.</td><td>Leinweber and Madhavan (2001), Vila (1989), MAR Art. 12 (1)(c), MAR Art. 12 (2)(d)</td></tr><tr><td>Cornering (squeezing)</td><td>The manipulator corners the market of a security by obtaining large quantities of the security, thereby gaining a price-controlling market position due to the shortage of supply. Third parties that, for example, must fulfill contracts based on short positions are then forced to buy the security at inflated prices (squeezing).</td><td>Møllgaard (1997), Golmohammadi et al. (2014), Lomnicka (2001), Allen et al. (2006), Cooper and Donaldson (1998), Jarrow (1992), Putnins (2012), MAR Art. 12 (2)(a)</td></tr><tr><td>Advancing the bid</td><td>Increasing the bid for a security to artificially increase its price.</td><td>Cumming and Johan (2008), Klein et al. (2012), MAR Art. 12 (1)(a)(ii)</td></tr><tr><td>Reducing the askMatched orders</td><td>Reducing the ask for a security to artificially decrease its price.Transactions in which colluding traders enter matching buy and sell orders simultaneously to feign an active market to lure other investors into buying the security, thereby causing a price increase.</td><td>Cumming and Johan (2008), Klein et al. (2012), MAR Art. 12 (1)(a)(ii)Fischel and Ross (1991), Lomnicka (2001), Cumming and Johan (2008)</td></tr><tr><td rowspan="7"></td><td>Painting the tape</td><td>Painting the tape refers to a trader engaging in a series of publicly reported transactions to give the impression of trading activity and price movements. As for matched orders, the objective is to attract other investors buying the security, leading to higher stock prices. However, collusion of several traders is not a necessary characteristic of painting the tape.</td><td>Cumming and Johan (2008), Carhart et al. (2002)</td></tr><tr><td>Wash sales</td><td>Wash sales describe a manipulation technique of fictitious transactions performed by one trader without change of actual ownership because the same party is buyer and seller to create a record of rising prices and the illusion of an active market.</td><td>Thel (1993), Lomnicka (2001), MAR Annex 1 (A) (c)</td></tr><tr><td>Capping (pegging)</td><td>A practice in which the price of a security underlying an option is manipulated shortly before the option's expiration date to prevent a rise/decline in price of the security so that the previously written call/put option will expire worthless, thereby protecting the option premium initially received.</td><td>Cumming and Johan (2008), Putnins (2012)</td></tr><tr><td>Marking the close/open (also banging the close)</td><td>Placement of buy orders with high limits/sell orders with low limits to boost/suppress the closing (opening) price of a security. This manipulation technique is often used to influence performance measures that are based on securities' closing prices (less frequent: opening prices). The technique is also called Banging the Close when a trader transacts a large amount of an asset during the closing period to benefit from another, even larger position, e.g., in an option or other derivative.</td><td>Comerton-Forde and Putnins (2011), Cumming and Johan (2008), Hillion and Suominen (2004), MAR Art. 12 (2)(b), CFTC (2016), Karz and Wagner (2006)</td></tr><tr><td>Front running</td><td>Front running refers to brokers or market makers making use of their private information about incoming order flow by buying or selling a security in advance of other parties' large trades, thereby profiting from the price movement that follows the large trades.</td><td>Cataldo and Killough (2003), Chaturvedula et al. (2015)</td></tr><tr><td>Churning</td><td>Churning describes the activity of a broker engaging in excessive buying and selling of securities in a client's account to create higher commissions, disregarding the client's interests.</td><td>Shapiro et al. (2012), Cumming and Johan (2008)</td></tr><tr><td>ScalpingSpoofing</td><td>Scalping refers to manipulative action of investment advisors purchasing a security shortly before recommending that security to third parties without disclosing their position. The fraudster profits from the rise in the price following the recommendation and immediately sells off his shares.Spoofing refers to the placement of limit orders that are not intended to be executed but to mislead other investors with respect to the demand or supply of a security. The manipulator later submits his real order, thereby profiting from the price change resulting from his spoofing activity.</td><td>Hazen (2010), Tripp (1963), MAR annex 1 (B) (b)Lee et al. (2013), Biais and Woolley (2011), MAR Art. 12 (1)(a)(i)</td></tr><tr><td rowspan="4"></td><td>Pinging</td><td>Pinging describes the submission of small marketable orders without an intention to trade to detect large hidden orders (abusive liquidity detection) with the intention of benefiting from that information.</td><td>IIROC (2012), Scopino (2015)</td></tr><tr><td>Quote stuffing</td><td>Quote stuffing is a technique employed by HFTs that involves the placement and immediate cancelation of a large number of orders in an attempt to flood the trading system with excessive messages. Quote stuffing can create information arbitrage opportunities for HFTs due to increased data latencies for other market participants.</td><td>IIROC (2012), Biais and Woolley (2011), Easley et al. (2011), MAR Art. 12 (2)(c)(i)</td></tr><tr><td>Ramping</td><td>HFTs enter buy orders at successively increasing prices to lead other investors to perceive an active interest in a security.</td><td>Cumming and Johan (2008), MAR Art. 12 (2)(c)(iii)</td></tr><tr><td>Layering (order book fade)</td><td>Layering describes a strategy in HFT in which a trader places an order away from the market bid/ask on one side of the market and subsequently submits increasing/decreasing bids/asks for the same security on the other side of the market without the intention of the additional orders being executed to move the market price in the direction of his first order by creating a false impression of supply and demand. Once the initial order is executed, the trader cancels all other orders and profits from the price reversal.</td><td>IIROC (2012), MAR Art. 12 (2)(c)(ii)</td></tr></table>

Table 6 Example for a taxonomy with two objects and two classes; the ‘X’ indicates the assignment (Nickerson et al., 2013)

<table><tr><td rowspan="2">Objects</td><td colspan="2">Dimension1</td></tr><tr><td>Characteristic1</td><td>Characteristic2</td></tr><tr><td>Object1</td><td>X</td><td></td></tr><tr><td>Object2</td><td></td><td>X</td></tr></table>

$$
T _ {1} = \left\{\text { Dimension } _ {1} [ \text { Characteristic } _ {1}, \text { Characteristic } _ {2} ] \right\}\tag{2}
$$

Several iterations are accomplished to find possible dimensions that describe the manipulation techniques in more detail until the ending conditions are met. The method ends when both subjective and objective conditions have been met: (1) the taxonomy must be concise, robust, comprehensive, extendible and explanatory (subjective conditions); and (2) in the last iteration, no (new) characteristics or dimensions have been added/split/merged (objective condition) (for a detailed set of possible combinations, see Nickerson et al., 2013). For developing the taxonomy, we initially start with the four categories determined by the classification of SEC LRs (see Table 3). Then, we integrate the financial market manipulations found in Table 5. In each iteration, either the empirical-to-conceptual or the conceptual-to-empirical approach can be followed to identify characteristics and objects. If significant domain understanding is available, the conceptual-to-empirical approach is chosen (first, identification of new characteristics; thereafter, determination of appropriate objects). In contrast, if significant data on the objects are available, the empirical-toconceptual approach is selected (first, identifying a set of objects; thereafter, identification of common characteristics). In the following, we outline the different iterations of our taxonomy development process (due to space constraints, the identified objects are shown in the final result of the taxonomy development process).

## Iteration 1

For the first iteration, the empirical-to-conceptual approach is chosen; the objects of the first iteration are determined by the four clusters that were found in the analysis of the SEC LRs: financial instrument manipulation, accounting fraud, investment fraud and insider trading.

Furthermore, the work of Allen and Gale (1992) is the reference work in the manipulation literature and provides a first categorization (Aggarwal and Wu, 2006; Kyle and Viswanathan, 2008; Hillion and Suominen, 2004). According to Allen and Gale (1992), financial market manipulations can be classified by the means of the manipulative act. They define three means of manipulation techniques: actions which alter the actual or perceived value of the underlying assets (action-based manipulation), information misusage by disseminating false information or rumors (informationbased manipulation), and trading techniques to manipulate the market (trade-based manipulation).

However, in today’s markets, with traders using lowlatency infrastructures, manipulation techniques also exist that are based not on trades but only on orders because traders make use of their superior latency to cancel orders before they are executed (Biais and Woolley, 2011). Therefore, we extend the categorization by Allen and Gale (1992) with the category of order-based manipulation, leading to the following taxonomy:

$$
T _ {1} = \{\text { Means   [Action   based, Information   based, }
$$

$$
\left. \text { Trade   based,   Order   based } \right] \}\tag{3}
$$

The ending conditions are not fully met. The subjective ending conditions conciseness and comprehensiveness are met, but the taxonomy is not yet robust in terms of covering all manipulation techniques, its explanatory power is not sufficient, and extendibility is not achieved. Furthermore, new characteristics and dimensions were added. Therefore, both objective and subjective ending conditions are not met, and an additional iteration is required.

## Iteration 2

The empirical-to-conceptual approach was chosen for the second iteration. Specifically, more manipulation techniques can be identified through the analysis provided in Table 5. These techniques provide a closer view into the structure of the previous objects because they split them into more specific manipulation techniques.

Additionally, a new dimension can be added in this step by analyzing the manipulator with respect to the employed technique. Possible manipulators are issuers of a financial asset, intermediaries and investors (Kyle and Viswanathan, 2008). Intermediaries are banks and brokers; however, they can also act as investors if they trade on their own account. Investors, therefore, are defined as market participants trading on their own account, e.g., dealers, HFTs and other ultimate recipients of rights in a security.

Not all ending conditions are met; specifically, the taxonomy is not sufficiently explanatory because some dimensions that could add explanatory power are not yet included. Moreover, new objects and dimensions were added; therefore, iteration 2 does not yet mark an ending point but results in the following taxonomy:

T<sub>2</sub> ¼ fMeans ½Action based; Information based; Trade based;

Order based; Manipulator Issuer ½ g ; Intermediary; Investor

ð4Þ

## Iteration 3

For the next iteration, the conceptual-to-empirical approach is chosen (Nickerson et al., 2013). No new objects can be defined, because the list of objects in Table 5 is exhaustive and reflects all of the techniques currently prosecuted by regulators and discussed in academic studies. A new set of characteristics can be found by describing the manipulation target. Asset prices, volumes patterns and fundamental data are often targeted by manipulators (Putnins, 2012). Moreover, the bid/ask spread, commissions and latency might be possible targets of manipulation techniques. The knowledge of manipulation targets can help officials and fraud detection tools to prevent manipulation by closely monitoring the key targets usually chosen by manipulators (Lenard and Alam, 2009). The previously found characteristics can be further summarized under the dimension manipulation target:

T ¼ fMeans ½Action based; Information based; Trade based;

Order based; Manipulator Issuer½ ; Intermediary; Investor ; Manipulation target ½Bid=Ask; Price; Volume;

Fundamental data; Commissions; Latencyg

ð5Þ

Most subjective ending conditions are met, but many of the objects are not yet explicitly distinguishable through the characteristics. Moreover, there was a new dimension added, so an additional iteration is necessary.

## Iteration 4

For this iteration, the conceptual-to-empirical approach is chosen. We rely on the studies of Ledgerwood and Carpenter (2012) and Aggarwal and Wu (2006), which provide information about potential dimensions to be added.

The first characteristic to be added is whether a technique is economically reasonable or based on uneconomic decisions (Ledgerwood and Carpenter, 2012). A manipulation technique can include sell or purchase practices that are specifically designed to lose money initially, compensated by illicit profits later. This category can be of high importance for the detection of market manipulation because uneconomical trades should be rare in manipulation-free markets and stand out when transactions are being monitored (Fama, 1970).

The second characteristic that can be added is whether a manipulation technique has a specific direction to which the target is manipulated (Aggarwal and Wu, 2006). This characteristic is of high importance when distinguishing objects in a reliable manner. For example, ‘‘Pump and Dump’’ and ‘‘Short and Distort’’ cannot be discriminated through the taxonomy from iteration 3. However, the initial action of ‘‘Pump and Dump’’ (‘‘Short and Distort’’) has the goal of increasing (decreasing) the price. Consequently, both can be distinguished. In contrast, ‘‘Marking the Close’’ can lead to price manipulations in both directions, depending upon the intention of the manipulator. The subjective ending conditions of taxonomy development are fully met, but in this iteration, new dimensions were added; therefore, a new iteration is necessary:

T ¼ fMeans ½Action based; Information based; Trade based;

Order based; Manipulator Issuer½ ; Intermediary; Investor ;

Manipulation target ½Bid=Ask; Price; Volume;

Fundamental data; Commissions; Latency;

Economically reasonable Yes ½  ; No ;

Specific target direction Up½ g; Down; Both possible; No

ð6Þ

## Iteration 5

For this iteration, the conceptual-to-empirical approach was again chosen. The MAR states in article 12 (2)(a) that specific times of the day can be used as an indicator for the occurrence of certain manipulation strategies. Therefore, we include the dimension specific point in time to distinguish manipulation techniques that depend upon specific points in time to be accomplished, e.g., ‘‘Marking the Close,’’ which is only feasible at the end of the trading day. Additionally, the MAR suggests that some fraudulent activities depend upon the collusion of market participants. Therefore, we incorporate the dimension collusion in the taxonomy. ‘‘Benchmark Manipulation’’ with and without official fixing is the prime example of such a fraudulent activity. Furthermore, MAR recital 38 points out that specific abusive strategies can be performed by algorithmic traders and, in particular, HFTs using low-latency infrastructure. Consequently, we added the dimension low latency. Examples of such manipulative strategies are ‘‘Quote Stuffing’’ and ‘‘Layering.’’ Due to three new dimensions, an additional iteration is necessary. The iteration results in the following taxonomy:

T ¼ fMeans ½Action based; Information based; Trade based;

Order based; Manipulator Issuer½ ; Intermediary; Investor ;

Manipulation target ½Bid=Ask; Price; Volume;

Fundamental data; Commissions; Latency;

Economically reasonable Yes½ ; No ;

Specific target direction Up ½  ; Down; Both possible; No ;

Specific time Yes ½  ; No ; Collusion Yes ½  ; No ;

Low latency Yes½ g; No

ð7Þ

## Iteration 6

An empirical-to-conceptual approach cannot be pursued in this iteration because there are no further empirical findings relevant for extending the taxonomy. Furthermore, no important additional concepts remain; thus, nor can a conceptual-to-empirical approach be applied. All ending conditions, subjective and objective, are met, and the taxonomy is provided by $\mathrm { T } _ { 5 }$ (iteration 5). Therefore, the final taxonomy of market manipulations in interaction with the environment of the manipulated market is shown in Table 7. Based on the methodology used by Nickerson et al. (2013), we derived eight dimensions for our taxonomy of market manipulations that can be used for the configuration of an automated market surveillance system to detect manipulative actions.

## Evaluation of the taxonomy

Evaluation following Nickerson et al.

This section tests and discusses the developed taxonomy to assess the contribution to the financial market manipulation literature and the overall understanding of manipulations. First, because the objective criterion is already fulfilled, the subjective (qualitative) criteria are tested. Then, the practical applicability and overall usefulness will be addressed.

Conciseness Nickerson et al. (2013) stated that an overly broad taxonomy is a weak one. Because the cognitive capacity of the decision maker is naturally limited, a taxonomy that covers every characteristic and object possible is not concise (Nickerson et al., 2013). The taxonomy developed above does not suffer from this issue, because all characteristics are documented in the literature, and most can be found in actual LRs. Eight dimensions and 25 characteristics are also unlikely to exceed the decision makers’ cognitive capacity (Carroll, 1993; Miller, 1956).

Robustness A robust taxonomy can clearly distinguish objects from one another via characteristics and dimensions; a small number of dimensions can hardly achieve this goal (Nickerson et al., 2013). This taxonomy is able to distinguish clearly two objects from one another; for example, the two techniques ‘‘Pump and Dump’’ and ‘‘Scalping’’ are hard to distinguish due to their similar appearance. The dimension manipulator, however, helps to distinguish the two clearly because ‘‘Pump and Dump’’ can be accomplished by investors, whereas ‘‘Scalping’’ is conducted by intermediaries.

Comprehensiveness A taxonomy that is developed both conceptually and empirically, such as this one, should cover all dimensions and all objects possible to be viewed as comprehensible (Nickerson et al., 2013). An extensive literature review and the use of EU legislation and market manipulations sued by the SEC in the USA ensure that all objects (manipulation techniques) currently considered relevant and all dimensions that could possibly characterize those techniques are covered.

Extendibility A taxonomy should also be applicable in the future, when new objects or dimensions extend the domain for which the taxonomy was developed (Nickerson et al., 2013). This criterion is hard to test because knowledge about future forms of manipulation is only vague. However, the taxonomy can be extended due to technological enhancements because it is already capable of including manipulation techniques associated with HFT, which represents a recent major technological trend.

Explanatory power According to Nickerson et al. (2013), a taxonomy should help to understand the domain without describing every object in detail. The developed taxonomy helps to understand the anatomy of market manipulations and shows which manipulation techniques should be considered by regulatory authorities. Nevertheless, the explanatory power is not as strong for some objects as for others. For example, the difference between ‘‘Matched Orders’’ and ‘‘Wash Sales’’ is only identifiable based on whether collusion of market participants is necessary.

Table 7 Taxonomy of financial market manipulations

<table><tr><td rowspan="2">Manipulation category</td><td rowspan="2">Manipulation technique</td><td colspan="4">Means of manipulation</td><td colspan="3">Manipulator</td><td colspan="5">Manipulation target</td><td></td></tr><tr><td>Action based</td><td>Information based</td><td>Trade based</td><td>Order based</td><td>Issuer</td><td>Intermediary</td><td>Investor</td><td>Bid/Ask</td><td>Price</td><td>Volume</td><td>Fundamental</td><td>Commissions</td><td>Latency</td></tr><tr><td>Accounting fraud</td><td>Fraudulent financial statements</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td rowspan="3">Investment fraud</td><td>Benchmark manipulation (official fixing)</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Benchmark manipulation (no official fixing)</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Ponzi scheme</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Insider trading</td><td>Insider trading</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="18">Financial instrument manipulation</td><td>Pump and dump</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Short and distort</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Cornering (squeezing)</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Advancing the bid</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reducing the ask</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Matched orders</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Painting the tape</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Wash sales</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Capping (pegging)</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Marking the close/open (banging the close)</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Front running</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Churning</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>Scalping</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Spoofing</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pinging</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Quote stuffing</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td></tr><tr><td>Ramping</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Layering (order book fade)</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">Manipulation category</td><td rowspan="2">Manipulation technique</td><td colspan="4">Specific target direction</td><td colspan="2">Econ. reasonable</td><td colspan="2">Specific time</td><td colspan="2">Collusion</td><td colspan="2">Low latency</td></tr><tr><td>Up</td><td>Down</td><td>Both possible</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Accounting fraud</td><td>Fraudulent financial statements</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td></tr><tr><td rowspan="3">Investment fraud</td><td>Benchmark manipulation (official fixing)</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>Benchmark manipulation (no official fixing)</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>Ponzi scheme</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Insider trading</td><td>Insider trading</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td rowspan="18">Financial instrument manipulation</td><td>Pump and dump</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Short and distort</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Cornering (squeezing)</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Advancing the bid</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Reducing the ask</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Matched orders</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>Painting the tape</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Wash sales</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Capping (pegging)</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Marking the close/open (banging the close)</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Front running</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Churning</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Scalping</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Spoofing</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>Pinging</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Quote stuffing</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>Ramping</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>Layering (order book fade)</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td></tr></table>

## Application of the taxonomy in decision support system development

To show the applicability of the taxonomy for DSS configuration, we focus on ‘‘Marking the Close’’ market manipulations. We assume that the taxonomy is appropriate for finding a proper DSS configuration if the specific configuration (i.e., most importantly, the data sources considered) leads to a successful system for fraud detection. Therefore, the ‘‘Marking the Close’’ manipulation technique is suitable for investigating the appropriateness of the taxonomy because different previous studies have proposed systems for detecting manipulations in which the closing price of a financial instrument is manipulated.

For marking the close, the means of market manipulation is trade based. In other words, by means of specific trades, the closing price is manipulated (dimension: manipulation target). Consequently, an appropriate DSS should analyze trading data including stock prices for manipulation detection. Because the closing price can be manipulated either upwards or downwards, depending upon the specific goal of the manipulator, both directions of manipulation are possible. Thus, a DSS should consider whether the suspicious stock price consistently moves in one direction. In addition, the manipulation focuses on a specific point in time, which shows that in this case, closing prices should be considered by DSSs. Nevertheless, no specific low-latency infrastructure is necessary to pursue this manipulation technique, so the utilization of such infrastructures cannot be considered a cue for manipulation detection.

Furthermore, focusing on the manipulator performing the manipulation, here the investor tries to perform marking the close manipulations. This might be attempted, e.g., to avoid margin calls, to support a flagging price or to affect the valuation of a fund’s portfolio at the end of a specific relevant period (e.g., quarter). Specifically, data identifying whether an investor has an incentive because of his position in the instrument might be helpful to identify related information. Nevertheless, such data are only available for market surveillance authorities and should therefore be considered within their specific fraud detection systems. Concerning the collusion dimension, note that no collusive behavior is necessary for ‘‘Marking the Close’’; therefore, this dimension should not be considered in a DSS.

Finally, the taxonomy also shows that the manipulative behavior is not economically reasonable, i.e., in the case of a marking the close manipulation, there should be other gains for the investor to compensate him for performing this costly activity, e.g., a higher valuation that is applied to reveal a higher own portfolio performance of a fund (window dressing). Therefore, data that allow crosschecking positions of the respective investors should be used as additional input.

Focusing on previous research to confirm whether the proposed system configuration is actually implemented, we consider the studies by O<sup>¨</sup> g˘u¨t et al. (2009) and Kim and Sohn (2012). O<sup>¨</sup> g˘u¨t et al. (2009) consider average daily returns and other daily trading statistics as input variables to detect ‘‘Marking the Close’’ by means of different machine learning techniques. Additionally, Kim and Sohn (2012) consider daily trading data encompassing closing prices to perform a peer group analysis to detect suspicious behavior.

Both studies confirm the configuration as derived from the taxonomy, and both studies consider trading data, including stock prices. Furthermore, the studies consider a specific point in time, i.e., the closing price. Because the closing price might be manipulated in both directions depending upon the manipulator’s intention, the direction is not directly considered, but a deviation from a benchmark is considered. Because neither study has access to trading data, including the market participant trading the financial instrument, they are not able to consider whether the investor performs a potential market manipulation. Finally, both studies could also be improved if – in suspicious cases – the economic reasonability of trades is assessed to identify investors who have significant positions in the financial instrument under investigation.

Consequently, the application of the taxonomy for DSS configuration (including the comparison with previous studies) shows that the taxonomy provides very useful guidelines on the specific design of a DSS; it corresponds to the design of existing systems and provides insights into potential system enhancements.

## Discussion

As shown by the evaluation of the taxonomy according to the criteria proposed by Nickerson et al. (2013) and by the application of the taxonomy for DSS configuration, the proposed taxonomy is valid and very useful in the field of classification and detection of market manipulations. It thus helps to distinguish different forms of market manipulations and to identify similarities between diverse types of manipulative behavior. It also indicates clearly which information an automated fraud detection system must incorporate. Due to the comprehensive sources upon which the taxonomy is built (cases actually prosecuted by a market surveillance authority, cases reported in the literature and cases extracted from financial market manipulation regulations), the taxonomy can be assumed to offer a broad overview on market manipulations. Furthermore, the different dimensions directly allow drawing conclusions on the specific configuration of fraud detection systems. Consequently, the proposed taxonomy can support market surveillance authorities in detecting securities fraud to ensure fair and efficient financial markets and a level playing field for market participants, which is in the interests of all stakeholders, particularly in the light of the financialization debate.

The distribution of the characteristics assigned to objects is not even for all dimensions of the taxonomy. In particular, the means of manipulation, the manipulator and the collusion dimension place a great deal of weight on the characteristics trade based, investor and no collusion necessary. This result occurs because many financial instrument manipulations have these characteristics in common. Nevertheless, these dimensions are necessary because they represent key information for regulators and automated fraud detection systems trying to detect market manipulation and to differentiate clearly between different manipulation techniques.

We are aware that fraudulent market participants might also use the insights of the proposed taxonomy to circumvent the risk of being detected by an automated fraud detection system. Nevertheless, the taxonomy provides general insights into DSS configuration that also apply in the case of changed manipulator behavior. In this case, an appropriate DSS must be recalibrated to detect the altered manipulative behavior.

The current study also has several limitations. The taxonomy provides implications for how to configure DSSs, particularly in terms of the input data to be considered. However, we are aware that the taxonomy does not itself provide insights into how to process such potential input data in a DSS. For instance, diverse machine learning algorithms have been shown to lead to different performance figures. In addition, from the specific point in time when a manipulation is conducted, e.g., in the case of ‘‘Marking the Close,’’ further aspects concerning the time passed for executing strategies can hardly be considered within the taxonomy because manipulators might chose different intervals for their manipulations. Therefore, DSS developers considering the taxonomy should also perform different machine learning experiments to find the best-performing configuration.

Finally, as already shown during the application of the taxonomy in DSS development, not every dimension of a market manipulation can be detected automatically. Nevertheless, the taxonomy provides a useful base to develop DSSs that help to reduce information overload and to identify cases that must be examined manually. Particularly against the background of the increasing importance of financial markets in the context of financialization, IS should consider the taxonomy because domain knowledge for detecting market manipulations can help to increase trust in and the integrity of financial markets.

## Conclusion

As long as financial markets have existed, fraudulent market participants have tried to profit by manipulating markets and deceiving others. Because market manipulations result in substantial losses that must be borne by market participants, understanding and detecting manipulations are of fundamental importance to establishing trust and market integrity – particularly against the background of financialization and the role of markets in financialization economies. Nevertheless, until now, different terms have been used even for the same market manipulation techniques, and no unified terminology prevails, which also hampers proper fraud detection.

Within this study, we follow a multi-method approach to develop a taxonomy of financial market manipulations. In particular, we consider officially prosecuted current market manipulations by performing a cluster analysis on SEC LRs. We also perform a literature review and a regulatory review to identify market manipulations and their characteristics. On that basis, we develop a novel taxonomy that covers existing market manipulation techniques, including those based on HFT. Applying eight dimensions, the taxonomy helps to distinguish clearly between different fraudulent activities and shows which information must be considered by automated fraud detection systems. Based on the ‘‘Marking the Close’’ manipulation, we successfully evaluate the taxonomy and show how to employ the taxonomy to build a fraud detection system. Guided by this taxonomy, researchers and practitioners developing DSSs can find an appropriate system configuration.

We provide a solid understanding of the different manipulation techniques and their characteristics. We thereby extend previous studies and contribute to the literature by specifically considering the manipulation techniques actually performed and prosecuted and by specifically considering manipulation techniques caused by novel technological developments such as HFT. Therefore, our study also contributes to the call by Ngai et al. (2011), who find that there is a lack of research in the field of securities fraud detection; the study shows how the taxonomy can be used as a foundation for DSSs helping to detect fraud.

Our results are also relevant for practitioners, regulators and financial market participants. First, our study provides an overview of current financial market manipulations and their characteristics. This classification can provide an important means for increasing the financial literacy of both institutional and private investors by showing them potential market manipulations and for generating awareness concerning suspicious market behavior. Based on this research, financial institutions and market surveillance authorities can develop DSSs that help to identify market manipulations. Consequently, these organizations are enabled to enforce recent market regulations to ensure fair and efficient financial markets and thus to alleviate the negative effect of fraud on the economy, particularly in the light of financialization. Our results are also of relevance for software vendors because the study provides indications on how to configure appropriate DSSs to detect financial market manipulations. As also identified during the taxonomy development, HFT is accompanied by novel manipulation techniques. Because our paper shows which type of DSS configuration might help to identify related fraudulent activities, future research might build upon the taxonomy to develop specific deception detection systems.

Given the massive increase in regulation of financial markets and the banking industry as well as the need to provide efficient and low-cost technological support and automation in this field, a novel future research stream ‘‘Reg-Tech’’ will be an interesting and highly relevant topic for further research at the intersection of financialization and IS. Reg-Tech encompasses ‘‘the adoption of new technologies to facilitate the delivery of regulatory requirements’’ (Financial Conduct Authority (FCA), 2015). Our work is one step in that direction; however, additional future research in the fields of, for example, artificial intelligence, big data analysis and text mining techniques might provide very useful input for investment firms, regulators, digital solution providers and consultancy houses to fulfill ever-growing regulatory requirements in banking and financial markets.

## References

Aalbers, M. (2016). Corporate financialization. In D. Richardson, N. Castree, M. F. Goodchild, A. Kobayashi, W. Liu, and R. A. Marston (Eds.), International Encyclopedia of Geography: People, the Earth, Environment and Technology. Oxford: Wiley.

Abbasi, A., Zhang, Z., Zimbra, D., Chen, H., Nunamaker, Jr, and Jay, F. (2010). Detecting Fake Websites: The Contribution of Statistical Learning Theory. MIS Quarterly, 34(3), 435–461.

Abrantes-Metz, R. M., Kraten, M., Metz, A. D., and Seow, G. S. (2012). Libo Manipulation? Journal of Banking & Finance, 36(1), 136–150.

Aggarwal, R. K., and Wu, G. (2006). Stock Market Manipulations. Journal of Business, 79(4), 1915–1953.

Akhigbe, A., Madura, J., and Martin, A. (2005). Accounting Contagion: The Case of Enron. Journal of Economics and Finance, 29(2), 187–202.

Aliguliyev, R. M. (2009). Performance Evaluation of Density-Based Clustering Methods. Information Sciences, 179(20), 3583–3602.

Allen, F., and Gale, D. (1992). Stock-Price Manipulation. Review of Financial Studies, 5(3), 503–529.

Allen, F., Litov, L., and Mei, J. (2006). Large Investors, Price Manipulation, and Limits to Arbitrage: An Anatomy of Market Corners. Review of Finance, 10(4), 645–693.

Allen, S., and Ramanan, R. (1995). Insider Trading, Earnings Changes, and Stock Prices. Management Science, 41(4), 653–668.

Arshadi, N. (1998). Insider Trading Liability and Enforcement Strategy. Financial Management, 27(2), 70–84.

Bailey, K. D. (1984). A Three-Level Measurement Model. Quality & Quantity, 18(3), 225–245.

Baker, N. (2005). Fraud and Artificial Intelligence. Internal Auditor, 62(1), 29–32.

Bartels, K. C. (2000). Click Here to Buy the Next Microsoft: The Penny Stock Rules, Online Microcap Fraud, and the Unwary Investor. Indiana Law Journal, 75(1), 353–378.

Biais, B. and Woolley, P. (2011). High frequency trading [WWW document] http://www.eifr.eu/files/file2220879.pdf (accessed 24th February 2016).

Bonner, S. E., Palmrose, Z.-V., and Young, S. M. (1998). Fraud Type and Auditor Litigation: An Analysis of SEC Accounting and Auditing Enforcement Releases. The Accounting Review, 73(4), 503–532.

Bouwman, M. J. (1983). Human Diagnostic Reasoning by Computer: An Illustration from Financial Analysis. Management Science, 29(6), 653–672.

Carhart, M. M., Kaniel, R., Musto, D. K., and Reed, A. V. (2002). Leaning for the Tape: Evidence of Gaming Behavior in Equity Mutual Funds. The Journal of Finance, 57(2), 661–693.

Carroll, J. B. (1993). Human Cognitive Abilities: A Survey of Factor-Analytic Studies. Cambridge: Cambridge University Press.

Carroll, B. (2006). How to Prevent Investment Adviser Fraud. Journal of Accountancy, 201(1), 40–43.

Cataldo, A. J., and Killough, L. N. (2003). Market Makers’ Methods of Stock Manipulation. Management Accounting Quarterly, 4(4), 10–13.

Chaturvedula, C., Bang, N. P., Rastogi, N., and Kumar, S. (2015). Price Manipulation, Front Running and Bulk Trades: Evidence from India. Emerging Markets Review, 23, 26–45.

Coffee, J. C. (2005). A Theory of Corporate Scandals: Why the USA and Europe Differ. Oxford Review of Economic Policy, 21(2), 198–211.

Comerton-Forde, C., and Putnins, T. J. (2011). Measuring Closing Price Manipulation. Journal of Financial Intermediation, 20(2), 135–158.

Cooper, D. J., and Donaldson, R. G. (1998). A Strategic Analysis of Corners and Squeezes. The Journal of Financial and Quantitative Analysis, 33(1), 117–137.

Cumming, D., and Johan, S. (2008). Global Market Surveillance. American Law and Economics Review, 10(2), 454–506.

Cumming, D., Zhan, F. and Aitken, M. (2012). High Frequency Trading and End-of-Day Manipulation [WWW document] https://www.legacy.wlu.ca/ documents/54105/Cumming-Zhan-Aitken-15012013\_2.pdf (accessed 24th February 2016).

Davis, H. A. (2007). Summary of Selected FINRA Regulatory Notices. Journal of Investment Compliance, 8(4), 60–67.

Denney, A. S., and Tewksbury, R. (2013). How to Write a Literature Review. Journal of Criminal Justice Education, 24(2). 218–234

Easley, D., Prado, De, Lopez, Marcos M., and O’Hara, M. (2011). The Microstructure of the ‘‘Flash Crash’ : Flow Toxicity, Liquidity Crashes, and the Probability of Informed Trading. Journal of Portfolio Management, 37(2), 118.

European Parliament and Council (2014). Market Abuse Regulation No 596/2014 [WWW document] http://eur-lex.europa.eu/legal-content/EN/TXT/ ?uri=celex%3A32014R0596 (accessed 24th February 2016).

European Parliament and Council (2016). Benchmark Regulation 2016/1011 [WWW document] http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri= CELEX:32016R1011&from=EN (accessed 4th August 2016).

Fama, E. F. (1970). Efficient Capital Markets: A Review of Theory and Empirical Work, The Journal of Finance, 25(2), 383–417.

Fatudimu, I., Musa, A., Ayo, C., and Sofoluwe, A. B. (2008). Knowledge Discovery in Online Repositories: A Text Mining Approach. European Journal of Scientific Research, 22(2), 241–250.

Fayyad, U., Piatetsky-Shapiro, G., and Smyth, P. (1996). From Data Mining to Knowledge Discovery in Databases. AI Magazine, 17(3), 37–54.

Financial Conduct Authority (FCA) (2014). FCA Final Notice: Reference Number, 124491. [WwW document] http://www.fca.org.uk/vour-fca/ documents/final-notices/2014/jpmorgan-chase-bank (accessed 25th August 2016).

Financial Conduct Authority (FCA) (2015). Call for Input: Supporting the Development and Adoption of RegTech [WWW document] https://www.fca. org.uk/publication/call-for-input/regtech-call-for-input.pdf (accessed 12th September 2016).

Financial Services Authority (FSA) (2012). FSA Final Notice: Reference Number 122702 [WWW document] http://www.fsa.gov.uk/static/pubs/final barclays-jun12.pdf (accessed 25th August 2016).

Fischel, D. R., and Ross, D. J. (1991). Should the Law Prohibit ‘‘Manipulation’’ In Financial Markets? Harvard Law Review, 105(2), 503–553.

Fouquau, J., and Spieser, P. K. (2015). Statistical Evidence About LIBOR Manipulation: A ‘ Sherlock Holmes’’ Investigation. Journal of Banking & Finance, 50, 632–643.

Frank, J. (1994). Artificial Intelligence and Intrusion Detection: Current and Future Directions, in 17th National Computer Security Conference; Baltimore, USA, 1994, pp. 1–12.

Gerety, M., and Lehn, K. (1997). The Causes and Consequences of Accounting Fraud. Managerial and Decision Economics, 18(7–8), 587–599.

Golmohammadi, K., Zaiane, O.R. and Diaz, D. (2014). Detecting Stock Market Manipulation Using Supervised Learning Algorithms, in International Conference on Data Science and Advanced Analytics (DSAA); Shanghai, China, 2014, pp. 435–441.

Gomber, P., Sagade, S., Theissen, E., Weber, M.C. and Westheide, C. (2016). Competition Between Equity Markets: A Review of the Consolidation Versus Fragmentation Debate, Journal of Economic Surveys (forthcoming).

Hanke, M., and Hauser, F. (2008). On the Effects of Stock Spam e-Mails. Journal of Financial Markets, 11(1), 57–83.

Hazen, T. L. (2010). Are Existing Stock Broker Standards Sufficient? Principles, Rules and Fiduciary Duties. Columbia Business Law Review, 2010(3), 710–761.

Hellwig, M. F. (1980). On the Aggregation of Information in Competitive Markets. Journal of Economic Theory, 22(3), 477–498.

Hillion, P., and Suominen, M. (2004). The Manipulation of Closing Prices. Journal of Financial Markets, 7(4), 351–375.

Humpherys, S. L., Moffitt, K. C., Burns, M. B., Burgoon, J. K., and Felix, W. F. (2011). Identification of Fraudulent Financial Statements Using Linguistic Credibility Analysis. Decision Support Systems, 50(3), 585–594.

IIROC (2012). Proposed Guidance on Certain Manipulative and Deceptive Trading Practices [WWW document] http://www.iiroc.ca/Documents/2012/ f62c746a-b5c9-448a-b57f-f1c04c88de14\_en.pdf (accessed 19th February 2016).

Ionescu, L. (2010). Madoff’s Fraudulent Financial Scheme, His Decades-Long Swindle, and the Failure of Operational Risk Management. Economics, Management, and Financial Markets, 5(3), 239–244

Jarrow, R. A. (1992). Market Manipulation, Bubbles, Corners, and Short Squeezes. Journal of Financial and Quantitative Analysis, 27(03), 311–336.

Jones, K. S. (1972). A Statistical Interpretation of Term Specificity and Its Application in Retrieval. Journal of Documentation, 28(1), 11–21.

Jones, M. J. (2011). Creative Accounting, Fraud And International Accounting Scandals. Hoboken: Wiley.

Karz, G., and Wagner, W. H. (2006). Should I Fire My Trader or Pay Him A Million? The Journal of Trading, 1(4), 85–89.

Kim, Y., and Sohn, S. Y. (2012). Stock Fraud Detection Using Peer Group Analysis. Expert Systems with Applications, 39(10), 8986–8992.

Kirkos, E., Spathis, C., and Manolopoulos, Y. (2007). Data Mining Techniques for the Detection of Fraudulent Financial Statements. Expert Systems with Applications, 32(4), 995–1003.

Klein, L. R., Dalko, V., and Wang, M. (2012). Regulating Competition in Stock Markets: Antitrust Measures to Promote Fairness and Transparency Through Investor Protection and Crisis Prevention. Hoboken: Wiley.

Kumar, P., and Langberg, N. (2009). Corporate Fraud and Investment Distortions in Efficient Capital Markets. The Rand Journal of Economics, 40(1), 144–172.

Kyle, A. S., and Viswanathan, S. (2008). How to Define Illegal Price Manipulation. American Economic Review, 98(2), 274–279.

Lagoarde-Segot, T. (2016). Financialization: Towards a New Research Agenda, International Review of Financial Analysis. doi:10.1016/j.irfa.2016.03.007.

Ledgerwood, S. D., and Carpenter, P. (2012). A Framework for the Analysis of Market Manipulation. The Review of Law & Economics, 8(1), 253–295.

Lee, E. J., Eom, K. S., and Park, K. S. (2013). Microstructure-Based Manipulation: Strategic Behavior and Performance of Spoofing Traders. Journal of Financial Markets, 16(2), 227–252.

Leinweber, D. J., and Madhavan, A. N. (2001). Three Hundred Years of Stock Market Manipulations. The Journal of Investing, 10(2), 7–16.

Lenard, M. J., and Alam, P. (2009). An Historical Perspective on Fraud Detection: From Bankruptcy Models to Most Effective Indicators of Fraud in Recent Incidents. Journal of Forensic & Investigative Accounting, 1(1), 1–27.

Levy, Y., and Ellis, T. J. (2006). A Systems Approach to Conduct an Effective Literature Review in Support of Information Systems Research. Informing Science: International Journal of an Emerging Transdiscipline, 9(1), 181–212.

Lomnicka, E. (2001). Preventing and Controlling the Manipulation of Financial Markets: Towards a Definition of ‘ Market Manipulation’’. Journal of Financial Crime, 8(4), 297–304.

Losiewicz, P., Oard, D. W., and Kostoff, R. N. (2000). Textual Data Mining to Support Science and Technology Management. Journal of Intelligent Information Systems, 15(2), 99–119.

LR 17346 (2002). Litigation Release No. 17346: Securities and Exchange Commission v. Patrick O. Wheeler, Steven S. Gallers, and Robert L. Carberry, Case No. 02-60131-CIV-GRAHAM (S.D. Fla.) [WWW document] http://www. sec.gov/litigation/litreleases/lr17346.htm (accessed 19th February 2016).

LR 17645 (2002). Litigation Release No. 17645: Securities and Exchange Commission v. Michael A. Ofstedahl, et al., United States District Court for the Northern District of California, Civil Action No. C-02-3685 RS. [WWW document] http://www.sec.gov/litigation/litreleases/lr17645.htm (accessed 19th February 2016).

LR 21423 (2010). Litigation Release No. 21423: Securities and Exchange Commission v. Frank J. Custable, Jr., et al., Civil Action No. 03-CV-2182 (N.D. Ill.) [WWW document] http://www.sec.gov/litigation/litreleases/2010/lr21423. htm (accessed 19th February 2016).

LR 22545 (2012). Litigation Release No. 22545: SEC v. Berton M. Hochfeld et al., Civil Action No. 12-CV-8202 (S.D.N.Y.) [WWW document] http://www.sec. gov/litigation/litreleases/2012/lr22545.htm (accessed 19th February 2016).

MacQueen, J. (1967). Some Methods for Classification and Analysis of Multivariate Observations, in Fifth Berkeley Symposium on Mathematical Statistics and Probability (Berkeley, USA, 1967), pp. 281–297.

Miller, G. A. (1956). The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information. Psychological Review, 63(2), 343–352.

Miller, J. G., and Roth, A. V. (1994). A Taxonomy of Manufacturing Strategies. Management Science, 40(3), 285–304.

Møllgaard, H. P. (1997). A Squeezer Round the Corner? Self-Regulation and Forward Markets. The Economic Journal, 107(440), 104–112.

Ngai, E., Hu, Y., Wong, Y., Chen, Y., and Sun, X. (2011). The Application of Data Mining Techniques in Financial Fraud Detection: A Classification Framework and an Academic Review of Literature. Decision Support Systems, 50(3), 559–569.

Nickerson, R. C., Varshney, U., and Muntermann, J. (2013). A Method for Taxonomy Development and Its Application in Information Systems. European Journal of Information Systems, 22(3), 336–359.

O<sup>¨</sup> g˘u¨t, H., Dog˘anay, M. M., and Aktas¸, R. (2009). Detecting Stock-Price Manipulation in an Emerging Market: The Case of Turkey. Expert Systems with Applications, 36(9), 11944–11949.

Pagano, M., and Immordino, G. (2012). Corporate Fraud, Governance, and Auditing. Review of Corporate Finance Studies, 1(1), 109–133.

Pelleg, D. and Moore, A. (2000). X-Means: Extending K-Means with Efficient Estimation of the Number of Clusters, in 17th International Conference on Machine Learning; Stanford, USA, 2000, pp. 727–734.

Porter, M. F. (2006). An Algorithm for Suffix Stripping. Electronic Library and Information Systems, 40(3), 211–218.

Pozza, C. L., Jr., Cox, T. R., and Morad, R. J. (2009). Review of Recent Investor Issues in the Madoff, Standford and Forte Ponzi Scheme Cases. Journal of Business and Securities Law, 10, 113–132.

Putnins, T. J. (2012). Market Manipulation: A Survey. Journal of Economic Surveys, 26(5), 952–967.

Rapoport, N. B. (2012). Black Swans, Ostriches, and Ponzi Schemes. Golden Gate University Law Review, 42, 627–661.

Rehman, Z., Anwar, W., Bajwa, U. I., Xuan, W., Chaoying, Z., and Patterson, R. L. (2013). Morpheme Matching Based Text Tokenization for a Scarce Resourced Language. PLoS ONE, 8(8), e68178.

Roddenberry, S., and Bacon, F. (2011). Insider Trading and Market Efficiency: Do Insiders Buy Low and Sell High? Journal of Finance & Accountancy, 8, 1–15.

Rokach, L. and Maimon, O. (2005). Clustering Methods, in O. Maimon and L. Rokach, (eds.), Data Mining and Knowledge Discovery Handbook, New York: Springer US, pp. 321–352.

Rowley, J., and Slack, F. (2004). Conducting a Literature Review. Management Research News, 27(6), 31–39.

Sabherwal, S., Sarkar, S. K., and Zhang, Y. (2011). Do Internet Stock Message Board Influence Trading? Evidence from Heavily Discussed Stocks with no Fundamental News. Journal of Business Finance & Accounting, 38(9–10), 1209–1237.

Scopino, G. (2015). The (Questionable) Legality Of High-Speed Pinging and Front Running in the Futures Market. Connecticut Law Review, 47(3), 607–697.

Shapiro, S., Kinkela, K., and Harris, P. (2012). Churning and Suitability of Investments: A Financial Industry Regulatory Authority Arbitration Case Study. Review of Business & Finance Case Studies, 3(1), 61–67.

Shleifer, A., and Vishny, R. W. (1997). A Survey of Corporate Governance. The Journal of Finance, 52(2), 737–783.

Tabrizi, S. A., Shakery, A., Asadpour, M., Abbasi, M., and Tavallaie, M. A. (2013). Personalized PageRank Clustering: A Graph Clustering Algorithm Based on Random Walks. Physica A: Statistical Mechanics and its Applications, 392(22), 5772–5785.

Thel, S. (1993). 850,000 in Six Minutes-The Mechanics of Securities Manipulation. Cornell Law Review, 79(2), 219–298.

Tripp, M. J. W. (1963). Securities Regulation: Stock Scalping by the Investment Adviser: Fraud or Legitimate Business Practice? California Law Review, 51(1), 232–245.

U.S. Commodity Futures Trading Commission (CFTC) (2016). Education Center: CFTC Glossary [WWW document] http://www.cftc.gov/ consumerprotection/educationcenter/cftcglossary/glossary\_b (accessed 4th August 2016).

Vaughan, L. (2016). Broken Benchmarks: Six Years of Probes into Financial Fiddling [WWW document] https://www.bloomberg.com/quicktake/brokenbenchmarks (accessed 25th August 2016).

Vila, J.-L. (1989). Simple Games of Market Manipulation. Economics Letters, 29(1), 21–26.

Webster, J., and Watson, R. T. (2002). Analyzing the Past to Prepare for the Future: Writing a Literature Review. Management Information Systems Quarterly, 26(2), 3.

Wheeler, R., and Aitken, S. (2000). Multiple Algorithms for Fraud Detection. Knowledge-Based Systems, 13(2), 93–99.

Willett, P. (1988). Recent Trends in Hierarchic Document Clustering: A Critical Review. Information Processing and Management, 24(5), 577–597.

Willett, P. (2006). The Porter Stemming Algorithm: Then and Now. Electronic Library and Information Svstems, 40(3), 219–223

Ye, J. (2011). Cosine Similarity Measures for Intuitionistic Fuzzy Sets and Their Applications. Mathematical and Computer Modelling, 53(1), 91–97.

Zahedi, F. M., Abbasi, A., and Chen, Yan. (2015). Fake-Website Detection Tools: Identifying Elements that Promote Individuals’ Use and Enhance Their Performance. Journal of the Association for Information Systems, 16(6), 448–484.

Zhou, L., Burgoon, J. K., Twitchell, D. P., Qin, T., Nunamaker, Jr, and Jay, F. (2004). A Comparison of Classification Methods for Predicting Deception in Computer-Mediated Communication. Journal of Management Information Systems, 20(4), 139–166.

## About the Authors

Michael Siering is a Postdoctoral Research Associate at Goethe University Frankfurt and works as a Business Consultant in the field of risk management. His research focuses on decision support systems in electronic markets, with a focus on the analysis of user generated content. His work has been published in Decision Support Systems and the Journal of Management Information Systems.

Benjamin Clapham (clapham@wiwi.uni-frankfurt.de) is a Graduate Researcher at Goethe University Frankfurt. He received his M.Sc. degree in Management with majors in Finance and Accounting from Goethe University. His research interests include market microstructure, algorithmic trading, sentiment analysis, and financial market manipulations.

Oliver Engel (oliengel@gmx.de) holds a M.Sc. degree in Management from Goethe University Frankfurt, with a specialization on e-finance. His research focuses on text mining and financial market manipulations.

Peter Gomber (gomber@wiwi.uni-frankfurt.de) holds the Chair of e-Finance at the Faculty of Economics and Business Administration, University of Frankfurt. His academic work focuses on market microstructure and auction theory, institutional trading, innovative concepts/technologies for electronic trading and post trading systems and information systems in Finance.
