---
otero_id: 2820
otero_key: "Y6ZR92ME"
title: "RubE: Rule-based methods for extracting product features from online consumer reviews"
authors: "Yin Kang; Lina Zhou"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2016.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

## Title: RubE: Rule-based Methods for Extracting Product Features from Online Consumer Reviews

## Author: Yin Kang Lina Zhou

![](/api/attachments/Y6ZR92ME/fulltext/images/a86b868a74abbc232cc3d03913bb05d7dc31b9486f036e6305b2e9e1c8ac4e18.jpg)

PII: S0378-7206(16)30054-4

DOI: http://dx.doi.org/doi:10.1016/j.im.2016.05.007

Reference: INFMAN 2911

To appear in: INFMAN

Received date: 12-5-2015

Revised date: 12-1-2016

Accepted date: 26-5-2016

Please cite this article as: Yin Kang, Lina Zhou, RubE: Rule-based Methods for Extracting Product Features from Online Consumer Reviews, Information and Management http://dx.doi.org/10.1016/j.im.2016.05.007

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# RubE: Rule-based Methods for Extracting Product Features from Online Consumer Reviews

Yin Kang\*, Lina Zhou

Department of Information Systems, University of Maryland, Baltimore County, 1000

Hilltop Circle, Baltimore, MD 21250, USA

Corresponding Author”

Yin Kang

Department of Information Systems

University of Maryland

Baltimore County

1000 Hilltop Circle

Baltimore

MD 21250

USA

E-mail: [ky6, zhoul]@umbc.edu

Highlights

 The rule-based method is useful for analyzing online consumer reviews.

 The performance of feature extraction can be improved by recognizing different types of features and through design of extraction methods for each type of features separately.

 For product feature extraction, subjective feature-oriented methods perform better than objective feature-oriented methods.

 Direct dependency relation and review-specific patterns resulted in best recall in each category.

 The generality of rule-based methods can be approached by developing domain-independent rules and pruning strategies.

## ABSTRACT

Motivated by the role of product features in enabling personalized recommendations and marketing, this research aims to extract product features from online consumer reviews. Previous studies are dominated by statistical-based techniques or focused on subjective features that are associated with opinions. In this research, we propose RubE − unsupervised rule-based methods that extract both subjective and objective features from online consumer reviews. We identify objective features by incorporating part–whole relation and review-specific patterns. We extract subjective feature by extending double propagation with indirect dependency and comparative construction. The experiment results demonstrate that RubE significantly outperforms the state-of-the-art techniques for product feature extraction and is generalizable from search goods to experience goods.

Keywords: product feature extraction, rule-based method, objective feature, indirect dependency relation

## INTRODUCTION

Online consumer reviews are central to the emergence of social commerce (Zhou, Zhang, & Zimmermann, 2013). As a form of online word-of-mouth (Dellarocas, 2003), these reviews are used to supplement expert reviews and product descriptions with actual usage experience of consumers. Compared with manufacturer descriptions, consumer reviews are considered unbiased, comprehensive, and credible (Jensen, Averbeck, Zhang, & Wright, 2013). Such reviews can help potential buyers make better purchase decisions by reducing uncertainty (Dimoka, Hong, & Pavlou, 2012; Wu, Wu, Sun, & Yang, 2013), search cost, and switching cost (X. X. Li, Hitt, & Zhang, 2011). However, harnessing the power of online consumer reviews is limited by our ability to process the large volume of review data. Automatic product feature extraction has emerged as a promising direction to tap into the potential of online reviews.

The extraction of product features (e.g., attributes and parts) is important for consumers because they care about and have their preference for specific product features (S. Li, Zhou, & Li, 2015). Understanding the role of product features and how they affect consumers’ shopping behavior is important in marketing (Du, Hu, & Damangir, 2015). In addition, feature extraction is fundamental to other complex analyses of online reviews that have significant implications for marketing application, including feature-based opinion mining (K. Liu, Xu, & Zhao, 2014; Poria, Cambria, Winterstein, & Huang, 2014; Probst, Ghani, Krema, Fano, & Liu, 2007; Qiu, Liu, Bu, & Chen, 2011; Xu, Liu, Lai, Chen, & Zhao, 2013), personalized product recommendation (Scaffidi et al., 2007), review summarization (Xiong, 2013), and review helpfulness assessment (Archak, Ghose, & Ipeirotis, 2011; Kim, Pantel, Chklovski, & Pennacchiotti, 2006; J. Liu, Cao, Lin, Huang, & Zhou, 2007; Xiong, 2013).

There has been an extensive amount of work on product feature extraction. Various

#

methods have been applied to this problem, including statistical methods such as hidden Markov model (HMM) (Wong & Lam, 2005) and conditional random field (CRF) (Jakob & Gurevych, 2010; Yang & Cardie, 2013) and rule-based methods (RbMs) such as double propagation (DP) (Qiu et al., 2011). Despite their gradual improvement to the performance in product feature extraction, the state-of-the-art methods expose several limitations: (1) they were dominated by statistical techniques but gave little attention to RbMs. Some recent studies (Poria, Cambria, Ku, Gui, & Gelbukh, 2014; Qiu et al., 2011) provided evidence that RbMs can be effective for product feature extraction. In contrast to statistical methods, RbMs do not rely on training corpora, which remain hard to obtain and difficult to prepare. (2) Only a small number of RbMs (e.g., Qiu et al., 2011) were focused on subjective features on which reviewers had explicitly expressed opinions while ignoring nonsubjective features that were not associated with opinions (i.e., objective features); in addition, they did not address the complexity of indirect dependency in developing the rules, which could hurt the recall. 3) Previous pruning methods mainly relied on product-specific heuristics and information to improve the precision of feature extraction (e.g., Hu & Liu, 2004; Qiu et al., 2011), which are difficult to generalize across different types of products. On a related note, most studies have focused on online reviews of search goods (e.g., electronic products), but omitted those of experience goods. For instance, none of the studies has addressed online movie reviews, which pose a number of unique challenges to feature extraction (Zhou & Chaovalit, 2008).

This research aims to improve product feature extraction by addressing the above-mentioned limitations. We propose unsupervised rule-based extraction (RubE) methods to extract both objective and subjective product features from online consumer reviews. We extract objective features by discovering part–whole relations and review-specific patterns. We extract subjective features by extending DP (Qiu et al., 2011)

#

with two new types of linguistic structures: indirect dependency and comparative constructions. This research makes multifold contribution to the literature. First, we introduce a new classification scheme of product features in online consumer views (i.e., subjective vs. objective categories) that can guide the design of RbMs for feature extraction. Second, we improve the recall of product feature extraction by addressing objective feature extraction for the first time and by improving the extraction of subjective features. Third, we improve the precision of feature extraction by introducing a two-step domain-independent pruning method based on semantic similarity and document frequency. In addition, we provide evidence for the superior generality of RubE to previous RbMs.

The remainder of this paper is organized as follows: we first review previous literature as related to our research setting; we then propose our feature extraction methods – RubE –– followed by the introduction of our data collection, experiment design, and results; finally, we discuss our findings and conclude the paper with future work.

## DEFINITIONS AND RELATED WORK

## A New Classification Scheme

We use “feature” as a generic term to refer to attributes, components, and related concepts of both the object as a whole and its parts. Product features have been classified as explicit and implicit categories based on whether the related feature expressions actually appear in a review or not, or classified as frequent and infrequent features based on the level of their occurrence frequency (B. Liu, 2007). Motivated by a recent feature extraction study (e.g., Qiu et al., 2011), we propose a new classification scheme based on whether there are opinions expressed about the features in a review, which classified features into subjective and objective categories.

Definition 1 (subjective feature): If a reference to feature f is associated with opinion expressions in a review, f is considered a subjective feature. For example, “I like this bundle, the rechargeable battery is a life saver…” and “This camera is awesome...”

Definition 2 (objective feature): If a reference to feature f is not associated with any opinions in a review, f is considered an objective feature. For example, “This phone comes with a rechargeable battery...” and “This phone has three colors...”

State-of-the-art rule-based feature extraction studies (Gindl, Weichselbraun, & Scharl, 2013; Qiu et al., 2011) only addressed subjective features but ignored objective features. It is important to consider objective features for several reasons. First, incorporating objective features is expected to boost the recall of extraction methods. The distinctive characteristics of objective features point to the need for developing new extraction methods. Second, the extraction of subjective and objective features can mutually reinforce each other. This is because the differentiation of subjective and objective features depends on their specific review context. In other words, an objective feature extracted from one review context may be expressed as a subjective feature in another context (see rechargeable battery in Definitions 1 and 2). Third, objective features have the potential to support promotional review detection and assessment of trustworthiness of online information (Mayzlin, Dover, & Chevalier, 2012) in that objective features are presumably more objective and credible.

## Related Work

Based on our extensive literature review, extant methods for product feature extraction can be grouped into two broad categories: statistical-based and RbMs (see Table 1). Each of them can be further classified into supervised and unsupervised methods based on whether they require training data labeled with product features.

Statistical methods have been widely used in product feature extraction. Hu and Liu (2006) proposed class sequential rule mining to generate meaningful patterns for extracting features from online reviews; Wong and Lam (2005) used HMM for identifying (product feature-based) hot items from auction websites, and they treated product feature extraction as a graph labeling problem using CRF in a follow-up study (Wong & Lam, 2008). Unlike supervised methods, unsupervised methods do not require training data. Hu and Liu (2004) applied association rule mining (ARM) to feature extraction by assuming that people tend to use the same words when commenting on the same product features. Popescu and Etzioni (2007) adapted PMI to the problem of feature extraction by computing the PMI between a noun/noun phrase and class-specific discriminators. Chen et al. (2013) exploited how to incorporate domain knowledge into topic modeling to improve the performance of product feature extraction, and subsequently proposed automated knowledge LDA to learn prior knowledge and generate product features (Chen et al., 2014).

The other paradigm of feature extraction methods is rule based, which uses rules derived from uncovered patterns. DP is a state-of-the-art rule-based semisupervised method for extracting noun-phrase-based features (Qiu et al., 2011). DP is based on the dependency relation between product features and opinion words. Zhang et al. (2010) extended DP with part–whole pattern and no pattern. Gindl et al. (2013) leveraged syntactic patterns (e.g., dependency relations) that take sentence relations into consideration. Poria, Cambria, Ku, et al. (2014) manually encoded three sets of rules in RbM, including subjective-noun relations, nonsubjective-noun relation, and other rules, to address both implicit and explicit features.

Statistical methods generally require large corpora to mitigate the data scarcity problem in computing probabilities. Preparing the corpora is challenging particularly for supervised methods because creating a large-scaled annotated corpus can be very costly. Despite the availability of corpora in support of traditional information extraction research, those corpora were collected from editorials and news, which are distinctively different from online consumer reviews. In addition, the target of traditional information extraction was focused on named entities rather than product features. By contrast, RbMs do not rely on large corpora. Nevertheless, DP and other variants mainly dealt with subjective features and overlooked objective features. In addition, although DP was built on dependency structures, it only considered direct dependency while ignoring indirect dependency relations. RbM used handcrafted rules, which were inefficient to develop and difficult to generalize across domains. Furthermore, some named entities (e.g., brand and model names) that are unique to the product review domain have not been exploited by extant feature extraction methods.

## RubE METHODS

We propose RubE, unsupervised RubE methods for extracting both subjective features and objective features.

## Subjective Feature-Oriented Extraction Methods

RubE aims to extract subjective features by applying DP (Qiu et al., 2011) to deal with direct dependency, and, more importantly, by introducing two new types of linguistic structures: indirect dependency and comparative constructions.

Dependency refers to a binary asymmetrical connection between two words in a sentence. There are two types of dependency: direct and indirect (Qiu et al., 2011).

 Direct dependency indicates that one word directly depends on another, or both directly depend on an intermediate word. Based on the observation that opinion words are often used to modify features, opinion words and features can be directly linked to each other via certain dependency relations. For example, “The phone has a great color screen” (great mod color screen), and “iPod is the best mp3 player” (best amod player nsubj iPod, where ‘ ’ or ‘ ’ denotes dependency relation, “amod” and “nsubj” are specific types of dependency relations.)

 Indirect dependency indicates that one word indirectly depends on another through a third word or both depend on a third word through additional words (see Table 2). For example, “the camera is very easy to use” (camera xsubj use xcomp easy), where feature “camera” depends on “easy” via another word “use.”

We followed DP (Qiu et al., 2011) in handling direct dependency. DP extracted opinion words and product features iteratively based on propagation using the dependency relations between them. It required a set of seed opinion words to bootstrap the propagation. Eight rules were generated to perform the following four tasks: (1) extracting product features using opinion words; (2) extracting product features using the extracted product features; (3) extracting opinion words using the extracted product features; and (4) extracting opinion words using both the given and the extracted opinion words. We use the same strategy but exclude opinion words in the final step.

However, DP did not handle indirect dependency due to its complexity. Thus, the following introduction is focused on our method for addressing indirect dependency.

## Indirect Dependency

We fill the gap in the literature by incorporating indirect dependency in extracting subjective features. We propose the following three types of indirect dependency structures (see Table 2).

 Simple indirect dependency, where word A indirectly depends on word B via an intermediate word $I ,$ and word A or B is a feature candidate. This kind of structure usually describes performing certain actions on features.

 Explicitly pivoted indirect dependency, where both words A and B indirectly depend on word I via word $I _ { 1 }$ and word ${ \cal I } _ { 2 } ,$ respectively, and both A and B can be feature candidates. This type of indirect dependency is typically expressed as a

complex sentence.

 Implicitly pivoted indirect dependency, where both A and B indirectly depend on an intermediate word I via I1 and ${ \cal I } _ { 2 } ,$ respectively, and either A or B is a feature candidate.

Similar to DP, we extract product features iteratively via propagation using the indirect dependency relations as defined in Table 2. Specifically, node A or B from the dependency relations that satisfied the conditions of the rules (see Table 2) would be extracted as potential features. Consider the following sentence as an example. “I’m a happier person after discovering the i/p button” (person (NN) ← Dep (prepc-after) ← discovering (VBG) ← Dep (dobj) ← button (NN)). Given that the dependency structure of the sentence satisfied the conditions of two of the specified indirect dependency relations from Table 2 (i.e., POS of Word I is VB, and POSes of Word A and B are NNs), the word associated with “dobj” would be extracted as a candidate product feature.

## Comparative Constructions

Comparative constructions are used to present explicit orderings among different objects in terms of the degree or amount to which they possess some gradable property. Identifying comparative sentences is useful for feature extraction because consumers may express their opinions in a relative sense by comparing a target product against other alternatives. The syntactic structure of comparative sentences tends to be complex, in that they generally involve long-distance dependency and lack opinion words.

Before extracting comparative constructions using RubE, we first classify comparative constructions into four subtypes: comparative (e.g., longer), superlative (e.g., best), equality (e.g., the same as), and unique words (e.g., beat); and then we extract rules based on POS tags and comparative words from the sentence structures of each type (see Table 3).

The representation of the rules followed Sarawagi (2008). All of the rules are defined using indicative words and patterns of dependency relations and sentence structures.

To apply the rules, we first match a review against patterns on the left of each rule; if there is a match, we then extract the components tagged with “:f” as candidate product features. The extraction of comparative constructions also needs to deal with noncomparative sentences that contain comparative words such as “I cannot agree with you more,” “more than often.” To this end, we analyze the dependency relations between two nodes and check whether there existed certain dependency relations and POS tags (e.g., “prep\_than” and “JJR”) expected of a comparative structure. In addition, we compile a list of patterns to filter other noncomparative sentences.

## Objective Feature Extraction

Objective features are not uncommon in online consumer reviews for at least the following two reasons: (1) reviews filled with subjective features are more likely to mislead consumer’s decision and (2) descriptive reviews tend to state facts about a product or product features such as “no audio, no video,” and “There are three colors to choose from....” However, these features were not addressed by extant extraction methods. For instance, DP is not applicable due to the lack of use of opinion words in expressing objective features, and frequent-item based methods would be ineffective because objective features tend to have low occurrence frequency in online reviews.

We developed methods for extracting objective features based on two observations. First, objective features are typically expressed by a variety of lexicosyntactic structures such as part–whole relation. Second, objective features are often expressed in concrete terms such as specific quantities, weights, and measures.

#

## Part–whole Relation

A part–whole relation indicates that one or more objects are part of another object. Both supervised approaches (e.g., Girju, Badulescu, and Moldovan (2006)) and unsupervised approaches (e.g., Xia and Cao (2014)) have been developed to detect part–whole relations. Zhang et al. (2010) incorporated part–whole relations to address the low recall problem of DP. However, they assumed that the most frequent words in a corpus belong to class concepts and their part words product features. The assumption is problematic because the same word can be used as both a class and a feature word (e.g., “lens of the camera,” “cap of lens”). We extend and improve the syntactic patterns of part–whole relations (Girju et al., 2006) for the extraction of objective features. Compared with the unambiguous structure of part–whole relations (Girju et al., 2006), the extraction of its ambiguous counterpart is more challenging, which was the focus of RubE.

In addition to existing lexicosyntactic patterns of ambiguous part–whole relations such as “NP<sub>x</sub> PP<sub>y</sub>,” “NP<sub>x</sub>’s $N P _ { y } ,$ ” “NP<sub>x</sub> have $N P { _ y } , ^ { \prime }$ and ${ } ^ { * } N P _ { x }$ of $N P _ { y } ,$ ,” we introduce two new sentence-level patterns: ${ } ^ { * } N P _ { x }$ verb $N P _ { y }$ $( P P _ { z } )$ ” and “PRP/Ex Verb NP,” where NP, PP, PRP, and Ex denote noun phrase, prepositional phrase, personal pronoun, and existential there, respectively, and $N P _ { x }$ and $N P _ { y }$ contain the part or a candidate feature, separately. These patterns are introduced in detail below.

 Genitive phrase $( N P _ { x } \ P P _ { y }$ ${ \cal N P } _ { x } \mathrm { : }$ s $N P _ { y }$ $N P _ { x }$ of/have $N P y$ : Genitive phrases typically follow one of the patterns listed in the above parentheses, such as “battery ${ l i f e ^ { \prime \prime } }$ and “camera’s battery.” However, these patterns can be ambiguous. For example, the following two phrases share the same syntactic structure, “the engine of my car” and “the car of my friend,” but only the first phrase denotes a part–whole relation. To resolve the ambiguity, we developed a pruning strategy (see the pruning section).

 Verb phrase $( N P _ { x }$ Verb $N P _ { y }$ $I P P z I ,$ , where PPz is optional): Based on the sample relations (Girju et al., 2006), we extract cue verbs such as “have,” “include,” “contain,”

and “consist” to extract features from ambiguous part–whole patterns; for example, “the camera bundle contains a memory card.”

 Verb phrase with prefix (PRP Verb NP), where PRP (pronoun) is commonly used to refer a product. For example, “It has a tripod and a memory card.” In addition, some part–whole relations can also be expressed with verbal phrases such as “there be” and “comes with.”

Based on the above patterns, we generate a set of rules for extracting part–whole relations, and sample rules are listed in Table 4. For example, the following sentence “the camera comes with a rechargeable battery,” contains a syntactic pattern that matches the second rule in Table 4. Specifically, “the camera” matches NP, which is followed by “come,” and “a rechargeable battery” matches NP; thus, we extracted the “battery” as a potential product feature.

Online consumer reviews have unique genre characteristics, which point to some review-specific patterns such as specific named entities, negative and with-expressions, and cue phrases.

 Named entities. An expression of product brand and/or model names typically exhibits some structural patterns such as brand + numbers. We adapt named entity recognition techniques and regular expressions to the extraction of the domain-specific entities.

 Negative and with-expressions. Short negation (i.e., “no/not”) and with-expression patterns (i.e., “with/without”) may indicate features in an online consumer review such as “no audio” and “without auto mode.” We extend the negation expressions (Zhang et al., 2010) by introducing not-expressions and “with/without” patterns to capture additional features.

 Cue phrases. Some phrases such as “pros and cons” commonly signal following expressions of features.

## Pruning Methods

To improve the precision of feature extraction, we developed a two-stage pruning method, which includes (1) nonfeature candidate identification and (2) semantic similarity and document frequency-based filtering. In view of the informal writing style of online consumer reviews such as conjoined words (e.g., wifi and wi-fi) and misspellings, we first apply a text similarity function based on the editing distance (Rimrott & Heift, 2008) to group variant expressions of the same features.

 Stage 1: Identification of nonfeature candidates. The identification stage used two strategies: self-filtering and mutual exclusion. We propose a self-filtering strategy − if a word feature candidate is not part of any phrase candidate, the word feature is likely to be noise, and vice versa. In mutual exclusion (Qiu et al., 2011), if more than one feature candidate appeared in the same sentence without any conjunctions in-between, all such candidates except for one would be treated as noise. In addition, the survival feature candidate is the one with the highest similarity to product word and then highest frequency (when similarity scores are the same).

 Stage 2: Filtering nonfeature candidates. We design two complementary filtering methods. The intersection between the two sets of results would be treated as the final set of nonfeatures.

− Document frequency-based filtering. The design of the method is inspired by a common assumption in feature extraction research that terms with rare occurrences are unlikely to be features. Here, documents refer to consumer reviews. We choose the most conservative threshold for document frequency in this study − 2.

− Semantic similarity-based filtering. Terms that are not semantically related to the product under review are unlikely to be features of the product. Based on the assumption, we propose a new measure − differential similarity to assess the semantic relatedness between a candidate feature and a product. Drawing on Wordnet-based similarity metrics such as hso (Hirst & St-Onge, 1998) and lesk (Banerjee & Pedersen, 2003), the differential similarity of candidate feature $f ( f \in F )$ 11 DS(j), was derived as the difference in average similarity between F and a product word before and after removing f-inferior features from $F ,$ which included f itself and other candidates whose similarity scores were below that of f (see equation (1)). For example, given $F = \left\{ f _ { i } / \thinspace i = 1 . . . n \right\}$ of product P, where n is the total number of features of $P ,$ we first measured the semantic similarities between $f _ { i }$ and P: $\{ s i m ( f i , P ) / \ i =$ $\left. 1 . . n \right\}$ , and then sorted all $f _ { i } \in F$ in an ascending order of $s i m ( f i , P )$ into $F ^ { \prime } = \{ f _ { j } / j _ { 1 } < j _ { 2 }$ when ?????? $( f _ { j _ { 1 } } , P ) \leq s i m ( f _ { j _ { 2 } } , P ) , j _ { 1 } , j _ { 2 } = 1 . . . n \}$ . DS(fj), the differential similarity of $f _ { j }$ was normalized by the average similarities of all $f _ { j } \in F .$ Those features with DS(fj) below 0.5 were filtered. The threshold was determined empirically.

$$
D S \big (f _ {j} \big) = (\frac {1}{n - j} \sum_ {k = j + 1} ^ {n} s i m (f _ {k}, P) - \frac {1}{n} \sum_ {k = 1} ^ {n} s i m (f _ {k}, P)) / \frac {1}{n} \sum_ {k = 1} ^ {n} S i m (f _ {k}, P)\tag{1}
$$

Assume that $\begin{array} { r } { F = \{ \stackrel { \epsilon \epsilon } { \mathrm {  ~ \epsilon ~ } } \} \mathrm { e n s } , } \end{array}$ ” “battery,” “coffee,” “car”}, P = “camera,” sim(“camera,” “lens”) $= 0 . 8 .$ , sim(“camera,” “battery”) = 0.7, sim(“camera,” “coffee”) = 0.3, and sim(“camera,” $^ { * } \mathrm { c a r } ^ { * 3 } ) = 0 . 2$ . Then, Fʹ = {“car,” “coffee,” “battery,” “lens”}. $D S ( ^ { \ll } \mathrm { c a r } ^ { , > } ) = ( ( 0 . 8 + 0 . 7 +$ $0 . 3 ) / 3 - ( 0 . 8 + 0 . 7 + 0 . 3 + 0 . 2 ) / 4 ] / ( ( 0 . 8 + 0 . 7 + 0 . 3 + 0 . 2 ) / 4 ) = 0 . 2 < 0 . 5 , D S ( ^ { \ast } \mathrm { c o f f e e ^ { \ast } } ) = 0 . 3 0 9 ( ^ { \circ } \mathrm { c o n d f e e ^ { \ast } } ) = 1 . 0 2 6$ $0 . 5 , D S ( ^ { \mathrm { c } \mathrm { c } } \mathrm { b a t t e r y ^ { \mathrm { 3 } } } ) = 0 . 6 ,$ , and $D S ( ^ { \ast } \mathrm { { l e n s } ^ { \prime \ast } ) = 1 }$ . Thus, car and coffee were filtered from F.

## EXPERIMENTS

## DATASETS

We test RubE using two datasets. One dataset consists of reviews of five electronic products (Hu & Liu, 2004), and the other contains movie reviews (Zhenxue, 2013). The distinctive types of products represented by the two datasets allowed us to test the generality of RubE. Some descriptive statistics of the datasets is reported in Table 5.

## EVALUATION METRICS AND BASELINES

We select precision, recall, and F-measure as the evaluation metrics. Precision is defined as the ratio of the number of correctly identified features to the total number of identified features. Recall is defined as the ratio of the number of correctly identified features to the total number of actual features in the gold standard. F-measure is defined as a harmonic mean of the precision and recall.

We select four methods as the baselines, including ARM (Hu & Liu, 2004), DP (Qiu et al., 2011), an RbM (Poria, Cambria, Ku, et al., 2014), and CRF (Jakob & Gurevych, 2010; Yang & Cardie, 2013). They represent either the most popular or the state-of-the-art methods for product feature extraction.

## PROCEDURE

The procedure for feature extraction consists of three key processes: preprocessing, feature extraction, and pruning, as shown in Fig. 1.

As both feature extraction and pruning have been described in detail in the previous section, so we focus on the preprocessing step here. The preprocessing used the following analyses: tokenization, POS tagging, named entity recognition, and dependency grammar analysis, using tools including Natural Language Toolkit (NLTK; Loper & Bird, 2002) and Stanford Natural Language Processing (NLP; De Marneffe, MacCartney, & Manning, 2006). Among them, the named entity recognition is focused on some review-specific entities such as brand names.

## RESULTS

The average performances of RubE and the baseline methods over all the products are reported in Table 6. It is shown from the table that RubE outperforms all the baselines in terms of recall, precision, and F-measure. Specifically, the average recall improvement of

#

RubE is about 9% over the ARM, RbM, and CRF, and about 5% over the DP. The average precision improvement is about 17% over ARM, about 2% over DP, 11% over RbM, and about 10% over CRF. The average improvement of RubE in the F-measure is 13% over ARM, 3% over DP, 9% over RbM, and about 9% over CRF. Paired-sample t-tests showed that the recall of RubE is greater than that of DP $( p < 0 . 0 5 )$ , ARM $( p < 0 . 0 1 )$ , RbM $( p <$ 0.05), and CRF $( p < 0 . 0 1 )$ ), respectively; the precision of RubE is higher than that of DP $( p$ $< 0 . 1 )$ ), ARM $( p < 0 . 0 1 )$ , RbM $( p < 0 . 0 1 )$ , and CRF $( p < 0 . 0 1 )$ ), and the F-measure of RubE is higher than that of DP $( p < 0 . 1 )$ , ARM $( p < 0 . 0 1 )$ , RbM $( p < 0 . 0 1 )$ ), and CRF $( p < 0 . 0 1 )$ , respectively.

To assess the impact of our pruning strategies, we report the performance of RubE before and after pruning on each of the products in Fig. 2. The figure shows that our proposed pruning methods significantly improved precision with only a slight drop on recall.

To gain an understanding of the generality of RubE and other methods, we reported their performance for electronic products and movies separately in Fig. 3. The side-by-side comparisons showed that RubE outperformed all the baseline methods on both electronic products and movie reviews, and the improvements of RubE over the baselines are even more pronounced on the movie data. The results demonstrated the generalizability of RubE across different types of products.

To gain insights into efficacy of individual components of RubE in recall, we report their marginal improvements over DP for electronic products and for movies in Table 7 separately. The results show that every component of RubE contributed to its overall performance with indirect dependency leading to the largest improvements.

## DISCUSSION

## FINDINGS AND ALTERNATIVE EXPLANATIONS

Our experimental results demonstrate the superior performance of RubE to the state-of-the-art methods for extracting features from online consumer reviews. Specifically, the proposed feature extraction methods improve the recall, and the pruning methods improve the precision of feature extraction. Moreover, the performance improvements are consistently demonstrated across the online reviews of two distinctive product types.

Given the importance of our proposed classification scheme of product features in guiding our development of RubE, we provide detailed information about the two types of features. It should be noted, however, that the distinction of subjective features from objective features is inconsequential for the extracted features due to the context dependency of their definitions. For example, the same feature (e.g., lens) may be extracted as a subjective feature from one context of camera review and as an objective feature from another context. In other words, the same product features may be extracted by more than one rule due to the overlaps among the features extracted by different components of RubE. As a result, we do not report descriptive statistics of either type of the features in the datasets. Nevertheless, to give a rough idea of the occurrences of objective features, which were overlooked in previous methods, we computed the percentage distribution of features extracted by individual components of RubE (i.e., recall) by replicating their overlaps in the set of extracted features. For example, if a feature is extracted by both indirect dependency and part–whole components, typically from different reviews, the feature would be counted twice toward the total number. The recall percentage distribution of RubE components is reported in Fig. 4.

It is shown from Fig. 4 that objective features, including those extracted by part–whole and review-specific patterns accounted for about 15% of the total recall. This number was not negligible, which provided preliminary evidence for incorporating objective features.

Compared with part–whole relations, review-specific patterns resulted in higher recall. It underscores the value of incorporating unique linguistic characteristics of online review genre for feature extraction. In addition, among the subjective patterns, indirect dependency (31%) was ranked the second highest in recall, which was next to direct dependency using DP (45%). The results highlight the significance of indirect dependency in extracting product features from online reviews.

## THEORETICAL IMPLICATIONS

This study makes multifold contributions to the literature. First, RubE improves the state of performance in product feature extraction by extracting both objective and subjective features from online reviews. Our proposed classification scheme of product features can be used to guide further improvement of feature extraction methods. Second, this is the first research that exploited indirect dependency in extracting features from online consumer reviews. The three types of indirect dependency structures explored in this study helped to detect long-distance dependency and complex relationships between words. In addition, this study introduces additional new patterns for extracting subjective features such as comparative constructions. Third, it proposes pruning strategies that consider both semantics and context information, which are not only complementary but also domain-independent. In addition, RubE is developed on the basis of the lexicosyntactic structure rather than pure heuristics, which overcomes the overfitting and low generality problem of RbMs. Finally, in view of significant challenges of extracting features from the movie domain (Zhou & Chaovalit, 2008), RubE addresses the challenges by demonstrating superior performance (i.e., 81% in F-measure) to alternative methods.

RubE has significant theoretical implications for text mining and NLP research. First, despite the ongoing trend of applying statistical-based methods in text processing, this

#

study demonstrates that RbMs remain effective in analyzing text in a confined domain such as online consumer reviews. In addition, RbMs can be a promising alternative for those domains that lack annotated datasets. Second, the prevalent use of indirect dependency in online consumer reviews calls for adding corresponding functions to existing dependency analysis tools. Third, the findings of this study suggest that the design of complementary and domain-independent pruning strategies is one way to improve the generality of feature extraction methods.

This research also has implications for the analysis of social media content. RubE can be used to detect sentence subjectivity. In addition, the feature extraction methods proposed here pave the way for feature-based sentiment analysis of online reviews. Further, the feature extraction methods enable fine-grained summarization of online consumer reviews.

## PRACTICAL IMPLICATIONS

The findings of this study have practical implications for consumers, online retailers, and manufacturers. First, RubE improves the usefulness of online reviews for customers in their purchase decision making by enabling feature-based retrieval and summarization. Second, RubE can be used to improve online recommender systems with feature-based personalization, which in turn improves customers’ adoption and stickiness to retailer’s websites. Third, manufacturers may leverage consumer feedback on specific product features to improve product quality. Fourth, RubE can be extended to support topic detection by extracting opinion targets using subjective feature-oriented methods and by extracting the subjects of sentences using the objective feature-oriented methods as candidate topics), and to support ontology learning in discovering concepts and their relationships.

## CONCLUSION

#

This research lends strong support to the use of RbMs for analyzing online consumer reviews. Our study demonstrates that the performance of feature extraction can be improved by recognizing different types of features and through design of extraction methods for each type of features separately. The generality of RbMs for feature extraction may be approached by developing domain-independent rules and pruning strategies.

This study exposes several limitations that suggest future research. First, the part–whole patterns may be refined to improve its relatively low recall in extracting objective features. Second, although our indirect dependency relations demonstrate a strong capability of handling long distance relations, some issues such as reference resolution and long distance negation detection need to be addressed in the future. Third, the generality of RubE can be evaluated more fully by using datasets of online reviews from other domains such as hotels and physicians. Finally, the efficacy of RbMs demonstrated in this study may be combined with the strengths of statistical methods to further improve the performance of feature extraction in future.

## Acknowledgment

This research was partly supported by the National Science Foundation. The authors also thank Zhenxue Zhang for sharing of the annotated datasets.

## References

Archak, Nikolay, Ghose, Anindya, & Ipeirotis, Panagiotis G. (2011). Deriving the pricing power of product features by mining consumer reviews. Management Science, 57(8), 1485-1509.

Banerjee, Satanjeev, & Pedersen, Ted. (2003). Extended gloss overlaps as a measure of semantic relatedness. Paper presented at the Ijcai.

Chen, Zhiyuan, Mukherjee, Arjun, & Liu, Bing. (2014). Aspect Extraction with

Automated Prior Knowledge Learning. Paper presented at the ACL.

Chen, Zhiyuan, Mukherjee, Arjun, Liu, Bing, Hsu, Meichun, Castellanos, Malu, & Ghosh, Riddhiman. (2013). Exploiting Domain Knowledge in Aspect Extraction. Paper presented at the Emnlp

De Marneffe, Marie-Catherine, MacCartney, Bill, & Manning, Christopher D. (2006). Generating typed dependency parses from phrase structure parses. Paper presented at the Proceedings of LREC.

Dellarocas, Chrysanthos. (2003). The Digitization of Word of Mouth: Promise and Challenges of Online Feedback Mechanisms. Management Science, 49(10), 1407-1424.

Dimoka, Angelika, Hong, Yili, & Pavlou, Paul A. (2012). On product uncertainty in online markets: theory and evidence. MIS Quarterly, 36(2), 395-426.

Du, Rex Yuxing, Hu, Ye, & Damangir, Sina. (2015). Leveraging Trends in Online Searches for Product Features in Market Response Modeling. Journal of Marketing, 79(1), 29-43.

Gindl, Stefan, Weichselbraun, Albert, & Scharl, Arno. (2013). Rule-based opinion target and aspect extraction to acquire affective knowledge. Paper presented at the Proceedings of the 22nd international conference on World Wide Web companion.

Girju, Roxana, Badulescu, Adriana, & Moldovan, Dan. (2006). Automatic discovery of part-whole relations. Computational Linguistics, 32(1), 83-135.

Hirst, Graeme, & St-Onge, David. (1998). Lexical chains as representations of context for the detection and correction of malapropisms. WordNet: An electronic lexical database, 305, 305-332.

Hu, Minqing, & Liu, Bing. (2004). Mining opinion features in customer reviews. Paper presented at the Aaai.

Hu, Minqing, & Liu, Bing. (2006). Opinion Feature Extraction Using Class Sequential

Rules. Paper presented at the AAAI Spring Symposium: Computational Approaches to Analyzing Weblogs.

Jakob, Niklas, & Gurevych, Iryna. (2010). Extracting opinion targets in a single-and cross-domain setting with conditional random fields. Paper presented at the Proceedings of the 2010 Conference on Empirical Methods in Natural Language Processing.

Jensen, M. L., Averbeck, J. M., Zhang, Z., & Wright, K. B. (2013). Credibility of Anonymous Online Product Reviews: A Language Expectancy Perspective. Journal of Management Information Systems, 30(1), 293-323. doi: Doi 10.2753/Mis0742-1222300109

Jin, Wei, & Ho, Hung Hay. (2009). A novel lexicalized HMM-based learning framework for web opinion mining. Paper presented at the Proceedings of the 26th Annual International Conference on Machine Learning.

Kim, Soo-Min, Pantel, Patrick, Chklovski, Tim, & Pennacchiotti, Marco. (2006). Automatically assessing review helpfulness. Paper presented at the Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing.

Kobayashi, Nozomi, Inui, Kentaro, & Matsumoto, Yuji. (2007). Extracting Aspect-Evaluation and Aspect-of Relations in Opinion Mining. Paper presented at the Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning.

Li, Shi, Zhou, Lina, & Li, Yijun. (2015). Improving aspect extraction by augmenting a frequency-based method with web-based similarity measures. Information Processing & Management, 51(1), 58-67.

Li, X. X., Hitt, L. M., & Zhang, Z. J. (2011). Product Reviews and Competition in Markets for Repeat Purchase Products. Journal of Management Information Systems, 27(4), 9-41. doi: Doi 10.2753/Mis0742-1222270401

Liu, Bing. (2007). Web data mining: Springer.

Liu, Jingjing, Cao, Yunbo, Lin, Chin-Yew, Huang, Yalou, & Zhou, Ming. (2007). Low-Quality Product Review Detection in Opinion Summarization. Paper presented at the EMNLP, Prague.

Liu, Kang, Xu, Liheng, & Zhao, Jun. (2014). Extracting Opinion Targets and Opinion Words from Online Reviews with Graph Coranking. Paper presented at the ACL.

Loper, Edward, & Bird, Steven. (2002). NLTK: The natural language toolkit. Paper presented at the Proceedings of the ACL-02 Workshop on Effective tools and methodologies for teaching natural language processing and computational linguistics-Volume 1.

Mayzlin, Dina, Dover, Yaniv, & Chevalier, Judith A. (2012). Promotional reviews: An empirical investigation of online review manipulation: National Bureau of Economic Research.

Mukherjee, Arjun, & Liu, Bing. (2012). Aspect extraction through semisupervised modeling. Paper presented at the Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics: Long Papers-Volume 1.

Popescu, Ana-Maria, & Etzioni, Orena. (2007). Extracting product features and opinions from reviews Natural language processing and text mining (pp. 9-28): Springer.

Poria, Soujanya, Cambria, Erik, Ku, Lun-Wei, Gui, Chen, & Gelbukh, Alexander. (2014). A rule-based approach to aspect extraction from product reviews. SocialNLP 2014, 28.

Poria, Soujanya, Cambria, Erik, Winterstein, Gregoire, & Huang, Guang-Bin. (2014). Sentic patterns: Dependency-based rules for concept-level sentiment analysis. Knowledge-Based Systems, 69, 45-63.

Probst, Katharina, Ghani, Rayid, Krema, Marko, Fano, Andrew E., & Liu, Yan. (2007).

Semi-Supervised Learning of Attribute-Value Pairs from Product Descriptions. Paper presented at the Ijcai.

Qiu, Guang, Liu, Bing, Bu, Jiajun, & Chen, Chun. (2011). Opinion word expansion and target extraction through double propagation. Computational linguistics, 37(1), 9-27.

Rimrott, Anne, & Heift, Trude. (2008). Evaluating automatic detection of misspellings in German. Language Learning & Technology, 12(3), 73-92.

Sarawagi, Sunita. (2008). Information extraction. Foundations and trends in databases, 1(3), 261-377.

Scaffidi, Christopher, Bierhoff, Kevin, Chang, Eric, Felker, Mikhael, Ng, Herman, & Jin, Chun. (2007). Red Opal: product-feature scoring from reviews. Paper presented at the Proceedings of the 8th ACM conference on Electronic commerce.

Wong, Tak-Lam, & Lam, Wai. (2005). Hot item mining and summarization from multiple auction Web sites. Paper presented at the Data Mining, Fifth IEEE International Conference on.

Wong, Tak-Lam, & Lam, Wai. (2008). Learning to extract and summarize hot item features from multiple auction web sites. Knowledge and Information Systems, 14(2), 143-160.

Wu, Jianan, Wu, Yinglu, Sun, Jie, & Yang, Zhilin. (2013). User reviews and uncertainty assessment: A two stage model of consumers' willingness-to-pay in online markets. Decision Support Systems, 55, 175-185. doi: 10.1016/j.dss.2013.01.017

Xia, F., & Cao, C. (2014). Extracting Part-Whole Relations from Online Encyclopedia. Xiong, Wenting. (2013). Helpfulness-Guided Review Summarization. Paper presented at the Hlt-naacl.

Xu, Liheng, Liu, Kang, Lai, Siwei, Chen, Yubo, & Zhao, Jun. (2013). Mining Opinion Words and Opinion Targets in a Two-Stage Framework. Paper presented at the Proceedings of the 51st Annual Meeting of the Association for Computational

Linguistics.

Yang, Bishan, & Cardie, Claire. (2013). Joint Inference for Fine-grained Opinion Extraction. Paper presented at the Acl (1).

Zhang, Lei, Liu, Bing, Lim, Suk Hwan, & O'Brien-Strain, Eamonn. (2010). Extracting and ranking product features in opinion documents. Paper presented at the Proceedings of the 23rd international conference on computational linguistics: Posters.

Zhenxue, Zhang. (2013). Urcf: an approach to integrating user reviews into memory-based collaborative filtering. (Doctoral), University of Maryland at Baltimore County.

Zhou, Lina, & Chaovalit, Pimwadee. (2008). Ontology‐supported polarity mining. Journal of the American Society for Information Science and technology, 59(1), 98-110.

Zhou, Lina, Zhang, Ping, & Zimmermann, Hans-Dieter. (2013). Social commerce research: An integrated view. Electronic commerce research and applications, 12(2), 61-68.

#

## Biographies

Yin Kang is a PhD student in the Department of Information Systems at the University of Maryland, Baltimore County, USA. His research interests focus on natural language processing, web data mining, and machine learning.

Lina Zhou is an associate professor of information systems at the University of Maryland, Baltimore County, USA. Her research aims to improve human decision making and knowledge management through the design of intelligent technologies and understanding of human behavior. Her current research interests include deception detection, natural language processing, mobile web adaptation, ontology learning, and online social networks. Dr. Zhou has authored and/or coauthored over 50 referred articles in journals such as Journal of Management Information Systems, MIS Quarterly, Communications of the ACM, Information & Management, IEEE Transactions on Knowledge and Data Engineering, and Decision Support Systems.

##

![](/api/attachments/Y6ZR92ME/fulltext/images/82b566739f416a7ae17774832ef35753c85abbf14ca59ed64104816517c2648c.jpg)  
Figure 1. Procedure for Feature Extraction

![](/api/attachments/Y6ZR92ME/fulltext/images/ce26381d72f9cc1379e2303dc3e396250e5d227534d5dcdbc7f37d25ab352271.jpg)  
Figure 2. Performance (recall, precision, and f-measure) of RubE before and after pruning on all products

Figure 3. Performance of all methods on electronic products and movies  
![](/api/attachments/Y6ZR92ME/fulltext/images/d5d4553502e477d982287322ac42b36adeca1aa6df4e2cb55162d26073dd0611.jpg)

![](/api/attachments/Y6ZR92ME/fulltext/images/100572afc3c53cdd4310160bb0255b467ed163baf7ff30ed0419183d964e433a.jpg)  
Figure 4. Percentage distribution in recall for individual components of RubE

TABLE 1. A summary of previous studies on product feature extraction

<table><tr><td>Method</td><td>Study</td><td>Techniques</td><td>Performance</td><td>Product type/Source</td></tr><tr><td rowspan="5">Statistical-basedUnsupervised</td><td>Hu and Liu (2004)</td><td>Association rule miningCompactness pruning and redundancy pruning</td><td>Recall: 80%Precision: 72%</td><td>Electronic products from Amazon</td></tr><tr><td>Popescu and Etzioni (2007)</td><td>Frequency-based extraction and PMI</td><td>Precision: 94%Recall: 77%</td><td>Electronic products from Amazon</td></tr><tr><td>Scaffidi et al. (2007)</td><td>A language model approach based on statistical distribution difference between different corpora</td><td>Precision: 85–90%</td><td>7 products (e.g., electronics, books, and games) from Amazon</td></tr><tr><td>Chen et al. (2013)</td><td>MC-LDA (LDA with m-set and c-set) based on an extended generalized E-GPU model</td><td>N/A</td><td>4 products (e.g., camera, food, computer, and care) from Amazon</td></tr><tr><td>Chen, Mukherjee, and Liu (2014)</td><td>Use prior knowledge to extract aspects, propose AKL to learn knowledge and deal with error knowledge</td><td>N/A</td><td>Electronic products from Amazon</td></tr><tr><td rowspan="6">Statistical-basedSupervised/Semisupervised</td><td>Wong and Lam (2005)</td><td>HMM-based learning method</td><td>Precision: 78.5%Recall: 72%</td><td>Electronic products from 3 bidding websites</td></tr><tr><td>Hu and Liu (2006)</td><td>Class Sequential Rules MiningPattern matching</td><td>Precision: 83.8%Recall: 84.9%</td><td>Electronic products from Amazon</td></tr><tr><td>Probst et al. (2007)</td><td>Naive Bayes combined with a multiview semisupervised algorithm (co-EM)</td><td>Precision: 38%Recall: 75%</td><td>2 sport products from DICK's sporting goods</td></tr><tr><td>Kobayashi, Inui, and Matsumoto (2007)</td><td>Combine contextual and statistical cluesTemplate slot filling</td><td>Precision: 72%Recall: 62%</td><td>Restaurants from Japanese weblog posts</td></tr><tr><td>Wong and Lam (2008)</td><td>CRF-based learning method</td><td>Precision: 78.5%Recall: 74.5%</td><td>Electronic products from auction websites</td></tr><tr><td>Jin and Ho (2009)</td><td>Lexicalized HMM</td><td>Precision:73–88%Recall:65–97%</td><td>16 cameras fromAmazon</td></tr><tr><td></td><td>Mukherjee and Liu (2012)</td><td>Two novel statistical models:SAS and ME-SAS</td><td>N/A</td><td>Hotel from TripAdvisor</td></tr><tr><td rowspan="3">Rule-basedUnsupervised</td><td>Zhang, Liu, Lim, and O’Brien-Strain (2010)</td><td>Part-whole and “no” patternsPruning-based HIT</td><td>Precision:60–70%Recall:40–70%</td><td>4 products (e.g., car, mattress, phone, and LCD) from Amazon</td></tr><tr><td>Gindl et al. (2013)</td><td>Syntactic Patterns(Dependency relations)Anaphora resolution</td><td>N/A</td><td>Electronic products from Amazon</td></tr><tr><td>(Poria, Cambria, Ku, et al., 2014; Poria, Cambria, Winterstein, et al., 2014)</td><td>Manually encoded rules for sentences with subjective noun relation or not, and other specific conditions</td><td>Precision:82.15–93.25%Recall:86.15–93.32%</td><td>Electronic products from Amazon</td></tr><tr><td>Rule-basedSupervised/semisupervised</td><td>Qiu et al. (2011)</td><td>Double propagation</td><td>Precision:88%Recall: 83%</td><td>Electronic products from Amazon</td></tr></table>

Note: N/A indicates the study adopted evaluation metrics that are distinctively different from precision and recall.

Note: A, B, and I are words in a sentence, A, B ∈ {features}; I denotes intermediate word Dep (dependency relations)

TABLE 2. Rules for extracting indirect dependency

<table><tr><td>Types</td><td>Structures</td><td>Rules</td><td>Examples</td></tr><tr><td>Simple</td><td><img src="/api/attachments/Y6ZR92ME/fulltext/images/8fbe7712fcc51391f58b67c9e088ebf80b8c15e171daefe8d568baf95b3b4ae5.jpg"/></td><td>A → Dep1 → I → Dep2 → BA∈{NN}, I∈{VB}B∈{features}Dep1 ∈{dobj, nsubj, xsubj}Dep2 ∈{prepc, xcomp}</td><td>“I’m a happier person after discovering the i/p button” (person (NN) ← Dep (prepc-after) ← discovering (VBG) ← Dep (dobj) ← button (NN))</td></tr><tr><td>Explicitly pivoted</td><td><img src="/api/attachments/Y6ZR92ME/fulltext/images/06a3bdef16dc11f4c1a3ad48582dc817fee2a7cebaa89d817b2f760bdd12b3fe.jpg"/></td><td>A → Dep1 → I1 → Dep2 → I ← Dep3 ← I2 ← Dep4 ← BA or B ∈ {features}Dep1,2,3,4 ∈ {nn, prep}I ∈ {VB}</td><td>“You can move the focus range to almost anywhere in the scene with the push of a button”(Focus (N) → Dep (nn) → range (N) → Dep (dobj) → move (verb) ← Dep(prep-in) ← scene(N) ← Dep (prep-with) ← push (verb))</td></tr><tr><td>Implicitly pivoted</td><td><img src="/api/attachments/Y6ZR92ME/fulltext/images/9605442e6078919d5c1ba29f1fa4633f1760ebe61b1edfad463c74e7418644da.jpg"/></td><td>A → Dep1 → I1 --- I2 ← Dep2 ← BA ∈ {NN}, I1,2∈{VB}I: missing, B ∈ {features}Dep1,2∈{nsubj, dobj}</td><td>“Another nice thing is that the unit has both optical and coax digital audio outputs”(Thing (NN) → Dep (nsubj) → is (verb) --- Dep (ccomp) --- has (verb) ← Dep (dobj) ← audio output (NN))</td></tr></table>

{'ccomp','amod','xcomp','partmod','csubj','csubjpass','nsubj',

'nsubjpass','dobj','iobj','acomp'},

JJ(adjective) ∈ {JJ, JJR, JJS}, $\begin{array} { r } { V B ( \nu e r b ) \in \mathit { \Omega } / V B , } \end{array}$ , VBZ, VBP} and RB(adverb) ∈ {RB, RBR, RBS}.

TABLE 3. Sample Rules of Comparative Construction

<table><tr><td>Category</td><td>Pattern(s)</td><td>Sample Rules</td><td>Examples</td></tr><tr><td rowspan="2">Comparative</td><td> $G(F, P_1) + CW + G(F, P_2)$ </td><td>({Dependency = Dep2}? {Node = NP/POS=NN}:f{String = "of"? {Node = NP/POS = NN}) ({String = CW}{Dependency = Dep1})({Dependency = Dep2}? {Node = NP/POS = NN/POS = DT}:f{String = "of"}{Node = NP/POS = NN/POS = DT}) →Feature = f</td><td>"The battery life of Camera X is longer than that of Camera Y""The battery life" (NP) → nmod of ∈ Dep2 → "Camera X"(NP)“longer than” (CW) → advmod ∈ Dep1 → “that” (DT) → nmod of ∈ Dep2→"Camera X" (NP)therefore, “battery life”:f → feature</td></tr><tr><td> $P_1 + CW + F + P_2$ </td><td>{Node = NP/POS = NN}{String = CW} {Dependency = Dep1}) {Node = NP/POS = NN}:f{Node = NP/POS = NN} →Feature = f</td><td>In “Camera X has a longer battery life than Camera Y”“Camera X” (NP) → “longer” (CW) → amod ∈ “Dep1” → “battery life” (NP) →“Camera Y” (NP)therefore, “battery life”:f → feature</td></tr><tr><td rowspan="2">Equality</td><td> $G(F, P_1) + G(F, P_2) + EW$ </td><td>({Dependency = Dep2}? {Node = NP/POS = NN}:f {String = "of"} {Node = NP/POS = NN})({Dependency = Dep2}? {Node = NP/POS = NN}:f {String = "of"} {Node = NP/POS = NN})({String = EW} {Dependency = Dep1}) →Feature = f</td><td>In “The price of camera X and camera Y are the same.”“The price” (NP) → nmod of ∈ Dep2 → “Camera X” (NP)/“Camera X” (NP)“The price” (NP) → nmod of ∈ Dep1 → “same” (EW)therefore, “price”:f → feature</td></tr><tr><td> $P_1 + P_2 + EW + F$ </td><td>{Node = NP/POS = NN}{Node = NP/POS = NN}{String = EW} {Dependency = Dep1}) {Node = NP/POS = NN}:f →Feature = f</td><td>In “Camera X and Camera Y are about the same size.”“Camera X” (NP)/“Camera Y” (NP) → nsubj of ∈ Dep1 → “size”“same” (EW) → amod of ∈ Dep1 → “size”therefore, “size”:f → feature</td></tr><tr><td>Superlative</td><td> $G(F, P) +$ SW</td><td>({Dependency = Dep2}?{Node = NP/POS = NN}{String = ""}{Node = NP/POS = NN}:f)( {String = SW} → Feature = f)</td><td>In “Camera X’s lens is thebest."“Camera X” (NP) → “best”(CW) → nsubj ∈ Dep1 → “lens”(NN)therefore, “lens”:f → feature</td></tr><tr><td></td><td>F + SW</td><td>{Node = NP/POS = NN}:f({String = SW} {Dependency = Dep1}) → Feature = f</td><td>In “The picture quality is the best.”“best” (CW) → nsubj ∈ Dep1 → “picture quality” (NP)therefore, “picture quality”:f → feature</td></tr><tr><td>Unique words</td><td>P1 + P2 + UW+ FOr P1 + F + UW + P2</td><td>{Node = NP/POS = NN}{Node = NP/POS = NN}{String = UW} {Dependency = Dep1}) ({Node = NP/POS = NN}:f) → Feature = f</td><td>In “Camera X and Camera Y have different OS.”“Camera X” (NP) → “Camera Y” (NP) →“different” (UW) → amod ∈ Dep1 →“OS” (NN):therefore, “OS”:f → feature</td></tr></table>

Note: G: a genitive relation between two words; F: features, “P: product words; CW: comparative words; EW: equality words; SW: superlative words; UW: unique words; “Node”: syntactic structure; $^ { \prime \prime } N P ^ { \prime \prime } ;$ noun phrases; $" N N " .$ noun; “f”: product feature; Dep1 {‘nsubj’, ‘prep\_than’, ’nmod’, ‘amod’, ‘advmod’}; $\begin{array} { r } { D e p _ { 2 } \supset \{ ^ { \prime } p r e p _ { - } o f _ { \prime } ^ { \prime } } \end{array}$ ‘nmod\_of’, ‘advmod’, ‘amod’}.

TABLE 4. Sample Rules of Part–Whole Relation

<table><tr><td>Category</td><td>Sample Rules</td><td>Usage Examples</td></tr><tr><td>Genitive phrase</td><td>{Node = NP/POS = NN}{String = &quot;s&quot;)?{Node = NP/POS = NN}:y → Feature = y</td><td>&quot;This phone&#x27;s battery life&quot;&quot;This phone&quot; (NP), &quot;battery life&quot; (NP),&quot;s&quot; match {String = &quot;s&quot;?therefore, &quot;battery life&quot;:f → feature</td></tr><tr><td>Verb phrase</td><td>{Node = NP/POS = NN}{POS = VB}{Node = NP/POS = NN}{Node = NP/POS = NN}?:y → Feature = y</td><td>In &quot;This camera comes with a rechargeable battery&quot;&quot;This phone&quot; (NP), &quot;a rechargeable battery&quot; (NP),&quot;come&quot; (VB)therefore, &quot;battery&quot;:f → feature</td></tr><tr><td>Verb phrase with prefix</td><td>{POS = PRP/POS = Ex}{POS = VB}{Node = NP/POS = NN}:y → Feature = y</td><td>In &quot;There is a rechargeable battery&quot;&quot;There is&quot; (Ex), &quot;a rechargeable battery&quot; (NP),therefore, &quot;battery&quot;:f → feature</td></tr></table>

Note: “Node”: syntactic structure; “NP”: noun phrases; “NN”: noun; “VB”: verb; “PRP”: personal pronoun; “EX”: existential there.

Review-Specific Patterns

TABLE 5. Descriptive Statistics of the Datasets

<table><tr><td>Product Name</td><td>No. Reviews</td><td>No. Features</td></tr><tr><td>Camera (Canon)</td><td>45</td><td>79</td></tr><tr><td>Camera (Nikon)</td><td>34</td><td>96</td></tr><tr><td>Cell Phone (Nokia)</td><td>41</td><td>67</td></tr><tr><td>MP3 Player(Creative)</td><td>95</td><td>57</td></tr><tr><td>DVD Player (Apex)</td><td>99</td><td>49</td></tr><tr><td>Movie</td><td>356</td><td>30</td></tr></table>

TABLE 6. Average Recall, Precision, and F-measure of RubE and the baseline methods

<table><tr><td>Metric s</td><td>A RM</td><td>D P</td><td>R bM</td><td>C RF</td><td>R ubE</td></tr><tr><td>Recall</td><td>0.78</td><td>0.82</td><td>0.78</td><td>0.78</td><td>0.87</td></tr><tr><td>Precision</td><td>0.71</td><td>0.86</td><td>0.77</td><td>0.78</td><td>0.88</td></tr><tr><td>F-measure</td><td>0.74</td><td>0.84</td><td>0.78</td><td>0.78</td><td>0.87</td></tr></table>

TABLE 7. Marginal improvement (recall) of each component of RubE

<table><tr><td></td><td>Electronics</td><td>Movie</td></tr><tr><td>DP</td><td>0.81</td><td>0.73</td></tr><tr><td>DP + indirect dependency</td><td>+0.03</td><td>+0.04</td></tr><tr><td>DP + indirect dependency + comparatives</td><td>+0.01</td><td>+0.01</td></tr><tr><td>DP + indirect dependency + comparatives + part-whole</td><td>+0.01</td><td>+0.01</td></tr><tr><td>DP + indirect dependency + comparatives + part-whole + specific patterns</td><td>+0.02</td><td>+0.02</td></tr></table>
