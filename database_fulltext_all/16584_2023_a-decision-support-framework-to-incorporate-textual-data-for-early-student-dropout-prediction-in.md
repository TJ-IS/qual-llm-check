---
otero_id: 16584
otero_key: "XTK43DNK"
title: "A decision support framework to incorporate textual data for early student dropout prediction in higher education"
authors: "Minh Phan; Arno De Caigny; Kristof Coussement"
year: "2023"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2023.113940"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support framework to incorporate textual data for early student dropout prediction in higher education

Minh Phan, Arno de Caigny, Kristof Coussement

## To cite this version:

Minh Phan, Arno de Caigny, Kristof Coussement. A decision support framework to incorporate textual data for early student dropout prediction in higher education. Decision Support Systems, 2023, 168 (C), pp.113940. ⟨10.1016/j.dss.2023.113940⟩. ⟨hal-04274684

HAL Id: hal-04274684 https://hal.science/hal-04274684v1

Submitted on 9 Jul 2025

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L’archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la difusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d’enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

Version of Record: https://www.sciencedirect.com/science/article/pii/S0167923623000155 Manuscript\_dd1b93679e1069ff427e21bcda6044ec

# A Decision Support Framework to Incorporate Textual Data for Early Student Dropout Prediction in Higher Education

Minh Phan<sup>1</sup>, Arno De Caigny<sup>1</sup>, Kristof Coussement<sup>1</sup>

<sup>1</sup> IESEG School of Management, Univ. Lille, CNRS, UMR 9221 - LEM - Lille Economie

Management, F-59000 Lille, France

E-mail addresses: m.phan@ieseg.fr (Minh Phan); a.de-caigny@ieseg.fr (Arno De Caigny);

k.coussement@ieseg.fr (Kristof Coussement)

Corresponding author: Dr. Arno De Caigny, +33 3 20 54 58 92, a.de-caigny@ieseg.fr

# A Decision Support Framework to Incorporate Textual Data for Early Student Dropout Prediction in Higher Education

## Abstract

Managing student dropout in higher education is critical, considering its substantial impacts on students’ lives, academic institutions, and society as a whole. Using predictive modeling can be instrumental for this task, as a means to identify dropouts proactively on the basis of student characteristics and their academic performance. To enhance these predictions, textual student feedback also might be relevant; this article proposes a hybrid decision support framework that combines predictive modeling with student segmentation efforts. A real-life data set from a French higher education institution, containing information of 14,391 students and 62,545 feedback documents, confirms the superior performance of the proposed framework, in terms of the area under the curve and top decile lift, compared with various benchmarks. In contributing to decision support system research, this study (1) proposes a new framework for automatic, data-driven segmentation of students based on textual data; (2) compares multiple text representation methods and confirms that incorporating student textual feedback data improves the predictive performance of student dropout models; and (3) establishes useful insights to help decision-makers anticipate and manage student dropout behaviors.

## Keywords

Decision support framework; Learning analytics; Student dropout prediction; Textual data; doc2vec; Segmentation

## 1. Introduction

Student dropout has been one of the most important topics in education and academic research [1,2]. Along with the development of educational models, this persistent problem becomes more and more diverse. Studies on student dropout, therefore, are also divided into several categories, focusing on different aspects of the problem, such as the levels of education (e.g., primary, secondary, tertiary education, etc.), the studying environments (e.g., on site, online, mixed, etc.), and/or the scale of studying (e.g., course, semester, program, etc.) [3–7]. Dropping out also manifests at different scales, from a single course (including online course) which may need the attention of the teacher, to an entire program leaving more serious consequences. Within this study, we investigate the dropout problems of students for an entire program at tertiary level in higher education institutions (HEIs) since this is the level of education in which dropping out is common, and if it happens, leaves significant impact to learners and stakeholders [8,9]. When students drop out of their HEIs programs, they suffer resource losses, in terms of time, effort, and financial investments [4,8]. Society at large also suffers, because graduation rates tend to influence unemployment rates, income tax contributions, and social activities [10]. The HEIs need to maintain low student dropout rates to ensure high rankings, maintain accreditations, and enhance external perceptions among prospective students [2,11]. Most institutions thus adopt initiatives to provide support for students, such as tutoring services [9]. Yet more than one-quarter of students who start a four-year curriculum do not obtain their degrees [12]. The dropout behaviors also vary depending on the peculiarities of the national education system as well as the quality of the institution’s educational environment [13,14]. Institutions with high international rankings might have low dropout rates compared to others [15].

Beyond supportive initiatives, HEIs also rely on decision support frameworks and predictive modeling to anticipate student dropouts [2]. This modeling task is usually carried out by a binary classification setup that trains machine learning methods to classify new probabilistic student observations in two groups: dropout and non-dropout. This setup relies on historical student data to predict future student dropout probabilities, which decision-makers leverage to undertake a smart,

data-driven selection of which students to target with retention campaigns [16]. The availability of

various rich data sources offers new opportunities for such data-driven decision making. Data often

are classified as structured or unstructured [17], such that structured data can be stored in tabular

formats in a relational database with a clear metadata structure [18,19] (e.g., student demographics,

needs; classroom characteristics; cognitive, academic and behavioral engagement variables). These

data often are numerical [3]. Unstructured data instead do not have a metadata structure and need to

be converted into a structured format before they can be modeled [18,20], such as text, images, audio

or video files. They comprise approximately 80% of data stored in any organization’s databases

For example, HEIs gather substantial textual data from student reviews, feedback, or posts on the schools’ online learning platforms. Such textual student feedback data offer notable promise for student dropout prediction, because in these data, students freely express their opinions of learning processes, facilities, courses, and academic staff. In addition, textual data have proven valuable for other predictive modeling applications, such as those related to customer churn [23], financial risk [24] or even student dropout [25]. High-dimensional representations of textual data capture information that is not available from structured data sources; in this sense, student feedback might improve the performance of existing student dropout prediction models by adding new information. Unstructured textual data even may be particularly well-suited for segmentation efforts to improve predictive performance [26]. Student textual feedback likely can reveal different groups of otherwise similar students, so from a predictive modeling perspective, textual data might be able to uncover latent student groups with potentially different dropout drivers. Despite that, there have not been many research efforts on incorporating unstructured textual data to student dropout predictions and segmentation in higher education contexts. In addition, previous research acknowledges that a segmented approach to student dropout prediction can yield significant improvements in predictive performance. For example, Coussement et al. [3] propose a logit leaf model (LLM), a hybrid algorithm based on decision trees (DT) and logistic regression (LR), in a subscription-based online learning context. The LLM algorithm automatically creates segments of students and can detect segment-specific dropout drivers, so it offers a good balance between predictability and interpretability [27]. However, previous studies tend to rely solely on structured data for segmentation efforts and neglect unstructured data. Therefore, we incorporate textual feedback data into a student dropout prediction application, using text representation and segmentation methods, in an attempt to answer the following research questions:

RQ1. Does incorporating textual feedback data improve student dropout prediction?

RQ2. What insights can be derived from the incorporated textual data to help decisionmakers anticipate and manage student dropout?

To test our proposed approach, we also gather five years of student data from a HEI in France, which span 14,391 students and 62,545 textual feedback documents. In turn, we make three main contributions. First, we propose a new framework for automatic, data-driven segmentation of observations that is based on unstructured, textual data. Second, we introduce unstructured, textual feedback data to student dropout prediction application. Incorporating such data enables us to compare multiple text representation methods and assess their value, relative to structured data. We also validate the performance of a predictive model, based on the proposed framework, using reallife data and in comparison with benchmark approaches. Third, we demonstrate that these unstructured, textual data contain actionable information that can support decision-makers, on the basis of model interpretation and visualization.

## 2. Literature review

We present an overview of peer-reviewed literature between 2009 and 2021 pertaining to student dropout predictions in HEIs that uses predictive modeling approaches in Table 1; it reveals three main aspects that are relevant for our study. First, the input data used thus far to model and predict student dropouts include mostly variables derived from structured data sources, usually the

HEI’s relational database. The two most frequently investigated sets of structured variables are

students’ background information and academic performance. The former category includes

sociodemographic information, such as students’ age, gender, nationality or ethnicity, parents’ jobs,

and whether they require financial aid [2,6,28]. This information is available at the start of students’

academic careers and unlikely to change over time. Kemper et al. [6] report that older (age) and

German (nationality) students tend to drop out more; Mason et al. [28] claim that financial aid

acceptance and amounts (financial aid) and family income levels (parents’ jobs) also increase

dropout likelihood. Gender does not emerge as an important predictor in either study. Variables

related to academic performance, prior to or during current literature, include school performance,

course/program enrollments, grades/GPA, acquired/failed credits, failed courses, number of studying

hours, number of retakes, and class ranking [1,2,29]. Delen et al. [2] find that students whose GPA is

equivalent to an A have an only 7.3% probability of attrition, whereas students who receive an F

average exhibit a much higher probability, of 87.8%. Manrique et al. [29] predict student dropout

with high accuracy and F1 scores, using only their academic performance; Thammasiri et al. [1] find

that GPA, rate of hours earned over hours registered, SAT scores, scholarships, and financial aid are

among the top 10 predictors for dropout prediction. A few studies also creatively incorporate other

sources of structured data, such as when Bayer et al. [30] construct a social graph based on students

discussion boards, and Waheed et al. [31] leverage clickstream data that reflect student interactions

with online learning platforms to identify at-risk students. Unstructured textual data, on the other

hand, have been rarely included for predicting student dropout, despite being available from many

institutions. Zhang et al. [32] develop a data mining system to predict students at-risk of dropping

out which relies on rich sources of educational data. Though, the collected textual data is limited to

descriptions of courses and modules and is not used to predict dropout but only serves as input for a

post-hoc analysis. Jayaraman [25] demonstrates that the dropout behaviors can be predicted with

high accuracy by using solely the student advisors’ text notes. However, this study does not

investigate the possibilities of incorporating textual data with structured data as well as using it to

detect students’ segments.

Second, several predictive modeling algorithms inform student dropout predictions. Our

literature review indicates that LR is the most popular algorithm and achieves robust prediction

performance. According to Delen [33], LR, decision tree (DT), and neural network (NN) can predict

dropouts by students in an unbalanced data set (21.03% dropout) with accuracies between 70% and

80% and recall metrics between 63% and 68%. Thammasiri et al. [1] compare four models: LR, DT,

NN, and support vector machines (SVM), with and without sampling techniques. Recent studies also

investigate the application of more complex machine learning methods. For example, Aulck et al.

[34] show that LR performed equivalently with ensemble methods (random forest [RF] and gradient

boost tree [GBT]) for student attrition prediction. Waheed et al. [31] find that deep learning (DL)

outperforms traditional shallow machine learning models when it includes student clickstream data,

though at a huge cost of additional complexity for the model tuning and deployment. Our literature

review also indicates that most previous work groups students into a single homogeneous cohort

(global), instead of predicting dropout behavior for different groups (segment). To advance decision

support system and learning analytics literature, we thus propose a decision support framework that

allows for the automatic segmentation of students, on the basis of their textual feedback data, before

applying a LR to each segment. We present the details of this framework in Section 3.

Third, the interpretability of prediction models is critical to data science in general [35] and

to decision-makers who seek to manage student dropout in particular [3,6]. But it depends on human

interpretation and cannot be described with a pure mathematical formula. For this study, we define

interpretability as the degree to which humans can understand the decision recommended by the

algorithm [36], and we distinguish global and segment interpretability. The former offers insights

into the model’s predictions over all observations; the latter supports interpretations at the segment

level. A global interpretation can pertain to all types of prediction models, suggesting a capacity to

extract and analyze the model structure and/or internal statistics directly (e.g., coefficients, decision rules), or else use a post hoc method, such as permutation feature importance or the Shapley Additive exPlanations (SHAP) method. In contrast, a segment interpretation should reveal different group characteristics that remain unknown at a global level and that depend on whether the prediction model has the ability to create segments or not [27]. As Table 1 indicates, various studies offer interpretations of their prediction models and offer insights about student dropout drivers. For example, Delen [33] reports the most important variables based on a sensitivity analysis, and Thammasiri et al. [1] cite feature importance scores for the DT model. Both Mason et al. [28] and Kemper et al. [6] explain dropout behaviors using the beta coefficients of their LR model. In more recent work, Delen et al. [2] propose a Bayesian belief network (BBN) that captures probabilistic interactions and nonlinear relationships between the dependent variable and the independent variables. These studies thus consider a global scope of interpretability; with our decision support framework, we seek to allow for interpretation at the segment level and thereby provide decisionmakers with insights into the rationale for different predictions about different groups of students.

## [INSERT TABLE 1 HERE]

## 3. Methodology

In presenting our hybrid decision support framework, to incorporate textual data into predictive modeling efforts, we start in Section 3.1 by introducing the framework used to predict student dropout (Figure 1), which leverages both structured and unstructured textual data. Section 3.2 describes the representation methods we propose to handle unstructured textual data. Then in Sections 3.3 and 3.4, we describe the methodological building blocks for our framework.

## 3.1. Framework to incorporate textual data

As Figure 1 reveals, the proposed framework contains two stages: segmentation and modeling. Its input is data about the set of all students $D T = ( X ^ { S } , X ^ { U } , Y )$ , which includes structured data <sup></sup>, unstructured textual data <sup></sup>, and binary student dropout status 	. The unstructured textual $X ^ { S }$ $X ^ { U }$ data $X ^ { U }$ are processed through a text pre-processing pipeline and transformed into a structured format, according to a text representation method. In the first, segmentation stage, we create homogeneous segments of students on the basis of the transformed textual data. That is, we specifically use unstructured, textual data to construct student segments and maximize interpretability, while avoiding issues associated with using mixed data for distance-based segmentation [37]. The transformed textual data serve as input for a segmentation algorithm to create  homogeneous segments; on the basis of these created segments, we can divide the processed, structured data and transformed textual data into  subsets, $D T _ { k \in [ 1 . . K ] } = ( X _ { k } ^ { S } , X _ { k } ^ { U } , Y _ { k } )$

In the second, classification stage, we train models for each segment separately. For each subset $D T _ { k \in [ 1 . . K ] } ,$ the structured data $X _ { k } ^ { S }$ and transformed textual data $X _ { k } ^ { U }$ get combined and serve to train a predictive model that can produce segment-specific dropout probabilities. The output of this stage is a unique predictive model for every student segment.

The selection of methods for the two stages of the proposed decision support framework can be flexible, but for this study, we use vector space, doc2vec and BERT for text representation, and kmeans and hierarchical clustering algorithms for clustering. Then in the modeling stage, we prefer LR, due to its good prior performance and interpretability. We provide more information about these selected methods in Sections 3.2–3.4.

## [INSERT FIGURE 1 HERE]

## 3.2. Text representation methods

We adopt three methods to represent textual data, the vector space approach, the doc2vec approach and the state-of-the-art transformer language model BERT [38–40]. The transformed textual data serve as input to create student segments but also as features to train the dropout prediction model (Figure 1).

## 3.2.1. Vector space

The vector space approach provides a baseline method, reflecting its popularity and strong performance [20,23]. It features two main steps: term-vector weighting and dimension reduction [39,41]. The term-vector weighting method represents each textual feedback document as a numerical vector in a feature space, using weighted term frequencies [39]. This method can represent a collection of feedback using a list of unique terms, as well as identify the most informative terms on the basis of their weights. The weighting vector of each term $t _ { i }$ in the feedback document $d _ { j }$ can be determined by calculating the term frequency $( T F _ { i j } )$ and the inverse document frequency $( I D F _ { i } )$ , in which $i \in [ 1 . . M ]$ where  is the number of unique terms in the feedback document corpus, and $j \in [ 1 . . N ]$ where  is the number of feedback documents. The - values measure the importance of terms in representing the content of a feedback document, while the $I D F$ adjusts the impact of common (rare) terms in the feedback document corpus. The term weight $v _ { i j }$ of the term $t _ { i }$ in the feedback document $d _ { j }$ , therefore, is calculated by multiplying the corresponding $T F _ { i j }$ with the $I D F _ { i }$ values, as in Equation (1):

$$
v _ {i j} = T F _ {i j} * I D F _ {i}.\tag{1}
$$

Thus, a feedback document $d _ { j }$ can be represented by a vector of corresponding term weights ${ \vec { v } } _ { j } =$ $( v _ { 1 j } , v _ { 2 j } , \ldots , v _ { M j } )$ in the feature space, and the collection of all feedback vectors is the $T F - I D F _ { M x N }$ term-feedback document matrix.

In a second step, the term-feedback document matrix, usually high dimensional but sparse, is transformed into a low-dimensional space based on latent semantic indexing (LSI), using a singular value decomposition (SVD) method [41]. Using LSI, based on SVD dimensionality reduction, not only helps reduce noise but also improves predictive performance [42,43]. In detail, LSI anticipates ( latent semantic concepts in the corpus. The term-feedback document matrix gets projected from a high dimensional space to a lower dimensional, semantic latent subspace, because we group the terms into ( distinct concepts. This step relies on a truncated SVD that can decompose the weighted term-document matrix into three distinct matrices:

$$
T F - I D F _ {M x N} \approx U _ {M x l}. \Sigma_ {l x l}. (V _ {N x l}) ^ {T},\tag{2}
$$

where $U _ { M x l }$ and $V _ { N x l }$ are orthogonal matrices, and $\Sigma _ { l x l }$ is a non-negative diagonal matrix. Furthermore, $U _ { M x l }$ and $V _ { N x l }$ represent the relationships of the M-terms and N-feedback documents with the ( latent concepts, respectively, and the diagonal of $\Sigma _ { l x l }$ indicates the importance of the latent semantic concepts in the ( dimensional subspace. Finally, to find the optimal number of ( semantic concepts, we use the profile log-likelihood method proposed by Zhu and Ghodsi [44].

## 3.2.2. doc2vec

The document representation method doc2vec derives directly from the word representation method word2vec [45,46]. word2vec method is a self-supervised framework mapping every word in the vocabulary to a unique vector in the representation vector space so that similar words are located close to each other. This representation model can be trained by two ways, in which, each word either is predicted by the surrounding words (CBOW method) or used to predict other words in the same context (Skip-gram method). By using neural networks with new architectures, word2vec can preserve the linear regularities among words, and is able to capture syntactic and semantic word similarities better than other methods [45]. As a natural extension, doc2vec vectorization, introduced by Le and Mikolov [38], represents a feedback document corpus according to a continuous distributed vector. Previous studies show that it is more robust and accurate in document classification than other baseline methods [38,47,48]. Similar to word2vec, there are two main architectures to train the doc2vec model: a distributed memory model of paragraph vectors (PV-DM) and the distributed bag of words version of the paragraph vector (PV-DBOW).

## 3.2.3. BERT

Bidirectional Encoder Representations from Transformers (BERT) is a transformer-based language model introduced by Devlin et al. [40] in 2018 as a state-of-the-art method in natural language processing research. Unlike vector space and doc2vec, BERT applies a masked language model that enables bidirectional training from text and allows the model to capture deeper sense of the context [40,49]. Like modern language models, a pre-trained model of BERT is available that can be finetuned for different tasks. In this study, we select and compare three common variants of BERT from the TensorFlow Hub, which are the BERT Base (transformer blocks L=12, hidden size of H=768, attention heads A=12), the Small BERT (L=4, H=512, A=8), and the ALBERT (L=12, H=768, A=12).

## 3.3. Segmentation methods

In this study, we test two common unsupervised methods for segmentation, i.e., k-means and hierarchical clustering. On the one hand, k-means segments the input data into  different clusters [50]. These clusters are randomly initialized, then updated in several iterations to minimize the within-cluster variation, as calculated according to the Euclidean distance. On the other hand, hierarchical clustering uses a bottom-up approach in our study and initiates every single input data point as singleton cluster. The algorithm then sequentially merges pairs of clusters that are closest together. Euclidean distance is used to measure the distance between clusters’ centroids [51]. A challenge to using the k-means and hierarchical clustering algorithm is the need to select an optimal and/or reasonable number of clusters (K). However, since segmentation is an integral step in the decision support framework, the optimal number of  segments depends on the predictive performance of the framework, according to a cross-validation setup. We apply segmentation methods only to transformed textual data with the same value range, so it is not necessary to scale the input [50].

Furthermore, the segmented and transformed textual data can be visualized and evaluated using various visualization tools. In this study, we use three most common tools to present the results i.e., principal component analysis (PCA), t-distributed stochastic neighbor embedding (t-SNE) and uniform manifold approximation and projection (UMAP). These visualization tools, although different in methodology, have the same goal to reduce the complexity of the high-dimensional representations of textual data while preserving the most important information to validate the detected segments. PCA is the oldest yet most common dimensional reduction method that linearly transforms the original variables to a new set orthogonal variables (a.k.a. principal components) where the data variance is compressed and stored principally in the first few components. Plotting these first two or three components gives an overview of what the data look like [52,53]. t-SNE is a visualization technique based on stochastic neighbor embedding (SNE) that maps data points, which are described by pairwise dissimilarities, from high-dimensional space to low-dimensional space in a way that preserves local structure. For that reason, t-SNE plots tend to show data clusters thus is very useful in segmentation-oriented applications [54,55]. Lastly, we use the recent dimension reduction and visualization tool: UMAP. This state-of-the-art method constructs two fuzzy topological representations of the data in high and low dimensional spaces, then optimize the data representation in low dimensional space to minimize the cross-entropy between two of them [56,57].

## 3.4. Logistic regression

Logistic regression is one of the most popular classification method in learning analytics [58], and especially for predicting student dropout [59–62]. This popularity arises because (1) the output of LR is interpretable, in that it reveals the linear relationship of a variable with the log-odds of the dependent variable; (2) it provides good and stable prediction results; and (3) it is efficient to train. Furthermore, LR can handle large amounts of structured and unstructured variables with its regularization method, such as the shrinkage Lasso (L1) [63]. This L1 method also acts as a variable selection step, which helps reduce the complexity and increase the stability of the LR model.

## 4. Research procedure

In this section, we detail the research procedure, starting with a description of the real-world data set and a definition of student dropout. After we present the data processing pipeline for structured and unstructured textual data, we describe our experimental setup: timeline for the independent and dependent variables, the 5×3 cross-validation setup, the hyperparameter tuning method, selection process, and data segmentation strategy. Finally, we outline the evaluation metrics.

## 4.1. Data

This study uses real-life data of 14,391 students, provided by a French HEI. The data cover five consecutive academic years, from 2013 to 2018, and refer to both bachelor’s and master’s degree program students. The structured data refer to students’ sociodemographic information, program and course enrollment information, grades, and study status. The unstructured data include their textual feedback about each of their enrolled courses. Students provide this textual feedback at several moments in the academic year, as part of course evaluations. About half of the sample (7,226 students, 50.2%) provided detailed textual feedback, and each student evaluates an average of eight courses.

Student dropout after the first year is a major issue; the first semester is the most intense period for most students [2,64,65]. We identify an early dropout as a student who completely quits school during the second or third semesters of the program. Figure 2 depicts the time window of the experiment, in which the independent period is always the student’s first semester (S1), which starts in the last week of August and ends just before the Christmas holidays in December; the dependent period covers the two next semesters (S2, S3), starting in the following January and lasting until the end of the third semester (next December). The holiday break, between the first and second semester, is a gap period. By using available information in their first semester of the first year at the HEI, we attempt to predict if students will drop out in the second or third semester; during the fiveyear period, 1.2% of all students dropped out.

## [INSERT FIGURE 2 HERE]

## 4.2. Data processing

The data processing involves three steps (Figure 3). First, the raw structured data are extracted from the institution’s database to create a student basetable. These raw data contain information about students’ studying activities, academic performance, and sociodemographics. Aggregated to the student level, they represent the student’s first semester of the first year. Missing values are assigned a value of 0 or mean imputed, depending on the variable. Outliers, or observations that differ significantly from others, are imputed for each variable in the student basetable, using the mean ±3 standard deviations. Finally, any categorical variables get converted to dummy variables.

Second, the raw, unstructured, textual data come from student evaluation forms, completed after every course. We gather the feedback text at the student level, to derive a single document per student. These raw texts are processed, step by step, as in Figure 3. To clean the text, we removed special characters and punctuation, then converted the cleaned text to lowercase and tokenized it on the word level. Part-of-speech tagging (POS), using the Penn Treebank tag set, identifies the grammatical combination, filtered according to informative tokens (i.e., nouns, verbs, adjectives, and adverbs) [66,67]. In this step, stop words and low frequency words, which appear less than 3 times, are dropped. Finally, the cleaned words are stemmed according to a Snowball method [68].

## [INSERT FIGURE 3 HERE]

Third, the tokenized, unstructured, textual feedback data need to be transformed into document vectors. Different methods are available for this step, so we compared the most popular text representation method, being vector space, doc2vec and BERT. The number of dimensions of the embedding vector is based on the cross-validation. Table 2 presents an overview of all variables in the data set.

## [INSERT TABLE 2 HERE]

## 4.3. Experimental setup

The processed, structured data and the transformed, unstructured, textual data then combine to provide the inputs for the experimental setup. Table 3 contains all these setups, listing the groups, indexes, and names of the models; the data from students with (T) or without (NT) textual data; and the two types of data. The unstructured, textual data type, denoted U in Table 3, is only available for the student group with textual data, by definition. The table also reveals the representation method, vector space, doc2vec or BERT method, and k-means or hierarchical clustering segmentation method. By combining those elements, we create 7 models, which we label based on their elements. In turn, we can classify the models into three groups, which we use to assess the implications of incorporating textual data for student dropout predictions. The models in Group 1 reflect the differences between the two student groups, T and NT, which would imply benefits to modeling them separately. Groups 2 and 3 focus on students that provide feedback text T to gauge the value of U data type and the improvement in student dropout prediction if we incorporate this type of data and its segmentation layer.

## [INSERT TABLE 3 HERE]

The models are trained and tuned using 5×3 cross-validation (5×3CV) [23]. It repeats five times on the complete data (5 outer folds), and each outer fold includes three inner folds, for which the data are split into three equal parts for use, sequentially, used as training, validation, and test sets. The validation sets to tune the hyperparameters for the models, for the vector space, doc2vec and BERT methods. The two first representation models need to be trained on the whole text corpus while the last model comes with different pre-trained options, so we select the best hyperparameters/pre-train models according to the one with the highest predictive performance on the validation set for each inner fold of the 5×3CV. For the vector space–based method, the optimal number of ( dimensions of truncated SVD are selected according to the scree plot of the profile loglikelihood, or ( = 606 [44]. For doc2vec, no available method exists to pre-identify the best values for the hyperparameters, so the model needs to be fine-tuned using the 5×3CV. For BERT, we select the best model based on their performance on the validation set of the 5x3 CV. Table 4 contains the list of text representation hyperparameters.

## [INSERT TABLE 4 HERE]

Finally, we evaluate the performance of the student dropout prediction models, using area under the receiver operating characteristic curve (AUC) and top-decile lift (TDL) metrics. The AUC is a common evaluation metric for binary classification and is popular in student dropout prediction literature [2,8,69]. It reflects the probability that the model correctly ranks a randomly selected dropout student as at higher risk than a randomly selected non-dropout student. Then the TDL, another popular evaluation metric for binary prediction models from the business analytics domain [27,70,71], indicates the relative density of students in the top decile; if it exceeds 1, the density of dropout students in the top decile is higher than the density of dropout students in the whole data set, so the model predicts high risk dropout students better than random guessing.

## 5. Results and discussion

In presenting our study results, we actively address the research questions. Section 5.1 pertains to the potential benefits of incorporating unstructured, textual data to predict student dropouts, and Section 5.2 outlines the interpretability of the proposed decision support framework, with extensive visualizations and analyses.

## 5.1. RQ1: Does incorporating textual feedback data benefit student dropout predictions?

To answer RQ1, we consider three sub-questions, step by step, and thus investigate the benefits of using the feedback text as a simple indicator to separate student groups (RQ1a), using only textual feedback data as predictors (RQ1b), and integrating textual feedback data with traditional structured data (RQ1c).

## 5.1.1. RQ1a: Modeling students with and without textual feedback separately

With the models in Group 1, we test for any noticeable difference in dropout prediction between groups of students, based on whether they offer textual data or not. This binary indicator enabled us to create two basic segments, to which we apply four models trained only on structured data. The first, Mod\_FD\_S, is trained with full structured data from both student groups, that is, with and without feedback text. To compare Mod\_FD\_S with other models, we extract predictions based on the test sets of the two different groups of students, with and without feedback text, for which Mod\_FD\_S\_testT and Mod\_FD\_S\_testNT represent two additional variances for each group of students, respectively. Then the second and third models, Mod\_T\_S and Mod\_NT\_S, are trained independently on the structured data from either student group. Finally, Mod\_TNT\_S is a concatenation of Mod\_T\_S and Mod\_NT\_S, which represents a simple segmentation approach for a comparison with the first model. Table 5 summarizes the predictive performance of these models, according to their AUC and TDL; Table 6 provides the results of Wilcoxon signed-rank tests.

## [INSERT TABLES 5 and 6 HERE]

To assess the general effect of modeling student groups with and without textual feedback separately, we compare Mod\_FD\_S with Mod\_TNT\_S. According to Table 5, the average performance of model Mod\_TNT\_S with two student segments (AUC = 0.750, TDL = 3.493) is lower than that of Mod\_FD\_S (AUC = 0.755, TDL = 3.818). The Wilcoxon test in Table 6 instead indicates that these differences are only significant for TDL $( p _ { T D L } < 0 . 1 )$ , not for AUC $( p _ { A U C } >$ 0.1 . When we compare the predictive performance of these two models for each particular group of students, with and without textual feedback, the results in Table 5 further indicate that the models trained with the full structured data, Mod\_FD\_S\_testT $( \mathrm { A U C } ~ = ~ 0 . 7 9 1$ 2 $\mathrm { T D L } ~ = ~ 4 . 2 2 5 )$ and Mod\_FD\_S\_testNT $( \mathrm { A U C } ~ = ~ 0 . 7 0 9$ $\mathrm { T D L } = 3 . 3 0 5 )$ , attain slightly higher AUC and TDL than Mod\_T\_S $( \mathrm { A U C } = 0 . 7 8 4$ $\mathrm { T D L } = 3 . 9 4 7 )$ and Mod\_NT\_S $( \mathrm { A U C } = 0 . 7 0 4$ $\mathrm { T D L } = 3 . 0 4 9 )$ . Only the TDL difference between Mod\_FS\_S\_testNT and Mod\_NT\_S is significant though (Table 6). Therefore, the use of a binary signal to segment students, according to whether they offer textual feedback, does not improve predictions for the respective groups.

## 5.1.2. RQ1b: Information in unstructured, textual data

The preceding findings suggest the need to consider unstructured, textual data. To assess its incorporation, we zoom in on the specific group of students that provide feedback text, T. Table 7 contains the predictive performance results for Group 2, model Mod\_T\_U with three text representation methods corresponding to three sub-models trained only on unstructured, textual data, Mod\_T\_U\_VS, Mod\_T\_U\_DV and Mod\_T\_U\_BERT, which represent the data using the vector space, doc2vec and BERT approaches, respectively. The best method is then selected for model Mod\_T\_U. As a comparison baseline, we also include a random guess model. Table 8 reports the findings of Wilcoxon signed-rank significant tests.

According to the results in Table 7, Mod\_T\_U\_VS (AUC = 0.539, TDL = 1.213), Mod\_T\_U\_DV (AUC = 0.591, TDL = 1.656) and Mod\_T\_U\_BERT (AUC = 0.545, TDL = 1.467) all perform better than random guessing. Comparing the performance in terms of AUC and TDL of these models, we observe that the doc2vec method performs better than the vector space and BERT methods for predicting students at risk. Table 8 confirms that the differences between model Mod\_T\_U (using doc2vec method) and random guessing are significant, so the unstructured, textual data provide valuable information for predicting dropout students $( p < 0 . 0 1 )$ .

## [INSERT TABLES 7 and 8 HERE]

Although these results clearly indicate that there is valuable information in unstructured, textual data, they are not sufficient on their own to build a good predictive model; they should be incorporated with structured data. Considering the evidence that the doc2vec text representation method performs better than vector space and BERT, we focus on doc2vec in our continued analyses.

## 5.1.3. RQ1c: Incorporating unstructured, textual data and its segmentation layer

For this sub-question, we address the most important part of RQ1, namely the benefits of incorporating unstructured, textual data and the segmentation approach. With doc2vec, we build segmented prediction models (for the detailed process, see Section 3.1). Here, we investigate the predictive performance of the models in Group 3, Mod\_T\_SU and Mod\_T\_SU\_SEG, where the first setup integrates both structured and unstructured data, whereas the latter represents the final combination of Mod\_T\_SU with an additional layer of segmentation, on top of the student feedback text. Furthermore, we compare two setups of model Mod\_T\_SU\_SEG using k-means (Mod\_T\_SU\_KM) and hierarchical clustering (Mod\_T\_SU\_HC) method to select the best one. The two relevant models from Group 1 provide a benchmark. We present the results in Table 9 and the pairwise statistical tests for the models in Table 10.

To find the best setup for incorporating unstructured, textual data with structured data, we compare Mod\_T\_SU with its segmented modeling versions Mod\_T\_SU\_KM and Mod\_T\_SU\_HC. As Table 9 shows, the average performance of both Mod\_T\_SU\_KM $( \mathrm { A U C } = 0 . 8 0 1$ $\mathrm { T D L } = 4 . 5 2 4 )$ and Mod\_T\_SU\_HC $( \mathrm { A U C } = 0 . 7 8 8$ $\mathrm { T D L } = 4 . 1 8 8 )$ is better than that of Mod\_T\_SU $( \mathrm { A U C } = 0 . 7 8 4$ $\mathrm { T D L } = 4 . 1 8 1 \rangle$ . Additionally, we find that the model using k-means segmentation method perform better than hierarchical clustering in terms of AUC and TDL. Therefore it is selected as the final method for Mod\_T\_SU\_SEG. Table 10 confirms that the 2.2% increase in AUC and 8.2% improvement in TDL are both significant $( p < 0 . 0 5 )$ . Thus, the unstructured, textual data provide a good segmentation base for improving the performance of the student dropout prediction model.

When we compare the performance of the best model in Group 3 with the models trained only on structured data in Group 1, we specify the benefits of incorporating unstructured, textual data. According to Tables 9 and 10, Mod\_T\_SU\_SEG using k-means method $( \mathrm { A U C } = 0 . 8 0 1 , \mathrm { T D L } =$ 4.524) outperforms the baseline model Mod\_T\_S (AUC = 0.784, TDL = 3.947) for both AUC $( p =$ 0.022) and TDL $( p = 0 . 0 6 2 )$ ). Moreover, Mod\_T\_SU\_SEG, trained only on the specific group of students with feedback text (about half of them), performs even better than Mod\_FD\_S\_testT (AUC $= 0 . 7 9 1$ , TDL = 4.225), which is trained on all students. The difference is significant for TDL $( p _ { T D L } < 0 . 1 )$

## [INSERT TABLES 9 and 10 HERE]

In summary, three sub-questions, RQ1a–1c, together inform RQ1. As we find by testing RQ1a, simply using the information that a student gives feedback, as a binary indicator, is not enough to improve student dropout predictions, and more advanced incorporation techniques are needed. With RQ1b and RQ1c, we confirm that there is valuable information in the unstructured, textual feedback data, which can create meaningful student segments and significantly improve the predictive performance of the dropout application. In conclusion, the student dropout prediction application works better for students who provide feedback text, and institutions and academic decision-makers should collect and incorporate more unstructured, textual data from students.

5.2. RQ2: What insights can be derived from the incorporated textual data to help decision-makers better understand and manage student dropout?

To help decision-makers understand different dropout drivers per student group and develop more personalized different retention strategies, we focus the best modeling model approach, Mod\_T\_SU\_SEG, which uses a doc2vec text representation method and k-means segmentation algorithm. The results of the model come from the first fold of the 5×3CV. Then, to evaluate and interpret the incorporated textual data for each student, we use four visualization tools and expert labeling. First, we construct a visualization based on the vectors of the doc2vec transformed text to evaluate the separation of the student segments [54]. Second, to extract segment-level insights, we set up an expert labeling task, in which three independent experts assign the top bigram words of each student segment to four categories that reflect different feedback dimensions: student, teacher, course, and facility. The final assignment of each bigram reflects a majority vote and agreement among the three experts, which we confirm with an interrater reliability (IRR) analysis based on Fleiss’s Kappa index [72,73]. According to the IRR, the experts achieve strong agreement, with $k a p p a > 0 . 9 , p < 0 . 0 0 1$ , for both student segments.

For the selected CV fold, the k-means algorithm and doc2vec methods create two segments of students. Figure 4 shows the transformed feedback text for each student segment, reduced to two dimensions using PCA, t-SNE, t-SNE with PCA as input, and UMAP techniques. The low dimension version appears together with the student segment labels, according to these twodimensional scatter plots. This visualization clearly reveals that the two student groups can be well segmented, with very little overlap. Therefore, the segmentation algorithm in the proposed decision support framework successfully detects two meaningful student groups in the data.

## [INSERT FIGURES 6 and 7 HERE]

Figure 5 presents the profiles of the two student segments. The top 100 bigrams of each segment are extracted and labeled, according to student, teacher, course, and facility categories. Then for each student segment, we calculate the percentage difference in bigrams per category, relative to the overall percentage of two segments in the same category. Thus, we determine which topics students describe relatively more in each segment, compared with all students on average. According to Figure 5, students in segment 1 care more about teachers (2.43% above average), student life (0.65% above average), and school facilities (0.56% above average) but less about courses (3.65% below average). The interests of the students in segment 2 reflect the opposite trends, such that they talk more about the courses (3.65% above average) but less about the teachers, student life, or school facilities (2.43%, 0.65% and 0.56% below average, respectively).

As a further assessment of student segments, we analyze the variables in the LR models to derive the importance of each variable group per student segment (see Figure 6). For this calculation, we multiple the coefficient of the LR model and the standard deviation of the corresponding input variable, then take the absolute value. Summing these importance values of the group and dividing by total importance provides the percentage of variable importance per group. According to Figure 6, students in segment 1 exhibit higher dropout percentages (1.9%) than those in the second segment (0.8%). In student segment 1, information related to course enrollment (46%) and feedback text (17%) contribute more to dropout predictions than this information does for student segment 2 (43% and 14%, respectively). Sociodemographic information indicates opposite effects.

## [INSERT FIGURE 6 HERE]

Finally, in Figure 7 we present the coefficients of the LR model for structured data for each segment of students. Using the findings we have gathered thus far, we can derive a full picture of dropped out students and strategies for communicating with them. The students at risk in segment 1 mostly study on the Paris campus; have changed their address at least once; enrolled in the course categories ACC, ECO, LAN, LAW, or QMS in their first semester (see Figure 7 for the full names of each category); and provide feedback mostly about teachers, student life, and facilities. Students at risk in segment 2 instead are mostly international students; enrolled in the course categories ACC, MIS, QMS, STR, or RES in the first semester; and share a tendency to offer feedback about courses. Therefore, the HEI should identify students with these profiles and learn what difficulties they face, on the basis of their feedback, before initiating an intervention.

## [INSERT FIGURE 7 HERE]

## 6. Conclusions

This study proposes a new decision support framework to incorporate both structured and unstructured, textual data and thereby improve student dropout applications, in terms of both their predictive performance and their interpretation. Applying this framework to a real-life data set, obtained from of a French HEI, reveals that textual feedback data contain valuable information that can be used to detect at-risk students. By integrating these data, we significantly improve the predictive performance of the student dropout prediction model. Moreover, unstructured, textual data can be leveraged to create meaningful student segments. The proposed approach outperforms existing methods, in terms of predictive performance, and successfully identifies student segments that require distinct predictive models. From an interpretability perspective, because it can analyze student segments, our proposed method offers informative insights about student concerns and communication habits. These findings can be used to design and adapt interactions with different groups of students.

This study extends research that identifies segmented modeling approaches to improve predictive performance and interpretability in predictive modeling tasks [3,27]. By adding another layer of student segments, we significantly improve the predictive performance of the model. Building segmentation on unstructured, textual information reveals informative segments, which provide clearer understanding of heterogeneity in the data set. In turn, our segmentation approach suggests avenues for further research related to decision support system and learning analytics. First, our approach might be applied to detect student segments using other textual data, such as student submission files, communications on a course page, or student questions shared by email. Second, we test our framework with a unique, real-world data set, but additional tests with different sets of data would help validate its general performance in other settings. Third, the choice of components to include in the framework is flexible. We rely on a set of proven and SOTA methods, but future research can also test and compare between other text representation, segmentation, and predictive modeling methods.

## REFERENCES

[1] D. Thammasiri, D. Delen, P. Meesad, N. Kasap, A critical assessment of imbalanced class distribution problem: The case of predicting freshmen student attrition, Expert Syst. Appl. 41 (2014) 321–330.

[2] D. Delen, K. Topuz, E. Eryarsoy, Development of a Bayesian Belief Network-based DSS for predicting and understanding freshmen student attrition, Eur. J. Oper. Res. 281 (2020) 575– 587.

[3] K. Coussement, M. Phan, A. De Caigny, D.F. Benoit, A. Raes, Predicting student dropout in subscription-based online learning environments: The beneficial impact of the logit leaf model, Decis. Support Syst. (2020).

[4] N. Raisman, The cost of college attrition at four-year colleges & universities-an analysis of 1669 US institutions, Policy Perspect. (2013).

[5] S. Jiang, A.E. Williams, K. Schenke, M. Warschauer, D.O. Dowd, Predicting MOOC

Performance with Week 1 Behavior, in: Proc. 7th Int. Conf. Educ. Data Min., 2014: pp. 273– 275.

[6] L. Kemper, G. Vorhoff, B.U. Wigger, Predicting student dropout: A machine learning approach, Eur. J. High. Educ. 10 (2020) 28–47.

[7] G.W. Dekker, M. Pechenizkiy, J.M. Vleeshouwers, Predicting Students Drop Out: A Case Study., Int. Work. Gr. Educ. Data Min. (2009).

[8] D. Olaya, J. Vásquez, S. Maldonado, J. Miranda, W. Verbeke, Uplift Modeling for preventing student dropout in higher education, Decis. Support Syst. (2020) 113320.

[9] S. Maldonado, J. Miranda, D. Olaya, J. Vásquez, W. Verbeke, Redefining profit metrics for boosting student retention in higher education, Decis. Support Syst. 143 (2021) 113493.

[10] N. Sutter, S. Paulson, Predicting college students’ intention to graduate: a test of the theory of planned behavior, Coll. Stud. J. 50 (2017) 409–421.

[11] J. Vásquez, J. Miranda, Student desertion: What is and how can it be detected on time?, in: Data Sci. Digit. Bus., 2019.

[12] J.M. Braxton, a. S. Hirshy, Theoretical developments in the study of college student departure, Coll. Student Retent. Formula Student Success. (2005).

[13] A. Behr, M. Giese, H.D. Teguim Kamdjou, K. Theune, Dropping out of university: a literature review, Rev. Educ. 8 (2020) 614–652.

[14] OECD, Education at a Glance 2008, 2008.

[15] R. Mantle, Non-continuation: UK Performance Indicators 2017/18, High. Educ. Stat. Agency. (2019).

[16] D. Delen, A comparative analysis of machine learning techniques for student retention management, Decis. Support Syst. 49 (2010) 498–506.

[17] M. Arenas, R. Hull, W. Marten, T. Milo, T. Schwentick, Foundations of data management (Dagstuhl perspectives workshop 16151), in: Dagstuhl Reports, 2016.

[18] C.C. Shilakes, J. Tylman, Enterprise Information Portals, Merrill Lynch, Inc., New York, NY. (1998).

[19] H. Baars, H.-G. Kemper, Management support with structured and unstructured data—an integrated business intelligence framework, Inf. Syst. Manag. 25 (2008) 132–148.

[20] K. Coussement, D. Van den Poel, Improving customer complaint management by automatic email classification using linguistic style features as predictors, Decis. Support Syst. 44 (2008) 870–882.

[21] A. Gandomi, M. Haider, Beyond the hype: Big data concepts, methods, and analytics, Int. J. Inf. Manage. 35 (2015) 137–144.

[22] C.C. Shilakes, Enterprise information portals, Merrill Lynch In-Depth Rep. (1998).

[23] A. De Caigny, K. Coussement, K.W. De Bock, S. Lessmann, Incorporating textual information in customer churn prediction models based on a convolutional neural network, Int. J. Forecast. (2019).

[24] M.F. Tsai, C.J. Wang, On the risk prediction and analysis of soft information in finance reports, Eur. J. Oper. Res. (2017).

[25] J.D. Jayaraman, Predicting Student Dropout by Mining Advisor Notes, in: Proc. 13th Int. Conf. Educ. Data Min. (EDM 2020), 2020: pp. 629–632.

[26] N.N.Y. Vo, S. Liu, X. Li, G. Xu, Leveraging unstructured call log data for customer churn prediction, Knowledge-Based Syst. 212 (2021) 106586.

[27] A. De Caigny, K. Coussement, K.W. De Bock, A new hybrid classification algorithm for customer churn prediction based on logistic regression and decision trees, Eur. J. Oper. Res. 269 (2018) 760–772.

[28] C. Mason, J. Twomey, D. Wright, L. Whitman, Predicting engineering student attrition risk using a probabilistic neural network and comparing results with a backpropagation neural network and logistic regression, Res. High. Educ. 59 (2018) 382–400.

[29] R. Manrique, B.P. Nunes, O. Marino, M.A. Casanova, T. Nurmikko-Fuller, An analysis of student representation, representative features and classification algorithms to predict degree

dropout, in: Proc. 9th Int. Conf. Learn. Anal. Knowl., 2019: pp. 401–410.

[30] J. Bayer, H. Bydzovská, J. Géryk, T. Obsivac, L. Popelinsky, Predicting Drop-Out from Social Behaviour of Students, Int. Educ. Data Min. Soc. (2012).

[31] H. Waheed, S.-U. Hassan, N.R. Aljohani, J. Hardman, S. Alelyani, R. Nawaz, Predicting academic performance of students from VLE big data using deep learning models, Comput. Human Behav. 104 (2020) 106189.

[32] Y. Zhang, S. Oussena, T. Clark, H. Kim, Use Data Mining to Improve Student Retention in Higher Education-A Case Study., in: ICEIS (1), 2010: pp. 190–197.

[33] D. Delen, Predicting student attrition with data mining methods, J. Coll. Student Retent. Res. Theory Pract. 13 (2011) 17–35.

[34] L. Aulck, D. Nambi, N. Velagapudi, J. Blumenstock, J. West, Mining University Registrar Records to Predict First-Year Undergraduate Attrition., Int. Educ. Data Min. Soc. (2019).

[35] M.T. Ribeiro, S. Singh, C. Guestrin, “Why should i trust you?” Explaining the predictions of any classifier, in: Proc. ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., 2016.

[36] T. Miller, Explanation in artificial intelligence: Insights from the social sciences, Artif. Intell. (2019).

[37] Y. Sun, Q. Zhu, Z. Chen, An iterative initial-points refinement algorithm for categorical data clustering, Pattern Recognit. Lett. 23 (2002) 875–884.

[38] Q. Le, T. Mikolov, Distributed representations of sentences and documents, in: Int. Conf. Mach. Learn., 2014: pp. 1188–1196.

[39] G. Salton, C. Buckley, Term-weighting approaches in automatic text retrieval, Inf. Process. Manag. 24 (1988) 513–523.

[40] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, Bert: Pre-training of deep bidirectional transformers for language understanding, ArXiv Prepr. ArXiv1810.04805. (2018).

[41] S. Deerwester, S.T. Dumais, G.W. Furnas, T.K. Landauer, R. Harshman, Indexing by latent semantic analysis, J. Am. Soc. Inf. Sci. 41 (1990) 391–407.

[42] K. Coussement, D. Van den Poel, Integrating the voice of customers through call center emails into a decision support system for churn prediction, Inf. Manag. 45 (2008) 164–174.

[43] B. Rosario, Latent semantic indexing: An overview, Techn. Rep. INFOSYS. 240 (2000) 1– 16.

[44] M. Zhu, A. Ghodsi, Automatic dimensionality selection from the scree plot via the use of profile likelihood, Comput. Stat. Data Anal. 51 (2006) 918–930.

[45] T. Mikolov, K. Chen, G. Corrado, J. Dean, Efficient estimation of word representations in vector space, ArXiv Prepr. ArXiv1301.3781. (2013).

[46] T. Mikolov, I. Sutskever, K. Chen, G.S. Corrado, J. Dean, Distributed representations of words and phrases and their compositionality, Adv. Neural Inf. Process. Syst. 26 (2013).

[47] J.H. Lau, T. Baldwin, An empirical evaluation of doc2vec with practical insights into document embedding generation, ArXiv Prepr. ArXiv1607.05368. (2016).

[48] D. Kim, D. Seo, S. Cho, P. Kang, Multi-co-training for document classification using various document representations: TF--IDF, LDA, and Doc2Vec, Inf. Sci. (Ny). 477 (2019) 15–29.

[49] W.L. Taylor, “Cloze procedure”: A new tool for measuring readability, Journal. Q. 30 (1953) 415–433.

[50] G. James, D. Witten, T. Hastie, R. Tibshirani, An Introduction to Statistical Learning: With Applications in R, Springer Publishing Company, Incorporated, 2014.

[51] J.H. Ward Jr, Hierarchical grouping to optimize an objective function, J. Am. Stat. Assoc. 58 (1963) 236–244.

[52] H. Abdi, L.J. Williams, Principal component analysis, Wiley Interdiscip. Rev. Comput. Stat. 2 (2010) 433–459.

[53] I.T. Jolliffe, Graphical representation of data using principal components, Princ. Compon. Anal. (2002) 78–110.

[54] L. van der Maaten, G. Hinton, Visualizing data using t-SNE, J. Mach. Learn. Res. 9 (2008) 2579–2605.

[55] G.E. Hinton, S. Roweis, Stochastic neighbor embedding, Adv. Neural Inf. Process. Syst. 15 (2002).

[56] L. McInnes, J. Healy, J. Melville, Umap: Uniform manifold approximation and projection for dimension reduction, ArXiv Prepr. ArXiv1802.03426. (2018).

[57] M.W. Dorrity, L.M. Saunders, C. Queitsch, S. Fields, C. Trapnell, Dimensionality reduction by UMAP to visualize physical and genetic interactions, Nat. Commun. 11 (2020) 1–6.

[58] R. Barber, M. Sharkey, Course Correction: Using Analytics to Predict Course Success, in: Proc. 2Nd Int. Conf. Learn. Anal. Knowl., ACM, New York, NY, USA, 2012: pp. 259–262.

[59] S.B. Kotsiantis, C.J. Pierrakeas, P.E. Pintelas, Preventing student dropout in distance learning using machine learning techniques, in: Int. Conf. Knowledge-Based Intell. Inf. Eng. Syst., 2003: pp. 267–274.

[60] T. Sinha, P. Jermann, N. Li, P. Dillenbourg, Your click decides your fate: Inferring information processing and attrition behavior from mooc video clickstream interactions, ArXiv Prepr. ArXiv1407.7131. (2014).

[61] S. Jiang, A. Williams, K. Schenke, M. Warschauer, D. O’dowd, Predicting MOOC performance with week 1 behavior, in: Educ. Data Min. 2014, 2014.

[62] K.R. Koedinger, J. Kim, J.Z. Jia, E.A. McLaughlin, N.L. Bier, Learning is not a spectator sport: Doing is better than watching for learning from a MOOC, in: Proc. Second ACM Conf. Learn. Scale, 2015: pp. 111–120.

[63] R. Tibshirani, Regression shrinkage and selection via the lasso, J. R. Stat. Soc. Ser. B. 58 (1996) 267–288.

[64] L. Aulck, N. Velagapudi, J. Blumenstock, J. West, Predicting Student Dropout in Higher Education, ArXiv E-Prints. (2016).

[65] S.A. Elkins, J.M. Braxton, G.W. James, Tinto’s separation stage and its influence on firstsemester college student persistence, Res. High. Educ. 41 (2000) 251–268.

[66] M.P. Marcus, M.A. Marcinkiewicz, B. Santorini, Building a Large Annotated Corpus of English: The Penn Treebank, Comput. Linguist. 19 (1993) 313–330.

[67] B. Santorini, Part-of-speech tagging guidelines for the Penn Treebank Project, (1990).

[68] M.F. Porter, Snowball: A language for stemming algorithms, (2001).

[69] Y. Chen, A. Johri, H. Rangwala, Running out of stem: a comparative study across stem majors of college students at-risk of dropping out early, in: Proc. 8th Int. Conf. Learn. Anal. Knowl., 2018: pp. 270–279.

[70] K. Coussement, S. Lessmann, G. Verstraeten, A comparative analysis of data preparation algorithms for customer churn prediction: A case study in the telecommunication industry, Decis. Support Syst. 95 (2017) 27–36.

[71] S.A. Neslin, S. Gupta, W. Kamakura, J. Lu, C.H. Mason, Defection Detection: Measuring and Understanding the Predictive Accuracy of Customer Churn Models, J. Mark. Res. XLIII (2006) 204–211.

[72] J.L. Fleiss, Measuring nominal scale agreement among many raters., Psychol. Bull. 76 (1971) 378.

[73] A.J. Conger, Integration and generalization of kappas for multiple raters, Psychol. Bull. 88 (1980) 322.

[74] A. Nandeshwar, T. Menzies, A. Nelson, Learning patterns of university student retention, Expert Syst. Appl. 38 (2011) 14984–14996.

[75] E. Aguiar, N. V Chawla, J. Brockman, G.A. Ambrose, V. Goodrich, Engagement vs performance: using electronic portfolios to predict first semester engineering student retention, in: Proc. Fourth Int. Conf. Learn. Anal. Knowl., 2014: pp. 103–112.

[76] C. Beaulac, J.S. Rosenthal, Predicting university Students’ academic success and major using random forests, Res. High. Educ. 60 (2019) 1048–1064.

<table><tr><td rowspan="2">Authors</td><td rowspan="2">Context</td><td rowspan="2">Data Set</td><td colspan="2">Data Type</td><td colspan="2">Modeling Approach</td><td colspan="2">Interpretability</td></tr><tr><td>Structured</td><td>Textual</td><td>Algorithm</td><td>Segmentation</td><td>Global</td><td>Segment</td></tr><tr><td>[7]</td><td>Freshmen dropout, public university in Netherlands</td><td>648 students, 49% dropouts</td><td>√</td><td>-</td><td>DT, BN, LR, RF, RL, OneR</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[32]</td><td>Student at risk, public university in UK</td><td>4,223 students, n/a dropouts</td><td>√</td><td>-</td><td>NB, SVM, DT</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[16]</td><td>Freshmen dropout, public university in US</td><td>16,066 students, 21.84% dropouts</td><td>√</td><td>-</td><td>DT, NN, SVM, LR</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[33]</td><td>Freshmen dropout, public university in US</td><td>25,224 students, 21.03% dropouts</td><td>√</td><td>-</td><td>DT, NN, LR</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[74]</td><td>Freshmen retention, public university in US</td><td>n/a students, 28.7%, 39.6%, 45.2% dropouts after  ${1}^{\text{st }}, {2}^{\text{nd }}, {3}^{\text{rd }}$  year</td><td>√</td><td>-</td><td>OneR, DT, NB, BN, NN</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[30]</td><td>Student dropout, public university in Czech Republic</td><td>775 students, 58.86% dropouts</td><td>√</td><td>-</td><td>NB, SVM, RL, OneR, DT, LL</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[75]</td><td>Freshmen dropout, private university in US</td><td>429 students, 11.5% dropouts</td><td>√</td><td>-</td><td>NB, DT, LR, RF</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[1]</td><td>Freshmen dropout, public university</td><td>21,654 students, 21.3% dropouts</td><td>√</td><td>-</td><td>NN, SVM, DT, LR</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[69]</td><td>Student dropout, public HEI in US, STEM program</td><td>12,293 students, n/a dropouts</td><td>√</td><td>-</td><td>SA, LR, DT, NB, AB</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[28]</td><td>Freshmen dropout, public university</td><td>682 students, n/a dropouts</td><td>√</td><td>-</td><td>LR, NN, PNN</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[34]</td><td>First year student attrition, public university in US</td><td>66,060 students, 28.40% dropouts</td><td>√</td><td>-</td><td>LR, kNN, RF, SVM, GBT</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[76]</td><td>Student at risk, public university in Canada</td><td>38,842 students 31.65% dropouts</td><td>√</td><td>-</td><td>RF</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[29]</td><td>Student dropout, university in Brazil</td><td>2,175 students, 13.2% dropouts</td><td>√</td><td>-</td><td>NB, SVM, RF, GBT, kNN</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[25]</td><td>Student dropout, university in US</td><td>7,343 students, n/a dropouts</td><td>-</td><td>√</td><td>RF, SVM, LR, DT</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[2]</td><td>Freshmen dropout, public university</td><td>36,461 students, 20% dropouts</td><td>√</td><td>-</td><td>BN</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[6]</td><td>Student dropout, public university</td><td>3,176 students, 19.5% dropouts</td><td>√</td><td>-</td><td>LR, DT</td><td>-</td><td>√</td><td>-</td></tr><tr><td>[31]</td><td>Student at-risk (withdrawn/dropout), public university in Canada</td><td>25,541 students, n/a dropouts</td><td>√</td><td>-</td><td>DL, SVM, LR</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[9]</td><td>Student dropout, HEI in Chile</td><td>3,362 students 12.4%, 5.4% dropouts after the  ${2}^{\text{nd }}, {3}^{\text{rd }}$  year</td><td>√</td><td>-</td><td>LR, kNN, DT, RF, NN, SVM</td><td>-</td><td>√</td><td>-</td></tr><tr><td>This study</td><td>First year student dropout private business school</td><td>14,391 students, 1.2% dropouts</td><td>√</td><td>√</td><td>LR</td><td>√</td><td>√</td><td>√</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 1 <sub>:</sub> St<sub>u</sub>di<sub>es</sub> <sub>pre</sub>di<sub>c</sub>ti<sub>ng</sub> <sub>s</sub>t<sub>u</sub>d<sub>en</sub>t d<sub>ropou</sub>t<sub>s</sub> f<sub>rom</sub> HEI <sub>us</sub>i<sub>ng</sub> <sub>pre</sub>di<sub>c</sub>ti<sub>ve</sub> <sub>mo</sub>d<sub>e</sub>li<sub>ng</sub> <sub>pu</sub>bli<sub>s</sub>h<sub>e</sub>d 2009–202 1  
Notes : The <sub>p</sub>redictive al<sub>g</sub>orithm abbreviations are as follows : ada<sub>p</sub>tive boost (AB ) <sub>,</sub> B a<sub>y</sub>esian belief network (BN) <sub>,</sub> dee<sub>p</sub> learnin<sub>g</sub> (DL) <sub>,</sub> decision tree and its variants (e. <sub>g</sub> . CART<sub>,</sub> C4 . 5 <sub>,</sub> J4 . 8) (DT) <sub>,</sub> <sub>g</sub>radient boosted trees (GB T) k-nearest nei<sub>g</sub>hbor (kNN) laz<sub>y</sub> learnin<sub>g</sub> (LL) lo<sub>g</sub>istic re<sub>g</sub>ression (LR) naïve B a<sub>y</sub>es (NB ) neural network (NN) one rule (OneR) <sub>p</sub>robabilistic neural networks (PNN) random forest (RF) rule-based learner (RL) su<sub>pp</sub>ort vector machines (SVM) and survival anal<sub>y</sub>sis (SA) .

<table><tr><td>No.</td><td>Variable Group</td><td>Variable Description</td><td># Variables</td></tr><tr><td>1</td><td rowspan="8">Sociodemographic information</td><td>Gender (Male/Female)</td><td>1</td></tr><tr><td>2</td><td>Citizen status</td><td>1</td></tr><tr><td>3</td><td>Civil status</td><td>1</td></tr><tr><td>4</td><td>Continent</td><td>1</td></tr><tr><td>5</td><td>2 first digits of zip code</td><td>1</td></tr><tr><td>6</td><td>Age</td><td>1</td></tr><tr><td>7</td><td>Information change (Yes/No)</td><td>1</td></tr><tr><td>8</td><td>Campus (Lille/Paris)</td><td>1</td></tr><tr><td>9</td><td rowspan="4">Course enrollment</td><td>Number of courses enrolling in this semester</td><td>1</td></tr><tr><td>10</td><td>Number of courses enrolled by category (Accounting, Economy, Finance, Marketing, Negotiation, Language, etc.)</td><td>23</td></tr><tr><td>11</td><td>Number of courses retaking in this semester</td><td>1</td></tr><tr><td>12</td><td>Number of internships having in this semester</td><td>1</td></tr><tr><td rowspan="3">13</td><td rowspan="3">Vectorized student feedback textual data</td><td>vector space matrix</td><td rowspan="3">Decided by hyperparameter tuning</td></tr><tr><td>doc2vec matrix</td></tr><tr><td>BERT matrix</td></tr><tr><td>14</td><td>Target variable</td><td>Student dropout after the first semester (Yes/No)</td><td>1</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 2 <sub>:</sub> Li<sub>s</sub>t <sub>o</sub>f <sub>var</sub>i<sub>a</sub>bl<sub>es</sub>

<table><tr><td colspan="3"></td><td colspan="2">Student Group</td><td colspan="2">Data Type</td><td colspan="3">Text Representation Method</td><td colspan="2">Segmentation with Textual Data</td></tr><tr><td>Group</td><td>No.</td><td>Model name</td><td>With text (T)</td><td>Without text (NT)</td><td>Structured (S)</td><td>Unstructured (U)</td><td>vector space (VS)</td><td>doc2vec (DV)</td><td>Transformer language model (BERT)</td><td>k-means (KM)</td><td>Hierarchical clustering (HC)</td></tr><tr><td rowspan="4">1</td><td>1</td><td>Mod_FD_S</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Mod_T_S</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Mod_NT_S</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>Mod_TNT_S</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>5</td><td>Mod_T_U</td><td>✓</td><td></td><td></td><td>✓</td><td>(a) ✓</td><td>(b) ✓</td><td>(c) ✓</td><td></td><td></td></tr><tr><td rowspan="2">3</td><td>6</td><td>Mod_T_SU</td><td>✓</td><td></td><td>✓</td><td>✓</td><td rowspan="2" colspan="3">Best method from Group 2</td><td rowspan="2">(a) ✓</td><td rowspan="2">(b) ✓</td></tr><tr><td>7</td><td>Mod_T_SU_SEG</td><td>✓</td><td></td><td>✓</td><td>✓</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 3 <sub>:</sub> Li<sub>s</sub>t <sub>o</sub>f <sub>mo</sub>d<sub>e</sub>l<sub>s an</sub>d d<sub>a</sub>t<sub>a com</sub>bi<sub>na</sub>ti<sub>ons</sub>

<table><tr><td>Text Representation Method</td><td># Models</td><td>Hyperparameter</td><td>Value Range</td></tr><tr><td>vector space</td><td>1</td><td>Number of dimensions of SVD (decided by Profile Log-likelihood)</td><td>l ∈ [1,4996]</td></tr><tr><td rowspan="5">doc2vec</td><td rowspan="5">36</td><td>Vector size</td><td>25, 50</td></tr><tr><td>Window size</td><td>1, 2, 5</td></tr><tr><td>Minimum word frequency</td><td>1</td></tr><tr><td>The training algorithm</td><td>PV-DM, PV-DBOW</td></tr><tr><td>Negative sampling</td><td>10, 15, 20</td></tr><tr><td>BERT</td><td>3</td><td>Pre-trained BERT model</td><td>BERT Base, Small BERT, ALBERT</td></tr></table>

Table 4: Hyperparameters for text representation methods

<table><tr><td>Group</td><td>No.</td><td>Model Name</td><td>AUC (SD)</td><td>TDL (SD)</td></tr><tr><td rowspan="6">1</td><td>1</td><td>Mod_FD_S</td><td>0.755 (0.046)</td><td>3.818 (0.872)</td></tr><tr><td>1a</td><td>Mod_FD_S_testT</td><td>0.791 (0.043)</td><td>4.225 (0.974)</td></tr><tr><td>1b</td><td>Mod_FD_S_testNT</td><td>0.709 (0.065)</td><td>3.305 (0.916)</td></tr><tr><td>2</td><td>Mod_T_S</td><td>0.784 (0.048)</td><td>3.947 (1.186)</td></tr><tr><td>3</td><td>Mod_NT_S</td><td>0.704 (0.064)</td><td>3.049 (0.840)</td></tr><tr><td>4</td><td>Mod_TNT_S</td><td>0.750 (0.044)</td><td>3.493 (0.866)</td></tr></table>

Table 5: Results of the dropout prediction models (average and standard deviation of AUC and TDL), Group 1

<table><tr><td rowspan="2"></td><td rowspan="2" colspan="2">Model Name</td><td rowspan="2">Model Name</td><td colspan="2">p-Value</td></tr><tr><td>AUC</td><td>TDL</td></tr><tr><td rowspan="3">Group 1 vs. 1</td><td>Mod_T_S</td><td>vs.</td><td>Mod_FD_S_testT</td><td>0.524</td><td>0.100*</td></tr><tr><td>Mod_NT_S</td><td>vs.</td><td>Mod_FD_S_testNT</td><td>0.489</td><td>0.449</td></tr><tr><td>Mod_TNT_S</td><td>vs.</td><td>Mod_FD_S</td><td>0.561</td><td>0.055*</td></tr></table>

Table 6: Wilcoxon signed-rank test for pairwise comparison of models in Group 1  
Notes: Significant differences at the 90%, 95%, and 99% levels are indicated by \*, \*\*, and \*\*\*.

<table><tr><td>Group</td><td>No.</td><td>Model Name</td><td>AUC (SD)</td><td>TDL (SD)</td></tr><tr><td rowspan="4">2</td><td>-</td><td>Random guessing</td><td>0.500 (0.000)</td><td>1.000 (0.000)</td></tr><tr><td>5a</td><td>Mod_T_U_VS</td><td>0.539 (0.046)</td><td>1.213 (0.369)</td></tr><tr><td>5b</td><td>Mod_T_U_DV</td><td>0.591 (0.030)</td><td>1.656 (0.625)</td></tr><tr><td>5c</td><td>Mod_T_U_BERT</td><td>0.545 (0.066)</td><td>1.467 (0.512)</td></tr></table>

Table 7: Results of the dropout prediction models (reported on average and standard deviation of AUC and TDL), Group 2. The best hyper-parameter combination is highlighted.

<table><tr><td rowspan="2"></td><td rowspan="2" colspan="2">Model Name</td><td rowspan="2">Model Name</td><td colspan="2">p-Value</td></tr><tr><td>AUC</td><td>TDL</td></tr><tr><td>Group 2 vs. 2</td><td>Mod_T_U</td><td>vs.</td><td>Random guessing</td><td>&lt;0.001***</td><td>0.003**</td></tr></table>

Table 8: Wilcoxon signed-rank test for pairwise comparisons of models in Group 2 Notes: Significant differences at the 90%, 95%, and 99% levels are indicated by \*, \*\*, and \*\*\*.

<table><tr><td>Group</td><td>No.</td><td>Model Name</td><td>AUC (SD)</td><td>TDL (SD)</td></tr><tr><td rowspan="2">1</td><td>1a</td><td>Mod_FD_S_testT</td><td>0.791 (0.043)</td><td>4.225 (0.974)</td></tr><tr><td>2</td><td>Mod_T_S</td><td>0.784 (0.048)</td><td>3.947 (1.186)</td></tr><tr><td rowspan="3">3</td><td>6</td><td>Mod_T_SU</td><td>0.784 (0.045)</td><td>4.181 (0.799)</td></tr><tr><td>7a</td><td>Mod_T_SU_KM</td><td>0.801 (0.035)</td><td>4.524 (0.872)</td></tr><tr><td>7b</td><td>Mod_T_SU_HC</td><td>0.788 (0.082)</td><td>4.188 (1.224)</td></tr></table>

Table 9: Results of the dropout predictive models (reported on average and standard deviation of AUC and TDL), Group 3. The best hyper-parameter combination is highlighted. Notes: Group 1 provides a benchmark.

<table><tr><td rowspan="2"></td><td rowspan="2" colspan="2">Model Name</td><td rowspan="2">Model Name</td><td colspan="2">p-Value</td></tr><tr><td>AUC</td><td>TDL</td></tr><tr><td>Group 3 vs. 3</td><td>Mod_T_SU</td><td>vs.</td><td>Mod_T_SU_SEG</td><td>0.018**</td><td>0.038**</td></tr><tr><td rowspan="2">Group 3 vs. 1</td><td>Mod_T_SU_SEG</td><td>vs.</td><td>Mod_T_S</td><td>0.022**</td><td>0.062*</td></tr><tr><td>Mod_T_SU_SEG</td><td>vs.</td><td>Mod_FD_S_testT</td><td>0.208</td><td>0.087*</td></tr></table>

Table 10: Wilcoxon signed-rank test for pairwise comparison of models in Groups 1 and 3 Notes: Significant differences at the 90%, 95%, and 99% levels are indicated by \*, \*\*, and \*\*\*.

![](/api/attachments/XTK43DNK/fulltext/images/0b692fb91234216e13cf5dde2976bafef7d13570dd87dc3f413a03da9a1e3502.jpg)  
Fi<sub>gure</sub> 1 <sub>:</sub> D<sub>ec</sub>i<sub>s</sub>i<sub>on</sub> <sub>suppor</sub>t f<sub>ramewor</sub>k t<sub>o</sub> i<sub>ncorpora</sub>t<sub>e</sub> t<sub>ex</sub>t<sub>ua</sub>l d<sub>a</sub>t<sub>a</sub> t<sub>o</sub> <sub>pre</sub>di<sub>c</sub>t <sub>s</sub>t<sub>u</sub>d<sub>en</sub>t d<sub>ropou</sub>t

![](/api/attachments/XTK43DNK/fulltext/images/13f2abd98d71716e18e958da60ee29bbacc9b5125a9fd3d9717cce00d1b61791.jpg)  
Figure 2: Time windows for early student dropout prediction

![](/api/attachments/XTK43DNK/fulltext/images/339c6ae25c29899ea2119215ccc9d959d69dddc698f07f817dcf38fc960c6248.jpg)  
Figure 3: Data processing pipeline

![](/api/attachments/XTK43DNK/fulltext/images/bffe2dda72bb335fbf004f7005adf9d077fd15a4f6a0a5236300b5b47954e9c0.jpg)  
Figure 4: Visualization of the student segments based on transformed textual data

![](/api/attachments/XTK43DNK/fulltext/images/841c7652ef4a29f245de7df652ab934163f99aa7b5ebd74f431c189ffb5ecae1.jpg)  
Figure 5: Discussion topics among the two student segments

<table><tr><td colspan="3">Segment Definition</td><td colspan="3">Variable Category Importance</td></tr><tr><td>Seg.</td><td>Number of observations</td><td>Percentage dropout</td><td>Sociodemographic information</td><td>Course enrollment</td><td>Feedback text</td></tr><tr><td>1</td><td>2,182</td><td>1.9%</td><td>37%</td><td>46%</td><td>17%</td></tr><tr><td>2</td><td>2,635</td><td>0.8%</td><td>43%</td><td>43%</td><td>14%</td></tr></table>

Fi<sub>gure</sub> 6 <sub>:</sub> P<sub>ercen</sub>t<sub>age</sub> <sub>o</sub>f <sub>var</sub>i<sub>a</sub>bl<sub>e</sub> i<sub>mpor</sub>t<sub>ance</sub> <sub>per</sub> <sub>group</sub> i<sub>n</sub> <sub>eac</sub>h <sub>segmen</sub>t

<table><tr><td rowspan="3">Seg.</td><td colspan="24">Variable Group</td><td></td></tr><tr><td colspan="8">Sociodemographic Information</td><td colspan="16">Course Enrollment</td><td></td></tr><tr><td>Age</td><td>Origin: Others</td><td>Region: 92</td><td>Region: Others</td><td>Civil status: B</td><td>Civil status: Others</td><td>Campus: Paris</td><td>Info. changed</td><td>Total</td><td>ACC</td><td>DEV</td><td>ECO</td><td>ENT</td><td>FAS</td><td>FIN</td><td>IBE</td><td>LAN</td><td>MIS</td><td>LAW</td><td>MKT</td><td>NEG</td><td>QMS</td><td>STR</td><td>RES</td><td>OPS</td></tr><tr><td rowspan="2">1</td><td>-</td><td></td><td></td><td>+</td><td></td><td>+</td><td>+</td><td>+</td><td>-</td><td>+</td><td></td><td>+</td><td></td><td></td><td>-</td><td></td><td>+</td><td>-</td><td>+</td><td></td><td>-</td><td>+</td><td></td><td></td><td>-</td></tr><tr><td>0.33</td><td></td><td></td><td>0.57</td><td></td><td>0.16</td><td>0.53</td><td>3.89</td><td>0.05</td><td>0.02</td><td></td><td>0.59</td><td></td><td></td><td>0.51</td><td></td><td>0.35</td><td>0.23</td><td>0.08</td><td></td><td>0.54</td><td>0.72</td><td></td><td></td><td>0.40</td></tr><tr><td rowspan="2">2</td><td>-</td><td>+</td><td>-</td><td>-</td><td>-</td><td></td><td>-</td><td>-</td><td>-</td><td>+</td><td>-</td><td></td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td>+</td><td></td><td>-</td><td>-</td><td>+</td><td>+</td><td>+</td><td></td></tr><tr><td>0.21</td><td>0.48</td><td>0.43</td><td>0.37</td><td>0.29</td><td></td><td>0.11</td><td>2.74</td><td>0.04</td><td>0.04</td><td>0.09</td><td></td><td>0.02</td><td>0.14</td><td>0.16</td><td>0.37</td><td></td><td>0.13</td><td></td><td>0.14</td><td>0.17</td><td>1.22</td><td>0.07</td><td>0.28</td><td></td></tr></table>

Fi<sub>gure</sub> 7 <sub>:</sub> C<sub>oe</sub>ffi<sub>c</sub>i<sub>en</sub>t<sub>s</sub> <sub>o</sub>f th<sub>e</sub> <sub>var</sub>i<sub>a</sub>bl<sub>es</sub> i<sub>n</sub> <sub>eac</sub>h <sub>s</sub>t<sub>u</sub>d<sub>en</sub>t <sub>segmen</sub>t  
Notes : The course cate<sub>g</sub>or<sub>y</sub> abbreviations are as follows : audit control accountin<sub>g</sub> (ACC) <sub>p</sub>ersonal develo<sub>p</sub>ment (DEV) economics (ECO) entre<sub>p</sub>reneurshi<sub>p</sub> (ENT) fashion (FAS) finance (FIN) international econom<sub>y</sub> (IBE) lan<sub>g</sub>ua<sub>g</sub>es (LAN) mana<sub>g</sub>ement of information s<sub>y</sub>stems (MIS) law (LAW) marketin<sub>g</sub> (MKT) ne<sub>g</sub>otiation (NEG) <sub>q</sub>uantitative methods (QMS) strate<sub>gy</sub> (STR) research (RES) o<sub>p</sub>eration mana<sub>g</sub>ement (OPS) .
