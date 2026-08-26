---
otero_id: 25390
otero_key: "KWZ8EEV8"
title: "Unveiling the Hidden Truth of Drug Addiction: A Social Media Approach Using Similarity Network-Based Deep Learning"
authors: "Jiaheng Xie; Zhu Zhang; Xiao Liu; Daniel Zeng"
year: "2021"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2021.1870388"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Unveiling the Hidden Truth of Drug Addiction: A Social Media Approach Using Similarity Network-Based Deep Learning

Jiaheng Xie, Zhu Zhang, Xiao Liu & Daniel Zeng

To cite this article: Jiaheng Xie, Zhu Zhang, Xiao Liu & Daniel Zeng (2021) Unveiling the Hidden Truth of Drug Addiction: A Social Media Approach Using Similarity Network-Based Deep Learning, Journal of Management Information Systems, 38:1, 166-195, DOI: 10.1080/07421222.2021.1870388

To link to this article: https://doi.org/10.1080/07421222.2021.1870388

![](/api/attachments/KWZ8EEV8/fulltext/images/a0aace8e91f43f742077c88604fbb06c12e94ba4adb3e23101f60dfd242fff59.jpg)

View supplementary material

![](/api/attachments/KWZ8EEV8/fulltext/images/fbb557908b1c386439b33fbf6975a718ae29217a8ab97ed2cd19a063a0013d4b.jpg)

Published online: 02 Apr 2021.

![](/api/attachments/KWZ8EEV8/fulltext/images/8d901de9b58b15e06b6b67e1280ffeb2d7a1eebd7c85fdc363fde2450a5618b8.jpg)

Submit your article to this journal

![](/api/attachments/KWZ8EEV8/fulltext/images/45ec96594f643a351f063cb533c44c02e1bb0e85124b217ff178a3a479a86c21.jpg)

Article views: 112

![](/api/attachments/KWZ8EEV8/fulltext/images/316502e91e3f4b3a850a63828be88bbd1a1e26ae7228569d9b4292e6743142a6.jpg)

View related articles

![](/api/attachments/KWZ8EEV8/fulltext/images/bb6e0ce23be3808b380f6f564108c42e05045e2e842061979cc22f1644faa63a.jpg)

View Crossmark data

Check for updates

# Unveiling the Hidden Truth of Drug Addiction: A Social Media Approach Using Similarity Network-Based Deep Learning

Jiaheng Xie<sup>a</sup>, Zhu Zhang<sup>b,d</sup>, Xiao Liu<sup>e</sup>, and Daniel Zeng<sup>b,c,d</sup>

<sup>a</sup>Department of Accounting and MIS, Lerner College of Business & Economics, University of Delaware, Newark, DE, USA; <sup>b</sup>State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences; <sup>c</sup>University of Chinese Academy of Sciences; <sup>d</sup>Shenzhen Artificial Intelligence and Data Science Research Institute (Longhua); <sup>e</sup>Arizona State University, Tempe, AZ, USA

## ABSTRACT

Opioid use disorder (OUD) is an epidemic that costs the U.S. healthcare systems \$504 billion annually and poses grave mortality risks. Existing studies investigated OUD treatment barriers via surveys as a means to mitigate this opioid crisis. However, the response rate of these surveys is low due to social stigma around opioids. We explore user-generated content in social media as a new data source to study OUD. We design a novel IT system, SImilarity Network-based DEep Learning (SINDEL), to discover OUD treatment barriers from patient narratives and address the challenge of morphs. SINDEL significantly outperforms state-of-the-art NLP models, reaching an F1 score of 76.79 percent. Thirteen types of treatment barriers were identified and verified by domain experts. This work contributes to information systems with a novel deep-learning-based approach for text analytics and generalized design principles for social media analytics methods. We also unveil the hurdles patients endure during the opioid epidemic.

## KEYWORDS

Computational design science; deep learning; social media analytics; health IT; HealthTech; opioid addiction; addiction treatment

## Introduction

Social media have been fundamentally changing the approach businesses communicate, collaborate, consume, and create [4]. According to a McKinsey Quarterly report, 50 percent of the more than 1,700 surveyed businesses use social networking, 41 percent use blogs, 25 percent use wikis, and 23 percent use microblogs [11]. These social media platforms, coupled with analytics methods, ofer powerful solutions to support business-related functions [58, 61], such as inferring consumer preferences, peer-to-peer and targeted marketing, and stock prediction, among others [7, 59]. In the medical domain, social media analytics is also a forerunner of reorganizing medical knowledge creation and medical work in the digital age, and a complement to established health research methods. Kallinikos and Tempini [29] analyzed data from a webbased, medical research network with patient self-reports, and assessed the value of social media for extracting medical knowledge and understanding patient experience. Witnessing the great potential of social media in health analytics research, we aim to explore an online social network with patient self-reports to uncover patient experience to treat opioid use disorder (OUD).

Opioids are a group of pain-relievers that interact with opioid receptors in cells [33]. In 2016, 11.8 million Americans misused prescription opioids or used illicit opioids [60]. Among them, 2.1 million sufered from opioid addiction. The cost of OUD exceeds \$504 billion in 2015, or 2.8 percent of the GDP [15]. These costs are reflected in healthcare, lost productivity, treatment for substance use disorder, and the criminal justice system. To address the nation’s opioid epidemic, the Support for Patients and Communities Act expands access to treatments of OUD. Patients who remain on treatments for a longer time tend to have better outcomes. The risk of relapse greatly escalates if patients stop these treatments. Nevertheless, retaining patients in treatment remains a significant challenge. Only 17.5 percent of patients with OUD continue to receive treatments [43]. Such a low adoption rate is due in part to significant access barriers to treatments, such as the fear of job loss, limited insurance coverage, social stigma, and treatment programs located in limited areas with long waitlists. Understanding these barriers is the premise to reduce overdose mortality, mitigate the transmission of infectious diseases, and lower healthcare costs.

Surveys are extensively used in prior work to understand the barriers to OUD treatments [21, 41]. These studies are challenged by the narrow patient population, as individuals with OUD are dificult to reach if they are not actively under treatment. User-generated content in social media can bridge this gap. Studies show that 59 percent of adults participate in health social media platforms, which ofer a vast amount of patient narratives about their medication-taking behavior [45]. Social media has also been used as an information technology (IT) application to provide innovative insights on various urgent health issues [12, 19]. Due to the anonymous nature of online forums, patients are willing to share their experience of taking prescription and illicit opioids and elaborate on their real decisionmaking on OUD treatments (e.g., Figure 1). This large-scale patient-reported information creates an unprecedented potential to study OUD treatment barriers from the patient standpoint and facilitate analyses on heterogeneous patients timely [14]. Nevertheless, social media analytics approach is still lacking in OUD research.

Significant challenges still linger to understand patient perspectives from drug forums despite their enormous potential. First, OUD treatment barriers are contingent on patients life events over time. Efective surveillance for OUD treatments necessitates fine-grained automated models that could identify barriers timely. Second, patients use vocabulary diferent from that of health professionals. Only 43 percent of symptom terms in social media are presented as exact or synonymous with terms in the professional language [55]. Such a language gap stems from the morphs (fake alternative names) that patients use to describe drugs and treatments in order to avoid censorship and surveillance, entertain readers, or use personal writing styles. For instance, morphs of Oxycodone include Oxy, O. C., Oxycet, Oxycontin, and more. Morphs of OUD treatments, such as meth, MMT, and chocolate chip cookies, are extensively used in patient discussions. The literal meanings of the morphs are distant from their contextual meanings. This gap between the literal and contextual meanings of morphs poses a significant challenge to understand patient discussions. Fortunately, the patient-generated morphs, like other community-specific languages, can be learned through representation learning and knowledge construction.

![](/api/attachments/KWZ8EEV8/fulltext/images/db613ece9dbdbf36b37f5cc132e6c27ac49590bc5ea4d5ef8467397c605a108f.jpg)  
Figure 1. Examples of patient narratives about opioid use disorder (OUD) treatment.

Motivated by the critical need for fine-grained and automated techniques to understand OUD treatment barriers in drug forums, we propose a novel computational method: SImilarity Network-based DEep Learning (SINDEL). We define the barriers to OUD treatment as patient self-described factors leading to the denial of OUD treatments. SINDEL extends the state-of-the-art text mining models with a similarity network-based component and multi-view deep learning architecture. The similarity network-based component bridges the literal and contextual semantics of morphs. The multi-view deep learning architecture enhances the learning performance on sparse OUD-related narratives through a recurrent and parallel hierarchical structure. SINDEL collects timely social media data about opioid use and identifies existing and emerging treatment barriers that could assist proactive interventions.

Our study makes the following contributions to information systems (IS) literature, data analytics methodology, and healthcare practice. First, we develop the SINDEL method to extract OUD treatment barriers from drug forums. The proposed method significantly outperforms the baseline models. The performance enhancement is attributed to SINDEL’s capability of interpreting the semantic meaning of morphs accurately. This finding contributes to the literature of text analytics and linguistics that incorporating a similarity network in language models could disentangle the complex semantics in specialized knowledge forums. SINDEL can also be generalized to extract information from many other text genres containing specialized morphs, such as hacker forums, health social media, and product reviews.

Second, our study falls under the realm of computational design science research that aims to design analytics solutions to problems with societal impact [48]. We provide an automated framework to understand patient decision-making. In line with the design science guidelines in Hevner et al. [24], this framework serves as the IT artifact. To select the best artifact design, we conducted rigorous experiments to test the hyperparameters in the input and hidden layers and the parameters in the similarity network, and to benchmark with other plausible systems, among others. The proposed framework contributes to the IS knowledge base, as the design principles (model selection and hyperparameter tuning) and the new method ofer generalized guidelines for design science research in social media analytics.

Third, our findings involve the heterogeneity among patients and open a window to understanding illicit drug users’ behavior. The drug forum exhibits rich knowledge and patient experience generated by patients. Our findings can complement the behavioral science research on OUD with comprehensive patient experience data. We discover 13 types of OUD treatment barriers, including lack of medical literacy, social stigma, concerns about job loss, withdrawal reactions and side efects, and more. Many of these treatment barriers have not been noted by prior survey studies, such as side efects of treatment, concerns about treatment addiction, poor patient-physician relationships, and depressed mental status. We provide valuable implications for medical professionals and policymakers to understand individual opioid-taking behavior and the real treatment barriers faced by patients. Tailored intervention measures can be taken accordingly to prevent medical and financial ramifications, improve OUD management, and reverse the opioid crisis.

## Literature Review

Our study is related to four research areas. First, we survey the literature on OUD treatments for the current understanding of OUD. Second, we review online community and design science to explore IT systems to assist opioid research. Third, we summarize opinion mining in social media to bring in design principles. Fourth, we review morphology studies to propose a method that can address the technical challenges to identify OUD treatment barriers in drug forums.

## Barriers to OUD Treatments

In the past decade, opioid use disorder (OUD) has drawn attention from clinical practitioners, policymakers, and researchers, who attempt to understand and remove the treatment barriers to OUD. Table 1 shows the recent studies on OUD treatment barriers. Surveys are commonly used to investigate the barriers to OUD treatment, with subject sample sizes ranging from 20 to over 4,000 patients [41]. The barriers to OUD treatment identified in these studies can be summarized as three categories: 1) System-related: the factors related to healthcare systems and regulations, such as government and insurance policies and funding barriers [32]; 2) Provider-related: the factors related to health providers, such as lack of DEA waiver, lack of institutional support, lack of resources, and geographic constraints [53]; 3) Patient-related: patient-specific factors, such as the fear of pain and lack of information on treatments [21].

Understanding the barriers to OUD treatment forms the basis for developing efective interventions. Current studies investigated the barriers to OUD treatment via surveys, which ofer only cursory descriptions of some well-known barriers, lacking depth and comprehensiveness. These surveys only capture a snapshot of barriers. In reality, many patient-level barriers are complicated by patient characteristics and policy changes, causing them to vary over time. Hence, surveys are unlikely to ofer a comprehensive view of treatment barriers. Moreover, survey studies are provider-centric, lacking understanding from the patients’ perspectives. This dominant provider perspective poses a significant challenge to translating these treatment barriers into real-world settings as providers have minimal control over patient decision-making on OUD treatments. Furthermore, patients are reluctant to disclose their issues with OUD treatments, especially illicit drug users. Some patients intentionally avoid being connected to OUD treatments due to the social stigma around opioids.

Table 1. Recent Studies on opioid use disorder (OUD) Treatment Barriers.

<table><tr><td>Author</td><td>Year</td><td>Method</td><td>Participants</td><td>OUD Treatment Barriers</td><td>Intervention</td></tr><tr><td>Livingston et al. [37]</td><td>2018</td><td>Interview</td><td>20</td><td>Access to methadone expertise, professional support</td><td>Enhance the uptake and availability of evidence-based treatment</td></tr><tr><td>Hassamal et al. [21]</td><td>2017</td><td>Review</td><td>5</td><td>Financial, administrative, policy, lack of information</td><td>Engage high-risk patients in substance abuse treatment, decrease recidivism, close monitoring and supervision</td></tr><tr><td>McKenna [41]</td><td>2017</td><td>Survey</td><td>4,100</td><td>Financial</td><td>National implementation of the Affordable Care Act (ACA)</td></tr><tr><td>Stumbo et al. [57]</td><td>2017</td><td>Interview</td><td>283</td><td>Fear of uncontrolled pain, stigma of addiction</td><td>Use separate addiction outpatient therapy groups</td></tr><tr><td>Andrilla et al. [6]</td><td>2017</td><td>Survey</td><td>1,124</td><td>Lack of physician&#x27;s Drug Enforcement Administration (DEA) waiver</td><td>Encourage physicians to add or maintain this service, including targeting former prescribers</td></tr><tr><td>Sharma et al. [53]</td><td>2017</td><td>Review</td><td>NA</td><td>Financial, regulatory, geographic, attitudinal, logistic</td><td>Expand Medicaid, cover all medications for OUD, discourage managed care organizations to erect further administrative barriers</td></tr><tr><td>Bojko et al. [10]</td><td>2016</td><td>Interview</td><td>86</td><td>Unclear treatment goal, provider and societal negative attitude, legislation</td><td>Quality improvement, patient education and medical professional development</td></tr><tr><td>Hutchinson et al. [26]</td><td>2014</td><td>Interview</td><td>92</td><td>Physician&#x27;s lack of institutional support</td><td>Increase the number of physicians who offer buprenorphine, technical assistance training</td></tr></table>

## Online Social Community and Design Science

Innovative approaches are needed to understand OUD treatment barriers, patient behaviors, and potential measures that can deliver care to patients in need. Health big data from social media make innovative projects possible and open opportunities for investigations that can yield insights into and understanding of issues such as patient decision-making, human motivation, and social phenomena [8, 14]. Because of the anonymous nature of social media, many patients, including illicit drug users, actively share their drug-taking experience with their peers.

Since the early 2000s, many social media applications have eficiently gathered a large volume of self-reported experience from a diverse patient population [14, 34]. This patient self-reported experience not only provides dynamic information but also covers an unprecedented scale of the patient population with heterogeneous characteristics. Yet, no social media analytics approach has been taken in OUD treatment studies.

Computational methods can be integrated into IT systems to yield more insights from the big health data with patients’ vantage point. The IS literature also stressed the value of health social media analytics, as online patient communities provide insights into patients’ illnesses [13, 65]. Since data being generated are increasingly unstructured and coming from networks of patients, it is essential to design more powerful algorithms and better knowledge representation schemes for making sense of this heterogeneous health information [2, 5]. Hevner et al. [24], Gregor and Hevner [20], and Chen et al. [14] have emphasized the necessity for such a design and computational category of IS research and outlined a guideline for design science studies so that cutting-edge algorithms can be leveraged to tackle significant problems with societal impact. This computational design science paradigm has contributed indispensable design principles and analytical methods to various IS research areas, such as healthcare IT, cybersecurity, e-commerce, and more [1, 3, 17, 40, 51, 56].

## Opinion Mining and Social Media Analytics

Extensive literature in IS utilizes opinion mining techniques to understand the factors of consumer behaviors, such as purchase decision, technology acceptance, and more [64]. Opinion mining usually includes the following procedures: data collection, opinion identification, aspect extraction, aspect clustering, and production summary [23]. The barriers to OUD treatment are aspects related to treatments, patients, and insurance, among others, which can be extracted with aspect extraction techniques in opinion mining. Most research in aspect extraction focuses on social media data. There are four common categories of techniques in aspect extraction: extraction based on high-frequency noun phrases, extraction based on exploiting opinion and aspect relations, extraction based on sequence learning, and extraction based on topic modeling.

## Extraction Based on High-Frequency Noun Phrases

When users express their opinions about various aspects of a product, they use similar noun phrases frequently. These noun phrases and nouns can be determined by syntactic parsing and POS tagging. Li et al. [35] proposed a method for improving feature extraction performance in online reviews. Their method, based on frequent nouns and noun phrases, is consisted of three components: frequency-based mining and pruning, order-based filtering, and similarity-based filtering. Jeyapriya and Selvi [27] extracted nouns and noun phrases from each review sentence and used a minimum support threshold to find frequent aspects in review sentences. Extraction based on high-frequency noun phrases is efective when aspects are expressed in consistent and common terms. When a new aspect or a variation of existing aspect emerges, this approach is not able to capture it.

## Extraction Based on Relations Between Opinion Words and Aspects

The opinion words can be used to describe diferent aspects. Qiu et al. [46] focused on two fundamental and important issues, opinion lexicon expansion and target extraction, and suggested the double propagation approach. They performed extraction based on syntactic relations that draw links between review words and aspects of products. This approach is limited because syntactic relations among words in reviews may not be accurately extracted and consumers do not always follow grammar rules when writing the reviews.

## Extraction Based on Topic Modeling

Topic models are unsupervised methods for aspect extraction in which they assume that any document contains k hidden topics. Some of these topics can be aspects of products. Statistical methods, such as latent semantic analysis (LSA) and latent Dirichlet allocation (LDA) with bag-of-words representation of documents, can be used in document-level aspect extraction. Ma et al. [39] proposed a probabilistic topic model approach based on LDA in order to search over citizens’ opinions about city issues on online platforms. Luo et al. [38] devised a Quad-tuple LSA for detection and rating aspects in product reviews. Sentences in drug forums are very long, because of the noisy nature of social media data and the misuse of punctuations. If we apply topic modeling at the sentence level, each sentence contains many topics. The majority of these topics are irrelevant to OUD. Because of the extensive existence of irrelevant topics, few to none words would be generated by OUDrelated topics. Additionally, as each word has a probability to be generated by any topic, OUD-related topics may still generate non-treatment barrier words. The unsupervised topic models cannot pinpoint the words about OUD treatment barriers, since there are no training labels. For these reasons, topics models are not feasible in this study.

## Extraction Based on Sequence Learning

The sequence learning approach is a promising technique for aspect extraction, which are usually developed for named entity recognition in natural language processing. This approach learns the patterns with labeled reviews and determines whether a word belongs to an entity of interest, in this case, an aspect expression. Support vector machine (SVM), conditional random fields (CRF), and hidden Markov model (HMM) are supervised learning methods that can be used to extract aspects [36]. Aspects were extracted from a collection of blog posts using machine learning methods, and the results were used as statistical patterns for aspect extraction. CRF achieves satisfying performance in formal text genres, but it falls short in processing patient narratives in drug forums. This is because CRF treats words as discrete atomic symbols, which require accurate input for training and prediction.

Unlike the data used in existing opinion mining studies, drug forums have unique features. When describing OUD treatments, patients use many morphs to represent drugs and treatment options to avoid censorship and surveillance. We refer to morphs as any derived terms other than the generic medical term. For instance, heroin can be referred to as H, hero, and China white by diferent users. None of the aforementioned extraction approaches are suited for this issue. Traditional text mining methods are not capable of interpreting the underlying semantics of morphs because they use discrete atomic symbols to represent the words.

## Morphology and Deep Learning

In order to address the challenges in opinion mining in drug forums, we draw insights from morphology and deep learning studies. Morphology is the study of words, how they are formed, and their relationship to other words in a language. In drug forums, users invent new slangs and idiomatic expressions to describe their experience. Related work in morphology aims to address the challenges of understanding slangs, synonyms, and other types of word variations in unstructured text and hence can help us understand OUD-related expressions in drug forums. Table 2 shows the recent literature in morphology. Similar to the drug morphs and patient idiomatic expressions in drug forums, morphology studies tackle internet slangs, synonyms, and semantically similar terms [62, 66]. The main body of literature in morphology utilizes distributed representation and deep learning methods, such as word embedding and recurrent neural network (RNNs), to interpret the semantics of morphs.

Word embedding is a vector-based representation of words commonly used in deep learning models for natural language processing. According to the Distributional Hypothesis, words with similar meanings occur with similar neighbors [50]. Word embedding represents each word in a vector of its surrounding words instead of by the symbolic word itself. Word embedding can efectively represent sparse entities, entities with typos, and entities with variations in social media data for machine learning models.

Table 2. Recent studies on morphology in online texts.

<table><tr><td>Author</td><td>Year</td><td>Data</td><td>Method</td><td>Morphs of Interest</td></tr><tr><td>Simpson et al. [54]</td><td>2018</td><td>Tweets</td><td>Word embedding</td><td>Emerging drug terms</td></tr><tr><td>Yao et al. [62]</td><td>2018</td><td>News articles</td><td>Word embedding</td><td>Word changes over time</td></tr><tr><td>Qu et al. [47]</td><td>2017</td><td>Wikipedia</td><td>Word embedding</td><td>Entity synonyms in Wikipedia</td></tr><tr><td>Huang et al. [25]</td><td>2017</td><td>WSJ articles</td><td>BLSTM</td><td>Synonyms in news articles</td></tr><tr><td>Sha et al. [52]</td><td>2017</td><td>Tweets</td><td>Character-level embedding</td><td>Internet morphs in Twitter</td></tr><tr><td>He et al. [22]</td><td>2016</td><td>Search query</td><td>Optimization</td><td>Attribute synonyms in search queries</td></tr><tr><td>Nguyen et al. [42]</td><td>2016</td><td>Web pages</td><td>Word embedding</td><td>Antonym and synonym in text</td></tr><tr><td>Zhang et al. [66]</td><td>2016</td><td>NYT articles</td><td>Word embedding</td><td>Semantically similar terms in articles</td></tr></table>

Notes: WSJ = Wall Street Journal; BLSTM = bidirectional long short-term memory; NYT = New York Times.

The RNN is a class of artificial neural network where connections between units form a loop. This feature creates internal states in the network and enables information to persist during the learning process. RNN with word embedding input achieves good performance in many sequence learning tasks, such as parts-of-speech tagging, named entity recognition, and machine translation [9, 44]. Long Short-Term Memory (LSTM), an improvement to standard RNN, addresses the long-term dependency issue. LSTM can add or remove information in each internal state through the internal gates in the LSTM units. A Bidirectional Long Short-Term Memory (BLSTM) network connects two hidden layers of opposite directions to the same output, thus making future input data available for the current state. BLSTM has achieved leading performance for named entity recognition on noisy user-generated text, because of its ability to consider interconnected information in a sentence.

The challenge to identify OUD treatment barriers is exacerbated by the morphs in online OUD discussions. The morphs of drugs and treatment options are widely used in OUD discussions. The literal meaning of these morphs is distant from their contextual meaning. Morphs for drugs in the same class are semantically closer than the morphs across drug classes. Each opioid class has a unique efect, regimen, and instruction, leading to varying semantic contexts in OUD discussions. For instance, Oxycodone is a semi-synthetic opioid, the morphs of which include Oxy, O.C., Oxycet, Oxycontin, and more. The morphs of heroin include H, China white, and more. Oxy and O.C. are not only morphs of opioid drugs, but they represent the same drug class (Oxycodone) as well. Therefore, Oxy and O. C. are more closely related than Oxy and China white. The vector representation of words models the semantic context of words using the neighboring words of the focal word. Interconnected relationships within the same opioid class are neglected by this method. A similarity network of words can help address this issue by explicitly examining the contextual similarity of words. In addition to the semantic relatedness to local neighboring words, key entities of interest, such as drug names and treatment efects, are related due to the medical context. Deep learning models for sequence learning are well-suited for extracting this interdependency across diferent terms in a sentence. Therefore, we are motivated to propose a new deep learning architecture that incorporates the vector representation of words and semantic similarity in a network to extract treatment barriers from drug forums.

## Research Method

## OUD Treatment Barrier Mining Problem Formulation

Let P denote a set of n users $P = \{ p _ { 1 } , \ldots , p _ { n } \}$ in the drug forum. Let O denote a set of opioids $O = \{ o _ { 1 } , \dots , o _ { m } \}$ reported by users in P. A review set $\nu _ { i j }$ is a set of all reviews posted by user $ { \boldsymbol { p } } _ { i }$ about opioid $o _ { j }$ regarding his or her drug-taking experience in drug forums. $\nu _ { i j }$ contains m sentences $s _ { K } ,$ where $K \in \{ 1 , 2 , \ldots , m \}$ . Sentence $s _ { k }$ with n words can be denoted as $[ w _ { k } ^ { ( 1 ) } , w _ { k } ^ { ( 2 ) } , . . . , w _ { k } ^ { ( n ) } ]$ , where $w _ { k } ^ { ( t ) }$ is the t-th word in $s _ { k }$ . If a user $ { \boldsymbol { p } } _ { i }$ with opioid $o _ { j }$ decides not to seek treatment, he or she would be likely to describe the barriers to OUD treatment in the review $\nu _ { i j }$ . The barriers to OUD treatment of user $ { \boldsymbol { p } } _ { i }$ reporting opioid $o _ { j }$ are denoted as $b _ { i j } ^ { 1 } , b _ { i j } ^ { 2 } , \ldots , b _ { i j } ^ { q } ( q$ is the number of barriers). A barrier $b _ { i j } ^ { k }$ can be a word $\left[ w _ { k } ^ { ( t ) } \right]$ or a phrase $[ w _ { k } ^ { ( 1 ) } , w _ { k } ^ { ( 2 ) } , \dots , w _ { k } ^ { ( m ) } ]$

The OUD treatment barrier mining involves two tasks. The first task is a sequence learning task, aimed at predicting whether each word $w _ { k } ^ { ( t ) }$ in sentence $s _ { k }$ belongs to the beginning of a barrier, inside of a barrier, or outside a barrier. The input is a sentence. The output is a set of barrier phrases $b _ { i j } ^ { 1 } , b _ { i j } ^ { 2 } , \ldots , b _ { i j } ^ { q }$ . The second task is a clustering task. The clustering task groups similar barriers together and identifies the general types of barriers. The input is the barriers identified from the first task. The output is several clusters of barriers.

## Similarity Network-Based Deep Learning Approach

The OUD treatment barrier mining has two objectives: barrier extraction and barrier clustering, following the established procedure of aspect-based opinion mining (aspect extraction and aspect clustering) [64]. Barrier extraction identifies patient self-described OUD treatment barriers $b _ { i j } ^ { 1 } , b _ { i j } ^ { 2 } , \ldots , b _ { i j } ^ { q }$ for each patient $ { \boldsymbol { p } } _ { i }$ taking opioid $o _ { j } .$ Since patients use diferent expressions to describe the same type of barrier, barrier clustering groups the identified OUD treatment barriers based on their semantic meaning. The process of the OUD treatment barrier mining is shown in Figure 2. The novelty of our approach is highlighted in red. The proposed OUD treatment barrier mining approach receives a sentence from drug forums as the input. Two parallel representation models represent the sentence with two vectors. Branch 1 utilizes word embedding to generate semantic vectors for each word. Branch 2 creates a similarity network of words and generates a network representation for each word. The two representations are fused to recognize the OUD treatment barriers in the sentence. A clustering model is utilized to cluster the extracted barriers into meaningful categories of general barriers. We elaborate on the details of our deep learning approach in the following subsections.

## Similarity Network-Based Representation

The proposed similarity network-based representation contains two parallel representations. The first representation is a word embedding to capture the semantic meaning of words, so that morphs can be interpreted as their intended meaning. Given a word, the objective of word embedding is to learn the vector representation of this word based on its neighboring words in the same sentence. This vector-based representation could be obtained by pre-trained embedding from large corpora or locally-trained embedding. Empirical studies suggest that pre-trained embedding, such as word2vec, yields superior performance than locally-trained embedding, due to the large training corpora (Google News). We build our word embedding model leveraging word2vec. To incorporate the semantic and syntactic characteristics of the OUD context into this representation, we set the embedding vector to be trainable. The embedding vector will learn to adjust based on the learning objective of our deep learning model (OUD treatment barrier mining). The resulting model obtains an array of semantic vectors with 300 dimensions.

The second representation aims to construct a network of words in order to capture the interconnected relationships. In this network $G = \left( V , E \right)$ , each node V is a word, and the edge E is the semantic similarity between words. As such, each word is linked to a set of words that are closely related. For instance, Oxy is linked to O.C. and Oxycet, because they are the most similar morphs. Oxy is not linked to China white, because they belong to diferent drug classes. This word similarity network addresses the limitation of word embedding by considering the semantic relationships among entities of interests. Instead of using the representation of the focal word, we use similar words that are connected to the focal word as the second representation for the focal word. Figure 3 shows an example.

![](/api/attachments/KWZ8EEV8/fulltext/images/ea7a26ae6a60aae7fb4bc4b729448f4fcbb55d0066aebd8cb2f51ffe46a02d96.jpg)  
Figure 2. The opioid use disorder (OUD) treatment barrier mining framework.

In the example in Figure 3, Oxycodone $( w ^ { ( 1 ) } )$ is linked to Oxy, O.C., Oxycet, and Oxycontin, because they belong to the same drug class. We use ${ \boldsymbol { w } } ^ { ( 2 ) } , { \boldsymbol { w } } ^ { ( 3 ) } , { \boldsymbol { w } } ^ { ( 4 ) }$ , and $\boldsymbol { w } ^ { ( 5 ) }$ to represent $\boldsymbol { w } ^ { ( 1 ) }$ . Likewise, China white, H, and hero are linked to heroin. We use $\boldsymbol { w } ^ { ( 7 ) } , \boldsymbol { w } ^ { ( 8 ) }$ and $\boldsymbol { w } ^ { ( 9 ) }$ to represent $\boldsymbol { w } ^ { ( 6 ) }$ . In our corpus, we construct a similarity network for all words and compute the similarity between each pair of words. We select a set of most similar words for each word and link them together. The network size (number of similar words) is determined in the empirical analyses with the highest performance. Word similarity is computed using the cosine similarity of word embedding as shown in Equation 1.

$$
s i m _ {i j} = \frac {x ^ {(i)} x ^ {(j)}}{\| x ^ {(i)} \| \| x ^ {(j)} \|}\tag{1}
$$

where variables $x ^ { ( i ) }$ and $x ^ { ( j ) }$ are the word embedding of word $\boldsymbol { w } ^ { ( i ) }$ and $\boldsymbol { w } ^ { ( j ) }$ . Given word w, let ${ \boldsymbol { w } } ^ { ( 1 ) } , { \boldsymbol { w } } ^ { ( 2 ) } , \dots , { \boldsymbol { w } } ^ { ( 1 0 ) }$ be the top ten words that are the most similar to word w. Let sim<sup>ð1Þ</sup>; sim<sup>ð2Þ</sup>; . . . ; sim<sup>ð10Þ</sup> be the similarity between word w and the other ten words. Let $x ^ { ( 1 ) } , x ^ { ( 2 ) } , \ldots , x ^ { ( 1 0 ) }$ be the word embedding for ${ \boldsymbol w } ^ { ( 1 ) } , { \boldsymbol w } ^ { ( 2 ) } , \dots , { \boldsymbol w } ^ { ( 1 0 ) }$ . The similarity network representation of word w is defined in Equation 2.

$$
x _ {w} = \sum_ {t = 1} ^ {1 0} \operatorname{sim} ^ {(i)} x ^ {(i)}.\tag{2}
$$

![](/api/attachments/KWZ8EEV8/fulltext/images/afd2ff1b9068721b7fc89f270c9ea64ffd7d274d26eee5e180faf4a87807047c.jpg)  
Figure 3. An example of a word similarity network.

## Multi-view Deep Learning Architecture

To efectively extract the barriers to OUD treatment, we utilize BLSTM architecture with a multi-view learning framework. Since a sentence follows semantic and syntactic rules, words in diferent locations in a sentence may exhibit semantic dependencies regardless of the word order. This bidirectional structure could capture such dependencies from both directions. We devise a multi-view BLSTM model that processes the word embedding representation and the similarity network representation in parallel. The multi-view BLSTM model contains two branches. Each branch has an independent BLSTM layer that contains bidirectional LSTM units. Our model is called SImilarity Network-based DEep Learning (SINDEL).

The LSTM units in branch one take the word embedding as the input, and the LSTM units in branch two take the similarity network representation as the input. The computational process for branch two is shown in Equations 3-8. The computational process in the first branch is the same, except that the input at each time step is word embedding $x ^ { ( t ) }$ instead of similarity network representation $x _ { s } ^ { ( t ) }$

Similarity network-based input gate:

$$
i _ {s} ^ {(t)} = \sigma \left(W _ {s i} x _ {s} ^ {(t)} + U _ {s i} h _ {s} ^ {(t - 1)} b _ {s i}\right);\tag{3}
$$

Similarity network-based forget gate:

$$
f _ {s} ^ {(t)} = \sigma \left(W _ {s f} x _ {s} ^ {(t)} + U _ {s f} h _ {s} ^ {(t - 1)} + b _ {s f}\right);\tag{4}
$$

Similarity network-based output gate:

$$
o _ {s} ^ {(t)} = \sigma \left(W _ {s o} x _ {s} ^ {(t)} + U _ {s o} h _ {s} ^ {(t - 1)} + b _ {s o}\right);\tag{5}
$$

Similarity network-based cell state:

$$
u _ {s} ^ {(t)} = \sigma \left(W _ {s u} x _ {s} ^ {(t)} + U _ {s u} h _ {s} ^ {(t - 1)} + b _ {s u}\right);\tag{6}
$$

Similarity network-based memory cell:

$$
c _ {s} ^ {(t)} = i _ {s} ^ {(t)} \circ u _ {s} ^ {(t)} + f _ {s} ^ {(t)} \circ c _ {s} ^ {(t - 1)};\tag{7}
$$

Similarity network-based hidden state:

$$
h _ {s} ^ {(t)} = o _ {s} ^ {(t)} \circ \tanh \left(c _ {s} ^ {(t)}\right).\tag{8}
$$

where $x _ { s } ^ { ( t ) }$ is the current input, and $h _ { s } ^ { ( t - 1 ) }$ is the previous hidden state. W, U, and b are weight parameters with values between 0 and 1. The gates $( i _ { s } ^ { ( t ) } , \ f _ { s } ^ { ( t ) }$ , and $o _ { s } ^ { ( t ) } )$ and memory cell $c _ { s } ^ { ( t ) }$ take the similarity network representation $x _ { s } ^ { ( t ) }$ at time step t and information from previous time steps in the last hidden state $h ^ { ( t - 1 ) }$ . Each forward or backward hidden state has 128 dimensions. We condense useful information from the 300-dimensional $x ^ { ( t ) }$ to 128 dimensions in the LSTM cell. The learning rate in gradient descent is 0.1. The dropout rate is 0.2. The above computation (BLSTM) is processed independently for the word embedding branch and the similarity network branch. These two branches are then fused together using element-wise sum as a multi-view learning framework. Figure 4 shows a graphic illustration of the model architecture. The red part indicates the innovation of this study.

The inputs to SINDEL are sentences from the research corpus. Each word in a sentence is represented with word embedding and the similarity network representation. At each timestep, two BLSTM layers process two representations of a sentence in parallel and generate two vectors of the same length as the input representation. These two vectors are merged using element-wise sum to maintain sequential information. Finally, this merged vector is passed to a Softmax layer to predict the word type (beginning of a barrier, inside of a barrier, or outside of a barrier).

![](/api/attachments/KWZ8EEV8/fulltext/images/9561feef90599d5c744d4b7f167bb3b69faa056b183c8023c295989409361eba.jpg)  
Figure 4. Similarity network-based deep learning architecture.

## OUD Treatment Barrier Clustering

Following the second step of aspect-based opinion mining, aspect clustering, we design a barrier clustering module. From drug reviews, SINDEL extracts OUD treatment barrier expressions, many of which may describe the same type of barriers. For instance, “expensive” and “cannot aford the treatment” both refer to the cost of treatments. Grouping similar aspect expressions, which are domain synonyms, is critical for efective opinion mining. We utilize a clustering method to identify the general types of OUD treatment barriers. As word embedding represents the semantic meaning of words in drug forums, we use word embedding as the features for the clustering model. Given a treatment barrier containing t words: $[ \boldsymbol { w } ^ { ( 1 ) } , \boldsymbol { w } ^ { ( 2 ) } , \dots , \boldsymbol { w } ^ { ( t ) } ]$ , the word embedding of each word is $[ x ^ { ( 1 ) } , x ^ { ( 2 ) } , \dots , x ^ { ( t ) } ]$ . The representation of this treatment barrier is the element-wise average over each dimension of the word embedding of those words (Equation 9). A salient number of studies utilized k-means for clustering. We, therefore, use the k-means clustering method to group OUD treatment barriers.

$$
x _ {b} = \frac {1}{t} \sum_ {i = 1} ^ {t} x ^ {(i)}.\tag{9}
$$

The methodological novelty of this study is three-folded. First, we design a new similarity network-based representation that can capture the relationships among morphs. This representation addresses the gap that existing semantic representations neglect word networks or graphs. Second, to consider two independent representations while incorporating meaningful information from both representations, we devise a multi-view learning framework. Third, we propose a barrier mining approach, including a classification module and a clustering module. This approach takes an innovative lens at social media data to unveil hidden patient behavior at a large scale. This automated approach ofers an opportunity for health IT researchers to study patient behavior with scalable analytical methods.

## Empirical Analyses

## Data Preparation

The research testbed comes from a popular drug discussion platform, Drugs-Forum.com. This platform enables OUD patients to interact with peers without being judged, because of the anonymity and the specificity of the platform. Patients on this platform elaborate on their drug use, addiction, and treatment experience, including illicit drug use, such as heroin, cocaine, and fentanyl. The research data contains narratives from the OUD patients’ perspective about illicit drugs and creates an unprecedented opportunity to extend the investigation on opioid addiction to an underrepresented population.

We collected the posts from Drugs-Forum related to drug use<sup>1</sup> (i.e., Buprenorphine, Methadone, and Opiate & Opioid addiction) from the start of Drugs-Forum to September 1, 2018. The raw dataset encompasses 27,154 posts, involving all prescription and illicit drugs in the forum, including amphetamine, cocaine, anti-depressants, tranquilizers, sleeping pills, 3,4-Methylenedioxymethamphetamine (MDMA), ethnobotanicals, gamma hydroxybutyrate (GHB), lysergic acid diethylamide (LSD), psilocybin mushroom, buprenorphine, hydrocodone, morphine, oxymorphone, codeine, hydromorphone, opium, heroin, oxycodone, methadone, and tramadol.

We randomly sampled 3,000 posts by repeatedly drawing a non-duplicate number between 1 and 27,154 using a random number generator. Four expert annotators reviewed these sampled posts and annotated the OUD treatment barriers for model training purposes. The inside, out, beginning (IOB) labeling scheme is adapted to assign tags for each word in a sentence. Each word has a label suggesting if it is inside (I), outside (O), or the beginning (B) of an expression of OUD treatment barriers. Figure 5 shows an example of the annotation. In model evaluations, if the predicted word label (I, O, or B) matches the true label, the prediction of this word is correct.

To test inter-annotator reliability, we leverage Cohen’s Kappa. The Kappa value for the OUD treatment barrier annotation is 0.92, indicating excellent reliability. A fifth expert annotator reviewed the disagreements and made the final judgment. We further segmented the posts into sentences with the sentence boundary detection package from NLTK. A total of 40,917 sentences were generated. We chose 70 percent of the annotated data as the training set, 10 percent as the validation set, and the remaining 20 percent as the test set. The summary statistics of the training and test set are shown in Table 3. The unit of analysis of the model is at the sentence level. The input to the model is a sentence while the output is a sequence of predicted word types in the input sentence. There are three diferent word types: B, I, and O, suggesting if a word is the beginning of, inside, or outside of a barrier. The post clustering analyses aggregate all the identified treatment barriers from all the sentences in a post.

## Baseline Models for Extracting OUD Treatment Barriers

Two classes of baseline methods are selected: conventional machine learning methods and deep learning methods. The conventional machine learning methods include SVM, Logistic Regression (LR), Naïve Bayes (NB), and CRF. To use SVM, LR, and NB for extracting OUD treatment barriers, we first use word2vec to represent each word as a feature vector and then feed the feature vectors into these classifiers respectively. These methods are implemented with the commonly adopted machine learning library scikit-learn. CRF is the most common machine learning sequence labeling model. We use CRFSuite to implement CRF. As SINDEL modifies standard deep learning models, we also benchmark SINDEL with three

<table><tr><td>I can not afford the treatment .O B I I O O .</td><td>OUD treatment barrier</td></tr></table>

## Figure 5. Annotation example.

Table 3. Summary statistics of training and test set.

<table><tr><td>Statistics</td><td>Training Set</td><td>Test Set</td></tr><tr><td>Number of posts</td><td>2,100</td><td>900</td></tr><tr><td>Number of sentences</td><td>27,128</td><td>13,789</td></tr><tr><td></td><td>483,052</td><td>232,797</td></tr><tr><td>Number of treatment barrier mentions</td><td>1,581</td><td>678</td></tr></table>

state-of-the-art deep learning models: RNN, LSTM, and BLSTM. These deep learning models are implemented using Keras. We also benchmark with attention-based SINDEL, SINDEL with the left branch only, and SINDEL with the right branch only.

## Evaluation Metrics

We adopt the common evaluation metrics in text mining—precision, recall, and F1 score— to assess the performance. Precision assesses how many OUD treatment barriers that the model retrieves are correct. Recall measures how many OUD treatment barriers in the research testbed the model can identify. F1 score is the harmonic average of precision and recall. In our study, we aim to extract as many OUD treatment barriers as possible and ensure the extracted barriers are accurate at the same time. Extracting more accurate OUD treatment barriers could operationalize more efective and complete intervention strategies, thus preventing unnecessary medical consequences. Therefore, F1 score is the most critical evaluation metric in our study.

## Evaluation of Extracting OUD Treatment Barriers

We evaluate our model on the annotated dataset and repeat the training procedure for each model 20 times and report the average performance in Table 4. SINDEL outperforms the conventional machine learning methods (SVM, LR, NB, and CRF) by a very large margin in F1 score and precision. While CRF achieves the highest precision (78.46 percent) among the baseline methods, SINDEL still outperforms CRF in precision by 6.85 percent. LR has the highest F1 score (50.01 percent) among the baseline methods. SINDEL manages to outperform LR in F1 score by 53.91 percent. NB achieves the highest recall, because it recognizes most instances as OUD treatment barriers (very low precision), which is not feasible for practical use. Since F1 score is the most important in this study, SINDEL is the best model for OUD treatment barrier mining. We conduct t-tests in R to compare the performance of SINDEL against the conventional machine learning baseline models. The t-test results indicate that our proposed SINDEL significantly outperforms all the baseline models (p < 0.001).

We also compare SINDEL with state-of-the-art deep learning methods. The results in Table 5 show that SINDEL outperforms RNN, LSTM, and BLSTM in all three evaluation metrics. BLSTM achieves the best results among the deep learning baseline methods due to the advantages of the bidirectional architecture. SINDEL improves upon BLSTM in precision by 4.15 percent, recall by 11.96 percent, and F1 score by 8.44 percent. The t-tests for SINDEL against the deep learning methods indicate the performance improvement of our

Table 4. SImilarity Network-based DEep Learning (SINDEL) vs. conventional machine learning methods.

<table><tr><td>Method</td><td>Precision (Percent)</td><td>Recall (Percent)</td><td>F1 score (Percent)</td></tr><tr><td>SVM</td><td>58.10***</td><td>40.09***</td><td>47.40***</td></tr><tr><td>LR</td><td>45.25***</td><td>61.15***</td><td>50.01***</td></tr><tr><td>NB</td><td>22.54***</td><td>95.50***</td><td>36.47***</td></tr><tr><td>CRF</td><td>78.46***</td><td>36.59***</td><td>49.90***</td></tr><tr><td>SINDEL (Ours)</td><td>85.31</td><td>70.14</td><td>76.97</td></tr></table>

Notes: SVM = support vector machine; LR = logistic regression; NB = Naïve Bayes; CRF = conditional random fields. $^ { * } p < 0 . 0 5 ;$ $^ { \star \star } p < 0 . 0 1 ; ^ { \star \star \star } p < 0 . 0 0 1$

Table 5. SImilarity Network-based DEep Learning (SINDEL) v.s. deep learning models.

<table><tr><td>Method</td><td>Precision (Percent)</td><td>Recall (Percent)</td><td>F1 score (Percent)</td></tr><tr><td>RNN</td><td>75.19***</td><td>48.49***</td><td>58.80***</td></tr><tr><td>LSTM</td><td>71.90***</td><td>54.48***</td><td>61.77***</td></tr><tr><td>SINDEL-Left (BLSTM)</td><td>81.91***</td><td>62.65***</td><td>70.98***</td></tr><tr><td>SINDEL-Right</td><td>80.76***</td><td>69.08</td><td>74.43*</td></tr><tr><td>SINDEL-ATT</td><td>80.02***</td><td>65.75***</td><td>72.18***</td></tr><tr><td>SINDEL (Ours)</td><td>85.31</td><td>70.14</td><td>76.97</td></tr></table>

Notes: RNN = recurrent neural network; LSTM = long short-term memory; BLSTM = bidirectional long short-term memory; SINDEL-ATT = SINDEL-Attention. \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

SINDEL is statistically significant. The superior performance of SINDEL against all the baseline methods in Tables 4 and Table 5 demonstrates the efectiveness of the proposed similarity network-based deep learning in extracting OUD treatment barriers.

To show the advantage of the similarity network branch in SINDEL, we conduct ablation studies. We test the performance of the left branch only (SINDEL-Left) and the right branch only (SINDEL-Right). The results are shown in Table 5. The right branch (similarity network branch) significantly outperforms the left branch. Combining the left and right branches fields the best performance over other baseline models. This result suggests the similarity network component contributes to the performance gain significantly.

As the attention mechanism shows promising results in deep learning studies, we add a self-attention mechanism in the right branch of SINDEL to search for the best model design. The result reported in Table 5 (SINDEL-ATT) indicates that adding the attention mechanism in SINDEL hampers the performance of SINDEL. Attention mechanism gives more weights to the important part of a sentence, which is useful in sentence-level prediction such as text classification. However, as we aim to predict a label for each word, enhancing the important part of a sentence does not benefit the prediction at a smaller granularity (word level). Attention mechanisms address the long-term dependency issue. The benefit of attention is not evident in drug forums because irrelevant topics emerge in long sentences, bringing in more noise than information gain. Therefore, we do not include the attention mechanism in our model.

In order to check the robustness of SINDEL’s advantages over deep learning methods, we conduct experiments with varying hyperparameters (the embedding size and the output dimension of BLSTM) in SINDEL and other baseline models. We choose the commonly adopted hyperparameter combinations (Online Supplemental Appendix A1) to perform grid search. Figures 6, Figures 7, and Figures 8 depict the performance of their precision, recall, and F1 score in this grid search. The results show SINDEL is robust and significantly outperforms SINDEL-ATT, SINDEL-Right, SINDEL-Left, BLSTM, LSTM, and RNN in all parameter combinations.

SINDEL utilizes word embedding and the similarity network as the representation. We utilize word2vec to generate word embedding in the previous analyses. We further test the robustness of our model by using other commonly adapted word embedding models, including locally-trained Skip-gram, GloVe, FastText [28], and SeVeN [16]. Table 6 shows the performance of these models.

The word2vec model reaches the best performance among all word embedding models. The locally-trained Skip-gram is inferior to word2vec because the word embedding training size is smaller than that of word2vec. GloVe also has lower performance than word2vec because many of the discussions in the entire dataset drift from OUD treatment. The global representation induces noisy information. Other state-of-the-art embedding models, including FastText and SeVeN, also result in lower performance than our approach. We further test the performance of SINDEL with various embedding models in diferent hyperparameter settings (the embedding size and the output dimension of BLSTM). Figures 9, Figures 10, and Figures 11 depict the performance curves of their precision, recall, and F1 score when the key parameters vary. The hyperparameter description and statistics are shown in Online Supplemental Appendix A2. The results indicate that the word2vec model is the best embedding model for SINDEL. The performance is also robust in various parameter settings. We, therefore, choose word2vec as the embedding model in SINDEL. SINDEL incorporates a word similarity network to address the challenge of various morphs of drugs and treatments. This similarity network representation for each word consists of a set of semantically similar words. We perform a sensitivity analysis to select the optimal network size in the similarity network representation. Figure 12 and Online Supplemental Appendix A3 summarize the sensitivity analysis results. We observe that the performance of SINDEL gradually improves when the network size grows from 1 to 3 words. Its performance stabilizes from 3 to 8 words with minor fluctuations. The performance decreases at 9 words due to over-complex model specifications.

![](/api/attachments/KWZ8EEV8/fulltext/images/759d17184075d86d9786a236a0cc834a413a2bc8f4805a22dd851532b4fcab40.jpg)  
Figure 6. Precision of SImilarity Network-based DEep Learning (SINDEL) and deep learning methods with varying parameters.

![](/api/attachments/KWZ8EEV8/fulltext/images/e1452d05718f2e7b78b14b848d19ae84843a6578b5c687b4df36757b32ea746a.jpg)  
Figure 7. Recall of SImilarity Network-based DEep Learning (SINDEL) and deep learning methods with varying parameters.

![](/api/attachments/KWZ8EEV8/fulltext/images/b21255cce7d91f8b115124989878bf537a56c63d7d3f9acb31b6ae5f8274d9c7.jpg)  
Figure 8. F1 Score of SImilarity Network-based DEep Learning (SINDEL) and deep learning methods with varying parameters.

Table 6. Evaluation of SImilarity Network-based DEep Learning (SINDEL) using diferent embeddings.

<table><tr><td>Method</td><td>Precision (Percent)</td><td>Recall (Percent)</td><td>F1 score (Percent)</td></tr><tr><td>SINDEL with Skip-gram</td><td>80.09***</td><td>68.56**</td><td>73.87***</td></tr><tr><td>SINDEL with GloVe</td><td>83.84*</td><td>59.14***</td><td>69.33***</td></tr><tr><td>SINDEL with FastText</td><td>80.34***</td><td>67.10***</td><td>73.10***</td></tr><tr><td>SINDEL with SeVeN</td><td>81.42***</td><td>68.71</td><td>74.51***</td></tr><tr><td>SINDEL (Ours)</td><td>85.31</td><td>70.14</td><td>76.97</td></tr></table>

Notes: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

Figure 12 shows that the performance of SINDEL is the highest when the network size is 3, 7, or 8 words. To select the best network size in the similarity network representation, we conduct t-tests to show their performance diferences. The t-test results in Table 7 indicate the performance has no significant diference when the network size is 3, 7, or 8 words. Therefore, we select 3 similar words in the similarity network representation because the computational complexity is the lowest and performance is the highest.

The similarity network representation captures the interconnected relationships among similar morphs, thus identifying more morphs of OUD treatment barriers together with the original term. In Table 8, we show examples of the additional morphs that the similarity network could capture. In addition to heroin, the similarity network could capture dopesick, H, and chinawhite. Therefore, OUD treatment barriers mentioned together with dopesick, H, and chinawhite could be identified as well. Ache is a withdrawal reaction after treatment, which can be a barrier that prevents patients from receiving treatment. Other types of barrier symptoms (achey, sore, bites) are also extracted by the similarity network. Methadone is an OUD treatment medication. Patients may mention it when describing treatment barriers, such as methadone addiction and withdrawal. Morphs of methadone, such as meth, M, and MMT, are extracted together to improve the model performance.

![](/api/attachments/KWZ8EEV8/fulltext/images/c7e129a29009c0b9fffb26216d95129ae4108593c9ea874edc195fb33ec8e8ca.jpg)  
Figure 9. Precision of SImilarity Network-based DEep Learning (SINDEL) using diferent word embeddings with varying parameters.

![](/api/attachments/KWZ8EEV8/fulltext/images/9d0680af84296497fbe9b14db6aabaf9d9cb28885373aea3198f369ee3adcf57.jpg)  
Figure 10. Recall of SImilarity Network-based DEep Learning (SINDEL) using diferent word embeddings with varying parameters.

![](/api/attachments/KWZ8EEV8/fulltext/images/ffe5b3f6f5d9636c16f4d3ebf491fc2d598d2bbdb2ad3e4db9f2a7fc926a34a0.jpg)  
Figure 11. F1 Score of SImilarity Network-based DEep Learning (SINDEL) using diferent word embeddings with varying parameters.

![](/api/attachments/KWZ8EEV8/fulltext/images/568a94c656a18ddecae3d475db5d72e2603b77d844c173f56ea181397d5092fe.jpg)  
Figure 12. SImilarity Network-based DEep Learning (SINDEL’s) performance with varying number of similar words.

Table 7. P-Value of T-tests for the Results with Diferent Network Sizes.

<table><tr><td>Pairwise T-tests</td><td>P-value (Precision)</td><td>P-value (Recall)</td><td>P-value (F1 score)</td></tr><tr><td>3 similar words vs 7 similar words</td><td>0.953</td><td>0.234</td><td>0.188</td></tr><tr><td>3 similar words vs 8 similar words</td><td>0.669</td><td>0.196</td><td>0.271</td></tr><tr><td>7 similar words vs 8 similar words</td><td>0.648</td><td>0.888</td><td>0.946</td></tr></table>

## Clustering OUD Treatment Barriers

We apply SINDEL to extract OUD treatment barriers from the entire research data. We, then, leverage K-means to identify the general types of barriers. K-means generated 40 clusters of barriers. To choose the optimal number of clusters, a medical expert panel, including two biomedical researchers, examined these clusters for medical relevance. The panel merged the clusters that have similar medical relevance. Thirteen clusters are identified by the expert panel. Table 9 shows the types of OUD treatment barriers. To evaluate the reliability of the 13 clusters, an independent biomedical researcher read a random sample of 1,000 barriers and labeled the barrier types. Among these 1,000 barriers, 876 (87.6 percent) share the same barrier type as labeled by the clustering model, indicating good reliability.

Table 8. Examples of morphs captured by the similarity network representation.

<table><tr><td>Original Term</td><td>Similar Morphs Captured by the Similarity Network</td></tr><tr><td>Heroin</td><td>Dopesick, H, chinawhite</td></tr><tr><td>Ache</td><td>Achey, sore, bites</td></tr><tr><td>Methadone</td><td>Meth, M, MMT</td></tr></table>

The results shed valuable insights to understand patient’s decisions about receiving OUD treatment. Lack of motivation is the most common barrier to receiving OUD treatments (24.67 percent). Prior survey shows that self-motivation is a prominent reason for longterm recovery from opioid addiction [18]. Although these patients are aware of the consequences of addiction, they postpone visits to health providers. To motivate these patients, community support, family encouragement, and follow-ups from the clinics are essential. While physically attending support group meetings or counseling may be infeasible for patients who have chronic conditions and disability, virtual support communities can form in online forums and provide recovering patients with support beyond that of traditional counseling.

Table 9. Types of opioid use disorder (OUD) treatment barriers.

<table><tr><td>Type</td><td>Description</td><td>Percentage</td><td>Examples</td></tr><tr><td>Lack of motivation</td><td>The patient does not have motivation to quit opioids</td><td>24.67</td><td>Don&#x27;t have time to go to a clinic, CANT stop, don&#x27;t want to quit</td></tr><tr><td>Lack of medical literacy</td><td>The patient lacks knowledge of consequences of addiction</td><td>21.88</td><td>Wasting time, dying of boredom, don&#x27;t have desire to be clean</td></tr><tr><td>Concerns about social stigma and job opportunities</td><td>The patient is concerned about social stigma or afraid of losing jobs</td><td>12.67</td><td>Fails a pre employment drug screen, new job requires no drug or medication use</td></tr><tr><td>Afraid of withdraw reactions</td><td>The patient is afraid of the withdrawals after quitting</td><td>12.35</td><td>Hate withdrawals, precipitated withdrawals</td></tr><tr><td>Side effects of treatment</td><td>The patient is concerned about the side effects of treatment</td><td>9.13</td><td>Headaches, migraines, insomnia</td></tr><tr><td>Reliance because of chronic pain/fatigue</td><td>The patient cannot stop opioids because of chronic pain</td><td>5.64</td><td>I&#x27;m sick in pain, chronic pain flares up</td></tr><tr><td>Concerns about buprenorphine/ methadone addiction</td><td>The patient is concerned about buprenorphine or methadone addiction</td><td>3.85</td><td>Methadone addiction</td></tr><tr><td>High cost of treatment</td><td>The patient cannot afford the treatment or insurance does not cover</td><td>2.91</td><td>Expensive, unaffordable</td></tr><tr><td>Poor patient-physician relationship</td><td>The patient does not have good relationship with the providers</td><td>2.19</td><td>Clinic denies me, doc was pissed</td></tr><tr><td>Enjoy euphoric feeling of drugs</td><td>The patient enjoys the euphoric feeling of opioids and does not want to quit</td><td>1.70</td><td>Like dope, craving</td></tr><tr><td>Depressed mental status</td><td>The patient is depressed and does not want to receive treatment</td><td>1.57</td><td>Severe depression</td></tr><tr><td>Lack of accessibility</td><td>Treatment is not accessible to patients</td><td>0.63</td><td>No rehab</td></tr><tr><td>Others</td><td>Others</td><td>0.82</td><td>Can&#x27;t, good</td></tr></table>

Lack of health literacy prevails as a common barrier for OUD treatment. Recent studies in medicine have identified that health literacy has a significant negative association with opioid misuse and the severity of opioid dependence [49]. Our findings revealed that patients may not understand the ramifications of opioid addiction due to health literacy and sufer from prolonged harm caused by OUD. Interventions targeting health literacy among this group of patients may help to address the opioid public health crisis. Online forums ofer the medium to raise awareness of OUD and quality health resources from reliable channels, while the data driven approach can help identify the audience in need. Other types of barriers to OUD treatment include social stigma and fear of job loss, withdrawal reactions and side efect of treatment, physical reliance, concerns about methadone or buprenorphine addiction, cost of treatment, poor patient-physician relationship, euphoric feeling, mental status, lack of accessibility, and more.

In addition to the barriers that confirm prior literature, we also uncovered new barriers that have not been noted in prior survey studies, such as side efects of treatment, concerns about buprenorphine or methadone addiction, poor patient-physician relationships, and depressed mental status. These barriers have not been identified by survey studies because these barriers are sensitive and involve personal behavior. The patients are willing to share these undisclosed opinions in drug forums because of the anonymity. Uncovering these new barriers enables a deeper understanding of patients’ opioid addiction behavior and facilitates more efective intervention strategies. For instance, poor patient-physician relationship prevents patients from seeking addiction treatment. Overlooking this perspective devastates the eforts of other stakeholders. In order to improve opioid addiction management, health providers need to foster a healthy relationship with their patients. Depressed patients also have little motivation to seek treatments. This new finding provides guidance for caregivers to treat the depression disorder of the patients together with OUD. The new findings further prove the value of social media platforms in opioid research. Future studies could also harness health social media to understand many other patient behaviors, such as medication compliance and drug abuse.

As our automated method could continuously collect data and provide up-to-date insights about emerging treatment barriers, our method could be utilized as a surveillance tool to unveil more new barriers over time. It also assists proactive decision-making. Key stakeholders, such as hospitals, health providers, insurance companies, and policymakers, could ensure the barriers related to their side are properly dealt with for new patients.

## Second Case Study in Extracting Barriers to Medication Adherence

In order to test the generalizability of SINDEL, we evaluate SINDEL on a diferent context with a diferent dataset. SINDEL is designed to discover barriers to human decision-making in textual data. We leverage SINDEL to extract the barriers to medication adherence from WebMD forum data. We collected 233,325 sentences from 53,180 reviews about 180 drugs in WebMD. These reviews are patient self-reported experience of taking medications, many of which contain information of the barriers to medication adherence. In the same manner of extracting OUD treatment barriers, we extract the phrases about barriers to medication adherence. We randomly selected 5,400 sentences for annotation. The annotation scheme is

Table 10. Evaluation of SImilarity Network-based DEep Learning (SINDEL) in medication nonadherence case.

<table><tr><td>Method</td><td>Precision (Percent)</td><td>Recall (Percent)</td><td>F1 score (Percent)</td></tr><tr><td>SVM</td><td>68.91***</td><td>79.64***</td><td>73.89***</td></tr><tr><td>LR</td><td>68.73***</td><td>80.63***</td><td>74.21***</td></tr><tr><td>NB</td><td>41.30***</td><td>71.21***</td><td>52.28***</td></tr><tr><td>CRF</td><td>94.00***</td><td>46.30***</td><td>62.04***</td></tr><tr><td>RNN</td><td>83.72***</td><td>81.60***</td><td>82.57***</td></tr><tr><td>LSTM</td><td>85.43***</td><td>82.24***</td><td>83.76***</td></tr><tr><td>BLSTM</td><td>88.26</td><td>85.94**</td><td>87.06***</td></tr><tr><td>SINDEL-ATT</td><td>87.73</td><td>86.56**</td><td>87.12***</td></tr><tr><td>SINDEL-Right</td><td>87.80</td><td>87.05***</td><td>87.39***</td></tr><tr><td>SINDEL (Ours)</td><td>88.13</td><td>88.09</td><td>88.10</td></tr></table>

Notes: SVM = support vector machine; LR = logistic regression; NB = Naïve Bayes; CRF = conditional random fields; RNN = recurrent neural network; LSTM = long short-term memory; BLSTM = bidirectiona long short-term memory; SINDEL-ATT = SINDEL-Attention.

IOB. Five expert annotators independently annotated these sentences in five batches. A sixth expert annotator reviewed all sentences independently. The Kappa value is 0.98, indicating excellent reliability. The performance of SINDEL and the benchmarks are reported in Table 10.

In the medication nonadherence context using WebMD data, SINDEL consistently outperforms all the baseline models. Using the WebMD data, we further compare SINDEL with alternative representations, including Skip-gram, GloVe, FastText, and SeVeN. The results, reported in Online Supplemental Appendices A8 and A9, show that SINDEL outperforms all the other representations. In order to test the robustness of SINDEL in diferent parameter settings in the medication nonadherence context, we evaluate SINDEL, baseline models, and alternative representations in the 36 hyperparameter settings used in the OUD experiments (Online Supplemental Appendix A7). SINDEL is able to consistently achieve the best performance, as reported in Online Supplemental Appendices A4-A6. We also performed robustness checks of diferent representations (SINDEL, Skip-gram, GloVe, FastText, and SeVeN) on diferent hyperparameter settings. The results, reported in Online Supplemental Appendix A10, suggest SINDEL is the best model among other representations in all hyperparameter settings.

## Discussion

## Contributions to IS Literature

This study seeks to address a high-impact health IT problem with significant societal relevance: opioid use disorder. Following the design science research guidelines, we develop a novel information system to understand the barriers to OUD treatments and conduct comprehensive and rigorous evaluations of this information system. This system can be utilized by multiple stakeholders in IS and healthcare. The design principles in the proposed method, including model selection, parameter settings, and model architecture, provides methodological and practical implications for IS research.

This study also fits into the computational data science research [48]. The computational data science research emphasizes an “interdisciplinary approach in developing novel data representations, computational algorithms, business intelligence, and analytics methods”

[48]. Our study develops an interdisciplinary approach that involves a novel computational algorithm and an analytical solution to a major healthcare problem, thus holding great potential for generating IS research with significant societal impact. Such impact includes the capability of advancing the understanding of OUD treatment issues from drug users perspective and discovering useful information from multi-scale biomedical data to support healthcare delivery.

In the same spirit of social media-based IS research [4, 30, 31, 63], we leverage an IT system from an online health community, opioid forums, to assist the understanding of opioid addiction. This new IT-enabled application ofers unprecedented scale and potential to deepen the investigation of the opioid crisis.

## Methodological Implications for IS

We devise a deep learning framework to extract OUD treatment barriers from social media, including OUD treatment barrier extraction and clustering. This framework can be adapted to many other IS research problems aiming to understand barriers to human behaviors. For instance, this framework could be utilized to extract the barriers to technology adoption, the barriers to investing in projects, and the barriers to medication adherence, among others. We develop a fine-grained deep learning model that captures the semantic meaning of words and the similarity network of text. Our proposed model improves upon standard deep learning models with a novel similarity network-based representation and a multi-view deep learning architecture. The similarity network-based component captures the interconnected relationships among morphs in drug forums. As shown in the empirical analyses, the similarity network helps identify many more OUD treatment barriers that are written as morphs. With this new method, patient intelligence can be fruitfully exploited from health social media. This method can be generalized to many other information retrieval tasks that involve morphs, such as cyber threat identification in hacker forums, aspect mining in product reviews, and drug surveillance in health social media. Table 11 shows the specific implications.

## Contributions to Design Theory

In line with [24], this study proposes a novel analytics method as an IT artifact. This IT artifact contributes four general design principles to design theory: 1) Incorporating word networks into language models could disentangle complex word semantics; 2) Designing multi-dimensional data representations (word embedding and network embedding) could enrich representation learning; 3) A subsequent clustering module after classification modules could provide interpretable and actionable insights for prescriptive analytics; 4) Knowledge discovery on social media could complement survey-based approaches on human behavior understanding. These design principles ofer generalized implications for other design science research, especially in social media analytics. To ensure problem relevance, we stressed the technical challenges in health social media mining as well as its significance. Guided by the technical challenges, we summarized the plausible methods and proposed the best approach through conceptual and empirical model selection. The model selection process and hyperparameter tuning could be leveraged as a generalized design guideline for other social media mining studies in IS.

Table 11. Methodological implications for other information systems research.

<table><tr><td>Domain</td><td>Data</td><td>Morphs</td><td>Implications Using Similarity Network-based DEep Learning (SINDEL)</td></tr><tr><td>Cybersecurity</td><td>Hacker forums</td><td>Hacker slang</td><td>Identify hacking tools</td></tr><tr><td>Ecommerce</td><td>Product reviews</td><td>Consumer vocabulary</td><td>Extract product features</td></tr><tr><td>Health analytics</td><td>Health social media</td><td>Drug street names</td><td>Extract drug adverse events</td></tr></table>

## Managerial Implications

This study is among the first attempts to explore drug forums to understand patient decisionmaking about OUD treatment. Many new OUD treatment barriers are uncovered from patient narratives in drug forums. Our findings provide valuable implications for key stakeholders, including patients, caregivers, health providers, insurers, and policymakers. Poor medical literacy significantly prohibits patients from receiving OUD treatment. Awareness of the barriers to OUD treatment can provide patients with social and informational support and motivate them to participate in online health communities to improve their understanding of opioid addiction. Caregivers play an important role in improving OUD treatment. Many patients lack the motivation or information to receive treatment. Caregivers need to actively seek treatment information and encourage patients to seek medical assistance. Understanding the treatment barriers also help caregivers seek targeted assistance to connect patients to practitioners. Poor patient-physician relationship could hinder patients’ attempt to seek OUD treatment. Health providers could reinforce their relationship with patients and provide informational support for patients. Our automated model can also actively collect social media data and identify emerging treatment barriers which assist physicians’ decisionmaking. Insurance plan design can encourage or discourage treating OUD. Patients with high-deductible insurance plans are less likely to receive treatments because of the financial burden. Insurance plans could encourage patients to receive treatments by reducing the copayments and deductibles. A comprehensive examination of OUD treatment barriers also provides a holistic view of the opioid crisis. Policymakers could design intervention policies to tackle these treatment barriers and ensure stakeholders all work in line with the same objective. The proposed analytical method also serves as a decision support system for policymakers to monitor emerging public health problems about opioids. We summarize the managerial implications for each stakeholder in the Table 12.

## Limitations and Future Directions

Our study has several limitations and areas for improvement. First, we incorporated a similarity network into our model as a multi-view learning framework. Future research can explore alternative mechanisms to integrate two representations. Second, although our framework can be generalized to process other text containing morphs, we only tested our method on opioid forums and WebMD. To extend this research and expand the external validity, future studies could use our framework to understand the barriers to technology adoption, barriers to investing in projects, and more. Third, the barriers identified in this study are the most direct barriers. These barriers could potentially be further caused by other indirect reasons. As the users only report the most direct barriers, we are not able to observe the hidden barriers. Despite this limitation, the most direct barrier ofers the more direct and efective intervention insights.

Table 12. Managerial implications for stakeholders.

<table><tr><td>Stakeholder</td><td>IT Artifact</td><td>Implication</td></tr><tr><td>Patients</td><td>Treatment barriers</td><td>Raise awareness of barriers and solutions</td></tr><tr><td>Caregivers</td><td>Treatment barriers</td><td>Raise awareness of barriers and solutions</td></tr><tr><td>Physicians</td><td>Treatment barriers, analytical method</td><td>Monitor barriers using our method and intervene actively</td></tr><tr><td>Insurers</td><td>Treatment barriers</td><td>Address barriers resulted from insurance limitation</td></tr><tr><td>Policymakers</td><td>Treatment barriers, analytical method</td><td>Monitor opioid users&#x27; behavior and public health crisis using the automated method</td></tr></table>

## Conclusion

OUD is an urgent public health crisis that causes serious medical and financial ramifications. Understanding OUD treatment barriers forms the premise to alleviate this crisis. Our research aims to develop a computational approach to understanding OUD treatment barriers from the patients’ perspective. We designed a novel deep-learning-based approach, SINDEL, to collect relevant patient discussions from drug forums, extract the OUD treatment barriers, and analyze the types of barriers. This is among the first attempts to analyze OUD treatment barriers from large-scale health social media data. We identified common barriers to OUD treatment, such as lack of medical literacy, concerns about job loss, concerns about withdrawal reactions and side efects, and more. Knowing these barriers, the key stakeholders, including physicians, patients, policymakers, pharmaceutical companies, and healthcare systems, could gain rich insights from the patient perspective and take proactive interventions to avoid harmful outcomes.

In line with the design science research methodology, we rigorously evaluated our model and compared it with state-of-the-art baseline models in two diferent contexts and two diferent datasets. SINDEL outperforms all the baseline models, attributed to the similarity network-based component. SINDEL can be generalized in many other information retrieval tasks involving morphs and applied to extract consumers’ opinion and understand their decision-making in various business contexts.

## Notes

1. We only select drug use-related subforums, such as methadone, opiate, and opioid addiction, and more. We do not collect the subforums irrelevant to drug use, such as drug laws and forum announcement.

## Acknowledgements

This work was supported in part by the following grants: Grant Nos. 2020AAA0108401, 2017YFC0820105, 2019QY(Y)0101, and 2020AAA0103405 from the Ministry of Science and Technology of China, Grant No. 2017ZX10303401-002 from the Ministry of Health of China, and Grant Nos. 71621002, 72074209, 71974187, and 71472175 from the National Natural Science Foundation of China. Part of the experiments were run on the El Gato supercomputer that was supported by the National Science Foundation under Grant No. 1228509.

## References

1. Abbasi, A.; Albrecht, C.; Vance, A.; and Hansen, J. Metafraud: A meta-learning framework for detecting financial fraud. MIS Quarterly, 36, 4 (2012), 1293–1327.

2. Abbasi, A.; and Chen, H. CyberGate: a design framework and system for text analysis of computer-mediated communication. MIS Quarterly, 32, 4 (2008), 811–837.

3. Abbasi, A.; Zhang, Z.; Zimbra, D.; Chen, H.; and Nunamaker, J.F. Detecting fake websites: The contribution of statistical learning theory. MIS Quarterly, 34, 3 (2010), 435–461.

4. Abbasi, A.; Zhou, Y.; Deng, S.; and Zhang, P. Text analytics to support sense-making in social media: A language-action perspective. MIS Quarterly, 42, 2 (2018), 427–464.

5. Agarwal, R.; and Dhar, V. Big data, data science, and analytics: The opportunity and challenge for IS research. Information Systems Research, 25, 3 (2014), 443–448.

6. Andrilla, C.H.A.; Coulthard, C.; and Larson, E.H. Barriers rural physicians face prescribing buprenorphine for opioid use disorder. Annals of Family Medicine, 15, 4 (July 2017), 359–362.

7. Aral, S.; and Walker, D. Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Science, 57, 9 (2011), 1623-1639.

8. Baesens, B.; Bapna, R.; Marsden, J.R.; Vanthienen, J.; and Zhao, J.L. Transformational issues of big data and analytics in networked business. MIS Quarterly, 40, 4 (2016), 807–818.

9. Baldwin, T.; Kim, Y.-B.; Catherine De Marnefe, M.; Ritter, A.; Han, B.; and Xu, W. Shared Tasks of the 2015 Workshop on Noisy User-generated Text: Twitter Lexical Normalization and Named Entity Recognition. Proceedings of the ACL 2015 Workshop on Noisy User-generated Text, 2015, pp. 126-135.

10. Bojko, M.J.; Mazhnaya, A.; Marcus, R.; Islam, Z.; Filippovych, S.; Dvoriak, S.; Altice, FL. The future of opioid agonist therapies in Ukraine: A qualitative assessment of multilevel barriers and ways forward to promote retention in treatment. Journal of Substance Abuse Treatment, 66, (July 2016), 37–47.

11. Bughin, J.; and Chui, M. The rise of the networked enterprise : Web 2.0 finds its payday. McKinsey Quarterly, 4(2010), 1–6.

12. Capurro, D.; Cole, K.; Echavarría, M.I.; Joe, J.; Neogi, T.; and Turner, A.M. The use of social networking sites for public health practice and research: A systematic review. Journal of medical Internet research, 16, 3 (March 2014), e79.

13. Chen, H. Call for papers MISQ special issue on the role of information systems and analytics in chronic disease prevention and management. MIS Quarterly, 41, 1 (2017), 1–3.

14. Chen, H.; Chiang, R.H.L.; and Storey, V.C. Business intelligence and analytics: From big data to big impact. MIS Quarterly, 36, 4 (2012), 1165–1188.

15. Council of Economic Advisers. The Underestimated Cost of the Opioid Crisis. Executive Ofice of the President of the United States, Council of Economic Advisers; 2017.

16. Espinosa-Anke, L.; and Schockaert, S. SeVeN: Augmenting word embeddings with unsupervised relation vectors. (August 2018), pp.2653–2665.

17. Fang, X.; Hu, P.J.H.; Li, Z.L.; and Tsai, W. Predicting adoption probabilities in social networks. Information Systems Research, 24, 1 (March 2013), 128–145.

18. Flynn, P.M.; Joe, G.W.; Broome, K.M.; Simpson, D.D.; and Brown, B.S. Recovery from opioid addiction in DATOS. Journal of Substance Abuse Treatment, 25, 3 (2003), 177–186.

19. Goh, J.M.; Gao, G.; and Agarwal, R. The creation of social value: Can an online health community reduce rural-urban health disparities? MIS Quarterly, 40, 1 (2016).

20. Gregor, S.; and Hevner, A. Positioning and presenting design science research for maximum impact. MIS Quarterly, 37, 2 (June 2013), 337–355.

21. Hassamal, S.; Goldenberg, M.; Ishak, W.; Haglund, M.; Miotto, K.; and Danovitch, I. Overcoming barriers to initiating medication-assisted treatment for heroin use disorder in a general medical hospital. Journal of Psychiatric Practice, 23, 3 (May 2017), 221–229.

22. He, Y.; Chakrabarti, K.; Cheng, T.; and Tylenda, T. Automatic discovery of attribute synonyms using query logs and table corpora. In International World Wide Web Conferences Steering Committee, 2016, pp. 1429–1439.

23. Hemmatian, F.; and Sohrabi, M.K. A survey on classification techniques for opinion mining and sentiment analysis. Artificial Intelligence Review, 52, 3 (2019), 1495–1545.

24. Hevner, A.R.; March, S.T.; Park, J.; and Ram, S. Design science in information systems research. MIS Quarterly, 28, 1 (2004), 75–105.

25. Huang, C.-Y.; Chen, M.-H.; and Ku, L.-W. Towards a better learning of near-synonyms: automatically suggesting example sentences via fill in the blank. In International World Wide Web Conferences Steering Committee, 2017, pp. 293–302.

26. Hutchinson, E.; Catlin, M.; Andrilla, C.H.A.; Baldwin, L.-M.; and Rosenblatt, R.A. Barriers to primary care physicians prescribing buprenorphine. Annals of Family Medicine, 12, 2 (March 2014), 128–133.

27. Jeyapriya, A.; and Selvi, C.S.K. Extracting aspects and mining opinions in product reviews using supervised learning algorithm. In 2015 2nd International Conference on Electronics and Communication Systems (ICECS). IEEE, 2015, pp. 548–552.

28. Joulin, A.; Grave, E.; Bojanowski, P.; Douze, M.; Jégou, H.; and Mikolov, T. FastText.zip: Compressing text classification models. arXiv preprint arXiv:1612.03651. (December 2016).

29. Kallinikos, J.; and Tempini, N. Patient data as medical facts: Social media practices as a foundation for medical knowledge creation. Information Systems Research, 25, 4 (2014), 817–833.

30. Karahanna, E.; Xu, S.X.; Xu, Y.; and Zhang, N. The needs-afordances-features perspective for the use of social media. MIS Quarterly, 42, 3 (2018), 737–756.

31. Kitchens, B.; Dobolyi, D.; Li, J.; and Abbasi, A. Advanced customer analytics: Strategic value through integration of relationship-oriented big data. Journal of Management Information Systems, 35, 2 (2018), 540–574.

32. Knudsen, H.K.; Abraham, A.J.; and Oser, C.B. Barriers to the implementation of medication-assisted treatment for substance use disorders: The importance of funding policies and medical infrastructure. Evaluation and Program Planning, 34, 4 (November 2011), 375–381.

33. Krieger Pharm. D. C. What are opioids and why are they dangerous? Mayo Clinic, (2018). Retrieved on February 20, 2021: https://newsnetwork.mayoclinic.org/discussion/what-areopioids-and-why-are-they-dangerous/

34. Lau, R.; Liao, S.; Wong, K.F.; and Chiu, D. Web 2.0 Environmental scanning and adaptive decision support for business mergers and acquisitions. MIS Quarterly, 36, 4 (2012), 1239–68.

35. Li, S.; Zhou, L.; and Li, Y. Improving aspect extraction by augmenting a frequency-based method with web-based similarity measures. Information Processing and Management, 51, 1 (2015), 58–67.

36. Liu, B. Sentiment Analysis and Opinion Mining. Synthesis lectures on human language technologies, 5, 1 (2012), 1–67.

37. Livingston, J.D.; Adams, E.; Jordan, M.; MacMillan, Z.; and Hering, R. Primary care physicians’ views about prescribing methadone to treat opioid use disorder. Substance Use and Misuse, 53, 2 (January 2018), 344–353.

38. Luo, W.; Zhuang, F.; Cheng, X.; He, Q.; and Shi, Z. Ratable aspects over sentiments: Predicting ratings for unrated reviews. In Proceedings - IEEE International Conference on Data Mining, ICDM. 2014, pp. 380–389.

39. Ma, B.; Zhang, N.; Liu, G.; Li, L.; and Yuan, H. Semantic search for public opinions on urban afairs: A probabilistic topic modeling-based approach. Information Processing and Management, 52, 3 (2016), 430–445.

40. Mai, F.; Shan, Z.; Bai, Q.; Wang, X. (Shane); and Chiang, R.H.L. How does social media impact bitcoin value? A test of the silent majority hypothesis. Journal of Management Information Systems, 35, 1 (2018), 19–52.

41. McKenna, R.M. Treatment use, sources of payment, and financial barriers to treatment among individuals with opioid use disorder following the national implementation of the ACA. Drug and Alcohol Dependence, 179, (October 2017), 87–92.

42. Nguyen, K.A.; im Walde, S.S.; and Vu, N.T. Integrating distributional lexical contrast into word embeddings for antonym-synonym distinction. arXiv preprint arXiv:1605.07766.2016.

43. NIDA. Overview | National Institute on Drug Abuse (NIDA). 2018. Retrieved on February 20, 2021: https://www.drugabuse.gov

44. Nogueira, C.; Santos, D.; and Zadrozny, B. Learning Character-level representations for part-ofspeech tagging. In International Conference on Machine Learning, 2014 Jun 18 (pp. 1818-1826). PMLR.

45. Pew Research. 61% of American adults look online for health information | Pew Research Center’s Internet & American Life Project. Pew Research Center, 2009. Retrieved on February 20, 2021: https://www.pewresearch.org/internet/2009/06/11/61-of-american-adults-lookonline-for-health-information/

46. Qiu, G.; Liu, B.; Bu, J.; and Chen, C. Opinion word expansion and target extraction through double propagation. Computational Linguistics, 37, 1 (2011), 9–27.

47. Qu, M.; Ren, X.; and Han, J. Automatic synonym discovery with knowledge bases. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2017, pp. 997–1005.

48. Rai, A. Editor’s comments: Diversity of design science research. MIS Quarterly, 41, 1 (2017), iii–xviii.

49. Rogers, A.H.; Bakhshaie, J.; Orr, M.F.; Ditre, J.W.; and Zvolensky, M.J. Health literacy, opioid misuse, and pain experience among adults with chronic pain. Pain medicine (Malden, Mass.), 21, 4 (2020), 670–676.

50. Rubenstein, H.; and Goodenough, J.B. Contextual correlates of synonymy. Communications of the ACM, 8, 10 (October 1965), 627–633.

51. Saboo, A.R. Using big data to model time-varying efects for marketing resource (RE) allocation. MIS Quarterly, 40, 4 (2016), 911–939.

52. Sha, Y.; Shi, Z.; Li, R.; Liang, Q.; and Wang, B. Resolving entity morphs based on characterword embedding. Procedia Computer Science, 108, (2017), 48–57.

53. Sharma, A.; Kelly, S.M.; Mitchell, S.G.; Gryczynski, J.; O’Grady, K.E.; and Schwartz, R.P. Update on barriers to pharmacotherapy for opioid use disorders. Current Psychiatry Reports, 19, 6 (June 2017), 35.

54. Simpson, S.S.; Adams, N.; Brugman, C.M.; and Conners, T.J. Detecting novel and emerging drug terms using natural language processing: A social media corpus study. JMIR Public Health and Surveillance, 4, 1 (January 2018), e2.

55. Smith, C.A.; and Wicks, P.J. PatientsLikeMe: Consumer health vocabulary as a folksonomy. In AMIA Symposium. 2008, p. 682. American Medical Informatics Association.

56. Stieglitz, S.; and Dang-Xuan, L. Emotions and information difusion in social media - Sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29, 4 (2013), 217–248.

57. Stumbo, S.P.; Yarborough, B.J.H.; McCarty, D.; Weisner, C.; and Green, C.A. Patient-reported pathways to opioid use disorders and pain-related barriers to treatment engagement. Journal of Substance Abuse Treatment, 73, (February 2017), 47–54.

58. Tang, Q.; Gu, B.; and Whinston, A. Content contribution for revenue sharing and reputation in social media: A dynamic structural model. Journal of Management Information Systems, 29, 2 (October 2012), 41–76.

59. Trusov, M.; Bodapati, A. V.; and Bucklin, R.E. Determining influential users in internet social networks. Journal of Marketing Research, 47, 4 (August 2010), 643–658.

60. Samhsa. Results from the 2010 National Survey on Drug Use and Health: Detailed Tables. (2011). Retrieved on February 20, 2021: https://www.samhsa.gov/data/sites/default/files/ NSDUHNationalFindingsResults2010-web/2k10ResultsRev/NSDUHresultsRev2010.pdf

61. Xie, K.; and Lee, Y.J. Social media and brand purchase: Quantifying the efects of exposures to earned and owned social media activities in a two-stage decision making model. Journal of Management Information Systems, 32, 2 (April 2015), 204–238.

62. Yao, Z.; Sun, Y.; Ding, W.; Rao, N.; and Xiong, H. Dynamic word embeddings for evolving semantic discovery. In Proceedings of the eleventh acm international conference on web search and data mining, 2018, pp. 673–681.

63. Zhang, D.; Zhou, L.; Kehoe, J.L.; and Kilic, I.Y. What online reviewer behaviors really matter? Efects of verbal and nonverbal behaviors on detection of fake online reviews. Journal of Management Information Systems, 33, 2 (April 2016), 456–481.

64. Zhang, L.; and Liu, B. Aspect and entity extraction for opinion mining. In Data mining and knowledge discovery for big data, Springer Berlin Heidelberg, 2014, pp. 1–40.

65. Zhang, W.; and Ram, S. A comprehensive analysis of triggers and risk factors for asthma based on machine learning and large heterogeneous data sources. MIS Quarterly

66. Zhang, Y.; Jatowt, A.; Bhowmick, S.S.; and Tanaka, K. The past is not a foreign country: Detecting semantically similar terms across time. IEEE Transactions on Knowledge and Data Engineering, 28, 10 (October 2016), 2793–2807.

## About the Authors

Jiaheng Xie (jxie@udel.edu; corresponding author) is an assistant professor in the Department of Accounting and MIS at the University of Delaware’s Alfred Lerner College of Business and Economics. His research interests lie in deep learning, health risk analytics and business analytics. Dr. Xie’s prior work has been published or is under review at several leading journals, including MIS Quarterly, Information Systems Research, and Journal of American Medical Informatics Association.

Zhu Zhang (zhu.zhang@ia.ac.cn) is an assistant professor at the Institute of Automation, Chinese Academy of Sciences. He received his Ph.D. degree in Computer Science from the University of Chinese Academy of Sciences. His research interests include data mining, artificial intelligence, health informatics, and business analytics. He has published a number of papers in journals and conference proceedings, including ACM Transactions on MIS, Knowledge-Based Systems, and International Conference on Information Systems.

Xiao Liu (xiao.liu.10@asu.edu) is an assistant professor in the Department of Information Systems, Arizona State University. Dr. Liu’s research interests are in data science and information system design, in areas such as health IT, social media analytics and predictive analytics.

Daniel Zeng (dajun.zeng@ia.ac.cn) is a professor in the Institute of Automation, Chinese Academy of Sciences, and the University of Chinese Academy of Sciences. He is the head of Shenzhen Artificial Intelligence and Data Science Research Institute (Longhua). He received his Ph.D. in industrial administration from Carnegie Mellon University. He serves as the Editor-in-Chief of ACM TMIS and the associate editor of INFORMS JOC. He is a fellow of IEEE and AAAS.
