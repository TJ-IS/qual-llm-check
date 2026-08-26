---
otero_id: 16160
otero_key: "9SGD78JB"
title: "Identifying disgruntled employee systems fraud risk through text mining: A simple solution for a multi-billion dollar problem"
authors: "Carolyn Holton"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identifying disgruntled employee systems fraud risk through text mining: A simple solution for a multi-billion dollar problem

Carolyn Holton

Management Information Systems, College of Business and Legal Studies, Southeastern University, 1000 Longfellow Blvd, Lakeland, FL 33801, United States

## a r t i c l e i n f o

Article history: Received 25 January 2007 Received in revised form 7 November 2008 Accepted 13 November 2008 Available online 24 November 2008

Keywords: IS security Occupational fraud Text mining Design science Disgruntled employee Organizational communication

## a b s t r a c t

Occupational fraud is a \$652 billion problem to which disgruntled employees are a major contributor. Much security research addresses reducing fraud opportunity and increasing fraud detection, but detecting motivational factors like employee disgruntlement is less studied. The Sarbanes–Oxley Act requires that companies archive email, creating an untapped resource for deterring fraud. Herein, protocols to identify disgruntled communications are developed. Messages cluster well according to disgruntled content, giving con<sup>fi</sup>dence in the value of email for this task. A highly accurate naïve Bayes model predicts whether messages contain disgruntled communications, providing extremely relevant information not otherwise likely to be revealed in a fraud audit. The model can be incorporated into fraud risk analysis systems to improve their ability to detect and deter fraud.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

The Sarbanes–Oxley Act [36] was created in the wake of a series of prominent <sup>fi</sup>nancial scandals to protect investors from their recurrence. The Act's provisions endeavor to reveal and prevent corporate fraud. Rules issued by the Securities and Exchange Commission (SEC) to enforce the Act are being construed to require all public companies to store every document that in<sup>fl</sup>uences <sup>fi</sup>nancial reporting, including all email messages sent and received, for a number of years [5,28,38,47]. Managing the huge volumes of text employees create every day has been called the biggest challenge for companies seeking Sarbanes–Oxley compliance [34]. Industry-speci<sup>fi</sup>c mandates such as Securities and Exchange Commission rules for brokers and traders, Medicare requirements for healthcare companies, and many other regulations pose their own email retention requirements [45,53].

The Sarbanes Oxley Act's focus is <sup>fi</sup>nancial reporting and certi<sup>fi</sup>cation as a fraud deterrent, or failing that, to enable fraud discovery [9]. Legislative and regulatory requirements to store email, along with techniques for analyzing unstructured text data, create a less obvious path for fraud deterrence and detection: <sup>fi</sup>nding non-<sup>fi</sup>nancial predictors and indicators of fraud risk or actual fraud in employees' email communications.

A national survey reports that 75% of organizations experienced fraud in the three months prior to the study, with employee fraud being the most prevalent [15]. Occupational fraud losses to companies in the United States are estimated to be around \$652 billion per year, equivalent to an average of about 5% of total corporate revenues and a far greater share of pro<sup>fi</sup>t [33]. Globally, the average fraud loss per company in the 2004–2007 period is estimated to be \$8.2 million [25]. Despite attempts to curtail fraud, its incidence continues to grow both at home and abroad [10,17].

## 1.1. Detecting and deterring fraud

Auditors are charged with uncovering and deterring fraud. In the United States, the American Institute of Certi<sup>fi</sup>ed Public Accountants (AICPA) issues Statements on Auditing Standards (SAS) to guide the work of its members. SAS No. 99, Consideration of Fraud in a Financial Statement Audit, was issued in October 2002, partly in response to the same scandals that led to the Sarbanes–Oxley Act. SAS No. 99 makes identifying and investigating fraud risks an integral part of continuous audit processes [32].

The AICPA endorses a fraud risk detection model in accordance with criminology theory that is much like any good crime novel's means, motive and opportunity test. Three conditions commonly accepted as pre-requisites for fraud, opportunity, rationalization, and incentive [2,3], are sometimes referred to as the fraud triangle. By decomposing fraud risk assessment into these factors, the fraud triangle reduces the cognitive effort required for the activity, which may promote accuracy [51].

Much existing academic work on IS security risks addresses how to secure systems through deterrent (e.g. security awareness to promote appropriate safeguarding of passwords or safer use of

Bluetooth devices) and preventive (e.g. physical locks, password access controls) activities to reduce the opportunity for malfeasance using a computer system [14,18], an important component of systems risk [42]. Another major stream of work relates to detection controls [10]. Information security journals have been described as saturated with articles promoting adherence to standards in these areas [41]. The discussion of cognitive factors is largely limited to knowledge and skills of the would-be perpetrator [52]. Components of the rationalization and incentive sides of the fraud triangle are little studied.

Opportunity is also a common focus of fraud auditing software tools [c.f. [1]]. For example, a typical procurement audit tool will analyze purchase orders, order receipts, invoices, payment amounts, quantities, dates, and the like to con<sup>fi</sup>rm that all money going out is accounted for in legitimate transactions corresponding to goods and services received in the amounts received. Duplicate payments, payments exceeding authority levels, or payments generated on weekends might be particular targets of this analysis activity. Audit tools <sup>fl</sup>ag unusual values for investigation, sometimes attaching a risk score to each potential fraud indicator identi<sup>fi</sup>ed.

Auditing packages may also analyze and assign risk scores for non-process data, such as the existence of potentially fraudulent entities. For instance, <sup>fi</sup>ctitious vendors may use post of<sup>fi</sup>ce boxes to receive payments and withhold physical addresses to make it harder to track down people associated with fraudulent transactions. They may not provide telephone numbers or may use answering services exclusively as they have no legitimate operating hours and want to limit links between the <sup>fi</sup>ctitious company and the person or people behind it. They may not provide tax identi<sup>fi</sup>cation numbers, which are dif<sup>fi</sup>cult to fabricate without detection. Each of these signals a potential fraud opportunity, but does not necessarily indicate fraud. A risk assessment score can be assigned to each identi<sup>fi</sup>ed fraud opportunity factor. Typically only entities or items with total risk assessment scores over some threshold trigger investigation.

## 1.2. The case for incorporating disgruntled employee fraud risk indicators

Although a predominant focus of both IS security research literature and fraud audit tools is the opportunity to commit fraud, employee dissatisfaction has been found to be a far more powerful predictor of fraud risk than opportunity [48]. A large study of nearly 5000 employees concluded that employees' deviant behavior, including property deviance like workplace fraud, is a function of conditions inside the organization [22]. This <sup>fi</sup>nding was further narrowed in a study of more than 9000 employees that concluded the more dissatis<sup>fi</sup>ed an employee, the more likely he or she was to commit property deviance [23]. This study thus considers a key factor in the rationalization and incentive components of the fraud triangle: whether an employee is disgruntled with his or her employer (Fig. 1).

At the base of the fraud triangle, incentives motivate fraud. As being disgruntled has a positive relationship with property deviance towards one's employer, causes for that disgruntlement, for instance layoffs, the perception of inadequate compensation, or other dissatisfactions with an employer, serve as fraud incentives. Since the perception of unfair rewards or other dissatis<sup>fi</sup>ers may lead to selfjusti<sup>fi</sup>cation of fraud as taking what's owed, it may also have a role in the rationalization point [17].

Rationalization is the process of aligning an act of fraud with one's personal code of ethics [32]. Prior work has found that age, gender, and the “domain of morality” in operation are relevant to attitudes and behaviors in the context of ethical computer use [16]. The domain of morality is determined by what standards are in operation. These may be personal standards irrelevant to others; social norms, values and attitudes for the domain; or domain-independent standards like justice and fair allocation of resources [39]. Which of these drives behavior is one determinant of the rationalization component of the fraud triangle. Auditors may be more sensitive to opportunity and incentive than to rationalization [51]. They are not trained in discerning morality, and rationalization has been a source of consternation for them since its indicators are often not observable [43]. Automated methods for discovering rationalization thus hold high promise.

Organizations' abundant email archives provide a path for detecting fraud incentives and potential for rationalization. Disgruntled employee emails appear to be common: examples have been made public in lawsuits, managerial advice websites, industry journals, and trade press. Fraud prevention literature cautions that certain employee comments are predictive of criminal action, for instance blaming executives for things that go wrong, displaying excessive anger, and making threats. [31] Consistent with this warning, emails expressing employee disgruntlement are known to have preceded some cases of internal fraud, and studies suggest that prior to committing fraud, extreme disgruntled email messages like those containing threats against superiors may be common [37,40] Fraud investigators have reported that internal fraud is often revealed after the fact through aggrieved employee email [50]. That such email communications occur after fraud, suggests that moving all disgruntled communications to a non-corporate venue or shutting down communications is not typical, and that “venting” does not supplant fraud. Collusion between employees and other parties is cited as contributing to 48% of all cases of fraud [15]. Since collusion requires communication, and fraud involving collusion results in losses nearly <sup>fi</sup>ve times as great as fraud involving a single individual [33], automated ways to <sup>fi</sup>nd email fraud indicators are very promising for reducing fraud losses.

![](/api/attachments/9SGD78JB/fulltext/images/4776810e50e0bfb35db3b9fc6528a4e2b0ebe7496f93f470eda242e23795e7fb.jpg)  
Fig. 1. Fraud triangle employee disgruntlement drivers.

Despite the fact that indicators of employee disgruntlement are likely to exist within a company's email stores, indicators that employees are disgruntled are not typically included in fraud detection systems in use at Big Four accounting <sup>fi</sup>rms or available from vendors. Automatic identi<sup>fi</sup>cation of this risk is a <sup>fi</sup>rst step to equipping such systems for the task in acknowledgement of associated rationalization and incentive for fraud.

To facilitate deterrence and detection of fraud with hard to detect warning signs and indicators, this paper seeks to design an artifact to detect disgruntled employee communications through automated text mining techniques. This new approach adds an important dimension to the array of layered system security strategies, a category most typically employed to limit external threats [54]. The artifact developed extends the layered approach to combat an internal security risk. Data mining is already a well-used component of fraud risk scoring, and use of sophisticated non-rule based techniques seems to be growing. While highly structured text documents have been mined for potential fraud indicators [c.f. [26]], the opportunity to combine the power of text mining unstructured data, such as that in email messages, with other fraud risk assessment and fraud prevention activities appears to be unrealized. This investigation of whether employee disgruntlement, a prime fraud risk indicator, can be detected in email repositories is an initial foray into this domain.

## 2. Research method

Highlights of the design science procedure used to develop, test and assess a disgruntled employee fraud risk assessment module speci<sup>fi</sup>cation are presented in Fig. 2 [21]. The <sup>fi</sup>rst task is to obtain and minimally stage email archives for subsequent analysis. Next, a preliminary assessment of the sample's predictive power is conducted. This step adds rigor by helping to rule out spurious results in later stages of the process. The design science artifact is created in the following step. Existing prediction algorithms from the relevant knowledge base are selected according to their face validity for the task. They are then trained on a sub-set of the data that is labeled as to whether or not it contains employee disgruntlement indicators. The created artifact is next applied to the environment through prediction of class membership – disgruntled or not – on the hold-out sample. Finally, prediction results are assessed to evaluate the designed artifact.

## 2.1. Data sample and staging

Obtaining a data store with an adequate sample of disgruntled employee messages is no easy feat. Disgruntled employees pose a legal threat [4,7], and perceived violations of privacy add to that threat [24]. Protecting against these risks dictates scrubbing certain information from email data prior to its release for text mining, but the scrubbing process may remove some of the predictive information sought for this investigation. While certain automated approaches show promise for this task [6], the business community has yet to be persuaded. To circumvent these problems, data from several Internet discussion groups used for intra-company communications off of the companies' networks was gathered. In some cases, these groups are used predominantly to discuss sensitive matters like salary negotiation strategies, to air grievances, and to exchange career advice. In other cases, the groups are used as intracompany email for manufacturing employees who do not have company email accounts.

Several Vault.com and Yahoo! discussion groups known for intracompany and/or disgruntled employee communications were selected. In these groups, it is common for some employees to identify themselves. Some have even discussed taking matters “of<sup>fl</sup>ine” for further discussion, indicating they know each other's identities. In other cases communications appear to be anonymous. Anonymity is different from the email conditions that are of greatest interest, but this limitation is tolerated in exchange for being able to include extreme and egregious examples of disgruntled employee communications, which might perhaps be the most predictive of fraud behaviors but among the least common in corporate email archives. No prediction differences on the basis of anonymity or non-anonymity were observed.

The order of selected groups was randomly determined before they were sampled. All messages from an arbitrarily chosen start date through 60 days after that date were selected from a particular group before the next group was sampled. This process continued until an initial quota of 40 disgruntled and 40 non-disgruntled intra-company messages was obtained (with 10 more disgruntled messages added later). A second coder independently labeled each sampled message as containing or not containing disgruntled communications. The coders were in complete agreement. Disgruntled communications met one or more of the following inclusion criteria, consistent with literature on sources of employee disgruntlement: Insulting or disparaging terms used to describe superior(s)/leadership or company; superior(s)/leadership blamed for perceived problem(s), or criticized for not acting for the good of the company or for incompetence; recipients encouraged to resist or get revenge on superior(s)/ leadership, or writer's plans for this described; replacement of superior(s)/leadership called for; complaint(s) about working conditions, salary, unfair treatment, and/or other decisions or conditions within the control of superior(s)/leadership issued; wrong(s) done to writer at work described.

The sampled documents were staged in two ways. First, they were separately stored in text <sup>fi</sup>les. Source information was removed to avoid biasing the results, since the discussion on each board selected consists of either predominantly disgruntled or predominantly nondisgruntled messages. Next, the content of each harvested document was embedded as a message in a single .mbx email mailbox <sup>fi</sup>le used for all 80 messages. Mbx is a common non-proprietary electronic mailbox format where messages are concatenated in a single <sup>fi</sup>le, with the beginning of a new message denoted by a “From” line. While there are some variations in implementation, simple text search and replace operations are suf<sup>fi</sup>cient for converting among them. Following creation of the .mbx <sup>fi</sup>le, messages were opened in an email application as an email inbox, and manually <sup>fi</sup>led into disgruntled and nondisgruntled directories to specify their true class for use in predictive model training and assessment.

![](/api/attachments/9SGD78JB/fulltext/images/2fc9c43520dba2c24fbb00c18abd294acd715c82967987672f657992cc01943d.jpg)  
Fig. 2. Procedural overview of research method.

All analysis was conducted within the d2k data mining application using its t2k text mining modules, along with modules from the General Architecture for Text Engineering (GATE). A module is an algorithm or analysis sequence that can typically be customized by setting its parameters and which may accept inputs and provide outputs. The modules can thus interact in a pre-determined sequence to produce sophisticated analytical results. d2k is a commercial data mining package freely licensed for academic use. GATE is open source, available under the GNU library license.

## 2.1.1. Preliminary assessment of predictive power: document clustering

Disgruntled employees are not known to use a great deal of common vocabulary. Their discontent may arise from and be expressed about such diverse topics as not being promoted, being the butt of a joke, receiving an unwanted work assignment, perceiving inequity inworking conditions, experiencing burn-out, and many other sources. The lack of common vocabulary makes detecting disgruntled communications a dif<sup>fi</sup>cult text mining task.

The <sup>fi</sup>rst analysis undertaken is to determine whether clustering, an unsupervised learning technique, can detect differences between documents based on whether a communication gives indications that an employee is disgruntled. Unsupervised learning models a set of inputs without bene<sup>fi</sup>t of class membership labels (e.g. disgruntled or non-disgruntled). A concern with data mining tasks is that patterns identi<sup>fi</sup>ed may be spurious. A <sup>fi</sup>nding that clusters are produced without the assistance of a training set from which attributes may be learned will help establish that the content of the documents may have predictive disgruntled or non-disgruntled classi<sup>fi</sup>cation power [46]. This test replaces power analysis to estimate whether the sample is suf<sup>fi</sup>cient for the task.

For this initial test, two document transformation models were alternately applied to compare their performance: the Brill part of speech tagger [8] and the GATE part of speech tagger based on it [20]. With part of speech tagging, a sentence about “a <sup>fi</sup>re” (noun) should be labeled as to part of speech, or “tagged” differently than one containing “to <sup>fi</sup>re” (verb). The former is likely to be of no interest for this investigation, but the latter could be relevant as a cause of employee disgruntlement.

The Brill tagger <sup>fi</sup>rst uses a lexicon and then context information to assign a part of speech label based on both rules and learned probabilities from a tagged document sample. GATE's tagger is a lexicon and rule-based algorithm that does not rely on probabilities. The GATE tagger assigns up to 48 parts of speech that make up a large sample of manually-tagged Wall Street Journal texts on which it was trained. The GATE part of speech tagging algorithm produced marginally better results, and so was retained.

Following tagging, common words from a pre-de<sup>fi</sup>ned, editable “stop list” are removed from the tagged results. These words, for instance, “a,” “and,” and “the,” provide little or no insight into the nature of the tagged content. Next, the Porter stemming algorithm [30] is applied to remove common suf<sup>fi</sup>xes. For instance, disgruntled becomes disgrunt, and requirement reduces to requir. Stemming allows different forms of a word, such as singular and plural, to be recognized as the same word.

Terms may be excluded according to part of speech for initial reduction of the data set. As the domain is challenging and the sample size manageable, all parts of speech were retained, but a part of speech exclusion module was included in the model for subsequent use with a larger sample.

Next, words that appear in only one document and those exceeding an upper bounds threshold (by appearing in more than a speci<sup>fi</sup>ed percentage of the documents) were removed. These have little value for determining similarity and dissimilarity of documents and their removal can compact the data array to achieve much faster processing while retaining the vast majority of distinguishing content.

A table based on the reduced word list records the frequency of each retained stemmed word in each document. Email metadata, such as the sender, date, and the name of the folder in which an email message was <sup>fi</sup>led (which in this case indicates whether a message is from the disgruntled or non-disgruntled sample) is retained but <sup>fl</sup>agged so that it will not be used as input for further processing unless speci<sup>fi</sup>cally selected.

The term frequency inverse document frequency (TFIDF) algorithm applies greater weight to a term as it increases in frequency within a document, while offsetting its importance according to its frequency across all documents in the set. Using TFIDF, terms of moderate frequency in the entire sample receive the greatest weight as they are expected to have the greatest class predictive power. This algorithm was applied to the stemmed text table.

At this stage of processing, the documents are represented as high dimensional, sparse vectors of terms. High dimensionality refers to the fact that many terms are used across the sample. Sparsity indicates that many of the terms do not appear at all in many of the documents. When clustering text documents represented in this way, the similarity between documents is expected to be low. Since compact clusters are therefore not anticipated, the clustering decision becomes one of desired level of granularity [35]. A hierarchical agglomeration clustering algorithm was selected to produce several levels of granularity. In this method, each document starts in a single cluster. A pair of documents determined by the clustering method and the distance or similarity metric to be more similar than every other pair is joined to form a new cluster at a higher level of aggregation. The process continues until all documents are in a single cluster or until some other stopping rule is satis<sup>fi</sup>ed. All levels of disaggregation can be displayed, allowing selection of an appropriate level of granularity for a particular task.

As the hierarchical agglomeration clustering process can be very time consuming, in the analysis artifact developed and tested herein, only a randomly selected sample of the documents is actually processed through the hierarchical agglomeration modules. The remaining documents are clustered in k-means fashion to the agglomerated clusters produced from the sample based on their distance from the centroids of these clusters. Using this “buckshot” procedure, the hierarchical view sought is produced in far less time, increasing the usefulness and practicality of the developed analysis sequence for large document samples [11].

Ward's clustering method, which minimizes distance from every point in a cluster to its centroid, was found under a variety of clustering parameters to more consistently produce two <sup>fi</sup>rst level groups breaking on disgruntled or non-disgruntled content than other clustering methods tested. A weighted pair group method, in which arithmetic averages between all pairs of observations in two clusters is used for cluster assignment, also performed especially well in this regard. Other methods tested sorted documents into almost pure clusters of disgruntled and not-disgruntled messages at lower levels of aggregation. That multiple clustering methods produced similar results is a strong indicator that natural, meaningful, non-spurious clusters exist within the data.

The cosine similarity function [12], which causes documents of similar composition but different length to be placed together, was more successful than other distance and similarity metrics tested.

![](/api/attachments/9SGD78JB/fulltext/images/559d88e157cf6feb779d1ed866011b78e6bd2cf2b23a62ca6218f931014655dd.jpg)  
Fig. 3. Clustering itinerary overview.

Euclidean distance also performed well, placing most disgruntled messages into a single cluster. As with the clustering methods, that two different distance measures provided similar results also supports the conclusion that disgruntled communications content has predictive power. An overview of the cluster analysis sequence is presented in Fig. 3. The detailed analysis itinerary is provided in Appendix A.

## 2.1.2. Cluster results

A dendogram of the clusters produced and a general characterization of each appears in Fig. 4. While some of the clusters seem imperfectly formed as compared with intuition, and the labels applied are only approximate, that the data breaks clearly into disgruntled and non-disgruntled communications is incontrovertible. It appears that disgruntled messages are further grouped into dissatisfaction with working conditions, and dissatisfaction with leadership. These results provide con<sup>fi</sup>rmation that meaningful distinctions exist between the two groups in the sample obtained, and support the conclusion that the sample holds substantial predictive power.

## 2.2. Predictive document classification

Since the documents are found to form solid clusters on the basis of whether or not they contain disgruntled communications, an indication that reliable structure exists within the text, the next step is to determine whether membership in a disgruntled or nondisgruntled class can be predicted. Developing an analysis sequence that is not sample-bound with parameters but ready for application within disparate organizations is the goal of this analysis phase.

As data cleansing and pre-processing typically add substantial overhead to text mining problems, being able to use an email mailbox in native format without extensive data staging would make this work far more practical. An initial step in the analysis sequence is therefore to transform a stream of emails in native, non-proprietary .mbx format into a table of document terms and document identi<sup>fi</sup>cation numbers where term frequencies populate the row and column intersections. Several inputs to the prediction sequence are possible, but only a single one is required beyond the feeds established in the model instantiation: the name of a directory containing one or more .mbx email <sup>fi</sup>les.

The messages from all mailboxes are parsed and the data processed into a single document, leaving the original mailboxes intact. This characteristic makes use of the analysis itinerary more practical for large organizations. As for the cluster itinerary developed and tested in the last section, the vector space of document terms is then tagged as to part of speech, has non-predictive stop words removed, is stemmed to allow related terms to be recognized, and <sup>fi</sup>nally is weighted to emphasize terms expected to have the most predictive power based on their frequency within and across documents. Email subject lines can be given additional modeling weight during this process. Results were slightly more accurate without extra weight, but the model was relatively insensitive to this factor.

## 2.2.1. Training and testing the prediction model

The resulting table of tagged, stemmed and weighted terms by email document is then used for training and testing text classi<sup>fi</sup>cation algorithms. The source of the message – the disgruntled or nondisgruntled mailbox folder – is selected as the dependent variable, or target class, and all non-meta-data table content is speci<sup>fi</sup>ed for use in the class membership prediction.

The simple, probabilistic, naïve Bayes text model has been shown to be a very good document classi<sup>fi</sup>er under a variety of conditions [13]. With this classi<sup>fi</sup>er, conditional probabilities are used to assign hold-out sample observations to classes of documents whose characteristics are determined from a training sample. The naïve

![](/api/attachments/9SGD78JB/fulltext/images/3f022be11c40bd38c1238478d8c42d844af3a4e13ab5ffb0dc6dbbb3f2ff946e.jpg)  
Fig. 4. Meaningful clusters identi<sup>fi</sup>ed.

![](/api/attachments/9SGD78JB/fulltext/images/aefc8228ad7eda8385f506caaeaf0829014c35f324110357fd211af62d9d10ad.jpg)  
Fig. 5. Email classi<sup>fi</sup>cation analysis overview.

Bayes model was selected to predict membership of each email message into a disgruntled or non-disgruntled class based on its similarity to the samples of disgruntled and non-disgruntled messages in the training set. To apply naïve Bayes prediction, the sparse table is sampled, with some rows randomly selected for training and others for prediction. Naïve Bayes model performance was very slightly improved with logarithmic smoothing, which avoids the problem of assigning probabilities based on small numbers nearly indistinguishable from zero. That model enhancement was retained. An overview of the prediction analysis sequence is presented in Fig. 5. The detailed analysis itinerary is provided in Appendix B.

## 2.2.2. Assessing email classification prediction results

Training sets ranging from 50–90% of the sample were compared for their performance on the remaining holdout sample of 10–50%, each using several different random seeds for sampling. Nondisgruntled messages were almost always all classi<sup>fi</sup>ed correctly. Disgruntled communications were more problematic. In general, the greater the training percentage, the higher the hit rates. With some seeds, perfect prediction was obtained. With others, over half of disgruntled messages were misclassi<sup>fi</sup>ed. This erratic behavior is a function of having too few records available for prediction when a larger training sample is allocated. A single incremental success or failure has a dramatic impact on hit and miss rates in this case. For that reason, the next 10 disgruntled records from the same discussion groups used to gather the original sample were sent to the sample email account and <sup>fi</sup>led into the disgruntled mailbox. With the additional examples, results were strong and relatively stable with an 80/20 training to prediction ratio. Representative results are depicted in Table 1.

## 2.2.3. Investigating the misclassified documents

The two misses re<sup>fl</sup>ected in Table 1 are understandable. The disgruntled message classi<sup>fi</sup>ed as non-disgruntled (see Fig. 6) includes employment issues that are unique within this sample, and uses an insulting term not found elsewhere in the sample. With a larger training sample, this message might have been classi<sup>fi</sup>ed correctly. The author of the non-disgruntled message classi<sup>fi</sup>ed as disgruntled was trying to present positive employment aspects alongside the same negatives discussed in many disgruntled communications. It is unclear that training on a larger sample would have helped.

With total accuracy clearly out of reach, false positives are preferred to false negatives when producing a risk scoring input to a fraud detection system. When a fraud detection system indicates high fraud risk, investigations are triggered that would reveal false positive classi<sup>fi</sup>cation errors. Unfruitful investigations are the price to be paid for avoiding false negatives, which could generate far more in fraud losses than the cost of the otherwise foregone fraud investigations.

## 2.3. Market basket patterns for event specification

Automation of message classi<sup>fi</sup>cation into disgruntled and nondisgruntled baskets is a <sup>fi</sup>rst step towards integrating a disgruntled employee risk score into fraud detection systems. Including this information is expected to elucidate the relationship between the causes and intensity of an employee's disgruntled status and true fraud risk. Let's consider a few hypothetical examples: Perhaps expressed anger over salary more than two months after the last salary increase (a fraud risk event) which is coincident with criticism that superiors are ignorant about what's going on in the company (a second fraud risk event) is a common pattern for embezzlers. Another pattern, such as successive complaints that one's superior is ignorant of the needs of customers and ignores HR policies, might be a stronger predictor of corporate espionage. Other sets of disgruntled communications might be less associated with fraud unless messages are present in much greater volumes. In anticipation of such discoveries, which would allow <sup>fi</sup>ne tuning of an organization's use of the text mining sequences developed herein, an additional investigation was undertaken.

Market basket algorithms associate items or events expected to occur together. Their name is derived from predicting what items might be expected to be purchased at the same time, for instance hamburger patties and buns. The CLOSET [29] and FPGrowth [19] market basket algorithms were applied to the data to seek associations between causes of disgruntlement and expressions of intensity. Once identi<sup>fi</sup>ed, patterns signaling fraud risk events, such as expression of intent to seek retribution for inadequate pay, could have their persons (“boss”), entities (“department”), dissatisfaction objects (“salary”), dissatisfaction expressions (“loathe,” an expression of high intensity), and other attributes tagged. Once entity-object or other patterns are learned, a particular series of tags along with pattern matching characters could be used as search parameters to <sup>fi</sup>nd speci<sup>fi</sup>c fraud risk events of interest in email text. Using this procedure, we could potentially locate messages expressing intent to seek retribution for perceived low compensation, for instance. Disgruntled communication events that prove especially valuable for fraud prediction would be assigned higher fraud risk scores within a fraud detection and deterrence system.

Although this analysis stream remains of interest, no patterns were found with either the CLOSET or FPGrowth algorithms. This might indicate that individual terms are of greater importance than patterns,

Classi<sup>fi</sup>cation results with 20% holdout sample

<table><tr><td colspan="4">Number of randomly selected holdout sample records</td><td>18</td></tr><tr><td>Correct predictions</td><td>16</td><td colspan="2">Percent correct</td><td>89%</td></tr><tr><td>Incorrect predictions</td><td>2</td><td colspan="2">Percent incorrect</td><td>11%</td></tr><tr><td rowspan="6">Actual</td><td colspan="4">Prediction</td></tr><tr><td></td><td>Non-disgruntled</td><td>Disgruntled</td><td>Recall</td></tr><tr><td>Non-disgruntled</td><td>9</td><td>1</td><td>90.0%</td></tr><tr><td>Disgruntled</td><td>1</td><td>7</td><td>87.5%</td></tr><tr><td>Precision</td><td>90.0%</td><td>87.50%</td><td></td></tr><tr><td>Type I error</td><td>10.0%</td><td>12.50%</td><td></td></tr></table>

(a)

Date: Apr 13, 4:06 PM EST Subject: It's bad and getting worse!

Thenumnutsrunning healthcare are running it into the ground. Layoffs have started - you know how - well your utilization is a little low! Thesales guys are selling next to nothing, henceno work for the consultant stiffs. What little is sold is priced so low that nobody can find the margin. What we need is leadership that knows this industry – provider and life sciences – and who know where the opportunities are. Bring Back Spiegel!!!!!!!!!!!!

Date: Feb 17, 5:49 PM EST Subject: Keep the hope alive!

![](/api/attachments/9SGD78JB/fulltext/images/ac2a7bd29f997be2fddf829eafafe82c7305e1dd21d7fdbad4925d1aae26264e.jpg)

I say to those who want to keep hope they get a promotion or raise - go for it!!! Realistically, unless you take action 'hope' alone will not win you the pay raise or the title change...but we need more people with these positive attitudes and not those that constantly look at the negative. I know many have not received a pay raise in a while and this is due to the fact they received 'very large' pay increases during the 'fatty' years and now they are leveling out with the rest of their peers. BUT...still keep hope alive. The grass is NOT greener on the other side, it is merely a different color. [Firm] is a great place to work as long as you 'work it' just like most any other consulting firm...good salaries, fairly flexible schedules (kind to the working mother & student)...could use improvement on education comp and mentoring...but overall I believe it's in your hands to make the best of what ever your situation...(o;

Fig. 6. False negative, a mis-classi<sup>fi</sup>ed disgruntled message (a), and false positive, a mis-classi<sup>fi</sup>ed non-disgruntled message (b) (emphasis added).

but it seems more likely to be a sign that too few messages with any given event type are available in the sample tested.

## 3. Design science contribution

By providing for detection of a dif<sup>fi</sup>cult to observe rationalization piece of the fraud triangle, in addition to automating the heretofore largely manual and post-hoc discovery of a fraud incentive indicator, this work addresses an important and previously unsolved fraud risk assessment challenge with a high degree of accuracy. The prediction itinerary developed enables incorporation of previously unavailable disgruntled employee risk indicators into fraud detection systems, a contribution to the design science knowledge base. The developed artifact is not sample-bound with parameters, and care has been taken to ensure its scalability for large organizations.

## 4. Application in organizations

The AICPA's SAS 99 outlines steps for detecting and deterring fraud [2]. After staff discussions are held to identify potential susceptibilities to fraud, management and auditors are questioned, and fraud risk factors, analytical results and other relevant information are considered to identify and assess risks. Next, the risk assessment is used to determine the appropriate fraud deterrent response, and audit evidence is evaluated and reported. Finally, each of the steps taken is carefully documented. The process is depicted in Fig. 7.

The disgruntled employee communication fraud risk detection and scoring system module designed herein is one of a number of analytical results that would serve as input to fraud risk assessments in step 1. Since a great deal of legislation and regulation now encourages or requires storage or monitoring of email, extensive email stores are newly available for this purpose.

Substantial evidence of employee disgruntlement indicates that one or two of the three conditions for fraud are likely to be present (Fig.1), and may be a precursor to fraud or a signal that fraud is already taking place [31,37,40]. However, that an employee sends a disgruntled message does not mean that employee has committed or will commit fraud, and certainly does not suggest that an employer should take action against the sender on this basis. Rather indications of employee disgruntlement should augment a fraud risk score that includes other fraud risk indicators as well. If high enough, the aggregate score would trigger an internal investigation. If it wished, an organization could also choose to investigate only when the automated process described herein <sup>fi</sup>nds disgruntled communications and some other fraud risk factor or factors. In conjunction with or as an alternative to such an investigation, fraud opportunity may be further restricted, for instance through job rotations or password changes.

Such a system must be implemented judiciously to avoid drawing employee ire as an invasion of privacy or perceived limitation on free speech. While employee communications on corporate networks have almost no privacy protection under the law in the United States [49], respecting employee privacy wishes to the extent that they do not con<sup>fl</sup>ict with a corporate need for fraud deterrence and detection is wise to avoid promoting employee disgruntlement. The systems in which the developed module is deployed should give auditors access to email contents only when a substantial fraud risk is indicated. In other cases, only machines, not people, need examine email content. This is similar to machine reading for spam <sup>fi</sup>ltering in that it provides a valuable service without exposing email content to those not on the distribution list.

![](/api/attachments/9SGD78JB/fulltext/images/cc05508dd724bdbe614bb06e1acd35d0928f823335d0a9b4c893815138a75ec8.jpg)  
Fig. 7. AICPA SAS 99 fraud risk assessment process.

The system module developed is likely to provide information not revealed in the course of staff, management, and auditor discussions by virtue of its comprehensive consideration of tremendous volumes of email communications. It adds to the process substantial consideration of factors outside of the more commonly considered opportunity portion of the fraud triangle.

## 5. Implications and future work

The Director of Research for the University of Tennessee's Corporate Governance Center reports that, “While the <sup>fi</sup>rst two years of SOX compliance were achieved with manual labor for enforcing and testing controls, companies are now looking for ways to mechanize the process” [44]. Although data mining has been applied to auditors' going concern prediction [27], and organizations are making progress on capturing email metadata and extracting content clues like keywords to assist in Sarbanes–Oxley compliance [34], the additional opportunity to identify employees with rationalization and/or incentive to commit fraud by virtue of being disgruntled has not yet been realized. This study develops and successfully tests a text mining instantiation that shows great promise in a new and dif<sup>fi</sup>cult domain where the need for solutions is both signi<sup>fi</sup>cant and urgent.

While the artifact has been tested on only a small sample of messages, several features make it practical for large scale implementation on the voluminous email archives produced by companies. Among these are processing in native mailbox format, limiting data staging, including a part of speech exclusion module to allow further data reduction to speed processing, and allowing the training percentage to be adjusted to produce a training set of reasonable absolute size.

With occupational fraud losses estimated at \$652 billion annually for companies in the United States alone and growing [33], and with many cases preceded by indicators of employee disgruntlement, none of which are known to be routinely automatically detected for fraud risk scoring, the disgruntled employee fraud risk scoring module developed herein could realistically help prevent billions of dollars of fraud each year just in this country. The cost of the additional fraud investigations that may be expected to be triggered by use of the disgruntlement fraud scoring module is easily justi<sup>fi</sup>ed by the savings to be realized from detection and deterrence of cases of fraud. To the extent that the false positive: false negative ratio is found to be wanting, the sensitivity of the analysis and scoring weights can be adjusted to an organization's tastes.

The artifact developed is the <sup>fi</sup>rst iteration of a continuing research process. Results were obtained from an 80–90 document sample. While very encouraging, the work must be repeated on a larger scale. Larger samples will allow more meaningful analysis of disgruntled communication patterns. In particular, historical samples containing emails of employees known to have committed fraud can be mined for associations between particular causes of employee disgruntlement or other aspects of disgruntled employee communications, and the type and severity of associated fraud. We might examine, for instance, if dissatisfaction with working conditions and dissatisfaction with superiors (the two major categories revealed in the clusters presented in Fig. 4) merit different fraud risk treatment. The information obtained could be used to decide by what increment various disgruntled communications should increase a fraud risk score. Such a sample might also allow discovery of additional, as yet unknown, patterns of concern, or suggest that certain types or patterns of disgruntled employee communications are not worthy of incrementing a fraud risk score at all.

While naïve Bayes prediction performance is impressive, future investigations might compare its success to that of other prediction models like neural networks that use self-organized adaptive learning to identify potential problems, and to decision trees.

The techniques described herein may also be applied to instant messaging transcripts, and for assessing other occupational fraud risk factors.

Appendix A. Detailed clustering analysis itinerary

![](/api/attachments/9SGD78JB/fulltext/images/96dae04280551f5e1420b76b8293b51ce44d533ada5c78c93b94da954b0b063e.jpg)

## Appendix B. Detailed prediction analysis itinerary

![](/api/attachments/9SGD78JB/fulltext/images/42b4a2a941d9de78a133fe72e603a87f7b8eda8ddc166f52ecd52738b8be9b6e.jpg)

Appendix C. Legend for analysis itineraries (Appendices A and B)

![](/api/attachments/9SGD78JB/fulltext/images/bd2f81865f2e1698afeb2aff873bc9ea74372d991d4280fe9bc91a0dd892a171.jpg)

Input file name.

![](/api/attachments/9SGD78JB/fulltext/images/b2849a2701b567dd2638e4510814111878aeb1e00f8e3f38c2b9472545e3100b.jpg)

Read file. This module type may return the file contents in a different format than the input file.

![](/api/attachments/9SGD78JB/fulltext/images/5bf212c1b39bd610371e10fb4003eca05e37a481c9e5289d0d6846e050d7919d.jpg)

![](/api/attachments/9SGD78JB/fulltext/images/6157284a85f8d3dba29a7b8719057d0331e206a66b2a9f0e5c0bf15ea06843be.jpg)

t2k (text to knowledge) analysis module. t2k is the name given to text mining components of the d2k (data to knowledge) commercial data mining package (provided without charge for academic use).

GATE (General Architecture for Text Engineering) open source analysis module available under the GNU library license

![](/api/attachments/9SGD78JB/fulltext/images/39399ccc01154ba90130ffafb2f4362893ffb6230ae874aeac497cb7ad414ed6.jpg)

Sets table input and output parameters

![](/api/attachments/9SGD78JB/fulltext/images/0eb0be768106bd7ceeaed39c21b5b0780627a5ff4be69fc0ae3291779d660ebc.jpg)

Displays the contents of a table.

![](/api/attachments/9SGD78JB/fulltext/images/aafea5116ab47cc8430ff96eb9c832e5e764d729fd59fb2ca71b0515c185a1af.jpg)

Creates one or more tables from the provided inputs.

![](/api/attachments/9SGD78JB/fulltext/images/b0b658a13155990a3482c0bf17c035caf120bf288cd9f3d2bf3e3ff12746bc44.jpg)

Provides a visualization of model performance

![](/api/attachments/9SGD78JB/fulltext/images/dd5c813190189a0e7dc939311dd366b8b38e8705a8568f4b7abbb169566802d3.jpg)

Duplicates a given input tomore than one output

Ports reveal whether a module accepts inputs or provides outputs. Ports of the same color are compatible, indicating, for instance, a given output from an upstream module may serve as input to a downstream module.

## References

[1] ACL Data Analysis Software Animated Presentation (Pentana Audit Software, Vancouver, BC, Canada, 2006).

[2] American Institute of Certi<sup>fi</sup>ed Public Accountants, Consideration of Fraud in a Financial Statement Audit — SAS No. 99. 2002

[3] American Institute of Certi<sup>fi</sup>ed Public Accountants, Statement on Auditing Standards. No. 99. Consideration of Fraud In a Financial Statement Audit. 2002

[4] D.W. Arnesen, C.P. Fleenor, M. Blizinsky, Name, rank, and serial number? Th dilemma of reference checks, Business Horizons 41 (4) (1998)

[5] D. Balovich, Sarbanes–Oxley Document Retention and Best Practices, Creditworthy News, 2007.

[6] S. Bapna, A. Gangopadhyay, A wavelet-based approach to preserve privacy for classi<sup>fi</sup>cation mining, Decision Sciences 37 (4) (2006).

[7] T. Brady, Employee handbooks: contracts or empty promises? Management Review 82 (6) (1993).

[8] E. Brill, Some advances in transformation-based part of speech tagging, Presented at Twelth National Conference on Arti<sup>fi</sup>cial Intelligence, Cambridge, MA, 1994.

[9] G.W. Bush, The White House, Statement by the President, 2002.

[10] H. Cavusoglu, B. Mishra, S. Raghunathan, The value of intrusion detection systems in information technology security architecture, Information Systems Research 16 (1) (2005).

[11] D.R. Cutting, J.O. Pedersen, D. Karger, J.W. Tukey, Scatter/gather: a cluster-based approach to browsing large document collections, Presented at 15th Annual ACM-SIGIR, 1992.

[12] I.S. Dhillon, D.S. Modha, Concept decompositions for large sparse text data using clustering, Machine Learning 42 (1) (2001).

[13] P. Domingos, M. Pazzani, Beyond independence: conditions for the optimality of the simple Bayesian classi<sup>fi</sup>er, Presented at 13th International Conference on Machine Learning, Bari, Italy, 1996

[14] E. Fernandez-Medina, J. Trujillo, R. Villarroel, M. Piattini, Access control and audit model for the multidimensional modeling of data warehouses, Decision Support Systems 42 (3) (2006).

[15] Fraud Survey (KPMG Forensic, 2003).

[16] U.E. Gattiker, H. Kelley, Morality and computers: attitudes and differences in judgments, Information Systems Research 10 (3) (1999).

[17] Global Economic Crime Survey (PricewaterhouseCoopers, New York, 2005).

[18] M. Gupta, J. Rees, A. Chaturvedi, J. Chi, Matching information security vulnerabilities to organizational security pro<sup>fi</sup>les: a genetic algorithm approach, Decision Support Systems 41 (3) (2006).

[19] J. Han, J. Pei, Y. Yin, Mining frequent patterns without candidate generation, presented at ACM-SIGMOD International Conference on Management of Data, Dallas, TX, 2000.

[20] M. Hepple, Independence and commitment: assumptions for rapid training and execution of rule-based POS taggers, Presented at 28th annual meeting of the association for computational linguistics, Hong Kong, 2000.

[21] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004).

[22] R. Hollinger, J. Clark, Employee deviance: a response to the perceived quality of the work experience, Work And Occupations 9 (1) (1982).

[23] R.C. Hollinger, J.P. Clark, Deterrence in the workplace: perceived certainty, perceived severity, and employee theft, Social Forces 62 (2) (1983).

[24] D.L. Jacobs, Are you guilty of electronic trespassing? Management Review 83 (4) (1994).

[25] Kroll Inc., Economist Intelligence Unit Overview in the Kroll Global Fraud Report (2008).

[26] H. Mailvaganam, Text Mining for Fraud Detection: Creating Cost Effective Data Mining Solutions for Fraud Analysis in Data Warehousing Review 2004 DWReview Vancouver BC

[27] D. Martens, L. Bruynseels, B. Baesens, M. Willekens, J. Vanthienen, Predicting going concern opinion with data mining, Decision Support Systems 45 (4) (2008).

[28] J.C. Montana, J.E. Dietel, C.S. Marrins, Strategies for RIM program compliance with Sarbanes–Oxley, The Information Management Journal 40 (6) (2006) 6.

[29] J. Pei, J. Han, R. Mao, CLOSET: an ef<sup>fi</sup>cient algorithm for mining frequent closed itemsets, presented at ACM-SIGMOD Workshop on Research Issues in Data Mining and Knowledge Discovery, 2000.

[30] M.F. Porter, An algorithm for suf<sup>fi</sup>x stripping, Program 14 (3) (1980)

[31] Preventing crime and violence in the workplace in workplace health, safety and security (AllBusiness.com, Undated).

[32] M. Ramos, Auditors' Responsibility for Fraud Detection, Journal of Accountancy 195 (2003).

[33] Report to the nation on occupational fraud and abuse (Association of Certi<sup>fi</sup>ed Fraud Examiners, Austin, TX, 2006).

[34] C. Rhinehart, Email management and Sarbanes–Oxley Compliance in Sarbanes– Oxley Compliance Journal, 2005.

[35] M.E.S.M. Rodrigues, L. Sacks, A scalable hierarchical fuzzy clustering algorithm for text mining, presented at 4th International Conference on Recent Advances in Soft Computing, Nottingham, UK, 2004.

[36] Sarbanes–Oxley Act, H.R. 3763, PL 107–204, 116 Stat 745, 107th Congress (2002)

[37] E.E. Schultz, A framework for understanding and predicting insider attacks, Computers and Security 21 (2002).

[38] E. Schwartz, Rethinking message storage: Sarbanes–Oxley demands better archiving and retrieval of electronic communications, InfoWorld 26 (24) 14–14 (1p).

[39] R.A. Schweder, M. Mahapatra, J.G. Miller, Culture and moral development, in: J. Kagan, S. Lamb (Eds.), The Emergence of Morality in Young Children, University of Chicago Press, Chicago, 1987.

[40] E.D. Shaw, The role of behavioral research and pro<sup>fi</sup>ling in malicious cyber insider investigations, Digital Investigation 3 (1) (2006)

[41] M. Siponen, Information security management standards: problems and solutions, presented at 7th Paci<sup>fi</sup>c Asia Conference on Information Systems, Adelaide, South Australia, 2003.

[42] D.W. Straub, R.J. Welke, Coping with systems risk: security planning modules for management decision making, MIS Quarterly 22 (4) (1998).

[43] The American Institute of Certi<sup>fi</sup>ed Public Accountants, Inc., Appendix to SAS No. 99, Fraud Risk Factors, 2002.

[44] The 2006 Oversight Systems Financial Executive Report on Sarbanes–Oxley (Oversight Systems, Inc., Atlanta, Georgia, 2006).

[45] B. Tolson, Email Retention Policy: A Step-by-Step Approach in Backup and Disaster Recovery, 2006 TechTarget.

[46] M. Tremblay, D. Berndt, P. Foulis, S. Luther, Utilizing text mining techniques to identify fall related injuries, Presented at Eleventh Americas Conference on Information Systems, Omaha, NE, 2005.

[47] E. Varon, Mandate from SEC regulators: save your electronic documents, CIO Magazine 16 (2003)

[48] J.T. Wells, Why employees commit fraud, Journal of Accountancy 191 (2) (2001).

[49] T.M. Wesche, Reading your every keystroke: protecting employee e-mail privacy, Journal of High Technology Law 1 (1) (2002).

[50] E. Wilding, J. Parker, Corporate computer fraud — straight from the secret investigators, Computer Fraud & Security 2002 (7) (2002).

[51] J. Wilks, M. Zimbelman, Decomposition of fraud risk assessments and auditors sensitivity to fraud cues, Contemporary Accounting Research 21 (3) (2004).

[52] R. Willison, Understanding the offender/environment dynamic for computer crimes: assessing the feasibility of applying criminological theory to the IS security context, presented at Proceedings of the 37th Hawaii International Conference on System Sciences, 2004.

[53] B. Worthen, Message therapy: federal regulations require an entirely new approach to storing and searching e-mails. Noncompliance is not an option, CIO Magazine 18 (7) (2005).

[54] W.T. Yue, M. ÇakanyIldIrIm, Y.U. Ryu, D. Liu, Network externalities, layered protection and IT security risk management, Decision Support Systems 44 (1) (2007).

![](/api/attachments/9SGD78JB/fulltext/images/0e20f2bd446c624c7b10fd72f27c9a83bdf3cb9a9ac46a04c54a0a1f1ec0f273.jpg)  
Carolyn F. Holton is an associate professor of management information systems in the College of Business and Legal Studies at Southeastern University, Lakeland, FL. Computermediated communications systems are her main research focus, particularly the impacts of system monitoring and user culture, group development, rumor promulgation and response strategies, fraud deterrence and detection, and pedagogical applications.
