---
otero_id: 27974
otero_key: "6TTGMQSY"
title: "Guided Diverse Concept Miner (GDCM): Uncovering Relevant Constructs for Managerial Insights from Text"
authors: "Dokyun “DK” Lee; Zhaoqi “ZQ” Cheng; Chengfeng Mao; Emaad Manzoor"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0494"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Guided Diverse Concept Miner (GDCM): Uncovering Relevant Constructs for Managerial Insights from Text

Dokyun “DK” Lee,<sup>a,</sup>\* Zhaoqi “ZQ” Cheng,<sup>a</sup> Chengfeng Mao,<sup>b</sup> Emaad Manzoor<sup>c</sup>

<sup>a</sup> Questrom School of Business, Boston University, Boston, Massachusetts 02215; <sup>b</sup> Marketing, Sloan School of Management, Massachusetts Institute of Technology, Cambridge, Massachusetts 02142; <sup>c</sup> Marketing, Samuel Curtis Johnson Graduate School of Management, Cornell University, Ithaca, New York 14853

\*Corresponding author

Contact: dokyun@bu.edu, https://orcid.org/0000-0002-3186-3349 (D“DK”L); chengzhaoqi@gmail.com, https://orcid.org/0000-0003-3295-0484 (Z“ZQ”C); maoc@mit.edu, https://orcid.org/0009-0002-6679-7764 (CM); emaadmanzoor@cornell.edu (EM)

Received: September 24, 2020 Revised: June 29, 2022; March 20, 2023; February 12, 2024 Accepted: March 16, 2024 Published Online in Articles in Advance: May 10, 2024

https://doi.org/10.1287/isre.2020.0494

Copyright: © 2024 INFORMS

Abstract. Guided Diverse Concept Miner (GDCM) is an interpretable deep learning algorithm to (1) automatically extract corpus-level concepts from text data, (2) focus the discovery of concepts to filter through only the concepts highly correlated to the userspecified managerial outcome, and (3) quantify the concept’s correlational importance to the outcome. GDCM is used to explore and potentially extract previously unknown concepts and insights from the text that may explain the managerial outcome, without the need to provide any human-predefined guidance or labeled data on concepts. GDCM embeds words, documents, and concepts all in the same vector space, enabling easy interpretation of discovered concepts by associating words local to the concept vector. GDCM is explicitly configured to increase recovered-concept diversity, coherence, and relevance to managerial outcomes. We demonstrate GDCM as a “guided exploratory” tool for a hypothetical managerial case involving online purchase journey data connected to consumed reviews. GDCM scalably extracts concepts hidden in customer reviews highly correlated to conversion and provides concept importance in comparison with product ratings. Concepts produced turn out to be product qualities previously theorized to impact conversion in the literature, and correlational importance gauged by GDCM closely matches estimates from a previous causal study run on a similar data set, serving as external validations of GDCM as a “guided exploratory” tool. Additional experiments with other data show that extracted insights are sensitive to guiding managerial variables and sensibly so, further demonstrating the flexibility of GDCM as a managerial tool.

History: Ahmed Abbasi, Senior Editor; Huimin Zhao, Associate Editor.

Funding: The authors acknowledge funding from the Marketing Science Institute [Grant 4000562] and Nvidia Academic Hardware Grant Program for research. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2020.0494.

Keywords: text • managerial insight extraction • guided exploration • concept extraction • deep learning • interpretable machine learnin

## 1. Introduction

Businesses increasingly rely on textual data analysis to inform strategic decisions. From customer reviews on e-commerce platforms informing product development to loan default prediction in finance, the utility of text data is becoming more pronounced (Feifer 2013, Wernicke 2015, Netzer et al. 2019, Toubia et al. 2019). However, the voluminous nature of textual data presents a significant cognitive challenge, necessitating the computational transformation of raw textual data into concepts comprehensible to managers and suitable for actionable insights. Consequently, these identified concepts must have a strong correlation with the relevant managerial outcome variables. Moreover, the diversity of these concepts is crucial for the discovery of unknown constructs, enhancing understanding and enabling the generation of innovative hypotheses for strategic decisions.

This paper proposes a novel text exploration algorithm,<sup>1</sup> Guided Diverse Concept Miner (GDCM), that hinges on three key requirements for uncovering relevant constructs for managerial insights: (1) interpretability, ensuring that extracted constructs and the outcome predictions are understandable to managers; (2) the capability to uncover a diverse array of concepts, potentially previously unknown, for enriched managerial insights; and (3) strong predictive capacity in relation to managerial outcome variables for relevance (Table 1).

To clearly define the goal of extracting insights from text, we identify concept as the target constructs grounded on theories of concepts. By definition, “concepts are the building blocks of thoughts” (Margolis and Laurence 2023, p. 1). Concepts constitute our knowledge and help us understand and act in the world (Murphy 2004). From managers seeking to identify customer needs from online reviews to researchers trying to develop new theories, they ultimately need concepts to formulate their thoughts. Driven by this need, we built GDCM, which was designed from the ground up to identify representations that qualify as concepts according to the definitions from theories of concepts.

Table 1. Algorithm Overview of the Guided Diverse Concept Miner

<table><tr><td></td><td>Description</td></tr><tr><td>Input</td><td>1. Structured X (e.g., numerical, categorical)2. Textual X (corpus)3. Managerial outcome variable Y linked to the corpus to guide concept extraction</td></tr><tr><td>Output</td><td>1. Corpus-level concepts potentially explaining managerial outcome2. Correlational relative importance of concepts against one another and X</td></tr><tr><td>Features</td><td>1. Easy interpretation of mined concepts and their coefficients2. Potential new previously unknown concept findings3. Diverse concepts relevant to Y4. Joint estimation of structured X and concepts that is end to end (in one pipeline)5. No need for predefined concepts nor human-tagged data</td></tr></table>

Figure 1 presents existing concept mining techniques and where GDCM belongs. Note that the categorization of these techniques is based on two contrasting goals:

(1) exploration versus extraction—whether the concept is a priori hypothesized or known—and (2) guided versus unguided—whether the process is guided by a specific managerial outcome.

For example, managers in e-commerce want to investigate the relationship between user-read review content and conversion. A manager with substantial experience may only seek to gauge the correlation between predetermined concepts (already known or hypothesized to influence conversion) and the conversion rates. In this case, techniques in Quadrant I (e.g., human tagging and optional machine learning (ML)- based scaling) in Figure 1 can be used. Alternatively, the manager may want to first scalably extract already known concepts for correlational analyses with other outcome variables not yet collected. Then, techniques in Quadrant IV (e.g., the seeded topic model (Jagarlamudi et al. 2012) or TopicGPT (Pham et al. 2023)) are useful. In Quadrants I and IV, interpretability is prioritized by extracting known concepts, which may not be the best predictors of the conversion. Conversely, managers entering a new domain or those seeking a broader understanding may first want to explore the salient concepts in reviews and thus, may prefer techniques in Quadrant III (e.g., topic models (Blei et al. 2003)). If they are specifically curious about review concepts highly correlated to particular managerial outcomes, such as conversion, return, or highly rated products, the “guided exploration” techniques in Quadrant II (e.g., the supervised topic model (Zhu et al. 2012)) may be used. Existing methods in Quadrant II, such as applying black-box deep learning models, prioritize prediction power over interpretability, whereas topic modeling variants do not explicitly optimize for the diversity and coherence of recovered concepts. Section 2.2 provides an overview of the mentioned concept extraction algorithms.

Figure 1. (Color online) Categorization of Existing Concept Mining Methods  
![](/api/attachments/6TTGMQSY/fulltext/images/8a3560bd3f98e387616e748d5cc3927d5ed12ebd3ad281abc2862c28beedde29.jpg)  
Note. LIME, local interpretable model-agnostic explanations (Ribeiro et al. 2016); SHAP, SHapley Additive exPlanation (Lundberg and Le 2017), respectively; ETM, embedded topic model (Dieng et al. 2020).

GDCM is an interpretable deep learning algorithm that falls within Quadrant II of text mining techniques. GDCM is designed to identify concepts that adhere to philosophical and cognitive science theories of concepts. These theories suggest that concepts should maximize information about the world with minimal cognitive effort (Rosch 2002). Four key criteria of concepts are identified from these theories and chosen as the underlying principle of GDCM.

1. Lexicalization. Lexicalization ensures that concepts can be expressed by language to enable knowledge accumulation and communication (Sloutsky and Deng 2019).

2. Conceptual coherence. Coherence demands that members within a concept should be similar so that it reduces cognitive effort and enhances pattern recognition (Goldstone and Son 2005).

3. Differentiation. Differentiation ensures that distinct concepts are easily distinguishable (Rosch 2002), reducing confusion and enhancing clarity in concept categorization.

4. Relevance. Concepts should provide maximum information for perceiving and predicting the real world (Solomon et al. 1999).

GDCM fulfills these criteria through custom architecture and training goals, as outlined in Section 3. A standout feature of GDCM among Quadrant II methods is its explicit focus on enhancing diversity. This not only ensures differentiation among concepts but also reduces redundancy across mined concepts, thereby elevating the informativeness of each concept (Murphy 2004). Distinct and diverse concepts increase the likelihood of new discoveries, a foundational step in scientific exploration as posited by the philosophy of science theorists, such as Kuhn (2012). GDCM excels in “guided exploration” by operationalizing the criteria of useful concepts discussed through these three desiderata:

1. Interpretability. This involves two aspects.

1. Space interpretability. GDCM achieves space interpretability by embedding words, concepts, and documents into a common multidimensiona space, where entities with similar semantic meaning are close to each other. This arrangement enables lexicalization as concepts are interpretable through adjacent words. Moreover, it ensures conceptual coherence by forming a connected region with each concept and concept member (words and documents) in the embedding space (Gardenfors 2004). This arrangement guarantees that each concept only consists of a concept prototype and concept members of similar meaning.

2. Prediction interpretability. In GDCM, prediction interpretability is achieved by an inherently interpretable linear model. The relationships between mined concepts and the managerial outcome variable can be accurately described by the weights assigned to these concepts in predicting the outcome (Murdoch et al. 2019).

2. Diversity. The model forces discovered concepts to be far from one another in the conceptual space, enabling differentiation among concepts and increasing potential recall of insightful candidate concepts. Note that this is possible only because of the space interpretability and vectorizing concepts.

3. Relevance. The mined concepts are focused on particular conceptual space subregions that are highly relevant to the managerial outcome variable.

Figure 2 and Table 2 visualize and discuss the three critical desiderata of GDCM—interpretability, diversity, and relevance. Each desideratum is essential; the absence of any one significantly diminishes the model’s effectiveness. Without interpretability, the predictive and diverse constructs would remain incomprehensible to managers and researchers. A lack of diversity leads to redundant discovery, potentially overlooking novel concepts. Absent relevance, the model might identify interesting patterns but fail to align with key managerial objectives. GDCM’s strength lies in its simultaneous optimization of these desiderata in one step, streamlining many steps worth of traditional text mining and processing. By achieving this balance, GDCM addresses the common critique of deep learning as an opaque “black box,” transforming it into a tool for insightful “guided exploration” in management.

Section 5 demonstrates the performance of GDCM in three criteria for good “guided exploration” in the context of exploring e-commerce reviews tied to conversion. Beyond human-subject and simulation-based benchmarks, we show that GDCM not only was able to extract out an already known construct in marketing theory (Garvin 1984) but also, provided an economic gauge of the extracted concept closely matching the results from a top-down theory-driven causal study (Liu et al. 2019) carried out on a similar data set in the same context.

Figure 2. (Color online) Stylized Illustration of Conceptual Spaces (of a User-Generated Review) with or Without the Desiderata  
![](/api/attachments/6TTGMQSY/fulltext/images/64a96f0845119d2b3c3b31e0ba2a3e9b2f2295dc53b3dd56e0b5d169cac498ee.jpg)  
Notes. (1) The white dots represent mined concept vectors. (2) The contours represent the ground truth correlation to managerial outcome. The correlation between a conceptual subregion space and the managerial outcome is directly proportional to the magnitude of its peak value. For instance, “money,” “poor,” “cheap,” and “price” may collectively represent the concept of price and value, whereas “space,” “clean,” and “design” may collectively represent the concept of aesthetics. (3) In the actual GDCM space, the colored areas represent the connected region around the concepts in the embedding space, encompassing only words that share the closest semantic meaning to each respective concept.

## 2. Related Literature

## 2.1. Philosophical Definition of the Concept

Concepts are the building blocks of insights. Their precise definition, however, has sparked extensive debate among philosophers, linguists, and psychologists (Jackendoff 1989). The classical theory of concepts requires strict definitions of criteria for the membership of every concept (Margolis et al. 1999), whereas the prototype theory posits that there exists a “prototype” that is an ideal or most representative example of a concept (Carey 2009). The members of a concept are the instances similar to the prototype. The prototype theory aligns better with modern cognitive science and provides a clear mathematical formulation for developing GDCM. A concept in the prototype theory can be described as a triplet, adapted from Osherson and Smith (1981): $( A , d , p )$ , where A represents a conceptual domain, encompassing all potential members of the concept. d measures the distance of each member in A to the concept prototype $p \in { \mathcal { A } } .$ . The closer an element is to the prototype p as measured by d, the more it exem plifies the concept.

In the context of GDCM, the conceptual domain A corresponds to the shared embedding space of concepts and words created by processing textual data. The distance metric d is operationalized through similarity measures in the embedding space, such as cosine similarity or dot product. Furthermore, the prototype p is represented by the concept embedding.

By operationalizing the prototype theory, GDCM aligns with the criteria of effective concept representation as described in Section 1. Lexicalization is achieved by representing the conceptual domain A with word embedding (Mikolov et al. 2013), rooted in distributional semantic theory (Harris 1954). This enables GDCM to group semantically similar words together. Combined with the distance metric d, the prototypes can be easily interpreted by the nearest words in the

Table 2. Desiderata of the Guided Exploratory Concept Mining Tool and Comparison Against Quadrant II Benchmarks

<table><tr><td>Desiderata</td><td>Interpretability</td><td>Diversity</td><td>Relevance</td></tr><tr><td>Relevant section</td><td>Section 5.1</td><td>Section 5.2</td><td>Section 5.3</td></tr><tr><td>Definition</td><td>1. Space interpretability.1.1. Lexicalization. Concepts must be represented by language for the accumulation of knowledge and communication.1.2. Conceptual coherence. Members within a concept should resemble one another.2. Prediction interpretability provides a human-understandable relationship between the mined concepts and managerial outcome.</td><td>The mined concepts are sufficiently different from one another, leading to high concept recallability.</td><td>The mined concepts are highly relevant to predicting the managerial outcome.</td></tr><tr><td>Related literature in theories of concepts</td><td>Lexicalization: Sloutsky and Deng (2019); conceptual coherence: Gardenfors (2004), Goldstone and Son (2005)</td><td>Rosch (2002)</td><td>Solomon et al. (1999)</td></tr><tr><td>Related literature in Computer Science</td><td>Chang et al. (2009), Lau et al. (2014), Guidotti et al. (2018), Murdoch et al. (2019), Schölkopf et al. (2021)</td><td>Airoldi and Bischof (2016), Dieng et al. (2020)</td><td>Mcauliffe and Blei (2008)</td></tr><tr><td>How GDCM achieves the desiderata</td><td>1.1. Lexicalization. By embedding words, concepts, and documents in a shared multidimensional space that preserves semantic similarity, concepts can be interpreted through the words with the closest semantic meaning.1.2. Conceptual coherence. By creating connected regions within the embedding space for each concept and its members, each concept only encompasses words with similar meanings.2. Prediction interpretability. GDCM predicts the outcome variable with a linear model of the concepts.</td><td>Customized objective function penalizes pairwise distances of concept vectors, encouraging the algorithms to explore different parts of conceptual space, thereby increasing the diversity of concepts. Consequently, recallability of unknown concepts is increased. Note that this is only possible because we have a vector representation of concepts and space interpretability.</td><td>Via customized objective function, GDCM penalizes the cross entropy between the supplied Y variable and the prediction made with concepts.</td></tr><tr><td>Does HSTM achieve the desiderata?</td><td>Partially. (1) Space interpretability. No, topics and words are not in the same space. (2) Prediction interpretability. Yes, prediction is made by a linear model.</td><td>Partially. Diversity may be implicitly modulated via Kullback-Leibler loss, but it is not explicit or controllable.</td><td>Yes. Heterogeneous supervised topic model (HSTM) reweighs the per-topic word affinity based on different values of y.</td></tr><tr><td>Does sDTM achieve the desiderata?</td><td>No. (1) Space interpretability. No, topics and words are not in the same space. (2) Prediction interpretability. No, prediction is made with a black-box deep learning algorithm.</td><td>Partially. δ in the shifted topic mixture is used to separate the attention weights of different topics, but this does not guarantee that the topics are semantically diverse.</td><td>Yes. The prediction loss is incorporated into the objective function of sDTM in an end-to-end fashion.</td></tr><tr><td>Does sLDA achieve the desiderata?</td><td>Partially. (1) Space interpretability. No, topics and words are not in the same space. (2) Prediction interpretability. Yes, prediction is made by a linear model.</td><td>No. It does not have explicit or controllable diversity regularization terms.</td><td>Yes. The Y variable is incorporated into the objective function.</td></tr></table>

embedding space. This combination also ensures that only words similar to a prototype p are associated with the corresponding concept, resulting in high conceptual coherence. Differentiation is achieved in GDCM by penalizing similarities between concept embeddings, ensuring that the prototypes are distant from each other within the conceptual domain A. Lastly, in the context of the prototype theory, relevance is about identifying the most pertinent groupings and prototypes within a conceptual domain that are instrumental in predicting managerial outcomes. Despite the multitude of ways to partition a conceptual domain into distinct concepts, GDCM focuses on those configurations that are most informative and predictive of the managerial outcome.

In summary, GDCM computationally implements the prototype theory for concept representation and categorization, making its models theoretically robust and practically useful. GDCM integrates concept prototypes (concept embedding) and concept members (word embedding) into a unified semantic space. This enhances interpretability and is augmented with loss functions for optimizing concept diversity (by penalizing similarities among concept embeddings) and relevance (by focusing on concepts that are informative for predicting the managerial outcome variable Y).

Topics in latent Dirichlet allocation (LDA) (Blei et al. 2003) or its variants (Mcauliffe and Blei 2008, Zhu et al. 2012, Srivastava and Sutton 2017, Sridhar et al. 2022, Yang et al. 2023) can be loosely interpreted as prototypes, but they are not in the same conceptual space as the concept members, contradicting the prototype theory’s definition that the concept prototype p and concept members belong to the same conceptual domain A. This limitation hinders the space interpretability of these models. Improvements have been made to embed topic and words in the same space (Liu et al. 2015, Moody 2016, Shi et al. 2017, Xun et al. 2017, Dieng et al. 2020), but these models lack a clearly defined distance metric d between words and topics. Although the probability of word occurrence in a topic might implicitly suggest d, the absence of explicit metrics limits these models’ ability to optimize for identifying diverse concepts across topics.

## 2.2. Algorithms for Finding Topics or Concepts in Business

Business have increasingly adopted natural language processing methods to extract meaningful concepts related to brand perception, market trends, or adverse events from social media corpus (Netzer et al. 2012; Abbasi et al. 2018, 2019; Lee et al. 2018; Zhang and Moe 2021) and consumer-generated product review data (Archak et al. 2011, Chen et al. 2019, Choi et al. 2019, Liu et al. 2019, Ransbotham et al. 2019). Traditional concept extraction methods, as shown in Quadrant I of Figure 1, involve human-defined and tagged content, which can be costly and is limited by existing domain knowledge, potentially introducing bias. For situations where the Y variable is not available but general concepts to extract are known (Quadrant IV in Figure 1), methods like seeded LDA (Jagarlamudi et al. 2012) and a ChatGPTbased approach (Pham et al. 2023) facilitate the discovery of topics related to user-provided seed words.

However, similar to the methods in Quadrant I, this reli ance on existing knowledge inherently limits the scope of discovery.

Topic modeling algorithms (see Vayansky and Kumar 2020 for a review) are popular choices for auto mating concept exploration (Quadrant III in Figure 1). The pioneering work, latent Dirichlet allocation, mod els topics as probability distributions over words and documents as distributions over these topics (Blei et al. 2003). Enhancements, like ProdLDA (Srivastava and Sutton 2017), adopt autoencoding variational Bayes, thereby improving topic coherence and computational efficiency. Recent developments further merge topic modeling with word embedding to refine topic quality (Liu et al. 2015, Moody 2016, Shi et al. 2017, Xun et al. 2017, Dieng et al. 2020). These models are effective as proxies for concept discovery. However, the topics they identify often lack essential desiderata of well defined concepts. This results in issues such as intrusion (one topic containing many concepts and being ambiguous) (Chang et al. 2009) and diffusion (same concepts appearing in multiple topics). Despite efforts to enhance semantic coherence in topic models, as explored in papers such as Mimno and McCallum (2008), these issues persist. To tackle these challenges, we have established and operationalized criteria for concept discovery based on theories of concepts. For instance, the conceptual coherence criterion aims to mitigate intrusion by ensuring that each concept consists of similar words, whereas the differentiation criterion addresses diffusion by maintaining clear distinctions among different concepts.

Recent extensions of LDA for guided exploration (Quadrant II in Figure 1) incorporate the outcome variable Y to inform concept exploration, such as supervised versions of LDA (Mcauliffe and Blei 2008, Zhu et al. 2012, Roberts et al. 2014). Back Propagation supervised LDA (BP-sLDA) (Chen et al. 2015) uses a deep feed-forward network tailored for supervised LDA. More recent variational autoencoder (VAE)-based topic models, such as Chai and Li (2019), Attention Neural Topic Model (Attention NTM) (Wang and Yang 2020), HSTM (Sridhar et al. 2022), and sDTM (Yang et al. 2023), employ neural networks to simulate the datagenerating process of the textual data, in which the topic representation and labels are derived and predicted from the latent variables via variational inference. More recently, a growing body of literature explores the uses of large language models (LLMs) to extract thematic structures from textual data; refer to Appendix A for a detailed discussion.

Although these models represent a notable advancement over traditional LDA, they continue to face chal lenges similar to those in Quadrant III approaches. Notably, they also lack a foundation in theories of concepts and fail to align with the essential desiderata of well-defined concepts. Therefore, we design GDCM to explicitly align with the desiderata of exploratory concept mining to fill the gap of guided exploration methods in Quadrant II. A detailed comparison between GDCM and these methods is presented in Table 2.

## 2.3. Interpretable Machine Learning

High-performing black-box algorithms, like deep neural networks (LeCun et al. 2015) and boosted trees (Chen and Guestrin 2016), give little rationale for their predictions. This poses challenges in intelligence systems, where auditability, liability, privacy, and other high-stakes issues are entangled, as understanding why algorithms made certain predictions is critical to prevent egregious failures, justify their usage, improve efficiency, and use them for decision making.

In response to the need for solutions that tackle both interpretability and predictive capacity simultaneously, several substreams of research have arisen since the mid-2010s (see Guidotti et al. 2018 for surveys). The explainable artificial intelligence (XAI) literature broadly defines (Rudin 2019) two different algorithm families for interpretability:

2.3.1. Explainable Machine Learning (Model Wise). The algorithm takes as an input a black box B and a data set $D = \{ X , Y \}$ , and it returns a transparent predictor T with requirements that (1) T replicates the prediction of B with high fidelity and that (2) T offers a humanunderstandable rationale for each prediction either at the instance level or at the model-average level. T may be a shallow tree, a small set of rules, etc.

2.3.2. Interpretable Machine Learning (Outcome Wise). These inherently transparent algorithms provide a human-understandable rationale for predictions yet still offer competitive performances compared with prediction-focused black-box algorithms.

Despite the growth of the XAI literature, the definition of “interpretability” remains elusive, fragmented, and varies across domains (Rudin 2019). Miller (2018) defines it as “the degree to which a human can understand the cause of a decision,” whereas Dhurandhar et al. (2017) states that artificial intelligence “is interpretable to the extent that the produced interpretation I can maximize a user’s target performance.” Lipton (2018) and Guidotti et al. (2018) conclude that there is no single agreed-upon definition of interpretability.

A few papers also tackle desiderata for interpretability conceptually, such as unambiguity (inputs and outputs are clear), selectiveness (a parsimonious explanation), contrastiveness (a “had input been x, output would have been y” type of explanation), factative (has to be highly truthful), etc. (Lipton 2018, Miller 2018, Lu et al. 2019).

In this paper, we carefully design an interpretable machine learning algorithm in the task of “guided exploration” such that it (1) increases human-centered understanding of the corpus and (2) offers competitive performances against black-box algorithms. GDCM’s features, such as promoting diversity, increase the potential extraction of highly relevant concepts. This both (1) enables a better interpretation of the managerial outcome and (2) promotes hypothesis development.

We measure the “interpretability” by (1) tapping into existing interpretability measurements in topic modeling called coherence and (2) confirming the coherence measure with human judgment directly from the Mechanical Turk (MTurk).

## 3. Empirical Challenges of Guided Exploration

Section 3.1 starts with an example of a “guided exploration” managerial task using the user reviews and conversion from an online retailer as if the manager has no idea about what constructs/concepts in customer reviews may be correlated to conversion. Section 3.2 outlines the major challenges for managers in extracting candidate concepts from the text data.

## 3.1. Data Context

Our data come from an online retailer in the United Kingdom through a top review platform company. They track 243,000 consumers via anonymous unique identifiers over two months in February and March of 2015 in the electronics category and the home and garden category, including 41 different subcategories. The data set encompasses a range of consumer activity data, such as clickstream, page view, and transactions. It also records consumers’ review-reading behaviors that are essential for GDCM, including (1) when a user clicks on review pages, (2) whether each review has appeared on a user’s browser, and (3) for how long the content was viewed on the user’s browser measured accurately down to milliseconds.

With this data set, we construct a “decision-making journey” that characterizes how a user purchases or abandons a particular product. In such a journey, a user will first visit the product page to read the description, then reads reviews of the product, and finally, decides whether to buy the product or not. Accord ingly, our data set is at the “decision-making journey” or the UserID-ProductID level. A data sample contains (1) the product review texts read by the user, (2) the explanatory variables shown to matter in predicting the purchase conversion in the business literature (e.g., product price and review star ratings), and (3) a binary label indicating conversion. Next, we discuss selection criteria and data construction. Online Appendix B.1 details the descriptive statistics and assumptions in constructing the journey data.

## 3.2. Desiderata of the Guided Exploratory Concept Mining Tool for Textual Insights

Our method, GDCM, focuses on “guided exploration” in text mining, aiming to discover concepts relevant to managerial outcomes without prior knowledge. Managers can utilize data, like consumer conversion rates (Y), auxiliary data (X), and product reviews, to identify concepts correlating with conversion, aiding in areas such as review platform and product design as well as market research.

As discussed in Sections 1 and 2.2, the extant guided exploration approaches (e.g., HSTM, sDTM, and sLDA) partially achieve the goal of guided exploration, but they miss key features, notably diversity regularization. This omission leads to topic overlap and could leave out important factors affecting the managerial outcome. Effective guided exploration requires identifying a diverse range of interpretable concepts relevant to managerial outcomes. Note that we can only directly optimize for diversity but not recall as the latter presupposes that the specific concepts to be identified are known a priori.

Figure 3 reports the words describing topics generated by extant models used for guided exploration. Take LDA (Figure 3(a)), and note the following observations. First, within a given topic, many different concepts appear; this is because of word intrusion (Chang et al. 2009) or the lack of conceptual coherence. For example, Topic 1 has concepts related to product names (e.g., phone, iron), fea tures (e.g., feature), and aesthetics (e.g., design, old). Second, single concepts appear across many different topics; we call this lack of differentiation. Many words related to singular concepts, such as aesthetics, product name, or features, appear in most, if not all, of the five topics. Presented with such outputs, it is unclear how managers may then utilize recovered topics as X for further insight. The manager may need to validate the results of the topic model using external sources or methods to ensure that they are accurate and reliable. Other benchmarks also exhibit these issues to varying extents.

Figure 3. (Color online) Describing Words Extracted by GDCM and Select Benchmark Models

<table><tr><td colspan="2">(a)</td></tr><tr><td colspan="2">LDA 1: phone iron lamp find feature steam replace old design</td></tr><tr><td colspan="2">LDA 2: sound picture old brilliant battery son feature problem smart fantastic</td></tr><tr><td colspan="2">LDA 3: kettle clean microwave quick size toaster design heat brilliant quickly</td></tr><tr><td colspan="2">LDA 4: assemble sturdy room curtain space size hold bin perfect design</td></tr><tr><td colspan="2">LDA 5: bed comfortable cover lovely pillow duvet floor mattress feel thin</td></tr><tr><td colspan="2">(b)</td></tr><tr><td colspan="2">HSTM 1: soundbar netflix lg freeview phone bt samsung hitachi bbc television</td></tr><tr><td colspan="2">HSTM 2: boil sandwich breville toastie jug grill taste hobbs boiling cook</td></tr><tr><td colspan="2">HSTM 3: hoover suction cleaner carpet vax hair vacuum bagless cylinder vacuum</td></tr><tr><td colspan="2">HSTM 4: cartridge ink printing epson printer scanner hp print canon inkjet</td></tr><tr><td colspan="2">HSTM 5: curtain blackout eyelet curtains finial shade lagoon pole fabric decorate</td></tr><tr><td colspan="2">(c)</td></tr><tr><td colspan="2">sDTM 1: look quality fit assemble nice money price lovely sturdy room</td></tr><tr><td colspan="2">sDTM 2: use great excellent work easy little purchase recommend phone old</td></tr><tr><td colspan="2">sDTM 3: good great use price excellent kettle sound buy phone recommend</td></tr><tr><td colspan="2">sDTM 4: good use easy great buy recommend need quality like money</td></tr><tr><td colspan="2">sDTM 5: use clean time work carpet vacuum suction hoover floor cleaner</td></tr><tr><td colspan="2">(d)</td></tr><tr><td colspan="2">sLDA 1: great money quality easy use recommend price pleased look size</td></tr><tr><td colspan="2">sLDA 2: easy look use excellent quality design small work money item</td></tr><tr><td colspan="2">sLDA 3: buy great price use recommend love find excellent purchase need</td></tr><tr><td colspan="2">sLDA 4: look easy buy use nice fit excellent price assemble money</td></tr><tr><td colspan="2">sLDA 5: great use easy work price quality buy excellent kettle sound</td></tr><tr><td colspan="2">(e)</td></tr><tr><td colspan="2">CM 1 (Aesthetics): small nice space little use design clean size love look</td></tr><tr><td colspan="2">CM 2 (Price &amp; Value): money quality cheap poor instruction price fine ok overall work</td></tr><tr><td colspan="2">CM 3 (Features): come item easily perfect long expect fit feel job bit</td></tr><tr><td colspan="2">CM 4 (Conformance): happy excellent definitely pleased far purchase need recommend worth</td></tr><tr><td colspan="2">CM 5 (Serviceability): problem work lovely room day replace return job use far</td></tr></table>

Notes. For select benchmarks, LDA is the most widely used model for unguided topic exploration. HSTM, sDTM, and sLDA are neural network for guided topic exploration. For LDA, average coherence is �2.25. Similar concepts are color coded by human experts for visualization. For GDCM, average coherence is �1.86. For HSTM, average coherence is �3.32. For sDTM, average coherence is �1.45. We show the highest coher ence outputs for each algorithm, (a) LDA. (b) HSTM. (c) sDTM. (d) sLDA. (e) GDCM.

## 4. Model

This section describes the major components of GDCM and the rationale for the design choice.

## 4.1. Overview of the Guided Diverse Concept Miner

GDCM is composed of three key components: (1) the concept allocator network (CAN), a fully connected neural network that infers the concept probability for each document; (2) an embedding network that embeds words, documents, and concepts into a common vector space; and (3) a classifier that predicts the managerial outcome variable based on the concept probabilities, resulting in the following loss function:

$$
\begin{array}{l} \mathcal {L} (\mathrm{pvt}, \mathrm{ctx}, d, y) = \underbrace {\mathcal {L} _ {\text { neg }} (\mathrm{pvt} , \mathrm{ctx})} _ {\text { Embedding }} + \underbrace {\mathcal {L} _ {\text { spr }} (d) + \mathcal {L} _ {\text { div }}} _ {\text { Concept   Regularization }} \\ \qquad + \underbrace {\mathcal {L} _ {\text { clf }} (d , y)} _ {\text { Classification }}. \end{array}\tag{1}
$$

The definition of each term will be discussed in the subsequent sections. For brevity, we highlight the models for concept presentation (Section 4.1.2) and embedding (Section 4.1.1), the regularization terms that facilitate concept sparsity (Section 4.1.3), concept diversity (Section 4.1.4), and relevance to target outcomes (Section 4.1.5). Refer to Online Appendix A for the training procedure and implementation details. Notation is summarized in Table 3 for the reader’s convenience.

4.1.1. Embedding Words in the Semantic Space. GDCM operationalizes the prototype theory discussed in Section 2.1 by representing the conceptual domain A as a shared semantic space, where $\mathcal { A } \subseteq \mathbb { R } ^ { E }$ is a real-valued embedding space of dimension E. Through processing textual data, each word is mapped to a vector in this space, $v _ { \mathrm { p i v o t } } \in { \mathcal { A } } ,$ , preserving semantic-similarity relationships. The structure of A is based on the distributional hypothesis, which posits that words in similar contexts have related meanings. The goal is for each word vector $v _ { \mathrm { p i v o t } }$ to be positioned such that semantically similar words are proximate. Mathematically, the embedding model aims to represent each central word by its embedding, $v _ { \mathrm { p i v o t } } .$ . Many well-known embedding models use the skip-gram negative sampling algorithm (Mikolov et al. 2013) to obtain word embeddings via sampling of pivot-context word pairs, which seeks to

minimize

$$
\begin{array}{c} \mathcal {L} _ {\text {neg}} = - \sum_ {(\text {pvt}, \text {ctx}) \in \mathcal {D}} \log (\sigma (\boldsymbol {v} _ {\text {ctx}} \cdot \boldsymbol {v} _ {\text {pvt}})) \\ - \sum_ {(\text {pvt}, \text {ctx}) \in \mathcal {D} ^ {\prime}} \log (\sigma (- \boldsymbol {v} _ {\text {ctx}} \cdot \boldsymbol {v} _ {\text {pvt}})), \end{array}\tag{2}
$$

where D and $\mathcal { D } ^ { \prime }$ indicate word pairs (pivot, context) (henceforth, (pvt, ctx)) that occur in the corpus (pvt, ctx) $\in \mathcal { D }$ or do not occur in the corpus $( \mathrm { p v t , c t x } ) \in \mathcal { D } ^ { \prime } , v _ { \mathrm { p v t } }$ and $v _ { \mathrm { c t x } }$ are the word embedding for the pivot and con text words, and σ is the logistic sigmoid function.

4.1.2. Representing Concepts and Documents. GDCM extends traditional word embedding models by also incorporating “concept embeddings” within the same semantic space. Each basic concept in the corpus is represented as a vector in this embedding space. These concept vectors are analogous to the concept prototypes p in the prototype theory.

The prototype theory suggests that concepts are not rigidly defined but instead, are best represented by typical or “prototypical” instances. Similarly, in GDCM, each basic concept’s vector (or concept embedding) can be seen as a prototype for that concept. It encapsulates the central, most representative features of the concept, much like a prototype in the prototype theory encapsulates the most typical attributes of a category.

These concept embeddings are not fixed but are learnable parameters. They are stored in a matrix $\mathbf { E } _ { c }$ which has dimensions $C \times E ,$ where C represents the number of distinct concepts in the corpus and E is the size of the embedding space. Just as a word’s embed ding captures its semantic essence in the embedding space, a concept’s embedding captures the core semantic meaning of that concept, serving as a prototype in the conceptual space defined by A.

Building upon the conceptual space formulated, GDCM adopts a containment model view for representing documents (Gardenfors 2004). In this model, a document is perceived as a composite concept, constituted by basic concepts. The basic concepts correspond to the concept prototypes, operationalized as concept embeddings E<sub>c</sub>. This perspective allows for a structured and interpretive representation of documents in the conceptual domain. Each document is represented as an embedding, v , derived as a weighted linear combination of the concept embeddings:

Table 3. Notation

<table><tr><td>Notation</td><td>Dimensions</td><td>Notation</td><td>Learned parameters</td><td>Notation</td><td>Loss weights</td></tr><tr><td>D</td><td>Number of documents</td><td> $\mathbf{E}_{\mathrm{c}}$ </td><td>Concept embedding matrix ( $C \times E$ )</td><td> $\lambda$ </td><td>Sparsity regularizer strength</td></tr><tr><td>C</td><td>Number of concepts</td><td> $\mathbf{W}$ </td><td>Document-concept weights ( $D \times C$ )</td><td> $\eta$ </td><td>Diversity regularizer strength</td></tr><tr><td>E</td><td>Embedding size</td><td> $\boldsymbol{\theta}$ </td><td>Concept-classification weights ( $1 \times C$ )</td><td> $\rho$ </td><td>Classification loss (relevance) strength</td></tr></table>

$$
\pmb {v} _ {d} = \mathbf {E} _ {c} ^ {\top} \pmb {p} _ {d},\tag{3}
$$

where $p _ { d }$ is the document-concept probability distribution inferred by the CAN using a bag-of-words representation of documents. The CAN, parameterized as a fully connected neural network, infers $p _ { d }$ from both documents in the training data and unseen documents, facilitating inductive learning. This design enables the model to be adaptable and implementable with various architectures (see Online Appendix A.3 for implementation details).

To ensure that the concept and document embeddings lie in the same space as the word embeddings, we extend the original word embedding model to represent words and concepts by combining ideas from Mikolov et al. (2013) and Moody (2016). Specifically, to ensure that word embedding $v _ { w }$ and document embedding $v _ { d }$ are in the same vector space, we connect the two embeddings by injecting both into the skip-gram negative sampling loss function:

$$
\begin{array}{l} \mathcal {L} _ {\text {neg}} = - \sum_ {(\mathrm{pvt}, \mathrm{ctx}) \in \mathcal {D}} \log (\sigma (v _ {\mathrm{ctx}} \cdot v _ {\mathrm{pvt}} + v _ {\mathrm{ctx}} \cdot v _ {d})) \\ \qquad - \sum_ {(\mathrm{pvt}, \mathrm{ctx}) \in \mathcal {D} ^ {\prime}} \log (\sigma (- v _ {\mathrm{ctx}} \cdot v _ {\mathrm{pvt}} - v _ {\mathrm{ctx}} \cdot v _ {d})), \end{array}\tag{4}
$$

where $d \in { 1 , \dots , D }$ is the index of the document containing pivot and context. Minimizing this loss now enables us to learn both $v _ { \mathrm { p v t } }$ and $v _ { d }$ from the training corpus.

4.1.3. Encourage Concept Sparsity. In GDCM, we expect each document to predominantly exhibit a limited set of concepts, whereas others remain minimal or absent, similar to the sparsity regularizer in LDA or Lasso (Tibshirani 1996). Promoting sparsity by focusing on a few key features can lead to better prediction interpretability (Murdoch et al. 2019). To ensure that the loss functions are differentiable, we adopt the Gaussian entropy function (Huang and Tran 2018) as the diversity regularizer given by

$$
\mathcal {L} _ {\mathrm{spr}} = \lambda \sum_ {d = 1} ^ {D} \sum_ {c = 1} ^ {C} \log (\boldsymbol {p} _ {d} [ c ]),\tag{5}
$$

where $\lambda$ is a hyperparameter that controls the strength of the sparsity. Intuitively, this regularization term penalizes the document-concept distributions for having too many nonzero probability values, effectively encouraging sparsity on the document-concept distribution.

4.1.4. Encourage Concept Diversity. Encouraging concept diversity directly ties to the principle of differentiation. Differentiation ensures that mined concepts are easily distinguishable, a critical aspect in overcoming the common challenges of overlap found in LDA-like topic modeling. In many instances, LDA-derived topics tend to overlap, particularly when a few concepts dominate the corpus. This overlapping can obscure less prevalent but equally important concepts.

To address this and enhance concept diversity, GDCM introduces a diversity regularizer that encourages dissimilarity between every pair of concept embeddings, $\mathbf E _ { \mathbf c } [ i ]$ and $\mathbf E _ { \mathbf c } [ j ] .$ , in terms of their dot product. This is for mulated as the following extension to the loss function:

$$
\mathcal {L} _ {\mathrm{div}} = \eta \sum_ {i = 1} ^ {C} \sum_ {j > i} ^ {C} \log \sigma (\mathbf {E _ {c}} [ i ] \cdot \mathbf {E _ {c}} [ j ]),\tag{6}
$$

where $\eta$ is a hyperparameter that controls the strength of the prior and the log σ or log-sigmoid transformation ensures that this term and its gradient lie on the same scale as the other terms in the loss function. In essence, this regularization can be seen as a method for identifying diverse concept prototypes within the text data that are also aligned with the relevant managerial outcomes (denoted by Y).

4.1.5. Uncovering Concepts Guided by Managerial Outcomes. In practice, the concepts embodied by documents may fall into several different descriptive modes. For example, the set of concepts “furniture,” “technology,” and “kitchen” describes the category of the product being sold, whereas the set of concepts “aesthetics,” “functionality,” and “reliability” describes characteristics of the product being sold; both of these descriptive modes may exist simultaneously in the corpus, and our goal is to uncover the one that best explains the given managerial outcome Y (e.g., conversion) associated with each document.

Hence, we introduce a loss component that “guides” the concepts toward explaining these outcomes. We assume that the target outcomes are binary, $y _ { d } \in \{ 0 , 1 \}$ $\forall d = 1 , \ldots , D$ . We introduce a parameter vector $\pmb { \theta } \in \mathbb { R } ^ { T }$ that assigns an explanation weight to each concept and that is shared across all documents. Given the explanation weights and the document-concept distribution ${ \pmb p } _ { d } ,$ define $\widehat { y _ { d } }$ for a document d as a weighted combination of its concept probabilities:

$$
\widehat {y _ {d}} = \pmb {\theta} \cdot \pmb {p} _ {d}.\tag{7}
$$

Given the observed outcome $y _ { d } ,$ we would like $\widehat { y _ { d } }$ to be large if y � 1 and small if $y = 0$ . This requirement is captured by the following cross entropy loss term that we append to the overall loss function weighted by hyperparameter $\rho \colon$

$$
\mathcal {L} _ {\mathrm{clf}} = \rho (y _ {d} \log \sigma (\hat {y} _ {d}) + (1 - y _ {d}) \log (1 - \sigma (\hat {y} _ {d})).\tag{8}
$$

Note that we could also add any user-specified X in Equation (7). This (1) increases prediction power and (2) allows managers to compare the correlational relative importance of mined concepts with key referential X (e.g., price and product ratings).

## 4.2. Summary: Theories of Concepts Within GDCM Operationalization

Table 4 summarizes the relationship between GDCM’s loss functions and its key operational desiderata: interpretability, diversity, and relevance. This table illustrates how GDCM’s technical aspects are aligned with its objectives in facilitating guided exploration in text mining for managerial outcomes.

4.2.1. Embedding for Space Interpretability. According to the prototype theory, a concept definition contains three main components: A, the conceptual domain that contains all possible objects to be categorized as concepts; the prototype p that characterizes the core semantics of a concept; and the distance metric d that characterizes the semantic similarity between semantic elements (e.g., words) and concepts cores. The closer an element is to the prototype p, the more characteristic it is as a member of the concept defined by p ∈ A. GDCM aligns with this framework by leveraging word embedding techniques to ensure that similar words are near each other. By designing a space where the concepts are vectorized to occupy the same space as words and documents, we ensure both lexicalization and conceptual coherence. This is achieved because similar words, documents, and concepts reside near each other, and therefore, we can lexicalize the concept and understand the concept by sampling the nearest word vectors.

4.2.2. Encouraging the Dissimilarity of Concept Embeddings for Diversity. The ability to penalize the pairwise distance among recovered concepts is made possible by having a vectorized form of concepts. This is unique to GDCM, and other competitor methods in Quadrant II lack it. This approach is designed to achieve maximum compression for high information quality while adhering to minimal mental processing. Furthermore, this diversity regularization is akin to the objective of contrastive learning, which seeks to increase the distance between different concepts.

4.2.3. Classification Loss for Concept Relevance. GDCM integrates an additional classification loss for a guided exploration of concepts as inductive biases. This classification loss is specifically tailored to ensure the concept relevant to business outcomes and steer the learned representation toward achieving the objectives of desiderata of guided exploration in business contexts.

The intuition of how all parts of GDCM work together to uncover relevant constructs is sketched here. Note that if we knew the concepts to be discovered a priori, we would directly be optimizing for higher recall, but we do not in “guided exploration.” Instead of recall, we explicitly optimize for diversity. In conjunction with end-to-end joint optimization of concepts and X variables working with the constraint on concept relevance to the managerial outcome, the diversity constraint then seeks to increase recall as well. Relevance constraint defines the hypotheses space for GDCM to maximize diversity and in turn, increases the recallability of relevant concepts.

## 5. Evaluating Mined Concept Quality

Table 5 lists the experiments conducted to evaluate GDCM’s performance of guided concept exploration in terms of interpretability, diversity, and relevance.

## 5.1. Space Interpretability

Like other guided exploration tools, GDCM can produce words that best describe each of the concepts uncovered from the corpus. The desiderata of interpretability require that these words are more semantically coherent within each concept. Concepts are both well focused within (not intruded) as well as separated from one another (not diffused).

We benchmark GDCM on its ability to extract interpretable concepts that may be insightful through human judgment (Section 5.1.1) and the algorithmic measure (Section 5.1.2).

Table 4. Connecting GDCM Loss Functions to Operational Desiderata

<table><tr><td colspan="4">GDCM loss functions and operational desiderata</td></tr><tr><td>Loss function</td><td>Interpretability</td><td>Diversity</td><td>Relevance</td></tr><tr><td> $\mathcal{L}_{neg}$  (embedding loss)</td><td>Concepts are close to semantically similar words for space interpretability</td><td>—</td><td>—</td></tr><tr><td> $\mathcal{L}_{spr}$  (sparsity loss)</td><td>Sparse document-concept assignment for prediction interpretability</td><td>—</td><td>—</td></tr><tr><td> $\mathcal{L}_{div}$  (diversity loss)</td><td>—</td><td>Promotes concept differentiation</td><td>—</td></tr><tr><td> $\mathcal{L}_{clf}$  (classification loss)</td><td>Linear model for prediction interpretability</td><td>—</td><td>Aids outcome prediction</td></tr></table>

Table 5. Overview of Experiments to Evaluate Mined Concept Quality

<table><tr><td>Experiments</td><td>Desiderata to evaluate</td><td>Section</td><td>Main figures and tables</td></tr><tr><td>Human judgement on concept quality via MTurk</td><td>Space interpretability, diversity</td><td>5.1.1, 5.2.1</td><td>Figure 4</td></tr><tr><td>Coherence score</td><td>Space interpretability</td><td>5.1.2</td><td>Figure 3, Table 10</td></tr><tr><td>Recallability of Garvin concepts</td><td>Diversity</td><td>5.2.2</td><td>Table 8</td></tr><tr><td>Recallability of unknown concept</td><td>Diversity</td><td>5.2.3, Online Appendix B.5</td><td>Figure 9</td></tr><tr><td>Predicting managerial outcome</td><td>Relevance</td><td>5.3.1</td><td>Figure 7, Table 10</td></tr><tr><td>Correlation of concept importance</td><td>Relevance, prediction interpretability</td><td>5.3.2</td><td>Figure 8</td></tr><tr><td>Impact of guiding variable</td><td>Relevance</td><td>5.3.3</td><td>Online Appendix C.2</td></tr><tr><td>Ablation study</td><td>Relevance, space interpretability</td><td>5.3.3</td><td>Figure 9</td></tr></table>

Notes. Online Appendix B.5 provide details of the experiments on higher relative recallability of unknown concepts. Online Appendix C.2 investigates the impact of the managerial variable Y on guiding GDCM output.

5.1.1. Interpretability Comparison Based on Human Judgement. We conduct a survey using Amazon Mechanical Turk (Online Appendix B.2) to evaluate the interpretability of GDCM and various topic modeling algorithms in Quadrant II of Figure 1. In this survey, MTurkers are presented with five themes identified from an online review. Each theme is represented by 10 concept/topic words generated by the algorithms. To evaluate these themes, we employ Garvin’s wellestablished dimensions of product price and quality (as detailed in Table 6), which are known to significantly impact consumer purchase decisions (Garvin 1984). Garvin’s dimensions serve as an effective and validated “ground truth” for this experiment, providing a structured framework for assessing the relevance and clarity of the themes identified by the algorithms. MTurkers are provided with descriptions of Garvin’s dimensions during the survey, ensuring informed selections, and attention checks are used to verify their comprehension of these dimensions. The core task for MTurkers involves selecting the Garvin dimension that most aptly aligns with each theme. For each theme, the interpretability is evaluated based on the coherence and the lack of ambiguity in the concepts identified by the MTurkers.

Coherence and interpretability are higher when MTurkers largely agree on fewer distinct Garvin’s dimensions for each theme. To measure this, we first calculate the proportion $p _ { i j }$ of MTurkers who classify the theme i as Garvin’s dimension $j .$ These proportions together form a vector $\mathbf { g _ { i } } = \{ p _ { i 1 } , p _ { i 2 } , \dots , p _ { i M } \}$ for each theme $i ,$ where $M = 7$ is the total number of Garvin dimensions. The Gini coefficient is then computed for each vector $\mathbf { g _ { i } }$ to quantify the consensus. A higher Gini coefficient indicates a more pronounced agreement among MTurkers about the most relevant Garvin’s dimension for each theme, signifying a theme’s strong association with a distinct and interpretable high-level concept.

For the survey, we engaged 100 MTurkers who had previously completed at least 100 tasks with a 98% or greater accuracy rate. To ensure data quality, we embedded attention questions and filtered results to prevent bot participation. The presentation of themes was ran domized to avoid order bias.

The results of this survey are depicted in Figure 4. The Gini coefficients calculated from the MTurkers selections provide a numerical basis for comparing the interpretability of GDCM and different topic modeling algorithms. GDCM exhibits the highest Gini coefficient, implying a higher degree of consensus among MTurkers about the dominant concept in a topic and indicating clearer and more interpretable topic summaries.

5.1.2. Interpretability Comparison Based on Coherence. As a robustness check, we adopt the coherence score, an algorithmic measure defined by Mimno and

Table 6. Literature-Defined Key Dimensions of Price and Quality

<table><tr><td>Dimension</td><td>Description</td></tr><tr><td>Aesthetics</td><td>The review talks about how a product looks, feels, sounds, tastes, or smells</td></tr><tr><td>Conformance</td><td>The review compares the performance of the product with pre-existing standards or set expectations</td></tr><tr><td>Durability</td><td>The review describes the experience with durability, product malfunctions, or failure to work</td></tr><tr><td>Feature and performance</td><td>The review talks about the presence or absence of product features</td></tr><tr><td>Brand</td><td>The review talks about indirect measures of the quality of the product, such as the reputation of the brand</td></tr><tr><td>Price</td><td>The review contains content regarding the price of the product</td></tr><tr><td>Serviceability</td><td>The speed, courtesy, competence, and ease of repair in case of any defects with the product</td></tr></table>

Figure 4. (Color online) Human-Judged Interpretability Measured by Gini Coefficients (Quadrant II Methods)  
![](/api/attachments/6TTGMQSY/fulltext/images/923e6a0e183052e9132b723e9aaa2191a11d6557c16b48fe9e9044f9f197677b.jpg)  
Notes. Interpretability was judged by MTurkers matching the themes to Garvin’s dimensions. Higher Gini coefficients signify stronger consensus among MTurkers in classifying each theme to the most related Garvin’s dimension. GDCM achieved the highest Gini coefficient, indicating clearer, more interpretable themes. The means and standard errors are calculated from bootstrap resampling (Efron and Tibshirani 1997).

McCallum (2008) to measure how well focused the group of top topic keywords is in describing a singular concept. A higher topic coherence means that the keywords within one topic dimension are more coherent with one another in concept. However, this measure does not account for other aspects, like topic diversity or alignment between the concepts and the managerial outcome of interests. See Appendix B for details on the definition of the coherence measure.

GDCM obtains an average coherence of �1.86, which is greater (indicating higher coherence leading to better interpretability) than the �2.25 obtained by LDA. Among the five concepts, the aesthetics concept represented by words such as “nice, little, big, clean, look, design” achieved the highest coherence of �1.38. Even for the concept of serviceability, which has the lowest coherence score of �2.20, the words are semantically coherent. Based on 50 runs, the LDA coherence range lies in (�3:5, �2:25), whereas the GDCM range lies in (�1:92, �1:68). The ranges do not overlap, and they are statistically significantly different, indicating that GDCM excels in extracting coherent (and thus, more human-interpretable) concepts from review texts.

Recent benchmarks, however, have shown different coherence scores. HSTM reports a coherence with a mean of �4.89 (range: �8.27 to �2.67), suggesting lower coherence. In contrast, sDTM and sLDA achieve higher coherence scores, with sDTM having a mean of �0.6543 (range: �1.00 to �0.62) and sLDA having a mean of �0.92 (range: �1.11 to �0.81). Although these scores are higher, it is essential to note that the topic words discovered by sDTM and sLDA tend to be repetitive. This repetition might artificially inflate their coherence scores. Later, in Section 5.1.1, we discuss how the topics from these benchmarks cannot be consistently interpreted as high-level concepts, such as Garvin’s dimensions, in contrast to the more varied and meaning ful topics extracted by GDCM.

The concepts recovered by GDCM closely coincide with the dimensions of product price and quality that are shown in the literature to influence consumer purchase. Garvin (1984, 1987) compiled and introduced a set of quality and price dimensions aimed at helping organizations think about products, as shown in Table 6. On multiple GDCM runs, we were able to automatically extract most concepts compiled by Garvin (1984, 1987). This serves as evidence of the external validity of GDCM.

## 5.2. Diversity

Experiments show that GDCM discovers a higher number of unique concepts compared with benchmarks.

5.2.1. Diversity and Recallability of Known Concepts Based on Human Judgement. We evaluate the diver sity and recallability with the same MTurk survey as in Section 5.1.1. The goal is to gauge how well the discovered concepts/topics align with the conceptual categories that are intuitive to human cognition and relevant to managerial decisions.

To measure the diversity of themes in terms of Garvin’s dimensions, we compute the vector $\mathbf { g _ { i } }$ for each theme i by calculating the proportions of MTurkers classifying theme i to each of the Garvin’s dimension. Then, we calculate the average pairwise cosine distance between the vectors $\mathbf { g _ { i } }$ and $\mathbf { g } _ { \mathrm { i } }$ for all pairs of different theme i and theme j. To calculate the number of distinct recalled Garvin’s dimensions, for each $\mathbf { g _ { i } } = \{ g _ { i 1 } , g _ { i 2 } , . . . ,$ $g _ { i M } \}$ , we first find the most frequently selected Garvin’s dimension: $\mathbf { d } _ { i } = \arg \operatorname* { m a x } _ { j } g _ { i j }$ : Then, we count the number of unique top Garvin’s dimensions across all k themes: $\{ \mathrm { d } _ { 1 } , \mathrm { d } _ { 2 } , \dots , \mathrm { d } _ { k } \} |$ | . The results of the diversity and recallability based on Garvin’s dimensions are displayed in Figure 5. GDCM clearly identifies themes that contain more distinct Garvin’s dimensions and also, recover more unique Garvin’s dimensions. Figure 6 further demonstrates that GDCM extracts the most interpretable concepts and recalls the highest number of Garvin’s dimensions, robust to different criteria of selecting benchmark topics.

5.2.2. Recallability of Known Concepts Based on the Overlap with Garvin’s Dimension Words. We run an empirical experiment to compare the concept recallability of GDCM against Quadrant II methods and other topic modeling methods on the main data set using Garvin’s dimensions as the “ground truth”

Figure 5. (Color online) Diversity and Recallability of Known Concepts Based on Human Judgement  
(a)  
![](/api/attachments/6TTGMQSY/fulltext/images/9e573d393a077be8a2001e29d1a1d7cb1732ae07c11ddf53a243375bfdfef473.jpg)

(b)  
![](/api/attachments/6TTGMQSY/fulltext/images/54e12be2f756852c5c4ca06af55146990aede0abaac48479a4de10ad63ea839c.jpg)  
Notes. Diversity and recallability are assessed by MTurkers matching themes to Garvin’s dimensions. Diversity was quantified by average pairwise cosine distances between vectors of Garvin’s dimensions classifications for each theme. Recallability was measured by the count of uniqu top Garvin’s dimensions across themes. GDCM identifies more distinct themes and recovers a higher number of unique Garvin’s dimensions, indicating better alignment with human cognition and managerial relevance. (a) Average pairwise cosine distance for measuring concept/topi diversity. (b) Number of recalled Garvin’s dimensions.

concepts. Garvin’s concepts, C(D) :� {Aesthetics, Brand, Conformance, Features, Serviceability, Value}, are operationalized by manually assigning a set of 10 concept words to each of Garvin’s concept. The concept words are chosen by two experts such that the selected set of words (1) must be semantically relevant to Garvin’s concept and (2) must attain high-term frequencies from data. Table 7 lists our operationalized concept words based on Garvin’s theory. Our results are robust to different operationalizations.

Figure 6. (Color online) Interpretability and Recallability of Known Concepts Based on Human Judgement  
![](/api/attachments/6TTGMQSY/fulltext/images/60a40bb519f9cd7a804ed96067144befacf9fd995f0111afc1f4a6b32580ec97.jpg)  
Notes. Interpretability is measured by Gini coefficients as in Figure 4, and recallability is measured by the number of recalled unique Garvin’s dimensions as in Figure 5. GDCM outperforms the bench marks in both measurements, demonstrating better interpretability and recallability in concept discovery.

We represent k concepts/topics produced by each method by a set of its top 10 words (e.g., highest topicword probability for topic modeling algorithms and lowest concept-word distance for GDCM) as follows:

$$
\begin{array}{l} \hat {\mathcal {W}} ^ {(m)} = \{\hat {W} _ {1} ^ {(m)}, \hat {W} _ {2} ^ {(m)}, \ldots , \hat {W} _ {k} ^ {(m)} \}, \text {where} \\ \hat {W} _ {i} ^ {(m)} = \{\hat {w} _ {i 1} ^ {(m)}, \hat {w} _ {i 2} ^ {(m)}, \ldots , \hat {w} _ {i 1 0} ^ {(m)} \} \text {for} i = 1, 2, \ldots , k. \end{array}\tag{9}
$$

Then, we say that method m successfully discovers a Garvin concept if m has a set of extracted words $\hat { W } _ { i } ^ { ( m ) }$ that have enough overlapping words (greater than $h _ { o v e r l a p } )$ with the operationalized words of the focal Garvin concept. Consequently, we define recallability as the total number of Garvin’s concepts recovered by method m.

Table 8 shows the number of concepts discovered by models with different $h _ { o v e r l a p }$ configurations. Runs refer to algorithm repetition with different initializations. With just 5 runs, GDCM recovers more “ground truth” concepts than benchmark methods can in 50 or even 150 runs. The result is robust to different initializations of Garvin’s concept words. GDCM’s recallability of known concepts is superior to benchmarks.

5.2.3. Recallability of Unknown Concepts. As a robust ness check, we also test GDCM’s relative recallability of unknown concepts assuming that the true concepts are unknown a priori. Specifically, we take all the machinerecovered concepts—as opposed to Garvin’s concepts— as the ground truth, and we show that GDCM achieves higher relative recallability (coverage rate) in discovering unknown concepts. Methods and results of relative recallability of unknown concepts are reported in Online Appendix B.5.

Table 7. Operationalized Concept Words for Garvin’s Concepts

<table><tr><td>Concept</td><td>Operationalized words</td></tr><tr><td>Aesthetics</td><td>bright, clean, design, gorgeous, look, lovely, nice, pretty, simple, stylish</td></tr><tr><td>Conformance</td><td>decent, different, disappointed, excellent, expect, faulty, feature, refund, use, work</td></tr><tr><td>Feature</td><td>assemble, compact, fit, function, handy, lightweight, mount, powerful, strong, versatile</td></tr><tr><td>Brand</td><td>dyson, htc, ipad, iphone, lg, microsoft, samsung, sony, windows, xbox</td></tr><tr><td>Price (value)</td><td>bargain, cheap, expensive, fit, inexpensive, money, price, purchase, reasonable, worst</td></tr><tr><td>Serviceability</td><td>break, durable, flimsy, poor, problem, quality, size, solid, strong, sturdy</td></tr></table>

## 5.3. Relevance

Experiments show that the concepts produced by GDCM correlate highly with the managerial outcome.

5.3.1. Predictive Performance. User-specified variable Y provides users with the filtering ability to retain only the concepts that are relevant to their interested outcome. When Y is supplied to guide concept mining, we can also calculate the prediction performances to see if GDCM passes the sanity check of achieving acceptable predictive performance. Using the main data set, GDCM takes X and the read reviews as inputs to predict a purchase/abandon (y).

We compare GDCM’s predictive performance against two sets of baseline models—interpretable models versus uninterpretable prediction-focused models as listed in Table 9. We show the Receiver Operating Characteristics (ROC) curves in Figure $7 , ^ { 3 }$ and test set accuracy, precision, recall, F1 score, and Area Under the ROC Curve (AUC) in Table 10.

Figure 7, left panel presents the ROCs and the AUC values for the GDCM (in blue), seven interpretable baselines (in red), and three prediction-focused baselines (in black). First, note that all interpretable models (in red)

Table 8. The Number of Garvin Concepts Discovered

<table><tr><td>Method</td><td> $h_{\text{overlap}} = 3$ </td><td> $h_{\text{overlap}} = 4$ </td><td> $h_{\text{overlap}} = 5$ </td></tr><tr><td>LDA (total runs = 50)</td><td>1</td><td>1</td><td>0</td></tr><tr><td>LDA (total runs = 150)</td><td>3</td><td>2</td><td>0</td></tr><tr><td>HSTM (total runs = 50)</td><td>3</td><td>1</td><td>0</td></tr><tr><td>HSTM (total runs = 150)</td><td>3</td><td>1</td><td>0</td></tr><tr><td>sDTM (total runs = 50)</td><td>3</td><td>1</td><td>0</td></tr><tr><td>sDTM (total runs = 150)</td><td>4</td><td>1</td><td>1</td></tr><tr><td>sLDA (total runs = 50)</td><td>3</td><td>2</td><td>0</td></tr><tr><td>sLDA (total runs = 150)</td><td>3</td><td>3</td><td>1</td></tr><tr><td>ETM (total runs = 50)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>ETM (total runs = 150)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>ProdLDA (total runs = 50)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>ProdLDA (total runs = 150)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>GDCM (total runs = 5)</td><td>5</td><td>5</td><td>4</td></tr></table>

fall significantly behind GDCM (in blue). Although there are two uninterpretable algorithms (in black) that surpass GDCM, the difference is rather small at less than 0.03 in AUC. We also provide ROC and AUC after replacing the logistic regression with XGB for topic model-based approaches in Figure 7, right panel. Note that performance increases (yet still falls behind GDCM) at the cost of interpretability because XGBoost does not provide coefficients like logistic regression.

The top two performing algorithms are, unsurprisingly, deep learning and XGB. CNN with GLoVe embedding achieves the highest AUC at 0.9186, with XGB performing nearly the same at 0.9184. GDCM follows closely at 0.8885 followed by sDTM (0.8181), a vari ational autoencoder-based topic model with a recurrent neural network as the prediction module. Given that we could also boost (reduce bias) and bootstrap aggregate (reduce variance) GDCM predictions, albeit at a higher computational cost, GDCM performance is competitive with cutting-edge prediction-focused methods. We can also turn GDCM into an uninterpretable predictionfocused model by making the classification hyperparameter ρ arbitrarily high while setting interpretability-related parameters (λ, η) to zero. Contrastingly, GDCM performs significantly better than the traditional bag-of words approach (0.7773), the basic sentiment analysis (0.6093), and all topic model variants plus XGB.

Among the interpretable competitors, the best is the SeededLDA (0.8087). Our seed words were driven by Garvin’s theory of consumer purchase behavior. With this prior domain knowledge to facilitate the data representation, it is unsurprising that SeededLDA excels over a naive bag-of-words approach. However, SeededLDA still falls short of GDCM, suggesting that GDCM extracts residual signals above and beyond theory-driven concepts. Note that the SeededLDA approach can be useful when managers are equipped with domain knowledge but not feasible for exploratory concept extraction, and therefore, it is not a competitor of GDCM. Other interpretable models, such as HSTM (0.7541), vanilla LDA (0.6086), supervised LDA (0.6041), structural topic mod els (0.6015), and BERTopic (0.6480), all perform worse than GDCM, even with good parameter tuning effort.

GDCM excels in predictive performance over all interpretable baselines while staying competitive with the top uninterpretable prediction-focused algorithms.

Table 9. Baseline Models to Compare GDCM’s Predictive Performance

<table><tr><td>Baseline</td><td>Literature</td><td>Comment</td></tr><tr><td colspan="3">Interpretable benchmarks</td></tr><tr><td>LDA + LR</td><td>Blei et al. (2003)</td><td>Plain LDA + logistic regression classifier. Plain LDA is the most widely used topic model, and logistic regression (LR) makes this combination easy to interpret.</td></tr><tr><td>Sentiment</td><td>Jurafsky (2000)</td><td>Classification based on review-level sentiment score.</td></tr><tr><td>sLDA + LR</td><td>Mcauliffe and Blei (2008)</td><td>Supervised LDA + logistic regression classifier. Supervision by Y could potentially improve the topic&#x27;s interpretability.</td></tr><tr><td>STM + LR</td><td>Roberts et al. (2014)</td><td>Structural topic model incorporates both X and natively handles Y.</td></tr><tr><td>SeededLDA + LR</td><td>Jagarlamudi et al. (2012)</td><td>SeededLDA + logistic regression classifier. We seed the topics based on dimensions of price and quality as defined in the literature to maximize their performance. These topics should perform better because they are better at capturing the data-generating process (of people reading the content that matters). Note that this is not a viable competitor to GDCM as it requires human-defined concepts based on prior domain knowledge.</td></tr><tr><td>BERTopic + LR</td><td>Grootendorst (2022)</td><td>A popular transformer-based unguided topic model.</td></tr><tr><td>ETM + LR</td><td>Dieng et al. (2020)</td><td>A topic model that models each word with a categorical distribution whose parameter is the inner product between the word&#x27;s embedding and an embedding of its assigned topic.</td></tr><tr><td>ProdLDA + LR</td><td>Srivastava and Sutton (2017)</td><td>A VAE-based topic model that models each word with the weighted product of experts model.</td></tr><tr><td>HSTM</td><td>Sridhar et al. (2022)</td><td>A recent VAE-based topic model that captures the variability in the relationship between text and outcomes across different latent topics.</td></tr><tr><td colspan="3">Uninterpretable models</td></tr><tr><td>BOW + LR</td><td>Jurafsky (2000)</td><td>Bag-of-words (BOW) approach + logistic regression classifier.</td></tr><tr><td>CNN</td><td>Pennington et al. (2014)</td><td>Convolutional neural networks (CNN) with GLoVe (Global Vectors for Word Representation) embedding as the first layer.</td></tr><tr><td>XGB</td><td>Chen and Guestrin (2016)</td><td>eXtreme gradient boosting use an ensemble of decision trees for prediction. It is often known to achieve the best predictive performance in a wide variety of ML competitions off the shelf. We also add topic models + XGB, which improves predictive power at the cost of interpretability for additional comparison.</td></tr><tr><td>BP-sLDA</td><td>Chen et al. (2015)</td><td>The prediction network in these types of models is based on black-box algorithms, and thus, it lacks the interpretability to provide the relative importance of topics.</td></tr><tr><td>Attention NTM</td><td>Wang and Yang (2020)</td><td>Another state-of-the-art supervised neural topics model.</td></tr><tr><td>sDTM</td><td>Yang et al. (2023)</td><td>A neural topic model that combines a neural variational autoencoder model and a recurrent neural network.</td></tr></table>

Notes. Interpretable benchmarks include concept mining models that give correlational importance to interpretable concepts. Uninterpretabl benchmarks include (1) concept mining models that do not give correlational importance and (2) prediction-focused models that do not give interpretable concepts. STM, structural topic model; LR, logistic regression classifier; ETM, embedded topic model (Dieng et al. 2020); BOW, bag of-words; NTM, neural topic model (Wang and Yang 2020).

5.3.2. Importance of Concepts for Predicting Managerial Outcome. To better utilize the extracted concepts, GDCM provides correlational importance of mined concepts against the user-input X. The idea is to supply GDCM with relatively well-understood X (e.g., price) along with texts to compare the correlational impact on the Y. In the last layer, GDCM predicts the conversion (Equation (10)) of a journey with the mined documentconcept distribution, $p _ { d } .$ We modify this prediction layer to include user-specified X. We rename $p _ { d }$ as Doc-ConceptD for clarity and add the explanatory variables ExpVar with a sigmoid function:

$$
\begin{array}{l} \widehat {\text { Conversion }} \\ = \sigma \left(\theta_ {0} + \sum_ {i} \theta_ {i} \text { DocConcept } D _ {i} + \sum_ {j} \theta_ {j} \text { ExpVar } _ {j}\right), \end{array}\tag{10}
$$

where DocConceptD is a probability vector of different concepts that sum up to one. For this exposition, concepts are named according to Figure 3(e). The coefficients here speak to the impact of concept volume present in the review documents, and the trained weights, h, characterize how much the predicted conversion will respond to the change in X. Although the sigmoid layer of GDCM follows the formula of a generalized linear regression, we are not aware of any work that could provide the confi dence interval of a deep learning-based model. Thus, we do not provide the confidence interval.

Figure 8 shows the coefficients. We standardized the average rating for easier interpretation. The results pass the sanity check: a negative coefficient for price and a high positive coefficient on average ratings. Aesthetic concepts had the highest positive correlation with conversion, whereas the serviceability and return-related concepts had the lowest. Calculating the average correlation

Table 10. Prediction Performance Against Competing Methods

<table><tr><td>Method</td><td>Coherence</td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1 score</td><td>AUC</td></tr><tr><td>GDCM</td><td>-1.86</td><td>0.8228</td><td>0.8346</td><td>0.8475</td><td>0.8410</td><td>0.8885</td></tr><tr><td colspan="7">Interpretable benchmarks</td></tr><tr><td>LDA + LR</td><td>-2.25</td><td>0.5653</td><td>0.5624</td><td>0.9630</td><td>0.7101</td><td>0.6086</td></tr><tr><td>Sentiment</td><td>N/A</td><td>0.5804</td><td>0.5896</td><td>0.7925</td><td>0.6762</td><td>0.6093</td></tr><tr><td>sLDA + LR</td><td>-2.17</td><td>0.5857</td><td>0.6163</td><td>0.6641</td><td>0.6393</td><td>0.6041</td></tr><tr><td>STM + LR</td><td>-5.13</td><td>0.5872</td><td>0.5977</td><td>0.7745</td><td>0.6747</td><td>0.6015</td></tr><tr><td>SeededLDA + LR</td><td>-1.95</td><td>0.7490</td><td>0.7945</td><td>0.7365</td><td>0.7644</td><td>0.8087</td></tr><tr><td>ETM + LR</td><td>-1.50</td><td>0.5812</td><td>0.5792</td><td>0.8865</td><td>0.7006</td><td>0.6142</td></tr><tr><td>ProdLDA + LR</td><td>-5.40</td><td>0.6156</td><td>0.6108</td><td>0.8392</td><td>0.7071</td><td>0.6557</td></tr><tr><td>HSTM</td><td>-3.32</td><td>0.6993</td><td>0.7040</td><td>0.7869</td><td>0.7431</td><td>0.7541</td></tr><tr><td>BERTopic + LR</td><td>-3.65</td><td>0.6116</td><td>0.6126</td><td>0.8089</td><td>0.6972</td><td>0.6480</td></tr><tr><td colspan="7">Uninterpretable benchmarks</td></tr><tr><td>BOW + LR</td><td>N/A</td><td>0.7212</td><td>0.7231</td><td>0.8033</td><td>0.7611</td><td>0.7773</td></tr><tr><td>CNN with GloVe</td><td>N/A</td><td>0.8421</td><td>0.8307</td><td>0.8973</td><td>0.8627</td><td>0.9186</td></tr><tr><td>XGB</td><td>N/A</td><td>0.8475</td><td>0.8525</td><td>0.8757</td><td>0.8639</td><td>0.9184</td></tr><tr><td>BP-sLDA</td><td>-12.44</td><td>0.6547</td><td>0.6665</td><td>0.7514</td><td>0.7064</td><td>0.7096</td></tr><tr><td>Attention NTM</td><td>-2.15</td><td>0.7469</td><td>0.7325</td><td>0.6836</td><td>0.7072</td><td>0.8138</td></tr><tr><td>LDA + XGB</td><td>-2.25</td><td>0.5684</td><td>0.5623</td><td>0.9902</td><td>0.7173</td><td>0.7058</td></tr><tr><td>sDTM</td><td>-1.45</td><td>0.7445</td><td>0.7976</td><td>0.7235</td><td>0.7571</td><td>0.8181</td></tr><tr><td>ETM + XGB</td><td>-1.50</td><td>0.7005</td><td>0.7138</td><td>0.7648</td><td>0.7384</td><td>0.7767</td></tr><tr><td>ProdLDA + XGB</td><td>-5.40</td><td>0.6851</td><td>0.6931</td><td>0.7725</td><td>0.7306</td><td>0.7516</td></tr><tr><td>sLDA + XGB</td><td>-2.17</td><td>0.5892</td><td>0.5740</td><td>0.9964</td><td>0.7284</td><td>0.7119</td></tr><tr><td>STM + XGB</td><td>-5.13</td><td>0.6539</td><td>0.6637</td><td>0.7581</td><td>0.7077</td><td>0.7038</td></tr><tr><td>SeededLDA + XGB</td><td>-1.95</td><td>0.7408</td><td>0.7274</td><td>0.8495</td><td>0.7837</td><td>0.8223</td></tr><tr><td>BERTopic + XGB</td><td>-3.65</td><td>0.6777</td><td>0.6913</td><td>0.7535</td><td>0.7211</td><td>0.7466</td></tr></table>

Note. N/A, not applicable; STM, structural topic model; LR, logistic regression classifier; ETM, embedded topic model (Dieng et al. 2020); BOW, bag-of-words; NTM, neural topic model (Wang and Yang 2020).

across each journey shows that a 10% concept increase is associated with a �20% to 15% change in predicted conversion probability. Given the GDCM results, a manager may then launch a more focused causal study to investigate how to prioritize certain concepts and information in customer reviews.

Figure 7. (Color online) Receiver Operating Characteristics Curve (ROC) of GDCM vs. Baselines  
![](/api/attachments/6TTGMQSY/fulltext/images/fd10d9f835961f6b4efc584ad6d58ac6be69c743678173f87f07a84d988c6725.jpg)

![](/api/attachments/6TTGMQSY/fulltext/images/585b3f36e4573426b68ffc0ecddb1da48dbecade25cc8c192c70a2c6b99074f0.jpg)  
Notes. The ROC curve in the right panel includes supervised neural topic models and traditional topic models in which linear layers are replaced with XGBoost for increased AUC at the cost of interpretability. See Table 10. STM, structural topic model; BOW, bag-of-words; LR, logistic regression classifier; sLDA, supervised latent Dirichlet allocation (Mcauliffe and Blei 2008); NTM, neural topic model (Wang and Yang 2020) ETM, embedded topic model (Dieng et al. 2020).

Figure 8. (Color online) Estimated Coefficients  
![](/api/attachments/6TTGMQSY/fulltext/images/96d92c54e6330b6a771f2b8b41a199d2f8af9eee0757c9749575a7c8c0117131.jpg)

(b) Results From GDCM Estimated Coefficients

<table><tr><td>Input Feature</td><td>Coef.</td></tr><tr><td colspan="2">Concepts</td></tr><tr><td>Aesthetics</td><td>0.107</td></tr><tr><td>Conformance</td><td>-0.076</td></tr><tr><td>Features</td><td>0.058</td></tr><tr><td>Value</td><td>0.054</td></tr><tr><td>Serviceability</td><td>-0.083</td></tr><tr><td colspan="2">Explanatory Variables</td></tr><tr><td>Price</td><td>-0.003</td></tr><tr><td>Avg Rating (std)</td><td>0.288</td></tr><tr><td>User-Page Views</td><td>-0.005</td></tr><tr><td>Prod Tot # Reviews</td><td>0.002</td></tr><tr><td>Prod Tot # Pg views</td><td>-0.0001</td></tr><tr><td>Total Wallet Size</td><td>0.0048</td></tr><tr><td>User-Pg # of Rev Read</td><td>0.012</td></tr></table>

(c) Results From Liu et al. (2019)

<table><tr><td>Input Feature</td><td>Coef.</td></tr><tr><td colspan="2">Concepts</td></tr><tr><td>Aesthetics</td><td>0.0897</td></tr><tr><td>Conformance</td><td>-0.001</td></tr><tr><td>Features</td><td>0.0128</td></tr><tr><td>Value</td><td>0.0187</td></tr><tr><td>Serviceability</td><td>-0.0367</td></tr><tr><td colspan="2">Explanatory Variables</td></tr><tr><td>Price</td><td>-0.0025</td></tr><tr><td>Avg Rating</td><td>0.3781</td></tr><tr><td>Total # Reviews</td><td>0.0002</td></tr></table>

Notes. Panel (a) and (b) presents estimated coefficients by GDCM. As a comparison, panel (c) reports coefficients from a causal study (Liu et al. 2019) that uses a similar data set from the same context.

Lastly, we highlight that GDCM’s end-to-end automated correlational result mostly replicates top-down theory-driven causal results by Liu et al. (2019) on the impact of consumer review content on sales conversion, serving as examples of external validity of GDCM as “guided exploration” tool. Liu et al. (2019) is a causal study run on similar data in the same setting that quantified the impact of the theory-driven concept (Garvin 1984) discussed in the user-generated review on conversion. As shown in Figure 8, (b) and (c), concepts discovered by GDCM not only (1) overlap with top-down causal study concepts by Garvin (1984) but also (2) closely match coefficient estimates. Notably, both GDCM and Liu et al. (2019) quantify that the concept of aesthetics has the highest positive relevance to conversion, whereas serviceability has the lowest negative relevance to conversion. 2

## 5.3.3. Additional Experiments

5.3.3.1. Impact of the Guiding Outcome Variable on Concepts Discovered. We demonstrate the role of the guiding variables on concept discovery using a different data set (DonorsChoose), which provides several different and sensible managerial outcome variables Y (which we lack in the main data set). The results show that extracted concepts are sensitive to guiding variables and sensibly so, further demonstrating the flexibility of GDCM as a managerial tool. See Online Appendix C for details.

5.3.3.2. Ablation Analysis. Furthermore, we conduct an ablation analysis to examine the impact of increasing the regularization strength λ (sparsity), η (diversity), and ρ (classification loss/relevance) on concept interpretability and prediction. We present several interesting findings in Figure 9. (1) The interpretability-accuracy trade-off correlation depends on different parameters of the model. (2)

Increasing ρ leads to an increase in AUC as intended and a slight enhance in interpretability. (3) Increasing concept sparsity, λ, decreases AUC, but it has no impact on interpretability. (4) Increasing concept diversity, η, has no impact on AUC, but it increases interpretability. See Online Appendix B.6 for more detailed information.

## 5.4. Results Summary

Using a data set on consumer purchases and reviewreading behavior, we have shown that GDCM is able to maximize the discovery of interpretable concepts that highly correlate with the managerial outcome Y variable.

Connecting GDCM method claims (Sections 5.1 and 5.2) to managerial impact, assume that we did not know much about dimensions of the product price and quality that influence consumers. Running LDA models 50 or even 150 times failed to recover many of Garvin’s concepts. In comparison, GDCM recovers most concepts in just five runs. This demonstrates the potential value of GDCM for text data without prior knowledge of what concepts are relevant. GDCM’s high interpretability provides values akin to those in the XAI literature, whereas high recall serves to discover potentially unseen insights. In addition, GDCM has demonstrated its ability against benchmark models (Section 5.3) to retain concepts that correlated highly with managerial variables Y. GDCM excels in predictive performance over interpretable baselines while remaining competitive with black-box prediction-focused methods.

## 6. Implications for Managers and Researchers

## 6.1. Managerial Implications

We have used the example of a guided exploration task in the e-commerce managerial setting to show how

Figure 9. (Color online) Variation in ROC and AUC and Coherence for Different Hyperparameter Settings  
![](/api/attachments/6TTGMQSY/fulltext/images/4bbecdd390d4a53cddd14c3252a61d697ad5410e0f7e61996a6a2ca3249c9568.jpg)

![](/api/attachments/6TTGMQSY/fulltext/images/3070ee53c9b5710eb35e9a000d2ffdafff38b6610a85f52c6258bc6a05c39362.jpg)  
Notes. Each hyperparameter was varied while keeping the other two fixed. (a) Variation in ROC and AUC. (b) Variation in coherence.

GDCM helps businesses discover from user-read review content the important concepts (i.e., Garvin’s dimensions) that highly correlate with conversion. The economic value of identifying Garvin’s dimensions from user-generated text is well documented in prior literature documents. For example, Abrahams et al. (2015) report that textual data from social media can be used to discover product defects to inform quality management (serviceability), Archak et al. (2011) reveal that review text can be used to learn consumers’ relative preferences for different product features (features), and Netzer et al. (2012) use text from online forums to mine the market structure and uncover characteristics of the competitive landscape (brand). Lastly, Liu et al. (2019) extract Garvin’s concept in the review text to quantify the causal impact on consumer purchase behavior.

More broadly, in research papers that discuss the value of the text, researchers either (1) quantify only the signal value of the text without describing the actual content or (2) quantify the values of concepts that are already proven to matter. The economic value of (1) identifying coherent concepts from text data known to provide significant signals and (2) recovering previously unknown concepts in the text along with a gauge of economic significance and thus, the value of GDCM is evident.

Apart from GDCM’s ability to mine interpretable concepts relevant to managerial outcome, GDCM is also able to (1) perform guided concept mining in “one click,” (2) provide predictions and extract concepts for previously unseen documents, and (3) retrain the learned model dynamically via stochastic gradient descent updates. Specifically, GDCM can be used to dynamically monitor consumer feedback and complaints (i.e., the dynamic resonance marketing tool (Clemons et al. 2006)) on social media and websites as a more exploratory version of techniques shown in Netzer et al. (2012) and Abbasi et al. (2019). Managers can benefit from a dashboard of daily or weekly summarization of consumer chatters using GDCM in place and quickly see different aspects by focusing on appropriate outcomes. Similarly, when applied to reviews of a specific product, GDCM could extract feature importance, which might inform product design. This would be a quicker (although less accurate) alternative to the method described by Timoshenko and Hauser (2019).

With respect to bias in algorithm literature, there is a lack of literature on unstructured data. GDCM could serve to detect content bias in the text. For example, say a news site is using a recommender system to suggest articles to read. If the recommender (which is based on consumer history) repeatedly recommends particular content, this may lead to filter bubbles (Pariser 2011, Lee and Hosanagar 2019), whereby consumers only consume content they like or agree with. This could be harmful to general consumer welfare and to the platform (Sunstein 2018). GDCM could serve to detect content biases. Similar applications exist in social media and search engines.

## 6.2. Implications for Researchers

For researchers, GDCM is an exploratory and noncausal technique that is correlational in nature. GDCM zeros in on potential candidate concepts toward building hypotheses and causal study for theory building. GDCM can serve as an essential tool to recover empirical generalization<sup>5</sup> or for computationally intensive theory construction<sup>6</sup>—in short, as a tool for augmented hypothesis development.

GDCM serves as a jumping-off point for further focused causal studies that may lead to prescriptive policies. In the context of business research, there are two broad use cases for machine learning: (1) scale hypotheses testing and (2) discovering hypotheses from empirical data. Extant papers already utilize ML to scale theory testing. GDCM is a tool for the second task. “Guided exploration” tools, such as the GDCM, and other interpretable machine learning techniques to augment hypothesis generation are ripe for serious consideration.

Ultimately, however, GDCM is only as good as the user, and it is not designed for making causal statements. For example, in our data, the online reviewers are selfselected and heterogeneous. GDCM captures insight from the text as is, albeit while controlling for any variables. Only researchers who practice sound logic through domain knowledge can be good judges of what is spurious and what is worth further investigation.

## 7. Conclusion

We introduced a new deep learning-based text mining method, the GDCM, to explore, organize, and extract information from textual data guided by any managerial outcome variable Y. We hope that managers and researchers can use GDCM creatively with any combination of text, structured, and managerial outcome variables to glean insights and build out new hypotheses (and ultimately, theories) from rich text data.

## Acknowledgments

The authors thank Eric Zhou, David Blei, Olivier Toubia, Oded Netzer, Jey Han Lau, Arun Rai, Gedas Adomavicius, Sudhir K., Carl Mela, Christophe Van Den Bulte, Raghu

Iyengar, Eric Bradlow, Ryan Dew, Alex Burnap, Mingfeng Lin, Panos Ipeirotis, D. J. Wu, Kunpeng Zhang, Daehwan Ahn, Alan Montgomery, Lan Luo, Dinesh Puranam, George Chen, Lizhen Xu, John McCoy, Eric Schwartz, Fred Feinberg, Anocha Aribarg, and Puneet Manchanda for very helpful com ments or conversations that shaped the paper. The authors also thank participants in the Marketing Science Conferences 2018 and 2019; Conference on Information Systems and Technology 2018; the Conference on Digital Marketing and Machine Learn ing 2018; the Advanced Computing in Social Sciences Sympo sium 2019; Choice Symposium 2019; INFORMS 2019; the Conference on Artificial Intelligence, Machine Learning, and Digital Analytics 2019; 2019 Korean Chapter of the Association for Information Systems (KrAIS) Research Workshop at International Conference of Information Systems (ICIS); and Wharton Behavioral Insights Through Text 2020 as well as seminar audiences at McGill University, Korea Advanced Institute of Science and Technology, Seoul National University, the University of Pittsburgh, the University of Southern California, the University of Minnesota, HEC Paris, the University of Maryland, Georgia Institute of Technology, Harvard University, the University of Michigan, The Wharton School, and Rutgers University for very helpful comments or conversations that shaped the paper.

## Appendix A. Using Pretrained Language Models for Topic Modeling

This appendix investigates the recent academic and technical literature on using LLMs for thematic structure extraction from textual data. This body of research remains relatively nascent, with the bulk of studies published in November and December 2023. We identify four distinct research directions in Table A.1. Here, we evaluate TopicGPT (Pham et al. 2023), a prominent prompt-driven LLM topic method. Refer to the online appendix for additional results utilizing BERTopic (Grootendorst 2022) in topic modeling.

Table A.1. Main Research Directions of Topic Modeling Based on Pretrained Language Models

<table><tr><td>Research directions</td><td>Comment</td></tr><tr><td>Explanation of topic words (Caballero 2023, Grootendorst 2023)</td><td>This approach leverages LLMs to create understandable phrases or sentences that explain the topic words produced by topic modeling algorithms. These techniques operate without modifying the foundational topic modeling algorithms or the LLMs themselves, relying on prompting the LLMs to summarize topic words. The objectives of these methods are different from that of GDCM. They can also be applied to the concept words generated by GDCM.</td></tr><tr><td>Document clustering with labeling (Grootendorst 2022, Han et al. 2023)</td><td>This approach utilizes the encoding capabilities of LLMs to embed documents, subsequently clustering these embeddings and assigning topics to the formed clusters. These methods maintain the original architecture and weights of the language models intact.</td></tr><tr><td>Prompt-driven LLM topic models (Pham et al. 2023, Wang et al. 2023)</td><td>This methodology prompts LLMs to initially identify all possible topics within each document. Subsequently, LLMs refine and select the relevant topics. This process involves an initial broad identification followed by a focused refinement of topics.</td></tr><tr><td>Autoencoder-based topic models (Xu et al. 2023)</td><td>This approach utilizes variational autoencoder architecture, which includes encoder and decoder networks that reconstruct the original documents.</td></tr></table>

Notes. (1) These methods do not incorporate managerial outcome variables to facilitate topic extraction. Therefore, they belong to Quadrant III or Quadrant IV (depending on whether seed topics are provided), and therefore, they are not direct competitors with GDCM. (2) Some methods have not been released publicly (Wang et al. 2023, Xu et al. 2023).

## Figure A.1. Sample Output from TopicGPT

<table><tr><td colspan="4">very light and easy to handle. love the fact that it lights and bleeps to let you know its on - was always leaving the old one on all day!! very good value too</td></tr><tr><td colspan="4">Extracted Topic List. TopicGPT assigns the following topics to this document:</td></tr><tr><td>Design FlawHiding CablesQuality IssuesRecommendationSizeConvenience</td><td>DurabilityFiltersQualityDesignEasy to StoreMaterial</td><td>ComfortableTechnologyComfortValuePowerStorage</td><td>GoodEasy to UseGood Value</td></tr><tr><td colspan="4">Selected Explanations. Here are some of the explanations given by TopicGPT:</td></tr><tr><td colspan="4">Price — the text mentions “very good value too”Design Flaw — the text mentions “love the fact that it lights and bleeps to let you know its on - was always leaving the old one on all day!”Hiding Cables — the text mentions “love the fact that it lights and bleeps to let you know its on - was always leaving the old one on all day!”</td></tr></table>

Unlike traditional topic models, TopicGPT does not explicitly model a document as a mixture of topics; instead, it directly summarizes each document into succinct labels. Spe cifically, this method consists of two main stages: topic generation and topic assignment. The first stage aims to generate a list of topics from an input corpus, and the second stage aims to assign the most relevant topic to a given document and provide an explanation.

Because TopicGPT’s results come directly from the free-text response of LLM, its performance is bounded by the reasoning ability of the large language models. As large language models often rely on in-context learning (providing LLMs with a few input-output data as demonstrations) to elicit reasoning in complicated tasks, TopicGPT relies on explicit seed topics to ensure the production of high-quality topics. Additionally, it may also suffer from the hallucination problem, a situation where the model generates content that is inaccurate or irrelevant to the tasks.

To demonstrate, we run TopicGPT based on Llama2-7B over the main data set in the manuscript. Figure A.1 shows one example taken from the output of TopicGPT. We observe instances where TopicGPT demonstrates a hallucination during the generation and explanation of topic assignments. In the first example, TopicGPT successfully captures the key concepts related to the concepts of aesthetics, features, and value of the item. Yet, it also erroneously assigns unrelated topics that are absent in the original text, such as hiding cables, filters, and storage.

Table A.2. Prediction Performance with TopicGPT Extracted Topics with Different Prompts and Self-Correction Iterations

<table><tr><td></td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1 score</td><td>AUC</td></tr><tr><td colspan="6">No seed</td></tr><tr><td>No correction</td><td>0.6329</td><td>0.6376</td><td>0.7781</td><td>0.7009</td><td>0.6820</td></tr><tr><td>1st correction</td><td>0.6354</td><td>0.6383</td><td>0.7858</td><td>0.7044</td><td>0.6882</td></tr><tr><td>2nd correction</td><td>0.6394</td><td>0.6435</td><td>0.7797</td><td>0.7051</td><td>0.6895</td></tr><tr><td>3rd correction</td><td>0.6434</td><td>0.6466</td><td>0.7827</td><td>0.7082</td><td>0.6916</td></tr><tr><td colspan="6">Seeded</td></tr><tr><td>No correction</td><td>0.6604</td><td>0.6865</td><td>0.7098</td><td>0.6980</td><td>0.7080</td></tr><tr><td>1st correction</td><td>0.6607</td><td>0.6863</td><td>0.7114</td><td>0.6986</td><td>0.7075</td></tr><tr><td>2nd correction</td><td>0.6633</td><td>0.6896</td><td>0.7108</td><td>0.7001</td><td>0.7095</td></tr><tr><td>3rd correction</td><td>0.6633</td><td>0.6896</td><td>0.7108</td><td>0.7001</td><td>0.7095</td></tr></table>

To evaluate the predictive capability of topics derived from TopicGPT, we transformed the topics assigned to each document into one-hot encoded vectors. These vectors were then combined with additional data, X, to predict the outcome variable, Y, using the XGBoost model. The results of these predictions are presented in Table A.2. We tested two versions of prompting: a “seeded” version, which incorpo rates Garvin’s dimensions as seed topics, and a “no seed” version, which uses a single example topic. The “seeded” approach consistently outperformed the “no seed” version. Additionally, we applied a three-round self-correction pro cess. Notably, even the best version of TopicGPT underperforms significantly when compared with GDCM.

## Appendix B. Definition on Coherence

The topic modeling literature first came up with ways to detect “interpretability” by human judgment through Mechanical Turkers (Chang et al. 2009); then, the “coherence” construct was validated with domain expert taggers who “annotated [topics] as ‘good’ if they contained words that could be grouped together as a single coherent concept” (Mimno and McCallum 2008). Next, automated measures were constructed that seem to perform as well as or better than humans (Mimno and McCallum 2008, Newman et al. 2010, Lau et al. 2014). For example, metrics based on word co-occurrences and mutual information based on an external corpus, such as Wikipedia, are more representative of how humans would evaluate a topic as interpretable (Newman et al. 2010). From the XAI literature perspective, this measure of interpretability fits the desiderata of measuring unambiguity (Ras et al. 2018) and selectivity of explanation (Lipton 2018, Miller 2018).

In this paper, we use the measure defined by Mimno and McCallum (2008) from the topic modeling literature. It computes the sum of a pairwise score function on the top n word $w _ { 1 } , w _ { 2 } . . , w _ { n }$ used to describe each topic:

$$
\text {Coherence} = \sum_ {i <   j} \log \frac {D (w _ {i} , w _ {j}) + 1}{D (w _ {i})},\tag{B.1}
$$

where $D ( w _ { i } )$ is the count of documents containing the word $w _ { i }$ and $D ( w _ { i } , w _ { j } )$ is the count of documents containing both words $w _ { i }$ and $w _ { j } .$ Simply put, the coherence metric measures how well focused the group of top topic keywords is in describing a singular concept. A higher topic coherence means that the keywords within one topic dimension are more coherent with each other in concept. Note that although the measure of coherence originates from topic modeling lit erature, it is directly applicable to any set of keywords.

## Endnotes

<sup>1</sup> Code is shared at https://github.com/cygit/gdcm.

<sup>2</sup> In this loss function, the first summation operates over all pivotcontext pairs in the corpus to ensure that words occurring often in the same context have similar embeddings. The second term operates over each pivot-context pair that does not occur in the corpus to encourage them to have dissimilar embeddings.

<sup>3</sup> For predictive performance measurement, data are split into 70% training, 15% validation, and 15% test sets. The model is trained on up to 500 different parameter configurations, and our model gives stable results across these sets. All results hereafter are produced by the model trained under the configuration $\lambda = 1 0 , \rho = 1 , 0 0 0 , \eta = 1 , 0 0 0$

<sup>4</sup> GDCM uses data from the same context as Liu et al. (2019) in replicating their results. However, the training data sets are different because of data availability and differences in processing methods.

<sup>5</sup> Bass (1995) describes empirical generalization as “a pattern or regularity that repeats over different circumstances and that can be described simply by mathematical, graphic, or symbolic methods.”

<sup>6</sup> Miranda et al. (2022) describes the computationally intensive theory construction as a genre of research that “produces theoretical insights from patterns identified using computational techniques,” such as “providing simulated data, pattern visualizations, or quantifications.”

## References

Abbasi A, Zhou Y, Deng S, Zhang P (2018) Text analytics to support sense-making in social media: A language-action perspective. MIS Quart. 42(2):427–464.

Abbasi A, Li J, Adjeroh D, Abate M, Zheng W (2019) Don’t mention it? Analyzing user-generated content signals for early adverse event warnings. Inform. Systems Res. 30(3):1007–1028.

Abrahams AS, Fan W, Wang GA, Zhang Z, Jiao J (2015) An integrated text analytic framework for product defect discovery. Production Oper. Management 24(6):975–990.

Airoldi EM, Bischof JM (2016) Improving and evaluating topic models and other models of text. J. Amer. Statist. Assoc. 111(516):1381–1403.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Bass FM (1995) Empirical generalizations and marketing science: A personal view. Marketing Sci. 14(3 Suppl):G6–G19.

Blei DM, Ng AY, Jordan MI (2003) Latent Dirichlet allocation. J. Machine Learn. Res. 3(January):993–1022.

Caballero AJ (2023) Document topic extraction with large language models (LLM) and the latent Dirichlet allocation (LDA) algorithm. Accessed April 17, 2024, https://towardsdatascience.com/documenttopic-extraction-with-large-language-models-llm-and-the-latentdirichlet-allocation-e4697e4dae87.

Carey S (2009) The Origin of Concepts (Oxford University Press, Oxford, UK).

Chai Y, Li W (2019) Toward deep learning interpretability: A topic modeling approach. Proc. Internat. Conf. Inform. Systems (Association for Information Systems, Atlanta).

Chang J, Boyd-Graber JL, Gerrish S, Wang C, Blei DM (2009) Reading tea leaves: How humans interpret topic models. Bengio Y, Schuurmans D, Lafferty JD, Williams CKI, Culotta A, eds. Adv. Neural Inform. Processing Systems (Curran Associates, Red Hook, NY), 288–296.

Chen T, Guestrin C (2016) XGBoost: A scalable tree boosting system. Proc. 22nd ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 785–794.

Chen W, Gu B, Ye Q, Zhu KX (2019) Measuring and managing the externality of managerial responses to online customer reviews. Inform. Systems Res. 30(1):81–96.

Chen J, He J, Shen Y, Xiao L, He X, Gao J, Song X, Deng L (2015) Endto-end learning of LDA by mirror-descent back propagation over a deep architecture. Cortes C, Lawrence N, Lee D, Sugiyama M, Garnett R, eds. Proc. 28th Internat. Conf. Neural Inform. Processing Systems (MIT Press, Cambridge, MA), 1765–1773.

Choi AA, Cho D, Yim D, Moon JY, Oh W (2019) When seeing helps believing: The interactive effects of previews and reviews on e-book purchases. Inform. Systems Res. 30(4):1164–1183.

Clemons EK, Gao GG, Hitt LM (2006) When online reviews meet hyperdifferentiation: A study of the craft beer industry. J. Management Inform. Systems 23(2):149–171.

Dhurandhar A, Iyengar V, Luss R, Shanmugam K (2017) Tip: Typifying the interpretability of procedures. Preprint, submitted June 9, https://arxiv.org/abs/1706.02952.

Dieng AB, Ruiz FJ, Blei DM (2020) Topic modeling in embedding spaces. Trans. Assoc. Comput. Linguistics 8:439–453.

Efron B, Tibshirani R (1997) Improvements on cross-validation: The.632+ bootstrap method. J. Amer. Statist. Assoc. 92(438):548–560.

Feifer J (2013) The Amazon whisperer. Accessed April 17, 2024 https://www.fast company.com/3021229/chaim-pikarski-theamazon-whisperer.

Gardenfors P (2004) Conceptual Spaces: The Geometry of Thought (MIT Press, Cambridge, MA).

Garvin DA (1984) What does “product quality” really mean? MIT Sloan Management Rev. (October 15), https://sloanreview.mit. edu/article/what-does-product-quality-really-mean/.

Garvin DA (1987) Competing on the 8 dimensions of quality. Harvard Bus. Rev. 65(6):101–109.

Goldstone RL, Son JY (2005) Similarity. Holyoak KJ, Morrison RG, eds. The Cambridge Handbook of Thinking and Reasoning (Cambridge University Press, Cambridge, UK), 13–36.

Grootendorst M (2022) BERTopic: Neural topic modeling with a classbased TF-IDF procedure. Preprint, submitted March 11, https:// arxiv.org/abs/2203.05794.

Grootendorst M (2023) Topic modeling with Llama 2. Accessed April 17, 2024, https://towardsdatascience.com/topic-modeling with-llama-2-85177d01e174.

Guidotti R, Monreale A, Ruggieri S, Turini F, Giannotti F, Pedreschi D (2018) A survey of methods for explaining black box models. ACM Comput. Surveys 51(5):1–42.

Han S, Shin M, Park S, Jung C, Cha M (2023) Unified neural topic model via contrastive learning and term weighting. Vlachos A, Augenstein I, eds. Proc. 17th Conf. Eur. Chapter Assoc. Comput. Linguistics (Association for Computational Linguistics, Stroudsburg PA), 1802–1817.

Harris ZS (1954) Distributional structure. Word 10(2–3):146–162.

Huang S, Tran TD (2018) Sparse signal recovery via generalized entropy functions minimization. IEEE Trans. Signal Processing 67(5):1322–1337

Jackendoff R (1989) What is a concept, that a person may grasp it? Mind Language 4(1–2):68–102.

Jagarlamudi J, Daume ´ H III, Udupa R (2012) Incorporating lexical priors into topic models. Daelemans W, ed. Proc. 13th Conf. Eur. Chapter Assoc. Comput. Linguistics (Association for Computational Linguistics, Stroudsburg, PA), 204–213.

Jurafsky D (2000) Speech & Language Processing (Pearson Education India, Noida, India).

Kuhn TS (2012) The Structure of Scientific Revolutions (University of Chicago Press, Chicago).

Lau JH, Newman D, Baldwin T (2014) Machine reading tea leaves: Automatically evaluating topic coherence and topic model qual ity. Wintner S, Goldwater S, Riezler S, eds. Proc. 14th Conf. Eur. Chapter Assoc. Comput. Linguistics (Association for Computational Linguistics, Stroudsburg, PA), 530–539.

LeCun Y, Bengio Y, Hinton G (2015) Deep learning. Nature 521(7553): 436–444.

Lee D, Hosanagar K (2019) How do recommender systems affect sales diversity? A cross-category investigation via randomized field experiment. Inform. Systems Res. 30(1):239–259.

Lee D, Hosanagar K, Nair H (2018) Advertising content and consumer engagement on social media: Evidence from Facebook. Management Sci. 64(11):5105–5131.

Lipton ZC (2018) The mythos of model interpretability: In machine learning, the concept of interpretability is both important and slippery. Queue 16(3):31–57.

Liu X, Lee D, Srinivasan K (2019) Large-scale cross-category analysis of consumer review content on sales conversion leveraging deep learning. J. Marketing Res. 56(6):918–943.

Liu Y, Liu Z, Chua TS, Sun M (2015) Topical word embeddings. Gunning D, Yeh PZ, eds. Proc. AAAI Conf. Artificial Intelligence, vol. 29(1) (AAAI, Palo Alto, CA).

Lu J, Lee D, Kim TW, Danks D (2019) Good explanation for algorith mic transparency. Preprint, submitted November 11, https://dx. doi.org/10.2139/ssrn.3503603.

Lundberg S, Lee SI (2017) A unified approach to interpreting model predictions. Guyon I, Luxburg UV, Bengio S, Wallach H, Fergus R, Vishwanathan S, Garnett R, eds. Proc. 31st Conf. Neural Inform. Pro cessing Systems (Curran Associates Inc., Red Hook, NY), 4768–4777.

Margolis E, Laurence S, eds. (1999) Concepts: Core Readings (MIT Press, Cambridge, MA).

Margolis E, Laurence S (2023) Concepts. Zalta EN, Nodelman U, eds. The Stanford Encyclopedia of Philosophy, Fall 2023 ed. (Metaphysics Research Lab, Stanford University, Stanford, CA).

Mcauliffe JD, Blei DM (2008) Supervised topic models. Platt J, Koller D, Singer Y, Roweis S, eds. Proc. 20th Internat. Conf. Neural Inform. Processing Systems (Curran Associates, Red Hook, NY), 121–128.

Mikolov T, Sutskever I, Chen K, Corrado GS, Dean J (2013) Distrib uted representations of words and phrases and their composi tionality. Burges CJC, Bottou L, Welling M, Ghahramani Z, Weinberger KQ, eds. Adv. Neural Inform. Processing Systems (Curran Associates, Red Hook, NY), 3111–3119.

Miller T (2018) Explanation in artificial intelligence: Insights from the social sciences. Artificial Intelligence 267(2019):1–38.

Mimno D, McCallum A (2008) Topic models conditioned on arbitrary features with Dirichlet-multinomial regression. Barzilay R, Johnson M, eds. Proc. 2011 Conf. Empirical Methods Natl. Language Processing (Association for Computational Linguistics, Stroudsburg, PA), 262–272.

Miranda S, Berente N, Seidel S, Safadi H, Burton-Jones A (2022) Edi tor’s comments: Computationally intensive theory construction: A primer for authors and reviewers. MIS Quart. 46(2):iii–xviii.

Moody CE (2016) Mixing Dirichlet topic models and word embeddings to make lda2vec. Preprint, submitted May 6, https://arxiv. org/abs/1605.02019.

Murdoch WJ, Singh C, Kumbier K, Abbasi-Asl R, Yu B (2019) Interpretable machine learning: Definitions, methods, and applications. Preprint, submitted January 14, https://arxiv.org/abs/ 1901.04592

Murphy G (2004) The Big Book of Concepts (MIT Press, Cambridge, MA).

Netzer O, Lemaire A, Herzenstein M (2019) When words sweat: Iden tifying signals for loan default in the text of loan applications. J. Marketing Res. 56(6):960–980.

Netzer O, Feldman R, Goldenberg J, Fresko M (2012) Mine your own business: Market-structure surveillance through text mining Marketing Sci. 31(3):521–543.

Newman D, Lau JH, Grieser K, Baldwin T (2010) Automatic evaluation of topic coherence. Kaplan R, Burstein J, Harper M, PennHuman G, eds. Language Tech. 2010 Annual Conf. North American Chapter Assoc. Comput. Linguist. (Association for Computational Linguistics, Stroudsburg, PA), 100–108.

Osherson DN, Smith EE (1981) On the adequacy of prototype theory as a theory of concepts. Cognition 9(1):35–58.

Pariser E (2011) The Filter Bubble: How the New Personalized Web Is Changing What We Read and How We Think (Penguin, New York).

Pennington J, Socher R, Manning CD (2014) Glove: Global vectors for word representation. Moschitti A, Pang B, Daelemans W, eds. Proc. 2014 Conf. Empirical Methods Natural Language Processing (EMNLP) (Association for Computational Linguistics, Stroudsburg, PA), 1532–1543.

Pham CM, Hoyle A, Sun S, Iyyer M (2023) TopicGPT: A promptbased topic modeling framework. Preprint, submitted November 2, https://arxiv.org/abs/2311.01449.

Ransbotham S, Lurie NH, Liu H (2019) Creation and consumption of mobile word of mouth: How are mobile reviews different? Marketing Sci. 38(5):773–792.

Ras G, van Gerven M, Haselager P (2018) Explanation methods in deep learning: Users, values, concerns and challenges. Escalante H, Escalera S, Guyon I, Baro ´ X, Guc¨ ¸lu¨ tu¨ rk Y, Guc¨ ¸lu ¨ U, van Gerven M, eds. Explainable and Interpretable Models in Computer Vision and Machine Learning, Springer Series on Challenges in Machin Learning (Springer, Cham, Switzerland), 19–36.

Ribeiro MT, Singh S, Guestrin C (2016) “Why should I trust you?”: Explaining the predictions of any classifier. Proc. 22nd ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Association for Computing Machinery, New York).

Roberts ME, Stewart BM, Tingley D, Lucas C, Leder-Luis J, Gadarian SK, Albertson B, Rand DG (2014) Structural topic models for open-ended survey responses. Amer. J. Political Sci. 58(4): 1064–1082.

Rosch E (2002) Principles of categorization. Levitin DJ, ed. Foundations of Cognitive Psychology: Core Readings (MIT Press, Cambridge, MA), 251–270.

Rudin C (2019) Stop explaining black box machine learning model for high stakes decisions and use interpretable models instead. Nature Machine Intelligence 1(5):206–215.

Scho¨lkopf B, Locatello F, Bauer S, Ke NR, Kalchbrenner N, Goyal A Bengio Y (2021) Toward causal representation learning. Proc. IEEE 109(5):612–634.

Shi B, Lam W, Jameel S, Schockaert S, Lai KP (2017) Jointly learning word embeddings and latent topics. Proc. 40th Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (Association for Computing Machinery, New York), 375–384.

Sloutsky VM, Deng W (2019) Categories, concepts, and conceptual development. Lang. Cogn. Neurosci. 34(10):1284–1297.

Solomon KO, Medin DL, Lynch EB (1999) Concepts do more than cat egorize. Trends Cogn. Sci. 3(3):99–105.

Sridhar D, Daume ´ H III, Blei D (2022) Heterogeneous supervised topic models. Trans. Assoc. Comput. Linguist. 10:732–745.

Srivastava A, Sutton C (2017) Autoencoding variational inference for topic models. Preprint, submitted March 4, https://arxiv.org/ abs/1703.01488

Sunstein CR (2018) Republic: Divided Democracy in the Age of Social Media (Princeton University Press, Princeton, NJ).

Tibshirani R (1996) Regression shrinkage and selection via the lasso. J. Roy. Statist. Soc. Ser. B Statist. Methodology 58(1):267–288.

Timoshenko A, Hauser JR (2019) Identifying customer needs from user-generated content. Marketing Sci. 38(1):1–20.

Toubia O, Iyengar G, Bunnell R, Lemaire A (2019) Extracting features of entertainment products: A guided LDA approach informed by the psychology of media consumption. J. Marketing Res. 56(1):18–36.

Vayansky I, Kumar SA (2020) A review of topic modeling methods. Inform. Systems 94(2020):101582.

Wang X, Yang Y (2020) Neural topic model with attention for supervised learning. Chiappa S, Calandra R, eds. Proc. Twenty Third Internat. Conf. Artificial Intelligence Statist. (PMLR, New York), 1147–1156.

Wang H, Prakash N, Hoang NK, Hee MS, Naseem U, Lee RKW (2023) Prompting large language models for topic modeling. 2023 IEEE Internat. Conf. Big Data (BigData) (IEEE, Piscataway, NJ), 1236–1241.

Wernicke S (2015) How to use data to make a hit TV show. Accessed April 17, 2024, https://www.ted.com/talks/sebastian\_wernicke\_ how\_to\_use\_data\_to\_make\_a\_hit\_tv\_show.

Xu W, Hu W, Wu F, Sengamedu S (2023) Detime: Diffusion-enhanced topic modeling using encoder-decoder based LLM. Preprint, submitted October 23, https://arxiv.org/abs/2310.15296.

Xun G, Li Y, Gao J, Zhang A (2017) Collaboratively improving topic discovery and word embeddings by coordinating global and local contexts. Proc. 23rd ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Association for Computing Machinery, New York), 535–543.

Yang Y, Zhang K, Fan Y (2023) SDTM: A supervised Bayesian deep topic model for text analytics. Inform. Systems Res. 34(1):137–156.

Zhang K, Moe W (2021) Measuring brand favorability using large-scale social media data. Inform. Systems Res. 32(4) 1128–1139.

Zhu J, Ahmed A, Xing EP (2012) MedLDA: Maximum margin supervised topic models. J. Machine Learn. Res. 13(August): 2237–2278.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>
