---
otero_id: 9442
otero_key: "CEPZHWFE"
title: "Effective spam filtering: A single-class learning and ensemble approach"
authors: "Chih-Ping Wei; Hsueh-Ching Chen; Tsang-Hsiang Cheng"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.06.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Effective spam filtering: A single-class learning and ensemble approach

Chih-Ping Wei <sup>a,⁎</sup>, Hsueh-Ching Chen <sup>b</sup>, Tsang-Hsiang Cheng

<sup>a</sup> Institute of Technology Management, College of Technology Management, National Tsing Hua University, Hsinchu, Taiwan, ROC <sup>b</sup> Allion Computer Inc., No. 14, Lane 160, Fu Yang St., Taipei, Taiwan, ROC

<sup>c</sup> Department of Business Administration, Southern Taiwan University, Tainan, Taiwan, ROC

Available online 23 June 2007

## Abstract

The annoyance of spam emails increasingly plagues both individuals and organizations. In response, most of prior research investigates spam filtering as a classical text categorization task, in which training examples must include both spam (positive examples) and legitimate (negative examples) emails. However, in many spam filtering scenarios, obtaining legitimate emails for training purpose can be more difficult than collecting spam and unclassified emails. Hence, it is more appropriate to construct a classification model for spam filtering that uses positive training examples (i.e., spam) and unlabeled instances only and does not require legitimate emails as negative training examples. Several single-class learning techniques, such as PNB and PEBL, have been proposed in the literature. However, they incur inherent limitations with regard to spam filtering. In this study, we propose and develop an ensemble approach, referred to as E2, to address these limitations. Specifically, we follow the two-stage framework of PEBL but extend each stage with an ensemble strategy. The empirical evaluation results from two spam filtering corpora suggest that our proposed E2 technique generally outperforms benchmark techniques (i.e., PNB and PEBL) and exhibits more stable performance than its counterparts.

Keywords: Spam filtering; Text categorization; Single-class learning; Ensemble approach; Learning from positive and unlabeled examples; Partially supervised classification

## 1. Introduction

Because of the advancement and proliferation of information and network technologies, individuals and organizations increasingly rely on emails to communicate and share information and knowledge. Although they may enjoy and appreciate this efficient, convenient medium, individuals and organizations also suffer from spam emails, which have increased dramatically in number recently. Spam, or unsolicited commercial or bulk email, is Internet mail sent to a group of recipients who do not request it [5,43,46]. These spam emails not only consume users' time and energy to identify and remove the undesired messages, but also cause many annoying problems such as taking up limited mailbox space, engulfing important personal emails, and wasting network bandwidth [46]. In some cases, spam emails even can be harmful, such as if children were to read spam containing pornographic materials [46,47].

The vastly increasing volume of spam emails has occurred because sending emails has nearly no cost, and spammers can obtain email addresses easily from address harvesting tools. Jupiter Research [40] estimates that 4.9 trillion spam emails were sent worldwide in 2003, and according to Brightmail,<sup>1</sup> an anti-spam software vendor, the volume of spam as a percentage of all emails rose from 8% in January 2001 to 56% in November 2003. Another recent report estimates that spam emails have increased from approximately 10% of overall mail volume in 1998 to as much as 80% today [29,17]. In terms of their costs to organizations and individuals, Ferris Research<sup>2</sup> estimates that spam emails cost U.S. companies \$10 billion in 2003 due to loss of user productivity, consumption of information technology resources, and help desk costs. Yet another study by Fallows [15] shows that 52% of email users indicate spam has made them less trusting of email communication, and 25% say that the volume of spam has reduced their email usage. To reduce these costs, effective spam filtering, which automatically discriminates spam from legitimate emails, can be essential to both individuals and organizations.

Prior studies commonly consider spam filtering a classical text categorization problem [7,14,17,20, 32,39,42], though other approaches also are possible (e.g., blacklists of known spammers and whitelists of trusted senders, hand-crafted rules that block messages containing specific words or phrases). As a text categorization problem, spam filtering uses a classification analysis or supervised learning algorithm to induce a classification model from a set of training examples, preclassified as belonging to either the spam or legitimate class. The resulting classification model thus assigns incoming emails into one of these classes. Common classification analysis algorithms used in the context of spam filtering include Naïve Bayes classifier [2,3,18,21,30,32,35–38], Support Vector Machines (SVM) [14,22,23], RIPPER rule induction [8,14,32], Rocchio [14], memory-based reasoning [9,28,36], AdaBoost [7,14], and the maximum entropy model [45]. Although these algorithms seems appealing, they require that the set of training examples contain instances from both classes (i.e., spam and legitimate). Nevertheless, in many real world scenarios, obtaining legitimate emails for training purposes is more difficult than collecting spam emails, because individuals may be willing to contribute spam emails they receive but generally are more reluctant to release their legitimate emails because of privacy concerns. In this situation, a more appropriate and effective approach might construct a classification model for spam filtering from positive (i.e., spam emails) and unlabeled instances only and eliminate the requirement of legitimate emails as negative training examples.

The described classification problem is regarded as “single-class learning,” “learning from positive and unlabeled examples,” “partially supervised classification,” and “learning without negative examples” [10,11, 25–27,44]. Prior studies propose several single-class learning techniques, such as Positive Naïve Bayes (PNB) [11] and Positive Example-Based Learning (PEBL) [44]. Let the class of positive examples be $C _ { \mathrm { p } }$ and that of negatives be $C _ { \mathrm { n } } .$ PNB takes as its inputs a set of positive training examples and a set of unlabeled documents and requires an estimate $\hat { P } ( C _ { \mathrm { p } } )$ of the class prior probability of $C _ { \mathrm { p } } .$ To determine an appropriate class for an unclassified document $d _ { j } ,$ PNB relies on $\hat { P } ( C _ { \mathrm { p } } )$ and estimates of the word probabilities $\hat { P r } ( w _ { i } | C _ { \mathrm { p } } )$ for all $w _ { i } { \in } d _ { j }$ to derive the probability that $d _ { j }$ belongs to the class $C _ { \mathrm { p } } .$ However, because it lacks access to negative training examples, PNB depends on the set of unlabeled instances and the estimate of the class prior probability of $C _ { \mathrm { n } } \left( \mathrm { i . e . , } \hat { P } ( C _ { \mathrm { n } } ) { = } \right.$ $1 - \hat { P } ( C _ { \mathrm { p } } ) )$ to obtain $\hat { P r } ( w _ { i } | C _ { \mathrm { n } } )$ for each $w _ { i } { \in } d _ { j }$ and thus derive the probability that $d _ { j }$ belongs to the class $C _ { \mathrm { n } } .$

In contrast, PEBL adopts a two-stage strategy to learn from positive and unlabeled documents. The mapping stage uses a rough classifier to identify a set of “strong negative” examples from the unlabeled set of documents. Subsequently, PEBL employs Support Vector Machines (SVM) in the convergence stage. For progressively better approximations of the negative class, PEBL iteratively identifies and selects for training purposes more negative examples from the unlabeled set of documents until it can recognize no more negative examples. Finally, PEBL uses the initial set of positive training examples and previously identified negative examples from the unlabeled documents to train a classifier that can provide class predictions for future unclassified documents.

Although their empirical results appear encouraging [11,44], these two techniques involve some inherent limitations for spam filtering. For example, PNB requires an estimate of $\hat { P } ( C _ { \mathrm { p } } )$ , whose accuracy greatly affects overall classification accuracy. However, in a spam filtering application, the percentage of spam emails varies significantly over time [11,40], which makes it difficult to obtain an accurate estimate of $\hat { P } ( C _ { \mathfrak { p } } )$ and limits the applicability of PNB. In contrast, PEBL's effectiveness depends on the accuracy of the initial set of strong negative examples identified by the rough classifier, but if this set is not trustworthy (i.e., contains some true positive examples), the accuracy of negative examples selected during the convergence stage gradually deteriorates over iterations and impairs the effectiveness of PEBL.

In response, we propose an ensemble approach, referred to as E2, to address both PNB's sensitivity to the estimate of $\hat { P } ( C _ { \mathrm { p } } )$ and PEBL's susceptibility to the accuracy of the initial set of strong negative examples. Specifically, we follow the two-stage framework of PEBL but extend each stage with an ensemble strategy to provide a more reliable single-class learning technique for spam filtering. Essentially, an ensemble classifier employs multiple classifiers (referred to as base classifiers) induced from a given set of training examples. To classify an unseen instance, the ensemble classifier combines predictions of the base classifiers through voting or some other mechanism [4,6,12,19,24,31]. Prior empirical results demonstrate that an ensemble classifier generally attains better classification effectiveness than individual base classifiers [12,13,31]. In this vein, to improve the accuracy of the initial set of strong negative examples in the first stage, the proposed E2 technique adopts an ensemble approach that combines the predictions made by PNB and the rough classifier of PEBL for the unlabeled examples. In addition, the second stage of the proposed E2 technique involves an ensemble classifier that adopts SVM [41], Naïve Bayes [16], and C4.5 [34] as its base classifiers. In this study, we empirically evaluate the proposed E2 technique with two spam filtering corpora and include PNB and PEBL as our performance benchmarks.

The remainder of this paper is organized as follows: In Section 2, we review PNB and PEBL for learning from positive and unlabeled documents and analyze their inherent limitations to highlight our motivation. In Section 3, we depict the design of the proposed E2 technique, including its overall process and algorithmic details. Subsequently, we describe our evaluation design and discuss important experimental results in Section 4. We conclude in Section 5 with a summary of this study and some future research directions.

## 2. Literature review

Single-class learning refers to a categorization problem that induces or trains a classification model solely on the basis of positive training examples and unlabeled instances. In this section, we review two single-class learning techniques, PNB and PEBL, and depict their limitations to highlight our research motivation.

## 2.1. Positive Naive Bayes (PNB)

As with classical Naïve Bayes classifiers, PNB assumes the existence of an underlying parametric model as a means to generate documents and therefore uses a collection of training examples to estimate the parameters of the generative model [11]. To categorize a new, unclassified document, it employs a Bayes rule and selects the class most likely to have generated the document.

Specifically, PNB takes a set PD of positive training examples and a set UD of unlabeled documents as inputs. Let $C _ { \mathrm { p } }$ be the positive class $( \mathrm { i . e . , }$ , spam emails in this study) and $C _ { \mathrm { n } }$ be the negative class (i.e., legitimate emails). Furthermore, let document $d _ { j }$ consist of n words $\{ w _ { 1 } , . . . , w _ { n } \}$ , with possible multiple occurrences of a word. PNB classifies $d _ { j }$ as a member of the class by:

$$
\operatorname{PNB} (d _ {j}) = \underset {C \in \{C _ {\mathrm{p}}, C _ {\mathrm{n}} \}} {\operatorname{argmax}} \hat {P} (C) \times \prod_ {i = 1} ^ {n} \hat {P r} (w _ {i} | C).
$$

PNB also assumes that an estimate $\hat { P } ( C _ { \mathfrak { p } } )$ of the class prior probability of $C _ { \mathrm { p } }$ is provided to the learner. Accordingly, PNB estimates each positive word probability $P r ( w _ { i } | C _ { \mathfrak { p } } )$ by the frequency with which w<sub>i</sub> occurs in the training documents of the positive class $C _ { \mathrm { p } } \left( \mathrm { i . e . , P D } \right)$ divided by the total number of word occurrences for the documents in PD. That is,

$$
\hat {P r} (w _ {i} | C _ {\mathrm{p}}) = \frac {N (w _ {i} , \mathrm{PD})}{N (\mathrm{PD})},
$$

where $N ( w _ { i } , \mathrm { P D } )$ is the total number of times $w _ { i }$ occurs in the documents in PD, and N(PD) is the total number of word occurrences in PD.

If a word $w _ { i }$ in document $d _ { j }$ does not appear in any documents in PD, $\hat { P r } ( w _ { i } | C _ { \mathfrak { p } } )$ becomes 0. Consequently, $\begin{array} { r } { \hat { P } ( C _ { p } ) \times \prod _ { i = 1 } ^ { n } \hat { P r } ( w _ { i } | C ) } \end{array}$ equals 0 as well. That is, doc-<sup>ð Þ</sup>ument $d _ { j }$ <sup>¼ ð j Þ</sup>will never be assigned to the positive class $C _ { \mathrm { p } }$ simply because of the occurrence of an unusual word in $d _ { j } .$ . To avoid the undesired bias caused by the described estimate of $P r ( w _ { i } | C _ { \mathfrak { p } } )$ , PNB adopts Lidstone's law of succession to smooth the maximum likelihood estimate [1] and defines

$$
\hat {P r} (w _ {i} | C _ {\mathrm{p}}) = \frac {N (w _ {i} , \mathrm{PD}) + \lambda}{N (\mathrm{PD}) + \lambda \times | V |},
$$

where $| V |$ is the number of distinct words in the training documents in PD, and $\lambda \geq 0$

In contrast, the prior probability $\hat { P } ( C _ { \mathrm { n } } )$ of class $C _ { \mathrm { n } }$ is estimated by $1 - \hat { P } ( C _ { \mathfrak { p } } )$ , and the estimate $\hat { P r } ( w _ { i } | C _ { \mathrm { n } } )$ of each negative word probability is derived as follows: Let $P r ( w _ { i } )$ be the probability that the underlying generative model creates $w _ { i } ,$ and let $P r ( C _ { \mathfrak { n } } )$ (or $P r ( C _ { \mathrm { p } } ) )$ be the probability that the generative model creates a word in a negative (positive) document. Accordingly, $P r ( w _ { i } ) =$ $P r ( w _ { i } | C _ { \mathrm { n } } ) \times P r ( C _ { \mathrm { n } } ) + P r ( w _ { i } | C _ { \mathrm { p } } ) \times P r ( C _ { \mathrm { p } } )$ . Because no negative training examples are available, the negative word probability of $w _ { i }$ is then estimated from the unlabeled documents, as follows:

$$
\hat {P r} (w _ {i} | C _ {\mathrm{n}}) = \frac {P r (w _ {i}) - P r (w _ {i} | C _ {\mathrm{p}}) \times P r (C _ {\mathrm{p}})}{1 - P r (C _ {\mathrm{p}})}.
$$

The probability $P r ( w _ { i } )$ can be estimated on the basis of the set of unlabeled documents, that is, $\hat { P r } ( w _ { i } ) =$ $\frac { \breve { N } ( w _ { i } , \mathrm { { U D } } ) } { N ( \mathrm { { U D } } ) }$ . Furthermore, according to the assumption that ð Þdocument length is independent of class, $P r ( C _ { \mathfrak { p } } )$ can be estimated as $\hat { P } ( C _ { \mathfrak { p } } )$ . Thus, the estimate for the negative word probability of $w _ { i }$ can be rewritten as:

$$
\hat {P r} (w _ {i} | C _ {\mathrm{n}}) = \frac {N (w _ {i} , \mathrm{UD}) - \hat {P r} (w _ {i} | C _ {\mathrm{p}}) \times \hat {P} (C _ {\mathrm{p}}) \times N (\mathrm{UD})}{(1 - \hat {P} (C _ {\mathrm{p}})) \times N (\mathrm{UD})}.
$$

Following smoothing of the estimates for positive word probabilities, the estimated negative word probability of $w _ { i }$ becomes:

$$
\hat {P r} (w _ {i} | C _ {\mathrm{n}}) = \frac {(N (w _ {i} , \mathrm{UD}) - \hat {P r} (w _ {i} | C _ {\mathrm{p}}) \times \hat {P} (C _ {\mathrm{p}}) \times N (\mathrm{UD})) + \lambda}{(1 - \hat {P} (C _ {\mathrm{p}})) \times N (\mathrm{UD}) + \lambda \times | V |}.
$$

Evidently, the unavailability of negative training examples means that most estimates $( \mathrm { e . g . } , \hat { P } ( C _ { \mathrm { n } } ) , \hat { P r } ( w _ { i } | C _ { \mathrm { n } } ) )$ involved in PNB are derived from the estimate $\hat { P } ( C _ { \mathrm { p } } )$ of the class prior probability of $C _ { \mathfrak { p } } .$ Therefore, the accuracy of $\hat { P } ( C _ { \mathrm { p } } )$ greatly determines the effectiveness of PNB. However, in a spam filtering application, because the percentage of spam emails varies significantly over time [11,40], an accurate estimate of $\cdot \hat { P } ( C _ { \mathrm { p } } )$ that conforms to the true class distribution at a particular point in time becomes difficult, and dynamic adjustments of the estimated $\hat { P } ( C _ { \mathfrak { p } } )$ over time are even more challenging, which limits PNB's applicability.

## 2.2. Positive Example-Based Learning (PEBL)

As an alternative, PEBL [44] attempts to induce a classification model capable of differentiating the boundary between positive and negative classes on the basis of a set PD of positive training examples and a set UD of unlabeled documents. PEBL adopts a two-stage framework: mapping and convergence. In the mapping stage, PEBL employs a rough classifier that draws an initial approximation of “strong negative” examples. Specifically, PEBL first identifies “strong positive” features by comparing the frequencies of features within the positive training versus the unlabeled examples and considers a feature a strong positive if it occurs frequently in the positive training examples in PD but rarely in the unlabeled examples in UD. Using this identified list of strong positive features, the PEBL technique selects as strong negative examples those unlabeled documents in UD that do not contain any strong positive features. The remaining documents in UD represent “plausible positive” examples.

In the convergence stage, PEBL constructs an initial classifier on the basis of the positive training examples and the strong negative examples identified in the previous stage. Next, PEBL iteratively detects and includes more negative examples from the unlabeled examples using SVM [41]. During each iteration, PEBL employs the classification model induced in the previous iteration to classify the current set of plausible positive examples into positive or negative classes. That is, PEBL expands the set of negative examples by incorporating negative examples identified during the iteration and then reconstructs a new classification model using SVM. The set of documents classified into the positive class becomes the set of plausible positive examples for the next iteration, and PEBL repeats both the negative example selection and the classification model reconstruction processes until it cannot find any more negative examples in the unlabeled examples in UD. From the convergence stage, PEBL discovers a class boundary that may eventually converge to the plausible boundary of the positive class in the feature space.

Evidently, the effectiveness of PEBL depends on the accuracy of the initial set of strong negative examples identified by the rough classifier in the mapping stage. If this initial set encompasses true positive examples however, the accuracy of negative examples identified in the convergence stage gradually deteriorates over iterations, degrading the resultant effectiveness of PEBL.

## 3. Design of proposed E2 technique

To address the aforementioned limitations of PNB and PEBL, we propose an ensemble approach, referred to as E2, for single-class learning for spam filtering. Specifically, we follow the two-stage framework of PEBL but extend each stage with an ensemble strategy. As we illustrate in Fig. 1, the overall process of the proposed E2 technique consists of two main stages: mapping via ensemble and convergence via ensemble. We detail each stage and the respective prediction process of E2 in the following subsections.

## 3.1. Mapping via ensemble

The mapping via ensemble stage begins with feature extraction and selection. For this study, we use all words in each document in the sets of positive training examples

![](/api/attachments/CEPZHWFE/fulltext/images/c740ef38f4a753ddfdf93799c797009f99dbf88c87ef2ad202d64107ff44e13c.jpg)  
Fig. 1. Overall process of E2 technique.

PD or unlabeled examples UD as the features of the document (i.e., without feature selection). We employ the Porter [33] stemmer to remove the suffixes and prefixes of words, then rely on the bag-of-words scheme for document representation. Therefore, each document (in PD or UD) is represented as a feature vector $< w _ { 1 } , . . . , w _ { k } >$ , where $w _ { i }$ is the term frequency of feature f in the document.

Subsequently, the mapping via ensemble stage employs an ensemble of two classifiers to identify strong negative examples from UD. Specifically, we use PNB and the rough classifier of PEBL and combine their predictions to form the initial set of strong negative examples. On the basis of the estimate of $\hat { P } ( C _ { \mathrm { p } } )$ , PNB classifies the unlabeled examples in UD into subsets of negative and positive examples. In contrast, the rough classifier of PEBL first identifies strong positive features from positive and unlabeled examples by comparing the frequency of features within PD and UD. Let $P ( f _ { i } , \mathrm { P D } )$ be the probability a feature $f _ { i }$ occurs in the positive examples and $P ( f _ { i } , \mathrm { U D } )$ be the probability it appears in the unlabeled examples. In this study, we define two parameters to determine if a feature is a strong positive: the positive threshold $( \alpha _ { \mathrm { P T } } )$ and the unlabeled threshold $( \alpha _ { \mathrm { U T } } )$ . If $P ( f _ { i } , \mathrm { P D } ) { > } \alpha _ { \mathrm { P T } }$ and $P ( f _ { i } , \mathrm { U D } ) { < } \alpha _ { \mathrm { U T } } ,$ we consider $f _ { i }$ a strong positive feature. Accordingly, we construct from PD and UD a list of strong positive features with respect to $\mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega }$ and $\alpha _ { \mathrm { U T } } .$ Furthermore, we consider an unlabeled example in UD that does not contain any of the strong positive features a strong negative example, according to the rough classifier of PEBL.

The decision combination step of the mapping via ensemble stage thus combines the classification results of the two base classifiers (i.e., PNB and the rough classifier) and selects as strong negative examples those unlabeled examples that both base classifiers consider negative. The use of this consensus-based strategy may improve the accuracy of the initial set of strong negative examples, which addresses PNB's sensitivity to the accuracy of the estimate of $P \Upsilon ( C _ { \mathrm { p } } )$ and PEBL's susceptibility to the accuracy of the initial set of strong negative examples. As a result, the mapping via ensemble stage produces an initial set of strong negative examples (referred to as $N _ { 1 } )$ and retains the remaining unlabeled examples as plausible positive examples $( P _ { 1 } )$

## 3.2. Convergence via ensemble

The convergence via ensemble stage constructs an ensemble classifier by adopting SVM [41], Naive Bayes [16], and C4.5 [34] as its base classifiers. Initially (i.e., iteration 1), both the positive training examples (PD) and the strong negative examples $( N _ { 1 } )$ from the mapping via ensemble stage form the training set $T S _ { 1 } \ ( \mathrm { i . e . , } T S _ { 1 } =$ $\mathrm { P D } \cup N _ { 1 } )$ for each of the three base classifiers. Each classifier then induces a classification model from the current training set and attempts to classify each plausible positive example in $P _ { 1 }$ . When all base classifiers suggest the negative class for a plausible positive example, it becomes a negative example in the next iteration; thus, forming an additional set of negative examples $N _ { 2 }$ for the next iteration. The remaining plausible positive examples then become $P _ { 2 }$ . During the next iteration i, the training set is defined as $T S _ { i } { = } T S _ { i - 1 } \cup N _ { i } ,$ which the three base classifiers use for retraining and to classify the plausible positive examples $P _ { i }$ into $N _ { i + 1 }$ and $P _ { i + 1 }$ . This process continues until no more negative examples can be extracted (i.e., $N _ { i + 1 } { = } O )$ ). Accordingly, we achieve an ensemble classifier that consists of three base classifiers and that we use to classify future unclassified documents.

## 3.3. Prediction

When receiving an unclassified document $( \mathrm { i . e . , e m a i l } ) .$ the proposed E2 technique uses the ensemble classifier constructed in the convergence via ensemble stage to classify the target document. For the ensemble decision, we employ a voting scheme, according to which if two or more base classifiers assign the unclassified document to the positive class (i.e., spam), we consider the target document a member of the positive class; otherwise, we include it in the negative class (i.e., legitimate email).

## 4. Empirical evaluation

In this section, we report our empirical evaluation of the proposed E2 technique, in which we use PNB and PEBL as performance benchmarks. We first describe our evaluation design, which includes the spam filtering corpora used for evaluation purposes, our evaluation procedure, and the evaluation criteria, and then discuss important evaluation results.

## 4.1. Spam filtering corpora

Our empirical evaluation employs two publicly available spam filtering corpora, namely, LingSpam and PU1.<sup>3</sup> The LingSpam corpus contains a total of 2893 emails, of which 481 (16.6%) are spam and 2412 (83.4%) are legitimate. The corpus author collected the 481 spam emails over a period of 22 months but excluded non-English emails and duplicate spam emails received on the same day and also removed attachments and HTML tags. The 2412 legitimate emails in LingSpam came from the Linguist list, a moderated, spam-free list about linguistics.

The PU1 corpus consists of 1099 emails: 481 (43.8%) spam messages and 618 (56.2%) legitimate emails. The spam emails are the same as those in the LingSpam corpus, whereas the 618 legitimate emails are English messages received and saved by the corpus author over a period of 36 months, with the exclusion of self-addressed messages, messages with empty bodies, and messages from regular correspondents.

## 4.2. Evaluation procedure and criteria

In the study, we assume only positive and unlabeled examples are available for training purposes, so we employ 40% of the spam emails in each spam filtering corpus as the positive training examples and use another 40% of the spam emails and 40% of the legitimate emails as the unlabeled examples. To maintain the class distribution in the set of unlabeled examples and the set of testing instances created from each spam filtering corpus, we create our testing set from the remaining 20% of spam emails and a randomly selected 20% of legitimate emails not included in the unlabeled set.

To minimize potential biases from the randomized sampling process and obtain more reliable performance estimates, we perform this validation process 30 times. The overall effectiveness of each single-class learning technique examined (E2 and the benchmark techniques) is then estimated by averaging the performance obtained from the 30 individual validation trials. We use three performance metrics to evaluate the effectiveness of each technique under investigation, including precision (for spam), recall (for spam), and accuracy.

## 4.3. Parameter-tuning results

We first conducted parameter-tuning experiments to determine appropriate values for the parameters involved in each technique. The rough classifier (in the mapping stage of PEBL and the mapping via ensemble stage of E2) involves the parameters $\mathsf { \alpha } _ { \mathrm { P T } }$ (positive threshold) and $\alpha _ { \mathrm { U T } }$ (unlabeled threshold) to identify strong positive features. In addition, PNB (the benchmark technique and one of the base classifiers in the mapping via ensemble stage of E2) requires the parameter λ to smooth the maximum likelihood estimate of word probability given a class. Finally, we also need to determine an appropriate value for $\lambda ,$ as required by Naive Bayes classifier that functions as a base classifier during the convergence via ensemble stage of E2.

We investigate the range of values for $\mathsf { \alpha } _ { \mathrm { P T } }$ from 0.1 to 0.7 in increments of 0.1. For each specific value for $\alpha _ { \mathrm { P T } } ,$ we examine the range of values for $\alpha _ { \mathrm { U T } }$ from 0.1 to the specified value in increments of 0.1. For both spam filtering corpora, our tuning results suggest that when both $\mathsf { \alpha } _ { \mathrm { P T } }$ and $\alpha _ { \mathrm { U T } }$ are set to 0.5, PEBL achieves the highest accuracy and recall rates and a satisfactorily high precision rate. Thus, we choose 0.5 for $\mathsf { \alpha } _ { \mathrm { P T } }$ and $\alpha _ { \mathrm { U T } }$ for our subsequent experiments.

To tune the parameter λ for PNB, we set $\hat { P } ( C _ { \mathfrak { p } } )$ to 0.5 and investigate different values for λ ranging from 0.3 to 3.9 in increments of 0.3. On the basis of a trade-off between the precision and recall rates, we select 2.7 and 2.1 for λ for the LingSpam and PU1 corpora, respectively. For the parameters involved in the mapping via ensemble stage, we adopt the values determined previously for $\mathsf { \alpha } _ { \mathrm { P T } }$ and $\alpha _ { \mathrm { U T } }$ for the rough classifier (i.e., 0.5 and 0.5) and λ for PNB (i.e., 2.7 for LingSpam and 2.1 for PU1). We then investigate different values of $\lambda ,$ ranging from 1.0 to 6.5 in increments of 0.5. Again trading off between the recall and precision rates, we determine values of 3.0 and 1.0 for the LingSpam and PU1 corpora, respectively. In Table 1, we summarize the parameter values selected for the three techniques under examination across the two spam filtering corpora.

## 4.4. Comparative evaluation results

Using the parameter values determined in the tuning experiments, we evaluate the performance of the proposed E2 technique for each spam filtering corpus, with the performance of PEBL and PNB as benchmarks. We first set $\hat { P } ( C _ { \mathrm { p } } )$ to 0.5 for PNB and E2 and will examine different values for $\hat { P } ( C _ { \mathrm { p } } )$ with regard to the effectiveness of PNB and E2 (see Section 4.5). As we illustrate in Table 2, for the LingSpam corpus, PNB (i.e., 99.13%) marginally outperforms E2 (98.45%) in accuracy, and both techniques outperform PEBL (93.29%) by a statistically significant difference at the 0.01 level. On the other hand, E2 achieves the highest precision rate (99.52%), whereas PEBL (93.16%) earns the worst. In terms of recall rate, PNB reaches the highest recall rate (96.25%), whereas the recall rate achieved by PEBL (64.41%) is far worse than that of either PNB or E2 (91.15%). Across all performance metrics evaluated, the effectiveness of our proposed E2 technique for the LingSpam corpus is comparable to that of PNB and significantly better, at the 0.01 level, than PEBL.

Table 1  
Summary of tuning results

<table><tr><td>Parameters</td><td>LingSpam</td><td>PU1</td></tr><tr><td> $\alpha_{\text{PT}}$  (PEBL and E2)</td><td>0.5</td><td>0.5</td></tr><tr><td> $\alpha_{\text{UT}}$  (PEBL and E2)</td><td>0.5</td><td>0.5</td></tr><tr><td> $\lambda$  (PNB and PNB in mapping via ensemble stage of E2)</td><td>2.7</td><td>2.1</td></tr><tr><td> $\lambda$  (Naïve Bayes in convergence via ensemble stage of E2)</td><td>3.0</td><td>1.0</td></tr></table>

As Table 3 shows, for the PU1 corpus, E2 achieves a higher accuracy (95.67%) than PNB (91.38%), and the difference is statistically significant at the 0.01 level. As with the LingSpam corpus, PEBL attains the lowest accuracy at 89.59%, significantly lower than that of E2 at the 0.01 level. In contrast, PEBL achieves the highest precision rate (96.09%) at the cost of its lowest recall (79.38%), whereas the precision rates of E2 and PNB are 92.81% and 92.99%, respectively. However, we record a recall rate of 97.81% for E2, significantly better (at the 0.01 level) than that achieved by PNB or PEBL (i.e., 86.98% and 79.38%, respectively).

Overall, across the two spam filtering corpora, our proposed E2 technique significantly outperforms PEBL in most performance metrics evaluated. The effectiveness (measured by accuracy, precision rate, and recall rate) attained by the proposed E2 technique is considered comparable to that achieved by PNB for the LingSpam corpus, but in general significantly better (at the 0.01 level) than that achieved by PNB for the PU1 corpus.

## 4.5. Sensitivity of E2 and PNB to $\hat { P } ( C _ { p } )$

Because both E2 and PNB involve an estimate of $\hat { P } ( C _ { \mathrm { p } } )$ , we examine the effects of the accuracy of $\hat { P } ( C _ { \mathrm { p } } )$

Table 2  
Comparative evaluation results for LingSpam

<table><tr><td></td><td>Accuracy (%)</td><td>Precision (%)</td><td>Recall (%)</td></tr><tr><td>E2</td><td>98.45</td><td>99.52</td><td>91.15</td></tr><tr><td>PNB</td><td>99.13</td><td>98.49</td><td>96.25</td></tr><tr><td>PEBL</td><td>93.29</td><td>93.16</td><td>64.41</td></tr></table>

Table 3  
Comparative evaluation results for PU1

<table><tr><td></td><td>Accuracy (%)</td><td>Precision (%)</td><td>Recall (%)</td></tr><tr><td>E2</td><td>95.67</td><td>92.81</td><td>97.81</td></tr><tr><td>PNB</td><td>91.38</td><td>92.99</td><td>86.98</td></tr><tr><td>PEBL</td><td>89.59</td><td>96.09</td><td>79.38</td></tr></table>

on the classification effectiveness of PNB and E2. Specifically, we simulate various scenarios by setting different values for $\hat { P } ( C _ { \mathrm { p } } )$ , whether close to the true probability (i.e., 0.2 for LingSpam and 0.4 for PU1), neutral (i.e., at 0.5, such that PNB's prior probability does not favor any class), and far from the true prior probability (i.e., 0.9 for both corpora). As Table 4 depicts, for the LingSpam corpus, the accuracy of E2 is 98.17%, 98.45%, and 98.45% when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 2 , 0 . 5 ,$ and 0.9, respectively. That is, the difference in accuracy between the two extreme scenarios (i.e., $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 9 \ \mathrm { v s }$ $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 2 )$ is marginal (i.e., 0.28%). For the same corpus, PNB records classification accuracies of 97.57%, 99.13%, and 98.32% when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 2 , 0 . 5 ,$ and 0.9, respectively. The accuracy differential between the two extreme scenarios is 0.75%, which is slightly greater than that of the proposed E2 technique. This result suggests that different values for $\hat { P } ( C _ { \mathrm { p } } )$ appear to have marginal effects on the accuracy of both techniques, though E2 performs slightly better than PNB in accuracy when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 2$ and 0.9.

The precision rates of E2 are 99.39%, 99.52%, and 99.41% when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 2 , 0 . 5 .$ , and 0.9, respectively; the minor difference (0.02%) in precision rates between the two extreme scenarios suggests the stability of the proposed E2 technique over the range of $\hat { P } ( C _ { \mathrm { p } } )$ values examined. In contrast, the precision rate of PNB decreases from 99.84% when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 2$ to 95.30% when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 9$ . This large precision gap (i.e., 4.54%) implies PNB is susceptible to $\hat { P } ( C _ { \mathrm { p } } )$ . Moreover, our empirical evaluations also suggest that the recall rate attained by PNB is susceptible to $\hat { P } ( C _ { \mathfrak { p } } )$ but that achieved by E2 is less sensitive to $\hat { P } ( C _ { \mathrm { p } } )$ . Specifically, the difference in recall between the two extreme scenarios recorded by PNB is 9.10%, whereas that by E2 is only 1.70%.

We observe similar results in the PU1 corpus. As we show in Table 5, the accuracy of E2 is 95.77%, 95.67%, and 94.62% when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 4 , 0 . 5$ , and 0.9, respectively, whereas that of PNB is 91.24%, 91.38%, and 85.18%. That is, E2 outperforms PNB in terms of accuracy across different $\hat { P } ( C _ { \mathrm { p } } )$ settings. Furthermore, different values for $\hat { P } ( C _ { \mathrm { p } } )$ appear to have marginal effects on the accuracy of E2 (accuracy differential = 1.15% between two extreme scenarios) but remarkable effects on the accuracy of PNB (accuracy differential = 6.06%). Similarly, the precision and recall rates achieved by E2 remain stable over the range of values of $\hat { P } ( C _ { \mathrm { p } } ) ;$ the precision and recall rate differences between the two extreme scenarios are just 2.59% and 0.62%, respectively. In contrast, the precision rate of PNB decreases from 95.26% when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 4$ to 77.61% when $\hat { P } ( C _ { \mathrm { p } } ) { = }$ 0.9, a remarkable difference of 17.65%. Likewise, the recall rate of PNB varies from 84.24% when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 4$ to 93.54% when $\hat { P } ( C _ { \mathrm { p } } ) { = } 0 . 9$ , again exhibiting the substantial difference in recall rates (i.e., 9.31%) between the two scenarios.

Sensitivity of E2 and PNB to $\hat { P } ( C _ { \mathrm { p } } )$ for LingSpam

<table><tr><td colspan="2"></td><td>Close to true  $P(C_p)$ (i.e., $\hat{P}(C_p)=0.2$ ) (%)</td><td> $\hat{P}(C_p)=0.5$  (%)</td><td>Far from true  $P(C_p)$ (i.e., $\hat{P}(C_p)=0.9$ ) (%)</td><td> $\Delta$  (%)</td></tr><tr><td rowspan="3">E2</td><td>Accuracy</td><td>98.17</td><td>98.45</td><td>98.45</td><td>0.28</td></tr><tr><td>Precision</td><td>99.39</td><td>99.52</td><td>99.41</td><td>0.02</td></tr><tr><td>Recall</td><td>89.55</td><td>91.15</td><td>91.25</td><td>1.70</td></tr><tr><td rowspan="3">PNB</td><td>Accuracy</td><td>97.57</td><td>99.13</td><td>98.32</td><td>0.75</td></tr><tr><td>Precision</td><td>99.84</td><td>98.49</td><td>95.30</td><td>-4.54</td></tr><tr><td>Recall</td><td>85.52</td><td>96.25</td><td>94.62</td><td>9.10</td></tr></table>

Notes: Δ denotes the effectiveness difference, calculated as (effectiveness attained by far from true $P ( C _ { \mathfrak { p } } )$ − effectiveness attained by close to true $P ( C _ { \mathfrak { p } } ) )$

Judging from all performance metrics, PNB appears susceptible to $\hat { P } ( C _ { \mathfrak { p } } )$ in both spam filtering corpora, whereas E2 remains stable over the range of $\hat { P } ( C _ { \mathfrak { p } } )$ investigated. Furthermore, across the range of $\hat { P } ( C _ { \mathfrak { p } } ) ,$ E2 can maintain its accuracy at least at the 98.17% level, its precision rate at the 99.39% level, and its recall rate at the 89.55% level for the LingSpam corpus, whereas PNB can only maintain these performance metrics at the 97.57%, 95.30%, and 85.52% levels, respectively. Similarly, in the PU1 corpus, the minimum accuracy, precision rate, and recall rate achieved by E2 are 94.62%, 90.62%, and 97.60% over the range of $\hat { P } ( C _ { \mathfrak { p } } )$ investigated, but those attained from PNB are only

85.18%, 77.61%, and 84.24%, respectively. Overall, our evaluation results suggest the utility of the ensemble strategy employed by E2.

## 4.6. Effects of size of positive training examples

We further examine the sensitivity of the different techniques to the size of the positive training examples. In the preceding experiments, we use 40% of spam emails from the spam corpus as the positive training examples and another 40% of spam emails and 40% of legitimate emails as the unlabeled examples for training. In this experiment, we instead fix the size of the unlabeled examples for training and vary the size of the positive training examples to range from 40% to 20% in decrements of 5%. We set $\hat { P } ( C _ { \mathrm { p } } )$ to 0.5 for PNB and E2 and employ the parameter values previously determined for each technique investigated (see Table 1).

For the LingSpam corpus, as we show in Fig. 2(a), the accuracy of E2 is slightly worse than that of PNB over the range of sizes of positive training examples, though the difference is not statistically significant. In contrast, the accuracy of PEBL is substantially inferior to that of E2, especially when the size of the positive training examples falls between 25% and 40% of the LingSpam corpus. In addition, E2 remains very steady in terms of its

Sensitivity of E2 and PNB to $\hat { P } ( C _ { \mathfrak { p } } )$ for PU1

<table><tr><td colspan="2"></td><td>Close to true  $P(C_p)$ (i.e.,  $\hat{P}(C_p)=0.4$ ) (%)</td><td> $\hat{P}(C_p)=0.5$  (%)</td><td>Far from true  $P(C_p)$ (i.e.,  $\hat{P}(C_p)=0.9$ ) (%)</td><td>Δ</td></tr><tr><td rowspan="3">E2</td><td>Accuracy</td><td>95.77</td><td>95.67</td><td>94.62</td><td>-1.15</td></tr><tr><td>Precision</td><td>93.20</td><td>92.81</td><td>90.62</td><td>-2.59</td></tr><tr><td>Recall</td><td>97.60</td><td>97.81</td><td>98.23</td><td>0.62</td></tr><tr><td rowspan="3">PNB</td><td>Accuracy</td><td>91.24</td><td>91.38</td><td>85.18</td><td>-6.06</td></tr><tr><td>Precision</td><td>95.26</td><td>92.99</td><td>77.61</td><td>-17.65</td></tr><tr><td>Recall</td><td>84.24</td><td>86.98</td><td>93.54</td><td>9.31</td></tr></table>

Notes: Δ denotes the effectiveness difference, calculated as (effectiveness attained by far from true $P ( C _ { \mathfrak { p } } )$ − effectiveness attained by close to true $P ( C _ { \mathrm { p } } ) )$

![](/api/attachments/CEPZHWFE/fulltext/images/97b1243a9e3a6305932283d34f6982f5d04dae2587ed2ef8ab7b0d8244b439e5.jpg)  
(a) Accuracy

![](/api/attachments/CEPZHWFE/fulltext/images/53dd12265c643b335e4aa81c2c56332bb7226795119b1200ad7a3ac9dce97833.jpg)  
(b) Precision Rate

![](/api/attachments/CEPZHWFE/fulltext/images/f16f7496cbf8c6c4c4cb6f736ec25debc3e94632b65854120e4db0904a352a9b.jpg)  
(c) Recall Rate  
Fig. 2. Effects of size of positive training examples (LingSpam Corpus).

precision rate and superior to the benchmark techniques at any size of positive training examples examined, as we depict in Fig. 2(b). As with E2, the precision rates attained by PNB and PEBL appear largely insensitive to the size of the positive training examples. However, for any size of the positive training examples, PEBL achieves a lower precision rate than E2 or PNB. Similarly, as we show in Fig. 2(c), the recall rate of PEBL remains inferior to that of E2 and PNB for any size of positive training examples. However, we note that all single-class learning techniques under investigation experience a large decline in recall rate when the size of the positive training examples decreases from 40% to 20% in the LingSpam corpus. This result highlights the

strong dependence of single-class learning techniques on the size of the positive training examples, because they lack access to negative training examples. However, because collecting many positive training examples is relatively attainable in a spam filtering application, compared with other applications, this sensitivity of singleclass learning techniques may not pose a serious constraint for our target application.

For the PU1 corpus, as we depict in Fig. 3(a), the accuracy of E2 improves noticeably over that of PNB and PEBL for the range of sizes of positive training examples examined. The accuracy difference between

![](/api/attachments/CEPZHWFE/fulltext/images/93b50833fa0768bcd2619cb976cee63578f2cdac428c0bd0226c5a32614e344e.jpg)  
(a) Accuracy

![](/api/attachments/CEPZHWFE/fulltext/images/8a30559657294aa160efb0d9d1be70d298d66b0ddcc17f2fcddd28490bc53791.jpg)  
(b) Precision Rate

![](/api/attachments/CEPZHWFE/fulltext/images/7ce336cdad0fbb7ab6fe9ad89c948b3be63358e968c498456dc2573f223e32de.jpg)  
(c) Recall Rate  
Fig. 3. Effects of size of positive training examples (PU1 Corpus).

E2 and PNB generally remains constant, but that between E2 and PEBL expands as the size of the positive training examples decreases from 40% to 20% in the PU1 corpus. With respect to precision rate (see Fig. 3(b)), PEBL marginally outperforms E2 and PNB when the size of the positive training examples is greater than 25% of the corpus, but at smaller levels, all three precision rates are comparable. As we found for the LingSpam corpus, all investigated single-class learning techniques experience a moderate or even large decline in recall rates when the size of the positive training examples decreases from 40% to 20% of the PU1 corpus (Fig. 3(c)). However, the recall rate achieved by E2 is always significantly higher than that of PNB, and PEBL attains the worst recall rate for any size of positive training examples investigated for the PU1 corpus.

## 5. Conclusion and future research directions

In many spam filtering scenarios, obtaining legitimate emails for training purposes provides a far greater challenge than collecting spam and unclassified emails. Hence, it is more appropriate to construct a classification model for spam filtering that only requires positive (i.e., spam emails) and unlabeled instances. Several singleclass learning techniques, such as PNB and PEBL, have been proposed in the literature. However, they face fundamental limitations in applications to spam filtering. In this study, we propose and develop an ensemble approach, referred to as E2, to address PNB's sensitivity to the estimate $\hat { P } ( C _ { \mathrm { p } } )$ and PEBL's susceptibility to the accuracy of the initial set of strong negative examples. We follow the two-stage framework of PEBL and extend each stage with an ensemble strategy. The empirical evaluation results from two spam filtering corpora suggest that our proposed E2 technique generally outperforms the benchmark techniques (i.e., PNB and PEBL) and exhibits more stable performance than its counterparts.

Some further research topics that could extend this study include the following. First, though our proposed E2 technique is less insensitive to $\hat { P } ( C _ { \mathfrak { p } } )$ (i.e., estimate of the prior probability of the spam class), inaccurate estimates of $\hat { P } ( C _ { \mathrm { p } } )$ have some negative effects on its precision rate. Because the percentage of spam emails varies significantly over time, development of an effective mechanism for estimating $\hat { P } ( C _ { \mathfrak { p } } )$ is essential to the proposed E2 technique. Second, the topics of spam emails change constantly. Thus, adaptive learning ability of single-class learning techniques will be highly relevant and desirable in the spam filtering context, as well as in similar application scenarios. Third, our empirical evaluation results indicate the unsatisfactory performance by all single-class learning techniques when the size of the positive training examples is relatively small. Therefore, to extend applications of the proposed E2 technique beyond spam filtering, additional research should attempt to enhance its effectiveness by addressing learning from a small positive training set. Fourth, in this study, we use only SVM, Naive Bayes, and C4.5 as base classifiers in the convergence via ensemble stage of E2. Inclusion and empirical evaluation of different base classifiers represents an interesting research direction. Fifth and finally, we only consider a monolingual spam filtering problem in this study. In the future, the proposed E2 technique should be extended to deal with multilingual spam filtering on the basis of positive and unlabeled training emails written in different languages.

## Acknowledgement

This work was supported by the National Science Council of the Republic of China under the grants NSC 94-2416-H-110-002, NSC 95-2416-H-218-019, and NSC 95-2752-H-007-004-PAE.

## References

[1] R. Agrawal, R. Bayardo, R. Srikant, Athena: mining-based interactive management of text databases, Proceedings of the 7th International Conference on Extending Databases Technology (EDBT00), Konstanz, Germany, 2000, pp. 365–379.

[2] I. Androutsopoulos, J. Koutsias, K.V. Chandrinos, G. Paliouras, C.D. Spyropoulos, An evaluation of Naive Bayesian anti-spam filtering, Proceedings of Workshop on Machine Learning in the New Information Age, Barcelona, Spain, 2000, pp. 9–17.

[3] I. Androutsopoulos, J. Koutsias, K.V. Chandrinos, C.D. Spyropoulos, An experimental comparison of Naive Bayesian and keyword-based anti-spam filtering with encrypted personal e-mail messages, Proceedings of the 23rd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Athens, Greece, 2000, pp. 160–167.

[4] E. Bauer, R. Kohavi, An empirical comparison of voting classification algorithms: bagging, boosting, and variants, Machine Learning 36 (1–2) (1999) 105–139.

[5] P.O. Boykin, V.P. Roychowdhury, Leveraging social networks to fight spam, IEEE Computer 38 (4) (2005) 61–68.

[6] L. Breiman, Stacked regressions, Machine Learning 24 (1) (1996) 49–64.

[7] X. Carreras, L. Márquez, Boosting trees for anti-spam email filtering, Proceedings of the 4th International Conference on Recent Advances in Natural Language Processing (RANLP), Bulgaria, 2001, pp. 58–64.

[8] W. Cohen, Learning rules that classify e-mail, Proceedings of AAAI Spring Symposium on Machine Learning in Information Access, Stanford, CA, 1996, pp. 18–25.

[9] P. Cunningham, N. Nowlan, S.J. Delany, M. Haahr, A case-based approach to spam filtering that can track concept drift, Proceedings of International Conference on Case-Based Reasoning, Trondheim, Norway, June 2003.

[10] F. De Comité, F. Denis, R. Gilleron, F. Letouzey, Positive and unlabeled examples help learning, Lecture Notes in Artificial Intelligence 1720 (1999) 219–230.

[11] F. Denis, R. Gilleron, M. Tommasi, Text classification from positive and unlabeled examples, Proceedings of the 9th International Conference on Information Processing and Management of Uncertainty in Knowledge-Based Systems, 2002, pp. 1927–1934.

[12] T.G. Dietterich, Ensemble methods in machine learning, Proceedings of the First International Workshop on Multiple Classifier Systems, 2000, pp. 1–15.

[13] Y.S. Dong, K.S. Han, A comparison of several ensemble methods for text categorization, Proceedings of 2004 IEEE International Conference on Services Computing, September 2004, pp. 419–422.

[14] H. Drucker, D. Wu, V. Vapnik, Support vector machines for spam categorization, IEEE Transactions on Neural Networks 10 (5) (1999) 1048–1054.

[15] D. Fallows, Spam: How It Is Hurting E-Mail and Degrading Life on the Internet, Technical Report (Pew Internet and American Life Project), October 2003, available at http://www.pewinternet. org/reports/toc.asp?Report=102.

[16] I.J. Good, The Estimation of Probabilities: an Essay on Modern Bayesian Methods, MIT Press, Cambridge, MA, 1965.

[17] J. Goodman, G.V. Cormack, D. Heckerman, Spam and the ongoing battle for the inbox, Communications of the ACM 50 (2) (2007) 24–33.

[18] P. Graham, A Plan for Spam, , August 2002 available at http:/ www.paulgraham.com/spam.html.

[19] L. Hansen, P. Salamon, Neural network ensembles, IEEE Transactions on Pattern Analysis and Machine Intelligence 12 (10) (1990) 993–1001.

[20] J.M. Hidalgo, G.C. Bringas, E.P. Sanz, F.C. Garcia, Content based SMS spam filtering, Proceedings of the 2006 ACM Symposium on Document Engineering, Amsterdam, The Netherlands, 2006, pp. 107–114.

[21] J. Hovold, Naïve Bayes spam filtering using word-position-based attributes, Proceedings of the 2nd Conference on Email and Anti Spam, Stanford, CA, 2005.

[22] T. Joachims, Text categorization with support vector machines: learning with many relevant features, Proceedings of the 10th European Conference on Machine Learning (ECML 98), Chemnitz, Germany, 1998, pp. 137–142.

[23] A. Kolcz, J. Alspector, SVM-based filtering of email spam with content-specific misclassification costs, Proceedings of Workshop on Text Mining, Chicago, IL, 2001.

[24] L. Larkey, W. Croft, Combining classifiers in text categorization, Proceedings of the 19th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Zurich, Switzerland, 1996, pp. 289–297.

[25] F. Letouzey, F. Denis, R. Gilleron, Learning from positive and unlabeled examples, Proceedings of the 11th International Conference on Algorithmic Learning Theory, Sydney, Australia, December 2000, pp. 71–85.

[26] X. Li, B. Liu, Learning to classify text using positive and unlabeled data, Proceedings of the 18th International Joint Conference on Artificial Intelligence (IJCAI-03), Acapulco, Mexico, August 2003, pp. 587–594.

[27] B. Liu, W.S. Lee, P.S. Yu, X. Li, Partially supervised classification of text documents, Proceedings of the 19th International Conference on Machine Learning (ICML-2002), Sydney, Australia, July 2002, pp. 387–394.

[28] B. Masand, G. Linoff, D. Waltz, Classifying news stories using memory based reasoning, Proceedings of the 15th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Copenhagen, Denmark, 1992, pp. 59–65.

[29] Messaging Anti-Abuse Working Group, MAAWG Email Metrics Program, First Quarter 2006 Report, June 2006, available at www.maawg.org/about/FINAL\_1Q2006\_Metrics\_Report.pdf.

[30] V. Metsis, I. Androutsopoulos, G. Paliouras, Spam filtering with Naïve Bayes—which Naïve Bayes? Proceedings of the 3rd Conference on Email and Anti-Spam, Mountain View, CA, July 2006.

[31] D. Opitz, R. Maclin, Popular ensemble methods: an empirical study, Journal of Artificial Intelligence Research 11 (1999) 169–198.

[32] P. Pantel, D. Lin, SpamCop: a spam classification and organization program, Proceedings of 1998 Workshop on Learning for Text Categorization, Madison, WI, 1998.

[33] M.F. Porter, An Algorithm for Suffix Stripping, Program 14 (3) (1980) 130–137 (Porter Stemming Algorithm also available at http://www.tartarus.org/\~martin/PorterStemmer/.).

[34] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993.

[35] M. Sahami, S. Dumais, D. Heckerman, E. Horvitz, A Bayesian approach to filtering junk e-mail, Proceedings of 1998 Workshop on Learning for Text Categorization, Madison, WI, 1998.

[36] G. Sakkis, I. Androutsopoulos, G. Paliouras, V. Karkaletsis, C. Spyropoulos, P. Stamatopoulos, A memory-based approach to anti-spam filtering for mailing lists, Information Retrieval 6 (1) (2003) 49–73.

[37] K.M. Schneider, A comparison of event models for Naïve Bayes anti-spam e-mail filtering, Proceedings of the 10th Conference of the European Chapter of the Association for Computational Linguistics, Budapest, Hungary, 2003, pp. 307–314.

[38] K.M. Schneider, On word frequency information and negative evidence in Naïve Bayes text classification, Proceedings of the 4th International Conference on Advances in Natural Language Processing, Alicante, Spain, 2004, pp. 474–485.

[39] F. Sebastiani, Machine learning in automated text categorization, ACM Computing Surveys 34 (1) (2002) 1–47.

[40] C. Taylor, Spam's big bang, Time (June 16, 2003) 51.

[41] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer-Verlag, New York, NY, 1995.

[42] S.M. Weiss, C. Apte, F.J. Damerau, D.E. Johnson, F.J. Oles, T. Goetz, T. Hampp, Maximizing text-mining performance, IEEE Intelligence Systems 14 (4) (1999) 63–69.

[43] B. Whitworth, E. Whitworth, Spam and the social-technical gap, IEEE Computer 37 (10) (2004) 38–45.

[44] H. Yu, J. Han, K.C.C. Chang, PEBL: web page classification without negative examples, IEEE Transaction on Knowledge and Data Engineering 16 (1) (2004) 70–81.

[45] L. Zhang, T. Yao, Filtering junk mail with a maximum entropy model, Proceedings of the 20th International Conference on Computer Processing of Oriental Languages (ICCPOL 03), 2003, pp. 446–453.

[46] L. Zhang, J. Zhu, T. Yao, An evaluation of statistical spam filtering techniques, ACM Transactions on Asian Language Information Processing 3 (4) (2004) 243–269.

[47] V. Zorkadis, M. Panayotou, D.A. Karras, Improved spam e-mail filtering based on committee machines and information theoretic feature extraction, Proceedings of International Joint Conference on Neural Networks, Montreal, Canada, 2005, pp. 179–184.

![](/api/attachments/CEPZHWFE/fulltext/images/289cda9b3d000bb1bfdc2218498a73c37813ae5cb5b0be6b54cfcaf31acd805a.jpg)

Chih-Ping Wei received a BS in Management Science from the National Chiao-Tung University in Taiwan, R.O.C. in 1987 and an MS and a Ph.D. in Management Information Systems from the University of Arizona in 1991 and 1996. He is currently a professor of Institute of Technology Management at National Tsing Hua University in Taiwan, R.O.C. Prior to joining the National Tsing Hua University in 2005, he was a faculty member at Department of Information Man-

agement at National Sun Yat-sen University in Taiwan since 1996 and a visiting scholar at the University of Illinois at Urbana-Champaign in Fall 2001 and the Chinese University of Hong Kong in Summer 2006 and 2007. His papers have appeared in Journal of Management Information Systems (JMIS), Decision Support Systems (DSS), IEEE Transactions on Engineering Management, IEEE Software, IEEE Intelligent Systems, IEEE Transactions on Systems, Man, Cybernetics, IEEE Transactions on Information Technology in Biomedicine, European Journal of Information Systems, Journal of Database Management, Information Processing and Management, and Journal of Organizational Computing and Electronic Commerce, etc. His current research interests include knowledge discovery and data mining, information retrieval and text mining, knowledge management, multidatabase management and integration, and data warehouse design. He has edited special issues of Decision Support Systems, International Journal of Electronic Commerce, and Electronic Commerce Research and Applications. He can be reached at Institute of Technology Management, National Tsing Hua University, Hsinchu, Taiwan, R.O.C; cpwei@mx.nthu. edu.tw.

![](/api/attachments/CEPZHWFE/fulltext/images/223a2fbafca3479004ba5fb08eaba6d8ab47e6f2f8858c764455840dc053b553.jpg)

Hsueh-Ching Chen received an MS degree in Management Information Systems from National Sun Yat-sen University, Taiwan, in 2006. She is currently a specialist in Allion Computer Inc, Taiwan. Her research interests include data mining, text categorization, and information retrieval. She can be reached at No. 14, Lane 160, Fu Yang St., Taipei City, Taiwan, R.O.C; jinachen@allion.com.

![](/api/attachments/CEPZHWFE/fulltext/images/c46e0b52c85e497ae4e47ceff6443c6fefa4be2a118269aa68a9c57ade92c5ed.jpg)

Tsang-Hsiang Cheng received a BS in Information Science and an MBA in Management Information Systems from the National Chiao-Tung University in Taiwan, R.O.C. in 1989 and 1991, and a Ph.D. in Management Information Systems from the National Sun Yat-Sen University in Taiwan, R.O.C. in 2003. He is currently an associate professor of Department of Business Administration at Southern Taiwan University in Taiwan, R.O.

C. His papers have appeared (including forthcoming) in IEEE Transactions on Systems, Man, Cybernetics Part A: Systems and Humans, Decision Support Systems, Journal of Database Management, and Information Processing and Management, etc. His current research interests include knowledge discovery and data mining, information retrieval and text mining, knowledge management, and medical informatics. He can be reached at the Department of Business Administration at Southern Taiwan University of Technology, Tainan County, Taiwan, R.O.C; cts@mail.stut.edu.tw.
