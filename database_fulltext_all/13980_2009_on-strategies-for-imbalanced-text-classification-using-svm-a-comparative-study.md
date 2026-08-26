---
otero_id: 13980
otero_key: "3JH3DE7G"
title: "On strategies for imbalanced text classification using SVM: A comparative study"
authors: "Aixin Sun; Ee-Peng Lim; Ying Liu"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On strategies for imbalanced text classi<sup>fi</sup>cation using SVM: A comparative study

Aixin Sun <sup>a,</sup>⁎, Ee-Peng Lim <sup>b</sup>, Ying Liu <sup>c</sup>

<sup>a</sup> School of Computer Engineering, Nanyang Technological University, Singapore

<sup>b</sup> School of Information Systems, Singapore Management University, Singapore

<sup>c</sup> Department of Industrial and Systems Engineering, Hong Kong Polytechnic University, Hong Kong

## a r t i c l e i n f o

Article history: Received 15 December 2008 Received in revised form 8 July 2009 Accepted 29 July 2009 Available online 8 August 2009

Keywords: Imbalanced text classi<sup>fi</sup>cation Support Vector Machines SVM Resampling Instance weighting

## a b s t r a c t

Many real-world text classi<sup>fi</sup>cation tasks involve imbalanced training examples. The strategies proposed to address the imbalanced classi<sup>fi</sup>cation (e.g., resampling, instance weighting), however, have not been systematically evaluated in the text domain. In this paper, we conduct a comparative study on the effectiveness of these strategies in the context of imbalanced text classi<sup>fi</sup>cation using Support Vector Machines (SVM) classi<sup>fi</sup>er. SVM is the interest in this study for its good classi<sup>fi</sup>cation accuracy reported in many text classi<sup>fi</sup>cation tasks. We propose a taxonomy to organize all proposed strategies following the training and the test phases in text classi<sup>fi</sup>cation tasks. Based on the taxonomy, we survey the methods proposed to address the imbalanced classi<sup>fi</sup>cation. Among them, 10 commonly-used methods were evaluated in our experiments on three benchmark datasets, i.e., Reuters-21578, 20-Newsgroups, and WebKB. Using the area under the Precision–Recall Curve as the performance measure, our experimental results showed that the best decision surface was often learned by the standard SVM, not coupled with any of the proposed strategies. We believe such a negative <sup>fi</sup>nding will bene<sup>fi</sup>t both researchers and application developers in the area by focusing more on thresholding strategies.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

With the rapid development of the Web, huge amount of textual information are now accessible online. Moreover, much more textual documents are being created through Web 2.0 platforms e.g., blogs, wikis and forums, where millions of Web users are now active information providers. This further increases the importance of text classi<sup>fi</sup>cation (i.e., automatically classifying textual documents into topical categories), such that the information can be easily searched and browsed.

In many real-world text classi<sup>fi</sup>cation tasks, a classi<sup>fi</sup>er has to learn from imbalanced training examples. That is, the negative training examples overwhelmingly outnumber the positive ones<sup>1</sup> making the classi<sup>fi</sup>er training to be imbalanced. Classifying news articles received from multiple news agencies that are interesting to a particular user is one example. Besides text domain, imbalanced classi<sup>fi</sup>cation is also an important problem in medical diagnosis, fraud detection and many other tasks. In the literature, a number of strategies have been proposed to address the imbalanced classi<sup>fi</sup>cation and the commonly used ones are (i) resampling that under-samples negative examples or over-samples positive examples so as to re-balance the training examples; (ii) instance weighting that assigns different error-classi<sup>fi</sup>- cation costs to negative and positive training examples in classi<sup>fi</sup>er training; and (iii) thresholding that adjusts decision thresholds of a classi<sup>fi</sup>er to balance the precision and recall.

## 1.1. Motivation

Existing works on the effectiveness of these strategies have been mainly conducted on non-text domain (e.g., using UCI datasets<sup>2</sup>) [1,12]. There is a lack of a comparative study on the effectiveness of these strategies in imbalanced text classi<sup>fi</sup>cation. Given the importance of imbalanced text classi<sup>fi</sup>cation in real-world applications and the uniqueness of text classi<sup>fi</sup>cation tasks (e.g., high dimensionality, sparse feature spaces, and linearly separability in most tasks [13]), we believe a comparative study of imbalanced text classi<sup>fi</sup>cation will greatly bene<sup>fi</sup>t application developers as well as researchers in Information Retrieval, Machine Learning, and related areas.

Moreover, most existing studies in imbalanced classi<sup>fi</sup>cation used the area under the Receiver Operating Characteristic (ROC)-curve for performance evaluation [1,4,10]. A very recent study [7], however, showed that the area under ROC-curve (AUR) could present “an overly optimistic view of an algorithm's performance” in the imbalanced setting and suggested the area under Precision–Recall curve (PR-Curve) instead. Such a <sup>fi</sup>nding further motivates this study to evaluate the strategies using the area under the PR-Curve (AUP) as the performance evaluation metric, to better re<sup>fl</sup>ect their effectiveness. Speci<sup>fi</sup>cally, in this paper, we study the effectiveness of the above-mentioned strategies in imbalanced text classi<sup>fi</sup>cation using Support Vector Machines (SVM) classi<sup>fi</sup>ers with AUP. SVM classi<sup>fi</sup>er is the interest of this study for three reasons.

• First, SVM has been very successfully applied to text classi<sup>fi</sup>cation and many other supervised learning tasks [3,9,13,24,26,34,36]. Strategies to improve SVM classi<sup>fi</sup>ers for imbalanced text classi<sup>fi</sup>- cation will therefore bene<sup>fi</sup>t existing text classi<sup>fi</sup>cation approaches that use SVM classi<sup>fi</sup>ers.

• Second, with SVM being a binary classi<sup>fi</sup>er, imbalanced training is almost inevitable when using SVM classi<sup>fi</sup>er in multi-category classi<sup>fi</sup>cation tasks. These tasks usually adopt one-against-all learning strategy. That is, one SVM classi<sup>fi</sup>er is learned for each category, and the positive (negative) training examples are the examples belonging to (not belonging to) the target category. There is therefore a huge number of training examples from the nontarget categories.

• Third, studies have shown that SVM can be adversely affected by imbalanced training where negative training examples heavily outnumber positive ones [1]. With imbalanced training examples, SVM often gives high precision but low recall on the target category.

## 1.2. Contributions

We summarize our research contributions as follows.

• First, we propose a clear taxonomy to describe all strategies for addressing imbalanced classi<sup>fi</sup>cation. Based on the taxonomy, we survey the techniques that have been studied in literature. Although this taxonomy is provided in the context of text classi<sup>fi</sup>cation using SVM classi<sup>fi</sup>ers, it can be easily adopted in other imbalanced classi<sup>fi</sup>cation tasks with minimum modi<sup>fi</sup>cation.

• Second, our comparative study systematically evaluated 10 methods best representing the various strategies (and their combinations) on 3 benchmark datasets. The 8 methods materialized with SVM as the underlying classi<sup>fi</sup>er are: standard SVM, Strati<sup>fi</sup>ed RANDom sampling (SRAND), CLuster-based Under-Sampling (CLUS), Synthetic Minority Over-sampling Technique (SMOTE), and the above four methods with instance weighting. The other 2 methods $( \mathrm { i . e . , } \mathrm { S V M } _ { B E P } \mathrm { a n d } \mathrm { S V M } _ { F 1 } )$ are based on $\mathrm { S V M } ^ { p e r } ~ f$ where the two methods are formulated for optimizing Precision/Recall Break-Even Point (BEP) and $F _ { 1 }$ respectively in training.

Note that, this paper aims to provide a comparative study of existing strategies proposed for imbalanced text classi<sup>fi</sup>cation using SVM through extensive experiments on multiple benchmark datasets. Hence proposing new techniques addressing imbalanced text classi-<sup>fi</sup>cation is not the main focus. In our experiments on the three datasets, standard SVM learned either the best or the second best decision surface in almost all experiments. That suggests that <sup>fi</sup>nding an appropriate threshold is more worthwhile in imbalanced text classi<sup>fi</sup>cation tasks. We argue that such a negative <sup>fi</sup>nding would bene<sup>fi</sup>t application developers and researchers to focus more on thresholding strategy when dealing with imbalanced text classi<sup>fi</sup>cation tasks.

## 1.3. Paper organization

The rest of the paper is organized as follows. In Section 2, we give a brief introduction to SVM and a taxonomy of strategies for handling imbalanced classi<sup>fi</sup>cation. The experiment design and experimental results are reported in Sections 3 and 4 respectively. In Section $5 ,$ we study the impact of varying parameters in resampling and instance weighting and the impact of varying imbalance ratio. In Section $6 ,$ the performance of SVM and $\mathsf { S V M } ^ { p e r f }$ is compared. The <sup>fi</sup>ndings from the experiments are discussed in Section 7. Finally, Section 8 concludes the paper and proposes future works.

## 2. SVM and imbalanced learning

We <sup>fi</sup>rst give a brief introduction to SVM and then review the strategies addressing the imbalanced classi<sup>fi</sup>cation. The possible impact of applying these strategies on SVM learning is also discussed.

## 2.1. Support Vector Machines

The training of a SVM classi<sup>fi</sup>er involves <sup>fi</sup>nding a hyperplane, as its decision surface, that separates the positive training examples from the negative ones with the largest margin [30]. Fig. 1 illustrates the training of a linear separable SVM. Given training examples represented as pairs $( \overrightarrow { \mathbf { X } } _ { i } , y _ { i } )$ , where $\overrightarrow { \mathbf { X } _ { i } }$ is the weighted feature vector of the ith training example and $y _ { i } \in \{ 1 , - 1 \}$ is the label of the example. The search for such a hyperplane can be expressed as an optimization problem of minimizing $\bar { \frac { 1 } { 2 } } | | \bar { \overrightarrow { w } } | | ^ { 2 }$ subject to $y _ { i } ( \overrightarrow { \mathbf { w } } { \cdot } \overrightarrow { \mathbf { x } } _ { i } - b ) { \geq } 1 ,$ ∀ , where <sup>→</sup>w is a vector perpendicular to the hyperplane which de<sup>fi</sup>nes the orientation of the hyperplane, and b de<sup>fi</sup>nes the position of the hyperplane. The learned hyperplane is de<sup>fi</sup>ned by a subset of positive and negative training examples, known as positive and negative support vectors respectively (see Fig. 1).

Once w<sup>→</sup>and b are learned, SVM computes a score for an unlabeled document represented by its feature vector $\overrightarrow { \mathbf { x } }$ using the decision function $f ( \overrightarrow { \mathbf { x } } ) = \overrightarrow { \mathbf { w } } { \cdot } \overrightarrow { \mathbf { x } } - b .$ The sign of the score is used to predict the label of the document. That ${ \mathrm { i } } s ,$ the document is labeled positive if $f ( { \overrightarrow { \mathbf { x } } } ) \geq 0 ,$ , and negative otherwise. In other words, SVM takes 0 as the “default” threshold in its decision function (i.e., default thresholding).

As the hyperplane learned by SVM is de<sup>fi</sup>ned by support vectors only, it is expected that SVM is less affected by imbalanced training examples [31]. However, it is found that with imbalanced training examples, the hyperplane is often skewed to the minority and the ratio between the positive and negative support vectors is imbalanced (i.e., the hyperplane is de<sup>fi</sup>ned by more negative support vectors than positive ones) [1,32]. For these two reasons, SVM is more likely to give a negative score when classifying a document in an imbalanced setting.

In this work, we model a SVM classi<sup>fi</sup>er with two components: a decision surface and a threshold θ. As the score $f ( \overrightarrow { \mathbf { x } } )$ is a real number, it is not dif<sup>fi</sup>cult to introduce a threshold $\theta ,$ and label a document positively $\dot { \mathrm { i f } } f ( \overrightarrow { \mathbf { x } } ) \geq \theta .$ That is, given a set of documents to be classi<sup>fi</sup>ed, a classi<sup>fi</sup>er outputs a score for each document based on H, indicating the document's likelihood of belonging to the target category. The category label of each document is then determined based on a given threshold $\theta ( \theta = 0$ with default thresholding). A better decision surface is the one which better ranks the documents according to their likelihood of belonging to the target category. To measure the goodness of a decision surface , we adopt a thresholdindependent measure, the area under the Precision–Recall curve (see Section 3.3).

![](/api/attachments/3JH3DE7G/fulltext/images/a1151313e47994c96f23ec066fe413189056fa816be6844da5c97a0bd4ee8222.jpg)  
Fig. 1. A linear separable Support Vector Machine.

## 2.2. Strategies for imbalanced classification

Fig. 2 illustrates both the training and classification processes in a typical text classi<sup>fi</sup>cation task<sup>3</sup>. Both labeled and unlabeled documents are represented by feature vectors according to certain weighting scheme, e.g., tf·idf. In the training and classi<sup>fi</sup>cation processes, the strategies for handling imbalanced data, $\mathrm { e . g . }$ , resampling, instance weighting and thresholding, are applied at different stages, namely, pre-training, in-training, and post-training stages respectively.

## 2.2.1. Pre-training stage

Resampling is a pre-training strategy that arti<sup>fi</sup>cially re-balances training examples by either under-sampling to select a subset of negative training examples [5,11,16,18,27], or over-sampling to (synthetically) generate more positive examples [4].

One typical under-sampling method is random sampling (or undirected sampling) which refers to the process of randomly drawing a subset of training examples from the original set. Many studies have shown that random sampling hurts classi<sup>fi</sup>er performance [1]. Directed sampling, on the other hand, aims to select the negative training examples that are expected to be close to the decision surface [5,27]. As the decision surface is de<sup>fi</sup>ned by both the positive and negative examples, negative training examples close to the decision surface are those that are close to the positive training examples. In [27], the closeness of a negative training example to the positive training examples is computed based on the number of discriminative features it contains. Yoon and Kwek proposed a method to select negative training examples through clustering in [35]. Both negative and positive training examples are <sup>fi</sup>rst clustered using a supervised clustering algorithm with a class purity maximization function. The clusters containing almost purely negative examples are discarded.

Over-sampling refers to the process of generating more positive training examples. Since studies have shown that over-sampling with replication does not signi<sup>fi</sup>cantly improve the classi<sup>fi</sup>cation accuracy, Chawla et al. proposed Synthetic Minority Over-sampling Technique (SMOTE) to create positive training instances synthetically [4]. For each positive example, its k nearest neighbors among other positive examples are identi<sup>fi</sup>ed. The example and one of its neighbors form a pair which corresponds to two points in the vector space. A new positive example is created by picking up any random point along the line linking these two points (see more detailed discussion in Section 3.2). Despite the effectiveness reported in the literature, it is known that under-sampling involves loss of information and oversampling does not gain any information but increases the training size [31].

Pre-training methods also include feature selection and term weighting techniques that address class imbalance [6,20,37]. For instance, Zheng et al. proposed a feature selection framework to select positive features that are most indicative of membership of target category and negative features that are most indicative of membership of non-target category separately. The positive and negative features are then combined and used to represent training documents. The proposed technique, however, was not evaluated on SVM classi<sup>fi</sup>ers in their experiments. Combarro et al. proposed a family of linear measures for feature selection and evaluated their effectiveness with SVM classi<sup>fi</sup>ers on two text datasets (i.e., Reuters-21578 and Ohsumed) and improvement on $F _ { 1 }$ was observed. Liu et al. proposed a probability based feature weighting scheme for imbalanced classi<sup>fi</sup>- cation [20]. A feature is assigned more weight if it appears more frequently in the positive training examples than negative ones measured by document frequency.

![](/api/attachments/3JH3DE7G/fulltext/images/3fcd1c2e74390854451813f12aa996fcf618388089229eb62fb04043c714aa92.jpg)  
Fig. 2. Training and classi<sup>fi</sup>cation processes.

## 2.2.2. In-training stage

Instance weighting is a commonly-used in-training strategy that assigns different error-classi<sup>fi</sup>cation costs on the positive and the negative training examples respectively [2]. For instance, in $S V M ^ { l i g h t }$ package<sup>4</sup>, cost-factor j is used to de<sup>fi</sup>ne by which training errors on the positive examples outweigh errors on negative examples. Examples of more complicated in-training methods include the method that modi<sup>fi</sup>es the kernel matrix according to the imbalanced data distribution [32], and SVM formulated to optimize multivariate performance measures (e.g., to optimize the SVM learning for $F _ { 1 } ,$ Precision/Recall break-even point, or other measures) [14]. Recall that with imbalanced training examples, SVM often gives high precision but low recall on the target category. The learning algorithm aiming at optimizing $F _ { 1 }$ or Precision/Recall break-even point may therefore achieve more balanced precision and recall values.

Another option to address imbalanced learning is to partition the negative training examples into subsets for training multiple SVM classi<sup>fi</sup>ers, each learning from the same set of positive examples and one subset of negative examples [15,19]. Nevertheless, Rifkin and Klautau have shown that simple one-against-all learning strategy is as accurate as any other learning strategy, assuming that the underlying binary classi<sup>fi</sup>ers are well-tuned regularized classi<sup>fi</sup>ers such as SVM [23].

## 2.2.3. Post-training stage

Thresholding is a post-training strategy that adjusts decision thresholds (see [24] for a good discussion on thresholding). Provost pointed out that it “may well be a critical mistake” to use classi<sup>fi</sup>ers learned from imbalanced data without adjusting the output threshold [22]. When SVM is used in text classi<sup>fi</sup>cation tasks, the default threshold (i.e., θ= 0 as discussed in Section 2.1), is commonly adopted. However, depending on the application, a negative threshold may be used and a document may be labeled positively even if it receives a negative score from SVM classi<sup>fi</sup>er. Such kind of threshold relaxation has been used in hierarchial text classi<sup>fi</sup>cation to avoid blocking documents at high-level categories in the hierarchy [29].

Yang studied three thresholding strategies in text classi<sup>fi</sup>cation and found that proportional thresholding (i.e., PCut) performed well in classifying rare categories for multi-category classi<sup>fi</sup>cation task which involves imbalanced classi<sup>fi</sup>cation [33]. With proportional thresholding, it is assumed that the percentage of positive documents in the test data matches the percentage in the training data. Experiments have shown that better SVM classi<sup>fi</sup>cation accuracy can be achieved by adjusting the thresholds when learning from imbalanced data [2,25]. Nevertheless, the effectiveness of PCut heavily depends on the distribution of the data as it assumes that the ratio between positive and negative examples does not change from training data to test data.

Another commonly used approach of determining a reasonable threshold is through validation set (e.g., cross-validation). With this approach, the training data is further split into two sets. The <sup>fi</sup>rst set is used to learn a classi<sup>fi</sup>er and the second set is used to search for a threshold which leads to the best result with respect to the performance evaluation metric (e.g., F ).

## 2.2.4. Discussion

Among the above discussed strategies, thresholding does not directly affect the training of a SVM classi<sup>fi</sup>er. However, applying strategies in pre- and/or in-training stage (e.g., resampling or instance weighting) could lead to a very different decision surface compared to the decision surface learned by a SVM classi<sup>fi</sup>er without applying any strategy. In this paper, we therefore aim to <sup>fi</sup>nd out through experiments whether or not applying strategies in pre-/intraining stage (or both) leads to a better decision surface in imbalanced text classi<sup>fi</sup>cation. The answer to this question has important implications. For instance, if none of these strategies could learn a better decision surface than the standard SVM, then <sup>fi</sup>nding an appropriate threshold is more worthwhile when dealing with imbalanced text classi<sup>fi</sup>cation. On the other hand, if some strategy could lead to a better decision surface than the standard SVM, then whether or not to apply such a strategy heavily depends on the computational cost of applying the strategy and the cost of <sup>fi</sup>nding an appropriate threshold.

Among all methods discussed above, we restrict our investigation to the commonly-used ones, namely, random sampling, directed under-sampling, over-sampling, instance weighting, and SVM for multivariate performance measures.

## 3. Experiment setup

All our experiments were conducted on three benchmark datasets commonly used in text classi<sup>fi</sup>cation tasks, i.e., 20-Newsgroups, Reuters-21578, and WebKB. In total three sets of experiments were conducted. In the first set of experiments, we compare the goodness of the decision surfaces learned by eight methods including standard SVM, random under-sampling, directed under-sampling, over-sampling, and their combinations with instance weighting. In the second set of experiments, we study the impact of varying parameters in resampling and instance weighting and also the impact of varying imbalance ratios. In the third set of experiments, the standard SVM was compared to SVM optimized for $F _ { 1 }$ and Precision/Recall break-event point respectively. In summary, 10 methods have been evaluated over 3 datasets.

## 3.1. Datasets

The three datasets used in our experiments are 20-Newsgroups, Reuters-21578, and WebKB. All these datasets have been commonly used in text classi<sup>fi</sup>cation tasks and the three datasets well represent three types of documents, i.e., UseNet messages, news articles, and personal/project homepages.

20-Newsgroups contains posts collected from 20 UseNet groups with nearly 1000 posts from each group. We used the “bydate” version preprocessed by Ana Cardoso-Cachopo<sup>5</sup>, which contains 11,293 training documents and 7528 test documents. All the 20 categories were used as target categories in our experiments. Thus, using one-against-all learning strategy, the imbalance ratio (i.e., the ratio between the negative and the positive training examples) is about 19:1 for each category.

Reuters-21578 corpus is one of the most popular datasets used in text classi<sup>fi</sup>cation<sup>6</sup>. The 21,578 documents in this collection are organized in 135 categories. Each document may have zero, one or more category labels. With “ModLewis” split, we had 13,625 training and 6188 test documents respectively. We chose 26 categories as target categories such that each category has at least 50 positive training documents. This is to avoid lack of training examples to confound our study on imbalanced classi<sup>fi</sup>cation<sup>7</sup>. The documents that do not belong to any of the selected 26 target categories were used as negative training/test examples in the experiments. The imbalance ratios range from 4:1 to 272:1 for the 26 categories. Among them, 15 categories have imbalance ratios greater than 100:1.

WebKB dataset contains Web pages collected from Computer Science departments of four universities by the CMU text learning group<sup>8</sup>. The 4162 Web pages collected are classi<sup>fi</sup>ed in 7 categories and the four target categories used in our experiments are student, faculty, course and project. All pages from the remaining categories were used as negative training and test pages. As there is no prede<sup>fi</sup>ned train/test split, we used leave-one-university-out crossvalidation to conduct training and evaluation. That is, for each category, pages from three universities were used as training examples and the classi<sup>fi</sup>er learned was tested with the pages from the remaining university. The imbalance ratios range from 6:1 to 50:1 for WebKB dataset.

The preprocessing of the dataset includes HTML tag removal (for WebKB dataset only), stopword removal, and stemming. Document feature vectors are weighted with tf×idf scheme and normalized to unit length.

## 3.2. Methods

The methods evaluated in our experiments are divided into three groups. The <sup>fi</sup>rst group includes the standard SVM, Strati<sup>fi</sup>ed Random Sampling (SRAND), CLuster-based Under-Sampling (CLUS), and SMOTE. The second group refers to the above four methods with instance weighting. The third group includes SVM optimized for $F _ { 1 }$ and SVM optimized for Precision/Recall break-even point.

SVM: or standard SVM, refers to the SVM classi<sup>fi</sup>er with all default setting. We used $S V M ^ { l i g h t }$ (version $5 . 0 ) ^ { 9 }$ with linear kernel as the underlying classi<sup>fi</sup>er in our experiments. We used linear kernel as linear kernel has been commonly used in text classi<sup>fi</sup>cation and the

Table 2

choice of kernel functions do not affect text classi<sup>fi</sup>cation performance much [17].

SRAND: Strati<sup>fi</sup>ed Random Sampling represents undirected undersampling method. It selects negative training documents according to a under-sampling ratio s with strati<sup>fi</sup>ed sampling. For a given undersampling ratio of s, one document is randomly chosen in every s negative training documents sorted by document id. As there is no guideline on how to set a proper sampling ratio, in the <sup>fi</sup>rst set of experiments, we simply set s = 2. That is, half of the negative training documents were selected and used in SVM training for each category. The impact of choosing different s is studied in the second set of experiments, reported in Section 5.

CLUS: CLuster-based Under-Sampling is a parameter-free directed under-sampling method. The basic idea is to <sup>fi</sup>nd those negative examples that are close to any positive example. For each category, the pool of training documents (including both positive and negative) are clustered using k-means algorithm, where k is the number of positive documents and each cluster centroid is initialized as one positive document. After clustering, the clusters that contain only negative training documents are discarded. Negative documents from the clusters that each contains at least one positive example form the new set of negative training examples<sup>10</sup>.

SMOTE: Synthetic Minority Over-sampling Technique, is a method to generate synthetic positive training examples [4]. Given a positive training document, its k nearest neighbors among other positive training documents are <sup>fi</sup>rst identi<sup>fi</sup>ed. Let $\overrightarrow { \mathbf { X } _ { i } }$ be the feature vector of document $d _ { i } ,$ and $\overrightarrow { \mathbf { X } _ { j } }$ be the feature vector of one of d 's k nearest neighbors. The feature vector of a synthetic document is created by $( \overrightarrow { \mathbf { x } _ { i } } + g ( \overrightarrow { \mathbf { x } _ { j } } - \overrightarrow { \mathbf { x } _ { i } } ) )$ where g is a random value between 0 and 1. In our experiments, we use k as over-sampling ratio where one synthetic positive training example is generated from each of the k nearest neighbors of a positive training example. In the <sup>fi</sup>rst set of experiments, we set k=5 as in [4]. The impact of using different k values is studied in the second set of experiments in Section 5.

Instance weighting: Instance weighting assigns different errorclassi<sup>fi</sup>cation costs to positive and negative training examples. In our experiments, instance weighting was implemented by setting the cost-factor (parameter j) in $S V M ^ { l i g h t }$ <sup>t</sup>. Following early works [21], in the <sup>fi</sup>rst set of experiments, we set j to be the imbalance ratio of the target category, $\begin{array} { r } { \mathbf { e } . \mathbf { g } . , j = \frac { L ^ { n } } { L ^ { p } } , } \end{array}$ where L<sup>n</sup> and L<sup>p</sup> refer to the number of the negative and positive training examples respectively for the category. The impact of setting different $j ^ { \prime } s$ is studied in the second set of experiments. The method where instance weighting is applied to the standard SVM is denoted by $\mathsf { S V M } _ { w } .$ . Similarly, we use $\mathrm { S R A N D } _ { w } , \mathrm { C L U S } _ { w } ,$ and SMOTE to denote the other three methods using instance weighting together with resampling (See Table 1).

SVM and $S V M _ { F 1 } ;$ refer to the SVM classi<sup>fi</sup>ers formulated for optimizing Precision/Recall break-even point (BEP) and $F _ { 1 }$ respectively. The two methods were based on $S V N ^ { p e r f }$ (version $2 . { \overset { \cdot } { 1 } } ) ^ { 1 1 }$ implementation using the corresponding loss function setting.

## 3.3. Performance metrics

The commonly-used performance measures are Precision, Recall, and $F _ { 1 } .$ Precision for a category, denoted by $P r ,$ is the percentage of correct assignments among all the documents assigned to the target category. Recall, denoted by Re, is the percentage of correct assignments among all the documents that should be assigned to the target category. $F _ { 1 } = { \frac { 2 \cdot { \mathrm { P r } } \cdot { \mathrm { R e } } } { \mathrm { P r } + { \mathrm { R e } } } }$ is the harmonic mean of Pr and Re.

However, both Pr, Re (and hence $F _ { 1 } )$ are threshold dependent. To measure how good a learned decision surface H is, performance metrics independent of threshold values are required. Both Receiver Operating Characteristic (ROC)-curve and Precision–Recall curve (or

Table 1  
List of the eight methods.

<table><tr><td>Strategy</td><td>Without instance weighting</td><td>With instance weighting</td></tr><tr><td>-</td><td>SVM</td><td> $SVM_w$ </td></tr><tr><td>Undirected under-sampling</td><td>SRAND</td><td> $SRAND_w$ </td></tr><tr><td>Directed under-sampling</td><td>CLUS</td><td> $CLUS_w$ </td></tr><tr><td>Oversampling</td><td>SMOTE</td><td> $SMOTE_w$ </td></tr></table>

PR-Curve) have been used in previous works. Although ROC has been used in many studies [1,4,10], a very recent study showed that ROC curve could present “an overly optimistic view of an algorithm's performance” in the imbalanced setting [7]. We therefore adopt PR-Curve to visualize the performance of a classi<sup>fi</sup>er and use the Area Under the PR-Curve (or AUP for short) to measure the goodness of a decision surface.

## 4. Experimental results

Table 2 reports the macro-averaged imbalance ratio over all categories after resampling with different methods on the three datasets. Note that, for SRAND and SMOTE, the resultant imbalance ratios are purely determined by the parameters given. As a parameterfree method, CLUS selected slightly more than half of negative training documents on Newsgroups and about a quarter on Reuters. OnWebKB dataset, CLUS selected 85% of negative training examples.

In the following pages, we report the experimental results of the 8 methods listed in Table 1 as they are all based on the same underlying classi<sup>fi</sup>er (see Section 3.2).

## 4.1. PR-Curve

The PR-Curves of the eight methods on three datasets are plotted in Fig. 3. Two sets of PR-Curves are plotted for each dataset for better illustration. The <sup>fi</sup>gures on the left are for those methods that do not involve instance weighting and the <sup>fi</sup>gures on the right are for the methods with instance weighting. On both sets of <sup>fi</sup>gures, the PR-Curve for SVM classi<sup>fi</sup>er is plotted for easy reference. These PR-Curves are plotted based on macro-averaged precision at each recall value computed using the tool provided by [7]. The dashed line in each plot is provided to identify the break-even point.

As shown in Fig. 3(a) and (b), on Newsgroup dataset, the PR-Curves of all methods are quite similar to each other and hard to distinguish. Nevertheless, among the eight methods, SRAND and $\mathsf { S R A N D } _ { w }$ performed slightly worse than others. On Reuters dataset, SVM was the method that achieved the best PR-Curve. It is also observed that applying instance weighting hurt the classi<sup>fi</sup>cation performance (see Fig. 3d). On WebKB, without instance weighting, all methods produced similar PR-Curves (see Fig. 3(e)); with instance weighting, SVM was much better than the other methods and ${ \mathrm { C L U S } } _ { w }$ was the worst, shown in Fig. 3(f).

## 4.2. Area under PR-Curve (AUP)

Table 3 reports the macro-averaged AUP for all methods on the three datasets. For each category in a dataset, the AUP is computed using the tool provided by [7]. The value reported for each method is the average over all categories on the dataset. The best value is in bold and the second best is underlined. Two observations can be made from the results.

Macro-averaged imbalance ratio.

<table><tr><td>Dataset</td><td>SVM</td><td>SRAND</td><td>CLUS</td><td>SMOTE</td></tr><tr><td>Newsgroups</td><td>19.3</td><td>9.6</td><td>8.8</td><td>3.2</td></tr><tr><td>Reuters</td><td>116.4</td><td>58.2</td><td>25.4</td><td>19.4</td></tr><tr><td>WebKB</td><td>24.1</td><td>12.0</td><td>20.3</td><td>4.0</td></tr></table>

(a) Newsgroups  
![](/api/attachments/3JH3DE7G/fulltext/images/5a699f887c49eb5f7ec6bde3d5032f4cbae1cf2a65ca822a02f0a93683d53b5d.jpg)  
(c) Reuters

(b) Newsgroups (with instance weighting)  
![](/api/attachments/3JH3DE7G/fulltext/images/52bb1232667284cce2487fb64643039315455d1c0e47fcf4d4a8cd2be466457a.jpg)  
(d) Reuters (with instance weighting)

![](/api/attachments/3JH3DE7G/fulltext/images/fab504cd1a95709b13099140ee3e4b8d043a3ff2dc6c1f5c0569f1d482aae1f4.jpg)  
(e) WebKB

![](/api/attachments/3JH3DE7G/fulltext/images/70272ffa853f6c5787a28b6f6849862a4862bcb85e683ec7e7478fd0a7a3dc10.jpg)  
(f) WebKB (with instance weighting)

![](/api/attachments/3JH3DE7G/fulltext/images/b88707f3836c9b539c553a2f400b4af2cfa2219b2b5f858ff30da4a7b94aa67f.jpg)

![](/api/attachments/3JH3DE7G/fulltext/images/b7446f3d5244455f3e43c85ef95965c8be6b8fd7b3fbf7126eff6e962b996875.jpg)  
Fig. 3. Precision–Recall curves on Newsgroups, Reuters, and WebKB datasets.

• The standard SVM achieved the best results on Newsgroups and Reuters, and the second best on WebKB. Such an observation suggests that the standard SVM could be the best method among all.

• No method involving instance weighting achieved either the best or the second best. Moreover, each method using instance weighting gave poorer AUP than the same method without instance weighting. That is, method M always delivered better AUP than method $M _ { w } ,$ for M {SVM, SMOTE, CLUS, SRAND}.

To verify whether the above two observations are statistically signi<sup>fi</sup>cant, we conducted paired t-test on AUP over all categories for each dataset. The p-values are reported in Table 4. Note that, we use 0.001 to indicate that the p-value is either 0.001 or smaller for easy reading, and we use a minus sign (‘ ’) to indicate that the method at the corresponding row is worse than the method at the corresponding column. All those p-values that are smaller than 0.05 are marked with ‘\*’. Based on the signi<sup>fi</sup>cance test, we conclude the following points.

Table 3  
Macro-averaged area under PR-Curve.

<table><tr><td>Dataset</td><td>SVM</td><td>SRAND</td><td>CLUS</td><td>SMOTE</td><td> $SVM_w$ </td><td> $SRAND_w$ </td><td> $CLUS_w$ </td><td> $SMOTE_w$ </td></tr><tr><td>Newsgroups</td><td>0.861</td><td>0.849</td><td>0.855</td><td>0.858</td><td>0.854</td><td>0.844</td><td>0.851</td><td>0.856</td></tr><tr><td>Reuters</td><td>0.804</td><td>0.795</td><td>0.786</td><td>0.788</td><td>0.780</td><td>0.780</td><td>0.765</td><td>0.781</td></tr><tr><td>WebKB</td><td>0.427</td><td>0.429</td><td>0.427</td><td>0.420</td><td>0.400</td><td>0.398</td><td>0.368</td><td>0.405</td></tr></table>

For each dataset the best value is in bold and the second best is underlined.

• Standard SVM was signi<sup>fi</sup>cantly better than any method involving resampling and/or instance weighting on both Newsgroups and Reuters datasets (i.e., pb0.05). On WebKB, SVM was comparable with resampling methods (including SRAND, CLUS, and SMOTE),and was signi<sup>fi</sup>cantly better than all methods involving instance weighting.

• Applying instance weighting resulted in signi<sup>fi</sup>cant performance degradation for all methods on all datasets. The only exception was SMOTE (compared to $\mathsf { S M O T E } _ { w } )$ on WebKB dataset with $\begin{array} { r } { p = 0 . 0 5 8 . } \end{array}$

• The three resampling methods performed quite differently on the three datasets. On Newsgroups, SMOTENNCLUSNNSRAND, where NN means signi<sup>fi</sup>cantly better; on Reuters, SRANDNN{SMOTE, CLUS} where SMOTE and CLUS were comparable; on WebKB, all these three methods were comparable.

The <sup>fi</sup>rst two points well support the two observations made in Section 4.2. Note that SVM was signi<sup>fi</sup>cantly better than all other methods on both Newsgroups and Reuters datasets, but were comparable with SRAND, CLUS and SMOTE on WebKB dataset. One possible reason is that WebKB dataset is relatively small; it is about one-<sup>fi</sup>fth of the other two datasets in number of documents, and contains only 4 categories while the other two datasets contains 20 or more categories. With only 4 categories, it is relatively hard for one method to be signi<sup>fi</sup>cantly better than another.

p-values for paired t-test on AUP.

<table><tr><td>Method</td><td>SRAND</td><td>CLUS</td><td>SMOTE</td><td> $SVM_w$ </td><td> $SRAND_w$ </td><td> $CLUS_w$ </td><td> $SMOTE_w$ </td></tr><tr><td colspan="8">(a) Newsgroups dataset</td></tr><tr><td>SVM</td><td>0.001*</td><td>0.001*</td><td>0.005*</td><td>0.001*</td><td>0.001*</td><td>0.001*</td><td>0.001*</td></tr><tr><td>SRAND</td><td>-</td><td>-0.030*</td><td>-0.002*</td><td>-0.060</td><td>0.004*</td><td>-0.293</td><td>-0.017*</td></tr><tr><td>CLUS</td><td></td><td>-</td><td>-0.038*</td><td>0.350</td><td>0.003*</td><td>0.004*</td><td>0.377</td></tr><tr><td>SMOTE</td><td></td><td></td><td>-</td><td>0.003*</td><td>0.001*</td><td>0.001*</td><td>0.007*</td></tr><tr><td> $SVM_w$ </td><td></td><td></td><td></td><td>-</td><td>0.001*</td><td>0.006*</td><td>-0.009*</td></tr><tr><td> $SRAND_w$ </td><td></td><td></td><td></td><td></td><td>-</td><td>-0.008*</td><td>-0.001*</td></tr><tr><td> $CLUS_w$ </td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>-0.001*</td></tr><tr><td colspan="8">(b) Reuters dataset</td></tr><tr><td>SVM</td><td>0.016*</td><td>0.001*</td><td>0.002*</td><td>0.001*</td><td>0.001*</td><td>0.001*</td><td>0.001*</td></tr><tr><td>SRAND</td><td>-</td><td>0.022*</td><td>0.022*</td><td>0.004*</td><td>0.002*</td><td>0.001*</td><td>0.007*</td></tr><tr><td>CLUS</td><td></td><td>-</td><td>-0.331</td><td>0.210</td><td>0.243</td><td>0.001*</td><td>0.264</td></tr><tr><td>SMOTE</td><td></td><td></td><td>-</td><td>0.004*</td><td>0.015*</td><td>0.001*</td><td>0.011*</td></tr><tr><td> $SVM_w$ </td><td></td><td></td><td></td><td>-</td><td>-0.410</td><td>0.012*</td><td>-0.035*</td></tr><tr><td> $SRAND_w$ </td><td></td><td></td><td></td><td></td><td>-</td><td>0.012*</td><td>-0.404</td></tr><tr><td> $CLUS_w$ </td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>-0.007*</td></tr><tr><td colspan="8">(c) WebKB dataset</td></tr><tr><td>SVM</td><td>-0.342</td><td>0.406</td><td>0.144</td><td>0.014*</td><td>0.040*</td><td>0.002*</td><td>0.032*</td></tr><tr><td>SRAND</td><td>-</td><td>0.317</td><td>0.143</td><td>0.015*</td><td>0.013*</td><td>0.002*</td><td>0.035*</td></tr><tr><td>CLUS</td><td></td><td>-</td><td>0.173</td><td>0.015*</td><td>0.021*</td><td>0.002*</td><td>0.035*</td></tr><tr><td>SMOTE</td><td></td><td></td><td>-</td><td>0.021*</td><td>0.034*</td><td>0.003*</td><td>0.058</td></tr><tr><td> $SVM_w$ </td><td></td><td></td><td></td><td>-</td><td>0.335</td><td>0.004*</td><td>-0.018*</td></tr><tr><td> $SRAND_w$ </td><td></td><td></td><td></td><td></td><td>-</td><td>0.010*</td><td>-0.131</td></tr><tr><td> $CLUS_w$ </td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>-0.001*</td></tr></table>

\* pb0.05.

## 4.3. $F _ { 1 } ^ { M }$ with optimal thresholding

Using AUP as the performance measure, we found that the standard SVM could learn better decision surface than other methods involving resampling and/or instance weighting. That is, the standard SVM could better rank the documents to be classi<sup>fi</sup>ed according to their likelihood of belonging to the target category. This also suggests that, if an appropriate threshold is found, SVM should achieve better $F _ { 1 }$ than other methods. To verify, we report the macro-averaged $F _ { 1 } ,$ denoted by $F _ { 1 } ^ { M } ,$ , using optimal thresholding.

With optimal thresholding, all test documents are ranked in descending order according to their scores returned by a classi<sup>fi</sup>er. The top ranked d documents are labeled as positive such that the $F _ { 1 }$ of the category is maximized. The score of the dth document is the optimal threshold for that category. Note that optimal thresholding is not possible in practice as the true labels of test documents are not known a priori. Optimal thresholding however provides the ideal performance of the decision surface learned by a classi<sup>fi</sup>er, as our main objective of this study is to measure the goodness of a learned decision surface.

Fig. 4(a), (b), and (c) report $F _ { 1 } ^ { M }$ for eight methods on three datasets respectively. As shown in the <sup>fi</sup>gure, with optimal thresholding, SVM achieved the best $F _ { 1 } ^ { M }$ on Newsgroups and Reuters and the second best on WebKB dataset. This is consistent with the results of AUP in Table 3. It is also observed that SMOTE and $\mathsf { S M O T E } _ { w }$ achieved slightly better $F _ { 1 } ^ { M }$ than other methods on Newsgroups and Reuters. On WebKB, similar to that of AUP, random sampling was slightly better than SVM.

As mentioned earlier, it is not possible to pre-determine an optimal threshold for a classi<sup>fi</sup>er. In reality, many classi<sup>fi</sup>cation tasks simply adopt default thresholding. With default thresholding, SVM assigns a document positive label if the score of the decision function is non-negative, $\mathrm { i } . \mathrm { e } . , f ( \overrightarrow { \mathbf { x } } ) { \geq } 0$ (see Section 2.1). For the completeness of the results, we also report $F _ { 1 } ^ { \dot { M } }$ obtained with default thresholding in Fig. 4. It is interesting to observe that, with default thresholding, SVM became the worst method on all three datasets. Either resampling or instance weighting could further improve $F _ { 1 } ^ { M } .$ . This could be the reason why resampling and/or instance weighting are applied in many imbalanced classi<sup>fi</sup>cation tasks as those tasks often adopt default thresholding.

To better explain why SVM became the worst, we plot the optimal thresholds of all methods in Fig. $4 ( \mathsf d )$ . It is observed that the difference between the optimal threshold and the default threshold $( \mathrm { i . e . , 0 ) }$ for SVM is the largest among all methods. That is, although standard SVM has learnt the best decision surface, the position of the decision surface is far away from its optimal position. To achieve better classi<sup>fi</sup>cation accuracy for standard SVM, one has to <sup>fi</sup>nd an appropriate threshold to rede<sup>fi</sup>ne the learned decision surface close to its optimal position.

It is worth noting that <sup>fi</sup>nding an appropriate threshold itself is a challenging task [24,25,33] and is out of the scope of this paper.

## 5. Impact of parameters and imbalance ratio

In our <sup>fi</sup>rst set of experiments, the over-sampling ratio k in SMOTE, under-sampling ratio s in SRAND and the cost-factor j for instance weighting were pre-de<sup>fi</sup>ned, for easy comparison among all methods. In this set of experiments, we study the impact of the corresponding parameter for each of the three methods, and also the impact of imbalance ratio.

## 5.1. Impact of parameters

Over-sampling ratio k determines the number of synthetic documents generated from each positive training document. For example, $\mathrm { i f } k = 1$ , one synthetic positive training example is generated from each positive training document. To study the impact of k, we varied k from 1 to 5 and recorded the macro-averaged AUP on the three datasets<sup>12</sup>, shown in Table 5. To verify whether the results are statistically signi<sup>fi</sup>cant, the p-values resulted from the paired t-test between SVM and SMOTE (at different k's) are included in Table 5. On Newsgroups, varying k did not affect the AUP much for SMOTE method, and on Reuters, a larger k led to slightly poorer AUP. On both datasets, SVM was signi<sup>fi</sup>cantly better than SMOTE on all k values except k=2 on Newsgroups. On WebKB, SMOTE methods at all k values were comparable with SVM.

Under-sampling ratio s determines how many negative samples to select. For instance, ${ \mathrm { i f } } s = 3 ,$ , one negative training example is selected among three; hence the imbalance ratio is reduced to the one-third of the original. Similar to the over-sampling ratio k, we evaluated 5 values for s from 2 to 6. Note that s=1 means all negative samples are selected, i.e., no change made to the original dataset. Table 6 reports the macroaveraged AUP, together with signi<sup>fi</sup>cance test comparing SVM and SRAND. On both Newsgroups and Reuters, a larger s led to poorer AUP for SRAND. SVM was signi<sup>fi</sup>cantly better than SRAND on almost all s values except s=3 on Reuters. On WebKB, no signi<sup>fi</sup>cant different result is observed comparing SVM with SRAND at different s values. For both under-sampling parameter s and over-sampling parameter k, the larger the value, the more the resulted dataset are different from the original training dataset. As the test dataset usually follows the similar distribution as the original training dataset, it is not a surprise that the decision surfaces learned are poorer with larger s and k values.

Cost-factor j de<sup>fi</sup>nes the weight of training errors on positive examples over negative examples [21]. In our experiments, we compared SVM and $\mathsf { S V M } _ { w }$ at different $j ^ { \prime } s$ de<sup>fi</sup>ned based on imbalance ratio r, shown in Table 7. Similar to the experiments on k and $s , ~ 5$ values of j were evaluated from 0.2r to r since j has often been set to r [21,28]. On Newsgroups and Reuters, increasing j resulted in slightly poorer AUP delivered by $\mathrm { { S V M } } _ { w \mathrm { { \cdot } } }$ On WebKB, when $j = 0 . 2 r ,$ , a better

Table 7  
(a) Newsgroups  
![](/api/attachments/3JH3DE7G/fulltext/images/2df9353b22ad7e56d6645564366ded97a0d1e712587757c92c67e186e5bf1fd9.jpg)  
(c) WebKB

(b) Reuters  
![](/api/attachments/3JH3DE7G/fulltext/images/5d5744dd93ada021c848ce8f80d611efb657cc603c8a06939f6bcd65545c2e29.jpg)

![](/api/attachments/3JH3DE7G/fulltext/images/a6a169287fb7e197942f208ab73d1c0a3ba6d55c0b688dc3b2e27bdeb065941c.jpg)

(d) Optimal threshold values  
![](/api/attachments/3JH3DE7G/fulltext/images/ded88508aee121ee8c3ab902438a721320b5536fe57c07d3c4efa6e4b60bdd4e.jpg)  
Fig. 4. F<sup>M</sup> with optimal and default thresholding and optimal threshold values.

AUP than SVM was achieved. However, the AUP achieved was not signi<sup>fi</sup>cantly better than standard SVM. Larger $j ^ { \prime } s$ on WebKB led to poorer AUP; similar observation holds on the other two datasets.

## 5.2. Impact of imbalance ratio

Experimental results reported in Sections 4 and 5 are based on three datasets with <sup>fi</sup>xed imbalance ratios. In this section, we design another set of experiments to study the impact of different imbalance ratios on resampling and instance weighting methods, and also the standard SVM classi<sup>fi</sup>er. The objective is to answer the question whether resampling and/or instance weighting could be more effective when the imbalance ratio is higher.

We constructed 6 datasets from 20-Newsgroups dataset with different imbalance ratios ranging from 19:1 to 191:1. To construct datasets with different imbalance ratios, for each of the 20 categories, we <sup>fi</sup>rst derived the category's positive and negative training documents with one-against-all setting. Keeping the negative training documents unchanged, we applied strati<sup>fi</sup>ed sampling to the positive training examples according to a sampling ratio s. These chosen documents form the positive training documents for that category in the new dataset. Strati<sup>fi</sup>ed sampling (with the same sampling rate) was also applied to the category's positive test documents to maintain the positive/negative distribution between the training and test documents. Dataset $D _ { s }$ is obtained by applying the same sampling ratio s over the 20 categories. The 6 datasets were obtained with s=1, 2, 4, 6, 8, 10. Table 8 reports the averaged positive/negative training/ test documents for each category over the 20 categories in each dataset, and the averaged imbalance ratios, where $L ^ { p } , L ^ { n } , T ^ { p } ,$ , and $T ^ { n }$ denote the number of positive training, negative training, positive test and negative test documents respectively. Note that, $D _ { 1 }$ refers to the original 20-Newsgroups dataset.

Impact of over-sampling ratio k in SMOTE.

<table><tr><td rowspan="2">Method Parameter k</td><td colspan="2">Newsgroups</td><td colspan="2">Reuters</td><td colspan="2">WebKB</td></tr><tr><td>AUP</td><td>p-value</td><td>AUP</td><td>p-value</td><td>AUP</td><td>p-value</td></tr><tr><td>SVM</td><td>0.861</td><td>-</td><td>0.804</td><td>-</td><td>0.427</td><td>-</td></tr><tr><td>SMOTE (k=1)</td><td>0.858</td><td>0.023*</td><td>0.796</td><td>0.001*</td><td>0.425</td><td>0.356</td></tr><tr><td>SMOTE (k=2)</td><td>0.859</td><td>0.063</td><td>0.792</td><td>0.001*</td><td>0.422</td><td>0.138</td></tr><tr><td>SMOTE (k=3)</td><td>0.858</td><td>0.046*</td><td>0.792</td><td>0.005*</td><td>0.427</td><td>-0.472</td></tr><tr><td>SMOTE (k=4)</td><td>0.858</td><td>0.011*</td><td>0.788</td><td>0.001*</td><td>0.428</td><td>-0.403</td></tr><tr><td>SMOTE (k=5)</td><td>0.858</td><td>0.005*</td><td>0.788</td><td>0.002*</td><td>0.420</td><td>0.144</td></tr></table>

The best results are in bold. \* p<0.05.

Table 9 reports the area-under PR-Curve of all methods on the 6 datasets. Similar to our earlier results, the best value is in bold and the second best is underlined. From Table 9, we can observe that imbalance ratio has signi<sup>fi</sup>cant impact on all the eight methods including SVM. The higher the imbalance ratio, the poorer the AUP values. Nevertheless, SVM remained the best method which achieved the highest AUP on all 6 datasets. That is, either resampling or instance weighting could not learn a better decision surface than the standard SVM regardless of the imbalance ratio.

Impact of under-sampling ratio s in SRAND

<table><tr><td rowspan="2">Method Parameter s</td><td colspan="2">Newsgroups</td><td colspan="2">Reuters</td><td colspan="2">WebKB</td></tr><tr><td>AUP</td><td>p-value</td><td>AUP</td><td>p-value</td><td>AUP</td><td>p-value</td></tr><tr><td>SVM</td><td>0.861</td><td>-</td><td>0.804</td><td>-</td><td>0.427</td><td>-</td></tr><tr><td>SRAND (s=2)</td><td>0.849</td><td>0.001*</td><td>0.795</td><td>0.016*</td><td>0.429</td><td>-0.342</td></tr><tr><td>SRAND (s=3)</td><td>0.845</td><td>0.001*</td><td>0.794</td><td>0.052</td><td>0.436</td><td>-0.088</td></tr><tr><td>SRAND (s=4)</td><td>0.836</td><td>0.001*</td><td>0.792</td><td>0.020*</td><td>0.419</td><td>0.131</td></tr><tr><td>SRAND (s=5)</td><td>0.834</td><td>0.001*</td><td>0.785</td><td>0.003*</td><td>0.414</td><td>0.107</td></tr><tr><td>SRAND (s=6)</td><td>0.830</td><td>0.001*</td><td>0.783</td><td>0.004*</td><td>0.423</td><td>0.359</td></tr></table>

The best results are in bold. \* pb0.05.

Impact of cost-factor j in SVM .

<table><tr><td>Method</td><td colspan="2">Newsgroups</td><td colspan="2">Reuters</td><td colspan="2">WebKB</td></tr><tr><td>Parameter j</td><td>AUP</td><td>p-value</td><td>AUP</td><td>p-value</td><td>AUP</td><td>p-value</td></tr><tr><td>SVM</td><td>0.861</td><td>-</td><td>0.804</td><td>-</td><td>0.427</td><td>-</td></tr><tr><td> $SVM_{w} (j=0.2r)$ </td><td>0.856</td><td>0.001*</td><td>0.781</td><td>0.001*</td><td>0.429</td><td>-0.312</td></tr><tr><td> $SVM_{w} (j=0.4r)$ </td><td>0.855</td><td>0.001*</td><td>0.780</td><td>0.001*</td><td>0.403</td><td>0.022*</td></tr><tr><td> $SVM_{w} (j=0.6r)$ </td><td>0.855</td><td>0.001*</td><td>0.780</td><td>0.001*</td><td>0.401</td><td>0.026*</td></tr><tr><td> $SVM_{w} (j=0.8r)$ </td><td>0.854</td><td>0.001*</td><td>0.780</td><td>0.001*</td><td>0.401</td><td>0.014*</td></tr><tr><td> $SVM_{w} (j=r)$ </td><td>0.854</td><td>0.001*</td><td>0.780</td><td>0.001*</td><td>0.400</td><td>0.024*</td></tr></table>

The best results are in bold. \* p<0.05.

Table 9  
Table 8 Dataset statistics.

<table><tr><td>Dataset</td><td> $L^p$ </td><td> $L^n$ </td><td> $T^p$ </td><td> $T^n$ </td><td>Imbalance Ratio</td></tr><tr><td> $D_1$ </td><td>565</td><td>10,728</td><td>376</td><td>7152</td><td>19.3</td></tr><tr><td> $D_2$ </td><td>283</td><td>10,728</td><td>188</td><td>7152</td><td>38.5</td></tr><tr><td> $D_4$ </td><td>142</td><td>10,728</td><td>94</td><td>7152</td><td>76.8</td></tr><tr><td> $D_6$ </td><td>94</td><td>10,728</td><td>63</td><td>7152</td><td>115.2</td></tr><tr><td> $D_8$ </td><td>71</td><td>10,728</td><td>47</td><td>7152</td><td>152.9</td></tr><tr><td> $D_{10}$ </td><td>57</td><td>10,728</td><td>38</td><td>7152</td><td>191.2</td></tr></table>

## 6. SVM, SVM<sub>BEP</sub>, and $\mathbf { S V M } _ { F 1 }$

In this set of experiments, we compare the performance of SVM, $\mathsf { S V M } _ { B E P } ,$ and ${ \sf S V M } _ { F 1 }$ on the three datasets using AUP as performance measure.

Table 10 reports the macro-averaged AUP for the three classi<sup>fi</sup>ers on the three datasets. SVM achieved the best AUP on both Newsgroup and Reuters datasets but the worst on WebKB. According to the signi<sup>fi</sup>cance test shown in Table 11, SVM signi<sup>fi</sup>cantly outperformed both $\mathsf { S V M } _ { B E P }$ and ${ \mathsf { S V M } } _ { F 1 }$ on Newsgroup dataset and $\mathsf { S V M } _ { B E P }$ on Reuters dataset. The WebKB is the only dataset where $\mathsf { S V M } _ { F 1 }$ was the best performer. On all three datasets, SVM was always comparable with $\mathsf { S V M } _ { F 1 }$ . In summary, SVM formulated with optimization for either break-even point or $F _ { 1 }$ did not achieve signi<sup>fi</sup>cant performance improvement on AUP compared to standard SVM on two largest datasets out of the three evaluated. Note that the PR-Curves are not reported for this set of experiments as they are very similar to each other as in Fig. 3.

Similar to the results reported in Section 4.3, we also obtained the macro-averaged $F _ { 1 }$ values for the three methods on the three datasets (see Table 12 ) with default and optimal thresholding respectively. The results are consistent with that reported earlier; once a suitable threshold is given, the standard SVM outperformed both SVM and ${ \sf S V M } _ { F 1 }$ on the two largest datasets. Even with default thresholding (e.g., 0), the standard SVM was the best performer on Newsgroups and Reuters. An interesting observation on the optimal threshold values is that the optimal threshold values for standard SVM are always below zero. That is, with default thresholding, SVM would give more False Negatives. However, for both $\mathsf { S V M } _ { B E P }$ and ${ \mathrm { S V M } } _ { F 1 } ,$ the optimal threshold values were all above zero. With default thresholding, both classi<sup>fi</sup>ers led to more False Positives.

## 7. Discussion

From our experiments, an interesting observation was that resampling and instance weighting strategies were not effective as expected in imbalanced text classi<sup>fi</sup>cation. However, these strategies have been reported to be effective in some other experiments. We believe there are mainly three reasons for their poor performance in our experiments.

Area under PR-Curve.

<table><tr><td>Dataset</td><td>SVM</td><td>SRAND</td><td>CLUS</td><td>SMOTE</td><td> $SVM_w$ </td><td> $SRAND_w$ </td><td> $CLUS_w$ </td><td> $SMOTE_w$ </td></tr><tr><td> $D_1$ </td><td>.861</td><td>0.849</td><td>0.855</td><td>0.858</td><td>0.854</td><td>0.844</td><td>0.851</td><td>0.856</td></tr><tr><td> $D_2$ </td><td>.784</td><td>0.770</td><td>0.778</td><td>0.782</td><td>0.776</td><td>0.761</td><td>0.771</td><td>0.777</td></tr><tr><td> $D_4$ </td><td>.680</td><td>0.658</td><td>0.673</td><td>0.673</td><td>0.669</td><td>0.650</td><td>0.665</td><td>0.669</td></tr><tr><td> $D_6$ </td><td>.607</td><td>0.587</td><td>0.602</td><td>0.603</td><td>0.604</td><td>0.584</td><td>0.598</td><td>0.604</td></tr><tr><td> $D_8$ </td><td>.563</td><td>0.539</td><td>0.560</td><td>0.554</td><td>0.539</td><td>0.524</td><td>0.533</td><td>0.540</td></tr><tr><td> $D_{10}$ </td><td>.487</td><td>0.468</td><td>0.481</td><td>0.485</td><td>0.480</td><td>0.465</td><td>0.478</td><td>0.480</td></tr></table>

For each dataset, the best values are in bold and the second best are underlined.

Table 10  
Macro-averaged area under PR-Curve.

<table><tr><td>Dataset</td><td>SVM</td><td> $SVM_{BEP}$ </td><td> $SVM_{F1}$ </td></tr><tr><td>Newsgroups</td><td>0.861</td><td>0.821</td><td>0.822</td></tr><tr><td>Reuters</td><td>0.804</td><td>0.794</td><td>0.794</td></tr><tr><td>WebKB</td><td>0.427</td><td>0.430</td><td>0.434</td></tr></table>

For each dataset, the best values are in bold and the second best are underlined.

• Performance evaluation metric. As discussed in Section 1.1, many work involving imbalanced classi<sup>fi</sup>cation adopted area under the ROC-Curve (AUR) as performance measure. With AUR as performance metric used in other experiments, sampling or instance weighting methods may show to be effective. However, a recent study on the relationship between Precision–Recall and ROC curves showed that AUR could present “an overly optimistic view of an algorithm's performance” in the imbalanced setting [7]. This was also the reason we conducted the comparative study.

• Nature of the classifier. In other experiments, the methods had been evaluated with classi<sup>fi</sup>ers other than SVM including decision tree, Naïve bayes and others. For instance, in [4], where SMOTE algorithm was originally proposed, decision tree, Naïve bayes and Ripper classi<sup>fi</sup>ers were evaluated in their experiments. The arti<sup>fi</sup>cially rebalancing of the dataset through resampling certainly changes the statistical properties of the features. Hence the classi<sup>fi</sup>ers that heavily rely on statistical properties of features (e.g., decision tree and Naïve bayes) may give very different classi<sup>fi</sup>cation results. However, for SVM, the decision surface relies on the positive/ negative support vectors, hence SVM is less sensitive to the statistical prosperities of the features.

• Characteristics of the data. Compared to data from other domains, text data has its unique characteristics such as high-dimensional feature space, fewer irrelevant features, and sparse feature vectors [13]. The results obtained on datasets from other domains may not necessarily be repeated on text dataset.

In our experiments, we have also observed that the setting of threshold played a critical role in obtaining accurate classi<sup>fi</sup>cation results. However, it is well known that <sup>fi</sup>nding optimal thresholding is infeasible in reality in most cases. On the other hand, the setting of the threshold could be heavily application-dependent [24]. Depending on the application, various thresholding techniques maybe adopted. For instance, proportional thresholding has shown its effectiveness when the distribution of the test data (e.g., the ratio between the positive and negative examples) follows that of the training data [33]. Another common approach of <sup>fi</sup>nding an appropriate threshold is to use a validation set. In some real-world applications, a classi<sup>fi</sup>er may need to classify data objects received along the time, and the threshold could be adjusted during the classi<sup>fi</sup>cation when necessary. In such applications where threshold can be <sup>fl</sup>exibly set, the goodness of the decision surface learned from the training data determines the classi<sup>fi</sup>cation accuracy. In our experiments, we showed that the standard SVM could learn a good decision surface without applying resampling or instance-weighting techniques.

Table 11  
p-values for paired t-test on AUP.

<table><tr><td>Dataset</td><td colspan="2">Newsgroup</td><td colspan="2">Reuters</td><td colspan="2">Webkb</td></tr><tr><td>Method</td><td> $SVM_{BEP}$ </td><td> $SVM_{F1}$ </td><td> $SVM_{BEP}$ </td><td> $SVM_{F1}$ </td><td> $SVM_{BEP}$ </td><td> $SVM_{F1}$ </td></tr><tr><td>SVM</td><td>0.001*</td><td>0.001*</td><td>0.018*</td><td>0.088</td><td>-0.084</td><td>-0.041*</td></tr><tr><td> $SVM_{BEP}$ </td><td>-</td><td>-0.182</td><td>-</td><td>0.487</td><td>-</td><td>-0.151</td></tr></table>

\* pb0.05.

Table 12  
F<sub>1</sub><sup>M</sup> with optimal and default thresholding, and optimal threshold values.

<table><tr><td>Dateset</td><td> $F_1^M$  and Threshold</td><td>SVM</td><td> $SVM_{BEP}$ </td><td> $SVM_{F1}$ </td></tr><tr><td rowspan="3">Newsgroup</td><td> $F_1^M$  with Default Threshold</td><td>0.753</td><td>0.380</td><td>0.611</td></tr><tr><td> $F_1^M$  with Optimal Threshold</td><td>0.824</td><td>0.792</td><td>0.791</td></tr><tr><td>Optimal threshold</td><td>-0.417</td><td>2.103</td><td>1.437</td></tr><tr><td rowspan="3">Reuters</td><td> $F_1^M$  with Default Threshold</td><td>0.706</td><td>0.125</td><td>0.467</td></tr><tr><td> $F_1^M$  with Optimal Threshold</td><td>0.783</td><td>0.775</td><td>0.773</td></tr><tr><td>Optimal threshold</td><td>-0.269</td><td>3.479</td><td>2.804</td></tr><tr><td rowspan="3">WebKB</td><td> $F_1^M$  with Default Threshold</td><td>0.15</td><td>0.196</td><td>0.366</td></tr><tr><td> $F_1^M$  with Optimal Threshold</td><td>0.480</td><td>0.494</td><td>0.495</td></tr><tr><td>Optimal threshold</td><td>-0.705</td><td>0.739</td><td>0.348</td></tr></table>

The best results are shown in bold.

## 8. Conclusion and future work

In this paper, we give a comparative study on the strategies addressing imbalanced text classi<sup>fi</sup>cation using SVM classi<sup>fi</sup>ers. We <sup>fi</sup>rst summarize the strategies in a taxonomy in the context of text classi<sup>fi</sup>cation. Based on the taxonomy, we give a survey on the techniques proposed for imbalanced classi<sup>fi</sup>cation including resampling and instance weighting and others. Through extensive experiments, we evaluated 10 methods on 3 benchmark datasets using AUP as the performance metric. To the best of our knowledge, this is the <sup>fi</sup>rst comparative study on imbalanced classi<sup>fi</sup>cation in text domain. Our experimental results showed the standard SVM often learn the best decision surface in most test cases. For the classi<sup>fi</sup>cation tasks involving high imbalance ratios, it is therefore more critical to <sup>fi</sup>nd an appropriate threshold than applying any of the resampling or instance weighting strategies.

Based on the <sup>fi</sup>ndings, we suggest two future research directions. One direction is to look deep into thresholding strategies, which may consider the data distribution, the information obtained during the classi<sup>fi</sup>er training, and user feedback if available. Another research direction is to improve the SVM learning objective function to consider the data imbalance in learning the decision surface such that the default threshold could be easily adopted.

## Acknowledgement

This work was partially supported by A\*STAR Public Sector R&D, Singapore, Project Number 062 101 0031.

## References

[1] R. Akbani, S. Kwek, N. Japkowicz, Applying support vector machines to imbalanced datasets, Proc. of ECML'04, Sep. 2004, pp. 39–50, Pisa, Italy.

[2] J. Brank, M. Grobelnik, N. Milic-Frayling, D. Mladenic, Training text classi<sup>fi</sup>ers with SVM on very few positive examples, Technical Report MSR-TR-2003-34, Microsoft Research, Apr. 2003.

[3] M. Chau, H. Chen, A machine learning approach to web page <sup>fi</sup>ltering using content and structure analysis, Decision Support Systems 44 (2) (2008) 482–494.

[4] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: synthetic minority over-sampling technique, Journal of Arti<sup>fi</sup>cial Intelligence Research 16 (2002) 321–357.

[5] C.-M. Chen, H.-M. Lee, M.-T. Kao, Multi-class svm with negative data selection for web page classi<sup>fi</sup>cation, Proc. of IEEE Int'l Joint Conf. on Neural Networks, vol. 3, Jul 2004, pp. 2047–2052, Budapest, Hungary.

[6] E.F. Combarro, E. Montanes, I. Diaz, J. Ranilla, R. Mones, Introducing a family of linear measures for feature selection in text categorization, IEEE Transactions on Knowledge and Data Engineering(TKDE) 17 (9) (Sep. 2005) 1223–1232.

[7] J. Davis, M. Goadrich, The relationship between precision–recall and ROC curves, Proc. of ICML'06, ACM Press, Pittsburgh, Pennsylvania, June 2006, pp. 233–240.

[8] S.T. Dumais, J. Platt, D. Heckerman, M. Sahami, Inductive learning algorithms and representations for text categorization, Proc. of ACM CIKM'98, Nov. 1998, pp. 148–155, Bethesda, Maryland.

[9] W. Fan, M.D. Gordon, P. Pathak, An integrated two-stage model for intelligent information routing, Decision Support Systems 42 (1) (2006) 362–374.

[10] T. Fawcett. Roc graphs: Notes and practical considerations for data mining researchers. Technical Report HPL-2003-4, HP Laboratories, Jan. 2003. http:// www.hpl.hp.com/techreports/2003/HPL-2003-4.html.

[11] D. Fragoudis, D. Meretakis, S. Likothanassis, Integrating feature and instance selection for text classi<sup>fi</sup>cation, Proc. of ACM SIGKDD'02, Edmonton, Alberta, Canada, July 2002, pp. 501–506.

[12] N. Japkowicz, S. Stephen, The class imbalance problem: a systematic study, Intelligent Data Analysis 6 (5) (2002) 429–449.

[13] T. Joachims, Text categorization with support vector machines: learning with many relevant features, Proc. of ECML'98, Apr. 1998, pp. 137–142, Springer-Verlag.

[14] T. Joachims, A support vector method for multivariate performance measures, Proc. of ICML'05, Aug. 2005, pp. 377–384, Bonn, Germany.

[15] U.H.-G. Krebel, Pairwise classi<sup>fi</sup>cation and support vector machines, in: B. Schölkopf, C. Burges, A. Smola (Eds.), Advances in kernel methods: support vector learning, MIT Press, 1999, pp. 255–268

[16] M. Kubat, S. Matwin, Addressing the curse of imbalanced training sets: one-sided selection, Proc. of ICML'97, July 1997, pp. 179–186

[17] E. Leopold, J. Kindermann, Text categorization with support vector machines how to represent texts in input space? Machine Learning 46 (1–3) (2002) 423–444.

[18] H. Liu, H. Motoda, On issues of instance selection, Data Mining and Knowledge Discovery 6 (2002) 115–130.

[19] X.-Y. Liu, J. Wu, Z.-H. Zhou, Exploratory under-sampling for class-imbalance learning, Proc. of ICDM'06, Dec. 2006, pp. 965–969, Hong Kong, China.

[20] Y. Liu, H.T. Loh, A. Sun, Imbalanced text classi<sup>fi</sup>cation: a term weighting approach, Expert System with Applications 36 (1) (2009) 690–701.

[21] K. Morik, P. Brockhausen, T. Joachims, Combining statistical learning with a knowledge-based approach — a case study in intensive care monitoring, Proc. of ICML'99, 1999, pp. 268–277, Bled, Slowenien.

[22] F. Provost, Machine learning from imbalanced data sets 101, Proc. of Workshop on Learning from Imbalanced Data Sets (AAAI'00), 2000, pp. 1–3, Menlo Park, California

[23] R. Rifkin, A. Klautau, In defense of one-vs-all classi<sup>fi</sup>cation, Journal of Machine Learning Research 5 (2004) 101–141.

[24] F. Sebastiani, Machine learning in automated text categorization, ACM Computing Surveys 34 (1) (2002) 1–47.

[25] J.G. Shanahan, N. Roma, Boosting support vector machines for text classi<sup>fi</sup>cation through parameter-free threshold relaxation, Proc. of CIKM'03, 2003, pp. 247–254, New Orleans, LA.

[26] D. Song, R.Y.K. Lau, P.D. Bruza, K.-F. Wong, D.-Y. Chen, An intelligent information agent for document title classi<sup>fi</sup>cation and <sup>fi</sup>ltering in document-intensive domains, Decision Support Systems 44 (1) (2007) 251–265

[27] A. Sun, E.-P. Lim, B. Benatallah, M. Hassan, FISA: Feature-based instance selection for imbalanced text classi<sup>fi</sup>cation, Proc. of PAKDD'06, 2006, pp. 250–254, Singapore.

[28] A. Sun, E.-P. Lim, W.-K. Ng, Web classi<sup>fi</sup>cation using support vector machine, Proc. of WIDM'02, ACM, McLean, Virginia, USA, 2002, pp. 96–99.

[29] A. Sun, E.-P. Lim, W.-K. Ng, J. Srivastava, Blocking reduction strategies in hierarchical text classi<sup>fi</sup>cation, IEEE Transactions on Knowledge and Data Engineering (TKDE) 16 (10) (Oct. 2004) 1305–1308.

[30] V.N. Vapnik, The nature of statistical learning theory, Springer Verlag, Heidelberg, DE, 1995.

[31] S. Visa, A. Ralescu, Issues in mining imbalanced data sets — a review paper, Proc. of Midwest Artificial Intelligence and Cognitive Science Conference (MAICS'05), 2005, pp. 67–73, Dayton.

[32] G. Wu, E.Y. Chang, KBA: kernel boundary alignment considering imbalanced data distribution, IEEE Transactions on Knowledge and Data Engineering (TKDE) 17 (6) (June 2005) 786–795.

[33] Y. Yang, A study of thresholding strategies for text categorization, Proc. of SIGIR'01, 2001, pp. 137–145, New Orleans, USA.

[34] Y. Yang, X. Liu, A re-examination of text categorization methods, Proc. of ACM SIGIR'99, Aug. 1999, pp. 42–49, Berkeley, USA.

[35] K. Yoon, S. Kwek, An unsupervised learning approach to resolving the data imbalanced issue in supervised learning problems in functional genomics, Proc. of International Conference on Hybrid Intelligent Systems, 2005, pp. 303–308

[36] Y. Zhang, Y. Dang, H. Chen, M. Thurmond, C. Larson, Automatic online news monitoring and classi<sup>fi</sup>cation for syndromic surveillance, Decision Support Systems 47 (4) (2009) 508–517.

[37] Z. Zheng, X. Wu, R. Srihari, Feature selection for text categorization on imbalanced data, SIGKDD Explorations Newsletter 6 (1) (2004) 80–89

![](/api/attachments/3JH3DE7G/fulltext/images/0252889a6451ed1d3a182fee2817f11123556ea32f02dccdea49c7e3b4baae6f.jpg)  
Aixin Sun is an Assistant Professor with School of Computer Engineering, Nanyang Technological University (NTU), Singapore. He received his B.A.Sc with First Class Honours and Ph.D. in 2001 and 2004 respectively, both in Computer Engineering from NTU. His research interests include information retrieval, text/web mining, and digital libraries. He has published more than 40 papers in major international conferences and journals including SIGIR, WSDM, CIKM, ACM/IEEE JCDL, IEEE ICDM, PAKDD, IEEE TKDE, JASIST, and KAIS. Aixin is serving as a PC member of various data mining/information retrieval conferences and reviewer for various journals. He is a member of ACM and a member of IFFE

![](/api/attachments/3JH3DE7G/fulltext/images/f5b04401d05ae00a5f20cb61e27e52abac4b8187fdf49381ebd9f5e183614ab7.jpg)

Ee-Peng Lim is a professor at the School of Information Systems of the Singapore Management University (SMU). He received Ph.D. from the University of Minnesota, Minneapolis in 1994. His research interests include information integration, data/text/web mining, and digital libraries. He is currently an Associate Editor of the ACM Transactions on Information Systems (TOIS), Journal of Web Engineering (JWE), International Journal of Digital Libraries (IJDL) and International Journal of Data Warehousing and Mining (IJDWM). He is a member of the ACM Publications Board. He is also on the Steering Committees of the International Conference on Asian Digital Libraries (ICADL), and Paci<sup>fi</sup>c Asia Conference on Knowledge

Discovery and Data Mining (PAKDD). He is a member of ACM and a senior member of IEEE.

![](/api/attachments/3JH3DE7G/fulltext/images/0416620fdb94d33edd0011dc0dae7e3b547b307b3d247963ae1562ca15c27252.jpg)

Dr. Ying Liu is presently an Assistant Professor with the Department of Industrial and Systems Engineering at the Hong Kong Polytechnic University. He obtained his Bachelor and Master from Chongqing University in 1998 and 2001 respectively, and M.Sc. and Ph.D. from the Singapore MIT Alliance (SMA) at the Nanyang Technological University and the National University of Singapore in 2002 and 2006 respectively. His current research interests focus on design informatics, data mining and text mining, intelligent information processing and management, machine learning, and their joint research and applications in engineering design, manufacturing and medical and healthcare industry for knowledge discovery and management purpose. He is the lead editor for the book “Advances of Computational Intelligence in Industrial Systems” Springer 2008 and he has served as guest editor for several special issues with the Journal of Intelligent Manufacturing, Information. Systems Frontiers and Advanced Engineering Informatics. He is a member with ACM, IEEE, ASME and the Design Society.
