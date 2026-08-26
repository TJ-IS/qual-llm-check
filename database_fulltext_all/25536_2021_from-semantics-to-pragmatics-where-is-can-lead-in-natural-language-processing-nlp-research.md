---
otero_id: 25536
otero_key: "RS5W3ES5"
title: "From semantics to pragmatics: where IS can lead in Natural Language Processing (NLP) research"
authors: "Yan Li; Manoj a Thomas; Dapeng Liu"
year: "2021"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1816145"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# From semantics to pragmatics: where IS can lead in Natural Language Processing (NLP) research

Yan Li , Manoj a Thomas & Dapeng Liu

To cite this article: Yan Li , Manoj a Thomas & Dapeng Liu (2020): From semantics to pragmatics: where IS can lead in Natural Language Processing (NLP) research, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1816145

To link to this article: https://doi.org/10.1080/0960085X.2020.1816145

![](/api/attachments/RS5W3ES5/fulltext/images/2dbd1770620863d9ff5d73736c173464c98a4b1e8a29f5395943bd9c5458010a.jpg)

Published online: 24 Sep 2020.

![](/api/attachments/RS5W3ES5/fulltext/images/a787ebca7c8412d3868be9c7cdb5319450dacb017842ad96abc975727d796bc0.jpg)

Submit your article to this journal

![](/api/attachments/RS5W3ES5/fulltext/images/36417d7a420aa153666b4b557fce51e3259930111e2286b0ede20f60dc47d5c0.jpg)

View related articles

![](/api/attachments/RS5W3ES5/fulltext/images/c638fa534cddb5d0c41f5096b807e1b3828671ae48b9bd860d3a55ec9f7ab7c5.jpg)

View Crossmark data

RESEARCH ESSAY

Check for updates

# From semantics to pragmatics: where IS can lead in Natural Language Processing (NLP) research

Yan Li <sup>a</sup>, Manoj a Thomas<sup>b</sup> and Dapeng Liu <sup>c</sup>

<sup>a</sup>Center for Information Systems and Technology, Claremont Graduate University, CISAT, Claremont, CA, USA; <sup>b</sup>Business Information Systems, University of Sydney, Sydney, Australia; <sup>c</sup>Information Systems & Technology Management, University of New South Wales, Sydney, Australia

## ABSTRACT

Natural Language Processing (NLP) is now widely integrated into web and mobile applications, enabling natural interactions between humans and computers. Although there is a large body of NLP studies published in Information Systems (IS), a comprehensive review of how NLP research is conceptualised and realised in the context of IS has not been conducted. To assess the current state of NLP research in IS, we use a variety of techniques to analyse a literature corpus comprising 356 NLP research articles published in IS journals between 2004 and 2018. Our analysis indicates the need to move from semantics to pragmatics. More importantly, our findings unpack the challenges and assumptions underlying current research trends in NLP. We argue that overcoming these challenges will require a renewed disciplinary IS focus. By proposing a roadmap of NLP research in IS, we draw attention to three NLP research perspectives and present future directions that IS researchers are uniquely positioned to address.

ARTICLE HISTORY Received 27 February 2019 Accepted 21 August 2020

Natural Language Processing; natural language generation; natural language understanding; pragmatics; semantics; disciplinary IS research; NLP roadmap

## 1. Introduction

Natural Language Processing (NLP) is an interdisciplinary field of computer science, artificial intelligence (AI), and linguistics that explores how computers can be used to understand and manipulate natural language text or speech. Although NLP has a cumulative history since the 1950s (Kumar, 2011), it has mostly remained as an area of research within the computational linguistics domain. In recent years, the growing vastness of textual data through electronic communication systems, the World Wide Web, and research corpora, combined with the need for quick access to context-specific information, has driven the advancement and commercialisation of NLP. Today, NLP is widely integrated into web and mobile applications, enabling natural interactions between humans and computers. It has matured to the point where spoken language is portrayed as the next humancomputer interface (Plummer et al., 2017).

As humans, we speak or write in native natural language to extract and understand information, and more importantly, use natural language as a tool to communicate our intentions to act (Cherpas, 1992). Natural languages are symbols that humans use to communicate, collaborate, and craft social contracts. Arguably, the true value of information systems (IS) also lies in its potential to support the communicative and collaborative functions central to human activity (Ågerfalk et al., 2008). It is therefore no surprise that NLP is becoming increasingly central to IS. However, despite the fact that many engaging, relevant, and timely NLP studies have been published, NLP has yet to be recognised as a mainstream IS research area. A likely reason is that the wide-scale adoption of NLP is a relatively recent phenomenon, and related research until lately has largely endured in the field of computer science. To the best of our knowledge, no rigorous assessment has been conducted to determine the role IS plays in the overall NLP research landscape and how NLP research fits within the overall IS research agenda.

This study targets three high-level enquiries. First, we investigate how NLP research is conceptualised and realised in IS and aim to create an organising framework to review IS-related NLP literature. Second, we review 356 NLP articles published in IS journals between 2004 and 2018. An exploratory analysis is conducted using a variety of descriptive, text analysis, and rule-based knowledge discovery techniques to determine current research trends in NLP. Third, we seek to develop a roadmap that examines the boundaries of NLP research in IS, and in doing so, persuade IS researchers to explore new areas outside of the norm.

The contributions of this research are threefold. First, we identify and categorise 12 prototypical NLP tasks that are widely researched and applied in IS studies. Although published studies individually contribute to exploring one or more of these tasks and related techniques, no studies have comprehensively reviewed or synthesised them. Our synthesis indicates the need to go beyond the current over-specialised and siloed focus (Alvesson & Sandberg, 2014) in NLP research. Second, through the analysis of the NLP literature, we draw insights into challenges that result in the impromptu positioning of NLP research in the IS discourse. We show that many published NLP studies undertake a “gap-spotting” approach (i.e., identifying and addressing gaps in literature without challenging underlying assumptions or generating new and interesting research questions or theories) (Alvesson & Sandberg, 2011). Building upon this, we argue that current boundaries in NLP research have stymied the examination of new areas and the rethinking of “box-breaking” research (Alvesson & Sandberg, 2014). Thus, our third contribution is a roadmap of NLP research in IS. The roadmap presents three research perspectives where IS researchers may engage in a broader and more varied intellectual pursuit in the NLP landscape.

The rest of the paper is organised as follows. We first provide a background on NLP in Section 2. Section 3 explains the research procedure and Section 4 presents a three-step data analysis of the NLP literature corpus. Insights from the analysis and underlying research assumptions are summarised in Section 5. Section 6 proposes a roadmap of NLP research in IS. Finally, Section 7 presents the limitations of the study along with concluding thoughts.

## 2. Background

Natural language (NL) refers to any human written or spoken language that has evolved naturally for human communication. NL interactions between humans and computers generally comprise two branches of activities: natural language understanding (NLU) and natural language generation (NLG). NLU concerns the computational process of transferring natural language from humans to a machine-understandable format. NLG focuses on computer systems that produce understandable texts in human language. While NLU and NLG share similar theoretical foundations and are often used together in many real-world applications, the internal processes of these two activities are quite diferent (Reiter et al., 2000). Essentially, NLU is the process of mapping human language into a computational representation (i.e., given some natural language inputs, how to choose an appropriate interpretation among multiple possible alternatives), and NLG is the process of mapping the computational representation into human language (i.e., given the diferent means to achieve the desired natural language outputs, how to decide which one to use) (Reiter et al., 2000).

Both NLU and NLG are concerned with the computational modelling of human language, which requires linguistic analysis of all aspects of language (Winograd, 1972), including words and parsing, parts of speech (POS) and morphology (word formation), phrases (word order) and grammars, etc. Drawing upon theoretical linguistics, the process of linguistic analysis can be decomposed into three distinct yet interrelated dimensions: syntactics, semantics, and pragmatics (Oller, 1972). Syntactic analysis focuses on understanding the proper ordering and structuring of a string of words (i.e., a sentence). As a necessary step, syntax-centred NLP relies mainly on arbitrary keywords, punctuation, and word co-occurrence frequencies. Semantic analysis concerns the interpretation of literal meaning of the natural language that is not explicitly ascribed in the syntactic form. Instead of word-based techniques, semantics-based NLP exploits concepts and multi-word expressions that carry different types of semantic knowledge representations. The semantic knowledge can be captured extrinsically through ontologies or semantic knowledge bases, or intrinsically by building semantic structures within a corpus using machine-learning techniques (Cambria & White, 2014). In contrast, pragmatic analysis emphasises the determination of the context and purpose of an utterance, often focusing on narrativelevel analysis. To efectively understand and generate human-like utterances, pragmatic NLP requires significant knowledge of the social context and discourse structure, as well as the ability to model the sensemaking process of humans (Howard & Cambria, 2013). It represents the most dificult linguistic analysis dimension in NLP.

Once natural language is processed into machinereadable formats, advanced analytical algorithms and techniques are applied for tasks such as information extraction (Grant & Conlon, 2006; Mangassarian & Artail, 2007) and spoken language processing (Lopez-Cozar et al., 2010). In their seminal book on NLP, Manning and Schütze (1999) introduced common NLP tasks that include grammatical text analysis, machine translation, text clustering, text classification, information retrieval, corpus analysis, and word sense disambiguation. More recently, Cambria and White (2014) summarised NLP research areas as information retrieval, information extraction, machine translation, text summarisation, text generation (i.e., question answering), and sentiment analysis and opinion mining. Many NLP tools have been developed to support various NLP tasks. For example, NLTK, a leading platform for building Python-based NLP programs, implements a comprehensive set of tools for NLP tasks that include grammatical analysis, text classification, information extraction, word sense disambiguation, and semantic annotation (Bird et al., 2009). The Stanford CoreNLP, a Java-based NLP tool, provides many common NLP capabilities for grammatical text analysis, named-entity extraction, and sentiment analysis (Manning et al., 2014).

While it is not practical to list an exhaustive set of NLP-related tasks, we synthesised 12 prototypical NLP tasks based on a thorough review of published NLP literature and commonly used NLP tools. They are text classification or categorisation (TC), information extraction (IE) and information retrieval (IR), text summarisation (TS), machine translation (MT), corpus analysis (CA), text generation (TG), sentiment analysis or opinion mining (SA), natural language inference (NLI), grammatical text analysis (GT), word sense disambiguation (WSD), speech recognition (SR), and semantic annotation (SAN). Description D3 in Appendix A provides a detailed description of each task as well as how these 12 tasks are synthesised.

As an applied discipline, NLP research also seeks to solve real-world problems by applying existing NLPrelated algorithms and tasks (Hirschberg & Manning, 2015). Research output from these studies are usually designed artefacts that implement one or more prototypical tasks and/or algorithms. For example, Valencia-Garcia et al. (2005) designed a system to translate surgeons’ natural language into robotexecuted commands by integrating SR, IE, SAN, and NLI tasks.

## 3. Research procedure

The first step of our research was to create a corpus of NLP literature. We conducted a broad review to ensure comprehensive coverage of the NLP literature published in IS. We identified all journals listed on the MIS journal ranking page of the Association for Information Systems (Association for Information

Systems [AIS], n.d.), the 45 journals rated and ranked by Holsapple (2009), and the composite journal ranking by Fisher et al. (2007). This yielded a list of 102 journals. We then searched articles published in these journals between 2004 and 2018 using the terms “Natural Language Processing” or “NLP” in the title, abstract, and keywords. Description D1 in Appendix A provides a detailed explanation of the search procedure.

We then reviewed every retrieved article to verify that they were NLP-related IS publications. Our search identified 356 journal articles for further analysis. The retrieved literature shows an increasing trend of NLP research in IS, especially since 2012 (Figure 1). This trend coincides with what is regarded as the third wave of NLP development (Deng, 2018), i.e., the arrival of NLP and AI heralded by the striking success of speech recognition in 2010–2011.

After creating the NLP literature corpus, our review and analysis involved three phases. The first phase aimed to understand the nature of NLP research and included two steps. First, the three authors coded the research methodologies commonly employed in NLP studies. Second, we analysed keyword frequencies to explore popular and important NLP topics addressed by IS researchers. The two steps are described in Appendix D2. Our findings indicated that the top frequently used keywords are representative of the 12 prototypical tasks that we synthesised.

The initial assessment also highlighted the lack of a framework for synthesising NLP research. Synthesis is the most important part of the review in order to deliver a global representation of the literature. According to Rowe (2014), a review framework is needed to map the literature so that researchers can make sense of the literature within broad categories.

![](/api/attachments/RS5W3ES5/fulltext/images/adbc6dcc905f477e3dce12bdb8251c050e18efcc72e5879b62d8e4e981b5f619.jpg)  
Figure 1. Count of NLP publications by year.

Such a framework can be selected by the researchers or developed (Rowe, 2014). Because such a framework is not available, the objective of the second phase was to develop an organising framework to review NLP literature. We independently reviewed a set of 50 randomly selected articles from the NLP literature corpus and analysed how NLP is conceptualised and realised in each study. Discussion among the authors led to the creation of an organising framework that included three IS research dimensions (i.e., algorithms, prototypical NLP tasks, and design artefacts) in addition to the two NLP research orientations (i.e., NLU and NLG) and three foundational linguistic analysis dimensions (i.e., syntactics, semantics, and pragmatics). We describe each of the IS research dimensions below.

## 3.1. Dimension 1: algorithms

Algorithms have received considerable attention from NLP scholars. NLP-related algorithms can be divided into two groups: rule-based and statistics-based. The former emphasises rules that are inducted from the language characteristics, while the latter focuses on the use of statistical methods to analyse large corpora. The adoption of machine learning (ML) algorithms and statistical NLP methods leads to purposeful design artefacts that benefit NLU, NLG, and their utilities. For example, a variety of ML algorithms, such as Genetic Algorithms, Deep Neural Networks (DNNs), and Hidden Markov Models, are employed in various prototypical NLP tasks (e.g., DNNs are used for text classification; K. Lee et al., 2018 and semantic annotation; Chen et al., 2017). Advancements in algorithms also help improve the performance of specific NLP tasks, such as speech recognition (Lopez-Cozar, 2015).

## 3.2. Dimension 2: prototypical tasks

NLP research often combines several prototypical tasks to solve a real-world problem. For example, Montoyo et al. (2012) surveyed SA; Karimi et al. (2011) explored the state of art of machine translation; and Wong et al. (2012) analysed natural language inference. Although these studies individually contributed to exploring one or more NLP tasks, none comprehensively reviewed or synthesised most commonly studied NLP tasks. Identifying these tasks provides a starting point for IS researchers engaging in the NLP research landscape.

## 3.3. Dimension 3: design artefacts

The assessment showed a significant number of design science research (DSR) studies (see Description D2.1 in Appendix A). DSR is the development of purposeful artefacts targeting unsolved real-world problems (Vaishnavi et al., 2017). The implementation of NLP artefacts often combines multiple prototypical tasks. For instance, to enable machines to execute tasks by following natural language instructions from humans, Liu and Zhang (2018) designed a system that extracted task-related information from natural language (an IE task), applied semantic analysis to identify tasks, subtasks, and their logic relations (a SA task), and inferred executable machine operations (an NLI task). For IS researchers, this dimension represents how NLP algorithms and tasks are applied to develop real-world design artefacts.

The researchers also agreed that the studies relied on lexical sources and the IS knowledge base as research inputs, to which the outputs reciprocally contribute. The lexical sources serve as the foundation for NLP-related research and delimit the scope of studies. The knowledge base is the foundational body of knowledge and methodologies through which IS research is accomplished (Vaishnavi et al., 2017). It provides reference theories, frameworks, research methods, and evaluation approaches for conducting NLP research in IS.

Based on the above discussions, an organising framework was created for NLP literature coding. It includes three categories: two NLP research orientations (i.e., NLU and NLG), three foundational linguistic analysis dimensions (i.e., syntactics, semantics, and pragmatics), and three IS research dimensions (i.e., algorithms, prototypical NLP tasks, and design artefacts). In the last phase of the study, we coded the literature corpus based on the organising framework. To address the concern of subjectivity in the manual coding process, we adopted a multi-researcher coding strategy similar to Sarker et al. (2019). The detailed coding procedure is provided in the Description D1 of Appendix A. After coding, we conducted an exploratory analysis using a variety of analytical techniques, including trend analysis, latent semantic analysis (LSA), latent Dirichlet allocation (LDA), document clustering, and association rules (AR). Figure 2 summarises the overall research procedure.

## 4. Data analysis and findings

Our data analysis included three separate steps: descriptive, exploratory, and rule-based knowledge discovery. First, we performed a descriptive analysis of the coded dataset to evaluate the scope and purpose of prototypical tasks in published NLP studies. We also analysed general trends in linguistic analysis and NLU/NLG research. Second, we conducted exploratory text analysis on our NLP corpus using topic modelling and clustering techniques, the main purpose of which was to confirm the validity of our coding protocol. Lastly, we used association rules (AR) mining to discover interesting relationships between diferent prototypical tasks. Below, we synthesise the results to benefit IS researchers and practitioners interested in NLP.

![](/api/attachments/RS5W3ES5/fulltext/images/b9a52ce639a652056f8e983baf95bb1a4b4f7d98cca344eafc0c443ea858bee2.jpg)  
Figure 2. Research procedure.

## 4.1. Descriptive analysis results

Of the 356 articles that we coded, 316 articles addressed one or more of the 12 prototypical tasks, and most studies used one or more NLP algorithms. For example, Altınel and Ganiz (2016) designed a semi-supervised learning algorithm for text classification based on a semantic kernel with a Support Vector Machine. Similarly, Yang et al. (2015) proposed a new multi-document summarisation approach using hierarchical Bayesian models. Some studies used multiple prototypical tasks to build design artefacts. For instance, Wang and Xu (2018) used IE and TC to facilitate automobile insurance fraud detection in claims. Figure 3 illustrates the frequency (actual number of articles) within which the 12 prototypical tasks appear. It can be seen that tasks such as IE and IR, as well as SAN, have received the most attention, which we discuss in Section 5.1.

Of the 356 journal articles in our literature corpus, 334 were coded for the three linguistics dimensions (i.e., syntactics, semantics, and pragmatics). We excluded survey publications that cover more than one linguistic dimension and studies that focus on lower level linguistics such as lexical analysis and tokenisation. Because of the inherent hierarchy in the three linguistic dimensions (i.e., semantic-NLP necessitating syntactic processing, and pragmatic-NLP requiring semantic understanding), each article was coded for only one dimension based on its primary focus. The coding results showed only 17 syntactic-centred NLP studies, all of which use syntactic analysis to advance linguistics pre-processing of lexical sources. The majority of studies (87%) were semantic-centred; pragmatic-centred research represented only 8% of our corpus. The implications of this finding are discussed in Section 5.2.

Lastly, 48 studies are oriented towards NLG, and almost all NLG studies required the initial NLU. For example, text summarisation would first require the interpretation and presentation of the source text (an NLU process) and then transform the source representation into a summary representation before generating summary text (an NLG process). Only one article (Ferreira & Atkinson, 2009) focused solely on NLG, where feedback generation strategies were designed for an intelligent tutoring system with the assumption that the source text had already been interpreted and presented. The trend analysis indicates a noticeable increase in NLU research (see Figure 4) since 2012, while NLG studies are yet to attract more research attention.

![](/api/attachments/RS5W3ES5/fulltext/images/437a599c246412fb87f4ffb0b5a2da5b6b4740c6b48d80e8445515dbea560fbd.jpg)  
Figure 3. Prototypical tasks commonly studied in NLP research.

![](/api/attachments/RS5W3ES5/fulltext/images/da1b94e5ad1afba89cd64f9a83813b33242a4388deff73d3503fa153fb32b6b6.jpg)  
Figure 4. NLU and NLG studies in the reviewed NLP literature between 2004 and 2018.

We further synthesised NLP research by aligning the 12 prototypical tasks with two coding categories. First, we created two correlation matrices: one between the 12 tasks and the NLG (because almost all studies have an NLU focus), and one between the 12 tasks and the linguistic dimensions (syntactics, semantics, and pragmatics). Then, we compared the Pearson correlation coeficient (r) of each prototypical task with respect to each coded feature. A higher value of r implies a stronger alignment. For example, the r value between semantic annotation (SA) and semantics is the highest when compared to those for syntactics and pragmatics, which indicates that SA may align more with semantics. Appendix D4 describes the correlation analysis and results in detail. We further reflected on the results with our own understanding of the literature corpus and created Figure 5 to show how NLP prototypical tasks, research orientations, and linguistics dimensions may be positioned together.

## 4.2. Exploratory analysis of the NLP literature corpus

While our coding strategy aimed to minimise subjectivity, it relied on the 12 prototypical tasks synthesised from the NLP literature. The validity of the coding results thus depended on the correct categorisation of the 12 prototypical tasks. To substantiate the descriptive coding, we therefore analysed our literature corpus using exploratory text analysis techniques with the objective of discovering hidden semantic structures (topics or clusters) in the corpus. With the assumption that each semantic structure would include one or more tasks, we compared whether each topic or cluster label reflected or difered from the 12 prototypical tasks.

![](/api/attachments/RS5W3ES5/fulltext/images/d930ce38d179a0b3671f0049cb1a16136bd7c94ed65055f5f784bb3ec6bb8fe3.jpg)  
Figure 5. Synthesis of the NLP research in information systems.

We experimented with diferent topic modelling (LSA and LDA) and document clustering (K-means, Expected Maximum (EM), and hierarchical algorithms) techniques. All these algorithms are popular learning algorithms for NLP and topic detection. While LDA (Blei et al., 2003, January) creates a generative model that specifies joint probability distributions of documents and topics (i.e., one document can belong to multiple topics), document clustering builds a discriminative model (i.e., each document is unique in its own cluster). LSA (Landauer et al., 1998) constructs singular value decompositions (SVDs) to reduce the higher dimensional terms-by-document matrix to a lowerdimensional latent semantic space, and then cluster documents in the semantic space according to the cooccurrence of document terms. Based on whether SVDs are constructed orthogonally or not, each document may appear in only one topic or multiple topics.

The clustering analysis did not provide comprehensible distinguishing results, possibly due to the nondeterministic nature of NLP research, where each article may belong to multiple semantic spaces. However, the LDA models provided interpretable and coherent results. We ran multiple LDA models by changing diferent input parameters and selected a final model with the most discriminant and interpretive result, as well as the highest topic coherence score (0.43 based on the UMass metric) (Mimno et al., 2011). The final model includes 12 topics (see Table 1).

Table 1. Latent Dirichlet Allocation (LDA) results.

<table><tr><td>Topic</td><td>Terms</td><td>Topic Label</td></tr><tr><td>1</td><td>Word, disambiguation, sense, context, meaning</td><td>Word sense disambiguation</td></tr><tr><td>2</td><td>Answer, query, question, web, search</td><td>Question and Answering</td></tr><tr><td>3</td><td>Opinion, online, sentiment analysis, emotion</td><td>Sentiment Analysis</td></tr><tr><td>4</td><td>Similarity, semantic, relation, wikipedia, wordnet</td><td>Semantic Annotation and Corpus Analysis</td></tr><tr><td>5</td><td>Artificial intelligence, application, ontology</td><td>AI and ontology</td></tr><tr><td>6</td><td>Process, requirement, case, software, design</td><td>Requirements engineering from textual documents</td></tr><tr><td>7</td><td>Model, extract, content, topic, term</td><td>Information Extraction</td></tr><tr><td>8</td><td>Classifier, support vector, prediction, entity</td><td>Text Classification</td></tr><tr><td>9</td><td>Computer, human, dialogue, virtual, architecture</td><td>Human computer language interaction</td></tr><tr><td>10</td><td>Summarisation, extraction, automatic, text, document</td><td>Information Extraction and Text Summarisation</td></tr><tr><td>11</td><td>Sentiment analysis, classification, neural network</td><td>Sentiment Analysis and Text Classification</td></tr><tr><td>12</td><td>Real-world, improve, machine learning, reduce</td><td>NLP applications</td></tr></table>

To create topic labels, we independently coded each topic by reviewing the top-ranked words and associated articles and then compared the results. If there was a disagreement, the researchers carried out in depth discussion until an agreement was reached. This approach was followed to label all 12 topics with meaningful terms with an inter-coder agreement of 84%. However, we were able to map only seven topic labels to the corresponding prototypical tasks. For example, Topic 1 matches perfectly with the WSD task, while topic 8 matches perfectly with the text summarisation task. Additionally, the results show correlations between the topics. For example, Topics 7 and 10 are related to information extraction. However, Topic 7 centres around diferent models to extract features from the documents, whereas Topic 10 focuses on using extracted features to summarise from text. Similarly, although both Topics 3 and 11 cover senti ment analysis (SA), Topic 3 emphasises the application of SA on emotion detection, and Topic 11 underlines how diferent classification techniques can improve SA. These findings highlight two limitations of LDA. First, LDA employs a bag-of-words approach to understand lexical semantics (i.e., the meaning of individual words) without considering the semantic relationships between words. Second, it models topics as being independently drawn from a single distribution, whereas, in the real world, distributions over words are often correlated (Blei & Laferty, 2005). To gain a better understanding of how prototypical tasks are correlated, we further conducted AR mining as described below.

## 4.3. Association rules (AR) mining

To investigate whether the presence of one task implies the presence of other tasks in the same study, we used AR mining (Agrawal et al., 1993) to analyse the corpus. The AR results showed three significant rules (see Table 2). The first rule confirmed the notion that NL inference has received much attention in NLP research, and jointly with semantic annotation (SAN). The second rule indicated that corpus analysis is used in conjunction with SAN for the discovery of semantic concepts and relationships. The third rule suggested the use of IE and IR for text generation (see Appendix D5 for a more detailed discussion of the rules).

Table 2. Association rules (AR) mining results.

<table><tr><td>Lift</td><td>Confidence (%)</td><td>Transaction Count</td><td colspan="2">Rule</td></tr><tr><td>1.68</td><td>42.42</td><td>14</td><td colspan="2">Natural Language Inference Semantic Annotation</td></tr><tr><td>1.40</td><td>21.00</td><td>7</td><td>Corpus Analysis Annotation</td><td>Semantic</td></tr><tr><td>1.33</td><td>59.09</td><td>13</td><td>Text Generation</td><td>IE and IR</td></tr></table>

## 5. Discussion

## 5.1. Dominant received view of NLP research

Our descriptive analysis (see Section 4.1) highlights the popularity of information extraction and retrieval (IE and IR), and semantic annotation (SAN) in published research. A likely explanation is their expanding use and applicability for interactive functions on mobile devices. The popularity of NLP engines such as Google, IBM Watson Assistant, and Amazon Lex may also play a role in drawing greater attention to research involving IE and IR for extracting knowledge from natural language (Andres Paredes-Valverde et al., 2015; Herbert & Kang, 2018). SAN adds formal structure and semantics to interconnect textual data based on semantic commonalities. Many NLP studies related to SAN investigate the role of ontologies (e.g., Bateman et al., 2010; Bertola & Patti, 2016) for representing underlying semantics. In fact, our descriptive analysis (see Table A1 in Appendix A) indicated “semantics” as the keyword with the highest frequency, a reflection of the growing popularity of SAN in NLP research.

## 5.2. From semantics to pragmatics

While earlier NLP studies have primarily focused on the syntactic analysis of text, our exploratory assessment (Section 4.2) showed a clear trend towards semantic processing of spoken and textual language. For example, Desmet and Hoste (2013) found that combining lexical (lemmas, POS tags, and trigrams) and semantic (SentiWordNet and subjective clues) features were better predictors of detecting emotions in suicide notes. Newer studies have also advanced from discovering semantics at the word and phrase levels to sentences and paragraphs, as evidenced by the popularity of sentencelevel embedding methods (Pan et al., 2013; Tang et al., 2015). Our analysis also indicated that NLP research is leveraging newer ML techniques to extract semantic structures from text. Examples include an improved hidden Markov model to capture word dependencies in LDA (Yang et al., 2015), an ensemble of neural networks for dependency parsing (Kim et al., 2017), and DNNs to extract semantic information flow at the discourse level for text classification (K. Lee et al., 2018).

Compared to semantic NLP research, we found only 29 pragmatics-centred research that explored the integration of semantics and theories of pragmatics in improving the performance of NLP tasks. Among them, very few have gone beyond sentencelevel textual analysis to include in-depth communicative narrative analysis. Chakrabarti and Luger (2015) is one of the few studies that has attempted to generate pragmatic knowledge from human narratives, where stochastic approaches were used to construct domainspecific knowledge from utterance.

Rapid advances in NLP technologies continue to make NLP a part of our everyday experiences. Although syntactic- and semantic-level approaches are the first step towards efective NLP, new research directions point towards pragmatic-level NLP studies to decode the process of understanding, generating, shaping, and realising contextually relevant social discourses (Cambria & White, 2014). One good example is Nistor et al. (2018) who employed NLP and Bakhtin’s theory of dialogism to understand how online communities would respond to newcomer inquiries.

## 5.3. Emergence of NLG

As discussed in Section 4.1, NLU dominates NLP research in IS, whereas NLG is yet to attract much research attention. With powerful and efective computational models for syntactic- and semantic-level NLU as a foundation, the field of NLG has seen the emergence of successful text-to-text and vision-totext generation applications (Gatt & Krahmer, 2018). Yet, NLG research at the pragmatic level, such as generating texts with metaphors and narratives that account for personality and emotions, is still in its infancy.

Cambria and White (2014) identified six symbolic level capabilities required for NLU. Our review showed that NLU systems have achieved much of the symbolic capabilities through approaches such as keyword co-occurrence frequencies and bag-of-words analysis. Semantic-level NLU, however, requires computational methods and tools to go beyond syntactic representations and interpret semantic features that are not explicitly expressed in the text or spoken language (Conde-Clemente et al., 2018; Furlan et al., 2013). Achieving these objectives would require MLbased semantic reasoning and inferencing using knowledge bases such as ontologies (Paredes-Valverde et al., 2016).

NLP is more than just using computers to recognise words or spawn pre-coded output. If the goal of pragmatic-NLP research is to assist humans with non-computer skills to interact with computers naturally, the ability to infer from natural language in its difering forms, filter decisions, and generate real and usable information is essential. Thus, pragmatic-level

NLG requires leveraging not only syntactic and semantic concepts from utterances but also knowledge of context and domain of discourse with respect to the actors and their intentions (Howard & Cambria, 2013). This presents significant challenges and may explain the low number of NLG studies in our literature corpus. Only when pragmatic-level NLP is achieved, can NLU and NLG be put to good use in real-life situations. For NLU or NLG, related research needs to address how NLP responds to preemptive utterances (textual and spoken) by detecting crucial signals such as conversational contexts and actor’s intentions.

## 5.4. Challenges of positioning NLP research in the IS discourse

Our study highlights three challenges that may explain why NLP has yet to receive mainstream IS research focus. They build upon each other and stem from underlying assumptions that are neither theoretically explicable nor logically expedient. First, much of published NLP research can be epistemologically identified with the received view of IS (Hassan et al., 2018; Hirschheim, 1985). The bearing of the symbolic nature of natural language on the human agency is vastly ignored in this form of NLP research. This category of studies has not examined linguistic presuppositions embedded in information systems (Weigand, 2005) or its efect on communication and collaboration (Aakhus et al., 2011). We reason that this form of knowledge generation is grounded on the predominant assumption that NLP is a siloed specialisation of computer scientists and applied linguists.

This leads to the second challenge: how new research questions drive NLP research in IS based on difering schools of thought. Studies that focus on design artefacts integrate NLP algorithms and prototypical tasks to solve particular problems. They treat NLP as a computational tool for language representation and as a conduit for producing understandable information from human language. Published literature in this category thus takes a representational perspective of NLP (Burton-Jones & Grange, 2013; Wand & Wang, 1996). Very few studies in this group have explored how NLP enables human agency to build identities, coordinate relationships, and support decision-making. More enquiries are needed to examine the use and efect of natural language in creating social contracts and to investigate the increased potential of NLP in shaping identity creation and social action. Here, we reason the key assumptions underlying this group of studies to be that they follow a “gap spotting” approach (Alvesson & Sandberg, 2011) to build design artefacts that previously did not exist.

As NLP becomes more democratised, it is not just trained linguists that implement and use NLP. A lay person interacting with NLP applications is unaware of biases encoded in NLP models and algorithmic prejudices. This raises the third challenge, namely lack of research investigating the impacts of NLP on humans, society, and organisations. Digitisation of natural language has blurred the separation of language purely as a symbol, and action solely as a computational outcome. Although the evolution and use of NLP as a symbiotic bridge between human and machine are contemporary thinking, it bears the risk of targeting human vulnerabilities in ways we have witnessed with other contemporary technologies (Gibney, 2018) such as facial recognition and computer vision (Dormehl, 2014). IS research is yet to provide guidance in this area, such as the responsible development and application of NLP technologies, best practices around language data collection and use, and shared minimum standards for acceptable NLP practices to uphold the welfare of the public.

If NLP research is to be contemporary and emergent, researchers have to recognise that human actors are an integral part of this pervasive socio-technical phenomenon. Should IS research fall behind in investigating related areas, knowledge valuable for scholars, practitioners, and policymakers would be stifled. A renewed approach is thus desired to challenge the current boundary sets of assumptions that underlie NLP research and conduct inquires based on the disciplinary view of IS. As NLP capabilities achieve humanlike quality in sophistication and fluency, the IS disciplinary view of NLP is essential to address new and emergent questions around information systems use and social behaviour afected by NLP. Instead of repackaging old problems and “gap spotting” (Alvesson & Sandberg, 2011), the disciplinary view of IS presents immense opportunities for researchers to develop new theories and broaden the NLP knowledge base. In the next section, we unpack the above challenges and assumptions further and present a roadmap of NLP research in IS.

## 6. A roadmap of NLP research in IS

To elucidate the above distinctions, we propose a roadmap of NLP research in IS (see Figure 6). It distinguishes three NLP research perspectives: 1) NLP algorithms and prototypical tasks (received view focus on algorithms and prototypical tasks); 2) NLP applications (focus on NLP-based design artefacts); and 3) disciplinary IS Research in NLP (focus on the role and efect of NLP on humans, society, and organisations). The arrows connect the research perspectives to the appropriate lexical sources and the IS knowledge base.

![](/api/attachments/RS5W3ES5/fulltext/images/d11f485ab8953d6916541e7c5a855d8be7cf5d2e647bd43062413b81201f28f9.jpg)  
Figure 6. Roadmap of NLP research in IS.

Next, we present three examples of how the research perspectives can be applied in NLP studies to generate new research questions and theories. The examples are presented as a means to demonstrate how NLP research in IS may progress towards a broader and more varied intellectual territory than the currently dominated typical “boxed-in research” approach (Alvesson & Sandberg, 2014).

## 6.1. Grounding NLP research in the context of new theoretical perspectives

Our analysis suggests that NLP discourse in IS literature has not fully bridged the received view framing to its constitutive relationship with human agency. The growing influence of NLP-based information systems in shaping human actions surely cannot be ignored. Yet, there is a paucity of research that aims to understand the role and efect of NLP on humans, society, and businesses. For instance, in a previous example that we discussed (see Section 5.2), Nistor et al. (2018) stopped short of investigating the constitutive role that NLP plays in influencing newcomers’ integration into online communities. Here, the symbolic action perspective, the language action perspective (LAP) (Dwivedi, 2009, pp.113–130; Weigand, 2005), or even the sociomateriality view (Leonardi & Barley, 2008) are viable options to understand the constitutive role that NLP plays in forming social relationships, establishing communication, and collaborating for knowledge creation.

As to why these seemingly relevant perspectives have thus far not been a serious contender in the disciplinary IS research in NLP, our analysis sheds light on two underlying epistemological reasons. First, we reiterate that much of NLP research is anchored in the received view. Even the recent trend towards designing NLP-based artefacts mostly focuses on the representational framing of NLP and bypasses how NLP enables, conditions, and shapes social interactions. Second, the underlying assumptions in NLP research have not been challenged. As our analysis indicates, NLP research is mostly gap-spotting rather than consensus-challenging. In this regard, our roadmap may serve as a vantage point to inspire researchers to spawn new research questions and develop more interesting and influential theories in NLP. We also encourage researchers to consider “problematization” (Alvesson & Sandberg, 2011) as a means to challenge the boundary set of assumptions underlying current NLP research.

## 6.2. Advancing pragmatic enquiry

Over the years, NLP has progressed from simple lexical understanding through syntactic and semantic processing to pragmatic analysis of natural language. While early studies investigated lexical vocabulary and ordering of words and phrases (syntactic focus), more recent enquiries have focused on addressing linguistics ambiguities (semantic focus). However, the true power of NLP resides in its ability to understand the implicit context and the intention of the utterance. NLP should enumerate not only information represented in language symbols but also the actor’s intention to act. Here, a starting point would be for pragmatic-NLP research to address how utterances are socially structured.

As discussed in Section 5.2, a pragmatic-focused NLP approach is essential to generate knowledge based on the communicative processes associated with language forms and language patterns that facilitate or constrain actions (Ågerfalk, 2010). However, only a few pragmatic-centric studies in IS have moved beyond merely treating natural language as symbols to include the context of human interactions. This undermines the role of information systems and its NLP components and downplays the value of language systems in supporting human communication (Dwivedi, 2009, pp. 113–130) and collaboration (Aakhus et al., 2014). The roadmap we propose provides a renewed perspective for pragmatic-NLP research to navigate the practical, social, and ethical dimensions (Cherpas, 1992) of NLP-based information systems. Advancing pragmatic enquiry may also lead to new and emergent prototypical NLP tasks (for e.g., intent recognition and NL identity creation). We call for future studies to explore these notions independently or as a subset of motivating positions linked to NLP.

## 6.3. Ethical imperatives of NLP

Our literature review did not identify any studies that addressed the ethical imperatives of NLP-based information systems. The digitisation of natural language and its increasing potential in shaping social contracts and actions raise many pivotal questions around its ownership, privacy, data filtering, intellectual property, acceptable practices, and governance. “Policy vacuums” created by technologies (Mathiesen, 2004) such as NLP, pose significant threats to society and leave policymakers blinded to what new technologies can or cannot do.

New and unimagined possibilities for human connections using NLP, ingenious ways of using NLP technologies for censorship, and threatening ways in which NLP capabilities may target human vulnerabilities are just a few glaring examples of ethical imperatives of NLP. A recent example is the case of GPT2, an open-source language generation NLP algorithm developed by OpenAI.org (Whitwam, 2019). With a certain amount of human-provided prompt text, the algorithm is capable of piecewise predicting the next word in the sequence, and then continuing to grow language generation using a set of prototypical NLP tasks. While not perfect, the GPT2 algorithm provides strong results on a wide variety of processing tasks such as generating an impressive story, placing characters correctly in the storyline, maintaining basic narrative coherence, and understanding contextual references. In the age of fake news and deep fakes, fine and subtle errors in the generated text are hard to recognise for an unaware consumer. OpenAI.org declined to release GPT2 in the public domain because the concerns are real and the algorithm has potential to target human vulnerabilities. Although humans may still have an advantage over machines in the use of knowledge and commonsense reasoning, the capabilities of NLP to generate symbols equivalent to, or indistinguishable from humans would have farreaching consequences.

The intent here is not to discourage or limit important NLP research. Rather, it is to sensitise researchers, practitioners, and policymakers to the ethical imperatives of NLP and to safeguard against costly and harmful pitfalls. It is to evoke conversations around related topics such as the importance of protecting populations vulnerable to NLP technological changes, while at the same time, legitimising the beneficiary role of associated technologies. Ultimately, the question is how IS researchers may help prepare a new kind of society shaped by technologies such as NLP. In this regard, the disciplinary view of IS research in NLP provides a sound basis to challenge current research boundaries, generate contemporary research questions, and develop new front lines of theories to facilitate discussions around related topics.

In Table 3, we provide some examples of future research directions across the three NLP research perspectives. While not exhaustive, the table serves as a starting point for IS researchers engaging in the NLP research landscape.

## 7. Conclusion

Information and communication technologies integral to our lives are made richer and more versatile with new and emerging NLP capabilities. Innovative technologies such as NLP increasingly fulfil business and societal goals through their material properties and functional afordances (Markus & Silver, 2008; Rai, 2017). To understand the role IS plays in the NLP landscape and how NLP research fits within the overall IS research agenda, we conducted a comprehensive review of 356 articles published between 2004 and 2018. Our descriptive analysis indicated that NLP research is gaining maturity and credence among IS researchers, as evidenced by the increasing number of publications, and the breath of NLP tasks and application areas covered. However, our review suggests that much of the published NLP research takes the received view of information systems (Hassan et al., 2018; Hirschheim, 1985). Our study indicates the absence of a methodological framework or a conceptual direction to guide NLP research in IS. Without such an understanding, related enquiries would, at best, continue to be “gap spotting” and provisional. Through the analysis of challenges and assumptions underlying the current NLP research, we propose a roadmap of NLP research in IS to elucidate three distinctive research perspectives – 1) NLP algorithms and tasks, 2) NLP applications, and 3) disciplinary IS research in NLP. Our findings indicate that the majority of published literature has thus far focused on the first and second perspectives. The third perspective, the disciplinary IS research in NLP, presents immense opportunities for IS scholars and remains largely untapped. We encourage IS researchers to explore new and emergent research questions along with this perspective, from which the NLP knowledge base can greatly improve.

Table 3. NLP research perspectives and prospective research directions.

<table><tr><td>NLP Research perspectives</td><td>Prospective Research Directions</td></tr><tr><td>NLP Algorithms and Tasks (Received view focus on NLP algorithms &amp; prototypical tasks)</td><td>Human like quality in sophistication and fluency in NLU and NLG (e.g., generating text with metaphors)Pragmatic-level NLP for understanding and generating contextually relevant communicative narratives (e.g., addressing linguistics ambiguities)Pre-Emptive NLG by detecting conversational contexts and actor intentionsML-based semantic analysis and inferencing from knowledge bases (e.g., Web ontologies)</td></tr><tr><td>NLP Applications (Focus on NLP based design artefacts)</td><td>Communicative narrative analysis (beyond sentence-level textual analysis)Pragmatic knowledge generation from human narratives accounting for personality and affectionConstruct domain-specific knowledge from utterancesInfer natural language in its differing forms, filter decisions, and generate real and usable informationPrevention and detection of NL spoofing and NL identity impersonation.</td></tr><tr><td>Disciplinary IS Research in NLP (Focus on the role and effect of NLP on humans, society, and organisations)</td><td>Understand users in their routines, activities, and interactions with NLP artefacts (e.g., pervasiveness of NLP in mobile devices and applications).Theoretical framing and interpretation of NLP in IS based on differing schools of thought (e.g., using symbolic action, language action perspectives, etc.)Behavioural studies (e.g., how well does NLP assist humans with non-computer skills to interact naturally with computers?)Adoption perspectives (e.g., how does NLP affect information systems use, how does incorporating NLP for communication and collaboration impact organisational culture).How does NLP enable human agency build NL identities, coordinate relationships, and support decision-making (e.g., role and effect of NLP in social and communicative functions)?Understand the role of NLP-based systems in enabling, conditioning, and shaping social interactions.Examine the manifestation of NLP in politics, humanities, medicine, and society-at-large and its impact (e.g., the impact of GPT2-based applications on election campaigns).Issues of NL ownership, privacy, filtering, intellectual property, and governance (e.g., informing policies and policymakers)NLP ethics in the development and use of NLP technologies</td></tr></table>

The study is not without limitations. First, in our keywords search, we did not include other research areas that may employ NLP techniques or methods, such as social media analytics and text mining. Although we explored the use of social media and text mining as keywords in the literature search, we determined that the retrieved articles were merely applications of NLP techniques rather than contributing to the broader NLP landscape. Hence, in our literature corpus, we only considered articles where the title, abstract, or keywords included “Natural Language Processing” and “NLP”. Similarly, our literature search did not include IS conference proceedings based on the assumption that these additional articles would likely be sub-groups compared to those published in journal articles. Given the growing interests in NLP-related research and practice, an updated review with recent conference proceedings would be beneficial. Nevertheless, our approach allowed us to create a comprehensive, yet manageable literature corpus that we could analyse in a constructive and informative manner. It also enabled us to uncover underlying research assumptions and extract insights.

Second, our descriptive analysis identified 12 prototypical NLP tasks. A more exhaustive review that uses all 12 prototypical tasks as keywords for another round of literature search would be beneficial.

However, the objective of our study was to not limit our view by the narrow lens of summarising prototypical NLP tasks used in NLP studies, but to widen perspectives on how IS investigates NLP and its impact on the human agency. We encourage future studies that conduct this level of NLP literature analysis.

Lastly, our exploratory text analysis can be further improved. In this paper, we used three popular topic modelling approaches to validate the 12 prototypical tasks that we synthesised. Exploratory text analysis techniques, such as LDA, LSA, and document clustering have the potential of detecting complementary as well as novel topic labels. Future research may experiment with other topic modelling techniques using emergent literature to provide an even broader view with additional insights. Similarly, although document clustering analysis did not yield interpretive results in our analysis, future research may add a subsequent analytical step based on AR mining or Decision Tree analysis to describe the document clusters. This might serve to provide meaningful cluster labels.

Simply put, NLP-based information systems symbolise communicative roles and relations through which actors engage in collective practices (Aakhus et al., 2011). NLP upholds the social and symbolic characteristics of IS. Its expanding presence in our everyday lives underlines the increasing need to amplify research that conceptualises the use and efect of NLP and development of theories that explain or predict its interplay with the social environment.

## Notes

1. It is to be noted that the seminal article on design science research by Hevner et al. (2004) was published after the reviews conducted by Palvia et al. (2003).

2. Given the growing prominence of DSR in IS, its inclusion as an important research methodology is critical, and an update to Palvia et al. (2003) categorisation to address this omission is highly warranted.

3. Palvia et al. (2003) conducted a comprehensive review of IS articles published during a five-year period (- 1993–1997) and identified 12 most methodologies used by seven leading MIS journals (Table 1, pp. 291). Palvia et al. (2004) presented an updated list of methodologies that included “content analysis”. However, since the definition of “content analysis” would cover the spectrum of NLP research, it was not included in our coding.

4. We created the grammatical text analysis task to include a cluster of methods to analyse sentence structure. In all the books we reviewed, related methods (e.g., statistical parsing, part-of-speech tagging) are discussed separately.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## ORCID

Yan Li http://orcid.org/0000-0002-0415-0140 Dapeng Liu http://orcid.org/0000-0002-8822-656X

## References

Aakhus, M., Agerfalk, P., Lyytinen, K., & Te’eni, D. (2011). Call for Papers MISQ Special Issue on Information Systems for Symbolic Action: Social Media and Beyond. MIS Quarterly. https://pdfs.semanticscholar.org/5b72/ c034727ba2877e18c9cde0962b1cfe229acc.pdf?\_ga=2. 102641025.1486237949.1599332623-1525804017. 1598298096

Aakhus, M., Ågerfalk, P., Lyytinen, K., & Te’eni, D. (2014). Symbolic action research in information systems: Introduction to the special issue. MIS Quarterly, 38(4), 1187–1200. https://doi.org/10.25300/MISQ/2014/38:4.3

Ågerfalk, P., Aakhus, M., & Lind, M. (2008). Introduction to the inaugural meeting of the AIS special interest group on pragmatist IS research [Paper presentation]. Sprouts: Working Papers on Information Systems, Paris. http:/ sprouts.aisnet.org/8–49

Ågerfalk, P. (2010). Getting pragmatic. European Journal of Information System, 19(3), 251–256. https://doi.org/10. 1057/ejis.2010.22

Agrawal, R., Imieliński, T., & Swami, A. (1993). Mining association rules between sets of items in large databases [Paper presentation]. 1993 ACM SIGMOD international conference on Management of data, Washington D.C. USA. pp.207–216

Allen, J. (1995). Natural language understanding (2nd ed.). Benjamin-Cummings Publishing Co., Inc.

Altınel, B., & Ganiz, M. C. (2016). A new hybrid semi-supervised algorithm for text classification with class-based semantics. Knowledge-Based Systems, 108, 50–64. https://doi.org/10.1016/j.knosys.2016.06.021

Alvesson, M., & Sandberg, J. (2011). Generating research questions through problematization. Academy of Management Review, 36(2), 247–271. https://doi.org/ 10.5465/amr.2009.0188 2 doi:10.5465 AMR.2011.59330882

Alvesson, M., & Sandberg, J. (2014). Habitat and habitus: Boxed-in versus box-breaking research. Organization Studies, 35(7), 967–987. https://doi.org/10.1177/ 0170840614530916

Andres Paredes-Valverde, M., Angel Rodriguez-Garcia, M., Ruiz-Martinez, A., Valencia-Garcia, R., & Alor-Hernandez, G. (2015). ONLI: An ontology-based system for querying DBpedia using natural language paradigm. Expert Systems with Applications, 42(12), 5163–5176. https://doi.org/10.1016/j.eswa.2015.02.034

Association for Information Systems (AIS). (n.d.). MIS journal rankings.

Bateman, J. A., Hois, J., Ross, R., & Tenbrink, T. (2010). A linguistic ontology of space for natural language processing. Artificial Intelligence, 174(14), 1027–1071. https://doi.org/10.1016/j.artint.2010.05.008

Bellot, P., Moriceau, V., Mothe, J., SanJuan, E., & Tannier, X. (2016). INEX Tweet Contextualization task: Evaluation, results and lesson learned. Information Processing & Management, 52(5), 801–819. https://doi. org/10.1016/j.ipm.2016.03.002

Bertola, F., & Patti, V. (2016). Ontology-based afective models to organize artworks in the social semantic web.

Information Processing & Management, 52(1), 139–162. https://doi.org/10.1016/j.ipm.2015.10.003

Bikakis, A., Patkos, T., Antoniou, G., & Plexousakis, D. (2007). A survey of semantics-based approaches for context reasoning in ambient intelligence [Paper presentation]. The European conference on ambient intelligence, Darmstadt, Germany. https://doi.org/10.1007/978-3-540- 85379-4\_3

Bird, S., Klein, E., & Loper, E. (2009). Natural language processing with python. O’Reilly Media, Inc.

Blei, D. M.,& Laferty, J. D. 2005. Correlated Topic Models [Paper presentation]. The 18th International Conference on Neural Information Processing Systems, Vancouver, British Columbia, Canada. https://dl.acm.org/doi/ 10.5555/2976248.2976267

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003, January). Latent dirichlet allocation. Journal of Machine Learning Research, 3, 993–1022. https://www.jmlr.org/papers/ volume3/blei03a/blei03a.pdf

Borah, P. P., Talukdar, G., & Baruah, A. (2014). Approaches for word sense disambiguation–A survey. International Journal of Recent Technology and Engineering, 3(1), 35– 38. https://www.ijrte.org/wp-content/uploads/papers/ v3i1/A1020033114.pdf

Browner, W., Newman, T., & Hulley, S. (2013). Estimating Sample Size and Power: Applications and Examples. In S. Hulley, S. Cummings, W. Browner, D. Grady, & T. Newman (Eds.), Designing clinical research : an epidemiologic approach (pp. 65–95). Philadelphia, PA: Lippincott Williams & Wilkins

Burton-Jones, A., & Grange, C. (2013). From use to efective use: A representation theory perspective. Information Systems Research, 24(3), 632–658. https://doi.org/10. 1287/isre.1120.0444

Cambria, E., & White, B. (2014). Jumping NLP curves: A review of natural language processing research. IEEE Computational Intelligence Magazine, 9(2), 48–57. https://doi.org/10.1109/MCI.2014.2307227

Carenini, G., & Moore, J. D. (1993). Generating explanations in context [Paper presentation]. The 1st international conference on Intelligent user interfaces, Orlando, Florida, USA. https://doi.org/10.1145/169891.169962

Chakrabarti, C., & Luger, G. F. (2015). Artificial conversations for customer service chatter bots: Architecture, algorithms, and evaluation metrics. Expert Systems with Applications, 42(20), 6878–6897. https://doi.org/10.1016/ j.eswa.2015.04.067

Chen, T., Xu, R., He, Y., & Wang, X. (2017). Improving sentiment analysis via sentence type classification using BiLSTM-CRF and CNN. Expert Systems with Applications, 72, 221–230. https://doi.org/10.1016/j. eswa.2016.10.065

Cherpas, C. (1992). Natural language processing, pragmatics, and verbal behavior. The Analysis of Verbal Behavior, 10(1), 135–147. https://doi.org/10.1007/ BF03392880

Clark, A., Fox, C., & Lappin, S. (2013). The handbook of computational linguistics and natural language processing. John Wiley & Sons.

Conde-Clemente, P., Alonso, J. M., & Trivino, G. (2018). Toward automatic generation of linguistic advice for saving energy at home. Soft Computing, 22(2), 345–359. https://doi.org/10.1007/s00500-016-2430-5

Corcoglioniti, F., Rospocher, M., & Aprosio, A. P. (2016). Frame-based ontology population with PIKES. IEEE Transactions on Knowledge and Data Engineering, 28

(12), 3261–3275. https://doi.org/10.1109/TKDE.2016. 2602206

Cuzzola, J., Jovanovic, J., Bagheri, E., & Gasevic, D. (2015). Evolutionary fine-tuning of automated semantic annotation systems. Expert Systems with Applications, 42(20), 6864–6877. https://doi.org/10.1016/j.eswa.2015.04.054

Deng, L. (2018). Artificial intelligence in the rising wave of deep learning: The historical path and future outlook [perspectives]. IEEE Signal Processing Magazine, 35(1), 180–277. https://doi.org/10.1109/MSP.2017.2762725

Desmet, B., & Hoste, V. (2013). Emotion detection in suicide notes. Expert Systems with Applications, 40(16), 6351–6358. https://doi.org/10.1016/j.eswa.2013.05.050

Dormehl, L. (2014). Facial recognition: Is the technology taking away your identity? The Guardian. Retrieved from https://www.theguardian.com/technology/2014/may/04/ facial-recognition-technology-identity-tesco-ethicalissues

Dwivedi, Y. K. (2009). Handbook of research on contemporary theoretical models in information systems. IGI Global.

Eisman, E. M., Navarro, M., & Castro, J. L. (2016). A multi-agent conversational system with heterogeneous data sources access. Expert Systems with Applications, 53, 172–191. https://doi.org/10.1016/j.eswa.2016.01.033

Ferreira, A., & Atkinson, J. (2009). Designing a feedback component of an intelligent tutoring system for foreign language. Knowledge-Based Systems, 22(7), 496–501. https://doi.org/10.1016/j.knosys.2008.10.012

Fisher, J., Shanks, G., & Lamp, J. W. (2007). A ranking list for information systems journals. Australasian Journal of Information Systems, 14(2). https://doi.org/10.3127/ajis. v14i2.469

Freitas, A., Oliveira, J. G., O’Riain, S., Curry, E., & Da Silva, J. C. P. (2011). Querying linked data using semantic relatedness: A vocabulary independent approach. In R. Muñoz, A. Montoyo, & E. Métais (Eds.) Natural language processing and information systems. NLDB 2011. Lecture Notes in Computer Science, vol 6716. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-642-22327- 3\_5

Furlan, B., Batanović, V., & Nikolić, B. (2013). Semantic similarity of short texts in languages with a deficient natural language processing support. Decision Support Systems, 55(3), 710–719. https://doi.org/10.1016/j.dss. 2013.02.002

Gacitua, R., Sawyer, P., & Rayson, P. (2008). A flexible framework to experiment with ontology learning techniques. Knowledge-Based Systems, 21(3), 192–199. https://doi.org/10.1016/j.knosys.2007.11.009

Galgani, F., Compton, P., & Hofmann, A. (2015). LEXA: Building knowledge bases for automatic legal citation classification. Expert Systems with Applications, 42(17–18), 6391–6407. https://doi.org/10.1016/j.eswa.2015.04.022

Gatt, A., & Krahmer, E. (2018). Survey of the state of the art in natural language generation: Core tasks, applications and evaluation. Journal of Artificial Intelligence Research, 61, 65–170. https://doi.org/10.1613/jair.5477

Gibney, E. (2018). The ethics of computer science: This researcher has a controversial proposal. Nature. https:// doi.org/10.1038/d41586-018-05791–w

Gómez-Rodríguez, C. (2014). Finding the smallest binarization of a CFG is NP-hard. Journal of Computer and System Sciences, 80(4), 796–805. https://doi.org/10.1016 j.jcss.2013.12.003

Grant, G. H., & Conlon, S. J. (2006). EDGAR extraction system: An automated approach to analyze employee

stock option disclosures. Journal of Information Systems, 20(2), 119–142. https://doi.org/10.2308/jis.2006.20.2.119

Gruber, T. R. (1993). A translation approach to portable ontology specifications. Knowledge Acquisition, 5(2), 199–220. https://doi.org/10.1006/knac.1993.1008

Gutiérrez, Y., Vázquez, S., & Montoyo, A. (2016). A semantic framework for textual data enrichment. Expert Systems with Applications, 57, 248–269. https:// doi.org/10.1016/j.eswa.2016.03.048

Hassan, N. R., Mingers, J., & Stahl, B. (2018). Philosophy and information systems: Where are we and where should we go? Taylor & Francis.

Herbert, D., & Kang, B. H. (2018). Intelligent conversation system using multiple classification ripple down rules and conversational context. Expert Systems with Applications, 112, 342–352. https://doi.org/10.1016/j.eswa.2018.06.049

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105.

Hirschberg, J., & Manning, C. (2015). Advances in natural language processing. Science, 349(6245), 261–266. https:// doi.org/10.1126/science.aaa8685

Hirschheim, R. (1985). Information systems epistemology: An historical perspective [Paper presentation]. The IFIP TC8 WG 8.2 international conference on Research methods in information systems, Aarhus, Denmark. https:// ifipwg82.org/sites/ifipwg82.org/files//Hirschheim\_0.pdf

Holsapple, C. W. (2009). A new map for knowledge dissemination channels. Communications of the ACM, 52(3), 117–125. https://doi.org/10.1145/1467247.1467276

Howard, N., & Cambria, E. (2013). Intention awareness: Improving upon situation awareness in human-centric environments. Human-centric Computing and Information Sciences, 3(1), 9. https://doi.org/10.1186/ 2192-1962-3-9

Hu, J., Fang, L., Cao, Y., Zeng, H.-J., Li, H., Yang, Q., & Chen, Z. (2008). Enhancing text clustering by leveraging Wikipedia semantics [Paper presentation]. The proceedings of the 31st annual international ACM SIGIR conference on research and development in information retrieval, Singapore, Singapore. https://doi.org/10.1145/ 1390334.1390367

Hu, S., Zou, L., Yu, J. X., Wang, H., & Zhao, D. (2017). Answering natural language questions by subgraph matching over knowledge graphs. IEEE Transactions on Knowledge and Data Engineering, 30(5), 824–837. https:// doi.org/10.1109/TKDE.2017.2766634

Hutchins, J. (2010). Machine Translation: A Concise History. Journal of Translation Studies, 13(1-2), 29–70

Indurkhya, N., & Damerau, F. J. (2010). Handbook of natural language processing. Chapman and Hall/CRC.

Jurafsky, D., & Martin, J. H. (2000). Speech and language processing: An introduction to natural language processing, computational linguistics, and speech recognition. Prentice Hall.

Karimi, S., Scholer, F., & Turpin, A. (2011). Machine transliteration survey. Acm Computing Surveys, 43(3), 1–46. https://doi.org/10.1145/1922649.1922654

Kelly, S., & Ahmad, K. (2018). Estimating the impact of domain-specific news sentiment on financial assets. Knowledge-Based Systems, 150, 116–126. https://doi.org/ 10.1016/j.knosys.2018.03.004

Kilgarrif, A., & Grefenstette, G. (2003). Introduction to the special issue on the web as corpus. Computational Linguistics, 29(3), 333–347. https://doi.org/10.1162/ 089120103322711569

Kim, K., Jin, Y., Na, S.-H., & Kim, Y.-K. (2017). Centershared sliding ensemble of neural networks for syntax analysis of natural language. Expert Systems with Applications, 83, 215–225. https://doi.org/10.1016/j. eswa.2017.04.048

Kiryakov, A., Popov, B., Terziev, I., Manov, D., & Ognyanof, D. (2004). Semantic annotation, indexing, and retrieval. Web Semantics: Science, Services and Agents on the World Wide Web, 2(1), 49–79. https://doi. org/10.1016/j.websem.2004.07.005

Ko, Y., Park, S., Seo, J., & Choi, S. (2007). Using classification techniques for informal requirements in the requirements analysis-supporting system. Information and Software Technology, 49(11), 1128–1140. https://doi.org 10.1016/j.infsof.2006.11.007

Kumar, E. (2011). Natural language processing. I.K. International Publising House Pvt. Ltd.

Landauer, T. K., Foltz, P. W., & Laham, D. (1998). An introduction to latent semantic analysis. Discourse Processes, 25(2–3), 259–284. https://doi.org/10.1080 01638539809545028

Lee, K., Han, S., & Myaeng, S.-H. (2018). A discourse-aware neural network-based text model for document-level text classification. Journal of Information Science, 44(6), 715–735. https://doi.org/10.1177/0165551517743644

Lee, T. (2007). Constraint-based ontology induction from online customer reviews. Group Decision and Negotiation, 16(3), 255–281. https://doi.org/10.1007 s10726-006-9065-3

Lee, Y.-S., & Wu, Y.-C. (2007). A robust multilingual portable phrase chunking system. Expert Systems with Applications, 33(3), 590–599. https://doi.org/10.1016/j. eswa.2006.06.022

Leonardi, P. M., & Barley, S. R. (2008). Materiality and change: Challenges to building better theory about technology and organizing. Information and Organization, 18 (3), 159–176. https://doi.org/10.1016/j.infoandorg.2008. 03.001

Liu, C.-L., Lee, C.-H., & Ding, B.-Y. (2012). Intelligent computer assisted blog writing system. Expert Systems with Applications, 39(4), 4496–4504. https://doi.org/10. 1016/j.eswa.2011.09.139

Liu, R., & Zhang, X. (2018). Generating machine-executable plans from end-user’s natural-language instructions. Knowledge-Based Systems, 140, 15–26. https://doi.org 10.1016/j.knosys.2017.10.023

Lopez-Cozar, R. (2015). Using knowledge on word-islands to improve the performance of spoken dialogue systems. Knowledge-Based Systems, 88, 223–243. https://doi.org 10.1016/j.knosys.2015.07.029

Lopez-Cozar, R., Callejas, Z., & Griol, D. (2010). Using knowledge of misunderstandings to increase the robustness of spoken dialogue systems. Knowledge-Based Systems, 23(5), 471–485. https://doi.org/10.1016/j. knosys.2010.03.004

Luhn, H. P. (1958). The automatic creation of literature abstracts. IBM Journal of Research and Development, 2 (2), 159–165. https://doi.org/10.1147/rd.22.0159

Mangassarian, H., & Artail, H. (2007). A general framework for subjective information extraction from unstructured English text. Data & Knowledge Engineering, 62(2), 352–367. https://doi.org/10.1016/j.datak.2006.10.001

Manning, C., & Schütze, H. (1999). Foundations of statistical natural language processing. MIT press.

Manning, C., Surdeanu, M., Bauer, J., Finkel, J., Bethard, S., & McClosky, D. (2014). The Stanford CoreNLP natural language processing toolkit [Paper presentation].

Proceedings of 52nd annual meeting of the association for computational linguistics: System demonstrations, Baltimore, Maryland, USA

Maria Ruiz-Martinez, J., Valencia-Garcia, R., Tomas Fernandez-Breis, J., Garcia-Sanchez, F., & Martinez-Bejar, R. (2011). Ontology learning from biomedical natural language documents using UMLS. Expert Systems with Applications, 38(10), 12365–12378. https://doi.org/ 10.1016/j.eswa.2011.04.016

Markus, M. L., & Silver, M. S. (2008). A foundation for the study of IT efects: A new look at DeSanctis and Poole’s concepts of structural features and spirit. Journal of the Association for Information Systems, 9(10), 5. https://doi. org/10.17705/1jais.00176

Mathiesen, K. (2004). What is information ethics? SIGCAS Computers and Society, 34(1), 6. https://doi.org/10.1145/ 1050305.1050312

Mimno, D., Wallach, H., Talley, E., Leenders, M., & McCallum, A. (2011). Optimizing semantic coherence in topic models [Paper presentation]. Proceedings of the 2011 conference on empirical methods in natural language processing , Edinburgh, Scotland, UK

Mitkov, R. (2014). The Oxford handbook of computational linguistics (2nd ed.). Oxford University Press.

Montoyo, A., Martinez-Barco, P., & Balahur, A. (2012). Subjectivity and sentiment analysis: An overview of the current state of the area and envisaged developments. Decision Support Systems, 53(4), 675–679. https://doi. org/10.1016/j.dss.2012.05.022

Ng, H. T., & Zelle, J. (1997). Corpus-based approaches to semantic interpretation in NLP. AI Magazine, 18(4), 45. https://doi.org/10.1609/aimag.v18i4.1321

Nistor, N., Dascalu, M., Serafin, Y., & Trausan-Matu, S. (2018). Automated dialog analysis to predict blogger community response to newcomer inquiries. Computers in Human Behavior, 89, 349–354. https://doi.org/10. 1016/j.chb.2018.08.034

O’Shaughnessy, D. (2008). Automatic speech recognition: History, methods and challenges. Pattern Recognition, 41 (10), 2965–2979. https://doi.org/10.1016/j.patcog.2008. 05.008

Oller, J. W. (1972). On the relation between syntax, semantics, and pragmatics. Linguistics, 10(83), 43–55. https:// doi.org/10.1515/ling.1972.10.83.43

Palvia, P., Leary, D., Mao, E., Midha, V., Pinjani, P., & Salam, A. F. (2004). Research Methodologies in MIS: An Update. The Communications of the Association for Information Systems, 14(1), 58.

Palvia, P., Mao, E., Salam, A., & Soliman, K. S. (2003). Management information systems research: What’s there in a methodology? Communications of the Association for Information Systems, 11(1), 16. https:// doi.org/10.17705/1CAIS.01116

Pan, S. J., Toh, Z., & Su, J. (2013). Transfer joint embedding for cross-domain named entity recognition. ACM Transactions on Information Systems (TOIS), 31(2), 7. https://doi.org/10.1145/2457465.2457467

Pang, B., & Lee, L. (2008). Opinion mining and sentiment analysis. Foundations and Trends in Information Retrieval, 2(1–2), 1–135. https://doi.org/10.1561/ 1500000011

Paredes-Valverde, M. A., Valencia-García, R., Rodríguez-García, M. Á., Colomo-Palacios, R., & Alor-Hernández, G. (2016). A semantic-based approach for querying linked data using natural language. Journal of Information Science, 42(6), 851–862. https://doi.org/10. 1177/0165551515616311

Penalver-Martinez, I., Garcia-Sanchez, F., Valencia-Garcia, R., Rodriguez-Garcia, M. A., Moreno, V., Fraga, A., & Sanchez-Cervantes, J. L. (2014). Feature-based opinion mining through ontologies. Expert Systems with Applications, 41(13), 5995–6008. https://doi.org/10. 1016/j.eswa.2014.03.022

Perez, A., Gojenola, K., Casillas, A., Oronoz, M., & de Ilarraza, A. D. (2015). Computer aided classification of diagnostic terms in spanish. Expert Systems with Applications, 42(6), 2949–2958. https://doi.org/10.1016 j.eswa.2014.11.035

Plummer, D. C., Andrews, W., Marquis, H., McGuire, M., Chesini, F., Leow, A., Reynolds, M., Lovelock, J. D., Hill, J. B., Furlonger, D., Smith, D. M., & Revang, M. (2017). Top strategic predictions for 2018 and beyond: Pace yourself, for sanity’s sake. Gartner databse.

Polites, G. L., Roberts, N., & Thatcher, J. (2012). Conceptualizing models using multidimensional constructs: A review and guidelines for their use. European Journal of Information Systems, 21(1), 22–48. https://doi. org/10.1057/ejis.2011.10

Rai, A. (2017). Editor’s comments: Diversity of design science research. MIS Quarterly, 41(1), iii–xviii.

Ramesh, G., Selvakumar, K., & Venugopal, A. (2017). Intelligent explanation generation system for phishing webpages by employing an inference system. Behaviour & Information Technology, 36(12), 1244–1260. https:/ doi.org/10.1080/0144929X.2017.1369569

Reiter, E., Dale, R., & Feng, Z. (2000). Building natural language generation systems (Vol. 33). MIT Press.

Reiter, E., Sripada, S., Hunter, J., Yu, J., & Davy, I. (2005). Choosing words in computer-generated weather forecasts. Artificial Intelligence, 167(1–2), 137–169. https://doi.org/10.1016/j.artint.2005.06.006

Rowe, F. (2014). What literature review is not: Diversity, boundaries and recommendations. Taylor & Francis.

Rychtyckyj, N. (2007). Machine translation for manufacturing: A case study at ford motor company. AI Magazine, 28(3), 31. https://doi.org/10.1609/aimag.v28i3.2053

Rychtyckyj, N., & Plesco, C. (2013). Applying automated language translation at a global enterprise level. AI Magazine, 34 (1), 43. https://doi.org/10.1609/aimag.v34i1.2436

Sarker, S., Chatterjee, S., Xiao, X., & Elbanna, A. (2019). The sociotechnical axis of cohesion for the IS discipline: Its historical legacy and its continued relevance. MIS Quarterly, 43(3), 695–719. https://doi.org/10.25300 MISQ/2019/13747

Shams, M., & Baraani-Dastjerdi, A. (2017). Enriched LDA (ELDA): Combination of latent Dirichlet allocation with word co-occurrence analysis for aspect extraction. Expert Systems with Applications, 80, 136–146. https://doi.org 10.1016/j.eswa.2017.02.038

Soderland, S. (1999). Learning information extraction rules for semi-structured and free text. Machine Learning, 34 ( 1 – 3 ) , 2 3 3 – 2 7 2 . h t t p s : / / d o i . o r g / 1 0 . 1 0 2 3 / A:1007562322031

Stubbs, M. (1996). Text and corpus analysis: Computerassisted studies of language and culture. Blackwell Oxford.

Tang, D., Wei, F., Qin, B., Yang, N., Liu, T., & Zhou, M. (2015). Sentiment embeddings with applications to sentiment analysis. IEEE Transactions on Knowledge and Data Engineering, 28(2), 496–509. https://doi.org/10.1109/ TKDE.2015.2489653

Uysal, A. K., & Gunal, S. (2012). A novel probabilistic feature selection method for text classification. Knowledge-Based Systems, 36, 226–235. https://doi.org/ 10.1016/j.knosys.2012.06.005

Vaishnavi, V., Kuechler, W., & Petter, S. (2017). Design science research in information systems. Retrieved from http://desrist.org/desrist/content/design-scienceresearch-in-information-systems.pdf

Valencia-Garcia, R., Martinez-Bejar, R., & Gasparetto, A. (2005). An intelligent framework for simulating robot-assisted surgical operations. Expert Systems with Applications, 28(3), 425–433. https://doi.org/10.1016/j. eswa.2004.12.003

Vilares, D., Alonso, M. A., & Gómez-Rodríguez, C. (2015). A linguistic approach for determining the topics of Spanish Twitter messages. Journal of Information Science, 41(2), pp. 127–145. https://doi.org/10.1177/ 0165551514561652

Vlas, R. E., & Robinson, W. N. (2012). Two rule-based natural language strategies for requirements discovery and classification in open source software development projects. Journal of Management Information Systems, 28(4), 11–38. https://doi.org/10.2753/mis0742- 1222280402

Wand, Y., & Wang, R. Y. (1996). Anchoring data quality dimensions in ontological foundations. Communications of the ACM, 39(11), 86–95. https://doi.org/10.1145/ 240455.240479

Wang, Y., & Xu, W. (2018). Leveraging deep learning with LDA-based text analytics to detect automobile insurance fraud. Decision Support Systems, 105, 87–95. https://doi. org/10.1016/j.dss.2017.11.001

Wei, X., Huang, H., Nie, L., Zhang, H., Mao, X.-L., & Chua, T.-S. (2016). I know what you want to express: Sentence element inference by incorporating external knowledge base. IEEE Transactions on Knowledge and Data Engineering, 29(2), 344–358. https://doi.org/10. 1109/TKDE.2016.2622705

Weigand, H. (2005). LAP: 10 years in retrospect [Paper presentation]. The 10th international working conference on the language-action perspective on communication modeling, Linköping, Sweden

Whitwam, R. (2019). Fake-news-generating AI deemed too dangerous for public release. Retrieved from https:// www.extremetech.com/extreme/285857-fake-news-generating-ai-deemed-too-dangerous-for-public-release

Winograd, T. (1972). Understanding natural language. Cognitive Psychology, 3(1), 1–191. https://doi.org/10. 1016/0010-0285(72)90002–3

Wong, W., Liu, W., & Bennamoun, M. (2012). Ontology Learning from text: A look back and into the future. Acm Computing Surveys, 44(4), 1–36. https://doi.org/10.1145/ 2333112.2333115

Yang, G., Wen, D., Chen, N.-S., & Sutinen, E. (2015). A novel contextual topic model for multi-document summarization. Expert Systems with Applications, 42(3), 1340–1352. https://doi.org/10.1016/j.eswa.2014.09.015

Yu, H., Kim, W., Hatzivassiloglou, V., & Wilbur, J. (2006). A large scale, corpus-based approach for automatically disambiguating biomedical abbreviations. Acm Transactions on Information Systems, 24(3), 380–404. https://doi.org/10.1145/1165774.1165778

## Appendix A

## Description D1: Description of the journal search and research procedure

For a comprehensive coverage of the NLP literature published in the field of IS, we conducted a broad review. We identified all journals listed on the MIS journal ranking page of the Association for Information Systems (AIS, n.d.), the 45 journals rated and ranked by Holsapple (2009), and the composite journal ranking by Fisher et al. (2007). This yielded a list of 102 journals. Next, we searched various scholarly database, including EBSCOHost’s Academic Search Complete and Business Source Complete, all databases within Proquest (e.g., ABI/INFORM) and all databases within PsycNet (e.g., PsycINFO), using terms as “Natural Language Processing” or “NLP” in title, abstract, or keywords in IS journals from 2004 to 2018. Many journals had no publications that matched our search terms. Additionally, some identified journals were not electronically accessible via business databases. In such cases, if possible, we used the search features of the journal’s website. We then reviewed every retrieved article to make sure that they were NLP related IS publications. Overall, our search resulted in 356 articles from 36 diferent journals for further analysis.

Three researchers then engaged in three phases of review and analysis. The purpose of the review was to organise the articles based on an organising framework that we established. All phases of coding followed the sampling approach similar to Sarker et al. (2019). The first phase includes two steps. In the first step, the researchers coded a set of 50 articles randomly selected from the literature corpus and categorised them based on Palvia et al. (2003) classification of IS methodologies. The researchers met to discuss issues and problems encountered during this coding process. One such instance is where all researchers independently found that Palvia et al. (2003) did not include design science research (DSR) as a methodology in their categorisation,<sup>1</sup> whereas the review sample was dominated by DSR. The researchers therefore agreed to proceed coding all DSR articles into two categories, “frameworks, conceptual models, methods, or instantiations” per its design artefact, and “laboratory experiment” per its evaluation.<sup>2</sup> Coding was then completed for all articles in the corpus. In the second step, keyword frequencies were analysed. A more detailed description of Phase 1 is provided in Description D2 of the Appendix.

The second phase aimed to develop an organising framework for the corpus review. To do so, the researchers first sampled 50 articles to analyse how NLP studies were conceptualised and realised. Discussion among the researchers led to the creation of an organising framework that included – NLP research orientations (i.e., NLU and NLG), three foundational linguistic analysis dimensions (i.e., syntactics, semantics, and pragmatics), and three IS research dimensions (i.e., algorithms, prototypical NLP tasks, and design artefacts). In the third phase, the articles were then classified based on the organising framework. Following the approach from prior systematic literature reviews, all researchers joined in discussion until consensus was achieved (Polites et al., 2012).

## Description D2: Description of phase 1, two-step assessment of the NLP Literature

This section describes the first phase where we conducted a two-step assessment of the NLP literature. First, to understand the nature of NLP research published in IS journals, we assessed the research methodologies commonly employed in these studies. Second, we analysed keyword frequencies to explore popular and important NLP topics studied by IS researchers. These two steps are described below.

## D2.1. Assessment of NLP research methodologie

To determine how NLP research fits within IS discourse, we first conducted a detailed assessment of methodologies commonly used in NLP research based on the compilation of 12 methodologies identified by Palvia et al. (2003) as applicable to IS research.<sup>3</sup> Our review identified some studies employing more than one methodology. In such cases, we coded each study up to four methodologies. The initial coding result shows that the top four methodologies that most commonly appeared in NLP research are “frameworks, conceptual models, methods, or instantiations”, “laboratory experiment”, “secondary data”, and “library research”. The remaining eight methodologies account for less than 5% of published NLP literature, four of which (interview, field study, qualitative research, and field experiment) do not appear at all.

## D2.2. Keyword frequency assessment

In this second step, we analysed keyword frequencies in our corpus, assuming that keywords would highlight important NLP topics addressed in each study. We applied stemming and lemmatisation to present the keywords in their base forms (e.g., semantics, semantic, and semantic analyses are all processed as their base form – semantics). Table A1 ranks frequencies of each base form keyword and its percentage based on total keywords from our corpus.

The most frequent keyword was “semantics”, which appeared in diferent forms, such as semantic web, semantic similarity, semantic analysis, semantic annotation, etc. This highlights the dominance of semantic-NLP in IS research, which we explored further in Section 5 of the paper. Other frequently appearing keywords such as “information extraction”, “information retrieval”, “text classification”, “sentiment analysis”, “opinion mining”, and “word sense disambiguation” were all representative of the prototypical NLP tasks that we synthesised. Another frequent keyword was “ontology”, which is a formal specification of a shared conceptualisation (Gruber, 1993). Ontologies are the building blocks for inference techniques based on semantic web technologies. Correspondingly, a closer look at related literature shows other ontology-related tasks such as NLI (Corcoglioniti et al., 2016) and SA (Penalver-Martinez et al., 2014). This highlights the popularity of research integrating advanced and powerful NLP techniques with ontology-based machine-readable domain vocabularies.

Table A1. Summary of keyword frequency in NLP literature.

<table><tr><td>Rank</td><td>Keyword</td><td>Freq.</td><td>%</td></tr><tr><td>1</td><td>Semantics</td><td>77</td><td>8.24%</td></tr><tr><td>2</td><td>Information extraction</td><td>45</td><td>4.81%</td></tr><tr><td>3</td><td>Sentiment analysis</td><td>37</td><td>3.96%</td></tr><tr><td>4</td><td>Information retrieval</td><td>34</td><td>3.64%</td></tr><tr><td>5</td><td>Machine Learning</td><td>31</td><td>3.32%</td></tr><tr><td>6</td><td>Text mining</td><td>30</td><td>3.21%</td></tr><tr><td>7</td><td>Text classification</td><td>29</td><td>3.10%</td></tr><tr><td>8</td><td>Ontology</td><td>22</td><td>2.35%</td></tr><tr><td>9</td><td>Text summarisation</td><td>15</td><td>1.60%</td></tr><tr><td>10</td><td>Word sense disambiguation</td><td>14</td><td>1.50%</td></tr><tr><td>11</td><td>Named entity recognition</td><td>14</td><td>1.50%</td></tr><tr><td>12</td><td>Deep learning</td><td>14</td><td>1.50%</td></tr><tr><td>13</td><td>Artificial intelligence</td><td>12</td><td>1.28%</td></tr><tr><td>14</td><td>Question answering</td><td>12</td><td>1.28%</td></tr><tr><td>15</td><td>Opinion mining</td><td>11</td><td>1.18%</td></tr></table>

Additionally, three closely related keywords, “text mining”, “machine learning”, and “deep learning”, together represented one of the most important application areas of NLP – the process of extracting interesting and non-trivial patterns from unstructured text. Almost all text mining research in our literature corpus involved the use of NLP methods and techniques. While NLP research in IS journals also covers conventional application areas such as “question answering”, “artificial intelligence (AI)” has attracted significant attention recently. Among 12 articles that had “artificial intelligence” as one of the keywords, nine were published after 2012. This finding coincides with what is regarded as the third wave of NLP development (Deng, 2018) – the arrival of NLP and AI heralded by the striking success of speech recognition in 2010–2011.

## Description D3: Description of the prototypical tasks

NLP-related IS research often combines several prototypical tasks to solve a real-world problem. To the best of our knowledge, no study has comprehensively reviewed or synthesised the tasks most commonly addressed in NLP research. Identifying these tasks provides a starting point for IS researchers engaging in the NLP research landscape. While it is not practical to list an exhaustive set of NLPrelated tasks, we synthesised 12 prototypical NLP tasks based on a thorough review of published NLP literature and commonly used NLP tools. Table A2 maps 11 out of 12 prototypical tasks with seminal NLP literature. Notably, ontology research is rarely included in the literature. However, in IS research, ontology-related NLP studies have attracted much attention, owing to the popularity of reasoners and inference engines for NLU and NLG. Our analysis also showed “ontology” as a frequently used keyword in the NLP literature corpus (see Table A2). Ontologies along with reasoners enable natural language inferencing or semantic annotation. Thus, we added natural language inferencing (NLI) as one of the prototypical tasks.

Below we describe each prototypical task in detail.

## 3.1. Text classification/categorisation (TC)

With the fast-paced growth of textual information in electronic data, text classification/categorisation has gained increasing attention. Based on the similarity attributes of natural language, texts can be classified, managed, and stored to provide conceptual views of text collections. In the last decade, researchers have made eforts to employ intelligent categorisation techniques in NLP studies to address various types of problems, such as diagnostic terms classification (Perez et al., 2015), citation classification (Galgani et al.,

2015), and informal requirements analysis (Ko et al., 2007). Attempts have been made to improve TC eficacy and eficiency by using diferent ML algorithms such as neural networks (Uysal & Gunal, 2012). More recent studies have aimed at enhancing text classification techniques by leveraging utterance semantics (J. Hu et al., 2008) and context-awareness (Vilares et al., 2015; Vlas & Robinson, 2012). The recent growth in the pragmatic orientation of TC may be attributable to two factors – one, the increasing number of IS research investigating TC in a variety of application areas; and two, more focus on improving TC performance with regard to the contexts where it is used.

## 3.2. Information extraction (IE) and information retrieval (IR)

IE is a process to extract specific information (including entities, relationships, events, etc.) from natural language text (Soderland, 1999). The extracted data can then be further processed into structured form to be stored and managed. IR is a relevant, yet slightly diferent process of retrieving useful information of interest from a large volume of text collection. IR is important for the web or system users to find specific knowledge from chaotic data. IE and IR are widely used for syntactic, semantic, and pragmatic NLP. For example, Vlas and Robinson (2012) designed a shallow parsing approach for dealing with phrase-level variation in European languages such as Spanish. To solve problems deriving from syntactic and morpho-syntactic language variations, the proposed approach obtained more precise index terms by extracting syntactic dependencies as complex index terms. Shams and Baraani-Dastjerdi (2017) presented a method that combines LDA topic modelling with semantic relationships for extracting diferent aspects in textual data.

## 3.3 Text summarisation (TS)

Automatic TS dates back to 1958, when Luhn (1958) introduced the concept of “auto abstract”. Since then, many automatic TS approaches and techniques have been explored and proposed. TS is a process to extract the most important information from the source text based on user needs and generate a summary. The summary should be compressed, content-integrated, and readable. Recent NLP studies have started to focus on the pragmatic perspective of text summarisation. For example, Bellot et al. (2016) designed a framework to automatically contextualise a tweet in a short summary.

## 3.4 Machine translation (MT)

MT is the automatic translation of text or speech from one language to another (Karimi et al., 2011). Research in

Table A2. Mapping between prototypical tasks and NLP literature.

<table><tr><td>Source Tasks</td><td>Manning and Schütze (1999)</td><td>Allen (1995)</td><td>Jurafsky and Martin (2000)</td><td>Indurkhya and Damerau (2010)</td><td>Clark et al. (2013)</td><td>Mitkov (2014)</td></tr><tr><td>Text Categorisation/ Classification</td><td>√</td><td></td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>Information Extraction and Retrieval</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Text Summarisation</td><td></td><td>√</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Machine Translation</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td></tr><tr><td>Corpus Analysis</td><td></td><td></td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>Text Generation</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Sentiment Analysis</td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>NL Inferencing</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Grammatical Text Analysis $^{4}$ </td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td></tr><tr><td>Word sense disambiguation</td><td></td><td></td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>Speech Recognition</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>Semantic Annotation</td><td>√</td><td></td><td>√</td><td>√</td><td></td><td>√</td></tr></table>

MT originated soon after ENIAC, the earliest electronic general-purpose computer was developed (Hutchins, 2010). MT focuses on decoding the source text and reencoding into the target language. Behind this seemingly simple task lies complex cognitive operations. MT requires an in-depth knowledge of linguistic attributes such as idioms, cultural context, and mood of text source for both the source and target language. Challenges in MT may be summarised as – how to “understand” the meaning of a text and how to “generate” a text in the target language. MT has attracted much interest among researchers as they have important and influential role in many NLP applications. Examples of studies include global-level enterprises (Rychtyckyj & Plesco, 2013) and motor manufacturing companies (Rychtyckyj, 2007) where MT has been applied for appropriate and accurate translations that benefit the business process and customer satisfaction.

## 3.5 Corpus analysis (CA)

A corpus is a carefully structured set of reference material that acts as lexical resources for NLP. CA involves employing various corpus-linguistic methods to analyse and/or compare the features of corpora (Stubbs, 1996). A corpus may feature one or more of the following characteristics: the corpus inventory should achieve a certain scale; the data must be authentic materials (written or spoken); and, the data in the corpus must be processed and labelled in advance (Kilgarrif & Grefenstette, 2003). A corpus may be monolingual or multilingual according to the number of languages it contains. Applications of corpus analysis include corpus-based approaches to semantic interpretation in NLP (Ng & Zelle, 1997), as well as using a corpus of human conversations to train conversational chatterbots to understand contextual continuity (Chakrabarti & Luger, 2015).

## 3.6 Text generation (TG)

NLP places emphasis on both NLG and NLU. TG concentrates on the process of “using discourse strategies and focus constraints to generate natural language text” (Carenini & Moore, 1993). In TG tasks, researchers map computational annotations or representations into human language text. From a commercial perspective, successful TG helps to build up data-to-text systems that generate textual natural language from data stored in databases and data sets. For example, Reiter et al. (2005) built a system to generate textual weather forecasts from weather data by using consistent data-to-words rules. The evaluation of the system indicated that forecast users preferred machine-generated texts to human-generated texts because of better wording. Recent studies have employed TG for pragmatic-NLP applications such as blog writing (Liu et al., 2012) and question answering systems (S. Hu et al., 2017).

## 3.7 Sentiment analysis (SA)

The computational treatment of opinion, sentiment, and subjectivity in text is referred as SA (Pang & Lee, 2008). It emerged in response to the surge of interest in understanding opinions expressed in social media. Specifically, SA targets the recognition of sentiment characteristic in the text of interest, and the rating of sentiment by employing learning method or sentiment dictionary. The SA process can be summarised as identify the sentiment sentences, find keywords (especially, recognise the emotion-relevant words), determine the polarity and score (positive/negative) words, and analyse the emotion tendency of the subject of interest. For example, Kelly and Ahmad (2018) proposed a method to analyse how domain-specific news sentiment influences financial returns over time and created a trading signal based on predicted news impact.

## 3.8 NL reasoning and inference (NLI)

Considerable literature has been published on NLI in the past decade focusing on the development and application of reasoner and inference engines. Over the years, reasoners have evolved from constraint solver and rule-based engines to ontology-based reasoning and case-based reasoning (Bikakis et al., 2007). Research in NLI has covered a wide range of applications such as analysing customer review (T. Lee, 2007), designing intelligent conversational systems (Herbert & Kang, 2018), and improving text autocompletion (Wei et al., 2016). More recently, semantic web techniques have gained popularity in NLI research and have been widely employed owing to its inherent inference capabilities (Ramesh et al., 2017).

## 3.9 Grammatical text analysis (GT)

This task utilises a clustering of methods to analyse sentence structure, including natural language parsing, and part of speech tagging (Gómez-Rodríguez, 2014). It is often used for a preliminary treatment of natural language data. GT can be employed to chunk multilingual portable phrases (Lee & Wu, 2007), and to label grammatical relations as features for text classification (Kim et al., 2017).

## 3.10 Word sense disambiguation (WSD)

This prototypical NLP task employs “supervised, unsupervised, and knowledge-based approaches” to identify “the meaning of words in context in a computational manner” (Borah et al., 2014). WSD is a challenging research problem in NLP domain. It involves the analysis of the cooccurrences of words to measure context similarity and disambiguate word sense. Researchers have used WSD to automatically disambiguate biomedical abbreviations (Yu et al., 2006), as well as for supporting recommender systems (Gutiérrez et al., 2016)

## 3.11 Speech recognition (SR)

The emergence of NLP technique for SR aligns with the development of interactive technologies on mobile devices. SR represents a clustering of approaches relevant to the recognition and processing of spoken language (O’Shaughnessy, 2008). NLP technique for spoken language is diferent from text-related techniques, because the audio signal often contains speaker-specific features with greater uncertainties arising from NL communication and utterance. More specifically, SR relies on phonetic analysis, a process that enables the recognition of spoken language and its translation into text. SR has gained increasing attention among IS researchers. For example, various techniques have been proposed to increase the performance of spoken dialogue system (Eisman et al., 2016; Lopez-Cozar, 2015).

## 3.12 Semantic annotation (SAN)

SAN is the process of annotating meta-data and usage schema expressed in semantic web (Kiryakov et al., 2004). With the advancement in semantic web techniques, NLP scholars have widely adopted ontologies to represent knowledge and conduct SAN. For example, Cuzzola et al. (2015) proposed a new algorithm for automating the tuning of semantic annotation tools that are capable of interlinking syntactical texts with their underlying semantic concepts.

## Description D4: Description of Correlation Analysis between Coding Categories

Correlation analysis is performed to understand how 12 prototypical tasks align with two other coding categories (i.e. NLP research orientations and linguistic analysis dimensions).

We first created a Pearson correlation matrix between 12 prototypical tasks and three linguistic dimensions (i.e., syntactics, semantics, and pragmatics), as shown in Table A3 below. For each prototypical task, we selected the linguistic dimension that has the highest correlation score. For example, the Pearson’s r is 0.059 between the grammatical text analysis (GT) and syntactics, 0.016 between GT and semantics, and 0.005 between GT and pragmatics. This indicates that the correlation between GT and syntactics is the strongest. Thus, Figure 5 in the manuscript places GT near syntactics.

Note that there are negative (inverse) correlation coeficients between some tasks and linguistic dimensions. A negative correlation coeficient describes the extent to which a prototypical task and a linguistic dimension moves in opposite directions. For example, the Pearson’s r is −0.029 between speech recognition and syntactics. This means that an increase in speech recognition is associated with a decrease in syntactics. Similarly, an increase in speech recognition is also associated with a decrease in semantics, while it is positively associated with pragmatics. Hence, Figure 5 in the manuscript shows that speech recognition is closely related to pragmatics.

Because the expected correlation coeficient (r) between a task and linguistic dimension is small (between 0.01 and 0.08), the total sample size required to determine whether r is significant (i.e., difers from zero) is large (Hulley et al., 2013). For example, if α (two-tailed) = 0.05; β = 0.20 (Type II error rate) and expected correlation coeficient r = 0.05, the desired sample size is 3137. Our sample size is only 356. Hence, we are unable to do a statistically significant test of the coeficients in Table A3.

Similarly, we created a Pearson correlation matrix between 12 prototypical tasks and natural language generation (NLG) as shown in Table A4. Because the expected r between each task and NLG varies, the desired sample size is also diferent between NLG and diferent prototypical tasks. The statistic significant test shows that the three highest correlations between NLG and text summarisation, machine translation, and text generation are statistically significant at $p < . 0 1$ where our sample size (356) satisfies the required sample size to draw such a conclusion. For three other tasks that are statistically significant at $\begin{array} { r } { p < . 0 5 . } \end{array}$ , our sample size is not suficient to determine if the test can reject the null hypothesis. Thus, we infer that text summarisation, machine translation, and text generation are highly correlated to NLG, and show this conclusion in Figure 5 of the manuscript.

Table A3. Correlations between tasks and linguistics dimensions<sup>#</sup>.

<table><tr><td>Task</td><td>Syntactics</td><td>Semantics</td><td>Pragmatics</td></tr><tr><td>Information extraction and information retrieval</td><td>0.002</td><td>0.083</td><td>0.025</td></tr><tr><td>Text classification or categorisation</td><td>-0.010</td><td>0.042</td><td>0.005</td></tr><tr><td>Text summarisation</td><td>-0.059</td><td>0.099</td><td>-0.036</td></tr><tr><td>Machine translation</td><td>0.027</td><td>-0.020</td><td>-0.058</td></tr><tr><td>Corpus analysis</td><td>-0.072</td><td>0.081</td><td>-0.024</td></tr><tr><td>Text generation</td><td>-0.057</td><td>0.036</td><td>0.052</td></tr><tr><td>Sentiment analysis or opinion mining</td><td>-0.089</td><td>0.028</td><td>0.090</td></tr><tr><td>NL inference</td><td>-0.072</td><td>-0.017</td><td>0.082</td></tr><tr><td>Grammatical text analysis</td><td>0.059</td><td>0.016</td><td>0.005</td></tr><tr><td>Word sense disambiguation</td><td>-0.057</td><td>0.006</td><td>0.094</td></tr><tr><td>Speech recognition</td><td>-0.029</td><td>-0.047</td><td>0.121</td></tr><tr><td>Semantic annotation</td><td>-0.119</td><td>0.119</td><td>0.016</td></tr></table>

<sup>#</sup>The bold text indicates the highest correction score of the related prototypical task.

Table A4. Correlations between tasks and NLG.

<table><tr><td>Task</td><td>NLG (r)</td><td>Sample Size (α =.05)</td><td>Sample Size (α =.01)</td></tr><tr><td>Information extraction and information retrieval</td><td>-0.093</td><td>783</td><td>1163</td></tr><tr><td>Text classification or categorisation</td><td>-0.105**</td><td>783</td><td>1163</td></tr><tr><td>Text summarisation</td><td>0.498*</td><td>29</td><td>42</td></tr><tr><td>Machine translation</td><td>0.186*</td><td>194</td><td>287</td></tr><tr><td>Corpus analysis</td><td>0.044</td><td>3137</td><td>4667</td></tr><tr><td>Text generation</td><td>0.445*</td><td>29</td><td>42</td></tr><tr><td>Sentiment analysis or opinion mining</td><td>-0.134**</td><td>462</td><td>686</td></tr><tr><td>NL inference</td><td>-0.013</td><td>783</td><td>1163</td></tr><tr><td>Grammatical text analysis</td><td>-0.130**</td><td>462</td><td>686</td></tr><tr><td>Word sense disambiguation</td><td>0.001</td><td>too large</td><td>too large</td></tr><tr><td>Speech recognition</td><td>0.076</td><td>1224</td><td>1820</td></tr><tr><td>Semantic annotation</td><td>-0.130</td><td>462</td><td>686</td></tr></table>

\*p < .01 \*\*p < .05

## Description D5: Description of AR mining results

To investigate whether the presence of one task would imply the presence of other tasks in the same article, we employed AR mining. The AR mining results showed three significant association rules (Table 2 in the manuscript) which are discussed below.

## Rule 1: Natural Language Inference ≫ Semantic annotation

Our keyword analysis showed that ontology-based inference and reasoning have received much attention in recent years. Semantic web technologies, specifically ontologies, and reasoning engines provide an excellent foundation for NLI (Gacitua et al., 2008; Maria Ruiz-Martinez et al., 2011). This first rule confirms this notion and suggests a strong association between NLI and SAN in published NLP research. Ontologies are the backbone of the semantic web that provide standardised vocabulary to facilitate knowledge acquisition and processing. Concepts and relationships represented by ontologies may be parsed via NLP techniques. For example, Maria Ruiz-Martinez et al. (2011) used text processing techniques (e.g., POS tagging) to obtain relevant concepts and relations from biomedical text to be included in an ontology. With the advancement in semantic web techniques, utilising SAN for NLI is prime for future research.

## Rule 2: Corpus Analysis ≫ Semantic annotation

Our AR mining results indicate the co-occurrence of CA and SAN. As stated by Ng and Zelle (1997), a corpus is a resource that greatly benefits NLP tasks related to text mining and SAN. In recent years, robust syntactic parsers have been built based on large, hand-annotated corpora and statistical techniques. However, these parsers have not been able to capture the semantic meaning of sentences. Hence, adding a semantic representation layer to the syntactic structure of a corpora has attracted research attention. Upon a closer examination, we found many studies that utilised CA in conjunction with SAN for automated discovery of concepts and relations among them. For example, Freitas et al. (2011) employed SAN to query linked data in Wikipedia using a vocabulary independent approach.

## Rule 3: Text Generation ≫ IE & IR

Another finding from AR mining is the co-occurrence of IE and IR with TG. As discussed in Description D3, TG is a crucial task associated with NLG. One of the important subtasks in TG is to determine the kind of communication in natural language (Reiter et al., 2000). It involves content determination and discourse structuring, both of which are closely related to IE and IR. For example, Herbert and Kang (2018) designed and implemented an intelligent conversation system, where IE and IR techniques were used to retrieve relevant texts based on the user’s question, and the retrieved texts were then used as input for TG. Similarly, Liu et al. (2012) utilised IR techniques to obtain text examples from the Web as inputs for blog generation.
