---
otero_id: 3090
otero_key: "WKM6UFVM"
title: "An Ontology of Emotion Process to Support Sentiment Analysis"
authors: "Veda C. Storey; Eun Hee Park"
year: "2022"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00749"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2022

# An Ontology of Emotion Process to Support Sentiment Analysis

Veda C. Storey , vstorey@gsu.edu

Eun Hee Park

, epark@odu.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# An Ontology of Emotion Process to Support Sentiment Analysis

Veda C. Storey,<sup>1</sup> Eun Hee Park<sup>2</sup>

<sup>1</sup>Georgia State University, USA, VStorey@gsu.edu <sup>2</sup>Old Dominion University, USA, epark@odu.edu

## Abstract

Sentiment analysis is used to mine text data from many sources, including blogs, support forums, and social media, in order to extract customers’ opinions and attitudes. The results can be used to make important assessments about a customer’s attitude toward a company and if and how a company should respond. However, much research on sentiment analysis uses simple classification, where the polarity of a text that is mined is classified as positive, negative, or neutral. This research creates an ontology of emotion process to support sentiment analysis, with an emphasis on obtaining a more fine-grained assessment of sentiment than polarity. The ontology is grounded in a theory of emotion process and consists of concepts that capture the generation of emotion all the way from the occurrence of an event to the resulting behaviors of the person expressing the sentiment. It includes two lexicons: one for affect and one for appraisal. The ontology is applied to posts obtained from customer support forums of large companies to show its applicability in a multilevel evaluation. Doing so provides an example of a complete ontology assessment effort.

Keywords: Sentiment Analysis, Ontology of Emotion Process, Emotion, Ontology, Lexicon, Appraisal, Affect, Sentiment, Polarity, Event, Design Science Research

Huigang Liang was the accepting senior editor. This research article was submitted on September 8, 2019 and underwent three revisions.

## 1 Introduction

There has been explosive growth in user-generated content on social media over the past two decades (Boone et al., 2019; Wang et al., 2020). Customers who purchase products and services often generate a large amount of text data about their experiences on social media. Angry customers might boycott a company or post negative comments, whereas positive comments can bolster sales and retention as potential customers read reviews that express the opinions of existing customers (Kumar & Reinartz, 2018). Companies thus need to be able to control their online reputation. To do so, it would be useful for companies to know how customers respond to their products so that they can “respond to their responses.” For example, if a customer assesses that a product is not working, the customer might become angry and threaten the company with a lawsuit or refuse to buy from the company again (Park et al., 2012; Park et al., 2019). Understanding the process by which customers become angry (for example) and then trying to alleviate this anger would be helpful. However, to know what action to take, a company needs to first understand the behavior and what motivated it or triggered an action.

Sentiment analysis is opinion mining or subjectivity analysis achieved by natural language processing, computational linguistics, and text analysis (Cambria et al., 2020; Pang & Lee, 2008). It is “the computational study of people’s opinions, attitudes, and emotions”

toward something (Medhat et al., 2014)<sup>1</sup> and is useful for businesses that seek to extract customers’ opinions about their products or services (Kontopoulos et al., 2013; Liu & Zhang, 2012). Opinions are subjective and represent “people’s sentiments, appraisals, or feelings toward entities, events, and their properties” (Liu, 2010, p. 627).

Sentiment analysis of online text data is useful because it can provide insights into how to support customers, address complaints, and advertise products (Abbasi et al., 2018; Chau & Xu, 2012; Liu et al., 2017; Stauss & Seidel, 2019). Consider the following paraphrased excerpts from an online discussion forum. Such forums have been shown to influence post-purchase behavior and often include refusals to purchase from a company in the future. <sup>2</sup> The first threatens legal action, the second expresses frustration.

Customer A: Everyone who appears to have received “repairs” from this company has the same problems. This is terrible and absurd! I am so outraged! Let’s consider a class-action lawsuit.

Customer B: I also implemented the company’s suggested “fix” with absolutely no success. I expect that the hardware is fine because I have other things to work on.

It is necessary to distinguish between appraisal (e.g., not working) and affect (e.g., feeling angry), although this distinction is usually not recognized in research on sentiment analysis. Prior research suggests that customers have different affect resulting from their appraisals of events and show idiosyncratic responses toward a company (Gelbrich, 2010). For example, after a service failure, angry customers who attribute a goalobstructive event to an external source, such as a specific company, might engage in vindicative wordof-mouth or complaint activities (Gelbrich, 2010). Frustrated customers who attribute a goal-obstructive event to an uncontrollable situation might engage in word-of-mouth communication, with the intent of seeking support from others. They might also engage in complaint activities but seek to resolve their problem. Extracting appraisal and affect can help companies avoid negative results. A company’s strategy to respond to a customer showing anger might include compensation, which can be considered “the most powerful service recovery effort” or informational support (e.g., explanation) (Gelbrich, 2010, p.580). A company’s strategy for a customer expressing frustration could focus on encouraging support-seeking behaviors to reduce complaints by providing communication and information support. Capturing appraisal and affect can thus help a company identify when it needs to take explicit action, avoid escalation of an issue, prioritize customers’ issues, customize response strategies, and generally prevent reputational damage.

Much sentiment analysis research classifies the polarity of text as positive, negative, or neutral (Abbasi et al., 2008; Kontopoulos et al., 2013; Liu, 2012; Storey & O’Leary, in press). Sentiment analysis studies have not captured or represented the interrelated constructs that reflect the reason why a customer feels angry or happy. Nor have they considered how a customer expresses an affect that resulted from the customer’s appraisal of a situation. Affect refers to the feelings that an individual experiences. <sup>3</sup> Sharing affect can lead to customers becoming emotional or even irrational. Therefore, affect is a major force in shaping the outcomes of a customer’s attitude toward a company or product (Park et al., 2012).

Indeed, studies on sentiment analysis rarely reveal how emotions are generated. The question addressed in this research thus becomes: How can we support sentiment analysis by capturing the process of generating emotions? Such insights could, for example, enable companies to provide customized services to resolve a customer’s issue that caused a negative reaction. Two important components of this process are how someone appraises a situation (appraisal) and the feelings of the individual triggered by the appraisal of the situation (affect). If we could capture both appraisal and affect and clearly distinguish them while understanding the context within which they occur, this would assist in capturing a more fine-grained level of understanding of emotion than previously possible.

The objective of this research is to support sentiment analysis by focusing on affect and contextual information which, taken together, can provide insights into how emotions are generated. We develop an ontology of emotion process, with specific components that capture affect and contextual information (appraisal and event). This research is based on a theory of emotion process in which emotion is viewed as a dynamic, multi-componential phenomenon (Frijda, 2007). Generating emotions starts when an individual (e.g., a customer) encounters a significant event and appraises (or evaluates) that event. The appraisal can trigger affect, which a company might want to capture and analyze.

To carry out the research, we took a design science approach that develops an ontology of emotion process as a technical artifact and includes lexicons for the appraisal and affect components. The ontology is evaluated at multiple levels (architecture/design, lexical, and context/application). The contribution of this research is an ontology of emotion process to support sentiment analysis. The ontology strives to capture rich and meaningful constructs. The evaluation is a multilevel assessment, often lacking in ontology research (Brank et al., 2005; McDaniel & Storey, 2019). This paper proceeds as follows. Section 2 reviews related research on general sentiment analysis, aspect-based sentiment analysis, and ontology-based approaches to sentiment analysis. Sections 3 and 4 describe the development and evaluation of the ontology of emotion process, respectfully. Section 5 discusses the implications and Section 6 concludes the paper.

## 2 Related Research

This section reviews research on sentiment analysis to identify its significant challenges and ontology-based approaches to sentiment analysis. Table 1 first describes the main terms used throughout this paper.

## 2.1 Sentimental Analysis

Sentiment analysis enables information systems to extract sentiment from text (Abbasi et al., 2008) so the user can appreciate the attitude of the contributor. Social media has created much interest in sentiment analysis, with user feedback and recommendations a common source of information on products and services for both companies and customers (Polites et al., 2018). User-generated content can be analyzed, in part, by natural language processing. Sentiment classification uses taxonomies to label words, phrases, or documents. Techniques include polarity tags (e.g., a word is labeled as positive or negative) and appraisal groups (e.g., attitude, graduation, orientation) (Whitelaw et al., 2005).

## 2.2 Challenges of Sentiment Analysis

A significant amount of research has focused on sentiment analysis, using a variety of approaches and techniques. Much of sentiment analysis attempts to address the difficult problem of capturing affect (emotion) from text. Appendix A summarizes prominent review articles that provide an overview of the work that has been carried out on sentiment analysis; based on this, the authors identify specific, related, challenges and research gaps. Several trends emerge.

First, overall, these articles reveal a heavy reliance on polarity classification, which organizes the results into distinct classes that might be labeled positive or negative, good or bad, etc. This labeling provides limited insight. (Albeit, knowing whether a customer, for example, has a positive or negative attitude toward something is useful.) Polarity classifications usually require an underlying lexicon that identifies sentiment terms, which is difficult to develop (Hussein, 2016) because the size and content of a lexicon limit its uses, especially for terms that are domain or topic dependent (Qazi et al., 2017).

Second, affect is an important indicator of sentiment because the intensity of affect is closely associated with the level of sentiment (Liu, 2010). However, there is no good, comprehensive way to capture affect because it is usually not explicitly mentioned in text. Furthermore, it is not easy to identify affect when there is a reliance on keywords (Liu, 2010).

Third, many studies have captured different types of discrete emotions for sentiment analysis (e.g., Abbassi & Chen, 2008; Bae & Lee, 2012; Mohammad, 2012). Most of them provide a coarse classification of affect (Liu, 2012). A finer level that captures contextual information related to affect is needed. Such information could help explain, for example, why a customer experiences a specific affect. Especially in social media studies, there is a problem interpreting information extracted, due, in part, to relying on keywords without considering the relationships among affect and contextual information, resulting in a low accuracy level.

## 2.3 Aspect-Based Sentiment Analysis

Sentiment analysis is a topic related to both natural language processing and data mining (Basiri et al., 2021). Commercial tools have been developed, applied, and analyzed (Ahmed Abbasi & Dhar, 2014). Sentiment analysis, often called opinion mining, can be conducted at three levels: document-level, sentiment-level, and aspect-level. Aspect-based sentiment analysis, which is the interest of our study, extracts specific entities and aspects from un/structured texts (Nazir et al., 2020). The aspect includes a variety of concepts such as opinions, judgments, thoughts, ways of thinking, perspectives, and social themes (Nazir et al., 2020). Aspect-based sentiment analysis has been conducted through three major phases (Nazir et al., 2020): (1) aspect extraction (extracting implicit/explicit aspects, aspect terms, or entities) (Ma et al., 2018); (2) aspect sentiment analysis (classifying polarity for an aspect or entity and developing semantic relationships between different aspects or entities to increase classification accuracy) (Yang et al., 2018); and (3) sentiment evolution (capturing aspects or events over a given period of time) (Chi et al., 2018).

Table 1. Terms and Descriptions

<table><tr><td>Term</td><td>Description</td></tr><tr><td>Affect</td><td>A broad range of feelings that individuals experience, including feeling states and traits (e.g., positive and negative affectivity) (Barsade &amp; Gibson, 2007, p. 38).</td></tr><tr><td>Emotion</td><td>Category of feeling states, elicited by target or cause. Includes physiological reactions and action sequences that are relatively intense and short-lived (Barsade &amp; Gibson, 2007, p. 37). Discrete emotion examples include joy, anger, or fear.</td></tr><tr><td>Appraisal</td><td>Individual&#x27;s thoughts, perceptions, evaluations, and judgments of an event of interest (Frijda, 2007; Frijda et al., 1989)</td></tr><tr><td>Contextual information</td><td>Information on an event and other components that triggers affect in the individual (e.g., event and appraisal).</td></tr><tr><td>Lexicon</td><td>Terms used to describe the vocabulary of a language or branch of knowledge (Oxforddictionaries.com, 2017). Supports retrieval of sentiment text by representing basic token (word or phrase instrumental to sentiment analysis (Liu, 2012; Zernik, 1991).</td></tr><tr><td>Ontology</td><td>Specification of a conceptualization; defines a set of formal constructs and the relationships among them (Gruber, 1993).</td></tr><tr><td>Polarity</td><td>Positive or negative assessment sentiment. Can be assessed at the document, sentence, or phrase level (Abbasi et al., 2008).</td></tr><tr><td>Sentiment</td><td>“Attitude, thought, or judgment prompted by feeling notion” (Munezero et al., 2014, p. 102). Can be captured by cognitive data (e.g., judgment, thought, opinion) and affective data (e.g., feeling, emotion) (Liu, 2012).</td></tr></table>

While aspect-based sentiment analysis offers a great benefit to help analyze sentiments that occur in social media, by extracting various aspects over time across different contents (Wang et al., 2015), it struggles with the following challenges (Nazir et al., 2020). First, to improve the aspect extraction process, how should the explicit/implicit aspects be extracted and the relationships between the different aspects or entities be mapped to each other? Second, to improve aspect sentiment analysis, how can one determine whether to perform the analysis at the aspect or entity level? Our research attempts to address these challenges by proposing an ontology-based sentiment analysis.

## 2.4 Ontology-Based Sentiment Analysis

An ontology, generally, represents concepts and their relationships in a domain of interest (Dragoni et al., 2022; Gruber, 1993; Stojanovic et al., 2004) Representative, prior ontology-based sentiment analysis studies that extract terms from text and map them to constructs in an ontology are summarized in Table 2. The ontologies can be classified as supporting: (1) polarity analysis, or (2) a hybrid of polarity and contextual information. This research adopts a hybrid ontology approach since the objective is to capture more than polarity.

For polarity, the purpose of an ontology is to capture polarity from affect-suggesting texts (e.g., positive, negative) and/or types of emotions. Zhou and Chaovalit (2008) propose ontology-supported polarity mining (OSPM) to analyze movie reviews and classify them as positive or negative. ArsEmotica (Baldoni et al., 2012) infers emotions from social tagging sites for art. Its ontology has 87 categories, with a sentiment score (positive or negative) and a strength score (level of semantic affinity of a term with an affect) calculated on the data retrieved. For hybrid analysis, most ontologies capture both contextual information and the polarity of affect-suggesting texts but do not extract interrelated constructs that would capture the process of generating an emotion. Grassi et al. (2011) develop a human emotion ontology that extracts emotion and contextual information such as associated appraisal, regulation, and type of modalities, and incorporate a Semantic Web technique to analyze blog contents.

An ontology-based approach to sentiment analysis has important benefits. First, an ontology can be designed to capture contextual (or background) information, in addition to sentiment constructs (Balahur et al., 2012; Lopez et al., 2008). For a given purpose, specific constructs and relationships can be added (Balahur et al., 2012; Cambria et al., 2013). Second, ontologies can increase the accuracy and possibility of retrieving sentiment-bearing terms (Cambria et al., 2020; Dragoni et al., 2022; Stojanovic et al., 2004). In contrast to syntactical techniques, an ontology-based approach can detect sentiments, expressed using constructs that do not directly convey affect but are implicitly associated with other constructs that do (Balahur et al., 2012; Cambria et al., 2015). Ontologies have been recognized as a promising tool that can capture both explicit and implicit sentiment to improve the aspect extraction process (Nazir et al., 2020). Third, an ontology helps to map relationships. An ontology’s structure, as a knowledge base, supports both defining target constructs and their relationships, even in different domain concepts, and deriving implicit aspect information for improved extraction performance (de Kok et al., 2018). Fourth, strong theoretical support obtained from emotion theories can be used to design an ontology (Balahur et al., 2012; Grassi, 2009).

Table 2. Representative Studies of Ontology-Based Sentiment Analysis

<table><tr><td>Study</td><td>Ontology</td><td>Sentiment analysis</td><td>Ontology structure</td><td>Uniqueness of study</td></tr><tr><td>Zhou &amp; Chaovalit, 2008</td><td>Online products &amp; services ontology</td><td>Polarity mining;semantic orientation</td><td>Ontology-supporting polarity mining</td><td>Movie review contextSupervised and unsupervised techniques for sentiment analysis</td></tr><tr><td>Polpinij &amp; Ghose, 2008</td><td>Lexical variation ontology</td><td>Sentiment classifier based on support vector machine algorithm</td><td>Ontology-supporting polarity mining</td><td>Online product review contextLexical ontology acquisition for variations of nouns and verbs</td></tr><tr><td>Lau et al., 2009</td><td>Product domain ontology</td><td>Context-sensitive polarity;semantic orientation</td><td>Ontology-supporting hybrid analysis of polarity and contextual information</td><td>Customer review contextPredict polarity of sentiment by a variant of Kullback-Leibler divergence statistical learning technique (Kullback, 1968)Context-sensitive opinion mining system</td></tr><tr><td>Garcia-Crespo et al., 2010</td><td>Customer emotion ontology &amp; CRM ontology</td><td>Latent semantic analysis; TF-IDF (term frequency-inverse document frequency)</td><td>Ontology-supporting polarity mining</td><td>Customer relationship management (CRM) contextVector space model applied in natural language documentsCustomer emotion ontology: negative and positive affect</td></tr><tr><td>Wei &amp; Gulla, 2010</td><td>Product ontology</td><td>Hierarchical learning (HL)-sentiment ontology tree (SOT) algorithm</td><td>Ontology-supporting hybrid analysis of polarity and contextual information</td><td>Product review contextSOT: tree-like ontology structureHL-SOT approach: attributes identification and sentiment annotation tasks</td></tr><tr><td>Grassi et al., 2011</td><td>Human emotion ontology</td><td>Natural language processing module;semantic parser;AffectSpace</td><td>Ontology-supporting hybrid analysis of polarity and contextual information</td><td>Social media contextSentic Web using artificial intelligence (AI) and Semantic Web techniques to extract opinion and sentiments</td></tr><tr><td>Baldoni et al., 2012</td><td>Emotion ontology Word ontology</td><td>Emotional semantics from tagged resources;polarity</td><td>Ontology-supporting polarity mining</td><td>Artwork classification contextOntology structured emotional categories in taxonomy (87 constructs)Collections of tags</td></tr><tr><td>Balahur et al., 2012</td><td>EmotiNet ontology</td><td>Semantic role labeling (SRL) system</td><td>Ontology-supporting analysis of emotion and action</td><td>International survey of emotional antecedents and reactions (ISEAR) corpus (few/no lexical clues for affect)Comparative analysis for emotion detection among supervised, lexical knowledge-based, and ontology-based methodsEmotionNet action chains and emotion tags</td></tr><tr><td>Kontopoulos et al., 2013</td><td>Product domain ontology</td><td>Sentiment score based on the intensity of sentiment expression</td><td>Ontology-supporting opinion mining and product</td><td>Microblogging contextOntology created and attributes detected by formal concept analysis and ontology learning</td></tr><tr><td>Ali et al., 2017</td><td>SWRL rule ontologyFuzzy ontology</td><td>Polarity of opinionated phrases</td><td>Ontology-supporting hybrid analysis of polarity andcontextual information</td><td>Feature extraction (transportation &amp; city features)SentiWordNet scoring (transportation &amp; city phrases scoring)Opinion lexiconsFuzzy logic for classification</td></tr><tr><td>Dragoni et al., 2018; Dragoni et al., 2022</td><td>Emotion ontology (MFOEM)</td><td>Polarity and emotions</td><td>Ontology-supporting hybrid analysis of polarity and contextual information</td><td>Contextual informationSenticNet (a semantic network)Commonsense knowledge organized at entity, concept, and primitive levelsGraph-mining and multidimensional scaling techniques</td></tr></table>

## 2.5 Lexical Development for Sentiment Analysis

Ontology-based sentiment analysis typically involves four phases (D’Andrea et al., 2015): (1) the data input phase where data is collected from social media sites; (2) the sentiment detection phase, in which an ontology guides the decisions on what data should be retained or removed; (3) the sentiment classification phase, during which sentiment is classified at the document, sentence, or aspect levels (with lexicon-based classification the most commonly used method (Ghiassi et al., 2013; Medhat et al., 2014) and the focus of our research; and (4) the output presentation phase, where unstructured text format results are organized to present meaningful information.

There are two classes of techniques for sentiment analysis: a lexicon-based approach and a machinelearning approach (Medhat et al., 2014). Within the lexicon-based approach (Liu, 2012) the dictionarybased approach uses dictionaries and searches synonyms and antonyms of seed words, and the corpus-based approach discovers additional words for a domain corpus, based on known seed words or a general-purpose lexicon. The machine learning approach uses linguistic features and machine learning algorithms (Medhat et al., 2014). There are two types of text classification with a machine learning approach (Ghiassi et al., 2016; Medhat et al., 2014): supervised when there are numerous labeled training documents, and unsupervised, when it is difficult to find labeled training documents. Since our research objective is to develop lexicons for the appraisal and affect components of an ontology of emotion process, the dictionary-based approach is particularly useful when a lexicon is newly developed (Liu, 2012). It is a simple technique, enabling researchers to compile basic tokens from existing dictionaries by starting with a few seed words and bootstrapping based on the structure of a dictionary, and can identify a large number of words easily and quickly.

## 3 Methodology

This research takes a design science approach to developing an artifact, the ontology of emotion process, as shown in Figure 1. There are multiple genres in design science research, with each genre having different goals and processes (Baskerville et al., 2015). This research aims to solve a general problem of representing emotion, as inspired by a problem occurring in practice (carrying out proper sentiment analysis) (Iivari, 2015). We apply the design science research methodology proposed by Peffers et al. (2007) to develop and evaluate useful artifacts. Table 3 summarizes the steps followed in the creation and evaluation of the ontology, based on Peffers et al. (2007).

## 3.1 Artifact Creation

The artifact is an ontology of emotion process. The literature review on sentiment analysis studies, as summarized in Appendix A, revealed little effort to capture the process of generating an emotion. Especially needed is support for capturing affect and associated contextual information to achieve a more fine-grained approach to capturing sentiment than previously possible with research that concentrated mainly on polarity. However, a more fine-grained understanding of emotion can have important implications for appropriate reactions to a situation.

Our objective is to support sentiment analysis by capturing the process of generating an emotion. To do so, we develop a theory-driven, domain-independent ontology. Ontology plays an important role in sentiment analysis by mapping terms to a specific construct, identified based on prior theory and knowledge bases. For example, if the term “angry” appears in an “Affect” construct in the ontology, then, parsing a text with some indication of “angry” and mapping it to the Affect construct would enable a user to make an inference about a customer’s affect. The word angry, a synonym for angry, or a word containing some form of anger, could appear in the text, and they would all be mapped to angry.

![](/api/attachments/WKM6UFVM/fulltext/images/bd0bae2d57a154e1738c686634c62c42e553e27392319970e7fb0f83c9cc0386.jpg)  
Figure 1. The Ontology of Emotion Process

Table 3. Design Science Research Approach to Creation and Evaluation of Process of Emotion Ontology

<table><tr><td>Process</td><td>Step in artifact creation process</td><td>Description</td><td>Activities and outputs of this research</td></tr><tr><td rowspan="3">Artifact creation</td><td>Identity problem and motivate</td><td>Identify an issue that needs to be addressed and motivate seeking a solution</td><td>Need for support for sentiment analysis researchIdentify a research question: How can we support sentiment analysis by capturing the process of generating an emotion?</td></tr><tr><td>Define objectives of solution</td><td>Understand the objectives for seeking a solution</td><td>Improve sentiment analysis to capture affectCapture a more fine-grained level of detailCreate a better solution than polarityCapture and incorporate the process of generating an emotion to understand the relatedness of events, appraisals, and potential outcomes</td></tr><tr><td>Design and develop</td><td>Create artifacts to address the problem</td><td>Create an ontology of emotion processCreate two lexicons (“Affect” and “Appraisal”)</td></tr><tr><td rowspan="2">Artifact evaluation</td><td>Demonstration/example</td><td>Provide evidence of how the artifact is used and an explanation of how the artifact addresses one or more instances of the problem</td><td>Create prototype for sentiment analysis using an ontology of emotion process.Show application of ontology to the sentiment analysis problemProvide an ex ante assessment within a context (Venable et al., 2016)</td></tr><tr><td>Evaluation at multiple levels</td><td>Assess artifacts in formal multilevel evaluation based on utility, efficacy, or other criteria.</td><td>Evaluate ontology at the design levelEvaluate lexicons at the lexical levelEvaluate outcomes of a prototype (artifact instantiation) developed with ontology and lexicons at context/application level</td></tr></table>

As shown in Figure 2, our research extends previous work on emotion theories, sentiment analysis, and ontology-based sentiment analysis. The ontology provides a finer-grained level of detail than prior work on polarity analysis. It does so by capturing contextual information related to affect and developing supporting lexicons on appraisal and affect. The multilevel evaluation assesses the usefulness of the ontology and contributes to an end-to-end evaluation of ontologies.

## 3.2 Artifact Design and Development

The design and development efforts involved the creation of the ontology of emotion process and the “Affect” and “Appraisal” lexicons. Uschold and King (1995) identify ontology development as identifying the purpose and scope; and building, evaluating, and documenting the ontology. These result in the following steps, as identified by prior studies (Gruber, 1995; Medland, 2007; Noy & McGuinness, 2001).

## 3.2.1 Step 1: Identify the Domain and Scope of the Ontology

Our objective is to develop a domain-independent ontology that captures the process of generating an emotion for use in sentiment analysis. Competency questions (Table 4) are helpful during the initial development stage because they help identify the scope, clarify the objective, and guide how the ontology can evolve (Uschold & King, 1995).

![](/api/attachments/WKM6UFVM/fulltext/images/44d537e50ae4f8da94ca7e120d4568825cf42920b0a01a9cf0cbbe35e4857cfe.jpg)  
Figure 2. Solution and Extension of Prior Work

Table 4. Types of Knowledge and Competency Questions

<table><tr><td>Type of knowledge</td><td>Competency questions</td><td>Examples</td></tr><tr><td>Target environment</td><td>Which environment are we targeting?Which characteristics of the environment should we consider?</td><td>Potential target environments: online discussion forum, web blog, social media, etc.Characteristics: types of support forums, types of functions provided in a web blog, etc.</td></tr><tr><td>Target domains</td><td>What is the target domain?Which characteristics of the specific domain should we consider?</td><td>Potential target domains: product review, customer support, healthcare, etc.Characteristics: issues in customer support forums, expressions in online news, etc.</td></tr><tr><td>Target users</td><td>Who are the target users?Which characteristics of users should we consider?</td><td>Potential target users: customers and customer service reps in the customer support forum, readers of web blogs and news feeds, etc.Characteristics: profile of consumers, users, readers, etc.</td></tr><tr><td>Target information</td><td>What is the target information we are looking for?What is the specific information we are looking for?</td><td>Target information: extract sentiments and opinions of consumers, users, and readersSpecific information: patterns of types of event, appraisal, affect, patterns of activities</td></tr></table>

## 3.2.2 Step 2: Identify Sources of Input for Ontology Development from Established Theories

Two theories provide the basis for the ontology’s constructs and relationships. The theory of emotion process (Frijda, 2007; Frijda et al., 1989) provides the major constructs and the relationships among them. Absent from this theory are the dimensions (i.e., valence and activation) of affect, which can present a more finegrained level regarding the details of affect (Russell, 1980, 2009; Scherer, 2005).

(1) Theory of emotion process: A theory provides significant benefits (Baskerville et al., 2014; Kim et al., 2016). First, we adopt Frijda et al.’s (1989) theory of emotion process, which includes affect, its precedence, and outcome, which we represent as concepts in our ontology. (Sometimes these are called entities, constructs, classes, or components). Hence, this theory allows researchers to capture the occurrence and changes of emotion-related constructs. Second, this theory presents emotion as a process with specific components, rather than a simple set of basic emotions and their features (Frijda, 2007). The process identifies the precedence (event, appraisal) that triggers affect and its resulting consequences (e.g., action readiness or behavior). Emotionally significant events such as a technology hardware malfunction or an unfortunate news report can generate affect and “action readiness” after such events are appraised by an individual. Affect and action readiness can lead individuals to change their environment. The concepts and relationships of this theory have been established in various research contexts (Baskerville et al., 2014; Kim et al., 2016).

Thus, the theory enables us to capture the relationships between these components (concepts) in our ontology. This theory also enables us to obtain more fine-grained classification than is possible using polarity analysis.

Event, appraisal, and affect form the main components of the ontology. Patterns exist between: (a) appraisal and affect, (b) appraisal and action readiness, and (c) affect and action readiness (Frijda, 2007). From these patterns, inferences can be made about potential behaviors.

(2) Dimensional approach to representing affect: The affect component is augmented using a “dimensional approach,” which defines affect in terms of dimensions, valance, and activation (Russell, 2003; Scherer, 2005). Valence represents “a subjective feeling of pleasantness or unpleasantness,” whereas activation captures “a subjective state of feeling activated or deactivated” (Barrett, 1998, p. 580). Circumplex models (Russell, 1980; Scherer, 2005) show the location of affect in a circumplex with two dimensions (valence, activation). Valence has an “orientation” attribute and activation has a “graduation” attribute (Argamon et al., 2009; Whitelaw et al., 2005). The application of this dimensional approach allows us to capture rich, finegrained information on affect. Thus, event, appraisal, and effect form the top-level constructs of the ontology. The theoretical bases of the constructs of our ontology are summarized in Table 5.

## 3.2.3 Step 3: Define Classes and Class Hierarchy

The class hierarchy is defined by starting with a topdown identification of classes and subclasses and iterating bottom-up to refine the classes (Noy & McGuinness, 2001). The ontology of emotion process, as shown in Figure 1, consists of constructs (event, appraisal, and affect) and sub-constructs (subject and topic), commonly referred to as classes and subclasses. An event leads to an appraisal, which triggers an affect. Two additional subclasses of Event are subject and topic. A subject (something of interest to a user) must exist before a topic can arise. These are identified based on the competency questions in Step 1. The types of events differ by application.

## 3.2.4 Step 4: Define the Properties of Classes

Each class has properties, such as those shown for the Event and Affect classes in Table 6. For example, TitleOfEvent names the Event. These properties, or slots, represent the elements that constitute each class. The Affect classes, AffectDimensionValence and AffectDimensionActivation, both use the dimensional approach (Scherer, 2005), with levels of valence and activation ranging from +5 to -5.

## 3.3 Lexical Development

Two lexicons are developed: an appraisal lexicon and an affect lexicon. Together, they can play a critical role in automatically retrieving text related to sentiment by identifying basic words and phrases important to sentiment analysis. The appraisal lexicon appears to be the first attempt to develop such a lexicon based on emotion theories. Here, “appraisal” is used in a narrow sense, as a cognitive component that triggers affect (Frijda, 2007). Although Whitelaw et al. (2005) make some attempt to develop appraisal groups, ours is specific to appraisal terms.

The affect lexicon is based on affect detection, with affect words scored on valence and activation dimensions (Bradley & Lang, 1999; Hu et al., 2009; Redondo et al., 2007; Stevenson et al., 2007). Starting from Scherer’s (2005) 36 categories, we map the original placements of Scherer’s affect words to a number that captures the levels of valence and activation. The result is a numeric positioning on the circumplex model to provide a degree of affect. For example, (4, 1) for happiness means an affective state at high positive valence (+4) and medium activation (+1). Our affect lexicon differs from those of other sentiment lexicons (e.g., MPAQ, Bing Liu) in that it includes only affect-indicating words, whereas other lexicons include neural words as well. Appendix B compares our affect lexicon to the MPQA Subjectivity Lexicon and Bing Liu’s sentiment lexicon (Liu, 2012).

We adopt a dictionary-based approach to develop our lexicon. The two most common approaches to ontology development are machine learning based and dictionary based (Liu, 2012; Medhat et al., 2014; Nazir et al., 2020), although the exact method used in the development of the lexicon is less important than how the ontology can be used. The development was based on the following steps (e.g., Liu, 2012; Mohammad et al., 2009; Valitutti et al., 2004): (1) collect a basic set of seed categories or words from the literature, (2) search additional words/phrases by finding synonyms and antonyms from WordNet (Miller et al., 1990) and/or other dictionaries or collect synonymic phrases manually, and (3) add new words/phrases to the existing set of seed words (Whitelaw et al., 2005). The second and third steps are repeated until no further new words/phrases are found. The final step (4) cleans the word/phrase list (Valitutti et al., 2004).

## 3.3.1 Step 1: Identify Seed Words

Affect lexicon seed words: Scherer’s (2005) 36 categories of affect form the seed words, as shown in Table 7. These help to identify terms related to affect from natural language (Tabak & Evrim, 2016). Within each category, there are several word stems with pertinent labels related to affect. These word stems are transformed to complete words, based on their adjectives, adverbs, nouns, and verbs.

Table 5. Top Level Concepts of Ontology for Emotion Process

<table><tr><td>Concept</td><td>Description</td><td>Theoretical approach and sources</td></tr><tr><td>Event</td><td>Various types of context (problem or issue, product, organization, or industry) that an individual encounters.</td><td>Theory of emotion process: (Frijda et al., 1989), (Frijda, 1996), (Frijda, 2007)</td></tr><tr><td>Appraisal</td><td>Individual&#x27;s perception and evaluation of an event of interest.Can be represented by a set of (appraisal) dimensions.</td><td>Theory of emotion process: (Frijda et al., 1989), (Frijda, 2007)</td></tr><tr><td>Affect</td><td>Feeling and emotion.Dimension approach applied to “affect.” Valence and activation dimensions of affect captured.</td><td>Theory of emotion process: (Frijda et al., 1989), (Scherer, 2005), (Frijda, 2007)Dimensional approach of affect: (Russell, 1980), (Barsade &amp; Gibson, 2007)</td></tr></table>

Table 6. Properties of Event and Affect Classes

<table><tr><td colspan="3">Event [Class]</td></tr><tr><td>Property</td><td>Description</td><td>Example</td></tr><tr><td>EventUserID</td><td>Initiator or user of discussion or dialogue</td><td>Z_Klaus</td></tr><tr><td>TitleOfEvent</td><td>Title of event</td><td>Why is the download speed so slow with my notebook?</td></tr><tr><td>StartingTime</td><td>Starting time of discussion or dialogue</td><td>01:10 PM 06-05</td></tr><tr><td>EndingTime</td><td>Ending time of discussion or dialogue</td><td>09:50 PM 09-25</td></tr><tr><td>TotNumberOfPages</td><td>Total # of pages in discussion or dialogue</td><td>5</td></tr><tr><td colspan="3">Affect [Class]</td></tr><tr><td>Property</td><td>Description</td><td>Example</td></tr><tr><td>AffectType</td><td>Types of affect</td><td>anger</td></tr><tr><td>AffectDimensionValence</td><td>Positive (from 1 to 5) vs. negative affect (from -1 to -5)</td><td>Affect_Neg_-3</td></tr><tr><td>AffectDimensionActivation</td><td>Activated (from 1 to 5) vs. deactivated affect (from -1 to -5)</td><td>Affect_inactivated_-2</td></tr></table>

Table 7. Affect Categories (Seed Words) for Affect Lexicon Development

<table><tr><td>Admiration/awe</td><td>Desperation</td><td>Happiness</td><td>Lust</td></tr><tr><td>Amusement</td><td>Disappointment</td><td>Hatred</td><td>Pleasure/enjoyment</td></tr><tr><td>Anger</td><td>Disgust</td><td>Hope</td><td>Pride</td></tr><tr><td>Anxiety</td><td>Dissatisfaction</td><td>Humility</td><td>Relaxation/serenity</td></tr><tr><td>Being touched</td><td>Envy</td><td>Interest/enthusiasm</td><td>Relief</td></tr><tr><td>Boredom</td><td>Fear</td><td>Irritation</td><td>Sadness</td></tr><tr><td>Compassion</td><td>Feeling of affection/love</td><td>Jealousy</td><td>Shame</td></tr><tr><td>Contempt</td><td>Gratitude</td><td>Joy</td><td>Surprise</td></tr><tr><td>Contentment</td><td>Guilt</td><td>Longing</td><td>Tension/Stress</td></tr></table>

Note: Partial affect lexicon is provided in Appendix B.

Table 8. Appraisal Categories (Seed Words) and Examples of Words/Phrases

<table><tr><td>Positive appraisal categories</td><td>Example</td><td>Negative appraisal categories</td><td>Example</td></tr><tr><td>Pleasantness</td><td>Pleasant</td><td>Unpleasantness</td><td>Crappy</td></tr><tr><td>Bearableness</td><td>Bearable</td><td>Unbearableness</td><td>Unbearable</td></tr><tr><td>Goal conduciveness</td><td>Helpful</td><td>Goal obstructiveness</td><td>Crash</td></tr><tr><td>Fairness</td><td>Fair</td><td>Unfairness</td><td>Unfair</td></tr><tr><td>Certainty</td><td>Certain</td><td>Uncertainty</td><td>Uncertain</td></tr><tr><td>Expectedness</td><td>Expected</td><td>Unexpectedness</td><td>Unexpected</td></tr><tr><td>Modifiability</td><td>Can fix</td><td>Unmodifiability</td><td>Can’t fix</td></tr><tr><td>Controllability</td><td>Can handle</td><td>Uncontrollability</td><td>Can’t handle</td></tr><tr><td rowspan="3" colspan="2"></td><td>Responsibility</td><td>Responsible</td></tr><tr><td>Familiarity (time of event in the past)</td><td>Happened yesterday</td></tr><tr><td>Familiarity (time of event at the present)</td><td>Happened today</td></tr></table>

Appraisal lexicon seed words: Human affect and behaviors result from human interpretation, evaluation, and judgment of their situations (Frijda, 2007; Frijda et al., 1989). The theory of emotion process provides appraisal categories (seed words) for the appraisal lexicon. Appraisal is a cognitive evaluation process of an emotionally significant event that can: (1) determine whether affect is generated, and (2) impact its intensity. Examples of the appraisal categories, from which the appraisal terms were drawn, are shown in Table 8. Additional terms are given in Appendix C, which juxtapositions our lexicon with Whitelaw et al.’s (2005) appraisal group.<sup>4</sup>

## 3.3.2 Step 2: Identify Synonyms and Synonymic Phrases

After identifying seed words for the affect and appraisal lexicons, the synonyms of each word are selected from online dictionaries (e.g., Merriam-Webster Thesaurus, Thesaurus.com) and lexicons (e.g., WordNet). If a word has multiple definitions, the one closest to either the affect or appraisal word is selected. For example, for “amusement,” which has two definitions: “the feeling of being entertained or made to laugh” and “an activity that you can take part in for entertainment” (Cambridge Dictionary, 2022). The former definition would be selected for the affect lexicon because it is more affect oriented than the other. As shown in Table 9, we identified synonyms such as “fun and laughter,” which are closely aligned with the affect category of the seed word “amusement” (Scherer 2005).

To create the appraisal lexicon, we collected synonymic phrases, as shown in Appendix C. Relevant phrases were also extracted from online websites (e.g., customer support sites) and by identifying, comparing, and contrasting synonymic phrases from dictionaries.

## 3.3.3 Step 3: Refine Word Lists through Manual Inspection

Cleaning and refining processes ensure there are no typographical errors and that a synonym/phrase belongs to only one affect category or appraisal word. Each synonym was reviewed to check whether the word belonged to more than one category, using definitions from online dictionaries. The affect lexicon contains a total of 1,933 words; the appraisal lexicon has 691 words and phrases. Both the affect and appraisal lexicons have a three-level hierarchical structure, consisting of the affect/appraisal categories, the words derived from word stems, and the synonyms of the derived words. The structure of the affect lexicon is shown in Figure 3. Although lexicons, by nature, are never complete, ours are large enough to investigate their usefulness.

## 3.3.4 Step 4: Score Affect Categories for Affect Lexicon

The affect lexicon required an additional development step. The properties of classes were designed and defined, specifically, AffectDimensionValence and AffectDimensionActivation (Table 6). To assess the levels of valence and activation of affect, we assigned a score to each affect category, based on the affect circumplex model (Scherer, 2005). Doing so provides both previously validated support for the 36 affect seed categories and corresponding numeric values for valence (horizontal) and activation (vertical). As shown in Figure 4, the affect dimensions are positioned on the circumplex to show both levels of positive/negative valence (+5 [high] \~ -5 [low]) and activation (or arousal) (+5 \~ -5). For example, the affect of “excited” has a high positive valence (+4) and a high level of activation (+4).

Table 9. Examples of Word Stems for Affect Words (Adapted from Scherer (2005))

<table><tr><td>Admiration/ Awe</td><td>admir*, ador*, awe*, dazed, dazzl*, enrapt*, enthrall*, fascina*, marveli*, rapt*, reveren*, spellbound, wonder*, worship*</td></tr><tr><td>Amusement</td><td>amus*, fun*, humor*, laugh*, play*, rollick*, smil*</td></tr><tr><td>Fear</td><td>afraid*, aghast*, alarm*, dread*, fear*, fright*, horr*, panic*, scare*, terror*</td></tr><tr><td>Surprise</td><td>amaze*, astonish*, dumbfound*, startl*, stunn*, surpris*, aback, thunderstruck, wonder*</td></tr></table>

![](/api/attachments/WKM6UFVM/fulltext/images/4a2c23c146a3e6fef92fa0bdb5f8281330f632daf35ec1796afb728b5665ca23.jpg)  
Figure 3. Hierarchical Structure of Affect Lexicon

![](/api/attachments/WKM6UFVM/fulltext/images/b59d7f598fc6b7ca6cd045d49fbcb6d1dcb317751022d31795b1d46226475f0d.jpg)  
Figure 4. Affect Categories and Scores in Circumplex Model (Adapted from Scherer, 2005)

The affect of “longing” has a very low positive valence (+1) and medium activation (-2). The scores can be helpful to understand the attributes of a particular affect (i.e., positive/negative and de/activated).

Note that this provides fine-grained information that can help to clarify the state of customers’ affect and indicate when customers are in a state of high negative valence and high activation (e.g., hatred).

## 4 Artifact Evaluation of Ontology of Emotion Process

Many studies have conducted a single-level evaluation of an ontology, but no single approach can be used to effectively evaluate an ontology (Bajaj et al., 2017). For example, applying the ontology to a single application makes it difficult to generalize the results, with an ontology only being assessed as “good” or “bad” for a given task.

Evaluating an ontology at multiple levels (e.g., lexical, semantic relations, application, structure) is a much more rigorous way to assess performance (Bajaj et al., 2017; Brank et al., 2005). Thus, we conducted a multilevel assessment of the ontology of emotion process. In doing so, we contribute to ontology development research by providing a concrete example of this assessment approach.

## 4.1 Example: A Case Study in Social Media

To provide an overall evaluation, we developed a prototype and applied it to extract sentiment from two real-world customer support forums. This commonly used evaluation demonstrates that an artifact can achieve its purpose in at least one context (Venable et al., 2016).

## 4.1.1 Emotion Ontology Prototype

Figure 5 shows the architecture of the Emotion Ontology System. The external input module captures the user’s input. The data extraction workflow contains crawlers for raw data and extractors for information to construct events. Then, the analysis workflow processes the events data for word dependency part-ofspeech (POS) analysis, appraisal analysis, and affect analysis. The output workflow aggregates and visualizes the outcomes with event (subject and topic), appraisal, and affect information.<sup>5</sup>

## 4.1.2 Application to Real-World Customer Support Forums

To apply the prototype, we collected over 375,000 customer-supplied posts that can be used to extract customers’ sentiments. We extracted the posts from two online customer technology support forums, managed by two global technology companies that produce various hardware and software products (notebooks, desktops, phones, tablets, etc.), and refer to the companies as Company A and Company B.<sup>6</sup> Consumers post comments, from which their opinion, appraisal, affect, and attitude, and action readiness can be extracted.<sup>7</sup> They also relate their experiences with malfunctions of technology products to solicit help from company experts and other participants. Examples are shown in Figure 6a (screenshot) and Figure 6b (posts and mapping to the ontology).

The collected data was parsed, stored, and analyzed by the prototype. The terms corresponding to the ontology of emotion process (Figure 1) were retrieved and relevant properties were captured. Table 10 shows the main classes and subclasses with their properties and descriptions.<sup>8</sup> An event has subclasses, Subject and Topic. For Company A, we collected 197,407 posts in 35,980 threads from 37,417 participants. For Company B, there were 184,445 posts, in 44,946 threads from 65,070 participants. Table 11 summarizes this data.

Figure 7 shows partial results and how they might be used. For presentation purposes, the original posts are color coded and presented in the upper boxes. The corresponding results, similarly color coded, are presented in the bottom boxes. The information includes: (1) the subject and topic that triggered affective responses of a customer(s), (2) the detailed features of appraisal and affect, and (3) the change in appraisal and/or affect over time. The latter could be practically used to alert a company to the potential seriousness of a problem. The following information is captured.

• Subject: general and specific subject categories

• Topic: user ID posed a topic, user type, title of topic, time of topic posted, and message number in total pages

• Appraisal: appraisal category (Table 8), orientation of appraisal

![](/api/attachments/WKM6UFVM/fulltext/images/ec79c72c02237a0d047020bb8462201de4e397ec7a1f4db4f557e80196532ba5.jpg)  
Figure 5. Architecture of Emotion Ontology Prototype

![](/api/attachments/WKM6UFVM/fulltext/images/34fb93d003aaa52fd46a688bd586ba31ce854f1d5ec0d0eb94b074632947798d.jpg)  
Figure 6a. Screenshot of Typical Online Customer Support Forum

![](/api/attachments/WKM6UFVM/fulltext/images/9f5c073833c223180cefeab072f40c173b76f916322bdaca888624b8b5f01d57.jpg)  
Figure 6b. Sample Application Emotion Process and Action Readiness

Table 10. Main Properties and Descriptions of Event, Appraisal, and Affect Classes

<table><tr><td colspan="3">Event [Class]</td></tr><tr><td colspan="3">Subject [SubClass]</td></tr><tr><td>Property</td><td>Description</td><td>Example</td></tr><tr><td>GeneralSubjectCategory</td><td>General subject category</td><td>Laptop</td></tr><tr><td>SpecificSubjectCategory</td><td>Specific subject category</td><td>Network/Wireless</td></tr><tr><td colspan="3">Topic [SubClass]</td></tr><tr><td>Property</td><td>Description</td><td>Example</td></tr><tr><td>TopicUserID</td><td>UserID of a topic</td><td>S_Timmy</td></tr><tr><td>UserType</td><td>User type in profile</td><td>Top student</td></tr><tr><td>TitleOfTopic</td><td>Title of topic posted</td><td>Laptop Wi-Fi not working</td></tr><tr><td>TimeOfTopic</td><td>Time of topic posted</td><td>06-18-2012 01:30 PM</td></tr><tr><td>NumInPostings</td><td>Message number in total pages</td><td>3 of 56</td></tr><tr><td colspan="3">Appraisal [Class]</td></tr><tr><td>Property</td><td>Description</td><td>Example</td></tr><tr><td>AppraisalCategory</td><td>Appraisal category based on Frijda&#x27;s appraisal dimension (Frijda, 2007; Frijda et al., 1989): pleasantness (Appraisal_P1), unpleasantness (Appraisal_N1), bearable (Appraisal_P2), unbearable (Appraisal_N2), goal-conducive (Appraisal_P3), goal-obstructiveness (Appraisal_N3), etc.</td><td>Appraisal_N3</td></tr><tr><td>AppraisalOrientation</td><td>Appraisal is positive (Appraisal_Pos) or negative (Appraisal_Neg).</td><td>Appraisal_Neg</td></tr><tr><td colspan="3">Affect [Class]</td></tr><tr><td>Property</td><td>Description</td><td>Example</td></tr><tr><td>AffectCategory</td><td>Category of affect</td><td>Anger</td></tr><tr><td>AffectDimensionValence</td><td>Positive (from 1 to 5) vs. negative affect (from -1 to -5)</td><td>Affect_Neg_-3</td></tr><tr><td>AffectDimensionActivation</td><td>Activated (from 1 to 5) vs. inactivated affect (from -1 to -5)</td><td>Affect_inactivated_-2</td></tr></table>

Note: Only the main properties and descriptions are presented in the tables.

Table 11. Data Collected on Posts

<table><tr><td></td><td>Number of posts</td><td>Number of participants</td><td>Number of event (subject &amp; topic)</td><td>Number of appraisal</td><td>Number of affect</td></tr><tr><td colspan="6">Company A</td></tr><tr><td>Sub12</td><td>58141</td><td>12681</td><td>11431</td><td>27668</td><td>349502</td></tr><tr><td>Sub39</td><td>46886</td><td>6865</td><td>7263</td><td>21214</td><td>293098</td></tr><tr><td>Sub47</td><td>92380</td><td>17871</td><td>17286</td><td>43061</td><td>534401</td></tr><tr><td colspan="6">Company B</td></tr><tr><td>Sub34</td><td>65660</td><td>24434</td><td>17984</td><td>40450</td><td>406800</td></tr><tr><td>Sub36</td><td>81457</td><td>27259</td><td>17964</td><td>45007</td><td>513477</td></tr><tr><td>Sub39</td><td>37328</td><td>13377</td><td>8998</td><td>21517</td><td>233687</td></tr></table>

![](/api/attachments/WKM6UFVM/fulltext/images/750f69ab1445e60352bc19c2adca99439414a2400b46fc7567356f824d234c66.jpg)  
Note: Color-coding for presentation purposes: Green (subject): Blue (appraisal): Yellow (topic): Red: (affect)  
Figure 7. Partial Opinion Results

• Affect: category of affect (Table 7), valence (affect score [x]) and activation (affect score [y]) levels of affect (Figure 4).

Figure 7 shows a post at 02:10 PM, customer#1 has a topic (laptop Wi-Fi not working) related to a subject (laptop). Customer #1 has mixed expressions of appraisal, which are positive (goal conducive) and negative (goal obstructive and uncontrollable). The system also captures customer#1’s affect (“annoyed”), which is a type of affect in the “irritation” affect category (Table 7). The affect score of “irritation” has a valence level (-2) and an activation level (3), which is a low-negative (-2) and medium-activated (or aroused) affect (3).

The results are practically useful because they can capture changes over time. At 02:10 PM, customer#1 has an emotionally significant event related to a subject (laptop). Negative appraisal and annoyance (affect score -2, 3) are expressed. The 2:30 PM post shows involvement by a company administrator.

At 6:15 PM, customer#1 continues to express negative appraisal and further experiences an “angry” affect (score -1, 4), which is a negative (-1) but more highly activated affect (4) than the activation level of “annoyed” (3) above. From this example, one can infer that the issues have not been resolved to customer#1’s satisfaction.

This case can be further analyzed to infer potential behaviors or intentions, as shown in Table 12. The components (event, appraisal, affect) have relationships between them, which are inherently captured in the ontology: the event leads to appraisal, the appraisal triggers affect, and the affect leads to action readiness and behavior (Frijda, 2007). The intensity of the affect can be used to predict behaviors. An individual with high negative intensity tends to “move away” or “move against.” An individual with high positive intensity is likely to “move toward” (in Frijda’s [2007] terms). This case shows how affect can be inferred from fine-grained scores, suggesting the possible behaviors shown in Table 12.

## 4.2 Multilevel Evaluation

This research develops an ontology of emotion process as a purely technical artifact (Venable et al., 2016), with the intent of the ontology becoming part of an automated sentiment analysis system. The evaluation of the ontology artifact follows an accepted design science research evaluation (Venable et al., 2016):

• Why to evaluate—to demonstrate the applicability and usefulness of the ontology of emotion process for sentiment analysis.

• When to evaluate—after completing a detailed literature review on sentiment-related topics, understanding and comparing existing tools, and implementing a prototype.

• How to evaluate—by applying existing ontology evaluation guidelines.

Table 12. Potential Inferences of Behaviors and Intentions

<table><tr><td>Post timeline</td><td>Customer #1 &amp; 02:10 PM</td><td>Customer #1 &amp; 06:15 PM</td></tr><tr><td>Results from prototype</td><td>Event (subject &amp; topic): laptop and Wi-Fi not workingAppraisal: positive goal conduciveAppraisal: negative goal obstructiveAffect: irritation &amp; affect score (-2,3)Appraisal: negative uncontrollable</td><td>Event (subject &amp; topic): laptop and Wi-Fi not workingAppraisal: negative goal obstructiveAppraisal: unfairAffect: angry &amp; affect score (-1,4)Appraisal: negative unfair</td></tr><tr><td rowspan="2">Inference of behaviors/intentions(Frijda, 2007)</td><td>Move away</td><td>Move away and/or move against</td></tr><tr><td>Customer #1 had a positive goalTwo negative appraisals show the customer-appraised product or situation as goal obstructive and uncontrollable.The customer experienced irritation. Affect score shows low-negative (-2) and medium-level activated affect (3).Inference (theory-based): customer likely to “move away.”</td><td>An administrator&#x27;s involvement at 02:30 PM is not effective in changing negative appraisal and affect.The intensity of negative affect increased (activation from 3 to 4).Inference (theory-based): customer likely to “move away (or move against).”</td></tr></table>

The evaluation also remains consistent with existing ontology evaluation guidelines (Brank et al., 2005; Dellschaft & Staab, 2006; Matsokis & Kiritsis, 2010; Wong et al., 2012). This assessment is performed at multiple levels (architecture/design, lexical, and context/application levels), as advocated by Brank et al. (2005), and is one of the first attempts to conduct such a complete evaluation. Table 13 summarizes the evaluation approach at each level.

## 4.2.1 Evaluation at the Architecture and Design Level

Evaluation at the architecture and design level focuses generally on whether the development of the ontology satisfies predefined design criteria or principles and whether it is suitable for further development (e.g., Brank et al., 2005; Gómez-Pérez & Benjamins, 1999; McDaniel & Storey, 2019).

Manual assessment: The criteria for evaluation were extracted from prior studies, as shown in Table 14. An evaluation episode was needed, so we developed the case description shown in Table 15. Nine participants performed an evaluation and provided feedback. In the assessment, the participants were asked to read the instructions and case description (Table 15) and to assess the ontology of emotion process on the evaluation criteria (Table 14). The judges also rated the ontology on the semiotics metrics for ontology assessment (Burton-Jones et al., 2005; McDaniel & Storey, 2019). The results in Table 16 suggest that the syntactic, semantic, and pragmatic qualities are sound (Brank et al., 2005). Table 17 summarizes the participant’s assessment of the main characteristics.

## 4.2.2 Evaluation at Lexical Level

We evaluated the affect and appraisal lexicons against other popular lexicons and tools and reported precision and recall.<sup>9</sup> Popular lexicons are MPQA and A New ANEW. Examples of lexicon-based tools are Semantria and Microsoft Text Analytics API. Although the results from these lexicons and tools are primarily based on polarity, it is possible to compare our work to them in an effort to demonstrate the effectiveness of the affect lexicon.

The comparison lexicons and tools are MPQA, A New ANEW, Semantria, and Microsoft Text Analytics API. These were selected because they have been widely used and cited and cover a variety of approaches to capturing and representing affect. The unique features of the MPQA corpus (Ruppenhofer, 2006) support annotating intensity and capturing the polarity of expressive-subjective elements and direct-subjective expression. A New ANEW (Bradley & Lang, 1999) provides normative affective state ratings for words and also allows for the annotation of words on various dimensions of affect (i.e., pleasure, arousal, and dominance).

Table 13. Multilevel Evaluation

<table><tr><td>Level</td><td>Approach to evaluation</td><td>Description</td></tr><tr><td>Architecture/design</td><td>Assessment by humans</td><td>Ontology users evaluate a set of ontology design criteria or principles (Brank et al., 2005; Burton-Jones et al., 2005).</td></tr><tr><td>Lexical</td><td>Comparison</td><td>Compare affect and appraisal lexicons evaluated against other lexicons using existing corpora (Brank et al., 2005; Vrandečić, 2009).</td></tr><tr><td>Context/application</td><td>Assessment by humans</td><td>Conduct controlled experiments in multiple domains to compare the outcomes of the ontology prototype to outcomes of existing sentiment analysis tools.</td></tr></table>

Table 14. Evaluation Objectives and Items

<table><tr><td rowspan="2">Objective</td><td rowspan="2">Evaluation criteria</td><td rowspan="2">Evaluation item and description</td><td colspan="5">Rating (n = 9)</td></tr><tr><td>Good</td><td>Fair</td><td>Marginal</td><td>Poor</td><td>NA</td></tr><tr><td rowspan="5">Assessment of main characteristicsBurton-Jones et al., 2005; Welty &amp; Andersen, 2005</td><td>Expressiveness</td><td>Ability to faithfully conceptualize the relevant details of a particular domain and represent them in an understandable and unambiguous manner.</td><td>67%</td><td>22%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Temporality</td><td>Ability to track changes of ontology objects over time.</td><td>67%</td><td>22%</td><td>-</td><td>-</td><td>11%</td></tr><tr><td>Extensibility</td><td>Ability to expand the ontology gracefully in order to be able to cope and capture future needs.</td><td>100%</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="2">Objectivity</td><td>Ability to produce conceptualizations of ontologies in a smooth, managed, and guided way.</td><td>56%</td><td>33%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Ability to identify customers&#x27; appraisals and affect regarding a product</td><td>89%</td><td>11%</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="8">Assessment based on semiotics metrics set for ontology qualityBurton-Jones et al., 2005; Gómez-Pérez &amp; Benjamins, 1999</td><td rowspan="2">Syntactic quality</td><td>Lawfulness of syntax (correctness of syntax)</td><td>78%</td><td>11%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Richness of syntax used (breadth of syntax used)</td><td>67%</td><td>22%</td><td>-</td><td>-</td><td>11%</td></tr><tr><td rowspan="3">Semantic quality</td><td>Interpretability (meaningfulness of terms)</td><td>78%</td><td>11%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Consistency (consistency of meaning of terms</td><td>67%</td><td>11%</td><td>11%</td><td>-</td><td>11%</td></tr><tr><td>Clarity (average number of word senses)</td><td>44%</td><td>44%</td><td>-</td><td>-</td><td>11%</td></tr><tr><td rowspan="3">Pragmatic quality</td><td>Comprehensiveness (number of classes and properties)</td><td>44%</td><td>33%</td><td>22%</td><td>-</td><td>-</td></tr><tr><td>Accuracy (accuracy of information)</td><td>67%</td><td>22%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Relevance (relevance of information for a task)</td><td>89%</td><td>11%</td><td></td><td>-</td><td>-</td></tr></table>

Note: NA = No answer provided (participant skipped question)

Table 15. Case Description for Assessment

<table><tr><td>Research problem</td><td>Sentiment analysis mines text to identify and extract subjective information about a topic. Sentiment analysis is widely used for many business applications, ranging from marketing to product review. However, two problems result from using computers for sentiment analysis. It is difficult to capture meaningful concepts from text, such as: (1) the cognitive evaluation and judgment of users' issues and problems (called appraisal), and (2) the feelings and emotions of users.</td></tr><tr><td>Objective of the ontology of emotion process artifact</td><td>Based on the theory of emotion process (Frijda, 2007; Frijda et al., 1989), we develop a domain-independent ontology that can support (1) automatically capturing meaningful concepts related to sentiments and (2) analyzing online forum text. The ontology can capture the following concepts related to sentiments:Ontology of Emotion Process</td></tr><tr><td rowspan="2"></td><td>Event→:LeadsTo→ Appraisal→:Triggers→ AffectSubject→:Creates→ Topic</td></tr><tr><td>Event: indicates various types of context (problem or issue, product, organization, or industry) that an individual encounters.Subject: refers to the things of interest (e.g., laptop that a customer bought).Topic: indicates the topic of discussion or dialogue (e.g., Wi-Fi does not work).Appraisal: indicates evaluation and interpretation of the problem of the product and situation (e.g., Wi-Fi issue delays my work—goal obstructiveness).Affect: it refers to feeling and emotion caused by event and appraisal (e.g., I feel angry).</td></tr><tr><td>Theoretical support</td><td>Frijda's theory of emotion process explains individuals' behaviors through an emotion process consisting of event, appraisal, affect, action readiness, and behavior.</td></tr><tr><td>Context of use</td><td>Text mining in online customer support forums, blogs, news feeds, online communities</td></tr><tr><td>Scope</td><td>Data—texts from online discussion or dialogue</td></tr></table>

Table 16. Evaluation Objectives and Items

<table><tr><td rowspan="2">Objective</td><td rowspan="2">Evaluation criteria</td><td rowspan="2">Evaluation item and description</td><td colspan="5">Rating (n = 9)</td></tr><tr><td>Good</td><td>Fair</td><td>Marginal</td><td>Poor</td><td>Na</td></tr><tr><td rowspan="5">Assessment of main characteristicsBurton-Jones et al., 2005; Welty &amp; Andersen, 2005</td><td>Expressiveness</td><td>Ability to faithfully conceptualize the relevant details of a particular domain and represent them in an understandable and unambiguous manner.</td><td>67%</td><td>22%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Temporality</td><td>Ability to track changes of ontology objects over time.</td><td>67%</td><td>22%</td><td>-</td><td>-</td><td>11%</td></tr><tr><td>Extensibility</td><td>Ability to expand the ontology gracefully in order to cope with and capture future needs.</td><td>100%</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="2">Objectivity</td><td>Ability to produce conceptualizations of ontologies in a smooth, managed, and guided way.</td><td>56%</td><td>33%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Ability to identify customers&#x27; appraisals and affect on a product</td><td>89%</td><td>11%</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="8">Assessment based on semiotics metrics set for ontology qualityBurton-Jones et al., 2005; Gómez-Pérez &amp; Benjamins, 1999</td><td rowspan="2">Syntactic quality</td><td>Lawfulness of syntax (correctness of syntax)</td><td>78%</td><td>11%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Richness of syntax used (breadth of syntax used)</td><td>67%</td><td>22%</td><td>-</td><td>-</td><td>11%</td></tr><tr><td rowspan="3">Semantic quality</td><td>Interpretability (meaningfulness of terms)</td><td>78%</td><td>11%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Consistency (consistency of meaning of terms</td><td>67%</td><td>11%</td><td>11%</td><td>-</td><td>11%</td></tr><tr><td>Clarity (average number of word senses)</td><td>44%</td><td>44%</td><td>-</td><td>-</td><td>11%</td></tr><tr><td rowspan="3">Pragmatic quality</td><td>Comprehensiveness (number of classes and properties)</td><td>44%</td><td>33%</td><td>22%</td><td>-</td><td>-</td></tr><tr><td>Accuracy (accuracy of information)</td><td>67%</td><td>22%</td><td>11%</td><td>-</td><td>-</td></tr><tr><td>Relevance (relevance of information for a task)</td><td>89%</td><td>11%</td><td></td><td>-</td><td>-</td></tr></table>

Note: NA = No answer provided (participant skipped question)

Table 17. Assessment of Main Characteristics

<table><tr><td>Criteria</td><td>Qualitative data</td></tr><tr><td>Expressiveness</td><td>...the connection between event and subject and topic needs further clarification. (P1 = Participant 1)The ontology captures the essential aspects of the sentiment domain in terms of events, appraisal of the events, the affect and a person&#x27;s reaction/intention. (P2)I found the ontology very focused [on] products and customers. Out of these particular domains, I believe some modifications would be needed. (P3)...the differences between the terms Triggers and LeadsTo need clarification. (P4)If you clearly define the domain, I think it could be easily understood since it would relate to the overall subject being evaluated. (P8)</td></tr><tr><td>Temporality</td><td>Changes will be easily tracked. (P1)The notion of time is incorporated in all the objects. Using this time stamp, it may be easy to track the changes in the objects. (P2)It seems the changes can be tracked over time... (P3)This is something that I believe would be heavily influenced by the context... (P8)</td></tr><tr><td>Extensibility</td><td>The ontology appears easily adaptable and extended. (P1)The class structure shown can be easily extended by including more classes. (P2)Easy to expand. (P4 &amp; P6)I think this depends on the goals... If you are solely text mining to measure or evaluat[e] ontologies as a goal, then I think it should be possible to expand or retract the ontology by adjusting the scope that you are evaluating for subjects and topics...(P8)</td></tr><tr><td>Objectivity</td><td>The ontology appears objective. (P1)The relationships between the objects need more clarification...(P2)Good theoretical lens for this [ontology development]. (P5)I feel this is very possible and should be easy to identify [customers&#x27; appraisal and affect on product] based on the customer&#x27;s comments if the subject and topics are well defined. (P8)</td></tr></table>

Two commercial lexicon-based applications are Semantria and Microsoft Test Analytics API, Semantria (Lexalytics, 2018) supports annotating the polarity of a word and rating the sentiment scores of themes, entities, and documents. Microsoft Text Analytics API (Microsoft, 2018) uses classification techniques and assigns scores (close to 0 for negative sentiment and close to 1 for positive).

All of these lexicons and tools support polarity classification. Precision, recall, and accuracy were calculated to measure the performance of our affect lexicon, with the results shown in Table 18. Overall, our affect lexicon outperformed the comparison lexicons in precision and accuracy, except for recall for three of the comparisons. F1-scores indicate that the affect lexicon performed well.

The appraisal lexicon appears to be somewhat unique to our research, so direct comparisons are not possible. The closest related work is that of Whitelaw et al. (2005) who discuss appraisal groups but use different constructs.<sup>10</sup>

## 4.2.3 Evaluation at Context and Application Level

We conducted an online experiment to compare the outcomes of the prototype with the ontology of emotion process to the outcomes of a polarity approach, following Brank et al. (2005) and Venable et al. (2016).

## 4.2.3.1 Research Hypotheses

The testing is based on: (1) the usefulness of the outcomes of the system, (2) the helpfulness of the outcomes for understanding users’ sentiment, and (3) deep analysis support of further analysis.

Usefulness is a user’s perception that the outcomes of a system would enhance performance (Davis, 1989). The prototype provides a fine-grained level of sentiment and affective information. The outcomes include contextual information (event and user appraisal) that triggers an affect (with affective state ratings) in addition to polarity.

comparison of the terms available provides face validity, as does the development process used.

Table 18. Precision, Recall, Accuracy and F1-Score for Comparison Lexicons

<table><tr><td>Lexicon / Tool</td><td>Precision</td><td>Recall</td><td>Accuracy</td><td>F1 score</td></tr><tr><td>Our affect lexicon</td><td>0.7451</td><td>0.5700</td><td>0.9771</td><td>0.6459</td></tr><tr><td>MPQA</td><td>0.1997</td><td>0.8263</td><td>0.9285</td><td>0.3217</td></tr><tr><td>A New ANEW</td><td>0.0845</td><td>0.7165</td><td>0.6999</td><td>0.1512</td></tr><tr><td>Semantria</td><td>0.2912</td><td>0.6354</td><td>0.9184</td><td>0.3993</td></tr><tr><td>Microsoft text analytics API</td><td>0.0375</td><td>0.2421</td><td>0.7688</td><td>0.0649</td></tr></table>

Hypothesis 1: Subjects considering the results from the prototype with the ontology of emotion process are more likely to perceive the prototype as being useful than subjects considering the results from a tool that uses a polarity approach.

Helpfulness is the user’s belief that the outcomes of a system offer effective, proper, and responsive help (Alavi, 1984; Mcknight et al., 2011). Practitioners need to respond quickly to customers’ issues (Abbasi et al., 2008; Balahur et al., 2012), but polarity approaches can only achieve a coarse level of classification and detection of sentiment (including affect) (Liu, 2012). The results from the prototype should be helpful because the prototype captures affect (by extracting valence and activation levels) and identifies what causes specific emotion(s) (by extracting the precedence of affect—event and appraisal).

Hypothesis 2. Subjects considering the results from the prototype with the ontology of emotion process are more likely to perceive the prototype as being helpful than subjects considering the results from a tool that uses a polarity approach.

Deep analysis support is adapted from deep structure usage, which is “the extent to which the user exploits features of the system to perform in the task” (Burton-Jones & Straub, 2006, p. 236). In sentiment analysis, capturing meaningful and insightful information is most important (Rana & Cheah, 2016; Schouten & Frasincar, 2016); thus, we focus on the quality of the outcomes, rather than the prototype. When the level of (deep analysis) support of outcomes becomes higher, the outcomes are more likely to support a user who is engaged in activities associated with sentiment (e.g., compare, conduct further analysis, infer customers behaviors/intentions, or derive insightful conclusions) (Burton-Jones & Straub, 2006). The outcomes from the prototype should improve users’ sentiment analysis tasks since they contain richer information on affect and associated context than polarity, thus providing further insights than previously possible.

Hypothesis 3: Subjects considering the results from the prototype with the ontology of emotion process are more likely to perceive deep analysis support from the outcomes of the prototype than subjects considering the results from a tool that uses a polarity approach.

## 4.2.3.2 Experiment

We conducted an online experiment<sup>11</sup> for two domains (product review and forum discussion). Subjects in each experiment were randomly assigned to assess the outcomes of the prototype compared to those of Semantria (Lexalytics, 2017), a well-known commercial lexicon-based sentiment analysis tool. Semantria uses a polarity approach and identifies positive, negative, and neutral tones from customergenerated content (Ribeiro et al., 2016).

A total of 120 subjects were recruited from Amazon Mechanical Turk for Experiment 1 (70 females and 86 males) and 156 subjects were recruited for Experiment 2 (43 females and 77 males). Among these 276 subjects, 11% had graduate degrees or higher, 75% had undergraduate degrees or were students, and the remainder had high school degrees. 60% of the subjects were 18-34 years, 31% were 34-54 years, and 9% were over 55 years.

Task and procedure: The subjects were randomly assigned to either the Emotion Ontology System prototype or Semantria. They were asked to read the text of a scenario and given results which, they were informed, summarized the sentiment information in the text. An example is given in Appendix D. For the first experiment, we used a product review from Amazon.com and the outcomes from either the prototype or Semantria were shown. The output for the prototype is the data for each component of the ontology of emotion process (event, subject, topic, appraisal, and affect). Semantria (Lexalytics, 2017) provides a report that includes the core elements of polarity. The subjects were given a questionnaire with a manipulation check, demographic questions, and measures associated with usefulness, helpfulness, and deep analysis support. In

Experiment 2 (forum discussion domain), the subjects were given the same instructions, task, and procedure but the text was from forum posts in an online support forum of an IT company.<sup>12</sup>

Constructs and measures: Appendix E provides information on the constructs (usefulness, helpfulness, and deep analysis support), the measurement items, and sources. All measures for the constructs were adapted from prior studies and used multiple items. The constructs were reflectively modeled, and the measurement scales for the questions were on an 11- point Likert scale.

Manipulation checks: Nineteen subjects responded incorrectly in both experiments, so the data from these subjects was removed.

Results: Table 19 provides the descriptive statistics. Cronbach’s alpha is used with all values exceeding 0.700, providing adequate evidence of reliability (Bearden et al., 1993; Yi & Davis, 2003).

Hypothesis testing. A one-way multivariate analysis of variance (MANOVA) was used. Wilks’ lambda test shows that there is a significant difference between the prototype and the Semantria groups on all three dependent variables (usefulness, helpfulness, and deep analysis support). The test provided a multivariate F value (F (8, 128) = 2.662, η<sup>2</sup> = 0.143, p = 0.0098). The result (Wilk’s lambda) is 0.857, significant at the 0.01 level. MANOVA further provides the results of between-group effects, as shown in Table 20. The results imply that the dependent variables (usefulness, helpfulness, and deep analysis support) are significantly different at the 0.001 level.

Post hoc t-tests were conducted to determine whether pairs of means are significantly different between the two groups, with the results shown in Table 21. In Experiment 1, usefulness is significant at t = 3.34, p = 0.001. For helpfulness, the result is significant at t = 3.14, p = 0.002. Deep analysis support is significant at t = 4.45, p < 0.001. In Experiment 2, all three results for the dependent variables are significant at p < 0.001. In both experiments, the effect sizes (Cohen’s d) range from 0.65 to 0.72, except for helpfulness in Experiment 1. This indicates that the prototype has a medium to large effect on the outcomes, compared to Semantria.

Overall, all three hypotheses (H1, H2, and H3) are supported, suggesting that the outcomes from the prototype with the ontology of emotion process are more useful and helpful and provide deeper support, than the outcomes from the representative polarity approach of Semantria.

## 5 Discussion

This research developed an artifact—an ontology of emotion process—based on prior work on emotion theories and ontology development. The ontology development was based on a design science research approach and evaluated with a multilevel assessment.

The ontology is based on the theory of emotion process, which starts from an event that has a subject and topic. The event triggers an individual’s appraisal, which, in turn, leads to the individual experiencing affect, causing action readiness and, eventually, actual behavior (Frijda, 2007; Frijda et al., 1989). In this sense, the relationships between the concepts are inherently represented. Our adoption of this theory extends prior research in which emotion ontologies have focused primarily on a simple classification of types of affect (e.g., anger, joy, fear) and their polarity. The ontology of emotion process is domain-independent and intended to support sentiment analysis.

Capturing contextual information that suggests how emotion is generated is rarely accomplished but can provide rich insights into sentiment (Dragoni et al., 2022; Montoyo et al., 2012). Our ontology of emotion process can capture contextual information from the event (subject or topic) and appraisal that might have triggered an affect, which can then be used to help provide appropriate responses to users’ issues (Zhang et al., 2013). The supporting lexicons are also unique in that they focus on capturing only affect or appraisal terms,<sup>13</sup> and are theory-based (emotion process and dimensional approach of affect, respectively) (Tabak & Evrim, 2016). Our research appears to be the first attempt to develop an appraisal lexicon that focuses on appraisal words/phrases and their synonyms. Both the appraisal and affect lexicons can be used independently of this research.

Although extracting affective information from objective statements is challenging (Balahur et al., 2012), our research does so by capturing the precedence of affect (event and appraisal). This is possible because the theory identifies the relationships between affect and the types of appraisals known to trigger affect (Frijda, 2007; Frijda et al., 1989). The result is a practical way to infer or predict affect from a type of appraisal, even if it is not explicitly expressed. Although prior studies (Argamon et al., 2009; Maas et al., 2011; Whitelaw et al., 2005) use “attitude” to capture affect, appreciation, and judgment, “affect” is extracted in separate concept in this research.

Table 19. Descriptive Statistics

<table><tr><td colspan="2"></td><td colspan="3">Experiment 1 (Product review domain)</td><td colspan="3">Experiment 2 (Forum discussion domain)</td></tr><tr><td rowspan="2">Construct</td><td rowspan="2">Item</td><td colspan="2">Mean (SD)</td><td></td><td colspan="2">Mean (SD)</td><td></td></tr><tr><td>Group 1 (n = 46)</td><td>Group 2 (n = 55)</td><td>Alpha</td><td>Group 1 (n = 66)</td><td>Group 2 (n = 71)</td><td>Alpha</td></tr><tr><td rowspan="3">Usefulness</td><td>UF1</td><td>7.76 (1.45)</td><td>7.02 (1.90)</td><td rowspan="3">0.786</td><td>7.15 (2.10)</td><td>5.35 (2.88)</td><td rowspan="3">0.935</td></tr><tr><td>UF2</td><td>7.74 (1.44)</td><td>6.44 (2.22)</td><td>7.05 (2.28)</td><td>5.52 (2.93)</td></tr><tr><td>UF3</td><td>7.71 (1.86)</td><td>6.76 (2.06)</td><td>7.17 (2.04)</td><td>5.65 (2.88)</td></tr><tr><td rowspan="2">Helpfulness</td><td>HF1</td><td>8.09 (1.13)</td><td>7.11 (1.84)</td><td rowspan="2">0.717</td><td>7.18 (1.90)</td><td>5.66 (2.60)</td><td rowspan="2">0.871</td></tr><tr><td>HF2</td><td>7.70 (1.66)</td><td>6.62 (2.19)</td><td>7.15 (2.12)</td><td>5.35 (3.01)</td></tr><tr><td rowspan="3">Deep analysis support</td><td>DS1</td><td>7.74 (1.63)</td><td>6.33 (2.16)</td><td rowspan="3">0.748</td><td>7.39 (1.90)</td><td>5.82 (2.87)</td><td rowspan="3">0.935</td></tr><tr><td>DS2</td><td>7.76 (1.64)</td><td>6.62 (2.16)</td><td>7.33 (1.73)</td><td>5.94 (2.68)</td></tr><tr><td>DS3</td><td>7.85 (1.35)</td><td>6.20 (2.00)</td><td>7.32 (1.79)</td><td>5.82 (2.86)</td></tr></table>

Note: Group 1: Prototype with the ontology of emotion process. Group 2: Semantria.

Table 20. Results of Tests on Between-Group Effects

<table><tr><td>Dependent variable</td><td>df</td><td>F</td><td>Sig.</td><td>Partial eta squared</td></tr><tr><td colspan="5">Experiment 1 (Product review)</td></tr><tr><td>Usefulness</td><td>1</td><td>10.406</td><td>0.002**</td><td>0.095</td></tr><tr><td>Helpfulness</td><td>1</td><td>9.275</td><td>0.003**</td><td>0.086</td></tr><tr><td>Deep analysis support</td><td>1</td><td>18.469</td><td>0.000***</td><td>0.157</td></tr><tr><td colspan="5">Experiment 2 (Forum discussion)</td></tr><tr><td>Usefulness</td><td>1</td><td>16.194</td><td>0.000***</td><td>0.107</td></tr><tr><td>Helpfulness</td><td>1</td><td>17.691</td><td>0.000***</td><td>0.116</td></tr><tr><td>Deep analysis support</td><td>1</td><td>15.800</td><td>0.000***</td><td>0.105</td></tr></table>

Note: \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001 (two-tailed test)

Table 21. Results of t-test and Effect Size

<table><tr><td colspan="7">Experiment 1 (Product review)</td></tr><tr><td rowspan="2">Dependent variable</td><td colspan="2">Mean (SD)</td><td rowspan="2">T</td><td rowspan="2">Sig.</td><td rowspan="2">Effect Size</td><td rowspan="2">Hypothesis testing</td></tr><tr><td>Group 1 (n = 46)</td><td>Group 2 (n = 55)</td></tr><tr><td>Usefulness</td><td>7.89 (1.24)</td><td>6.86 (1.84)</td><td>3.34</td><td>0.001**</td><td>d = 0.65r = 0.31</td><td>H1: Supported</td></tr><tr><td>Helpfulness</td><td>7.40 (1.32)</td><td>6.74 (1.87)</td><td>3.14</td><td>0.002**</td><td>d = 0.41r = 0.20</td><td>H2: Supported</td></tr><tr><td>Deep analysis support</td><td>7.78 (1.25)</td><td>6.38 (1.89)</td><td>4.45</td><td>0.000***</td><td>d = 0.87r = 0.40</td><td>H3: Supported</td></tr><tr><td colspan="7">Experiment 2 (Forum discussion)</td></tr><tr><td rowspan="2">Dependent variable</td><td colspan="2">Mean (SD)</td><td rowspan="2">T</td><td rowspan="2">Sig.</td><td rowspan="2">Effect size</td><td rowspan="2">Hypothesis testing</td></tr><tr><td>Group 1 (n = 66)</td><td>Group 2 (n = 71)</td></tr><tr><td>Usefulness</td><td>7.12 (1.93)</td><td>5.49 (2.72)</td><td>4.02</td><td>0.000***</td><td>d = 0.69r = 0.33</td><td>H1: Supported</td></tr><tr><td>Helpfulness</td><td>7.17 (1.87)</td><td>5.51 (2.65)</td><td>4.21</td><td>0.000***</td><td>d = 0.72r = 0.34</td><td>H2: Supported</td></tr><tr><td>Deep analysis support</td><td>7.35 (1.59)</td><td>5.86 (2.63)</td><td>3.97</td><td>0.000***</td><td>d = 0.69r = 0.32</td><td>H3: Supported</td></tr></table>

Note: \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001 (two-tailed test). Group 1 = Prototype; Group 2 = Semantria.

Our ontology of emotion process provides a finegrained approach to support aspect-based sentiment analysis in two ways. First, the theory of emotion process and subsequent empirical studies (e.g., Baskerville et al., 2014; Frijda, 2007; Frijda et al., 1989; Kim et al., 2016) provide a strong theoretical grounding for the concepts and relationships built into our ontology. The ontology captures the contextual information that leads to affect, thus providing more information that is more meaningful for capturing emotion than was previously possible. Second, the ontology facilitates the extraction of affect and appraisal at a fine level of granularity. Each affect word is scored on valence (negative -5 \~ positive +5) and activation (passive -5 \~ active +5). Appraisal words have an orientation (positive versus negative). The prototype demonstrates the feasibility of automated sentiment analysis using the ontology of emotion process.

Our multilevel evaluation contributes to research on ontologies by evaluating the ontology at multiple levels, as proposed by Brank et al. (2005), where each level contributes to the overall rigor with which the ontology is assessed. Our research appears to be one of the few attempts to perform such a complete end-toend evaluation.

For practice, the use of the ontology of emotion process for sentiment analysis can aid companies in their customer relationship management and brand management. The ontology was developed to capture the interrelated concepts of event, appraisal, and affect. It extracts richer concepts related to sentiment than polarity because it includes affect and contextual information in the form of an event and appraisal. These insights could assist companies in providing customized services to customers, or protecting their reputation, as has been illustrated by the application to the consumer posts from two real-world global software companies.

For any ontology or lexicon development effort, it is difficult to demonstrate completeness. The ontology of emotion process, including its lexicons, is constructed to be domain independent, making it challenging to both create and test. Future research is needed to address the many other challenges of sentiment analysis, some of which are identified in Appendix A. Further applications of the ontology would be helpful. It might also be useful to incorporate the ontology into existing tools for sentiment analysis and to apply them within various companies on a wide variety of applications.

## 6 Conclusion

This research has developed an ontology of emotion process to support sentiment analysis. The ontology is based on emotion theories from psychology, with the main concepts being event, appraisal, and affect, which lead to action readiness. The ontology includes lexicons for affect and appraisal, both of which were developed as part of this research but could serve as stand-alone lexicons. The ontology contributes to capturing a finer level of granularity than is possible with the current, mostly polarity, approaches to sentiment analysis. It also captures the progression from an event to an outcome. The ontology has been assessed by applying it to various applications in a multilevel evaluation, with the latter demonstrating an end-to-end ontology evaluation process.

## References

Abbasi, A., Chen, H., & Salem, A. (2008). Sentiment analysis in multiple languages: Feature selection for opinion classification in web forums. ACM Transactions on Information Systems, 26(3), 1-34.

Abbasi, A., Zhou, Y., Deng, S., & Zhang, P. (2018). Text analytics to support sense-making in social media: A language-action perspective. MIS Quarterly, 42(2), 1-38.

Abbassi, A., & Chen, H. (2008). Cybergate: A design framework and system for text analysis of computer-mediated communication. MIS Quarterly, 32(4), 811-837.

Adams, D. A., Nelson, R. R., & Todd, P.A. (1992). Perceived usefulness, ease of use, and usage of information technology: A replication. MIS Quarterly, 16(2), 227-247.

Ahmed Abbasi, A. H., & Dhar, M. (2014). Benchmarking Twitter sentiment analysis tools. Proceedings of the 9th International Conference on Language Resources and Evaluation.

Alavi, M. (1984). An assessment of the prototyping approach to information systems development. Communications of the ACM, 27(6), 556-563.

Ali, F., Kwak, D., Khan, P., Islam, S. R., Kim, K. H., & Kwak, K. S. (2017). Fuzzy ontology-based sentiment analysis of transportation and city feature reviews for safe traveling. Transportation Research Part C: Emerging Technologies, 77, 33-48.

Argamon, S., Bloom, K., Esuli, A., & Sebastiani, F. (2009). Automatically determining attitude type and force for sentiment analysis. In Z. Vetulani, H. Uszkoreit (Eds). Human language technology. Challenges of the information society. Springer (pp. 218-231).

Bae, Y., & Lee, H. (2012). Sentiment analysis of Twitter audiences: Measuring the positive or negative influence of popular Twitterers. Journal of the American Society for Information Science & Technology, 63(12), 2521-2535.

Bajaj, G., Agarwal, R., Singh, P., Georgantas, N., & Issarny, V. (2017). A study of existing ontologies in the IoT-domain. Available at https://arxiv.org/pdf/1707.00112.pdf

Balahur, A., Hermida, J. M., & Montoyo, A. (2012). Detecting implicit expressions of emotion in text: A comparative analysis. Decision Support Systems, 53(4), 742-753.

Baldoni, M., Baroglio, C., Patti, V., & Rena, P. (2012). From tags to emotions: Ontology-driven sentiment analysis in the social semantic web. Intelligenza Artificiale, 6(1), 41-54.

Barrett, L.F. (1998). Discrete emotions or dimensions? The role of valence focus and arousal focus. Cognition and Emotion, 12(4), 579-599.

Barsade, S., & Gibson, D. (2007). Why does affect matter in organizations? The Academy of Management Perspectives ARCHIVE, 21(1), 36-59.

Basiri, M. E., Nemati, S., Abdar, M., Cambria, E., & Acharya, U.R. (2021). ABCDM: An attentionbased bidirectional CNN-RNN deep model for sentiment analysis. Future Generation Computer Systems, 115, 279-294.

Baskerville, R., Park, E. H., & Kim, J. (2014). An emote opportunity model of computer abuse. Information Technology & People, 27(2), 155- 181.

Baskerville, R. L., Kaul, M., & Storey, V.C. (2015). Genres of inquiry in design-science research: Justification and evaluation of knowledge production. MIS Quarterly, 39(3), 541-564.

Bearden, W. O., Netemeyer, R. G., & Mobley, M. F. (1993). Handbook of marketing scales. SAGE.

Boone, T., Ganeshan, R., Jain, A., & Sanders, N. R. (2019). Forecasting sales in the supply chain: Consumer analytics in the big data era. International Journal of Forecasting, 35(1), 170-180.

Bradley, M. M., & Lang, P.J. (1999). Affective norms for English words (ANEW): Instruction manual and affective ratings. Technical report C-1, the Center for Research in Psychophysiology, University of Florida.

Brank, J., Grobelnik, M., & Mladenić, D. (2005). A survey of ontology evaluation techniques Proceedings of the Conference on Data Mining and Data Warehouses.

Burton-Jones, A., Storey, V. C., Sugumaran, V., & Ahluwalia, P. (2005). A semiotic metrics suite for assessing the quality of ontologies. Data & Knowledge Engineering, 55(1), 84–102.

Burton-Jones, A., & Straub, D. W. (2006). Reconceptualizing system usage: An approach and empirical test. Information Systems Research, 17(3), 228-246.

Cambria, E., Fu, J., Bisio, F., & Poria, S. (2015). Affectivespace 2: Enabling affective intuition for concept-level sentiment analysis.

Proceedings of the 29th AAAI Conference on Artificial Intelligence (pp. 508-514).

Cambria, E., Li, Y., Xing, F.Z., Poria, S., & Kwok, K. (2020). Senticnet 6: Ensemble application of symbolic and subsymbolic AI for sentiment analysis. Proceedings of the 29th ACM International Conference on Information & Knowledge Management (pp. 105-114).

Cambria, E., Schuller, B., Xia, Y., & Havasi, C. (2013). New avenues in opinion mining and sentiment analysis. IEEE Intelligent Systems, 28(2), 15-21.

Cambridge Dictionary. (2022). Amusement. https://dictionary.cambridge.org/us/dictionary/ english/amusement.

Chau, M., & Xu, J. (2012). Business intelligence in blogs: Understanding consumer interactions and communities. MIS Quarterly, 36(4), 1189- 1216.

Chi, C. G.-Q., Ouyang, Z., & Xu, X. (2018). Changing perceptions and reasoning process: Comparison of residents’ pre-and post-event attitudes. Annals of Tourism Research, 70, 39-53.

Clavel, C., & Callejas, Z. (2016). Sentiment analysis: From opinion mining to human-agent interaction. IEEE Transactions on Affective Computing, 7(1), 74-93.

D’Andrea, A., Ferri, F., Grifoni, P., & Guzzo, T. (2015). Approaches, tools and applications for sentiment analysis implementation. In Proceedings of International Journal of Computer Applications, 125(3), 26-33.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319-340.

de Kok, S., Punt, L., van den Puttelaar, R., Ranta, K., Schouten, K., & Frasincar, F. (2018). Aggregated aspect-based sentiment analysis with ontology features. Progress in Artificial Intelligence, 7(4), 295-306.

Dellschaft, K., & Staab, S. (2006). On how to perform a gold standard based evaluation of ontology learning. Proceedings of International Semantic Web Conference (pp. 228-241).

Dragoni, M., Donadello, I., & Cambria, E. (2022). Ontosenticnet 2: Enhancing reasoning within sentiment analysis. IEEE Intelligent Systems, 37(2), 103-110.

Dragoni, M., Poria, S., & Cambria, E. (2018). Ontosenticnet: A commonsense ontology for sentiment analysis. IEEE Intelligent Systems, 33(3), 77-85.

Egghe, L. (2008). The measures precision, recall, fallout and miss as a function of the number of retrieved documents and their mutual interrelations. Information Processing & Management, 44(2), 856-876.

Frijda, N. H. (1996). Passions: Emotion and socially consequential behavior. In R.D. Kavanaugh, B. Zimmerberg, S. Fein (Eds.), Emotion: Interdisciplinary perspectives (pp. 1-27). Lawrence Erlbaum.

Frijda, N. H. (2007). The laws of emotion. Lawrence Erlbaum.

Frijda, N. H., Kuipers, P., & ter Schure, E. (1989). Relations among emotion, appraisal, and emotional action readiness. Journal of Personality and Social Psychology, 57(2), 212- 228.

Garcia-Crespo, A., Colomo-Palacios, R., Gomez-Berbis, J. M., & Ruiz-Mezcua, B. (2010). LSEMO: A framework for customer social networks analysis based on semantics. Journal of Information Technology, 25(2), 178-188.

Gelbrich, K. (2010). Anger, frustration, and helplessness after service failure: Coping strategies and effective informational support. Journal of the Academy of Marketing Science, 38(5), 567-585.

Ghiassi, M., Skinner, J., & Zimbra, D. (2013). Twitter brand sentiment analysis: A hybrid system using n-gram analysis and dynamic artificial neural network. Expert Systems with Applications, 40(16), 6266-6282.

Ghiassi, M., Zimbra, D., & Lee, S. (2016). Targeted twitter sentiment analysis for brands using supervised feature engineering and the dynamic architecture for artificial neural networks. Journal of Management Information Systems, 33(4), 1034-1058.

Gómez-Pérez, A., & Benjamins, R. (1999). Overview of knowledge sharing and reuse components: Ontologies and problem-solving methods. Proceedings of CEUR Workshop.

Grassi, M. (2009). Developing HEO human emotions ontology. In J. Fierrez, J. Javier Ortega-Garcia, A. Esposito, A. Drygajlo, M. Faundez-Zanuy, eds. Biometric ID management and multimodal communication (pp. 244-251). Springer.

Grassi, M., Cambria, E., Hussain, A., & Piazza, F. (2011). Sentic web: A new paradigm for managing social media affective information. Cognitive Computation, 3(3), 480-489.

Gruber, T. R. (1993). A translation approach to portable ontology specifications. Knowledge Acquisition, 5(2), 199-220.

Gruber, T. R. (1995). Toward principles for the design of ontologies used for knowledge sharing? International Journal of Human-Computer Studies, 43(5-6), 907-928.

Hu, Y., Chen, X., & Yang, D. (2009). Lyric-based song emotion detection with affective lexicon and fuzzy clustering method. Proceedings of the 10th International Society for Music Information Retrieval Conference (pp. 123-128).

Hussein, D. M. E. M. (2016). A survey on sentiment analysis challenges. Journal of King Saud University-Engineering Sciences, 30(4), 330- 338.

Iivari, J. (2015). Distinguishing and contrasting two strategies for design science research. European Journal of Information Systems, 24(1), 107-115.

Kaur, A., & Duhan, N. (2015). A survey on sentiment analysis and opinion mining. International Journal of Innovations & Advancement in Computer Science, 4, 107-116.

Kim, J. J., Park, E. H. E., & Baskerville, R. L. (2016). A model of emotion and computer abuse. Information & Management, 53(1), 91-108.

Kontopoulos, E., Berberidis, C., Dergiades, T., & Bassiliades, N. (2013). Ontology-based sentiment analysis of Twitter posts. Expert Systems with Applications, 40(10), 4065–4074.

Korayem, M., Aljadda, K., & Crandall, D. (2016). Sentiment/subjectivity analysis survey for languages other than English. Social Network Analysis and Mining, 6(1), 1-28.

Kumar, A., & Sebastian, T. M. (2012). Sentiment analysis: A perspective on its past, present and future. International Journal of Intelligent Systems and Applications, 4(10), https://www.mecs-press.org/ijisa/ijisa-v4- n10/v4n10-1.html

Kumar, V., & Reinartz, W. (2018). Concepts of customer value. In V. Kumar, W. Reinartz (Eds.), Customer relationship management (pp. 17-29). Springer.

Lau, R. Y., Lai, C. C., Ma, J., & Li, Y. (2009). Automatic domain ontology extraction for context-sensitive opinion mining. Proceedings of the International Conference on Information Systems (pp. 35-53).

Lexalytics. (2017). Text analytics software with sentiment analysis, categorization & named entity extraction. https://www.lexalytics.com/

Lexalytics. (2018). What is text analytics? https://www.lexalytics.com/technology/textanalytics#sentiment

Liu, B. (2010). Sentiment analysis and subjectivity. In N. Indurkhya, F. J. Damerau (Eds.), Handbook of natural language processing (2nd ed., 627- 666). CRC Press.

Liu, B. (2012). Sentiment analysis and opinion mining. Morgan & Claypool.

Liu, B., & Zhang, L. (2012). A survey of opinion mining and sentiment analysis. C. C. Aggarwal, C. Zhai (Eds.), Mining text data (pp. 415-463). Springer.

Liu, X., Burns, A.C., & Hou, Y. (2017). An investigation of brand-related user-generated content on twitter. Journal of Advertising, 46(2), 236-247.

Lopez, J. M., Gil, R., García, R., Cearreta, I., & Garay, N. (2008). Towards an ontology for describing emotions. M.D. Lytras, J.M. Carroll, E. Damiani, R.D. Tennyson (Eds.), Emerging technologies and information systems for the knowledge society (pp. 96-104). Springer.

Ma, Y., Peng, H., Khan, T., Cambria, E., & Hussain, A. (2018). Sentic LSTM: A hybrid network for targeted aspect-based sentiment analysis. Cognitive Computation, 10(4), 639-650.

Maas, A. L., Daly, R. E., Pham, P. T., Huang, D., Ng, A.Y., & Potts, C. (2011). Learning word vectors for sentiment analysis Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics (pp. 142-150).

Matsokis, A., & Kiritsis, D. (2010). An ontology-based approach for product lifecycle management. Computers in industry, 61(8), 787-797.

McDaniel, M., & Storey, V. C. (2019). Evaluating domain ontologies: Clarification, classification, and challenges. ACM Computing Surveys, 52(4), Article 70.

Mcknight, D. H., Carter, M., Thatcher, J. B., & Clay, P.F. (2011). Trust in a specific technology: An investigation of its components and measures. ACM Transactions on Management Information Systems, 2(2), 1-24.

Medhat, W., Hassan, A., & Korashy, H. (2014). Sentiment analysis algorithms and applications: A survey. Ain Shams Engineering Journal, 5(4), 1093-1113.

Medland, M B. (2007). Tools for knowledge analysis, synthesis, and sharing. Journal of Science Education and Technology, 16(2), 119-153.

Microsoft. (2018). Text analytics. Retrieved June 30, 2018, from https://azure.microsoft.com/en-us/ services/cognitive-services/textanalytics/?v=18.05

Miller, G. A., Beckwith, R., Fellbaum, C., Gross, D., & Miller, K.J. (1990). Introduction to wordnet: An on-line lexical database. International Journal of Lexicography, 3(4), 235-244.

Mohammad, S., Dunne, C., & Dorr, B. (2009). Generating high-coverage semantic orientation lexicons from overtly marked words and a thesaurus Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing (pp. 599-608).

Mohammad, S. M. (2012). From once upon a time to happily ever after: Tracking emotions in mail and books. Decision Support Systems, 53(4), 730-741.

Montoyo, A., Martínez-Barco, P., & Balahur, A. (2012). Subjectivity and sentiment analysis: An overview of the current state of the area and envisaged developments. Decision Support Systems, 53(4), 675-679.

Munezero, M. D., Montero, C. S., Sutinen, E., & Pajunen, J. (2014). Are they different? Affect, feeling, emotion, sentiment, and opinion detection in text. IEEE Transactions on Affective Computing, 5(2), 101-111.

Nassirtoussi, A. K., Aghabozorgi, S., Wah, T. Y., & Ngo, D. C. L. (2014). Text mining for market prediction: A systematic review. Expert Systems with Applications, 41(16), 7653-7670.

Nazir, A., Rao, Y., Wu, L., & Sun, L. (2020). Issues and challenges of aspect-based sentiment analysis: A comprehensive survey. IEEE Transactions on Affective Computing, 13(2), 845-863.

Noy, N. F., & McGuinness, D. L. (2001). Ontology development 101: A guide to creating your first ontology. http://liris.cnrs.fr/alain.mille/ enseignements/Ecole\_Centrale/What%20is%20 an%20ontology%20and%20why%20we%20ne ed%20it.htm

Oxforddictionaries.com. (2017). Definition of lexicon in English. Retrieved July 19, 2017, from https:// en.oxforddictionaries.com/definition/lexicon

Padmaja, S., & Fatima, S.S. (2013). Opinion mining and sentiment analysis-an assessment of peoples’ belief: A survey. International Journal of Ad hoc, Sensor & Ubiquitous Computing, 4(1), 21-33.

Pang, B., & Lee, L. (2008). Opinion mining and sentiment analysis. Foundations and Trends in Information Retrieval, 2(1-2), 1-135.

Park, E., Im, G., & Storey, V. C. (2012). Repurchase intentions of information technology: An emotion process perspective. In Proceedings of International Conference on Information Systems.

Park, E., Im, G., Storey, V. C., & Baskerville, R. L. (2019). Never, never together again: How postpurchase affect drives consumer outcomes within the context of online consumer support communities. Journal of the Association for Information Systems, 20(1), 1, 58-104.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77.

Polites, G. L., Serrano, C., Thatcher, J. B., & Matthews, K. (2018). Understanding social networking site (SNS) identity from a dual systems perspective: An investigation of the dark side of SNS use. European Journal of Information Systems, 27(5), 600-621.

Polpinij, J., & Ghose, A. K. (2008). An ontology-based sentiment classification methodology for online consumer reviews. Proceedings of Web Intelligence and Intelligent Agent Technology (pp. 518-524).

Pradhan, V. M., Vala, J., & Balani, P. (2016). A survey on sentiment analysis algorithms for opinion mining. International Journal of Computer Applications, 133(9), 7-11.

Qazi, A., Raj, R. G., Hardaker, G., & Standing, C. (2017). A systematic literature review on opinion types and sentiment analysis techniques: Tasks and challenges. Internet Research, 27(3), 608- 630.

Rana, T.A., & Cheah, Y. (2016). Aspect extraction in sentiment analysis: Comparative analysis and survey. Artificial Intelligence Review, 46(4), 459-483.

Ravi, K., & Ravi, V. (2015). A survey on opinion mining and sentiment analysis: Tasks, approaches and applications. Knowledge-Based Systems, 89, 14-46.

Redondo, J., Fraga, I., Padrón, I., & Comesaña, M. (2007). The Spanish adaptation of ANEW (affective norms for English words). Behavior Research Methods, 39(3), 600-605.

Ribeiro, F. N., Araújo, M., Gonçalves, P., Gonçalves, M. A., & Benevenuto, F. (2016). Sentibench: A

benchmark comparison of state-of-the-practice sentiment analysis methods. EPJ Data Science, 5(1), 1-29.

Ruppenhofer, J. (2006). MPQA annotation scheme details. http://mpqa.cs.pitt.edu/annotation/mpqa\_ scheme/

Russell, J. A. (1980). A circumplex model of affect. Journal of Personality and Social Psychology, 39(6), 1161-1178.

Russell, J. A. (2003). Core affect and the psychological construction of emotion. Psychological Review, 110(1), 145-172.

Russell, J. A. (2009). Emotion, core affect, and psychological construction. Cognition and Emotion, 23(7), 1259-1283.

Scherer, K. R. (2005). What are emotions? And how can they be measured? Social Science Information, 44(4), 695-729.

Schouten, K., & Frasincar, F. (2016). Survey on aspect-level sentiment analysis. IEEE Transactions on Knowledge and Data Engineering, 28(3), 813-830.

Stanford\_NLP\_Group. (2016). The Stanford parser: A statistical parser. https://nlp.stanford.edu/ software/lex-parser.shtml

Stauss, B., & Seidel, W. (2019). Human resource aspects of complaint management. Springer.

Stevenson, R. A., Mikels, J. A., & James, T. W. (2007). Characterization of the affective norms for English words by discrete emotional categories. Behavior Research Methods, 39(4), 1020-1024.

Stojanovic, L., Schneider, J., Maedche, A., Libischer, S., Studer, R., Lumpp, T., Abecker, A., Breiter, G., & Dinger, J. (2004). The role of ontologies in autonomic computing systems. IBM Systems Journal, 43(3), 598-616.

Storey, V. C., & O’Leary, D. E. (in press). Text analysis of evolving emotions and sentiments in COVID-19 Twitter communication. Cognitive Computation. https://doi.org/10.1007/s12559- 022-10025

Tabak, F. S., & Evrim, V. (2016). Comparison of emotion lexicons Proceedings of 13th International Symposium on Smart MicroGrids for Sustainable Energy Sources Enabled by Photonics and IoT Sensors (pp. 154-158).

Tsytsarau, M., & Palpanas, T. (2012). Survey on mining subjective data on the web. Data Mining and Knowledge Discovery, 24(3), 478-514.

Uschold, M., & King, M. (1995). Towards a methodology for building ontologies. Artificial Intelligence Applications Institute.

Valitutti, A., Strapparava, C., & Stock, O. (2004). Developing affective lexical resources. PsychNology Journal, 2(1), 61-83.

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). Feds: A framework for evaluation in design science research. European Journal of Information Systems, 25(1), 77-89.

Vinodhini, G., & Chandrasekaran, R. (2012). Sentiment analysis and opinion mining: A survey. International Journal, 2(6), 282-292.

Vrandečić, D. (2009). Ontology evaluation. S. Staab, R. Studer, eds. Handbook on ontologies. (pp. 293-313).

Wang, J., Tong, W., Yu, H., Li, M., Ma, X., Cai, H., Hanratty, T., & Han, J. (2015). Mining multiaspect reflection of news events in Twitter: Discovery, linking and presentation Proceedings of 2015 IEEE International Conference on Data Mining (pp. 429-438).

Wang, S., Lv, G., Mazumder, S., & Liu, B. (2020). Detecting domain polarity-changes of words in a sentiment lexicon. Available at https://arxiv.org/pdf/2004.14357.pdf

Wei, W., & Gulla, J.A. (2010). Sentiment learning on product reviews via sentiment ontology tree. Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics (pp. 404-413).

Welty, C., & Andersen, W. (2005). Towards Ontoclean 2.0: A framework for rigidity. Applied Ontology, 1(1), 107-116.

Whitelaw, C., Garg, N., & Argamon, S. (2005). Using appraisal groups for sentiment analysis. Proceedings of the 14th ACM International Conference on Information and Knowledge Management (pp. 625-631).

Wong, W., Liu, W., & Bennamoun, M. (2012). Ontology learning from text: A look back and into the future. ACM Computing Surveys, 44(4), Article 20.

Yadav, S. K. (2015). Sentiment analysis and classification: A survey. International Journal of Advance Research in Computer Science and Management Studies, 3(3), 113-121.

Yang, J., Yang, R., Wang, C., & Xie, J. (2018). Multientity aspect-based sentiment analysis with context, entity and aspect memory. Proceedings of the AAAI Conference on Artificial Intelligence.

Yi, M. Y., & Davis, F. D. (2003). Developing and validating an observational learning model of

computer software training and skill acquisition. Information Systems Research, 14(2), 146-169.

Zernik, U. (1991). Lexical acquisition: Exploiting on-line resources to build a lexicon. Lawrence Erlbaum.

Zhang, P. (2013). The affective response model: A theoretical framework of affective concepts and their relationships in the ICT context. MIS Quarterly, 37(1), 247-274.

Zhang, X., Hu, B., Chen, J., & Moore, P. (2013). Ontology-based context modeling for emotion recognition in an intelligent web. World Wide Web, 16(4), 497-513.

Zhou, L., & Chaovalit, P. (2008). Ontology-supported polarity mining. Journal of the American Society for Information Science and Technology, 59(1), 98-110.

Appendix A: Literature Review on Sentiment Analysis (SA) Surveys— Identified Challenges and Research Gaps

<table><tr><td>Survey paper</td><td># of articles</td><td>Objective of survey</td><td>Main focus of classification</td><td>Challenges and research gaps</td></tr><tr><td>Qazi et al., 2017</td><td>24</td><td>Various classification techniques</td><td>Research focus, data type, technique, accuracy, precision, and output</td><td>·Identify a correct set of keywords acceptable level of accuracy·Sentic computing to overcome the deficiency of keyword-based techniques.·Challenges: use of different types of opinions, complexity of sentences, emotion detection, sentiment orientation, strength of classification, presentation of opinion, development of common sense knowledge.</td></tr><tr><td>Clavel &amp; Callejas, 2016</td><td>22 (SA) &amp; 20 (HAI)</td><td>Mutual benefits of SA and HAI</td><td>Psychological, theoretical frameworks (dimensional, discrete, and appraisal approaches)</td><td>·Human-agent interaction (HAI) community: relies on psychological theories to model phenomenon; SA community does not.·SA community: tends not to provide in-depth definitions related to sentiment or affect, even use very different meanings.·Polarity detection (dimensional &amp; discrete approaches) is very frequent in SA community (positive vs. negative classification).</td></tr><tr><td>Hussein, 2016</td><td>47</td><td>SA challenges on approaches &amp; techniques</td><td>SA challenge, domain-oriented, review structure, technique used, and lexicon type</td><td>·Challenges: size of lexicon, bipolar, extracting features, natural language processing (NLP) overhead, negation, and domain dependence.</td></tr><tr><td>Korayem et al., 2016</td><td>25</td><td>Different methods for building SA systems for languages other than English</td><td>Methodology, pros and cons, classification types (machine learning, rule-based), corpus, SA analysis level, and lexical features</td><td>·Most SA systems and resources English-based·Need to build language-specific features.·High cost to develop resources for each language.·SA systems focus on the computation of polarity for words and sentences.</td></tr><tr><td>Pradhan et al., 2016</td><td>9</td><td>Various SA algorithms for mining</td><td>Supervised learning, dictionary-based algorithms, and accuracy level</td><td>·Most SA Algorithms aim for polarity detection.·Positive or negative sentiment words: can have opposite meanings in a particular domain.·Interrogative sentences may not have positive nor negative sentiment but keywords found in opinion may be positive or negative.·Sentences do not use sentiment words, e.g., good, better, best, worst, bad, etc. but sentences may have positive/negative feedback about products, services, and policies.</td></tr><tr><td>Rana &amp; Cheah, 2016</td><td>46</td><td>Various aspect extraction techniques and approaches</td><td>Un-/semi-supervised techniques, algorithms, domain, language, and aspect type</td><td>·Many studies extract explicit aspects, implicit aspects not studied rigorously.·Lack of studies for supervised learning approaches due to extensive efforts required to train dataset.·Need: a combination of approaches to produce higher recall and precision.</td></tr><tr><td>Schouten &amp; Frasincar, 2016)</td><td>45</td><td>Various methods for aspect detection and SA</td><td>Aspect detection method, domain, evaluation task, and performance</td><td>·Movement from traditional word-based approaches to semantically rich-concept, centric aspect-level (e.g., using ontology to improve aspect detection).·Concept-centric approach could be beneficial since semantic approaches naturally integratecommon sense, general world, and domain knowledge.</td></tr><tr><td>Kaur &amp; Duhan, 2015</td><td>17</td><td>Various techniques used for SA</td><td>Technique, language dependency, lexicon, tagged review, and dataset</td><td>SA: Polarity approach dominantIssues with respect to polarity: difficulty handling negation, domain dependency of words, slang.</td></tr><tr><td>Ravi &amp; Ravi, 2015</td><td>159</td><td>Various approaches, techniques, and applications</td><td>Technique, application, level of analysis, dataset, approach, accuracy, domain, language, and dictionary</td><td>Lack of study of irony and sarcasmComputational approaches needed based on appraisal theoryOntology-based studies promising to resolve scalability. Vagueness issues in SA.Machine learning combined with ontology needs researchCross-domain is a major challenge.Aspect level required for comparative visualization of similar products.Other issues: contextual SA, intrinsic feature-based SA</td></tr><tr><td>Yadav, 2015</td><td>18</td><td>Various techniques for document-level classification</td><td>Dataset, features, techniques &amp; classification approach</td><td>Polarity detection dominant approach.Challenges: discovering sentiment and polarity in complex sentences, identification of intrinsic aspect, cross-domain</td></tr><tr><td>Medhat et al., 2014</td><td>54</td><td>Various algorithms and applications</td><td>Task, domain-oriented, algorithm, polarity, dataset, and language</td><td>Lacking: benchmark datasets, studies with natural process tools, domain-specific studies, context-based studies</td></tr><tr><td>Nassirtoussi et al., 2014</td><td>26</td><td>Various text mining tools and approaches for market prediction</td><td>Text source, market index, forecast type, feature selection, dimensionality reduction, algorithm, and software</td><td>Needed: advanced techniques for semantics, ontology-based approaches with new/customized dictionaries (e.g., WordNet)Market-predictive sentiment investigationMachine learning techniques for market-predictive mining.</td></tr><tr><td>Padmaja &amp; Fatima, 2013</td><td>19</td><td>Various machine learning tools in SA</td><td>Machine learning algorithm, un/supervised, dataset and accuracy</td><td>Dominant approach: polarity detection.Ontology-based learning: needed for extracting opinion and sentiment from user-generated text.</td></tr><tr><td>Kumar &amp; Sebastian, 2012</td><td>36</td><td>Various approaches, tasks, and granularity levels</td><td>Granularity level, model, feature and data source</td><td>Polarity detection problem: when sentiment is delicately expressedIssues: domain-specific sentiment, multiple opinions in a sentence, negation handling, implicit opinion extraction, fake opinions.Machine learning techniques: promising but challenging.</td></tr><tr><td>Tsytsarau &amp; Palpanas, 2012</td><td>60</td><td>Various techniques and approaches</td><td>Topic, algorithm (precision), dataset, and scale</td><td>Dominant sentiment classification: polarity (binary or three-class of positive, negative, or neutral).Increasing demand for quality of sentiments: development of new methods based on machine learning and dictionary-based methods.</td></tr><tr><td>Vinodhini &amp; Chandrasekaran, 2012</td><td>22</td><td>Various techniques and methods</td><td>Technique, feature selection, data source, and accuracy</td><td>Many sentiment classifiers: domain or topic dependent.Challenges: subjectivity of sentiment expressions; cross-language; negation handling; extraction from complex sentences and documents.</td></tr></table>

Note: Prominent survey studies.

Appendix B. Comparison of Our Affect Lexicon to Other Lexicons

<table><tr><td>Our affect lexicon</td><td>MPQA subjectivity lexicon</td><td>Bing Liu&#x27;s sentiment lexicon</td></tr><tr><td>Affect—Admiration / awe categoryadmirableadmirablyadmirationadmiredadmiringlyadorabilityadorableadorablenessadorablyadorationadoreadoring...etc...Affect—Amusement categoryamuseamusedamusementamusingamusinglyanticbreak upcacklechortlechucklecomedycomiccomical...etc...Affect—Anger categoryamokanger (noun)anger (verb)angeredangrilyangrinessangryapoplecticballisticbedevilbegrudgeberserkbeset...etc...Affect—Anxiety categoryagitationagitationalarmalarmalertalertnessantsyanxietyanxien anxiousanxiousness...more affect categories &amp; relevant words...</td><td>abandonedabandonmentabandonabaseabasementabashabateabdicateaberration (adj)aberration (noun)abhorabhor (verb)abhorredabhorrenceabhorrentabhorrentlyabhors (adj)abhors (noun)abidance (adj)abidance (noun)abideabjectabjectlyabjureabilitiesabilityableabnormalabolishabominableabominablyabominateabominationaboveabove-averageaboundabradeabrasiveabruptabscondabsenceabsenteeabsent-mindedabsolveabsoluteabsolutelyabsorbedabsurdabsurdityabsurdlyabsurdnessabundantabundanceabuse (adj)abuse (noun)abuse (verb)abuses (adj)abuses (noun)...etc...</td><td>Positive wordsaboundaboundsabundanceabundantaccessibleaccessibleaccessibleacclaimacclaimedacclamationaccoladeaccoladesaccommodativeaccommodativeaccomplishaccomplishedaccomplishmentaccomplishmentsaccurateaccuratelyachievableachievementachievementsachievableacumenadaptableadaptiveadequate...etc...Negative wordsabnormalabolishabominableabominablyabominateabominationabortabortedabortsabradeabrasiveabruptabruptablyabscondabsenceabsent-mindedabsenteeabsurdabsurdityabsurdlyabsurdnessabuseabusedabusesabusiveabysmalabysmallyabyss...etc...</td></tr></table>

Appendix C. Comparison of Appraisal Lexicon to Whitelaw et al.’s (2005) Appraisal Group Lexicon

<table><tr><td>Our appraisal lexicon</td><td>Whitelaw et al.&#x27;s appraisal group lexicon</td></tr><tr><td>Appraisal—Pleasantness category</td><td>Attitude—Affect type</td></tr><tr><td>acclaimed</td><td>... gloomy</td></tr><tr><td>affirmative</td><td>happy</td></tr><tr><td>affluent</td><td>joyful</td></tr><tr><td>amazing</td><td>miserable</td></tr><tr><td>angelic</td><td>...etc...</td></tr><tr><td>appealing</td><td></td></tr><tr><td>approved</td><td>Attitude—Appreciation type</td></tr><tr><td>attractive</td><td>...</td></tr><tr><td>beaming</td><td>amazing</td></tr><tr><td>...etc...</td><td>awful</td></tr><tr><td>Appraisal—Goal obstructiveness category</td><td>beautiful</td></tr><tr><td>adverse</td><td>compelling</td></tr><tr><td>banned</td><td>consistent</td></tr><tr><td>betrap</td><td>convoluted</td></tr><tr><td>broke</td><td>derivative</td></tr><tr><td>broken</td><td>detailed</td></tr><tr><td>bug</td><td>discordant</td></tr><tr><td>buggy</td><td>dull</td></tr><tr><td>bump</td><td>elaborate</td></tr><tr><td>burned out</td><td>elegant</td></tr><tr><td>challenging</td><td>hideous</td></tr><tr><td>clash</td><td>inferior</td></tr><tr><td>clogged</td><td>innovative</td></tr><tr><td>collapsed</td><td>monotonous</td></tr><tr><td>collapses</td><td>profound</td></tr><tr><td>conflict</td><td>...etc...</td></tr><tr><td>corrupted</td><td>Attitude—Judgment—Social esteem type</td></tr><tr><td>corrupt</td><td>...</td></tr><tr><td>cracked</td><td>brave</td></tr><tr><td>crashed</td><td>clever</td></tr><tr><td>crashing</td><td>competent</td></tr><tr><td>damage</td><td>disloyal</td></tr><tr><td>damaged</td><td>eccentric</td></tr><tr><td>...etc...</td><td>faithful</td></tr><tr><td>Appraisal—Goal conduciveness category</td><td>famous</td></tr><tr><td>accommodating</td><td>foolhardy</td></tr><tr><td>accomplished</td><td>foolish</td></tr><tr><td>appropriate</td><td>immature</td></tr><tr><td>advanced</td><td>lucky</td></tr><tr><td>advantage</td><td>obscure</td></tr><tr><td>advantageous</td><td>popular</td></tr><tr><td>beneficial</td><td>...etc...</td></tr><tr><td>benefit</td><td>Attitude—Judgment—Social sanction type</td></tr><tr><td>clarify</td><td>...</td></tr><tr><td>cleared</td><td>callous</td></tr><tr><td>conducive</td><td>corrupt</td></tr><tr><td>convenient</td><td>devious</td></tr><tr><td>efficacious</td><td>generous</td></tr><tr><td>efficient</td><td>honest</td></tr><tr><td>enhanced</td><td>sincere</td></tr><tr><td>facilitative</td><td>sneaky</td></tr><tr><td>favorable</td><td>virtuous</td></tr><tr><td>...more appraisal categories &amp; relevant words...</td><td>...etc...</td></tr></table>

## Appendix D. Sample Scenarios Used in Experiment

Scenario: Sentiment analysis outcomes from the prototype with the ontology of emotion process

<table><tr><td rowspan="2" colspan="2">Original Review and Content</td><td colspan="2">Result from Sentiment Analysis System</td></tr><tr><td>Retrieved Words</td><td>Result - Features</td></tr><tr><td>Event:Customer&#x27;s Review</td><td>Product review on Kindle Fire HD 8</td><td>ReviewKindle Fire</td><td>Subject: ProductTopic: Kindle Fire</td></tr><tr><td rowspan="11">Review</td><td rowspan="11">So happy with my new fire and I wish I had bought more! Some of the PROS of this tablet are it has Alexa, Memory expansion slot, and a nice size.At 8 inches it is the perfect size to take on the go and ebook. It is a little thicker than some of the more expensive tablets on the market but because of this it seems more durable especially for kids. The apps and games seem to run smoothly and the colors are good on screen. I install the Google Play store and Connect to the google play store to download apps is easy, like Youtube.Overall, it is a good value for the price. This tablet can do whatever other tablets those cost twice or triple the price do.</td><td>Happy</td><td>Affect: HappinessAffect Score (5, 1)</td></tr><tr><td>Wish</td><td>Affect: LongingAffect Score (1, -3)</td></tr><tr><td>Nice</td><td>Affect: ContentmentAffect Score (4, -3)</td></tr><tr><td>PROS</td><td>Appraisal: PositiveGoal Constructive</td></tr><tr><td>expensive</td><td>Appraisal: NegativeGoal Obstructive</td></tr><tr><td>durable</td><td>Appraisal: PositiveGoal Constructive</td></tr><tr><td>Smoothly</td><td>Affect: RelaxationAffect Score (3, -3)</td></tr><tr><td>Good</td><td>Affect: ContentmentAffect Score (4, -3)</td></tr><tr><td>Easy</td><td>Affect: ContentmentAffect Score (4, -3)</td></tr><tr><td>good</td><td>Affect: ContentmentAffect Score (4, -3)</td></tr><tr><td colspan="2"></td></tr></table>

Scenario: Sentiment analysis outcomes from Semantria with polarity approach

<table><tr><td rowspan="2" colspan="2">Original post and comment</td><td colspan="2">Result from Sentiment Analysis System</td></tr><tr><td>Retrieved Words</td><td>Result - Features</td></tr><tr><td>Event:Customer&#x27;s Review</td><td>Product review on Kindle Fire HD 8</td><td>ReviewKindle Fire</td><td>Subject: ProductTopic: Kindle Fire</td></tr><tr><td rowspan="10">Review</td><td rowspan="10">So happy with my new fire and I wishI had bought more! Some of the PROS of this tablet are it has Alexa, Memory expansion slot, and a nice size.At 8 inches it is the perfect size to take on the go and ebook. It is a little thicker than some of the more expensive tablets on the market but because of this it seems more durable especially for kids. The apps and games seem to run smoothly and the colors are good on screen. I install the Google Play store and Connect to the google play store to download apps is easy, like Youtube.Overall, it is a good value for the price. This tablet can do whatever other tablets those cost twice or triple the price do.</td><td>Happy</td><td>Positive</td></tr><tr><td>Nice</td><td>Positive</td></tr><tr><td>Perfect</td><td>Neutral</td></tr><tr><td>Expensive</td><td>Neutral</td></tr><tr><td>Durable</td><td>Positive</td></tr><tr><td>Smoothly</td><td>Positive</td></tr><tr><td>Good</td><td>Neutral</td></tr><tr><td>Easy</td><td>Neutral</td></tr><tr><td>Good</td><td>Neutral</td></tr><tr><td colspan="2"></td></tr></table>

Appendix E: Constructs and Measurements

<table><tr><td>Construct</td><td>Measurement items (1 = strongly disagree to 11 = strongly agree)</td><td>Sources</td></tr><tr><td>Usefulness (reflective)</td><td>(UF1) The results from the Sentiment Analysis System enable me to evaluate the sentiment contained in this customer&#x27;s review quickly.(UF2) The results from the Sentiment Analysis System enhance my effectiveness when performing an evaluation of the text of this customer&#x27;s review.(UF3) Using the results from the Sentiment Analysis System would increase my productivity of analyzing the customer&#x27;s review.</td><td>Davis, 1989; Adams, et al., 1992</td></tr><tr><td>Helpfulness (reflective)</td><td>(HF1) The results from the Sentiment Analysis System are helpful in summarizing the customer&#x27;s sentiment.(HF2) The results of the Sentiment Analysis System help me to obtain a better understanding of the customer&#x27;s review.</td><td>Alavi, 1984; Mcknight et al., 2011</td></tr><tr><td>Deep analysis support (reflective)</td><td>(DS1) The results from the Sentiment Analysis System would help me carry out further analysis of the customer&#x27;s review.(DS2) The results from the Sentiment Analysis System would help me compare and contrast aspects of the analysis results that I could manually extract based upon my own common sense knowledge.(DS3) The results from the Sentiment Analysis System would help me derive an insightful conclusion from the text.</td><td>Burton-Jones &amp; Straub, 2006; Mcknight et al., 2011</td></tr></table>

## About the Authors

Veda C. Storey is the Tull Professor of Computer Information Systems and professor of computer science at the J. Mack Robinson College of Business, Georgia State University. Her research interests are in intelligent information systems, data management, conceptual modeling, and design science research. She is particularly interested in the assessment of the impact of new technologies on business and society from a data management perspective. Dr. Storey is a member of the steering committee of the International Conference of Conceptual Modelling and a member of the AIS Senior Scholars College. She is a recipient of the Peter P. Chen Award, an AIS Fellow, and an INFORMS Fellow.

Eun Hee Park is an associate professor of information technology & decision sciences at Old Dominion University. She received her PhD degree in CIS from Georgia State University. Her research interests include IT investment decisions, agile project management, IS security, social media, sentiment analysis, and emotion ontology. Her work has appeared in Journal of Management Information Systems, Information and Management, Information Systems Journal, Journal of the Association for Information Systems, Information Technology and People, Computers & Security, and Information Technology and Management, among other outlets.

Copyright © 2022 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
