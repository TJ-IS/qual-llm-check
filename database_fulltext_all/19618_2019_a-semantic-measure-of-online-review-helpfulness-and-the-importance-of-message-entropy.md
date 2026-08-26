---
otero_id: 19618
otero_key: "QH2MBWVR"
title: "A semantic measure of online review helpfulness and the importance of message entropy"
authors: "Jorge E. Fresneda; David Gefen"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113117"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A semantic measure of online review helpfulness and the importance of message entropy

![](/api/attachments/QH2MBWVR/fulltext/images/7e15ab7e67bb876869e23d7a7ac6a557d4be9a6249df76c1a5ed5e64846cc527.jpg)

Jorge E. Fresneda<sup>a,⁎</sup>, David Gefen<sup>b</sup>

<sup>a</sup> Martin Tuchman School of Management, New Jersey Institute of Technology, 184 Central Avenue, Newark, NJ 07102, United States of America <sup>b</sup> LeBow College of Business, Drexel University, 3220 Market Street, Philadelphia, PA 19104, United States of America

## A R T I C L E I N F O

Keywords: Online consumer reviews Ecommerce Review helpfulness Latent semantic analysis Information entropy increment

## A B S T R A C T

The helpfulness of online reviews and their impact on purchase decisions is well established. Much previous research measured that helpfulness by analyzing vote assessments. This study examines an alternative semantic measure based on a text analysis of the term “helpful" in those reviews. Analyzing over 20.000 reviews shows that the semantic measure has a considerably higher R<sup>2</sup> than vote assessments. Moreover, the new measure, as opposed to those based on votes, is not afected by posting order, avoiding a known source of bias in vote measures, and is conceptually unrelated to the number of previous helpfulness evaluations. The study also examines the role of the incremental entropy of each review's content as a new determinant of both the existing measures and the new semantic measure of online review helpfulness. The potential of the semantic measure, including that it can be automatically calculated even before human review users read the review, is discussed.

## 1. Introduction

Online consumer reviews are an increasingly important source of information in online purchase decisions, complementing and sometimes substituting for other forms of business-to-consumer and consumer-to-consumer information [15,32]. Online reviews provide information based on the posted personal experience of previous buyers of a specific product working as free “sales assistants” to help other consumers identify the product that best matches their needs and tastes [13]. The development of websites whose primary focus is to provide purchase information through consumer reviews e.g. Consumerafairs.com or Angieslist.com – exemplifies their growing popularity as relevant product information providers [3]. Indeed, a 2012 survey conducted by Nielsen among 28,000 Internet users from 56 countries reported that 70% of respondents considered online consumer reviews a trustworthy source of information, ranking them as the second most trusted form of advertising among 19 diferent choices [59]. Online product reviews impact sales [15,16,23,47,82], especially helpful reviews [12].

The evaluation of a review's helpfulness by potential buyers is among the most relevant tools to assess the quality of the information provided [56]. The literature has extensively analyzed factors that in crease review helpfulness. These factors can be roughly classified into review-related factors [e.g. 48,56,61,71] and reviewer-related factors [e.g. 14,71,83]. However, the suitability of helpfulness ratings measures in assessing the actual quality of the information provided in the reviews has been brought into question [11,75] and the operationalization of the variable ‘review helpfulness’ has also raised concerns [34], including that the posting order of the review may cause unwanted biases [80]. Moreover, the definition of what makes an online review helpful as applied in current research is inherently subjective and therefore ambiguous because it depends on the evaluation of human readers who are unlikely to all apply the same criteria. Moreover, many online reviews may not have been assessed by other readers by the time an interested person reads them. An automated measure, especially one that addresses those limitations, while also considering the actual information content of the review. is needed.

Addressing that need, this study (1) proposes a new measure of the review helpfulness construct that is based on a Latent Semantic Analysis (LSA) of its text. This focus on content as revealed through semantics contrasts with current measures that are based on counting vote-up/ vote-down human rater assessments of how helpful a review is. The method proposed in this paper avoids the imbalanced vote bias and the posting order influence associated with counting vote-up/vote-down evaluations according to Liu et al. [46] (see section 2.2). Posting order is at the core of other sources of bias, such as the early bird bias and, to a large extent, the winner cycle bias. (2) Focusing on the actual information content of the review without the need for a human rater, the study also proposes a new measure of information entropy increment. This measure accounts to some extent for the newness of the information in the review compared to previous reviews. (3) Showing the validity of the semantic measure of helpfulness and of the entropy in crement measure, this study analyzes 20,722 online reviews about appliances at Amazon.com. The semantic measure of helpfulness was afected, as expected, by sentiment but not by posting order, and showed markedly higher R<sup>2</sup> than the two popular vote-up/vote-down counting measures when the number of previous votes is excluded, which is a known source of bias in the literature, e.g. Cao, Duan and Gan [11].<sup>1</sup> In contrast, the vote-up/vote-down measures were not affected by sentiment but were afected by posting order. Information entropy increment contributed significantly to the new and to the voteup/vote-down measures of helpfulness. Other previously identified determinants of review helpfulness were also significant: total number of words, number of evaluations, and number of stars.

Putting this new measure of semantic helpfulness into context, past research into what makes online consumer reviews helpful concentrated on easily accessible numeric characteristics, such as the number of stars and the number of words included in the textual portion [e.g. 56, 61]. The textual part of consumer reviews has been mostly ignored, possibly because of a lack of appropriate methodologies [15]. Semantic helpfulness and information entropy increment provide new theoretical and applied lenses through which online reviews can be assessed and planned. Additionally, further putting this new measure into context, by no means is the semantic helpfulness approach we are suggesting the only one possible. Rather, our claim is that this method is a simple machine-learning enabled data content measure that can avoid known biases.

The remainder of this paper is organized as follows. The second section presents the theoretical background, leading to the research hypotheses. The third section introduces the conceptual model. The fourth section explains the methodology. The fifth section is the data analysis. Finally, the sixth section discusses the findings, limitations, and avenues for future research.

## 2. Theoretical development

## 2.1. The context. Electronic word-of-mouth and review helpfulness

Online consumer reviews are a form of word-of-mouth (WOM). WOM is a term that includes diferent types of informal communications among consumers about products, services, or companies [47,63] and is a source of purchasing information that influences potential customers' behavior [10,53]. It is often considered by consumers to be a reliable and valid source of information that can reduce purchase risks [8,30,50]. Possibly, this is because of its non-commercial nature and because consumers generally trust other peer consumers more than they trust marketers or advertisers [7,67]. The electronic counterpart of WOM (e-WOM) is defined as “any positive or negative statement made by potential, actual or former consumers about a product or company, which is made available to a multitude of people and institutions via the Internet” [33]. Typically, e-WOM interactions take place among people who have no previous connection or relationship, which constitutes a major diference compared to traditional WOM [19]. E-WOM includes a broad range of mediums beyond online reviews, including blogs, social networking sites, online forums, and electronic bulletin boards [23].

Although there is no standard e-WOM structure, online consumer reviews usually include several informational elements. These element comprise: (1) review valence (frequently referred to as ‘number of stars’); (2) review text (where reviewers provide further qualitative information); and (3) an overall helpfulness score of the review. The helpfulness score is based on ratings provided by people who read the review, not the person who posted it and is calculated from the number of vote-up/vote-down clicks made by people who read the review. The literature suggests that helpfulness ratings can impact sales [12,13,29], presumably by certifying the value of the information in the review [28].

As a prominent example of the relevance of the helpfulness ratings, Spool [73] estimated that Amazon.com added \$2.7 billion to its annual revenue by requesting that potential customers assess the perceived helpfulness of online reviews, and making the most ‘helpful’ reviews more visible to potential customers. Helpfulness ratings may also enable consumers to filter the overwhelming amount of information available on popular ecommerce sites, reducing information overload [11]. The availability of product reviews may also increase the time that potential buyers spend on a particular website, increasing its “stickiness” [56]. Review helpfulness is “the extent to which consumers perceive the product review as being capable of facilitating judgment or purchase decisions” [45,p.,103], i.e. a review is ‘helpful’ if it provides potential buyers with new information that informs their purchasing decision.

## 2.2. Problems with the current measures of review helpfulness

As described above, the helpfulness score is based on ratings provided by people who read the review, not the person who posted it. Current literature operationalizes review helpfulness either as the ratio of thumb-up to total votes (henceforth, helpfulness vote ratio) or as the total number of thumb-up helpful votes (henceforth, helpfulness thumb-up votes). Hong et al. [34] suggest that the choice between these two operationalization approaches of review helpfulness results in conflicting findings on the impact of the same antecedents.

Not only does review helpfulness have two diferent operationalizations, but the assessments of helpfulness by users on which both definitions are based might themselves be biased [46]. Liu et al. [46] identified three types of biases in the evaluation of review help fulness: imbalanced vote bias, winner cycle bias, and early bird bias. The imbalanced vote bias occurs because Internet users tend to rate others' opinions positively rather than negatively. The winner cycle bias states that reviews awarded high helpfulness votes will continue to attract more votes because the reviews that are top ranked are more easily accessible to users. The early bird bias is that the earlier a review is posted, the more votes it will receive. These biases might result in early reviews being more accessible and receiving more positive help fulness votes [58]. Additionally, the algorithm employed by Amazon. com to rank the most helpful reviews is based on the aggregated number of evaluations that the reviews received. This feature has an “anchoring efect,” leading to more helpful reviews receiving more votes, since they are made more salient for potential buyers [11,75]. This study specifically addresses the impact of posting order by suggesting a new approach that is not afected by this variable.

## 2.3. An alternative measure of review helpfulness based on semantics

Acknowledging the limitations of the vote-up/vote-down based measures, the primary objective of this study is to propose an alternative measure that is based on the semantics of the content of the review text itself. This measure defines helpfulness as a function of words/terms that have the highest cosine closeness to the term ‘helpful’ based on LSA.<sup>2</sup>

In brief, LSA (more on LSA in the Calculating the Variables section)

can reveal the cosine closeness among words/terms, such as how close the term “helpful” is to any other word in that corpus, and do so irrespective of the sentences the words appear in and irrespective of whether the word is a noun, pronoun, adjective, or any other part of speech they relate to in the sentence. The only context being considered in this type of analysis is the context of the entire corpus of documents – in this case, it is the set of online reviews being analyzed. The cosine distances produced by LSA can be thought of as revealing an abstract meaning of the word in terms of other words it is related to. The semantic measure of review helpfulness is defined accordingly as how close the combination of the words in the online review is to the term ‘helpful’. That combination is calculated as a vector that combines the cosine closeness of all the words in the review, except stopwords.<sup>3</sup> This calculation is “directly related to the distance between two points described by the projection of the vectors onto the surface of the hyper sphere in which they are contained” [41].

## 2.4. Assessing this alternative semantic measure of review helpfulness

To assess how good the semantic measure of review helpfulness is, it was compared with the two vote-up/vote-down based measures of helpfulness. The semantic measure is better practically because it can be applied even before human readers rate the online review. Additionally, it is expected that statistically it would be predicted better by known antecedents of review helpfulness because it relates directly to the essence of the review rather than through how a rater assessed it – avoiding the imbalanced vote bias reported by Liu et al. [46]. The semantic measure also avoids the risk that a reader might be influenced by prior reader ratings. The antecedents of review helpfulness were developed from previous research on this topic.

We now discuss those antecedents one by one. Research shows that the length of the review predicts review helpfulness. When readers are told more about the product, the chances are that the review will be more helpful. In normal length reviews, the longer the review, the more helpful it can be [e.g. 48, 56, 76].<sup>4</sup> This refers to the number of words in the review, and by extension of the same logic, it should apply also to the number of words in the product description provided by the seller/manufacturer. These two variables were added as controls, as they are known to be important but are not the essence of this study.

Another antecedent is the sentiment in the review text, which has had divergent findings in existing research. In the early literature on this topic, negative sentiments were suggested to be more helpful to consumers [37]. Salehan and Kim [65] suggested that reviews with neutral polarity are assessed as more helpful. Others suggested that positive reviews are more helpful and that product type – utilitarian versus hedonic – moderates the impact of the positive sentiments [67]. Yet another determinant of review helpfulness is readability. This vari able appears as ARI, Automated Readability Index, in Fig. 1. Some authors suggest that higher readability has a positive efect on the helpfulness of the review [28,39], while others claim a negative impact [83]. Another predictor is posting order, which is a variable calculated at the product level and added in this study as a control variable. Some studies found a positive impact of the number of days since posting a review on its assessed helpfulness [63,65,80], others suggested a negative impact [77]. Also making a review helpful are the number of previous helpfulness evaluations [24,44].

The number of stars is another antecedent that produced mixed re sults in previous research. This variable has been employed in many studies due to its ease of access. The literature reports mostly a positive impact of the number of stars on review helpfulness [61,76], but some studies report a negative impact [63,83]. The number of stars is added in this study as a control.

## 2.5. Information entropy increment as a measure of review uniquenes

Existing research has scarcely assessed the actual information content of online reviews and its impact beyond sentiment. This limited attention to the actual information content may be the result of a lack of appropriate methodologies to analyze large corpora of textual data [15], the necessary costly analyses, and the noisy results it can produce [30]. The second objective of this study is to suggest a measure to address the efect of incremental information content, more precisely the information entropy increment of the review. Entropy represents a measure of information uniqueness, and its increment over previous reviews is therefore a potential positive influence on review helpfulness. To the best of our knowledge, Singh et al. [72] is the only study that linked information entropy to review helpfulness, finding a positive efect of entropy on review helpfulness.<sup>5</sup>

Entropy is an established method for calculating disorder, i.e. unpredictability. The concept of information entropy was suggested by Shannon [69]. Entropy, in the context of information systems, is often defined as a “measure of the amount of information the system contains” [6,p.,301]. The more a message can be predicted based on previous messages, the lower its entropy. The more unique its wording is compared to previous messages, the higher its entropy. Higher entropy messages are of higher potential incremental contribution because they introduce new words, and hence potentially new ideas.<sup>6</sup> Incremental entropy is calculated compared to both previous reviews and the information that is provided by the seller/ manufacturer – allowing that rational potential buyers might consult both of these readily available sources of information. Specifically, the information provided in the product description is the baseline for the increment of the first review. For the following reviews, the incremental entropy is calculated as the additional entropy compared to previous reviews – i.e. the second to the first, third to the second and first, etc. The logic is that if a reader reads many reviews that say the same thing, at least in that they repeat the same words as in previous reviews, then the value of that review is lower. If, however, a review adds a new idea, e.g. by introducing new words, it may convey new information, and, hence, be of more value. Our methodology approximates this conceptualization.

According to entropy theory, if a message contains elements that are statistically independent of each other, then the information contained in the message is the sum of the information content of the individual elements [49,69]. Shannon's entropy of a categorical random variable with size p and with associated probabilities $\mathsf { \theta } _ { 1 } , . . . , \mathsf { \theta } _ { p }$ with $\theta _ { \mathbf { k } } \ > \ 0$ and $\Sigma _ { \mathbf { k } } \ \theta _ { \mathbf { k } } = 1$ in natural units is given by Hausser and Strimmer [31] as:

![](/api/attachments/QH2MBWVR/fulltext/images/41e6a53c4c7e8bf937df2aecfd44e6e5246cdcdbd67ee795e33252928e03d738.jpg)  
Fig. 1. Conceptual model.

$$
H = - \sum_ {k = 1} ^ {p} \Theta_ {k} \log (\Theta_ {k})\tag{1}
$$

Information entropy is closely related to the concept of uncertainty reduction [38]. In this sense, Ross [64] defines information as “knowledge, after which one receives and processes, that changes, in an uncertainty changing way, their ex ante probability distribution regarding a set of propositions or states” (p. 5). Information reduces uncertainty [69,78], and so the amount of information that a system provides can be measured by the amount of uncertainty that it reduces [6]. Knowledge that is informative should change a user's probability distribution regarding a set of propositions in an uncertainty reduction way [64]. Note that the argument for entropy is that a unique review, measured through the uniqueness/unpredictability of its words, is more helpful. We are not making an argument that this process reduces the uncertainty of the product or service, the argument relates only to the uniqueness of the review. Our Methodology portion describes the op erationalization of Eq. (1).

## 3. Research model and hypotheses

Evaluating the proposed semantic measure of review helpfulness, and in the process also the new information entropy increment measure, was done in the context of comparing the same model with the semantic measure of review helpfulness as its dependent variable with the two measures based on the vote-up/vote-down numbers. The research model is shown in Fig. 1. Antecedents that are not central to the study are added as controls. The hypotheses test that the semantic measure of review helpfulness behaves theoretically much as the vote up/vote-down based measures do, and that the new information en tropy increment behaves as expected. The overall pattern of the research model is intended to show that, combined, the hypotheses and controls predict the degree that the review is assessed as helpful as tested in terms of three alternative measures: the proposed semantic helpfulness measure, helpfulness vote ratio, and thumb-up votes. Additionally, it demonstrates that this prediction is better for the semantic measure of review helpfulness in terms of both $\mathbb { R } ^ { 2 }$ and bias minimization. The proposed semantic measure in this study is more closely aligned with the expected theoretical antecedents of review helpfulness than the vote-up/vote-down based measures of previous research.

## 3.1. The importance of the increment of information entropy

Information is more valuable when it reveals something new, i.e. has not been posted previously. Such information is less predictable, and hence more helpful. Entropy measures that information uniqueness [69]. Specifically, the measure applied in this study is the incremental information entropy of the current review compared to all previous reviews, with the first review being the information in the seller/ manufacturer site. If a potential buyer reads a review that adds no further information, or merely repeats previously used words, then the value of that review will be lower.

$\mathbf { H _ { 1 } } .$ . The higher the information entropy increment, the more helpful the review.

## 3.2. The importance of moderate sentiment

The literature suggests a negative impact of extreme negative or positive sentiments on consumers through psychological reactance [9]. Hu et al. [36] found that customers may find reviews with moderately negative and moderately positive sentiments to have the greatest value. Hu et al. also suggest that extremely positive sentiments may be perceived as fake attempts by sellers or manufacturers to promote a product. In this sense, Mudambi and Schuf [56] added a quadratic term to examine review extremity in their analysis. Schindler and Bickart [66] found that reviews containing negative or positive style characteristics were perceived as less helpful. For this reason, the next hypothesis tests whether reviews with moderate sentiment or with balanced levels of negative and positive sentiments – named by Salehan and Kim [65] as “neutral polarity” – are assessed as more helpful.<sup>7</sup> The square root of this variable was used because of its high kurtosis. Sentiment deviation is the degree that the sentiment is not neutral.

$\mathbf { H } _ { 2 } .$ The stronger the sentiment deviation, the less helpful the review.

## 3.3. The importance of text readability

Due to the open and available nature of online reviews to a broad spectrum of users, the way the information is conveyed may impact the ability of potential new buyers to understand and use that information. Research suggests that higher readability has a positive efect on review helpfulness [28,39]. To measure readability, this study employs the Automated Readability Index (ARI) developed by Senter and Smith [68].

H . The higher the ARI of the text, the more helpful the review.

## 3.4. Number of previous helpfulness assessments

Consumers rely on the recommendations of other online consumers when making purchasing decisions [e.g. 24, 44]. This peer persuasion may also impact the helpfulness assessment of a review, even though it has nothing to do directly with the specific review being assessed. The number of previous helpfulness assessments can have an impact on the subsequent evaluations, as potential customers may follow the re commendations of others regarding the helpfulness perception of the review [17,20]. Research suggests that vote-up/vote-down measures are biased by previous votes [46] and how those reviews are presented [11,75].

Allowing that our data are not theoretically diferent from data in previous studies, this hypothesis is also added to the research model. While it is expected that this hypothesis will be significant with the vote-up/vote-down based measures as in past research, it is expected that it will not be significant in predicting the semantic measure of review helpfulness because that measure relates to the current review only, regardless of the assessment of previous reviews. The ln of the number of previous helpfulness evaluations was taken because the diference between having no helpfulness evaluations and having one evaluation should be more noticeable and important than between having, say, 100 or 101 helpfulness evaluations.

H . The more previous helpfulness evaluations a review has, the more helpful the review for vote-up/vote-down based measures but not fo the semantic measure.

## 3.5. Controls

Allowing that our data are not theoretically diferent from data in previous studies, we should find that more words in a review will contain more information [e.g. 48, 56, 76]. The length of the description provided by the seller or manufacturer was also added as a control, based on the same logic that longer descriptions can provide more information and should therefore be more helpful. Words are the primary medium through which previous buyers, sellers, and manufacturers provide information about a product. It is expected that a very short review cannot tell as much about the product or experience with it as a longer review can. Hence, a longer review could be more informative, and thereby more helpful, although this impact should have diminishing returns. Longer descriptions may also provide additional information beyond the strict specifications of what is being sold, such as customer service, guarantees, or return policies. Description length was collected as part of the new information entropy increment measure. The ln of these two controls were added to account for their expected diminishing efect as the number of words increases.

To account for the known bias of posting order, this was also added as a control variable. Including posting order allows for testing the assumption that reviews of the same product are independent of each other [80]. The ln of this variable was taken because people will presumably notice, even without counting, the diference between the second and the third review, but may not notice the diference between

review 100 and review 101.

We also control for the number of stars in the review. The number of stars may assist potential customers in learning about the quality of a product [22]. Pan and Zhang [61] found that positive ratings are more influential than negative ones and are rated as more helpful. Pan and Zhang suggested a positive correlation between the number of stars and review helpfulness. If that is the case, then the number of stars might be considered as a surrogate recommendation [1]. The existence of a market for artificially inflating ratings [e.g. 40,57,79] supports the idea that the number of stars increases perceived helpfulness. The con ceptual model is shown in Fig. 1.

## 4. Methodology

The dataset analyzed consists of 20,722 reviews relating to appli ances and appliance supplies available for purchase on Amazon.com. This specific category was selected for two main reasons: (1) lack of seasonality and (2) less marketing activity, e.g. advertising, than other more popular categories. We selected 25,000 random reviews belonging to this product category from the McAuley dataset.<sup>8</sup> The data was collected in 2014 and updated in 2016 and has been used in previous research [51,52]. The variables available in this dataset are: ID of the reviewer, ID of the product (Amazon's ASIN number), name of the reviewer, helpfulness evaluation of the review, text of the review, review valence, heading of the review, time of the review (Unix time), and date of the review (regular format). Using the ASIN number, we scraped the description of the product provided by the seller/manufacturer. The total number of reviews decreased from 25,000 to 20,722 because of missing values and product unavailability on Amazon.com at the time of the product description data collection. The total number of products reviewed in the final dataset was 4545 and the total number of unique reviewers was 20,397. The number of words in the review, number of words in the product description, number of helpfulness evaluations, and number of stars came straight from the data. The semantic helpfulness measure, information entropy increment, sentiment score deviation, and ARI are explained next.

## 4.1. Calculating the variables

Determining the semantic helpfulness of the reviews was done using LSA. LSA identifies through singular value decomposition (SVD), a process somewhat equivalent to a two-way principal component analysis (PCA), what terms (words) and what documents (in this case online consumer reviews) factor together by analyzing their Document-Term [frequency] Matrix (DTM). In previous literature, SVD was successfully applied to other areas of online review research [e.g. 81]. Terms that factor together are assumed to carry a shared latent meaning, much as factors are assumed to do in a PCA. As in a PCA, only factors that explain high degrees of the variance are retained. The resulting retained factors identify the words that carry the most weight in explaining the variance in the DTM. LSA has been shown to closely approximate some aspects of human learning [26,43]. Those characteristics make it especially suitable for the kind of analysis performed in this study. Another advantage of LSA is that it allows for the analysis of many documents, in this case product reviews, with minimal human intervention.

The semantic measure of helpfulness was calculated using the default parameters of LSA in R. In building the DTM, stop words and punctuation marks were removed, and a standard Tf-idf transformation was run. This standard procedure gives more weight to less used words [21,43]. A reduced-rank SVD was then applied to the DTM [2]. SVD retains the k-largest singular values and sets the other dimensions to 0. After applying SVD, each document and each term is represented as a kdimensional vector in a semantic space. Finally, the cosine similarity of each document to the term ‘helpful’ was estimated.<sup>9</sup> This closeness to the term ‘helpful’ is what constitutes the dependent variable of our suggested measure in Fig. 1.

Table 1 Descriptive statistics.

<table><tr><td>Variable</td><td>N</td><td>Mean</td><td>Standard Deviation</td><td>Median</td><td>Min</td><td>Max</td><td>Skewness</td><td>Kurtosis</td></tr><tr><td>Semantic Review Helpfulness</td><td>20,722</td><td>0.11</td><td>0.03</td><td>0.12</td><td>0.00</td><td>0.30</td><td>-0.27</td><td>0.76</td></tr><tr><td>Helpfulness Vote Ratio</td><td>20,722</td><td>0.28</td><td>0.43</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.94</td><td>-1.02</td></tr><tr><td>Helpfulness Thumb-up Votes</td><td>20,722</td><td>1.85</td><td>9.42</td><td>0.00</td><td>0.00</td><td>546.00</td><td>24.30</td><td>978.39</td></tr><tr><td>ln (Helpfulness Thumb-up Votes)</td><td>20,722</td><td>3.16</td><td>6.99</td><td>1.00</td><td>1.00</td><td>109.00</td><td>7.44</td><td>73.10</td></tr><tr><td>Information Entropy Increment</td><td>20,722</td><td>0.23</td><td>0.22</td><td>0.15</td><td>-0.95</td><td>0.69</td><td>0.77</td><td>-0.58</td></tr><tr><td>Sentiment Score Deviation</td><td>20,722</td><td>2.53</td><td>2.65</td><td>2.00</td><td>0.00</td><td>48.00</td><td>3.25</td><td>22.89</td></tr><tr><td>Square Root (Sentiment Score Deviation)</td><td>20,722</td><td>1.37</td><td>0.81</td><td>1.41</td><td>0.00</td><td>6.93</td><td>0.29</td><td>1.02</td></tr><tr><td>ARI</td><td>20,722</td><td>5.16</td><td>2.73</td><td>5.01</td><td>-7.85</td><td>36.36</td><td>0.83</td><td>4.41</td></tr><tr><td>Number of Helpfulness Evaluations</td><td>20,722</td><td>2.25</td><td>10.32</td><td>0.00</td><td>0.00</td><td>552</td><td>21.90</td><td>803.12</td></tr><tr><td>ln (Number of Helpfulness Evaluations)</td><td>20,722</td><td>3.63</td><td>7.84</td><td>1.00</td><td>1.00</td><td>115</td><td>6.72</td><td>60.31</td></tr><tr><td>Number of Words in Review</td><td>20,722</td><td>78.39</td><td>100.84</td><td>44.00</td><td>4.00</td><td>2137.00</td><td>5.55</td><td>55.06</td></tr><tr><td>ln (Number of Words in Review)</td><td>20,722</td><td>3.97</td><td>0.80</td><td>3.78</td><td>1.39</td><td>7.67</td><td>0.78</td><td>0.61</td></tr><tr><td>Number of Words in Product Description</td><td>20,722</td><td>73.84</td><td>100.17</td><td>43.00</td><td>2.00</td><td>1186.00</td><td>4.80</td><td>33.53</td></tr><tr><td>ln (Number of Words in Product Description)</td><td>20,722</td><td>3.81</td><td>0.95</td><td>3.76</td><td>0.69</td><td>7.08</td><td>0.33</td><td>-0.21</td></tr><tr><td>Posting Order</td><td>20,722</td><td>30.16</td><td>64.16</td><td>6.00</td><td>1.00</td><td>471</td><td>3.41</td><td>12.67</td></tr><tr><td>ln (Posting Order)</td><td>20,722</td><td>1.97</td><td>1.64</td><td>1.79</td><td>0.00</td><td>6.15</td><td>0.57</td><td>-0.61</td></tr><tr><td>Number of Stars</td><td>20,722</td><td>4.05</td><td>1.42</td><td>5.00</td><td>1.00</td><td>5.00</td><td>-1.27</td><td>0.10</td></tr></table>

The information entropy increment for each review was calculated as the number of words in each review added beyond the number of words provided by the seller/manufacturer in the product description and in previous reviews. The entropy was estimated with Maximum Likelihood (ML) [31], which estimates entropy from discrete counts without assuming any prior distribution. As the underlying probability of the discrete random variable is unknown, H and $\theta _ { \mathbf { k } }$ in Eq. (1) were estimated from the observed counts where $\mathbf { y } _ { \mathbf { k } } \geq 0 .$ The ML estimator derived from Eq. (1) is:

$$
\widehat {H} ^ {M L} = - \sum_ {k = 1} ^ {p} \widehat {\theta} _ {k} ^ {M L} \log (\widehat {\theta} _ {k} ^ {M L})\tag{2}
$$

Eq. (2) is constructed by plugging the ML frequency estimates $\widehat { \Theta } _ { k } ^ { M L } = \frac { y _ { k } } { n }$ into Eq. (1), with $\begin{array} { r } { n = \sum _ { k = 1 } ^ { p } y _ { k } } \end{array}$ being the total number of counts. For example, if a review contained 16 words and the description of the product reviewed contained 51 words, then the entropy value of that review is entropy( $\mathrm { 5 1 , 1 6 ) = - \left[ \left( \left( \frac { 5 1 } { 6 7 } \right) ^ { \ast } l o g \Big ( \frac { 5 1 } { 6 7 } \Big ) \right) + \left( \left( \frac { 1 6 } { 6 7 } \right) ^ { \ast } l o g \Big ( \frac { 1 6 } { 6 7 } \Big ) \right) ^ { - } \right. }$ \~ 0.5497. Once this value was calculated, all the reviews were ordered according to their posting date. The increment in entropy was calculated as the entropy of the number of words included in review n and all the previous reviews and the product description itself minus the entropy of the number of words included in review n-1 and all the previous reviews and the product description itself. For example, if the product description provided by the seller/manufacturer contained 49 words. the first review contained 84 words. and the second review contained 117 words, then the increment of entropy for the second review would be entropy(49, 84, 117) - entropy(49, 84) \~ 0.3831.

The sentiment score was calculated for each review by applying the standard Bing lexicon-based sentiment analysis [35,74]. Vocabularybased techniques classify text by afect categories based on the presence of afect words such as “happy,” “sad,” “afraid,” or “bored” – detected from a dictionary – and provide a global score that reflects the negative, positive, or neutral polarity of a given text [60]. In order to study the extremity of the sentiments of the review, we estimated the deviation from the median of the sentiment score of all the reviews – the value of this median in our dataset is +2. Sentiment score deviation is the absolute value of the sentiment score of the review minus the value of the median score for the dataset.

Readability of the text, the ARI score, was calculated applying its standard formula [68] based on the number of characters, number of words, and the number of sentences in each individual review:

$$
A R I S c o r e = 4. 7 1 \left(\frac {\text {number of characters}}{\text {number of words}}\right) + 0. 5 \left(\frac {\text {number of words}}{\text {number of sentences}}\right) - 2 1. 4 3\tag{3}
$$

## 5. Analysis

Descriptive statistics of the data are shown in Table 1.

The research model was tested with linear regression models for semantic helpfulness (Model 1) and thumbs-up votes (Models 3 and 5). Vote ratio (Models 2 and 4) was tested with logistic regression in accordance with previous literature (e.g. [61]) because of its [0, 1] range. Table 2 shows the standardized estimates, estimates, and standard errors for the models. We also run Models 2 and 4 with censored regression, limiting the dependent variable to the range of [0, 1] and obtained equivalent results. Because Table 1 showed that the thumb-up votes measure has high skewness and kurtosis values, that measure was transformed by calculating its logarithm. Models 2 and 3 show that Votes ratio and Thumb-up votes are strongly influenced by the number of helpfulness evaluations. To assess this influence, Models 4 and 5 were run, removing the ln (number of helpfulness evaluations) measure. Henceforth, Models 4 and $^ { 5 , }$ rather than Models 2 and $^ { 3 , }$ are discussed.<sup>10</sup>

The new measure of Information Entropy Increment is a significant predictor of all three measures of helpfulness (except in Model 2), supporting $\mathrm { H } _ { 1 }$ and showing the value of assessing incremental entropy too. The square root of Sentiment Score Deviation significantly decreases only the semantic measure of helpfulness, supporting $\mathrm { H } _ { 2 }$ with the semantic measure and suggesting that the two measures based on votes do not behave as theoretically expected (and it is insignificant in Model 2). Readability (ARI) decreased the semantic measure of helpfulness but did not significantly afect the Helpfulness Vote Ratio and the Helpfulness Thumb-up Votes, leaving $\mathrm { H } _ { 3 }$ unsupported. This may be consistent with some previous research that found that the readability of the text is not a predictor of review helpfulness [83] and in view of the meta-analysis by Hong et al. [34] that found no significant influence of readability on review helpfulness. The number of previous helpfulness evaluations had a significant positive efect on the two vote-up/vote-down based measures, partly supporting $\mathrm { H } _ { 4 } ,$ but it also had an unexpected small negative efect on the semantic measure of helpfulness, possibly because the sample was so large.

Linear regression analysis results.

<table><tr><td colspan="2">Hypothesis</td><td>Model 1 Semantic Helpfulness Measure Standard. E. Estimate (Std. Err.)</td><td>Model 2 Helpfulness Vote Ratio Standard. E. Estimate (Std. Err.)</td><td>Model 3 ln (Helpfulness Thumb-up Votes) Standard. E. Estimate (Std. Err.)</td><td>Model 4 Helpfulness Vote Ratio Standard. E. Estimate (Std. Err.)</td><td>Model 5 ln (Helpfulness Thumb-up Votes) Standard. E. Estimate (Std. Err.)</td></tr><tr><td></td><td>Intercept</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td></td><td></td><td>0.03(0.0012)***</td><td>-4.62(0.17)***</td><td>-1.68(0.14)***</td><td>-4.86(0.16)***</td><td>-8.95(0.40)***</td></tr><tr><td>H1</td><td>Information Entropy Increment</td><td>0.040.0048(0.0011)***a</td><td>0.0090.04(0.16) p = 0.79</td><td>-0.002-0.07(0.13)***</td><td>0.0650.29(0.14)*</td><td>0.041.42(0.36)***</td></tr><tr><td>H2</td><td>Square Root (Sentiment Score Deviation)</td><td>-0.03-0.0008(0.0002)***</td><td>0.030.04(0.026) p = 0.12</td><td>0.010.09(0.02)***</td><td>0.050.06(0.02)**</td><td>0.050.42(0.06)***</td></tr><tr><td>H3</td><td>ARI</td><td>-0.06-0.0006(0.0001)***</td><td>-0.002-0.001(0.007) p = 0.92</td><td>-0.001-0.003(0.006) p = 0.63</td><td>-0.004-0.001(0.007) p = 0.84</td><td>-0.01-0.02(0.02) p = 0.20</td></tr><tr><td>H4</td><td>ln (Number of Helpfulness Evaluations)</td><td>-0.05-0.0002(0.0001)***</td><td>2.700.34(0.009)***</td><td>0.940.84(0.002)***</td><td>-</td><td>-</td></tr><tr><td>Control</td><td>ln (Number of Words in Review)</td><td>0.700.0223(0.0002)***</td><td>0.440.55(0.03)***</td><td>0.030.23(0.03)***</td><td>0.710.90(0.03)***</td><td>0.312.76(0.07)***</td></tr><tr><td>Control</td><td>ln (Number of Words in Product Description)</td><td>0.020.0006(0.0001)***</td><td>0.180.19(0.02)***</td><td>0.0020.01(0.02) p = 0.39</td><td>0.270.29(0.02)***</td><td>0.060.44(0.05)***</td></tr><tr><td>Control</td><td>ln (Posting Order)</td><td>-0.002-0.0000(0.0002) p = 0.86</td><td>-0.28-0.17(0.02)***</td><td>-0.006-0.03(0.02) p = 0.15</td><td>-0.49-0.30(0.02)***</td><td>-0.11-0.48(0.05)***</td></tr><tr><td>Control</td><td>Number of Stars</td><td>0.030.0006(0.0001)***</td><td>-0.01-0.01(0.014) p = 0.45</td><td>0.040.20(0.01)***</td><td>-0.18-0.13(0.01)***</td><td>-0.02-0.08(0.03)*</td></tr><tr><td colspan="2">R2</td><td>0.41</td><td>-</td><td>0.89</td><td>-</td><td>0.16</td></tr><tr><td colspan="2">Cox-Snell pseudo-R2</td><td>-</td><td>0.28</td><td>-</td><td>0.18</td><td>-</td></tr><tr><td colspan="2">McFadden pseudo-R2</td><td>-</td><td>0.31</td><td>-</td><td>0.18</td><td>-</td></tr></table>

Significance levels \*\*\* at 0.001, \*\* at 0.01, \* at 0.05.  
<sup>a</sup> An additional analysis of Model 1 was run in which entropy increment was recalculated by implementing textual data preparation, which included casting the data into all lowercase, removing numbers and punctuation marks, removing stopwords and white spaces, as well as stemming. This yielded almost identical results as in Table 2. This additional test was implemented to assess a possible negative influence of misspelled words and singular vs. plural forms.

Across the three measures of review helpfulness the more words there were in the review text and in the product description, the more helpful the review was, as expected. The other controls tell an interesting story that supports the assertion that the semantic measure of review helpfulness behaves more as theory would expect. Posting Order was a significant predictor of the two vote-up/vote-down based mea sures (except in Model 3), however, again as might be expected, not so with the semantic measure. This shows that the semantic measure is not susceptible to the bias that the vote-up/vote-down based measures are. The Number of Stars that should have had a positive efect on review helpfulness [61], increased the semantic measure of helpfulness (Model 1) but decreased both Helpfulness Vote Ratio and Helpfulness Thumb-up

Votes (Models 4 and 5). Again, this can be interpreted as supporting the suggested improvement of the semantic measure of helpfulness over the vote-up/vote-down based measures.

## 6. Discussion

Adding to previous research, this study shows that (1) an alternative measure of semantic review helpfulness may overcome some of the biases in the vote-up/vote-down based measures, and (2) that there is reason to add another antecedent of review helpfulness that deals with the information entropy increment of the content of the review compared to previous reviews and the product description as provided by the seller/manufacturer. The importance of these two contributions is discussed next. The results (3) also confirm some of the previously noted problems with the vote-up/vote-down based measures. Another problem the analysis reveals with the vote-up/vote-down based measures is that strong sentiment that is supposed to decrease the value of a review, as suggested by psychological reactance theory [9], only does so with the semantic helpfulness measure while it increases the voteup/vote-down based measures.

## 6.1. Contribution to theory

Recent research [34] highlights that the current operationalization of helpfulness – either as the ratio of helpful votes over the total number of helpfulness assessments or the total number of helpful votes – results in inconsistent efects on review helpfulness. Research also reports several sources of bias that impact the evaluation of the helpfulness of the review, such as the early bird bias, the imbalanced vote bias, and the winner cycle bias [46]. Cao et al. [11] and Wan and Nakayama [75] even question the reliability of the current measures of review helpfulness and pointed out that more accessible reviews might receive more votes. The strong influence of number of helpfulness evaluations on both vote measures may be a reflection of the anchoring efect reported by these authors. Once the number of helpfulness evaluations was removed from Model 2 and Model $^ { 3 , }$ the $\scriptstyle \mathrm { \mathrm { R } } ^ { 2 }$ in Model 4 and Model 5 dropped markedly. Our results show that the new semantic measure of helpfulness may be less susceptible to those biases, since our suggested new semantic measure defines what is helpful based on the content of the reviews themselves.

Apart from its lack of susceptibility to biases that were noted by previous research, the new semantic measure is also practically and theoretically appealing for additional reasons. Practically, the new measure allows assessing reviews that other people have not assessed yet and allows for a prediction of how helpful a review might be even before it is posted. This can assist companies in automatically promoting the more helpful reviews and in removing the less helpful ones. And, importantly, that decision can be made not only automatically but also based on the implied meaning that the writers give to reviews, rather than based on the inevitable bias of a person in a company that is paid to promote a product. Considering the susceptibility of the online environment to manipulation by unscrupulous vendors, having an au tomated method of assessing reviews based on what customers write can be a powerful tool.

From a theoretical perspective, review helpfulness can be assessed by readers, as in the current two vote-up/vote-down assessments. That, however, is a subjective evaluation, being an assessment of what the other people thought of it, rather than an assessment of the review itself directly. The semantic measure of helpfulness, in contrast, is directly tied to the review, and, even more so, it assesses the review in view of a semantic context created by many other reviews. This allows for the assessment of the review not only based on its content, but on its content in context. That opens new lenses into studying the helpfulness of reviews, and, by extension, many other important properties of those reviews such as how trustworthy the review is. Trust is a crucial en abling determinant of ecommerce [25,54], so crucial that buyers are willing to even pay a premium for it [4,62]. And yet, if one were to try to assess the trustworthiness of a review based on the way its help fulness is assessed, one would hit a brick wall because the entire ap proach to measuring helpfulness by votes would need to be recreated for measuring that construct. Not so, however, with the semantic measure of helpfulness. Applying that same approach to measuring other constructs of interest, such as trust, can easily be done with minor adaptations of the way the semantic measure of helpfulness was created in this study.

The study of incremental entropy, likewise, can shed new light on ecommerce research. To the best of our knowledge, Singh et al. [72] is the only study that incorporates a measure of review entropy and studies its impact on helpfulness. (As noted in footnote 5, that study, however, operationalized review helpfulness as a ratio of positive votes over the total number of helpfulness evaluations.) Singh et al. indeed found that information entropy is a significant predictor of review helpfulness as measured by votes. Difering from Singh et al., our study employs entropy increment, which is mostly unrelated to review length.

Looking at reviews through the theoretical lenses of entropy increment suggests another interesting nuance. Adding words to a review is important, but those added words must have a purpose: to provide novel information bevond what was already said by the seller/manufacturer and previous reviewers. Our results suggest that such unique information, i.e. less predictable content, is very helpful. This finding suggests that it is not only the number of words, i.e. how much is written, that increases the helpfulness perception of the review – an approach common in the early literature [e.g. 15] – but, rather, how unique those words are. It is not that previous research did not recognize the importance of “what” versus “how much”, but rather that previous research did not have the tools to do so objectively. Indeed, Filieri [22] suggested that potential buyers are more influenced by the quality of the information (information quality being defined by information depth and breadth, relevance, credibility, and factuality) than by information quantity. Mudambi and Schuf [56] also suggested that information depth is an important predictor of review helpfulness. Cao et al. [11] found that semantic characteristics (related to the ‘substance’ of the text) are the most important in determining helpfulness votes. The proposed measure of information entropy increment allows the analysis of the text portion through a more nuanced lens. This is important because past research concentrated on review ratings – for a meta-analysis on the impact of the number of stars and the volume of reviews on sales see Floyd et al. [23] – even if the short comings of relying on these reviews ratings was recognized [18].

Another potential theoretical and practical contribution relates to the number of words in the product description as provided by the seller/manufacturer. The results indicate the importance of this information. To the best of our knowledge, ours is the first study to investigate the role of this variable in afecting review helpfulness. As shown in Table 2, the more words that are included in the description of the product, the more helpful the review is. This rich source of information from sellers and manufacturers could serve as a stronger foundation for reviewing the product. This mechanism may have important practical implications as well, as the amount of information provided in the description of the product should be carefully considered. Although our results suggest that longer descriptions might be recommendable, none of the descriptions of the products included in our dataset was long enough to potentially trigger information overload – the longest description contained 1186 words, as shown in Table 1. Longer descriptions may be better, and yet too much information may have a negative impact through information overload [70]. The content and length of product description and its role in impacting review helpfulness calls for further research.

Research suggested that reviews with moderate sentiments are more helpful [36]. Very positive sentiments may be treated with suspicion, as they may be perceived as illicit attempts from sellers to promote a product [36]. The results of this study suggest a more nuanced picture. In this study, we find that more extreme sentiment actually increased both the Helpfulness Vote Ratio and the transformed Helpfulness Thumbup Votes. This may be due to the type of product studied, and more research is needed to assess this.

## 6.2. Contribution to practice

Sellers, manufacturers, marketers, and buyers all rely on online reviews. Understanding what makes a review more helpful is of undeniable economic benefit, as the case of Amazon reveals [73]. What makes a review helpful, however, is less clear and has been the subject of much previous research. In that context, this study makes two contributions that apply to practice too. First, it views review helpfulness from a new perspective, looking at the semantic meaning of “helpful” as a guide in that matter, rather than relying on previous votes. Measuring review helpfulness through previous votes is known to be problematic [34].

The semantic measure has a practical constructive appeal: it can be measured automatically and directly without resorting to human voters. Human voters can unintentionally introduce bias, add costs, and inadvertently delay the assessment of the review until they read and think about it. The automatic semantic measure of review helpfulness avoids all those because it is directly derived from the review in the context of other reviews. Moreover, having a semantic measure could even allow tweaking a review to increase its helpfulness before it is posted. This is impactful also because the semantic measure is assessed directly by the software, which means that one can avoid the posting of non-helpful reviews.

The second practical contribution is the ability to assess incremental entropy and its importance automatically and without a human rater should be of value for the same reasons. Being able to assess this antecedent automatically could allow sellers, manufacturers, and marketers to tweak the review so it is more valuable to potential buyers, increasing the appeal and value of the review and of the market it is posted on. Avoiding, or delegating to the end of the list, postings that repeat previous content, and preferably doing so automatically, could also be achieved through this method.

Perhaps no less important from an application of the model per spective, it is important to show that the regression is both significant and is estimated with little bias. Skewness and kurtosis will cause such bias, and that is a problem with the number of helpfulness evaluations shown in Table 1. That problem is much reduced in the Helpfulness Vote Ratio and the transformed Helpfulness Thumb-up Votes dependent variable measures that were derived from the number of helpfulness eva luations. However, skewness and kurtosis are not an issue at all with the semantic measure of helpfulness. That may indicate that the estimated regression betas of the antecedents of the semantic measure of help fulness in Table 2 are also less biased. Knowing with little bias what the beta of each antecedent is could provide guidance on where to best invest to increase helpfulness.

## 6.3. Contribution to methodology

Another contribution of this study is in suggesting a new methodology to operationalize review helpfulness and in showing what elements impact this new operationalization, as well as showing how the new construct information entropy increment can be calculated. In essence, the methodological approach of this study employs the meaning of helpfulness provided by the reviewers of the product. Arguably, the 20,397 individuals who had already interacted with the product and who are the ones who define what is helpful, should do so in term that overlap with what is considered helpful by other buyers.

This methodology has the potential to overcome many of the shortcomings of previous measures of review helpfulness (e.g. [34]). The new semantic helpfulness measure should not afected by the im balanced vote bias, winner cycle bias, early bird bias, or the anchoring efect [11,46,75]. The diference between our approach and previous ones can be corroborated by the impact of the number of helpfulness evaluations over review helpfulness and the impact of the posting order – as compared by their standardized estimates in Table 2. Assessing the goodness-of-fit of the new semantic measure to the current ones that are based on vote-up/vote-down assessments, the new semantic approach had an R<sup>2</sup> of 0.41 (Model 1), noticeably higher than the 0.18 of the helpfulness vote ratio approach (Model 4) and the 0.16 of the helpfulness thumb-up votes approach (Model 5). The semantic approach not only overcomes reported sources of bias, but it also explains more of the variance. Another potential of the semantic approach to measuring helpfulness is that it does not depend on voting system dynamics. The helpfulness of reviews can be assessed even without review votes. From a practical standpoint, this allows companies to respond and act faster. Likewise, accounting for entropy increment may also open new practical possibilities, such as assessing reviews before people read them. Moreover, supporting the current practice of many review sites to recognize their most important reviews and reviewers [5], it may be time to also recognize reviews and reviewers that increase information en tropy.

## 6.4. Limitations and avenues for future research

The data included in this research consisted on a single product category, deliberately chosen to reduce potential seasonality and promotions that may impact the analyses implemented. Since research suggests that product type may play an important role in determining the perceived helpfulness of online reviews [e.g. 55,56,61], replicating the study with other products or product types may reveal additional insight. What is perceived as helpful within a specific setting may not be perceived as such within a diferent one. In this sense, practitioners may be interested in characterizing and making more accessible those reviews that are considered more helpful. Practitioners could also be interested in making less helpful reviews less accessible or even deleting them. Another limitation of this study is that it does not incorporate reviewer characteristics. The data did not include those characteristics.

Our contributions are in developing a new, easy method to calculate a semantic measure of review helpfulness and adding incremental entropy as a new antecedent. Accordingly, we elected to use a currently available and widely used data analysis method. The contributions we claim are more convincing to current theory and practitioners if they apply tools that are already known, meaning that the results cannot readily be attributed to the method we chose or fishing, i.e. choosing the method that best fit the particular dataset we had. This is consistent with the Positivist epistemology we applied. Nonetheless, applying other text analysis methods, such as latent Dirichlet allocation (LDA), could be an interesting avenue of future research.<sup>11</sup>

Another issue possibly warranting additional study is the importance of the length of product description by the manufacturer or seller. It may well be that the beta of this control variable may vary depending on the product. In our data there were in all 4545 diferent products across 20,722 reviews, and so this was not investigated.

Although we tested that misspelled words, singular vs. plural forms, and even out-of-context messages have a minimal prevalence in our data, researchers may be interested in developing methodologies that are also robust to ‘messy’ textual data.

As stated in the Introduction, the information entropy increment measure we propose is not a panacea, nor is it claimed to be the only possible way to measure the value of the information in a review. For instance, if it were possible to measure the “comprehensiveness” of a review automatically, then such a measure might have been even more useful. The issue at hand, however, is that such a measure, and assessing its value, would be product- and reader- and culture-specific. This means that applying such a measure might require subjective assessments by readers and reviewers, thus introducing many of the biase our measure avoids and requiring reader votes.

Another critique that can be levied on the measure of information entropy increment is that it does not directly measure new, relevant information. Rather, it measures new words as a proxy for new information, which is an approximation that improves on previous approximations, e.g. Singh et al. [72], but it is still only an approximation. In this regard, this study should be regarded as a refinement on Singh et al., who measured only raw entropy (instead of the entropy increment employed in this study) as an example of possible machine learning analysis of factors that increase review helpfulness. Singh et al. found that entropy is one of the most important predictors of review helpfulness. Our study refines that approach, considering that the information provided by manufacturers and sellers as well as previous reviews should be considered as the baseline to calculate information entropy for a new review.

An issue sometimes raised against LSA is that incorrect spelling or the introduction of unrelated text (such as people using the online review to promote totally unrelated products or services) might introduce alternative terms and so mathematically bias the results. While that is a concern for existing helpfulness measures, since it could confuse readers, it has been shown in previous research (e.g. [27,42]) that when those issue arise in small number that LSA is rather immune to them, mapping alternative spelling, such as in British and American English, as totally overlapping terms. Indeed, the analysis in Model 1 that was replicated by implementing textual data preparation that included stemming yielded almost identical results as in the original Model 1 where it was not done.

## 6.5. Conclusion

This study proposes a new semantic measure of review helpfulness that potentially overcomes many of the theoretical and practical limitations of current measures. The results show that this new semantic measure behaves more as theory suggests that it should than the current vote-up/vote-down based measures do. The analysis also suggests the need to include information entropy increment. Textual data is readily available. It would be a pity not to incorporate it too into studying what makes an online review more helpful.

## References

[1] S.L.T. Alex, G. Prendergast, Is a "star" worth a thousand words? European Journal of Marketing 43 (11/12) (2009) 1269–1280.

[2] M. Anandarajan, C. Hill, T. Nolan, Practical Text Analytics, Springer, Cham, Switzerland, 2019.

[3] E.T. Anderson, D.I. Simester, Reviews without a purchase: low ratings, loyal customers, and deception, Journal of Marketing Research 51 (3) (2014) 249–269.

[4] S. Ba, P.A. Pavlou, Evidence of the efect of trust building technology in electroni markets: price premiums and buver behavior. MIS Ouarterly 26 (3) (2002) 243-268.

[5] H. Baek, J. Ahn, Y. Choi, Helpfulness of online consumer reviews: readers’ objectives and review cues. International Journal of Electronic Commerce 17 (2) (2012 99–126.

[6] J. Belzer. Information theory as a measure of information content. Journal of the American Society for Information Science 24 (4) (1973) 300–304.

[7] A. Benlian, R. Titah, T. Hess, Diferential efects of provider recommendations and consumer reviews in e-commerce transactions: an experimental study, Journal of Management Information Systems 29 (1) (2012) 237–272.

[8] B. Bickart, R.M. Schindler, Internet forums as influential sources of consumer information, Journal of Interactive Marketing 15 (3) (2001) 31–40

[9] S.S. Brehm, J.W. Brehm, Psychological Reactance: A Theory of Freedom and Control, Academic Press, New York, NY, 1981

[10] J.J. Brown, P.H. Reingen, Social ties and word-of-mouth referral behavior, Journal of Consumer Research 14 (3) (1987) 350–362

[11] Q. Cao, W. Duan, Q. Gan, Exploring determinants of voting for the “helpfulness” of online user reviews: a text mining approach, Decision Support Systems 50 (2) (2011) 511–521.

[12] P.-Y. Chen, S. Dhanasobhon, M.D. Smith, All reviews are not created equal: the disaggregate impact of reviews and reviewers at amazon.com, Available at SSRN, 2008. http://ssrn.com/abstract=918083.

[13] Y. Chen, J. Xie, Online consumer review: word-of-mouth as a new element of marketing communication mix, Management Science 54 (3) (2008) 477–491.

[14] Y.-H. Cheng, H.-Y. Ho, Social influence's impact on reader perceptions of online reviews, Journal of Business Research 68 (4) (2015) 883–887.

[15] JA. Chevalier. D. Mavzlin. The effect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (3) (2006) 345–354

[16] P.K. Chintagunta, S. Gopinath, S. Venkataraman, The efects of online user reviews on movie box ofice performance: accounting for sequential rollout and aggregation across local markets, Marketing Science 29 (2010) 944.

[17] R.B. Cialdini, N.J. Goldstein, Social influence: compliance and conformity, Annual Review of Psychology 55 (2004) 591–621

[18] B. De Langhe, P.M. Fernbach, D.R. Lichtenstein, Navigating by the stars: investigating the actual and perceived validity of online user ratings, Journal of Consumer Research 42 (6) (2016) 817–833

[19] C. Dellarocas, The digitization of word of mouth: promise and challenges of online feedback mechanisms, Management Science 49 (10) (2003) 1407–1424.

[20] M. Deutsch. H.B. Gerard, A study of normative and informational social influences upon individual judgment. The Journal of Abnormal and Social Psychology 51 (3) (1955) 629.

[21] S.T. Dumais, Latent semantic analysis, Annual Review of Information Science and Technology 38 (1) (2004) 188–230

[22] R. Filieri, What makes online reviews helpful? A diagnosticity-adoption framework to explain informational and normative influences in e-WOM. Journal of Business Research 68 (6) (2015) 1261–1270.

[23] K. Floyd, R. Freling, S. Alhoqail, H.Y. Cho, T. Freling, How online product reviews affect retail sales: a meta-analysis, Journal of Retailing 90 (2) (2014) 217–232

[24] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Information Systems Research 19 (3) (2008) 291–313-395

[25] D. Gefen, E. Karahanna, D.W. Straub, Trust and TAM in online shopping: an integrated model, MIS Quarterly 27 (1) (2003) 51–90.

[26] D. Gefen, K.R. Larsen, Controlling for lexical closeness in survey research: a demonstration on the technology acceptance model, Journal of the Association for Information Systems 18 (10) (2017) 727–757

[27] D. Gefen, J. Miller, J.K. Armstrong, F.H. Cornelius, N. Robertson, A. Smith McLallen, J.A. Taylor, Identifying patterns in medical records through latent se mantic analysis, Communications of the ACM 61 (6) (2018) 72–77.

[28] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Transactions on Knowledge and Data Engineering 23 (10) (2011) 1498–1512.

[29] A. Ghose, P.G. Ipeirotis, B. Li, Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content, Marketing Science 31 (3) (2012) 493–520.

[30] D. Godes, D. Mayzlin, Using online conversations to study word-of-mouth communication. Marketing Science 23 (2004) 545

[31] J. Hausser, K. Strimmer, Entropy inference and the James-Stein estimator, with application to nonlinear gene association networks, Journal of Machine Learning Research 10 (2009) 1469–1484

[32] Q.-C. He, Y.-J. Chen, Dynamic pricing of electronic products with consumer reviews, Omega 80 (2018) 123–134.

[33] T. Hennig-Thurau, K.P. Gwinner, G. Walsh, D.D. Gremler, Electronic word-of-mouth via consumer-opinion platforms: what motivates consumers to articulate them selves on the Internet? Journal of Interactive Marketing 18 (1) (2004) 38

[34] H. Hong, D. Xu, G.A. Wang, W. Fan, Understanding the determinants of online review helpfulness: a meta-analytic investigation, Decision Support Systems 102 (Supplement C) (2017) 1–11.

[35] M. Hu, B. Liu, Mining and summarizing customer reviews, ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2004, pp. 168–177 Seattle, WA

[36] N. Hu, N.S. Koh, S.K. Reddy, Ratings lead you to the product, reviews help you clinch it? The mediating role of online review sentiments on product sales. Decision Support Systems 57 (2014) 42–53

[37] H.H. Kelley, The processes of causal attribution, American Psychologist 28 (2) (1973) 107.

[38] G.J. Klir, Generalized information theory: aims, results, and open problems. Reliability Engineering and System Safety 85 (1) (2004) 21–38.

[39] N. Korfiatis, E. García-Bariocanal, S. Sánchez-Alonso, Evaluating content quality and helpfulness of online product reviews: the interplay of review helpfulness ys review content., Electronic Commerce Research and Applications 11 (3) (2012 205–217.

[40] N. Kumar, D. Venugopal, L. Qiu, S. Kumar, Detecting review manipulation on online platforms with hierarchical supervised learning, Journal of Management Information Systems 35 (1) (2018) 350–380

[41] T.K. Landauer, S.T. Dumais, A solution to Plato’s problem: the latent semantic analysis theory of acquisition, induction, and representation of knowledge, Psychological Review 104 (2) (1997) 211–240.

[42] T.K. Landauer, P.W. Foltz, D. Laham, An introduction to latent semantic analysis, Discourse Proceses 25 (2–3) (1998) 259–284.

[43] T.K. Landauer. D.S. McNamara. S. Dennis. W. Kintsch. Handbook of Latent Semantic Analysis. Psychology Press. New York. NY. 2013.

[44] J. Li. L. Zhan. Online persuasion: how the written word drives WOM. Journal of Advertising Research 51 (1) (2011) 239–257

[45] M. Li, L. Huang, C.-H. Tan, K.-K. Wei, Helpfulness of online product reviews as seen by consumers: source and content features, International Journal of Electronic Commerce 17 (4) (2013) 101–136.

[46] J. Liu, Y. Cao, C.-Y. Lin, Y. Huang, M. Zhou, Low-Quality Product Review Detection in Opinion Summarization, EMNLP-CoNLL, 2007, pp. 334–342.

[47] Y. Liu, Word of mouth for movies: its dynamics and impact on box ofice revenue, Journal of Marketing 70 (3) (2006) 74–89.

[48] Z. Liu, S. Park, What makes a useful online review? Implication for travel product websites, Tourism Management 47 (2015) 140–151.

[49] J. Machta, Entropy, information, and computation, American Journal of Physics 67 (12) (1999) 1074–1077.

[50] D. Mayzlin, Promotional chat on the internet, Marketing Science 25 (2) (2006) 155-163.201.

[51] J. McAuley, R. Pandey, J. Leskovec, Inferring networks of substitutable and com plementary products, Knowledge Discovery and Data Mining (2015) 1–10.

[52] J. McAuley, C. Targett, J. Shi, A. van den Hengel, Image-based recommendations on styles and substitutes, SIGIR, 2015, pp. 1–10.

[53] D.L. McFadden, K.E. Train, Consumers’ evaluation of new products: learning from self and others, Journal of Political Economy 104 (4) (1996) 683–703.

[54] D.H. McKnight, V. Choudhury, C. Kacmar, Developing and validating trust mea sures for E-commerce: an integrative typology, Information Systems Research 13 (3) (2002) 334–359.

[55], S.G. Moore, Attitude predictability and helpfulness in online reviews: the role of explained actions and reactions, Journal of Consumer Research 42 (1) (2015) 30-44.

[56], S.M. Mudambi, D. Schuff, What makes a helpful online review? A study of customer reviews on Amazon com, MIS Ouarterly 34 (1) (2010) 185–200

[57] B. News, Samsung Probed in Taiwan over 'fake Web Reviews. BBC News Technology, 2013.

[58] T.L. Ngo-Ye, A.P. Sinha, The influence of reviewer engagement characteristics on online review helpfulness: a text regression model, Decision Support Systems 61 (Supplement C) (2014) 47–58.

[59] Nielsen, Consumer Trust in Online, Social and Mobile Advertising Grows, Nielsen,

2012.

[60] A. Ortony, G. Clore, A. Collins, The Cognitive Structure of Emotions, Cambridge University Press, Cambridge, UK, 1988.

[61] Y. Pan, J.Q. Zhang, Born unequal: a study of the helpfulness of user-generated product reviews, Journal of Retailing 87 (4) (2011) 598–612.

[62] P.A. Pavlou, D. Gefen, Building efective online marketplaces with institution-based trust, Information Systems Research 15 (1) (2004) 37–59.

[63] P. Racherla, W. Friske, Perceived ‘usefulness’ of online consumer reviews: an exploratory investigation across three services categories, Electronic Commerce Research and Applications 11 (6) (2012) 548–559.

[64] J. Ross, The information content of accounting reports: an information theory perspective, Information 7 (3) (2016) 48.

[65] M. Salehan, D.J. Kim, Predicting the performance of online consumer reviews: a sentiment mining approach to big data analytics, Decision Support Systems 81 (2016) 30–40.

[66] R.M. Schindler, B. Bickart, Perceived helpfulness of online consumer reviews: the role of message content and style, Journal of Consumer Behaviour 11 (3) (2012) 234–243.

[67] S. Sen, D. Lerman, Why are you telling me this? An examination into negative consumer reviews on the Web, Journal of Interactive Marketing 21 (4) (2007) 76–94.

[69] C.E. Shannon, A mathematical theory of communication, Bell Systems Tech J 27 (1948) 379–423 (623-656).

[68] R.J. Senter, E.A. Smith, Automated Readability Index, DTIC Document, 1967.

[70] C. Shapiro, H.R. Varian, Information Rules, Harvard Business School Publications, Boston, MA, 1999.

[71] M. Siering, J. Muntermann, B. Rajagopalan, Explaining and predicting online review helpfulness: the role of content and reviewer-related signals, Decision Support Systems 108 (2018) 1–12

[72] J.P. Singh, S. Irani, N.P. Rana, Y.K. Dwivedi, S. Saumya, P. Kumar Roy, Predictin the “helpfulness” of online consumer reviews, Journal of Business Research 70 (2017) 346–355.

[73] J.M. Spool, The magic behind Amazon’s 2.7 billion dollar question, User Interface Engineering, User Interface Engineering, 2009.

[74] M. Taboada, J. Brooke, M. Tofiloski, K. Voll, M. Stede, Lexicon-based methods fo sentiment analysis, Computational Linguistics 37 (2) (2011) 267–307.

[75] Y. Wan, M. Nakayama, The reliability of online review helpfulness, Journal of Electronic Commerce Research 15 (3) (2014) 179

[76] P.F. Wu, In search of negativity bias: an empirical study of perceived helpfulness of online reviews, Psychology & Marketing 30 (11) (2013) 971–984.

[77] G. Yin, W. Liu, S. Zhu, What makes a helpful online review?—the perspective of

information adoption and social network, Library and Information Service 16 (2012) 140–147.

[78] L.A. Zadeh, Toward a generalized theory of uncertainty (GTU)––an outline, Information Sciences 172 (1) (2005) 1–40.

[79] D. Zhang, L. Zhou, J.L. Kehoe, I.Y. Kilic, What online reviewer behaviors really matter? Efects of verbal and nonverbal behaviors on detection of fake online re views, Journal of Management Information Systems 33 (2) (2016) 456–481

[80] S. Zhou, B. Guo, The order efect on online review helpfulness: a social influenc perspective, Decision Support Systems 93 (2017) 77–87.

[81] S. Zhou, Z. Qiao, Q. Du, G.A. Wang, W. Fan, X. Yan, Measuring customer agility from online reviews using big data text analytics, Journal of Management Information Systems 35 (2) (2018) 510–539.

[82] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating rol of product and consumer characteristics, Journal of Marketing 74 (2) (2010) 133–148.

[83] L. Zhu, G. Yin, W. He, Is this opinion Leader’s review useful? Peripheral cues for online review helpfulness, Journal of Electronic Commerce Research 15 (4) (2014) 267–280.

Dr. Jorge Fresneda is an Assistant Professor of Digital Marketing and Marketing Analytics in the Martin Tuchman School of Management at New Jersey Institute of Technology. He has 10 years of industry experience prior to taking his doctoral degree. His lectures and workshops are focus on practical applications of Artificial Intelligence, Text Mining, and Big Data Analytics tools. His main research focus is on the role of online information in e-commerce consumer decision making. Dr. Fresneda holds a PhD in Marketing from the LeBow College of Business at Drexel University, an MS in Applied Statistics from UNED, and an MA in Marketing and Sales Management from EAE Business School.

David Gefen, gefend@drexel.edu, is a Professor of MIS and the Provost Distinguished Research Professor at Drexel University, Philadelphia, PA. He teaches Business Analytics, Advanced Statistical Methods, Management and outsourcing of information systems, and the role of interpersonal trust and its management in ecommerce and IT management. Professor Gefen was a senior editor at MISQ and is on the editorial board of JMIS. Professor Gefen has authored some of the most cited papers in MIS on trust management in information systems, ecommerce and online markets management. His research findings have been published in some of the leading journals, including MISQ, ISR, IEEE TEM, JMIS, and Omega. Professor Gefen is an author of a textbook on VB.NET Programming and a book on the Art of IS Outsourcing.
