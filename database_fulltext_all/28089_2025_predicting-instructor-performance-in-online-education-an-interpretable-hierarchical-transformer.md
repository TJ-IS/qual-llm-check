---
otero_id: 28089
otero_key: "JRFT3K43"
title: "Predicting Instructor Performance in Online Education: An Interpretable Hierarchical Transformer with Contextual Attention"
authors: "Wen Wang; Mi Zhou; Beibei Li; Honglei Zhuang"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0310"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting Instructor Performance in Online Education: An Interpretable Hierarchical Transformer with Contextual Attention

Wen Wang,<sup>a</sup> Mi Zhou,<sup>b,</sup>\* Beibei Li,<sup>c</sup> Honglei Zhuang<sup>d</sup>

<sup>a</sup> University of Maryland, College Park, Maryland 20742; <sup>b</sup>UBC Sauder School of Business, Vancouver, British Columbia V6T 1Z2, Canada; <sup>c</sup> Carnegie Mellon University, Pittsburgh, Pennsylvania 15213; <sup>d</sup> Google Research, Mountain View, California 94043 \*Corresponding author

Contact: wenw@umd.edu, https://orcid.org/0000-0001-5983-3224 (WW); mi.zhou@sauder.ubc.ca, https://orcid.org/0000-0001-8648-0225 (MZ); beibeili@andrew.cmu.edu, https://orcid.org/0000-0001-5466-7925 (BL); hlz@google.com (HZ)

Received: June 10, 2021 Revised: September 26, 2022; May 13, 2023 Accepted: July 6, 2023 Published Online in Articles in Advance: February 14, 2025

https://doi.org/10.1287/isre.2021.0310

Copyright: © 2025 INFORMS

Abstract. Online education is a vital consumer industry that is undergoing rapid technological change. This paper develops a deep learning model to predict instructor performance on online education platforms from a content-based perspective. Specifically, we design an interpretable hierarchical transformer with contextual attention to predict instructor rating and course rating using textual data. Our model captures the inherent hierarchical structure of online courses and the sequential dependency of lectures within a course. Moreover, it goes beyond prediction and enables interpretability analysis, which provides additional insights into potential reasons behind the predictions made by the model. Extensive experiments demonstrate that our model outperforms classic machine learning models as well as state-of-the-art deep learning models. Furthermore, we conduct in-depth interpretability analysis to explore what factors might predict the success of an online course at the lecture, sentence, and word level. We also showcase the value and applicability of our model through a randomized experiment. Our findings and method provide managerial implications for instructors and online education platforms to improve course creation and delivery in this vitally important emerging market.

History: Ravi Bapna, Senior Editor; Tianshu Sun, Associate Editor.

Funding: This work was supported by the Social Sciences and Humanities Research Council of Canada [Grant 430-2022-00297].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0310.

Keywords: online education • instructor performance • unstructured data analytics • natural language processing • interpretable deep learning

## 1. Introduction

Education is one of the most important industries for the global economy. The market size of educational services in the United States reached \$1.6 trillion in 2020 (IBISWorld 2020). Education is not only essential at a global level but also significant at a personal level because it plays a crucial role in everyone’s life. With the development of technology, the online education market has been growing rapidly over the past decade. It is predicted that the global online education market will reach \$319 billion by 2025 (Research and Markets 2020). A large portion of this market is dominated by major platforms such as Coursera, Udemy, edX, and FutureLearn. These platforms offer accessible and affordable remote learning opportunities to students worldwide. Online education is having an unprecedented impact on learners throughout the world. According to Coursera’s 2020 impact report, about 70 million learners in 140 countries are engaged in online education on their platform (Coursera 2020). The importance of online education services has become even further underscored during the ongoing COVID-19 pandemic, which created an unprecedented disruption of education systems, impacting nearly 1.6 billion learners in over 190 countries (United Nations 2020). In response, many schools turned to online education, requiring instructors to adapt to online delivery of lessons because of school closures during this difficult time.

Several managerially relevant issues for online education have recently emerged. For example, instructors with limited online teaching experience face significant challenges in planning their online courses because of the fundamental differences between online and offline teaching (e.g., lack of human interaction, increased freedom and flexibility). A recent survey indicated that 70% of the 1.5 million faculty members in the United States had never taught an online course prior to the COVID-19 pandemic (American Marketing Association 2020). Given this, an automated tool that assists instructors in preparing for online teaching is of vital importance to both the education industry and society at large. In addition, online platforms heavily rely on product ratings as a quality signal in their recommendation algorithms and ranking systems to improve consumer engagement and retention. However, accurately measuring course quality on online education platforms, especially for newly created courses, is challenging, potentially leading to suboptimal recommendation outcomes. Therefore, an automated tool that can accurately predict product quality based on course content is of significant importance to the business success of online education platforms.

Our study aims to develop such a tool that predicts course ratings from a content-based perspective, addressing these timely issues for various stakeholders in the online education market. In particular, the input of the tool is the original unstructured content of course materials, consisting of all the textual subtitles of the lectures. The output of the system is a rating indicating teaching performance or course quality. Student ratings are the most widely used metric for measuring teaching performance, both online and offline (Wilson 1932, Feldman 1977, Chatterjee et al. 2009). Student ratings constitute direct feedback from the learning experience. In an offline setting, universities heavily rely on student ratings to evaluate instructors’ teaching quality and make decisions on academic tenure (Costin et al. 1971, Algozzine et al. 2004, Benton and Cashin 2014). This is reflected in the online setting. Online education platforms like Coursera and Udemy also emphasize the importance of ratings, displaying the instructor and course ratings on their websites as a quality indicator. Therefore, our developed tool aims to predict student ratings, which is important not only for a platform’s business success but also for the success of online instruction more broadly.

Although developing such a tool is considered to be an urgent priority, there are several nontrivial challenges because of the unique characteristics of the online educational setting. First, courses have an inherent hierarchical structure. Specifically, each course usually consists of a series of lectures with a strong sequential dependency. Thus, how to leverage the information contained within this hierarchical course structure to predict instructors performance presents a significant challenge. Second, deep learning models are often viewed as black boxes because of a lack of interpretability. This limits people’s trust in these models as they do not provide explanations behind their predictions. However, in the online education setting, the interpretability of the model is essential to provide practical implications for instructors and online education platforms.

Our research aims to tackle these challenges in this crucial and emerging customer service sector. In particular, we develop an interpretable hierarchical transformer with contextual attention for instructor performance prediction. Our model adopts the global-local hierarchical transformer architecture to capture the hierarchical structure of online courses and the sequential dependency of lectures within a course. Additionally, we develop a customized contextual attention mechanism to enhance model interpretability, providing insights into the potential reasons behind the model’s predic tions. This customized contextual attention seeks to understand how predicted student ratings on instructors performance might vary under different educational contexts, offering valuable insights and managerial implica tions for instructors and online education platforms.

We demonstrate the feasibility and value of our model using a unique data set from Coursera. Experimental results shows that the model provides signifi cant performance gains over 14 non-deep learning methods, with the performance improvements attributed to each component of our model (hierarchical structure, contextual attention, etc.) through an ablation study. Furthermore, we conduct a series of interpretability analyses to demonstrate the decision support showcase to assist instructors with interpretable insights behind the predictions. Our analysis uncovers what factors might predict the success of a course at the lecture, sentence, and word level, which can serve as a starting point for instructors and platforms seeking to improve course content creation and delivery in the future.

For the lecture-level interpretability analysis, we use the learned contextual attention to demonstrate how much each lecture’s material contributes to the fina prediction under different educational contexts such as academic discipline, difficulty level, course duration, and type of affiliation. Our results show that the predictive impact of different lectures varies significantly among different contexts. For the sentence-level interpretability analysis, we use a two-stage counterfactua prediction strategy to identify potential “bad sentences” that might lower the predicted rating. We further inves tigate why these sentences might negatively impact course evaluation prediction in terms of various aspects. Our results show that “bad sentences” are significantly less relevant to the main topic of the course than “good sentences.” For the word-level interpretability analysis, we extract five different word-level verbal cues and explore their predictive impact on the ratings. We conduct counterfactual prediction using our model by mod ifying verbal cues to investigate how they might affect the predicted instructors’ performance. We believe these interpretable insights can serve as an initial guide for instructors and online education platforms in the design and preparation of future online courses.

In addition to assisting instructors with accurate predictions and interpretable insights, our method can also aid online education platforms. Specifically, we have conducted a randomized experiment to demonstrate the applicability and value of our model for online education platforms. In this experiment, participants were shown two lists of courses—one generated by our model based on the predictions and one generated randomly from the data. Our results showed that 71% of participants exhibited a preference for the course list generated by our model. Moreover, the average rating assigned by participants to our course list was significantly higher than that of the randomly generated course list. This demonstrates that the platform can utilize our model to improve course ranking systems. For example, when the platform needs to rank different courses in user recommendations or search result pages, they could potentially prioritize the recommendation of courses with higher predicted ratings over those with lower predicted ratings, based on the predictions made by our model.

In summary, our contributions are threefold. First, our paper is among the first to apply hierarchical transformer models to the important domain of online education, improving predictions for instructor rating and course rating. Second, the customized contextual attention in our model enables interpretable prediction insights, assisting instructors in improving their teaching materials at various levels. Third, we demonstrate that our model can serve as a decision support system for stakeholders in online education through a randomized experiment. Together, our model and findings provide instructors and online education platforms with new tools to enhance course creation and delivery in this vitally important emerging market.

## 2. Literature Review

## 2.1. Online Education Market

Despite its economic importance and rapid growth in recent years, online education has received relatively little attention in business research (Zhang et al. 2017). There are only a small number of studies in this burgeoning field. For example, Adamopoulos (2013) studied the student retention in online courses. Dellarocas and Van Alstyne (2013) investigated business models for massive open online courses (MOOCs). Zhang et al. (2017) examined the impact of social interaction on students’ online learning outcomes. Kumar and Mehra (2018) investigated how computer-aided learning applications can improve student learning. Huang et al. (2021) examined the efficacy of informational interventions for reducing users’ procrastination in MOOCs. Zhou et al. (2021) analyzed unstructured video data to predict customers’ online video consumption behavior in the context of digital learning. Leung et al. (2022) investigated the effectiveness of gamification on learners’ engagement and learning outcomes in MOOCs. Our research complements these studies by designing an automated system to accurately predict instructors performance and also provide practical implications for both instructors and platforms in this emerging and vitally important customer service sector.

## 2.2. Education Mining

Our research is closely related to education mining broadly. Existing literature includes MOOC-related studies on student behavior analysis (Feng et al. 2019, Trakunphutthirak et al. 2019), course concept mining (Pan et al. 2017, Yu et al. 2019), and course recommendation (Zhang et al. 2019). Feng et al. (2019) investigated students’ dropouts in MOOCs, identifying a high correlation between dropouts for different courses and the strong influence of friends’ dropout behaviors. They developed a context-aware feature interaction network to model and predict users’ dropout behavior. Trakunphutthirak et al. (2019) examined students’ internet access activities that can indicate their time management during their studies, exploring the relationship between these activities and academic performance. Pan et al. (2017) studied the design of effective and fine-grained course concepts to help students from diverse backgrounds grasp the essence of a course through an embedding-based method for learning latent representations of candi date concepts. We contribute to this body of literature by focusing on a novel question of managerial relevance—predicting instructors’ performance based on course material content—and developing an interpretable hierarchical transformer with contextual attention to predict instructor rating and course rating, providing practical implications for various stakeholders in online education.

## 2.3. Traditional Education Theory

Our study is also closely related to traditional education research (e.g., instructors’ performance evaluation (Deci et al. 1982, Rowan et al. 1997, Gordon et al. 2006) and teaching skills (Shavelson 1973, van de Grift et al. 2014)). However, these studies predominantly rely on self-reported surveys or qualitative methods limited to small-scale data. We extend this literature by developing a model from a content-based perspective to predict instructors’ performance in a scalable and automatic manner, which also provides interpretable insights that can help instructors and online education platforms enhance course creation and delivery in the future.

## 2.4. Natural Language Processing (NLP) and Transformer-Based Real-World Applications Transformer-Based Real-World Applications

NLP has been widely used in information systems research (Lee et al. 2018; Liu et al. 2018, 2020). As an advanced NLP tool, transformers have been utilized in addressing various real-world problems with signifi cant success, including humor detection, hate speech detection, fake news detection, and adverse drug reaction detection from tweets (Liu et al. 2019, Mao and Liu 2019, Mozafari et al. 2019, Breden and Moore 2020, Roitero et al. 2020). To the best of our knowledge, our paper is the first to develop a customized interpretable hierarchical transformer with contextual attention, and the first to apply such a model to a course corpus and achieve a significant performance result. Our paper also contributes to the growing literature on the development of customized deep learning models for business contexts in information systems research (Kokkodis and Ipeirotis 2021; Wang et al. 2021, 2022; Sun et al. 2022; Yang et al. 2022).

Table 1. Descriptive Statistics

<table><tr><td></td><td>Mean</td><td>SD</td><td>Median</td></tr><tr><td>No. of lectures/course</td><td>40.09</td><td>25.01</td><td>35.00</td></tr><tr><td>No. of tokens/lecture</td><td>1,158.87</td><td>855.50</td><td>969.00</td></tr></table>

## 3. Data

We collected a large-scale data set consisting of 1,085 free online courses available on Coursera. As the largest global platform of MOOCs, Coursera serves over 70 million learners globally and partners with more than 150 universities (Coursera 2020). The free courses on Coursera are readily accessible for learners to download. The descriptive statistics for these courses are shown in Table 1. On average, each course has about 40 lectures and each lecture has approximately 1,159 tokens.

Like most online platforms, Coursera primarily relies on user-generated ratings for assessing and communicating product quality. Two distinct ratings are displayed on the platform to indicate course quality: the course rating and the instructor rating. The course rating reflects the overall course experience as evaluated by enrolled students, whereas the instructor rating measures the quality of the instructor’s teaching collected through postcourse surveys. As Coursera puts it, “we asked all learners to give feedback on our instructors based on the quality of their teaching style.” Note that instructors with multiple courses will have different ratings for each course, based on the evaluations from students enrolled in each specific course. For each course, we observed aggregated average ratings without each individual student’s rating. The distribution of the two ratings is depicted in Figure 1. Both ratings range from 1 to 5. Most ratings in our data set skew toward the higher end, with a majority exceeding 3.5. However, a few ratings fall on the lower end of the scale, including some extremely low ratings (e.g., 2.5, 2.7).

Figure 1. (Color online) Distribution of Instructor and Course Ratings  
![](/api/attachments/JRFT3K43/fulltext/images/4aab84e3d338d3b0e8fa9dfc64aabfb6db0f446e9288c9fada5bc441745276d4.jpg)

## 4. Interpretable Hierarchical Transformer Model with Contextual Attention for Instructors’ Performance Prediction 4.1. Model Description

In our study, we developed an interpretable hierarchical transformer with contextual attention to predict instructors’ performance on online education platforms. Our model accounts for the inherent hierarchical struc ture of online courses and the sequential dependency of lectures within a course. In addition, it models various educational contexts with contextual attention, providing managerially relevant interpretability to assist both instructors and platforms.

The overall structure of our model is illustrated in Figure 2. Assume that $\left\{ \mathbf { x } _ { i } , \mathbf { c } _ { i } , y _ { i } \right\} _ { i = 1 } ^ { N }$ represents N courses, where $\mathbf { x } _ { i } = \{ \mathbf { l } _ { i 1 } , \mathbf { l } _ { i 2 } , \ldots , \mathbf { l } _ { i J _ { i } } \}$ is the i-th course’s subtitles with $J _ { i }$ lectures l. Each lecture $\mathbf { l } _ { i j }$ is a subtitle, represented by a sequence of tokens. $\mathbf { c } _ { i }$ denotes a contextual feature vector for course i, containing the academic discipline (e.g., arts, business, STEM), difficulty level (e.g., beginner, intermediate, advanced), duration (e.g., short, medium, long), and affiliation type (e.g., academic versus industry). y is the corresponding ground-truth label (i.e., ratings).

4.1.1. Local Transformer to Capture Lecture Semantic Features. We use a local transformer to learn from each individual lecture’s subtitle. For lecture j in course i where the subtitle sequence is denoted as $\begin{array} { r } { \mathbf { l } _ { i j } , } \end{array}$ , we add a special token [CLS] ([SEP]) at the beginning (end) of each lecture, and do a forward pass with the local transformer model. Then we take the mean pooling of all token embeddings and obtain the lecture representation $\mathbf { z } _ { i j } \in \mathbb { R } ^ { 1 \times H }$ for lecture j, where H is the hidden size $( \mathrm { e . g . }$ , 768 hidden units). For this process, we adopt the Bidirectional Encoder Representations from Transformers (BERT) model as the local transformer (Devlin et al. 2019).

![](/api/attachments/JRFT3K43/fulltext/images/8661c1abc05d7b8988dd8beb2505bece496a16be2ce35eb122f8db1fff0a315a.jpg)

Figure 2. (Color online) The Structure of Our Interpretable Hierarchical Transformer Model with Contextual Attention  
![](/api/attachments/JRFT3K43/fulltext/images/8a1463a4f61e68fe21b662ad696056b6294d8bcfc01191eced304c10d3251af1.jpg)

4.1.2. Global Transformers to Exchange the Lecture Information Within a Course. On top of the local transformer, we add global transformers to capture the inherent hierarchical structure of a course and the sequential dependency of lectures within a course. We take the sequence of all lectures’ representations $\begin{array} { r } { \mathbf { z } _ { i } = c o n c a t e ( \mathbf { z } _ { i 0 } , \mathbf { z } _ { i 1 } , \mathbf { z } _ { i 2 } , \dots , \mathbf { z } _ { i J _ { i } } , \mathbf { z } _ { i , j _ { i } + 1 } ) \in \mathbb { R } ^ { ( J _ { i } + 2 ) \times H } } \end{array}$ with two new special tokens, including $\mathbf { z } _ { i 0 } = [ C L S ]$ at the beginning and $\mathbf { z } _ { i , J _ { i } + 1 } = [ S E P ]$ at the end of the course. Here $c o n c a t e ( \cdot , \ldots , \cdot )$ is a function to concatenate vectors along the first dimension. The global transformers are used to exchange lecture token information within the same course. Here we use the vanilla transformer layer (Vaswani et al. 2017), which is composed of two sublayers,

$$
\mathbf {h} _ {i} ^ {l} = \mathrm{LayerNorm} (\mathbf {z} _ {i} ^ {l - 1} + \mathrm{MHAtt} (\mathbf {z} _ {i} ^ {l - 1})) \in \mathbb {R} ^ {(J _ {i} + 2) \times H},\tag{1}
$$

$$
\mathbf {z} _ {i} ^ {l} = \operatorname{LayerNorm} (\mathbf {h} _ {i} ^ {l} + \operatorname{FFN} (\mathbf {h} _ {i} ^ {l})) \in \mathbb {R} ^ {(J _ {i} + 2) \times H},\tag{2}
$$

where $l \geq 1$ , LayerNorm is a layer normalization proposed in Ba et al. (2016), MHAtt is the multihead attention mechanism introduced in Vaswani et al. (2017) which allows each token to attend to other tokens with different attention distributions, and FFN is a two-layer feed-forward network with ReLU as the acti vation function. Here $\mathbf { z } _ { i } ^ { l }$ represents the output of the lth global transformer layer, and $ { \mathbf { z } } _ { i } ^ { 0 }$ is the output of the local lecture semantic feature, that is, $\mathbf { z } _ { i }$

4.1.3. Contextual Attention. Educational contexts, such as academic discipline, difficulty level, and duration, are critical in understanding the differences among courses on online education platforms as well as in traditional education institutions. This contextual information is important in educational settings because they can capture inherent differences among courses. In our setting, Coursera uses such information to categorize its courses, a practice that is also prevalent on other online education platforms such as edX and Udacity.

Modeling such contextual information can help us understand how students’ evaluations of instructors’ performance may vary across different educational contexts. For example, although students typically rate a course based on the course content, their evaluations might inherently differ across various course contexts. This is because they might place different emphasis on the course materials, depending on the specific context. To capture this, we add contextual attentions to model the heterogeneity in course content emphasis influenced by course contexts. Our purpose is to use the contextual feature embeddings to weigh different lectures within a given course. The attention weights can serve as indicators of the extent to which each specific lecture contributes to the final prediction in each context. Specifically, we set up academic discipline embedding, difficulty level embedding, course duration embedding, and affiliation indicator embedding. These embeddings are used to incorporate the contextual information of each course and construct the con textual attention.

Here are more details for one specific head. Assume that the contextual feature embedding is $\mathbf { E } _ { c o n t e x t , ~ i , ~ k } \in$ $\mathbb { R } ^ { H \times 1 }$ for the k-th contextual features $c _ { i k } ,$ and the output for a course i of the global transformer is $\mathbf { z } _ { i } ^ { L } =$ $[ \pmb { z } _ { i 0 } ^ { L } , \mathbf { z } _ { i 1 } ^ { L } , \ \ldots , \mathbf { z } _ { i J _ { i } } ^ { L } , \mathbf { z } _ { i , J _ { i } + 1 } ^ { L } ]$ . The attention is constructed as follows:

$$
\operatorname{AttnMatrix} _ {\text { context }, i, k} = \mathbf {z} _ {i} ^ {L} \mathbf {E} _ {\text { context }, i, k} ^ {T} \in \mathbb {R} ^ {(J _ {i} + 2) \times 1}.\tag{3}
$$

To apply the attention matrix to the original value $( \mathsf { a } . \mathsf { k } . \mathsf { a } . \mathsf { z } _ { i } ^ { L } )$ , the output $\mathrm { A t t n M a t r i x } _ { \mathrm { c o n t e x t } } ^ { i }$ needs to be normalized as

$$
\begin{array}{c} \text {AttnProp} _ {\text {context}, i, k} = \text {Softmax} \left(\frac {\text {AttnMatrix} _ {\text {context} , i , k}}{\tau}\right) \\ \in \mathbb {R} ^ {(J _ {i} + 2) \times 1}, \end{array}\tag{4}
$$

where τ is the scaling parameter of the attention module which is $\scriptstyle { \frac { 1 } { \sqrt { H } } }$ (with H being the hidden size dimension), and Softmax(·) is performed along the first dimension.

The final weighted output is formulated as

$$
\mathbf {z} _ {\text {context}, i, k} = \operatorname{diag} (\mathrm{AttnProp} _ {\text {context}, i, k}) \mathbf {z} _ {i} ^ {L} \in \mathbb {R} ^ {(J _ {i} + 2) \times H},\tag{5}
$$

where diag(·) transforms the vector into a diagonal matrix.

Recall that we have multiple contextual features (four in our setting). By adding them all together, our overall contextual attention is as follows:

$$
\mathbf {z} _ {\text {context}, i} = \sum_ {k = 1} ^ {4} \mathbf {z} _ {\text {context}, i, k} \in \mathbb {R} ^ {(J _ {i} + 2) \times H}.\tag{6}
$$

We use the sum pooling to aggregate the course information from the local lectures:

$$
\hat {\mathbf {z}} _ {\mathbf {i}} = \sum_ {j = 1} ^ {J _ {i}} \mathbf {z} _ {c o n t e x t, i} ^ {j} \in \mathbb {R} ^ {H},\tag{7}
$$

where $\mathbf { z } _ { c o n t e x t , i } ^ { j }$ is the j-th lecture (a.k.a. j-th row) of ${ \mathbf { z } } _ { c o n t e x t , i }$ . We then feed $\hat { z } _ { i }$ into a linear layer to conduct the final rating prediction $\hat { y } _ { i }$ as

$$
\hat {y} _ {i} = <   W, z _ {i} > + b,\tag{8}
$$

where $\mathbf { W } \in \mathbb { R } ^ { H }$ denotes the weight matrix, $b \in \mathbb { R }$ denotes bias, and $< \cdot , \cdot >$ is the inner product function. Finally, we minimize the Euclidean distance between $\hat { y } _ { i }$ and $y _ { i }$ for all i to optimize our model.

## 4.2. Experiment Setup

We conducted experiments for two prediction tasks: instructor rating and course rating prediction. We conducted five-fold cross-validation for comparison. For each fold, we trained the model using two parts: one part for validation and the other for reporting as the test score. The validation set was used for hyperparameter tuning with all methods. We reported the average test results with standard deviation. Following Pappagari et al. (2019), we fine-tuned the local transformer (i.e., BERT) on the lecture level and used the pretrained $\mathrm { B E R T } _ { b a s e }$ with 12 layers to encode local semantic features from each lecture. Then, we added the global transformer layers and contextual attention to integrate the lecture-level embedding to the course level, and the output served as a course embedding. For the details of the model setup and hyperparameter tuning process, please refer to the Online Appendix.

To evaluate the performance of our model, we compared it with various baseline models as described below.

(1) Word2Vec + machine learning regressors: We used the pretrained Word2Vec embedding from the FastText<sup>1</sup> library to obtain a 300-dimensional word embedding. All words in the same course were joined together, and each course was represented as a weighted average of word embeddings in a course, following previous research (Asr et al. 2018, Qin and Yang 2019, Gupta et al. 2020).

The regression with extracted course textual features was conducted using seven machine learning algorithms to account for variability, including Linear Regression, Support Vector Machines with the radial-based kernel (SVM), Multilayer Perceptron (MLP), Random Forest, AdaBoost, GradientBoosting, and Bagging.

(2) Doc2Vec + machine learning regressors: We used the paragraph vector algorithm developed by Le and Mikolov (2014) to obtain 300-dimensional course embed dings. Using the Gensim implementation (Rehurek and Sojka 2010), Doc2Vec models for 20 epochs were trained, whereas words occurring fewer than 10 times in the respective training corpus were ignored following prior literature (Le and Mikolov 2014). All words in the same course were joined together as a document. We repeated the same machine learning algorithms and the hyperparameter tuning process as in item (1).

(3) LectureBERT: We also used advanced deep learning—a transformer variant, LectureBERT—as a baseline. LectureBERT does not have access to the course structure or contextual information. We assumed that lectures in the same course independently shared the same rating. We assigned the same rating score to the lectures in the same course for training. The model was trained to minimize loss on individual lectures in the training stage. In the test stage, we first made predictions for each lecture, and then averaged these predictions within the same course to obtain the course rating prediction. For the details of the hyperparameter tuning process for all baseline models, please refer to the Online Appendix.

We used two metrics to measure prediction performance: mean squared error (MSE)—the average squared differences between predicted and actual ratings—and mean absolute error (MAE)—the average absolute dif ferences between predicted and actual ratings, where all course differences have equal weight.

## 4.3. Experimental Results

4.3.1. Model Comparison. Table 2 shows the results of our model comparison using MSE and MAE for two prediction tasks: instructor rating and course rating. We report the mean and standard deviation of performance metrics across five folds. The results show that our model performs the best among all models, achieving an MSE of 0.0318 and an MAE of 0.1145 when predicting instructor rating, and an MSE of 0.0243 and an MAE of 0.1035 when predicting course rating. To test the statistical significance, we conducted paired t-tests between our model and the other models. The results show that our model significantly outperforms all other models.

Compared with 14 non-deep learning baseline methods, our model on average significantly reduced MSE by 29.40% $( p < 0 . 0 0 1 )$ ) and MAE by 23.57% $( p < 0 . 0 0 1 )$ for the instructor rating prediction task. Regarding the course rating prediction task, our model on average significantly reduced MSE by 25.90% $( p < 0 . 0 0 1 )$ and MAE by 19.68% $( p < 0 . 0 0 1 )$ ). In addition, our model also significantly outperformed the other transformer variant model—LectureBERT. Compared with Lecture-BERT, our model significantly reduced MSE by 19.41% $( p < 0 . 0 0 1 )$ and reduced MAE by 10.30% $( p < 0 . 0 0 1 )$ for the course rating prediction task, and reduced MSE by 19.19% $( p < 0 . 0 \bar { 0 } \bar { 1 } )$ and reduced MAE by 9.22% $( p <$ 0.001) for instructor rating prediction.

Table 2. Performance Comparison

<table><tr><td rowspan="2">Class</td><td rowspan="2">Model</td><td colspan="2">Instructor rating prediction</td><td colspan="2">Course rating prediction</td></tr><tr><td>MSE</td><td>MAE</td><td>MSE</td><td>MAE</td></tr><tr><td rowspan="7">Word2Vec + ML</td><td>Linear Regression</td><td>0.0762 ± 0.0260</td><td>0.1855 ± 0.0102</td><td>0.0584 ± 0.0148</td><td>0.1621 ± 0.0118</td></tr><tr><td>SVM</td><td>0.0472 ± 0.0027</td><td>0.1449 ± 0.0053</td><td>0.0337 ± 0.0030</td><td>0.1195 ± 0.0056</td></tr><tr><td>MLP</td><td>0.0456 ± 0.0030</td><td>0.1473 ± 0.0069</td><td>0.0333 ± 0.0031</td><td>0.1291 ± 0.0072</td></tr><tr><td>Random Forest</td><td>0.0397 ± 0.0025</td><td>0.1386 ± 0.0088</td><td>0.0305 ± 0.0022</td><td>0.1244 ± 0.0036</td></tr><tr><td>AdaBoost</td><td>0.0446 ± 0.0030</td><td>0.1604 ± 0.0141</td><td>0.0321 ± 0.0035</td><td>0.1335 ± 0.0099</td></tr><tr><td>GradientBoosting</td><td>0.0423 ± 0.0032</td><td>0.1414 ± 0.0096</td><td>0.0298 ± 0.0022</td><td>0.1208 ± 0.0035</td></tr><tr><td>Bagging</td><td>0.0444 ± 0.0035</td><td>0.1481 ± 0.0098</td><td>0.0335 ± 0.0018</td><td>0.1303 ± 0.0034</td></tr><tr><td rowspan="7">Doc2Vec + ML</td><td>Linear Regression</td><td>0.0509 ± 0.0086</td><td>0.1730 ± 0.0142</td><td>0.0348 ± 0.0045</td><td>0.1370 ± 0.0089</td></tr><tr><td>SVM</td><td>0.0415 ± 0.0041</td><td>0.1532 ± 0.0054</td><td>0.0301 ± 0.0030</td><td>0.1316 ± 0.0070</td></tr><tr><td>MLP</td><td>0.0463 ± 0.0024</td><td>0.1507 ± 0.0069</td><td>0.0326 ± 0.0029</td><td>0.1285 ± 0.0058</td></tr><tr><td>Random Forest</td><td>0.0402 ± 0.0028</td><td>0.1341 ± 0.0077</td><td>0.0297 ± 0.0026</td><td>0.1192 ± 0.0038</td></tr><tr><td>AdaBoost</td><td>0.0460 ± 0.0041</td><td>0.1614 ± 0.0151</td><td>0.0312 ± 0.0033</td><td>0.1319 ± 0.0063</td></tr><tr><td>GradientBoosting</td><td>0.0401 ± 0.0043</td><td>0.1385 ± 0.0109</td><td>0.0301 ± 0.0029</td><td>0.1219 ± 0.0071</td></tr><tr><td>Bagging</td><td>0.0422 ± 0.0037</td><td>0.1376 ± 0.0123</td><td>0.0315 ± 0.0032</td><td>0.1240 ± 0.0054</td></tr><tr><td rowspan="2">Transformer variants</td><td>LectureBERT</td><td>0.0394 ± 0.0034</td><td>0.1261 ± 0.0038</td><td>0.0301 ± 0.0039</td><td>0.1153 ± 0.0062</td></tr><tr><td>Ours</td><td>0.0318 ± 0.0040</td><td>0.1145 ± 0.0040</td><td>0.0243 ± 0.0034</td><td>0.1035 ± 0.0044</td></tr></table>

Notes. Our model significantly outperforms all benchmark methods (p < 0.001). We conducted five-fold cross-validation to compute th standard deviation of the MSE and MAE. We then conducted paired t-tests between our model and all other models to identify the statistica significance. ML, machine learning

4.3.2. Ablation Study. In addition to the overall model comparison, we also conducted an ablation study to evaluate the predictive power of each component of our model and explain the superiority of our model. Overall, our model has two components and we remove them step by step to quantify the performance change. The performance change is summarized in

Figure 3. We plotted the mean and standard deviation across five folds along two performance metrics for comparison. We also conducted paired t-tests to identify the statistical significance of performance change. Specifically, the following three models are compared for the ablation study: (i) our proposed model; (ii) our proposed model without contextual attention, but still with the hierarchical structure; and (iii) LectureBERT— we further remove the hierarchical structure from (ii). Comparing (i) and (ii) can quantify the contribution of the contextual attention, whereas comparing (ii) and (iii) can quantify the contribution of the hierarchical structure.

Figure 3. (Color online) Ablation Study  
Note. Each component of our model provides significant performance gain.  
![](/api/attachments/JRFT3K43/fulltext/images/68e41bc71018c64a0edf1983e894a9563dc5f796aba39b355ec04196a2383209.jpg)

First of all, we remove the contextual attention from our model and quantify the performance gain resulting from this component. Compared with the proposed model without contextual attention, our model provides a significant 3.85% MSE $( p = 0 . 0 0 6 )$ performance gain and 2.02% MAE $( p = 0 . 0 0 4 )$ performance gain for instructor rating prediction. For course rating prediction, our model provides a significant 4.85% MSE $( p =$ 0.009) performance gain and 2.01% MAE $( p = 0 . 0 0 8 )$ performance gain compared with the proposed model without contextual attention.

(b) MAE  
![](/api/attachments/JRFT3K43/fulltext/images/26d0cbdd2b59bfe18632e40b9e03475208b1c1c492fbd90c7662b026c779257d.jpg)

After removing the contextual attention, we further remove the hierarchical structure from our model and quantify the performance gain of the global-local hierarchical structure. Compared with LectureBERT, the hierarchical structure in the proposed model provides a significant 15.95% MSE $( p < 0 . 0 0 1 )$ ) performance gain and 7.35% MAE $( p < 0 . 0 0 1 )$ performance gain for instructor rating prediction. For course rating prediction, the hierarchical structure in the proposed model provides a significant 15.30% MSE $( p < 0 . 0 0 1 )$ performance gain and 8.46% MAE $( p < 0 . 0 0 1 )$ performance gain compared with LectureBERT.

In summary, each component of our model provides significant gains. On the one hand, hierarchical globallocal hierarchical structure provides a large proportion of performance gains. This indicates that the online course has a strong hierarchical structure and sequential dependency; thus, capturing such information is vital for accurate prediction. In addition, the contextual attention also provides additional gain. This indicates that predicted student ratings on instructors’ performance might vary under different educational contexts, and modeling such information can further improve the performance.

## 5. Decision Support Showcase: Assisting Instructors with Model Interpretability

Although deep learning models have been successful in prediction and automation, they are usually considered to be black boxes because of people’s concerns regarding model interpretability. A key benefit of our model is that it goes beyond prediction and enables interpretability analysis, which can provide valuable insights into the potential underlying mechanisms driving the model’s predictions made by the model. In this section, we showcase in-depth interpretability analysis to uncover managerial insights learned from the model, which can provide actionable suggestions for instructors.

Specifically, we conducted interpretability analysis at three different levels, including (1) lecture-level analysis wherein we used the model’s learned contextual attention weights to analyze lecture importance in final predictions across different educational contexts, (2) sentence-level analysis wherein we employed a twostage counterfactual prediction strategy to identify specific sentences that negatively impact predicted ratings, and (3) word-level analysis wherein we constructed multiple interpretable word-level verbal cues and explored their potential effects on predicted ratings.

## 5.1. Lecture-Level Interpretability Analysis

For the lecture-level interpretability analysis, we used the model-learned contextual attention weights to visualize the lecture importance across different contexts. Given that courses may consist of a varying number of lectures, we partitioned each course’s lectures into five equal chunks (i.e., first 20%, 20%–40%, 40%–60%, $6 0 \% { - } 8 0 \% , 8 0 \% { - } 1 0 0 \% )$ for comparison purposes. Then, we plotted the mean and standard deviation of the contextual attention weights for lectures corresponding to each chunk.

Firstly, we visualized the contextual attention weights across different academic disciplines in Figure 4. The distribution of learned lecture importance displayed considerable variation across these disciplines. In particular, for courses in arts, social sciences, and humanities, a convex curve trend emerged wherein the initial lec tures highly contributed to rating predictions, with a gradual decline in importance for lectures in the middle before surging again toward the end. This was likely because in fields like performing arts, the first impression usually has a dominating influence on the audience’s evaluation of the performer (Williamon 2004, Platz and Kopiez 2013). In these disciplines, the first impressions instructors give to the students in initial lec tures may significantly influence students’ perceptions and evaluations. Moreover, the last few lectures consistently showed a large impact on predicted ratings across all disciplines, with an average lecture importance exceeding 0.9 in the final chunk. This was likely due to the recency effect frequently observed in learning environments (Jones and Sieck 2003). From a student’s per spective, the last few lectures are more recent and better recalled, which might have considerable influence over their course evaluations. Our findings suggest that these lectures, accordingly, may require particular attention when instructors prepare their teaching materials.

For STEM courses, we observed a different upward trend, with lecture importance in predicting ratings progressively escalating from start to finish. Because STEM course content usually has strong sequential dependencies, where early lectures cover simpler topics and more challenging subjects are saved for later, students’ evaluations of instructors’ performances in these courses could hinge primarily on the quality of the more complex segments. This highlights the need for instructors to dedicate extra attention and efforts to these lectures. For business courses, we observed a relatively flat trend, with average lecture importance consistently exceeding 0.9 across all five chunks. This indicates that lectures in these courses hold roughly equal importance in rating predictions. For example, a digital marketing course often consists of topics such as search engine marketing, social media, and content marketing, whereas an entrepreneurship course usually covers aspects of management, markets, and strategy.

Figure 4. (Color online) Model-Learned Attention Weights Across Academic Disciplines  
(a) Arts, Social Sciences, and Humanities  
![](/api/attachments/JRFT3K43/fulltext/images/87653205e786a7bf026a869156fec33e2803c7c526adf75f156abc3669277953.jpg)

(b) Business  
![](/api/attachments/JRFT3K43/fulltext/images/83fdd65ce18913d21d892fb29d8bb77435aa3be346a42941b9d8faef00b95a81.jpg)

(c) STEM  
![](/api/attachments/JRFT3K43/fulltext/images/f5ea4f479e004def278ed8371826e1f7da19231230ebd9d0139d39a44ed71809.jpg)  
Notes. x-axis refers to lecture chunks, and y-axis refers to learned contextual attention weights. For improved visualization, attention bars hav been normalized by the maximum attention value across all bars.

Unlike STEM courses, these sessions tend to be more independent, complementing rather than building upon each other. Given the practical and professional orientation of business courses, the importance of different lectures in predicting final ratings might exhibit less variability.

Secondly, we analyzed the course difficulty level and plotted the corresponding attention weights in Figure 5, which shows interesting heterogeneous patterns. For beginner-level courses, where most topics are relatively simple, and for courses lacking specific difficulty labels, we observed a relatively flat trend, with average lecture importance above 0.8 across all five chunks. However, for intermediate-level and advanced-level courses, we found an upward trend where later, more complex lectures contribute more to rating predictions. In addition, the slope of this upward trend increased with the difficulty level, as shown in Figure 5. This suggests that lectures covering more challenging topics could heavily influence students’ course evaluations. Given the inherent complexity of teaching advanced materials, which often builds upon concepts covered in earlier lectures, our results suggest that such lectures may require particular attention during online teaching preparation.

Thirdly, we analyzed course duration and plotted the corresponding attention weights in Figure 6. We found that for courses of medium and long duration, all lectures displayed similar weights, with an average value consistently above 0.8 across all chunks. However, for courses of short duration, lectures in the latter part of the course contributed more to rating predictions, whereas the earlier lectures had less impact. This suggests that for shorter courses, students may tend to discount initial lectures and place greater emphasis on those toward the end of the course, which are likely fresher in memory, when making final course evaluations.

Lastly, we examined the course’s affiliation type (i.e., academic course versus industry course) and plotted their attention weights in Figure 7. We found that academic courses featured a more uniform distribu tion of weights across different lectures. In contrast, industry courses showed an increasing importance of lectures from the beginning to the end. This trend was likely because instructors from industries, rather than academia, are usually not full-time instructors. Consequently, it may take more time for them to become familiar with online teaching, and it may also require extra effort for them to establish trust with students who might perceive them as lacking prior teaching experience.

Figure 5. (Color online) Model-Learned Attention Weights for Courses at Different Difficulty Levels  
(a) Beginner-Level  
![](/api/attachments/JRFT3K43/fulltext/images/2e3616c05c1f168c22d7814e16fceac47846886d4eb3aac8f940bc84a236c44a.jpg)

(b) Intermediate-Level  
![](/api/attachments/JRFT3K43/fulltext/images/4ce8414ef89c9440320348d75fb6088c198356b8986469114fb7c8048936fbfc.jpg)

(c) Advanced-Level  
![](/api/attachments/JRFT3K43/fulltext/images/027b62258a44d1adda12d0e85e7f7901f5f8e21e3ee007d584daea87ba7d1f25.jpg)

(d) No Level Labeled  
![](/api/attachments/JRFT3K43/fulltext/images/beaf737620ef2c640f02b19e718a899e11570431a436ee3e8c6ebe055e2b15b8.jpg)  
Note. x-axis refers to the lecture chunks, and y-axis refers to the learned contextual attention weights

Overall, our findings provide interpretable insights into which lectures require particular attention when producing different types of online courses. These insights can serve as valuable starting points for instructors and platforms when preparing and scripting course materials. Next, we will conduct a more granular analysis to uncover further insights at the sentence level and word level.

## 5.2. Sentence-Level Interpretability Analysis

This section delves into our sentence-level interpretability analysis. We leverage the hierarchical global-local transformer architecture of our model and a two-stage counterfactual prediction strategy to identify potential sentences that might negatively influence the rating. We focus on instructor rating predictions to demonstrate this. In the first stage, we sequentially masked each lecture to obtain counterfactual rating predictions. A rise in predicted rating after removing a lecture implies that the lecture may have negatively affected the predictions. We collected such “bad” lectures if the counterfactual prediction was higher than the original prediction. In the second stage, we masked sentences one by one within each “bad” lecture and obtained counterfactual predictions in a similar manner. We collected the sentences if the counterfactual prediction (after removing that sentence) was higher than the orig inal prediction. These sentences could potentially have a negative impact on the predicted rating. For clarity, we refer to them as “bad sentences” in the subsequent analysis.

Next, we investigated why these sentences might negatively influence course evaluations. We selected the top 1,000 bad sentences based on the difference between the counterfactual prediction and the original prediction. For a meaningful comparison, we also selected the top 1,000 good sentences that likely had a positive impact on the predictions. We collected those sentences for which the counterfactual prediction after removing it was lower than the original prediction.

(b) Industry Course  
Figure 6. (Color online) Model-Learned Attention Weights for Courses of Different Duration  
![](/api/attachments/JRFT3K43/fulltext/images/88317afba0747ae5fd6a1fb668ab55a443147a44f54e91f3ccc91e3d051fac06.jpg)

![](/api/attachments/JRFT3K43/fulltext/images/356d8228baf7c2e1da21a16ec2a75d499836a5c2c5eadbc3dc06180ec1156be6.jpg)

![](/api/attachments/JRFT3K43/fulltext/images/f1594c47a2e73246ff77cac79688c53ac49079f1563bbb9ef05d7b690ce5db8f.jpg)  
Note. x-axis refers to lecture chunks, and y-axis refers to learned contextual attention weights.

Based on this sample, we compared the characteristics of these sentences across various dimensions, including topic and context relevance, part-of-speech tagging, and inappropriate language usage.

5.2.1. Relevance. Relevance is the extent to which text segments are germane to the reader’s goals and purposes (Lehman and Schraw 2002). Studies in prior literature have shown that the relevance of information increases people’s recall of text segments (Schraw et al. 1993, Di Vesta and Di Cintio 1997); plays an important role in their selecting, allocation attention $^ { \mathrm { t o , } }$ and remembering text segments (Narvaez et al. 1999); and enhances deeper text processing (Lehman and Schraw 2002). In the context of online education, the relevance of instructors’ language to the topic may play an important role in students’ perception and learning. To account for its potential effect in the online education setting, we analyzed the relevance between selected sentences and the main topic of the course, quantifying it using four different measurements to ensure robustness.

Figure 7. (Color online) Model-Learned Attention Weights for Courses with Different Affiliations  
![](/api/attachments/JRFT3K43/fulltext/images/a280c1d021d888fee0163f69ce6075b47405193993ec80a3da860861efa40aab.jpg)  
Note. x-axis refers to lecture chunks, and y-axis refers to learned contextual attention weights.

![](/api/attachments/JRFT3K43/fulltext/images/43f01e4f2cc7f08f1e8493bd97e3254f88ede21dfb9d102177d5d73ba22a4b47.jpg)

Firstly, we measured topic relevance based on the first three sentences of each lecture, because instructors typically provide a brief overview of the teaching content at the beginning of the lecture. This can reflect the lecture’s main topic. Secondly, we used the entire lecture’s text in subtitle to measure the main topic of the course. Thirdly, we collected each module’s<sup>2</sup> title and description from Coursera. These elements capture the main topics covered in each module, thus being suitable for our analysis. We then quantified the main topic of each course based on titles and descriptions, respectively. To measure the relevance between selected sentences and the main topic of the course, we first used pretrained Word2Vec models to obtain the word embedding, and then took the average of word embedding in each sentence to represent the whole sentences. We calculated the sentence embedding for both bad and good sentences in our sample, as well as for each of the four main topic measurements. Then we quantified the relevance using cosine similarity between sentences and main topic measurements. We show the box plots of relevance score in Figure $8 ( \mathrm { a } )$ . We found that all good sentences were significantly more relevant to the main course topic than bad sentences $( p < 0 . 0 0 1 )$ . This finding was consistent and robust when we used different metrics to quantify the course’s main topic. Our results indicate that bad sentences usually diverged from the main topic of the course, which likely had a negative impact on the predicted rating.

We also quantified the context relevance of sentences based on their similarity to neighboring sentences. As can be seen in Figure 8(b), bad sentences generally showed less relevance to their neighboring sentences, which might make them appear disconnected from the context and lead to a negative impact on the predicted rating.

5.2.2. Part-of-Speech Tagging. We adopted ${ \mathrm { N L T K } } ^ { 3 }$ to classify words into their parts of speech and label them as nouns, verbs, adjectives, and adverbs. We first obtained the tagging and then calculated the ratio of each tagging for each sentence. This ratio was measured as the total number of each tagging (e.g., nouns) divided by the total token length for each sentence. We plot the ratio dis tribution in Figure $9 ( \mathrm { a } )$ . We found that bad sentences used significantly more descriptive words $( \mathrm { e . g . , \ a d j e c { - } }$ tives and adverbs) than did good sentences $( p < 0 . 0 0 1 ) .$ whereas good sentences used more objective words $( \mathrm { e . g . , }$ nouns and verbs) than did bad sentences $( p < 0 . 0 0 \bar { 1 } )$ Our results suggest that flowery language might negatively affect the predicted course evaluations, whereas more straightforward and plain language may lead to higher predicted ratings in the context of online learning.

5.2.3. Offensive and Hateful Language Usage. We detected instances of offensive and hateful language using Twitter-roBERTa-base (Barbieri et al. 2020). We found that bad sentences had higher offensiveness and hatefulness scores than good sentences $( p < 0 . 0 0 1$ for the hatefulness score) as illustrated in Figure 9(b). Our results suggest that although there appear to be fewe restrictions and more freedom in the online setting compared with traditional physical classrooms, instructors should still avoid offensive or hateful language as it might negatively impact their predicted ratings.

## 5.3. Word-Level Interpretability Analysis

Choosing the right words when conveying ideas to an audience is of great importance in a variety of contexts, such as education, marketing, and politics. In this section, we discuss detailed interpretability analysis at the word level to provide insights for instructors, which could serve as starting points to guide their choice of vocabulary in the development of teaching materials.

Figure 8. (Color online) Comparison of Good vs. Bad Sentences Based on Two Types of Relevance  
(a) Relevance With Five Main Topics Measurements  
![](/api/attachments/JRFT3K43/fulltext/images/8c122566dcbb8e79419ae56e8534ced36e045a1db43a040cdb50782d27b04369.jpg)

(b) Relevance With Neighboring Sentences  
![](/api/attachments/JRFT3K43/fulltext/images/c21631281fe9beffb1ded959f530aeabb3946e2db1f6f756d6a5f5f70086f8d4.jpg)

Figure 9. (Color online) Comparison of Good vs. Bad Sentences Based on Part of Speech and Inappropriate Language  
![](/api/attachments/JRFT3K43/fulltext/images/6275137addecf5240a3f81a32450c1b4f4170132c7a831063c124826d4699ee2.jpg)

In this analysis, we extracted five linguistic features at the word level by gathering existing hand-crafted, linguistic lexicons for relevant concepts (i.e., named entity ratio, WH-word usage ratio, emotional word usage diversity, ratio of strong modal words, and ratio of weak modal words).<sup>4</sup> We then conducted a correlation analysis and a counterfactual prediction analysis to explore their potential impacts on the predicted ratings.

5.3.1. Named Entity Ratio. Keith and Stent (2019) used the named entity ratio to quantify the concentrated speaking of financial analysts in earnings calls. In a similar vein, a higher named entity ratio in our context might indicate concentrated teaching content and less unrelated material. To quantify this ratio, we first counted the total number of named entities for each course in our data using OntoNotes,<sup>5</sup> which includes five broad categories: (1) events, (2) numbers, (3) organizations/locations, (4) persons, and (5) products. Then, the named entity ratio was calculated as the total number of named entities in the course divided by the total number of tokens in that course.

5.3.2. WH-Word Usage Ratio. Prior studies suggest that asking questions in class can stimulate students’ thinking and interaction (Clough 2007, Olsher and Kantor 2012). To quantify instructors’ question-asking behavior in our data, we used Basic Parse Tree created by Stanford’s CORE ${ \mathrm { N L P } } ^ { 6 }$ to calculate the WH-word usage ratio,<sup>7</sup> which is defined as the total number of sentences containing WH-words divided by the total number of sentences in a given course. Specifically, we checked for the occurrence of two tags: (1) SBARQ—direct question introduced by a WH-word or WH-phrase, indirect questions—and (2) SQ—inverted yes/no questions, or main clause of a WH-question, following the WH-phrase in SBARQ. A higher WH-word usage ratio might indicate that the instructor prefers to ask more questions during teaching, which may encourage student thinking and interaction.

(b) Offensive and Hateful Language Usage  
![](/api/attachments/JRFT3K43/fulltext/images/5153e2faa8461d6fafd47a409ce474a6f43b9a08ae6e8cd9017503b8579ac794.jpg)

5.3.3. Emotional Word Usage Diversity. Prior research shows that instructors’ elicitation of emotions may attract students’ attention while learning (Wang et al. 2019). In our analysis, we used NRC Sentiment Lexi cons (Mohammad et al. 2013) to extract each instructor’s emotional word usage across eight dimensions: anticipation, joy, surprise, trust, anger, disgust, fear, and sadness. We then calculated the emotion entropy to measure the diversity of an instructor’s emotional word usage, which is defined as $\begin{array} { r } { - \sum _ { i = 1 } ^ { 8 } r _ { i } \times l o g ( r _ { i } ) . } \end{array}$ where $r _ { i }$ denotes the ratio of emotion tokens to total tokens for each specific emotion dimension i.

5.3.4. Strong/Weak Modal Word Usage. A modal adverb is a lexical marker that is used to illustrate different levels of certainty and uncertainty (Suzuki and Fujiwara 2017). For example, the modal adverbs “undoubtedly” and “possibly” convey different levels of certainty, with the former indicating certainty and the latter uncertainty. We computed the ratios of (1) strong modal words such as “always,” “clearly,” and “undoubtedly” and (2) weak modal words such as “appears,” “maybe,” and “possibly” using the respective lexicons from Loughran and McDonald (2011). In each case, the ratio of terms in the respective category to the number of tokens in each course was calculated.

5.3.5. Correlation Analysis. We present the results of the correlation analysis in Table 3, which shows some interesting patterns that could provide initial guidance for instructors in an online education setting to enhance their teaching evaluations in the future. Below, we discuss the statistically significant results for positive (+) and negative (�) correlations with the ratings.

5.3.5.1. (<sup>1</sup>) WH-Word Ratio. We found that the WH-word ratio was significantly positively associated with student ratings. A potential explanation for this is that asking questions may enhance students’ learning experience by encouraging students’ thinking and capturing attention in online classes, despite the inherent lack of direct interaction in the online education setting.

Table 3. Results from Pearson Correlations Between Word-Level Verbal Cues and Rating

<table><tr><td>Word-level verbal cues</td><td>Corr with instructor rating</td><td>Corr with course rating</td></tr><tr><td>Named entity ratio</td><td>0.02</td><td>0.01</td></tr><tr><td>WH-word ratio</td><td>0.09**</td><td>0.04*</td></tr><tr><td>Emotional word usage diversity</td><td>0.16***</td><td>0.17***</td></tr><tr><td>Strong modal word usage</td><td>-0.12***</td><td>-0.11**</td></tr><tr><td>Weak modal word usage</td><td>0.08**</td><td>0.04</td></tr></table>

\*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

5.3.5.2. (<sup>1</sup>) Emotional Word Usage Diversity. The diversity of emotional word usage was significantly positively associated with student ratings. A potential explanation for this is that the use of diverse emotional words might catch students’ attention and maintain their engagement in online classes. This is important for online courses where students have greater flexibility and freedom. For example, unlike a traditional classroom where there are direct interactions and eye contact between the instructor and students, in an online education setting, students can leave the class at any time, making it even more challenging for the instructor to keep students engaged.

5.3.5.3. (<sup>2</sup>) Strong Modal Word Usage. Strong modal words such as “always,” “clearly,” and “undoubtedly” were significantly negatively associated with student ratings. This could be due to the perception of a high ratio of strong modal verbal cues in a course as an indicator of the instructor’s dominance. Prior literature (Tost et al. 2013) suggests that overly dominant leaders might stifle team creativity, leading to subpar performance. Similarly, Wang and Li (2021) showed that dominant speakers might make an audience less openminded, potentially hurting the overall engagement.

5.3.6. Counterfactual Prediction Analysis. To further demonstrate the applicability of our model, we conducted a counterfactual prediction analysis to examine to what extent the instructors’ performance might be improved by modifying their verbal cues. We here discuss the analysis for the strong modal word usage as an example. In our data set, about 98% of courses included strong modal words in the course content. On average, about 74 strong modal words were used in a course. In the most extreme case, an instructor in our data used 384 strong modal words in their lectures. We removed all the strong modal words from our course corpus and obtained the counterfactual predictions accordingly. We found that by removing the strong modal words, the predicted rating could be signifi cantly improved by 0.028% on average across the courses $( p < 0 . 0 0 1 )$

Finally, we caution that our focus in this research is on predictive models, and we do not make any claims of causality. Nonetheless, our predictive results and interpretability analyses offer important managerial insights given the current lack of understanding of how exactly course content affects its product performance on online education platforms.

## 6. Decision Support Showcase: Assisting Educational Platforms with Accurate Predictions

From the platform’s perspective, our developed meth odology can be directly used for tasks such as search engine design, course recommendations, and product quality control. Specifically, when instructors submit their recorded lectures, the platform can utilize our model to assess the quality based on the predicted rat ings. This predictive ability assists platforms in overcoming cold-start problems, allowing them to prioritize the recommendation of high-quality courses over those predicted to have lower ratings. Currently, evaluating the quality of an online course is still very costly as it is labor-intensive to review the entire course content before making a fair evaluation. Our model can be used to effectively complement human experts in this pro cess. For example, when expert evaluators are con strained for time, or faced with the task of assessing an overwhelming number of courses, our model can serve as an invaluable tool for initial screening. By predicting potential ratings, our model can provide a preliminary ranking of courses, offering a useful starting point for experts and platforms in their decision-making processes. Based on evaluations from millions of online students, our system can facilitate product quality evaluation in an accurate, scalable, and automatic manner. Moreover, the predicted ratings could also be used to inform the platform’s recommendation algorithms and the search engine design, enabling the prioritization of high-quality courses in the ranking process.

To further demonstrate the value and applicability of our model, we conducted a randomized experiment on Amazon Mechanical Turk (AMT) to illustrate how our tool can be used to assist platforms with accurate predictions. Specifically, we demonstrated our model’s applicability to the course ranking problem. In this experiment, we generated two distinct course ranking lists: one based on the top 10 ratings predicted by our model, which we’ll refer to as the algorithm-generated list for brevity, and another featuring 10 randomly selected courses, known as the randomly generated list. We then presented these two lists to 100 AMT workers and asked for their preference. Each list was designed to mirror the presentation on Coursera, displaying brief information for each of the 10 courses, including the course title, course level, a short description, and a “learn more” button that allowed the workers to access a separate web page for each course. This separate web page contained a course summary and a detailed syllabus. Further details about the web page design and experiment specifics are provided in the Online Appendix.

In the task instructions, we asked the AMT workers to carefully review the content of both ranking lists. After that, we asked them different questions to assess their preferences between these two lists. Our results from the experiment indicated a clear preference, with 71% of workers favoring our algorithm-generated list. In addition, the average rating for the algorithm-generated list (mean � 4.20) was significantly higher than that for the randomly generated list (mean � 3.72, p < 0.001), further substantiating the efficacy of our model.

## 7. Conclusions

In this paper, we develop an interpretable hierarchical transformer with contextual attention for predicting instructors’ performance in the online education context using unstructured course content. Our research provides immediate and actionable implications for stakeholders in online education by developing a practical tool for them to accurately predict teaching performance online, which is important not only for business success but also for the success of online instruction more broadly in our society.

Our study has substantial implications for online education platforms, instructors, and students. For online education platforms, our tool can be directly used for tasks like search engine design, course recommendation systems, and product quality management. For instructors, our tool can provide automated rating predictions and interpretable insights to guide improvements in future teaching content design. Students stand to benefit from enhanced product quality control on online education platforms and improved teaching performance.

Although we believe that our model and findings represent an important advancement in predicting student ratings using unstructured course data, there are several limitations to our research. First, although student rating is a widely used measure of teaching quality, other metrics such as the course completion ratio are also important, which could be further explored by future researchers if these data become accessible. Second, in the context of online education, examining student learning is important. Regrettably, because of privacy concerns, platforms like Coursera and many others do not disclose students’ homework or test grades, preventing us from incorporating such a measure into our study. It would be valuable for future studies to investigate how course content impacts students’ learning outcomes. Finally, our data are observational, and thus we are not able to claim causal effects. It would be useful for future studies to experimentally analyze the causal impact of course content and structure on students’ evaluations on the instructors.

## Endnotes

<sup>1</sup> FastText is a library for efficient learning of word representations and sentence classification.

<sup>2</sup> A module is a set of lectures that belong to a common topic.

<sup>3</sup> NLTK is a leading platform for building Python programs to work with human language data.

<sup>4</sup> Note that we do not intend to perfectly measure these quantities but rather to provide some interpretable insights at the word level.

<sup>5</sup> See OntoNotes Release 5.0, Section 2.6: https://catalog.ldc.upenn. edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf.

<sup>6</sup> See https://stanfordnlp.github.io/CoreNLP/.

<sup>7</sup> WH-words are used to introduce questions and relative clauses. The main WH-words are why, who, which, what, where, when, and how.

## References

Adamopoulos P (2013) What makes a great MOOC? An interdisciplinary analysis of student retention in online courses. 34th Internat. Conf. Inform. Systems ICIS 2013 (Association for Information Systems, Atlanta), 13.

Algozzine B, Gretes J, Flowers C, Howley L, Beattie J, Spooner F, Mohanty G, Bray M (2004) Student evaluation of college teaching: A practice in search of principles. College Teaching 52(4): 134–141.

American Marketing Association (2020) Higher education marketing statistics before and during the covid-19 pandemic. Retrieved August 24, 2020, https://www.ama.org/marketing-news/highereducation-marketing-statistics-before-and-during-the-covid-19- pandemic/.

Asr FT, Zinkov R, Jones M (2018) Querying word embeddings for similarity and relatedness. Walker M, Ji H, Stent A, eds. Proc. 2018 Conf. North Amer. Chapter Assoc. Comput. Linguistics Human Language Tech., vol. 1 (Long Papers) (Association for Computa tional Linguistics, Kerrville, TX), 675–684.

Ba JL, Kiros JR, Hinton GE (2016) Layer normalization. Preprint, submitted July 21, https://arxiv.org/abs/1607.06450.

Barbieri F, Camacho-Collados J, Neves L, Espinosa-Anke L (2020) TweetEval: Unified benchmark and comparative evaluation for tweet classification. Preprint, submitted October 23, https:// arxiv.org/abs/2010.12421.

Benton SL, Cashin WE (2014) Student ratings of instruction in college and university courses. Paulsen M, ed. Higher Education: Handbook of Theory and Research (Springer, Dordrecht, Nether lands), 279–326.

Breden A, Moore L (2020) Detecting adverse drug reactions from Twitter through domain-specific preprocessing and BERT ensembling. Preprint, submitted May 11, https://arxiv.org/abs/2005. 06634.

Chatterjee A, Ghosh C, Bandyopadhyay S (2009) Assessing students rating in higher education: A SERVQUAL approach. Total Quality Management Bus. Excellence 20(10):1095–1109.

Clough MP (2007) What is so important about asking questions? Iowa Sci. Teachers J. 34(1):2–4.

Costin F, Greenough WT, Menges RJ (1971) Student ratings of col lege teaching: Reliability, validity, and usefulness. Rev. Ed. Res. 41(5):511–535.

Coursera (2020) Coursera 2020 impact report. Retrieved August 24, 2020, https://about.coursera.org/press/wp-content/uploads 2020/09/Coursera-Impact-Report-2020.pdf.

Deci EL, Spiegel NH, Ryan RM, Koestner R, Kauffman M (1982) Effects of performance standards on teaching styles: Behavior of controlling teachers. J. Ed. Psych. 74(6):852–859.

Dellarocas C, Van Alstyne MW (2013) Money models for MOOCs. Comm. ACM 56(8):25–28.

Devlin J, Chang MW, Lee K, Toutanova K (2019) BERT: Pretraining of deep bidirectional transformers for language understanding. Burstein J, Doran C, Solorio T, eds. Proc. 2019 Conf. North Amer. Chapter Assoc. Comput. Linguistics Human Language Tech. (Association for Computational Linguistics, Kerrville. TX), 4171–4186.

Di Vesta FJ, Di Cintio MJ (1997) Interactive effects of working memory span and text context on reading comprehension and retrieval. Learn. Individual Differences 9(3):215–231.

Feldman KA (1977) Consistency and variability among college students in rating their teachers and courses: A review and analy sis. Res. Higher Ed. 6(3):223–274.

Feng W, Tang J, Liu TX (2019) Understanding dropouts in MOOCs. Proc. AAAI Conf. Artificial Intelligence 33(01):517–524.

Gordon RJ, Kane TJ, Staiger D (2006) Identifying Effective Teachers Using Performance on the Job (Brookings Institution, Washington, DC).

Gupta V, Saw A, Nokhiz P, Netrapalli P, Rai P, Talukdar P (2020) P-SIF: Document embeddings using partition averaging. Proc. AAAI Conf. Artificial Intelligence 34(05):7863–7870.

Huang N, Zhang J, Burtch G, Li X, Chen P (2021) Combating procrastination on massive online open courses via optimal calls to action. Inform. Systems Res. 32(2):301–317.

IBISWorld (2020) Educational services in the US market size 2005–2026. Retrieved August 24, 2020, https://www.ibisworld. com/industry-statistics/market-size/educational-services-unitedstates/.

Jones M, Sieck WR (2003) Learning myopia: An adaptive recency effect in category learning. J. Experiment. Psych. Learn. Memory Cognition 29(4):626–640.

Keith KA, Stent A (2019) Modeling financial analysts’ decision making via the pragmatics and semantics of earnings calls. Preprint, submitted June 7, https://arxiv.org/abs/1906.02868.

Kokkodis M, Ipeirotis PG (2021) Demand-aware career path recommendations: A reinforcement learning approach. Management Sci. 67(7):4362–4383.

Kumar A, Mehra A (2018) Remedying education with personalized homework: Evidence from a randomized field experiment in India. Working paper, University of Florida, Gainesville.

Le Q, Mikolov T (2014) Distributed representations of sentences and documents. Xing EP, Jebara T, eds. Proc. 31st Internat. Conf. Machine Learn., Proceedings of Machine Learning Research, vol. 32, no. 2 (PMLR, Bejing, China), 1188–1196.

Lee D, Hosanagar K, Nair HS (2018) Advertising content and con sumer engagement on social media: Evidence from Facebook. Management Sci. 64(11):5105–5131.

Lehman S, Schraw G (2002) Effects of coherence and relevance on shallow and deep text processing. J. Ed. Psych. 94(4):738–750.

Leung ACM, Santhanam R, Kwok RCW, Yue WT (2022) Could gamification designs enhance online learning through personal ization? Lessons from a field experiment. Inform. Systems Res. 34(1):27–49.

Liu X, Zhang B, Susarla A, Padman R (2018) YouTube for patient education: A deep learning approach for understanding medical knowledge from user-generated videos. Preprint, submitted July 6, https://arxiv.org/abs/1807.03179.

Liu X, Zhang B, Susarla A, Padman R (2020) Go to You Tube and call me in the morning: Use of social media for chronic condi tions. MIS Quart. 44(1b):257–283.

Liu C, Wu X, Yu M, Li G, Jiang J, Huang W, Lu X (2019) A twostage model based on BERT for short fake news detection. Douligeris C, Karagiannis D, Apostolou D, eds. Knowledge Sci. Engrg. Management 12th Internat. Conf. KSEM 2019 Proc. Part II, Lecture Notes in Computer Science, vol. 11776 (Springer, Berlin), 172–183.

Loughran T, McDonald B (2011) When is a liability not a liability? Textual analysis, dictionaries, and 10-ks. J. Finance 66(1): 35–65.

Mao J, Liu W (2019) A BERT-based approach for automatic humor detection and scoring. Proc. IberLEF 2019 Iberian Languages Evaluation Forum 2019 35th Conf. Spanish Soc. Natl. Language Processing (SEPLN 2019) (Bilbao, Spain), 197–202.

Mohammad SM, Kiritchenko S, Zhu X (2013) NRC-Canada: Building the state-of-the-art in sentiment analysis of tweets. Preprint submitted August 28, https://arxiv.org/abs/1308.6242.

Mozafari M, Farahbakhsh R, Crespi N (2019) A BERT-based transfer learning approach for hate speech detection in online social media. Cherifi H, Gaito S, Mendes JF, Moro E, Rocha LM, eds. Complex Networks Appl. VIII Complex Networks 2019, Studies in Computational Intelligence, vol. 881 (Springer, Cham, Switzerland), 928–940.

Narvaez D, Van Den Broek P, Ruiz AB (1999) The influence of reading purpose on inference generation and comprehension in reading. J. Ed. Psych. 91(3):488–496.

Olsher G, Kantor ID (2012) Asking questions as a key strategy in guiding a novice teacher: A self-study. Studying Teacher Ed. 8(2):157-168

Pan L, Wang X, Li C, Li J, Tang J (2017) Course concept extraction in MOOCs via embedding-based graph propagation. Kondrak G, Watanabe T, eds. Proc. Eighth Internat. Joint Conf. Natl. Lan guage Processing, vol. 1 (Long Papers) (Asian Federation of Natural Language Processing, Kerrville, TX), 875–884

Pappagari R, Zelasko P, Villalba J, Carmiel Y, Dehak N (2019) Hierarchical transformers for long document classification. 2019 IEEE Automatic Speech Recognition Understanding Workshop (ASRU) (IEEE, Piscataway, NJ), 838–844.

Platz F, Kopiez R (2013) When the first impression counts: Music performers, audience and the evaluation of stage entrance behaviour. Musicae Sci. 17(2):167–197.

Qin Y, Yang Y (2019) What you say and how you say it matters: Predicting stock volatility using verbal and vocal cues. Korhonen A, Traum D, Ma\`rquez L, eds. Proc. 57th Annual Meeting Assoc. Comput. Linguistics (Association for Computational Linguistics, Kerrville, TX), 390–401.

Rehurek R, Sojka P (2010) Software framework for topic modelling with large corpora. Proc. LREC 2010 Workshop New Challenges NLP Frameworks (University of Malta, Valletta), 45–50.

Research and Markets (2020) Global online education market worth \$319+ billion by 2025 - North America anticipated to provide the highest revenue generating opportunities. Retrieved August 24, https://www.globenewswire.com/news-release/2020/04/ 16/2017102/0/en/Global-Online-Education-Market-Worth-319.

Billion-by-2025-North-America-Anticipated-to-Provide-the-Highest-Revenue-Generating-Opportunities.html.

Roitero K, Bozzato C, Della Mea V, Mizzaro S, Serra G (2020) Twitter goes to the doctor: Detecting medical tweets using machine learning and BERT. Couto FM, Krallinger M, eds. Proc. Internat. Workshop Semantic Indexing Inform. Retrieval Health Heterogeneous Content Types Languages (SIIRH 2020).

Rowan B, Chiang FS, Miller RJ (1997) Using research on employees performance to study the effects of teachers on students achievement. Sociol. Ed. 70(4):256–284.

Schraw G, Wade SE, Kardash CA (1993) Interactive effects of text based and task-based importance on learning from text. J. Ed. Psych. 85(4):652–661.

Shavelson RJ (1973) What is the basic teaching skill? J. Teacher Ed. 24(2):144–151.

Sun C, Adamopoulos P, Ghose A, Luo X (2022) Predicting stages in omnichannel path to purchase: A deep learning model. Inform. Systems Res. 33(2):429–445.

Suzuki D, Fujiwara T (2017) The multifunctionality of ‘possible modal adverbs: A comparative look. Language 93(4):827–841.

Tost LP, Gino F, Larrick RP (2013) When power makes others speechless: The negative impact of leader power on team per formance. Acad. Management J. 56(5):1465–1486.

Trakunphutthirak R, Cheung Y, Lee VC (2019) A study of educational data mining: Evidence from a Thai university. Proc. AAAI Conf. Artificial Intelligence 33(01):734–741.

United Nations (2020) Policy brief: Education during COVID-19 and beyond. Retrieved August 24, https://www.un.org/development desa/dspd/wp-content/uploads/sites/22/2020/08/sg\_policy\_ brief\_covid-19\_and\_education\_august\_2020.pdf.

van de Grift W, Helms-Lorenz M, Maulana R (2014) Teaching skills of student teachers: Calibration of an evaluation instrumen and its value in predicting student academic engagement. Stud. Ed. Evaluation 43:150–159.

Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser Ł, Polosukhin I (2017) Attention is all you need. Guyon I, Von Luxburg U, Bengio S, Wallach H, Fergus R,

Vishwanathan S, Garnett R, eds. Adv. Neural Inform. Processing Systems 30 (NIPS 2017) (Long Beach, CA), 5998–6008.

Wang W, Li B (2021) Empower audience creativity using multi modal video analytics: Evidence from TED talks. ICIS 2021 Proc. 12 (Association for Information Systems, Atlanta).

Wang Y, Currim F, Ram S (2022) Deep learning of spatiotemporal patterns for urban mobility prediction using big data. Inform. Systems Res. 33(2):579–598.

Wang T, He C, Jin F, Hu YJ (2021) Evaluating the effectiveness of marketing campaigns for malls using a novel interpretable machine learning model. Inform. Systems Res. 33(2):659–677.

Wang X, Shi W, Kim R, Oh Y, Yang S, Zhang J, Yu Z (2019) Persuasion for good: Towards a personalized persuasive dialogue system for social good. Preprint, submitted June 16, https://arxiv. org/abs/1906.06725.

Williamon A, ed. (2004) Musical Excellence: Strategies and Techniques to Enhance Performance (Oxford University Press, New York).

Wilson WR (1932) Students rating teachers. J. Higher Ed. 3(2):75–82.

Yang K, Lau RY, Abbasi A (2022) Getting personal: A deep learning artifact for text-based measurement of personality. Inform. Systems Res. 34(1):194–222.

Yu J, Wang C, Luo G, Hou L, Li J, Liu Z, Tang J (2019) Course concept expansion in MOOCs with external knowledge and interactive game. Korhonen A, Traum D, Ma\`rquez L, eds. Proc. 57th Annual Meeting Assoc. Comput. Linguistics (Association for Com putational Linguistics, Kerrville, TX), 4292–4302.

Zhang DJ, Allon G, Van Mieghem JA (2017) Does social interaction improve learning outcomes? Evidence from field experiments on massive open online courses. Manufacturing Service Oper. Management 19(3):347–367.

Zhang J, Hao B, Chen B, Li C, Chen H, Sun J (2019) Hierarchical reinforcement learning for course recommendation in MOOCs. Proc. AAAI Conf. Artificial Intelligence 33(01):435–442.

Zhou M, Chen GH, Ferreira P, Smith MD (2021) Consumer behavior in the online classroom: Using video analytics and machin learning to understand the consumption of video courseware. J. Marketing Res. 58(6):1079–1100.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
