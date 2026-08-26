---
otero_id: 13032
otero_key: "ZUZD2AE9"
title: "Understanding Medication Nonadherence from Social Media: A Sentiment-Enriched Deep Learning Approach"
authors: "Jiaheng Xie; Xiao Liu; Daniel Dajun Zeng; Xiao Fang"
year: "2022"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/15336"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# UNDERSTANDING MEDICATION NONADHERENCE FROM SOCIAL MEDIA: A SENTIMENT-ENRICHED DEEP LEARNING APPROACH<sup>1</sup>

Jiaheng Xie Department of Accounting and Management Information Systems, Lerner College of Business & Economics, University of Delaware, Newark, DE, U.S.A {jxie@udel.edu}

Xiao Liu Department of Information Systems, W. P. Carey School of Business, Arizona State University, Tempe, AZ, U.S.A. {Xiao.Liu.10@asu.edu}

## Daniel Dajun Zeng

State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing, and University of Chinese Academy of Sciences, Beijing, CHINA {dajun.zeng@ia.ac.cn}

Xiao Fang Department of Accounting and Management Information Systems, Lerner College of Business & Economics, University of Delaware, Newark, DE, U.S.A {xfang@udel.edu}

Medication nonadherence (MNA) can lead to serious health ramifications and costs U.S. healthcare systems \$290 billion annually. Understanding the reasons underlying patients’ MNA is thus an urgent goal for researchers, practitioners, and the pharmaceutical industry in order to mitigate negative health and economic consequences. In recent years, patient engagement on social media sites has soared, making it a cost-efficient and rich information source that can complement prior survey studies and deepen the understanding of MNA. Yet these data remain untapped in existing MNA studies because of technical challenges such as long texts, decision-making based on negative sentiment, varied patient vocabulary, and the scarcity of relevant information. For this study, we developed a sentiment-enriched deep learning method (SEDEL) to address these challenges and extract reasons for MNA. We evaluated SEDEL using 53,180 reviews concerning 180 drugs and achieved a precision of 89.25%, a recall of 88.48%, and an F1 score of 88.86%. SEDEL significantly outperformed state-of-the-art baseline models. We identified nine categories of MNA reasons, which were verified by domain experts. This study contributes to IS research by devising a novel deep-learning-based approach for reason mining and by providing direct implications for the health industry and for practitioners regarding the design of interventions.

Keywords: Sentiment-enriched deep learning, reason mining, social media analytics, health risk analytics, medication nonadherence

## Introduction

Medication nonadherence (MNA) is a complex and multidimensional problem characterized by patients not following recommendations for prescribed treatments (Hugtenburg et al. 2013). Despite the prevailing evidence that medical therapies prevent death and improve quality of life, numerous studies have shown that fewer than 50% of patients take medications as prescribed (Traverso and Langer 2015), which can lead to adverse effects such as intensified pharmacotherapy, increased medication dosage, misdiagnoses, the exacerbation of disease, and even death (Dunbar et al. 2008). MNA leads to estimated deaths of

125,000 per year and 33% to 69% of medication-related hospital admissions in the U.S. In terms of economic impact, MNA accounts for \$290 billion in preventable annual costs in the U.S. and 19% of all medication-related emergency room visits (Traverso and Langer 2015). Stakeholders are interested in understanding the reasons for MNA in order to formulate effective strategies to improve medication adherence and thereby remedy the health and economic ramifications of this problem. We define the reasons for MNA as factors described by patients that lead to their nonadherence decisions. Our research objective is to propose and evaluate an innovative computational approach to identifying MNA reasons.

Existing research has investigated MNA behaviors via surveys (Marcum et al. 2013; Williams et al. 2014), which, however, have major deficiencies. First, most surveys focus on a single medication or disease, but since most patients take multiple drugs for various health conditions, the adherence interventions based on these single-drug surveys may not be applicable to a large portion of the patient population. Second, existing surveys are provider centered because direct and timely communications from patients are difficult to obtain. However, the provider perspective is insufficient because providers have little control over the actual medication-taking behaviors of their patients. Evidence suggests that patients’ perspectives are lacking in existing MNA research (Xie et al. 2017). A survey by Pew Internet Research (2013) revealed that 61% of adults search online for health information and 59% of adults are active on health social media platforms (Pew Internet Research 2013). Because of the anonymous nature of health social media, patients are likely more willing to elaborate on their reasons for MNA in this context (Goh et al. 2016). Thus, this largescale dataset of patient self-reported information creates an unprecedented opportunity to study MNA reasons from the standpoint of patients’ decision-making (Chen et al. 2012). To the best of our knowledge, no social media approach has heretofore been adopted in studies of MNA.

While identifying MNA reasons using social media is challenging, as we further note below, it offers a unique opportunity to leverage sentiment in this context. Patients’ discussions about why they stop taking a drug are often accompanied by negative sentiment based on unpleasant experiences. Thus, the sentiment-enriched text analytics method is well-suited to understanding decision-making associated with negative sentiment. Reason extraction contexts beyond MNA can also benefit from our work. For instance, product returns are costly for retailers, and there has been substantial research on how to manage returns. One of the key aspects of this is understanding why products are returned in the first place. Negative sentiment in product reviews could similarly help extract potential causes. Although sentiment can be incorporated into text mining models in different ways, our approach learns an embedding that jointly predicts contextual words and word-level sentiment. This new type of embedding captures the nuance of sentiment and the contextual information of each word and can be used to accurately extract reasons for MNA.

Despite the opportunity of leveraging sentiment to assist MNA-reason mining, significant technical challenges remain. Social media users describe diseases and symptoms using a wide range of consumer health vocabulary. For instance, arthritis is often described as “joint pain” or “joint swelling.” Furthermore, discussions that are irrelevant to MNA are abundant on health social media sites, far outnumbering those about MNA. Figure 1 shows two posts from a popular online health community (WebMD).

This work is motivated by the critical need for a fine-grained social media analytics technique to understand the reasons for MNA. We propose a computational method, sentimentenriched deep learning (SEDEL), that addresses decisionmaking based on negative sentiment in social media, varied health vocabulary among users, and the scarcity of MNArelated narratives. SEDEL extends state-of-the-art social media analytics techniques with a novel sentiment-enriched representation and a hybrid deep-learning architecture. The sentiment-enriched component effectively captures the impact of patients’ negative sentiments on decision-making and improves the representation of varied patients’ health vocabulary. Furthermore, the hybrid deep learning architecture enhances the learning performance in minority classes through a recurrent hierarchical structure, which improves the extraction of sparse MNA-related narratives.

Our study makes the following contributions. First, we design a sentiment-enriched deep learning approach for reason mining. We evaluate this method in the context of MNAreason mining with a dataset consisting of 53,180 reviews of 180 drugs. Our proposed approach significantly outperforms baseline methods for opinion-based social media text. This performance enhancement is mainly attributed to the sentiment-enriched component, which accounts for the negative user sentiment expressed in decision-making. We performed hyperparameter fine-tuning and carefully designed dropout and regularization mechanisms in the hybrid deep-learning architecture. This refined architecture enhances the learning performance on the sparse information available. Our proposed sentiment-enriched computational approach is not restricted to the MNA domain. It can also translate into identifying the factors of consumer behaviors in opinion-based texts, such as product reviews, physician reviews, and commentary articles.

![](/api/attachments/ZUZD2AE9/fulltext/images/83f54c8642bc27f8bee400a3e6e942f2805aa612c852fbef3d6619a96473e691.jpg)  
Figure 1. An Example of the Technical Challenges in Health Social Media

Second, we outline a social media approach to understanding patients’ risky behaviors that is complementary to the commonly adopted survey approach. Our approach extends current behavioral research on MNA with comprehensive patient experience data. Third, we reveal nine categories of MNA reasons, including several that are unreported by prior studies, such as social influence and specific population (e.g., children and liver disease patients, respectively). Our findings provide valuable insights for stakeholders seeking to understand MNA from the patient perspective, allowing for tailored interventions to improve disease management and reduce healthcare costs.

## Literature Review

## Understanding MNA Using Social Media

The MNA reasons for a particular drug class or patient group are commonly investigated using surveys. Subject group sizes in these surveys have ranged from 19 to over a thousand patients (Weidenbacher et al. 2015). A summary of the evidence-based MNA reasons and corresponding clinical strategies to improve adherence is provided in Table 1.

Understanding MNA reasons is essential for developing effective interventions. However, studies on MNA reasons are largely limited in the following ways: First, most surveys focus on one medication, which is insufficient for understanding the MNA reasons of patients that take multiple medications simultaneously. Second, most patients are reluctant to reveal their real levels of adherence in surveys, and obtaining research subjects is time- and resource-consuming (Krousel-Wood et al. 2009). Third, survey studies only offer a snapshot of MNA reasons and cannot address MNA reasons for new drugs. These limitations are perhaps responsible for the rather low intervention success rates—only 36 out of 83 interventions reported in 70 randomized trials are associated with significant improvement in adherence, and only 25 of these trials led to improvements in patient outcomes (Gellad et al. 2009). To increase the intervention success rate, MNA-reason mining needs health data sources from a substantial and diverse population so that new models can learn from heterogeneous patient groups and drug classes and predict MNA reasons for future patients.

Since the early 2000s, health social media have made innovative projects possible and created opportunities for investigations that yield insights into patient decision-making (Chen et al. 2012; Baesens et al. 2014). Furthermore, information systems literature has stressed the value of health social media analytics because online patient communities provide insight into diseases and analytics offers the potential to estimate patients’ level of adherence to medication regimens (Bardhan et al. 2017).

Given that social media data are unstructured and come from networks of patients, it is essential to design powerful algorithms and data representations specifically for this heterogeneous health information dataset (Abbasi et al. 2010, 2012; Fang et al. 2013; Mai et al. 2018; Saboo 2016; Stieglitz and Dang-Xuan 2013). Hevner et al. (2004), Gregor and Hevner (2013), and Chen et al. (2012) emphasized the necessity for such a design and computational category of IS research and outlined a guideline for design science studies seeking to leverage cutting-edge algorithms to tackle significant problems with societal impacts.

<table><tr><td colspan="3">Table 1. Medication Nonadherence Reasons and Clinical Strategies in Prior Research</td></tr><tr><td>Reason type</td><td>Definition</td><td>Clinical strategies to improve adherence</td></tr><tr><td rowspan="3">Low health literacy</td><td rowspan="3">Low ability to read, understand, and use information to make treatment decisions (Sørensen et al. 2012).</td><td>Use education to give instructions to patients</td></tr><tr><td>Give instructions to a second person</td></tr><tr><td>Use community liaisons to reinforce information</td></tr><tr><td rowspan="3">Poor provider-patient communications</td><td rowspan="3">Communication gaps among patients, caregivers, and providers (Bosworth et al. 2011)</td><td>Communication training for clinics and provider staff</td></tr><tr><td>Engage patients in using e-health diaries</td></tr><tr><td>Avoid overwhelming patients or using jargons</td></tr><tr><td rowspan="4">Complex medication plan</td><td rowspan="4">The complexity of a medication regimen and the use of multiple medications (Hugtenburg et al. 2013)</td><td>Simplify the dosing regimen</td></tr><tr><td>Alter the administration route</td></tr><tr><td>Explore the patient&#x27;s preference for dosing schedule</td></tr><tr><td>Use electronic adherence aids</td></tr><tr><td rowspan="3">No-fill of the first prescription</td><td rowspan="3">Failure to fill first-time prescriptions (Tamblyn et al. 2014)</td><td>Dispense the first fill to the patients at discharge</td></tr><tr><td>Discuss the patient&#x27;s willingness to take new drugs</td></tr><tr><td>Identify a person to obtain the medication for the patient</td></tr><tr><td rowspan="4">Forgetfulness</td><td rowspan="4">Forgetfulness and not knowing exactly how to use medications (Bosworth et al. 2011)</td><td>Choose drug available in a calendar blister-packaging</td></tr><tr><td>Enroll patient in a follow-up program to receive reminders</td></tr><tr><td>Include a caregiver in the communication for reminders</td></tr><tr><td>Engage patients with an accountability partner of their choice</td></tr><tr><td rowspan="3">Cost prohibitive for patients</td><td rowspan="3">Financial challenges for patients (Goldman et al. 2007)</td><td>Select a different medication or a generic</td></tr><tr><td>Identify a local low-cost drug program</td></tr><tr><td>Identify a payment program for nongeneric drugs</td></tr><tr><td rowspan="2">Nonresponders or medication ineffectiveness</td><td rowspan="2">Patients do not respond to specific treatments as expected (McHorney et al. 2007)</td><td>Ask patients about medication-taking using a validated assessment tool</td></tr><tr><td>Use a short-term monitor and reevaluate drug response</td></tr><tr><td>Severe mental illness</td><td>Presence of coexisting mental illness (anxiety) (Gellad et al. 2009)</td><td>Treat mental health first, then resume other medication adherence/interventions and monitoring</td></tr><tr><td rowspan="4">Adverse events</td><td rowspan="4">The harmful health outcome associated with the use of medical products (Bosworth et al. 2011)</td><td>Attempt to confirm the drug-event relationship</td></tr><tr><td>Modify dose</td></tr><tr><td>Discontinue medication</td></tr><tr><td>Alter medication choice</td></tr></table>

MNA is a significant issue that requires a thorough understanding of patients’ decision-making processes. Health social media data provide a new source of heterogeneous patient opinions in a timely manner. To harness the value of social media, we develop a fine-grained and scalable text analytics method. Our study by no means attempts to substitute for the survey approach. Instead, we seek to enrich the existing knowledge on MNA from the perspective of patients.

## Reason Mining Using Social Media

Research from the well-established discipline of aspect mining, which includes many applications such as purchase decisions and technology acceptance (Zhang and Liu 2014), is useful for distilling patient intelligence from social media data. Aspect mining has two subtasks: aspect extraction and aspect clustering (Zhang and Liu 2014). Aspect extraction identifies aspect expressions<sup>2</sup> in texts, using latent Dirichlet allocation (LDA), conditional random fields (CRFs), and recurrent neural networks (RNNs) (Liu et al. 2016; Wang et al. 2016a). Since it is common to use different aspect expressions to describe the same aspect, aspect clustering groups similar aspect expressions and identifies metalevel aspects. Common aspect clustering methods include k-means and LDA (Wang et al. 2016b; Xiong and Ji 2016). Aspect clustering is relatively trivial because the aspect expressions retrieved by aspect extraction are semantically related. However, fine-grained aspect extraction nevertheless requires a sophisticated research design.

MNA reasons might be related to treatments, patients, patient-provider relationships, etc. (Gellad et al. 2011). Thus, LDA is not suitable for reason mining because LDA may generate many topic clusters that are irrelevant to MNA reasons because MNA reasons are sparse in the data. It is also difficult to single out one topic cluster related to MNA reasons. CRFs in aspect extraction usually achieve good performance regarding the identification of entities of interest in formal text corpora. However, their performance is unsatisfying in the context of health social media because of the colloquial and diverse expressions that patients use to describe similar medical terms. Since conventional sequence learning models rely on symbolic representation to label words, “joint pain” and “joint swelling,” for example, would be represented as two different features even though they both indicate rheumatoid arthritis. Semantic relationships among the varied forms of patients’ descriptions of the same disease or symptom are thus neglected by CRFs. Furthermore, CRFs require balanced data to train parameters, and their performance on minority classes in data is lower. Moreover, CRFs use generic textual features that are only suited for generic information retrieval tasks. MNA is a special context where patients discuss decisionmaking based on negative sentiment. The negative sentiment of such decisions is overlooked by CRFs. These limitations make CRFs unable to handle varied patient vocabulary, the scarcity of MNA-related information, and decision-making based on negative sentiment in social media data.

Building on prior work in aspect mining, previous studies have proposed reason mining in order to examine more nuanced user behaviors. Kim and Hovy (2006) first proposed identifying reasons for opinions in product reviews. They defined reason mining as the problem of extracting reasons that explain why review authors like or dislike a product. Hasan and Ng (2014) designed the maximum entropy Markov model (MEMM) to identify reasons in the context of political debates.

MNA-reason mining and aspect mining are similar because they both identify the attributes of objects that affect consumers’ decision-making. However, there are differences between these two tasks. First, MNA reasons are not limited to the attributes of objects. The factors leading to MNA are related not only to medications but also to patients and patient-provider relationships, which do not fall under the realm of aspect mining. Second, patients who intentionally do not adhere to their treatment protocols usually have unfavorable opinions about their prescribed drugs because of side effects, unexpected costs, ineffectiveness, etc. Studies in health informatics have suggested that nonadherence-related patient narratives on the web are associated with more negative sentiment compared to product aspect discussions (Hart et al. 2020; Onishi et al. 2018). Although product aspect mining studies rely on textual features, such as syntactic features and domain lexicons, MNA-reason mining demands special attention to the negative sentiment associated with patients decision-making. In developing our approach, we needed to improve existing aspect mining techniques and word representations and incorporate sentiment into the representation learning method.

## Representation Learning

The performance of machine learning methods is heavily dependent on the data representation they are applied to (Bengio et al. 2013): “A good representation is one that makes a subsequent learning task easier” (Goodfellow et al. 2016, p. 518). This data representation guideline has given rise to an interesting and actively evolving research area in the deep learning community called representation learning. The rapid increase in scientific activities on representation learning has been accompanied and fostered by a remarkable stream of empirical success in the areas of speech recognition (Chorowski et al. 2019), object detection and computer vision (Kim et al. 2019), natural language processing (Devlin et al. 2018), and social network analysis (Hamilton et al. 2017).

Training word embedding with neural networks has recently become a primary focus in the representation learning method for text analytics. Word embedding has resulted in state-ofthe-art performance for knowledge discovery and applications in the context of drug reviews and patient support forum discussions (Cheng et al. 2016). Word embedding is a vectorbased representation learning model that represents a word with its neighboring words (Levy and Goldberg 2014). There are two main model families for learning word embedding: (1) local context window methods such as Skip-gram and CBOW, and (2) global matrix factorization such as GloVe. Skip-gram and CBOW are prediction methods; they learn the neighboring words of a focal word within a window size across the corpus and predict the most likely neighbors for it. The window size can be empirically adjusted based on whether the MNA reason has a long or short dependency. Skip-gram is superior to CBOW in predicting rare cases, such as MNA reasons in our study.

GloVe creates a global co-occurrence matrix of words on the entire corpus. Logistic regression is trained on the global wordword co-occurrence counts to predict the neighbors of a word. The predicted result is the GloVe vector for the word. Existing literature has found competing support for both Skip-gram and GloVe (Pennington et al. 2014). We choose Skip-gram as the base model for this study, as the local context window is more favorable to MNA-reason mining. Social media users generally do not follow formal writing rules. Run-on sentences and incomplete sentences negatively impact the GloVe model.

Furthermore, MNA-reason expressions account for a very small portion of the corpus. Creating a representation with a global context may dilute the critical characteristics of these MNAreason expressions.

Word embedding is still limited in terms of understanding MNA because MNA is often caused by unpleasant experiences associated with taking medication. Solely relying on word embedding is insufficient to capture the essence of such opinion-based behaviors. When patients discuss MNA reasons in social media, they usually express negative sentiment. In this study, we aim to incorporate sentiment into the analytics method to effectively capture decision-making based on negative sentiment.

## The Role of Sentiment in Machine Learning

Sentiment has assisted the comprehension of many decisionmaking processes, which can be either rational or irrational. Luo et al. (2017) found that sentiment in expert blogs influences brand perception by consumers and enables brands to achieve competitive advantages. Deng et al. (2018) show that the influence of social media sentiment on stock returns is both statistically and economically significant at the hour level. Because of its critical value, sentiment has been widely studied to improve the performance of machine learning models.

Extant work leveraging sentiment in machine learning models falls into three categories. The first category of studies aims to predict sentiment. Sentiment serves as the outcome variable to measure consumer responses, such as purchase intention and consumer satisfaction. For instance, Wallace et al. (2014) developed a factorial LDA to predict the sentiment of each topic in physician reviews. Labutov and Lipson (2013) proposed a method for repurposing existing word embedding to predict document-level sentiment scores in movie reviews.

The second category of research adopts sentiment as a symbolic feature in the input to filter results or enrich the feature set. For instance, Fu et al. (2012) proposed a sentiment-based web crawler to retrieve relevant web pages. The authors trained a sentiment classifier to predict the sentiment of web pages. In addition to a topic model that retrieves web pages of interest, this sentiment classifier works as a filter to extract web pages with the intended sentiment. Paul and Dredze (2012) used factorial LDA to predict document sentiment together with a document topic to make document retrieval more accurate in opinion-based texts. Abbasi et al. (2018) designed a language-action perspectivebased text analytics framework to support sensemaking in online discourse, where sentiment is used as a linguistic feature for coherence analysis.

The third category of studies adds document-level sentiment as a regulator in the loss function of syntactic models. For instance, Tang et al. (2014) developed a neural network to capture the sentence-level syntactic structure and predict the sentiment of tweets. The input layer of this neural network takes in the target word and related contextual words in a sentence. The output layer of this neural network contains the tweet sentiment and syntactic score, which is manually created by the researchers to reflect the syntactic relationship of the words in the input sentence. The loss function of the network accounts for both tweet-level sentiment loss and sentence-level syntactic loss. The representation is optimized for document-level sentiment and syntactic structure prediction. It learns the syntactic relationships among words but not the semantic meaning, which is critical for understanding user behaviors in the context of social media. Furthermore, aggregated sentiment at the document or sentence level neglects the nuance in the sentiment expressed at the word or phrase level. Sentences in social media posts can be long and address multiple issues due to informal writing and little use of punctuation, and a single sentence may contain phrases and words with varying sentiment polarity. This approach can work well on Twitter, as most tweets are short and have uniform sentiment; however, it is not practical for long documents.

A good representation is expected to disentangle factors of variation: variation in the data relevant to the subsequent learning task should be preserved while the representation should be insensitive to variations in the data that are uninformative to the task at hand (Bengio et al. 2013). Although sentiment is considered to be an explanatory factor in consumer decision-making, there is very limited work on how learning a vector representation and word sentiment can harness the explanatory power of sentiment. In this study, we devise a sentiment-enriched word embedding that simultaneously learns the word sentiment and its vector representation in order to improve the understanding of MNA reasons in online drug reviews.

This research differs from prior sentiment-based methods in the following ways. First, in contrast to prior studies that regard sentiment as a prediction outcome (e.g., Maas et al. 2011; Labutov and Lipson 2013; Tang et al. 2014; Wallace et al. 2014; Paul and Dreze 2012), our learning task is MNAreason mining, not sentiment analysis. Sentiment does not directly indicate the reason behind an MNA decision. Instead, it can be an informative aspect that can be used to infer MNA reasons.

Second, we train a vector-based representation rather than adopting a static and symbolic sentiment feature (e.g., Fu et al. 2012 and Abbasi et al. 2018). Health social media posts are relatively long and may include mixed sentiments. The assumption that sentiment is a static feature at the sentenceor document level does not always hold. Representing sentiment as a symbolic feature may elide the nuances of patients’ self-reported medical experience, which is crucial in this study. In a vector-based representation, each dimension contributes to learning the correlation of a word with its contextual words. Hence, sentiment cannot be directly added as a feature in this vector without learning because it introduces an incompatible dimension.

Third, our proposed sentiment-enriched word embedding is different from that of Tang et al. (2014) because we train the embedding of word-level sentiment jointly with semantic context. The semantic context of a word is more important than its syntactic relationship for understanding user decision-making. A sentence could contain expressions of varying sentiments in relation to different topics. A sentence-level sentiment may mask the subtle sentiment differences among individual expressions. We leverage unigram sentiment jointly with the semantic context of a word to train the embedding because it better captures the sentiment heterogeneity among different phrases in a sentence. A good data representation for MNA-reason mining must capture variation in the semantic context as well as the sentiment of drug reviews and then translate this representation into appropriate training criteria.

## Deep Learning Methods

A carefully designed data representation also requires a finetuned downstream architecture for text analytics. Text mining has benefited greatly from the resurgence of deep neural networks because of their superior performance and their reduced need for feature engineering. Supervised deep learning architectures can be broadly categorized into three types: convolutional neural networks (CNNs), recurrent neural networks (RNNs), and hybrid networks. CNNs utilize layers with filters to extract local features, which has demonstrated good performance in sentiment analysis and text classification. For tasks that involve sequential inputs, such as speech and text, it is often better to use RNNs. Long short-term memory (LSTM) is a variation of an RNN (Tai et al. 2015). Since LSTM uses a memory cell to store the previous information, it can retain useful information about each word even though the word is distant from the current time step. RNNs and LSTMs have been utilized in various health studies for, e.g., mortality predictions (Aczon et al. 2017) and activity of daily life predictions (Ordóñez and Roggen 2016).

In order to further improve the performance of text mining, researchers have modified the learning methodologies and architectures of CNN and RNN. Kalchbrenner et al. (2014)

developed a dynamic CNN that can capture long-term dependencies to model the semantics of sentences. Yang et al. (2016) applied an attention mechanism to extract words and sentences that are important to classification tasks and assigned them higher weights in RNN-based hierarchical attention networks. Other studies have attempted to combine CNN and RNN. A large portion of CNN-RNN cooperation algorithms feed convolutional or pooling layers into LSTM or simply the recurrent layer output (Zhou et al. 2016), or feed LSTM or a recurrent layer into the convolutional or pooling layer output (Wang et al. 2016c). Such architectures also integrate additional techniques to improve performance. The recurrent structure can capture contextual information to a large extent and preserve a larger range of the word order when learning the word representation. Adding a maxpooling or convolutional layer can automatically judge which features play key roles in the learning objective and capture key components in the text. Tang et al. (2015) averaged the outputs from pooling layers with different sizes when using CNN to compute continuous representations of sentences with semantic composition and fed the aggregated result into a gated RNN for document representation. Hierarchically combining deep neural networks, researchers found that using CNN and RNN together leads to better sentence comprehension.

As a separate stream of deep learning techniques, probabilistic graphical models have been developed as effective ways of enhancing the accuracy of deep learning models. In particular, Markov random fields (MRFs) and their variant, CRFs, have been broadly successful (Zheng et al. 2015). Chen et al. (2017) applied BLSTM-CRF to identify opinion targets in the text. The key idea of including a CRF layer is to formulate the opinion-target detection problem as a probabilistic inference problem. The prediction of whether a word in a text is part of the opinion target can be inferred from neighboring words. In this paper, we design a hybrid network that integrates multiple advantages to extract scarce MNA-reason expressions.

## Research Gaps

The literature review reveals multiple challenges and opportunities. First, health social media, a previously untapped data source for MNA, has the potential to reveal patient perspectives. Second, existing methods have failed to accurately and effectively identify user opinions from social media sources. Deep learning methods are well-positioned to address the technical challenges in social media analytics. Third, sentiment is a critical element to understanding patients’ MNA decisions, which thus motivates us to incorporate sentiment into text analytics models. However, the existing sentiment-based machine learning methods present major deficiencies. Based on these observations, we designed an information system with a vector representation and a hybrid deep architecture that simultaneously accounts for sentiment in health-oriented social media.

## MNA-Reason Mining Problem and Approach

## MNA-Reason Mining Problem Formulation

Let ?? denote a set of ?? patients $p _ { i }$ in the online health community. Let $D$ denote a set of drugs $d _ { i }$ used by patients in $P .$ Patient $p _ { i }$ taking drug $d _ { j }$ posts reviews $v _ { i j }$ (integrate all reviews of patient $p _ { i }$ taking drug $d _ { j } )$ about medication use on social media sites. Review $v _ { i j }$ contains ?? sentences $s _ { k }$ Each sentence $s _ { k }$ is denoted as $( w _ { k 1 } , w _ { k 2 } , . . . , w _ { k t } )$ , where $w _ { k t }$ is a word in $s _ { k }$ . If patient $p _ { i }$ taking drug $d _ { j }$ decides to discontinue the medication, this patient would be likely to describe MNA reasons in review $v _ { i j }$ . The MNA reasons of patient $p _ { i }$ taking drug $d _ { j }$ are denoted as $r _ { i j } ^ { 1 } , r _ { i j } ^ { 2 } , \ldots , r _ { i j } ^ { q }$ (?? is the number of MNA reasons). MNA reason $r _ { i j } ^ { k }$ can be a single word $w _ { k } .$ , a multiword phrase $( w _ { k 1 } , w _ { k 2 } , \dots w _ { k m } )$ , or a part of a sentence $( w _ { k 1 } , w _ { k 2 } , \dots w _ { k n } )$

We define the MNA-reason mining problem as follows: in an online health community, we observe a set of patients taking drugs in a certain drug set. The input is social media drug review $v _ { i j }$ for patient $p _ { i }$ taking drug $d _ { j }$ . The objective of the MNA-reason mining problem is two-fold. First, we aim to discover MNA reasons $r _ { i j } ^ { 1 } , r _ { i j } ^ { 2 } , \ldots , r _ { i j } ^ { q }$ for each patient $p _ { i }$ taking a particular drug $d _ { j }$ . Second, we cluster the identified MNA reasons based on their semantic meaning. The output is the MNA-reason types summarizing $r _ { i j } ^ { 1 } , r _ { i j } ^ { 2 } , \ldots , r _ { i j } ^ { q }$ for each drug and patient.

## The Sentiment-Enriched Deep Learning Approach

Consistent with the aspect mining procedures, aspect extraction and aspect clustering, our approach is composed of reason extraction and reason clustering. Reason extraction identifies patients’ self-described MNA reasons in phrases. Reason clustering groups together similar MNA-reason expressions to identify the reason types. The MNA-reason mining process is depicted in Figure 2. Our proposed approach extends the state-of-the-art deep learning model with a novel sentiment-enriched word embedding and hybrid deep learning architecture. Our approach addresses three technical challenges: identifying decision-making based on negative sentiment in long texts, interpreting informal health vocabulary, and extracting sparse MNA-relevant terms from texts.

## MNA-Reason Extraction

## Sentiment-Enriched Word Embedding Layer

Word embedding can represent the semantics of a word by learning from its neighboring words. Hence it can capture the semantic meaning of varied patient vocabulary. For this reason, we build on word embedding when designing our word representation. Patients’ MNA decisions are associated with their expressed sentiment. Therefore, we propose a new representation: sentiment-enriched word embedding. We incorporate a new sentiment aspect to signal expressions relevant to MNA. The sentiment-enriched word embedding represents each word’s sentiment along with the likelihood of the co-occurrence of common words. Figure 3 shows the structure of our sentiment-enriched word embedding.

In contrast to standard word embedding that only learns the semantic context of words (Mikolov et al. 2013a), sentimentenriched word embedding considers both the semantic context and the sentiment of words. Many MNA reasons are associated with negative sentiment. In our dataset, 97% of MNA reasons have negative sentiment, whereas other regular terms have random sentiment. The new sentiment aspect in the sentiment-enriched word embedding effectively distinguishes MNA reasons from other words in similar contexts. For instance, patients may discuss the cost of medications in online drug reviews. The semantic context of the discussions on cost is similar. Thus, they have similar word embedding. The cost of a medication could be an MNA reason, as some patients cannot afford the medication. These patients may express negative sentiment about medications in discussions related to MNA, while other regular discussions about the cost of medications may exhibit neutral sentiment. The combination of learning sentiment and semantic meaning may be able to distinguish MNA reasons from other regular discussions.

Let S be a training sequence $( w _ { 1 } , w _ { 2 } , . . . , w _ { T } )$ . Variable $w _ { i }$ denotes the ??-th word in the sequence. The training objective is to minimize the objective function $L _ { s }$ in Equation (1).

$$
L _ {s} = - \log p \big (w _ {O, c o n t}, w _ {O, s e n t i} \big | w _ {I} \big) = \alpha L _ {c o n t} + (1 - \alpha) L _ {s e n t i}.\tag{1}
$$

Variable $w _ { I }$ is the focal word. Variable $w _ { O , c o n t }$ is the neighboring words of the focal word.

![](/api/attachments/ZUZD2AE9/fulltext/images/4bd7bbdb2ab96a32bb3bbc6b8eb4c9c58eb90996a20f2c7e2defd66041991f98.jpg)  
Figure 2. The Sentiment-Enriched Deep Learning Approach for MNA-Reason Mining

We use a window size of five for the neighboring words, as it is the most commonly used and effective size for social media texts (Baroni et al. 2014; Goldberg and Levy 2014). Variable $w _ { O , s e n t i }$ is the sentiment of the focal word. We design a decreasing function $\frac { 1 } { e ^ { s e n t i } }$ to compute the sentiment,<sup>3</sup> where ?????????? is the sentiment score of the focal word. This decreasing function has a steep slope when a word is negative and a flat slope when a word is positive. Therefore, a unit of change in word sentiment (x-axis) results in a bigger change in the function value (y-axis) on the negative side, while it results in a smaller change in the function value (y-axis) on the positive side. As negative words have a higher probability to indicate MNA reasons, such skew in sentiment distribution could magnify the subtlety in MNA-related words. We leverage VaderSentiment to compute the sentiment score (Hutto and Gilbert 2014), which is attuned to sentiments expressed in social media and could capture the sentiment dependencies among words in phrases (Horne and Adali 2017). We use the sentiment of the focal word instead of the neighboring words, because the sentiment of the neighboring words may drift from that of the focal word. For instance, in the sentence “the drug is too expensive,” “expensive” is the MNA-reason expression of interest. Its neighboring words do not share the same sentiment. Parameter ?? is the weighting factor. Function $L _ { c o n t }$ is the loss of the neighboring words. Function $L _ { s e n t i }$ is the loss of the sentiment. The updating rule of the sentimentenriched word embedding is shown in Equation 2.

$$
\pmb {x} _ {w _ {I}} ^ {(n e w)} = \pmb {x} _ {w _ {I}} ^ {(o l d)} - \eta \big (\alpha \mathrm{E} _ {c o n t, i} + (1 - \alpha) \mathrm{E} _ {s e n t i, i} \big).\tag{2}
$$

$\mathrm { E } _ { c o n t , i }$ is the sum of the output of all words weighted by the prediction error. $\mathrm { E } _ { s e n t i , i }$ is the output of sentiment weighted by the prediction error. With this new updating rule, the sentimentenriched word embedding takes into account the learning errors from both the neighboring words and the sentiment. The derivation of Equation 2 can be found in Appendix Table A2.

We use the Skip-gram model as the base method to devise the sentiment-enriched word embedding, as it performs better than other models (e.g., CBOW) in predicting rare words (Mikolov et al. 2013b). MNA reasons are also sparse expressions. The sentiment-enriched word embedding is generated from the entire corpus. For each unique word in the dataset, all the sentences containing the word are used to learn the likelihood of the focal word’s neighboring words. Each word has one unique vector representation, which is used to represent the focal word across all the occurrences in the corpus. The resulting model obtains an array of vectors with 300 dimensions. We set the dimension to be 300 as it has been successfully tested in multiple deep learning studies (Garten et al. 2015; Ma and Hovy 2016).

In contrast to previous studies, our proposed approach to incorporating sentiment addresses the limitations of prior sentiment-based methods. Our research objective is to determine whether a word in a drug review belongs to an MNA-reason expression, which is different from studies that aim to predict sentiment (Wallace et al. 2014; Labutov and Lipson 2013). In contrast to prior work that directly uses sentiment as a symbolic feature (without learning) (Fu et al. 2012; Abbasi et al. 2018), our proposed method incorporates sentiment into the learning objective that trains a vectorbased representation to represent semantic meaning and sentiment. A sentence on a health social media site could contain many topics beyond MNA (e.g., dietary recommendations, health policies, etc.), because of the long and noisy nature of writing in social media posts. Even if MNA is one of the mentioned topics in a sentence, the sentence-level sentiment is an aggregation of the sentiments of all the topics, many of which are irrelevant to MNA. The sentence-level sentiment does not necessarily align with the sentiment related to MNA. Since existing methods fail to capture the nuanced sentiment related to MNA at the word level (Tang et al. 2014), our approach predicts the semantic meaning and sentiment at the word level. As shown in Figure 3, each word in a sentence is represented as an embedding within the input layer of the model. In contrast to methods that focus on learning syntactic relationships among words (Tang et al. 2014), our proposed method learns the semantic meaning of words, which is more critical for MNA-reason mining. As shown in the output layer in Figure $^ { 3 , }$ the sentiment-enriched word embedding is supervised by the correct prediction of the contextual words and the sentiment of the focal word. Parameters in each dimension of the embedding are computed to approximate the semantic similarity between the focal word and its contextual words to predict the sentiment of the focal word. The learned sentimentenriched word embedding is used to represent each word in the drug review corpus and later to detect MNA reasons.

## Convolutional Layer

The sentiment-enriched word embedding is fed into the convolutional layer. This layer is designed to extract salient features from the 300-dimensional embedding. Relevant information about MNA could be enhanced, thus addressing the sparse MNA-related-information challenge.

The number of filters in this layer is 128. The kernel size is 5. The stride is 1. The padding strategy is “same,” meaning the output has the same length as the input.

## Bidirectional Long Short-Term Memory Layer

To effectively extract sparse MNA-related information and enable sequence learning, we utilize a bidirectional-LSTM deep learning architecture. We use the bidirectional structure because a sentence follows semantic and syntactic rules, so that words in different locations in a sentence may exhibit semantic dependencies regardless of the word order (Crain and Nakayama 1987). This bidirectional structure is capable of capturing such dependencies from both directions.

The input vector is embedded with semantic meaning and sentiment information learned from the corpus but this vector is not customized according to the final learning objective (MNA-reason mining). In our model, we devise an element-wise multiplier $\pmb { \beta }$ in the input vector (Equation 3). This multiplier allows the weight of each dimension of the vector to adjust according to its relevance to MNA reasons. This learnable weight further injects meaningful information about the final task (MNA-reason mining) into the vector. The multiplier also addresses the challenge of sparse MNArelevant terms by strengthening useful information and degrading irrelevant information in the learning process.

$$
\boldsymbol {x} _ {l s t m} ^ {(t)} = \boldsymbol {\beta} \odot \boldsymbol {x} _ {c o n v} ^ {(t)} = \Big (\beta_ {1} x _ {c o n v, 1} ^ {(t)}, \beta_ {2} x _ {c o n v, 2} ^ {(t)}, \dots , \beta_ {3 0 0} x _ {c o n v, 3 0 0} ^ {(t)} \Big).\tag{3}
$$

The $\pmb { \beta }$ is learned through the training process in the LSTM unit. The $\pmb { \beta }$ assigns different weights to different dimensions in the input vector according to its relevance to the learning objective, while other hyperparameters within the LSTM unit assign different weights to different input vectors. Such a difference is facilitated by using different computation: the computation between $\pmb { \beta }$ and $\pmb { x } _ { c o n v } ^ { ( t ) }$ is element-wise multiplication, thus allowing weight adjustments within the input embedding vector. The computation between the hyperparameters in the LSTM unit and $\pmb { x } _ { l s t m } ^ { ( t ) }$ is matrix multiplication, thus enabling weight adjustments on the vector level. The LSTM units learn to decrease the weight when the input $\pmb { x } _ { l s t m } ^ { ( t ) }$ is not relevant to our learning target and increase the weight when $\pmb { x } _ { l s t m } ^ { ( t ) }$ is our target (MNA reasons).

Since the bidirectional structure has two reversed LSTM layers, the output of this step is the concatenation of the forward and backward states. Each forward or backward layer has 128 dimensions, in accordance with prior studies (Chan and Lane 2015; Rao et al. 2015). The optimization method is Adam. The learning rate is 0.1. The dropout rate is 0.2 in the BLSTM layer.

## Conditional Random Field Layer

In order to classify the word type (MNA reason or not) for each word in the input sentence, we designed a CRF layer. The CRF layer also complements the BLSTM layer by considering the dependency between class labels. Given input sequence $( \pmb { o } _ { 1 } , \dots , \pmb { o } _ { T } )$ , we aim to predict the class labels $( s _ { 1 } , \dots , s _ { T } )$ (MNA reason or not). The CRF layer seeks to maximize the following function:

$$
p (s | \boldsymbol {o}, \boldsymbol {w}) = \frac {\exp (\boldsymbol {w} \cdot \Phi (\boldsymbol {o} , s))}{\sum_ {s ^ {\prime}} \exp (\boldsymbol {w} \cdot \Phi (\boldsymbol {o} , s ^ {\prime}))}.\tag{4}
$$

Parameter ?? is the weight vector. Function $\Phi ( \pmb { o } , s )$ is a scoring function that evaluates how well the class label sequence fits the given input sequence. We define the $\Phi ( \pmb { o } , s )$ as:

$$
\Phi (\boldsymbol {o}, s) = \sum_ {t} \boldsymbol {W} _ {s ^ {(t - 1)}, s ^ {(t)}} \cdot \boldsymbol {o} ^ {(t)} + \boldsymbol {b} _ {s ^ {(t - 1)}, s ^ {(t)}}.\tag{5}
$$

Parameters $W _ { s ^ { ( t - 1 ) } , s ^ { ( t ) } }$ and ${ \pmb b } _ { s ^ { ( t - 1 ) } , s ^ { ( t ) } }$ are the weight matrix and bias corresponding to the transition from $\boldsymbol { s } ^ { ( t - 1 ) } \mathrm { ~ t o ~ } \boldsymbol { s } ^ { ( t ) }$ Variable $\mathbf { \pmb { o } } ^ { ( t ) }$ is the output of the BLSTM layer at time step ??.

![](/api/attachments/ZUZD2AE9/fulltext/images/f6d2c9b78acccffb6225e1a22888adec55952285cd4b2ba15e6639e3768ecd39.jpg)  
Figure 3. Sentiment-Enriched Word Embedding

![](/api/attachments/ZUZD2AE9/fulltext/images/3f1b371df2f808cbc52c577bb4a65831c183623155b06e62581600b79eb89bdd.jpg)  
Figure 4. SEDEL Architecture

An illustration of the architecture of SEDEL is shown in Figure 4. In order to ensure that the results will converge without overfitting, we implement a stop mechanism in the deep learning model. The training stop criterion is validation loss. The patience level is 2, meaning the training process will stop if over two consecutive epochs do not show further reduction of validation loss. The formulas of each layer in the architecture can be found in the Appendix (see “Architecture Details of SEDEL”).

## MNA-Reason Clustering

SEDEL extracts reason expressions in texts. The clustering step identifies the types of MNA reasons. As sentimentenriched word embedding represents the semantic meaning of words in patient-generated content, we use the sentimentenriched word embedding as the features of the clustering model. Each unique reason expression extracted in the previous step represents a clustering instance. If an MNAreason expression contains multiple words, the vector of this expression will be generated with an element-wise computation for all the words in it. In the element-wise computation, we average across each dimension of the sentiment-enriched word embedding of those words. This element-wise average for phrase representation has been used in various text mining studies (Mikolov et al. 2013b). Each MNA-reason expression obtains a single vector representation, which is used in MNA-reason clustering. Since a salient number of studies have utilized k-means for aspect clustering, we use k-means as the clustering method to group MNA-reason expressions based on their semantic meanings.

## Empirical Analyses

## Data Preparation

Our research test bed was collected from a leading health IT platform, WebMD, which features drug reviews and medication-taking experiences from large numbers of patients. We collected all the drug reviews posted on this site from January 2005 to October 2016. This dataset comprises 233,325 sentences from 53,180 reviews concerning 180 drugs. To protect user privacy, WebMD does not require a username, email, or any personally identifiable information when users submit reviews, and each review is considered independent. The drug reviews are categorized by drug name and contain retrospective evaluations of drugs that users have taken. Appendix Figure A1 presents an example of a drug review. Figures A3 and A4 show the gender and age distributions of the patients in our dataset, which indicate good representativeness of all patient groups.

Drug reviews on WebMD cover a wide range of topics, including drug effectiveness, satisfaction, adverse events, and more. Some users reveal their nonadherence decisions in their reviews. We filtered the reviews indicating MNA using a BLSTM model and generated 20,977 reviews that we used for MNA-reason extraction and clustering (“Details of Filtering MNA Reviews” in the Appendix details the specifications of the text classification model). Based on these reviews, we randomly selected 4,500 reviews and annotated them for reason extraction model training and evaluation. Five expert annotators with bioinformatics backgrounds independently read the reviews and tagged MNA reasons in five batches. The IOB labeling scheme was used to assign tags for each word in the sentence. Each word was given a label indicating whether it is inside (I), outside (O), or the beginning (B) of an MNAreason expression. Figure 5 shows an example of the annotation for MNA-reason extraction. We labeled “gained” as the beginning of the reason (B), and “too,” “much,” and “weight” as inside of the reason (I). In the annotated dataset, 11.3% of words were MNA reasons.

After we annotated the 4,500 reviews with MNA reasons, we segmented the reviews into sentences with the sentence boundary detection package from NLTK, generating a total of 5,400 sentences.<sup>4</sup> We chose 4,500 sentences as the training set for the reason extraction model, and the remaining 900 sentences were used for testing. This size of training and test sets have been successfully tested in many information systems studies (Abbasi and Chen 2008; Arazy et al. 2016; Zhang et al. 2016). The sixth expert annotator independently annotated the same 4,500 reviews to test inter-annotator reliability. The kappa value is 0.98 for MNA-reason annotation, indicating excellent reliability (Blackman and Koval 2000). The seventh expert annotator reviewed all disagreements and made the final judgment.

## Evaluation of MNA-Reason Mining

We constructed six groups of baseline methods: (1) a discriminative machine learning model—SVM; (2) a sequence learning model—CRF; (3) deep learning models— CNN, RNN, LSTM, and BLSTM; (4) state-of-the-art hybrid networks based on Chiu and Nichols 2016, Lample 2016, and Ma and Hovy 2016; (5) state-of-the-art sentiment methods from Fu et al. 2012, Abbasi et al. 2018, and Tang et al. 2014; and (6) we constructed another three benchmarks— DL\_Senti<sub>1</sub>, DL\_Senti<sub>2</sub>, and DL\_Senti—that share the same architecture as SEDEL but use different approaches to incorporate sentiment in order to test the best approach of incorporating sentiment.<sup>5</sup> The implementation details of these baseline models are shown in the Appendix (see “Description of Baseline Models”).

We adopted common text mining evaluation metrics, precision, recall, and F1 score to assess the performance. Precision assesses how many MNA reasons that the model retrieved are correct. Recall measures how many MNA reasons in the research test bed the model can identify. The F1 score is an integration of precision and recall. In our study, we aimed to extract as many MNA reasons as possible. Extracting more MNA reasons could lead to more complete intervention strategies. A better understanding of MNA and comprehensive interventions could prevent adverse medical consequences caused by MNA and significantly reduce patient mortality and morbidity rates. Therefore, recall is more important than precision for our study.

We evaluated our model on the annotated dataset using 4,500 sentences as the training set and 900 sentences as the test set. The training set contains 9,610 unique word tokens. We used a vocabulary size of 5,000 to train the sentiment-enriched word embedding to capture frequent word tokens.

<table><tr><td>Gained too much weightB I I I</td><td>. So I stopped Abilify .O O O O .</td><td>Medicationnonadherence reason</td></tr></table>

Figure 5. An Example of Annotation

To avoid overfitting, we used 10% of the training set as the validation set to help adjust hyperparameters in each epoch. We repeated the training procedure for each model 20 times and reported the average performance in Table 2. The experiments were performed on an Apple Mac computer, with a 2.7 GHz Intel Core i7 processor, 16 GB of memory, and a Radeon Pro 455 2 GB graphic card.

Our proposed SEDEL model achieved the highest recall (88.48%) and F1 score (88.86%). Our SEDEL model had the most salient advantage in the recall. The recall was 34.88% higher than SVM, 42.18% higher than CRF, 6.53% higher than CNN, 10.53% higher than RNN, 9.42% higher than LSTM, and 6.12% higher than BLSTM. While SEDEL attained the most impressive performance, the training time of SEDEL only increased minimally (0.94 s more than BLSTM). CRF achieved relatively higher precision than SEDEL because it aims to maximize the probability of generating observations. Considering that recall is more important and SEDEL also reached sufficiently high precision, we determined that SEDEL is the best method for MNA-reason mining.

SEDEL improved the state-of-the-art BLSTM in recall by 6.12%. The improved recall enabled SEDEL to extract 1,520 more MNA-reason expressions than BLSTM. These MNA reasons impacted an additional 895 patients in our dataset, accounting for 4.3% patients with MNA intentions. The significant improvement offered by SEDEL has significant implications for healthcare systems. Since MNA results in \$290 billion in preventable annual costs in the U.S. alone, awareness of the MNA reasons for an additional 4.3% of patients could save up to \$12.5 billion in annual costs, assuming a 100% success rate of interventions.

We also compared SEDEL with state-of-the-art hybrid networks (Chiu and Nichols 2016; Lample 2016; Ma and Hovy 2016). SEDEL also outperformed these methods. The superior performance demonstrates the successful design of the sentiment-enriched component, which could boost the performance of state-of-the-art architecture in opinion-based texts.

Further, we compared SEDEL with other models using alternative approaches to incorporate sentiment (mentioned above in the literature review, see Fu et al. 2012; Abbasi et al. 2018; Tang et al. 2014). SEDEL outperformed all the other alternative sentiment-based methods, with an F1 score improvement of 85.14%, 5.89%, and 4.19%, respectively (p < 0.001).

Lastly, we constructed DL\_Senti , DL\_Senti , and DL\_Senti , which incorporate sentiment in different ways. Our SEDEL approach significantly outperformed these three approaches, suggesting that SEDEL is the best approach to incorporate sentiment in the model.

To test the significance of the performance improvement of SEDEL, we repeated the training and testing procedures for each model 20 times and conducted t-tests to compare the performance of SEDEL against baseline models. The results indicate that SEDEL significantly outperforms all the baseline models (p < 0.05) because of its sentiment-enriched word embedding and hybrid architecture. SEDEL is capable of extracting semantically related and low-density MNA reasons. For instance, SEDEL can retrieve semantically related MNA reasons such as “anxious” and “restless,” both of which indicate a potential anxiety disorder caused by the medication. These MNA reasons are associated with negative sentiment, which can be captured by SEDEL to enrich the semantics. SEDEL also retrieved scarce MNA reasons from our research data, such as medication ineffectiveness (0.35% of all MNA reasons) and specific population (0.04% of all MNA reasons), as well as varied forms of MNA reasons.

## Ablation Studies

## Impact of Sentiment-Enriched Word Embedding

Sentiment-enriched word embedding is a major contribution of this study. We tested the impact of this new component by replacing it with a generic word embedding. We also added the sentiment component to other baseline models to test its influence on the baseline models. The performance is shown in Table 3.

The comparison between SEDEL and SEDEL-sentiment (generic word embedding) shows the impact of the sentimentenriched word embedding. The sentiment-enriched component improved recall by 3.84% (p < 0.001) and the F1 score by 2.64% (p < 0.001).

<table><tr><td colspan="5">Table 2. Evaluation of MNA-Reason Mining</td></tr><tr><td>Method</td><td>Precision (%)</td><td>Recall (%)</td><td>F1 Score (%)</td><td>Training time (s)</td></tr><tr><td>SVM</td><td>29.30***</td><td>53.60***</td><td>37.90***</td><td>0.83</td></tr><tr><td>CRF</td><td>94.00***</td><td>46.30***</td><td>62.04***</td><td>19.55</td></tr><tr><td>CNN</td><td>84.97***</td><td>81.95***</td><td>83.40***</td><td>66.34</td></tr><tr><td>RNN</td><td>77.71***</td><td>77.95***</td><td>77.69***</td><td>34.55</td></tr><tr><td>LSTM</td><td>83.06***</td><td>79.06***</td><td>80.93***</td><td>92.76</td></tr><tr><td>BLSTM</td><td>84.80***</td><td>82.36***</td><td>83.49***</td><td>161.15</td></tr><tr><td>Chiu and Nichols (2016)</td><td>85.55</td><td>84.34*</td><td>84.94***</td><td>149.53</td></tr><tr><td>Lample (2016)</td><td>84.93</td><td>80.24*</td><td>82.52*</td><td>155.78</td></tr><tr><td>Ma and Hovy (2016)</td><td>86.15</td><td>83.27***</td><td>84.69***</td><td>162.51</td></tr><tr><td>DL_Senti1</td><td>86.03***</td><td>84.51***</td><td>85.26***</td><td>170.29</td></tr><tr><td>DL_Senti2</td><td>87.95**</td><td>87.28*</td><td>87.61***</td><td>158.37</td></tr><tr><td>DL_Senti3</td><td>83.88***</td><td>84.21***</td><td>84.04***</td><td>165.25</td></tr><tr><td>Fu et al. (2012)</td><td>3.75***</td><td>3.68***</td><td>3.72***</td><td>164.98</td></tr><tr><td>Tang et al. (2014)</td><td>83.59***</td><td>85.77***</td><td>84.67***</td><td>156.38</td></tr><tr><td>Abbasi et al. (2018)</td><td>84.23***</td><td>81.75***</td><td>82.97***</td><td>160.58</td></tr><tr><td>SEDEL (Ours)</td><td>89.25</td><td>88.48</td><td>88.86</td><td>162.09</td></tr></table>

Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

<table><tr><td colspan="4">Table 3. Impact of Sentiment</td></tr><tr><td>Method</td><td>Precision (%)</td><td>Recall (%)</td><td>F1 Score (%)</td></tr><tr><td>SVM</td><td>29.30***</td><td>53.60***</td><td>37.90***</td></tr><tr><td>SVM + Sentiment</td><td>17.22</td><td>76.28</td><td>28.10</td></tr><tr><td>CRF</td><td>94.00***</td><td>46.30***</td><td>62.04***</td></tr><tr><td>CRF + Sentiment</td><td>86.84</td><td>64.71</td><td>74.16</td></tr><tr><td>CNN</td><td>84.97</td><td>81.95</td><td>83.40*</td></tr><tr><td>CNN + Sentiment</td><td>84.64</td><td>82.96</td><td>83.75</td></tr><tr><td>RNN</td><td>77.71</td><td>77.95</td><td>77.69</td></tr><tr><td>RNN + Sentiment</td><td>78.19</td><td>78.26</td><td>78.22</td></tr><tr><td>LSTM</td><td>83.06</td><td>79.06</td><td>80.93*</td></tr><tr><td>LSTM + Sentiment</td><td>82.37</td><td>82.14</td><td>82.16</td></tr><tr><td>BLSTM</td><td>84.80</td><td>82.36</td><td>83.49**</td></tr><tr><td>BLSTM + Sentiment</td><td>86.41</td><td>82.90</td><td>84.60</td></tr><tr><td>Chiu and Nichols (2016)</td><td>85.55*</td><td>84.34</td><td>84.94**</td></tr><tr><td>Chiu and Nichols (2016) + Sentiment</td><td>87.27</td><td>85.65</td><td>86.45</td></tr><tr><td>Lample (2016)</td><td>84.93</td><td>80.24</td><td>82.52</td></tr><tr><td>Lample (2016) + Sentiment</td><td>87.08</td><td>82.88</td><td>84.78</td></tr><tr><td>Ma and Hovy (2016)</td><td>86.15***</td><td>83.27***</td><td>84.69***</td></tr><tr><td>Ma and Hovy (2016) + Sentiment</td><td>87.97</td><td>86.59</td><td>87.27</td></tr><tr><td>SEDEL – Sentiment</td><td>87.86</td><td>84.64***</td><td>86.22***</td></tr><tr><td>SEDEL</td><td>89.25</td><td>88.48</td><td>88.86</td></tr></table>

Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

<table><tr><td colspan="4">Table 4. Using Different Representations</td></tr><tr><td>Method</td><td>Precision (%)</td><td>Recall (%)</td><td>F1 Score (%)</td></tr><tr><td>SentiWordNet</td><td>88.18</td><td>86.64**</td><td>87.39***</td></tr><tr><td>Textblob</td><td>88.39</td><td>87.26</td><td>87.80*</td></tr><tr><td>VaderSentiment</td><td>89.25</td><td>88.48</td><td>88.86</td></tr></table>

Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

Adding sentiment also effectively improved the performance of CRF, CNN, LSTM, and BLSTM. Since sentiment plays a vital role in patient MNA decision-making, our model leverages sentiment to better understand patient MNA decision-making and improve model performance. Our results support this proposition and demonstrate the relevance of sentiment for judgment and decision-making.

The sentiment score of each word in the sentiment-enriched word embedding was computed using VaderSentiment. We also tested two other commonly adopted sentiment methods: SentiWordNet and Textblob. The performance of each method is shown in Table 4. VaderSentiment outperformed other sentiment methods, suggesting successful design choices.

We further compared our sentiment-enriched word embedding with other commonly adopted representation methods. GloVe has achieved good performance in many text mining studies (Pennington et al. 2014). We compared our method with GloVe. Representation richness components, such as POS and suffix features, have also been used to enrich representations (Popov 2016). We added representation richness as an additional feature into the sentiment-enriched word embedding to test its influence. POS features were generated by the NLTK package, and suffix features were the same as those used in SVM. We designed two approaches to incorporate representation richness: single-view and multi-view. The single-view model concatenates the sentiment-enriched word embedding and representation richness features. The multiview model has two separate branches that process sentimentenriched word embedding and representation richness independently. We replaced the representation with Glove and two other representation richness methods and reported the results in Table 5. Sentiment-enriched word embedding outperformed all other representations, indicating successful representation designs.

## Impact of Convolutional Layer

SEDEL utilizes the convolutional layer to extract salient local features. We removed this layer to test its influence; results are shown in Table 6. The convolutional layer improved recall by 5.6% (p < 0.05) and the F1 score by 4.08% (p < 0.05). This improvement shows the successful design of the convolutional layer, which addresses the challenge of sparse MNA-related information.

## Impact of BLSTM Layer

The BLSTM layer is utilized in SEDEL for sequence learning. We illustrate the individual effect of the BLSTM in Table 7.

The BLSTM layer plays a vital role in the SEDEL model, and removing this layer significantly hampered precision, recall, and the F1 score. We also devised a $\pmb { \beta }$ parameter to adjust the input to the BLSTM layer. Table 8 shows its influence and indicates that the $\pmb { \beta }$ parameter significantly improved all three metrics.

## Impact of CRF Layer

The SEDEL model utilizes the CRF layer as the classifier. We tested its effectiveness by replacing it with other classifiers such as the Softmax classifier. Table 9 presents the results and shows that the CRF layer significantly improved recall (2.83% increase) and the F1 score (2.41% increase).

## Adding the Attention Mechanism

The attention mechanism was recently invented to capture distant word correlations in long sentences. We tested the additive attention mechanism in SEDEL (on top of the BLSTM layer). The architecture of the attention-based SEDEL is shown in Appendix Figure A4. As shown in Table 10, the performance of attention-based SEDEL was inferior to that of SEDEL. Attention mechanisms are used to address the long-term dependency issue in deep learning models. In our data, irrelevant topics may appear when considering fardistant dependencies, meaning that the benefit of attention is not significant. Therefore, we did not include the attention mechanism in our model.

## MNA-Reason Clustering

SEDEL identified 24,832 MNA-reason expressions from the entire research data. These reason expressions are the actual phrases that patients used in health social media posts. We grouped similar reason expressions using k-means to interpret reason types. We used the Calinski-Harabaz index, a commonly adopted clustering evaluation measurement, to help identify the number of clusters (Maulik and Bandyopadhyay 2002). The Calinksi-Harabaz index is defined as the ratio of the between-cluster dispersion mean and the within-cluster dispersion. Clustering results should ideally have a reasonably high Calinski-Harabaz index. As shown in Appendix Table A3, the Calinski-Harabaz index monotonously decreases as the cluster number increases because MNA reasons are already closely related, although they differ in medical practice. To identify the optimal number of clusters, a medical expert panel, including a pharmacist, a medical doctor, and a bioinformatics researcher, examined the clusters for medical relevance.

<table><tr><td colspan="4">Table 5. Using Different Representations</td></tr><tr><td>Method</td><td>Precision (%)</td><td>Recall (%)</td><td>F1 Score (%)</td></tr><tr><td>Glove</td><td>87.86</td><td>85.41**</td><td>86.56***</td></tr><tr><td>SEDEL + Representation Richness (Single View)</td><td>87.31*</td><td>87.45</td><td>87.32***</td></tr><tr><td>SEDEL + Representation Richness (Multi View)</td><td>84.72*</td><td>85.83*</td><td>85.15**</td></tr><tr><td>SEDEL</td><td>89.25</td><td>88.48</td><td>88.86</td></tr></table>

Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

<table><tr><td colspan="4">Table 6. Impact of Convolutional Layer</td></tr><tr><td>Method</td><td>Precision</td><td>Recall</td><td>F1 score</td></tr><tr><td>SEDEL: Convolution</td><td>87.08%</td><td>82.88%*</td><td>84.78%*</td></tr><tr><td>SEDEL</td><td>89.25%</td><td>88.48%</td><td>88.86%</td></tr></table>

Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

<table><tr><td colspan="4">Table 7. Impact of BLSTM Layer</td></tr><tr><td>Method</td><td>Precision</td><td>Recall</td><td>F1 score</td></tr><tr><td>SEDEL: BLSTM</td><td>14.23%***</td><td>36.63%***</td><td>13.72%***</td></tr><tr><td>SEDEL</td><td>89.25%</td><td>88.48%</td><td>88.86%</td></tr></table>

Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

<table><tr><td colspan="4">Table 8. Impact of Beta</td></tr><tr><td>Method</td><td>Precision</td><td>Recall</td><td>F1 score</td></tr><tr><td>SEDEL: Beta</td><td>85.91%***</td><td>81.26%***</td><td>83.47%***</td></tr><tr><td>SEDEL</td><td>89.25%</td><td>88.48%</td><td>88.86%</td></tr></table>

Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

<table><tr><td colspan="4">Table 9. Impact of CRF Layer</td></tr><tr><td>Method</td><td>Precision</td><td>Recall</td><td>F1 score</td></tr><tr><td>SEDE: CRF</td><td>87.27%</td><td>85.65%*</td><td>86.45%***</td></tr><tr><td>SEDEL</td><td>89.25%</td><td>88.48%</td><td>88.86%</td></tr></table>

Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

<table><tr><td colspan="4">Table 10. Influence of Attention Mechanism</td></tr><tr><td>Method</td><td>Precision</td><td>Recall</td><td>F1 score</td></tr><tr><td>SEDEL + Attention</td><td>88.57%</td><td>86.92%*</td><td>87.71%***</td></tr><tr><td>SEDEL</td><td>89.25%</td><td>88.48%</td><td>88.86%</td></tr></table>

Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

The bioinformatics researcher first interpreted the content in nine clusters and labeled them into nine types of MNA reasons,<sup>6</sup> presented in Table 11. The medical expert panel discussed and confirmed the nine types of MNA reasons. To further evaluate the reliability of the nine clusters, an independent pharmacist manually read a random sample of 400 MNA reasons and labeled the reason types. Among these 400 manually labeled reasons, 346 (86.5%) shared the same reason type, as labeled by the clustering model, indicating good reliability.

The results offer valuable insight into patients’ intentional medication nonadherence behavior. Adverse drug events are the most common type of MNA reason. Not only have adverse drug events resulted in medical injuries, our results show that they also significantly affect patients’ adherence levels and thus indirectly hamper disease management. Healthcare providers and pharmaceutical companies should be aware of major adverse drug events associated with nonadherence and provide timely alternatives.

Apart from adverse drug events, we identified other common types of reasons, including drug switching, low health literacy, high cost, complex medication plan, and medication ineffectiveness, which are consistent with the findings of prior survey studies. In addition to these known reasons, our method also unveiled new reasons.

<table><tr><td colspan="4">Table 11. Types of Medication Nonadherence Reasons</td></tr><tr><td>Reason type</td><td>Description</td><td>Percentage</td><td>Examples</td></tr><tr><td>Adverse event</td><td>The medication has adverse events or leads to complications.</td><td>56.76%</td><td>It caused a rash on my face. Need to stop.</td></tr><tr><td>Drug switching</td><td>The patient switches to other medications by his/herself.</td><td>15.21%</td><td>Stopping Abilify. Switching to Geodon.</td></tr><tr><td>Complex medication plan</td><td>The medication regimen is complicated. The patient does not like the complicated procedure or forgets to take the medication.</td><td>13.98%</td><td>It&#x27;s so annoying to take this drug three times a day. I&#x27;m not gonna do it.</td></tr><tr><td>Social influence</td><td>The patient stops the medication because his/her peers/caregivers/friends encourage him/her to stop.</td><td>7.67%</td><td>My mom told me that I should quit this drug.</td></tr><tr><td>Cost prohibitive for patient</td><td>The price of the drug is too high, or insurance does not cover it. The patient cannot afford it.</td><td>0.93%</td><td>I can&#x27;t afford this expensive drug anymore.</td></tr><tr><td>Medication ineffectiveness</td><td>The medication is ineffective, so the patient stops it.</td><td>0.09%</td><td>The drug does not help at all! I&#x27;m not taking it.</td></tr><tr><td>Low health literacy</td><td>The patient discontinues the medication because of low health literacy.</td><td>0.04%</td><td>They give me too much of it! Don&#x27;t want to risk my life.</td></tr><tr><td>Specific population</td><td>The patient stops the medication because he/she is pregnant/is a child/has liver disease and more.</td><td>0.02%</td><td>I&#x27;m pregnant and had to stop.</td></tr><tr><td>Others</td><td>Others</td><td>5.30%</td><td>This is absolutely a nightmare! Stop and get better!</td></tr></table>

The MNA reasons of social influence and specific populations have not been noted in prior survey studies. These additional findings may be attributed to the unique characteristics of social media, especially the impact of social influence on patients in this context. Also, some previously identified MNA reasons, such as poor communication between providers and patients, did not appear in our findings, likely because WebMD recommends that patients emphasize issues encountered with drugs rather than health providers in their reviews.

We further evaluated the proposed sentiment-enriched component on the reason-type level. SEDEL retrieves MNA reasons but does not categorize reason types. The clusterlevel extraction method was unsupervised. Since there was not enough ground truth to compute precision and recall for all the reasons at the reason type level, we used accuracy to assess model performance. The accuracy for a particular reason type is calculated as follows:

## ????????????????(???????????? ????????<sub>??</sub>) =

???????????? ???? ?????????????? ?????????????????? ???? ?????????? ??ℎ???? ???????????? ???? ???????????? ???????? ???????????? ???? ?????????????? ???? ???????????? ????????

(6)

Table 12 shows the effectiveness of the sentiment-enriched component. The sentiment-enriched component helps improve performance for most of the reason types. Adverse events, drug switching, high costs, and complex medication plans were associated with negative sentiment. Therefore, sentiment information could improve the performance of MNA-reason mining. Low health literacy and social influence reflect patients’ attitudes. Adding sentiment could also help retrieve these reasons. Performance for the high-cost reason type was low because the percentage of this reason type was itself very low (0.93%). Misclassifying just one instance could skew the performance metrics.

## Error Analysis

We selected false positive and false negative expressions from the test dataset. False positive expressions are irrelevant words that the model misclassified as MNA reasons. False negative expressions are MNA reasons that the model misclassified as irrelevant words. Of the 13,765 words in the test dataset, 218 of them were false positives (1.58%), and 111 were false negatives (0.81%). We categorized the likely sources of errors and present them in Table 13.

SEDEL extracted 1,520 more MNA-reason expressions than BLSTM. Examples include: “anxiety is worse,” “body just felt awful,” “extremely worried about being addicted to it,” “moods worsened,” and “scary dreams.” Such expressions not only suggest MNA but also signal negative sentiment. Since SEDEL is capable of learning sentiments associated with MNA decisions, SEDEL has a higher recall than other baseline models.

<table><tr><td colspan="4">Table 12. The Effectiveness of the Sentiment-Enriched Component by Reason Type</td></tr><tr><td>Reason Type</td><td>BLSTM (%)</td><td>SEDEL (%)</td><td>Reason percentage</td></tr><tr><td>Adverse event</td><td>92.51</td><td>93.87</td><td>56.76%</td></tr><tr><td>Drug switching</td><td>91.20</td><td>93.96</td><td>15.21%</td></tr><tr><td>Complex medication plan</td><td>99.06</td><td>99.08</td><td>13.98%</td></tr><tr><td>Social influence</td><td>91.53</td><td>94.12</td><td>7.67%</td></tr><tr><td>Cost prohibitive for patient</td><td>9.77</td><td>9.95</td><td>0.93%</td></tr><tr><td>Medication ineffectiveness</td><td>99.73</td><td>98.57</td><td>0.09%</td></tr><tr><td>Low health literacy</td><td>97.75</td><td>99.41</td><td>0.04%</td></tr><tr><td>Specific population</td><td>50.00</td><td>100.00</td><td>13.98%</td></tr><tr><td>Others</td><td>94.73</td><td>95.56</td><td>7.67%</td></tr></table>

<table><tr><td colspan="4">Table 13. Error Analysis</td></tr><tr><td colspan="4">False positive</td></tr><tr><td>Source</td><td>Percentage</td><td>Example</td><td>Description</td></tr><tr><td>Modifier for reason entities</td><td>67.43%</td><td>Lots of</td><td>The modifier “lots of” before “headache” is also classified as nonadherence reason.</td></tr><tr><td>Nonreason adverse event</td><td>17.43%</td><td>Anxiety</td><td>Anxiety is an indication of a drug.</td></tr><tr><td>Prepositions and conjunctions</td><td>6.42%</td><td>Of</td><td>“of” has no meaning.</td></tr><tr><td>Others</td><td>8.72%</td><td>Take</td><td>Not relevant.</td></tr><tr><td colspan="4">False negative</td></tr><tr><td>Source</td><td>Percentage</td><td>Example</td><td>Description</td></tr><tr><td>Misclassify partial reason</td><td>35.14%</td><td>Headache and nausea</td><td>Retrieves “headache” but misses “nausea.”</td></tr><tr><td>Lack of context</td><td>32.34%</td><td>I have headache and anxiety</td><td>Context words are “I have” and “and”: little information.</td></tr><tr><td>Vague</td><td>20.72%</td><td>Noise</td><td>Noise is not due to a medication.</td></tr><tr><td>Few training instances</td><td>9.91%</td><td>Insurance</td><td>“insurance” appeared just once.</td></tr><tr><td>Fail to identify drug names</td><td>1.89%</td><td>Abilify</td><td>Patients want to switch to Abilify, but the model fails to identify “Abilify.”</td></tr></table>

## Heterogeneity of MNA Reasons across Drugs and Patients

Medication nonadherence is a complex medical issue with MNA reasons varying across patients and drugs. Table 14 shows that MNA reasons differ across different drug classes. The bold numbers are the highest percentage in each column. For instance, treatments for arthritis patients include nonsteroidal anti-inflammatory drugs, steroids, analgesics, narcotics, and immunosuppressive drugs. Given that this patient group must take multiple medications for an extended period of time, complex medication plans represent the leading MNA reason for arthritis patients (3.35%). In contrast, since there is a wide variety of available diabetes medications, drug switching is prevalent among diabetes patients (10.59%), who often seek better treatment options.

MNA reasons are also diverse for individual drugs. Appendix Table A5 lists the top discontinued drugs for each reason. Varied MNA reasons across drug classes and individual drugs shed light on drug-specific medication nonadherence. For instance, Opana is an opioid agonist that treats moderate to severe pain. It has a high risk of addiction and dependence.

The most common reason for discontinuing Opana is drug switching among patients seeking to avoid drug dependence and other severe outcomes. Vyvanse is a central nervous system stimulant to treat attention deficit hyperactivity disorder (ADHD), but it can also produce increased energy, euphoria, and appetite suppression. Since many people abuse Vyvanse for recreational, academic, or weight-loss reasons, Vyvanse users often discontinue the medication due to social influence from family members, friends, and caregivers. Valtrex is an enhanced antiviral drug. It is more effective than many alternatives but it is expensive. The cost per dose for Valtrex ranges from \$12.3 to \$15.6. A 30-day course of Valtrex costs between \$370 to \$470, almost four times as much as competing drugs such as Zovirax and Trifluridine. Patients may thus discontinue Valtrex due to its high cost and low level of insurance coverage.

Once MNA reasons are detected for individual drugs, key stakeholders can infer targeted intervention strategies to improve adherence and disease management for different drugs. For instance, for medications that are costly, providers should consider prescribing the generic form of the medications to achieve optimal treatment effects.

<table><tr><td colspan="10">Table 14. Differed Medication Nonadherence Reasons by Drug Class</td></tr><tr><td>Drug class</td><td>Adverse event</td><td>Drug switching</td><td>Low health literacy</td><td>Social influence</td><td>Cost prohibitive</td><td>Complex medication plan</td><td>Medication ineffectiveness</td><td>Specific population</td><td>Others</td></tr><tr><td>Diabetes</td><td>59.25%</td><td>10.59%</td><td>12.66%</td><td>2.22%</td><td>0.49%</td><td>2.18%</td><td>0.81%</td><td>0.02%</td><td>11.78%</td></tr><tr><td>High blood pressure</td><td>64.24%</td><td>8.41%</td><td>9.45%</td><td>1.87%</td><td>1.56%</td><td>2.33%</td><td>0.99%</td><td>0.01%</td><td>11.13%</td></tr><tr><td>Infectious</td><td>64.76%</td><td>7.17%</td><td>8.48%</td><td>2.26%</td><td>0.44%</td><td>2.45%</td><td>1.11%</td><td>0.04%</td><td>13.29%</td></tr><tr><td>Mental</td><td>57.83%</td><td>7.26%</td><td>10.79%</td><td>2.42%</td><td>0.68%</td><td>3.25%</td><td>1.62%</td><td>0.05%</td><td>16.10%</td></tr><tr><td>Respiratory</td><td>60.65%</td><td>7.18%</td><td>10.77%</td><td>2.52%</td><td>0.90%</td><td>2.88%</td><td>1.07%</td><td>0.04%</td><td>13.99%</td></tr><tr><td>Allergic</td><td>58.09%</td><td>10.15%</td><td>8.65%</td><td>1.65%</td><td>2.03%</td><td>3.08%</td><td>2.23%</td><td>0.09%</td><td>14.02%</td></tr><tr><td>Arthritis</td><td>59.75%</td><td>8.21%</td><td>9.54%</td><td>2.36%</td><td>0.69%</td><td>3.35%</td><td>1.63%</td><td>0.02%</td><td>14.46%</td></tr><tr><td>Seizure</td><td>60.32%</td><td>7.25%</td><td>10.04%</td><td>2.50%</td><td>0.91%</td><td>2.98%</td><td>1.33%</td><td>0.05%</td><td>14.63%</td></tr><tr><td>Cancer</td><td>62.16%</td><td>6.68%</td><td>10.43%</td><td>2.40%</td><td>0.53%</td><td>3.01%</td><td>1.04%</td><td>0.06%</td><td>13.69%</td></tr><tr><td>Heart</td><td>62.58%</td><td>6.55%</td><td>10.37%</td><td>2.21%</td><td>0.99%</td><td>3.05%</td><td>1.05%</td><td>0.04%</td><td>13.17%</td></tr><tr><td>Kidney</td><td>63.76%</td><td>7.00%</td><td>9.63%</td><td>2.26%</td><td>0.40%</td><td>2.92%</td><td>1.28%</td><td>0.05%</td><td>12.70%</td></tr></table>

<table><tr><td colspan="10">Table 15. Different Medication Nonadherence Reasons by Gender</td></tr><tr><td>Gender</td><td>Adverse event</td><td>Drug switching</td><td>Low health literacy</td><td>Social influence</td><td>Cost prohibitive</td><td>Complex medication plan</td><td>Medication ineffectiveness</td><td>Specific population</td><td>Others</td></tr><tr><td>Female</td><td>60.50%</td><td>7.28%</td><td>14.74%</td><td>2.33%</td><td>0.75%</td><td>3.02%</td><td>1.39%</td><td>0.05%</td><td>9.94%</td></tr><tr><td>Male</td><td>59.42%</td><td>7.93%</td><td>13.93%</td><td>2.30%</td><td>0.82%</td><td>3.23%</td><td>1.49%</td><td>0.00%</td><td>10.88%</td></tr><tr><td>Unknown</td><td>60.77%</td><td>7.23%</td><td>14.46%</td><td>2.48%</td><td>0.72%</td><td>3.24%</td><td>1.35%</td><td>0.00%</td><td>9.76%</td></tr></table>

<table><tr><td colspan="10">Table 16. Different Medication Nonadherence Reasons by Age</td></tr><tr><td>Age</td><td>Adverse event</td><td>Drug switching</td><td>Low health literacy</td><td>Social influence</td><td>Cost prohibitive</td><td>Complex medication plan</td><td>Medication ineffectiveness</td><td>Specific population</td><td>Others</td></tr><tr><td>0-2</td><td>54.62%</td><td>10.08%</td><td>20.17%</td><td>7.56%</td><td>0.00%</td><td>0.00%</td><td>5.04%</td><td>2.52%</td><td>0.00%</td></tr><tr><td>3-6</td><td>58.34%</td><td>6.34%</td><td>20.20%</td><td>7.41%</td><td>0.00%</td><td>0.29%</td><td>6.05%</td><td>1.27%</td><td>0.10%</td></tr><tr><td>7-12</td><td>58.44%</td><td>7.99%</td><td>18.69%</td><td>8.12%</td><td>0.05%</td><td>0.36%</td><td>4.54%</td><td>1.81%</td><td>0.00%</td></tr><tr><td>13-18</td><td>64.46%</td><td>7.42%</td><td>19.88%</td><td>2.71%</td><td>0.04%</td><td>0.28%</td><td>3.26%</td><td>1.94%</td><td>0.00%</td></tr><tr><td>19-24</td><td>66.27%</td><td>7.38%</td><td>18.98%</td><td>1.61%</td><td>0.10%</td><td>0.47%</td><td>3.19%</td><td>1.90%</td><td>0.10%</td></tr><tr><td>25-34</td><td>66.27%</td><td>7.46%</td><td>17.95%</td><td>2.20%</td><td>0.12%</td><td>0.51%</td><td>3.52%</td><td>1.84%</td><td>0.13%</td></tr><tr><td>35-44</td><td>66.20%</td><td>8.22%</td><td>16.98%</td><td>2.69%</td><td>0.15%</td><td>0.63%</td><td>3.42%</td><td>1.67%</td><td>0.05%</td></tr><tr><td>45-54</td><td>67.52%</td><td>8.44%</td><td>15.73%</td><td>2.51%</td><td>0.22%</td><td>0.68%</td><td>3.38%</td><td>1.51%</td><td>0.01%</td></tr><tr><td>55-64</td><td>58.95%</td><td>7.73%</td><td>12.28%</td><td>2.41%</td><td>0.26%</td><td>0.68%</td><td>2.98%</td><td>1.15%</td><td>0.00%</td></tr><tr><td>65-74</td><td>69.35%</td><td>9.29%</td><td>12.96%</td><td>2.90%</td><td>0.27%</td><td>0.88%</td><td>3.15%</td><td>1.20%</td><td>0.00%</td></tr><tr><td>Unknown</td><td>67.47%</td><td>8.58%</td><td>14.33%</td><td>3.37%</td><td>0.23%</td><td>0.96%</td><td>3.87%</td><td>1.20%</td><td>0.00%</td></tr></table>

Payers should also conduct a cost-benefit analysis considering the potential cost of MNA. For medications that have adverse effects, providers should communicate with patients to improve patient health literacy, identify medication ineffectiveness and severe adverse events in a timely manner, and conduct necessary interventions.

MNA reasons also vary among different patient groups. Table 15 shows distinct MNA reasons for different gender groups, and Table 16 shows varied MNA reasons for different age groups. The bold numbers represent the highest percentage in each column. As shown in Table 15, female patients are more likely to discontinue medications because of constrained use among specific populations (i.e., pregnant and breastfeeding women). Male patients are more likely to discontinue medications because of drug switching and cost. The MNA reasons presented show significant variance among different age groups. For instance, patients aged 65 and over are more likely to discontinue medications due to adverse events, probably because senior citizens are more likely to suffer from multiple chronic diseases and weaker immune systems. Patients aged 0-2 are more likely to stop medications because of a specific population reason, namely their parents stop giving them medications because of age-related concerns.

MNA reasons are not static. The type and proportion of MNA reasons fluctuate over time. Figure 6 shows the trends related to adverse-event and medication ineffectiveness reasons. The blue line is the trend of the average number of adverse event reasons per drug review (the number of adverse event reasons monthly divided by the number of reviews monthly). The gray line is the trend of the average number of medication ineffectiveness reasons per drug review. The dashed lines are the regressed trending lines. While adverse event reasons have been rising steadily over the years, medication ineffectiveness reasons have been increasingly fluctuating.

## Discussion

## Relevance to IS Literature

In line with design science research guidelines (Hevner et al. 2004), our study identifies a relevant health IT problem: MNA-reason mining. We demonstrate that no adequate solutions exist in the prior literature. In the spirit of social media-based IS research (Abbasi et al. 2018; Karahanna et al. 2018; Kitchens et al. 2018; Zhang et al. 2016), we developed a novel information system that mines health social media to understand patient decision-making about MNA. We conducted comprehensive evaluations of the information system we developed and assessed its utility. In addition, we articulated how the extracted patient MNA reasons can add value to existing knowledge about MNA and lead to better and more effective interventions.

This study also relates to computational design science research (Rai 2017). This paradigm emphasizes an “interdisciplinary approach in developing novel data representations, computational algorithms, business intelligence, and analytics methods” (Rai 2017). Our study develops an interdisciplinary approach that involves a novel computational algorithm and an analytical solution to a major healthcare problem, which thus offers great potential for generating IS research with significant societal impacts. Such impacts include advancing the understanding of medication nonadherence issues from the patient’s perspective and identifying useful information within multiscale biomedical data to support healthcare delivery.

## Methodological Implications

In this study, we formulate the MNA-reason mining problem. The MNA-reason mining problem can be generalized as seeking to understand the reason underlying various types of decision-making, such as consumer retention, technology adoption, and project investment crowdfunding. To approach this problem, we developed SEDEL to process patient-generated medication experiences and innovatively incorporate sentiment into wordembedding representations. Both hybrid deep learning architecture and sentiment-enriched word embedding contribute to the improved MNA- reason mining performance of the SEDEL model, which can identify relevant information from a large amount of user-generated content with high performance.

Sentiment-enriched word embedding represents the varied vocabularies in user-generated content and sentiments that can impact decision-making. Incorporating sentiment in word embedding improves reason-mining performance. Indeed, such a sentiment-enriched approach is not restricted to the MNA domain. Opinion-based text has been the focus of a wide range of text analytics applications. Applying existing sentiment-insensitive models in those domains, however, has failed to capture the nuances of human emotion. Our approach serves as a domain-independent tool to solve the common challenge that prior methods have faced regarding reason mining in opinion-based texts. Our proposed hybrid CNN-BLSTM-CRF architecture further maximizes the advantages of sentiment-enriched word embedding via hyperparameter fine-tuning, dropout, and regularization mechanisms. This architecture contributes to information retrieval tasks in reason mining. SEDEL is capable of enhancing the unique emotions expressed in texts and accurately identifying the user decision-making associated with those emotions. Beyond MNA, SEDEL could contribute to the understanding of consumer decisionmaking in many other opinion-based contexts, including healthcare, online reviews, crowdfunding, video games, mobile apps, and more. Table 17 shows the domains, the opinion-based data that can be utilized, and the decisionmaking that can be identified by SEDEL.

## Practical Implications

Patients’ health beliefs, health literacy, and knowledge about healthcare regimens play a significant role in medication adherence. The availability of patient MNA reasons not only offers patients social and informational support but can also empower them to communicate more intensively with their physicians. Such information can indirectly benefit patients by improving other stakeholders’ awareness of the elements that are crucial to patients’ adherence.

Nonadherence may complicate healthcare providers’ clinical decision-making because they assume that their patients have taken the prescribed medications, which can lead to inappropriate medication and/or dosage changes and result in complications and negative health outcomes.

![](/api/attachments/ZUZD2AE9/fulltext/images/13a659cd5cf074d16278452e9f1052ea83236413f62fd82f605fbab91e40ceed.jpg)

Figure 6. Medication Nonadherence Reasons Vary Over Time

<table><tr><td colspan="3">Table 17. Methodological Implications for Other Information Systems Research</td></tr><tr><td>Domain</td><td>Data</td><td>Implications of using SEDEL</td></tr><tr><td>Healthcare</td><td>Health social media</td><td>Extract reasons for medication nonadherence</td></tr><tr><td>Online reviews</td><td>Product review</td><td>Extract reasons for purchasing products</td></tr><tr><td>Crowdfunding</td><td>Crowdfunding project review</td><td>Extract reasons for investing in crowdfunding projects</td></tr><tr><td>Video games</td><td>Game review</td><td>Extract reasons for playing/giving up video games</td></tr><tr><td>Mobile apps</td><td>Mobile app review</td><td>Extract reasons for adopting mobile apps</td></tr></table>

Likewise, patients may experience negative health consequences or withdrawal effects due to medication nonadherence. Our findings offer healthcare providers a better understanding of key factors leading to nonadherence, which could facilitate more empathic communication with patients, improve patient education, and encourage better participation from patients regarding decisions about their health.

Hospitals could implement our method in their electronic health record systems. Since social media sites offer streaming data that relate to MNA, our method can collect data in real-time and offer timely analysis of potential MNA reasons. For health providers prescribing a medication, our method could display potential MNA reasons for this medication for specific patient groups. Our method could help hospitals take proactive intervention strategies to prevent negative consequences.

The pharmaceutical industry loses tens of billions of dollars in worldwide sales each year due to medication nonadherence. A significant percentage of patients decide not to refill prescriptions because they fail to respond to the medications as expected or experience unpleasant or serious side effects. Drug companies are now interested in identifying drug nonrespondents and severe adverse drug events during the postmarketing phase. For instance, GlaxoSmithKline and Merck have turned to social media to allow patients to voice their concerns and opinions about their products (Harding 2015). Our findings provide comprehensive insights for drug companies seeking to understand the underlying issues related to their products and invite further research about problems such as drug ineffectiveness and serious adverse drug events.

Insurance plans can also encourage or discourage adherence. Patients with high-deductible plans are more likely to be nonadherent because they shoulder a greater portion of the cost. In contrast, value-based insurance design may encourage adherence by reducing or eliminating copayments and deductibles. Understanding nonadherence reasons such as high cost and negative consequences can help insurers make better decisions when designing their health plans.

Our findings also offer opportunities for developers. While mobile apps designed to remind patients to take pills can address the MNA reason of forgetfulness by sending mobile notifications, feature designs could address other nonadherence reasons. For instance, social influence is a new finding presented by this study, which could also be utilized to improve adherence. Pill reminder apps could design social interaction features that allow users to invite friends, peers, and caregivers on the app to motivate each other to improve adherence.

## Limitations and Future Directions

Our study has several limitations. First, in rare cases on WebMD, users can rate a medication that their parents or children use. Although most of the drug reviews appear to be genuine, it is possible that our data exhibits some false informers and personal biases. However, while such noise likely does not influence the categories of MNA reasons, which are evaluated by medical experts, false information and collective biases may affect the distribution of reason types for a drug. To minimize potential biases, we followed Ruths and Pfeffer’s (2014) guidelines (see “Social Media Biases” in the Appendix) to carefully examine the biases in order to avoid false conclusions, and compared our proposed method with benchmarks using the same data. Future research could extend the scope of analyses to other major platforms such as PatientsLikeMe and Drugs.com in order to mitigate the potential influence of biases and false information. Second, not all patients share their opinions on social media sites. This issue is minimized because the social media user base is significantly larger than the patient cohorts of surveys used in previous studies. Our research data also represent a diverse range of gender and age groups. These advantages of the social media approach effectively complement survey approaches in terms of data representativeness. Nevertheless, MNA is a rather complicated behavior, and no single approach is sufficient to reveal the complete scope of this problem. A combination of the social media approach and the survey approach could provide a more comprehensive understanding of this issue. Third, although our approach is a generalizable framework to understand individuals’ decisionmaking, we did not test the efficacy of our approach in other contexts. To extend this line of research, future studies could use this framework to understand reasons for consumer retention, technology adoption, crowdfunding project investment, and more.

## Conclusion

MNA exacerbates the health conditions of patients. Our research objective was to understand the reasons for MNA. We designed a sentiment-enriched deep learning approach to collect data from a health social media site and extract MNA reasons. Consistent with design science research methodology, we performed a series of empirical analyses to rigorously test the components of our framework and compare it with state-of-the-art methods. Evaluation results show that SEDEL outperformed all the baseline models. Our proposed MNA detection framework can be utilized by various studies to extract information in the text. Some of the MNA reasons detected by our method have not been noted by previous studies, which further demonstrates the value of health social media data for understanding MNA. Our findings have direct implications for stakeholders seeking to understand patients perspectives and thoughts about medications. Knowledge about why individual patients do not adhere to specific medication regimens can be used to design proactive measures and early interventions that can mitigate the harmful outcomes caused by MNA.

## Acknowledgments

This work was supported in part by the National Key Research and Development Program of China under Grant 2020AAA0103405, the National Natural Science Foundation of China under Grants 71621002 and 62071467, as well as the Strategic Priority Research Program of the Chinese Academy of Sciences under Grant XDA27030100.

## References

Abbasi, A., Albrecht, C., Vance, A., and Hansen, J. 2012. “Metafraud: A Meta-Learning Framework for Detecting Financial Fraud,” MIS Quarterly (36:4), pp. 1293-1327.

Abbasi, A., and Chen, H. 2008. “CyberGate: A Design Framework and System for Text Analysis of Computer-Mediated Communication,” MIS Quarterly (32:4), pp. 811-837.

Abbasi, A., Zhang, Z., Zimbra, D., Chen, H., and Nunamaker, J. F. 2010. “Detecting Fake Websites: The Contribution Of Statistical Learning Theory,” MIS Quarterly (34:3), pp. 435- 461.

Abbasi, A., Zhou, Y., Deng, S., and Zhang, P. 2018. “Text analytics to support sense-making in social media: A language-action perspective,” MIS Quarterly (42:2), pp. 427-464.

Aczon, M., Ledbetter, D., Ho, L., Gunny, A., Flynn, A., Williams, J., and Wetzel, R. 2017. “Dynamic Mortality Risk Predictions in Pediatric Critical Care Using Recurrent Neural Networks,” arXiv (1701.06675).

Arazy, O., Daxenberger, J., Lifshitz-Assaf, H., Nov, O., and Gurevych, I. 2016. “Turbulent Stability of Emergent Roles: The Dualistic Nature of Self-Organizing Knowledge Coproduction,” Information Systems Research (27:4), pp. 792- 812.

Asif Ekbal, S. B. 2010. “Named Entity Recognition Using Support Vector Machine: A Language Independent Approach,” International Journal of Electrical, Computer, and Systems Engineering (4:2), pp. 155-170.

Baesens, B., Bapna, R., Marsden, J. R., Vanthienen, J., and Zhao, J. L. 2014. “Transformational Issues of Big Data and Analytics in Networked Business,” MIS Quarterly (38:2), pp. 629-631.

Bardhan, I., Chen, H., and Karahanna, E. 2017. “The Role of Information Systems and Analytics in Chronic Disease Prevention and Management,” MIS Quarterly, (41:1), pp. 333- 334.

Baroni, M., Dinu, G., and Kruszewski, G. 2014. “Don’t Count, Predict! A Systematic Comparison of Context-Counting vs. Context-Predicting Semantic Vectors,” in Proceedings of the 52nd Annual Meeting of the Association for Computational

Linguistics, pp. 238-247.

Bengio, Y., Courville, A., and Vincent, P. 2013. “Representation Learning: A Review and New Perspectives,” IEEE Transactions on Pattern Analysis and Machine Intelligence (35:8), pp. 1798-1828.

Björne, J., Kaewphan, S., and Salakoski, T. 2013. “UTurku: Drug Named Entity Recognition and Drug-Drug Interaction Extraction Using SVM Classification and Domain Knowledge,” in Proceedings of the Seventh International Workshop on Semantic Evaluation, vol. 2, pp. 651-659.

Blackman, N. J.-M., and Koval, J. J. 2000. “Interval Estimation for Cohen’s Kappa As A Measure Of Agreement,” Statistics in Medicine (19:5), Wiley, pp. 723-741.

Bosworth, H. B., Granger, B. B., Mendys, P., Pharm, D., Brindis, R., Burkholder, R., Czajkowski, S. M., Daniel, J. G., Ekman, I., Ho, M., Johnson, M., Kimmel, S. E., Liu, L. Z., Musaus, J., Shrank, W. H., Buono, E. W., Weiss, K., and Granger, C. B. 2011. “Medication Adherence: A Call for Action,” American Heart Journal (162), pp. 412-424.

Brisson, L., and Torrel, J.-C. 2015. “Opinion Mining on Experience Feedback: A Case Study on Smartphones Reviews,” in Proceedings of the 9th International Conference on Research Challenges in Information Science, pp. 187-192.

Chan, W., and Lane, I. 2015. “Deep Recurrent Neural Networks for Acoustic Modelling,” ArXiv ( https://arxiv.org/pdf/1504.01482.pdf)

Chen, H., Chiang, R. H. L., and Storey, V. C. 2012. “Business Intelligence and Analytics: From Big Data to Big Impact,” MIS Quarterly (36:4), pp. 1165-1188.

Chen, T., Xu, R., He, Y., and Wang, X. 2017. “Improving Sentiment Analysis via Sentence Type Classification Using BiLSTM-CRF and CNN,” Expert Systems with Applications (72), Elsevier Ltd, pp. 221-230.

Chen, Z., Mukherjee, A., and Liu, B. 2014. “Aspect Extraction with Automated Prior Knowledge Learning,” in Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics, pp. 347-358.

Cheng, J., Zhang, X., Li, P., Zhang, S., Ding, Z., and Wang, H. 2016. “Exploring Sentiment Parsing of Microblogging Texts for Opinion Polling on Chinese Public Figures,” Applied Intelligence (45), pp. 429-442.

Chiu, J. P. C., and Nichols, E. 2015. “Named Entity Recognition with Bidirectional LSTM-CNNs,” Transactions of the Association for Computational Linguistics (4), pp. 357-370.

Chiu, J. P. C., and Nichols, E. 2016. “Named Entity Recognition with Bidirectional LSTM-CNNs,” Transactions of the Association for Computational Linguistics (4), pp. 357-370.

Chollet, F. 2017. “Keras: The Python Deep Learning library.,”

Chorowski, J., Weiss, R. J., Bengio, S., and Van Den Oord, A. 2019. “Unsupervised Speech Representation Learning Using WaveNet Autoencoders,” IEEE Transactions on Audio Speech and Language Processing (27:12), pp. 2041-2053.

Crain, S., and Nakayama, M. 1987. “Structure Dependence in Grammar Formation,” Language (63:3), p. 522-543.

Deng, S., Huang, Z., and Sinha, A. 2018. “Can Social Media Sentiment Affect Stock Market Performance?,” LSE Business Review (https://blogs.lse.ac.uk/businessreview/2018/09/19/ microblogging-sentiment-and-stock-returns/)

Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. 2018. “BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding,” ArXiv (https://arxiv.org/pdf/1810.04805.pdf)

Dunbar, S. B., Clark, P. C., Quinn, C., Gary, R. A., and Kaslow, N. J. 2008. “Family Influences on Heart Failure Self-Care and Outcomes,” The Journal of cardiovascular nursing (23:3), pp. 258-265.

Eickholt, J., Deng, X., and Cheng, J. 2011. “DoBo: Protein Domain Boundary Prediction by Integrating Evolutionary Signals and Machine Learning,” BMC Bioinformatics (12), Article 43 .

Faisal, M., Chowdhury, M., Fondazione, A. L., and Kessler, B. 2013. “FBK-irst : A Multi-Phase Kernel Based Approach for Drug-Drug Interaction Detection and Classification that Exploits Linguistic Information,” in Proceedings of the 7th International Workshop on Semantic Evaluation, Vol. 2, pp. 351-355.

Fang, Q., Xu, C., Sang, J., Hossain, M. S., and Muhammad, G. 2015. “Word-of-Mouth Understanding: Entity-Centric Multimodal Aspect-Opinion Mining in Social Media,” IEEE Transactions on Multimedia (17:12), pp. 2281-2296.

Fang, X., Hu, P. J. H., Li, Z. L., and Tsai, W. 2013. “Predicting adoption probabilities in social networks,” Information Systems Research (24:1), pp. 128-145.

Fu, T., Abbasi, A., Zeng, D., and Chen, H. 2012. “Sentimental Spidering: Leveraging Opinion Information in Focused Crawlers,” ACM Transactions on Information Systems (30:4), Article 24.

Garten, J., Sagae, K., Ustun, V., and Dehghani, M. 2015. “Combining Distributed Vector Representations for Words,” in Proceedings of NAACL-HLT, pp. 95-101.

Gellad, W. F., Grenard, J. L., and Marcum, Z. A. 2011. “A Systematic Review of Barriers to Medication Adherence in the Elderly: Looking Beyond Cost and Regimen Complexity,” The American Journal of Geriatric Pharmacotherapy (9:1), pp. 11- 23.

Gellad, W. F., Grenard, J., and Mcglynn, E. A. 2009. A Review of Barriers to Medication Adherence: A Framework for Driving Policy Options, RAND Corporation.

Goh, J. M., Gao, G., and Agarwal, R. 2016. “The Creation of Social Value: Can an Online Health Community Reduce Rural-Urban Health Disparities?,” MIS Quarterly (40:1), pp. 247-263.

Goldberg, Y., and Levy, O. 2014. “word2vec Explained: Deriving Mikolov et al.’s Negative-Sampling Word-Embedding Method,” ArXiv (https://arxiv.org/pdf/1402.3722.pdf).

Goldman, D. P., Joyce, G. F., and Zheng, Y. 2007. “Prescription Drug Cost Sharing,” JAMA (298:1), pp. 61-69.

Goodfellow, I., Bengio, J., and Courville, A. 2016. Deep Learning.

Gregor, S., and Hevner, A. 2013. “Positioning and Presenting Design Science Research for Maximum Impact,” MIS Quarterly (37:2), pp. 337-355.

Hai, Z., Chang, K., Kim, J.-J., and Yang, C. C. 2014. “Identifying Features in Opinion Mining via Intrinsic and Extrinsic Domain Relevance,” IEEE Transactions on Knowledge and Data Engineering (26:3), pp. 623-634.

Hamilton, W. L., Ying, R., and Leskovec, J. 2017. “Inductive Representation Learning on Large Graphs,” in Proceedings of the 31st International Conference on Neural Information Processing Systems, pp. 1025-1035.

Harding, E. 2015. “How Pharma Companies Are Using Social Media to Learn About Drugs’ Affects on Patients,” Healthcare (https://healthcareglobal.com/technology-and-ai/how-pharmacompanies-are-using-social-media-learn-about-drugs-affectspatients).

Hart, K. L., Perlis, R. H., and McCoy, T. H. 2020. “What Do Patients Learn about Psychotropic Medications on the Web? A Natural Language Processing Study,” Journal of Affective Disorders (260), pp. 366-371.

Hasan, K. S., and Ng, V. 2014. “Why Are You Taking this Stance? Identifying and Classifying Reasons in Ideological Debates,” in Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, pp. 751-762.

Hevner, A. R., March, S. T., Park, J., and Ram, S. 2004. “Design Science in Information Systems Research,” MIS Quarterly (28:1), pp. 75-105.

Horne, B. D., and Adali, S. 2017. “The Impact of Crowds on News Engagement: A Reddit Case Study,” in Proceedings of the International AAAI Conference on Web and Social Media.

Hugtenburg, J. G., Timmers, L., Elders, P. J., Vervloet, M., and van Dijk, L. 2013. “Definitions, Variants, and Causes of Nonadherence with Medication: A Challenge for Tailored Interventions.,” Patient Preference and Adherence (7), pp. 675-682.

Hutto, C. J., and Gilbert, E. 2014. “VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text,” in Proceedings of the 8th International AAAI Conference on Weblogs and Social Media.

Jeyapriya, A., and Selvi, C. S. K. 2015. “Extracting Aspects and Mining Opinions in Product Reviews Using Supervised Learning Algorithm,” in Proceedings of the 2nd International Conference on Electronics and Communication Systems, pp. 548-552.

Joachims, T. 2003. “Learning to Classify Text Using Support Vector Machines: Methods, Theory, and Algorithms,” Journal of Computational Linguistics (29:4), pp. 655-664.

Ju, Z., Wang, J., and Zhu, F. 2011. “Named Entity Recognition from Biomedical Text Using SVM,” in Proceedings of the 5th International Conference on Bioinformatics and Biomedical Engineering.

Kalchbrenner, N., Grefenstette, E., and Blunsom, P. 2014. “A Convolutional Neural Network for Modelling Sentences,” in Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Vol. 1), pp. 655-665.

Karahanna, E., Xu, S. X., Xu, Y., and Zhang, N. 2018. “The Needs-Affordances-Features Perspective for the Use of Social Media,” MIS Quarterly (42:3), pp. 737-756.

Khoury, M. J., and Ioannidis, J. P. A. 2014. “Big Data Meets Public Health,” Science (346:6213), 1054-1055.

Kim, J.-D., Ohta, T., Tateisi, Y., and Tsujii, J. 2003. “GENIA Corpus: A Semantically Annotated Corpus for Bio-Textmining,” Bioinformatics (19:Suppl. 1), pp. i180-i182.

Kim, S.-M., and Hovy, E. 2006. “Automatic Identification of Pro and Con Reasons in Online Reviews,” in Proceedings of the COLING/ACL on Main Conference Poster Sessions, pp. 483- 490.

Kim, T., Jeong, M., Kim, S., Choi, S., and Kim, C. 2019. “Diversify and Match: A Domain Adaptive Representation Learning Paradigm for Object Detection,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 12456-12465).

Kitchens, B., Dobolyi, D., Li, J., and Abbasi, A. 2018. “Advanced Customer Analytics: Strategic Value Through Integration of Relationship-Oriented Big Data,” Journal of Management Information Systems (35:2), pp. 540-574.

Krousel-Wood, M., Islam, T., Webber, L. S., Re, R. N., Morisky, D. E., and Muntner, P. 2009. “New Medication Adherence Scale versus Pharmacy Fill Rates in Seniors with Hypertension.,” The American Journal of Managed Care (15:1), pp. 59-66.

Lample, G. 2016. “Neural Architectures for Named Entity Recognition,” in Proceedings of NAACL-HLT, pp. 260-270.

Lau, R., Liao, S., Wong, K. F., and Chiu, D. 2012. “Web 2.0 Environmental Scanning and Adaptive Decision Support for Business Mergers and Acquisitions,” MIS Quarterly (36:4), pp. 1239-1268.

Lazer, D., Kennedy, R., King, G., and Vespignani, A. 2014. “The Parable of Google Flu: Traps in Big Data Analysis,” Science (343:6176), pp. 1203-1205.

Lee, K.-J., Hwang, Y.-S., Kim, S., and Rim, H.-C. 2004. “Biomedical Named Entity Recognition Using Two-Phase Model Based on SVMs,” Journal of Biomedical Informatics (37:6), pp. 436-447.

Levy, O., and Goldberg, Y. 2014. “Neural Word Embedding as Implicit Matrix Factorization,” in Proceedings of the 27th International Conference on Neural Information Processing Systems, Vol. 2, pp. 2177-2185.

Li, H., Lin, R., Hong, R., and Ge, Y. 2015. “Generative Models for Mining Latent Aspects and Their Ratings from Short Reviews,” in Proceedings of the IEEE International Conference on Data Mining.

Liang, D., and Zhang, Y. 2016. “AC-BLSTM: Asymmetric Convolutional Bidirectional LSTM Networks for Text Classification,”

Liu, P., Joty, S., and Meng, H. 2015. “Fine-Grained Opinion Mining with Recurrent Neural Networks and Word Embeddings,” in Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, pp. 1433- 1443.

Liu, Q., Liu, B., Zhang, Y., Kim, D. S., and Gao, Z. 2016. “Improving Opinion Aspect Extraction Using Semantic Similarity and Aspect Associations,” in Proceedings of the 30th AAAI Conference on Artificial Intelligence, pp. 2986- 2992.

Luo, X., Zhang, J. (Jennifer), Gu, B., and Phang, C. 2017. “Expert Blogs and Consumer Perceptions of Competing Brands,” MIS Quarterly (41:2), pp. 371-395.

Ma, X., and Hovy, E. 2016. “End-to-End Sequence Labeling via Bi-Directional LSTM-CNNs-CRF,” in Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics.

Mai, F., Shan, Z., Bai, Q., Wang, X. (Shane), and Chiang, R. H. L. 2018. “How Does Social Media Impact Bitcoin Value? A Test of the Silent Majority Hypothesis,” Journal of Management Information Systems (35:1), pp. 19-52.

Marcum, Z. A., Sevick, M. A., and Handler, S. M. 2013. “Medication Nonadherence,” JAMA (309:20), pp. 2105-2106.

Marrese-Taylor, E., Velásquez, J. D., and Bravo-Marquez, F. 2014. “A Novel Deterministic Approach for Aspect-Based Opinion Mining in Tourism Products Reviews,” Expert Systems with Applications (41:17), pp. 7764-7775.

Maulik, U., and Bandyopadhyay, S. 2002. “Performance Evaluation of Some Clustering Algorithms and Validity Indices,” IEEE Transactions on Pattern Analysis and Machine Intelligence (24:12), pp. 1650-1654.

McHorney, C. A., Schousboe, J. T., Cline, R. R., and Weiss, T. W. 2007. “The Impact of Osteoporosis Medication Beliefs and Side-Effect Experiences on Non-Adherence to Oral Bisphosphonates,” Current Medical Research and Opinion (23:12), pp. 3137-3152.

Mikolov, T., Corrado, G., Chen, K., and Dean, J. 2013. “Efficient Estimation of Word Representations in Vector Space,” in Proceedings of the International Conference on Learning Representations.

Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., and Dean, J. 2013. “Distributed Representations of Words and Phrases and their Compositionality,” in Proceedings of the 26th International Conference on Neural Information Processing Systems, Vol. 2 , pp. 3111-3119.

Okazaki, N. 2007. “CRFsuite: A Fast Implementation of Conditional Random Fields (CRFs).,”

Onishi, T., Weissenbacher, D., Klein, A., O’Connor, K., and Gonzalez, G. 2018. “Dealing with medication non-adherence expressions in Twitter,” in Proceedings of the 3rd Social Media Mining for Health Applications Workshop & Shared Task, pp. 32-33.

Ordóñez, F., and Roggen, D. 2016. “Deep Convolutional and LSTM Recurrent Neural Networks for Multimodal Wearable Activity Recognition,” Sensors (16:1), pp. 115-140.

Paul, M., and Dredze, M. 2012. “Factorial LDA: Sparse Multi-Dimensional Text Models,” in Proceedings of the 25th International Conference on Neural Information Processing Systems.

Patra, B. G., Mandal, S., Das, D., and Bandyopadhyay, S. 2014. “JU\_CSE: A Conditional Random Field (CRF) Based Approach to Aspect Based Sentiment Analysis,” in Proceedings of the 8<sup>th</sup> International Workshop on Semantic Evaluation, pp. 370-374.

Pennington, J., Socher, R., and Manning, C. D. 2014. “GloVe: Global Vectors for Word Representation,” in Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, pp. 1532-1543.

Pew Internet Research. 2013. “61% of American Adults Look Online for Health Information,” Pew Research Center (https://www.pewresearch.org/internet/2009/06/11/61-ofamerican-adults-look-online-for-health-information/).

Popov, A. 2016. “Deep Learning Architecture for Part-of-Speech Tagging with Word and Suffix Embeddings,” in Proceedings of the International Conference on Artificial Intelligence: Methodology, Systems, and Applications, pp. 68-77.

Poria, S., Cambria, E., and Gelbukh, A. 2016. “Aspect Extraction for Opinion Mining with a Deep Convolutional Neural Network,” Knowledge-Based Systems (108), pp. 42-49.

Rai, A. 2017. “Editor’s Comments: Diversity of Design Science Research,” MIS Quarterly (41:1), pp. iii-xviii.

Rao, K., Peng, F., Sak, H., and Beaufays, F. 2015. “Grapheme-to-Phoneme Conversion Using Long Short-Term Memory Recurrent Neural Networks,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing, pp. 4225-4229.

Ruths, D., and Pfeffer, J. 2014. “Social Media for Large Studies of Behavior,” Science (343:6176), pp. 1203-1205.

Saboo, A. R. 2016. “Using Big Data to Model Time-Varying Effects for Marketing Resource (Re)Allocation,” MIS Quarterly (40:4), pp. 911-939.

Sørensen, K., Van den Broucke, S., Fullam, J., Doyle, G., Pelikan, J., Slonska, Z., and Brand, H. 2012. “Health Literacy And Public Health: A Systematic Review and Integration of Definitions and Models,” BMC Public Health (12), Article 80.

Stieglitz, S., and Dang-Xuan, L. 2013. “Emotions and Information Diffusion in Social Media: Sentiment of Microblogs and Sharing Behavior,” Journal of Management Information Systems (29:4), pp. 217-248.

Sun, B., Mitra, P., Lee Giles, C., and Mueller, K. T. 2011. “Identifying, Indexing, and Ranking Chemical Formulae and Chemical Names in Digital Documents,” ACM Transactions on Information Systems (29:2), pp. 1-38.

Tai, K. S., Socher, R., and Manning, C. D. 2015. “Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks,” in Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing, pp. 1556-1566.

Tamblyn, R., Eguale, T., Huang, A., Winslade, N., and Doran, P. 2014. “The Incidence and Determinants of Primary Nonadherence With Prescribed Medication in Primary Care,” Annals of Internal Medicine (160:7), pp. 441-450.

Tang, D., Qin, B., and Liu, T. 2015. “Document Modeling with Gated Recurrent Neural Network for Sentiment Classification,” in Conference Proceedings: EMNLP 2015, pp. 1422-1432.

Tang, D., Wei, F., Yang, N., Zhou, M., Liu, T., and Qin, B. 2014. “Learning Sentiment-Specific Word Embedding for Twitter Sentiment Classification,” in Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics, pp. 1555-1565.

Traverso, G., and Langer, R. 2015. “Perspective: Special Delivery for the Gut,” Nature (519:7544), pp. S19-S19.

Turian, J., Ratinov, L., and Bengio, Y. 2010. “Word Representations: A Simple And General Method For Semi-Supervised Learning,” in Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics, pp. 384-394.

Wallace, B. C., Paul, M. J., Sarkar, U., Trikalinos, T. A., and Dredze, M. 2014. “A Large-Scale Quantitative Analysis of Latent Factors and Sentiment in Online Doctor Reviews,” Journal of the American Medical Informatics Association (21:6), pp. 1098-1103.

Wang, S., Chen, Z., and Liu, B. 2016. “Mining Aspect-Specific Opinion Using a Holistic Lifelong Topic Model,” in Proceedings of the 25th International Conference on World Wide Web, pp. 167-176.

Wang, W., Tan, G., and Wang, H. 2016. “Cross-Domain Comparison of Algorithm Performance in Extracting Aspect-Based Opinions from Chinese Online Reviews,” International Journal of Machine Learning and Cybernetics (8), pp, 1053- 1070.

Wang, X., Jiang, W., and Luo, Z. 2016. “Combination of Convolutional and Recurrent Neural Network for Sentiment Analysis of Short Texts,” in Proceedings of the 26th International Conference on Computational Linguistics, pp. 2428-2437.

Weidenbacher, H. J., Beadles, C. A., Maciejewski, M. L., Reeve, B. B., and Voils, C. I. 2015. “Extent and Reasons for Nonadherence to Antihypertensive, Cholesterol, and Diabetes

Medications: The Association with Depressive Symptom Burden in a Sample of American Veterans.,” Patient Preference and Adherence (9), pp. 327-336.

Williams, J. L. S., Walker, R. J., Smalls, B. L., Campbell, J. A., and Egede, L. E. 2014. “Effective Interventions to Improve Medication Adherence in Type 2 Diabetes: A Systematic Review,” Diabetes Management (4:1), pp. 29-48.

Xie, J., Zeng, D. D., and Marcum, Z. A. 2017. “Using Deep Learning to Improve Medication Safety: The Untapped Potential of Social Media,” Therapeutic Advances in Drug Safety (8:12), pp. 375-377.

Xiong, S., and Ji, D. 2016. “Exploiting Flexible-Constrained K-Means Clustering with Word Embedding for Aspect-Phrase Grouping,” Information Sciences (367), pp. 689-699.

Yang, Z., Yang, D., Dyer, C., He, X., Smola, A., and Hovy, E. 2016. “Hierarchical Attention Networks for Document Classification,” in Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies 2016, pp. 1480- 1489.

Zhang, D., Zhou, L., Kehoe, J. L., and Kilic, I. Y. 2016. “What Online Reviewer Behaviors Really Matter? Effects of Verbal and Nonverbal Behaviors on Detection of Fake Online Reviews,” Journal of Management Information Systems (33:2), pp. 456-481.

Zhang, L., and Liu, B. 2014. “Aspect and Entity Extraction for Opinion Mining,” in Data Mining and Knowledge Discovery for Big Data: Studies in Big Data, vol 1., W. Chu (ed.), Springer, pp. 1-40.

Zheng, S., Jayasumana, S., Romera-Paredes, B., Vineet, V., Su, Z., Du, D., Huang, C., and Torr, P. H. S. 2015. “Conditional Random Fields as Recurrent Neural Networks,”

Zhou, C., Frankowski, D., Ludford, P., Shekhar, S., and Terveen, L. 2007. “Discovering Personally Meaningful Places: An Interactive Clustering Approach,” ACM Transactions on Information Systems (25:3), pp. 12-es.

Zhou, P., Qi, Z., Zheng, S., Xu, J., Bao, H., and Xu, B. 2016. “Text Classification Improved by Integrating Bidirectional LSTM with Two-Dimensional Max Pooling,” in Proceedings of 26th International Conference on Computational Linguistics 2016, pp. 3485-3495.

## About the Authors

Jiaheng Xie is an assistant professor in the Department of Accounting and MIS at the University of Delaware’s Alfred Lerner College of Business and Economics. His research interests lie in explainable deep learning, health risk analytics, and business analytics. His dissertation, titled “Big

Data-Based Health Risk Analytics: A Deep Learning Approach,” develops novel deep learning methods to understand, predict and mitigate three levels of critically important health risks: patient behavioral risk, disease risk, and policy risk. His prior works have been published at many premier journals, including Journal of Management Information Systems and Journal of American Medical Informatics Association.

Xiao Liu is an assistant professor in the Department of Information Systems. Previously, she was an assistant professor at The University of Utah. Liu’s research interests are in data science and information system design, in areas such as health IT, social media analytics, and predictive analytics.

Daniel Zeng is a researcher in the State Key Laboratory of Management and Control for Complex Systems at the Chinese Academy of Sciences. His areas of expertise include software agents and multi-agent systems, collaborative information and knowledge management, recommender systems, social computing, digital economic institutions, automated negotiation and auction, security informatics, spatiotemporal data analysis, and online surveillance. Zeng is a member of the Association for Information Systems (AIS), the Institute for Operations Research and the Management Sciences (INFORMS), The Association for Computing Machinery, and the Institute of Electrical and Electronics Engineers.

Xiao Fang is a professor of management information systems at the Lerner College of Business and Economics, University of Delaware. He received a B.S. and an M.S. from Fudan University, China, and a Ph.D. in management information systems from the University of Arizona. He studies business and social network analytics with research methods and tools drawn from reference disciplines including management science (e.g., optimization) and computer science (e.g., data mining and machine learning). He has published in MIS Quarterly, Management Science, Information Systems Research, Operations Research, INFORMS Journal on Computing, Journal of Management Information Systems, ACM Transactions on Information Systems, and IEEE Transactions on Knowledge and Data Engineering, among other outlets.

The aspects of an object O are defined as its components and attributes (Zhang and Liu 2014). An aspect expression is an actual phrase that indicates an aspect in the text. Table A2 shows three examples of aspects and aspect expressions in the cellular phone domain.

## Appendix

<table><tr><td colspan="9">Table A1. Recent Studies in Aspect Mining</td></tr><tr><td>Author</td><td>Year</td><td>Aspect extraction</td><td>Aspect clustering</td><td>Method</td><td>Data</td><td>Object</td><td>Aspect</td><td>Performance</td></tr><tr><td>Wang et al. (c)</td><td>2016</td><td>Yes</td><td>No</td><td>CRF</td><td>3,646 reviews</td><td>Restaurant</td><td>Food, price, service</td><td>F-score: 63%</td></tr><tr><td>Liu et al.</td><td>2016</td><td>Yes</td><td>No</td><td>CRF</td><td>5.8m reviews</td><td>Camera</td><td>Battery life, picture quality</td><td>F-score: 73%</td></tr><tr><td>Xiong and Ji</td><td>2016</td><td>No</td><td>Yes</td><td>K-means</td><td>1,389 sentences</td><td>Camera</td><td>Photo, battery</td><td>RI: 59%</td></tr><tr><td>Xiong and Ji</td><td>2016</td><td>No</td><td>Yes</td><td>K-means</td><td>1,389 sentences</td><td>Camera</td><td>Photo, battery</td><td>Entropy: 1.74</td></tr><tr><td>Wang et al. (b)</td><td>2016</td><td>Yes</td><td>Yes</td><td>LDA</td><td>1,000 reviews</td><td>Laptop</td><td>Screen, battery</td><td>Precision: 79%</td></tr><tr><td>Poria et al.</td><td>2016</td><td>Yes</td><td>No</td><td>CNN</td><td>7,686 reviews</td><td>Laptop</td><td>Battery, camera</td><td>F-score: 87%</td></tr><tr><td>Fang et al. (b)</td><td>2015</td><td>Yes</td><td>Yes</td><td>LDA</td><td>5,632 reviews</td><td>Tourist spot</td><td>Architecture, park, food, museum</td><td>Perplexity: 3,375</td></tr><tr><td>Jeyapriya and Selvi</td><td>2015</td><td>Yes</td><td>No</td><td>Rule-based</td><td>100 reviews</td><td>Camera</td><td>Pictures, resolution, memory</td><td>F-score: 80%</td></tr><tr><td>Liu et al.</td><td>2015</td><td>Yes</td><td>No</td><td>RNN</td><td>2,358 reviews</td><td>Laptop</td><td>Hard disk, screen</td><td>F-score: 74%</td></tr><tr><td>Li et al.</td><td>2015</td><td>Yes</td><td>No</td><td>CRF</td><td>6,847 reviews</td><td>Mouse</td><td>Durability, compatibility, sensitivity</td><td>Precision: 65%</td></tr><tr><td>Brisson and Torrel</td><td>2015</td><td>Yes</td><td>No</td><td>CRF</td><td>40,160 reviews</td><td>Smartphone</td><td>Battery, camera</td><td>F-score: 68%</td></tr><tr><td>Marrese-Taylor et al.</td><td>2014</td><td>Yes</td><td>No</td><td>CRF</td><td>200 reviews</td><td>Hotel</td><td>Price, food, service, pool</td><td>F-score: 73%</td></tr><tr><td>Hai et al.</td><td>2014</td><td>Yes</td><td>Yes</td><td>LDA</td><td>10,073 reviews</td><td>Cellphone</td><td>Screen, battery, money</td><td>F-score: 56%</td></tr><tr><td>Patra et al.</td><td>2014</td><td>Yes</td><td>No</td><td>CRF</td><td>3,045 sentences</td><td>Restaurant</td><td>Service, food, ambiance</td><td>F-score: 72%</td></tr><tr><td>Chen et al.</td><td>2014</td><td>Yes</td><td>Yes</td><td>LDA, K-means</td><td>36k reviews</td><td>Camera</td><td>Battery, service, memory</td><td>Coherence: -1,450</td></tr></table>

<table><tr><td colspan="2">Table A2. Updating Rules of the Sentiment-Enriched Word Embedding</td></tr><tr><td>Aspect</td><td>Aspect expressions</td></tr><tr><td>Price</td><td>Expensive, cannot afford, high price</td></tr><tr><td>Camera</td><td>High resolution, high-quality picture</td></tr><tr><td>Screen size</td><td>Big screen, large screen, screen is big</td></tr></table>

The updating rule of the sentiment-enriched word embedding is:

$$
\pmb {x} _ {w _ {I}} ^ {(n e w)} = \pmb {x} _ {w _ {I}} ^ {(o l d)} - \eta \frac {\partial L _ {s}}{\partial w _ {k , i}} = \pmb {v} _ {w _ {I}} ^ {(o l d)} - \eta \frac {\partial L _ {s}}{\partial h _ {i}} \cdot \frac {\partial h _ {i}}{\partial w _ {k , i}}.\tag{A1}
$$

Variable $\scriptstyle x _ { w _ { I } }$ is the vector representation of the input word $w _ { I }$ . Parameter ?? is the learning rate. Variable $w _ { k , i }$ is the weight between the input layer and the hidden layer. Variable $h _ { i }$ is the output of the hidden layer. The terms ${ \frac { \partial { \cal L } _ { s } } { \partial h _ { i } } } \operatorname { a n d } { \frac { \partial h _ { i } } { \partial w _ { k , i } } }$ can be further computed as follows:

$$
\frac {\partial h _ {i}}{\partial w _ {k , i}} = x _ {k}.\tag{A2}
$$

Variable $x _ { k }$ is the input. The term $\frac { \partial L _ { s } } { \partial h _ { i } }$ can be calculated as:

$$
\frac {\partial L _ {s}}{\partial h _ {i}} = \alpha \frac {\partial L _ {c o n t}}{\partial h _ {i}} + (1 - \alpha) \frac {\partial L _ {s e n t i}}{\partial h _ {i}} = \alpha \sum_ {j = 1} ^ {V} \frac {\partial L _ {c o n t}}{\partial u _ {j}} \cdot \frac {\partial u _ {j}}{\partial h _ {i}} + (1 - \alpha) \frac {\partial L _ {s e n t i}}{\partial u _ {s}} \cdot \frac {\partial u _ {s}}{\partial h _ {i}}.\tag{A3}
$$

Variables $u _ { j }$ and $u _ { s }$ are the values of the output layer. Therefore

$$
\frac {\partial L _ {c o n t}}{\partial u _ {j}} = \frac {\partial \left(\frac {1}{2} (t - y) ^ {2}\right)}{\partial y} = y - t = e _ {j};\tag{A4}
$$

$$
\frac {\partial u _ {j}}{\partial h _ {i}} = w _ {i j} ^ {\prime}.\tag{A5}
$$

Variable ?? is the true output value. Variable ?? is the output. Variable $e _ { j }$ is the learning error. Parameter $w _ { i j } ^ { \prime }$ is the weight between the hidden layer and the output layer. Similarly,

$$
\frac {\partial L _ {s e n t i}}{\partial u _ {s}} = e _ {s};\tag{A6}
$$

$$
\frac {\partial u _ {s}}{\partial h _ {i}} = w _ {s} ^ {\prime}.\tag{A7}
$$

Variable $e _ { s }$ is the learning error of the sentiment component. Parameter $w _ { s } ^ { \prime }$ is the weight for the sentiment between the hidden and the output layer. Combining Equations A3-A7:

$$
\frac {\partial L _ {s}}{\partial h _ {i}} = \alpha \sum_ {j = 1} ^ {V} e _ {j} \cdot w _ {i j} ^ {\prime} + (1 - \alpha) e _ {s} w _ {s} ^ {\prime} = \alpha \mathrm{E} _ {c o n t, i} + (1 - \alpha) \mathrm{E} _ {s e n t i, i}.\tag{A8}
$$

Variable $\mathrm { E } _ { c o n t , i }$ is the sum of the output vectors of all words weighted by the prediction error. Variable $\mathrm { E } _ { s e n t i , i }$ is the output of sentiment weighted by the prediction error.

The updating rule of the sentiment-enriched word embedding is shown in Equation A9.

$$
\pmb {x} _ {w _ {I}} ^ {(n e w)} = \pmb {x} _ {w _ {I}} ^ {(o l d)} - \eta \big (\alpha \mathrm{E} _ {c o n t, i} + (1 - \alpha) \mathrm{E} _ {s e n t i, i} \big).\tag{A9}
$$

## Architecture Details of SEDEL

Convolutional layer: the information extraction method in the convolutional layer is shown in Equation A10.

$$
\pmb {x} _ {c o n v, i, j} = \pmb {b} + \sum_ {p = 0} ^ {P} \sum_ {q = 0} ^ {Q} \pmb {w} _ {p, q} \pmb {x} _ {i + p, j + q}.\tag{A10}
$$

Variable $\pmb { x } _ { c o n v , i , j }$ is the output vector. Variable ?? is the bias. Parameter $w _ { p , q }$ is the filter weight matrix to extract salient features. Variable $x _ { i + p , j + q }$ is the sentiment-enriched word embedding.

BLSTM layer: the LSTM unit takes the output from the convolutional layer as the input. The computational process in the LSTM unit is summarized in Equations A11-A15.

$$
\boldsymbol {i} ^ {(t)} = \operatorname{sigm} \left(\boldsymbol {W} _ {i} \boldsymbol {x} _ {l s t m} ^ {(t)} + \boldsymbol {U} _ {i} \boldsymbol {h} ^ {(t - 1)} + \boldsymbol {b} _ {i}\right);\tag{A11}
$$

$$
\pmb {f} ^ {(t)} = s i g m \left(\pmb {W} _ {f} \pmb {x} _ {l s t m} ^ {(t)} + \pmb {U} _ {f} \pmb {h} ^ {(t - 1)} + \pmb {b} _ {f}\right);\tag{A12}
$$

$$
\pmb {o} ^ {(t)} = s i g m \left(\pmb {W} _ {o} \pmb {x} _ {l s t m} ^ {(t)} + \pmb {U} _ {o} \pmb {h} ^ {(t - 1)} + \pmb {b} _ {o}\right);\tag{A13}
$$

$$
\pmb {c} ^ {(t)} = t a n h \left(\pmb {W} _ {u} \pmb {x} _ {l s t m} ^ {(t)} + \pmb {U} _ {u} \pmb {h} ^ {(t - 1)} + \pmb {b} _ {u}\right);\tag{A14}
$$

$$
\boldsymbol {h} ^ {(t)} = \boldsymbol {o} ^ {(t)} \odot \tanh \left(\boldsymbol {i} ^ {(t)} \odot \boldsymbol {c} ^ {(t)} + \boldsymbol {f} ^ {(t)} \odot \boldsymbol {c} ^ {(t - 1)}\right).\tag{A15}
$$

Variable $\pmb { x } _ { l s t m } ^ { ( t ) }$ is the current input. Variable $\boldsymbol { x } _ { c o n v } ^ { ( t ) }$ is the output vector of the convolutional layer. Variable $\pmb { h } ^ { ( t - 1 ) }$ is the previous hidden state. Parameters ??, ??, and ?? are weight parameters with values between 0 and 1. The gates $( \pmb { i } ^ { ( t ) } , \pmb { f } ^ { ( t ) }$ , and $\mathbf { \pmb { o } } ^ { ( t ) } )$ and memory cell $\pmb { c } ^ { ( t ) }$ take $\pmb { x } _ { l s t m } ^ { ( t ) }$ at time step ?? and information in the last hidden state $\pmb { h } ^ { ( t - 1 ) }$ . This mechanism allows useful information from previous time steps to persist and learn useful information in new inputs.

## User Reviews & Ratings -Abilifyoral

![](/api/attachments/ZUZD2AE9/fulltext/images/e3981102a89737e9a17e880f44598500062a034c1db612bdb5b3d119601d8039.jpg)  
Figure A1. An Example of WebMD Drug Reviews

![](/api/attachments/ZUZD2AE9/fulltext/images/d8842ed01b9e939d79b1504d705a1b928d16bd497587eda1603e6be851979aa5.jpg)

Figure A2. Gender Distribution of Patients in the Corpus

![](/api/attachments/ZUZD2AE9/fulltext/images/4c465a9a88b8953827352bef7268b90fda722886b161e956f99eb7d17d4a6dd5.jpg)  
Figure A3. Age Distribution of Patients in the Corpus

## Details of Filtering MNA Reviews

We filter the reviews that indicate MNA using a BLSTM model, the state-of-the-art method in text classification (Liang and Zhang 2016). The parameter dimension setup (300-dimensional sentiment-enriched word embedding and 128-dimensional forward and backward hidden size) is consistent with previous studies (Ma and Hovy 2016; Rao et al. 2015). A total of 200 undergraduate students read 10,000 drug review and annotated whether the reviews indicated MNA. We trained the BLSTM text classification model on 8,000 annotated reviews and tested the performance on the remaining reviews. The BLSTM text classification model achieved an accuracy of 84.18% in the test data (precision for MNA class: 84.16%; recall for MNA class: 81.58%), indicating good performance. We applied the BLSTM model on the entire corpus and generated 20,977 reviews that are used for MNA-reason extraction and clustering.

## Description of Baseline Models

SVM has achieved a satisfying performance in various studies (Abbasi et al. 2010, 2012; Fang et al. 2013). We use SVM-Light (Joachims 2003) as the implementation for SVM because it has been used as a strong baseline model in many studies (Eickholt et al. 2011; Faisal et al. 2013; Sun et al. 2011). The SVM classifier predicts whether a phrase is a reason for MNA or not, given a set of features of the containing words. Consistent with previous studies (Asif Ekbal 2010; Björne et al. 2013; Ju et al. 2011; Lee et al. 2004), four groups of features are selected:

1. Lexicon features: The lexicon feature is a binary variable indicating whether a word is included in the lexicon. The lexicon indexes the top-10,000 frequent words in the GENIA corpus (2,000 abstracts of articles from the MEDLINE database) (Kim et al. 2003)

2. Suffix features: The suffix feature is a binary indicator to show whether a word contains the suffix in a pre-defined set (Lee et al. 2004). These suffixes are parts of complex medical terms and are helpful for identifying words related to medications.

3. Frequent Hyphen Suffix List: -acting, -activated, -activating, -activation, -active, -affinity, -associated, -based, -binding, -bound, -box, -cell, -chain, -containing, -coupled, -deficient, -dependent, -depleted, -derived, -encoded, -encoding, -endothelial, -enhancer, -erythroid, -exposed, -expressing, -factor, -family, -fold, -forming, -free, -function, -gene, -helix, -independent, -induced, -inducer, -inducible, - inducing, -infected, -initiated, -labeled, -linked, -luciferase, -lymphoid, -macrophage, -mediated, -myb, -negative, -onset, -phase, - positive, -producing, -promoting, -protein, -proximal, -reactive, -receptor, -regulated, -regulating, -regulatory, -related, -resistant, - response, -reponsive, -restricted, -selectin, -sensitive, -shift, -site, -specific, -stimulated, -stimulating, -stimulation, -term, -terminal, - terminus, -transformed, -treated, -tropic, -tumor, -type.

4. POS features: The POS feature is the part-of-speech tag of a word.

5. Context features: The context features are the previous and next words for the word of interest.

Conditional random fields (CRFs) are the most popular machine learning sequence labeling models (Lau et al. 2012; Sun et al. 2011; Zhou et al. 2007). Salient prior research in aspect mining adopted CRFs (Fang et al. 2015b; Liu et al. 2016; Marrese-Taylor et al. 2014; Wang et al. 2016b). We, therefore, benchmark our proposed method against CRFs. We use CRFSuite as the implementation for the CRFs due to its outstanding performance and efficiency (Okazaki 2007; Turian et al. 2010). CRFSuite is able to generate features automatically given training and test text. The annotation scheme and data for CRF are the same as used in SEDEL.

Furthermore, we benchmark the proposed SEDEL model against four standard deep learning models: Convolutional neural network (CNN), recurrent neural network (RNN), long short-term memory (LSTM), and bidirectional long short-term memory (BLSTM). All the four baseline models are implemented with the Keras library (Chollet 2017). The standard word embedding contains 300 dimensions, and the hidden layer contain 128 nodes.

We also compare SEDEL with other methods that incorporate sentiment in alternative approaches (Fu et al. 2012; Abbasi et al. 2018; Tang et al. 2014). To implement Fu et al. (2012), we devise a sentiment classifier using VaderSentiment in the input. We filter the reviews that have negative sentiment, because medication nonadherence reviews usually have a negative sentiment. We then apply SEDEL on the filtered results. To implement Abbasi et al. (2018), we add sentiment as an additional feature in the embedding vector. To implement Tang et al. (2014), we use the same model as described in the original paper and replace the representation in SEDEL with the representation learned from Tang et al. (2014).

![](/api/attachments/ZUZD2AE9/fulltext/images/d78e4ee4806c8660cde0c75e38287e5ea77afd35adf3e179ba9e080bf2a7ad98.jpg)  
Figure A4. Architecture of Attention-Based SEDEL

<table><tr><td colspan="2">Table A3. Clustering Evaluation</td></tr><tr><td>Number of Clusters</td><td>Calinski-Harabaz Index</td></tr><tr><td>2</td><td>1646.794</td></tr><tr><td>3</td><td>1241.946</td></tr><tr><td>4</td><td>970.196</td></tr><tr><td>5</td><td>833.974</td></tr><tr><td>6</td><td>758.822</td></tr><tr><td>7</td><td>640.090</td></tr><tr><td>8</td><td>583.821</td></tr><tr><td>9</td><td>539.384</td></tr><tr><td>10</td><td>484.750</td></tr></table>

<table><tr><td colspan="4">Table A4. Correlation Between Effectiveness Ratings and MNA Reasons</td></tr><tr><td>Reason type</td><td>Drug effectiveness rating</td><td>Drug ease of use rating</td><td>User satisfaction rating</td></tr><tr><td>Adverse event</td><td>0.052</td><td>-0.008</td><td>-0.006</td></tr><tr><td>Drug switching</td><td>0.050</td><td>0.017</td><td>0.051</td></tr><tr><td>Low health literacy</td><td>0.126</td><td>0.055</td><td>0.110</td></tr><tr><td>Social influence</td><td>-0.018</td><td>-0.029</td><td>-0.015</td></tr><tr><td>Cost prohibitive for patient</td><td>0.031</td><td>0.028</td><td>0.042</td></tr><tr><td>Complex medication plan</td><td>0.040</td><td>0.013</td><td>0.029</td></tr><tr><td>Medication ineffectiveness</td><td>0.071</td><td>0.068</td><td>0.080</td></tr><tr><td>Specific population</td><td>0.034</td><td>0.011</td><td>0.024</td></tr><tr><td>Others</td><td>0.117</td><td>0.075</td><td>0.118</td></tr><tr><td>All</td><td>0.090</td><td>0.024</td><td>0.051</td></tr></table>

Table A5 shows the differences in MNA reasons for individual drugs. The top-five discontinued drugs for each reason type are reported.

<table><tr><td colspan="2">Table A5. MNA Reasons for Individual Drugs</td></tr><tr><td>Reason type</td><td>Top-five discontinued drugs for each reason</td></tr><tr><td>Adverse event</td><td>Cialis, Levaquin, Lisinopril, Avelox, Bactrim DS</td></tr><tr><td>Drug switching</td><td>Opana, Roxicodone, Valium, Cymbalta, Coumadin</td></tr><tr><td>Low health literacy</td><td>Cialis, Opana, Gabapentin, Lisinopril, Actos</td></tr><tr><td>Social influence</td><td>Risperdal, Digoxin, Namenda, Vyvanse, Roxicodone</td></tr><tr><td>Cost prohibitive for patient</td><td>Valtrex, Bystolic, Protonix, Lopressor, Phenergan</td></tr><tr><td>Complex medication plan</td><td>Valium, Diazepam, Oxycontin, Gabapentin, Roxicodone</td></tr><tr><td>Medication ineffectiveness</td><td>Gabapentin, Opana, Vyvanse, Valium, Promethazine</td></tr><tr><td>Specific population</td><td>Vistaril, Valtrex, Loratadine, Furosemide, Zofran</td></tr><tr><td>Others</td><td>Vyvanse, Cialis, Effexor XR, Adderall, Paxil</td></tr></table>

## Social Media Biases

Researchers raised concerns that forecasts and analyses produced from social media could misrepresent the real world. These concerns stem from the biases in social media data, such as selection bias, confounding variables, and lack of generalizability (Khoury and Ioannidis 2014). Two major issues in social media analytics contributing to these biases are big data hubris and algorithm dynamics (Lazer et al. 2014). Big data hubris is the implicit assumption that big data are a substitute for, rather than a supplement to, traditional data collection and analysis. Algorithm dynamics are the changes and design choices made by engineers to improve the service and by consumers to use the service. Empirical research stands on a foundation of measurement. It is critical for instrumentation to capture the theoretical construct of interest. As a result of algorithm dynamics, the measurement might not be stable or comparable across cases and over time. To address these issues, Ruths and Pfeffer (2014) provide a guideline to distill the challenges into operational pieces and particular standards. They recommend quantifying the relevant biases from the platform, data, proxy population, applying filters for nonhumans in data, and comparing results to existing methods on the same data.
