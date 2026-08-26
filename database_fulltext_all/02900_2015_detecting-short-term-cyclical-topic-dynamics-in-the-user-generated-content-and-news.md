---
otero_id: 2900
otero_key: "ZFKJMNJD"
title: "Detecting short-term cyclical topic dynamics in the user-generated content and news"
authors: "Hsin-Min Lu"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.11.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Detecting short-term cyclical topic dynamics in the user-generated content and news

Hsin-Min Lu ⁎

Department of Information Management, National Taiwan University, Taipei 106, Taiwan

a r t i c l e i n f o

Article history: Received 6 June 2014 Received in revised form 22 October 2014 Accepted 30 November 2014 Available online 6 December 2014

Keywords: Topic models Gibbs sampling Temporal dynamics Context dependent Cyclical dynamics

## a b s t r a c t

With the maturation of the Internet and the mobile technology, Internet users are now able to produce and consume text data in different contexts. Linking the context to the text data can provide valuable information regarding users' activities and preferences, which are useful for decision support tasks such as market segmentation and product recommendation. To this end, previous studies have proposed to incorporate into topic models contextual information such as authors' identities and timestamps. Despite recent efforts to incorporate contextual information, few studies have focused on the short-term cyclical topic dynamics that connect the changes in topic occurrences to the time of day, the day of the week, and the day of the month. Short-term cyclical topic dynamics can both characterize the typical contexts to which a user is exposed at different occasions and identify user habits in speci<sup>fi</sup>c contexts. Both abilities are essential for decision support tasks that are context dependent. To address this challenge, we present the Probit-Dirichlet hybrid allocation (PDHA) topic model, which incorporates a document's temporal features to capture a topic's short-term cyclical dynamics. A document's temporal features enter the topic model through the regression covariates of a multinomial-Probit-like structure that in<sup>fl</sup>uences the prior topic distribution of individual tokens. By incorporating temporal features for monthly, weekly, and daily cyclical dynamics, PDHA is able to capture interesting short-term cyclical patterns that characterize topic dynamics. We developed an augmented Gibbs sampling algorithm for the non-Dirichlet-conjugate setting in PDHA. We then demonstrated the utility of PDHA using text collections from user generated content, newswires, and newspapers, Our experiments show that PDHA achieves higher hold-out likelihood values compared to baseline models, including latent Dirichlet allocation (LDA) and Dirichlet-multinomial regression (DMR). The temporal features for short-term cyclical dynamics and the novel model structure of PDHA both contribute to this performance advantage. The results suggest that PDHA is an attractive approach for decision support tasks involving text mining.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Making informed decisions in our current fast-changing environment often demands the timely and comprehensive analysis of large amounts of text data. Researchers have attempted to address this challenge by developing text mining approaches such as topic models [1]. Topic models, including latent Dirichlet allocation (LDA) and its variations [2,3], have been applied to discover coherent topics, analyze trends in academic publications [4], and examine user-generated content from different sources [5].

Additional contextual information that signals the unobservable structures beneath the observed textual data can help a model extract better latent topics. Thus, an emerging research direction in topic models is to incorporate contextual information such as authors' identities and timestamps to extract latent topics that reveal the in<sup>fl</sup>uence of changing contexts. For example, incorporating the authors' identities into a topic model [6] can improve performance because an author's specialties can reveal additional information regarding the latent topics of the document.

Incorporating contextual information into topic models also provides a direct route for topic models to support decision making. As a generative probabilistic model, the learned topic model is essentially the joint distribution of contextual information and textual data. By computing the conditional distributions of contextual information given observed textual data, a topic model can provide crucial information that supports decision-making employing contextual information. For example, by incorporating additional information of microblog users who shared news articles online, a model is able to recommend news articles to other microblog users who may have similar interests [7].

Despite recent progressions, few studies have focused on the shortterm cyclical topic dynamics that connect changing topic occurrences to the time of day, the day of the week, and the day of the month. Content generated by social media and mobile platforms often reveal strong short-term cyclical dynamics because users' day-to-day routines heavily in<sup>fl</sup>uence the contexts of use, which contribute to the variations of topic occurrence. By including short-term cyclical dynamics in a topic model, we are able to better characterize the cyclical dynamics that re<sup>fl</sup>ect users' activities, habits, and preferences [8], three factors that can improve decision support tasks such as market segmentation [9] and product recommendation [10].

To <sup>fi</sup>ll this gap, we introduce a new family of topic models that can discover short-term cyclical patterns from a document collection. The proposed Probit-Dirichlet hybrid allocation (PDHA) provides a general framework with which to link discrete and continuous documentspeci<sup>fi</sup>c exogenous temporal features to topic distributions. PDHA includes features for daily, weekly, and monthly cyclical patterns as a way of capturing short-term dynamics. In addition to the topic–token distributions and document–topic mixes provided by a typical topic model, PDHA learns the coef<sup>fi</sup>cients of these temporal features through a multinomial Probit-like structure; these coef<sup>fi</sup>cients can reveal the occurrences of topic changes within a day, week, or month. Unlike the topic over time (TOT) [11] and dynamic topic model (DTM) [12], which focus more on the long-term evolution of topics, PDHA can model short-term cyclical variations that may be harder to capture using other <sup>fl</sup>avors of topic models. Moreover, our PDHA model includes random variables for document-speci<sup>fi</sup>c topic tendencies. These random variables allow each document to deviate from the mean tendency speci<sup>fi</sup>ed by the temporal features while preserving a common theme for each document.

In the subsequent sections, we <sup>fi</sup>rst review previously proposed time-dependent topic models. We then present the PDHA model and discuss in detail the Gibbs sampling algorithm. Afterward, we present experimental results that incorporate daily, weekly, and monthly cyclical patterns. We conclude with a short discussion of future research directions.

## 2. Literature review

Topic models [1,4] are a family of algorithms aimed at discovering latent structures in large document collections. Based on the assumption that observed tokens are governed by latent topics, topic models de<sup>fi</sup>ne a generative process that <sup>fi</sup>rst generates the mixture of topics in a document and then select observed tokens conditioned on latent topics. The data generating process provides a rich structure that is capable of capturing meaningful latent topical structures in documents. Compared to their predecessors, such as the probabilistic latent semantic indexing (pLSI), topic models do not have the over-<sup>fi</sup>tting problem and outperform pLSI in terms of perplexity [1].

The original topic models are often referred to as the latent Dirichlet allocation (LDA) because they adopt the conjugate prior for multinomial distribution, the Dirichlet distribution, to simplify computation. The idea of capturing short-term cyclical dynamics is related to the research stream that incorporates additional time-dependent information to improve LDA models. We review selected time-dependent topic models in this section. We refer readers to Blei [13] for a general introduction of topic models.

## 2.1. Time-dependent topic models

We start with an overview of the LDA model and then extend it to time-dependent topic models. For a document collection that contains D documents indexed by integers $1 , 2 , . . . , \mathrm { D } , \mathrm { L D A }$ assumes that the $N _ { d }$ tokens in the document $d , w _ { d } = ( w _ { d 1 } , w _ { d 2 } , . . . , w _ { d N _ { d } } )$ , were generated by <sup>fi</sup>rst drawing the topic mix $\theta _ { d } \sim D i r ( \alpha )$ , where Dir(α) is a Dirichlet distribution with symmetric concentration parameter α. The topic mix $\theta _ { d }$ is a vector of length J, where J is the total number of topics in a document collection. Each element of $\theta _ { d }$ is the probability of selecting the corresponding topic for a position in document d. All elements of θ sum to one.

The second step is to determine the topic for a token at position i, $1 \leq i \leq N _ { d } ,$ by drawing $z _ { d i } \sim M u l t i n o m i a l ( \theta _ { d } )$ . This process assumes that given the topic mix $\theta _ { d } ,$ , the latent topic for each token in document d is independent of one another. Finally, a token at position i is determined by drawing from the corresponding topic–token distribution $w _ { d i } \sim M u l t i n o m i a l \left( \phi _ { z _ { d i } } \right)$ , where $\phi _ { z _ { d i } }$ is a vector determining the probability that a token may appear given $z _ { d i }$ , the topic at position i of document d. The length of each $\phi _ { j }$ is the vocabulary size W for $j =$ $0 , 1 , . . . , J - 1$ . The model assumes that each $\phi _ { j }$ is generated from a Dirichlet distribution with a symmetric concentration parameter β.

The generative process can be represented using the plate notation shown in Fig. 1. The shaded circle indicates observed variables, and the open circles indicate latent variables and parameters. Starting from the upper left, Panel (A) in Fig. 1 provides a summary for the data-generating process described above.

In the subsequent discussion, variables such as $z _ { d i }$ and $\theta _ { d }$ should be regarded as latent variables because the number of these variables grow with the size of the dataset [14]. Other variables, including α, $\beta ,$ and $\phi _ { z _ { d i } }$ are regarded as parameters. The joint distribution of observed tokens, latent topic variables and other parameters conditional on α and $\beta$ is given by:

$$
p (\theta , \phi , Z, w | \alpha , \beta) = \prod_ {d = 1} ^ {D} p (\theta_ {d} | \alpha) \prod_ {j = 0} ^ {J - 1} p \left(\phi_ {j} | \beta\right) \prod_ {i = 1} ^ {N _ {d}} p (z _ {d i} | \theta_ {d}) p \left(w _ {d i} | \phi_ {z _ {d i}}\right),\tag{1}
$$

where $\boldsymbol { \theta } = ( \theta _ { 1 } , \theta _ { 2 } , . . . , \theta _ { D } ) , \boldsymbol { \phi } = ( \phi _ { 1 } , \phi _ { 2 } , . . . , \phi _ { J } ) , \boldsymbol { w } = ( w _ { 1 } , w _ { 2 } , . . . , w _ { D } ) , \boldsymbol { Z } =$ $( z _ { 1 } , z _ { 2 } , . . . , z _ { D } )$ , and $\boldsymbol { z _ { d } } = \left( z _ { d 1 } , z _ { d 2 } , . . . , z _ { d N _ { d } } \right)$ . One challenge presented by topic models is to design ef<sup>fi</sup>cient and effective algorithms for estimat ing $\theta ,$ ϕ, and Z given w, α, and $\beta .$ We will review model estimation methods later.

The LDA model does not explicitly include temporal features. However, simple post-processing can be used to determine time trends. As demonstrated by Grif<sup>fi</sup>ths and Steyvers [4], the estimated $\theta _ { d }$ for individual documents can be averaged by year to identify the trending topics across the sample period. This post-processing approach, however, is unable to take advantage of the potential time-dependent clusters naturally occurring in datasets.

Two types of time-dependence structures, upstream and downstream, can incorporate temporal features (see Fig. 2) [3]. The upstream structure allows the temporal features (e.g., timestamps) to in<sup>fl</sup>uence the topic–mix distribution of a document, thereby determining the latent topics and tokens in a document. The downstream structure, in contrast, generates both tokens and timestamps conditioned on a latent topic. We <sup>fi</sup>rst introduce TOT, a downstream model, followed by two upstream models, temporal collection (TC) and DTM.

The TOT model (see Panel (B) of Fig. 1) associates the document timestamp to every token in the document. It assumes that the topic mix of a document determines the latent topic at each position, which subsequently determines the observed tokens and the timestamp [11]. This model has a downstream structure because the topic mix $\left( \theta _ { d } \right)$ ) determines the distribution of observed tokens $( w _ { d i } )$ and timestamps $\left( t _ { d i } \right)$ [3]. The additional timestamp variables in TOT allow the discovery of time-sensitive topics. One example is discovering topics over 21 decades of U.S. Presidential State-of-the-Union Addresses. The LDA model combines statements about the Mexican-American War (1846– 1848) with those about World War I. The result is in contrast with topics discovered by TOT. TOT is able to localize statements about the Mexican-American War [11] and considers statements about World War I as belonging to a different topic because of the time gap between the two wars.

The temporal collection (TC) model [5] is based on similar ideas but instead adopts an upstream structure. The timestamp variable t enters the topic model under the assumption that the parameters of the prior distribution of topic mix, α, are a function of t. As a result, t in<sup>fl</sup>uences the topic mix of document d, $\theta _ { d } ,$ the latent topics, and the observed tokens. TC adopts the gamma distribution to model timedependent topic occurrence.

![](/api/attachments/ZFKJMNJD/fulltext/images/1193e16d36399efe754a9b3ea3405e7a4106f53cd95b4a82af2834cb9ca3fe69.jpg)  
(A) Latent Dirichlet Allocation (LDA)

![](/api/attachments/ZFKJMNJD/fulltext/images/59f75d35714c47ea84e73e6fa295ceb626fcf4e0c8c53774dc4fd6ada04cbd58.jpg)

![](/api/attachments/ZFKJMNJD/fulltext/images/e370323cbab3db880248df8e7c68e6e67037b2b90cc0a583809ed4e936e19f4f.jpg)  
(C) The Dynamic Topic Model (DTM)  
Fig. 1. Selected time-dependent topic models

A somewhat different approach is adopted in DTM [12]. DTM assumes that both topic occurrence and topic-token distributions (i.e., topic meanings) can change over time. In this way, DTM is different from TOT and TC, which have <sup>fi</sup>xed topic-token distributions but changing topic occurrences. One implication of changing topic-token distribution is that the meaning of a given topic can change substantially over a long time period. While this characteristic may be useful in some situations, it can lead to DTM accidentally piecing together unrelated topics across time. More studies are needed to determine whether an evolving topic-token distribution is a reasonable assumption.

## 2.2. Inference for time-dependent topic models

The insights the topic models provide come from the estimated latent variables and parameters given the observed documents. As an illustrative example, consider the LDA model discussed above. The key problem is to compute the joint posterior probability distribution of latent variables and parameters given w (the observed documents):

$$
p (\theta , \phi , Z | w, \alpha , \beta) = \frac {p (\theta , \phi , z , w | \alpha , \beta)}{p (w | \alpha , \beta)},\tag{2}
$$

where p(θ, ϕ, Z, w|α, β) is de<sup>fi</sup>ned in Eq. (1) and p(w|α, β) can be computed from p(θ, ϕ, z, w|α, β) by integrating out θ, ϕ, and Z. The TOT model has a similar structure but contains additional parameters from the beta distributions; these additional parameters generate the normalized timestamps. The TC model needs to include additional parameters and latent variables that control the time-dependent topic occurrence. The DTM model has a dynamic structure that further complicates the estimation problem. Each period t has vectors α and β that need to be estimated.

![](/api/attachments/ZFKJMNJD/fulltext/images/f975ce3c9e383917ddf3515e16aae88e05d7e12ccd1cb26aeae0ce8ccd6cfa79.jpg)  
Fig. 2. Upstream and downstream time-dependent structures.

The inference methods for topic models fall roughly into two types: sampling-based algorithms and variational algorithms. A samplingbased algorithm constructs a Markov chain whose limiting distribution is the joint posterior of latent variables and parameters [15,16]. This type of algorithm can approximate the joint posterior to an arbitrary precision given unlimited computing resources. In practice, a <sup>fi</sup>xed number of iterations will collect enough samples for subsequent inference tasks.

A variational algorithm [17] is a deterministic approach that searches for the best solution in a restricted family of probability distributions that is “simpler” compared to the joint posterior of latent variables and parameters. The nature of a variational algorithm is optimization. Noteworthy is that the solutions found by variational algorithms live in the restricted family of the probability distribution. The solution is, in general, not the mode of the joint posterior of latent variables and parameters. Whether the solutions found by variational algorithms are adequate is an empirical question.

One interesting question concerns the relative performance of the estimation approaches. Previous studies have shown that collapsed Gibbs sampling outperforms variational Bayes in terms of perplexity [4,18]. However, collapsed Gibbs sampling can require a longer running time to ensure convergence. The stochastic EM algorithm allows for the adjustment of parameters that are <sup>fi</sup>xed in collapsed Gibbs sampling; this can have a positive impact on model performance [3].

## 2.3. Comparison of time-dependent topic models

To allow for a better understanding of the current status of timedependent topic models, I discuss the following important characteristics of time-dependent topic models: time range, time-dependent structure, topic–token evolution, continuous or discrete time, timedependent topic occurrence, and model estimation methods. Table A.1 in Appendix A provides a summary of time-dependent topic models based on these characteristics.

Time range characterizes the rough time interval from which the dynamic is considered. LDA relies on post-processing to capture the dynamic and, thus, does not have a target time range. DTM needs to <sup>fi</sup>rst divide a dataset into discrete time intervals and aims at long-term topic dynamics that cover decades of documents. TOT also focuses on long-term topic clusters that can span months or years. TC targets medium-term changes across days or months. Short-term dynamics, ranging from hours to days, do not receive much attention in this research stream.

Noteworthy is that the discussion on time range is based on the model characteristics and the experiments conducted using these models. These time ranges are often the typical use cases intended in the original design. Adopting a model to different time ranges is possible and might be worth further investigation.

The time-dependent structure provides a channel for topic models to incorporate time-sensitive topic occurrences. As discussed in the previous subsection, this can be achieved through an upstream or downstream structure. The TOT model has a downstream structure while DTM and TC adopt an upstream structure. The upstream structure is consistent with the intuition that timestamps “in<sup>fl</sup>uence” topics instead of the other way around. It also provides a clean analytical structure for model inference.

Previous studies adopted two types of granularity in the timedependent structure: document-level and token-level. Documentlevel granularity assumes that every token in a document has the same temporal features while token-level granularity allows different feature values for tokens in a document. The dependence structure of the DTM and TC models is at document-level, while the timestamp in TOT is at token-level. Token-level dependence has the potential to provide more detailed information but can require additional computing resources.

Topic–token distributions determine the meanings of topics. Most time-dependent topic models, including TOT and TC, adopt <sup>fi</sup>xed topic–token distributions. The meaning of a topic, as a result, is the same across time. The time-dependent topic occurrence determines the chance of encountering a topic at a given time. A topic might not be associated with a document if the topic is no longer active. Evolving topic–token distribution, on the other hand, allows the meaning of a topic to change over time. DTM adopts an evolving topic–token and topic occurrence setting.

A time-dependent topic model can adopt discrete or continuous time. A continuous time model allows the timestamp to enter the model directly without the need to be discretized. Both TOT and TC are continuous time models while DTM is a discrete time model. DTM, as a result, needs to determine the time interval for discretization before model inference. The continuous time dynamic topic model (cDTM) addresses this issue by relaxing the time-dependent structure of topic–token distributions [19]. The cDTM model allows for different time intervals between observations. Longer time intervals are associated with larger variances.

Time-dependent topic occurrences allow the occurrence rate of a topic to change over time. TOT adopts the beta distribution to model the normalized timestamp so that time-dependent clusters can be better captured. TC adopts the gamma distribution for a similar purpose. DTM model adopts the random walk process for changing topic occurrence. The cDTM model does not include this type of timedependency structure but instead focuses on changing topic–token distributions.

Previous studies on time-dependent topic models have mostly focused on long-term (months-to-years) to median-term (days-tomonths) dynamics; few studies have focused on short-term dynamics (hours-to-days). Both TOT and TC use single-modal (beta and gamma) distributions to model time-dependent topic occurrence. DTM adopts a random walk process for the same purpose. These approaches are unsuitable for modeling cyclical topic occurrence patterns. This study addresses the gap in the previous studies and proposes a novel topic model that can capture short-term cyclical topic dynamics in large document collections.

![](/api/attachments/ZFKJMNJD/fulltext/images/872adb2db7ed971bdd4cbff417b39453addc5841bc9b8f8dc4770e1f322e4fa6.jpg)

## 3. Probit-Dirichlet hybrid allocation (PDHA)

The basic idea of PDHA is to adopt a multinomial Probit-like structure so that temporal features can in<sup>fl</sup>uence the latent topic of each token. PDHA has a token-level upstream structure, which is different from other time-dependent topic models. Table A.1 in Appendix A provides a summary of the differences between PDHA and existing time-dependent topic models.

This section presents the general structure of PDHA, followed by the temporal features incorporated for short-term cyclical patterns. We then discuss augmented Gibbs sampling for model inference. To streamline the discussion, it is assumed that all tokens in a document have the same temporal features. Extending this to the case of having different feature values for each token is straightforward.

## 3.1. The general structure of PDHA

The data-generating process (DGP) of PDHA is similar to that of the original LDA model. The main difference is how the temporal features affect topic distributions. In the following discussion, the J latent topics are indexed from 0 to J − 1. The topic index starts from zero instead of one to facilitate the subsequent discussion of Probit-based topic generation de<sup>fi</sup>ned by Eqs. (3) and (4). Fig. 3 plots the PDHA model in plate notation. The tokens in a document $( w _ { d i } )$ and their temporal feature vectors (x ) are observable in PDHA. Other latent variables, including the latent topic $z _ { d i } ,$ are unobservable and require estimation. PDHA assumes that a document is associated with a documentspeci<sup>fi</sup>c topic tendency vector $q _ { d } = ( q _ { d , 1 } , q _ { d , 2 } , . . . , q _ { d , J - 1 } )$ . Each element $q _ { d , j } ( \mathrm { j } = 1 , 2 , . . . , J { - } 1 )$ is normally distributed with variance $s _ { q } ^ { 2 }$ and mean zero. The other source of in<sup>fl</sup>uence comes from the temporal feature vector $x _ { d i }$ and its weight $g _ { j } ( \mathrm { j } = 1 , 2 , . . . , J { - } 1 )$ . For a token at position i of document d, the latent topic $z _ { d i }$ is generated by drawing from a multinomial distribution with parameters that are a function of $q _ { d } , x _ { d i } , g _ { j } ,$ and $\Sigma _ { j } .$ The token can then be generated by drawing from a multinomial distribution with the probability vector $\phi _ { z _ { d i } } .$

The key idea of PDHA is that the sub-problem of generating ${ z _ { d i } }$ given temporal features resembles a classi<sup>fi</sup>cation problem (e.g., [20]). The main difference is that the outcome variable $z _ { d i }$ in this classi<sup>fi</sup>cation problem is unobservable in the larger model de<sup>fi</sup>ned by PDHA. As a result, it is dif<sup>fi</sup>cult to extend a classi<sup>fi</sup>cation model directly into a topic model that incorporates token-level temporal features. However, because Gibbs sampling allows for approximating a larger model by drawing from the posteriors of smaller sub-problems, PDHA can be considered a classi<sup>fi</sup>cation sub-problem coupled with a tokengenerating structure if the latent topic $z _ { d i }$ can be treated as observable in the classi<sup>fi</sup>cation sub-problem during model inference using Gibbs sampling. This line of reasoning leads to the adoption of multinomial Probit regression in the classi<sup>fi</sup>cation sub-problem of PDHA due to the development of Gibbs sampling-based inference for multinomial Probit regression (Imai and Dyk [21], and Albert and Chib [22]).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Document-specific variables for cyclical patterns:  
$x_{di}^{T} = (1,x_{di,1}^{T},x_{di,2}^{T},x_{di,3}^{T})$;  
Daily: $x_{di,1}^{T} = (\cos \left(2\pi \frac{hd_{d}}{24}\right),\sin \left(2\pi \frac{hd_{d}}{24}\right))$ $hd_{d}$: time of day in hour, starting from midnight  
Weekly: $x_{di,2}^{T} = (w1_{d},w3_{d},w4_{d},w5_{d},w6_{d},w7_{d})$ $wa_{d}$: day-of-the-week dummy, a = 1,3,4,5,6,7.  
Monthly: $x_{di,3}^{T} = (\cos \left(2\pi \frac{md_{d}}{ml_{d}}\right),\sin \left(2\pi \frac{md_{d}}{ml_{d}}\right))$ $md_{d}$: day of the month  
$ml_{d}$: number of day in the month
</div>

Fig. 3. Probit-Dirichlet hybrid allocation (PDHA).

![](/api/attachments/ZFKJMNJD/fulltext/images/a26002bd89c969ac56b9891666fa61c957442b3ba606f92d05410401682c2b04.jpg)

![](/api/attachments/ZFKJMNJD/fulltext/images/592f1c6e89a8b8af6445282d15b1b46ca62254091d4a59dafc6b6b4a1d09eca1.jpg)  
(A) PDHA as a classification problem coupled with a token-generating problem  
(B) PDHA augmented with additional latent variable for topic generation  
Fig. 4. Two sub-problems of PDHA.

Panel (A) of Fig. 4 plots the classi<sup>fi</sup>cation sub-problem and tokengenerating sub-problem in PDHA. The upper-half is a multinomial Probit regression model while the lower-half resembles LDA. Following the speci<sup>fi</sup>cation of multinomial Probit regression, the probability of selecting a latent topic for ${ z _ { d i } }$ is de<sup>fi</sup>ned by an additional latent vector $H _ { d i } \equiv ( H _ { d i , 1 } , H _ { d i , 2 } , \dots , H _ { d i , J - 1 } )$

$$
H _ {d i, j} = q _ {d, j} + x _ {d i} ^ {T} g _ {j} + e _ {d i, j}; \cdot j = 1, 2, \dots , J - 1,\tag{3}
$$

where $\mathbf { e } _ { \mathrm { d i , j } } \sim N ( 0 , \Sigma _ { j } )$ is white noise. The latent topic ${ \cal Z } _ { d i }$ is then determined by inspecting the relative value of $H _ { d i }$ and assigning the topic by:

$$
z _ {d i} = Y (H _ {d i}) = \left\{ \begin{array}{l l} 0, & \text { if } \quad \max (H _ {d i}) \leq 0 \\ j, & \text { if } \quad \max (H _ {d i}) = H _ {d i, j} > 0, \end{array} \right.\tag{4}
$$

The augmented vector $H _ { d i }$ bridges the discrete topic assignment $z _ { d i }$ and other document-speci<sup>fi</sup>c variables. As de<sup>fi</sup>ned by $Y ( \cdot )$ in Eq. $( 4 )$ the J-1 elements in $H _ { d i }$ compete for topic assignment, and the one with the highest positive value “wins.” The <sup>fi</sup>rst topic (that of index 0) is assigned if all of the elements in $H _ { d i }$ are negative. The vector $g _ { j }$ determines the effect of $x _ { d i }$ on topic j. The <sup>fi</sup>rst element in $g _ { j } \ ( \mathrm { i } . \mathrm { e } . , g _ { j , 1 } )$ is the corpora-wide proportion of topic j. Other things being equal, a higher $g _ { j , 1 }$ leads to a higher proportion of tokens associated with topic j in a document collection. The document-speci<sup>fi</sup>c $q _ { d , j }$ in<sup>fl</sup>uences the proportion of topic j in tokens from document d.

Note that the token-level white noise $e _ { d i , j }$ introduces the variation of topics within a document given the document-level mean topic tendency de<sup>fi</sup>ned by $q _ { d , j } + x _ { d i } g _ { j }$ when all tokens in a document have the same $x _ { d i \cdot }$ The latent topics of tokens in the same document can differ because each token is associated with a different white noise. Following the speci<sup>fi</sup>cations of Imai and Dyk [21] for multivariate probit regression, the <sup>fi</sup>rst white noise has unit variance $( \mathsf { V a r } ( e _ { d i , 1 } ) = 1 )$ ), which makes the model identi<sup>fi</sup>able.

## 3.2. Temporal features for short-term cyclical dynamics

There are two common approaches to model cyclical patterns. The <sup>fi</sup>rst approach is to use dummy variables (i.e., indication variables). For example, 6 dummy variables can describe different topic occurrence rates across the 7 days in a week. The other approach is to adopt the Ser<sup>fl</sup>ing model [23]. The basic idea of the Ser<sup>fl</sup>ing model is to use appropriate sine and cosine functions to capture the cyclical patterns of selected frequencies. Consider a document d with time of day $h d _ { d }$ (in hours; starting from midnight), $0 \leq h d _ { d } < 2 4$ . Then $\begin{array} { r } { a _ { 1 } \cos \left( \frac { 2 \pi h d _ { d } } { 2 4 } \right) + b _ { 1 } \sin \left( \frac { 2 \pi h d _ { d } } { 2 4 } \right) } \end{array}$ can be used to capture the daily cyclical pattern. The coef<sup>fi</sup>cients $a _ { 1 }$ and $b _ { 1 }$ are estimated from training data. Similarly, monthly cyclical patterns can be captured by $\begin{array} { r l r } {  { a _ { 2 } \cos ( 2 \pi \frac { m d _ { d } } { m l _ { d } } ) + b _ { 2 } \sin ( 2 \pi \frac { m d _ { d } } { m l _ { d } } ) } } \end{array}$ , where $m d _ { d }$ is the day of the month of document d, and $m l _ { d }$ is the total number of days in the corresponding month.

For a document d that contains timestamps up to minutes, the temporal features for daily, weekly, and monthly cyclical patterns are

$$
\begin{array}{c} x _ {d i} ^ {T} = (1, \cos \left(2 \pi \frac {h d _ {d}}{2 4}\right), \sin \left(2 \pi \frac {h d _ {d}}{2 4}\right), w 1 _ {d}, w 3 _ {d}, w 4 _ {d}, w 5 _ {d}, w 6 _ {d}, w 7 _ {d}, \\ \cos \left(2 \pi \frac {m d _ {d}}{m l _ {d}}\right), \sin \left(2 \pi \frac {m d _ {d}}{m l _ {d}}\right)). \end{array}\tag{5}
$$

Table 1 Research testbeds

<table><tr><td>Dataset</td><td># of doc.</td><td># of tokens</td><td># of unique tokens</td><td>Temporal features</td><td>Remarks</td></tr><tr><td>WMT</td><td>24,995</td><td>825,653</td><td>37,315</td><td>Day of the week, day of the month, and time of day</td><td>Postings on the Yahoo Finance Wal-Mart message board from 1/1/2007 midnight to 5/1/2007 midnight (Eastern Time)</td></tr><tr><td>NYT</td><td>4224</td><td>1,056,717</td><td>59,830</td><td>Day of the week and day of the month</td><td>10% random sample of NYT articles from 1/1/2008 to 6/30/2008</td></tr><tr><td>RTS</td><td>11,771</td><td>775,553</td><td>26,898</td><td>Day of the week, day of the month, and time of day</td><td>Reuters-21578</td></tr></table>

![](/api/attachments/ZFKJMNJD/fulltext/images/4c749cf8d73e1f31af1e3be85bb07f4534830e84c861bf61fef390bee4ab5f94.jpg)  
Regression Parameters:

![](/api/attachments/ZFKJMNJD/fulltext/images/15d1a9ba39916af6cdefede6622fbe06eacc993f6976bce99fe36915ffc74548.jpg)  
(A)  
Top Keyword Probability:

<table><tr><td>Variable</td><td>Est. Value</td><td>t-value $^{1}$ </td></tr><tr><td>const.</td><td>-1.434***</td><td>-2260.4</td></tr><tr><td>w7</td><td>-0.106***</td><td>-13.4</td></tr><tr><td>w1</td><td>0.064***</td><td>7.1</td></tr><tr><td>w3</td><td>0.038***</td><td>6.1</td></tr><tr><td>w4</td><td>0.143***</td><td>20.6</td></tr><tr><td>w5</td><td>-0.007</td><td>-0.9</td></tr><tr><td>w6</td><td>-0.109***</td><td>-17.1</td></tr><tr><td>Mcos $^{\dagger}$ </td><td>0.011***</td><td>2.6</td></tr><tr><td>Msin $^{\dagger}$ </td><td>0.196***</td><td>35.4</td></tr><tr><td>Hcos $^{\ddagger}$ </td><td>-0.209***</td><td>-24.3</td></tr><tr><td>Hsin $^{\ddagger}$ </td><td>0.226***</td><td>36.8</td></tr></table>

![](/api/attachments/ZFKJMNJD/fulltext/images/0bdda238ab4eefefe22ca4bb40240925c1f748613edfc9cb2fff0f8afa9e62e7.jpg)  
<sup>†</sup>For monthly cyclical patterns.  
<sup>‡</sup>For daily cyclical patterns.  
¹Computed using time-series corrected standard error.  
<sup>\*\*\*,</sup> <sup>\*\*,</sup> and <sup>\*</sup> indicate significant at the 99%, 95%,  
and 90% confidence levels.

(B)

<table><tr><td>Word</td><td>Prob.</td><td>2.5% Percentile</td><td>97.5% Percentile</td></tr><tr><td>sales</td><td>0.0365</td><td>0.0348</td><td>0.0383</td></tr><tr><td>year</td><td>0.0312</td><td>0.0298</td><td>0.0329</td></tr><tr><td>growth</td><td>0.0211</td><td>0.0204</td><td>0.0220</td></tr><tr><td>percent</td><td>0.0193</td><td>0.0177</td><td>0.0206</td></tr><tr><td>stores</td><td>0.0176</td><td>0.0156</td><td>0.0190</td></tr><tr><td>billion</td><td>0.0161</td><td>0.0148</td><td>0.0180</td></tr><tr><td>years</td><td>0.0130</td><td>0.0114</td><td>0.0146</td></tr><tr><td>store</td><td>0.0129</td><td>0.0111</td><td>0.0142</td></tr><tr><td>stock</td><td>0.0117</td><td>0.0105</td><td>0.0131</td></tr><tr><td>company</td><td>0.0092</td><td>0.0074</td><td>0.0109</td></tr><tr><td>earnings</td><td>0.0082</td><td>0.0072</td><td>0.0089</td></tr><tr><td>target</td><td>0.0081</td><td>0.0067</td><td>0.0095</td></tr></table>

Number of significant tokens in this topic: 284

![](/api/attachments/ZFKJMNJD/fulltext/images/b3030710c8cb0df01b145e5babc821f1c5da1e09202f72bc6fc1b93b1e4f8c35.jpg)

Regression Parameters:

<table><tr><td>Variable</td><td>Est. Value</td><td>t-value $^{1}$ </td></tr><tr><td>const.</td><td>-1.438***</td><td>-903.3</td></tr><tr><td>w7</td><td>-0.011*</td><td>-1.9</td></tr><tr><td>w1</td><td>0.001</td><td>0.2</td></tr><tr><td>w3</td><td>-0.004</td><td>-0.8</td></tr><tr><td>w4</td><td>-0.045***</td><td>-7.3</td></tr><tr><td>w5</td><td>-0.052***</td><td>-7.0</td></tr><tr><td>w6</td><td>-0.048***</td><td>-8.1</td></tr><tr><td>Mcos $^{\dagger}$ </td><td>0.052***</td><td>12.4</td></tr><tr><td>Msin $^{\dagger}$ </td><td>-0.013***</td><td>-3.4</td></tr><tr><td>Hcos $^{\ddagger}$ </td><td>-0.029***</td><td>-5.1</td></tr><tr><td>Hsin $^{\ddagger}$ </td><td>0.049***</td><td>12.1</td></tr></table>

<sup>†</sup>For monthly cyclical patterns.  
<sup>‡</sup>For daily cyclical patterns.  
¹Computed using time-series corrected standard error.  
申率率 <sup>,</sup> and <sup>\*</sup> indicate significant at the 99%, 95%, and 90% confidence levels.

(B)  
(C)  
Fig. 5. Topic “earnings” from WMT.  
![](/api/attachments/ZFKJMNJD/fulltext/images/04249f07b4d56c7893e134f930461925a766cff761ca5eeea64e6a02f5d55633.jpg)  
(A)

![](/api/attachments/ZFKJMNJD/fulltext/images/48bd85487572b14423c56f25f1af7e0ff7715a671ed27ac8042a987c7c3f31af.jpg)

Top Keyword Probability:

<table><tr><td>Word</td><td>Prob.</td><td>2.5% Percentile</td><td>97.5% Percentile</td></tr><tr><td>people</td><td>0.0200</td><td>0.0180</td><td>0.0219</td></tr><tr><td>time</td><td>0.0130</td><td>0.0104</td><td>0.0145</td></tr><tr><td>business</td><td>0.0113</td><td>0.0092</td><td>0.0133</td></tr><tr><td>make</td><td>0.0105</td><td>0.0098</td><td>0.0115</td></tr><tr><td>work</td><td>0.0092</td><td>0.0053</td><td>0.0147</td></tr><tr><td>pay</td><td>0.0081</td><td>0.0049</td><td>0.0119</td></tr><tr><td>good</td><td>0.0076</td><td>0.0055</td><td>0.0090</td></tr><tr><td>back</td><td>0.0066</td><td>0.0039</td><td>0.0081</td></tr><tr><td>company</td><td>0.0066</td><td>0.0030</td><td>0.0119</td></tr><tr><td>job</td><td>0.0063</td><td>0.0041</td><td>0.0080</td></tr><tr><td>long</td><td>0.0056</td><td>0.0048</td><td>0.0064</td></tr><tr><td>working</td><td>0.0050</td><td>0.0046</td><td>0.0056</td></tr></table>

Number of significant tokens in this topic: 238  
(C)  
Fig. 6. Topic “employee relationship” from WMT

(D): “Arts”  
![](/api/attachments/ZFKJMNJD/fulltext/images/2b2f201aa6e849c4b5c973afff2dc165265cac7230677ebbfa916502acb9578e.jpg)

![](/api/attachments/ZFKJMNJD/fulltext/images/9ee8159f32ada994fbe328f9c1c768665e45c72e6fc9dd665bce8c47acfee64a.jpg)

(B): “Education”  
![](/api/attachments/ZFKJMNJD/fulltext/images/a64a50063f5d72516ed4e406301e5adf5a0d7b4d3b856195b2f967ff918dccd2.jpg)  
(A): “Education”  
(C): “Arts”

![](/api/attachments/ZFKJMNJD/fulltext/images/4c7e1a86ba14fdf0828029dc0887475f1f027382576af4759622fef0192b711f.jpg)  
Fig. 7. Topics from NYT

If the document's publication time is speci<sup>fi</sup>c only up to the date, then the daily variables are removed:

$$
x _ {d i} ^ {T} = \left(1, w 1 _ {d}, w 3 _ {d}, w 4 _ {d}, w 5 _ {d}, w 6 _ {d}, w 7 _ {d}, \cos \left(2 \pi \frac {m d _ {d}}{m l _ {d}}\right), \sin \left(2 \pi \frac {m d _ {d}}{m l _ {d}}\right)\right).\tag{6}
$$

Cyclical patterns of frequencies higher than days or lower than months can also be included using the Ser<sup>fl</sup>ing model representation. For example, the cyclical patterns for a half-day (12 h) can be captured by adding $\left( \cos \left( 2 \pi \frac { h d _ { d } } { 1 2 } \right) \right.$ ; sin $\left( 2 \pi { \frac { h d _ { d } } { 1 2 } } \right) \quad$ to the feature vector. Second, it is possible to automatically select the best combination of frequencies using standard model selection techniques, such as model evidence [14]. This study considers the case of cyclical patterns with <sup>fi</sup>xed frequencies.

## 3.3. Model inference using augmented Gibbs sampling

We adopted Gibbs sampling for model inference because it facilitates the extension and combination of inference algorithms. Speci<sup>fi</sup>cally, we extend augmented Gibbs sampling for multinomial Probit regression developed by Imai and Dyk [21] and Albert and Chib [22] for use in PDHA inference. Gibbs sampling constructs a Markov chain that converges to the posterior of latent variables and coef<sup>fi</sup>cients [16,24]. Both our inference algorithm and the one for multinomial Probit regression adopt additional augmented variables (e.g., $H _ { d i }$ in PDHA) to facilitate the sampling process. We refer to these algorithms as augmented Gibbs sampling algorithms to indicate the use of additional augmented variables.

All variables with open circles in Panel (A) of Fig. 4 are parameters or latent variables and require estimation. Our approach follows the collapsed Gibbs sampling for LDA developed by Grif<sup>fi</sup>ths and Steyvers [4] and integrates out $\phi _ { z _ { d i } }$ . The remaining parameters and latent variables are divided into two groups. The <sup>fi</sup>rst group contains the latent topic $\langle Z = \{ z _ { d i } \}$ , and the second group contains the parameters and latent variables related to the multinomial Probit regression sub-problem, including slopes $G = \{ g _ { j } \}$ , document-speci<sup>fi</sup>c topic tendency $Q = \{ q _ { d , j } \}$ and variance $\Sigma _ { j } .$ The tokens in all documents $w = \{ w _ { d i } \}$ and their temporal features $\boldsymbol { X } = \left( x _ { 1 1 } ^ { T } , x _ { 1 2 } ^ { T } , . . . , x _ { 1 N _ { 1 } } ^ { T } , x _ { 2 1 } ^ { T } , x _ { 2 2 } ^ { T } , . . . , x _ { 2 N _ { 2 } } ^ { T } , . . . , x _ { D 1 } ^ { T } , x _ { D 2 } ^ { T } , . . . , x _ { D N _ { D } } ^ { T } \right) ^ { T }$ are observable variables in PDHA. Augmented Gibbs sampling approximates the joint posterior $p ( Z , Q , G , \Sigma | w , X , ^ { . } )$ by iteratively updating the latent topic Z and regression coef<sup>fi</sup>cients via the steps:

![](/api/attachments/ZFKJMNJD/fulltext/images/703890039bfd0e57af0f5b2e91244ecc8fa0b4069faed13b3360d76048151e60.jpg)

![](/api/attachments/ZFKJMNJD/fulltext/images/64ef71015f7051ca112d14fecb1f88511c482a40d528549fabed04d71847de3a.jpg)

![](/api/attachments/ZFKJMNJD/fulltext/images/8831b193e58c94ae98e9726ac038dd88b554118511698eb76c5172ff45344c68.jpg)

Number of significant tokens in this topic: 134  
Top Keyword Probability:

<table><tr><td>Word</td><td>Prob.</td><td>Word</td><td>Prob.</td><td>Word</td><td>Prob.</td></tr><tr><td>company</td><td>0.0330</td><td>sale</td><td>0.0165</td><td>letter</td><td>0.0137</td></tr><tr><td>agreement</td><td>0.0327</td><td>mln</td><td>0.0161</td><td>acquisition</td><td>0.0133</td></tr><tr><td>dlrs</td><td>0.0206</td><td>corp</td><td>0.0140</td><td>subject</td><td>0.0133</td></tr><tr><td>general</td><td>0.0167</td><td>signed</td><td>0.0139</td><td>transaction</td><td>0.0128</td></tr></table>

Fig. 8. Topic “merger and acquisition” from RTS

![](/api/attachments/ZFKJMNJD/fulltext/images/035b4352b79a23221433a52f85adc14b0d35ed79ce7eb6c75130e19552845f9a.jpg)  
(A) WMT

![](/api/attachments/ZFKJMNJD/fulltext/images/10159aeb0579a5abe3f5698fb617a6e1388aa038da5aed7ae90c22f09bd86a1f.jpg)

![](/api/attachments/ZFKJMNJD/fulltext/images/fcf388dcc7ae543fc9d2d487938496bb5b226e611c6ea5701cd9bee254e814e4.jpg)

![](/api/attachments/ZFKJMNJD/fulltext/images/8e998ae7b033485f26d47e24b36efc71c44ce6973cf160ec18b7303bea67dbad.jpg)  
(C) RTS

(B) NYT  
(D) WMT  
![](/api/attachments/ZFKJMNJD/fulltext/images/6729b17118e93812198560badf84cc49d16854217296d1c65ad1a46b8d8ebfa0.jpg)  
(E) NYT

![](/api/attachments/ZFKJMNJD/fulltext/images/710aa6160afc8b894991843412c8348426592675ff906cbf885645c986d261f8.jpg)  
(F) RTS  
Fig. 9. Likelihood of WMT, NYT, and RTS. The upper panels are boxplots of the likelihood of the DMR, LDA, PDHA, and PDHA without temporal features (PDHA\_C). The lower panels show the comparison of only PDHA and PDHA\_C.

1. Sample latent topic Z from p(Z|w, X, Q, G, Σ,⋅).

2. Sample regression coef<sup>fi</sup>cients Q, G, Σ from $p ( Q , G , \Sigma | w , X , Z , ^ { . } ) .$

Note that Step 2 can be achieved by the augmented Gibbs sampling algorithms for multinomial Probit regression because, given the latent topic Z, the conditional posterior $p ( Q , G , \Sigma | w , X , Z , ^ { . } )$ has the same structure as that of the multinomial Probit regression. The subsequent discussion focuses on developing the sampling procedure in Steps 1 and 2.

## 3.3.1. Sampling latent topic Z

Similar to the collapsed Gibbs sampling scheme of the LDA model [4], our method updates z in a sequential manner. The posterior $z _ { d i }$ conditional on other variables is

$$
\begin{array}{l} p (z _ {d i} = j | z _ {- d i}, w _ {d i}, w _ {- d i}, X, Q, G, \Sigma) \\ \quad \propto p (w _ {d i} | z _ {d i} = j, z _ {- d i}, w _ {- d i}) p (z _ {d i} = j | Q, G, \Sigma , X) \\ \quad = \frac {n _ {- d i , j} ^ {(w _ {d i})} + \beta}{n _ {- d i , j} ^ {(\cdot)} + W \beta} p (z _ {d i} = j | q _ {d}, G, \Sigma , x _ {d}), \end{array}\tag{7}
$$

![](/api/attachments/ZFKJMNJD/fulltext/images/719c9b594d5e8c0442b4cbda00fb80351c1f2c9726b7e33ac0934a54ba28765c.jpg)  
(A) NYT

![](/api/attachments/ZFKJMNJD/fulltext/images/6f5647af4cd107a84a936d93559ca82c0c2ec7e8a3a6e129981631e963bb70ce.jpg)  
(B) RTS

![](/api/attachments/ZFKJMNJD/fulltext/images/4ff210c5de765ac9817fbbb2ee00cc2950fc0eaf0ce1d6d59f38fea6be0f1004.jpg)  
(C) WMT  
Fig. 10. Likelihoods of LDA, DMR, PDHA, and PDHA\_C with 50, 100, 500, and 1000 latent topics. Panels (A), (B), and (C) plot the results using NYT, RTS, and WMT datasets

where $n _ { - d i , j } ^ { ( \cdot ) }$ is the number of assignments to topic j, excluding the assignment at position i of document d; $n _ { - d i , j } ^ { ( w _ { d i } ) }$ is the instance tokentype $w _ { d i }$ assigned to topic j, excluding the instance at position i in document d; W is the number of unique tokens in the corpus. The token position index is suppressed for temporal features $x _ { d }$ because all tokens in a document have the same value.

The <sup>fi</sup>rst term in Eq. (7) is derived by integrating out ϕ and can be readily computed based on token–topic assignments. The second term, however, involves intractable integrals. We propose using a simulation method to evaluate this term.

Let $\hat { \theta } _ { d \vert x _ { d } , j }$ denote the estimated $p ( z _ { d i } = j | q _ { d } , G , \Sigma , \mathbf { x _ { d } } )$ , the probability of assigning a token to topic j given $x _ { d }$ and regression parameters. The idea is to compute $\hat { \theta } _ { d \vert x _ { d } , j }$ by generating $e _ { d i , j } \sim N ( 0 , \Sigma _ { j } )$ and computing $H _ { d i , j }$ using Eq. (3). The topic assignment then can be determined using Eq. (4). The process is repeated G times to compute $\widehat { \theta } _ { d \vert x _ { d } , j } .$

Direct implementation of this approach introduces independent simulation error into $\widehat { \theta } _ { d \vert x _ { d } , j } ,$ which can be undesirable in this setting. Consider the case of two documents, $d _ { 1 }$ and $d _ { 2 } ,$ having exactly the same temporal features and document-speci<sup>fi</sup>c topic tendency $\left( q _ { d _ { 1 } } = \right.$ $q _ { d _ { 2 } } )$ . Then $p ( z _ { d _ { 1 } i } = j | q _ { d _ { 1 } } , G , \Sigma , \mathbf { x } _ { d _ { 1 } } )$ and $p ( z _ { d _ { 2 } i } = j | q _ { d _ { 2 } } , G , \Sigma , \mathbf { X } _ { \mathrm { d _ { 2 } } } )$ should be the same for each topic j. However, because of the simulation error, the numerical procedure usually results in $\hat { \theta } _ { d _ { 1 } | x _ { d _ { 1 } } , j } { \neq } \hat { \theta } _ { d _ { 2 } | x _ { d _ { 2 } } , j } .$ . To address this problem, we adopt the common random variable method [25] and cache $C ( J - 1 )$ draws of a random variable from the standard normal distribution. The probability estimation $\hat { \theta } _ { d \mid x _ { d } , j }$ for each document is computed based on the same set of random variables. This approach provides the internal consistency for the estimated probability and ensures that $\hat { \theta } _ { d _ { 1 } | x _ { d _ { 1 } } , j } = \hat { \theta } _ { d _ { 2 } | x _ { d _ { 2 } } , j } s$ in the above example. The procedure is summarized in Algorithm 1.

## Algorithm 1. Estimate $p ( z _ { d i } = j | q _ { d } , G , \Sigma , \mathbf { x _ { d } } )$ via simulation

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs: C(J-1) random variables drawn from N(0,1) ( $\epsilon_{c,j} \sim N(0,1)$ , c=1,2,...C, j=1,2,...,J-1);
temporal feature  $x_{d}$ ; document-specific topic tendency  $q_{d}$ ; regression coefficients g, $\Sigma$ .

Outputs: Numerically estimated  $p(z_{di}=j|q_{d},g,\Sigma,x_{d})$  (i.e.,  $\hat{\theta}_{d|x_{d},j}$ ) for each document.

Set  $\hat{\theta}_{d|x_{d},j}=0$  for  $d=1,2,\ldots,D$  and  $j=0,2,\ldots,J-1$ .

for each  $d=1,2,\ldots,D$  do

    for each  $c=1,2,\ldots,C$  do

    for each  $j=1,2,\ldots,J-1$  do

    $H_{d,j}^{(c)}=q_{d,j}+x_{d}^{T}g_{j}+\sqrt{\Sigma_{jj}}\epsilon_{g,j}$ ;

    end

    $z=\begin{cases}0,&amp;\text{if}\max\left(H_{d}^{(c)}\right)\leq0\\j,&amp;\text{if}\max\left(H_{d}^{(c)}\right)=H_{d,j}^{(c)}&gt;0;\end{cases}$ $\hat{\theta}_{d|x_{d},z}=\hat{\theta}_{d|x_{d},z}+1;$ 

    end

    for each  $j=0,2,\ldots,J-1$  do

    $\hat{\theta}_{d|x_{d},j}=\hat{\theta}_{d|x_{d},j}/C;$ 

    end

end
</div>

The parameter C should be large enough to enable accurate probability estimation. Preliminary experiments suggest that for a model with a moderate number of topics $( \mathbf { e } . \mathbf { g } . , 5 0 ) , C \approx 1 5 0 0$ is a reasonable choice. The time complexity of Algorithm 1 is O(DJC). Note that few changes are needed even if each token has different temporal features. The main change would be to loop over individual tokens, instead of documents and compute a simulated $H _ { d i , j }$ for each token.

## 3.3.2. Sampling regression coefficients

We applied the marginal data augmentation approach for multinomial Probit regression [21,26] to draw regression coef<sup>fi</sup>cients from $p ( Q , G , \Sigma | w , X , Z , ^ { . } )$ . We present the outline of the algorithm and the anal ysis of time complexity.

The basic idea is to include additional augmented variables to facilitate model inferences. Panel (B) of Fig. 4 plots the model with augmented variable $H _ { d i } .$ We adopted another augmented variable a $( a > 0 ;$ not visible in Panel (B) of Fig. 4) to address the technical dif<sup>fi</sup>culties caused by the identi<sup>fi</sup>cation constraint $\Sigma _ { 1 } = 1$ (the <sup>fi</sup>rst diagonal element in Σ). The variable a scales the original model to an equivalent one with $\Sigma _ { 1 } =$ $a ^ { 2 } .$ . The regression coef<sup>fi</sup>cients are updated through the transformed model. The updated variables are then scaled back to the original model. Fig. B.1 in Appendix B summarizes the major steps for drawing the regression coef<sup>fi</sup>cients.

Running a single sweep for PDHA inference includes computing $\hat { \theta } _ { d \vert x _ { d } , j }$ via Algorithm 1, updating Z, and other parameters (see Fig. B.1 in Appendix B for details). The overall time complexity is O $\left( D \overline { { { N } } } _ { d } K ^ { 2 } J + J K ^ { \gamma } + J ^ { \gamma } \right)$ , where $\overline { { N } } _ { d }$ is the average document length and the exponent γ is associated with the computational cost of matrix inversion. Inverting a matrix via Gauss–Jordan elimination has a time complexity of $O ( K ^ { 3 } )$ for a K-by-K square matrix. However, matrix inversion can run at the same time complexity as matrix multiplication using the block-wise inversion method [27], and matrix multiplication using the Coppersmith–Winograd algorithm [28] has a time complexity of $O ( K ^ { 2 . 3 \bar { 7 } 6 } )$ . As a result, $\gamma = 2 . 3 7 6$ would be a reasonable choice for the current analysis.

The <sup>fi</sup>rst term of the overall time complexity is contributed by the inner product of the temporal feature matrix X when computing the posterior mean of $\widetilde { g } _ { j } ^ { * }$ . The second term is contributed by inverting the precision matrix of $\tilde { g } _ { j } ^ { * }$ . The last term comes from the inversion of Σ (in Step 1 of Fig. B.1 in Appendix B). Note that the computational costs of updating $Z \left( D \overline { { N } } _ { d } J \right)$ and Algorithm 1 (DJC) are dominated by the cost of sampling regression coef<sup>fi</sup>cients.

The PDHA inference method grows linearly with respect to the size of the corpus $( D \overline { { N } } _ { d } )$ . This means that our approach is scalable if the number of topics and the lengths of the temporal features are <sup>fi</sup>xed. When the length of temporal features increases, the running time will eventually increase at the speed of $K ^ { \gamma } .$ Note that the <sup>fi</sup>rst term $( D \overline { { N } } _ { d } K ^ { 2 } J )$ typically has a larger constant compared to the second term $( J K ^ { \gamma } )$ . As a result, a growth rate close to $K ^ { 2 }$ will be observed for smaller K $( \mathrm { e . g . , } K < 1 0 0 )$ . A similar effect applies to the growth rate of the number of topics. The asymptotic growth rate is $J ^ { \gamma }$ but, in practice, a near-linear growth rate is observed for smaller J.

The main focus of the current study is to evaluate PDHA model in an archival setting. Applying a learned PDHA model in a streaming environment is possible. To do so, the latent topics of unseen documents need to be estimated based on a learned model. The time complexity for this is $O \left( D ^ { \prime } \overline { { N } } _ { d } ^ { \prime } J \right)$ , where $D ^ { \prime }$ is the number of unseen documents and $\overline { { N } } _ { d } ^ { \prime }$ is the average token length of these documents.

## 3.4. Analysis of sampling results

The augmented Gibbs sampling approach can be run for L sweeps to collect the sampling results. The <sup>fi</sup>rst B burn-in sweeps are discarded to minimize the impact of initial values. After the burn-in sweeps, every $L _ { T }$ sweep is recorded for subsequent analysis. The practice of storing only every L sweep is called “thinning.” Thinning is used to reduce the autocorrelation between the recorded sweeps introduced by Gibbs sampling. We refer readers to Gelfand [29] for a more detailed introduction to thinning and other related concepts.

To simplify notation, we re-index the collected sweeps from 1 to $L _ { S } .$ For example, for $L = 2 0 0 0 , B = 1 0 0 0$ , and $L _ { T } = 2 0$ , the augmented Gibbs sampling runs for 2000 sweeps and the <sup>fi</sup>rst 1000 sweeps are discarded. The latent variables and parameters from 1020, 1040, …, and 2000 sweeps are recorded and re-indexed from 1 to 50.

The latent topics from sweep $r , Z ^ { ( r ) }$ , can help with the estimation of the probability of observing token w, conditional on topic j:

$$
\phi_ {j, w} ^ {(r)} = \frac {n _ {j , w} ^ {(r)} + \beta}{n _ {j , \cdot} ^ {(r)} + W \beta}.
$$

where $n _ { j , \cdot } ^ { ( r ) }$ is the count of topic j in $Z ^ { ( r ) }$ , and $n _ { j , w } ^ { ( r ) }$ is the count for which token w is associated with topic j. Given the recorded $L _ { s }$ sweep, the posterior mean of $\begin{array} { r } { \phi _ { j , w } \mathrm { i } s \hat { \phi } _ { j , w } = \frac { 1 } { L _ { \mathrm { s } } } \sum _ { r = 1 } ^ { L _ { \mathrm { s } } } \phi _ { j , w } ^ { ( r ) } } \end{array}$ . The 95% con-<sup>fi</sup>dence interval of $\phi _ { j , w }$ is the interval between the 2.5 and the 97.5 percentiles of $\{ \phi _ { j , w } ^ { ( r ) } \} , r = 1 , 2 , . . . , L _ { s } .$ The con<sup>fi</sup>dence interval of $\phi _ { j , w }$ provides a convenient way to identify signi<sup>fi</sup>cant keywords in a topic. The conjugate prior to $\phi _ { j , w }$ has a mean of $1 / \mathsf { W } . \mathrm { A } \phi _ { j , w }$ with a con<sup>fi</sup>dence interval larger than 1/W suggests that token w is indeed associated with topic j and is therefore referred to as a signi<sup>fi</sup>cant keyword for the underlying topic. The number of signi<sup>fi</sup>cant keywords in a topic provides a useful reference for the vocabulary size of the topic.

The posterior distribution of G and Σ can be analyzed using the recorded sweeps. In addition to computing posterior mean and con<sup>fi</sup>dence interval, we compute the p-value of each element in G using the t-value computed based on a time-series standard error. The time-series standard error considers the potential autocorrelation in the recorded sweeps and is usually more conservative than the standard error computed ignoring the effects of autocorrelation.

Finally, the cyclical patterns of a topic can be computed using Algorithm 1. For example, to compute the dynamics of daily cyclical patterns of topic $j ,$ the input temporal features are $\begin{array} { r } { x ^ { T } = \left( 1 , \cos ( 2 \pi { \frac { h } { 2 4 } } ) , \sin ( 2 \pi { \frac { h } { 2 4 } } ) , \overline { { w 1 } } , \overline { { w 3 } } , \overline { { w 4 } } , \overline { { w 5 } } , \overline { { w 6 } } , \overline { { w 7 } } , \overline { { c o s ( 2 \pi { \frac { m d } { m l } } ) } } \right) } \end{array}$ are the sample means in X and h is the selected time of day in hours. The mean regression coef<sup>fi</sup>cients, ĝ and $\hat { \Sigma } _ { j j }$ are also needed. Note that we are interested in the cyclical patterns of a topic instead of those of a document. Thus, we use the average document-speci<sup>fi</sup>c topic tendency for each topic. Using the common random variable approach outlined in Algorithm 1, we can compute the conditional probability of a topic at different h.

## 3.5. Baseline model

This study adopts two baseline models for comparison with the proposed PDHA model. The <sup>fi</sup>rst baseline is the LDA that did not consider the temporal features included in PDHA. The LDA represents the performance of a widely-used topic model.

The second baseline is the DMR model that includes exactly the same set of temporal features as in the proposed PDHA model. DMR extends the LDA and allows temporal features to in<sup>fl</sup>uence the prior distribution of the topic distribution of a document. DMR is similar to the TC model but allows the timedependent features to capture cyclical topic dynamics. We excluded TOT as a baseline in this study mainly because the TOT model normalizes the timestamps to a value between zero and one as a way of accommodating the assumption that timestamps are generated from the beta distribution. The shape of beta distribution is controlled by two parameters and is not capable of tracking cyclical patterns.

## 3.6. Model evaluation

A common approach to evaluate a topic model is computing the log likelihood of a testing set given the learned coef<sup>fi</sup>cients. Let ${ \cal G } = \left\{ g ^ { ( 1 ) } , g ^ { ( 2 ) } , . . . , g ^ { ( L _ { s } ) } \right\} , q = \left\{ q ^ { ( 1 ) } , q ^ { ( 2 ) } , . . . , q ^ { ( L _ { s } ) } \right\}$ , and $\Omega =$ $\left\{ \boldsymbol { \Sigma } ^ { ( 1 ) } , \boldsymbol { \Sigma } ^ { ( 2 ) } , . . . , \boldsymbol { \Sigma } ^ { ( L _ { s } ) } \right\}$ denote the parameters and latent variables recorded from $L _ { S }$ sweeps. For a testing document d with temporal feature $x _ { d }$ and a collection of tokens $w _ { d } ,$ the testing likelihood $p ( w _ { d } | \boldsymbol { x } _ { d } , G , Q , \Omega )$ is computed using the importance sampling approach [30].

This approach mainly involves three steps. First, sample $\theta _ { d \vert x _ { d } } ^ { ( r ) }$ is created based on the record sweep $r , r = 1 , 2 , . . . , L _ { s } $ . This step follows the data-generating process of PDHA with a few exceptions. The document-speci<sup>fi</sup>c topic tendencies $q _ { j }$ are no longer drawn from the prior distribution $N ( 0 , s _ { q } ^ { 2 } )$ but from $N \left( \hat { m } _ { q , j } , \hat { s } _ { q , j } ^ { 2 } \right)$ where $\hat { m } _ { q , j }$ and $\hat { s } _ { q , j } ^ { 2 }$ are the mean and variance of the vector $( q _ { 1 , j } ^ { ( r ) }$ $q _ { 1 , j } ^ { ( r ) } , . . . , q _ { 1 , j } ^ { ( r ) } , q _ { 2 , j } ^ { ( r ) } , q _ { 2 , j } ^ { ( r ) } , . . . , q _ { 2 , j } ^ { ( r ) } , . . . , q _ { D , j } ^ { ( r ) } , q _ { D , j } ^ { ( r ) } , . . . , q _ { D , j } ^ { ( r ) } )$ ,witheachq<sub>d,j</sub><sup>(r)</sup>repeating $N _ { d }$ times. Combined with $g _ { j } ^ { ( r ) }$ and $\Sigma ^ { ( r ) } , \theta _ { d | x _ { d } } ^ { ( r ) }$ can be readily computed using Algorithm 1.

The second step is to compute the probability of a token w in document d, $\hat { w } _ { d i } .$ . Because $\theta _ { d | x _ { d } } ^ { ( r ) }$ is vector of topic probability in document $\begin{array} { r } { \mathrm { d } , \overline { { w } } _ { d i } = \frac { 1 } { L _ { s } } \sum _ { r = 1 } ^ { L _ { s } } \sum _ { j = 1 } ^ { J } \phi _ { j , w _ { d i } } ^ { ( r ) } \theta _ { d | x _ { d } , j } ^ { ( r ) } . } \end{array}$ The <sup>fi</sup>rst summation is over all possible topics that can contribute to the occurrence of the token $w _ { d i } \mathrm { : }$ the second summary is over all recorded sweeps. Finally, log $p ( w _ { d } | x _ { d } , G , Q , \Omega )$ sums up all log $\overline { { w } } _ { d i }$ because each token is independently distributed given $q _ { d } ,$ $g , \Sigma ,$ , and $x _ { d } .$

$$
\log p (w _ {d} | x _ {d}, G, Q, \Omega) = \sum_ {i = 1} ^ {N _ {d}} \log \hat {w} _ {d i}.
$$

A similar process can be used to compute the testing likelihood of the LDA, DMR, and DTM models.

## 4. Experimental results

We evaluated PDHA on three datasets: the Yahoo Finance Wal-Mart message board (WMT), the New York Times (NYT), and Reuters-21578 (RTS). The three datasets cover different types of text content. WMT is user generated content; NYT and RTS are news and newswire articles, respectively. The variety among the three datasets allows the study to better characterize the performance of the proposed PDHA. Table 1 presents a summary of the three datasets. We included different temporal features based on availability. The WMT dataset is composed of postings on Yahoo Finance's Wal-Mart message board. Because of the presence of timestamps (Eastern Time; precise to the second) for each posting, we included variables for daily, weekly, and monthly cyclical patterns, as in Eq. (5). The NYT dataset is a 10% random sample of NYT articles published between 1/1/2008 and 6/30/2008. The model for NYT only contains variables for weekly and monthly cyclical patterns as in Eq. (6). The RTS dataset includes timestamps precise to the second. Thus, we included variables for daily, weekly, and monthly cyclical patterns, as in Eq. (5). We normalized regressors to have a zero mean and unit variance.

![](/api/attachments/ZFKJMNJD/fulltext/images/b5eff90b884efe2117e5156f41d6819db91f78a46f857e64045a79ae8902fafd.jpg)  
Fig. 11. Running time comparison (using the WMT dataset).

We estimated all models with Gibbs sampling of 2000 sweeps. To minimize the impact of initial values, we discarded the <sup>fi</sup>rst 1000 sweeps. We recorded the sampled parameters every 20 sweeps to reduce autocorrelation and computed estimation results based on the recorded sweeps. We set the <sup>fi</sup>rst element in $m _ { 0 } ,$ the prior mean of intercept $g _ { j , 1 }$ , to give all topics an equal prior probability if all other coef<sup>fi</sup>cients in Eq. (3) were zero. The prior variances $s _ { g } ^ { 2 }$ and $s _ { q } ^ { 2 }$ were 2000=l and 100=l, where l was the average token length of documents in a corpus. We present the estimation results of PDHA with 50 latent topics in Section 4.1. In Section 4.2, we present the likelihood comparisons and running time comparisons of four different topic amounts (50, 100, 500, and 1000).

## 4.1. Topic cyclical patterns in WMT, NYT, and RTS

This section presents selected topic cyclical patterns estimated from WMT, NYT, and RTS. Fig. 5 summarizes the “Earnings” topic from WMT. The topic name was assigned manually based on the top keywords. Panel (A) plots the monthly, weekly, and daily cyclical patterns computed based on the recorded Gibbs sampling sweeps. This topic is clearly more popular during the <sup>fi</sup>rst half of a month. Thursday has the highest probability for this topic, while weekends have a much lower probability. The time-of-day pattern shows that it reaches a peak around the same time as the opening of the stock market: 9:30 am. The occurrence rate drops quickly after noon and reaches its trough around midnight. The probability differences between the peak and trough are quite large. The probability density during peak hours is 0.08 while the probability drops to 0.01 during the trough.

Panel (B) lists the estimated regression coef<sup>fi</sup>cients used to compute probability in Panel (A). The t-value listed in the last column is computed using a time-series corrected standard error to account for the autocorrelation between recorded sweeps. Coef<sup>fi</sup>cients for monthly and daily cyclical patterns are signi<sup>fi</sup>cant, consistent with the patterns in Panel (A). Most day-of-the-week coef<sup>fi</sup>cients are also signi<sup>fi</sup>cant.

Panel (C) lists the top keywords in this topic. All top keywords have 95% con<sup>fi</sup>dence intervals far above the expected prior probability of a keyword (0.000026 ≈ 1/37315), suggesting strong evidence for them. The top keywords such as “sales,” “year,” “growth,” “percent,” “stores,” and “billion” typically appear in postings discussing revenues, sales, store expansion, etc. This type of new information is directly related to stock price. Thus, the observance of a close relationship between the “Earnings” topic and stock trading hours is reasonable.

Fig. 6 plots the “Employee Relationship” topic from WMT. Like the “Earnings” topic from the same dataset, this topic shows distinct monthly, weekly, and daily cyclical patterns. The monthly pattern in Panel (A) shows that this topic is more popular during the beginning and ending of a month. Thursday has the lowest probability of all the days in a week. This topic is denser from around 7 am-to-3 pm. The probability difference between peak and trough hours, however, is smaller compared to that of the “Earnings” topic. One possible reason for this is that though trading activities drive discussions of earnings, no similar driving force exists for conversations on employee relationships. The phenomenon of a lower probability on Thursdays might be related to the payday schedule of Wal-Mart. Panel (C) lists the important keywords in this topic. Top keywords such as “people,” “time,” “business,” “make,” “work,” and “pay” in this topic often appear in postings about schedules, hourly wage, and the lifestyles of Wal-Mart employees.

Fig. 7 summarizes two selected topics from NYT. The estimated regression coef<sup>fi</sup>cients and con<sup>fi</sup>dence intervals for top keywords are suppressed to save space. Panel (A) plots the monthly and weekly patterns of the topic “Education.” This topic is without a clear monthly peak or trough. Weekly dynamics, on the other hand, clearly show that weekends have a much higher probability compared to weekdays. The weekly pattern might re<sup>fl</sup>ect the choices of NYT's editors. The top keywords in Panel (B), including “school,” “students,” “schools,” “college,” and “university,” typically appear in articles about educational issues, such as teacher pay, charter schools, principal hiring, and safety issues in schools. The “Arts” topic presented in Panel (C) has a clear monthly pattern that peaks around the 20th day of a month. Because the topic often appears in articles that comment on and introduce musical and theatrical events, which are often on weekends, the topic's higher probabilities on Monday and Friday are not surprising. The top keywords in Panel (D), including “dance,” “music,” “ballet,” “york,” and “orchestra,” are consistent with the common knowledge of news articles about this topic.

Fig. 8 summarizes the “Merger and Acquisition” (M&A) topic from RTS. Clear day-of-the-week and time-of-day patterns are present. Articles about M&A often appear on Monday and seldom appear during the weekends. The daily pattern shows a peak around 2 pm. The day-ofthe-month plot does not reveal a clear cyclical pattern. The top keywords in this topic, including “company,” “agreement,” “dlrs,” and “sale,” typically appear in articles that announce corporate mergers and unit sale events.

The selected estimation results presented in this section clearly show that PDHA is able to capture interesting monthly, weekly, and daily cyclical patterns in document collections. The additional information required for the proposed model to work is the timestamp for each document, which is usually available from the text from the mass media and user-generated content. We report the performance of the proposed approach and baselines in the following section.

## 4.2. Likelihood comparisons

This section reports the log-likelihood comparison of PDHA with other baseline models. We consider models with higher testing loglikelihoods to excel at generalizing the estimated models to unseen data. We designed the experiments to answer two research questions: (1) Does PDHA perform better compared to other baseline topic modeling approaches? (2) How do the temporal features included in PDHA contribute to the performance difference? To answer these two research questions, we compared PDHA to LDA, DMR, and a simpli<sup>fi</sup>ed PDHA model, PDHA\_C, that excluded temporal features from PDHA. The loglikelihood difference between LDA and PDHA can be interpreted as the joint effect of the model difference and temporal features. Since both DMR and PDHA have access to exactly the same set of temporal features, the log-likelihood difference stems from model difference only. The underlying models for PDHA and PDHA\_C are the same. The log-likelihood difference, as a result, stems from temporal features.

For each testbed, we allocated 70% of the documents for training and reserved the rest for testing. We set the smoothing parameters of all models to $\begin{array} { r } { \alpha = \frac { 5 0 } { T } , \beta = 0 . 0 1 } \end{array}$ , following a previous study [6]. We ran Gibbs sampling for 2000 sweeps, and used the importance sampling approach to compute the log-likelihood from the last 20 recorded sweeps (with thinning $L _ { T } = 2 0 )$ . For each model, we repeated the estimation 40 times using different seeds.

Fig. 9 presents boxplots of the log-likelihoods for the setting using 50 latent topics. Panels (A) to (C) plot the log-likelihood values for the DMR, LDA, PDHA, and PDHA\_C models estimated using WMT, NYT, and RTS. PDHA models, on average, achieved the highest loglikelihood values of the three testbeds. The LDA models, on the other hand, resulted in the lowest log-likelihood values. Note that the range for PDHA does not overlap with the range of the DMR or LDA, suggesting that the performance difference is statistically signi<sup>fi</sup>cant. ANOVA tests reject the null hypothesis that the log-likelihood values of the four models are the same (p-value b 0.01). The t-tests suggest that PDHA is signi<sup>fi</sup>cantly better than DMR, LDA, and PDHA\_C.

The other research question regards the contribution of the temporal features to the increase in performance. Observing the relative performances between PDHA and PDHA\_C can shed light on this question. The difference between these two models can be considered as the contribution of temporal features. Panels (D) to (F) plot the log-likelihood values of these two models. The loglikelihood difference is quite large for the WMT and RTS datasets and is smaller for that of NYT. One possible reason for this is that NYT articles lack intra-day variables; in addition, the weekly and monthly cyclical patterns are less informative compared to the <sup>fi</sup>ne-grained timestamps in WMT and RTS. The mode of PDHA is higher than that of PDHA\_C; this holds true for all three testbeds. The t-tests comparing PDHA and PDHA\_C are all signi<sup>fi</sup>cant at the 99% con<sup>fi</sup>dence level, suggesting that temporal features alone contribute positively to the performance of topic modeling.

The log-likelihood difference between the DMR and LDA can also be interpreted as the contribution of temporal features. Panels (A) to (C) clearly indicate that DMR delivers a higher log-likelihood than LDA. The performance difference is signi<sup>fi</sup>cant at the 99% con<sup>fi</sup>dence level, and is usually larger than the gap between PDHA and PDHA\_C. One reason for this is the <sup>fi</sup>xed prior parameter α for document–topic distribution constraining LDA's ability to adapt to the training data. DMR allows constant terms for each topic to be estimated based on data, a fact that provides an advantage in addition to the temporal features. This result is, in general, consistent with studies that investigate the effect of the prior distribution on LDA [31].

As discussed above, the difference between DMR and PDHA is due to the novel model structure of PDHA. PDHA performs signi<sup>fi</sup>cantly better than DMR (p-value b 0.01), suggesting that the upstream token-level structure performs better than the upstream document-level structure in DMR. Despite the performance gain of PDHA, Panels (A) to (C) reveal a disadvantage of PDHA. The testing log-likelihoods of the LDA and DMR models have smaller variances than those of the PDHA models. One possible reason is that the intermediate parameters of our LDA and DMR models are collapsed, which allow for more ef<sup>fi</sup>cient estimation. The PDHA models are also estimated via Gibbs sampling, but only with $\phi _ { z _ { d i } }$ integrated out. Thus, we observe a higher variation of the log-likelihood values for the PDHA and PDHA\_C models.

To understand the in<sup>fl</sup>uence of the number of latent topics, we performed tests using varying latent topic numbers: 50, 100, 500, and 1000. We report the results in Fig. 10. Increasing the latent topic number from 50 to 100 improved the performance of PDHA and other baseline models. The improvement of PDHA is smaller compared to that of LDA and DMR. We see this effect consistently across the three testbeds. Further increasing the latent topic number from 100 to 500 has different effects on the three testbeds. All models showed higher likelihood values for the WMT testbed while the likelihood values remains <sup>fl</sup>at for the NYT and RTS datasets. The likelihood values only changed slightly when the number of latent topics increased to 1000 from 500.

In addition to the discussion on computational complexity in Section 3.3.2, we have also included the running time comparisons of PDHA, LDA, and DMR. We conducted all experiments on a PC with an Intel i5 CPU and 16GB of RAM. Fig. 11 summarizes the running times of PDHA, DMR, and LDA using different numbers of latent topics. For a model with 50 latent topics, PDHA, DMR, and LDA took 98.9 min, 19.8 min, and 18 min to complete, respectively. PDHA took longer to complete but provided additional information regarding the shortterm cyclical patterns.

The running time for any of the three models is roughly linear with respect to the number of topics when the number is small $( \mathbf { e . g . , } \ J \leq 5 0 0 )$ . However, it took much longer for PDHA to <sup>fi</sup>nish when the number of topics was large $( { \bf e . g . , \mathrm { ~ J ~ } } = 1 0 0 0 )$ . In fact, PDHA took about a week to complete when the number of topics was 1000. In contrast, LDA took less than <sup>fi</sup>ve hours to <sup>fi</sup>nish estimating a model with 1000 topics. The additional computational cost of incorporating short-term cyclical dynamics is clearly high when using a large amount of latent topics (e.g., 1000). However, the additional running time can be justi<sup>fi</sup>ed when we need to include a moderate amount of latent topics (e.g., 50 or 100) because PDHA provides richer information, better summarizing the dynamics of latent topics. These results are generally consistent with the theoretical discussion in Section 3.3.2.

## 5. Conclusions

This paper presents a PDHA model that includes temporal features into topic models. The model adopts a multinomial Probit regression structure to incorporate temporal features. Temporal features that model monthly, weekly, and daily cyclical patterns allow PDHA to capture short-term cyclical patterns that naturally occur in text from user-generated content, newswire, and newspapers.

To facilitate the ef<sup>fi</sup>cient estimation of PDHA, we developed an augmented Gibbs sampling algorithm that iteratively updates latent topic variables and regression coef<sup>fi</sup>cients. Experimental results show that PDHA outperformed LDA and DMR in terms of hold-out log-likelihood. Both the temporal features and the more <sup>fl</sup>exible upstream token-level model structure contribute to the improved performance of PDHA. Likelihood comparisons show that daily and weekly cyclical patterns are more important in WMT and RTS compared to NYT, suggesting that short-term cyclical dynamics may be more important in some datasets.

Extending the PDHA model to include other meta-data variables, such as authors and citations, is possible. To further improve performance, we are also working on including token-level features such as the WordNet senses and the position of a word in a document. Another interesting application is to apply PDHA to context-aware recommender systems. PDHA can be used to recommend different products based on holiday seasons, day-of-the-week, time-of-day, and other relevant context variables.

The other extension is to consider “latent topics” that may have ordinal relationships. One application might be mining product reviews that naturally <sup>fi</sup>t into this application. A structure similar to ordinary Probit regression could be adopted for this purpose. Small modi<sup>fi</sup>cations to the inference method would be needed for such applications.

## Acknowledgments

This work was supported in part by the Ministry of Science and Technology of Taiwan under grants 100-2410-H-002-025-MY3 and 103-2410-H-002-110-MY3.

## Appendix A. Summary of selected time-dependent topic models

Table A.1  
Summary of selected time-dependent topic models.

<table><tr><td></td><td>Latent Dirichlet (LDA)</td><td>Dynamic topic model (DTM)</td><td>Topic over time (TOT)</td><td>Temporal collection (TC)</td><td>Probit-Dirichlet hybrid allocation (PDHA)</td></tr><tr><td>Main reference</td><td>Griffiths and Steyvers [4] and Blei et al. [1]</td><td>Blei and Laferty [12]</td><td>Wang and McCallum [11]</td><td>Hong et al. [5]</td><td>This study</td></tr><tr><td>Model estimation method</td><td>Collapsed Gibbs sampling, variational Bayes</td><td>Variational Bayes</td><td>Stochastic EM</td><td>Stochastic EM</td><td>Augmented Gibbs sampling</td></tr><tr><td>Topic-token distribution (topic meaning)</td><td>Fixed</td><td>Markovian (random walk)</td><td>Fixed</td><td>Fixed</td><td>Fixed</td></tr><tr><td>Time range</td><td>Not considered</td><td>Long-term (years)</td><td>Long-term (months-to-years)</td><td>Medium-term (days-to-months)</td><td>Short-term (hours-to-days)</td></tr><tr><td>Continuous or discrete time</td><td>Not considered</td><td>Discrete</td><td>Continuous</td><td>Continuous</td><td>Continuous</td></tr><tr><td>Time-dependence structure</td><td>Not considered</td><td>Upstream at document-level</td><td>Downstream at token-level</td><td>Upstream at document-level</td><td>Upstream at token-level</td></tr><tr><td>Time-dependent topic occurrence</td><td>Not considered</td><td>Dirichlet prior with random walk</td><td>Beta distribution for normalized time variable</td><td>Gamma distribution</td><td>Multinomial Probit regression with Serfling model</td></tr></table>

## Appendix B. Major steps for drawing regression coef<sup>fi</sup>cients

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs: Updated latent topic Z and regression coefficients from the previous sweep:  $Q^{(old)}$ ,  $G^{(old)}$ ,  $\Sigma^{(old)}$ ,  $H^{(old)}$ 

Outputs: Updated regression coefficients:  $Q^{(new)}$ ,  $G^{(new)}$ ,  $\Sigma^{(new)}$ ,  $H^{(new)}$ 

1) Draw  $a^{*2}$  from trace( $\Sigma^{-1^{(old)}}$ )/ $\chi_{(J-1)^{2}}^{2}$ .

2) Draw  $\widetilde{H}_{di,j}^{*}$  by first drawing  $H_{di,j}^{*}$  from the truncated normal distribution using the original model and scaling the result by  $\widetilde{H}_{di,j}^{*}=a^{*}H_{di,j}^{*}$ .

3) Draw scaled regression coefficients  $\tilde{g}_{j}^{*}$  from the multivariate normal distribution (j=1,2,...,J-1).

4) Draw scaled document-specific topic tendencies  $\tilde{q}_{d,j}^{*}$  from the normal distribution (d=1,2,...,D and j=1,2,...,J-1).

5) Draw another scale variable  $a^{**2}$  from the inverse Chi-squared distribution that depends on the newly-updated regression coefficients and document-specific topic tendencies.

6) Compute  $Q^{(new)}$ , and  $G^{(new)}$  by  $q_{d,j}^{(new)}=\tilde{q}_{d,j}^{*}/a^{**}$ ,  $g_{j}^{(new)}=\tilde{g}_{j}^{*}/a^{**}$ .

7) Draw  $\Sigma^{(new)}$  by first sampling  $\tilde{\Sigma}^{*}$  from the inverse Chi-squared distribution based on the scaled model and set  $\Sigma^{(new)}=\tilde{\Sigma}^{*}/\tilde{\Sigma}_{11}^{*}$ 

8) Compute  $H^{(new)}$  by  $H_{di,j}^{(new)}=\frac{\widetilde{H}_{di,j}^{*}}{\sqrt{\widetilde{\Sigma}_{11}^{*}}}$ .
</div>

Fig. B.1. Major steps for drawing regression coef<sup>fi</sup>cients.

## References

[1] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent Dirichlet allocation, Journal of Machine Learning Research 3 (2003) 993–1022.

[2] D.M. Blei, J.D. Lafferty, Correlated topic models, Neural Information Processing Systems (NIPS), 2006.

[3] D. Mimno, A. McCallum, Topic models conditioned on arbitrary features with Dirichlet-multinomial regression, Uncertainty in Arti<sup>fi</sup>cial Intelligence (UAI), 2008.

[4] T.L. Grif<sup>fi</sup>ths, M. Steyvers, Finding scienti<sup>fi</sup>c topics, Proceedings of the National Academy of Sciences of the United States of America 101 (2004) 5228–5235.

[5] L. Hong, B. Dom, S. Gurumurthy, K. Tsioutsiouliklis, A time-dependent topic model for multiple text streams, Presented at the Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Diego, California USA 2011

[6] M. Rosen-Zvi, C. Chemudugunta, T. Grif<sup>fi</sup>ths, P. Smyth, M. Steyvers, Learning authortopic models from text corpora ACM Transactions on Information Systems 28 (2010) 1-38

[7] K. El-Arini, M. Xu, E.B. Fox, C. Guestrin, Representing Documents Through Their Readers. Presented at the Proceedings of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Chicago, Illinois, USA. 2013.

[8] H. Ma, H. Cao, Q. Yang, E. Chen, J. Tian, A habit mining approach for discovering similar mobile users, Presented at the Proceedings of the 21st Internationa Conference on World Wide Web, Lyon, France, 2012.

[9] X. Wu, J. Yan, N. Liu, S. Yan, Y. Chen, Z. Chen, Probabilistic latent semantic user segmentation for behavioral targeted advertising, Presented at the Proceedings of the Third International Workshop on Data Mining and Audience Intelligence for Advertising, Paris, France, 2009.

[10] M. Deshpande, G. Karypis, Item-based Top-N recommendation algorithms, ACM Transactions on Information Systems 22 (2004) 143–177.

[11] X. Wang, A. McCallum, Topics over time: a non-Markov continuous-time model of topical trends, Presented at the KDD, Philadelphia, Pennsylvania, USA, 2006.

[12] D.M. Blei, J.D. Laferty, Dynamic topic models, International Conference on Machine Learning, Pittsburgh, PA, 2006.

[13] D.M. Blei, Introduction to probabilistic topic models, Communications of the ACM, 2012 (forthcoming).

[14] C.M. Bishop, Pattern Recognition and Machine Learning, Springer, 2006

[15] J. Besag, Spatial interaction and the statistical analysis of lattice systems, Journal of the Royal Statistical Society. Series B (Methodological) 36 (1974) 192–236.

[16] S. Geman, D. Geman, Stochastic relaxation, Gibbs distributions, and the Bayesian restoration of images, IEEE Transactions on Pattern Analysis and Machine Intelligence 6 (1984)721-741

[17] M. Jordan, Z. Ghahramani, T. Jaakkola, L. Saul, Introduction to variational methods for graphical methods, Machine Learning 37 (1999) 183–233

[18] Y.W. Teh, D. Newman, M. Welling, A collapsed variational bayesian inference algorithm for latent Dirichlet allocation, NIPS, 2006.

[19] C. Wang, D. Blei, D. Heckerman, Continuous time dynamic topic models, Uncertainty in Arti<sup>fi</sup>cial Intelligence (UAI), 2008.

[20] H.-Y. Lin, Ef<sup>fi</sup>cient classi<sup>fi</sup>ers for multi-class classi<sup>fi</sup>cation problems, Decision Support Systems 53 (2012) 473–481.

[21] K. Imai, D.A.v. Dyk, A Bayesian analysis of the multinomial probit model using marginal data augmentation, Journal of Econometrics 124 (2005) 311–334.

[22] J.H. Albert, S. Chib, Bayesian analysis of binary and polychotomous response data, Journal of the American Statistical Association 88 (1993) 669–679.

[23] R.E. Ser<sup>fl</sup>ing, Methods for current statistical analysis of excess pneumonia–in<sup>fl</sup>uenza deaths, Public Health Reports 78 (1963) 494–506.

[24] K.S. Chan, C.J. Geyer, Discussion: Markov chains for exploring posterior distributions, The Annals of Statistics 22 (1994) 1747–1758.

[25] J.M. Hammersley, D.C. Handscomb, Monte Carlo Methods, Halsted, New York, 1964.

[26] X.-L. Meng, D.A.V. Dyk, Seeking ef<sup>fi</sup>cient data augmentation schemes via conditional and marginal augmentation, Biometrika 86 (1999) 301–320.

[27] T.H. Cormen, C.E. Leiserson, R.L. Rivest, Introduction to Algorithms, MIT Electrical Engineering and Computer Science1990.

[28] D. Coppersmith, S. Winograd, Matrix multiplication via arithmetic progressions, Journal of Symbolic Computation 9 (1990) 251–280.

[29] A.E. Gelfand, Gibbs sampling, Journal of the American Statistical Association 95 (2000) 1300–1304.

[30] H.M. Wallach, I. Murray, R. Salakhutdinov, D. Mimno, Evaluation methods for topic models, Proceedings of the 26th International Conference on Machine Learning (ICML), 2009.

[31] H.M. Wallach, D. Mimno, A. McCallum, Rethinking LDA: why priors matter, Neural Information Processing Systems (NIPS), 2009.

Hsin-Min Lu received the bachelor's degree in business administration and MA degree in economics from the National Taiwan University, and the PhD degree in information systems from the University of Arizona. He is an Assistant Professor in the Department of Information Management at the National Taiwan University. His papers have appeared in IEEE Transactions of Knowledge and Data Engineering, IEEE Intelligent Systems, Journal of Biomedical Informatics International Journal of Medical Informatics Journal of Forecasting, Decision Support Systems, and Review of Accounting Studies. His research interests include data mining, text mining, and health informatics
