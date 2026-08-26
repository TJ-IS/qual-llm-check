---
otero_id: 20023
otero_key: "64WDNFPH"
title: "Removing order effects from human-classified datasets: A machine learning method to improve decision making systems"
authors: "Dmitry Romanov; Valentin Molokanov; Nikolai Kazantsev; Ashish Kumar Jha"
year: "2023"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113891"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Removing order effects from human-classified datasets: A machine learning method to improve decision making systems

Dmitry Romanov <sup>a</sup>, Valentin Molokanov <sup>b</sup>, Nikolai Kazantsev <sup>c</sup>, Ashish Kumar Jha <sup>d,\*</sup>

<sup>a</sup> Business Informatics, Graduate School of Business, HSE University, Russia

<sup>b</sup> IQMen Business Intelligence, Russia

<sup>c</sup> Institute for Manufacturing, University of Cambridge, United Kingdom

<sup>d</sup> Trinity Business School, Trinity College Dublin, Ireland

## A R T I C L E I N F O

Keywords: Order effect Machine learning Artificial intelligence Decision-making Information systems (IS) research

## A B S T R A C T

Although recent developments in Artificial Intelligence (AI) and machine learning (ML) aim to enhance the fairness and transparency of decision-making systems, research has found that neural networks (or other similar AI techniques) are still effected by human cognitive biases due to the training datasets. In this study, we focus on order effects, i.e., when the input of information impacts human perception and the decisions resulting from this information. We propose the Order Effect Removal Method (OERM) for handling the order effect which leads to bias and for helping organizations remove these biases from their training datasets and, therefore, from auto mated decision-making systems. Using design science principles to theoretically create, test, and validate the method, we can eliminate the order bias even in basic classification systems. Furthermore, the method can be applied in a multidisciplinary context. where an AI-based algorithm substitutes for manual work

## 1. Introduction

“Amazon scraps secret [artificial intelligence] recruiting tool that showed bias against women” [1].

“The Use of Artificial Intelligence in Business Codifies Gendered Ageism How Do We Fix $I t 2 ^ { \prime \prime } \ [ 2 ]$

These are two examples of news items that have recently shown the bias in artificial intelligence-led decision-making. It is no secret that human beings are prone to cognitive bias and preferences. Multiple studies have shown the different kinds of biases that humans exhibit in their decision-making [3]. Artificial intelligence (AI) was expected to cure these biases by taking decision-making away from humans and giving it to codified algorithms [4]. However, the reality, as seen in the recent discourse and news around the impact of AI, shows otherwise. We find that AI is not only unable to eliminate the human biases in decision making but instead reflects and sometimes enhances the human biases in decision making [5]. Multiple studies have advocated for more trans parency in AI-enabled decision-making by employing algorithms called explainable AI (XAI) [6]. However, these algorithms do not claim to eliminate biases in decision-making. Instead, they provide details on the process that led to the AI making the specific decision, which may lead to identifying the bias [7]. This research stream is a commendable step toward identifying biases in AI-led decision-making, but it does not do much to eliminate these biases. This paper proposes a method to elim inate one AI-led decision-making bias.

Humans exhibit many kinds of biases in decision-making, including anchoring bias, confirmation bias, and the halo effect [8]. Each of these biases has a different impact on our decision-making and hence each would require a different approach to identify and resolve it. In this study, we specifically focus on the order effect, i.e., the order of the information impacting human decision-making [9]. The order effect has been widely studied in decision-making and information systems as a mechanism that affects decision-making [10]. While social psychologist researchers focus on the psychological ways to identify and deal with human errors due to such biases, this research focuses on identifying and eliminating bias in AI-enabled decision-making.

As explained in the preceding paragraphs, if we use humangenerated datasets for training neural networks, these networks inherit the same effects from human beings and make the same mistakes [11,12] or express bias in decision-making. Therefore, new technology is needed to detect the impact of information order, as an example of a cognitive bias, eliminate it, and improve automated decision-making [13]. To this end, natural language processing technologies (such as machine learning(ML)) can automatically process text data quickly [14].

However, little is known about such attempts to eliminate the order effect [15,16].

Our paper strives to fill this gap by connecting the domains of cognitive psychology and ML. We propose the Order Effect Removal Method (OERM) for dealing with the order effect which leads to biases and for helping organizations remove these human cognitive distortions from decision-making. We use quantum lens theory to develop the proposed method. For validation, the paper utilizes five large datasets for ML with preliminary expert assessment: 20NG, Reuters, PhysRev, and our dataset ScopusAbstracts and ISAbstracts, randomly constructed to measure the lack of order effect when no manual classification took place. In the paper, we use these distinct datasets with various order effect strengths to test the detection and removal of the effect, making decision-making insensitive to the data sequence. We use basic classi fication algorithms to test our model’s efficacy in eliminating the order effect.

Our results show that even basic classification algorithms like naïve Bayes can be adopted to eliminate the order effect. Furthermore, our results show promise for the multidisciplinary application of the method in neural network learning. They could be applied in multiple industries where AI decision-making is planned as a substitute for human decision making. For instance, we can better control the work of human operators and detect their flaws when the person is tired or inaccurate during a defined time. Therefore, this study contributes to (a) applying ML to measure the order effect in organizational decision-making; (b) assess ing the influence of the order effect on text classification and enabling its removal.

## 2. Background and literature review

## 2.1. Research background

The necessity for this research is clear because a lot of organizational decision-making is becoming automated [17]. AI and black-box algo rithms, such as neural networks, are necessary [18] for process man agement in today’s business environment and beyond. While the biase displayed by humans in their decision-making are well-recognized, the role of AI in propagating or eliminating such discrimination is less well understood [17].

Microsoft Tay was an example of a twitter-bot, which learnt from massive social network datasets and communication with users. This example reveals how AI-enabled decision-making systems are vulner able to the quality and sequence of datasets they use for training. The goal of the Tay experiment was to create an AI that could communicate with humans and learn and get smarter through ML on a large human dataset. However, the results were disastrous. In less than 24 h of learning, Tay started to express a racist bias [19]. The AI learnt from the extreme amount of homophobic, racist, and extremist views on Twitter and started displaying the same tendencies. This was because of the quantity of unregulated content on Twitter used as the training dataset, and the learning Tay did on that dataset [19]. Coussement and Benoit [20] have called for the creation of interpretable data science to realize and acknowledge the biases in data-driven AI processes.

To appreciate the roots of this research it is important to broadly understand how AI algorithms work and what leads to their biases. Within the broader domain of AI, the major cause of preferences was identified to be biased datasets. AI-led decision-making is predicated upon ML algorithms (some examples of such algorithms are neural networks,<sup>1</sup> support vector machines, deep learning, and random forest.) which enable computers to learn from humans and perform similar ac tivities. This ML. from pre-specified data is called training in the context of AI. For instance, a system may be trained on a human-curated dataset with images of different fruits in column 1 and their names in column 2. The machine learns this dataset by forming patterns to link the pictures to the words. For example, it could be based on shape, size, and color. Once the machine is trained on this dataset, it can label new images with the names of the fruits. Most commonly, the training datasets are pre pared by humans, and these datasets exhibit conscious or subconscious human biases. It would be difficult and expensive to have multiple humans prepare the training datasets to eliminate such biases. It is here that our work contributes to this field.

## 2.2. The order effect in information system research

Chinander and Schweitzer [21] define the order effect as the cognitive distortion explained by associations and mental images of a human mind which occurs in weakly-structured decision-making. When people choose the first alternative out of several possible alternatives more frequently, this type of order effect is referred to as the primacy effect, which is usually explained by higher sensitivity to initial data and by the determinism of the decision-maker [22]. For instance, the images from the beginning of a video are best remembered, which plays a huge role in advertising [23]. The overall impression of the company’s suc cess is formed from the first facts of the company’s annual report, which directly affects the behavior of investors [24]. In courts, if the jury de clares the preliminary decision that the defendant was innocent, the final decision in most cases will be the same [25]. The primacy effect exists in electoral contests [26,27], scientific journal ranking [28], so ciology and public opinion surveys [29], judging presentation quality [30], car selection [31], tourism [32] and risk ratios [33]. Alternatively, when people choose the last alternative disproportionately more frequently, this type of order effect is called the recency effect. The recency effect appears when the input information sequence is built on the contrast of risks and benefits [34,35] or in the recollection of peo ple’s past experiences [36]. Some teachers give higher grades to students at the end of the course [37]. If the audit report contradicts the financial evidence, the loan officers tend to rely on the last information received [38]. The recency effect is observed even in the behavior of young children (under three years old). If a young child is asked if he wants a cake or broccoli, 8 out of 10 children will choose the second option [39]. Many examples of the recency effect are from healthcare [40,41], finance [35], decision-making under uncertainty [42], humanitarian aid [43] and interactive information retrieval [44], see Fig. 1.

Research in information systems (IS) has confirmed the impact of the order effect on how information is presented online, for example, online reviews aimed at helping prospective buyers in their decision-making. Zhou and Guo [10] showed that the order of online reviews impact their perceived helpfulness. Wilson et al. [45] found the order effect to be an important factor that impacts the validity of IS research surveys, as the order of items impacts the outcome of these surveys. In more recent work, Camilleri [46] showed that the importance of online reviews depends on the order in which they are presented. Chau et al. [47] says that as existing models do not consider the time-order effect of online reviews, more recent feedback may be considered more important than feedback earlier. They proposed a Bayesian model to represent buyers perceived reputation considering the time-order effect and assessing how well it can explain the variation in buyers’ trust and price pre miums. Tripathi et al. [48] also investigate the order effect associated with online reviews, in particular the dependency of text attributes over the temporal order of the reviews. The results indicate that earlier re views tend to have more information for prospective customers. In the film industry, customer choice is influenced not only by the rating and the price of the movie but also by the position of the movie or series in the list on the website [49]. In the context of tourism, it has been found that people are biased by order in analyzing the cities they have visited [50].

![](/api/attachments/64WDNFPH/fulltext/images/56ec92e673b94a7cb99846bc591bc7af08d70633f0a7e5d33cf7abb2aad63bba.jpg)  
Fig. 1. The taxonomy of the order effect arguably met its training datasets for machine learning algorithms.

Companies may use the order effect to improve the quality of decision-making of employees or customers. For example, an effective recruitment strategy for large organizations implies detecting the order effect in the perceived attractiveness of the job description and making timely adjustments by the HR department [51]. Companies widely use AI and ML to detect discrepancies in decision-making. However, Seeber et al. [52] open a Pandora’s box of issues related to collaboration with machines: what if AI became teammates rather than tools?

While the order effect was broadly used as an antecedent to research, there is limited research on detecting and eliminating the order effect in data using ML. There is a need to extend the solution continuum [47,48,51], to tackle the problem space identified in IS research, and to propose an automated method that will work in interdisciplinary con texts—a gap this study aims to fill.

## 2.3. Existing approaches to detecting the order effect

The standard approach to detecting the order effect utilizes a human assessment of the order. Typically, this requires humans to assess the importance of information order in data. Such settings need an experi ment to divide participants into two groups and to assess two papers (for instance), A and B. These are provided in the standard order (AB) for one group of participants and reverse order (BA) for the other. Traditionally results have indicated that the fraction of the relevance evaluation for a pair of documents to a given theme by participants depends on the document order, i.e. the results for AB are different from those for BA. Wang and Cao [53] investigated the order effect associated with the cognitive aspect of judging document relevance in a multi-thematic field, which provides an example for manual detection. They divided a set of 16 documents into pairs, where each pair included a document from a news portal, with documents corresponding to the same topic. The participants were divided into two equal-size groups. The docu ments within each team were swapped together with the document presentation sequence. Eventually, the collected set of documents enabled the computing of independent probabilities of relevant docu ments, and the data of participants’ questionnaires served as the sources for conditional probabilities. The order effect was verified because the second document within each pair was assessed in changed conditions compared to the first and the context imposed by the first document influenced the judgment of the second.

## Table 1 shows research on order effects and their limitations.

The research mostly improves the order effect manually, which is time-consuming; automated methods are required. Moreover, as the order effect is manifested in various situations, the approach to detect ing and removing the order effect must have an interdisciplinary scope. Thus, this paper focuses on developing an interdisciplinary method that can automatically improve decision-making by removing the order ef fect in real-time.

Table 1  
Summary of research on order effects.

<table><tr><td>#</td><td>Research field</td><td>Order effect</td><td>Manifestation</td><td>Source</td><td>Limitations</td></tr><tr><td>1</td><td>Sociology</td><td>Survey answer decision-making</td><td>The sequence of questions influences indicated beliefs and survey answers.</td><td>McFarland [29],Haugtvedt and Wegener [30]</td><td></td></tr><tr><td>2</td><td>Research</td><td>Journal ranking decision-making</td><td rowspan="7">Experts overestimate journals located higher in the list.80% of election cases depend on a voting bulletin sequence of candidates&#x27; names.The sequence of clinical information shown to the doctor influenced the diagnosis.If patients were informed about small risks after potential benefits, they were less likely to accept the treatment.The early introduction of any travel feature increased its importance in the eyes of tourists.The quality and amount of disclosing financial statements influenced potential investors and the order in which those statements were sorted.Real partial existence of order effect and quantum-like interference on relevance judgment.</td><td>Serenko and Bontis [28]</td><td></td></tr><tr><td>3</td><td>Politics</td><td>Electoral decision-making</td><td>Chen, Simonovits, Krosnick and Pasek [26]</td><td></td></tr><tr><td>4</td><td>Medicine</td><td>Diagnosis decision-making</td><td>Bergus, Chapman, Levy, Ely and Oppliger [40]</td><td></td></tr><tr><td>5</td><td>Medicine</td><td>Patients&#x27; treatment acceptance decision-making</td><td>Bergus, Levin and Elstein [34]</td><td>Manual data collection and analysisLimited data setLimited scope of application</td></tr><tr><td>6</td><td>Tourism</td><td>Vacation decision-making</td><td>Oppewal, Huybers and Crouch [32]</td><td></td></tr><tr><td>7</td><td>Finance</td><td>Investment decision-making</td><td>Theis, Yankova and Eulerich [35]</td><td></td></tr><tr><td>8</td><td>Document processing</td><td>human assessment of relevance relative to the given query</td><td>Wang and Cao [53]</td><td></td></tr></table>

## 3. Methodology

## 3.1. Design science research

We selected the design science methodology [54] to build a purposeful artefact to address an interdisciplinary problem [55,56]. The resulting artefact—the Order Effect Removal Method (OERM)—can detect and eliminate cognitive bias in different contexts. To develop this kind of artefact, we gathered underlying knowledge [57,58] to “provide a useful generalization for extending knowledge in the problem or so lution domains” [57](p. 352). Fig. 2 outlines our methodology (adapted from [55]) to develop OERM in three cycles: relevance, design and rigor.

The relevance cycle collects the requirements for the development of OERM and to identify the research problem from the theoretical back ground and industrial requirements. The design cycle enables iterative demonstrations of the early results, which leads to early evaluation—a key component for deriving new requirements by assessing OERM’s usefulness in practice. We use various corpora of news and scientific article abstracts, which are classified manually or automatically to evaluate OERM (see 3.3). For example, the editors of PhysRev perform a manual classification of the journal subsection of the article; therefore, we expect to see order effects here; we do not, however, expect order effects for the ScopusAbstracts corpus, which has an automated classifi cation. The evaluation follows the design artefact’s utility, quality, and usability as key acceptance criteria for the ultimate evaluation of the research results. Inconsistencies with requirements triggered more it erations of the relevance cycle which started with environmental feed back. Finally, in the rigor cycle, we contribute to theory: in Design Science, a theory (e.g., kernel theory) may refer to “any descriptive theory that informs artefact construction” [57,59]. As classical proba bility theory uses Markov chains, which cannot explain the order effect [60,61], we use quantum probability theory to present human cognition as a quantum object that depends on the action sequence [62]. Quantum probability theory is a geometric approach to probability where different possibilities (or events or questions) are represented as sub spaces, of varying dimensionality, in a multidimensional Hilbert space [63]. The theory can explain order effects via “quantum objects”, which result from document classification based on mental perception [62.64]. During the manual classification of a dataset, each human operator did not know about the text content before reading the first part, which made all potential attribution categories equally probable. While reading, the comprehension of the text increases, and the initial topic propositions which do not match the text are rejected. The operator continues reading the second part of the text with a more precisely formulated perception of a potential topic. Therefore, the reading pro cesses for the first and second parts of the text are made with different initial conditions. Before reading the second part of the text, the oper ator’s susceptibility to different categories has already been changed.

The operator’s vision follows vector $\mathbf { \delta S _ { A } } ,$ , a projection of vector $\bf { { s } _ { 0 } }$ on (Part 1 = А). After reading the second part, the operators’ perception of the A category is defined by the vector $\pmb { S } _ { \mathbf { A B }  \mathbf { A } }$ , which is a projection of vector $\mathbf { s _ { A } }$ on (part12 = А). The second part needs a stronger dominance of topic B to change an operator’s perception from one topic to another. Similarly, suppose after reading the first part, the operator’s perception was defined by vector $\mathbf { \delta s } _ { \mathbf { \delta B } } ,$ then after reading the second part and relating all text to category A. In that case, the operator’s perception will be represented by vector $\pmb { S _ { \mathrm { B A  A } } } .$

$$
\frac {P r (A B \rightarrow A)}{P r (B A \rightarrow A)} = \frac {\left| S _ {A B \rightarrow A} \right| ^ {2}}{\left| S _ {B A \rightarrow A} \right| ^ {2}}
$$

Quantum objects reside in the superposition of conditions—the unit vector $\bf { { s } _ { 0 } }$ in Fig. 3.

To date, major experiments to automate decision-making relate to quantum models [65–70] which are still focused on a particular appli cation. To advance the quantum approaches [53,71], we complement it using the artefact—OERM—supported by ML. This helps to eliminate the order effect quickly. Further, we use five large datasets with different expectancies of the order effect to increase generalizability. Therefore, OERM contributes to quantum probability theory by enabling an auto mated tool to detect and eliminate order effects in interdisciplinary

settings.

## 3.2. OERM part 1—Detecting the order effect

We execute OERM as follows:

Step 1. We split the document into two parts—A and B—where an automatic classifier independently processes each part.

Step 2. We process the first and second parts of the text and assign a thematic category.<sup>2</sup>

Step 3. These categories attributed to the classifier’s first and second parts of the text are compared with the text category in the original dataset.

Step 4. We apply a naive Bayes classifier<sup>3</sup> [e.g. [72]] on terms and bigrams to both parts of each document in the dataset to classify texts symmetrically, i.e., without any perception caused by the text read earlier. Fig. 4 summarizes the classifier with a standard 10-fold cross-validation [73].

Step 5. To detect the order effect, we calculate the value of R by sum marizing the numbers of correctly defined categories in the left part (N(A)) and in the right part (N(B)).<sup>4</sup>

Step 6. We subsequently divide R by the 10-fold number of documents in the corpus. $^ 5 \mathrm { { N } _ { \mathrm { { t o t a l } } } }$ is the number of records in the dataset. For each corpus, the following formula is applied:

$$
R ^ {\prime} = (N (A) + N (B)) / \left(N _ {\text { total }} * 1 0\right)
$$

Step 7. Each document with the order effect satisfies two conditions: a. Our classifier assigned the same category for the left (A) or the right (B) part

b. The categories defined for A and B parts are different.

For further calculations, we keep only documents with order effects.

Step 8. We assign the category of each document based on the category of only part A or part B.

Step 9. We calculate the determination frequency as the fraction of documents with correct classification on the A or B part as follows:

$$
f (A) = N (A) / (N (A) + N (B)),
$$

$$
f (B) = N (B) / (N (A) + N (B)).
$$

If both values f (A) and f (B) are near 0.5, the order effect is absent in that corpus of documents; otherwise the order effect exists.

## 3.3. OERM part 2—Eliminating the order effect

We cannot change human biases, however, we can identify where such biases occur in training datasets and enable ML tools to eliminate the order effect. To enable automated decision-making systems that do not inherit human biases, we propose the second part of OERM to remove the order effect and train decision making systems. This has been shown diagrammatically in Fig. 5.

![](/api/attachments/64WDNFPH/fulltext/images/aff90695b3143fe3dccf0b59fb32574de2c4eb64c0577c2bffbbc7e5acc11807.jpg)  
Fig. 2. Design science research methodology.

![](/api/attachments/64WDNFPH/fulltext/images/1571a975e527a2c6557d6eced53c17402e9452b1a4f4c2c4c8a4f8e4193afbef.jpg)  
Fig. 3. The model of the order effect for document classification.

## 3.4. Datasets with different expectancies of the order effect

Many recent studies in AI/ML stress the need to use pre-established datasets to ensure the robustness and validity of models [74,75]. We focus on a range of datasets: fully manually labelled,<sup>6</sup> party manually labelled, and fully automatically labelled. The order effect is expected in all datasets, which include manually assigned categories for documents and will found by the prevalence of the first part topic. For example, if the first part of the document is about topic in A, and the second is about topic in B, topic in A will be selected as the category for the whole document. The corpora used in the study are summarized in Table 2.

• Reuters [76] is a benchmark dataset for news document classifica tion, containing \~8000 training documents and \~ 3000 testing documents, grouped into 90 classes. Due to manual classification, we expect to find a strong order effect in this dataset.

• The dataset of Physical Review Letters, Physical Review, and Reviews of Modern Physics (PhysRev) [77] comprises approximately 450,000 papers dating back to 1893. To predict the order effects in this dataset, we analyzed submission and review process described in Physical Review. Authors indicate several keywords at the submis sion stage. Later, Physical Review provides its own internal key words classifier, which defines suitable variants of publication placing. Thus, editors get a perception of the paper’s topic. Bearing in

![](/api/attachments/64WDNFPH/fulltext/images/f250e1a4776f7aa7a41303ce62704bb565f8d2112ccdca3023df4c57085afbf3.jpg)  
Fig. 4. Flowchart of the naïve Bayes decision tree algorithm

![](/api/attachments/64WDNFPH/fulltext/images/82fb8835e5f6ef099a7ae8096af88fcaba8f63f8afac896e1c5867259af8bb2a.jpg)  
Fig. 5. Flowchart of the OERM decision tree algorithm to remove order effects.

mind this thematic cutoff, editors read the abstract and finally select the appropriate volume. We took the document names and the ab stract publishers’ abstract categories (e.g., the Physical Review A, B, $\mathrm { C } , \mathrm { D } ,$ and E journal collections). If the order effect occurs, some ab stracts from PhysRev papers could have been assigned to the thematic category of the publisher based on the first part of the text. Since some documents have been automatically classified, we expect to find a moderate order effect in this dataset.

• 20 Newsgroups (20NG) [78] is a collection of \~18,000 news grouped into 20 categories when creating the documents. Since no manual classification was done after the report was published, we expect to find no order effect in this dataset.

Table 2  
Description of datasets used in the study.

<table><tr><td>Dataset</td><td>Type</td><td>Pre-processing of dataset</td><td>Expected the older effect</td><td>Created by us</td></tr><tr><td>Reuters</td><td>news</td><td>yes, manual</td><td>high</td><td>no</td></tr><tr><td>PhysRev</td><td>scientific papers</td><td>yes, manual and automated</td><td>moderate</td><td> $no^a$ </td></tr><tr><td>20NG</td><td>news</td><td>no</td><td>low</td><td>no</td></tr></table>

<sup>a</sup> This dataset is available for testing purpose.

• ScopusAbstracts is a dataset of 5583 abstracts we created by randomly downloading paper abstracts from Scopus on a specific topic (biomedicine and cell physiology) from several publishers. As the dataset was constructed without any preliminary screening, we expect to find no order effect in this dataset.

• ISAbstracts is a dataset of 2825 abstracts we created by randomly downloading paper abstracts from Scopus on a specific topic (in formation systems).<sup>7</sup> The division of the dataset into categories (Artificial, Big Data, Cloud, engineering, ERP, Government, Network) was made automatically based on the existence of one keyword in text and on the non-existence of others. As the dataset was constructed without any preliminary screening, we expect to find no order effect in this dataset.

All documents shorter than 100 symbols were skipped to increase classification reliability. We also eliminated stop words such as “the”, “is” and “and” from the training model, allowing applications to focus on the important words. As a result, we derived 7869 documents from Reuters, 10,035 documents from PhysRev, 18,631 documents from 20NG, 5583 documents from ScopusAbstracts, and 2825 documents from ISAbstracts, which we believe is sufficient for the estimation of the order effect in each corpus by splitting each corpus into multiple parts ac cording to our experimental design. Finally, we perform data cleaning for each dataset by deleting all digits, punctuation marks, and unique signs, normalizing token space sequences to single spaces and convert ing the resulting text string to lowercase. As per previous studies in this field, we train our classifier on 10% of the dataset (training subset) and classify it using the remaining 90% (testing subset). We choose word bigrams<sup>8</sup> as the simplest sequential lexical unit of text, which are unique for the document to have a meaningful dependency in the current dataset.

## 4. Evaluation

All five datasets differ by volume and number of categories; there fore, the classification precision will vary. There were seven reasons why we selected naïve Bayes (NB):

1. NB provided guaranteed symmetry in the classification of different text parts (human bias implies asymmetry).

2. NB supports bigrams as the simplest, relatively unique, sequential lexical unit of text.

3. For NB, the significance of a bigram does not depend on its location.

4. NB can calculate the aggregated significance of a bigram in the left and right parts of the text and divide the text in order to equalize the thematic distribution.

5. NB has a speed of execution.

6. NB is easy to implement.

7. NB has low code complexity.

Naïve Bayes is well-known for its simplicity and symmetry, but as a classification method, it is not the most accurate, which results in higher dispersion across datasets. Nevertheless, we can still detect the order effect even with this relatively low precision. The reason is that even if the automated classification is not perfect, it makes all errors with a similar probability. However, as human bias implies asymmetry, when we compare the automated classification results with the human clas sification, we see that humans make more mistakes in the second part of the text. As a result, we obtained a high average precision for all data sets, except for 20NG (56%). In this dataset, there are more categories than in other datasets (20), and the texts are quite short, i.e., a random classifier would only be successful in 5% of cases; therefore, the classi ficatory precision for this dataset is lower, see Table 3.

As defined in Section 3.2, we measure the prevalence of the order effect as a fraction of texts (R) that are wrongly classified. Therefore, we calculate R as 0.12 for Reuters, 0.15 for PhysRev, 0.27 for 20NG, 0.08 for ScopusAbstracts and 0.07 for ISAbstracts (see Table 4).<sup>9</sup> These are the documents that have been classified differently by the A and B parts of the same document.

For example, the order effect varies dramatically between two similar datasets, i.e., collections of news materials from the absent order effect (20NG) to the powerful order effect (Reuters). In contrast to Reuters, composed manually, 20NG does not use manual classifica tion. Therefore, we assumed there should have been no order effect for the latter, and we needed to get f(A) close to 0.5 to confirm this assumption. Indeed, during the evaluation, we saw that the values f(A) and f(B) for 20NG are 0.51 and 0.48, respectively, indicating a negligible order effect in the 20NG dataset that could be approximated for 20NG being equal. Therefore, we confirm the absence of order effect for 20NG. Thus, the manual classification process in Reuter’s corpus is the main reason the order effect manifests there, see Table 4.

Although splitting the documents in the middle could detect the order effect for the manual classification datasets, like Reuters, what if the order effect also manifests for the automated classification? One of the reasons might be the writing style, where humans write texts in a manner where most information is concentrated in one part of the document. For example, comparing news materials and scientific article abstracts, the first half of abstracts use more thematic words than the second. Nothing but the abstract text distinguishes them from news, where a thematic lexicon is distributed uniformly across the whole text.

## Table 3

Precision of the classifier

<table><tr><td rowspan="2">Dataset</td><td colspan="3">Precision, %</td></tr><tr><td>min</td><td>max</td><td>average</td></tr><tr><td>Reuters</td><td>83.1%</td><td>85.9%</td><td>84.2%</td></tr><tr><td>PhysRev</td><td>83.7%</td><td>85.3%</td><td>84.7%</td></tr><tr><td>20NG</td><td>54.0%</td><td>59.6%</td><td>56.7%</td></tr><tr><td>ScopusAbstracts</td><td>65.2%</td><td>66.1%</td><td>65.7%</td></tr><tr><td>ISAbstracts</td><td>77.2%</td><td>83.5%</td><td>80.4%</td></tr></table>

## Table 4

Numbers and frequencies of correct classifications by the A and B parts of the text.

<table><tr><td>Dataset</td><td> $N_{total}$ </td><td>N (A)</td><td>N (B)</td><td>f (A)</td><td>f (B)</td><td>SD</td></tr><tr><td>Reuters</td><td>7869</td><td>7163</td><td>2248</td><td>0.761</td><td>0.239</td><td>0.013</td></tr><tr><td>PhysRev</td><td>10,035</td><td>9456</td><td>6009</td><td>0.611</td><td>0.389</td><td>0.010</td></tr><tr><td>20NG</td><td>18,631</td><td>25,536</td><td>24,263</td><td>0.513</td><td>0.487</td><td>0.006</td></tr><tr><td>Scopus Abstracts</td><td>5583</td><td>3048</td><td>1696</td><td>0.642</td><td>0.358</td><td>0.018</td></tr><tr><td>ISAbstracts</td><td>2825</td><td>1034</td><td>942</td><td>0.523</td><td>0.477</td><td>0.033</td></tr></table>

Therefore, for datasets with automated classification, like ScopusAb stracts, the concentration of information in the first part can explain the order effect. To verify this assumption, we investigate configurable splitting of the document, i.e., how to split documents between two parts to see the content evenly. To do so, we perform a calibration of the A and B part lengths according to writing style and calculate the statistical weight distribution of lexical units (terms and bigrams) over abstract texts.

We calibrate the thematic distribution for both text parts to eliminate the order effect from the ScopusAbstracts dataset. In Fig. 6, we plot the classification frequency of part A [f(A)], depending on the split point’s relative position in the text. This has been performed for all texts of the ScopusAbstracts corpus.

We notice that the order effect vanishes $( \mathrm { i } . \mathrm { e } . , f ( A ) = 0 . 5 )$ at the split position much earlier than the middle of the text: 35% of the text length. However, such a result is still averaged over all training set documents, so there can be quite a difference between summary statistical weights of the A and B parts in each text. Table 5 indicates the classification per formance when the documents in all five databases have been split at the equilibrium point.

If texts are constructed with thematic words shifted toward the beginning, one can expect that the first text half yields more precise classifications than the second. Therefore, the split position must be adjusted to balance the lexicon’s summary statistical weights in both texts. The appropriate split position should be chosen based on the equality of the total statistical weights of lexical units in both parts rather than their lengths.

• For 20NG and Reuters, there are almost no changes in size of the order effect obtained at two different text splits.

o This is because the lexicon difference between the two halves of a news message is negligible, and the statistical weight equilibrium between them is near the middle of the text.

## Table 5

Numbers and frequencies of correct classifications by left and right text parts relative to the equilibrium text split point.

<table><tr><td>Dataset</td><td>N (A)</td><td>N (B)</td><td>f (A)</td><td>f (B)</td><td>SD</td></tr><tr><td>Reuters</td><td>7026</td><td>2312</td><td>0.752</td><td>0.248</td><td>0.013</td></tr><tr><td>PhysRev</td><td>10,373</td><td>6894</td><td>0.601</td><td>0.399</td><td>0.009</td></tr><tr><td>20NG</td><td>25,967</td><td>24,019</td><td>0.519</td><td>0.481</td><td>0.006</td></tr><tr><td>ScopusAbstracts</td><td>2724</td><td>2706</td><td>0.502</td><td>0.498</td><td>0.018</td></tr><tr><td>ISAbstracts</td><td>1013</td><td>958</td><td>0.514</td><td>0.485</td><td>0.014</td></tr></table>

• In PhysRev, a correction of the order effect does not occur.

o It confirms our earlier explanation of the order effect in this dataset due to manual classification.

• For ScopusAbstracts, we confirm our assumption about the absence of order effect due to human bias.

• In ISAbstracts, which was later constructed during the paper revision process, we also notice the better classification quality of the first part of the text. ISAbstracts dataset is similar to Scopus and 20NG—there is no order effect caused by human decision-making.

o Still, a side effect is explained using more expressive vocabulary in the first part of the abstract. It can be almost entirely compensated for by choosing the equilibrium point for text separation.

As a result, the values obtained at the statistical weight equilibrium split are very close to those for two equal parts, despite the substantial variability of the human classification-based order effect from corpus to the corpus. The evaluation suggests we can significantly reduce the order effect by having an appropriate split of documents before classification.

To further investigate this phenomenon, we analyze the statistical weights of the content of the documents in these corpora. First, we normalize the summary statistical weight overall viewed lexical units by 1, where 1 stands for the summary statistical weight of all terms and bigrams in the whole text. Then, we averaged the overall results in the documents for each corpus. We also indicate the splitting position be tween 0 and 1, where the latter indicates the text length. Fig. 7 dem onstrates the difference between the news corpora (20NG and Reuters) and the corpora of article abstracts (PhysRev, ScopusAbstracts and ISAbstracts). For the former, the cumulative statistical weight reveals a consistent linear growth, which proves that an equally significant lexicon can be encountered in any place of a message. However, for the latter, the profiles are slightly convex, with more rapid growth at their beginning and slower growth at the end. This results in half of the

![](/api/attachments/64WDNFPH/fulltext/images/3f0c71fbff789c52459fc0e6ff689a7fa16f054c59ef13f3e867196ad6440d93.jpg)  
Fig. 6. Frequency of correct category determination by part A depending on the split point position.

![](/api/attachments/64WDNFPH/fulltext/images/5684043173542c88593e70b7ef3787314bd5996b7cdf331e27e8d0c3dbb99688.jpg)  
20NGReutersPhysRevScopusAbstracts

Fig. 7. Averaged over the corpora cumulative significance profiles of the left text part relative to the specified text position, 20NG and Reuters overlap

abstract’s statistical weight gained by a minor part of lexical units viewed from the beginning: about 45% for PhysRev and 37% for Ab stracts corpus. This indicates that article abstracts are saturated with a more thematic lexicon in their initial parts.

## 5. Discussion

This paper investigates human bias in categorizing datasets by developing a ML tool to detect and eliminate the order effect. We use inter-disciplinary settings to test the method and eliminate the order effect from the datasets, extending the former approach [53].

## 5.1. Theoretical contribution

Following Wang and Cao [53], who confirmed a quantum-like interference on relevance judgments using a small sample size, we extend this work to a larger scale and apply ML tools to facilitate order effect recognition and removal.

We see that there is a dependency of order effect on the size of the document. We explain it by the existence of a short-term memory, so the time when the reader remembers text. We observe situation when humans have competing hypothesis and thematic assignment, where the first or second is prioritized. To show the oscillations, we analyze this effect taking documents with the various length, measured by the number of words in the document. Fig. 8 shows the dependency of order effect on the length of text. We demonstrate the resulting dependencies on the dataset ScopusAbstracts, for 20 and 5 words for two split-step values. We arrange the dataset by document size (in words) and split all sizes into fixed-step intervals, for document sizes in the same gap this could be less than the split step. The blue line indicates the average fluctuations, when our method flattens the noise.

The dependence of the order effect on text length has a quasioscillating character, which confirms the result obtained in a smaller sample [71]. However, the characteristic period does not retain at the transition to another split step. On the contrary, the oscillation period always has several split steps and typically consists of 2 to 5 values. This indicates that we are mainly dealing with statistical fluctuations and leaps between adjacent split steps. The noisy nature of the oscillations is due to the number of documents in each interval being relatively small. There are too few data in the corpora for such an analysis; each length interval contains only tens of documents or fewer. Thus, currently, only a critical assessment of order effect without subdivision into different length intervals has a practical implication.

![](/api/attachments/64WDNFPH/fulltext/images/99928edaeec39a5eb19879e3b8f0ba298161307ca5fb49664286b8f18ee41cf5.jpg)  
Fig. 8. Dependence of writing-based order effect on document size for Scopus abstracts.

Taken together, we notice the quasi-periodic change of the choice probability of the first part of a topic when we gradually increase the document length. To compensate for this effect, we append several text strings (e.g., 100–150 characters) to change the reaction of the human operator in a cycle. We propose the following model to explain the order effect:

1. When people read an unknown text, quantum interference gradually changes their opinion about its topic, sentence by sentence.

2. The altered perception impacts this unspoken judgment following the sequence of information consumed.

3. The first impression of the document is more critical for its under standing than follow-up interactions with the text.

## 5.2. Lessons learned for IT, businesses, and individuals

We advance managerial knowledge by recommending organizations use OERM to avoid cognitive bias in their decision-making. There are two clear components of these recommendations. First, IT and busi nesses can better understand the order effect and design initiatives to leverage it. Second, individuals should also consider this order effect and be aware of it in their interactions with companies and other individuals.

Companies can use OERM to improve the quality of employee or customer decision-making; ignoring the order effect can lead to mistakes and losses in a company’s business processes. For instance, in the film industry, customer choice is influenced not only by the rating and the price of the movie but also by the position of the movie or series in a list on the website (the primacy effect), which suggests cinemas should install a recommendation system to increase the conversion rate of the online cinema users to consume relevant media products [49]. Furthermore, an effective recruitment strategy for organizations implies detecting the order effect in the perceived attractiveness of job de scriptions and the human resource department making the appropriate adjustments [51].

Using OERM can effectively manage decision-making by imple menting recommendation systems on online platforms and tackling the negative side of the order effect. For example, it can eliminate the pri macy effect in conditions of high workload of employees, who pre dominantly choose the first alternative in documents [14]. Furthermore, such technology can suggest a change in the order of information based on customer requests, eliminating the default order effect, and using it for the company’s benefit [13].

## 6. Conclusions

Machine Learning methods can inform the removal of the order ef fect from human-classified datasets and improve decision-making sys tems. Our approach is the first to enable ML to detect and remove the order effect in real-time. Using five large-scale datasets, our study con tributes to the existing spectrum of works on order effect research. The proposed method detects order effect bias and removes this bias from the dataset.

## 7. Limitations and future work

This study is not without its limitations. There is a need for signifi cantly more extensive data sets to elicit whether the length of a message being analyzed by humans influences the decisions being made. Except for the order effect, the paper fails to answer how to remove other forms of cognitive bias, such as gender and racial biases. Future work should investigate the differences in the meaningfulness of the language used in different scientific domains. Furthermore, we invite more research on the quantum probability theory and, in particular, checking the exis tence of quantum interference. This could further explore the nature of the oscillations of the order effect depending on the size of the document and suggest essential changes to probability theory. As such, we invite the testing of oscillations associated with the multiple changes of the vector of states or the interferences between perceptions of thematic categories. Furthermore, adjusting machine learning to identify gender data gaps in AI training data and further mathematical formalization of other cognitive biases could strengthen the experiments in this paper.

## CRediT author statement

Dmitry Romanov: Conceptualization, Methodology, Data curation, Software, Formal analysis, Investigation

Valentin Molokanov: Methodology, Data curation, Software, Original draft preparation.

Nikolai Kazantsev: Writing- Original draft preparation, Project administration, Visualization, Writing - reviewing & editing.

Ashish Kumar Jha: Writing- Original draft preparation, Writing - reviewing & editing.

Declaration of Competing Interest

All the authors declare that they have no competing or financial interests.

## Data availability

Data will be made available on request.

## Acknowledgement

The authors wish to thank HSE University students for their assis tance in this research: Ekaterina Semenova, Ekaterina Shilova, Daria Davydova, Elina Zaytseva (Edgeeva), and Nikita Pronin. The third author acknowledges the EPSRC funding via ‘Next Stage Digital Econ omy Centre’ and UKRI funding, grant reference EP/T022566/1. The last author acknowledges the support of Science Foundation Ireland research Centre ADAPT through Grant 13/RC/2106\_P2.

## References

[1] J. Dastin, Amazon Scraps Secret AI Recruiting Tool that Showed Bias Against Women. https://www.reuters.com/article/us-amazon-com-jobs-automation-insigh t/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUS KCN1MK08G, 2018 (accessed on: November 10, 20221,2021).

[2] B. Marcus, The Use Of Artificial Intelligence In Business Codifies Gendered Ageism How Do We Fix It?. https://www,forbes.com/sites/bonniemarcus/2021 /10/25/the-use-of-artificial-intelligence-in-business-codifies-gendered-ageism -how-do-we-fix-it/?sh=45d376eeec9c, 2021 (accessed on: November 10, 2021,2021).

[3] B.D. Martino, D. Kumaran, B. Seymour, R.J. Dolan, Frames, biases, and rationa decision-making in the human brain, Science 313 (5787) (2006) 684–687.

[4] J. Shanteau, T.R. Stewart, Why study expert decision making? Some historical

[5] E. Ntoutsi, P. Fafalios, U. Gadiraju, V. Iosifidis, W. Nejdl, M.E. Vidal, S. Ruggieri F. Turini, S. Papadopoulos, E. Krasanakis, I. Kompatsiaris, Bias in data-driven artificial intelligence systems—an introductory survey, Wiley Interdiscip. Rev. : Data Min, Knowl, Discov. 10 (3) (2020) 1356.

[6] A. Rai, Explainable AI: from black box to glass box, J. Acad. Mark. Sci. 48 (1) (2020) 137–141.

[7] S.T. Mueller, R.R. Hoffman, W. Clancey, A. Emrey, G. Klein, Explanation in Human-AI Systems: A Literature Meta-Review. Synopsis of Key Ideas and Publications, and Bibliography for Explainable AI. Arxiy 1902. 2019. p. 01876.

[8] T.K. Das. B.S. Teng, Cognitive biases and strategic decision processes: an integrative perspective, J. Manag. Stud. 36 (6) (1999) 757–778.

[9] S. Highhouse, A. Gallo, Order effects in personnel decision making, Hum. Perform. 10 (1) (1997) 31–46.

[10] S. Zhou, B. Guo, The order effect on online review helpfulness: a social influence

[62] P. Yan, L. Li, D. Zeng, Quantum probability-inspired graph attention network for modeling complex text interaction, Knowl.-Based Syst. 107557 (2021).

## D. Romanov et al.

[11] S. Akter, G. McCarthy, S. Sajib, K. Michael, Y.K. Dwivedi, J. D’Ambra, K.N. Shen, Algorithmic bias in data-driven innovation in the age of AI, Int. J. Inf. Manag. 60 (2021) 1–13.

[12] N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman, A. Galstyan, A survey on BIAS and fairness in machine learning, ACM Comput. Surv. 54 (6) (2021) 1–35.

[13] A. Felfernig, G. Friedrich, B. Gula, M. Hitz, T. Kruggel, G. Leitner, R. Melcher, D. Riepan, S. Strauss, E. Teppan, O. Vitouch, Persuasive Recommendation: Serial Position Effects in Knowledge-Based Recommender Systems, Springer Berlin Heidelberg, Berlin, Heidelberg, 2007, pp. 283–294.

[14] P. Jackson. I. Moulinier. Natural Language Processing for Online Applications: Text Retrieval, Extraction and Categorization, John Benjamins Publishing, 2007.

[15] L. Kung, D. Hall, H.-J. Kung, De-bias Techniques and Cognitive Ability in Decision-Making, 2022.

[16] T. Kliegr, S. <sup>ˇ</sup> Bahník, J. Fürnkranz, A review of possible effects of cognitive biases on interpretation of rule-based machine learning models, Artif. Intell. 295 (2021), 103458.

[17] Y.R. Shrestha, S.M. Ben-Menahem, G. von Krogh, Organizational decision-making structures in the age of artificial intelligence, Calif. Manag. Rev. 61 (4) (2019) 66–83.

[18] C. Moreira, Y.L. Chou, M. Velmurugan, C. Ouyang, R. Sindhgatta, P. Bruza, LINDA-BN: an interpretable probabilistic approach for demystifying black-box predictive models, Decis. Support. Syst. 113561 (2021).

[19] E. Hunt, Tay, Microsoft’s AI chatbot, gets a crash course in racism from Twitter, in: The Guardian, 2016.

[20] K. Coussement, D.F. Benoit, Interpretable data science for decision making, Decis. Support. Syst. 150 (2021) 1–6.

[21] K.R. Chinander, M.E. Schweitzer, The input bias: the misuse of input information in judgments of outcomes, Organ. Behav. Hum. Decis. Process. 91 (2) (2003) 243–253.

[22] A. Arad, Past decisions do affect future choices: an experimental demonstration, Organ, Behav, Hum, Decis, Process, 121 (2) (2013) 267–277.

[23] C. Li, Primacy effect or recency effect? A long-term memory test of Super Bowl commercials, J. Consum. Behav. 9 (1) (2010) 32–44.

[24] D. Joshi, The primacy effect impact of information’s order on investors perception, Int. J. Res. Commer. Manag. 5 (6) (2014) 46–48.

[25] V.A. Stone, A primacy effect in decision-making by jurors, J. Commun. 19 (3) (1969) 239–247.

[26] E. Chen, G. Simonovits, J.A. Krosnick, J. Pasek, The impact of candidate name order on election outcomes in North Dakota, Elect. Stud. 35 (2014) 115–122.

[27] D. Grant, The ballot order effect is huge: evidence from Texas, Public Choice 172 (3) (2017) 421–442.

[28] A. Serenko. N. Bontis. First in. best dressed: the presence of order-effect bias in journal ranking survevs, J. Informetrics 7 (1) (2013) 138–144.

[29] S.G. McFarland, Effects of question order on survey responses, Public Opin. Q. 45 (2) (1981) 208–215.

[30] C.P. Haugtvedt, D.T. Wegener, Message order effects in persuasion: an attitude strength perspective, J. Consum. Res. 21 (1) (1994) 205–218.

[31] A. Rey, K. Le Goff, M. Abadie, P. Courrieu, The primacy order effect in complex decision making, Psychol. Res. 84 (6) (2020) 1739–1748.

[32] H. Oppewal, T. Huybers, G.I. Crouch, Tourist destination and experience choice: a choice experimental analysis of decision sequence effects, Tour. Manag. 48 (2015) 467-476.

[33] A.E. Schlosser, What are my chances? An imagery versus discursive processing approach to understanding ratio-bias effects, Organ. Behav. Hum. Decis. Process. 144 (2018) 112–124.

[34] G.R. Bergus, I.P. Levin, A.S. Elstein, Presenting risks and benefits to patients, J. Gen. Intern. Med. 17 (8) (2002) 612–617.

[35] I C Theis K Yankova M Fulerich Information order effects in the context of management commentary—initial experimental evidence, J. Manag. Control. 23 (2) (2012) 133–150

[36] R. Pieters, H. Baumgartner, R. Bagozzi, Biased memory for prior decision making: evidence from a longitudinal field study, Organ. Behav. Hum. Decis. Process. 99 (1) (2006) 34–48.

[37] D. Dickey, C. Pearson, Recency effect in college student course evaluations, Pract. Assess. Res. Eval. 10 (6) (2005) 1–10.

[38] A. Guiral-Contreras, J.A. Gonzalo-Angulo, W. Rodgers, Information content and recency effect of the audit report in loan rating decisions, Account. Finance 47 (2) (2007) 285–304.

[39] E. Sumner, E. DeAngelis, M. Hyatt, N. Goodman, C. Kidd, Cake or broccoli? Recency biases children's verbal responses, PLoS One 14 (6) (2019), e0217207

[40] G.R. Bergus. G.B. Chapman. B.T. Leyy. J.W. Ely. R.A. Oppliger, Clinical diagnosis and the order of information, Med. Decis. Mak. 18 (4) (1998) 412–417.

[41] N. Bansback, L.C. Li, L. Lynd, S. Bryan, Exploiting order effects to improve the quality of decisions, Patient Educ, Couns, 96 (2) (2014) 197–203.

[42] K. Sohn, Understanding the order effect in eliciting risk aversion. Financ. Res. Lett 30 (2019).314–317

[43] M. Huber, L. Van Boven, A.P. McGraw, L. Johnson-Graham, Whom to help? Immediacy bias in judgments and decisions about humanitarian aid. Organ. Behay Hum, Decis, Process, 115 (2) (2011) 283–293.

[44] M.L. Clemmensen, P. Borlund. Order effect in interactive information retrieval evaluation: an empirical study, J. Doc. 72 (2) (2016) 194–213.

[45] V. Wilson, M. Srite, E. Loiacono, The effects of item ordering on reproducibility in (2021) 41,

[46] A.R. Camilleri, The importance of online reviews depends on when they are presented, Decis. Support. Syst. 133 (2020) 1–11.

[47] M. Chau, W. Li, B. Yang, A.J. Lee, Z. Bao, Incorporating the time-order effect of feedback in online auction markets through a Bayesian updating model, MIS Q. 45 (2) (2021) 985–1005.

[48] S. Tripathi, A.V. Deokar, H. Ajjan, Understanding the order effect of online reviews: a text mining perspective, Inf. Syst. Front. (2021) 1–18. Forthcoming.

[49] Y. Xu, H.-W. Kim, Order effect and vendor inspection in online comparison shopping, J. Retail. 84 (4) (2008) 477–486.

[50] S. Zare, P. Pearce, Order effects and multi-city visits: tour guides’ perspectives, Int. J. Tour, Cities 4 (2) (2018) 194–206.

[51] R. Buda, The interactive effect of message framing, presentation order, and source credibility on recruitment practices, Int. J. Manag. 20 (2) (2003) 156.

[52] I. Seeber, E. Bittner, R. Briggs, T.D. Vreede, G.D. Vreede, A. Elkins, R. Maier, A. Merz, S. Oeste, N. Randrup, G. Schwabe, M. Sollner, Machines as teammates: a research agenda on AI in team collaboration. Inf. Manag, 57 (2) (2020). 103174

[53] Z. Wang, S. Cao, Order effect on relevance judgment: an exploratory study on the detection of quantum interference, Proc. Assoc. Inf. Sci. Technol. 56 (1) (2019) 803-804.

[54] S.T. March, G.F. Smith, Design and natural science research on informatior technology, Decis. Support. Syst. 15 (4) (1995) 251–266.

[55] A.R. Hevner, A three cycle view of design science research, Scand. J. Inf. Syst. 19 (2) (2007) 4.

[56] J. vom Brocke, J. Mendling, Frameworks for business process management: A taxonomy for business process management cases, in: Business Process Management Cases, Springer, 2018, pp. 1–17.

[57] S. Gregor, A.R. Hevner, Positioning and presenting design science research for maximum impact, MIS Q. (2013) 337–355.

[58] S. Gregor, D. Jones, The Anatomy of a Design Theory, Association for Information Systems, (Association for Information Systems, in, 2007.

[59] R. Baskerville, A. Baiyere, S. Gregor, A. Hevner, M. Rossi, Design science research contributions: finding a balance between artifact and theory, J. Assoc. Inf. Syst. 19 (5) (2018) 358–376.

[60] E. Behrends, Introduction to Markov Chains, Springer, 2000.

[61] A.N. Kolmogorov, A.T. Bharucha-Reid, Foundations of the Theory of Probability: Second, English edition, Courier Dover Publications, 2018.

[63] J.S. Trueblood, E.M. Pothos, J.R. Busemeyer, Quantum probability theory as a common framework for reasoning and similarity, Front. Psychol. 5 (322) (2014).

[64] B. Wang, P. Zhang, J. Li, D. Song, Y. Hou, Z. Shang, Exploration of quantum interference in document relevance judgement discrepancy, Entropy 18 (4) (2016) 144.

[65] D. Aerts, Ouantum structure in cognition, J. Math. Psychol, 53 (5) (2009) 314–348.

[66] A.Y. Khrennikov, Ubiquitous Quantum Structure, Springer, 2014.

[67] A. Lambert Mogiliansky, S. Zamir, H. Zwirn, Type indeterminacy: a model of the KT(Kahneman–Tyersky)-man, J. Math. Psychol. 53 (5) (2009) 349–361

[68] E.M. Pothos, J.R. Busemeyer, Can quantum probability provide a new direction for cognitive modeling? Behav. Brain Sci, 36 (3) (2013) 255–274.

[69] Z. Wang, J.R. Busemeyer, A quantum question order model supported by empirical tests of an a priori and precise prediction, Top. Cogn, Sci. 5 (4) (2013) 689–710.

[70] J.M. Yearsley, J.R. Busemeyer, Quantum cognition and decision theories: a tutorial, J. Math. Psychol. 74 (2016) 99–116.

[71] D. Romanov, N. Kazantsev, E. Edgeeva, The Presence of Order-Effect Bias in Moscow Administration, Springer International Publishing, Cham, 2019,

[72] P. Kaviani, S. Dhotre, Short survey on naive baves algorithm, Int. J. Ady. Eng. Res Dev. 4 (11) (2017) 607–611.

[73] D. Berrar, Cross-Validation. Reference Module in Life Sciences, 2018.

[74] D. Veganzones, E. S´everin, An investigation of bankruptcy prediction in imbalanced datasets, Decis. Support. Syst. 112 (2018) 111–124.

[75] A. Andreassen, Y. Bahri, B. Neyshabur, R. Roelofs, The evolution of out-of distribution robustness throughout fine-tuning, Arxiv, 2021.

[76] Reuters, Reuters, 2017.

[77] PhysRev, PhysRev, in: Physical Review Journals, 2019.

[78] 20NG, 20 Newsgroups, 2017.

Dmitry A. Romanov is an Associate Professor at Graduate School of Business / Depart ment of Business Informatics. Professional Interests are natural language processing, social capital. computational modelling. knowledge management. social network analysis. se mantic technologies, ECM. Computer modelling and simulation, artificial intelligence.

Valentin Molokanov, PhD is a senior systems analyst at IQMen Business Intelligence, Moscow from 2014. During 2011–2012 Valentin collaborated with HSE university to develop the text mining engine for a variety of application. Interests of Valentin are: text analytics, search-based applications and machine learning.

Nikolai Kazantsev is a postdoctoral research associate in the Institute for Manufacturing, University of Cambridge. His research interests are related to data-driven business model innovation and the orchestration of nascent ecosystems in manufacturing. Nikolai col laborates with the DIGIT Lab, Initiative in the Digital Economy (INDEX) at the University of Exeter.

Ashish Kumar Jha is an Associate Professor in the field of Business Analytics at Trinity Business School. He is the founding director of M.Sc, in Business Analytics at Trinity Business School. He is the director of Centre of Digital Business and Analytics. His research

revolves around the areas of technology innovation and social media analysis. Ashish uses statistical and analytical techniques to understand how firms and consumers interact on social platforms and its effects for both firms and their consumers. His papers have been published in many top journals of the field JMIS, DSS, I&M, IJPE, CAIS among others. He has also presented his work at numerous top conferences of field including ICIS, ECIS among others. Ashish has been a part of research groups working on robotic process automation in IT services industry and holds multiple patents.
