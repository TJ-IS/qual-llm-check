---
otero_id: 610
otero_key: "PVU3FW7F"
title: "Mining Semantic Soft Factors for Credit Risk Evaluation in Peer-to-Peer Lending"
authors: "Zhao Wang; Cuiqing Jiang; Huimin Zhao; Yong Ding"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1705513"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mining Semantic Soft Factors for Credit Risk Evaluation in Peer-to-Peer Lending

Zhao Wang, Cuiqing Jiang, Huimin Zhao & Yong Ding

To cite this article: Zhao Wang, Cuiqing Jiang, Huimin Zhao & Yong Ding (2020) Mining Semantic Soft Factors for Credit Risk Evaluation in Peer-to-Peer Lending, Journal of Management Information Systems, 37:1, 282-308, DOI: 10.1080/07421222.2019.1705513

To link to this article: https://doi.org/10.1080/07421222.2019.1705513

![](/api/attachments/PVU3FW7F/fulltext/images/c2832451a1ed36521c4e4587cda20898f9442fee23a7d54bf469004c3a1d2e9d.jpg)

View supplementary material

![](/api/attachments/PVU3FW7F/fulltext/images/988b9abc56882cc395cadf9024eaecc008c183352d5565b74968fc42c4a5a47d.jpg)

Published online: 01 Mar 2020.

![](/api/attachments/PVU3FW7F/fulltext/images/d7b97ba4ec5227a338048611a7b57ea370d5f1b5caeb5ca67f5fdc7173842233.jpg)

Submit your article to this journal

![](/api/attachments/PVU3FW7F/fulltext/images/a6737ab7a25fea31d61fde664b9d2c9fa038f8053585f0f90eec16d4db032d7b.jpg)

Article views: 12

![](/api/attachments/PVU3FW7F/fulltext/images/96d7fe3334e9932fe04531fa1115e6d9713ec4b12ec19dc5fa57b3a89d78a048.jpg)

View related articles

![](/api/attachments/PVU3FW7F/fulltext/images/63f909ab57a84ffac5fa0007691ec79f64208a382c0d6dd964d43822c1e2b798.jpg)

View Crossmark data

Check for updates

# Mining Semantic Soft Factors for Credit Risk Evaluation in Peer-to-Peer Lending

Zhao Wang<sup>a</sup>, Cuiqing Jiang<sup>a,b</sup>, Huimin Zhao<sup>c</sup>, and Yong Ding<sup>a</sup>

<sup>a</sup>School of Management, Hefei University of Technology, Hefei, Anhui, P.R. China; <sup>b</sup>Laboratory of Process Optimization and Intelligent Decision-making, Ministry of Education, Hefei, Anhui, P.R. China; <sup>c</sup>Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee, Milwaukee, WI, USA

## ABSTRACT

While Peer-to-Peer (P2P) lending is rapidly growing, it is also accompanied by high credit risk due to information asymmetry. Besides conventional hard information, soft information also enters into the lending decision process. The descriptive loan texts submitted by borrowers have great potential for exploiting useful soft factors, but also pose great challenges due to the semantic sensitivity to context and the complexity of content representation. We propose a novel text mining method for automatically extracting semantic soft factors from descriptive loan texts. The method maps terms to an embedding space, assembles semantically related terms together into semantic cliques, and then de<sup>fi</sup>nes semantic soft factors corresponding to the semantic cliques. Empirical evaluation shows that the extracted semantic soft factors contributed to signi<sup>fi</sup>cant improvement on credit risk evaluation in terms of both discrimination performance and granting performance. This work advances our knowledge of soft information indicative of a borrower’s credit risk.

## KEYWORDS

P2P lending; descriptive loan text; credit risk evaluation; text mining; soft information; semantic soft factor; online lending

## Introduction

Peer-to-Peer (P2P) lending, with its practice of lending money to individuals or businesses through online services that match lenders with borrowers, has been enjoying rapid development in recent years[25, 47]. By o<sup>f</sup>ering services generally online and bypassing traditional intermediaries, P2P lending can operate with lower overhead, thus often resulting in higher returns for lenders and lower interest rates for borrowers [19]. However, the pro<sup>fi</sup>table P2P lending is also accompanied by a high degree of credit risk due to information asymmetry, as lenders do not know the borrowers and are investing based on limited information provided by P2P lending platforms. Evaluating the credit risk of borrowers and identifying non-creditworthy ones thus become a matter of great importance for the P2P lending market.

Credit risk refers to the risk of default on a loan that may arise from the borrower failing to make required repayments [28]. The methods to best evaluate the credit risk (i.e., loan default prediction) when making granting decision is understandably di<sup>fi</sup>cult. It is even harder in P2P lending since most of the lenders in this market are non-experts with limited experience and no formal training in judging borrower creditworthiness. Meanwhile, the borrower group is more complicated, compared to that in the traditional bank loan context, as some of the borrowers may not be approved for traditional bank loans due to lack of conformity to credit criteria and underwriting [24]. Furthermore, the future performance of a borrower, defaulting or not, is not just the result of a mechanical <sup>fi</sup>nancial measurement, but is also driven by the complexities and idiosyncrasies of human behavior [18, 23]. Even in the identical <sup>fi</sup>nancial situation, di<sup>f</sup>erent borrowers may vary in the ability and willingness of repayment [23]. Accordingly, in addition to the classical hard information, soft information about borrowers also becomes important in the process of credit risk evaluation in P2P lending.

Information, including hard information and soft information, is an essential component of all <sup>fi</sup>nancial transactions and markets. While the literature has expanded, the problem of creating precise de<sup>fi</sup>nitions for hard information and soft information “has not gotten easier” [29, p. 3], but their characteristics have been described by several researchers [4, 29]. For example, Liberti and Petersen [29, pp. 3 -5] described the characteristics of soft and hard information in three aspects. First, “hard information is almost always recorded as numbers,” whereas “soft information is often communicated as text.” Second, another characteristic of hard information “is the unimportance of the context under which the information is collected,” whereas “with soft information, the context under which the information is collected and the collector of the information are part of the information.” Third, “the unimportance of context for hard information means it is possible to separate the collection of hard information from the decision-making based on that information,” whereas “soft information must be collected in person, and the information collector and the decision maker are often the same person.” Another factor that prior literature often mentions is the veri<sup>fi</sup>ability of information, that is, hard information tends to be veri<sup>fi</sup>able, and soft information tends to be unveri<sup>fi</sup>able [4]. While “there is no clear dichotomy” and “we should think of a continuum along which information can be classi<sup>fi</sup>ed” [29, p. 3], in this paper, for simplicity, we refer to the information in descriptive loan texts as soft information and other information submitted by borrowers (e.g., loan amount, interest rate, and income) or provided by the P2P platform (e.g., credit grade), which has been commonly used in credit risk evaluation models, as hard information. However, we caution that this simple distinction is for a pragmatic purpose only and is certainly imprecise. For instance, gauged in terms of veri<sup>fi</sup>ability, some of the quantitative information self-reported by borrowers is unveri<sup>fi</sup>- able and would be better considered as soft information.

When lenders browse the loan listings at a P2P lending platform for investing, the available information about the loan listings consists of hard information (e.g., interest rates and the income of borrowers) and soft information (e.g., descriptive loan texts). Descriptive loan texts, as self-reported information re<sup>fl</sup>ecting the mental process of borrower behavior, constitute a valuable repository of soft factors [12, 46]. It contains various (e.g., <sup>fi</sup>nancially connoted, emotionally connoted, and socially connoted) aspects of soft factors that relate to borrowers. Such soft factors, which are implied in the contents of descriptive loan texts, have the potential to re<sup>fl</sup>ect the repayment willingness and ability of borrowers to some extent and therefore help to predict the credit risk of a borrower [12, 23, 24, 46]. Such soft factors, however, are always implicit in the contents and need to be e<sup>f</sup>ectively mined. Given the importance of soft information that carries implicit discriminant factors and the fact that a large number of lenders in P2P lending are not experts, an e<sup>f</sup>ective method for mining such soft factors from descriptive loan texts is extremely valuable for lending decision support.

In this study, we explore the utility of descriptive loan text-related soft information for credit risk evaluation in P2P lending. There has been some research to examine the use of self-descriptions of borrowers for mitigating issues of information asymmetry in the P2P lending market. Certain features of descriptive loan texts have been shown to have meaningful discrimination abilities for loan default and could be applied in credit risk modeling, examples including statistics features, readability features, and sentiment features [17, 23, 46]. However, such features examined in the past (i.e., statistics, readability, sentiment, etc.) mostly capture linguistic and stylistic characteristics but barely re<sup>fl</sup>ect the contents (i.e., semantics), which may contain more direct and e<sup>f</sup>ective information related to creditworthiness.

Consider the following real example of descriptive loan text:

I have a stable job and I will be absolutely no problem making monthly payments. Loan will be used to close high interest credit card accounts on which I’ve never had a late payment.

From the conventional perspective of soft information, this descriptive text is quite readable and easy to understand. The text also shows strong subjectivity with subjective description in <sup>fi</sup>rst person. Meanwhile, based on the judgment of sentiment words, it also conveys positive sentiment. The potentially more intuitive and e<sup>f</sup>ective information related to creditworthiness, however, is hidden in the contents represented by keywords. In this case, the keywords stable job imply a good solvency for monthly payments, the keywords close high interest credit state the loan purpose, and the keywords never late payment express the repayment history.

The certain aspects of content that a borrower wants to express are presented with a set of keywords. Di<sup>f</sup>erent borrowers may use di<sup>f</sup>erent keywords to express a certain aspect of content, but the meanings (i.e., semantics) should be close, thus forming a group of semantically related words. For instance, suppose a borrower intends to express a positive personality, she might take advantage of keywords like studious, industrious, and hardworking. Similarly, if she wants to talk about education, she might use keywords like school, graduate, and college. If she simply wants to state time, she might use keywords like today, yesterday, and this month. The challenges in e<sup>f</sup>ectively extracting this kind of soft factors (i.e., semantic soft factors) lie in how to capture the various syntactical and semantic relationships between keywords (e.g., school should be close to college but not city), and how to construct content-based soft factors for describing multiple aspects of meaning.

In this paper, we strive to address the challenges of extracting semantic soft factors from descriptive loan texts. Aiming at exploiting content-based soft factors to improve the performance of credit risk evaluation (i.e., loan default prediction), we propose a novel text mining method for automatically extracting semantic soft factors from the descriptive texts of loan applications borrowers submit at a P2P lending platform. In order to capture the complex syntactical and semantic relationships, the proposed method transfers the terms in the descriptive loan texts into a vector form by constructing an embedding space, in which semantically related terms are close to each other. Speci<sup>fi</sup>cally, we <sup>fi</sup>rst adopt the existing word embedding algorithm GloVe [36] to capture the semantic relationships among terms in descriptive loan texts. Then, considering the representation of di<sup>f</sup>erent aspects of contents (e.g., past credit experience, current <sup>fi</sup>nancial situation, and future repayment plan) hidden in descriptive loan texts, we propose a semantic clique extraction algorithm for clustering the semantically close terms in the embedding space. A semantic clique refers to a group of semantically close terms, including collocations. We then propose a set of semantic soft factors, each of which corresponds to a semantic clique, and use the semantic soft factors to complement the traditional hard factors in credit risk evaluation models.

We have evaluated our proposed method using a large dataset on personal loans from a major P2P lending platform in the United States. Even a small improvement (e.g., 1 percent) on the performance of credit risk evaluation may result in a considerable reduction in the loss caused by the event of default in the P2P lending market, given its volume and velocity [45]. We evaluated our extracted semantic soft factors at two levels, the model level and the application level. From the model perspective, credit risk evaluation generally poses a classi<sup>fi</sup>cation problem, that is, whether a borrower will default on a particular loan or not, and hence we evaluated the extracted semantic soft factors by comparing models based on hard factors, semantic soft factors, and their combination in terms of discrimination performance. From the application perspective, in real P2P lending scenarios, lenders tend to diversify their investments to mitigate total credit risk, and hence we also evaluated the usefulness of the extracted semantic soft factors in improving granting performance by simulating real investment scenarios of loan portfolio selection. The results show that incorporating the extracted semantic soft factors signi<sup>fi</sup>- cantly improved both discrimination performance and granting performance.

## Literature Review

Since the <sup>fi</sup>rst P2P lending platform, Zopa (www.zopa.com), started to o<sup>f</sup>er P2P loans in 2005, P2P lending has experienced enormous development all over the world. Some examples of major players in this domain are Lending Club and Prosper in the United States and PaiPaiDai in China. Like in the traditional credit market, the participants in the P2P lending market can be divided into two groups: borrowers and lenders. As a result, decision making and risk evaluation can be viewed from the perspectives of these two groups.

From a borrower’s perspective, the point of concern is whether her loan application can be funded. Several studies have examined factors that may in<sup>fl</sup>uence funding success. For example, Larrimore et al. [27] showed that borrowers can optimize their persuasiveness by monitoring their language used in textual descriptions, and Iyer et al. [23] showed that providing a picture along with a loan application has a positive e<sup>f</sup>ect on funding success.

From a lender’s perspective, the point of concern is generally related to decision making on a particular loan based on credit risk evaluation (i.e., loan default prediction). Loan default prediction has attracted extensive research in two main streams. One stream of literature focuses on loan default prediction methods, which classify each loan application as either creditworthy or non-creditworthy. In this case, the traditional loan evaluation methods, also called credit scoring methods [3, 28] are also applicable to P2P lending. A number of studies have used data mining techniques to support the classi<sup>fi</sup>cation of loan applications. Some examples are logistic regression [14, 18], support vector machine [21, 48], neural network [26, 35], and survival analysis [41, 44]. In recent years, ensemble learning, with its competitive and robust discrimination performance, has been broadly used in credit risk evaluation [1, 11, 16].

The other main stream of literature focuses on <sup>fi</sup>nding e<sup>f</sup>ective factors related to loan default. Several studies provided valuable insights into the relationship between loan default and hard factors, which usually serve as repayment ability indicators [30]. For example, Emekter et al. [14] found that credit grade, debt-to-income ratio, FICO score, and revolving line utilization play important roles in evaluating loan default risk. Soft information can, however, still help to mitigate the information asymmetry. When hard information is missing or insu<sup>fi</sup>cient, soft information provides e<sup>f</sup>ective supplementary factors to improve the performance of credit risk evaluation [37, 46]. Description texts, speci<sup>fi</sup>cally in the context of P2P lending, contain useful features for credit risk evaluation [12]. Iyer et al. [23] showed that statistical characteristics of loan listing texts (e.g., document length, average word length, percentage of words misspelled, and number of dollar signs) are related to loan repayment, and soft features are relatively more important when evaluating low-quality borrowers. Gao et al. [17] also showed that some wellestablished features, including readability, objectivity, negativity, and deception cues, are all meaningfully related to loan repayment. Wang et al. [46] proposed a credit risk evaluation system and used <sup>fi</sup>ve dimensions of textual information (i.e., statistical, POS, sentiment, entity, and temporal features) to improve the performance of an ensemble of multiple expert systems.

Most previous studies examined the utility of descriptive loan text related soft information from linguistic or stylistic aspects. As far as we know, the only work that examined descriptive loan texts in P2P lending from the semantic aspect is Jiang et al. [24], which extracted topic-related soft factors for loan default prediction. However, topic-related methods are poor at capturing the semantic similarity between words, and are therefore inadequate at extracting semantic soft factors. In this study, we strive to <sup>fi</sup>ll this gap in the current literature by mining descriptive loan texts from the semantic aspect and evaluating the e<sup>f</sup>ect of the mined semantic soft factors on credit risk evaluation.

## Proposed Semantic Soft Factor Mining Method

In this section, we describe in detail our proposed method for extracting semantic soft factors from descriptive loan texts in P2P lending.

The proposed semantic soft factor mining method aims to identify di<sup>f</sup>erent patterns of semantic representation by good (non-default) versus bad (default) borrowers, in terms of the distribution of the kinds of semantics expressed in the descriptive loan text. The certain aspects of content that a borrower wants to express are presented with a set of keywords. Di<sup>f</sup>erent borrowers may use di<sup>f</sup>erent keywords to express a certain aspect of content, but the semantics should be close, thus forming a group of semantically related keywords. Therefore, we apply semantic analysis to measure the semantic similarities among di<sup>f</sup>erent keywords, and then group semantically related keywords together. Speci<sup>fi</sup>cally, in order to capture complex syntactical and semantic relationships in descriptive loan texts, we <sup>fi</sup>rst map terms into an embedding space, in which semantically related terms are close to each other. Subsequently, considering that borrowers may use di<sup>f</sup>erent terms from a group of semantically related terms to describe a certain aspect of meaning, we also propose a sequential extraction algorithm to automatically extract semantic cliques, that is, sets of semantically related terms. The semantics of a piece of descriptive loan text is then represented as a set of semantic soft factors, each of which corresponds to a semantic clique, by integrating all the terms in the corresponding semantic cliques. Such semantic soft factors can then be used to complement the traditional hard factors in credit risk evaluation models and hopefully improve the predictive performance.

![](/api/attachments/PVU3FW7F/fulltext/images/7869db6292b756844a6a30fca557cfee72898deb78fe9cd3b3f936bb1cc6fbc6.jpg)  
The proposed semantic soft factor extraction method.

As illustrated in Figure 1, the proposed method consists of four phases: vocabulary construction, word embedding space construction, semantic clique extraction, and semantic soft factor de<sup>fi</sup>nition. The following is an outline of the phases in our method.

(1) Build a vocabulary with terms, including single words and collocations.

(2) Train a word embedding for capturing semantic relationships among the terms.

(3) Create a semantic clique and sequentially add semantically close terms into the clique. This is repeated until every term in the vocabulary has been added into some semantic clique.

(4) De<sup>fi</sup>ne semantic soft factors according to the semantic cliques.

## Fixed Multiword Expressions

Besides individual words, which are regularly used in text mining applications, the vocabulary built in our method also includes <sup>fi</sup>xed multiword expressions. A <sup>fi</sup>xed multiword expression refers to a string of words, which behaves like a single word [22]. Such expressions often appear in descriptive loan texts. For example, we always use the term “nest egg” to refer to rescue fund that can be used for something special in the future, rather than its literal meaning (i.e., a kind of egg). A more domain-speci<sup>fi</sup>c example is “Lending Club,” which is the name of one of the most popular P2P lending platforms in the United States. Looking at the words in these expressions individually cannot uncover the true meanings of the expressions and will mislead the subsequent analysis. We refer to this type of <sup>fi</sup>xed multiword expressions as collocations in this paper. Given the implicit meaning a collocation carries, concatenating a meaningful multiword expression as a new term is valuable for semantic text analytics. Hence, before building a vocabulary, the proposed method <sup>fi</sup>rst extracts collocations by going through successive words and calculating some statistics, e.g., how frequently one word follows another and frequencies of words. Speci<sup>fi</sup>cally, we comprehensively apply four existing scores for extracting collocations: Co-Occurrence Frequency (COF), Pointwise Mutual Information (PMI), Log-Frequency biased Mutual Dependency (LFMD), and Gensim.

COF of a colocation of words $w _ { i }$ and $w _ { j }$ is simply the frequency that $w _ { i } w _ { j }$ co-occurs (i.e., bigram) in the focal corpus, denoted as $c o u n t \big ( w _ { i } w _ { j } \big )$

PMI quanti<sup>fi</sup>es the discrepancy between the coincidence probability of a pair of words given their joint distribution and their individual distributions, and has been widely used in previous studies (e.g., [7]). Given the probabilities of a pair of words $w _ { i }$ and $w _ { j } , P ( w _ { i } )$ and $P \big ( w _ { j } \big )$ , respectively, and the probability of the bigram $w _ { i } w _ { j } , \ P \big ( w _ { i } w _ { j } \big )$ , PMI can be calculated as

$$
P M I \left(w _ {i}, w _ {j}\right) = \log_ {2} \frac {P \left(w _ {i} w _ {j}\right)}{P \left(w _ {i}\right) P \left(w _ {j}\right)}.\tag{1}
$$

LFMD is a combination of the t-score and Mutual Dependency (MD), which is PMI minus self-information, for introducing a slight frequency bias [22]. Speci<sup>fi</sup>cally, LFMD can be calculated as:

$$
L F M D \left(w _ {i}, w _ {j}\right) = \log_ {2} \frac {P ^ {2} \left(w _ {i} w _ {j}\right)}{P \left(w _ {i}\right) P \left(w _ {j}\right)} + \log_ {2} P \left(w _ {i} w _ {j}\right).\tag{2}
$$

Gensim is a widely used open source library that can automatically detect multi-word expressions. It uses a simple data-driven method, in which word collocations are extracted based on unigram and bigram counts [33]. Speci<sup>fi</sup>cally, the following score is computed.

$$
\operatorname{Score} \left(w _ {i}, w _ {j}\right) = \frac {\left(\operatorname{count} \left(w _ {i} w _ {j}\right) - \delta\right) \times N}{\operatorname{count} \left(w _ {i}\right) \times \operatorname{count} \left(w _ {j}\right)},\tag{3}
$$

where δ is a discounting coe<sup>fi</sup>cient used to prevent forming too many collocations consisting of very infrequent words and N is the vocabulary size.

Given the four scores (i.e., COF, PMI, LFMD, and Gensim), successive words are concatenated into a collocation when some preset thresholds on the four scores are all met. While these scores all have their advantages and drawbacks, by applying all of them jointly, the proposed method is able to reduce noise (i.e., spurious collocations) in the resulting vocabulary. Combining the four existing scores results in a stronger measure since every single score needs to be above the threshold. Similar practice can be found in Tong et al. [44], who combined multiple convergence measures into a stronger measure.

## Word Embedding

In order to capture the syntactical and semantic relationships among terms $( \mathrm { i . e . }$ , words and collocations), the proposed method constructs an embedding space (also called vector space), in which semantically related terms are close to each other, and maps each term in the vocabulary into the embedding space. Some main method families for understanding texts in a vector space are: (1) one-hot representation, (2) global matrix factorization, and (3) word embedding based on local context window. However, all three method families have various degrees of insu<sup>fi</sup>ciencies in this case. One-hot representation, which intuitively treats each term as a feature and processes each term as a vector, may su<sup>f</sup>er from the “lexical $\mathrm { g a p } ^ { \mathfrak { n } }$ problem, that is, terms are isolated and the relationship between two terms cannot be obtained from their vectors even though their semantics may be very similar or related. Global matrix factorization methods, such as latent semantic analysis (LSA) [13], e<sup>f</sup>ectively utilize global statistical information, but are insu<sup>fi</sup>cient at forming a vector space structure for capturing syntactical and semantic relationships. Word embedding models based on local context windows, such as Word2Vec, which are also known as skip-gram models [34], may be able to capture syntactical and semantic relationships, but poorly leverage global statistical information, since they train on local context windows, instead of on global co-occurrence matrix. A method that can both capture syntactical and semantic relationships and leverage global statistical information is therefore highly desirable. To this end, we adopt a recently proposed word embedding algorithm, GloVe [36], which e<sup>f</sup>ectively utilizes global corpus statistics and produces a vector space with meaningful substructures. For completeness, we brie<sup>fl</sup>y describe GloVe in the following section.

Let X denote the matrix of word-word co-occurrence counts. Let $X _ { i } = \sum _ { k } X _ { i k }$ denote the number of any words in the context of word i (i.e., a <sup>fi</sup>xed-sized window around word i within which words are deemed to co-occur) and $X _ { i j }$ denote the number of times that word j occurs in the context of word i. Let $\begin{array} { r } { P _ { i j } = P ( j | i ) = \frac { X _ { i j } } { X _ { i } } } \end{array}$ denote the probability that word j appears in the context of word i. Then, the relationship between word i and word j can be measured by the ratio of co-occurrence probabilities with various probe words k (i.e., $\begin{array} { r } { \frac { P _ { i k } } { P _ { j k } } ) } \end{array}$ ). If word k is related to word i but not word $j ,$ the ratio $\frac { P _ { i k } } { P _ { j k } }$ is expected to be large. If word k is related to word j but not word i, the ratio $\frac { P _ { i k } } { P _ { j k } }$ is expected to be small. If word k is related to both word i and word j or is not related to either of them, the ratio $\frac { P _ { i k } } { P _ { j k } }$ should be close to one. Hence, the general model for word vector can be expressed as [36]:

$$
w v _ {i} ^ {T} \widetilde {w v} _ {k} + b _ {i} + \tilde {b} _ {k} = \log (X _ {i k}),\tag{4}
$$

where $b _ { i }$ and $\tilde { b } _ { k }$ are biases for a main word vector $w \nu _ { i }$ and a context word vector $\widetilde { w \nu _ { k } }$ respectively.

Equation (4) is still inadequate since the logarithm diverges when its argument approaches zero. The divergence problem can be resolved using a global log-bilinear regression model [36]. By building a least squares problem, Equation (4) can be transformed into a cost function:

$$
J = \sum_ {i, j = 1} ^ {V} f (X _ {i j}) \left(w v _ {i} ^ {T} \widetilde {w v} _ {j} + b _ {i} + \tilde {b} _ {j} - \log (X _ {i j})\right) ^ {2},\tag{5}
$$

where V is the size of the vocabulary and $f \left( X _ { i j } \right)$ is a weighting function de<sup>fi</sup>ned as

$$
f (x) = \left\{ \begin{array}{c} \left(\frac {x}{x _ {\max}}\right) ^ {\alpha} i f x <   x _ {\max} \\ 1 \text { otherwise } \end{array} \right..\tag{6}
$$

As shown in Equation (4), the outcome consists of two vectors, that is, main word vector $w \nu _ { i }$ and context word vector $\widetilde { w \nu _ { k } }$ . Typically, the two word vectors are equivalent [36]. It has been shown that taking advantage of both vectors by training on multiple observations and combining the results is bene<sup>fi</sup>cial for reducing over<sup>fi</sup>tting and obtaining better results [9]. Hence, the <sup>fi</sup>nal word vector is calculated by taking the sum of the main and context word vectors [36].

$$
W V _ {f i n a l} = W V + \widetilde {W V}.\tag{7}
$$

## Semantic Clique Extraction

After mapping each term (i.e., word or collocation) in the vocabulary into an embedding space, in which semantically related terms are close to each other, semantic factors, subsequently, could be extracted from the embedding space in terms of semantic cliques. A straightforward way to obtain semantic cliques is to use traditional clustering methods, such as k-means [49], in which all objects are clustered into a preset number (k) of groups. However, this kind of methods always face the di<sup>fi</sup>culties in determining the appropriate number of groups and selecting clustering centers. These problems are of critical concerns in the case of extracting semantic soft factors from descriptive loan texts, since di<sup>f</sup>erent numbers of groups may re<sup>fl</sup>ect varying degrees of semantics (e.g., one group may be divided into several <sup>fi</sup>ner-grained groups when increasing the number of groups) and it is more rational to preferentially consider the terms that are relatively more important in the context. To this end, we propose a sequential extraction algorithm for automatically extracting semantic cliques without presetting the number of groups and clustering centers.

Figure 2 presents our proposed algorithm. In order to preferentially extract relatively more important terms in a sequentially extracting process, all the terms are sorted on an importance score $I M P _ { t _ { i } }$ . The document-term matrix (DTM) is <sup>fi</sup>rst transformed from a term frequency form into a term frequency-inverse document frequency (TFIDF) form. TFIDF is a statistic that re<sup>fl</sup>ects how important a term is to a document and has been widely used in the <sup>fi</sup>eld of natural language processing [2]. Given a term (i.e., word or collocation) $t _ { i }$ and a document $d _ { z }$ , the TFIDF of term $t _ { i }$ in document $d _ { z }$ can be computed as:

$$
T F I D F _ {i, z} = T F _ {i, z} \times I D F _ {i} = \frac {n _ {i , z}}{\sum_ {t _ {k} \in d _ {z}} n _ {k , z}} \times \log \frac {| D |}{1 + | \{d _ {z} \in D : t _ {i} \in d _ {z} \} |},\tag{8}
$$

where $n _ { i , z }$ denotes the number of times that term $t _ { i }$ appears in document $d _ { z } , | D |$ denotes the total number of documents, and $\left| \{ d _ { z } \in D : t _ { i } \in d _ { z } \} \right|$ denotes the number of documents where term $t _ { i }$ appears. Subsequently, the importance of each term $I M P _ { t _ { i } }$ is measured as the total TFIDF across all the documents:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Vocabulary  $KV = \{w_{1}, w_{2}, ..., w_{i}\}$ ;
Document-term matrix DTM;
Word vector for each term  $WV = \{w v_{1}, w v_{2}, ..., w v_{i}\}$ ;
Threshold on semantic similarity  $\theta$ .
Output: Semantic cliques,  $SC = \{sc_{1}, sc_{2}, ..., sc_{k}\}$ .
1 Sort terms in DTM based on TFIDF,  $DTM_{sort} = \text{Sort}(DTM)$ ;
2  $SC = \emptyset$ ,  $ss_{max} = 1$ ;
3 k = 1;
4 while count(KV) &gt; 1 do
5  $sc_{k} = \{DTM_{sort}[1]\}$ ;
6 while  $ss_{max} &gt; \theta$  do
7  $L_{SC} = \text{count}(sc_{k})$ ;
8 for  $w_{x} \in KV \land w_{x} \notin sc_{k}$  do
9  $ss_{w_{x}} = (1/L_{SC}) \sum_{w_{z} \in sc_{k}} \text{cosine}(w_{x}, w_{z})$ ;
10 end for
11  $ss_{max} = \max_{w_{x} \in KV \land w_{x} \notin sc_{k}} (ss_{w_{x}})$ ;
12 if  $ss_{max} &gt; \theta$  then
13  $sc_{k} = sc_{k} \cup \{w_{ss_{max}}\}$ ;
14  $KV = KV - \{sc_{k}\}$ ;
15 end if
16 end while
17 Remove  $sc_{k}$  from  $DTM_{sort}$ ;
18  $k = k + 1$ ;
19 end while
</div>

Procedure for extracting semantic cliques from the word embedding space.

$$
I M P _ {t _ {i}} = \sum_ {d _ {m} \in D} T F I D F _ {i, m}.\tag{9}
$$

After obtaining the sorted term list, our proposed algorithm selects the top-rank term to create a new semantic clique and sequentially adds the semantically close terms into the semantic clique according to the average semantic similarity between the candidate term and all the terms in the clique. The semantic similarity between two terms in the embedding space is measured by the cosine similarity between their word vectors. Two terms are considered to be semantically close only when the cosine distance between their word vectors are higher than a similarity threshold. When no term reaches the similarity threshold, the current semantic clique is completed and the terms in this semantic clique are removed from the vocabulary. This process is repeated, with the remaining terms, to create another semantic clique. The algorithm terminates when the vocabulary becomes empty. As a result, multiple semantic cliques are generated, each of which represents a certain aspect of meaning that borrowers want to express.

The only parameter that needs to be preset is the semantic similarity threshold. The semantic representation of descriptive loan texts with semantic cliques of di<sup>f</sup>erent granularities would be generated as the semantic similarity threshold changes. A high threshold would increase speci<sup>fi</sup>city but decrease sensitivity, leading to a large number of semantic cliques, some of which may be even independent (i.e., a semantic clique consisting of a single term). Inversely, a low threshold would increase sensitivity but decrease speci<sup>fi</sup>city, leading to a small number of semantic cliques, in which plenty of terms, possibly including semantically unrelated ones, are gathered in a semantic clique. An appropriate threshold needs to be empirically tuned.

## Semantic Soft Factor De<sup>fi</sup>nition

Once the semantic cliques are extracted, the semantic representation of a piece of descriptive loan text is then built as a set of semantic soft factors, each of which corresponds to a semantic clique, by integrating all the terms in the corresponding semantic cliques. As a result, the number of soft factors is equal to the number of extracted semantic cliques. The semantic soft factors for each descriptive loan text are measured by summing the TFIDF values of all the terms in the corresponding semantic cliques. Given the weighted vector of each term (i.e., the corresponding column of TFIDF weighted document-term matrix) in a semantic clique, $\displaystyle S C _ { x } = \{ W t \mathbf { V } _ { 1 } , W t V _ { 2 } , \ldots , W t V _ { l } \}$ , the corresponding vector of each soft factor can be expressed as:

$$
\boldsymbol {S F} _ {\boldsymbol {x}} = \sum_ {W t V _ {u} \in S C _ {x}} W t V _ {\boldsymbol {u}}.\tag{10}
$$

The semantic soft factors can then be used as features to complement the typical features based on hard factors in credit risk evaluation models, hopefully leading to improved performance.

## Empirical Evaluation

We have evaluated our proposed method on a large dataset from Lending Club. The platform allows quali<sup>fi</sup>ed borrowers to apply for unsecured personal loans with a 36- month or 60-month term. Investors can search and browse the active loan listings on the platform and select any number of loans (i.e., single loan or loan portfolio) they want to invest in, based on the information, both hard information and soft information, supplied by the platform. If a loan is issued, the platform charges a fee for providing the matchmaking and credit-checking the borrower.

## Data

In order to obtain the entire loan status, we used data on the 36-month loans between 2007 and 2012 (i.e., ending in 2015). After removing some observations with missing values, the dataset used in our evaluation consists of 40,010 loan observations. A loan observation “is considered defaulted when at least one payment is more than 120 days late and it is charged-o<sup>f</sup> no later than when it reaches 150 days late,” according to the platform. We treated both these cases as bad loans, collectively called default. Accordingly, there are 35,103 non-default loan observations and 5007 default loan observations in the dataset (12.48 percent default rate). Table 1 summarizes the attributes of loan application information available in the dataset. All attributes except the loan description constitute hard factors, which are commonly used in credit risk evaluation.

Attributes used in analysis.

<table><tr><td rowspan="2">No.</td><td>Attribute</td><td colspan="4">Summary Statistics</td></tr><tr><td>Continuous</td><td>Min</td><td>Max</td><td>Mean</td><td>SD</td></tr><tr><td>1</td><td>Loan Amount</td><td>500</td><td>35,000</td><td>10,828</td><td>6,624.60</td></tr><tr><td>2</td><td>Interest Rate</td><td>5.42</td><td>24.89</td><td>11.70</td><td>3.52</td></tr><tr><td>3</td><td>Installment</td><td>15.69</td><td>1,380.63</td><td>358.25</td><td>225.60</td></tr><tr><td>4</td><td>Annual Income</td><td>4,000</td><td>1,900,000</td><td>66,573</td><td>47,031.26</td></tr><tr><td>5</td><td>Dti *</td><td>0</td><td>34.97</td><td>14.83</td><td>7.33</td></tr><tr><td>6</td><td>Delinquency Incidences in Past 2 Years</td><td>0</td><td>14</td><td>0.15</td><td>0.54</td></tr><tr><td>7</td><td>Earliest Credit Line (days)</td><td>2,406</td><td>22,495</td><td>6,765</td><td>2,448.10</td></tr><tr><td>8</td><td>Inquiries in Past 6 Months</td><td>0</td><td>8</td><td>0.81</td><td>1.02</td></tr><tr><td>9</td><td>Last Delinquency (months)</td><td>0</td><td>115</td><td>13.05</td><td>21.76</td></tr><tr><td>10</td><td>Last Public Record (months)</td><td>0</td><td>129</td><td>3.31</td><td>17.60</td></tr><tr><td>11</td><td>Number of Open Credit Lines</td><td>2</td><td>46</td><td>9.88</td><td>4.34</td></tr><tr><td>12</td><td>Number of Derogatory Public Records</td><td>0</td><td>3</td><td>0.04</td><td>0.20</td></tr><tr><td>13</td><td>Total Credit Revolving Balance</td><td>0</td><td>149,527</td><td>13,416</td><td>13,907.36</td></tr><tr><td>14</td><td>Revolving Line Utilization Rate</td><td>0</td><td>99.90</td><td>52.19</td><td>26.56</td></tr><tr><td>15</td><td>Number of Credit Lines</td><td>2</td><td>90</td><td>22.22</td><td>10.93</td></tr><tr><td></td><td>Categorical</td><td>Number of Categories</td><td>Values</td><td></td><td></td></tr><tr><td>16</td><td>Platform-assigned Grade</td><td>7</td><td colspan="3">{A, B, C, D, E, F, G}</td></tr><tr><td>17</td><td>Platform-assigned Sub-grade</td><td>35</td><td colspan="3">{A1-A5, B1-B5, C1-C5, D1-D5, E1-E5, F1-F5, G1-G5}</td></tr><tr><td>18</td><td>Employment Length (years)</td><td>12</td><td colspan="3">{none, &lt;1y, 1y, 2y, 3y, 4y, 5y, 6y, 7y, 8y, 9y, 10+y}</td></tr><tr><td>19</td><td>Home Ownership</td><td>4</td><td colspan="3">{mortgage, own, rent, other}</td></tr><tr><td>20</td><td>Verification Status</td><td>3</td><td colspan="3">{no verified, source verified, verified}</td></tr><tr><td>21</td><td>Purpose</td><td>14</td><td colspan="3">{debt consolidation, credit card, home improvement, major purchases, small business, ..., other} **</td></tr><tr><td>22</td><td>State</td><td>44</td><td colspan="3">{CA, NY, TX, FL, NJ, IL, ... } **</td></tr><tr><td>23</td><td>Initial Listing Status</td><td>2</td><td colspan="3">{whole, fractional}</td></tr><tr><td></td><td>Text</td><td></td><td></td><td></td><td></td></tr><tr><td>24</td><td>Descriptive Loan Text</td><td></td><td></td><td></td><td></td></tr></table>

: \* Dti denotes a ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, <sup>otes</sup>excluding mortgage and the requested loan, divided by the self-reported monthly income.  
\*\* Some infrequent categories are omitted, in the interest of space.

Due to the nature of P2P lending, most attribute values are self-reported by borrowers and not veri<sup>fi</sup>ed, making accurate credit risk evaluation more di<sup>fi</sup>cult than in the traditional bank loan context.

The descriptive loan text is a self-description provided by the borrower. As discussed earlier, the descriptive loan text may communicate the borrower’s past credit experience, current <sup>fi</sup>nancial situation, or future repayment plan, and the content may imply various (e.g., <sup>fi</sup>nancially connoted, emotionally connoted, and socially connoted) soft factors. The more detailed the descriptive loan text, the more useful information it may convey. Before extracting the semantic soft factors, we <sup>fi</sup>rst preprocessed the corpus by lemmatization to enhance the applicability of our method. In descriptive loan texts, especially in English, words appear in several in<sup>fl</sup>ected forms. For example, the verb lend may appear as lends, lent, and lending, but their semantics is the same as that of the lemma for the word. We used an open source toolkit, Stanford CoreNLP, to group together the in<sup>fl</sup>ected forms of a word into a single item, namely, the word lemma [31].

## Extracting Semantic Soft Factors

In the process of applying the proposed method, we <sup>fi</sup>rst <sup>fi</sup>ltered out some words that may be useless for our purpose of extracting semantic soft factors, namely, stop words and sparse words. We used a basic stop word list including 174 stop words (e.g., my, we, he, and she) to delete some of the most common words. We also removed some sparse words, which appear very rarely in all descriptive loan texts. We set the sparsity threshold to 0.001 (i.e., the proportion of the descriptive loan texts containing a certain word should be greater than 0.001).

As discussed earlier, before constructing the vocabulary, the proposed method also extracts collocations, which may carry special meanings. The thresholds on the four scores (i.e., COF, PMI, LFMD, and Gensim) were set to 10, 8, -25, and 10, respectively, as recommended by the R package we used, text2vec,<sup>1</sup> resulting in 256 selected collocations (e.g., san\_francisio, active\_duty, and clean\_slate). Note that these recommended threshold values are heuristic, and better results may be generated after tuning the thresholds. A sensitivity analysis for the thresholds is reported in Appendix A.

We then trained a word embedding model using GloVe and subsequently extracted semantic cliques. Semantic soft factors were then de<sup>fi</sup>ned according to the semantic cliques. The independent terms (i.e., words and collocations), which are not semantically related to any other term in the vocabulary, are less likely to be able to fully re<sup>fl</sup>ect a certain aspect of semantics. We therefore <sup>fi</sup>ltered out the semantic cliques that contain only a single term. As a result, each extracted semantic clique includes at least two terms.

It is intriguing that some of the extracted semantic cliques express the purpose of the loan, such as {wedding, honeymoon}, which can also be found in the hard factor “purpose.” The consistency between the soft factor freely narrated by the borrower and the hard factor selected from a given drop-down list may re<sup>fl</sup>ect the repayment willingness of the borrower to some extent [17]. Such correspondence between the extracted soft factors and the prede<sup>fi</sup>ned hard factors provides some evidence supporting the e<sup>f</sup>ectiveness of the proposed method.

![](/api/attachments/PVU3FW7F/fulltext/images/654618469296a5351a36a71738445c253f82e429a8a6db25c7c0f6f6709fcb27.jpg)  
Number of extracted semantic soft factors versus semantic similarity threshold.

Figure 3 shows the number of extracted semantic soft factors versus the semantic similarity threshold. It should be noted that an excessively high threshold will bring a universal semantic dissimilarity between terms, whereas an excessively low threshold will lead to a large number of terms with di<sup>f</sup>erent semantics being grouped together in one big clique. We ran a pilot experiment to select an appropriate value for the semantic similarity threshold. Parameter selection is often accomplished using a grid search on discrete sets of parameter values to select the optimal ones with the aid of cross validation (e.g., [15, 32]). Hence, we also used a grid search to select the value of the semantic similarity threshold. Speci<sup>fi</sup>cally, we varied the threshold value from 0.1 to 0.9 in increment of 0.1. Under each threshold value, we trained a random forests model for loan default prediction using the resulting semantic soft factors. We evaluated the performance of the model in terms of the Area Under the Receiver Operating Characteristic Curve (AUC) using ten 10-fold cross validations. The threshold value that gave the best performance was 0.6 (mean AUC was 0.622), leading to 166 semantic soft factors. In the subsequent evaluation, we therefore used these 166 semantic soft factors. Note that we used random forests, an ensemble learning method that can e<sup>f</sup>ectively handle a large number of features and limit over<sup>fi</sup>tting, thus often delivering competitive predictive performance, but other state-of-the-art classi<sup>fi</sup>cation methods could also be used for this purpose.

The extracted semantic cliques are summarized in Appendix B. Some of the cliques consist of many semantically close terms, such as {consolidation, consolidate, debt, card, credit, interest, rate, high, higher, lower, pay, loan, balance}, {job, stable, secure, steady, position, employment, employ}, and {good, borrower, excellent, history, score, rating}. Some other cliques consist of only a few semantically close terms, such as {purchase, buy} and {business, expand, grow}.

## Heterogeneity in Semantic Representation

The essence of the proposed semantic soft factor mining method is to identify di<sup>f</sup>erent patterns of semantic representation by good (non-default) versus bad (default) borrowers, in terms of the distribution of the kinds of semantics expressed in the descriptive loan text. Before evaluating the utility of the extracted semantic soft factors in credit risk evaluation, we <sup>fi</sup>rst tested the di<sup>f</sup>erences between default borrowers and non-default borrowers in their semantic distribution patterns. Speci<sup>fi</sup>cally, we used three statistical tests: T-test, Mann-Whitney test, and Pearson’s Chi-squared test.

With T-test and Mann-Whitney test, we <sup>fi</sup>rst divided each semantic soft factor into two groups, corresponding to default borrowers and non-default borrowers, respectively. Then, we used T-test to examine if there is a signi<sup>fi</sup>cant di<sup>f</sup>erence between the means of the two groups and used Mann-Whitney test to examine whether the two groups of samples are from populations with the same distribution. With Pearson’s Chi-squared test, we <sup>fi</sup>rst dichotomized each semantic soft factors (i.e., zero or nonzero) and then used the response variable (i.e., default or non-default) and the dichotomized semantic soft factor to perform the test.

Figures 4, 5, and 6 show the p-values of the extracted semantic soft factors at the 0.1, 0.5, and 0.01 signi<sup>fi</sup>cance levels for the three tests, respectively. The results show similar patterns across the three tests, indicating that the results are quite robust. A considerable number of semantic soft factors have signi<sup>fi</sup>cantly di<sup>f</sup>erent means (i.e., T-test) and distributions (i.e., Mann-Whitney test) between default and non-default borrowers, showing that there are indeed di<sup>f</sup>erent patterns of semantic representation by default versus non-default borrowers.

![](/api/attachments/PVU3FW7F/fulltext/images/55ffd29f5ec3538db81ace2edfefebce796451cac5f0c2f10b1b900af8e1d84c.jpg)

![](/api/attachments/PVU3FW7F/fulltext/images/945c8c3635a79ab588543b3a8690daa67eb10b12f9fc9b65ab5867d920531460.jpg)

![](/api/attachments/PVU3FW7F/fulltext/images/8f436ca052f5c44886684beeb5b6e3b316864f1cd2726367e312a26c9f7e0fc4.jpg)  
Results of T-Test.

The results of Pearson’s Chi-squared test also show that there is signi<sup>fi</sup>cant heterogeneity in semantic representation between default borrowers and non-default borrowers.

Although some of the extracted semantic soft factors did not show statistical signi<sup>fi</sup>cance in the tests, we should note that they may still have discriminative value for default versus nondefault borrowers. The tests were conducted for each semantic soft factor individually. Some individual factors may be weak, but assembling multiple weak factors may generate stronger discrimination ability, since a complete meaning often needs multiple keywords to convey.

## Evaluation of Semantic Soft Factors

After validating the heterogeneity in semantic representation, we evaluated the utility of the extracted semantic soft factors in credit risk evaluation (speci<sup>fi</sup>cally, loan default prediction). Our goal is to predict, and not to explain [39]. We are more likely to extract potentially e<sup>f</sup>ective (for prediction) soft factors from a data-driven perspective, as Thomas [42, p. 5] pointed out that the philosophy of a credit scoring model “was pragmatic, in that it only wanted to predict not to explain, and so anything that increased the predictive power of the system could be used, provided it was not illegal.” To test whether and how much the extracted semantic soft factors a<sup>f</sup>ect the performance of loan default prediction, we compared three types of feature sets: hard features (attributes 1 to 23 in Table 1), soft features (the 166 semantic soft factors extracted from the loan description), and their combination. We tested both discrimination performance and granting performance.

![](/api/attachments/PVU3FW7F/fulltext/images/690046e72aa4949f93fabaf38787f1404a43ba8ed5555c32141bf0482db765ef.jpg)

![](/api/attachments/PVU3FW7F/fulltext/images/c169d6adc85541ca29b21691fe05b4bb0cf7ab0350e7b0f9dfba1f81ce71afa3.jpg)

![](/api/attachments/PVU3FW7F/fulltext/images/92c4791e54282cc9cbb2b879176ce932d2038860a5975bdc75dbd6e0319c625c.jpg)  
Results of Mann-Whitney Test.

Loan default prediction is generally considered as a classi<sup>fi</sup>cation problem, in which each loan application is classi<sup>fi</sup>ed as default or non-default. We compared both linear models and non-linear models. For linear models, we applied Logistic Regression (LR) and Lasso Regression (LASSO). Logistic regression is one of the most widely-used credit scoring models and is commonly used as a benchmark method for credit risk evaluation. Considering the high dimensionality of the feature space, we also applied Lasso regression to hopefully enhance the predictive performance by performing regularization. Due to the nature of its constraint, Lasso regression enjoys some of the favorable properties of both subset selection and ridge regression, namely, it produces simpler models like subset selection and exhibits the stability of ridge regression [43]. For non-linear models, we applied Random Forests (RF) and eXtreme Gradient Boosting (XGB). Random forests are an e<sup>f</sup>ective and well-established method for generating multiple classi<sup>fi</sup>cation and regression trees based on bagging and random subspace. Extreme gradient boosting is a state-ofthe-art method for tree boosting and has been battle-tested with win in many data science and machine learning challenges. RF and XGB are two representative methods of ensemble learning, which has been shown to have the ability to improve performance over a single learner [16].

![](/api/attachments/PVU3FW7F/fulltext/images/c69e6735365a23f46fcf897ddfdc49061b92717a397ee1de3bb0ca62be9d71b6.jpg)

![](/api/attachments/PVU3FW7F/fulltext/images/875197d6e28b5444d78c5f39e164335256071b180176c75948311351d3caf02b.jpg)

![](/api/attachments/PVU3FW7F/fulltext/images/b5bf175d9d9f08228f44da330b08cad3c47b2cf22120ea03af4063aefafb17fa.jpg)  
Results of Pearson’s Chi-squared test.

Discrimination performance refers to the ability to distinguish bad loans from good loans. While there are several measures for gauging discrimination performance, it has been shown that comprehensively using multiple measures is more reasonable in analyzing discrimination performance [28]. Therefore, besides standard measures, such as AUC and Kolmogorov–Smirnov (KS) statistic, we also computed the H measure proposed by Hand [20], which can avoid the de<sup>fi</sup>ciency of AUC that it uses di<sup>f</sup>erent misclassi<sup>fi</sup>cation cost distributions for di<sup>f</sup>erent classi<sup>fi</sup>ers, by specifying a preset beta distribution for misclassi<sup>fi</sup>cation cost. Typically, the larger the AUC, KS, and H measure, the better the performance of a prediction model. Note that we did not use the standard error rate, as the two classes (i.e., default and non-default) are largely unbalanced and the costs of the two types of errors (i.e., false positive and false negative) are largely asymmetric.

To estimate the discrimination performance (in terms of AUC, KS, and H measure) of each model, we performed 10-fold cross validation ten times, resulting in 100 performance estimates, to get a robust result. Discrimination performance (mean and 95 percent con<sup>fi</sup>dence interval) reported later are all based on the 100 estimates. For a fair comparison between models, the partitioning was kept identical across all models during each 10- fold cross validation.

We also evaluated the granting performance from a practical point of view. In the actual P2P lending market, given the possible risk of losing some or even all the principal due to the default of a borrower, lenders often mitigate their total risk by diversifying their investments across multiple borrowers and investing in a portfolio of multiple loans, rather than a single loan. We simulated real investment scenarios and selected multiple loan applications in our dataset using either the risk ranking results of credit risk evaluation models or the platform-assigned credit sub-grade. We then computed the default rates under di<sup>f</sup>erent granting ratios (i.e., granting performance). For example, assuming we decide to lend money to 10 percent of the loan applications in our dataset, we choose the 10 percent top-ranked loan applications based on the results of credit risk evaluation models and compare the default rate with that when selecting loan applications using the platform-assigned credit sub-grade.

## Results

## Discrimination Performance

Table 2 summarizes the discrimination performance, in terms of AUC, KS, and H measure, respectively, of the four classi<sup>fi</sup>cation methods (LR, LASSO, RF, and XGB), using the three types of feature sets (hard, soft, and their combination). The results across the three performance measures (i.e., AUC, KS, and H Measure) show similar patterns, indicating that the results are quite robust. Overall, the four classi<sup>fi</sup>cation methods (i.e., LR, LASSO, RF, and XGB) provided similar performances. Across the three types of feature sets, hard features signi<sup>fi</sup>cantly outperformed soft features (this is expected), but the combination of hard and soft features always provided the best performance in terms of every performance measure. The results show that although the semantic soft factors alone cannot well identify the credit risk of a borrower, they can be combined with hard information to improve the discrimination performance of loan default prediction models.

Discrimination performance (mean and 95 percent con<sup>fi</sup>dence interval) of loan default <sup>Table 2.</sup>prediction models.

<table><tr><td rowspan="2">Model</td><td rowspan="2">Measure</td><td colspan="3">Features</td></tr><tr><td>Hard</td><td>Soft</td><td>Hard + Soft</td></tr><tr><td rowspan="3">LR</td><td>AUC</td><td>.703(.701-.706)</td><td>.607(.604-.609)</td><td>.714(.712-.717)</td></tr><tr><td>KS</td><td>.304(.299-.308)</td><td>.177(.173-.181)</td><td>.319(.315-.323)</td></tr><tr><td>H Measure</td><td>.139(.136-.142)</td><td>.059(.056-.061)</td><td>.157(.153-.160)</td></tr><tr><td rowspan="3">LASSO</td><td>AUC</td><td>.704(.701-.706)</td><td>.606(.604-.609)</td><td>.715(.713-.718)</td></tr><tr><td>KS</td><td>.303(.299-.307)</td><td>.175(.171-.179)</td><td>.317(.313-.322)</td></tr><tr><td>H Measure</td><td>.140(.137-.142)</td><td>.058(.056-.061)</td><td>.158(.154-.161)</td></tr><tr><td rowspan="3">RF</td><td>AUC</td><td>.708(.706-.710)</td><td>.622(.620-.625)</td><td>.713(.710-.715)</td></tr><tr><td>KS</td><td>.296(.292-.299)</td><td>.181(.177-.185)</td><td>.313(.309-.317)</td></tr><tr><td>H Measure</td><td>.153(.150-.156)</td><td>.088(.086-.091)</td><td>.160(.157-.163)</td></tr><tr><td rowspan="3">XGB</td><td>AUC</td><td>.703(.701-.706)</td><td>.607(.604-.609)</td><td>.714(.711-.716)</td></tr><tr><td>KS</td><td>.296(.292-.300)</td><td>.163(.159-.167)</td><td>.314(.310-.318)</td></tr><tr><td>H Measure</td><td>.140(.137-.143)</td><td>.059(.057-.061)</td><td>.154(.151-.156)</td></tr></table>

The best performance in terms of each performance measure for each method is in boldface.

Results of full pairwise comparison.

<table><tr><td rowspan="2"></td><td rowspan="2">Average Rank</td><td colspan="2">p-value of Pairwise Comparison</td></tr><tr><td>Hard Features</td><td>Soft Features</td></tr><tr><td>Hard Features</td><td>1.89</td><td></td><td></td></tr><tr><td>Soft Features</td><td>3.00</td><td>&lt;.001</td><td></td></tr><tr><td>Hard + Soft</td><td>1.11</td><td>&lt;.001</td><td>&lt;.001</td></tr><tr><td>Friedman  $\chi^{2}$ </td><td>2166.602 (&lt;.001)</td><td></td><td></td></tr></table>

We further tested the statistical signi<sup>fi</sup>cance of the e<sup>f</sup>ect of the soft features on discrimination performance using both a parametric test and a non-parametric test. Table 3 reports the result of a non-parametric full pairwise comparison of the three types of feature sets. Since the Friedman test is a kind of rank sum test, the results across classi<sup>fi</sup>cation models (i.e., LR, LASSO, RF, and XGB) and performance measures (i.e., AUC, KS, and H measure) were put together (i.e., sample size is $1 0 0 \times 4 \times 3 = 1 2 0 0 )$ Overall, the di<sup>f</sup>erences across the three types of feature sets were statistically signi<sup>fi</sup>cant $( \chi ^ { 2 } = ~ 2 1 6 6 . 6 0 2 , \mathrm { p } < . 0 0 1 )$ ). Further pairwise comparisons show that adding the extracted semantic soft factors signi<sup>fi</sup>cantly improved discrimination performance over the hard features $( \mathtt { p } < . 0 0 1$ after Bonferroni correction).

Table 4 reports the result of repeated measure ANOVA with the type of feature set (hard features vs. hard features combined with soft features) as the main factor and the classi<sup>fi</sup>cation method as a between-subject factor. The e<sup>f</sup>ect of the type of feature set on discrimination performance in terms of every performance measure was statistically signi<sup>fi</sup>cant $\left( \mathtt { p } \ < \ . 0 0 1 \right)$ . Post-hoc pairwise comparisons further show that adding the extracted semantic soft factors signi<sup>fi</sup>cantly improved discrimination performance in terms of every performance measure over the hard features $( \mathtt { p } < . 0 0 1$ after Bonferroni correction).

## Comparison with Topic-Related Soft Factors

After con<sup>fi</sup>rming that the extracted soft factors indeed contributed to the improvement of discrimination performance, we further compared the proposed method with a wellknown semantic text analytics method, topic analysis. Topic analysis models are statistical methods for discovering latent semantic structures from an extensive text body [24]. We used a state-of-the-art topic model, Latent Dirichlet Allocation (LDA) [5], to extract topic features from the descriptive loan texts. Each topic feature represented a particular topic expressed in the descriptive loan texts. A parameter that needs to be preset in LDA is the number of topics. We used an inter-topic distance map via multidimensional scaling to select a reasonable number of topics [40]. In order to obtain more topics without overlapping in the inter-topic distance map, we selected the number of topics to be 16, resulting in 16 topic features. Considering the considerable di<sup>f</sup>erence between the selected number of topic features and the number of semantic soft features, we also selected the same number of topic features (i.e., 166 topics) in an additional comparison. We then compared the e<sup>f</sup>ects of the semantic soft features extracted using our proposed method and the topic features extracted using LDA on the discrimination performance of the loan default prediction models.

Results of repeated measure ANOVA.

<table><tr><td>Measure</td><td>F</td><td>p</td><td>Partial η2</td></tr><tr><td>AUC</td><td>794.136</td><td>&lt;.001</td><td>.667</td></tr><tr><td>KS</td><td>437.417</td><td>&lt;.001</td><td>.525</td></tr><tr><td>H Measure</td><td>1036.624</td><td>&lt;.001</td><td>.724</td></tr></table>

Table 5 summarizes the discrimination performance of four classi<sup>fi</sup>cation methods using three types of feature sets, namely, hard features combined with 16 topic features, hard features combined with 166 topic features, and hard features combined with the extracted semantic soft features. The results show that the topic features also contributed to performance improvement over the hard features, but the semantic soft features extracted using our proposed method led to bigger improvement. The di<sup>f</sup>erence between hard features combined with semantic soft features and hard features combined with either 16 or 166 topic features was statistically signi<sup>fi</sup>cant (p < .001) under a non-parametric test (i.e., related-sample Wilcoxon signed-rank test) assembling the results across classi<sup>fi</sup>cation models (i.e., LR, LASSO, RF, and XGB) and performance measures (i.e., AUC, KS, and H measure).

## Comparison with Linguistic and Stylistic Soft Factors

In addition to topic-related soft factors, we also compared the extracted semantic soft factors with linguistic and stylistic soft factors. We measured linguistic and stylistic soft factors using three types of features, including statistics features, readability features, and sentiment features. For statistics features, we calculated the number of sentences, the number of words, the number of unique words, and the number of characters. For readability features, we calculated <sup>fi</sup>ve readability indexes, including Automated Readability Index [38], Bormuth’s [6] Mean Cloze Formula and Grade Placement Score, and Coleman’s [10] Readability Formula 1 and Formula 2. For sentiment features, we used the sentiment analysis toolkit “SentiStrength” (http://sentistrength.wlv.ac.uk/) to estimate the strengths of positive sentiment and negative sentiment. Speci<sup>fi</sup>cally, we calculated positive and negative sentiment strengths using average, strongest, and total of sentiment words, respectively, forming six sentiment scores.

Comparison between semantic soft factors and topic factors.

<table><tr><td rowspan="2">Model</td><td rowspan="2">Measure</td><td colspan="3">Features</td></tr><tr><td>Hard+ Topic (16)</td><td>Hard + Topic (166)</td><td>Hard + Semantic</td></tr><tr><td rowspan="3">LR</td><td>AUC</td><td>.709(.706-.711)</td><td>.710(.707-.712)</td><td>.714(.712-.717)</td></tr><tr><td>KS</td><td>.313(.309-.317)</td><td>.317(.313-.321)</td><td>.319(.315-.323)</td></tr><tr><td>H Measure</td><td>.147(.144-.150)</td><td>.149(.146-.152)</td><td>.157(.153-.160)</td></tr><tr><td rowspan="3">LASSO</td><td>AUC</td><td>.709(.707-.711)</td><td>.713(.710-.715)</td><td>.715(.713-.718)</td></tr><tr><td>KS</td><td>.312(.308-.317)</td><td>.317(.312-.321)</td><td>.317(.313-.322)</td></tr><tr><td>H Measure</td><td>.147(.144-.150)</td><td>.152(.149-.155)</td><td>.158(.154-.161)</td></tr><tr><td rowspan="3">RF</td><td>AUC</td><td>.711(.709-.713)</td><td>.712(.710-.714)</td><td>.713(.710-.715)</td></tr><tr><td>KS</td><td>.306(.302-.309)</td><td>.310(.306-.313)</td><td>.313(.309-.317)</td></tr><tr><td>H Measure</td><td>.154(.151-.157)</td><td>.158(.155-.161)</td><td>.160(.157-.163)</td></tr><tr><td rowspan="3">XGB</td><td>AUC</td><td>.703(.700-.705)</td><td>.702(.700-.704)</td><td>.714(.711-.716)</td></tr><tr><td>KS</td><td>.297(.293-.301)</td><td>.297(.293-.301)</td><td>.314(.310-.318)</td></tr><tr><td>H Measure</td><td>.139(.136-.142)</td><td>.138(.135-.141)</td><td>.154(.151-.156)</td></tr></table>

The best performance in terms of each performance measure for each method is in boldface.

Comparison between semantic soft factors and linguistic and stylistic factors.

<table><tr><td>Features*</td><td>Measure</td><td>LR</td><td>LASSO</td><td>RF</td><td>XGB</td></tr><tr><td>H</td><td>AUC</td><td>.703(.701-.706)</td><td>.704(.701-.706)</td><td>.708(.706-.710)</td><td>.703(.701-.706)</td></tr><tr><td>H + A</td><td></td><td>.705(.702-.707)</td><td>.704(.702-.707)</td><td>.704(.702-.706)</td><td>.703(.701-.705)</td></tr><tr><td>H + B</td><td></td><td>.704(.701-.706)</td><td>.704(.702-.706)</td><td>.704(.702-.706)</td><td>.703(.701-.705)</td></tr><tr><td>H + C</td><td></td><td>.704(.702-.707)</td><td>.704(.701-.706)</td><td>.705(.703-.707)</td><td>.704(.702-.706)</td></tr><tr><td>H + D</td><td></td><td>.714(.712-.717)</td><td>.715(.713-.718)</td><td>.713(.710-.715)</td><td>.714(.711-.716)</td></tr><tr><td>H + A+B</td><td></td><td>.705(.703-.707)</td><td>.705(.702-.707)</td><td>.701(.699-.703)</td><td>.702(.700-.705)</td></tr><tr><td>H + A+B+C</td><td></td><td>.705(.703-.707)</td><td>.705(.702-.707)</td><td>.701(.699-.703)</td><td>.703(.701-.705)</td></tr><tr><td>H + A+B+C+D</td><td></td><td>.715(.713-.718)</td><td>.717(.714-.719)</td><td>.711(.709-.713)</td><td>.714(.711-.716)</td></tr><tr><td>H</td><td>KS</td><td>.304(.299-.308)</td><td>.303(.299-.307)</td><td>.296(.292-.299)</td><td>.296(.292-.300)</td></tr><tr><td>H + A</td><td></td><td>.305(.301-.309)</td><td>.305(.301-.309)</td><td>.292(.288-.296)</td><td>.300(.296-.304)</td></tr><tr><td>H + B</td><td></td><td>.304(.300-.308)</td><td>.303(.299-.307)</td><td>.297(.293-.301)</td><td>.298(.294-.302)</td></tr><tr><td>H + C</td><td></td><td>.306(.302-.310)</td><td>.304(.300-.308)</td><td>.292(.288-.296)</td><td>.300(.296-.304)</td></tr><tr><td>H + D</td><td></td><td>.319(.315-.323)</td><td>.317(.313-.322)</td><td>.313(.309-.317)</td><td>.314(.310-.318)</td></tr><tr><td>H + A+B</td><td></td><td>.306(.302-.309)</td><td>.305(.301-.309)</td><td>.293(.289-.296)</td><td>.298(.294-.302)</td></tr><tr><td>H + A+B+C</td><td></td><td>.306(.302-.310)</td><td>.304(.300-.308)</td><td>.293(.290-.297)</td><td>.299(.295-.303)</td></tr><tr><td>H + A+B+C+D</td><td></td><td>.322(.318-.326)</td><td>.320(.316-.324)</td><td>.309(.305-.313)</td><td>.315(.311-.319)</td></tr><tr><td>H</td><td>H Measure</td><td>.139(.136-.142)</td><td>.140(.137-.142)</td><td>.153(.150-.156)</td><td>.140(.137-.143)</td></tr><tr><td>H + A</td><td></td><td>.141(.138-.144)</td><td>.140(.137-.143)</td><td>.147(.144-.150)</td><td>.139(.136-.141)</td></tr><tr><td>H + B</td><td></td><td>.140(.137-.143)</td><td>.140(.137-.143)</td><td>.146(.144-.149)</td><td>.139(.136-.142)</td></tr><tr><td>H + C</td><td></td><td>.140(.137-.143)</td><td>.139(.137-.142)</td><td>.148(.145-.151)</td><td>.139(.137-.142)</td></tr><tr><td>H + D</td><td></td><td>.157(.153-.160)</td><td>.158(.154-.161)</td><td>.160(.157-.163)</td><td>.154(.151-.156)</td></tr><tr><td>H + A+B</td><td></td><td>.141(.138-.144)</td><td>.141(.138-.144)</td><td>.142(.139-.145)</td><td>.137(.134-.140)</td></tr><tr><td>H + A+B+C</td><td></td><td>.141(.138-.144)</td><td>.141(.138-.144)</td><td>.141(.138-.144)</td><td>.138(.136-.141)</td></tr><tr><td>H + A+B+C+D</td><td></td><td>.158(.154-.161)</td><td>.159(.156-.162)</td><td>.157(.154-.160)</td><td>.153(.150-.156)</td></tr></table>

H,Hard Features; A, Statistics Features; B, Readability Features; C, Sentiment Features; D, Semantic Features. The best performance in terms of each performance measure for each method is in boldface.

Table 6 summarizes the discrimination performance of four classi<sup>fi</sup>cation methods using eight types of feature sets. The results show that the enhanced e<sup>f</sup>ect of combining linguistic and stylistic soft factors and hard features varied across models. The linear models (i.e., LR and LASSO) bene<sup>fi</sup>ted more than the nonlinear models (i.e., RF and XGB). For all linear models, models using hard features combined with any of statistics features, readability features, and sentiment features outperformed models using hard features only, and models using hard features combined with all the soft features always gave the best performance in terms of every performance measure. Across the four types of soft features (i.e., semantic features, statistics features, readability features, and sentiment features), the semantic soft features extracted using our proposed method led to the most improvement.

## Granting Performance

The granting performance was measured using the default rate in the portfolio of loans selected under a certain granting proportion. The platform-assigned credit sub-grade, as a comprehensive evaluation of the platform on borrowers, is usually used by lenders as a major criterion to decide whether to lend or not. Thus, credit sub-grade was selected as a reference line to compare with credit risk evaluation models built on top of hard features and the combination of hard and soft features. As a result, three strategies were used to select portfolios under di<sup>f</sup>erent granting proportions: (1) selecting loans with high platform-assigned credit sub-grade; (2) selecting loans with low probability of default according to the credit risk evaluation models using hard features; (3) selecting loans with low probability of default according to the credit risk evaluation models using both hard features and extracted semantic soft features.

Figure 7 visualizes the granting performance of the three strategies. The horizontal axis represents the 35 levels of cumulative granting proportion corresponding to the platformassigned credit sub-grade. There are 7 grades (i.e., A, B, C, D, E, F, and G) and each grade has 5 sub-grades (i.e., totally 35 sub-grades from A1 to G5). In other words, the <sup>fi</sup>rst granting proportion equals the proportion of A1, the second granting proportion equals the cumulative proportion of A2 (i.e., the sum of the proportions of A1 and A2), and the last $( \mathrm { i } . \mathrm { e } . , 3 5 ^ { \mathrm { t h } } )$ granting proportion covers all sub-grades and is therefore 100 percent. The probability of default of a loan application predicted by a model was estimated through a 10-fold cross validation. The performance curves of the four classi<sup>fi</sup>cation methods show similar trends, indicating that the results are quite robust. With any of the four classi<sup>fi</sup>cation methods, modeling using hard features to scan loan applications produced a lower default rate than just relying on the platform-assigned credit sub-grade. This is not surprising since platform-assigned credit sub-grade was included as a hard feature in the classi<sup>fi</sup>cation models and the <sup>fi</sup>rst strategy only served as a baseline. When the extracted semantic soft features were added into modeling, the default rate in the selected portfolio further went down signi<sup>fi</sup>cantly, re<sup>fl</sup>ecting a signi<sup>fi</sup>cant improvement on granting performance. All the curves eventually approached the same point, since the last granting proportion is equivalent to lending money to all the loan applications in the dataset (in this case, the default rate is equal to the overall default rate of the dataset). The results show that the extracted semantic soft features were able to signi<sup>fi</sup>cantly improve the riskranking ability of credit risk evaluation models for selecting a loan portfolio with low default rate.

(a) Logistic Regression  
![](/api/attachments/PVU3FW7F/fulltext/images/2b81ce90ffe67c1d7d40acfcd1aff680b9af7161d3438928c9979edf5c8b9231.jpg)  
(c) Random Forests

(b) Lasso Regression  
![](/api/attachments/PVU3FW7F/fulltext/images/b733bae77cc07851a20f36814eb4a6dc7468ca8af0f2fb64c1873e39e02078a5.jpg)  
(d) eXtreme Gradient Boosting

![](/api/attachments/PVU3FW7F/fulltext/images/ec0508932411a9adaf743a00fa06a32ba1c8f75021add184790dcbf31b140df4.jpg)  
Granting performance of three strategies.

![](/api/attachments/PVU3FW7F/fulltext/images/35da20448ddab8d080b406434f3e6a2faf577a7b7e6d9ab3036a3a6fe41c25a7.jpg)

## Conclusion

Along with its advantage of low cost for borrowers and high return for lenders, P2P lending also faces the problem of high credit risk due to information asymmetry. Soft information that re<sup>fl</sup>ects a borrower’s individual situation therefore also enters into the process of credit risk evaluation in P2P lending. In this paper, we identi<sup>fi</sup>ed the challenges in extracting semantic soft factors from descriptive loan texts for credit risk evaluation in P2P lending. To address the challenges, we proposed a text mining method for automatically extracting semantic soft factors from descriptive loan texts. We evaluated our method on a major P2P lending marketplace using a large dataset, in terms of both discrimination performance and granting performance. The results show that the extracted soft factors signi<sup>fi</sup>cantly improved the performance of credit risk evaluation models. Our analysis provided evidence for the existence of di<sup>f</sup>erences between default borrowers and non-default borrowers in terms of the distribution of the kinds of semantics expressed in their loan descriptions. This work advances our knowledge of soft information indicative of a borrower’s credit risk.

Our work contributes to both research and practice. From the research perspective, <sup>fi</sup>rst, the proposed method is quite general and can also be used in other <sup>fi</sup>nancial service scenarios, such as bank loans, to exploit useful information hidden in texts, and may even be extended into other text mining applications. Second, as our empirical evaluation demonstrates the usefulness of the semantic soft factors extracted by our proposed method in credit risk evaluation, this broadens the well-established soft factors and bene<sup>fi</sup>ts the research dedicated to soft information for credit scoring [23, 24]. Third, our proposed method also has methodological implications. The word embedding model based on global log-bilinear regression is <sup>fi</sup>rst introduced into the credit risk evaluation domain, and we have shown that it is useful in capturing semantic relationships among terms in descriptive loan texts. In addition, it is also enlightening that integrating multiple co-occurrence based statistics is indeed useful for identifying collocations in descriptive loan texts.

From the practical perspective, P2P lending institutions and lenders may also show interest in our proposed method. For P2P lending institutions, obtaining a semantic representation of descriptive loan texts can help them provide more intuitive and useful information for lenders, as well as better verifying borrowers. For lenders, the access to semantic soft factors can help them mitigate the information asymmetry, thus allowing them to make better granting decisions not only on a single loan application but also on selecting a loan portfolio.

This work has several limitations, which may be addressed in future research. First, as discussed earlier, the preset parameter in our method, the semantic similarity threshold, determines whether two terms are deemed semantically close. We used a grid search to select an appropriate value for this parameter in our empirical evaluation. Future research may further explore how to choose an optimal threshold. Second, we only evaluated our proposed method on one dataset. More comprehensive evaluation involving multiple institutions and perhaps even multiple <sup>fi</sup>nancial service scenarios (e.g., bank loans) may be conducted to test the generalizability of our <sup>fi</sup>ndings. Third, as grammatical and syntactical rules may vary across languages, our method may also be tested in contexts using other languages, e.g., Chinese P2P lending platforms. Fourth, for the extreme cases of fraud where borrowers write deceiving contents, the proposed method may lose some e<sup>f</sup>ectiveness. Future research may consider introducing fraud detection methods, such as that presented in Carneiro et al. [8], to further improve the predictive performance.

## Notes

1. http://text2vec.org/index.html

## Funding

This work was funded by the National Natural Science Foundation of China (Grant Nos. 71731005, 71571059) and the Humanities and Social Science Planning Foundation of Ministry of Education of China (Grant No. 15YJA630010).

## References

1. Abellán, J.; and Castellano, J.G. A comparative study on base classi<sup>fi</sup>ers in ensemble methods for credit scoring. Expert Systems with Applications, 73, (May 2017), 1–10.

2. Abu-Errub, A. Arabic text classi<sup>fi</sup>cation algorithm using TFIDF and chi square measurements. International Journal of Computer Applications, 93, 6 (May 2014), 40–45.

3. Baesens, B.; Van Gestel, T.; Viaene, S.; Stepanova, M.; Suykens, J.; and Vanthienen, J. Benchmarking state-of-the-art classi<sup>fi</sup>cation algorithms for credit scoring. Journal of the Operational Research Society, 54, 6 (June 2003), 627–635.

4. Bertomeu, J.; and Marinovic, I. A Theory of hard and soft information. The Accounting Review, 91, 1 (January 2016), 1–20.

5. Blei, D.M.; Ng, A.Y.; and Jordan, M.I. Latent Dirichlet allocation. Journal of Machine Learning Research, 3, (January 2003), 993–1022.

6. Bormuth, J.R. Development of Readability Analysis. Final Report, Project No. 7-0052, The University of Chicago, Chicago, Illinois, 1969.

7. Bouma, G. Normalized (pointwise) mutual information in collocation extraction. In Proceedings of German Society for Computational Linguistics, Potsdam, German. 2009, pp. 31-40.

8. Carneiro, N.; Figueira, G.; and Costa, M. A data mining based system for credit-card fraud detection in e-tail. Decision Support Systems, 95, (March 2017), 91–101.

9. Ciresan, D.C., Giusti, A., Gambardella, L.M., and Schmidhuber, J. Deep neural networks segment neuronal membranes in electron microscopy images. In Proceedings of Advances in Neural Information Processing Systems, Lake Tahoe, Nevada, United States. 2012, pp. 2843- 2851.

10. Coleman, E.B. Developing a technology of written instruction: Some determiners of the complexity of prose. In Ernst Z. Rothkopf and Paul E. Johnson (Eds.), Verbal Learning Research and the Technology of Written Instruction. 1971, pp. 155-204. New York, United States: Teachers College Press.

11. Devi, C.R.D.; and Chezian, R.M. A relative evaluation of the performance of ensemble learning in credit scoring. In Proceedings of the 2016 IEEE International Conference on Advances in Computer Applications, Coimbatore, India. 2016, pp. 161–165.

12. Dor<sup>fl</sup>eitner, G.; Priberny, C.; Schuster, S.; Stoiber, J.; Weber, M.; de Castro, I.; and Kammler, J. Description-text related soft information in peer-to-peer lending – Evidence from two leading European platforms. Journal of Banking & Finance, 64, (March 2016), 169–187.

13. Dumais, S.T. Latent semantic analysis. Annual Review of Information Science and Technology, 38, 1 (September 2005), 188–230.

14. Emekter, R.; Tu, Y.; Jirasakuldech, B.; and Lu, M. Evaluating credit risk and loan performance in online Peer-to-Peer (P2P) lending. Applied Economics, 47, 1 (January 2015), 54–70.

15. Fayed, H.A.; and Atiya, A.F. Speed up grid-search for parameter selection of support vector machines. Applied Soft Computing, 80, (July 2019), 202–210.

16. Finlay, S. Multiple classi<sup>fi</sup>er architectures and their application to credit risk assessment. European Journal of Operational Research, 210, 2 (April 2011), 368–378.

17. Gao, Q.; Lin, M.; and Sias, R.W. Words matter: The role of texts in online credit markets (September 24, 2018). Available at SSRN: http://dx.doi.org/10.2139/ssrn.2446114.

18. Ge, R.; Feng, J.; Gu, B.; and Zhang, P. Predicting and deterring default with social media information in peer-to-peer lending. Journal of Management Information Systems, 34, 2 (April 2017), 401–424.

19. Guo, Y., Zhou, W., Luo, C., Liu, C., and Xiong, H. Instance-based credit risk assessment for investment decisions in P2P lending. European Journal of Operational Research, 249, 2 (March 2016), 417–426.

20. Hand, D.J. Measuring classi<sup>fi</sup>er performance: A coherent alternative to the area under the ROC curve. Machine Learning, 77, 1 (October 2009), 103–123.

21. Harris, T. Quantitative credit risk assessment using support vector machines: Broad versus Narrow default de<sup>fi</sup>nitions. Expert Systems with Applications, 40, 11 (September 2013), 4404–4413.

22. Hore, C.; Asahara, M.; and Matsumoto, Y. Automatic extraction of <sup>fi</sup>xed multiword expressions. In Proceedings of the International Conference on Natural Language Processing. 2005, pp. 565-575.

23. Iyer, R.; Khwaja, A.I.; Luttmer, E.F.P.; and Shue, K. Screening peers softly: Inferring the quality of small borrowers. Management Science, 62, 6 (June 2016), 1554–1577.

24. Jiang, C., Wang, Z., Wang, R., and Ding, Y. Loan default prediction by combining soft information extracted from descriptive text in online peer-to-peer lending. Annals of Operations Research, 266, 1–2 (July 2018), 511–529.

25. Jiang, Y.; (Chad) Ho, Y.-C.; Yan, X.; and Tan, Y. Investor platform choice: Herding, platform attributes, and regulations. Journal of Management Information Systems, 35, 1 (January 2018), 86–116.

26. Kiruthika; and Dilsha, M. A neural network approach for micro<sup>fi</sup>nance credit scoring. Journal of Statistics and Management Systems, 18, 1–2 (March 2015), 121–138.

27. Larrimore, L.; Jiang, L.; Larrimore, J.; Markowitz, D.; and Gorski, S. Peer to peer lending: The relationship between language features, trustworthiness, and persuasion success. Journal of Applied Communication Research, 39, 1 (February 2011), 19–37.

28. Lessmann, S.; Baesens, B.; Seow, H.-V.; and Thomas, L.C. Benchmarking state-of-the-art classi<sup>fi</sup>cation algorithms for credit scoring: An update of research. European Journal of Operational Research, 247, 1 (November 2015), 124–136.

29. Liberti, J.M.; and Petersen, M.A. Information: Hard and soft. The Review of Corporate Finance Studies, 8, 1 (March 2019), 1–41.

30. Lin, M.; Prabhala, N.R.; and Viswanathan, S. Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. Management Science, 59, 1 (January 2013), 17–35.

31. Manning, C.; Surdeanu, M.; Bauer, J.; Finkel, J.; Bethard, S.; and McClosky, D. The Stanford CoreNLP Natural Language Processing Toolkit. In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations, Baltimore, Maryland, United States. 2014, pp. 55–60.

32. Martens, D.; Provost, F.; Clark, J.; and Junqué de Fortuny, E. Mining massive <sup>fi</sup>ne-grained behavior data to improve predictive analytics. MIS Quarterly, 40, 4 (April 2016), 869–888.

33. Mikolov, T.; Sutskever, I.; Chen, K.; Corrado, G.; and Dean, J. Distributed representations ofwords and phrases and their compositionality. In Proceedings of Advances in Neural Information Processing Systems, Lake Tahoe, Nevada, United States. 2013, pp. 3111-3119.

34. Mikolov, T.; Yih, W.T.; and Zweig, G. Linguistic regularities in continuous spaceword representations. In Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Atlanta, Georgia, United States. 2013, pp. 746–751.

35. Oreski, S.; Oreski, D.; and Oreski, G. Hybrid system with genetic algorithm and arti<sup>fi</sup>cial neural networks and its application to retail credit risk assessment. Expert Systems with Applications, 39, 16 (November 2012), 12605–12617.

36. Pennington, J.; Socher, R.; and Manning, C. Glove: Global Vectors for word representation. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, Doha, Qatar. 2014, pp. 1532–1543.

37. Pötzsch, S.; and Böhme, R. The role of soft information in trust building: Evidence from online social lending. In Proceedings of the International Conference on Trust and Trustworthy Computing, Berlin, Germany. 2010, pp. 381-395.

38. Senter, R.J.; and Smith, E.A. Automated Readability Index. Technical Report AMRL-TR-66- 220, University of Cincinnati, Cincinnati, Ohio, 1967.

39. Shmueli, G. To explain or to predict? Statistical Science, 25, 3 (August 2010), 289–310.

40. Sievert, C.; and Shirley, K. LDAvis: A method for visualizing and interpreting topics. In Proceedings of the Workshop on Interactive Language Learning, Visualization, and Interfaces, Baltimore, Maryland, United States. 2014, pp. 63-70.

41. Stepanova, M.; and Thomas, L. Survival analysis methods for personal loan data. Operations Research, 50, 2 (April 2002), 277–289.

42. Thomas, Lyn C. Consumer Credit Models: Pricing, Profit and portfolios: Pricing, Profit and Portfolios. New York, United States: Oxford University Press, 2009.

43. Tibshirani, R. Regression shrinkage and selection via the lasso: A retrospective. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 73, 3 (June 2011), 273–282.

44. Tong, E.N.C.; Mues, C.; and Thomas, L.C. Mixture cure models in credit scoring: If and when borrowers default. European Journal of Operational Research, 218, 1 (April 2012), 132–139.

45. Wang, G.; Ma, J.; Huang, L.; and Xu, K. Two credit scoring models based on dual strategy ensemble trees. Knowledge-Based Systems, 26, (February 2012), 61–68.

46. Wang, S.; Qi, Y.; Fu, B.; and Liu, H. Credit risk evaluation based on text analysis. International Journal of Cognitive Informatics and Natural Intelligence, 10, 1 (January 2016), 1–11.

47. Wei, Z.; and Lin, M. Market mechanisms in online peer-to-peer lending. Management Science, 63, 12 (December 2017), 4236–4257.

48. Yao, X.; Crook, J.; and Andreeva, G. Support vector regression for loss given default modelling. European Journal of Operational Research, 240, 2 (January 2015), 528–538.

49. Zhang, D.; Leung, S.C.H.; and Ye, Z. A decision tree scoring model based on genetic algorithm and K-means algorithm. In Proceedings of the Third International Conference on Convergence and Hybrid Information Technology, Busan, South Korea, 2008, pp. 1043–1047.

## About the Authors

(xcwangzhao@163.com) is an Assistant Professor at the School of Management, Hefei <sup>Zhao Wang</sup>University of Technology. He received his PhD degree in management science and engineering from that university. His research interests include data mining, and credit evaluation theory and methodology. He has published in such journals as European Journal of Operational Research, Annals of Operations Research, Electronic Commerce Research and Applications, and many others.

(jiangcuiq@163.com, jiangcuiq2017@163.com; corresponding author) is a Professor <sup>Cuiqing Jiang</sup>at the School of Management, Hefei University of Technology. He received his PhD degree in management science and engineering from that University. His research interests include big data analytics and business intelligence, data mining and knowledge discovery, <sup>fi</sup>nancial technology (Fintech) and information systems. He has published in such journals as European Journal of

Operational Research, Information Sciences, Decision Support Systems, International Journal of Production Research, and many others.

(hzhao@uwm.edu) is a Professor of Information Technology Management at the <sup>Huimin Zhao</sup>Lubar School of Business, University of Wisconsin-Milwaukee. He received his Ph.D. degree in Management Information Systems from the University of Arizona. His research interests include data mining and healthcare informatics. He has published in such journals as MIS Quarterly, Journal of Management Information Systems, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, and many others. He serves in the editorial positions at several major scholarly journals.

(dingyong@hfut.edu.cn) is an Associate Professor at the School of Management, Hefei <sup>Yong Ding</sup>University of Technology, China. He received his Ph.D. degree from that university. Dr. Ding’s research interests include decision-making theory and methodology, project management, and knowledge management.
