---
otero_id: 19640
otero_key: "VESWP77B"
title: "Automated mortgage origination delay detection from textual conversations"
authors: "Arin Brahma; David M. Goldberg; Nohel Zaman; Mariano Aloiso"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113433"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Automated mortgage origination delay detection from textual conversations

![](/api/attachments/VESWP77B/fulltext/images/177ab5d8585a4b6bca8b6a1218ff22c2f3cb694152bffbf41d4caef3e391d1c5.jpg)

Arin Brahma <sup>a</sup>, David M. Goldberg <sup>b,\*</sup>, Nohel Zaman <sup>a</sup>, Mariano Aloiso

<sup>a</sup> Loyola Marymount University, 1 LMU Drive, Los Angeles, CA 90045, United States of America

<sup>b</sup> San Diego State University, 5500 Campanile Drive, San Diego, CA 92182, United States of America

## A R T I C L E I N F O

Keywords: Mortgages Loan origination Condition clearing Text analytics Machine learning Predictive analysis

## A B S T R A C T

For modern mortgage firms, the process of setting up and verifying a new loan, known as origination, is complex and multifaceted. The literature notes that this process is rife with delays that can stunt the firm’s business opportunities, but no modern analytical techniques have been developed to address the problem. In this paper, we suggest the use of text analytic and machine learning techniques to predict likely delays. In collaboration with a large national mortgage firm, we derive a large dataset of transcripts from employees’ communications per taining to potential loans. We first use information retrieval to generate an initial list of “seed terms,” or terms most associated with loans that were delayed. We then use an array of machine learning approaches to generate predictive models based upon these seed terms. We find that these approaches are comparable in performance to less interpretable state-of-the-art approaches utilizing word embeddings. The resultant models offer interpretable and high-performing solutions to mitigate the risk of delays through early risk detection.

## 1. Introduction

The processing involved in fully initiating and funding a new mort gage loan is known as loan origination. In 2018, over 7 billion mortgage loans whose value totaled over \$1.8 trillion were originated in the United States [22], making it one of the largest mortgage markets in the world and a significant portion of the American economy. In the origi nation process, closing time, or the amount of time required to complete the processing of the loan, is absolutely critical, and many lenders are pursuing process improvements and automation with the goal of reducing the closing time [9]. In recent years, closing times in the mortgage industry have improved slightly due to technological auto mation and document digitization. Despite this, closing times are still lengthy, and borrowers are often frustrated by the length of time required to complete the process [27].

As a part of financial services industry, mortgage loan-related pro cesses are lengthy, complex, time-sensitive, and involve interactions with many external entities, resulting in numerous decisioning points throughout the cycle. Funding delays, even when small in magnitude, can be critically detrimental to mortgage lenders’ businesses. This is because delays not only upset the borrower and all the external third parties taking part in the coordinated funding event, but a historical pattern of funding delays discourages brokers to bring new clients (borrowers) to the mortgage lender, leading to shrinking business pipeline over time. A recent industry white paper by Oracle Financial Services [27] states that:

“In today’s digital age of banking, customers are not easy to please. They expect an experience that is simply ‘frictionless’ throughout their banking journey. Customers also demand quick responses and faster turnaround times. … Origination and On-boarding is the first customer touch point; by offering the right product and simplifying the origination process, banks have the opportunity to demonstrate a comprehensive understanding of the customer’s unique individual needs, exceed their expectations and deliver a ‘wow’ moment.”

As the origination process is so fundamental to mortgage firms, any improvement in handling this process represents a remarkable oppor tunity to differentiate from the competition [8]. Even with the current level of digitization and technological automations, the industry average time for loan closing is in the range of 45 to 60 days [9]. Based on the analysis of about 48,000 loans in our dataset, we find that average time to close loans for one major firm has been 31 days, with 25% of the loans closing between 37 and 59 days. The data on closing delays are even more revealing. As found in our dataset, about 60% of the loans closed later than the target closing date as set by the lender in the beginning of the process. The average loan closing delay was 8 days, and 25% of the delayed loans closed with a delay between 12 and 22 days.

Contemporary mortgage firms are tasked with collecting numerous documents pertaining to each new origination, and many use modern software packages such as Calyx Point or Encompass to organize these processes. Communications pertaining to specific loans are often stored in databases as unified conversation threads that allow employees and external entities to collaborate and close loans. Thus, in this work, we utilize threads of such textual communications to predict whether associated originations are likely to be delayed. We use a novel meth odology to first generate “seed terms,” or specific words and phrases predictive of delays [1,3,25]. In turn, these words allow managers to quickly diagnose the causes of a potential delay. We then use contem porary machine learning techniques to construct high-performing pre dictive models. We show that values around 0.90 are feasible for each of accuracy, precision, recall, F1-score, and AUC. Using our techniques, managers can quickly prioritize the loans of greatest concern and effectively mitigate potential problems at an early stage.

## 2. Literature review

Literature from recent years indicates that researchers have been exploring and applying various machine learning techniques, including text analytics, to solve a range of issues in the financial and banking industries, such as bank failure, loan defaults, distress events, and se curity threats. The techniques involve building descriptive and predic tive models targeting specific problems using transactional data as well as textual data internal or external to organizations. However, research to address mortgage loan origination delays by identifying and flagging delay prone loans is not found in the literature and represents a major opportunity for process improvement in the mortgage industry. In this paper, the authors use text analytics combined with machine learning techniques to address this gap and suggest directions for future work.

In the following, we review the literature on several key areas. First, we examine the literature on mortgage loan processing with particular emphasis on loan origination. Second, we examine the literature on applications of various types of text analytics in the banking and financial services industry and highlight their success and drawbacks in addressing different types of challenges. Finally, we provide a rationale for our text analytics approach in predicting loan delays from internal textual communications of a mortgage firm and address the guiding research question and contributions of our work.

## 2.1. The mortgage industry and loan processing

Business processes in the mortgage industry in the United States are comprised of three distinct functional areas: (1) loan origination, (2) secondary marketing, and (3) servicing [6]. The loan origination func tional area deals with receiving borrowers’ loan applications, qualifying the applications for possible funding, condition resolution, underwriting and loan decisioning, closing document preparation, and funding. Closed loans are treated as financial assets as they earn interest over a long period of time. Individual loans are then pooled together and sold to the investment bankers in the second functional area called secondary marketing. On the other hand, the servicing function deals with inter action with the funded borrowers to collect monthly payments, provide loan related customer service, and deal with defaults, foreclosures, etc. Hess and Kemerer [29] provided an overview of the loan origination and secondary marketing functions and their interactions. In this work, we will delve into describing the loan origination function with a focus on the condition resolution process in more detail as illustrated in the Fig. 1 below.

The condition resolution process is closely intertwined with the un derwriting and loan decisioning process, which is a critical process responsible for risk assessment and decisioning [21]. It is in the firm’s interest to ensure that a loan’s risk is minimal and is balanced by its financial upside. Thus, loan underwriters not only calculate the risk scores of the borrowers with respect to specific loan products, but they also review the supporting documents for sufficiency, completeness, and accuracy [52]. For example, prospective borrowers may be asked to submit documentation demonstrating proof of income. When a short coming in the documentation is detected, a “condition” is created. Ex amples of conditions could be “proof of income document missing,” “property appraisal document inconsistent with the property detail in the application,” “employment verification still pending,” “tax return missing for the year 2018,” etc. Each unique condition is assigned a condition code and tracked until the issue is resolved.

A condition resolution team works on these conditions and com municates with the borrower, broker, loan officer, and various thirdparty service providers to facilitate correction of the current docu ments or collect missing documents [31]. Once such documentation deficiencies are resolved by the condition resolution team, the un derwriters review the loan again and decide to either approve the loan for funding (“clear to close”) or seek additional documentations or document corrections for the condition to be cleared. If a “clear to close” status is indicated by the underwriters, then loans move to the “final loan document preparation” stage and subsequently to closing and funding. The communications involving the underwriters, condition resolution team, borrowers, brokers, loan officers, and third-party ser vice providers are predominantly electronic and captured in the loan processing system as “textual content.” It may be noted by the readers from Fig. 1 that the “condition resolution” process is fundamentally iterative, subject to unforeseen delays and uncertainties, and conse quently this stage is a prime contributor to loan funding delays.

## 2.2. Text and sentiment analyses

With the growth of electronic communication, text analytics has proved a widespread and useful tool of mining meaning from websites, such as social media sites [55] and online review platforms [25]. As a result, text analytics is a fast-growing field that aims to detect meaning from these growing bodies of textual information. Text analytics in cludes various strategies, techniques, and algorithms that use textual information or communications as raw data and transform them into actionable intelligence in an automated fashion. Some techniques are effective in the context of only narrow sets of problems, while other techniques are designed with a more general purpose. Studies have used

![](/api/attachments/VESWP77B/fulltext/images/dc3b504199b6070e3aeb2ed6e47c1f079e216f0884caf4d31ca239268fe6d312.jpg)  
\* Focus of this research paper

Fig. 1. Condition resolution process as a part of the loan original function.

text to investigate the potential causes of bank failures, including undercapitalization, liquidity, safety and fraud [15,28,41,50]. Addi tionally, Chugani, Govinda and Ramasubbareddy [16] and Kvamme, Sellereite, Aas and Sjursen [36] detected similar patterns of textual complaints of consumer loans and predicted mortgage defaults from consumer transaction data across several banks by using data mining techniques such as cluster analyses and neural networks. Furthermore, text analytics has also been applied to credit scoring with the hope of assessing borrower risk [39]. For example, Li, Liu and Huang [38] use text analytics of financial news to analyze market-level credit risk. In addition, Wang, Jiang, Zhao and Ding [53] use text derived from a peerto-peer lending site to predict borrower-level credit risk.

Sentiment analysis applies methods from natural language process ing to automatically detect the emotive valence or polarity of authors attitudes toward a topic: positive, negative, or neutral [4]. For example, positive and negative terms may be kept in a word list [42] such that each word is associated with sentiment strength within some range, such as − 5 to +5 to reflect very negative to very positive emotive content. Then, this dictionary can be applied to unseen text to assess its sentiment based on lessons learned from previously examined text. A substantial advantage of sentiment analysis is that it is a generalizable tool that can be rapidly deployed for a wide range of domains. For example, the OpinionFinder system uses lexicons to determine the polarity orienta tion of a given query, topic, subject, or target.

Even though sentiment analysis is used extensively for text analytics, several researchers have highlighted the limitations of some sentimentbased techniques [1,25]. Sentiment dictionaries often fail to extract crucial context associated with the overall meaning of text. For example, a sentiment analytic tool might correctly identify that a document was generally positive, but it would not necessarily identify the specific topic about which the author felt positively. Second, sentiment dictionaries may fail to detect sarcasm, humor, and other issues that may mislead a dictionary-based approach. For instance, sentiment dictionaries could identify the phrase “called the phone number. Rang 13 times... awesome under an emergency situation” as positive because of the word “awesome,” but a human reader would likely identify that the phrase indicates sarcastic dissatisfaction. A potential remedy is the use of rule based sentiment analyses [30,49], which incorporate additional logic or machine-learned insights in addition to dictionaries. For instance, one common feature of these approaches is negation detection, in which the phrase “not horrible” would be understood to be very different from “horrible.”

A series of text analytic studies has examined the utilization of su pervised or semi-supervised methods for text classification, using in formation retrieval techniques to develop machine-learned “seed terms,” sometimes also referred to as “smoke terms” [1,3,23,25,40]. The purpose of these techniques is to generate a list of words and phrases that are strongly associated with some target class. For instance, Abra hams, Fan, Wang, Zhang and Jiao [1] sought to use these terms to identify online reviews that referred to defective products, enabling firms to remediate and improve product safety. As opposed to a general tool such a sentiment analysis, seed terms are instead more narrowly focused on a specific problem of interest. In this work, we seek to adapt elements of this paradigm for application to mortgage loan processing. Table 1 shows a survey of text classification methods used in prior works in the mortgage and banking industries. While this industry has been a fertile area for new research efforts, our study is the first to our knowledge to propose the use of text analytic or machine learning methods for prediction of mortgage loan origination delays.

## 2.3. Research questions and contributions

In this paper, we address two major research questions. First, we ask: to what extent can text analytic and machine learning techniques be used to predict risk of delays in mortgage loan condition resolution, and how does performance vary across techniques? The process of loan condition resolution is complex and involves the interaction between many different parties both inside and outside the mortgage firm. Delays in this process can substantially negatively affect a mortgage firm’s operations. Hence, early detection and managerial prevention are invaluable. Thus far, the academic literature has not attempted to use text analytics in addressing this problem. This represents an enormous untapped opportunity to utilize cutting-edge technology to address such a costly real-world business problem. Addressing this research question provides a practical contribution: if any one of these text analytic and machine learning approaches is effective, then the mortgage industry will gain a useful set of tools for rapidly analyzing textual communica tions related to delays in loan approval. For practitioners, these results would provide a rapid and automated means to predict costly delays before they occur. For text analytics researchers, these results would suggest a new approach to performing predictive analytics on real-time conversational data (transcripts). While data analytic techniques have been used in a few instances in the mortgage industry [8,41], this application is novel, addressing a critical gap in the literature and laying the groundwork for future research and solution development.

Table 1  
Survey of text classification methodology in mortgage and banking industries.

<table><tr><td>Study</td><td>Dataset</td><td>Methodology</td><td>Target class</td></tr><tr><td>Chen, Rabbani, Gupta and Zaki [15]</td><td>Over 100,000 documents across 8-K and 10-K SEC filings</td><td>LDA, Principal Component Analysis (PCA), K-Competitive Autoencoder (KATE)</td><td>Bank failure</td></tr><tr><td>Kvamme, Sellereite, Aas and Sjursen [36]</td><td>Transaction data from over 20,000 customers</td><td>Neural networks, random forests</td><td>Mortgage loan default</td></tr><tr><td>Netzer, Lemaire and Herzenstein [41]</td><td>Online crowdfunding microloan requests from over 120,000 potential borrowers</td><td>Naïve Bayes, logistic regression, L1 regularization, LDA</td><td>Microloan default</td></tr><tr><td>Rönnqvist and Sarlin [46]</td><td>Reuters online archive of 262,000 news articles</td><td>Deep neural network (feed-forward topology)</td><td>Bank distress events</td></tr><tr><td>Viviani and Hanh [50]</td><td>98 bank failure reports from FDIC-OIG</td><td>LDA, hierarchical clustering, k-means clustering</td><td>Governance and risk</td></tr><tr><td>Wei, Li, Zhu and Li [54]</td><td>Over 59,000 financial risk disclosure documents</td><td>Vector space model</td><td>Bank distress events</td></tr><tr><td>Our study</td><td>Over 48,000 loan threads from a major mortgage firm</td><td>Seed terms, LASSO, BERT</td><td>Mortgage loan origination delay</td></tr></table>

Second, we ask: to what extent can our text analytic techniques be reconciled to create an interpretable managerial tool for prioritization of loan conditions? “Interpretable AI” has been a major topic in the aca demic literature in recent years [33,44,47], as the performance of machine-learned techniques has improved, while the interpretability of results by practitioners has been often lacking. In our work, we attempt to package our text analytic insights into an interpretable tool by emphasizing the specific words and phrases (seed terms) that cause a loan to be flagged as a likely delay, informing decision-making. Many modern machine learning solutions are “black boxes” whose results are not easily interpretable, and the lack of interpretability poses an addi tional barrier to adoption [48]. Indicating the specific words and phrases that led to a classification has great potential to convince otherwise skeptical managers of the insights that the technologies provide. For researchers, our approach serves as a framework for how text analytics work can align text-based insights to be interpretable and convincing to practitioners.

## 3. Methodology

In this research, we collaborated with a large mortgage firm based in the United States with annual origination volume exceeding \$1 billion USD. The firm has national presence, and its annual origination volume ranks in the top 5% of United States mortgage firms based on records maintained by the Federal Financial Institutions Examination Council (FFIEC) [17]. The firm provided us with internal transcripts pertaining to mortgage loan origination for loans whose deadlines were in the twoyear period spanning from January 2018 through December 2019. These records focused on the condition resolution stage of the origina tion process, which is the stage most prone to delays and consequently the likeliest to delay the entire loan. This initial dataset consisted of 48,069 records, of which 26.5% pertained to delayed conditions, and the remaining 73.5% pertained to on-time conditions. To avoid biasing subsequent machine learning models given the class imbalance, we use a combination of the Synthetic Minority Oversampling Technique (SMOTE) and Tomek links as suggested by Batista, Bazzan and Monard [5]. This approach uses a combination of oversampling and under sampling to derive a balanced dataset that reflects the distributional characteristics of the original dataset [37]. We show an example record (delay) below in which a senior underwriter is asked to examine a po tential borrower’s credit report due to concerns over a high number of credit inquiries. As the example demonstrates, it is not necessarily obvious for the reader whether a delay is likely.

>> > Sr. UW to run a soft pull before release of docs for Borrowers. Since high number of inquires have been reported on credit report, need to validate that no new debt has been incurred between loan approval and closing.

$> > \ > \ S r . \ U W$ to review the soft pull credit report and condition accordingly (if required). Note: No action is required from client.

We show a visual overview of our methodology in Fig. 2. As our goal in this research is to develop a predictive mechanism to identify likely delays before they occur, we removed any comments within each transcript that occurred after a condition had already been delayed. We concatenated together all remaining comments within each transcript, creating one unified document for each record. Before moving forward to text processing, we performed basic text cleaning to improve the quality of our data, including standardizing capitalization, removing extraneous whitespace, and removing special characters.

The next stage of our analysis was to create a feature set from our textual data. We do so by generating “seed terms,” or specific words and phrases that occur frequently in documents pertaining to delayed con ditions and infrequently in documents pertaining to on-time conditions. These terms are likely to be predictive of delays, and as such there is reason to believe that they will be valuable features. This technique has been used in past literature for similar applications, such as parsing large volumes of textual data for indications of product defects [1,3]. These seed terms are then used in conjunction with machine learning tech niques to predict the existence of delays in unseen records. We divided our dataset into five equal segments for k-fold cross-validation, in which a machine learning model is trained on all but one segment, and the held-out segment is used for testing [18]. Ultimately, we structured our approach such that a total of 80% of the data was used for training purposes; 10% was used for tuning machine learning models; and 10% was used for testing. We ultimately report an average of the performance across each iteration.

Prior research has used a variety of information retrieval approaches for determining effective seed terms [1–3,25]. Several recent works [25,26,40,56] have utilized the Correlation Coefficient (CC score) al gorithm [24] extensively given its superior performance. Below, we present a contingency table (Table 2) displaying the input parameters for this technique. The CC score algorithm is used to obtain a relevance score for each term in a corpus, where higher scores indicate greater relevance. In our study, we ran this algorithm on unigrams (single words), bigrams (two-word phrases), and trigrams (three-word phrases). Unigrams are most likely to occur in many documents, but they are less specific. On the other side of the continuum, trigrams are likely to occur in the fewest documents, but they are more specific. We consider this range of possible terms in our research to ensure the robustness of our model.

Based upon the contingency table, each term is assigned a weight in (1):

$$
\text { Relev } = \frac {\sqrt {N} \times (A D - C B)}{\sqrt {(A + B) \times (C + D)}}\tag{1}
$$

This technique results in relevance scores for each term in such that higher relevance scores suggest terms that may be predictive of delays, as they appear frequently in delay-related documents and infrequently otherwise. To avoid overfitting, we chose the top 50 unigrams, top 50 bigrams, and top 50 trigrams based on their relevance scores as our seed terms. The presence (or absence) of each seed term serves as a feature for our machine learning models.

In addition to the textual features previously discussed, we also include four key borrower and loan characteristics in our modeling as follows:

• Credit (FICO) scores. FICO is a credit score model that estimates a borrower’s credit risk on a scale of 300 (high risk) to 850 (low risk). The scores may be used to evaluate a borrower’s credit history and evaluate the level of risk in offering them a loan. We expect that lower scores will be associated with greater scrutiny [12].

• Borrower debt. A borrower’s existing monthly debt obligations (for example, due to another mortgage, a car loan, educational loans, etc.) could indicate their ability to pay back a loan. Borrowers with great existing debt could be under greater financial strain, and thus they could be more likely to default on new loans [14]. This could also lead to greater scrutiny and increase the likelihood of delays.

• Loan type. Three loan types were considered: conventional, Federal Housing Administration (FHA), and Veterans Affairs (VA) (each was coded as a dummy variable). Depending on a borrower’s back ground, they may qualify for loans backed by certain federal agencies as opposed to conventional loans. This backing may reduce some risk on the part of the lender, although on the other hand it could also generate additional paperwork and verifications [43].

• Loan amount. Larger loans suggest greater risk on the part of lenders, although smaller loans are easier for borrowers to repay.

The final features that we incorporated in our machine learning models were sentiment analysis scores. On the assumption that negative sentiment would be likely associated with loan conditions that would be delayed, we incorporated two common sentiment techniques in our modeling: AFINN [42] and Harvard General Inquirer [32].

Using these features, we trained cross-validated machine learning models to predict the existence of delays. For robustness, we chose a variety of supervised machine learning models including logistic regression, elastic nets, k-nearest neighbors, decision trees, random forests, gradient boosting, naïve Bayes, support vector machines, neural networks, and AdaBoost. While we will not detail the inner workings of each of the machine learning techniques here, we direct the reader to Bonaccorso [10] and Delen and Zolbanin [18] for general background on each of these approaches. In this work, each supervised machine learning model was implemented in Python using the scikit-learn library (see scikit-learn.org). We show the tuning ranges utilized for hyper parameter tuning in Table 8 in Appendix A [34,35]. Per the suggestion of Bergstra and Bengio [7], we use a random search within each tuning range, as this approach has been shown to produce superior results relative to grid search.

To compare our methodology with other recent innovations in text analytics, we also consider two other recent approaches. One state-ofthe-art approach is BERT (Bidirectional Encoder Representations from Transformations) [20], which is a word-embedding-based approach that generates vectors capturing the semantic qualities of text. We used the $\mathtt { B E R T _ { L A R G E } }$ model that consists of a 24-layer, 340-million parameter neural network architecture. We then used these vectors to predict de lays using a bi-directional LSTM (Long Short-Term Memory) model implemented in Python using the keras library (see keras.io). In our model, we also incorporated the previously mentioned borrower and loan features in an additional layer. While these models are not always easily interpretable, their results are often quite impressive in terms of accuracy. Furthermore, a second recent approach we implemented was a utilization of LASSO (Least Absolute Shrinkage and Selection Oper ator) as suggested by Prollochs, ¨ Feuerriegel and Neumann [45]. Rather than using a separate information retrieval technique, the LASSO approach instead uses a statistical model with a penalty function to effectively perform feature selection. Thus, LASSO would also generate some key terms most associated with delays.

![](/api/attachments/VESWP77B/fulltext/images/e5ed69eeb5ef45a7799cd08429f6dfd4ba2a00f1ba60abcf7d14385eca7ef29d.jpg)  
Fig. 2. Overview of methodology.

Table 2  
Contingency table for each term. Adapted from Fan, Gordon and Pathak [24].

<table><tr><td></td><td>Document pertains to a delay</td><td>Document does not pertain to a delay</td><td>Row total</td></tr><tr><td>Document contains term</td><td>A</td><td>B</td><td>A+B</td></tr><tr><td>Document does not contain term</td><td>C</td><td>D</td><td>C+D</td></tr><tr><td>Column total</td><td>A+C</td><td>B+D</td><td>N</td></tr></table>

An advantage of using the seed terms or LASSO-generated terms as features is that our model is relatively interpretable; that is, while a neural network model on its own is often considered a “black box” whose inner workings are difficult to understand, our models offer far greater nuance. These models can indicate the specific words and phrases that resulted in that classification. This level of detail is useful to the managerial staff as they seek to determine the best course for remediation. Identifying the particular words and phrases that led to a particular recommendation from the model may offer insight into

rectifying the potential issue.

We report our results for each technique’s classifications according to five key metrics as follows. In each case, scores are scaled from 0 to 1, where 1 represents perfection:

• Accuracy: the proportion of records correctly classified.

• Precision: the proportion of records classified as delays that were actually associated with delays

• Recall: the proportion of records that were actually delay-associated that were correctly classified as such.

• F1-score: the harmonic mean between precision and recall, providing a holistic assessment of model performance, or 2\*<sup>(precision\*recall)</sup>. precision+recall

• AUC (Area Under the Curve): a scaled index of the area under a Receiver Operating Characteristic (ROC) curve, which compares the true positive rate to the false positive rate. We use the trapezoidal approximation suggested by Bradley [11].

## 4. Results

## 4.1. Machine learning modeling

In Table 3, we present the top ten unigrams, bigrams, and trigrams identified by the CC score information retrieval algorithm.<sup>1</sup> For brevity, we limit this table to the top ten terms of each type. Many of the terms returned appear fairly intuitive. For example, the unigram “report”

Table 3  
Top ten unigrams, bigrams, and trigrams retrieved by the CC score algorithm.

<table><tr><td>Unigram</td><td>Bigram</td><td>Trigram</td></tr><tr><td>Report</td><td>Its successors</td><td>Insurance agent company</td></tr><tr><td>Agent</td><td>Code 6</td><td>If insurance agent</td></tr><tr><td>Below</td><td>Insurance agent</td><td>Written request please</td></tr><tr><td>Insurance</td><td>Company request</td><td>Can be sent</td></tr><tr><td>Clause</td><td>Written request</td><td>Agent company request</td></tr><tr><td>Suite</td><td>First lien</td><td>Obtain the fax</td></tr><tr><td>Code</td><td>Carrier name</td><td>Request to send</td></tr><tr><td>Commitment</td><td>Send written</td><td>Company to update</td></tr><tr><td>Successors</td><td>Agent company</td><td>Policy and update</td></tr><tr><td>Assigns</td><td>Mortgage clause</td><td>Complete preliminary title</td></tr></table>

could refer to a document that the loan officers need to acquire before continuing to the next steps of the loan origination process. Some multiword phrases, such as “obtain the fax” or “request to send” are also intuitive, as they reflect the firm’s need to obtain additional documents to inform their process. However, some terms were not as obvious, such as the bigram “code 6.” Upon reflecting upon our dataset, we found that this bigram actually referred to an internal code used by the mortgage firm to refer to an instance in which a specific type of document was required for the next step in the origination process – a step that evidently was rather often associated with an upcoming delay.

In Table 4, we show the top ten unigrams, bigrams, and trigrams identified by LASSO coefficients. In this table, four unigrams, five bigrams, and four trigrams overlap with the top-ranking terms identified in Table 3. Overall, the competing methods were somewhat concordant and arrived at similar conclusions concerning which terms were topranking.

In Table 5, we show a comparison of the performance of our machine learning techniques’ classifications. For each metric, the best score is bolded and italicized. Overall, many of our techniques performed quite similarly to one another, scoring accuracy, precision, recall, F1-score, and AUC values in the mid-0.80s. The BERT + Bi-LSTM method had the top performance overall, scoring around 0.90 on each measure. Of the seed term techniques, the random forest method is a particularly appealing option for a general case as it scored around 0.88 on each of the five metrics. However, practitioners may have specific preferences based upon their organizational resources and risk tolerance. For instance, the Naïve Bayes model had both the highest precision score (0.9235) and the lowest recall score (0.3731). This result suggests that our Naïve Bayes model essentially had a high decision threshold to classify a record as likely to be associated with a delay; relatively few records were classified as delays, but records that were classified as delays were classified very accurately. Despite underperforming the other techniques based on accuracy, recall, F1-score, and AUC, some managers may nonetheless have a use case for this tool. For instance, in an organization with limited resources to devote to monitoring and managing potential delays, it is possible that insufficient resources will be available to devote to all likely delays. As such, the total number of likely delays retrieved (recall) is less important, and of more importance is that the resources expended are utilized to the greatest efficacy possible, requiring an accurate classification of the delay class (precision).

Table 4  
Top ten unigrams, bigrams, and trigrams retrieved by LASSO coefficients.

<table><tr><td>Unigram</td><td>Bigram</td><td>Trigram</td></tr><tr><td>Commitment</td><td>Condition by</td><td>Obtain the fax</td></tr><tr><td>Clients</td><td>First lien</td><td>Preliminary title report</td></tr><tr><td>Found</td><td>State requirement</td><td>Per state requirement</td></tr><tr><td>Written</td><td>Written request</td><td>Clause as below</td></tr><tr><td>Clause</td><td>Preliminary title</td><td>This condition by</td></tr><tr><td>Code</td><td>Its successors</td><td>Written request please</td></tr><tr><td>Alta</td><td>Company request</td><td>Can be sent</td></tr><tr><td>Holder</td><td>Due date</td><td>First lien holder</td></tr><tr><td>Assigns</td><td>Carrier name</td><td>Kindly provide further</td></tr><tr><td>Marital</td><td>Please request</td><td>Agent company request</td></tr></table>

On the other hand, some organizations may instead prefer higher recall at the expense of precision. For instance, the firm with which we collaborated on this research indicated a preference for recall over precision, as they deemed that they had sufficient organizational re sources to review all necessary records, and of more importance was identifying as many likely delay-associated records as possible (recall). For this use case, a modeling technique such as support vector machines (0.9141 recall) may be favored instead. A further consideration is over the interpretability of the technique, where BERT + Bi-LSTM is very high-performing but also rather opaque to interpret. As such, the random forest technique, which offers slightly lesser performance but substantial interpretability may be desirable. Regardless of the organi zational preferences, the bevy of machine learning options offered in this paper ensures that managers can choose a tool that best fits their organizational objectives.

## 4.2. Temporal robustness analysis

Given the temporal nature of our data, a potential concern is that our modeling is based upon a full internal transcripts pertaining to mortgage loans, and some of the comments comprising those transcripts could occur close to the intended condition resolution deadline. If this occurs, then the model would need to provide guidance based on incomplete information, as complete information could only be available narrowly prior to the condition resolution deadline.

In our dataset, we found that these potential effects were rather minor. In 90.89% of the conditions we evaluated, the final comment occurred at least one day prior to the condition resolution deadline, which may be enough time for a managerial intervention. Moreover, in 86.09% of conditions, the last comment occurred at least two days prior to the condition resolution deadline. Delayed conditions only differed slightly from these figures; the last comment in delayed conditions occurred at least one day prior to the condition resolution deadline 86.60% of the time and at least two days prior 81.69% of the time. Thus, in most real-world cases, our model would have a full transcript based upon which to make an evaluation.

To further evaluate this potential problem, we reran our analyses on a truncated dataset in which we omitted any comments that occurred within two days of the condition resolution deadline, thus leaving operational flexibility to act upon the results of the analysis. We display the result of these analyses in Table 6. As we would anticipate, the reduced information available for classification results in lesser perfor mance by each classification method via each measure. Despite this, performance is still quite promising, for instance with accuracy of up to 0.8409 by the BERT + Bi-LSTM model. In general, the BERT + Bi-LSTM method seemed most robust to the truncations in this dataset, although the performance of the random forest method was competitive. The choice of when to assess each condition for the likelihood of delay de pends on many organizational factors; organizations with substantial resources and flexibility may opt to wait until the day before deadlines before making delay or no delay predictions, as they will have the re sources to capitalize upon those more accurate predictions. On the other hand, firms without such resources may opt to analyze transcripts at an earlier stage when predictions may be less accurate, but they would be provided more time to prioritize and plan interventions.

## 4.3. Model interpretability

In Table $^ { 7 , }$ we show some exemplars showing annotated conversa tions transcripts in which seed terms are bolded and italicized. Along side these, we show our estimated delay likelihoods for the random forest model (highest accuracy, F1-score, and AUC of the seed termbased models); we note that these estimates would differ between the models, but they would be quite similar in most cases, and the seed

Table 5  
Performance comparison of each machine learning technique’s classifications.

<table><tr><td colspan="2">Classification method</td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1-score</td><td>AUC</td></tr><tr><td rowspan="10">CC score-based seed terms</td><td>Logistic regression</td><td>0.8380</td><td>0.8049</td><td>0.8887</td><td>0.8447</td><td>0.8384</td></tr><tr><td>Elastic net</td><td>0.8046</td><td>0.7940</td><td>0.8182</td><td>0.8059</td><td>0.8047</td></tr><tr><td>k-nearest neighbors</td><td>0.8739</td><td>0.8771</td><td>0.8673</td><td>0.8722</td><td>0.8739</td></tr><tr><td>Decision tree</td><td>0.8661</td><td>0.8682</td><td>0.8606</td><td>0.8644</td><td>0.8660</td></tr><tr><td>Random forest</td><td>0.8816</td><td>0.8881</td><td>0.8709</td><td>0.8794</td><td>0.8815</td></tr><tr><td>Gradient boosting</td><td>0.8588</td><td>0.8431</td><td>0.8788</td><td>0.8606</td><td>0.8590</td></tr><tr><td>Naïve Bayes</td><td>0.6739</td><td>0.9235</td><td>0.3731</td><td>0.5315</td><td>0.6713</td></tr><tr><td>Support vector machines</td><td>0.8400</td><td>0.7942</td><td>0.9141</td><td>0.8499</td><td>0.8406</td></tr><tr><td>Neural network</td><td>0.8302</td><td>0.7912</td><td>0.8931</td><td>0.8391</td><td>0.8307</td></tr><tr><td>AdaBoost</td><td>0.8457</td><td>0.8422</td><td>0.8475</td><td>0.8448</td><td>0.8457</td></tr><tr><td rowspan="2">Other methods</td><td>LASSO</td><td>0.8059</td><td>0.7556</td><td>0.9043</td><td>0.8233</td><td>0.8059</td></tr><tr><td>BERT + Bi-LSTM</td><td>0.9012</td><td>0.8976</td><td>0.9051</td><td>0.9013</td><td>0.9011</td></tr></table>

Table 6  
Performance comparison of each machine learning technique’s classifications.

<table><tr><td colspan="2">Classification method</td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1-score</td><td>AUC</td></tr><tr><td rowspan="10">CC score-based seed terms</td><td>Logistic regression</td><td>0.7637</td><td>0.7441</td><td>0.8156</td><td>0.7782</td><td>0.7642</td></tr><tr><td>Elastic net</td><td>0.7399</td><td>0.7470</td><td>0.7497</td><td>0.7483</td><td>0.7403</td></tr><tr><td>k-nearest neighbors</td><td>0.8144</td><td>0.8069</td><td>0.8111</td><td>0.8090</td><td>0.8148</td></tr><tr><td>Decision tree</td><td>0.8159</td><td>0.8067</td><td>0.7866</td><td>0.7965</td><td>0.8164</td></tr><tr><td>Random forest</td><td>0.8290</td><td>0.8358</td><td>0.8080</td><td>0.8217</td><td>0.8295</td></tr><tr><td>Gradient boosting</td><td>0.7910</td><td>0.7866</td><td>0.8171</td><td>0.8016</td><td>0.7913</td></tr><tr><td>Naïve Bayes</td><td>0.6180</td><td>0.8490</td><td>0.3418</td><td>0.4874</td><td>0.6183</td></tr><tr><td>Support vector machines</td><td>0.7689</td><td>0.7362</td><td>0.8475</td><td>0.7879</td><td>0.7693</td></tr><tr><td>Neural network</td><td>0.7579</td><td>0.7200</td><td>0.8397</td><td>0.7753</td><td>0.7582</td></tr><tr><td>AdaBoost</td><td>0.7800</td><td>0.7677</td><td>0.7900</td><td>0.7787</td><td>0.7803</td></tr><tr><td rowspan="2">Other methods</td><td>LASSO</td><td>0.7401</td><td>0.6695</td><td>0.8366</td><td>0.7438</td><td>0.7398</td></tr><tr><td>BERT + Bi-LSTM</td><td>0.8409</td><td>0.8413</td><td>0.8418</td><td>0.8416</td><td>0.8405</td></tr></table>

Table 7  
Exemplars of interpretable “seed terms” alongside estimated delay likelihoods.

<table><tr><td>Conversation transcript</td><td>Estimated delay likelihood</td><td>Delay?</td></tr><tr><td rowspan="3">&gt;&gt; &gt; Following documents are required:Complete Preliminary Title Report or Title Commitment. It must be inprescribed format and shouldcontainthe following:a) All the schedules inprescribed format of ALTA (2006) / CLTA (for CA State).b) Complete legal descriptionof the subject propertyalongwith interest in which land is held.c) Current/Proposed vestingalong with marital status as perstate requirement.d) Requirement/Exception sectionmust reflect all theliens/restrictionsassociated withsubject propertyand liensand judgments againstthe borrower(s) and seller(s).e) Tax details from all thetaxing authorities associated with the subject property.&gt;&gt; &gt;Kindlyverify the prelim and if any additional taxing authority/supplemental taxes is applicable then mention the same.&gt;&gt; &gt;DU - Fully automated approval and Account no. and password toreissue credit reportis required.&gt;&gt; &gt; Verify if the following is true on/before the application date for this loan:1. [COMPANY] is licensed in the subject property state.2. Broker’s / Correspondent’s / LO’s originating branch is licensed in the subject property state.3. Loan Officer is licensed in the subject property state.4. Broker’s / Correspondent’s / LO’s originating branch is approved in FHAC.5. Broker / Correspondent/ LO is approved for loan’s origination type in the property state.** Upload relevant documents to broker inbox</td><td>98%</td><td>Yes</td></tr><tr><td>69%</td><td>Yes</td></tr><tr><td>3%</td><td>No</td></tr></table>

terms would be the same.

In the first record, many seed terms are present, indicating to a manager that there are many potential avenues for delay, and the esti mated delay likelihood of 98% indicates that this loan may necessitate resources to get back on track. The second record is much shorter and has a 69% estimated delay likelihood because a reissued credit report is required, which the manager can quickly pick out and understand. The final record contains no seed terms, so its estimated delay likelihood was just 3%, indicating that it is likely low priority for additional scrutiny.

Although the performance of these seed term methods was slightly inferior to the BERT + Bi-LSTM model, a state-of-the-art technique, the interpretability of results is a noteworthy advantage of seed term ana lyses. From a managerial perspective, results are far more interpretable, which may improve acceptance in industry.

## 5. Limitations

Our study is subject to several key limitations. One limitation of our study is that our analysis is based on a single mortgage firm. While the collaborating national-level mortgage firm is large and thus processes a high volume of loans, resulting in a large dataset, we cannot guarantee that the results garnered from this analysis are generalizable to all other mortgage originators. However, we have no reason to believe that the linguistic properties of the collaborating firm’s communications would be exceptional within the industry. Nonetheless, one avenue for future work would be to examine the applicability of these models to additional firms.

A second limitation is that our analysis focused on relatively recent data sample from 2018 through 2019. While the performance of our text and predictive analytics was excellent during this date range, we cannot be certain about whether new linguistic characteristics will affect the efficacy of our techniques in the future. For example, some specific types of policies such as ALTA and CLTA were observed as seed terms (see Table 4 and Table 7); at some point, these may be replaced by newer policies. Future research may examine performance longitudinally to examine how stable these terms are over time, although this is beyond the scope of our paper.

A third limitation is that our study is focused on whether a delay is likely, but we do not model the severity of the delay either by assessing its length or its operational complexity. Predicting the length of a delay is somewhat complicated by the fact that archival delay data is affected not only by the condition resolution process preceding the delay but also by remediation efforts taken once the delay has begun. Upon consulting with the collaborating firm, we determined that little value was placed on the length of each delay, as any delays were treated as rather highpriority and allocated resources when available. Thus, we considered this extension outside the scope of this work, though it may be of interest to future studies.

Finally, in our modeling, we considered several borrower and loan characteristics including credit scores, borrower debt, loan type, and loan amount; however, we did not consider other demographic data such as age, gender, or ethnic origin. At least on a societal level, there is some evidence that these factors are related to loan default rates [51], and they may well be associated with the likelihood of delays in con dition resolution. However, there are substantial legal and ethical con cerns with using such data to support decision-making. Past occurrences of “racist AI” and “sexist AI” have been documented [57], and thus it is of great concern that these methodologies could algorithmically ingrain prejudices. As such, we do not include these features in our modeling.

## 6. Conclusions

Mortgage loan origination is a process involving many intricate steps, and delays are very common as a result. Mortgage firms have a vested interest in handling these processes gracefully, as they seek to establish a positive reputation and ensure the satisfaction of their cus tomers. Prior work has found that borrowers grapple with many serious considerations as they weigh the decision to take on substantial debt [13,19], and as a result, mortgage firms can substantially differentiate themselves from the competition if they offer streamlined originations.

In this paper, we have found that text analytic and machine learning techniques are viable and highly accurate for identifying those loan originations most likely to be delayed. We found that, using a combi nation of generated seed terms and machine learning modeling, we can accurately predict whether delays occur with approximately 88% ac curacy, and state-of-the-art word embeddings can achieve accuracy of approximately 90%. Depending on the manager’s preferences, a selection of models is available to address competing objectives, such a precision, recall, and interpretability, depending on organizational objectives

Our proposed methods have the potential to greatly improve busi ness processes. Fig. 3 illustrates the condition clearing process in the current business setup. Conditions to be cleared for each loan in the pipeline are listed on a graphical user interface (GUI). This screen also displays all textual communications related to each loan and condition combination. The condition clearing team is tasked with reviewing and monitoring these text communications and apply their experiential knowledge and intuition to identify and prioritize conditions those are at higher risk of delay. They then coordinate with the brokers, processors, and underwriters to clear these conditions so that the loan can be finally approved for funding. As intuitively sensing the likelihood of a delay is quite difficult, conditions are often treated with the same level of ur gency, leading to suboptimal efficacy. Essentially, a high delay-risk condition might be waiting in the queue while the team is busy with clearing conditions unlikely to be delayed.

The outcome of our research can transform the current condition clearing business process, leading to improved efficiency and business benefits. The collaborating mortgage firm plans to transform the above business process by implementing the findings from our research. Fig. 4 illustrates how the current business process might be transformed by implementing our findings.

In the proposed new process, new conditions will be extracted on a nightly basis and fed into the predictive model developed in this research. Using these methods, the predictive model analyzes the textual communications and calculates a risk score for each of the conditions. The estimated probability of delay could be used directly, or it could be collapsed into simpler categories such as “high risk,” “medium risk,” and “low risk” based upon some predetermined thresholds. The condition list is then displayed ranked by delay risk in descending order. This automated risk classification lays the foundation of the process trans formation and improved efficacy in the downstream condition clearing process. Once the conditions are classified, a risk-based routing function can be applied to distribute the conditions automatically to specialized teams based on skill requirements in handling conditions at varied risk levels.

The condition clearing process in mortgage origination business is a function critical to the success of a company, and as a result, employees require substantial experience and training. Consequently, these em ployees are among the most expensive resources in loan processing.

![](/api/attachments/VESWP77B/fulltext/images/40630037fb8de3aa78e3008ee4f39243ce5c620aedad45e013c1263944cfe0ad.jpg)  
Fig. 3. Current condition clearing process.

![](/api/attachments/VESWP77B/fulltext/images/df8616df0da08d7dbcb4f3930dc54217b2fd943133845249d3395060c9f58832.jpg)  
Fig. 4. Transformed business process.

Ability to tier the team based on skill levels and match them to the tasks of appropriate difficulty and importance has many benefits. Conditions with “high risk” can be automatically assigned to the queue of senior and experienced resources. This would ensure that the conditions most likely to be delayed are handled by the most competent resources, potentially reducing error and improving speed of execution. This also frees up these senior resources from spending time on the lower risk conditions, which can be resolved by less experienced and less expensive employees. These skill-based tiers and risk-based condition allocation not only leads to improved efficiencies in the process, but it also generates savings for the company due to optimized use of the expensive resources. Future work may investigate empirically the impact of these practices in practitioner applications.

## Appendix A. Tuning ranges

Tuning ranges used for hyperparameter tuning

<table><tr><td colspan="2">Classification method</td><td>Tuning parameter</td><td>Tuning range</td></tr><tr><td rowspan="23">CC score-based seed terms</td><td rowspan="2">Logistic regression</td><td>Penalty</td><td>L1, L2</td></tr><tr><td>C</td><td>1 to 4</td></tr><tr><td>Elastic net</td><td>N/A</td><td></td></tr><tr><td rowspan="2">k-nearest neighbors</td><td>Weights</td><td>Uniform, distance</td></tr><tr><td>Number of neighbors</td><td>3 to 9</td></tr><tr><td rowspan="5">Decision tree</td><td>Criterion</td><td>Gini, entropy</td></tr><tr><td>Maximum features</td><td>Automatic, square root</td></tr><tr><td>Maximum depth</td><td>20 to 100</td></tr><tr><td>Minimum samples for leaf</td><td>1 to 4</td></tr><tr><td>Minimum samples to split</td><td>2 to 10</td></tr><tr><td rowspan="6">Random forest</td><td>Criterion</td><td>Gini, entropy</td></tr><tr><td>Maximum features</td><td>Automatic, square root</td></tr><tr><td>Maximum depth</td><td>20 to 100</td></tr><tr><td>Minimum samples for leaf</td><td>1 to 4</td></tr><tr><td>Minimum samples to split</td><td>2 to 10</td></tr><tr><td>Number of estimators</td><td>100 to 400</td></tr><tr><td rowspan="5">Gradient boosting</td><td>Loss</td><td>Deviance, exponential</td></tr><tr><td>Learning rate</td><td>0.01 to 0.20</td></tr><tr><td>Minimum samples for leaf</td><td>1 to 4</td></tr><tr><td>Minimum samples to split</td><td>2 to 10</td></tr><tr><td>Number of estimators</td><td>100 to 400</td></tr><tr><td>Naïve Bayes</td><td>N/A</td><td></td></tr><tr><td>Support vector machines</td><td>C</td><td>1 to 1000</td></tr></table>

(continued on next page)

Table 8 (continued )

<table><tr><td>Classification method</td><td></td><td>Tuning parameter</td><td>Tuning range</td></tr><tr><td rowspan="11">Other methods</td><td rowspan="5">Neural network</td><td>Kernel</td><td>Linear, poly, RBF, sigmoid</td></tr><tr><td>Gamma</td><td>Scale, auto</td></tr><tr><td>Activation</td><td>Identity, logistic, tanh, relu</td></tr><tr><td>Learning rate</td><td>Constant, invscaling, adaptive</td></tr><tr><td>Alpha</td><td>0.0001 to 0.001</td></tr><tr><td rowspan="2">AdaBoost</td><td>Learning rate</td><td>0.25 to 5.00</td></tr><tr><td>Number of estimators</td><td>25 to 400</td></tr><tr><td>LASSO</td><td>N/A</td><td></td></tr><tr><td rowspan="3">BERT + Bi-LSTM</td><td>Activation</td><td>Linear, softmax, softplus, relu, tanh, sigmoid</td></tr><tr><td>Learning rate</td><td>0.0001 to 0.01</td></tr><tr><td>Dropout</td><td>0 to 0.4</td></tr></table>

## References

[1] A.S. Abrahams, W. Fan, G.A. Wang, Z. Zhang, J. Jiao, An integrated text analytic framework for product defect discovery. Prod. Oper, Manag, 24 (6) (2015) 975-990.

[2] A.S. Abrahams, J. Jiao, W. Fan, G.A. Wang, Z. Zhang, What’s buzzing in the blizzard of buzz? Automotive component isolation in social media postings, Decis. Support. Syst. 55 (4) (2013) 871–882.

[3] A.S. Abrahams, J. Jiao, G.A. Wang, W. Fan, Vehicle defect discovery from social media, Decis. Support. Syst. 54 (1) (2012) 87–97.

[4] S. Bag, M.K. Tiwari, F.T. Chan, Predicting the consumer’s purchase intention of durable goods: an attribute-level analysis, J. Bus. Res. 94 (2019) 408–419.

[5] G.E. Batista, A.L. Bazzan, M.C. Monard, Balancing training data for automated annotation of keywords: A case study, in: Workshop Brasileiro de Bioinformatica, 2003, pp. 10–18.

[6] J. Begley, H. Fout, M. LaCour-Little, N. Mota, Home equity conversion mortgages: the secondary market investor experience, J. Hous. Econ. 101623 (2019).

[7] J. Bergstra, Y. Bengio, Random search for hyper-parameter optimization, J. Mach. Learn. Res. 13 (1) (2012) 281–305.

[8] G. Bhat, S.G. Ryan, D. Vyas, The implications of credit risk modeling for banks loan loss provisions and loan-origination procyclicality, Manag. Sci. 65 (5) (2019) 2116–2141.

[9] E. Bigley, Origination Insight Report – January 2019, Ellie Mae, 2019.

[10] G. Bonaccorso, Machine Learning Algorithms, Packt Publishing Ltd, 2017.

[11] A.P. Bradley, The use of the area under the ROC curve in the evaluation of machin learning algorithms, Pattern Recogn. 30 (7) (1997) 1145–1159.

[12] R. Bubb, A. Kaufman, Securitization and moral hazard: evidence from credit score cutoff rules, J. Monet. Econ. 63 (2014) 1–18.

[13] M.W. Celsi, R.P. Nelson, S. Dellande, M.C. Gilly, Temptation’s itch: mindlessness, acceptance, and mindfulness in a debt management program, J. Bus. Res. 77 (2017) 81–94.

[14] S. Chan, A. Haughwout, A. Hayashi, W. Van der Klaauw, Determinants of mortgage default and consumer credit use: the effects of foreclosure laws and foreclosure delays, J. Money, Credit. Bank, 48 (2–3) (2016) 393–413

[15] Y. Chen, R.M. Rabbani, A. Gupta, M.J. Zaki, Comparative text analytics via topic modeling in banking, in: 2017 IEEE Symposium Series on Computational Intelligence (SSCI), IEEE, 2017, pp. 1–8.

[16] S. Chugani, K. Govinda, S. Ramasubbareddy, Data analysis of consumer complaints in banking industry using hybrid clustering, in: International Conference on Computing Methodologies and Communication (ICCMC), IEEE, 2018, pp. 74–78.

[17] FFEIC, Home Mortgage Disclosure Act Data, 2018.

[18] D. Delen, H.M. Zolbanin. The analytics paradigm in business research. J. Bus, Res. 90 (2018) 186–195.

[19] S. Dellande, M.C. Gilly, J.L. Graham, Managing consumer debt: culture, compliance, and completion, J. Bus, Res, 69 (7) (2016) 2594–2602

[20] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, BERT: Pre-training of deep

[21] M. Di Maggio, A. Kermani, S. Korgaonkar, Partial deregulation and competition: effects on risky mortgage origination, Manag, Sci. 65 (10) (2019) 4676–4711.

[22] J. Dietrich, F. Liu, A. Skhirtladze, M. Davies, Y. Jo, C. Candilis, Data Point: 2018 Mortgage Market Activity and Trends. Consumer Financial Protection Bureau. 2019

[23] A. Esuli, F. Sebastiani, SentiWordNet: A publicly available lexical resource for opinion mining, in: Language Resources and Evaluation Conference (LREC), Citeseer 2006 pp. 417-422

[24] W. Fan, M.D. Gordon, P. Pathak, Effective profiling of consumer information retrieval needs: a unified framework and empirical comparison, Decis. Support. Syst. 40 (2) (2005) 213–233.

[25] D.M. Goldberg, A.S. Abrahams, A Tabu search heuristic for smoke term curation in safety defect discovery, Decis. Support. Syst. 105 (2018) 52–65.

[26] D.M. Goldberg, N. Zaman, Text analytics for employee dissatisfaction in human resources management, in: 24th Americas Conference on Information Systems (AMCIS), 2018.

[27] S. Harden, Prepare for the Future of “Frictionless” Originations, Oracle Financial Services, 2018.

[28] W. He, X. Tian, J. Shen, Examining security risks of mobile banking applications through blog mining, in: International Conference on Information Systems (ICIS), 2016, pp. 103–108

[29] C.M. Hess, C.F. Kemerer, Computerized loan origination systems: an industry case study of the electronic markets hypothesis, MIS Q. (1994) 251–275.

[30] C.J. Hutto, E. Gilbert, VADER: A parsimonious rule-based model for sentiment analysis of social media text, in: Eighth International AAAI Conference on Weblogs and Social Media. 2014.

[31] W. Jiang, A.A. Nelson, E. Vytlacil, Liar’s loan? Effects of origination channel and information falsification on mortgage delinquency, Rev. Econ. Stat. 96 (1) (2014) 1–18.

[32] E.F. Kelly, P.J. Stone, Computer recognition of English word senses, North-Holland, 1975.

[33] B. Kim, J. Park, J. Suh, Transparency and accountability in AI decision support: explaining and visualizing convolutional neural networks for text information, Decis. Support. Syst. 113302 (2020).

[34] P. Koch, B. Wujek, O. Golovidov, S. Gardner, Automated hyperparameter tuning for effective machine learning, in: Proceedings of the SAS Global Forum 2017 Conference, SAS Institute Inc., 2017, pp. 1–23.

[35] M. Kraus, S. Feuerriegel, Decision support from financial disclosures with deep neural networks and transfer learning. Decis. Support. Syst. 104 (2017) 38–48

[36] H. Kvamme, N. Sellereite, K. Aas, S. Sjursen, Predicting mortgage default using convolutional neural networks, Expert Syst. Appl. 102 (2018) 207–217.

[37] G. Lemaître, F. Nogueira, C.K. Aridas, Imbalanced-learn: a Python toolbox to tackle the curse of imbalanced datasets in machine learning, J. Mach. Learn. Res. 18 (1) (2017) 559–563.

[38] C. Li, Q. Liu, L. Huang, Credit risk management of scientific and technologica enterprises based on text mining, Enterprise Inform. Syst. (2020) 1–17.

[39] S. Moro, P. Cortez, P. Rita, Business intelligence in banking: a literature analysis from 2002 to 2013 using text mining and latent Dirichlet allocation. Expert Syst Appl, 42 (3) (2015) 1314–1324.

[40] V. Mummalaneni, R. Gruss, D.M. Goldberg, J.P. Ehsani, A.S. Abrahams, Social media analytics for quality surveillance and safety hazard detection in baby cribs Saf Sci 104 (2018) 260–268

[41] O. Netzer, A. Lemaire, M. Herzenstein, When words sweat: identifving signals for loan default in the text of loan applications, J. Mark. Res. 56 (6) (2019) 960–980.

[42] F.Å. Nielsen, A new ANEW: Evaluation of a word list for sentiment analysis in microblogs, in: Proceedings of the 1st Workshop on Making Sense of Microposts 2011, pp. 93–98.

[43] K.A. Park, FHA loan performance and adverse selection in mortgage insurance J. Hous. Econ. 34 (2016) 82–97

[44] D. Pessach, G. Singer, D. Ayrahami, H.C. Ben-Gal. E. Shmueli, I. Ben-Gal Employees recruitment: a prescriptive analytics approach via machine learning and mathematical programming, Decis. Support. Syst. 113290 (2020)

[45] N. Pröllochs. S. Feuerriegel. D. Neumann, Statistical inferences for polarity identification in natural language, PLoS One 13 (12) (2018), e0209323.

[46] S. Ronnqvist, ¨ P. Sarlin, Bank distress in the news: describing events through deep learning, Neurocomputing 264 (2017) 57–70.

[47] C. Rudin, Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead, Nat. Machine Intell. 1 (5) (2019) 206–215.

[48] S. Sachan, J.-B. Yang, D.-L. Xu, D.E. Benavides, Y. Li, An explainable AI decisionsupport-system to automate loan underwriting, Expert Syst. Appl. 144 (2020) 113100.

[49] M. Thelwall, K. Buckley, G. Paltoglou, D. Cai, A. Kappas, Sentiment strength detection in short informal text, J. Am. Soc. Inf, Sci, Technol, 61 (12) (2010) 2544-2558.

[5o]JL. Viviani, H.L. Hanh. Why Do Banks Fail? - the Explanation from Text Analytics Technique, 2018.

[51] I. Voicu, M. Jacob, K. Rengert, I. Fang, Subprime loan default resolutions: do they vary across mortgage products and borrower demographic groups? J. Real Estate Financ. Econ, 45 (4) (2012) 939–964.

[52] C.M. Vojtech, B.S. Kay, J.C. Driscoll, The real consequences of bank mortgage lending standards, J Financ. Intermed. (2019) 100846.

[53] Z. Wang, C. Jiang, H. Zhao, Y. Ding, Mining semantic soft factors for credit risk

[54] L. Wei, G. Li, X. Zhu, J. Li, Discovering bank risk factors from financial statements based on a new semi-supervised text mining algorithm, Account. Finance 59 (3) (2019) 1519–1552.

[55] Y. Yu, W. Duan, Q. Cao, The impact of social and conventional media on firm equity value: a sentiment analysis approach, Decis. Support. Syst. 55 (4) (2013) 919–926.

[56] N. Zaman, D.M. Goldberg, A.S. Abrahams, R.A. Essig, Facebook hospital reviews: automated service quality detection and relationships with patient satisfaction, Decis, Sci, (2020).

[57] J. Zou, L. Schiebinger, AI Can Be Sexist and Racist—it’s Time to Make it Fair, Nature Publishing Group, 2018

Arin Brahma is Assistant Professor of Information Systems and Business Analytics in the College of Business Administration at Loyola Marymount University. With a graduate degree in Industrial Engineering, Arin received his PhD in Data Science and Analytics from Claremont Graduate University. Before his PhD, Arin served in the information technology consulting field for many Fortune 500 companies, including Amgen, Disney, AT&T, and several mortgage banking companies. His current research interests include exploring applications of machine learning and analytics in the field of healthcare, green energy, and financial services. His recent publications include DESRIST 2019 Conference Proceedings in Lecture Notes in Computer Science.

David M. Goldberg is Assistant Professor of Management Information Systems in the Fowler College of Business at San Diego State University. He received his doctoral and bachelor’s degrees from Virginia Tech. His current research interests are in the areas of business analytics, artificial intelligence, text mining, and event study analyses. He has published in Decision Support Systems, Decision Sciences, Information Technology & Man agement, Communications of the Association for Information Systems, and others.

Nohel Zaman is Assistant Professor of Information Systems and Business Analytics in the College of Business Administration at Lovola Marymount University. His research interests fall under the areas of business analytics, text mining, safety concerns of consumer products, and quality services. He received his PhD in Business Information Technology from Virginia Tech. Additionally, he earned a BSc degree in Business Administration along with a MSc degree in Economics from the University of Texas at Dallas and a MSc degree in Computational Science and Engineering from the North Carolina A&T State University. His work has recently been published in Decision Sciences.

Mariano Aloiso recently finished his bachelor’s degree of science in Mathematics at Loyola Marymount University. His research interests include the areas of decision analysis, applied probability, text mining and time series analysis
