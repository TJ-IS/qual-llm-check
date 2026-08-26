---
otero_id: 21129
otero_key: "5KSY3MSS"
title: "Mining customer product ratings for personalized marketing"
authors: "Kwok-Wai Cheung; James T. Kwok; Martin H. Law; Kwok-Ching Tsui"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00108-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mining customer product ratings for personalized marketing

Kwok-Wai Cheung <sup>a,</sup>\*, James T. Kwok <sup>b</sup>, Martin H. Law <sup>b</sup>, Kwok-Ching Tsui <sup>a</sup>

<sup>a</sup>Department of Computer Science, Hong Kong Baptist University, Kowloon Tong, Hong Kong, China

<sup>b</sup>Department of Computer Science, Hong Kong University of Science and Technology, Clear Water Bay, Hong Kong, China

## Abstract

With the increasing popularity of Internet commerce, a wealth of information about the customers can now be readily acquired on-line. An important example is the customers’ preference ratings for the various products offered by the company. Successful mining of these ratings can thus allow the company’s direct marketing campaigns to provide automatic product recommendations. In general, these recommender systems are based on two complementary techniques. Content-based systems match customer interests with information about the products, while collaborative systems utilize preference ratings from the other customers. In this paper, we address some issues faced by these systems, and study how recent machine learning algorithms, namely the support vector machine and the latent class model, can be used to alleviate these problems. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Recommender systems; Personalized marketing; Support vector machine; Latent class model

## 1. Introduction

Direct marketing is a promotion process which motivates customers to place orders through various channels [33]. A conventional example is direct mail, which sends out appealing customized catalogs or coupons to targeted customers. In order for this to work, one needs to have an accurate customer segmentation based on a good understanding of the customers, so that relevant product information can be delivered to different customer segments. Moreover, the costs involved in the related marketing research have to be carefully controlled. With the recent advances in the World Wide Web and the booming e-business, on-line companies can now acquire individual customer’s information via the Internet in real-time and at a much lower cost. Based on these acquired information, detailed customer profiles can be built to support one-to-one marketing and other personalized services (personalization). The effectiveness of direct marketing in cyberspace can thus be greatly improved.

Another consequence of moving the storefront to the cyberspace is that a tremendous amount of product information can now be made available to the customers at a very low cost. However, customers, who were used to having only a limited range of product choices due to physical and/or time constraints, are now facing the problem of information overload. An effective way to increase customer satisfaction and consequently customer loyalty should be one that helps the customers identify products according to their interests. This, again, calls for the provision of personalized product recommendations.

Nowadays, recommender systems have been implemented by many big Web retailers, such as Amazon.com and CDNow.com. Typically, they use an intelligent engine to mine the customer’s ratings records and then create predictive user models for product recommendation. These customer ratings may either be acquired explicitly by form-filling or implicitly via an intelligent agent [12]. Purchase records can also be good indicators of customer preferences. Moreover, software products for recommender systems are also available, such as NetPerceptions’ Personalization engine, Andromedia’s LikeMind and Manna’s FrontMind. All these can be integrated directly into a company’s Web server to provide personalized product recommendations.

Based on the underlying technology, recommender systems can be broadly categorized as content-based and collaborative. Content-based systems provide recommendations to a customer by automatically matching his/her interests with product contents, and have been reported in the literature on recommending webpages [41], newsgroup messages [31] and news items [9]. Notice that recommendations are made without relying on information provided by the other customers. Moreover, for certain products such as movies as will be discussed in Section 4, content information (such as the cast of a certain movie) can now be readily extracted from the Web. While extracting product contents may be straightforward, the resultant set of product attributes can be too large to handle. Existing systems rely heavily on preprocessing steps that select a manageable set of ‘‘important’’ features from these attributes. These, however, are often ad hoc and do not always show consistent improvement (The Feature Selection Problem).

Collaborative systems, on the other hand, provide recommendations by utilizing overlap of preference ratings to combine the opinions of ‘‘like-minded’’ customers. Using this word-of-mouth approach, customers may now be able to receive recommendations for products that are dissimilar in content to those he/ she has previously rated, as long as other like-minded customers prefer them. The concept of collaboration was first used by Goldberg et al. [19] for filtering emails, and then quickly pursued for product recommendation [43,45]. Most pioneering collaborative systems are based on the use of correlation coefficients, which, however, are known to be sensitive to the sparsity of preference ratings (The Sparsity Problem) and also problematic when new products are introduced (The First-Rater Problem) [28].

In this paper, we propose the use of the support vector machine (SVM) [8,48] and the latent class model (LCM) [22] to circumvent some of the aforementioned problems. Unlike other learning methods, SVM’s performance is related not to the number of features in the system, but to the margin with which it separates the data. Experimentally, SVM has achieved superior performance on a number of high-dimensional data sets. The LCM is a statistical mixture model which assumes that the observed data come from a set of hidden causes [34]. It has recently been applied to document categorization [18] and texture segmentation [23]. Here, the use of the LCM allows some ‘‘latent’’ clusters of preference ratings to be formed so that the sparse ratings distribution can effectively be smoothed out.

While the techniques discussed in this paper are generally applicable to any recommender system, for performance evaluation purposes, we consider here a specific recommendation task, namely, movie recommendation. This task has been popularly used as a testbed for recommender algorithms [3,5 – 7,11,20– 22], and a number of commercial websites (such as http://movies.eonline.com and http://reel.com) are providing such service. Moreover, to be more specific, we will use the Internet Movie Database (IMDb) for movie contents and the EachMovie database for movie ratings. These two databases exemplify the typical problems faced by recommender systems mentioned above. For example, as will be detailed in Section 4.1.1, the number of features extracted from the IMDb is very large (equal to 6620). As for the EachMovie database, there are a total of 1628 movies and 72,916 users. The number of possible movie– user pairs is thus $1 6 2 8 \times 7 2 9 1 6 = 1 . 1 8 7 \times 1 0 ^ { 8 }$ . The number of movie ratings actually present, however, is 2,811,983, which is equivalent to a data density of merely 2.4%.

The rest of this paper is organized as follows. Section 2 describes content-based recommender systems, with particular emphasis on the feature selection problem, and then an introduction to the SVM. Section 3 describes collaborative recommender systems, together with the sparsity and first-rater problems, and then an introduction to the LCM and our extension. Evaluation results on the SVM and the extended LCM are presented in Section 4, and the last section gives some concluding remarks.

## 2. Content-based recommendation

In content-based systems, products are described by a common set of attributes extracted from the available product descriptions. Customer’s preferences are then predicted by analyzing the relationship between the product ratings that a particular individual has given and the corresponding product attributes. A number of techniques have been used. A rudimentary method is by simple keyword matching [10]. However, the use of keywords suffers from the well-known problems of synonymy and polysemy in information retrieval [14]. Moreover, customer preferences are often too complex to be adequately captured by a set of keywords. Another popular technique that is capable of producing accurate recommendations is the naive Bayes classifier [36]. This, however, relies on the simple and often unrealistic assumption that product attributes are probabilistically independent of one another. Other algorithms, such as rule-based systems [5] and the winnow algorithm [40], have also been used.

## 2.1. The problem of feature selection

A central problem in content-based recommender systems is the need to identify a sufficiently large set of key attributes. When the set is too small, obviously there will be insufficient information to learn the customer profile. However, having too many attributes can also be problematic, as this results in a large number of trainable parameters in the model and consequently poor performance [35]. This is further aggravated by the usual feature representation scheme of using a set of binary features to represent multi-valued attributes. For example, the attribute Cast that describes the cast of a movie is typically represented by a set of binary features such as ‘‘Cast includes Dustin Hoffman’’, ‘‘Cast includes Bruce Willis’’, ‘‘Cast includes Leonardo DiCaprio’’, etc. Because of the large number of possible actors and actresses, the resultant set of features can be very sizable,<sup>1</sup> and it is therefore not surprising that a straightforward application of the approach may yield inferior performance [5].

To circumvent this problem, existing techniques thus rely heavily on manual/automatic preprocessing steps that select ‘‘useful’’ features [13]. However, the effectiveness of feature selection is quite controversial. Many of the selected features contain redundant information. Moreover, a feature that appears to be a poor predictor on its own may turn out to have great discriminative power in combination with others. Besides, another important question that has not been addressed thoroughly is how many features should be selected. In practice, this has to be chosen based on the individual’s experience.

Some machine learning algorithms, such as decision trees, have built-in methods of selecting features while generating the target concept, and may thus appear immune to the above controversy. However, Refs. [2,32] have shown that these learning algorithms are not effective at minimizing the number of features in the face of many irrelevant features, as may exist in content-based recommendation.

The issue of dimension reduction has also been studied widely in statistics and pattern recognition. All the methods mentioned above fall under the so-called filter model [26], in which they are performed as a preprocessing step. John et al. [26] proposed a wrapper model which uses a learning algorithm, together with cross-validation, as an alternative evaluating function in choosing the required features. However, this model can become very computationally expensive when there are a lot of candidate features.

## 2.2. Support vector machine

SVM has performed very well in a number of high-dimensional data sets even without feature selection. For example, it outperforms radial basis networks on recognizing the US postal service database of handwritten digits (using 16  16 bitmap as input) [44]. Promising results are also reported in face detection [39] (where the input dimensionality is 283) and text categorization [17,24,29] (where the input dimensionality is over 10,000). Its power stems from automatic regularization and also framing the computational problem as a quadratic programming problem. In this section, we briefly review SVMs for classification. Interested readers may refer to Refs. [8,48] for details.

## 2.2.1. Learning the SVM model

Assume that the customer has provided preference ratings for m products. To learn the SVM, we are given a training set containing tuples of the form $\{ ( \mathbf { f } _ { j } , \nu _ { j } ) \} _ { j = 1 } ^ { m }$ , with $\mathbf { f } _ { j }$ (as input) being product j’s feature vector and $\nu _ { j }$ (as output) being the corresponding preference rating. Here, the preference rating can either be $+ 1$ (indicating that the user likes this product) or - 1 (indicating that the user does not like this product). Thus, in the context of pattern recognition, we have a binary classification problem, and the task is to separate products that the customer likes from those that he/she dislikes.

First consider the simpler case when the data is linearly separable, i.e., the two classes of products in the above binary classification problem can be perfectly separated by a linear surface. The SVM constructs a hyperplane<sup>2</sup> $\mathbf { w } ^ { \mathrm { T } } \mathbf { f } + b$ for which the separation between the two classes is maximized (Fig. 1). Mathematically, this is equivalent to minimizing w and it can be shown that $\begin{array} { r } { \mathbf { w } { = } \sum _ { j = 1 } ^ { m } \alpha _ { j } \nu _ { j } \mathbf { f } _ { j } , } \end{array}$ , where ${ \pmb { \alpha } } \mathrm { = } \left( \alpha _ { 1 } , . . . , \alpha _ { m } \right) ^ { \mathrm { T } }$ can be found by solving the following quadratic programming (QP) problem

$$
\max W (\boldsymbol {\alpha}) = \boldsymbol {\alpha} ^ {T} \mathbf {1} - \frac {1}{2} \boldsymbol {\alpha} ^ {T} \mathbf {Q} \boldsymbol {\alpha},\tag{1}
$$

under the constraints $\mathbf { \alpha } _ { \mathbf { { \alpha } } \mathbf { { \alpha } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \alpha } } \mathbf { { \mathbf { { \alpha } } } } \mathbf { { \alpha } } \mathbf { { \alpha } } \mathbf { { \alpha } }  \mathbf { { \alpha } } \mathbf { { \alpha } } \mathbf { { \alpha } } \mathbf { { \alpha } } \mathbf { { \alpha } } $ and $\begin{array} { r } { \mathbf { \alpha } \mathbf { { \stackrel { { T } } { v } } } = 0 . } \end{array}$ , where $\mathbf { 1 } \ b { = } ( 1 , 1 , . . . , 1 ) ^ { \mathrm { T } } , \mathbf { v } \ b { = } ( \nu _ { 1 } , . . . , \nu _ { m } ) ^ { \mathrm { T } }$ and Q is a $m \times m$ symmetric matrix with entries $\nu _ { j } \nu _ { k } \mathbf { f } _ { j } ^ { \mathrm { T } } \mathbf { f } _ { k }$ . Notice that $\mathbf { Q }$ is always positive semi-definite and so there is no local optima for the QP problem. For those $\boldsymbol { \alpha _ { j } } ^ { \prime } \mathbf { s }$ greater than zero, it can be shown that the corresponding training examples must lie along the margins of the decision boundary, and these are called the support vectors.

When the training set is not linearly separable, the SVM algorithm accommodates the discrepancies by introducing non-negative slack variables $\boldsymbol { \zeta } _ { j } ^ { \mathrm { ~ , ~ } } { \bf s }$ that (whenever nonzero) measure the difference between $\nu _ { j }$ and the corresponding SVM output $a _ { j } = \mathbf { w } ^ { \mathrm { T } } \mathbf { f } _ { j } + b$ Then, instead of minimizing <sub>O</sub>w<sub>O</sub> in the separable case, the problem now becomes

![](/api/attachments/5KSY3MSS/fulltext/images/7327aab62330153fd491cb159401da85f70f8787df5fc20a23c0205bd0d5a33d.jpg)  
Fig. 1. In this figure, patterns belonging to the two classes are denoted by $\bigcirc$ and $\times ,$ respectively, and the double arrow denotes the margin that is to be maximized by the SVM algorithm. The resultant support vectors are shown in boldface.

$$
\min \frac {1}{2} \| \mathbf {w} \| ^ {2} + C \sum_ {j = 1} ^ {m} \xi_ {j},
$$

subject to $\nu _ { j } a _ { j } \geq 1 - \xi _ { j }$ and $\xi _ { j } \ge 0$ , for $j = 1 , . . . , m$ where C is a user-defined regularization parameter. Again, this minimization problem can be transformed to a QP problem, as: maximize Eq. (1) subject to the constraints $C \mathbf { 1 } \geq \mathbf { \alpha } \geq \mathbf { 0 }$ and $\mathbf { \Delta x } ^ { \mathrm { { T } } } \mathbf { v } = 0$

So far, we have only considered separating the two classes of products by a hyperplane. It is often more effective to perform the separation by nonlinear hyper-surfaces, say by a polynomial surface of degree 4. In SVM, this is achieved by nonlinearly mapping the original product feature vectors to another space $\mathcal { F }$ via a mapping $\mathbf { u } = \phi ( \mathbf { f } )$ , and then apply the same hyperplane algorithm in ${ \mathcal F } .$ The only change in the computation is that entries of Q now become $\nu _ { j } \nu _ { k } \mathbf { u } _ { j } ^ { \mathrm { { T } } } \mathbf { u } _ { k } .$ In general, it can be cumbersome to explicitly compute $\mathbf { u } _ { j } , \ \mathbf { u } _ { k }$ and then the dot product. For example, to construct a polynomial of degree 4 in a 200-dimensional space, $\mathbf { u } _ { j }$ will have dimensionality of over a billion. However, instead, it can be shown that the computation can be made much more efficient by using a kernel function $K ( \cdot , \cdot )$ such that $K ( \mathbf { f } _ { j } , \mathbf { f } _ { k } ) = \mathbf { u } _ { j } ^ { \mathrm { { T } } } \mathbf { u } _ { k }$ . For example, the kernel for a polynomial classifier of degree d is $K ( \mathbf { f } _ { j } , \mathbf { f } _ { k } ) { = } ( \mathbf { f } _ { j } ^ { \mathrm { { T } } } \mathbf { f } _ { k } + 1 ) ^ { d } .$ Discussions on more kernels can be found in Ref. [48].

## 2.2.2. Making recommendations

Once the SVM model for a particular customer has been learned, one can then determine whether to recommend another product (with feature vector f) to this customer. This is done by using $\mathbf { w } ^ { \mathrm { T } } \mathbf { f } + \mathbf { b }$ as an estimate of the customer’s preference. The larger its value, the more preferable is the product. More sophisticated techniques, based on a Bayesian analysis of SVM [30], may also be used.

## 3. Collaborative recommendation

In the following, let Y be the whole set of products, $y _ { \mathrm { h } } \subset \mathcal { V }$ be the subset that have been rated by customer x and $\mathcal { V } _ { \mathrm { r } } { = } \mathcal { V } \setminus \mathcal { V } _ { \mathrm { h } }$ be the subset that have not been rated by the same customer. Collaborative systems estimate customer $x ^ { \prime } \mathbf { s }$ preferences for products in Y based on the overlap between his/her preference ratings for products in ${ \mathcal { V } } _ { \mathrm { h } }$ and those of the other customers. According to Breese et al. [7], collaborative systems can be categorized as memory-based and model-based. The memory-based approach computes the proximities of ratings between the targeted customer and each of the others in the entire database, and then estimates the preferences of the targeted customer for the unrated products accordingly. Different proximity estimates have been proposed, with the Pearson correlation coefficient being the most common [43,45]. Model-based systems, on the other hand, use the preference ratings in the database to learn a model and then use this model in estimation. Different statistical models, including a variety of clustering models [22,47] and the Bayesian network [7], have been used.

Memory-based methods were proposed much earlier and are known to suffer from two problems, namely the sparsity and the first-rater problems. Model-based methods were recently proposed mainly for alleviating the sparsity problem to achieve higher recommendation accuracy.

## 3.1. The sparsity and first-rater problems

Collaborative recommender systems assume the presence of a large enough number of customers willing to provide preference ratings to many products. However, this may not be the case in reality. In fact, as most of the pioneering collaborative systems are based on the use of correlation coefficients (memory-based) and the effectiveness of the coefficients relies heavily on the degree of overlapping among the customer ratings, accuracy of the predicted ratings degrades significantly when the available ratings are sparse (sparsity problem). To alleviate this limitation, Konstan et al. [28] enhanced their Usenet news recommender system by partitioning the ratings and the user correlations databases based on the Usenet newsgroup hierarchy. Having demonstrated that grouping ratings information is an effective remedy, different clustering and related model-based techniques have then been applied to collaborative recommendation with promising results [22,27,47]. Besides being capable of providing more accurate predictions, the trained models also possess important information for market analysis. For example, product and customer segments may be derived from the clustering structure.

An extreme form of the sparsity problem is the first-rater problem, which arises when a new product is introduced into the market and thus has no previous ratings information available either for computing the correlations (in memory-based approaches) or training the models (model-based approaches). Although it is common practice for a lot of companies to deliver all the new product information to all their customers indiscriminately, some form of customization will still be preferred if the list of new products is long and/or the new products fall into many different categories (e.g., books, CDs, etc.). In this respect, the content-based approach should be able to play an important complementary role. For example, the Fab system [4] is one of the pioneering works along the direction of integrating the two recommendation techniques for solving the first-rater problem. However, in this paper, we emphasize on the use of the LCM and so the integration issue will not be addressed.

## 3.2. Latent class model

The LCM is a model-based approach. It assumes that preference ratings of the customers come from a pre-defined number of ‘‘latent’’ classes $\mathcal { Z } { = } \{ z _ { 1 } , . . . , z _ { \mathrm { K } } \}$ Each latent class thus corresponds to the preference pattern of a group of like-minded customers. In the following, let $( x , y )$ be the observation that customer x has evaluated product $y \in \mathcal { V } ,$ and $n ( x , y )$ be the corresponding preference rating.<sup>3</sup> The joint probability distribution of x and y can be expressed as:

$$
P (x, y) = \sum_ {z \in \mathcal {Z}} P (z) P (x \mid z) P (y \mid z),
$$

where $P ( x | z )$ and $P ( y | z )$ are the class-conditional multinomial distributions and $P ( z )$ is the class prior probability. The dependency relationships among the three random variables are shown in Fig. 2. Conditional independence of x and y given z implies that once the preference pattern z of a targeted customer is known, the products to be recommended are basically independent of the targeted customer.<sup>4</sup>

## 3.2.1. Dependency diagram of the LCM

To learn the LCM, we use a training set containing the preference ratings $n ( x , y )$ of a set of customers on the products in Y. Parameters in the distributions $P ( z ) ,$ $P ( x | z )$ and $P ( y | z )$ of the LCM are then estimated by the expectation maximization (EM) algorithm [15], which is an efficient optimization algorithm for maximum-likelihood estimation with missing information. In the LCM, the missing information is which latent classes the customers and products belong to. The EM algorithm involves two steps: the E-step and the Mstep. The E-step computes the expected values of the missing information based on the current model estimate

$$
P (z \mid x, y) = \frac {P (z) P (x \mid z) P (y \mid z)}{\sum_ {z ^ {\prime}} P (z ^ {\prime}) P (x \mid z ^ {\prime}) P (y \mid z ^ {\prime})},
$$

while the M-step computes the maximum-likelihood model estimates given the expected values of the

![](/api/attachments/5KSY3MSS/fulltext/images/5502976ec8004a91a6425597bf01e6a2ed8b340d02c968dc4b36012aad7e03bf.jpg)  
Fig. 2. Dependency diagram of the LCM.

missing information:

$$
P (z) = \frac {\sum_ {x , y ^ {\prime}} n (x , y ^ {\prime}) P (z \mid x , y ^ {\prime})}{\sum_ {x , y , z ^ {\prime}} n (x , y ^ {\prime}) P (z \mid x , y ^ {\prime})},
$$

$$
P (y \mid z) = \frac {\sum_ {x ^ {\prime}} n (x , y) P (z \mid x , y)}{\sum_ {x ^ {\prime} y ^ {\prime}} n (x , y ^ {\prime}) P (z \mid x , y ^ {\prime})},
$$

$$
P (x \mid z) = \frac {\sum_ {y ^ {\prime}} n (x , y ^ {\prime}) P (z \mid x , y ^ {\prime})}{\sum_ {x ^ {\prime} y ^ {\prime}} n (x ^ {\prime} y ^ {\prime}) P (z \mid x ^ {\prime} y ^ {\prime})}.
$$

The E-step and M-step are then iterated until convergence.

## 3.2.2. Recommendation within the training set

Using the Bayes rule, the probability that customer x buys product y is

$$
P (y \mid x) = \sum_ {z \in \mathcal {Z}} P (z \mid x) P (y \mid z),\tag{2}
$$

where $P ( z \mid x ) = P ( x \mid z ) P ( z ) / \sum _ { z ^ { \prime } \in { \mathcal { Z } } } P ( x \mid z ) P ( z )$ With a number of products, they can then be sorted by $P ( y | x )$ when providing recommendations.

## 3.2.3. Recommendation outside the training set

Hofmann and Puzicha [22] did not discuss on how the LCM can be used to provide recommendations to customers whose ratings have not been used to train the LCM. Here, we propose a method by using preference ratings that the customer has rated so far. Let $x _ { n } \notin \mathcal { X }$ be the new customer. The probability of recommending product $y { \in } { \mathcal { V } } _ { r } = \mathcal { V } \setminus \mathcal { V } _ { h }$ is equal to $\begin{array} { r } { P ( y \mid x _ { n } ) = \sum _ { z \in \mathcal { Z } } P ( z \mid x _ { n } ) P ( y \mid z ) } \end{array}$ . Here, the only unknown, $P ( z | x _ { n } )$ , is the probability that $x _ { n }$ falls in the latent class z. To estimate its value, we use the only available information about the new customers $x _ { n } ,$ i.e., his/her ratings for products in ${ \mathcal { N } } _ { \mathrm { h } } .$ . This is then used to compute the similarity between those ratings and the probability distribution of $y \in \mathcal { V } _ { \mathrm { h } }$ given z. Mathematically, $P ( z | x _ { n } )$ is estimated as:

$$
\begin{array}{l} P (z \mid x _ {n}) = \sum_ {y _ {h} \in \mathcal {Y} _ {h}} \hat {P} (z, y _ {h} \mid x _ {n}) \\ = \sum_ {y _ {h} \in \mathcal {Y} _ {h}} P (z \mid y _ {h}) P (y _ {h} \mid x _ {n}) \\ \propto \sum_ {y _ {h} \in \mathcal {Y} _ {h}} P (y _ {h} \mid z) P (z) P (x _ {n}, y _ {h}) \\ \simeq \sum_ {y _ {h} \in \mathcal {Y} _ {h}} P (y _ {h} \mid z) P (z) n (x _ {n}, y _ {h}) \end{array}\tag{3}
$$

where the prior $P ( y _ { h } )$ on the products in ${ \mathcal { V } } _ { \mathrm { h } }$ is assumed constant. The estimation of $P ( z | x _ { n } )$ based on Eq. (3) is equivalent to an inner product between $P ( y _ { h } | z )$ and $n ( x _ { n } , y _ { h } )$ weighted by P(z). If the prob ability distribution on ${ \mathcal { N } } _ { \mathrm { h } }$ is similar to the distribution of $\{ n ( x _ { n } , y _ { h } ) { : } y _ { h } { \in } { \mathcal { V } } _ { h } \}$ , the inner product will result in a higher value, indicating that it is highly likely for $x _ { n }$ belonging to the preference pattern z.

In the extreme case where the new customer has not rated anything before, $\mathcal { V } _ { \mathrm { h } } = \emptyset$ and $P ( y | x _ { n } )$ degenerates to $\begin{array} { r } { P ( y \mid x _ { n } ) = P ( y ) = \sum _ { z \in \mathcal { Z } } P ( z ) P ( y \mid z ) } \end{array}$ . Recommendations are thus simply based on the ‘‘averaged’’ opinions of all customers in the training set. In other words, the most popular products in $\mathcal { V }$ among all customers in X will be recommended.

## 4. Evaluation

For performance evaluation, we form our dataset by using the Internet Movie Database (IMDb)<sup>5</sup> for movie contents and the EachMovie database<sup>6</sup> for movie ratings. The EachMovie database was collected by the EachMovie collaborative filtering site, deployed by the Compaq Systems Research Center for an 18- month period from 1995 through 1997. Some collaborative systems [20,21] have used another movie ratings database from the MovieLens system,<sup>7</sup> which contains 122,176 ratings from 1173 users. Other works using smaller, proprietary databases have also been reported [3,5]. The advantages, however, in our selection of the IMDb and EachMovie databases are that they are large (with a total of 1628 movies and 2,811,983 user ratings from 72,916 users), publicly available and also have been widely used in previous studies (e.g., Refs. [6,7,11,22]). The ratings in the EachMovie are discretized into six levels, as 0, 0.2, 0.4, 0.6, 0.8 and 1. In the following, we define a movie as ‘‘interesting’’ to an individual customer if his/her preference rating for this movie is greater than 0.5.

In our experiments, two different performance measures have been used. The first one we use is the break-even point, which is the point at which recall equals precision, and has been commonly used in information retrieval. In the current context, movies in the test set are ordered by decreasing preference (estimate) $\nu _ { i j }$ and recall is the percentage of interesting movies that can be located, whereas precision is the percentage of movies that are predicted to be interesting and are really interesting to the customer. If one is more interested in the quality of the highly ranked items, the precision rate at low recall rate (say 10%) can also be used. The second measure is based on the expected utility used in Ref. [7] for evaluating the quality of the predicted product ranking. Again, we utilize the list used in computing the break-even point. We assume that each successive item in this list will be less likely to be viewed by the customer with an exponential decay. The expected utility for customer $x _ { i }$ is then

$$
R _ {i} = \sum_ {j} \frac {\max (v _ {i j} - d , 0)}{2 ^ {(j - 1) / (\beta - 1)}},
$$

where d is the neutral vote (here, we take 0.5) and $\beta$ is the viewing half-life (which is set to 5). We also compute the maximum and minimum achievable utilities $R _ { i } ^ { \operatorname* { m a x } }$ and $R _ { i } ^ { \mathrm { { \ m i n } } }$ , and the final score is then computed as

$$
\text { utility } = \frac {R _ {i} - R _ {i} ^ {\min}}{R _ {i} ^ {\max} - R _ {i} ^ {\min}}.\tag{4}
$$

## 4.1. Content-based recommendation

In this section, we compare five techniques that can be used for content-based recommendation, including the naive Bayes classifier, 1-nearest-neighbor classifier, the SVM, the decision tree classifier C4.5 [42] and its associated production rule generator C4.5rules.

## 4.1.1. Movie information

Information about the movies, as mentioned above, are extracted from the Internet Movie Database (IMDb). The following 12 attributes are extracted from each movie record:

. Continuous attributes: Release date and Runtime.

. Multi-valued attributes in which each movie can take on at most one value: Language, Certification, Directors, Producers, Original music and Writers. Note that Directors, Producers, Original music and Writers may actually involve more than one person. However, for simplicity, we will only consider the first one that appears on the list.

. Multi-valued attributes in which each movie may take on multiple values: Genre, Country, Plot keyword and Cast. Because of the possibly large number of actors, we extract only the first 10 from each movie.

For the multi-valued attributes, we take the popular approach of representing each of them as a set of binary features. For example, the Cast feature will be represented as a set of binary features such as ‘‘Cast includes Dustin Hoffman’’, ‘‘Cast includes Bruce Willis’’, ‘‘Cast includes Leonardo DiCaprio’’, etc. The total size of the resultant set of features is 6620. Moreover, here we adopt a purely content-based approach and so no collaborative information (e.g. such as User comments, External reviews and Newsgroup reviews) from the IMDb has been used. As demonstrated in previous studies [36], the incorporation of collaborative content can be expected to further boost the performance.

Table 1  
Performance of different content-based recommender systems

<table><tr><td></td><td>Utility (%)</td><td>Break-even point (%)</td></tr><tr><td>SVM</td><td>63.6*</td><td>80.3*</td></tr><tr><td>Naive Bayes</td><td>60.0</td><td>78.8</td></tr><tr><td>C4.5rules (no. of feature = 100)</td><td>52.3</td><td>75.1</td></tr><tr><td>C4.5rules (all features)</td><td>52.6</td><td>76.0</td></tr><tr><td>1-Nearest-neighbor</td><td>45.5</td><td>76.2</td></tr></table>

The best results are indicated with boldface. The results marked with asterisks mean that the improvement is 99% confident according to the t-test.

## 4.1.2. Experimental setup

Results reported here are based on five-fold crossvalidation, averaged over 100 customers randomly selected from the EachMovie database. All 1628 movies are used, and no feature selection is performed except for C4.5 and C4.5rules. Moreover, recall that computations of both the break-even point and the utility measure in Eq. (4) require ranking the movies by decreasing preference estimates. For the naive Bayes classifier, this is performed by ranking the movies by decreasing posterior odds. For the SVM, we rank the movies by decreasing $\mathbf { w } ^ { \mathrm { T } } \mathbf { f } + b$ . For C4.5rules, we rank by the distance (based on the simplified value difference metric [16]) between $\mathbf { f } _ { j }$ and its nearest rule.

## 4.1.3. Results

Table 1 shows the performance of different contentbased recommendation methods. As can be seen, the superiority of SVM is statistically significant under both measures.

## 4.2. Collaborative recommendation

## 4.2.1. Experimental setup

In this section, we compare the LCM with the standard memory-based method using the Pearson correlation coefficient (P-Corr). The first 500 movies and a random subset of 500 customers<sup>8</sup> from the EachMovie dataset are used. Five-fold cross-validation is adopted for the evaluation. For each customer in the test set, we use ratings for the first 250 products to estimate the latent class probability $P ( z | x _ { n } )$ and

those for the remaining 250 to compute the performance. For training the LCM, the EM algorithm we used can only converge to a local minimum in general, and its performance thus depends on the model initialization step. In our implementation, we have tried two different schemes. The first one is random initialization. The second one is based on a simple clustering scheme. Under the second scheme, $P ( z )$ is initialized to $1 / N _ { z }$ . For $P ( y | z )$ , ratings for all the customers of a particular product are collected into one feature vector (with all the missing ratings are set to zero) and then the K-means clustering algorithm is applied (with $K { = } N _ { z } )$ . Moreover, $P ( y | z )$ is initialized to one if y is in cluster z, and zero otherwise. $P ( y | z )$ is initialized similarly, and an individual customer’s ratings on all the products are collected as a feature vector for clustering. Experimental results reveal that both schemes give similar results. All the results reported in the following are based on random initialization. For performance evaluation, we have used break-even point, precision at 10% of recall and utility.

## 4.2.2. Results

Table 2 tabulates the results. Performance of the LCM is generally superior to that of P-Corr, especially when the preference history is short. We have also performed the t-test for our cross-validation results. As revealed in the table, based on the utility measure, the improvement is statistically significant in most of the cases, especially when the length of preference history is short. This improvement due to LCM is also in line with the argument that model-based approaches can effectively alleviate the sparsity problem. However, as the history length continues to increase, the performance of the LCM is found to be saturated while that of P-Corr keeps improving. This probably implies model deficiency in the LCM and further research effort is required along the model enhancement direction.

Performance comparison between LCM and P-Corr

<table><tr><td rowspan="2">History length</td><td rowspan="2">No. of latent classes</td><td colspan="2">Utility (%)</td><td colspan="2">Precision at 10% recall (%)</td><td colspan="2">Break-even point (%)</td></tr><tr><td>LCM</td><td>P-Corr</td><td>LCM</td><td>P-Corr</td><td>LCM</td><td>P-Corr</td></tr><tr><td rowspan="5">2.4</td><td>1</td><td>57.66</td><td>50.15</td><td>89.08</td><td>81.20</td><td>79.33</td><td>77.84</td></tr><tr><td>2</td><td>63.36*</td><td></td><td>92.90</td><td></td><td>80.19</td><td></td></tr><tr><td>3</td><td>62.49</td><td></td><td>92.32</td><td></td><td>80.07</td><td></td></tr><tr><td>5</td><td>62.96</td><td></td><td>93.20*</td><td></td><td>80.10</td><td></td></tr><tr><td>8</td><td>62.31</td><td></td><td>92.29</td><td></td><td>80.04</td><td></td></tr><tr><td rowspan="5">4.3</td><td>1</td><td>57.66</td><td>55.78</td><td>89.08</td><td>86.43</td><td>80.59</td><td>79.28</td></tr><tr><td>2</td><td>64.34*</td><td></td><td>93.76*</td><td></td><td>80.60</td><td></td></tr><tr><td>3</td><td>64.08</td><td></td><td>93.43</td><td></td><td>80.50</td><td></td></tr><tr><td>5</td><td>64.17</td><td></td><td>93.47</td><td></td><td>80.66</td><td></td></tr><tr><td>8</td><td>63.81</td><td></td><td>93.62</td><td></td><td>80.47</td><td></td></tr><tr><td rowspan="5">6.2</td><td>1</td><td>57.66</td><td>57.08</td><td>89.08</td><td>86.43</td><td>79.33</td><td>79.43</td></tr><tr><td>2</td><td>64.78</td><td></td><td>94.17</td><td></td><td>80.77</td><td></td></tr><tr><td>3</td><td>64.86</td><td></td><td>94.21*</td><td></td><td>80.78</td><td></td></tr><tr><td>5</td><td>65.08*</td><td></td><td>94.05</td><td></td><td>80.75</td><td></td></tr><tr><td>8</td><td>64.63</td><td></td><td>93.69</td><td></td><td>80.89</td><td></td></tr><tr><td rowspan="5">8.7</td><td>1</td><td>57.66</td><td>58.54</td><td>89.08</td><td>87.61</td><td>79.33</td><td>79.79</td></tr><tr><td>2</td><td>64.81</td><td></td><td>94.06</td><td></td><td>80.83</td><td></td></tr><tr><td>3</td><td>64.86</td><td></td><td>94.07</td><td></td><td>80.79</td><td></td></tr><tr><td>5</td><td>65.25*</td><td></td><td>94.21*</td><td></td><td>80.91</td><td></td></tr><tr><td>8</td><td>64.78</td><td></td><td>93.47</td><td></td><td>80.98</td><td></td></tr><tr><td rowspan="5">11.2</td><td>1</td><td>57.66</td><td>61.37</td><td>89.08</td><td>89.70</td><td>79.33</td><td>80.55</td></tr><tr><td>2</td><td>64.82</td><td></td><td>93.94</td><td></td><td>80.83</td><td></td></tr><tr><td>3</td><td>64.86</td><td></td><td>93.92</td><td></td><td>80.80</td><td></td></tr><tr><td>5</td><td>65.16</td><td></td><td>93.91</td><td></td><td>80.92</td><td></td></tr><tr><td>8</td><td>64.81</td><td></td><td>93.65</td><td></td><td>80.87</td><td></td></tr></table>

The best results are indicated with boldface. It is noted that LCM outperforms P-Corr in all the cases. The results marked with asterisks mean that the improvement is 99% confident according to the t-test.

![](/api/attachments/5KSY3MSS/fulltext/images/2180f5e6afa0233987d1c0bb1c5ccb9ec5302c33c172c229a226df1dc84116ae.jpg)  
(b)LCM (N=5)

LCM - Train: #movies=500.#raters=400: Test: #movies=250. #raters=100: #class=5  
![](/api/attachments/5KSY3MSS/fulltext/images/e3a828ff091750c3c1a67281340009a1a5cfe9a3c4fbb56b63deb9a7c582b998.jpg)  
Fig. 3. The recall – precision curves for the P-Corr and the LCM. It is noted that the LCM is superior to the P-Corr, especially when the recall is low.

Besides, it is observed that the improvement is not that significant when the evaluation is based on the break-even point but is much more prominent when the precision rate at 10% recall rate is used. Similar observation is also shown in Fig. 3a and b, the recall– precision curves for P-Corr and the LCM $( N _ { z } = 1 5 )$ respectively. By comparing the two figures, it is noted that both the P-Corr and the LCM perform similarly at around the break-even point. But when the recall is low (which is more common in recommender systems as customers normally do not prefer to go through a long list to look for interested items), the LCM achieves a significantly higher precision when compared to P-Corr.

Also, the performance of the LCM first improves as the number of latent classes increases. It then degrades when the number continues to increase, possibly caused by overfitting. According to our experiment, the optimal number of latent classes varies for different preference history lengths. The question of selecting an optimal number of latent classes remains an open research issue.

## 5. Conclusion

In this paper, we applied two recent machine learning methods for recommender systems. We used the support vector machine for content-based recommendation. This yields superior performance when compared to other traditional content-based techniques, while at the same time avoids the problem of feature selection. For collaborative recommendation, we extended the latent class model to recommend products to customers outside the training set. Experimentally, this model-based approach can effectively alleviate the sparsity problem.

An important characteristic of product recommendation is that the size of the customer pool and the number of available products are usually very large. So, other than accuracy, system efficiency is also a major concern. For both SVM and LCM, most of the computational cost is involved in the training process, and this can be done off-line in the initial training phase. After that, the resultant model is a compact representation of the raw ratings information, and thus the time and space complexities on making recommendations are quite low. With the (possibly batched) arrival of more preference ratings and/or new products, the models will still have to be re-trained. The SVM has been experimentally shown to perform very well under incremental training [46]. As for the EM algorithm, both fast and incremental versions have also been reported recently [37,38].

While content-based recommendation and collaborative recommendation are complementary in nature, in situations where both the product descriptions and the preference ratings are abundant, it would further boost the performance by integrating these two approaches. Recently, this is being investigated by a number of researchers [1,4,5,11,20] and we will continue to investigate this in the future.

## Acknowledgements

This research has been partially supported by the Research Grants Council of the Hong Kong Special Administrative Region under grant HKUST2033/00E and the Hong Kong Baptist University under grant FRG/99-00/II-36P. The EachMovie dataset for this paper was provided by Digital Equipment. The authors would also like to thank Thorsten Joachims for his SVM-Light [25] used in the experiments.

## References

[1] C.C. Aggarwal, J.L. Wolf, K.L. Wu, P.S. Yu, Horting hatches an egg: a new graph-theoretic approach to collaborative filtering, Proceedings of the Fifth ACM SIGKDD International Conference on Knowledge discovery and data mining, San Diego, August 1999, pp. 201 – 212.

[2] H. Almuallim, T.G. Dietterich, Learning with many irrelevant features, Proceedings of the Ninth National Conference on Artificial Intelligence, Anaheim, CA, USA, 1991, pp. 547 – 552.

[3] J. Alspector, A. Kolez, N. Karunanithi, Comparing featurebased and clique-based user models for movie selection, Proceedings of the Third ACM Conference on Digital Libraries, 1998, pp. 11– 18.

[4] M. Balabanovic´, Y. Shoham, Content-based, collaborative recommendation, Communications of the ACM 40 (3) (March 1997) 66– 72.

[5] C. Basu, H. Hirsh, W. Cohen, Recommendation as classification: using social and content-based information in recommen-

dation, Proceedings of the Fifteenth National Conference on Artificial Intelligence, Madison, WI, USA, July 1998, pp. 714–720.

[6] D. Billsus, M.J. Pazzani, Learning collaborative information filter, Proceedings of the Fifteenth International Conference on Machine Learning, Madison, WI, 1998, pp. 46 – 54.

[7] J.S. Breese, D. Heckerman, C. Kadie, Empirical analysis of predictive algorithms for collaborative filtering, Proceedings of the Fourteenth Conference on Uncertainty in Artificial Intelligence, Madison, WI, July 1998.

[8] C.J.C. Burges, A tutorial on support vector machines for pattern recognition, Data Mining and Knowledge Discovery 2 (2) (1998) 955–974.

[9] V.L. Centeno, C.F. Panadero, C.D. Kloos, Personalizing your electronic newspaper, Proceedings of the 4th Euromedia Conference, April 1999, pp. 26 – 28.

[10] M. Claypool, A. Gokhale, T. Miranda, Combining contentbased and collaborative filters in an online newspaper, SI-GIR’99 Workshop on Recommender Systems: Algorithms and Evaluation, 1999.

[11] M.K. Condliff, D.D. Lewis, Bayesian mixed-effects models for recommender systems, Proceedings of the SIGIR-99 Workshop on Recommender Systems: Algorithms and Evaluation, Berkeley, CA, August 1999.

[12] R. Cooley, B. Mobasher, J. Srivastava, Data preparation for mining world wide web browsing patterns, Knowledge and Information Systems 1 (1) (February 1999) 5 – 32.

[13] M. Dash, H. Liu, Feature selection for classification: a survey, Intelligent Data Analysis 1 (3) 1997.

[14] S. Deerwester, S.T. Dumais, G.W. Furnas, T.K. Landauer, R. Harshman, Indexing by latent semantic analysis, Journal of the American Society of Information Science 41 (6) (September 1990) 391– 407.

[15] A.P. Dempster, N.M. Laird, D.B. Rubin, Maximum-likelihood from incomplete data via the EM algorithm, Journal of the Royal Statistical Society, Series B 39 (1977) 1 – 38.

[16] P. Domingos, Unifying instance-based and rule-based induction, Machine Learning 24 (1996) 141– 168.

[17] S. Dumais, Using SVMs for text categorization, IEEE Intelligent Systems, (1998) 21– 23.

[18] D. Gildea, T. Hofmann, Topic-based language models using EM, Proceedings of Sixth European Conference On Speech Communication and Technology (Eurospeech99), 1999.

[19] D. Goldberg, D. Nichols, B.M. Oki, D. Terry, Collaborative filtering to weave an information tapestry, Communications of the ACM 35 (12) (December 1992) 61 – 70.

[20] N. Good, J.B. Schafer, J.A. Konstan, A. Borchers, B. Sarwar, J. Herlocker, J. Riedl, Combining collaborative filtering with personal agents for better recommendations, Proceedings of the 1999 Conference of the American Association of Artifical Intelligence (AAAI-99), July 1999.

[21] J.L. Herlocker, J.A. Konstan, A. Borchers, J. Riedl, An algorithmic framework for performing collaborative filtering, Proceedings of the 1999 Conference on Research and Develop ment in Information Retrieval, August 1999.

[22] T. Hofmann, J. Puzicha, Latent class models for collaborative filtering, Proceedings of the Seventeenth International Joint

Conference on Artificial Intelligence (IJCAI99), 1999, pp. 688– 693.

[23] T. Hofmann, J. Puzicha, J.M. Buhmann, Unsupervised texture segmentation in a deterministic annealing framework, IEEE Transactions on Pattern Analysis and Machine Intelligence 20 (8) (August 1998) 803 – 818.

[24] T. Joachims, Text categorization with support vector machines: learning with many relevant features, European Conference on Machine Learning, 1998.

[25] T. Joachims, Making large-scale support vector machine learning practical, in: B. Scho¨lkopf, C. Burges, A. Smola (Eds.), Advances in Kernel Methods - Support Vector Learning, MIT Press, Cambridge, MA, 1999, pp. 169–184.

[26] G.H. John, R. Kohavi, K. Pfleger, Irrelevant features and the subset selection problem, in: W.W. Cohen, H. Hirsh (Eds.), Machine Learning: Proceedings of the Eleventh International Conference, Morgan Kaufmann Publishers, San Francisco, CA, 1994, pp. 121–129.

[27] A. Kohrs, B. Merialdo, Clustering for collaborative filtering applications, Computational Intelligence for Modelling Control and Automation, IOS Press, Vienna, 1999.

[28] J.A. Konstan, B.N. Miller, D. Maltz, J.L. Herlocker, L.R. Gordon, J. Riedl, Applying collaborative filtering to Usenet news, Communications of the ACM 40 (3) (March 1997) 77 – 87.

[29] J.T. Kwok, Automated text categorization using support vector machine, Proceedings of the International Conference on Neural Information Processing, Kitakyushu, Japan, October 1998, pp. 347 – 351.

[30] J.T. Kwok, Moderating the outputs of support vector machine classifiers, IEEE Transactions on Neural Networks 10 (1999) 1018– 1031.

[31] K. Lang, NewsWeeder: learning to filter Netnews, Proceedings of the Twelfth International Conference on Machine Learning, Tahoe City, CA, 1995, pp. 331–339.

[32] D.D. Lewis, M. Ringuette, A comparison of two learning algorithms for text categorization, Third Annual Symposium on Document Analysis and Information Retrieval, Las Vegas, NV, April 1994, pp. 81– 93.

[33] W.J. McDonald, Direct Marketing, McGraw-Hill, Singapore, 1998.

[34] G.J. McLachlan, K.E. Basford, Mixture Models: Inference and Applications to Clustering, Dekker, New York, 1988.

[35] T.M. Mitchell, Machine Learning, McGraw-Hill, New York, 1997.

[36] R.J. Mooney, L. Roy, Content-based book recommending using learning for text categorization, SIGIR’99 Workshop on Recommender Systems: Algorithms and Evaluation, 1999.

[37] A. Moore, Very fast EM-based mixture model clustering using multiresolution kd-tree, Neural Information Systems Processing, December 1998.

[38] R.M. Neal, G.E. Hinton, A view of the EM algorithm that justifies incremental, sparse, and other variants, in: M.I. Jordan (Ed.), Learning in Graphical Models, Kluwer Academic Publishing, Dordrecht, 1998, pp. 355– 368.

[39] E. Osuna, R. Freund, F. Girosi, Training support vector machines: an application to face detection, Proceedings of Computer Vision and Pattern Recognition, Puerto Rico, June 1997.

[40] M.J. Pazzani, A framework for collaborative, content-based and demographic filtering, Artificial Intelligence Review, 1999.

[41] M. Pazzani, D. Billsus, Learning and revising user profiles: the identification of interesting web sites, Machine Learning 27 (1997) 313–331.

[42] J.R. Quinlan, C4.5: Programs for Machine Learning. Morgan Kaufmann, 1993.

[43] P. Resnick, N. Iacovou, M. Suchak, P. Bergstorm, J. Riedl, GroupLens: an open architecture for collaborative filtering of netnews, Proceedings of ACM 1994 Conference on Computer Supported Cooperative Work, New York, NY, ACM 1994, pp. 175– 186, (Chapel Hill, NC).

[44] B. Scho¨ lkopf, K. Sung, C. Burges, F. Girosi, P. Niyogi, T. Poggio, V. Vapnik, Comparing support vector machines with Gaussian kernels to radial basis function classifiers, IEEE Transactions on Signal Processing 45 (11) November 1996, pp. 2758– 2765.

[45] U. Shardanand, P. Maes, Social information filtering: algorithms for automating ‘word of mouth’, Proceedings of the Computer-Human Interaction Conference (CHI95), Denver, CO, May 1995.

[46] N.A. Syed, H. Liu, K.K. Sung, Incremental learning with support vector machines, Workshop on Support Vector Machines, International Joint Conference on Artificial Intelligence, 1999.

[47] L.H. Ungar, D.P. Foster, Clustering methods for collaborative filtering, Recommender Systems - Papers from the AAAI Workshop, Madison, WI, July 1998.

[48] V. Vapnik, Statistical Learning Theory, Wiley, New York, 1998.

Kwok-Wai Cheung received his BSc and MPhil degrees both in electronic engineering from the Chinese University of Hong Kong, and his PhD degree in computer science from the Hong Kong University of Science and Technology. He was the recipient of the Croucher Foundation Studentship and the Edward Youde Memorial Scholarship in 1991 and 1993, respectively. He is currently an Assistant Professor in the Department of Computer Science, Hong Kong Baptist University. His current research interests include pattern recognition, machine learning, data mining and intelligent agents.

James T. Kwok received the PhD degree in computer science from the Hong Kong University of Science and Technology in 1996. He was an Assistant Professor in Hong Kong Baptist University. Currently, he is an Assistant Professor in the Department of Computer Science, the Hong Kong University of Science and Technology. His research interests include support vector machines, artificial neural networks, pattern recognition and machine learning.

Martin H. Law received his BEng and MPhil degrees in computer science from the Hong Kong University of Science and Technology in 1996 and 1999, respectively. He is currently a PhD student at the Michigan State University. His research interests include support vector machines, statistical pattern recognition, machine learning and data mining.

Kwok-Ching Tsui received his PhD and MSc degree from King’s College, University of London and University of Essex, respectively, both in computer science. He is currently a Postdoctoral Teaching Fellow at Hong Kong Baptist University. Prior to joining the university, he was a senior research scientist at British Telecom. His current research interests include autonomy-oriented computation, intelligent agents and soft computing.
