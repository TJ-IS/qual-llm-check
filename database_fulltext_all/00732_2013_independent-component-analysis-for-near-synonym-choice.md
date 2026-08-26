---
otero_id: 732
otero_key: "TS7N28UA"
title: "Independent component analysis for near-synonym choice"
authors: "Liang-Chih Yu; Wei-Nan Chien"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.038"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Liang-Chih Yu ⁎, Wei-Nan Chien <sup>1</sup>

Department of Information Management, Yuan Ze University, 135 Yuan-Tung Road, Chung-Li, Taiwan 32003, ROC

## a r t i c l e i n f o

Article history: Received 3 March 2012 Received in revised form 21 October 2012 Accepted 31 December 2012 Available online 11 January 2013

Keywords: Near-synonym choice Independent component analysis Information retrieval Natural language processing

## a b s t r a c t

Despite their similar meanings, near-synonyms may have different usages in different contexts, and the development of algorithms that can verify whether near-synonyms do match their given contexts has been the focus of increasing concern. Such algorithms have many applications such as query expansion for information retrieval (IR), alternative word selection for writing support systems, and (near-)duplicate detection for text summarization. In this paper, we propose a framework that incorporates latent semantic analysis (LSA) and independent component analysis (ICA) to automatically select suitable near-synonyms according to the given context. LSA is used to discover useful latent features that do not frequently occur in the contexts of near-synonyms, and ICA is used to estimate a set of independent components by minimizing the dependence between features. An SVM classi<sup>fi</sup>er is then trained with the independent components for best near-synonym prediction. In experiments, we evaluate the proposed method on both Chinese and English sentences, and compare its performance to state-of-the-art supervised and unsupervised methods. Experimental results show that training on the independent components that contain useful contextual features with minimized term dependence can improve the classi<sup>fi</sup>ers' ability to discriminate among near-synonyms, thus yielding better performance.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Near-synonym sets represent groups of words with similar meanings, which can be derived from existing lexical ontologies such as WordNet [7], EuroWordNet [27], and Chinese WordNet [11]. These are useful knowledge resources for many applications such as query expansion for information retrieval (IR) [1,2,19,23,24,34], alternative word selection for writing support systems [14], and (near-)duplicate detection for text summarization [30]. In information retrieval, systems can perform a query term expansion to improve the recall rate, for example through recognizing that the weapon sense of “arm” corresponds to the weapon sense of “weapon” and of “arsenal”. In writing support systems, near-synonyms can be used to automatically suggest alternatives to avoid repeating the same word in a text when there are suitable alternatives in its near-synonym set [14].

Previous studies have shown that near-synonyms may have dif ferent usages in different contexts even though they have similar meanings. Consider the following examples.

(1) {strong, powerful} coffee

(2) ghastly {error, mistake}

(3) {bridge, overpass, tunnel} under the bay.

Examples (1) and (2) both present an example of collocational constraints for the given contexts. In (1), the word “strong” in the near-synonym set {strong, powerful} is more suitable than “powerful” to <sup>fi</sup>t the given context “coffee”, since “powerful coffee” is an anticollocation [25]. Similarly, in (2), “mistake” is more suitable than “error” because “ghastly mistake” is a collocation and “ghastly error” is an anti-collocation [14]. In (3), the near-synonym set {bridge, overpass, tunnel} represents the meaning of a physical structure that connects separate places by traversing an obstacle. Suppose that the original word is “tunnel” in the context “under the bay”. The word “tunnel” cannot be substituted by the other words in the same set because all the substitutions are semantically implausible [36]. The above examples indicate that near-synonyms are not necessarily interchangeable in practical use due to their speci<sup>fi</sup>c usages and collocational constraints. Actually, some near-synonyms may produce inadequate substitutions, thus reducing the applications' effectiveness.

Therefore, automatic near-synonym choice for selecting contextappropriate near-synonyms has emerged as an important problem which has recently been formulated as a “<sup>fi</sup>ll-in-the-blank” (FITB) task [6,8,14,15,31,35], as shown in Fig. 1. Given a near-synonym set and a sentence containing one of the near-synonyms, the nearsynonym is <sup>fi</sup>rst removed from the sentence to form a lexical gap. The goal is to predict an answer (best near-synonym) that can <sup>fi</sup>ll the gap from the given near-synonym set (including the original word). The systems can then be evaluated by examining their ability to restore the original word with the best nearsynonym.

<table><tr><td>English Sentence:</td><td>This will make the __ message easier to interpret.</td></tr><tr><td>Original word:</td><td>error</td></tr><tr><td>Near-synonym set:</td><td>{error, mistake, oversight}</td></tr></table>

Fig. 1. Example of FITB evaluation for automatic near-synonym choice.

Among approaches to automatic near-synonym choice, Edmonds' pioneering study used a lexical co-occurrence network to determine the near-synonym that is most typical or expected in a given context [6]. Other proposed methods can generally be categorized as unsupervised [8,14,15,36] and supervised methods [31,35]. In the unsupervised methods, the pointwise mutual information (PMI) [8,14] and n-gram based methods [15,36] are the two major methods. The PMI is used to measure the strength of co-occurrence between a near-synonym and each individual word appearing in its context, while the n-grams can capture contiguous word associations in the given context. Inkpen used the PMI formula to compute a score for each near-synonym in a near-synonym set by using the Waterloo terabyte corpus [14]. The near-synonym with the highest score is then considered to be the best substitute that can <sup>fi</sup>ll the gap in a given context. Following Inkpen's approach, Gardiner and Dras applied the PMI formula to the Web 1T 5-gram corpus, to explore whether near-synonyms differ in attitude [8]. Instead of using PMI, Yu et al. presented a method to compute the substitution scores for each near-synonym based on n-gram frequencies obtained by Google queries, followed by a statistical test to determine whether or not a target word can be substituted by its near-synonyms [36]. Islam and Inkpen's 5-gram language model, using the Web 1T 5-gram corpus for near-synonym choice [15], is the current state-of-the-art of unsupervised methods.

Supervised methods usually approach near-synonym choice tasks as classi<sup>fi</sup>cation tasks in which each near-synonym in a near-synonym set represents a class, and the features used for classi<sup>fi</sup>cation are the words which occur in the contexts of the near-synonyms [31,35]. The near-synonyms and their context words are represented by vectorbased representation which is frequently used in the distributional models of lexical semantics [10,20,28,32]. Based on this representation, a co-occurrence matrix of the near-synonyms and their context words can be built from the training data, i.e., a collection of sentences containing the near-synonyms. Each entry in the matrix represents a co-occurrence frequency of a context word and a near-synonym. Different techniques can then be applied to the context matrix to identify useful context features that contribute to the classi<sup>fi</sup>cation task. For instance, Yu et al. built a feature-by-class (i.e., word-by-near-synonym) matrix for each near-synonym set by using the Web 1T 5-gram corpus or, more precisely, the 5-grams containing the near-synonyms in the set [35]. In classi<sup>fi</sup>cation, each test example was <sup>fi</sup>rst represented as a vector of the feature words in the matrix. The cosine measure was then adopted as a base classi<sup>fi</sup>er to compute the similarity between the test vector and the column vectors (near-synonyms) in the matrix. Finally, the discriminative training technique was used to improve the base classi<sup>fi</sup>er by distinguishing positive and negative features for each near-synonym in the matrix. Instead of using the simple cosine measure, Wang and Hirst proposed a more effective learning method by combining the support vector machine (SVM) with latent semantic analysis (LSA) [31]. They <sup>fi</sup>rst built a word-by-document (i.e., sentences containing the near-synonyms) context matrix for each near-synonym set. Singular value decomposition (SVD) [9] was then used to discover latent features that do not frequently occur in the contexts of the near-synonyms, and represent them in a low dimensional latent semantic space consisting of a set of latent vectors. Finally, an SVM classi-<sup>fi</sup>er was trained with the latent vectors to improve classi<sup>fi</sup>cation performance.

In addition to the unsupervised and supervised methods presented above, another approach involves identifying the senses of a target word and its near-synonyms using word sense disambiguation (WSD) and determining whether they share a common sense [5,22]. Dagan et al. showed that WSD is an indirect approach since it requires the intermediate sense identi<sup>fi</sup>cation step, and thus presents a sense-matching technique to address the task directly [5].

In this paper, we also adopt SVM as the classi<sup>fi</sup>cation method, but instead of LSA we use independent component analysis (ICA) [13,18] to extract independent components from the context matrix for SVM training. The motivation is described as follows. The strength of LSA lies in discovering the latent context features for near-synonyms using SVD. Consider the example shown in Fig. 2. The original matrix, as shown in Fig. $2 ( \mathsf { a } )$ , is built by using <sup>fi</sup>ve training sentences containing two different near-synonyms $N S _ { i }$ and $N S _ { j } .$ Suppose that the words $w _ { 1 } ,$ w are the useful features for $N S _ { i } ,$ and $w _ { 3 } ,$ $w _ { 4 }$ are useful for $N S _ { j } ,$ but $w _ { 4 }$ is a latent feature because it does not frequently occur in the context of $N S _ { j } .$ . After applying SVD, the latent features can be identi<sup>fi</sup>ed by replacing the zero entries in the original matrix with non-zero real values through the indirect associations between words and sentences. For instance, $w _ { 4 }$ originally does not occur in s and $s _ { 4 } ,$ , but it does co-occur with $w _ { 3 }$ in the matrix (e.g., in $s _ { 5 } ) _ { \mathbb { \epsilon } }$ , which means that $w _ { 4 }$ might also occur in the sentences where $w _ { 3 }$ occurs $( \mathrm { e } . \mathrm { g } _ { \cdot } , s _ { 3 }$ and $s _ { 4 } )$ . Therefore, the zero entries $( w _ { 4 } , s _ { 3 } )$ and $( w _ { 4 } , s _ { 4 } )$ are replaced with a non-zero value through the indirect associations between $w _ { 3 }$ and $w _ { 4 }$ in $s _ { 5 } ,$ as shown in Fig. $2 ( \mathsf { b } )$ . This helps identify a useful latent feature $w _ { 4 }$ for $N S _ { j } .$ . However, identifying latent features through the indirect associations cannot avoid feature overlap when different near-synonyms share common words in their contexts. This might be possible because near-synonyms usually have similar contexts. For instance, in Fig. 2(a), $w _ { 1 }$ , which is useful for $N S _ { i } ,$ still occurs in the context of NS (e.g., s ). Through the indirect associations between $w _ { 1 }$ and $w _ { 3 }$ in $s _ { 4 } ,$ the frequency of $w _ { 1 }$ increases in the context of $N S _ { j }$ because it may also occur in the sentences where w occurs (e.g., $s _ { 3 }$ and $s _ { 5 } )$ , as shown in Fig. 2(b). Therefore, when all word features are to be accommodated in a low-dimensional space reduced by SVD, term overlap may occur between the latent vectors. As indicated in Fig. 2(c), the two sample latent vectors which contribute to two different near-synonyms share a common feature $w _ { 1 } .$ . Classi<sup>fi</sup>ers trained on such latent vectors with term overlap may decrease their ability to distinguish among near-synonyms.

In contrast to LSA, ICA extracts independent components by minimizing the term dependence of the context matrix. Therefore, LSA and ICA can be considered complementary methods where LSA can be used to discover latent features that do not frequently occur in the context of near-synonyms, and ICA can be used to further minimize the dependence of the latent features such that overlapped features can be removed, as presented in Fig. 2(d). Based on this complementariness, this work proposes an ICA-based framework that analyzes the LSA output to discover more useful latent features for different near-synonyms, and the dependence between them can also be minimized. The discriminant power of classi<sup>fi</sup>ers can thus be improved by training them on the independent components with minimized term overlap. In experiments, we evaluate our proposed method on both Chinese and English sentences, and compare its performance with two unsupervised methods, PMI [8,14] and a 5-gram language model [15], and two supervised methods, cosine measure [35] and LSA [31].

The rest of this paper is organized as follows. Section 2 describes previously proposed supervised and unsupervised methods for nearsynonym choice. Section 3 presents our proposed ICA-based framework combining LSA and ICA. Section 4 summarizes comparative results. Conclusions are <sup>fi</sup>nally drawn in Section 5.

## 2. Previous methods for near-synonym choice

## 2.1. Unsupervised methods

## 2.1.1. PMI-based method

The mutual information can measure the co-occurrence strength between a near-synonym and the words in a given context. A higher mutual information score indicates that the near-synonym <sup>fi</sup>ts well in the given context, and thus is more likely to be the correct answer. The pointwise mutual information [3,21] between two words x and $y$ is de<sup>fi</sup>ned as

![](/api/attachments/TS7N28UA/fulltext/images/4d944be925af7f6b82d6a4a15da97e3fae9e81b4830844417980c5257d4f3507.jpg)  
(a)

![](/api/attachments/TS7N28UA/fulltext/images/ee87650d99cec445f447743df9e33e974efc0ca9b2ea74ccc085d24387825ff2.jpg)

![](/api/attachments/TS7N28UA/fulltext/images/f1dbdfb8986e483aa7bdc8e5093f175e89d463f4ac72b21935e8f4793e5441e4.jpg)  
Fig. 2. Comparison of LSA and ICA for feature representation.

$$
\operatorname{PMI} (x, y) = \log_ {2} \frac {P (x , y)}{P (x) P (y)},\tag{1}
$$

where $P ( x , y ) { = } C ( x , y ) / N$ denotes the probability that x and y co-occur; $C ( x , y )$ is the number of times x and y co-occur in the corpus, and N is the total number of words in the corpus. Similarly, $P ( x ) = C ( x ) / N ,$ where $C ( x )$ is the number of times x occurs in the corpus, and $P ( y ) = C ( y ) / N$ , where C(y) is the number of times y occurs in the corpus. Therefore, Eq. (1) can be re-written as

$$
\operatorname{PMI} (x, y) = \log_ {2} \frac {C (x , y) \cdot N}{C (x) \cdot C (y)}.\tag{2}
$$

The frequency counts $C ( \cdot )$ presented in Eq. (2) can be retrieved from a large corpus such as the Waterloo terabyte corpus used in [14], and the Web 1T 5-gram corpus used in [8].

Given a sentence s with a gap, ${ \cal S } = { \bf \Omega } . . w _ { 1 } { \bf \Omega } . . w _ { \ell } { \bf \Omega } \quad { \bf W } _ { \ell + 1 } { \bf \Omega } . . w _ { 2 \ell } { \bf \Omega } .$ :, the PMI score for a near-synonym NS to <sup>fi</sup>ll the gap is computed from the words around the gap, de<sup>fi</sup>ned as

$$
\operatorname{PMI} \left(N S _ {j}, s\right) = \sum_ {i = 1} ^ {2 \ell} \operatorname{PMI} \left(N S _ {j}, w _ {i}\right).\tag{3}
$$

where ‘ is a window size representing ‘ words to the left and right of the gap. Finally, the near-synonym with the highest score is considered to be the answer.

## 2.1.2. 5-Gram language model

N-grams can capture contiguous word associations within given contexts. Assume a sentence $\begin{array} { r } { s = . . . w _ { i - 4 } w _ { i - 3 } w _ { i - 2 } w _ { i - 1 } w _ { i } w _ { i + 1 } w _ { i + 2 } } \end{array}$ ${ { W } _ { i + 3 } } { { W } _ { i + 4 } } . . . ,$ , where w represents a near-synonym in a set. In computing the 5-gram scores for each near-synonym, only the <sup>fi</sup>ve product items $P ( w _ { i } | w _ { i - 4 } ^ { i - 1 } ) , \ P ( w _ { i + 1 } | w _ { i - 3 } ^ { i } ) , \ P ( w _ { i + 2 } | w _ { i - 2 } ^ { i + 1 } ) , \ P ( w _ { i + 3 } | w _ { i - 1 } ^ { i + 2 } )$ and $P ( w _ { i + 4 } | w _ { i } ^ { i + 3 } )$ are considered [15]. The other items are excluded because they do not contain the near-synonym and thus will have the same values. Accordingly, the 5-gram language model $( n = 5 )$ with a smoothing method can be de<sup>fi</sup>ned as

$$
\begin{array}{l} P (s) = \prod_ {i = 0} ^ {5} P \left(w _ {i} \mid w _ {i - n + 1} ^ {i - 1}\right) \\ = \prod_ {i = 0} ^ {5} \frac {C \left(w _ {i - n + 1} ^ {i}\right) + (1 + \alpha_ {n}) M \left(w _ {i - n + 1} ^ {i - 1}\right) P \left(w _ {i} \mid w _ {i - n + 2} ^ {i - 1}\right)}{C \left(w _ {i - n + 1} ^ {i - 1}\right) + \alpha_ {n} M \left(w _ {i - n + 1} ^ {i - 1}\right)} \end{array}\tag{4}
$$

where $M ( w _ { i - n + 1 } ^ { i - 1 } )$ denotes a missing count used in the smoothing method, de<sup>fi</sup>ned as

$$
M \Big (w _ {i - n + 1} ^ {i - 1} \Big) = C \Big (w _ {i - n + 1} ^ {i - 1} \Big) - \sum_ {w _ {i}} C \Big (w _ {i - n + 1} ^ {i} \Big)\tag{5}
$$

where C(·) denotes an n-gram frequency, which can be retrieved from a large corpus such as the Web 1T 5-gram corpus used in [15]. The 5-gram language model is implemented as a back-off model. That is, if the frequency of a higher-order n-gram is zero, then its lower-order n-grams will be considered. Conversely, if the frequency of a higher-order n-gram is not zero, then the lower-order n-grams will not be included in the computation.

## 2.2. Supervised methods

## 2.2.1. Cosine measure

A classi<sup>fi</sup>cation using the cosine measure requires a vector-based representation for the near-synonyms and their context words. Therefore, the <sup>fi</sup>rst step is to build a feature-by-class (word-by-near-synonym) matrix for each near-synonym set, as shown in the sample matrix M in Fig. 3.

The F×K feature-by-class matrix can be built by extracting text instances (e.g., sentences, n-grams or documents) containing nearsynonyms in a near-synonym set from a large corpus such as the Web 1T 5-gram used in [35]. The columns represent the K near-synonyms (classes) in the set, and the rows represent the F distinct words (features) occurring in the near-synonyms' contexts in the corpus. Each entry in the matrix $m _ { i j }$ represents a weight of $w _ { i }$ with respect to $N S _ { j } ,$ which is computed as the number of times w<sub>i</sub> occurs in the contexts of NS<sub>j</sub> in the corpus, divided by the total number of words occurring in the contexts of $N S _ { j }$ in the corpus. That is,

![](/api/attachments/TS7N28UA/fulltext/images/b18f21db39f54f61b09f56592f27bebd9e7bc0ebfdf3c6c0d16ac040b87f5ffb.jpg)

![](/api/attachments/TS7N28UA/fulltext/images/909a423c320af015448eb7d52449b07987ec528b79444bda5d32a977ff2fbfbb.jpg)  
Fig. 3. Example of a feature-class matrix.

$$
m _ {i j} = \frac {C \left(w _ {i} , N S _ {j}\right)}{\sum_ {i = 1} ^ {F} C \left(w _ {i} , N S _ {j}\right)},\tag{6}
$$

where $C ( w _ { i } , N S _ { j } )$ is the number of times w<sub>i</sub> and NS<sub>j</sub> co-occur in the corpus. This frequency-based weight is then transformed into a probabilistic form, i.e., divided by the sum of the weights of word i with respect to all near-synonyms, as shown in Eq. (7).

$$
m _ {i j} = \frac {m _ {i j}}{\sum_ {j = 1} ^ {K} m _ {i j}}.\tag{7}
$$

Each test sentence is also transformed into an F-dimensional feature vector. Let $\mathbf { x } = [ x _ { 1 } , . . . , x _ { i } , . . . , x _ { F } ] ^ { T }$ denote the feature vector of an input sentence. The classi<sup>fi</sup>cation is performed by computing the cosine similarity between x and the column vectors (near-synonyms) in the matrix, de<sup>fi</sup>ned as

$$
\begin{array}{l} N S _ {j} ^ {\cdot} = \underset {j} {\operatorname{argmax}} \cos (\mathbf {x}, \mathbf {m} _ {j}) \\ = \underset {j} {\operatorname{argmax}} \frac {\mathbf {x} \cdot \mathbf {m} _ {j}}{\| \mathbf {x} \| \| \mathbf {m} _ {j} \|} \\ = \underset {j} {\operatorname{argmax}} \frac {\sum_ {i = 1} ^ {F} x _ {i} m _ {i j}}{\sqrt {\sum_ {i = 1} ^ {F} x _ {i} ^ {2}} \sqrt {\sum_ {i = 1} ^ {F} m _ {i j} ^ {2}}}, \end{array}\tag{8}
$$

where $\mathbf { m } _ { j }$ is the j-th column vector in the matrix M. The nearsynonym with the highest cosine similarity score, NS^, is the predicted class of the classi<sup>fi</sup>er.

## 2.2.2. Latent semantic analysis (LSA)

LSA is a technique for analyzing the relationships between words and documents and has been widely used in many application domains such as information retrieval [17], latent topic discovery [4], and document clustering [33]. For automatic near-synonym choice, LSA is used as a context analysis technique to identify useful latent context features for the near-synonyms through indirect associations between words and sentences.

The <sup>fi</sup>rst step in LSA is to build a word-by-document matrix for near-synonyms and their context words [31]. In addition to documents, for our task other text units such as sentences or 5-grams could also be used to build the matrix because these text units also contain contextual information for near-synonyms. Fig. 4 shows a sample matrix X built by using the sentence as the unit. The columns in $\mathbf { X } _ { v \times d }$ represent d sentences containing the near-synonyms in a near-synonym set, and the rows represent v distinct words occurring in the near-synonyms' contexts in the corpus. Singular value decomposition (SVD) is then used to decompose the matrix $\mathbf { X } _ { v \times d }$ into three matrices as follows:

$$
\mathbf {X} _ {v \times d} = \mathbf {U} _ {v \times n} \sum_ {n \times n} \mathbf {V} _ {n \times d} ^ {T},\tag{9}
$$

where U and V respectively consist of a set of latent vectors of words and sentences, ∑ is a diagonal matrix of singular values, and $n =$ min(v,d) denotes the dimensionality of the latent semantic space. Additionally, each element in U represents the weight of a context word, and the higher-weighted words are the useful context features for the near-synonyms. By selecting the largest k (≤n) singular values together with the <sup>fi</sup>rst $k _ { 1 }$ columns of U and V, the near-synonyms and their context words can be represented in a low-dimensional latent semantic space. The original matrix can also be reconstructed with the reduced dimensions, as shown in Eq. (10).

$$
\hat {\mathbf {X}} _ {v \times d} = \mathbf {U} _ {v \times k _ {1}} \sum_ {k _ {1} \times k _ {1}} \mathbf {V} _ {k _ {1} \times d} ^ {T},\tag{10}
$$

where X represents the reconstructed matrix.

In SVM training and testing, each input sentence with a lexical gap is <sup>fi</sup>rst transformed into the latent semantic representation as follows:

$$
\hat {\mathbf {t}} _ {k _ {1} \times 1} = \sum_ {k _ {1} \times k _ {1}} ^ {- 1} \mathbf {U} _ {k _ {1} \times v} ^ {T} \mathbf {t} _ {v \times 1},\tag{11}
$$

where $\mathbf { t } _ { \nu \times 1 }$ denotes the vector representation of an input sentence, and $\hat { \mathbf { t } } _ { k _ { 1 } \times 1 }$ denotes the transformed vector in the latent semantic space. Each transformed training vector is then appended by the correct answer (the near-synonym removed from the sentence) to form a $( k _ { 1 } + 1$ )-dimensional vector for SVM training.

## 3. Independent component analysis for near-synonym choice

Independent component analysis (ICA) is a technique for extracting independent components from a mixture of signals and has been successfully applied to solve the blind source separation problem [13,18]. Recent studies have shown that ICA can also be applied to other application domains such as text processing [16,26,29]. The ICA model can be formally described as

$$
\mathbf {X} = \mathbf {A S},\tag{12}
$$

![](/api/attachments/TS7N28UA/fulltext/images/398f58f3bede958a2f432b551cc7d9c9d83dece23780aa1f076f9caac649d04a.jpg)  
Fig. 4. Illustrative example of singular value decomposition for latent semantic analysis

where X denotes the observed mixture signals, A denotes a mixing matrix, and S denotes the independent components. The goal of ICA is to estimate both A and S. Once the mixing matrix A is estimated, the demixing matrix can be obtained by ${ \bf W } = { \bf A } ^ { - 1 }$ , and Eq. (12) can be re-written as

$$
\mathbf {S} = \mathbf {W X}.\tag{13}
$$

That is, the observed mixture signals can be separated into independent components by using the demixing matrix.

For our problem, the context matrix can be considered a mixture of signals because it consists of the contexts of different near-synonyms. Therefore, ICA used herein is to estimate the demixing matrix so that it can separate the mixed contexts to derive the independent components for each near-synonym. Fig. 5 shows the proposed ICA-based framework combining LSA and ICA.

## 3.1. LSA decomposition and reconstruction

In the training phase, the original context matrix $\mathbf { X } _ { v \times d }$ is <sup>fi</sup>rst decomposed by SVD by using Eq. (9), and then reconstructed with reduced dimensions by using Eq. (10). Useful latent features that do not frequently occur in the original matrix can thus be discovered in this step.

## 3.2. ICA decomposition and demixing

To further minimize term dependence in deriving the independent components, the reconstructed matrix $\hat { \mathbf { X } } _ { v \times d }$ is passed to ICA to estimate the demixing matrix. ICA accomplishes this by decomposing $\hat { \mathbf { X } } _ { v \times d }$ using Eq. (14). Fig. 6 shows an example of the decomposition.

$$
\hat {\mathbf {X}} _ {v \times d} = \mathbf {A} _ {v \times k _ {2}} \mathbf {S} _ {k _ {2} \times d}.\tag{14}
$$

Based on this decomposition, the demixing matrix can be obtained by $\pmb { \mathsf { W } } _ { k _ { 2 } \times \nu } = \pmb { \mathsf { A } } _ { \nu \times k _ { 2 } } ^ { - 1 }$ , where $k _ { 2 } ( \leq n )$ is the number of independent components. Similar to the matrix U in LSA, each element in W also represents the weight of a context word, and the higher-weighted words are useful context features for the near-synonyms. Therefore, the demixing matrix contains useful context features with minimized term dependence for different near-synonyms.

Once estimated, the demixing matrix is used to separate $\hat { \mathbf { X } } _ { v \times d }$ to derive the independent components as follows:

$$
\mathbf {S} _ {k _ {2} \times d} = \mathbf {W} _ {k _ {2} \times v} \hat {\mathbf {X}} _ {v \times d}.\tag{15}
$$

Each column vector in $\pmb { S } _ { k _ { 2 } \times d }$ is then appended by the correct answer for SVM training. Similarly, as shown in Fig. 5, each test instance $\mathbf { t } _ { v \times 1 }$ in the testing phase is also transformed by the demixing matrix, and then predicted with the trained SVM model.

## 4. Experimental results

This section presents the evaluation results of different methods for near-synonym choice. Section 4.1 describes the experiment setup, including experimental data, implementation details of methods used, and the evaluation metric. Section 4.2 investigates the selection of optimal parameters for LSA and ICA-based methods. Section 4.3 compares the results obtained by the various methods. Section 4.4 presents a detailed analysis to examine the effect of term overlap on classi<sup>fi</sup>cation performance.

![](/api/attachments/TS7N28UA/fulltext/images/eff09ca276111ed9bf71c289ccab3206d5e610ea9185071bc28340386e2c526f.jpg)  
Fig. 5. ICA-based framework for near-synonym choice.

![](/api/attachments/TS7N28UA/fulltext/images/b32287672aba2c925b43fd9832e182b412e18b46ea579a7a304672e7306912a9.jpg)  
Fig. 6. Illustrative example of ICA decomposition.

## 4.1. Experiment setup

## 4.1.1. Data

As shown in Table 1, seven English and Chinese near-synonym sets were used for evaluation [37]. For Chinese near-synonym choice evaluation, two test corpora were used: the Chinese News Corpus (CNC) and the Sinica Corpus (SC), both released by the Association for Computational Linguistics and Chinese Language Processing (ACLCLP). The test examples were collected from the two corpora by selecting sentences containing the near-synonyms in the seven Chinese near-synonym sets. A total of 36,427 (CNC) and 26,504 (SC) sentences were collected, where 20% of sentences from each corpus were randomly selected as a development set for the parameter tuning of LSA and ICA-based methods, and the remaining 80% were used as the test set for performance evaluation. In addition, the classi<sup>fi</sup>ers (described in the next section) were built from the Chinese Web 5-gram corpus released by the Linguistic Data Consortium (LDC). For English near-synonym choice evaluation, the Web 1T 5-gram corpus released by LDC was used for both classi<sup>fi</sup>er training and evaluation by using the cross-validation method.

## 4.1.2. Classifiers

The classi<sup>fi</sup>ers involved in this experiment included PMI, the 5-gram language model, cosine measure, LSA and the proposed ICA-based methods (including standalone ICA and a combination of

Table 1  
English and Chinese near-synonym sets. The English and Chinese near-synonyms in each set correspond to the same sense.

<table><tr><td>No.</td><td>Near-synonym sets</td></tr><tr><td rowspan="2">1</td><td>Difficult, hard, tough</td></tr><tr><td>困難的,艱難的,艱苦的,難懂的</td></tr><tr><td rowspan="2">2</td><td>Error, mistake, oversight</td></tr><tr><td>錯誤,錯,差錯,過失,失察</td></tr><tr><td rowspan="2">3</td><td>Job, task, duty</td></tr><tr><td>工作,任務,義務</td></tr><tr><td rowspan="2">4</td><td>Responsibility, burden, obligation, commitment</td></tr><tr><td>責任,職責,職務,約定</td></tr><tr><td rowspan="2">5</td><td>Material, stuff, substance</td></tr><tr><td>物質,材料,質料</td></tr><tr><td rowspan="2">6</td><td>Give, provide, offer</td></tr><tr><td>給,給予,給與,供應,供給</td></tr><tr><td rowspan="2">7</td><td>Settle, resolve</td></tr><tr><td>決定,確定,定奪,終結</td></tr></table>

LSA and ICA). The implementation details for each classi<sup>fi</sup>er are as follows:

• PMI: Given a near-synonym set and a test example with a gap, the PMI scores for each near-synonym were calculated by using Eq. (3), where the size of the context window was set to 2. The frequency counts were retrieved from the Web 1T 5-gram corpus and Chinese Web 5-gram corpus, respectively, for English and Chinese near-synonym choice evaluation.

• 5GRAM: The 5-gram scores for each near-synonym in a test example were calculated by using Eq. (4). The frequency counts for n-grams were retrieved by querying Google (as in [36]) for English near-synonym choice evaluation, and from the Chinese Web 5-gram corpus for Chinese evaluation.

• COS: Given a near-synonym set, all 5-grams containing the nearsynonyms in the set were <sup>fi</sup>rst extracted from the training data (i.e., from the Web 1T 5-gram corpus for English near-synonyms and from the Chinese Web 5-gram corpus for Chinese near-synonyms). The 5-grams with the near-synonyms removed were then used to build a word-by-class matrix for the near-synonym set. The best near-synonym for each test example was then predicted by comparing the cosine similarity of the test example and the near-synonyms in the matrix by using Eq. (8).

• LSA: COS used all 5-grams to build the context matrix but, due to the ef<sup>fi</sup>ciency consideration, we randomly selected only 20,000 5-grams to build the word-by-document (5-gram) matrix for each English and Chinese near-synonym set. The number of the 5-grams for each near-synonym in the matrix was selected according to their proportions in the corpus. Once the matrix was built, each training instance (i.e., each column vector of the matrix) was transformed into the latent space by using Eq. (11). The correct answer (the near-synonym removed from the training instance) was then appended to the corresponding transformed vector to form a $( k _ { 1 } + 1 )$ -dimensional vector for SVM training.

• ICA: Standalone ICA was implemented by using Eqs. (12) and (13). The input matrix was the same as that of LSA, and the demixing matrix was estimated by using the FastICA package [12]. An SVM classi<sup>fi</sup>er was then trained using the independent components obtained with the use of Eq. (13) with the correct answers appended.

• LSA+ICA: The combination of LSA and ICA was implemented by taking the LSA result as input to estimate the demixing matrix in ICA, as shown in Eq. (14). An SVM classi<sup>fi</sup>er was then trained using the independent components obtained with the use of Eq. (15) with the correct answers appended. For LSA, ICA and LSA+ICA, the best near-synonym for each test example was predicted by using the trained SVM models.

## 4.1.3. Evaluation metric

In testing, this experiment followed the FITB evaluation procedure (Fig. 1) to remove the near-synonyms from the test samples. The answers proposed by each classi<sup>fi</sup>er are the near-synonyms with the highest score. The correct answers are the near-synonyms originally in the gap of the test samples. Performance is determined by accuracy, which is de<sup>fi</sup>ned as the number of correct answers made by each classi<sup>fi</sup>er, divided by the total number of test examples.

## 4.2. Evaluation of LSA and ICA-based methods

Experiments were conducted to compare the performance of LSA, ICA, and $\mathrm { L S A } + \mathrm { I C A }$ by using different settings for the parameters $k _ { 1 }$ and $k _ { 2 } ,$ which respectively represent the dimensionality of the latent semantic space and the number of independent components. The optimal settings of the two parameters were tuned by maximizing the classi<sup>fi</sup>cation accuracy on the development set. Fig. 7 shows the classi<sup>fi</sup>cation accuracy of LSA, ICA, and $\mathrm { L S A } + \mathrm { I C A }$ with different settings of dimensionality $( k _ { 1 }$ or $k _ { 2 } )$ . The accuracies were obtained by averaging the seven Chinese near-synonym sets. For LSA, the x-axis represents different values of $k _ { 1 } ,$ , with performance increasing with $k _ { 1 }$ up to 2000. For ICA, the x-axis represents different values of $k _ { 2 } ,$ with an optimal performance at $k _ { 2 } = 5 0 0 .$ . For LSA+ICA, the performance was tuned by varying both $k _ { 1 }$ and $k _ { 2 } .$ Due to the large number of combinations of $k _ { 1 }$ and $k _ { 2 } ,$ , for $\mathrm { L S A } + \mathrm { I C A }$ , Fig. 7 only plots the optimal accuracy for each value of $k _ { 1 }$ on the x-axis, and the optimal accuracy for each value of $\mathbf { \dot { k } } _ { 1 }$ (e.g., 500) was determined by increasing k<sub>2</sub> by increments of 100 to select the highest accuracy among the different settings o $k _ { 2 } .$ . For instance, the accuracy of $\mathrm { L S A } + \mathrm { I C A }$ at $k _ { 1 } = 5 0 0$ was selected from the highest achieved at $k _ { 2 } = 5 0 0$ , and this accuracy (i.e., that reached at $k _ { 1 } = 5 0 0$ and $k _ { 2 } = 5 0 0 )$ was also the optimal performance of LSA+ICA.

The results presented in Fig. 7 show that LSA+ICA improved the performance of LSA for all dimensionalities because the degree of term overlap in LSA was reduced by ICA. In addition, the performance difference between LSA+ICA and LSA was greater when the dimensionality was smaller, indicating that ICA was more effective in reducing the degree of term overlap in a low-dimensional space. More detailed analysis of the relationship between the term overlap and the classi<sup>fi</sup>cation performance is discussed in Section 4.4. The best settings of the parameters were used in the following experiments.

![](/api/attachments/TS7N28UA/fulltext/images/111590438eae0f45203c2200e4f76a82180f58b55f3db2ecc4613a1a6c5025d2.jpg)  
Fig. 7. Classi<sup>fi</sup>cation accuracy of LSA, ICA and LSA+ICA on the development set, as a function of dimensionality.

## 4.3. Comparative results

This section reports the classi<sup>fi</sup>cation accuracy of supervised and unsupervised methods including PMI, 5GRAM, COS, LSA, ICA and LSA+ICA. Table 2 shows the comparative results for the Chinese corpora including Chinese News Corpus (CNC), Sinica Corpus (SC), and both (ALL). The binomial exact test was used to determine whether the performance difference was statistically signi<sup>fi</sup>cant.

For the two unsupervised methods, 5GRAM outperformed PMI on both test corpora. One possible reason is that the 5-gram language model can capture contiguous word associations in a given context, whereas in PMI words are considered independently within the given context. In addition, all supervised methods (i.e., COS, LSA, ICA and $\mathrm { L S A } + \mathrm { I C A } )$ achieved better performance than the two unsupervised methods on both test corpora. In the supervised methods, COS provided the baseline results since it did not use any technique for context analysis. As indicated in Table 2, COS yielded higher average accuracy than the best unsupervised method (i.e., 5GRAM) by 2.55% and 7.83% on CNC and SC, respectively, and by 4.79% on ALL. Once context analysis techniques were employed, LSA, ICA and LSA + ICA signi<sup>fi</sup>cantly improved COS, indicating that context analysis is a useful technique for near-synonym choice. For LSA, it improved the average accuracy of COS by 7.52%, 4.29% and 6.16% respectively on CNC, SC and ALL. The improvement mainly came from the discovery of useful latent features from the contexts of the near-synonyms. ICA also outperformed COS, with the improvement mainly coming from the discovery of independence components by minimizing the feature dependence among near-synonyms. After combining LSA and ICA, the performance of both LSA and ICA was further improved because LSA+ICA cannot only discover useful latent features for different near-synonyms but also can minimize the dependence between them, thus improving the discriminant power of classi<sup>fi</sup>ers to distinguish between near-synonyms.

Classi<sup>fi</sup>cation accuracy for Chinese corpora. All <sup>fi</sup>gures are in %.

<table><tr><td rowspan="2"></td><td colspan="6">Accuracy</td></tr><tr><td>PMI</td><td>5GRAM</td><td>COS</td><td>LSA</td><td>ICA</td><td>LSA + ICA</td></tr><tr><td colspan="7">CNC</td></tr><tr><td>1</td><td>72.72</td><td>71.33</td><td>67.47</td><td>71.49</td><td>72.81</td><td>76.55</td></tr><tr><td>2</td><td>59.70</td><td>53.70</td><td>65.05</td><td>65.97</td><td>68.65</td><td>69.36</td></tr><tr><td>3</td><td>67.90</td><td>70.68</td><td>81.40</td><td>87.02</td><td>88.38</td><td>89.38</td></tr><tr><td>4</td><td>56.35</td><td>56.87</td><td>59.90</td><td>69.62</td><td>70.53</td><td>72.63</td></tr><tr><td>5</td><td>75.85</td><td>64.39</td><td>78.96</td><td>83.77</td><td>83.69</td><td>86.32</td></tr><tr><td>6</td><td>51.85</td><td>57.71</td><td>57.67</td><td>65.98</td><td>66.35</td><td>67.99</td></tr><tr><td>7</td><td>60.81</td><td>72.27</td><td>63.69</td><td>73.53</td><td>79.98</td><td>82.03</td></tr><tr><td>Average</td><td>61.49</td><td>66.41</td><td>68.96</td><td>76.48</td><td> $79.02^*$ </td><td> $80.58^\dagger$ </td></tr><tr><td>Data size</td><td>29,141</td><td></td><td>28,694</td><td></td><td></td><td></td></tr><tr><td colspan="7">SC</td></tr><tr><td>1</td><td>68.84</td><td>70.66</td><td>69.35</td><td>68.08</td><td>72.37</td><td>73.31</td></tr><tr><td>2</td><td>67.51</td><td>52.47</td><td>76.12</td><td>77.40</td><td>79.02</td><td>80.11</td></tr><tr><td>3</td><td>64.67</td><td>76.72</td><td>84.96</td><td>90.01</td><td>90.71</td><td>92.06</td></tr><tr><td>4</td><td>50.14</td><td>68.58</td><td>68.86</td><td>75.70</td><td>77.51</td><td>79.10</td></tr><tr><td>5</td><td>73.29</td><td>59.52</td><td>76.13</td><td>72.13</td><td>75.96</td><td>78.63</td></tr><tr><td>6</td><td>69.85</td><td>65.68</td><td>76.72</td><td>81.52</td><td>82.66</td><td>84.57</td></tr><tr><td>7</td><td>61.58</td><td>71.98</td><td>70.17</td><td>74.88</td><td>76.79</td><td>78.75</td></tr><tr><td>Average</td><td>65.26</td><td>70.11</td><td>77.94</td><td>82.23</td><td> $83.60^*$ </td><td> $85.28^\dagger$ </td></tr><tr><td>Data size</td><td>21,192</td><td></td><td>21,098</td><td></td><td></td><td></td></tr><tr><td colspan="7">ALL</td></tr><tr><td>1</td><td>70.35</td><td>70.92</td><td>68.63</td><td>69.35</td><td>72.54</td><td>74.55</td></tr><tr><td>2</td><td>63.48</td><td>53.11</td><td>70.41</td><td>71.51</td><td>73.67</td><td>74.57</td></tr><tr><td>3</td><td>66.52</td><td>73.25</td><td>82.92</td><td>88.30</td><td>89.38</td><td>90.53</td></tr><tr><td>4</td><td>54.17</td><td>60.98</td><td>63.06</td><td>71.76</td><td>72.99</td><td>74.91</td></tr><tr><td>5</td><td>74.26</td><td>61.37</td><td>77.20</td><td>76.53</td><td>78.88</td><td>81.54</td></tr><tr><td>6</td><td>60.81</td><td>61.68</td><td>67.25</td><td>73.80</td><td>74.55</td><td>76.33</td></tr><tr><td>7</td><td>61.05</td><td>72.18</td><td>65.72</td><td>73.95</td><td>78.98</td><td>81.00</td></tr><tr><td>Average</td><td>63.07</td><td>67.97</td><td>72.76</td><td>78.92</td><td> $80.96^*$ </td><td> $82.57^\dagger$ </td></tr><tr><td>Data size</td><td>50,333</td><td></td><td>49,792</td><td></td><td></td><td></td></tr></table>

\* ICA vs LSA signi<sup>fi</sup>cantly different (pb0.05).  
<sup>†</sup> LSA+ICA vs ICA signi<sup>fi</sup>cantly different (pb0.05).

Table 3  
Classi<sup>fi</sup>cation accuracy for the English corpus. All <sup>fi</sup>gures are in %.

<table><tr><td rowspan="2">Web 1T</td><td colspan="6">Accuracy</td></tr><tr><td>PMI</td><td>5GRAM</td><td>COS</td><td>LSA</td><td>ICA</td><td>LSA + ICA</td></tr><tr><td>1</td><td>60.36</td><td>61.36</td><td>60.88</td><td>62.68</td><td>63.57</td><td>65.29</td></tr><tr><td>2</td><td>76.62</td><td>72.67</td><td>76.39</td><td>79.16</td><td>79.85</td><td>82.05</td></tr><tr><td>3</td><td>70.67</td><td>71.33</td><td>76.17</td><td>78.95</td><td>80.30</td><td>80.97</td></tr><tr><td>4</td><td>68.75</td><td>70.25</td><td>67.25</td><td>68.50</td><td>72.21</td><td>73.50</td></tr><tr><td>5</td><td>70.58</td><td>70.35</td><td>71.53</td><td>74.79</td><td>77.25</td><td>79.50</td></tr><tr><td>6</td><td>65.93</td><td>61.98</td><td>66.25</td><td>72.53</td><td>73.22</td><td>75.08</td></tr><tr><td>7</td><td>71.29</td><td>68.50</td><td>76.56</td><td>77.89</td><td>79.06</td><td>81.06</td></tr><tr><td>Average</td><td>69.17</td><td>68.06</td><td>70.72</td><td>73.50</td><td> $75.07^*$ </td><td> $76.78^†$ </td></tr></table>

\* ICA vs LSA signi<sup>fi</sup>cantly different (pb0.05).  
<sup>†</sup> LSA+ICA vs ICA signi<sup>fi</sup>cantly different (pb0.05).

For the evaluation of English near-synonym choice, 20,000 5-grams for each English near-synonym set were randomly selected from the Web 1T 5-gram corpus (Web 1T), and the near-synonyms in the 5-grams were removed for the purpose of FITB evaluation. Ten-fold cross-validation was then used to determine the classi<sup>fi</sup>cation accuracy of the methods used, with a t-test to determine statistical signi<sup>fi</sup>cance. In addition, for PMI, frequency counts were retrieved from the whole Web 1T 5-gram corpus, and those for 5GRAM were retrieved by querying Google (as in [36]). Table 3 shows the comparative results of the various methods, showing that LSA+ICA improved the performance of both standalone LSA and ICA

## 4.4. Term overlap analysis

This section investigates the effect of term overlap on classi<sup>fi</sup>cation performance. The term overlap in LSA and the ICA-based methods can be estimated from their respective corresponding matrices $\mathbf { U } _ { v \times k }$ and $\mathbf { W } _ { v \times k } ^ { T } .$ Each column of $\mathbf { U } _ { v \times k }$ and $\mathbf { W } _ { \nu \times k } ^ { \bar { T } }$ represents a latent vector/independent component of v words, and each element in the vector is a word weight representing its relevance to the corresponding latent vector/independent component. Therefore, the meaning of each latent vector/independent component can be characterized by its higher-weighted words. Fig. 8 shows two sample latent vectors for LSA and two independent components for LSA+ICA.

The upper part of Fig. 8 shows parts of the context words and their weights in the two latent vectors, where latent vector #1 can be characterized by friend, opinion and chance, which are the useful features for identifying the near-synonym “give”, and latent vector #2 can be characterized by protection, information, and increase, which are useful for identifying the near-synonym “provide”. Although the two latent vectors contained useful context features for the respective different near-synonyms, these features still had some overlap between the latent vectors, as marked by the dashed rectangles. The overlapped features, especially those with higher weights, may reduce the classi<sup>fi</sup>er's ability to distinguish between the near-synonyms. The lower part of Fig. 8 also shows two independent components for the near-synonyms “give” and “provide”. As indicated, the term overlap between the two independent components was relatively low.

To formally compare the degree of term overlap of LSA and the ICA-based methods, we used a measure, overlap@n, to calculate the degree of overlap of the top n ranked words among the latent vectors in $\mathbf { U } _ { v \times k }$ and independent components in $\mathbf { W } _ { v \times k } ^ { T } .$ First, the words in each latent vector (or independent component) were ranked according to the descending order of their weights. The top n words were then selected to form a word set. Let s<sup>n</sup> and $s _ { j } ^ { n }$ be the two word sets of the top n words for any two latent vectors (or independent components). The degree of term overlap between them was calculated by the number of intersections between their corresponding word sets divided by n, i.e., |s<sub>i</sub><sup>n</sup>∩s<sub>j</sub><sup>n</sup>|/n. Therefore, the degree of term overlap for a whole matrix, namely $o v e r l a p _ { { \mathbf { U } } _ { v \times k } }$ (or $o v e r l a p _ { { \bf W } _ { v \times k } ^ { T } } ) _ { \mathrm { ~ } }$ , can be calculated by the average of the de-<sup>-</sup>grees of term overlap between all latent vectors (or independent components) in $\mathbf { U } _ { v \times k }$ (or $\mathbf { W } _ { v \times k } ^ { T } )$ . That is,

LSA  
![](/api/attachments/TS7N28UA/fulltext/images/917321733e1b2d6d2289e0a1a5b2fc14f9d93ea11ed7672cacd9c83154952c2c.jpg)

LSA+ICA  
![](/api/attachments/TS7N28UA/fulltext/images/c54a16fbd5b64123f6f22f843035327f93c044ace3f1a38b3b4dc140c4ff3f73.jpg)  
Fig. 8. Examples of latent vectors, selected from $\mathbf { U } _ { \nu \times k }$ and independent components, selected from $\mathbf { W } _ { \nu \times k } ^ { T } ,$ for the near-synonyms “give” and “provide”. The weights shown in this <sup>fi</sup>gure are the absolute values of the weights in the latent vectors and independent components.

<table><tr><td colspan="2">k=1</td><td colspan="2">k=2</td><td colspan="2">k=3</td></tr><tr><td>A</td><td>0.4381</td><td>F</td><td>0.3678</td><td>F</td><td>0.2218</td></tr><tr><td>B</td><td>0.2708</td><td>A</td><td>0.2342</td><td>H</td><td>0.1582</td></tr><tr><td>C</td><td>0.2532</td><td>G</td><td>0.2095</td><td>E</td><td>0.1416</td></tr><tr><td>D</td><td>0.2342</td><td>H</td><td>0.1972</td><td>I</td><td>0.1332</td></tr><tr><td>E</td><td>0.2104</td><td>I</td><td>0.1895</td><td>C</td><td>0.1276</td></tr></table>

Fig. 9. Example of computing the degree of term overlap.

$$
\text { overlap } _ {\mathbf {U} _ {v \times k}} @ n = \frac {1}{C _ {2} ^ {k}} \sum_ {i = 1} ^ {k} \sum_ {j = i + 1} ^ {k} \frac {\left| s _ {i} ^ {n} \cap s _ {j} ^ {n} \right|}{n},\tag{16}
$$

where $C _ { 2 } ^ { k }$ denotes the number of combinations of any two vectors in $\mathbf { U } _ { v \times k } \left( \operatorname { o r } \mathbf { W } _ { v \times k } ^ { T } \right)$ . Fig. 9 presents a sample matrix for computing the degree of term overlap, consisting of three vectors of the top <sup>fi</sup>ve terms. The respective overlap@5 between the vectors (1, 2), (1, 3), and (2, 3), was 1/5, 2/5, and 3/5, yielding an average 2/5 as the overlap@5 for the matrix.

By averaging the degree of term overlap over the matrices corresponding to the near-synonym sets, we can obtain the degree of term overlap of LSA, ICA and $\mathrm { L S A } + \mathrm { I C A } ,$ , respectively de<sup>fi</sup>ned as $o \nu e r l a p _ { L S A } @ n , o \nu e r l a p _ { I C A } @ n$ , and $o v e r l a p _ { L S A + I C A } @ \Pi$ . Fig. 10 shows the degree of term overlap for LSA, ICA and $\mathrm { L S A } + \mathrm { I C A }$ averaged over the seven Chinese near-synonym sets against various dimensionality values. The results show that ICA achieved the lowest degree of term overlap for both overlap@10 and overlap@50. In addition, combining LSA and ICA reduced the degree of term overlap of using LSA alone, especially for a smaller dimensionality. As indicated in Fig. 10, the difference between both overlap $_ { L S A + I C A } @ 1 0$ and $o v e r l a p _ { L S A } @ 1 0$ and $o v e r l a p _ { L S A + I C A } @ 5 0$ and $o v e r l a p _ { L S A } @ 5 0$ increased with smaller dimensionality, mainly due to the fact that the features discovered by LSA were not easily separable in a lower-dimensional space. In this circumstance, incorporating ICA can more effectively reduce the degree of term overlap. As the dimensionality increased, the difference between LSA and $\mathrm { L S A } + \mathrm { I C A }$ gradually decreased, mainly because the increase in dimensionality decreased the degree of term overlap in LSA, thus ICA only produces a limited reduction of term overlap in LSA. As indicated, both $o v e r l a p _ { L S A + I C A } 1 0$ and $o v e r l a p _ { L S A + I C A } @ 5 0$ yielded a small decrease or increase of overlap when the dimensionality exceeded 1000.

![](/api/attachments/TS7N28UA/fulltext/images/6c12688b37915bb8ed94b6973cbd83bfedb3c022a3de75869723ef5659422ca8.jpg)  
Fig. 10. Degree of term overlap of LSA, ICA, and $\mathrm { L S A } + \mathrm { I C A } ,$ as a function of dimensionality

To further analyze the relationship between term overlap and classi<sup>fi</sup>cation performance, Fig. 11 compares the classi<sup>fi</sup>cation accuracy of LSA, ICA and LSA+ICA from Fig. 7 and $o v e r l a p _ { L S A } @ 5 0 , o \nu e r l a p _ { I C A } @ 5 0$ and $o v e r l a p _ { L S A + I C A } @ 5 0$ from Fig. 10. Comparing the degree of term overlap and classi<sup>fi</sup>cation performance of LSA+ICA and LSA found that reducing the degree of term overlap improved classi<sup>fi</sup>cation performance. Given a small dimensionality, the performance of LSA was low due to the high degree of term overlap. Combining LSA and ICA in this stage yielded a greater performance improvement because $\mathrm { L S A } + \mathrm { I C A }$ effectively reduced the degree of term overlap in LSA such that useful context features could be separated into different independent components according to their contribution to different near-synonyms. An increase in the dimensionality improves the performance of LSA due to the reduced degree of term overlap. Meanwhile, the performance of $\mathrm { L S A } + \mathrm { I C A }$ was not similarly improved due to the small reduction of the degree of term overlap, resulting in a gradual decrease in the performance difference between $\mathrm { L S A } + \mathrm { I C A }$ and LSA. Another observation is that $\mathrm { L S A } + \mathrm { I C A }$ also outperformed ICA, despite ICA having a lower degree of term overlap than $\mathrm { L S A } + \mathrm { I C A }$ This is mainly due to the fact that $\mathrm { L S A } + \mathrm { I C A }$ can discover more useful context features than ICA, and also minimizes feature dependence.

## 5. Conclusion

A framework that incorporates LSA and ICA for near-synonym choice is presented. Both LSA and ICA are used to analyze the contexts of near-synonyms. LSA is used to discover useful latent contextual features, while ICA is used to estimate the independent components with minimal dependence between the features. Experiments compared the proposed method with several supervised and unsupervised methods on both Chinese and English corpora. Results show that the proposed method can reduce the degree of term overlap to improve the classi<sup>fi</sup>ers' ability to distinguish among near-synonyms, thus yielding higher classi<sup>fi</sup>cation accuracy.

![](/api/attachments/TS7N28UA/fulltext/images/e16c1b56f351a5aedca032fccac5428955a2c9fd890d813307913821262994b6.jpg)  
Fig. 11. Comparison of the classi<sup>fi</sup>cation accuracy and the degree of term overlap of LSA, ICA, and LSA+ICA, as a function of dimensionality.

Future work will focus on improving classi<sup>fi</sup>cation performance by combining multiple features such as predicate–argument structure and named entities occurring in the context of near-synonyms. In addition, current near-synonym choice evaluation is carried out on several pre-selected near-synonym sets. To make the near-synonym choice task more practical (similar to all-words word sense disambiguation), all-words near-synonym choice evaluation could also be designed and implemented to verify whether every word in a text <sup>fi</sup>ts the context well.

## Acknowledgment

This work was supported by the National Science Council, Taiwan, ROC, under Grant Nos. NSC 97-2218-E-155-011 and NSC99-2221-E-155-036-MY3. The authors would like to thank the anonymous reviewers and the guest editors for their constructive comments.

## References

[1] J. Bhogal, A. Macfarlane, P. Smith, A review of ontology based query expansion, In formation Processing and Management 43 (4) (2007) 866–886.

[2] H. Chen, A.M. Lally, B. Zhu, M. Chau, HelpfulMed: intelligent searching for medical information over the internet, Journal of the American Society for Information Science and Technology 54 (7) (2003) 683–694.

[3] K. Church, P. Hanks, Word association norms, mutual information and lexicography, Computational Linguistics 16 (1) (1991) 22–29.

[4] T. Cribbin, Discovering latent topical structure by second-order similarity analy sis, Journal of the American Society for Information Science and Technology 62 (6) (2011) 1188–1207.

[5] I. Dagan, O. Glickman, A. Gliozzo, E. Marmorshtein, C. Strapparava, Direct word sense matching for lexical substitution, Proc. of the 21st International Conference on Computational Linguistics and 44th Annual Meeting of the Association fo Computational Linguistics (COLING/ACL-06), 2006, pp. 449–456.

[6] P. Edmonds, Choosing the word most typical in context using a lexical co-occurrence network, Proc. of the 35th Annual Meeting of the Association for Computational Linguistics (ACL-97), 1997, pp. 507–509.

[7] C. Fellbaum, WordNet: An Electronic Lexical Database, MIT Press, Cambridge, Mass, 1998.

[8] M. Gardiner, M. Dras, Exploring approaches to discriminating among nearsynonyms, Proc. of the Australasian Technology Workshop, 2007, pp. 31–39.

[9] G.H. Golub, C.F. Van Loan, Matrix Computations, Third edition Johns Hopkins Uni versity Press, Baltimore, MD, 1996.

[10] Z. Harris, Distributional structure, Word 10 (2–3) (1954) 146–162.

[11] C.R. Huang, S.K. Hsieh, J.F. Hong, Y.Z. Chen, I.L. Su, Y.X. Chen, S.W. Huang, Chinese Wordnet: design, implementation, and application of an infrastructure for cross-lingual knowledge processing, Proc, of the 9th Chinese Lexical Semantics Workshop, 2008.

[12] A. Hyvärinen, Fast and robust <sup>fi</sup>xed-point algorithms for independent component analysis, IEEE Transactions on Neural Networks 10 (3) (1999) 626–634.

[13] A. Hyvärinen, J. Karhunen, E. Oja, Independent Component Analysis, Wiley, New York, 2001.

[14] D. Inkpen, A statistical model of near-synonym choice, ACM Transactions on Speech and Language Processing 4 (1) (2007) 1–17.

[15] A. Islam, D. Inkpen, Near-synonym choice using a 5-gram language model, Research in Computing Science: Special issue on Natural Language Processing and its Applications, 46, 2010, pp. 41–52.

[16] T. Kolenda, L.K. Hansen, Independent components in text, Advances in Neural Information Processing Systems 13 (2000) 235-256

[17] T.K. Landauer, P.W. Foltz, D. Laham, An introduction to latent semantic analysis, Discourse Processes 25 (2&3) (1998) 259–284.

[18] T.W. Lee, Independent Component Analysis—Theory and Applications, Kluwer Norwell, MA, 1998.

[19] T.P. Liang, Y.F. Yang, D.N. Chen, Y.C. Ku, A semantic-expansion approach to personalized knowledge recommendation, Decision Support Systems 45 (3) (2008) 401–412.

[20] D. Lin, Automatic retrieval and clustering of similar words, Proc. of the 35th Annual Meeting of the Association for Computational Linguistics (ACL-98), 1998 pp. 768–774.

[21] C. Manning, H. Schütze, Foundations of Statistical Natural Language Processing, MIT Press, Cambridge, Mass, 1999.

[22] D. McCarthy, Lexical substitution as a task for WSD evaluation, Proc. of the SIGLEX/SENSEVAL Workshop on Word Sense Disambiguation at ACL-02, 2002, pp. 109–115.

[23] D. Moldovan, R. Mihalcea, Using Wordnet and lexical operators to improve internet searches, IEEE Internet Computing 4 (1) (2000) 34–43.

[24] R. Navigli, P. Velardi, An analysis of ontology-based query expansion strategies, Proc. of the Workshop on Adaptive Text Extraction and Mining (ATEM-03) at ECML-03, 2003.

[25] D. Pearce, Synonymy in collocation extraction, Proc. of the Workshop on WordNet and Other Lexical Resources at NAACL-01, 2001.

[26] R. Rapp, Mining text for word senses using independent component analysis, Proc. of the 4th SIAM International Conference on Data Mining (SDM-04), 2004, pp. 422–426.

[27] H. Rodríguez, S. Climent, P. Vossen, L. Bloksma, W. Peters, A. Alonge, F. Bertagna, A. Roventint, The top-down strategy for building EuroWordNet: vocabulary coverage, base concepts and top ontology, Computers and the Humanities 32 (1998) 117–159.

[28] D. Roussinov, J.L. Zhao, Automatic discovery of similarity relationships through Web mining, Decision Support Systems 35 (1) (2003) 149–166.

[29] X. Sevillano, F. Alías, J.C. Socoró, Reliability in ICA-based text classi<sup>fi</sup>cation, Proc. of 5th International Conference on Independent Component Analysis and Blind Signal Separation, 2004, pp. 1213–1220.

[30] I. Vanderwende, H. Suzuki. C. Brockett, A. Nenkova, Beyond SumBasic: taskfocused summarization with sentence simpli<sup>fi</sup>cation and lexical expansion, Information Processing and Management 43 (6) (2007) 1606–1618.

[31] T. Wang, G. Hirst, Near-synonym lexical choice in latent semantic space, Proc. of the 23rd International Conference on Computational Linguistics (COLING-10), 2010, pp. 1182–1190.

[32] J. Weeds, D. Weir, D. McCarthy, Characterising measures of lexical distributional similarity, Proc. of the 20th International Conference on Computational Linguistics (COLING-04), 2004, pp. 1015–1021.

[33] C.P. Wei, C.C. Yang, C.M. Lin, A latent semantic indexing-based approach to multilingual document clustering, Decision Support Systems 45 (3) (2008) 606–620.

[34] L.C. Yu, C.H. Wu, F.L. Jang, Psychiatric document retrieval using a discourse-aware model, Arti<sup>fi</sup>cial Intelligence 173 (7–8) (2009) 817–829.

[35] L.C. Yu, H.M. Shih, Y.L. Lai, J.F. Yeh, C.H. Wu, Discriminative training for near-synonym substitution, Proc. of the 23rd International Conference on Computational Linguistics (COLING-10), 2010, pp. 1254–1262.

[36] L.C. Yu, C.H. Wu, R.Y. Chang, C.H. Liu, E.H. Hovy, Annotation and veri<sup>fi</sup>cation of sense pools in OntoNotes, Information Processing and Management 46 (4) (2010) 436–447.

[37] L.C. Yu, W.N. Chien, S.T. Chen, A baseline system for Chinese near-synonym choice, Proc. of the 5th International Joint Conference on Natural Language Processing (IJCNLP-11), 2011, pp. 1366–1370.

![](/api/attachments/TS7N28UA/fulltext/images/59318839800ecf25561c2afae8092d5a30a56e9eeb58621c9c9a5815a4c9d69f.jpg)

Liang-Chih Yu is an assistant professor in the Department of Information Management at Yuan Ze University in Taiwan, ROC. He received his Ph.D. in Computer Science and Information Engineering from National Cheng Kung University in Taiwan, ROC. From 2007 to 2008, he was a visiting scholar at the Natural Language Group, Information Sciences Institute, University of Southern California (USC/ISI). His research interests include natural language processing, information retrieval, and text mining. His research has appeared in ACM Transactions on Information Systems, Artificial Intelligence, IEEE Intelligent Systems, IEEE Transactions on Audio, Speech and Language Processing, IEEE Transactions on Evolutionary Computation, IEEE Transactions on Information Technology in Biomedicine, Information

Processing and Management, Journal of Biomedical Informatics, ACL, COLING, IJCNLP, and elsewhere.

![](/api/attachments/TS7N28UA/fulltext/images/fa624065c2e5504035c0d6a3f6f1240ecccef90637c9804f2a33a15f2d336cee.jpg)

Wei-Nan Chien received his B.S. and M.S. in the Department of Information Management at Yuan Ze University in Taiwan. ROC, His research interests include natural language processing, text mining, and computer-assisted language learning.
