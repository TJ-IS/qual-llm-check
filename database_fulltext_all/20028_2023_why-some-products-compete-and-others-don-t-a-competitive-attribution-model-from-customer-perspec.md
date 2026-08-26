---
otero_id: 20028
otero_key: "CTJZ48FZ"
title: "Why some products compete and others don't: A competitive attribution model from customer perspective"
authors: "Yang Qian; Yuanchun Jiang; Jennifer Shang; Yidong Chai; Yezheng Liu"
year: "2023"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2023.113956"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Why some products compete and others don't: A competitive attribution model from customer perspective

Yang Qian <sup>a,b</sup>, Yuanchun Jiang <sup>a,b</sup>, Jennifer Shang <sup>c,\*</sup>, Yidong Chai <sup>a,b</sup>, Yezheng Liu <sup>a,d</sup>

<sup>a</sup> School of Management, Hefei University of Technology, Hefei, Anhui 230009, China

<sup>b</sup> Key Laboratory of Philosophy and Social Sciences for Cyberspace Behaviour and Management, Hefei, Anhui 230009, China

c The Joseph M. Katz Graduate School of Business, University of Pittsburgh, Pittsburgh, PA 15260, USA

<sup>d</sup> National Engineering Laboratory for Big Data Distribution and Exchange Technologies, Shanghai 200436, China

## A R T I C L E I N F O

Keywords: Competitor identification Competitive aspects Customer preferences Topic model Customer reviews

## A B S T R A C T

Competitive intelligence uses information collected about competitors to derive better managerial insights. In this study, we focus on identifying the competitors and detecting the competitive dimensions concurrently. To achieve this goal, we propose an aspect-level competitive attribution model (a variation of the topic model) to leverage consumer-reviewed products and their review texts. To better analyze product relations and the un derlying competitive aspects, we consider consumer limited attention when modeling consumers' preferences and introduce a background aspect to filter out the trivial and maintain the valuable competition-related in formation in review texts. We validate this approach using a dataset of 785 products reviewed by 15,669 consumers in the auto industry. Based on the empirical experiments, we show that our model can accurately infer high-quality competitive segments and decipher competition-related aspects corresponding to these segments. To highlight differences, we conduct comparisons and find our approach outperforms the benchmark models meaningfully in the literature when predicting consumers' online behaviors.

## 1. Introduction

With the market competition becoming fierce, a growing number of firms have turned to computational intelligence to conduct competitive analysis. Using information technology, competitive intelligence has been an essential component of deriving better managerial strategies. Driven by artificial intelligence (AI), companies use internal (e.g., user feedback) and external data (e.g., social media) to identify competitors that may pose threats to their brands and products [1,2]. Traditional competitive analysis is conducted from the firm perspective and regards the products with similar features as competitors. In the emerging era of big data, companies are striving to understand competition from the customer perspective [3,4]. Exploring customer opinions on competitive products helps companies allocate marketing resources to maximize their utility.

Recently, online platforms (e.g., forums, blogs, and other social media) have become important channels to record customer comments and feedback data from many aspects. Such contents contain compara tive information, which offers a rich source for companies to detect customers' sentiments and needs about the products [5,6]. Competitive intelligence analysis from online user-generated content (UGC) is an emerging direction of operations and marketing research. For example, Zuo et al. [7] identify the market structure and analyze the competitive power based on clickstream data. Netzer et al. [8] use online reviews to mine competitive relationships between products. While the extant studies stated the usefulness of the customer-created data, they mainly explore the co-occurrence pattern of products and the valuable text in formation is ignored. For example, from a user comment, “I considered several comparable BMWs and Mercedes-Benz but felt the Volvo would be the best combination of sports, luxury and technology”, the co-occurrent BMWs, Mercedes-Benz and Volvo would be extracted as potential com petitors by the current literature. The competitive aspects (i.e., sports, luxury and technology) stated in the comment are not fully utilized in the current study of competitiveness, though they can further reveal customer concerns for the competing products.

Haans [9] emphasizes that companies should not only know who their competitors are but also grasp the specific competitive dimensions, so as to position in the marketplace and focus on what matters.

Extracting competitive aspects from UGC enables firms a better under standing of the competitive dimensions from the customer perspective. Lately, researchers have started to conduct aspect-level competitor analysis. For example, Wang et al. [10] proposed a text-mining approach based on Latent Dirichlet Allocation to extract the key topics (or aspects) from online reviews. Though useful, current studies emphasize competitive aspect analysis for given competitors; but do not integrate the competitive aspects into the process of competitor identification.

In this study, we propose a model to simultaneously identify com petitors and explore the competitive aspects from the customer perspective. We focus on addressing two questions: (1) How to identify the competitive segments based on large-scale online customer behav iors? Each competitive segment contains several products that compete fiercely within the same segment and less outside the segment. (2) How to detect the competitive aspect of the products in each segment? Each competitive aspect consists of a set of words that reveal customer con cerns when they make a choice among competitors. The competitive aspect can be regarded as the reason for product competition.

To address the above questions, we exploit two types of data: user reviewed products and review contents (as shown in Fig. 1). Prior studies have focused on utilizing user reviews to extract co-occurring products for competitive analysis [8]. However, the sparsity of co occurrence data and the non-standard language of online reviews are serious limitations of these studies. Instead, to uncover the competitive segments, we make use of products mentioned in users' reviews (reviewed products), which have not been explored in the literature. Due to the uncertainty of purchasing durable goods, customers often seek information about products through inquiries and comments on line. The products reviewed in an online forum reveal the customer's interests before purchase. A consumer's purchase decision-making pro cess can be divided into two stages: product consideration and product evaluation [11]. The process of consumers commenting on products corresponds to the first stage. Thus, we combine each customer's reviewed products to construct consideration sets which are then used to explore the relations between products. Since the words in customer reviews voice their thoughts and opinions on different aspects of prod ucts, the textual contents of user reviews are useful data to infer customer concerns and needs [12]. Therefore, we employ the valuable information embedded in the textual content of user reviews to infer competitive aspects and uncover the reasons behind product competition.

From technical viewpoint, we propose a novel probabilistic topic model, called the Aspect-level Competitive Attribution (ACA) model. The ACA model extends the topic models [13] to meet the special characteristics of the competition context and has three distinct features. First, we incorporate the reviewed products and the textual contents of customer reviews into a unified framework, which enables us to detect the competitive segment and the competitive dimensions (aspects) jointly. Second, we take into account customers' limited attention when modeling customer choices among competing products. Limited atten tion is a well-known psychological factor and deserves a prominent role in shaping customers' choice behavior [14,15]. The psychology litera ture provides evidence that customers often face the problem of infor mation overload and choice overload in social media [16]. Due to the limited attention, customers often pay close attention to a small subset of the available information and overlook others. For example, the customer in Fig. 1 only focuses on a handful of preferred products (e.g., Audi A4L and Acura TLX) and posts online comments on a few interested aspects (e.g., promotion and paying taxes). To learn about user prefer ences, we borrow the theory of limited attention and introduce the “Spike and Slab” prior [17,18] to construct the ACA model. Third, we extract the competition-related aspects and a background aspect, to filter out the trivial and maintain the valuable competitive information in the review contents. The main reason for introducing the background aspect is that the reviewed contents often face noise and irrelevant in formation. We assume that the background aspect consists of non informative knowledge and the competition-related aspects are the di mensions truly cared by customers. We design a Bernoulli mixture mechanism to distinguish these aspects.

## The main contributions of this research are threefold:

(1) This study contributes to the rapidly expanding literature on data-driven decision support based on competitive analysis. Prior liter ature has stated that competitive analysis is the key factor to support firms' decision-making [19]. Much of this literature has focused on using the textual contents of online reviews to detect competitors [8], assess product competitive advantages [20], and analyze product defects [21]. Compared with these works, we are the first to jointly use the textual contents and reviewed products related to online reviews to simulta neously identify competitors and explore the competitive aspects.

(2) We extend the competitive intelligence literature by developing an interpretable machine learning method for processing unstructured text data. Specifically, we propose a novel probabilistic topic model that concurrently infers competitive segments and corresponding competi tive aspects, which explain the underlying reasons for product compe tition. The conventional way of treating product relations and underlying aspects separately is rather unsatisfactory, as competitive features do not play a role in mapping products' competitive position. In contrast, the proposed model extracts competitive aspects for each segment and uses the competitive aspects to discover product competition.

(3) Finally, we contribute to the burgeoning literature on analyzing customer preferences from user-generated content. Previous studies mainly use different types of online data (e.g., rating data and reviews) to infer customer product-level preferences [22,23]. We extend these works by quantifying customer preferences over contending products and competitive aspects. Operationally, firms need to know both their rivals and customers' choices facing substitutes. The proposed model provides unique insights since it considers customers' limited attention in modeling customers' choices among competitors.

![](/api/attachments/CTJZ48FZ/fulltext/images/47576c7baa9e8c9b2820e2dc9a0c67249f1c770bcbd8d2eb6fa3b4640ed8e919.jpg)  
Fig. 1. Reviewed products and textual contents of reviews.

The remainder of the paper is organized as follows. Section 2 pro vides a brief overview of the related literature. Section 3 introduces our model. Section 4 presents the empirical results. Finally, Section 5 gives concluding remarks and future research directions.

## 2. Literature review

In this section, we review the relevant literature on competitor identification, customer opinion mining, and topic models for natural language processing (NLP).

## 2.1. Competitor identification

Competitor identification, a major component of organizational strategic planning, has attracted considerable attention from practi tioners and researchers. Research on competitor analysis has been conducted from two directions: firm perspective and customer perspective. The firm-based approach classifies competitors by assessing the similarity over attributes of competing firms. For example, Chen [24] proposes a framework for competitor identification with two cat egories of firm information: market commonality and resource similar ity. Through questionnaire surveys, they obtain a series of firm attributes $( \mathbf { e . g . }$ , products offered and price) that affect the classification task. The weakness of the firm-based approach is that it requires a sys tematic competition evaluation system, e.g., resource elements, and market elements, corresponding to the attributes of the firm, which is costly and time-consuming. In addition, the firm-based approach is unable to reveal how customers perceive and respond to firms' brand and products.

Recently, researchers have focused on customer-based approaches that identify competitors based on customers' preferences and behaviors [25]. Traditional studies often relies on surveys and scanner panel data [26,27]. However, survey data are restricted by the cognitive capacity of consumers, which may produce blind spots in the competitive analysis [28]. In turn, analysis of panel data requires repeat purchases, which is hard to adapt to durable goods (e.g., cars). Recently, online usergenerated content (UGC) is catching on in competition analysis. Nam et al. [29] analyze brand attribute information gained from usergenerated tagging data for brand relationship research. Ringel and Skiera [3] construct consideration sets from clickstream data and use the community detection method to map product competition. Liu et al. [4] introduce favorite data and propose a bipartite graph model to identify the competitors. Lately, Wang et al. [30] extract comparable entities from web search logs. However, these studies only focus on detecting competitors or visualizing the competitive market structure, without integrating the competitive aspects (dimensions) related to product features. To help us position our research in the literature, we compare our work with prior studies in Appendix A.

In this research, we continue in the direction of analyzing product competition from UGC. And we develop an interpretable model to jointly use the textual contents and reviewed products.

## 2.2. Customer opinion mining

Customer opinion mining refers to the use of machine learning methods to identify customers' thoughts toward brands, products, or their attributes. Such studies can be divided into two categories: senti ment analysis and information extraction [31,32]. Sentiment analysis focuses on tracking customers' emotions toward a particular product or brand. For example, Lau et al. [33] use machine learning methods to mine sentiments hidden in online product reviews for improving sales forecasting performance. Mukhopadhyay et al. [34] measure the senti ment scores of the review texts and explore their impact on sales in a competitive environment.

Information extraction focuses on deriving detailed and specific in formation from massive data $( \boldsymbol { \mathrm { e . g . } }$ , online reviews). For example, Abrahams et al. [35] propose a text-mining framework to extract attri butes such as stylistic features, and product features, from social media comments. These features are employed as inputs to discover product defects. To examine how image content affects customer engagement, Li and Xie [36] use image processing methods to identify the image characteristics in social media posts.

The extant studies suggest extracting information from usergenerated content is an effective approach to understand customer be haviors. While many methods have been proposed to analyze customer needs and emotions, extracting competitive aspects to enhance competitor identification performance has not been explored. This research will extract competitive aspects from user-generated content and embeds them into competitor identification.

## 2.3. Topic models for natural language processing

Natural language processing (NLP) has become an increasingly popular technique in the operations management and marketing field [37–39]. Latent Dirichlet Allocation (LDA) is one of the most classical topic models for NLP tasks [13]. It is an unsupervised learning algorithm to extract topics from the textual corpus. Owing to their superiorities in interpretability and scalability, LDA-based models have been popular in analyzing textual contents. For example, Xiao et al. [40] use LDA to extract hidden topics as new variables for investigating the effects on crowdfunding platforms. Zheng et al. [21] propose a novel topic model for the detection of product defects. Although these models can learn the latent semantic pattern from textual data, they cannot control the pos terior sparsity, e.g., document-topic distribution [41]. In practice, a document often focuses on some salient topics instead of involving a wide variety of topics. Understanding the sparsity nature of information plays an important role in UGC analysis.

The application of the topic model has become an important trend because much business wisdom is embedded in textual data. This paper proposes a new topic model for competitive analysis. The proposed model significantly extends the current topic models by jointly using multi-source of data. It models customers' limited attention and in tegrates customer preferences with their behaviors into the competitive environment.

## 3. Aspect-level Competitive Attribution (ACA) model

In this section, we propose the ACA model to concurrently identify the competitors and detect the competitive dimensions. Fig. 2 gives the graphical representation of the model with three phases: (1) Modeling limited preference; (2) Modeling competitive segments and topics; and (3) Linking limited preference with review behavior. Different from previous studies that focus on the analysis of group consumer behavior [3], we focus on constructing the competitive analysis by modeling in dividual consumer behavior. In Phase I, we assume that each user's comment behavior is driven by his/her limited preference. In Phase ${ \mathrm { I I } } ,$ to identify the competitive segments and competition-related aspects, we introduce two discrete probability distributions over products and words, and introduce a background topic to manage the noise infor mation in textual reviews. Phase III connects consumers' limited pref erences to their specific review behavior.

Before detailing the proposed model, we will first define the nota tions necessary for our research. Suppose that there are |M| customers in the market. Each customer m $\in \{ 1 , 2 , \cdots , | M | \}$ } produces a series of re views. Each review corresponds to a reviewed product. We first construct consideration sets for each customer via merging products that he commented on. The consideration set refers to the sets of products that customers considered in their purchase journey [42], which is used to infer product competition in our model. Assume these consideration sets contain a total of E unique products, and each product is indexed by $e \in \{ 1 , 2 , \cdots , E \}$ . Let $\pmb { e _ { m } } = \{ e _ { m 1 } , e _ { m 2 } , \cdots , e _ { m L _ { m } } \}$ denotes the set of all products in the consideration set of customer m. $L _ { m }$ denotes the size of customer m’s consideration set, and $e _ { m j }$ denotes the jth product that customer m commented on.

![](/api/attachments/CTJZ48FZ/fulltext/images/364e6ace47b1bf9de7bc4dc31bf26683f02ea38b1ca5794f5c0473495891be72.jpg)  
Fig. 2. The three phases of ACA model.

We build textual content for each customer by merging the review texts posted by the customer. We use the textual content of reviews to infer the competitive aspects. Assume that these textual contents contain a total of V unique words, and each word is indexed by $\nu \in \{ 1 , 2 , \cdots , V \}$ We denote the bag of words for the textual content of customer m using $\pmb { w } _ { m } = \{ w _ { m 1 } , w _ { m 2 } , \cdots , w _ { m N _ { m } } \}$ $w _ { m i }$ is ith word in the $m ^ { \mathrm { t h } }$ customer review and $N _ { m }$ is the total number of words. As depicted in Fig. 2, the input of our model contains two parts: customers' consideration sets and their review contents. We assume that products in the consideration sets can be assigned to K competitive segments. And these are K competitionrelated topics corresponding to these competitive segments.

## 3.1. Modeling limited preference

Evidence has shown that most customers only pay attention to few products and some interesting information, due to limited cognitive capacity and information-processing capabilities [11,43]. We thus take in the limited attention concept when modeling individual preference.

Different from the classical topic models $( \mathbf { e . g . , \ L D A } )$ which use Dirichlet prior and suppose customers have preferences on all topics [23,44], the proposed model assumes that customers make choices among a few competitive segments and assess products on a small number of focused aspects. We choose a “Spike and Slab” prior to model the limited attention. The “Spike and Slab” prior [45] is a classical approach for Bayesian variable selection. For topic models, this prior has been used to constrain the probabilistic distribution [18,46]. Specif ically, using 0–1 dummy variables we can determine whether a topic is relevant to a document, or whether a word belongs to a topic. The “Spike and $\mathbf { S l a b } ^ { \prime \prime }$ prior can ensure that customers' preference is highly concentrated over a narrow space, revealing their limited attention.

Our model uses this prior by introducing the binary variable $c _ { m k } ,$ where $c _ { m k } \in \{ 0 , 1 \}$ indicates whether customer m is interested in the competitive segment $k \in \{ 1 , 2 , \cdots , K \}$ or uses the competition-related topic k $\in \{ 1 , 2 , \cdots , K \}$ to post reviews. If the competitive segment k or competition-related topic k is in accord with customer m’s preference, $c _ { m k } = 1 ;$ ; otherwise $c _ { m k } = 0$ . The $c _ { m k }$ follows a Bernoulli distribution with a parameter $\pi _ { m } \colon$

$$
c _ {m k} \sim \text { Bernoulli } (\pi_ {m})\tag{1}
$$

where $\pi _ { m }$ is drawn from a Beta distribution with hyperparameters p and q:

$$
\pi_ {m} \sim \mathrm{Beta} (p, q)\tag{2}
$$

Using “Spike and Slab” prior, we can effectively model user limited attention. Let the K dimensional vector $\pmb { \theta } _ { m }$ denote the customer m preference distribution over each competitive segment or competition related topic. $\pmb { \theta } _ { m }$ is related to the Bernoulli variables ${ \pmb { c } } _ { m } = \{ { \pmb { c } } _ { m k } \} _ { k } ^ { K } =$ = and follows a Dirichlet distribution:

$$
\boldsymbol {\theta} _ {m} \sim \text { Dirichlet } \left(\gamma_ {0} \boldsymbol {c} _ {m} + \gamma_ {1} \mathbf {1}\right)\tag{3}
$$

where 1 is a K dimensional vector with all elements 1; γ denotes smoothing prior and $\gamma _ { 1 }$ denotes weak smoothing prior.<sup>1</sup> Because the value of $\gamma _ { 1 }$ is very close to zero, customer preference distribution $\pmb { \theta } _ { m }$ is determined by the non-zero elements in $c _ { m } .$ Let $C _ { m } = \{ k : c _ { m k } = 1 , k \in$ $\{ 1 , 2 , \cdots , K \} \}$ denote the set of competitive segments or competitionrelated topics. Since $\left| C _ { m } \right| \ll K ,$ our model confines each customer pref erence distribution into a limited space.

## 3.2. Modeling competitive segments and two types of topics

For each competitive segment $k \in \{ 1 , 2 , \cdots , K \}$ , we define a E dimensional vector $\varphi _ { k }$ as a probability distribution over the products, where the element $\varphi _ { k e }$ is the probability weight with which product e is assigned to this segment. We assume that $\varphi _ { k }$ follows a Dirichlet distri bution with a symmetric prior $\beta _ { 0 } \colon$

$$
\boldsymbol {\varphi} _ {k} \sim \text { Dirichlet } (\beta_ {0})\tag{4}
$$

For a given competitive segment, customers often choose a specific aspect to discuss in the product forum. Therefore, we define a competition-related topic for each segment to describe the competitive aspect of the segment. We model each competition-related topic k $\in$ $\{ 1 , 2 , \cdots , K \}$ as a V dimensional vector $\phi _ { k } ,$ , where the element $\phi _ { k \nu }$ is the probability weight of the word v given the topic k. Similarly, we assume that $\phi _ { k }$ is drawn from a Dirichlet distribution with a symmetric prior $\beta _ { 1 } \colon$

$$
\boldsymbol {\phi} _ {k} \sim \text { Dirichlet } (\beta_ {1})\tag{5}
$$

Note that our model can build a one-to-one relationship between φ and $\phi _ { k }$ . The one-to-one relationship reflects that each competitive segment corresponds to a competition-related topic. In practice, online reviews are often filled with massive irrelevant and noisy information. To infer the competition-related topics more efficiently, we also define a background topic $\pmb { \phi } ^ { \prime }$ that is a V dimensional vector, to filter out the irrelevant information. The element $\phi _ { \nu } ^ { \prime }$ denotes the probability weight of the word v belonging to the background topic. We draw the $\phi ^ { \prime }$ from a Dirichlet distribution with a symmetric prior $\beta _ { 2 } \mathrm { : }$

$$
\boldsymbol {\phi} ^ {\prime} \sim \text { Dirichlet } (\beta_ {2})\tag{6}
$$

## 3.3. Linking limited preference with review behaviors

In the competitive environment, customers proceed with their re view journeys driven by their preferences. In our model, the preference distribution $\pmb { \theta } _ { m }$ determines customer m's decisions on which products to comment on and what aspects to use for describing these products. For the observed jth product in $e _ { m } ,$ , we draw its corresponding competitive segment $f _ { m j }$ from a Multinomial distribution with parameter $\theta _ { m } .$ Given the competitive segment $f _ { m j } \in \{ 1 , 2 , \cdots , K \}$ , the product $e _ { m j }$ can be drawn from a Multinomial distribution associated with this competitive segment $\varphi _ { f _ { m } }$ . We use a hierarchical representation to model this process:

$$
f _ {m j} \sim \text { Multinomial } (\boldsymbol {\theta} _ {m})\tag{7}
$$

$$
e _ {m j} \sim \text { Multinomial } \left(\boldsymbol {\varphi} _ {f _ {m j}}\right)\tag{8}
$$

For online reviews, we incorporate a Bernoulli mixture mechanism by assuming that each textual content $w _ { m }$ is a mixture of competitionrelated topics and the background topic. More specifically, we define a binary variable $b _ { m i } \in \{ 0 , 1 \}$ that acts as a switch. It determines that the word $w _ { m i }$ comes from which topic. Namely, $b _ { m i } = 1$ indicates that $w _ { m i }$ is a valuable word, and it should be drawn from the competition-related topic. $b _ { m i } = 0$ denotes that $w _ { m i }$ is an irrelevant or noisy word, and it should be drawn from the background topic. We generate $b _ { m i }$ from the Bernoulli distribution with parameter $\mu _ { m } .$

$$
b _ {m i} \sim \text { Bernoulli } (\mu_ {m})\tag{9}
$$

where $\mu _ { m }$ characterizes how likely a word in $w _ { m }$ is generated by a competition-related topic. To ensure conjugacy in inference, we use hyperparameters r and s in Beta distribution:

$$
\mu_ {m} \sim \operatorname{Beta} (r, s)\tag{10}
$$

$[ \boldsymbol { \mathrm { f } } \boldsymbol { b } _ { m i } = 1$ , we also use the customer preference distribution $\pmb { \theta } _ { m }$ to pick a competition-related topic $z _ { m i } .$ . Given $z _ { m i } \in \{ 1 , 2 , \cdots , K \}$ , we model the word $w _ { m i }$ via a Multinomial distribution related to this topic $\phi _ { z _ { m i } } \mathrm { : }$

$$
z _ {m i} \sim \text { Multinomial } (\boldsymbol {\theta} _ {m})\tag{11}
$$

$$
w _ {m i} \sim \text { Multinomial } \left(\boldsymbol {\phi} _ {z _ {m i}}\right)\tag{12}
$$

If $b _ { m i } = 0 ,$ , we directly use a Multinomial distribution with the parameter $\phi ^ { \prime }$ to draw w :

$$
w _ {m i} \sim \text { Multinomial } \left(\boldsymbol {\phi} ^ {\prime}\right)\tag{13}
$$

## 3.4. Model inference

For better understanding, we detail the process of generating two data types in Appendix B. Using the observed data of all consumers' consideration sets and review texts, we seek to infer the parameters that contain $c _ { m k } , b _ { m i } , f _ { m j } , z _ { m i } , \varphi _ { k } , \phi _ { k } , \phi ^ { \prime } ,$ and $\theta _ { m } .$ In Appendix $\mathrm { C } ,$ we give the complete likelihood of the observed data conditional on the hyper parameters, and analyze that exact model inference is intractable. Following the prior literature [47], we select an efficient MCMC sam pling method, called the collapsed Gibbs sampling algorithm, to approximate the posterior distribution. The collapsed Gibbs sampling algorithm requires iteratively sampling each variable from its condi tional posterior distribution over the remaining variables. Using Bayes rule, we first calculate the joint conditional distribution $c _ { m }$ and $\pi _ { m } .$

$$
P \left(\boldsymbol {c} _ {m}, \pi_ {m} | r e s t\right) \propto \prod_ {k = 1} ^ {K} P \left(c _ {m k} \mid \pi_ {m}\right) P \left(\pi_ {m} \mid p, q\right) \frac {\mathbb {I} \left[ A _ {m} \in C _ {m} \right] \Gamma \left(\left| C _ {m} \right| \gamma_ {0} + K \gamma_ {1}\right)}{\Gamma \left(N _ {m} + L _ {m} + \left| C _ {m} \right| \gamma_ {0} + K \gamma_ {1}\right)}\tag{14}
$$

where $\mathbb { I } [ \bullet ]$ is an indicator function, and $r e s t = \{ \beta _ { 0 } , \beta _ { 1 } , \beta _ { 2 } , p , q , r , s , \gamma _ { 0 } , \gamma _ { 1 } \}$ denotes the collection of all hyperparameters. $A _ { m } = \{ k : ( n _ { m } ^ { k } + x _ { m } ^ { k } ) > 0 ,$ k $\in \{ 1 , 2 , \cdots , K \} \}$ denotes the set of competitive segments and competitionrelated topics that have assignments in the consideration set and textual content of customer m. $n _ { m } ^ { \check { k } }$ denotes the number of products in the consideration set of customer m assigned to the competitive segment k. $x _ { m } ^ { k }$ is the number of words in the textual content of customer m assigned to the topic k. Based on Eq. (14), we integrate out the variable $\pi _ { m }$ to infer $c _ { m k } .$

$$
\propto \left\{ \begin{array}{c} P (c _ {m k} = c | r e s t) \\ \left(N _ {m, c} ^ {M C} + p\right) \frac {\mathbb {I} [ A _ {m} \in C _ {m} ] \Gamma (| C _ {m} | \gamma_ {0} + K \gamma_ {1})}{\Gamma (N _ {m} + L _ {m} + | C _ {m} | \gamma_ {0} + K \gamma_ {1})} \text { for } c = 1 \\ \left(N _ {m, c} ^ {M C} + q\right) \frac {\mathbb {I} [ A _ {m} \in C _ {m} ] \Gamma (| C _ {m} | \gamma_ {0} + K \gamma_ {1})}{\Gamma (N _ {m} + L _ {m} + | C _ {m} | \alpha + K \gamma_ {1})} \text { for } c = 0 \end{array} \right)\tag{15}
$$

where $N _ { m , \textit { ( ) } } ^ { M C }$ denotes the total number of times the binary variable c is associated with customer m. Next, we calculate the conditional distri bution of ${ \mathrm { ~ \it ~ { ~ f ~ } ~ } } _ { m j }$ as follows:

$$
\begin{array}{c} P \left(f _ {m j} = k | \mathbf {f} _ {- (m j)}, \mathbf {z}, e _ {m j} = e, \mathbf {E} _ {- (m j)}, \mathbf {W}\right) \\ \propto \left(n _ {m, - (m j)} ^ {k} + x _ {m} ^ {k} + c _ {m k} \gamma_ {0} + \gamma_ {1}\right) \left(\frac {n _ {k , - (m j)} ^ {e} + \beta_ {0}}{n _ {k , - (m j)} ^ {(*)} + E \beta_ {0}}\right) \end{array}\tag{16}
$$

where f $- ( m j )$ denotes the competitive segment assignments for all prod ucts except $f _ { m j }$ and z denotes all the topic assignments for all words in customer reviews. ${ \bf E } _ { - ( m j ) }$ denotes consideration sets except $e _ { m j } .$ . n<sup>e</sup> is the number of times product e is assigned to competitive segment k. $n _ { k } ^ { ( * ) }$ is the total number of products that are assigned to the competitive segment $k .$ The subscript − (mj) means the count without $e _ { m j } .$ From Eq. (16), we find that the conditional probability of $f _ { m j }$ relies on the product of two parts. The first part reveals the degree customer m pays attention to the competitive segment k. The second part measures the fraction of the number of times product e is assigned to competitive segment k.

Similar to $\operatorname { E q . }$ (16), the conditional distribution of $b _ { m i }$ is provided as follows:

$$
\begin{array}{l} P \left(b _ {m i} = b \mid w _ {m i} = v, \mathbf {W} _ {- (m i)}, \mathbf {b} _ {- (m i)}, \mathbf {f}, \mathbf {z}\right) \\ \propto \left\{ \begin{array}{l} \left(n _ {m, - (m i)} ^ {b _ {m i} = b} + r\right) \frac {x _ {k , - (m i)} ^ {v} + \beta_ {1}}{x _ {k , - (m i)} ^ {(*)} + V \beta_ {1}} \text { for } b = 1 \\ \left(n _ {m, - (m i)} ^ {b _ {m i} = b} + s\right) \frac {x _ {- (m i)} ^ {v} + \beta_ {2}}{x _ {- (m i)} ^ {(*)} + V \beta_ {2}} \text { for } b = 0 \end{array} \right. \end{array}\tag{17}
$$

where $\mathbf { W } _ { - ( m i ) }$ denotes all words except $w _ { m i }$ and $\mathbf { b } _ { - ( m i ) }$ denotes the binary variables corresponding to all words without considering $w _ { m i } . \ n _ { m } ^ { b _ { m i } = b }$ is the total number of words in reviews of customer m that occur in competition-related topics $( b = 1 )$ or the background topic $( b = 0 )$ . x<sup>v</sup> is the number of times the word v in the vocabulary is assigned to competition-related topic k. $x _ { k } ^ { ( * ) }$ is the total number of words in the reviews that are assigned to competition-related topic k. $x ^ { \nu }$ denotes the number of times the word v is assigned to the background topic. $x ^ { ( * ) }$ denotes the total number of words assigned to the background topic.

Once ascertaining the binary variables b using Eq. (17), we can infer the competition-related topic assignment $z _ { m i }$ for word $w _ { m i }$ using the following conditional distribution:

$$
\begin{array}{c} P \left(z _ {m i} = k | \mathbf {z} _ {- (m i)}, \mathbf {f}, w _ {m i} = v, \mathbf {W} _ {- (m i)}, \mathbf {E}\right) \\ \propto \left(n _ {m} ^ {k} + x _ {m, - (m i)} ^ {k} + c _ {m k} \gamma_ {0} + \gamma_ {1}\right) \left(\frac {x _ {k , - (m i)} ^ {v} + \beta_ {1}}{x _ {k , - (m i)} ^ {(*)} + V \beta_ {1}}\right) \end{array}\tag{18}
$$

Based on the above Equations, we can update the latent variables with Gibbs sampling in turn. This procedure needs many iterations to ensure convergence. Subsequently, we can estimate the model param eters $\varphi _ { k } , \phi _ { k } , \phi ^ { \prime } { } _ { \mathrm { { i } } }$ , and $\pmb { \theta } _ { m }$ using the following Equations.

$$
\varphi_ {k e} = \frac {n _ {k} ^ {e} + \beta_ {0}}{n _ {k} ^ {(*)} + E \beta_ {0}}\tag{19}
$$

$$
\phi_ {k v} = \frac {x _ {k} ^ {v} + \beta_ {1}}{x _ {k} ^ {(*)} + V \beta_ {1}}\tag{20}
$$

$$
\phi_ {v} ^ {\prime} = \frac {x ^ {v} + \beta_ {2}}{x ^ {(*)} + V \beta_ {2}}\tag{21}
$$

$$
\theta_ {m k} = \frac {n _ {m} ^ {k} + x _ {m} ^ {k} + c _ {m k} \gamma_ {0} + \gamma_ {1}}{N _ {m} + L _ {m} + | C _ {m} | \gamma_ {0} + K \gamma_ {1}}\tag{22}
$$

For the collapsed Gibbs sampling, we set the hyperparameters as suggested by Griffiths and Steyvers [47], i.e. $\begin{array} { r } { \gamma _ { 0 } = \frac { 5 0 } { K } ; } \end{array}$ β<sub>0</sub>, $\beta _ { 1 }$ and $\beta _ { 2 }$ are equal to 0.1. As suggested by [48], we set the hyperparameters $\gamma _ { 1 } = 1 . 0$ $\times ~ 1 0 ^ { - 7 } , p = q = 1$ and $r = s = 1$ . To ensure convergence, we set the number of iterations as 2000. Appendix D gives the pseudocode of our inference algorithm. And we theoretically analyze the time complexity in the Gibbs sampling procedure of the proposed model.

## 4. Empirical study

## 4.1. Data descriptions

We collect the data from the well-known Forum Edmunds.com by using customized Web crawling techniques. To avoid unwieldiness, we start with the forum site of all car models to obtain all user's nicknames. On Edmunds.com, one can place a URL prefix in front of a user's nick name to visit his homepage. This way, we gather all users' reviews on their homepages, including reviewed products and textual contents (see Fig. 1). Based on the raw data, we (1) select all comments from January 2013 to June 2018; (2) filter out the long reviews exceeding 400 words since they are generally promotion contents; (3) link each customer's textual contents and reviewed products (as consideration set); (4) tokenize the merged textual contents into distinct terms, and then lowercasing all words; (5) remove URL links, non-alphabetical expres sions $( \boldsymbol { \mathrm { e . g . } }$ , # and %), rare words (appearing fewer than 5 times) and stop words (e.g., “there” and “about”) from the merged textual contents.

In Appendix E, Table E1 shows summary statistics of our dataset that are obtained after the preprocessing procedure. The data includes tex tual contents and reviewed products from $^ { 1 5 , 6 6 9 }$ customers about 785 products. On average, each customer's consideration set consists of 4.16 products. The standard deviation of the number of products reviewed by customers is 0.58. On average, a product is reviewed by customers 83.09 times.

## 4.2. Identifying the appropriate number of competitive segments

Before reporting on the results, we first determine the number of competitive segments K for the proposed model that best fit our dataset. Advised by Griffiths and Steyvers [47], we use the perplexity score as the measure to evaluate the goodness-of-fit and select K. For traditional topic models (e.g., LDA), perplexity score is algebraically equivalent to the inverse of the geometric mean of per-word likelihood. However, our model consists of two components: textual content and reviewed prod uct. Thus, we need to calculate the joint likelihood of per-product and per-word. Specifically, the perplexity score is defined as follows:

$$
\text { perplexity } (\mathbf {M} _ {\text { test }}) = \exp \left\{- \frac {\sum_ {m \in \mathbf {M} _ {\text { test }}} \log P (\boldsymbol {w} _ {m} , \boldsymbol {e} _ {m})}{\sum_ {m \in \mathbf {M} _ {\text { test }}} (N _ {m} + L _ {m})} \right\}\tag{23}
$$

where $\mathbf { M } _ { t e s t }$ denotes a test dataset that is selected from our dataset. In our experiments, we vary the number of competitive segments from 10 to 60, and evaluate the average perplexity scores of fivefold crossvalidation. A lower perplexity score indicates better model performance.

Fig. 3 shows the average perplexity scores of our cross-validation. We note that the perplexity scores do not vary significantly from 40 to 60 competitive segments. Empirically, topic models often suffer from overfitting when K increases [13,44]. The best-fitting model is that with the smallest competitive segments, i.e., $K = 4 0$

## 4.3. Analysis of competitive segments

From the inferred $\varphi _ { k }$ in $\operatorname { E q . }$ (19), we can group competitors into K segments and rank products in each segment based on their competitive power. Fig. 4 presents the ten top-ranked products for sample segments. We find most of cars in segment 2 are pickup trucks, $\mathrm { e . g . , }$ , Ram\_1500. Segment 4 includes not only luxury sport-utility vehicles (e.g., Vol vo\_XC90) but also high-end sedan cars (e.g., Benz\_C). Segment 12 is mainly associated with economy-class cars, including standard (e.g., Toyota\_Camry) and hybrid vehicles $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } ,$ Toyota\_Camry-Hybrid). Segment 21 contains a set of sports cars (e.g., Porsche\_911). Vehicles in segment 28 are affiliated with multi-purpose vehicles (MPVs) that offer large cargo space. Segment 33 consists of a series of off-road SUVs (e.g., Jeep\_Cherokee) and pickup trucks (e.g., Ford\_F150).

Fig. 4 gives rich insights into competition in the car industry: (1) We show products across categories may compete with each other. SUVs and sedans compete in segment 4. Standard vehicles and hybrid cars compete in segment 12. The cross-category competition extracted can help firms capture products in “adjacent categories” affecting their market share. (2) We identify where product cannibalization occurs. A firm's newly launched product may compete intensely with the existing ones, as exemplified by Volvo\_XC90, XC60, and S60 in segment 4. Detecting intra-brand conflicts helps managers adjust strategies to attract users of other brands. (3) we discover that the derived segments have little overlap, indicating products can compete in multiple segments.

Fig. 5 uses Sankey diagrams to show relations among some segments and their competitive structure, where five segments are shown with their corresponding products. The relations between segments and products are connected by curved lines; and the thickness of each line denotes the representative degree of a product in the segment. Fig. 5 (a) shows that Ford\_F150 and Chevrolet\_Colorado compete in segments 2 and 33. Fig. 5 (b) shows Honda\_Civic competes against numerous cars in segments 8 and 32. From Fig. 5, managers can not only appraise their direct competitors but also obtain cues about tracking indirect rivals. For instance, Ram\_1500 could be regarded as the second-degree indirect competitor of Jeep\_Cherokee, according to the competition path Jeep\_Cherokee→Chevrolet\_Colorado→Ram\_1500.

![](/api/attachments/CTJZ48FZ/fulltext/images/95776c01c9585a3d97b8f3271525c25ad8723d739585ca7b7f57bd40524655ff.jpg)  
Fig. 3. Perplexity score with different number of competitive segments.

![](/api/attachments/CTJZ48FZ/fulltext/images/eeb238651c96c8c1eddfe2ff3cb01f45c4d582fd93598aeb61358924c1113487.jpg)  
Fig. 4. Example competitive segments learned by our model.

## 4.4. Analysis of competitive aspects

From the inferred $\phi _ { k }$ in $\operatorname { E q . }$ (20), we extract the competition-related topics to label the competing features of the cars in each segment. Table 1 presents six competition-related topics corresponding to the competitive segments in Fig. 4. For ease of comparison, we label each topic based on the meaning conveyed by its top words.

From Table 1 we find that although many features exist for cars, users usually only care for a few distinctive and limited aspects fo different segments. For example, the most important aspects in segment 2 are fuel and power. The words such as “engine,” “gas,” “mpg,” “rpm,” and “mph” are frequently mentioned. For segment 4, the competitive dimensions for luxury cars concentrate on price and financial factors. The words such as “price,” “mf” (i.e., money factors), “msrp” (i.e., manufacturer's suggested retail price), “month” and “bank” are the top mentioned words. Table 1 indicates that the proposed ACA model can identify key competitive dimensions concerned by users, while grouping products into competitive segments. The key competitive dimensions identified by our model provide managers insights to develop targeted strategies to gain edges on product competition.

From Table 1, we see that our model extracts suitable words to represent the competitive aspects. This is because the common and noisy words are all removed by introducing the background topic. In Appendix F, we show the probability rank of the words in the background topic. We find that our model can filter out these words without information to enhance the detection quality of competition aspects. In addition, we explore the sentiments about detailed aspects of products in Appendix G.

## 4.5. Analysis of limited preference

Fig. 6 presents the preference distributions and features concerned by four randomly selected customers. To explore the dispersion and asymmetry of customer preferences, we measure the standard deviation and skewness of $\pmb { \theta } _ { m } .$ Fig. 6 shows the preference distribution and the focused aspects differ significantly across customers. Customer 1 evidently likes products in segment 2, while customer 2 prefers products in segment 4. The standard deviations of preference distribution for these two customers are 0.11 and 0.10, with skewnesses 5.60 and 5.18 respectively. The statistics indicate that the preferences of customer 1 and customer 2 are highly concentrated and asymmetric. In contrast, the preference of customer 3 is relatively evenly distributed across segments 9, 13, 15, and 23. Compared with customer 1 and customer 2, the standard deviations and skewnesses for customer 3 are lower (Std = 0.07; Skewness = 3.50). This finding suggests that customer 1 and customer 2 have relatively focused preferences and customer 3 is more scattered.

Although the four customers may prefer products in different seg ments, the topics are quite well-defined. For example, customer 1 is concerned about the aspects of fuel, power, and price (See Appendix H). Price is the dominant factor impacting customer 2's purchase decision, while customer 3 focuses on configuration and price (See Appendix H). Fig. 6 shows that the proposed model can estimate individual prefer ences to help firms develop precise strategies to coordinate operations and marketing functions.

To examine consumers' limited attention, we use empirical estima tion to obtain their segments and aspects. Fig. 7 displays the distribution of the number of segments and product features preferred by customers. We note that the average number of segments concerned by a customer is 2.43 and the average number of topics is 3.18. About 91% of cus tomers pay close attention to four or fewer segments. Fig.s 6 and 7 verify users' limited attention and enable firms to understand the competitive dimension from the individual's perspective.

![](/api/attachments/CTJZ48FZ/fulltext/images/f98688ae2dba6ad1eed5edb824684b40338414cbdc88228516fb1e643a4fef06.jpg)  
(a)

![](/api/attachments/CTJZ48FZ/fulltext/images/61739fb88e19d5778f6059fbb682320bc6c58b46ac83005623082a5149c1c5d7.jpg)  
(b)  
Fig. 5. Visualizing overlaps among competitive segments.

Table 1  
Competition-related topics associated with the competitive segments in Fig. 4.

<table><tr><td>Topic</td><td>2 (Fuel and Power)</td><td>4 (Price and Financial Service)</td><td>12 (Configuration and Experience)</td></tr><tr><td rowspan="10">Representative words</td><td>fuel</td><td>price</td><td>seat</td></tr><tr><td>altitude</td><td>mf</td><td>back</td></tr><tr><td>power</td><td>msrp</td><td>nice</td></tr><tr><td>engine</td><td>month</td><td>rear</td></tr><tr><td>pull</td><td>incentive</td><td>interior</td></tr><tr><td>mpg</td><td>bank</td><td>love</td></tr><tr><td>gas</td><td>allowance</td><td>feature</td></tr><tr><td>ecoboost</td><td>discount</td><td>comfortable</td></tr><tr><td>rpm</td><td>cash</td><td>light</td></tr><tr><td>mph</td><td>pay</td><td>color</td></tr><tr><td>Topic</td><td>21 (Speed and Design)</td><td>28 (Travel Function)</td><td>33 (Power and Handling)</td></tr><tr><td rowspan="10">Representative words</td><td>transmission</td><td>city</td><td>problem</td></tr><tr><td>speed</td><td>live</td><td>engine</td></tr><tr><td>engine</td><td>safety</td><td>repair</td></tr><tr><td>appreciate</td><td>touring</td><td>battery</td></tr><tr><td>curious</td><td>trip</td><td>control</td></tr><tr><td>design</td><td>room</td><td>issue</td></tr><tr><td>idea</td><td>family</td><td>check</td></tr><tr><td>luxury</td><td>enjoy</td><td>pump</td></tr><tr><td>performance</td><td>seat</td><td>fuse</td></tr><tr><td>sound</td><td>comfortable</td><td>complaint</td></tr></table>

## 4.6. Model comparison

In this section, we employ the coherence score and prediction ac curacy to evaluate whether the proposed ACA model can obtain more accurate results than the existing models. The proposed ACA model is compared empirically with the following seven benchmarks:

DMM: Dirichlet Multinomial Mixture (DMM) model is an unsuper vised model for clustering [49]. In the task of NLP, this model can obtain the representative words for each cluster. In our context, we conduct experiments by using texts and reviewed products, respectively. For the hyper-parameter setting, we set α = 50/K and $\beta = 0 . 1$

LDA: Latent Dirichlet Allocation (LDA) is widely used to mine topics from documents [13]. Recently, several studies have used this model to identify product perceptions and competitive market structure [29]. We apply this model to process texts and reviewed products, respectively. And we empirically set the hyperparameters α = 50/K and β = 0.1.

CNTM: Contrastive Neural Topic Model (CNTM) [50] is the latest model that aims to re-formulate the objective of neural topic model as a contrastive objective. We apply this model to process texts and reviewed products, respectively. For this model, we set the batch size to 300 and the learning rate to 0.001.

Link-LDA: This model is proposed to infer topics and influential nodes at the same time by using citation networks [51]. We empirically set the hyperparameters α = 50/K and $\beta _ { 0 } = \beta _ { 1 } = 0 . 1$

PTM: This model integrates the latent role assignment of each node to extend Link-LDA [52]. As for this model, we set the hyperparameters $\alpha = 5 0 / K , \beta = \beta _ { 1 } = 0 . 1$ and $\eta = 0 . 0 1$

nS-ACA: This model is a simplified version of the proposed ACA model, which does not employ “Spike and Slab” prior to model cus tomers' limited attention. To enhance the comparability, the related hyperparameters of nS-ACA are in line with our proposed model.

nB-ACA: This model is also a simplified version of the proposed ACA model, which does not consider the background topic to filter out the irrelevant and noise information. For the best results, we set the related hyperparameters of nB-ACA the same as our proposed model.

![](/api/attachments/CTJZ48FZ/fulltext/images/1b95a7ef4b3b2620ecdc362501b4a3afdc5c294ba2485267ff5a92aeb2eda573.jpg)  
(a) User 1

![](/api/attachments/CTJZ48FZ/fulltext/images/a355f58186d3e4f5882f1d495d740f435fb6694a14bccd88789eaccc400d276e.jpg)  
(b) User 2

![](/api/attachments/CTJZ48FZ/fulltext/images/3073e0da787b46252b33a65c5cf4a0ba41bffb70afc8d74b4f35b7fe38d16965.jpg)  
(c) User 3

Fig. 6. Example of customer preference distributions.  
![](/api/attachments/CTJZ48FZ/fulltext/images/46f2149951304dc32827bed81750e81a1b62caa2953f690a9f80c0aec38d14f1.jpg)  
(a)

![](/api/attachments/CTJZ48FZ/fulltext/images/4a9424929b98258f1af5aad57dafb05911d0f5a314b8972c48cb1d17725e93c5.jpg)  
(b)  
Fig. 7. Histogram of the number of segments and aspects.

## 4.6.1. Coherence score evaluation

In topic models, the coherence score is a popular metric to measure clustering performance and has been proven to be highly correlated with human judgment [53,54]. The coherence score assumes that words from the same topic are likely to co-occur in several documents of the corpus. This metric is similar to pointwise mutual information (PMI). However, measuring PMI relies on the counting of word co-occurrence frequencies over an external corpus [55]. In contrast, the metric of coherence score computes the values over the original corpus. In the context of competitive analysis, if a competitive segment is well interpretable to humans, the representative products related to this segment should be co-commented by many customers. Given a competitive segment k and its top T representative products $V ^ { k } = ( e _ { 1 } ^ { ( k ) } , e _ { 2 } ^ { ( k ) } , \cdots , e _ { T } ^ { ( k ) } )$ , the coherence score is defined as

$$
C _ {k} = \sum_ {t = 2} ^ {T} \sum_ {l = 1} ^ {t - 1} \log \frac {D \left(e _ {t} ^ {(k)} , e _ {l} ^ {(k)}\right) + \epsilon}{D \left(e _ {l} ^ {(k)}\right)}\tag{24}
$$

where D(e) is the number of customers who commented on product $e ,$ and $D ( e , e ^ { \prime } )$ is the number of customers who commented on both product e and e<sup>′</sup>. ϵ is a small constant to help avoid log zero and is set to 0.01. From Eq. (24), we note that two products are likely to be in the same competitive segment, if they are frequently co-commented by con sumers. A large coherence score means all pairs of products have high co-commented frequencies, which shows good performance on model results. We calculate the average coherence score $\textstyle { \frac { 1 } { K } } \sum _ { k = 1 } ^ { K } C _ { k }$ to evaluate the overall quality of segments. To test the generalizability of the pro posed model, we run the proposed model and all baselines five times, respectively. We then conduct the paired t-test to check the statistical significance between the proposed model and each baseline.

Table 2 reports the coherence scores on competitive segments when the number of representative products ranges from 5 to 20. As shown in Table 2, our model obtains the best performance compared with the other models. The improvements of the proposed model over bench marks are statistically significant at $p < 0 . 0 1$ . In Table 2, the nB-ACA achieves the second-best scores, which implies considering customers limited attention can improve performance. The improvements from nB-ACA to ACA are 8.2%, 9.4%, 8.5%, and 5.7% respectively for $T = 5 , 1 0 ,$ 15 to 20. nS-ACA significantly outperforms Link-LDA and PTM, which shows filtering out noise information in comment contents is important when segmenting the market. Link-LDA outperforms LDA and DMM models, because it infers competitive segments with the help of other auxiliary information (i.e., review contents). In addition, we note that Link-LDA performs similarly to CNTM, which demonstrates introducing contrastive learning is also an efficient way to infer competitive segments.

Table 3  
Table 2  
The coherence scores on competitive segments for T representative products.

<table><tr><td>Model</td><td>T = 5</td><td>T = 10</td><td>T = 15</td><td>T = 20</td></tr><tr><td>DMM</td><td>-23.96***</td><td>-93.20***</td><td>-229.11***</td><td>-431.76***</td></tr><tr><td>LDA</td><td>-19.40***</td><td>-88.61***</td><td>-218.42***</td><td>-405.38***</td></tr><tr><td>CNTM</td><td>-18.75**</td><td>-83.97***</td><td>-214.68**</td><td>-392.14***</td></tr><tr><td>Link-LDA</td><td>-18.47**</td><td>-84.80***</td><td>-213.64**</td><td>-390.24***</td></tr><tr><td>PTM</td><td>-17.04***</td><td>-82.58***</td><td>-196.55***</td><td>-373.90***</td></tr><tr><td>nS-ACA</td><td>-15.24***</td><td>-80.21***</td><td>-183.35**</td><td>-364.32***</td></tr><tr><td>nB-ACA</td><td>-14.86**</td><td>-73.55**</td><td>-175.89***</td><td>-337.46**</td></tr><tr><td>ACA</td><td>-13.74</td><td>-67.22</td><td>-162.17</td><td>-319.40</td></tr></table>

Note: \* for p < 0.05, \*\* for p < 0.01, \*\*\* for $p < 0 . 0 0 1$

Similarly, we calculate the average coherence scores across all topics. For each topic k and its top T representative words $V ^ { k } = ( \nu _ { 1 } ^ { ( k ) } ;$ $\nu _ { 2 } ^ { ( \bar { k } ) } , \cdots , \nu _ { T } ^ { ( k ) } )$ the coherence score can be calculated by $\begin{array} { r } { \sum _ { t = 2 } ^ { T } \sum _ { l = 1 } ^ { t - 1 } l o g \frac { D \left( \nu _ { t } ^ { ( k ) } , \nu _ { l } ^ { ( k ) } \right) + \epsilon } { D \left( \nu _ { l } ^ { ( k ) } \right) } } \end{array}$ . And $D ( \nu _ { t } ^ { ( k ) } , \nu _ { l } ^ { ( k ) } )$ denotes the number of textual contents containing both words $\nu _ { t } ^ { ( k ) }$ and $\nu \nmid ^ { ( k ) } . D ( \nu \nmid ^ { ( k ) } )$ denotes the number of textual contents with at least one token $\operatorname { o f } \nu _ { l } ^ { ( k ) } .$ . In Table 3, we can see that coherence scores of Link-LDA and PTM under different T are close. However, Link-LDA performs slightly better than LDA, which shows incorporating segment assignment may improve topic learning, even not that obvious. CNTM performs slightly better than LDA, which shows using TF-IDF strategy to select positive and negative samples is not particularly effective on textual contents. nB-ACA and nS-ACA perform better than Link-LDA and PTM. Unsurprisingly, the proposed ACA out performs all baselines $( p < 0 . 0 1 )$ , indicating our model can effectively capture the potential relationship between customer reviews. The im provements from nB-ACA to ACA are 16.9%, 6.1%, 4.7%, and 6.4% respectively, when the representative words range from 5 to 20. From Tables 2 and 3. we conclude that our model can produce better results on the inference of competitive segments and topics.

In addition, to evaluate the influence of hyperparameters on model performance, we perform sensitivity analysis in Appendix I. From the results, we observe that the proposed model has good stability in the performance of detecting competitive segments and topics.

## 4.6.2. Prediction performance

We now report on the prediction performance of each method. The proposed model attempts to jointly leverage the review contents and their associated products to conduct competitive analysis. If the model performs well, then it should well model the relationships between these two types of data. To evaluate model performance on this aspect, we aim to predict whether the given review contents will be associated with some specific products. Specifically, we apply the proposed model and baselines to predict the reviewed products for the review contents that are not observed in the training stage. For the experimental design, we first use the training splits of the users' data to learn the parameters of al models. Then, giving only the review contents from the corresponding testing splits of users' data, we perform inference to estimate the pos terior distribution of user preferences. Using the probabilities of user preferences and the model parameters inferred during the training stage, we can compute the conditional probability of each product to any users in the test set. In this experiment, we compute the conditional proba bility $p ( e | w _ { m } ^ { \mathrm { T e s t } } )$ to make the prediction:

The coherence scores on topics for T representative words.

<table><tr><td>Model</td><td>T = 5</td><td>T = 10</td><td>T = 15</td><td>T = 20</td></tr><tr><td>DMM</td><td>-29.25***</td><td>-143.20***</td><td>-345.83***</td><td>-575.43***</td></tr><tr><td>LDA</td><td>-27.57***</td><td>-137.61***</td><td>-328.97**</td><td>-556.33***</td></tr><tr><td>CNTM</td><td>-26.17***</td><td>-135.65***</td><td>-324.60***</td><td>-550.72**</td></tr><tr><td>Link-LDA</td><td>-26.18**</td><td>-135.15***</td><td>-320.52***</td><td>-549.32***</td></tr><tr><td>PTM</td><td>-26.15***</td><td>-134.28**</td><td>-321.42***</td><td>-546.73***</td></tr><tr><td>nS-ACA</td><td>-24.38**</td><td>-128.04***</td><td>-301.62***</td><td>-527.88**</td></tr><tr><td>nB-ACA</td><td>-23.50**</td><td>-122.77**</td><td>-293.65**</td><td>-514.88***</td></tr><tr><td>ACA</td><td>-20.10</td><td>-115.66</td><td>-280.02</td><td>-483.71</td></tr></table>

Note: \* for p < 0.05, \*\* for p < 0.01, \*\*\* for p < 0.001.

$$
p \left(e | \boldsymbol {w} _ {m} ^ {\text { Test }}\right) = \sum_ {k = 1} ^ {K} p (e | k) \int p (k | \theta_ {m}) d \theta_ {m} \propto \sum_ {k = 1} ^ {K} \varphi_ {k e} \mathbb {E} \left[ \theta_ {m k} | \boldsymbol {w} _ {m} ^ {\text { Test }} \right]\tag{25}
$$

where ${ \pmb w } _ { m } ^ { \mathrm { T e s t } }$ is the partial review contents of user m in the test set. Intuitively, a large value for the probability $p ( e | w _ { m } ^ { \mathrm { T e s t } } )$ implies that review contents of ${ \pmb w } _ { m } ^ { \mathrm { T e s t } }$ are more relevant to product e. $\mathbb { E } \big [ \theta _ { m k } | w _ { m } ^ { \mathrm { T e s t } } \big ]$ is used to estimate the posterior distribution of user preferences. For each of the prediction methods, it is straightforward to produce a product ranking list over each test user, using products with the highest probability p(e| $w _ { m } ^ { \mathrm { T e s t } } )$ . We measure the prediction performance of this ranking list with respect to the ground truth, which is the set of actual products reviewed by the users in the test set. From Eq. (25), we note that the model can predict well the products of interest to users in the test set, if the model can accurately estimate the competitive segments and user preferences. Since the DMM model and LDA cannot model the reviewed products and the review texts simultaneously, we thus ignore these models. We select two popular metrics Precision @ N and Recall @ N to evaluate the per formance. High values of Precision @ N and Recall @ N indicate betterpredicted results obtained by the methods. In our experiment, we chronologically split the data into two sets. The first 90% of the reviewed products are used as a training set; the testing set comprises the last 10% of the reviewed products.

Fig. 8 gives the average Precision @ N and Recall @ N for each method. We find that the four baseline methods perform worse than the ACA model on precision and recall metrics, indicating our model is better at extracting competitive knowledge and user preference. From Fig. 8 (a) and (b), we find that nB-ACA and nS-ACA consistently outperform Link-LDA and PTM, consistent with the previous findings in Section 4.6.1. Compared with the second-best performing nB-ACA, our model has a gain of 5.7%, 9.0% and 11.2% on the precision metric over different sizes of ranked products. On recall metric, our model is better than nB-ACA by 4.8%. 4.4% and 6.1% over different sizes of ranked products.

## 4.7. Managerial implications

This paper contributes to providing an interpretable framework for competitive intelligence by using online reviews. Our results provide several important managerial implications.

First, our results enable managers to observe how products compete in the marketplace, so as to appraise their direct competitors and obtain cues about tracking indirect rivals. The proposed framework applies the reviewed products related to online reviews to uncover a set of competitive segments. For managers of a specific product, they can easily retrieve the direct or primary competitors from the competitive segments. For example, from Fig. 4, managers of Ford\_F150 can find its direct competitors in segment 2 and 33. In addition, based on the competitive segments, managers can easily construct the marketstructure perceptual maps, similar to previous studies [4,8]. Then, they can determine the indirect competitors via the network rules in the market structure [56]

Second, our results enable managers to ascertain competitive di mensions perceived by customers, so as to assess the competitive ad vantages and disadvantages of their products. The proposed framework uses the review contents to capture customers' cognition about compe tition. From the results in Section 4.4, we find that our framework ex tracts suitable words to present the competitive aspects. These competitive aspects indicate the customers' experience of specific product features. In Appendix G we also explore the consumers' senti ments about detailed aspects of products. Based on our results, managers can easily analyze consumers' overall attitude toward specific product features, and then assess the competitive advantages and disadvantages of their products.

![](/api/attachments/CTJZ48FZ/fulltext/images/9c3f5b46d30d78283d8449a043abe11ba43f0d2592d20296a9514dd2c83d4232.jpg)  
(a)

![](/api/attachments/CTJZ48FZ/fulltext/images/555d0aba8b5ae363573274ff8c1f8d1208cd26a275a3ec8a21e2d3a4854dc690.jpg)  
(b)  
Fig. 8. Prediction Performance on Precision@N and Recall@N Metrics.

Third, our results enable managers to capture individual customer preferences, so as to develop marketing strategies. For example, man agers can use individual preferences to group their customers and then provide personalized promotions based on available profile information to maximize firm's revenue. In addition, online platforms can apply in dividual preferences to identify consumer needs and optimize their search engine.

## 5. Conclusion and future work

The ability to uncover competitive information is a critical success factor necessary for operational and marketing efficiency. Recently, the rich data created by online customers provides an unprecedented op portunity for managers to not only identify competitors but also un derstand customers' cognition about competition. This paper proposes an aspect-level competitive attribution model to build competitive in telligence. Different from the firm perspective that regards product with similar features as competitors, the proposed ACA model detects the competition intelligence from customer perspective. Based on user generated reviews, our method jointly identifies competitive segments in the market and extracts the competitive dimensions among these competitors in each segment. By introducing limited attention to investigate customer behaviors, the proposed ACA model can capture customers' preferences as well as their choices more precisely. In empirical studies, we demonstrate the value of the proposed model. We find that the ACA model can accurately infer high-quality competitive segments and interpretable competition-related aspects corresponding to these segments. It is also an easy way to estimate customer prefer ences in a competitive environment.

There are several potential directions for further research. First, one can integrate the reviewed products with these products' attributes such as price to further improve the learning of the competitive segments. Second, future studies can model the one-to-many relationship between the competitive segment and competition-related topic, which can be used to acknowledge the fact that customers often discuss multiple dimensions associated with products in one segment. Finally, one can investigate the evolution of product competition. We hope that this research serves as a modest catalyst toward these future research directions.

## CRediT authorship contribution statement

Yang Qian: Idea, Experiment, Writing the manuscript. Yuanchun Jiang: Idea, Writing the manuscript. Jennifer Shang: Idea, Final proofreading. Yidong Chai: Experiment, Result analysis; Yezheng Liu: Design of the study, Final proofreading.

## Declaration of Competing Interest

The authors declare the following financial interests/personal re lationships which may be considered as potential competing interests: Yang Qian, Yuanchun Jiang, and Yezheng Liu reports financial support was provided by National Natural Science Foundation of China. Yang Qian reports financial support was provided by Fundamental Research Funds for the Central Universities.

## Data availability

Data will be made available on request.

## Acknowledgment

We appreciate the constructive comments from the anonymous re viewers. This work is supported by the National Natural Science Foun dation of China (72101072, 72171071, 72271084, 72101079), the Fundamental Research Funds for the Central Universities (JZ2022HGTB0282), and the National Engineering Laboratory for Big Data Distribution and Exchange Technologies.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi. org/10.1016/j.dss.2023.113956.

## References

[1] H. Rhim, L.G. Cooper, Assessing potential threats to incumbent brands: new product positioning under price competition in a multisegmented market, Int. J. Res, Mark, 22 (2) (2005) 159–182

[2] F.A. Gur, T. Greckhamer, Know thy enemy: a review and agenda for research on competitor identification, J. Manag, 45 (5) (2019) 2072–2100.

[3] D.M. Ringel, B. Skiera, Visualizing asymmetric competition among more than 1.000 products using big search data, Mark, Sci. 35 (3) (2016) 511–534.

[4] Y. Liu, et al., Using favorite data to analvze asymmetric competition: machine learning models, Eur. J. Oper. Res. 287 (2) (2020) 600–615.

[5] A. Griffin, J.R. Hauser, The voice of the customer, Mark. Sci. 12 (1) (1993) 1–27.

## Y. Qian et al.

[6] A. Timoshenko, J.R. Hauser, Identifying customer needs from user-generated content, Mark. Sci. 38 (1) (2019) 1–20.

[7] M. Zuo, et al., Dynamic competition identification through consumers’ clickstream data, in: Academy of Management Proceedings 10510, Academy of Management Briarcliff Manor, NY, 2020, p. 19916.

[8] O. Netzer, et al., Mine your own business: market-structure surveillance through text mining, Mark. Sci. 31 (3) (2012) 521–543.

[9] R.F. Haans, What’s the value of being different when everyone is? The effects of distinctiveness on performance in homogeneous versus heterogeneous categories, Strateg. Manag. J. 40 (1) (2019) 3–27.

[10] W. Wang, Y. Feng, W. Dai, Topic analysis of online reviews for two competitive products using latent Dirichlet allocation, Electron. Commer. Res. Appl. 29 (2018) 142–156.

[11] P. Nedungadi, Recall and consumer consideration sets: influencing choice without altering brand evaluations, J. Consum. Res. 17 (3) (1990) 263–276.

[12] T. Van Nguyen, et al., Predicting customer demand for remanufactured products: a data-mining approach, Eur. J. Oper. Res. 281 (3) (2020) 543–558.

[13] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, J. Mach. Learn. Res. 3 (Jan) (2003) 993–1022.

[14] J.G. Lynch Jr., T.K. Srull, Memory and attentional factors in consumer choice: concepts and research methods, J. Consum. Res. 9 (1) (1982) 18–37.

[15] R.A. Rensink, J.K. O’Regan, J.J. Clark, To see or not to see: the need for attention to perceive changes in scenes, Psychol. Sci. 8 (5) (1997) 368–373.

[16] C. Townsend, B.E. Kahn, The “visual preference heuristic”: the influence of visual versus verbal depiction on assortment processing, perceived variety, and choic overload, J. Consum. Res. 40 (5) (2014) 993–1015.

[17] H. Ishwaran, J.S. Rao, Spike and slab variable selection: frequentist and Bayesian strategies, Ann. Stat. 33 (2) (2005) 730–773.

[18] T. Lin, et al., The dual-sparse topic model: mining focused topics and focused terms in short text, in: Proceedings of the 23rd international conference on World wide web, ACM, 2014, pp. 539–550.

[19] K. Xu, et al., Mining comparative opinions from customer reviews for competitive intelligence, Decis. Support. Syst. 50 (4) (2011) 743–754.

[20] Y. Liu, C. Jiang, H. Zhao, Assessing product competitive advantages from the perspective of customers by mining user-generated content on social media, Decis. Support. Syst. 123 (2019), 113079.

[21] L. Zheng, Z. He, S. He, A novel probabilistic graphic model to detect product defects from social media data, Decis. Support. Syst. 137 (2020), 113369.

[22] P.S. Dhillon, S. Aral, Modeling dynamic user interests: a neural matrix factorization approach, Mark. Sci. 40 (6) (2021) 1059–1080.

[23] B.J. Jacobs, B. Donkers, D. Fok, Model-based purchase predictions for large assortments, Mark, Sci, 35 (3) (2016) 389–404.

[24] M.-J. Chen. Competitor analysis and interfirm rivalry: toward a theoretical integration, Acad, Manag, Rey, 21 (1) (1996) 100–134.

[26] C.F. Mela, S. Gupta, K. Jedidi, Assessing long-term promotional influences on

[28] S.A. Zahra, S.S. Chaples, Blind spots in competitive analysis, Acad. Manag. Perspect. 7 (2) (1993) 7–28.

[29] H. Nam, Y.V. Joshi, P. Kannan, Harvesting brand information from social tags, J. Mark, 81 (4) (2017) 88–108

[30] L. Wang, et al., Identifving comparable entities with indirectly associative relations and word embeddings from web search logs, Decis. Support. Syst. 141 (2021), 113465.

[31] M. Hu, B. Liu, Mining opinion features in customer reviews, in: AAAI, 2004, pp. 755–760.

[32] K.D. Varathan, A. Giachanou, F. Crestani, Comparative opinion mining: a review J. Assoc. Inf. Sci. Technol. 68 (4) (2017) 811–829.

[33] R.Y.K. Lau, W. Zhang, W. Xu, Parallel aspect-oriented sentiment analysis for sales forecasting with big data, Prod. Oper. Manag. 27 (10) (2018) 1775–1794.

[34] S. Mukhopadhyay, et al., Impact of review narrativity on sales in a competitive environment, Prod. Oper. Manag. 31 (6) (2022) 2538–2556.

[35] A.S. Abrahams, et al., An integrated text analytic framework for product defect discovery, Prod. Oper. Manag. 24 (6) (2015) 975–990.

[36] Y. Li, Y. Xie, Is a picture worth a thousand words? An empirical study of image content and social media engagement, J. Mark. Res. 57 (1) (2020) 1–19.

[37] T.R. Hannigan, et al., Topic modeling in management research: rendering new

[38] L. Ma, B. Sun, Machine learning and AI in marketing–connecting computing power to human insights. Int. J. Res. Mark, 37 (3) (2020) 481–504.

[39] N. Ilk, G. Shang, P. Goes, Improving customer routing in contact centers: an automated triage design based on text analytics, J. Oper. Manag. 66 (5) (2020)

[40] S. Xiao, Y.C. Ho, H. Che, Building the momentum: information disclosure and herding in online crowdfunding, Prod. Oper, Manag, 30 (9) (2021) 3213–3230.

[41] J.V. Graça, et al., Posterior vs. parameter sparsity in latent variable models, in: Proceedings of the 22nd International Conference on Neural Information Processing Systems, 2009, pp. 664–672.

[42] J.H. Roberts, J.M. Lattin, Development and testing of a model of consideration set composition, J. Mark, Res, 28 (4) (1991) 429–440

[43] A.C.M. Leung, et al., Network analysis of search dynamics: the case of stock habitats, Manag. Sci. 63 (8) (2017) 2667–2687.

[44] J. Liu, O. Toubia, A semantic approach for estimating consumer content preferences from online search queries, Mark, Sci. 37 (6) (2018) 930–952

[45] T.J. Mitchell, J.J. Beauchamp, Bayesian variable selection in linear regression, J. Am. Stat. Assoc. 83 (404) (1988) 1023–1032

[46] C. Wang, D. Blei, Decoupling sparsity and smoothness in the discrete hierarchical dirichlet process, Adv. Neural Inf. Proces. Syst. 22 (2009) 1982–1989.

[47] T.L. Griffiths, M. Steyvers, Finding scientific topics, Proc. Natl. Acad. Sci. 10 (Suppl. 1) (2004) 5228–5235.

[48] V. Rakesh, et al., A sparse topic model for extracting aspect-specific summaries from online reviews, in: Proceedings of the 2018 World Wide Web Conference on World Wide Web, International World Wide Web Conferences Steering Committee 2018. pp. 1573–1582

[49] K. Nigam, et al., Text classification from labeled and unlabeled documents using EM, Mach. Learn. 39 (2) (2000) 103–134.

[50] T. Nguyen, A.T. Luu, Contrastive learning for neural topic model, Adv. Neural Inf. Proces. Syst. 34 (2021) 11974–11986

[51] E. Erosheva, S. Fienberg, J. Lafferty, Mixed-membership models of scientific publications, Proc. Natl. Acad. Sci. 101 (Suppl. 1) (2004) 5220–5227.

[52] L. Yao, et al., A topic modeling approach for traditional Chinese medicine prescriptions, IEEE Trans. Knowl. Data Eng. 30 (6) (2018) 1007–1021.

[53] D. Mimno, et al., Optimizing semantic coherence in topic models, in: Proceedings of the 2011 Conference on Empirical Methods in Natural Language Processing, 2011, pp. 262–272.

[54] S.I. Nikolenko, Topic quality metrics based on distributed word representations, in: Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval, 2016, pp. 1029–1032.

[55] K. Stevens, et al., Exploring topic coherence over many models and many topics, in: Proceedings of the 2012 Joint Conference on Empirical Methods in Natura Language Processing and Computational Natural Language Learning, 2012, pp. 952–961.

[56] P.F. Skilton, E. Bernardes, Competition network structure and product market entry, Strateg. Manag. J. 36 (11) (2015) 1688–1696.

Yang Qian is an assistant professor at the School of Management, Hefei University of Technology. He received his Ph.D. in Management Science and Engineering from Hefei University of Technology in 2020, His research interests include electronic commerce. online marketing, and machine learning. His work has appeared in journals including European Journal of Operational Research, Decision Support Systems, ACM Transactions on Knowledge Discovery from Data, and Information Processing & Management.

Yuanchun Jiang is a professor at School of Management, Hefei University of Technology, China. He received his Ph.D. in Management Science and Engineering from Hefei Uni versity of Technology, Hefei, China. He teaches electronic commerce, business intelligence and business research methods. His research interests include online marketing, electronic commerce and data mining. He has published papers in journals such as Marketing Science, European Journal of Operational Research, Decision Support Systems, and IEEE Transactions on Dependable and Secure Computing.

Jennifer Shang is a Professor and the Area Director of Business Analytics and Operations at the University of Pittsburgh, Pitt Business. Her research focuses on operations man agement, e-commerce and healthcare analytics. She has published >130 papers, and her research appears in journals such as Management Science, Manufacturing & Service Opera tions Management, Production and Operations Management, Information Systems Research, and Marketing Science.

Yidong Chai is a professor at the School of Management at the Hefei University of Technology. He received his Ph.D. degree from the Department of Management Science and Engineering of Tsinghua University. His research centers around machine learning for business intelligence, health informatics, and cyber threat intelligence. His work has appeared in journals including MIS Quarterly, Journal of Management Information Systems, IEEE Transactions on Dependable and Secure Computing and Information Processing and Management.

Yezheng Liu is a professor of Electronic Commerce at Hefei University of Technology, China. He received his Ph.D. in Management Science and Engineering from Hefei Uni versity of Technology in 2001. His main research interests include decision science, electronic commerce, intelligent decision support systems and data mining. His work has appeared in journals including Marketing Science, IEEE Transaction on Software Engineering, Information Sciences, and ACM Transactions on Information Systems.
