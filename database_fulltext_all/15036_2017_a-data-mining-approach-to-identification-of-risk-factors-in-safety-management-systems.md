---
otero_id: 15036
otero_key: "N2BAMFE3"
title: "A Data-Mining Approach to Identification of Risk Factors in Safety Management Systems"
authors: "Donghui Shi; Jian Guan; Jozef Zurada; Andrew Manikas"
year: "2017"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2017.1394056"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Data-Mining Approach to Identification of Risk Factors in Safety Management Systems

Donghui Shi, Jian Guan, Jozef Zurada & Andrew Manikas

To cite this article: Mining Approach to Identification of Risk Factors in Safety Management Systems, Journal of Management Information Systems, 34:4, 1054-1081, DOI: 10.1080/07421222.2017.1394056

To link to this article: https://doi.org/10.1080/07421222.2017.1394056

![](/api/attachments/N2BAMFE3/fulltext/images/8dd9fd3233620a997184e26fe66ccc1d0ea830dbf1379420a0a07f36febeb5ff.jpg)

Published online: 02 Jan 2018.

![](/api/attachments/N2BAMFE3/fulltext/images/e4d39fec3d961746ddbd959813a42ecb7f17a9042bb3ff7893e6866c98cd3df3.jpg)

Submit your article to this journal

![](/api/attachments/N2BAMFE3/fulltext/images/3d037105100fa21f64fa922ba3aff7deac7c8ff7fad5a8eb2ed1a657b1f1d676.jpg)

Article views: 21

![](/api/attachments/N2BAMFE3/fulltext/images/0471b017daa62d1cd12ce4e6e0d94cc177d307d0b904d5e7510e1b0891a1d354.jpg)

View related articles

![](/api/attachments/N2BAMFE3/fulltext/images/c78a076d35b3a3151d4e375ecd97c524780a8cdc7705399f9954a9e90bd2078f.jpg)

View Crossmark data

# A Data-Mining Approach to Identification of Risk Factors in Safety Management Systems

DONGHUI SHI, JIAN GUAN, JOZEF ZURADA, AND ANDREWMANIKAS

DONGHUI SHI (sdonghui@gmail.com) is a professor in the Department of Computer Engineering, School of Electronics and Information Engineering, Anhui Jianzhu University, China. He received his Ph.D. in computer science from the University of Science and Technology of China. His research interests focus on machine learning and data mining, especially in adaptive neuro-fuzzy inference systems, data stream, and text mining. His recent work applies data-mining algorithms to solve practical problems in aviation safety, real estate, biomedicine, and power load forecasting.

JIAN GUAN (j0guan01@louisville.edu) is an associate professor of computer information systems in the College of Business, University of Louisville, Kentucky. He received his Ph.D. in computer science and engineering from the Speed Scientific School, University of Louisville. His research interests lie in data mining and its applications.

JOZEF ZURADA (jozef.zurada@louisville.edu; corresponding author) is a professor in the Department of Computer Information Systems, College of Business, University of Louisville and a professor at WSB Gdansk, Poland. He received his Ph.D. in computer science engineering from University of Louisville, Kentucky, and D.Sc. from the Polish Academy of Sciences, Warsaw, Poland. His research interests include applications of advanced computational intelligence methods for assisting in decision making in business and manufacturing systems and streaming data analytics.

ANDREW MANIKAS (asmani01@exchange.louisville.edu) is an assistant professor in the Management Department at the University of Louisville. He earned his Ph.D. from Georgia Institute of Technology. He was previously a management consultant for KPMG Peat Marwick, CSC, and Deloitte Consulting. He is a CCP (certified computing professional).

ABSTRACT: Incident reporting and investigation are components of safety management systems. Timely and accurate identification of risk factors is crucial to effective prevention strategies. However, risk factor identification is often hampered by size, complexity, and the need for human involvement in categorizing incident data. We present a data-mining approach to incident risk factor identification and analysis using data from the Aviation Safety Reporting System, which is part of the Federal Aviation Administration. Our approach is an attempt to overcome obstacles related to labor intensive manual identification of risk factors as well as incomplete data. First, topical mining techniques convert underused textual data (incident narratives) to serve as model input. Second, data-streaming algorithms are used to incrementally build and test classification models for risk factor identification. Three different classification algorithms were tested providing overall accuracy rates ranging from 76 percent to 88 percent, demonstrating the potential for effective use of large and unstructured incident data in safety management. Our research presents and demonstrates an approach to automated incident type identification and contributes to our understanding of the use of text-mining and data-streaming technologies in improving safety management systems.

KEY WORDS AND PHRASES: automated incident identification, data stream, clustering, incident cause evaluation, incident cause identification, safety management systems, text mining, topic mining.

An important part of a safety management strategy is the incident reporting and investigation system [20]. Incident reporting systems are used at different levels ranging from individual plant-based systems [36] to sector or industry-wide systems [5, 16]. Examples of sector/industry incident reporting systems include the Major Accident Reporting System for European chemical accidents [16] and the Aviation Safety Reporting System (ASRS), a joint effort by the Federal Aviation Administration (FAA) and the National Aeronautics and Space Administration (NASA) [5]. While the role of incident reporting systems is well recognized, and in some cases data collection has been ongoing for a long time, there is still a gap between incident data and effective safety improvement strategies [1, 36, 41, 42]. An important reason for this is the lack of adequate analysis of the incident data often due to the massive amount of manual work required [1, 34]. A case in point is aviation safety and its incident reporting system, ASRS. The goal of ASRS is to enhance aviation safety by providing a venue where pilots, air traffic controllers, flight attendants, mechanics, ground personnel, and others involved in aviation operations can share information about unsafe situations that they have encountered or observed during flight or on the ground [5]. The reports contain both structured and textual data. A critical field in these reports is the textual description in each incident report. Reports are generated as a data stream from airports in the United States on a daily basis. Since its inception in 1976, the number of reported incidents has increased dramatically to almost 400 per day [34]. One important task in the analysis of these incidents is the identification of the primary factor for each incident. Currently these primary factors are determined by human experts through time-consuming manual identification [41].

Effective analysis and use of aviation incident reports for risk management are hampered by the inherent complexity of aviation operations due to the interactions of human operators, aircraft, airport, weather, and myriad other factors [1, 5].

Analysis of incidents is further complicated by the data issues of the fast-growing collection of incident reports, such as unbalanced data and missing data. Finally, the unstructured textual narratives in the incident reports are very informative and existing studies clearly point to the need for further research into the use of textual data for risk identification [1, 3].

This study presents a data-mining approach to risk factor identification for aviation incidents using the incident narrative as the independent variable. Latent semantic analysis (LSA) is used to transform each narrative into topical weights based on patterns of co-occurrences of the terms in the narratives. A data-streaming model is used to train the risk factor classifiers. The resulting classifiers produce accuracy rates ranging from 76 percent to 88 percent for risk factor identification, thus demonstrating the viability of our approach. The research presented in this article is significant as it demonstrates the feasibility of an automated approach to the analysis of incident data and such feasibility can potentially be extended to general risk management for two important reasons. First, with an increasingly data-economy digital collection of data, and unstructured text data in particular, the need for automated unstructured analysis will only accelerate [17, 31, 46]. Thus it is important for risk identification and management research to consider this important source of input. Second, the approach described in the study demonstrates the feasibility of a data-streaming approach to building classification models. Explosive growth in data volume has started to present challenges to the traditional style of batch machine learning [9]. An understanding of how incremental learning using data streaming is important to the efficient and effective construction of machine learning models in a big data environment. The overall contribution of the article is perhaps best described in the tradition of design science research in information systems (IS) [21, 23, 39]. This research represents a situated implementation of a new approach to designing the incident data analysis in a well-defined environment—aviation risk management. The demonstrated effectiveness of the approach contributes to our understanding of possible solutions to an identified weak link in risk management [7]. The direct relevance of the research described in this article and its practical implications for risk management in general are recognized as a key distinguishing feature of design science research [47].

## Relevant Literature

Incident reporting and investigation are critical components of a risk modeling and management system. In recent years, various changes such as technological advances, increasing discrepancy between engineering techniques and safety engineering techniques, and more complex relationships between human operators and automation, have combined to stretch the limits of existing risk models [30, 42]. To address these challenges, new paradigms are needed [30]. Vital to the success of efforts to establish new paradigms is the accurate and timely identification of contributing factors to incidents [11]. An excellent example of such a situation is the aviation incident reporting system. The ASRS receives, processes, and analyzes voluntarily submitted incident reports from pilots, air traffic controllers, dispatchers, cabin crew, maintenance technicians, and others [34]. Reports submitted to the ASRS may describe both unsafe occurrences and hazardous situations. Information is gathered from these reports and disseminated to stakeholders. The ASRS’s particular concern is the quality of human performance in the National Airspace System [5]. While each incident report contains close to 100 attributes, the textual narrative remains the most valuable source of information on why the incident happened [41]. Though a human factor is the most likely cause for an incident, other types of factors exist [1, 41]. However, the analysis of these incidents is a daunting task that involves intensive manual work by human experts [1, 41]. The task of identifying the contributing factor is made more difficult by the fact that a majority of the incidents have an extremely high level of missing values in their structured fields (more details provided in a later section).

The voluntarily submitted reports on aviation incidents in the ASRS database are currently analyzed manually by experienced pilots, air traffic controllers, and aviation safety analysts [41]. Most incidents have been assigned 1 of 11 primary factors by human analysts. Because of the many incomplete structured fields in an incident report, the narrative remains the best source of information for explaining the major cause of the incident [41]. Existing research has focused on the automation of textual analysis with the objective of identifying incident causes. Existing studies have examined the use of different natural language processing (NLP) techniques in automating the cause identification process. Posse et al. [41] used textual templates to identify human factors from the incident narratives with positive results, but the results were based on a small sample of 20 incident reports. Moreover, their study used human experts (manual work) to create the lexicons for the known causes [41]. Data-mining algorithms such as support vector machine and nonnegative matrix factorization have also been used to classify the incident reports with help from human reviewers, with a focus on clustering incident reports [38]. However, the authors used the sparse document-term matrix as direct input to the machine learning algorithms without applying NLP preprocessing and dimension reduction techniques. Another study also used support vector machine (SVM) to build a classifier to identify incident causes [1]. Abedin et al. [1] used a modified Basilisk framework to automatically augment a seed lexicon. The resulting lexicon is used in an SVM classification for identifying incident causes. This use of a lexicon to identify incident causes is also found in a more recent study, but the authors acknowledge the difficulty with their approach to capture the potentially very useful latent meaning that exists in the documents [3]. Yet another study used a similar approach where the authors tested an SVM to classify incident reports using word frequencies [6]. Another study examined the various NLP techniques and the use of latent semantic indexing to cluster incident reports for knowledge discovery [40]. For example, hierarchical clustering can be used to identify new patterns and trends in operations. One common agreement among these studies is the importance of the narrative in the incident report and the need for more research into exploring this unstructured data source for better identification of incident causes. In addition, two main characteristics of these studies are (1) the use of a lexicon/thesaurus in the identification, and (2) the use of data-mining algorithms in clustering or classification of incident reports.

The above studies all use traditional batch learning algorithms and evaluation measures. In traditional batch learning, multiple models are constructed through selecting training and test data randomly from a limited data set. The final classification accuracy rate is obtained by averaging over the number of models created for different folds and runs. A k-fold cross-validation method is commonly used to evaluate the classification performance of models [51]. However, the main disadvantage of batch learning is that it does not use the incremental incident data that accumulate in real time. The aviation incidents report analysis can potentially benefit from a data-stream approach. Data-stream learning algorithms can take snapshots at different times during the induction of a model to see how much the model improves or worsens over time [9, 35].

A data-stream environment has requirements different from those in the traditional setting [35]. The most significant features are: (1) process one example at a time, and inspect it only once, (2) use a limited amount of memory, (3) work in a smaller amount of time, and (4) be ready to predict at anytime. The process of streamlearning algorithms is a repeated cycle [35]. The model constructed from initial data is constantly updated according to input cases from the stream. The algorithms execute in a limited amount of memory and within a much shorter time period than a full batch processing of all data at once. Therefore, a predictive model can be updated after processing a new input case. Common learning algorithms in stream scenarios are classification, clustering, and outlier analysis. Recent studies in datastream systems show significant progress in the use of data-stream methods in these areas. Examples of prior work include the research on data-stream clustering algorithms [8, 9], classification models for real estate data stream [48], and the use of the kappa statistic for evaluating time-changing Twitter data streams with unbalanced classes [8].

The aviation incident reports data set presents unique challenges that can be addressed by data-stream methods. The incident reports are unbalanced, as a majority of the records have been classified by human experts as the incidents being caused by human-related factors, while fewer records were classified as nonhuman factors. In a traditional batch learning setting, oversampling and undersampling [50] can be used to alter the class distribution of the training data for an unbalanced data set. The disadvantage with undersampling is that it discards potentially useful data. The main disadvantage with oversampling is that by artificially making exact or very similar copies of existing cases, it makes overfitting likely. Another approach used to analyze unbalanced data sets in batch learning setting is cost-sensitive learning [45]. In this article, we study the performance and evaluation measures of classification models constructed from the data stream of aviation incidents with unbalanced class labels. Topical mining is used to convert incident narratives into weights for the classifiers. Though topical weights have been used previously in the clustering of incidents, the approach presented in this study uses topical weights for incident cause identification because an effective and automated approach to identify incident types still remains a main challenge.

Topic mining and data mining, critical to the research described in this article, are emerging areas in information systems (IS) research. Topic mining is a relatively new area of research in IS and has mostly focused on the use of text-mining techniques in document clustering and analysis [18, 28, 32, 46]. These studies use topical mining to find latent structures or groupings that exist within a corpus. The LSA method has proved useful for uncovering meaningful clusters of research within large collections of abstracts of academic articles. A technique similar to LSA has recently been used in an identification and profiling system to capture latent features in textual communication [31]. Thus we begin to see research where the features extracted from textual content are used as input to a different model, including sentiment analysis models [19]. Evangelopoulos et al. [17] recommend the use of LSA as a precursor to predictive modeling in IS research. This study uses the extracted features of LSA as input to a supervised learning model, a classification model to identify incident causes.

The research described in this article follows the guidelines of the design science paradigm in IS research [21, 23, 39, 47]. The main contribution of the research in this study is an approach to automate incident cause identification in a well-defined real-world environment—that is, aviation safety management. The results of the research have direct relevance and applicability to risk analysis and risk management in an important industry [21]. More specifically, the approach described here addresses the key issue of incident cause identification. The use of dimension reduction techniques for textual data and a classification model with data streaming presents a novel and viable approach to a well-identified problem. The above approach is demonstrated in an instantiated implementation using 168,227 incident reports spanning 24 years [21]. Careful evaluation of the implementation is provided with common metrics and comparison with a baseline implementation using traditional batch approach to classification model construction [39].

## Data Description

The ASRS is a NASA-supported accident data collection system to help understand the causes of aviation incidents and an attempt to reduce similar incidents in the future [5]. Since its inception in 1976, the ASRS has accumulated a large of number incidents. In recent years the daily intake of reported incidents has increased dramatically. Figure 1 shows a daily intake of 372 incidents by 2015 [34]. This study used nearly 24 years of data representing 168,227 incident reports downloaded from the ASRS [5]. The data consist of incidents reported from January 1988 to July 2012. Each incident report contains 96 data fields including time, place, environment, aircraft, component, and personnel. The unstructured textual data contain narratives provided by the flight and ground crews about the incidents. The dependent variable is the Primary Problem, manually determined by human experts after careful examination of each report. There are 11 categories of the Primary Problem. Close examination of the data has identified 10,180 incidents for removal. These removed incident reports include 10,157 with no values for the dependent variable and 23 with no incident narrative. As a result, the final data set consists of 158,047 incident reports/observations. There are 11 distinct Primary Problems, as listed in Table 1. Human Factor remains the overwhelming factor (“Event Primary Problem”) for aviation incidents at 61.67 percent. The second largest category of incident primary problems, Aircraft, accounts for another 20.12 percent. The remaining nine categories are much smaller, as can be seen in Table 1.

![](/api/attachments/N2BAMFE3/fulltext/images/651dc236adb1c10ffc377713cf4d1f32a227661b7fcb43ea2b6d967f0abbd38e.jpg)  
Figure 1. Monthly Report Intake

Another interesting characteristic of the data is shown in Figure 2. Figure 2 shows the distribution of the four most common categories (classes) of incidents: Human factor, Aircraft, Ambiguous, and Weather. Class rate is defined as (the quantity of the class or category included in every 1,000 incidents)/1,000. One can see in the later part of the curves that Human Factor class rate decreases while those of Aircraft and Ambiguous increase. As will be discussed later, these fluctuations in class distributions will affect accuracy rates of classifiers but it is easier to isolate the effects of changes in class distributions with data streaming as batch processing does not account for drift.

Table 1. Categories of Incidents

<table><tr><td>Category</td><td>Incidents</td><td>Percent</td></tr><tr><td>Human Factor</td><td>97,466</td><td>61.67</td></tr><tr><td>Aircraft</td><td>31,792</td><td>20.12</td></tr><tr><td>Ambiguous</td><td>7,757</td><td>4.91</td></tr><tr><td>Weather</td><td>4,812</td><td>3.04</td></tr><tr><td>Company Policy</td><td>4,770</td><td>3.02</td></tr><tr><td>Airport</td><td>3,707</td><td>2.35</td></tr><tr><td>Ambiguous; Ambiguous; Ambiguous</td><td>3,707</td><td>2.35</td></tr><tr><td>ATC Equipment/Nav Facility/Buildings</td><td>2,102</td><td>1.33</td></tr><tr><td>Chart or Publication</td><td>1,832</td><td>1.16</td></tr><tr><td>Environment—Nonweather-Related</td><td>1,254</td><td>0.79</td></tr><tr><td>Airspace Structure</td><td>578</td><td>0.37</td></tr></table>

![](/api/attachments/N2BAMFE3/fulltext/images/fe7ac0f1f05a66b983929ca88c786b25c0accb73b4b15b77043254f8896bf6de.jpg)  
Figure 2. The Distribution of the Top Four Categories of Incidents

While there are 96 fields, many of these fields have missing values. The four fields with no missing values in our final data set are Report ID, Report Date, Narrative, and Primary Problem (the dependent variable). Table 2 summarizes the missing values for the rest of the fields (92). The first column represents the percent of missing values in a field. The second column represents the number of fields that have the corresponding percent of missing values. The last column represents the second column as a percent of all fields. For example, 55.43 percent of the fields are missing up to 80 percent of their values. Thus incomplete data make it very difficult to get reliable classification results using the structured data fields.

Table 2. Missing Values

<table><tr><td>Percent of values missing</td><td>Number of fields</td><td>Percent of all fields</td></tr><tr><td>10</td><td>76</td><td>82.61</td></tr><tr><td>20</td><td>70</td><td>76.09</td></tr><tr><td>30</td><td>68</td><td>73.91</td></tr><tr><td>40</td><td>67</td><td>72.83</td></tr><tr><td>50</td><td>62</td><td>67.39</td></tr><tr><td>60</td><td>61</td><td>66.30</td></tr><tr><td>70</td><td>58</td><td>63.04</td></tr><tr><td>80</td><td>51</td><td>55.43</td></tr><tr><td>90</td><td>41</td><td>44.57</td></tr><tr><td>100</td><td>3</td><td>3.26</td></tr></table>

Kantardzic [27] recommends several methods for dealing with missing values for numeric and categorical variables. The solutions for handling missing values may be viable if only a small or moderate percentage of the data have missing values. Given the massive amount of missing data in the structured fields, the replacement of missing values in the aviation data set used in this study may introduce noise and bias to the data set and it cannot be objectively justified. Also, many structured variables in the aviation data set are of the nominal/categorical type and take on many distinct values. To properly code nominal variables as input to the models, one would have to create a new dummy attribute for each distinct value for each of these variables. This would substantially increase the number of input variables to the models and make the classification difficult. For the above reasons, we chose to use only unstructured data in our analysis. This examination of the ASRS data thus makes a compelling case for the use of text data for classifying incident reports. Table 3 lists two sample incidents used in our modeling process. One incident has Aircraft as the primary problem and the other has Human Factor as the primary problem.

## Classification Modeling Using Textual Data

The main objective of this study is to present an approach to effectively and automatically classify risk factors for aviation risk management. Aviation incidents provide a compelling case as lives depend on rapidly identifying the sources of incidents to prevent future issues. Aviation incidents in the form of textual narratives for these incidents provide the model input data. As discussed earlier, the unstructured narrative data will be used in our solution approach due to the high level of missing values for structured fields. Figure 3 shows the architecture of this approach. Topic modeling using latent semantic analysis extracts features from the narratives and the resulting latent topics/singular value decompositions (SVDs) serve as input to data-streaming machine learning. Traditional batch-based learning where the original data set is divided into training, validation, and testing subsets is provided to establish a baseline for comparison with the results from data-stream learning. Two different strategies were used in evaluating the data-stream classifiers. First, the Holdout measure can evaluate a classifier on a stream by periodically testing a holdout set [10]. Second, the Prequential measure can evaluate a classifier on a stream by testing then training each sample incident in sequence. In this case a sliding window or a fading factor mechanism can be used in the measure [10]. The components of the architecture are described below in more detail.

As a preliminary step, the textual content in incident narratives were preprocessed with some simple techniques (NLP). There were a total of 517,615 unique terms. These include stemming, the use of stop terms (default stop terms from SAS), and

Table 3. Sample Incidents

<table><tr><td>Variable name</td><td>Sample record</td></tr><tr><td colspan="2">Sample Incident with Aircraft as the Primary Problem</td></tr><tr><td>ACN(ID)</td><td>448519</td></tr><tr><td>Report Date</td><td>September 1999</td></tr><tr><td>Primary Problem</td><td>Aircraft</td></tr><tr><td>Narrative</td><td>DURING VISUAL APCH (Approach) AT APPROX 200 KIAS, FLAPS HANDLE WAS PLACED IN POS (Position) #1 BRIEFLY AND THEN POS #2. ECAM (Electronic Centralized Aircraft Monitoring)MESSAGE WAS ANNUNCIATED FOR SLATS FAULT. ECAM PROC WAS FOLLOWED WHICH CALLED FOR RECYCLING OF FLAPS. SLATS REMAINED AT ZERO DEGS (Degrees) BUT FLAPS EXTENDED NORMALLY. AN UNEVENTFUL LNDG (Landing) WAS MADE.</td></tr></table>

Sample Incident with Human Factor as the Primary Problem

ACN(ID) 530949

Report Date November 2001

Primary Problem Human Factor

<table><tr><td>Narrative</td><td>THE STUDENT AND I ONLY HAD KNOWLEDGE FROM THE ZZZ FSS (Flight Service Station) TO BASICALLY ‘STAY AWAY’ FROM THE ZZZ VOR (Very-high-frequency Omnidirectional Range) BECAUSE A PWR (Power) PLANT WAS NEAR BY. THE FAA HAD HASTILY ENACTED THE NO FLY ZONES AROUND THE PWR PLANTS. WE THOUGHT THAT IF WE STAYED ABOUT 20 MILES OR SO AWAY FROM THE ZZZ VOR WE&#x27;D BE FINE. COMING BACK FROM THE SE PRACTICE AREA WE CALLED ZZZ1 APCH TO ASK FOR VECTORS BACK TO ZZZ2 TO STAY AWAY FROM THE ZZZ VOR AND THE PWR PLANT AIRSPACE. THEY GAVE US VECTORS TO ZZZ2 AND A FEW MINUTES LATER STATED THAT RADAR HAD TRACKED US OVER THE ZZZ PWR PLANT RESTR AREA (TFR). THE STUDENT COPIED DOWN A PHONE # AND CALLED IT UPON REACHING THE GND (Ground). WE THEN FOUND OUT THAT THERE WAS NOT JUST ONE PWR PLANT, BUT MULTIPLE WITH 10NM DIAMETER TFR&#x27;S. WE THOUGHT THERE WAS JUST THE ONE. WE AS GENERAL AVIATION PLTS FEEL THESE TFR&#x27;S WHICH WERE ENACTED THEN DETRACTED WITHIN A WEEK, SHOULD NOT HARM ANY OF OUR RECORDS OR FUTURE AVIATION CAREERS. THERE ARE NO NAVAIDS ON THESE PWR PLANTS AND REALLY NO WAY FOR US TO KNOW EXACTLY WHERE DOES THE 10 NM (Nautical Mile) RING BEGIN OR END. WE DID OUR AIRWORK 20 TO 30 NM DME (Distance Measuring Equipment) AWAY FROM VOR. WE THOUGHT THIS WAS ENOUGH. AGAIN, WE NEVER KNEW ABOUT THE OTHERS.</td></tr></table>

no parts of speech differentiation. Terms that appear in less than four narratives were also dropped from consideration. Since the authors are not experts in aviation operations, no synonyms were created or used and no custom stop terms were added. Given the ability of synonyms and custom stop terms to differentiate documents, properly constructed lists of synonyms and custom stop terms have the potential to improve classification performance. After NLP preprocessing, the collection of narratives is represented by a matrix $A ,$ where $a _ { i j }$ is the number of times a term i occurs in the narrative $j .$ Therefore A is an m × n term-by-narrative matrix with m = the number of unique terms (71,403) and n = the number of narratives/ incidents (158,047). A weighting function was then applied to each nonzero element $a _ { i j }$ of A. The weight function used in this study is as follows [12, 33]:

![](/api/attachments/N2BAMFE3/fulltext/images/6b69d861911330c7ab9ff116e389ebb96af490d8ac9294eb0df45bdc10ada68b.jpg)  
Figure 3. An Automated Approach to Identify Incident Causes in Aviation Safety Systems

$$
a _ {i j} = \operatorname{local} \left(a _ {i j}\right) * \operatorname{global} (i),
$$

where $l o c a l ( a _ { i j } )$ is the local weighting function for term i in narrative j and global(i) is the term’s global weighting function. The local weight function is directly related to the frequency of occurrence of the term in the narrative and the global weight function is inversely related to the frequency of the term across all the narratives in the collection of incidents. In the study the local weighting function is as follows [12]:

$$
\operatorname{local} \left(a _ {i j}\right) = \log \left(a _ {i j} + 1\right),
$$

where $a _ { i j }$ is the narrative-specific frequency for term i in narrative j. The global weighting function is [12]:

$$
\operatorname{global} (i) = 1 + \sum_ {j = 1} ^ {n} \frac {\frac {a _ {i j}}{f _ {i}} \log_ {2} \left(\frac {a _ {i j}}{f _ {i}}\right)}{\log_ {2} (n)},
$$

where $f _ { i }$ is the number of times term i appears in the collection of all the narratives. Singular value decomposition was used to transform the weighted matrix A into a reduced, dimensional representation [29]. Let A be the weighted term-by-document matrix. SVD computes the matrices U, , and V so that:

$$
A = U \Sigma V ^ {T},
$$

where U is a matrix of orthogonal matrix whose rows form the left singular vectors of A, V is an orthogonal matrix whose columns form the right singular values of A, and  is a diagonal matrix containing the square roots of eigenvalues from U or V in descending order [29]. U are the term loadings and V  are the narrative loadings.

The dimension reduction power behind SVD comes from an important property of SVD. The matrix A can be approximated by keeping the first k dimensions produced by SVD [29] or:

$$
A \approx A _ {k} = U _ {k} \Sigma_ {k} V _ {k} ^ {T}.
$$

The approximation can be successfully improved by increasing the value of k. The determination of the best k is still an open question [17, 22, 28]. In our study the best k was determined to be 24 based on two considerations consistent with recommendations in [17]. The first criterion for selecting k was based on an examination of a scree plot of the first 100 SVDs. As can be seen in Figure 4 a value of k = 24 occurs reasonably well within the range where the elbow occurs by visual inspection. However, other values of k could also be considered as possible “elbows,” such as 4, 7, or 17. Therefore the second criterion, based on experimentation, led to our decision to settle on k = 24. According to Albright [2] the optimal k value falls between 10 and 200, and “the precise number to use needs to be learned through experimentation and varies with the text.” Several different values of k were tried in our case and the resulting SVDs were used to test the classification models. A value of 24 for k yielded the best results in this study.

Each narrative was assigned a weight for each of the resulting SVD dimensions. Thus each narrative has 24 weights, each of which is the normalized sum of its local weights multiplied by their term topic weights [12]. These weights were subsequently used as input to the classifiers.

The ASRS aviation incident classification is a multiclass classification problem, where the task is to classify instances into one of the multiple possible classes (Primary Problem). A common solution is to treat the problem of multiclass classification as one of multiple binary classification problems [44]. Consistent with recommendations in Sebastiani [44], cause identification in this study is modeled as a collection of 11 independent binary classifiers corresponding to the 11 categories of Primary Problem (dependent variable) in the ASRS data set. For example, in the Human Factor classifier each incident with its Primary Problem = Human Factor is assigned a 1, and 0 otherwise. For the Aircraft Classifier each incident with its Primary Problem = Aircraft is assigned a 1, and 0 otherwise. Due to space constraint the next section only reports results from the two largest categories.

![](/api/attachments/N2BAMFE3/fulltext/images/cafc4d884b1068ef69971c5bea8c1cb3c1429168036ed168c59a55cd6e07dd67.jpg)  
Figure 4. Scree Plot for SVDs

These top two categories, Human Factor and Aircraft, account for over 80 percent of all the incidents.

In the study, we used Massive Online Analysis (MOA) as the platform for datastream learning and evaluation. MOA is a system for online learning from data streams [9]. To make the results as comparable as possible we used Weka 3.7 as the platform for batch learning. Figure 3 shown earlier provides the general architecture of the relationship among the textual input incident narratives, the extracted weights, the incident cause identification, and evaluation.

## Data-Streaming Classification Algorithms

Three algorithms were tested in our study, specifically, naive Bayes (NB) [14], Hoeffding tree (VFDT) [15], and OzaBagADWIN (OBA) [43]. The three algorithms are incremental and low computational cost algorithms that are suitable for large data sets. Most common machine learning algorithms, such as neural network, support vector machine, and random forest, would not process a data set of the size of this aviation problem in an acceptable amount of time.

NB performs classic Bayesian prediction while making the naive assumption that all inputs are independent [26]. NB is a classification algorithm known for its simplicity and low computational cost. Let C be the random variable denoting the class of an incident I and let $x _ { 1 } , \cdots , x _ { l }$ be a vector of l attributes, the weights extracted from the narratives in the case of this study. In NB classification the probability of an unobserved incident $I = ( x _ { 1 } = \nu , \cdot \cdot \cdot , x _ { l } = \nu _ { l } )$ being in class c is calculated as:

$$
P r [ C = c | I ] \cong \prod_ {i = 1} ^ {l} P r [ x _ {i} = v _ {i} | C = c ] = P r [ C = c ] \cdot \prod_ {i = 1} ^ {l} \frac {P r [ x _ {i} = v _ {i} \wedge C = c ]}{P r [ C = c ]}
$$

where $P r [ x _ { i } = \nu _ { i } \land C = c ]$ and $P r [ C = c ]$ are calculated from the training sample.

VFDT is an incremental, anytime decision tree induction algorithm that is capable of learning from data streams. VFDT exploits the fact that a small sample can often be enough to choose an optimal splitting attribute. This idea is supported mathematically by the Hoeffding bound [15, 24]. For a real-valued random variable r with range R, let r be the mean of n independent observations of r. The Hoeffding bound states that, with probability $1 - \delta ,$ the true mean of the variable is at least $\bar { r } - \varepsilon ,$ where:

$$
\varepsilon = \sqrt {\frac {R ^ {2} l n \left(\frac {1}{\delta}\right)}{2 n}}.
$$

The attractive feature of a Hoeffding tree is its performance.

OBA [9] is an incremental online bagging and boosting algorithm for data streams developed by Oza and Rusell with the addition of the ADWIN algorithm as a change detector and as an estimator for the weights of the boosting method. When a change is detected, the worst classifier of the ensemble of classifiers is removed and a new classifier is added to the ensemble.

## The Evaluation Measure for Data Streams

In batch learning, the evaluation measure allows training data and test data to be selected for constructing the models and then performs the tests repeatedly. The traditional batch learning uses cross validation to test the performance and is very time consuming. Two evaluation measures are proposed in the data-stream context: the Holdout method and the interleaved test-then-train or Prequential method [10]. Both methods are designed to build a picture of accuracy over time.

In the Holdout evaluation method the performance measure is obtained by reducing the number of folds given the limited time and memory for stream data. In the second evaluation method, Prequential, a common approach is to let each individual incident be used to test the model before it is used for training, and from this the accuracy can be incrementally updated [9]. Thus, the model is always being tested on incidents it has not seen. This method has the advantage that no holdout set is needed for testing, therefore making maximum use of the available data. It also ensures a smoother plot of accuracy over time, as each individual sample will become increasingly less significant to the overall average.

Prequential is the most common evaluation measure for data streams [10]. Bifet et al. [10] argue that the kappa statistic has advantages over the traditional accuracy measures when data streams have evolving unbalanced classes. The kappa statistic k was introduced by Cohen [13].

$$
k = \frac {p _ {0} - p _ {c}}{1 - p _ {c}}.
$$

The quantity $p _ { 0 }$ is the classifier’s Prequential accuracy, and $p _ { c }$ is the probability that a chance classifier would guess the class of an instance using the proportional split of the data. If the classifier is always correct then $k = 1$ . If its predictions are correct as often as those of a chance classifier, then k = 0. The range of k is [0,1] or [0,100] percent. The kappa statistic is better than traditional measures such as the area under the receiver operating characteristics (ROC) curve (AUC) due to its computational efficiency [8, 13].

## The Experiment Design and Results from Computer Simulation

This study used Weka and MOA for testing the classifiers in both the batch and datastream settings. The batch learning models were created for comparison purposes. We designed four different scenarios for testing and assessing our classifiers. In all four scenarios we used NB, VFDT, and OBA.

Table 4 shows the overall classification results for Scenario 1, the batch learning baseline scenario. For the Human Factor classifier, the OBA algorithm has produced the best performance in terms of the AUC and the mean overall accuracy rates. The AUC and overall accuracy rate for OBA are 0.820 and 76.5 percent, respectively. For the Aircraft classifier OBA has again produced the best performance with 88.3 percent for overall accuracy rate and 0.901 for AUC. We have also provided the ROC charts for the three algorithms in Scenario 1 (see Figures 5 and 6). As can be seen from these ROC charts the results are consistent with those presented in Table 4 with OBA producing the best performance.

To compare with batch learning, we performed a Holdout evaluation in a datastream setting in Scenario 2. The data for testing and training consisted of a stream of 158,047 incidents. The test size was set to 200, the training size was set as 1,000 and the sample frequency was set to 10. Table 5 presents the classification accuracy rates in the Holdout evaluation. For the Human Factor and Aircraft classifiers, the mean accuracy rates for NB, VFDT, and OBA are very close. However, the kappa statistic for VFDT is the worst, at 35.0 percent and 29.2 percent, for the Human Factors classifier and the Airport classifier, respectively. The accuracy rate for nonhuman incident classification and the accuracy rate for aircraft incident classification are very low. Figure 7 depicts the learning curves for NB, VFDT, and OBA for the Human Factor classifiers in the Holdout measure.

The Prequential evaluations described in Scenarios 3 and 4 require setting the sliding window size as it affects the classification accuracy rates and their fluctuations. If the window size is too large and there is a concept (rate) drift, the window possibly contains outdated information and the accuracy of the model may decrease [35]. If the window size is too small, the window may have deficient data and the model overfits as well as suffers from large variances in the classification rates [35]. Previous work considers a fixed value for the size of the sliding window specified by users or an experimental value [8, 9, 35]. Thus, in this study the window sizes (1,000 and 5,000) were chosen experimentally and results for both window sizes are provided for comparison purposes.

In Scenario 3, we performed a Prequential evaluation, testing, and then training, on the same data stream of 158,047 incidents. The same algorithms NB, VFDT, and

Table 4. Classification Results for the Three Algorithms Used in Scenario 1

<table><tr><td rowspan="2">Models</td><td colspan="4">Human Factor</td><td colspan="4">Aircraft</td></tr><tr><td></td><td>Mean accuracy (%)</td><td>Nonhuman Factor cases (%)</td><td>Human Factor cases (%)</td><td></td><td>Mean accuracy (%)</td><td>Nonaircraft cases (%)</td><td>Aircraft cases (%)</td></tr><tr><td>NB</td><td>0.783</td><td>73.2</td><td>62.6</td><td>77.0</td><td>0.863</td><td>81.1</td><td>82.0</td><td>73.2</td></tr><tr><td>VFDT</td><td>0.773</td><td>74.9</td><td>69.3</td><td>74.2</td><td>0.879</td><td>87.0</td><td>95.7</td><td>52.7</td></tr><tr><td>OBA</td><td>0.820</td><td>76.5</td><td>65.2</td><td>81.2</td><td>0.901</td><td>88.3</td><td>95.7</td><td>58.6</td></tr></table>

![](/api/attachments/N2BAMFE3/fulltext/images/44e1cbd1c140551a2de63db1c4557240509e2c76d8ee602261201a1bbd831b73.jpg)  
Figure 5. The ROC Charts Results for the Three Algorithms with Human Factor Data in Scenario 1

OBA were used in the scenario. Window size was set to 1,000. Table 6 reports the total Prequential accuracy rates with a window size of 1,000. Figure 8 provides the learning curves for the Human Factor classifiers. A close examination of Figure 8 suggests that the plots with NB, VFDT, and OBA include many fluctuations. OBA produced the best performance in Prequential evaluation in terms of the accuracy rates and kappa statistics for both the Human Factor and Aircraft classifiers. The results show that in order to obtain steady results, bigger window sizes should be used.

![](/api/attachments/N2BAMFE3/fulltext/images/4f8f9fa0dc0d8e3e118482ef4e3fac0ed2e2520c16adb58851ce827c54065deb.jpg)  
Figure 6. The ROC Charts Results for the Three Algorithms with Aircraft Data in Scenario 1

Table 5. Mean Accuracy Rates for Holdout in Scenario 2

<table><tr><td rowspan="2">Classifier</td><td colspan="4">Human Factor classifier</td><td colspan="4">Aircraft classifier</td></tr><tr><td>Mean accuracy (%)</td><td>Nonhuman Factor cases (%)</td><td>Human Factor cases (%)</td><td>Kappa (%)</td><td>Mean accuracy (%)</td><td>Nonaircraft cases (%)</td><td>Aircraft cases (%)</td><td>Kappa (%)</td></tr><tr><td>NB</td><td>76.7</td><td>54.7</td><td>84.2</td><td>38.6</td><td>86.3</td><td>95.3</td><td>47.1</td><td>46.7</td></tr><tr><td>VFDT</td><td>76.6</td><td>55.0</td><td>83.1</td><td>35.0</td><td>86.4</td><td>91.7</td><td>45.8</td><td>29.2</td></tr><tr><td>OBA</td><td>76.8</td><td>55.4</td><td>83.3</td><td>38.5</td><td>87.0</td><td>92.4</td><td>48.4</td><td>35.6</td></tr></table>

In Scenario 4, we performed a Prequential evaluation, testing, and then training with a window size of 5,000. Table 7 reports the total accuracy rates and the Kappa statistics for both the Human Factor classifier and the Aircraft classifier. For the Human Factor classifier, the overall accuracy rate and the kappa statistic for OBA are the best, 77.0 percent and 44.3 percent, respectively. For the Aircraft model, again OBA is the best, yielding 88.5 percent and 59.2 percent, respectively. The

![](/api/attachments/N2BAMFE3/fulltext/images/ff3e1c2f605c8a118e0c06caf352f330931ae1a2dc6573faf1c326ed55f19776.jpg)  
Figure 7. The Classification Accuracy Rates for Holdout in Scenario 2

Table 6. Prequential Mean Accuracy Rates for the Sliding Window Size of 1,000 in Scenario 3

<table><tr><td rowspan="2">Classifier</td><td colspan="4">Human Factor</td><td colspan="4">Aircraft</td></tr><tr><td>Mean accuracy (%)</td><td>Nonhuman Factor cases (%)</td><td>Human Factor cases (%)</td><td>Kappa (%)</td><td>Mean accuracy (%)</td><td>Nonaircraft cases (%)</td><td>Aircraft cases (%)</td><td>Kappa (%)</td></tr><tr><td>NB</td><td>72.7</td><td>63.2</td><td>79.7</td><td>36.3</td><td>79.5</td><td>94.0</td><td>49.5</td><td>47.6</td></tr><tr><td>VFDT</td><td>75.4</td><td>71.6</td><td>77.2</td><td>40.2</td><td>87.1</td><td>90.3</td><td>71.2</td><td>55.5</td></tr><tr><td>OBA</td><td>76.9</td><td>73.7</td><td>78.5</td><td>43.9</td><td>88.4</td><td>90.8</td><td>76.2</td><td>59.0</td></tr></table>

Note: The use of bold font indicates the best results.

Prequential evaluation is also better for unbalanced data than batch learning. In batching learning, classifiers tend to perform well on the majority class but relatively poorly on the minority class [49]. The Prequential evaluation improves the accuracy rates for the minority class and the accuracy rates for 1 and 0 cases are closer to each other. One can compare the performance of OBA in batch learning with the Prequential results. As can be seen in Table 4, the OBA accuracy rates for human factor incidents and nonhuman factor incidents are 81.2 percent and 65.2 percent, respectively. The OBA accuracy rates for aircraft incidents and nonaircraft incidents are 58.6 percent and 95.7 percent, respectively. In Table 7 the OBA accuracy rates for human factor incidents and nonhuman incidents are 78.5 percent and 73.7 percent, respectively. The OBA accuracy rates for aircraft incidents and nonaircraft incidents are 76.2 percent and 90.8 percent, respectively. Table 6 has very similar results. This shows that the Prequential evaluation has a better performance than batch learning for an unbalanced data stream. Figure 9 shows the learning curve for Prequential accuracy for the Human Factor model. We can see that the plot with a window size of 5,000 is smoother. We can see the relationship between the curves of accuracy rates and the curve of the distribution of human factor incidents. Accuracy rates change with category distribution. Some accuracy rates are under 70 percent after the point of 120,000 incidents, accuracy rates are above 73 percent before the point of 75,000 in Figure 9.

Sliding Window Prequential with Size 1000  
![](/api/attachments/N2BAMFE3/fulltext/images/e110ecff3c9839f9051dd7f2d63023381c7d770b410108ba723ce24a141a0f24.jpg)  
Figure 8. Prequential Accuracy Rates for the Sliding Window Size of 1,000 in Scenario 3

Most accuracy rates are above 60 percent from the curve of the class distribution of human factor incidents before 75,000 and the values are under 50 percent after 120,000 incidents have been processed. The decrease in accuracy rates coincides with the decline of the class distribution curve after 120,000 incidents have been processed. NB is more sensitive to the class distribution after the 120,000 incidents have been processed. The VFDT and OBA have a small reduction due to the decrease of the distribution of human factor incidents. From Figure 2, it can be seen that the number of Ambiguous incidents rises after 120,000 incidents. These Ambiguous instances may include many human factor incidents. The changes in distribution in Human Factor and Ambiguous Factor may have caused accuracy rates to decrease.

The kappa statistic, which normalizes a classifier’s accuracy by a chance predictor, is an appropriate measure in data-stream mining due to potential changes in class distribution. Figure 10 represents the kappa statistic plots using Prequential measure with a sliding window size of 1,000 for the Human Factor model in Scenario 3. The kappa value for NB is the lowest at the point of 144,000 incidents in Figure 10. We checked 1,000 incidents before the 144,000 point, from 143,000 to 144,000. The proportion of incidents with Human Factor as the primary factor is 33.5 percent, which is lower than the average value, 61.7 percent. Figure 11 shows the kappa statistic chart of Prequential measure with a sliding window size of 5,000 for the Human Factor model in Scenario 4. In the kappa statistic chart we can also see that the plot with a size of 5,000 is smoother. The plot with a size of 1,000 includes many fluctuations in accuracy rates due to class distribution changes. It shows that OBA has the best performance, much better than the other two algorithms. The figures also reveal that with the decrease of the number of Human Factor incidents, the kappa value decreases. NB is more sensitive to the class distribution than the other two algorithms.

Table 7. Prequential Accuracy Rates for the Sliding Window Size of 5,000 in Scenario 4

<table><tr><td rowspan="2">Classifier</td><td colspan="4">Human Factor</td><td colspan="4">Aircraft</td></tr><tr><td>Mean accuracy (%)</td><td>Nonhuman Factor cases (%)</td><td>Human Factor cases (%)</td><td>Kappa (%)</td><td>Mean accuracy (%)</td><td>Nonaircraft cases (%)</td><td>Aircraft cases (%)</td><td>Kappa (%)</td></tr><tr><td>NB</td><td>72.9</td><td>63.2</td><td>79.7</td><td>36.3</td><td>80.0</td><td>94.0</td><td>49.5</td><td>47.8</td></tr><tr><td>VFDT</td><td>75.5</td><td>71.6</td><td>77.2</td><td>40.6</td><td>87.1</td><td>90.3</td><td>71.2</td><td>55.6</td></tr><tr><td>OBA</td><td>77.0</td><td>73.7</td><td>78.5</td><td>44.3</td><td>88.5</td><td>90.8</td><td>76.2</td><td>59.2</td></tr></table>

Note: The use of bold font indicates the best results.

Sliding Window Prequential with Size 5000  
![](/api/attachments/N2BAMFE3/fulltext/images/462bb3bf3c6a9322e2e276004b38d68da3197d5b920119597d16786d447c17e3.jpg)  
Figure 9. Prequential Accuracy Rates for the Sliding Window Size of 5,000 in Scenario 4

Sliding Window Kappa Statistic with Size 1000  
![](/api/attachments/N2BAMFE3/fulltext/images/ddf34917408deb95c9feb0bc5cc197395204b34052083b86990f0189ddf3cba2.jpg)  
Figure 10. Prequential Kappa Statistic for the Sliding Window Size of 1,000 in Scenario 3

In addition to being used as input to the classifiers SVDs can also be used directly to gain insight into the distribution of the incidents. With the selected k = 24, incidents were grouped into their appropriate cluster or clusters (an incident’s weights may meet the thresholds for multiple clusters). Because human factors composed the largest share of the incidents, we use that indicator as an example below. We arranged the clusters in descending order of the number of matching incidents. This allows aviation, or other interested parties, to focus on the clusters related to the most incidents. Development of training procedures or finding other solutions to the most commonly occurring clusters (types of incidents) is likely to reduce more potential future incidents than randomly focusing on a cluster regardless of the number of incidents categorized within. Figure 12 shows the percentage of human factor incidents classified in each of the 24 clusters arranged from the cluster with the most incidents (labeled 1) to the cluster with the least number of incidents (labeled 24 on the x-axis). The line shows the cumulative percent of incidents captured by clusters to the point. For instance, the first six clusters account for 39.6 percent of human factor incidents.

Sliding Window Kappa Statistic with Size 5000  
![](/api/attachments/N2BAMFE3/fulltext/images/bab850c88040d0cd707cf07f052cbfdb895eb3afdda3191a4f19ee6397618223.jpg)  
Figure 11. Prequential Kappa Statistic for the Sliding Window Size of 5,000 in Scenario 4

![](/api/attachments/N2BAMFE3/fulltext/images/1d94befdbe1a303f0706d1ffd220c8e768cb1b19e5d74aed7c615b66b4b71b42.jpg)  
Figure 12. Clusters Prioritized by Most Number of Incidents Captured

For illustration purposes, we will look at the terms in the top three clusters (topics) for human factor primary problem incidents (see Table 8). Human Factors were the listed cause of the majority of incidents (more than 61 percent). The first cluster related to human factors has the top five terms of clearance, controller, frequency, tower, and hear (in abbreviation form). As an example of an incident that would fit this cluster, Ryanair B738 landed without clearance on January 6, 2011, at Alicante, Spain [25]. Spain’s Civil Aviation Accident and Incident Investigation Commission released its final report concluding that the cause of the incident was the crew’s failure to request landing clearance. From this incident, safety recommendations were released including a recommendation to enhance the landing checklist to specifically require a landing clearance to be obtained. Aviation experts can focus on recommendations to flight and tower personnel to reduce their likelihood of recurring in the future. Because this cluster had the most incidents, developing processes and procedures to avoid these incidents will have the biggest impact on incident occurrence.

Table 8. Top Terms for Human Factor and Aircraft as Primary Causes of Incidents (Top Three Topics Only)

<table><tr><td>Terms in top three topics</td><td>Matching incidents</td></tr><tr><td colspan="2">Human Factor as primary problem</td></tr><tr><td>1 clrnc (clearance), ctlr (controller), freq (frequency), twr (tower), hear</td><td>20,454 (8.3%)</td></tr><tr><td>2 gear, nose, main, down, lndg (landing)</td><td>16,306 (6.7%)</td></tr><tr><td>3 wx (weather), turb (turbulence), cloud, ice, condition</td><td>16,022 (6.5%)</td></tr><tr><td colspan="2">Aircraft as primary problem</td></tr><tr><td>1 day, hrs (hours), duty, fatigue, schedule</td><td>11,174 (11.8%)</td></tr><tr><td>2 rptr (reporter), callback, callback conversation, reveal, conversation</td><td>10,090 (10.7%)</td></tr><tr><td>3 ft (feet), alt (altitude), altimeter, cabin, msl (mean sea level)</td><td>8,410 (8.9%)</td></tr></table>

The second cluster has terms gear, nose, main, down, and landing. These types of incidents may be similar to the one experienced by Southwest Airlines Flight 345, which went from Nashville International Airport to LaGuardia Airport (New York) on July 22, 2013 [37]. The incident involved the collapse of the Boeing 737 front landing gear while landing, resulting in the injuries of 9 passengers.

The third most common incident cluster had top terms of weather, turbulence, cloud, ice, and condition. Aviation Information Analysis and Sharing (ASIAS) found that weather caused or contributed to many incidents [4]. Humans not responding correctly to the weather conditions made incidents show up as human factor although weather was involved. The report gives a representative incident for McGehee, Arkansas (National Transportation Safety Board Accident Number CHI03LA174). The pilot held a commercial pilot license, and had 1,482 total flight hours and 60 flights in similar make and model aircraft. On July 14, 2003, a Cessna CE–188 sustained substantial damage when it veered off the runway while landing. There was a 5-knot or better tailwind. Probable cause of the incident was the pilot’s failure to maintain directional control of the airplane during landing.

By having incidents clustered and then sorting those clusters by number of incidents contained within, agencies are able to focus their scarce resources on clusters that will provide the most benefit. By developing procedures, training, and/or processes to mitigate future occurrences of the largest clusters, many incidents can be avoided. This translates into reduced risks of important concerns such as injuries, fatalities, equipment damage, and public fears about aviation safety.

Close examination of these clusters can also help explain changes in classification rates. As shown earlier in Figure 2 and earlier in this section accuracy rates are affected by changes in class distribution. This is also supported by changes in cluster/topical weight distribution. Figure 13 shows the change rates of the top three clusters, the first cluster (Cluster 1), the second cluster (Cluster 2) and the third cluster (Cluster 3). Cluster rate is defined as the number of the Cluster included in every 1,000 incidents/1,000. The chart reveals that the rates of the three clusters are changing at similar points. After point 140,000, the rates of the three clusters are very low. The values are almost zero. It suggests that the clusters may have some relationship to the distribution of human factor incidents and classification performance. This ability of a data-stream classifier to monitor classification performance more closely is not available in a batch learning environment and should be another reason for further research into the use of data-streaming or incremental-learning approaches in building classification models.

![](/api/attachments/N2BAMFE3/fulltext/images/bb01fa5c815a00779de5a536008b982b1ac8cb03918390c75ebc60eb067ceb4d.jpg)  
Figure 13. The Top Three Clusters and Class Distribution for Human Factor Incidents

## Conclusion

Incident reporting and investigation are a critical component of any strategy to improve safety in high-risk environments. For incident reporting to effectively influence safety improvement in a timely manner it is critical to understand the causes of reported incidents as soon as possible. The ASRS database has been established to collect data on aviation incidents. Though these incident reports, particularly the textual narratives in the reports, are one of the most important sources of information on the incident causes, efforts to use this resource have been hampered by the extensive resources required to identify the causes manually. In this study we presented an approach to building classification models using textual data as input in a data-streaming environment. The initial data set consists of nearly 170,000 aviation incidents collected by NASA. Topic mining was used to extract the structured information from the textual data. Three different data-stream algorithms were tested to assess their potential in classifying the incidents. The classification results show that topic mining can be used to effectively build incident cause classifiers in incident reporting and management. The results also point to data streaming as an effective way to build and test cause classification models. Finally topic mining not only can convert textual data into useful input to classification models, but the resulting clusters can also be used to provide insights into causes of incidents.

The results in our study demonstrate a potential viable aproach to build classification models using textual data. Our study also demonstrates the potential of data-stream models in classifying these incidents. We conclude that OBA is the best classification algorithm by AUC in batch learning. Furthermore, we use two evaluation measures in the data-stream setting, the Holdout method and the Prequential method. In the Holdout scenario, NB,VFDT, and OBA are similar in accuracy, and kappa values with VFDT are worse than NB and OBA. The Prequential measure can solve the problem, predicting the class label in real time. The accuracy curve from Prequential with window size 1,000 shows that OBA is better than other algorithms. However, the plot with a window size of 1,000 includes many fluctuations. The classification results with a window size of 5,000 show fewer fluctuations in classification accuracy rates. The Prequential accuracy rates with a sliding window size of 5,000 show that OBA has the best performance, much better than the other two algorithms. Kappa statistic charts of Prequential measure with a sliding window size of 1,000 show that OBA has the best performance and is significantly better than the other algorithms. For the unbalanced data stream, the kappa statistic is better at describing the performance of the classification algorithms. An interesting observation is that AUC in batch learning and Prequential kappa measure both reveal that OBA is the best classification model.

From the simulations, we can conclude that the changes in category distribution influence the accuracy rates. NB models are sensitive to these variations. VFDT and OBA have a better performance. When we use data-stream classifiers to predict incident causes, the accuracy rates of testing every incident, distribution of categories and clusters can be seen in a real time. This can help us to gain better insight into the causes of the incidents. As digital data, particularly data in the form of text, become increasingly available, cause identification models using textual data warrant more examination and study. And it is not hard to predict that incident data may be generated in a more continuous stream, thus making data-stream-based algorithms potentially attractive solutions. Given these reasons the results in this study may shed light on better approaches to building classification models to more effectively and accurately identify incident causes in aviation and similar environments, such as medical facilities and hazardous work environments.

Our research makes several contributions. First, the general approach demonstrated in our study points to the feasibility of an automated analysis and identification of risk factors. Such automation may remove an obstacle to efficient and effective safety improvement strategies. Research is needed to examine the translation of incident analysis results into prevention strategies. Second, this article shows how topical mining can be used as a precursor to classification. Topical mining has been successfully used in document clustering in IS research. This study extends that line of research by using extracted features of topical mining in a classification model. As text data become more pervasive, the use of text data alone or in combination with structured data will present both challenges and opportunities in research. The results in this study have shown the feasibility of topical mining as part of a general data-mining model for prediction and classification. Finally, this research evaluates three different data-streaming algorithms and analyzes their results. The ability of a data-stream algorithm to capture concept drift should be particularly attractive in the analysis of large online generated content. Insights from this research can hopefully lead to further research in data streams. As data-streambased algorithms become more refined and robust, we expect to see more research that leverages the unique features of this class of data-mining algorithms in clustering, prediction, and classification involving large volumes of continuous data.

Acknowledgment: This work was supported in part by (1) Anhui Provincial Natural Science Foundation of China (1508085MF114); (2) Technology Foundation for Selected Overseas Chinese Scholar (2014); and (3) Anhui Provincial Science Foundation for Youths (1508085QF137).

## REFERENCES

1. Abedin, M.; Ng, V.; and Khan, L. Cause identification from aviation safety incident reports via weakly supervised semantic lexicon construction. Journal of Artificial Intelligence Research, 38 (2010), 569–631.

2. Albright, R. Taming Text with the SVD. SAS Institute Inc., 2004. Available at ftp://ftp. dataflux.com/techsup/download/EMiner/TamingTextwiththeSVD.pdf (accessed on September 5, 2017)

3. Andrzejczak, C.; Karwowski, W.; and Mikusinski, P. Application of diffusion maps to identify human factors of self-reported anomalies in aviation. Work: A Journal of Prevention, Assessment and Rehabilitation, 41 (2012), 188–197.

4. Aviation Information Analysis and Sharing (ASIAS). Weather-Related Aviation Accident Study, 2010. Available at. www.asias.faa.gov/i/2003-2007weatherrelatedaviationaccidentstudy. pdf (accessed on September 5, 2017).

5. Aviation Safety Reporting System (ASRS), 2017. Available at https://ntrs.nasa.gov/ (accessed on September 5, 2017)

6. Barrientos, F.; Castle, J.; McIntosh, D.; and Srivastava, A. Preliminary Evaluation of an Aviation Safety Thesaurus’ Utility for Enhancing Automated Processing of Incident Reports. 2007. Available at https://ntrs.nasa.gov/search.jsp?R=20070025054 (accessed 11/06/2017).

7. Baskerville, R.; Lyytinen, K.; Sambamurthy, V.; and Straub, D. A response to the design-oriented information systems research memorandum. European Journal of Information Systems, 20, 1 (2011), 11–15.

8. Bifet, A., and Frank, E. Sentiment knowledge discovery in twitter streaming data. In International Conference on Discovery Science. Berlin, Heidelberg, Germany: Springer, 2010, pp. 1–15.

9. Bifet, A.; Holmes, G.; Kirkby, R.; and Pfahringer, B. Moa: Massive online analysis. Journal of Machine Learning Research, 11 (May 2010), 1601–1604.

10. Bifet, A.; de Francisci Morales, G.; Read, J.; Holmes, G.; and Pfahringer, B. Efficient online evaluation of big data stream classifiers. In Proceedings of the 21st ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. Sydney, Australia: ACM, 2015, pp. 59–68.

11. Branford, K. Seeing the big picture of mishaps. Aviation Psychology and Applied Human Factors, 1, 1 (2011), 31–37.

12. Chakraborty, G.; Pagolu, M.; and Garla, S. Text mining and analysis: practical methods, examples, and case studies using SAS. Cary, NC: SAS Institute, 2014.

13. Cohen, J. A coefficient of agreement for nominal scales. Educational and Psychological Measurement, 20, 1 (1960), 37–46.

14. Domingos, P., and Pazzani, M. On the optimality of the simple Bayesian classifier under zero-one loss. Machine Learning, 29, 2–3 (1997), 103–130.

15. Domingos, P., and Hulten, G. Mining high-speed data streams. In Proceedings of the 6th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. Boston, MA: ACM, 2000, pp. 71–80.

16. Emars. Major Accident Reporting System. 2017.

17. Evangelopoulos, N.; Zhang, X.; and Prybutok, V.R. Latent semantic analysis: Five methodological recommendations. European Journal of Information Systems, 21, 1 (2012), 70–86.

18. Evangelopoulos, N. Thematic orientation of the ISJ within a semantic space of IS research. Information Systems Journal, 26, 1 (2016), 39–46.

19. Ghiassi, M.; Zimbra, D.; and Lee, S. Targeted Twitter sentiment analysis for brands using supervised feature engineering and the dynamic architecture for artificial neural networks. Journal of Management Information Systems, 33, 4 (2016), 1034–1058.

20. Goode, N.; Read, G.J.; van Mulken, M.R.; Clacy, A.; and Salmon, P.M. Designing system reforms: Using a systems approach to translate incident analyses into prevention strategies. Frontiers in Psychology, 7 (2016). doi:10.3389/fpsyg.2016.01974

21. Gregor, S., and Hevner, A.R. Positioning and presenting design science research for maximum impact. MIS Quarterly, 37, 2 (2013), 337–355.

22. Haley, D.T.; Thomas, P.; De Roeck, A.; and Petre, M. Tuning an LSA-based assessment system for short answers in the domain of computer science: The elusive optimum dimension. In Proceedings of the 1st International Conference on Latent Semantic Analysis in Technology Enhanced Learning .Heerlen, The Netherlands: Open University of the Netherlands, 2007, pp. 22–23.

23. Hevner, A.R.; March, S.T.; Park, J.; and Ram, S. Design science in information systems research. Management Information Systems Quarterly, 28, 1 (2004), 75–106.

24. Hoeffding, W. Probability inequalities for sums of bounded random variables. Journal of the American Statistical Association, 58, 301 (1963), 13–30.

25. Hradecky, S. Ryanair B738 at Alicante on Jan 6th 2011, landed without clearance Incidents and News in Aviation. Aviation Herald, March 11, 2013. Available at http:// avherald.com/h?article=437de80e&opt=0 (accessed on September 5, 2017)

26. John, G.H., and Langley, P. Estimating continuous distributions in Bayesian classifiers. In Proceedings of the 11th Conference on Uncertainty in Artificial Intelligence. San Francisco, CA: Morgan Kaufmann, 1995, pp. 338–345.

27. Kantardzic, M. Data Mining: Concepts, Models, Methods, and Algorithms. Hoboken, NJ: Wiley, 2011.

28. Kulkarni, S.S.; Apte, U.M.; and Evangelopoulos, N.E. The use of latent semantic analysis in operations management research. Decision Sciences, 45, 5 (2014), 971–994.

29. Landauer, T.K.; McNamara, D.S.; Dennis, S.; and Kintsch, W. Handbook of Latent Semantic Analysis. Hove, UK: Psychology Press, 2013.

30. Leveson, N. A new accident model for engineering safer systems. Safety Science, 42, 4 (2004), 237–270.

31. Li, W.; Chen, H.; and Nunamaker Jr., J.F. Identifying and profiling key sellers in cyber carding community: AZSecure text mining system. Journal of Management Information Systems, 33, 4 (2016), 1059–1086.

32. Love, J., and Hirschheim, R. Reflections on Information Systems Journal’s thematic composition. Information Systems Journal, 26, 1 (2016), 21–38.

33. Martin, D.I., and Berry, M.W. Mathematical foundations behind latent semantic analysis. In T. K. Landauer, D. S. McNamara, S. Dennis, and W. Kintsch (eds.), Handbook of Latent Semantic Analysis, Hove, UK: Psychology Press, 2007, pp. 35–56.

34. National Aeronautics and Space Administration (NASA). ASRS Program Briefing 2015. Available at http://asrs.arc.nasa.gov/docs/ASRS\_ProgamBriefing2015.pdf (accessed on September 5, 2017)

35. Nguyen, H.-L.; Woon, Y.-K.; and Ng, W.-K. A survey on data stream clustering and classification. Knowledge and Information Systems, 45, 3 (2015), 535–569.

36. Nielsen, K.J.; Carstensen, O.; and Rasmussen, K. The prevention of occupational injuries in two industrial plants using an incident reporting scheme. Journal of Safety Research, 37, 5 (2006), 479–486.

37. NTSB. NTSB Identification: DCA13FA131, 2013. Available at https://www.ntsb.gov/\_ layouts/ntsb.aviation/brief.aspx?ev\_id=20130723X13256 (accessed on September 5, 2017)

38. Oza, N.; Castle, J.P.; and Stutz, J. Classification of aeronautics system health and safety documents. IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews), 39, 6 (2009), 670–680.

39. Peffers, K.; Tuunanen, T.; Rothenberger, M.A.; and Chatterjee, S. A design science research methodology for information systems research. Journal of Management Information Systems, 24, 3 (2007), 45–77.

40. Péladeau, N., and Stovall, C. Application of Provalis Research Corp.’s statistical content analysis text mining to airline safety reports. Flight Safety Foundation Web site, 2005. Available at www.flightsafety. org/gain/Provalis\_text\_mining\_report. pdf. (accessed on September 5, 2017)

41. Posse, C.; Matzke, B.; Anderson, C.; Brothers, A.; Matzke, M.; and Ferryman, T. Extracting information from narratives: An application to aviation safety reports. In IEEE 2005 Aerospace Conference. Big Sky, MT: IEEE, 2005, pp. 3678–3690.

42. Rasmussen, J. Risk management in a dynamic society: A modelling problem. Safety Science, 27, 2 (1997), 183–213.

43. Read, J.; Bifet, A.; Holmes, G.; and Pfahringer, B. Scalable and efficient multi-label classification for evolving data streams. Machine Learning, 88, 1–2 (2012), 243–272.

44. Sebastiani, F. Machine learning in automated text categorization. ACM Computing Surveys (CSUR), 34, 1 (2002), 1–47.

45. Shi, D.; Guan, J.; and Zurada, J. Cost-sensitive learning for imbalanced bad debt datasets in healthcare industry. In 2015 Asia-Pacific Conference on Computer Aided System Engineering (APCASE). Quito, Ecuador: IEEE, 2015, pp. 30–35.

46. Sidorova, A.; Evangelopoulos, N.; Valacich, J.S.; and Ramakrishnan, T. Uncovering the intellectual core of the information systems discipline. MIS Quarterly, 32, 3 (2008), 467–482.

47. Straub, D., and Ang, S. Editor’s comments: Rigor and relevance in IS research: Redefining the debate and a call for future research. MIS Quarterly, 35, 1 (2011), iii–xi.

48. Trawinski, B. Evolutionary fuzzy system ensemble approach to model real estate market based on data stream exploration. Journal of Universal Computer Science, 19, 4 (2013), 539–562.

49. Wang, Q. A hybrid sampling SVM approach to imbalanced data classification. Abstract and Applied Analysis, 2014 (2014). Article ID 972786 doi: http://dx.doi.org/10.1155/2014/ 972786

50. Weiss, G.M.; McCarthy, K.; and Zabar, B. Cost-sensitive learning vs. sampling: Which is best for handling unbalanced classes with unequal error costs? In Proceedings of the 2007 International Conference on Data Mining, Las Vegas, NV: DMIN, 2007, pp. 35–41.

51. Witten, I.H., and Frank, E. Data Mining: Practical Machine Learning Tools and Techniques. San Francisco, CA: Morgan Kaufmann, 2005.
