---
otero_id: 6840
otero_key: "YFVGSB2P"
title: "A support system for predicting eBay end prices"
authors: "Dennis van Heijst; Rob Potharst; Michiel van Wezel"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.11.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A support system for predicting eBay end prices

Dennis van Heijst, Rob Potharst, Michiel van Wezel <sup>⁎</sup>

Econometric Institute, Erasmus School of Economics, Erasmus University, P.O. Box 1738, 3000 DR, Rotterdam, The Netherlands

Received 25 October 2006; received in revised form 18 October 2007; accepted 14 November 2007 Available online 22 November 2007

## Abstract

We create a support system for predicting end prices on eBay. The end price predictions are based on the item descriptions found in the item listings of eBay, and on some numerical item features. The system uses text mining and boosting algorithms from the field of machine learning. Our system substantially outperforms the naive method of predicting the category mean price. Moreover, interpretation of the model enables us to identify influential terms in the item descriptions and shows that the item description is more influential than the seller feedback rating, which was shown to be influential in earlier studies. © 2007 Elsevier B.V. All rights reserved.

Keywords: Boosting; eBay; Electronic auctions; Text mining

## 1. Introduction

Online auctions are hot. The world's largest online auction site eBay reports in its first quarter financial report over 2006 a net revenue of \$1.39 billion, realizing a growth rate of 35% in consecutive years [10]. For researchers with an interest in data mining, online auctions offer the opportunity to collect and mine large data sets at low costs.

The market price of a product is generally nonstationary at eBay — it fluctuates over time. It is even possible that identical items receive different bids at any given point in time. Merchants might buy items at eBay and try to re-sell these items with a profit. The success of these merchants depends on their ability to find bargains and, of course, their bidding strategy. Finding these bargains can be made easier by using a support system.

A recent paper [15] introduces the ‘Auction Advisor system, which simplifies the search for bargains by presenting its user with relevant information like the current bid and a recommended price based on recently closed auctions. Using this standardized presentation, the user is able to make bidding decisions within a short amount of time. In this paper we improve on this recommended price by making a price prediction based on several relevant characteristics of the auction: the number of pictures, the feedback rating, and the description of the item.

A substantial amount of research has been carried out on the analysis of historical auctions using data mining and statistical techniques. (An interesting review of this work from an economics perspective is given in [5].) Most of this work focuses on finding factors determining the auction end price. Reference [9] for example, tries to find such factors using a data set of ancient coin sales at eBay and finds that the number of participants, the use of reserve prices, and seller reputations are determinants of the end price. Others aim at characteristic behavior like last moment bidding [26]. For only a few studies the prediction of auction prices is the central problem. Several data mining methods are compared in [14] in order to find the most suitable method for price prediction, while [30] constructs a dynamic forecasting model, which can update the predicted price of an ongoing auction based on newly arrived information.

Unlike previous studies, we incorporate the textual information contained in the item description in our system when predicting the auction end price. To this end, our system downloads data on a large number of closed auctions from the eBay site. This data is then pre-processed and fed to a price–prediction model. Section 2 below discusses the data collection system and the pre-processing steps. The price–prediction model makes use of a vector space representation of the descriptions of the items [27]. Each position in the vector represents the occurrence — count of a specific word in an item description. This representation, known as the bag-of-words representation, is often used in Information Retrieval Systems. In these systems, the distance between the bag-of-word vectors of strings is used to find similar strings or documents.

Instead of using similarity calculations, our price– prediction model is based on boosting [13]. Boosting creates an ensemble of models that collectively make a prediction, in our case for the end price of the auction.

We use decision trees as the individual models that form the ensemble, as is often done. Decision trees select important input dimensions in the course of their calibration process. This is a desirable property in text mining, as the number of input dimensions is usually very high. Section 3 discusses the models that we use in our system in more detail.

We test our system in two experiments described in Section 4. The paper ends with conclusions and a discussion in Section 5.

## 2. Data

There are several ways to collect auction data from eBay. Examples include using eBay's API (Application Programmers Interface), a web crawler, and buying a data set. Our system uses a web crawler that downloads the HTML source code of an auction page given its auction ID. (The crawler was written in Java.) The downloaded auction pages are the main HTML pages from eBay, they do not include the seller's feedback pages nor do they include the bidding history. Fig. 1 shows an example of (part of) a downloaded auction page.

Finding the auction IDs of closed auctions in a specific product category can be done using eBay's search mechanism or by using a software tool called Harvex [16]. The

![](/api/attachments/YFVGSB2P/fulltext/images/43c81ac5bf93a5dfa5179e8d5097b7e52c7d6cf1b47de24df639416ce540e2bd.jpg)  
Fig. 1. One of the downloaded eBay auction pages.

IDs for two of the data sets we describe below were downloaded manually — these are the Nike and Canon data sets, downloaded in 2005. The other two data sets, downloaded in May 2007, were collected using Harvex. Harvex enabled us to filter auction IDs of the auctions that were either unsold or not sold in US dollars.

## 2.1. Features included

The prediction module in our system does not deal with the unstructured HTML data downloaded by the crawler. Instead, it needs input features with clear semantics that are relevant for the auction end price. Our prediction model is based upon the following features: The feedback rating, the number of pictures, and the description of an item. First, we will summarize the reasons for using these features. Next, we will discuss how we construct these features from an eBay HTML page.

The first feature included is the feedback rating. eBay has a reputation system called the Feedback Forum. This system captures the reputation of an eBay member based on his earlier transactions. There are several studies indicating that there is a relationship between a seller's reputation and the expected auction end price, see e.g. [4,24]. This is why we added the feedback score as an element in our price prediction model.

A feedback mechanism falls into the broader category of trust mechanisms in e-commerce, which has received a lot of attention in the literature, see, e.g. [1,21,3,2,17]. Trust is not only created as a result of a high feedback rating. Bidders also want to have as much information as possible about the item for sale. This information helps to reduce the uncertainty on the item's quality, rather than reducing uncertainty on the seller as reputation mechanisms do.

Some elements of information are difficult to describe in words. For example, a ‘slightly worn shoe' could be seriously worn or be in near-mint condition. In such a case, pictures of the item provide bidders with useful and objective information. For that reason we included the number of pictures in an item description as a feature.

Another way for the seller to overcome the information asymmetry between the seller and the buyer is by describing the item in words. This description of an item is written in natural language. The text usually contains information like the possible uses of an item and the state of the item. It may also contain information on the transaction, such as return policies and shipping fares. Since this information is useful to the bidders the item description is included in the feature set.

Interestingly, it is a well-known result in auction theory [18] that the seller should disclose all information about the object being auctioned that is potentially of use to the bidders. This policy of making information publicly available raises the expected revenue for the seller. This is another motivation for trying to capture the available information in the features of our prediction module.

## 2.2. Data pre-processing

We now describe how the above mentioned features were constructed from a raw eBay HTML page, of which Fig. 2 shows an example. Retrieving price and feedback rating was straightforward: they are parsed from the page by looking for the first occurrence of Winning bid: and Feedback respectively. The number of pictures can be found by counting the number of bimgN tags in the description of the item.

The description of an item is written in natural language. Since the data mining method we use requires numerical input data, we need to transform the text of an item description into a numerical representation. This transformation is performed using a dictionary. Each individual item description is encoded by the frequency of occurrence of each word from the dictionary. This frequency can be either Boolean, indicating whether the word does or does not appear in the text, or numerical, indicating the number of occurrences in the text. This method is known as the bagof-words (BOW) method [27,31].

![](/api/attachments/YFVGSB2P/fulltext/images/a26016be97ebe75e94c7a1e31907ff0ad6c602036a3f7418236238ce6f599218.jpg)  
Fig. 2. Relevant source code of an eBay auction page.

![](/api/attachments/YFVGSB2P/fulltext/images/b9566d78ce55043366cf077ea200f694b7fcf655e3f0f7ee291d93f86a32e882.jpg)  
Fig. 3. A sample text stripped by Porter's stemming algorithm.

There has been some criticism on BOW. One argument is that when we use BOW, we lose semantics [20]. By looking at words only, we lose the extra information given in a sentence. For instance, adding the word not to a sentence may change its semantics completely. This change in meaning is not detectable by just increasing the occurrence of not, when using large texts. The key assumption of BOW, namely that the position of a word in a document does not matter, is indeed disputable, but in practice BOW does perform quite well [19,28], and it is easy to implement. The following paragraphs illustrate how the dictionary of a description is made.

When creating the vectors we use a local pooled dictionary. This dictionary is therefore created by the words in the observed documents. Using these local pooled dictionaries instead of widely used ones is recommended in [31]. The authors of [31] conclude that the words in and the size of the dictionary are very important for the computational speed and the results of the prediction model.

To diminish the size of the dictionary we use Porter's stemming algorithm [22]. This algorithm strips the endings from many words in English. One example of this stripping is to convert plurals to their singular form by stripping the letter s. It is used as part of a term normalization process that is usually done when setting up Information Retrieval Systems. It assumes that although these words differ in quantity, they do belong to the same term. Therefore, we can change words to their root by stripping off the suffix, without changing what is meant. In Fig. 3 you can read this paragraph stripped by Porter's stemming algorithm.

The frequency of occurrence of each word was counted after stemming the description. We introduced a lower bound, $f _ { \mathrm { l } } ,$ to filter out infrequently used words from our dictionary. This means that only words which have at least a total occurrence of f were considered. Besides lowering the computational requirements of the system, the motivation for this lower bound is that our prediction model needs a certain number of examples to be able to correctly recognize the importance of a word: The model could easily over-fit on a misspelled or infrequent word, because it lacks counter examples.

The over-fitting problem does not only occur with infrequent words, but also with words which occur too frequently. These words are referred to as stop words. Stop words are commonly used words like I, is and and. These words do not contribute to the information that a description conveys. Therefore, these words are filtered out. Our list of stop words was not generated from the local dictionary, but a predefined frequently used list was downloaded from the internet.

A BOW representation is usually stored as a vector in which each dimension holds the occurrence or count of a specific word. An example of such a vector is shown in Fig. 4. It shows the previously stemmed paragraph, after filtering it with our list of stop words. (In this example the lower bound f<sub>l</sub> was set to 1.) For use in the support system, we extended our BOW vectors with dimensions for the feedback rating, the number of pictures and the price, as was discussed earlier.

## 2.3. Data sets used in the experiments

In order to test our price prediction module, we downloaded four independent data sets from four auction categories. These data sets concerned closed auctions of Canon digital cameras, Nike men shoes, H700 Motorola Bluetooth headsets, and 30 GB Apple iPod mp3 players. The first two data sets were downloaded in August 2005, the latter two in May 2007. All data sets were downloaded using a crawler as described in Section 2.

The Nike and Canon data sets are both heterogeneous data sets: The Nike data set contains data on auctions of various models of Nike men's shoes, both used and new.

```csv
Terms
plural, normal, form, strip, suffix, retrieve, belong, read,
singular, algorithm, figur, meant, letter, end, process, chang,
word, assum, usual, quantiti, system, stem, english, exampl,
term, root, set, convert, porter, inform, paragraph, diminish,
size, dictionari

Vector
(1,1,1,5,1,1,1,1,1,3,1,1,1,1,1,2,3,1,1,1,1,2,1,1,2,1,1,1,2,1,1,1,1)
```  
Fig. 4. Vector representation of the sample text.

The Canon data set contains data on multiple camera models, but also accessories like lenses and batteries. Therefore, it is likely that part of the variance in the observed auction prices is caused by this heterogeneity. Thus, we hypothesized that our learning algorithm would use terms in the item description related to product characteristics as important indicators for item value. For the Canon data sets, these terms were expected to be technical terms like ‘powershot’ and ‘rebel’, for the Nike data set we expected to find terms like ‘new’ and ‘used’.

Given an item that is up for auction, the characteristics of this item are beyond the seller's control. However, the way in which this item is described is within the seller's control. For instance, the seller may emphasize a flexible return policy, swift shipment, etcetera in his add text. To see whether an item's description actually influences the auction price we downloaded two (almost) homogeneous data sets. These data sets concerned auctions of H700 Motorola Bluetooth headsets and 30 GB Apple iPod mp3 players respectively — the items within each data set are technically identical. As stated earlier, the IDs for these auctions were collected using Harvex [16].

Unfortunately, the search mechanism also returned some auctions outside our target categories. For example, our data set included an auction of Nike shoes previously belonging to the famous basketball player Michael Jordan. Although these are Nike men's shoes, we did not want to predict collectibles. Also, some auctions resulted in a sale for a price that was not realistic, e.g., in auction number 3980930479, a brand new pair of Nike shoes that was sold for only \$0.01. We therefore excluded outliers of this type by filtering them using the upper and lower whiskers of a box-plot of the item's price: both very large and very small values were excluded. Table 1 gives a summary of the data sets and the pre-processing parameters.

## 3. Methodology used for price prediction

This section discusses the machine learning techniques used in our system. We denote the available data by $D = \{ ( \overrightarrow { \mathbf { x } _ { i } } ; y _ { i } ) \} _ { i = 1 } ^ { N }$ . An instance (observation, row) (<sup>Y</sup>x;y) consists of a vector of J attribute values $\scriptstyle { \overrightarrow { \mathbf { X } } } = ( x _ { 1 } , \ldots , x _ { J } )$ and a target value y. The J attributes are the explanatory or independent variables, in our case the term counts and other input features discussed in Section 2. The target is the explained or dependent variable, in our case the auction end price.

## 3.1. Classification And Regression Trees

CART (Classification And Regression Trees) [8] is one of the most frequently used methods for constructing decision trees. In this paper we use the CART regression tree.

A regression tree (see Fig. 3 for an example) consists of decision nodes and leaf nodes. Each decision node has two child nodes, which may again be decision nodes or leaf nodes. The root of the tree is on the very top — it is the only node in the tree without an ancestor. Every decision node (also called non-terminal node) contains a split criterion, which divides the data at that point into two parts. This split criterion has the format $x _ { j } \leq c _ { s }$ for continuous variables, where $x _ { j }$ is the jth variable and $c _ { s }$ is a constant that may be different for each split s. For a categorical variable the split criterion looks like $x _ { j } \in V ,$ with $V { \subset W _ { j } } .$ . Here $W _ { j }$ refers to the collection of all possible categories of variable $x _ { j } .$ The terminal nodes (leafs) contain a $\mathbf { \nabla } \cdot \hat { y }$ value, an estimate for the target value in that leaf. In practice this value is taken to be the average of all observed y values in that leaf.

Summary of the auction data sets

<table><tr><td></td><td>Nike</td><td>Canon</td><td>Headset</td><td>30G iPod</td></tr><tr><td>Download period</td><td>Aug 2005</td><td>Aug 2005</td><td>May 2007</td><td>May 2007</td></tr><tr><td>Downloaded auctions</td><td>5945</td><td>5042</td><td>4195</td><td>7087</td></tr><tr><td>Position upper whisker (price)</td><td>163.5</td><td>1175</td><td>25.05</td><td>260</td></tr><tr><td>Position lower whisker (price)</td><td>5</td><td>5</td><td>0.99</td><td>80</td></tr><tr><td>Non-outlier auctions</td><td>5546</td><td>4603</td><td>3861</td><td>5727</td></tr><tr><td>Average selling price ($)</td><td>60.61</td><td>355.86</td><td>12.41</td><td>174.51</td></tr><tr><td>Lower bound word occurrence (fi)</td><td>50</td><td>80</td><td>50</td><td>50</td></tr><tr><td>Number of words in dictionary</td><td>1258</td><td>1926</td><td>1007</td><td>1697</td></tr></table>

The whiskers refer to the box-plot used for filtering outliers. The parameter $f _ { 1 }$ was set in a series of preliminary experiments. The average selling price was computed over the non-outlier auctions.

The example regression tree shown in Fig. 3 can be used for prediction as follows. Suppose a new vector $\overrightarrow { \mathbf { X } } ^ { \prime }$ is presented to us, what will be our prediction of the target value for this vector? We begin at the root and if $\overrightarrow { \mathbf { X } } ^ { \prime }$ satisfies the split criterion we turn left; if not we turn right. We keep on doing this until we reach a terminal node and use the ŷ value in that node as our prediction of the target value for <sup>Y</sup>x.

Decision trees are usually built in two phases. The first phase is a growing phase, the second phase is a pruning phase. In the growing phase, the tree is grown until error reduction on the training set is no longer possible or a pre-determined threshold has been reached. The resulting model usually over-fits the data, and this is countered in a pruning phase, where the tree is shrunk until the error on a hold-out sample, the pruning set, is minimal. Details on the CART procedure for growing and pruning can be found in, e.g., [8,25]. Here, it is sufficient to remark that, given a data set $\{ ( \vec { \bf x } _ { i } ; y _ { i } ) \} _ { 1 } ^ { N } .$ , the CART algorithm constructs a regression tree B that attempts to minimize the squared error loss (Fig. 5)

$$
E _ {\overrightarrow {\mathrm{x}}, y} (B (\overrightarrow {\mathrm{x}}) - y) ^ {2},
$$

where B(<sup>Y</sup>x) denotes the prediction of tree B for input vector $\overrightarrow { \mathbf { X } } .$

In the context of boosting, discussed below, the pruning phase of the decision tree algorithm is usually skipped and instead the tree size is limited to a pre-determined depth. In the most extreme case the tree depth is 1. The tree then consists of a single decision node and two leaves. Such a special tree is called a decision stump. Although a single decision stump has very limited modeling power, an ensemble of such stumps is able to model complex relationships.

Regression trees have some advantages over the commonly used method of linear regression. In the first place, in contrast to regression functions, regression trees are able to determine themselves which of the attributes are to be used for modeling the relationship with the target variable. Another advantage is that regression trees are able to model interactions between attributes and nonlinear relationships with the target, without a required explicit transformation of the inputs. Furthermore, in contrast to many parametric models, regression trees can handle categorical variables and missing values without transformation of the data.

A drawback of decision trees is their instability — the implemented model depends heavily on the exact data set used for model creation, and a small change in the data may have large consequences for the model. Ensemble methods, such as bagging [6] and boosting, have a stabilizing effect by averaging over a number of decision trees. We discuss boosting next.

## 3.2. Boosting

Boosting is a method to combine multiple models to improve performance, i.e. to reduce the error on unseen data. Boosting was first applied to and developed for classification problems (with categorical response) in [11,12]. In a classification context boosting seemed to be able to strongly reduce the error rate on out-ofsample data in many cases [7]. The idea behind boosting is to create a sequence of models, called base learners, in which each subsequent base learner focuses on the residual error of the previous base learners. Often, these base learners are decision trees or stumps.

![](/api/attachments/YFVGSB2P/fulltext/images/f18245619b16effcc7356c2a20a2d85a2bdddd76e2d9ce8871de712e15e4b514.jpg)  
Fig. 5. A decision tree for a data set with two explanatory variables (left), and the corresponding partitioning of the feature space (right). For each leaf $\ell$ and each corresponding region $\mathrm { R } _ { \ell }$ the estimate of the target value is the average $\hat { y } _ { \ell }$ of the observed $y$ values within that region.

The original Freund and Schapire boosting algorithm for classification, AdaBoost.M1, was only applicable to binary classification problems. For these problems, the model predicts whether an instance belongs to a class or not. The model thus has a 0/1 output and the quality of the model is measured with the 0–1 loss function, which counts the number of misclassifications. For modeling eBay end prices this loss function is not suitable. Instead, we need a regression loss function that measures the deviance between two numerical values, as usual in regression. This means that we cannot apply the AdaBoost. M1 algorithm to eBay end prices. Instead, we use a special boosting algorithm, suitable for regression problems.

Various boosting algorithms have been designed for regression. Friedman [13] developed LSBoost, LADBoost and MBoost based on the squared, absolute and Huber loss function respectively. (All these loss functions apply to regression problems.) In this paper we use Friedman's LSBoost algorithm. This algorithm was chosen because, contrary to many other boosting algorithms, it has a solid mathematical foundation: it is an instantiation of a general boosting algorithm for general loss functions named GradientBoost.

We now give a brief description of GradientBoost and LSBoost. Contrary to fitting a single model, like the decision tree B above, boosting starts with an initial guess $F _ { 0 }$ and then fits a sequence of M models $B _ { 1 } , . . . , B _ { M }$ (the base learners) which are subsequently combined in a weighted manner. The final model is thus

$$
F _ {M} (\overrightarrow {\mathrm{x}}) = F _ {0} (\overrightarrow {\mathrm{x}}) + \nu \sum_ {m = 1} ^ {M} \rho_ {m} B _ {m} (\overrightarrow {\mathrm{x}}).
$$

Here, $\rho _ { m }$ denotes the weight for model m and is determined by the algorithm. M, the number of iterations, is set by the user. The number ν with $0 { < } \nu \leq 1$ denotes a regularization parameter called the learning rate. Small values of ν will help prevent the algorithm to over-fit the training data.

Note that at the mth iteration, $B _ { m } ( )$ is added to $F _ { m - 1 } \colon$

$$
F _ {m} (\overrightarrow {\mathrm{x}}) = F _ {m - 1} (\overrightarrow {\mathrm{x}}) + v \rho_ {m} B _ {m} (\overrightarrow {\mathrm{x}}).
$$

It makes sense to choose $B _ { m } ( )$ such that it minimizes the residual error of $F _ { m - 1 }$ . Roughly speaking, given a general loss function $L ( \nu , F ) , B _ { m }$ attempts to minimize the expected value of this loss function over the data set:

$$
B _ {m} = \arg \min _ {B} \sum_ {i = 1} ^ {N} L \left(y _ {i}, \left[ F _ {m - 1} (\overrightarrow {\mathrm{x} _ {i}}) + B (\overrightarrow {\mathrm{x} _ {i}}) \right]\right).\tag{1}
$$

In practice this is done by fitting pseudo-responses $\tilde { y _ { i } }$ in each iteration

$$
B _ {m} = \arg \min _ {B} \sum_ {i = 1} ^ {N} \left\{\widetilde {y} _ {i} - B (\overrightarrow {\mathrm{x} _ {i}}) \right\} ^ {2}.
$$

The values of the pseudo-responses depend upon the loss function in question. When GradientBoost is applied to the squared error loss function $L ( y , F ) { = } ( y { - } F ) ^ { 2 } / 2$ that is common in regression, the pseudo-responses are given by $\widetilde { y } _ { i | m } { = } y _ { i } { - } F _ { m - 1 } ( \overrightarrow { \mathbf { x } _ { i } } )$

The minimization over B in Eq. (1) is performed by minimizing over $B ^ { \prime } { \bf s }$ parameter space. If B is a tree, these parameters are the split variables and split points in the decision nodes, and $B _ { m }$ is the tree that gives the best fit of the y˜ values in iteration m. Fig. 1 summarizes the LSBoost algorithm.

## Algorithm 1. LSBoost algorithm [13]

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: data set with instances  $\{\overrightarrow{x_{i}};y_{i}\}_{1}^{N}$ 
number of iterations M
learning rate v

Output: Model  $F(\overrightarrow{x})$ $F_{0}(\overrightarrow{x})=\overline{y}$ 

For m=1 to M do
    $\{\tilde{y}_{i}=y_{i}-F_{m-1}(\overrightarrow{x_{i}})\}_{1}^{N}$ 
    train  $B_{m}(\overrightarrow{x})$  using  $\{\overrightarrow{x_{i}};\tilde{y}_{i}\}_{1}^{N}$ $\rho_{m}=\operatorname{argmin}_{\rho}\sum_{i=1}^{N}[\widetilde{y}_{i}-\rho B_{m}(\overrightarrow{x_{i}})]^{2}$ $F_{m}(\overrightarrow{x})=F_{m-1}(\overrightarrow{x})+\nu\rho_{m}B_{m}(\overrightarrow{x})$ 
end
</div>

## 3.3. Interpretation

Parametric techniques often have the advantage that a useful interpretation can be given to the model parameters, e.g., in linear regression the model parameters can be interpreted as the weights of the item characteristics. Although not parametric, regression trees are also highly interpretable and can be written as an equivalent set of if– then rules. Boosted trees lack both these appealing properties. Fortunately, at least to some degree boosted models can be interpreted by using relative importance $p l o t s . ^ { 2 }$

Relative importance plots visualize how important the various independent variables are relative to one another in predicting the dependent variable. Relative importance plots were developed for trees by Breiman et al. [8], but they are easily generalizable to an ensemble of trees. For a single CART model, the following formula measures the importance of variable x<sub>j</sub>:

$$
\hat {I} _ {j} ^ {2} (B) = \sum_ {n = 1} ^ {K - 1} \hat {i} _ {n} ^ {2} \chi \big (v _ {n} = x _ {j} \big).
$$

Here the summation is over the $K - 1$ non-terminal nodes in tree B having K terminal nodes and $\times 0$ denotes the indicator function. $\nu _ { n }$ is the split variable of node n. The factor $\hat { i } _ { n } ^ { 2 }$ measures the improvement in squared error as a result of the split in node $n ,$ and can be computed as follows:

$$
\hat {i} _ {n} ^ {2} = \frac {w _ {\mathrm{l}} w _ {\mathrm{r}}}{w _ {\mathrm{l}} + w _ {\mathrm{r}}} (\overline {{y}} _ {l} - \overline {{\mathbf {y}}} _ {r}) ^ {2}.
$$

Here $w _ { 1 }$ and $w _ { \mathrm { r } }$ are the probabilities an instance turns to the left or right child node of node $n , { \bar { y _ { 1 } } }$ and $\overline { { y } } _ { \mathrm { r } }$ are the mean target values for both children. Both the probabilities and the means are computed on the training set and saved in the CART model.

To compute the $\hat { I } _ { j } ^ { 2 , } \mathrm { \Phi } _ { \mathrm { S } }$ of a boosting model it is sufficient to average the $\hat { I } _ { j } ^ { 2 , } \mathrm { \bf s }$ of the base learners:

$$
\hat {I} _ {j} ^ {2} = \frac {1}{M} \sum_ {m = 1} ^ {M} \hat {I} _ {j} ^ {2} (T _ {m}).
$$

A variable $x _ { j }$ gets a high importance $I _ { j } ^ { 2 }$ when it is used in many splits, but more importantly when it is used in splits that divide the data in two almost equally large parts with a large difference in mean target value, thus contributing a lot to the total error reduction.

Finally, the variable $x _ { j }$ with the highest importance gets a relative importance index of RI = 100 and the other indices are adjusted to this:

$$
\mathrm{RI} _ {j} = \frac {\hat {I} _ {j} ^ {2}}{\hat {I} _ {\max} ^ {2}} 1 0 0.
$$

We will use relative importance plots below in Section 4 to identify the most important terms that influence prices in all four data sets.

## 4. Experiments and results

We experimented with our price prediction system using the data sets mentioned in Section 2. The data sets were randomly partitioned into a training set (80%) and a test set (20%). We repeated such splits 3 times for each data set, and built separate models on each training set.

The low number of repetitions, 3, is caused by the computational requirements for each experiment: Each run requires several hours of CPU time. The exact amount of time required varies with the number of auctions in the data set, the dictionary size, and the number of boosting iterations required. However, training the prediction module can be done off-line. Using the trained module for predictions is then only a matter of milliseconds.

Table 2  
Parameter settings in the performed experiments

<table><tr><td></td><td>Nike</td><td>Canon</td><td>Headset</td><td>30G iPod</td></tr><tr><td>Training set size</td><td>4437</td><td>3683</td><td>3089</td><td>4582</td></tr><tr><td>Test set size</td><td>1109</td><td>920</td><td>772</td><td>1145</td></tr><tr><td>Number of repetitions</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td> $C_p$ </td><td>0.0001</td><td>0.0005</td><td>0.0001</td><td>0.0001</td></tr><tr><td>Maxdepth</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Avg  $M$ </td><td>2538</td><td>609</td><td>632</td><td>1346</td></tr><tr><td> $v$ </td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td></tr></table>

M refers to the number of boosting iterations.

For our experiments, we used the decision tree implementation rpart [29] available in the statistical computing environment R [23] as a base learner. This implementation uses several parameters. The first parameter is a regularization parameter cp that helps control the size of the trees. Any split that does not decrease the overall lack of fit by a factor of $c p$ is not attempted by rpart. This parameter was set to 0.0005 for the Canon data set and 0.0001 for the other data sets. The second parameter is the maxdepth parameter which was set to 2. Although trees of depth 2 are unable to model complex functions, an ensemble of such trees is a very flexible model.

We implemented the LS\_Boost algorithm ourselves in R. The learning rate parameter ν was set to 0.1. The boosting algorithm was run until it became impossible to build an individual decision tree $B _ { m }$ other than a single root node. Thus, we did not use a pre-determined number of iterations M.

As a benchmark model, we used the most naive model possible: predicting the mean of the sales price in the training data per category. The outliers that were discarded from the data set were not included when computing the mean sales price.

To evaluate our models we use the error measures Mean Absolute Error (MAE) and Mean Relative Error (MRE):

$$
\mathrm{MAE} = \frac {1}{N} \sum_ {i = 1} ^ {N} | \text { Predicted   price } _ {i} - \text { Observed   price } _ {i} |,\tag{2}
$$

$$
\mathrm{MRE} = \frac {1}{N} \sum_ {i = 1} ^ {N} \frac {\left| \text { Predicted   price } _ {i} - \text { Observed   price } _ {i} \right|}{\text { Observed   price } _ {i}}.\tag{3}
$$

Table 3  
Average/minimal/maximal MAE and MRE, averaged over the three repetitions

<table><tr><td rowspan="2"></td><td colspan="2">Boosting</td><td colspan="2">Naïve</td></tr><tr><td>MAE</td><td>MRE</td><td>MAE</td><td>MRE</td></tr><tr><td>Nike</td><td>14.18/13.69/14.90</td><td>0.343/0.32/0.38</td><td>22.1/21.74/22.71</td><td>0.55/0.52/0.58</td></tr><tr><td>Canon</td><td>71.99/69.62/74.46</td><td>0.585/0.58/0.59</td><td>165.69/163.22/170.02</td><td>1.2/1.18/1.25</td></tr><tr><td>Headset</td><td>1.42/0/11.96</td><td>0.12/0/1.25</td><td>3.62/0.04/12.59</td><td>0.3/0/1.49</td></tr><tr><td>30G iPod</td><td>15.33/0.02/139.69</td><td>0.1/0/1.09</td><td>22.87/0.06/94.77</td><td>0.15/0/1.18</td></tr></table>

All errors are test set errors.

The MAE on the test set can be interpreted as the expected absolute error of the predictions with respect to the true values. The MRE is the expected proportional error — multiplying it by 100 gives the expected deviation of the predicted price from the actual price as a percentage (Table 2).

The experiments and the obtained results are summarized in Table 3. The errors reported in this table are test set errors. The reported errors clearly show that our system based on boosting outperforms the naive model of predicting the category mean price: for the Canon data set the MAE, or expected absolute error, is reduced from \$165 to \$72. Thus, the average absolute deviation from the final auction price is considerably smaller for our method than for the category mean. For the Nike data set, the MAE is reduced from \$22 to \$14. Similar reductions are achieved for the Headset (\$3.62 to \$1.42) and iPod (\$22.87 to \$15.33) data sets.

![](/api/attachments/YFVGSB2P/fulltext/images/d52d28cf4dc780563b117352b784776eeeb79e8981bb5ef85497d9d518b38ddc.jpg)

![](/api/attachments/YFVGSB2P/fulltext/images/8183ccc966033699489fa8a722707576b2dd9da27462b206d23168b4f816ca1b.jpg)

The reductions for the MRE, the proportional deviation from the final auction price, are also substantial. However, we see that for the data sets containing the heterogeneous products, the MRE values reported are relatively high: 0.58 for Canon and 0.34 for Nike. For the Headset and iPod data sets, which are more homogeneous, the relative errors are smaller: 0.12 and 0.1. These smaller errors are likely to be caused by the fact that fewer auctions are ‘used’ for creating a product classification, and thus within a product category more data are available.

It is interesting to consider the cumulative distribution of the relative errors. These are shown in Fig. 6. These graphs reveal that boosting predicts 57% of the Nikeauctions and 59% of the Canon auctions within a 20% range of the final auction price. For the iPod and headset auctions, these numbers are 89% and 83%. For the naive method, these numbers are much lower: 33% and 24% for

![](/api/attachments/YFVGSB2P/fulltext/images/fbfea2b49cd9c78141fd48a21bd7ff75845f988f553c0f87b79df7b84a477fe2.jpg)

![](/api/attachments/YFVGSB2P/fulltext/images/e17117a2613da566e0e9940ca91ad32e6cca1f03dd64c3ac4930828a25e5faed.jpg)  
Fig. 6. Distribution of the errors in the data sets. The horizontal axis values for the relative error, the vertical axis shows the percentage of auctions in the test set predicted with a relative error below that value.

Nike and Canon respectively. For iPod and headset we have 81% and 27%. Especially for the headset data set, the difference is striking. So, although the average MRE values are sometimes high, a substantial number of auctions is predicted with reasonable accuracy.

![](/api/attachments/YFVGSB2P/fulltext/images/ab64e8a5ce128f03fdd350bdd2c2493631b33f4562d7e047db380e575f3e1d88.jpg)

![](/api/attachments/YFVGSB2P/fulltext/images/3ac5d84e1225ab962c61a38659876ad6d84dbdb74d1b477ab566bab199d35cd2.jpg)  
Fig. 7. Relative importance plots showing the most influential predictors for each data set. For each data set, the bottom graph contrasts the influence of the dictionary words with feedback and number of pictures, the top graphs give the relative importance of the most important terms in the dictionary.

As was explained in Section 3, relative importance plots visualize the importance of the indicators relative to one-another. Fig. 7 shows these relative importance plots for all four data sets. The importance in these plots are averaged over the three experiments we performed.

For each data set, the bottom graph shows the importance of the total item description (Dict.) versus the number of pictures (PICS) and the seller feedback rating (FB). It is clear that the item description is by far the most important predictor in all data sets. PICS seems to come second and FB last. These are interesting observations, especially so since many papers stress the importance of FB for the auction outcome [4,24]. Interestingly, for Canon the FB and PICS features seem to be of negligible importance, whereas Headset is the only data set in which FB is more important than PICS.

The top graphs show the relative importance of the 25 most influential indicators. The most important terms for the Canon data set were mostly technical terms such as ef (extended focus), CMOS (a sensor which helps increase the quality of picture) and powershot. There are also important terms which identify models for example EOS and XT (Rebel XT series). The relative importance plot for the Nike data set shows a broad variety of split variables. Although a split term identifying one of the existing Nike shoe models (jordan) is the most important, other terms like deadstock and authentic, are also influential.

For the more homogeneous Headset and iPod data sets, we find many terms describing the item's condition (e.g., scratch, brand, broken). There are also terms describing conditions of sale (e.g., payment, dispatch, seal). Interestingly, there are many terms related to the technical characteristics of these items, such as mute, headset, video and firewire. Seemingly, it pays to emphasize an item's capabilities even in a homogeneous product group.

## 5. Summary, conclusions & discussion

In this article we present a decision support system for predicting prices for online auctions. The predictions are based on a boosting model, which uses closed auctions of some product to predict prices for current auctions of the same product. The system uses the seller's feedback rating, the number of pictures on the web page and the seller's description of the item. The contribution of this study is twofold: it is the first study that uses the item description and number of pictures in the prediction of eBay end prices, and it is the first study that uses boosting to this end. Boosting is based on combining decision trees, and therefore it is suitable for identifying important terms from a large term collection.

Gregg and Walczak have introduced an Auction Advisor system to support decisions for buyers and sellers [15]. Their support system summarizes several statistics about currently active and closed auctions. Our price prediction gives the user additional information. For example, it would enable the Auction Advisor to leave out those items, for which the current bid exceeds the predicted end price.

We tested our price prediction model in a series of experiments. Interpretation yielded some interesting insights. Based upon the split variables used, the prediction model is able to identify influential terms in the description. For heterogeneous data sets, these terms often relate to product subclasses and technical properties of the items and they are found without input of expert knowledge. For homogeneous data sets, technical terms are also important predictors, but terms describing the conditions of sale are important as well. In the current system we are unable to identify the directions of these influences, but the system could be easily extended with this functionality.

In our experiments, the prediction model was capable of predicting 20–40% of the auctions within a 5% range of the actual selling price. On homogeneous data we achieve a higher accuracy than on heterogeneous data. We remark that it may not be possible to achieve a much lower error. There are various reasons, such as bidding wars and sniping, why an item may be sold below or above its actual market value in practice. We can never model these effects fully, merely based on features that are available at auction start-time — part of the variance in the observed prices is likely to be ‘intrinsic noise’. Nevertheless, it would be an attractive feature if we were to extend our system so that it would recognize when a prediction is likely to be accurate, and when it is likely to have a large error. This functionality could be added by using a bootstrap procedure, but we leave this for further research.

Although this may change in the future, the computational requirements of the currently implemented system has rendered it impractical to train a new prediction model for individual end users on their own PC's. However, since generating a new prediction with a trained model is only a matter of milliseconds, our system could be deployed as an Internet service that is accessible to end users.

In such a setup, the maintainer of the web-service is responsible for gathering data and ‘training’ models, while allocating sufficient resources for this task. The gathering of data can largely be automated: per desired category the relevant auction IDs can be found using Harvex or eBay's search mechanism. These auctions are then automatically downloaded, a dictionary is created, and the auctions are cast into vector–space format. Building the predictive module is then started automatically. The whole process does not require much user involvement, except maybe if one wants to optimize over the system parameters such as f<sub>l</sub> (lower bound for word occurrence) or the parameters used in the boosting algorithm, but it is questionable whether this would be very useful.

Sellers can then use this service to submit draft versions of eBay auction pages. The system would then give them an indication of a reasonable sales price and hints on terms to include in their ad text. Buyers can use the service to check prices of items they have interest in and to locate bargains. Our system could thus support both buyers and sellers on eBay.

## Acknowledgments

We thank the anonymous referees and Nees Jan van Eck for their helpful suggestions.

## References

[1] Yacine Atif, Building trust in e-commerce, IEEE Internet Computing 6 (1) (2002) 18–24 Jan/Feb.

[2] S. Ba, Establishing online trust through a community responsibility system, Decision Support Systems 31 (3) (August 2001) 323–336.

[3] S. Ba, A.B. Whinston, H. Zhang, Building trust in online auction markets through an economic incentive mechanism, Decision Support Systems 35 (3) (June 2003) 273–286.

[4] Sulin Ba, Paul Pavlou, Evidence of the effect of trust building technology in electronic markets: price premiums and buyer behavior, MIS Quarterly 26 (3) (2002) 243–268.

[5] P. Bajari, A. Hortacsu, Economic insights from internet auctions, Journal of Economic Literature 42 (2) (2004) 457–486.

[6] L. Breiman, Bagging predictors, Machine Learning 24 (1996) 123–140.

[7] L. Breiman, Arcing classifiers, Annals of Statistics 26 (2) (1998) 801–824.

[8] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classification and Regression Trees, 2nd Edition, Chapman & Hall, NY, 1996.

[9] D. Bryan, D. Lucking-Reiley, N. Prasad, D. Reeves, Pennies from eBay: The Determinants of Price in Online Auctions. Working Papers 0003, Department of Economics, Vanderbilt University, November 1999 (May 2006 Version).

[10] eBay- Investor Relations. Web-site, 2006. http://investor.ebay com/. Accessed on 6/20/2006.

[11] Y. Freund, R.E. Schapire, Experiments with a new Boosting Algorithm, in: L. Saitta (Ed.), Proceedings of the 13th International Conference on Machine Learning, pages, Morgan Kaufmann, San Francisco, 1996, pp. 148–156.

[12] Y. Freund, R.E. Schapire, A decision-theoretic generalization of on-line learning and an application to boosting, Journal of Computer and System Sciences 55 (1) (1997) 119–139.

[13] J.H. Friedman, Greedy function approximation: a gradient boosting machine, Annals of Statistics 29 (5) (2001) 1189–1232 October.

[14] R. Ghani, H. Simmons, Predicting the end-price of online auctions, Proceedings of International Workshop on Data Mining and Adaptive Modelling Methods for Economics and Manage-

ment held in conjunction with the 15th European Conference on Machine Learning (ECML/PKDDD 2004), 2004, (Pisa, Italy/).

[15] D.G. Gregg, S. Walczak, Auction advisor: an agent-based online auction decision Support System, Decision Support Systems 41 (2) (2006) 449–471.

[16] HarvEX / Turbo Sniper software. Web-site, 2007. http://www. xellsoft.com/HarvEX.html. Accessed on 6/25/2007.

[17] Andrew J.I. Jones, On the concept of trust, Decision Support Systems 33 (3) (2002) 225–232 July.

[18] Vijay Krishna, Auction Theory, Academic Press/Elsevier Science0-12-426297-X, 2002.

[19] A. McCallum, K. Nigam, A comparison of event models for naive Bayes text classification, Proceedings of AAAI-98, Workshop on Learning for Text Categorization, 1998.

[20] Tetsuya Nasukawa, Tohru Nagano, Text analysis and knowledge mining system, IBM Systems Journal 40 (4) (2001) 967–984.

[21] Judith S. Olson, Gary M. Olson, i2i trust in e-commerce, Communications of the ACM 43 (December 2000) 41–44.

[22] M.F. Porter, An algorithm for suffix stripping, Program 14 (3) (1980) 130–137.

[23] R Development Core Team, R: a language and environment for statistical computing. R Foundation for Statistical Computing, 3-900051-07-0, 2005 (Vienna, Austria) http://www.R-project.org.

[24] P. Resnick, R. Zeckhauser, J. Swanson, K. Lockwood, The value of reputation on eBay: a controlled experiment, Experimental Economics 9 (2) (2006) 79–101 June.

[25] D. Brian Ripley, Pattern Recognition and Neural Networks, Cambridge University Press, Cambridge, 1996.

[26] A.E. Roth, A. Ockenfels, Last-minute bidding and the rules for ending second-price auctions: evidence from eBay and Amazon auctions on the internet, American Economic Review 92 (4) (2002) 1093–1103 September.

[27] G. Salton, Automatic Text Processing: The Transformation Analysis and Retrieval of Information by Computer, Addison– Wesley0201122278, 1989.

[28] S. Slattery, M. Craven, Combining statistical and relational methods for learning in hypertext domains, in: David Page (Ed.), Proceedings of ILP-98, 8th International Conference on Inductive Logic Programming, Springer Verlag, Madison, US, 1998, pp. 38–52, (Heidelberg, DE. Published in the “Lecture Notes in Computer Science” series, number 1446).

[29] T.M. Therneau, B. Atkinson, B. Ripley. rpart: Recursive Partitioning, 2005. R package version 3.1–22, S-PLUS 6.x original at http://www.mayo.edu/hsr/Sfunc.html.

[30] Shanshan Wang, Wolfgang Jank, Galit Shmueli. Explaining and forecasting online auction prices and their dynamics using functional data analysis. Journal of Business and Economic Statistics, in press.

[31] S.M. Weiss, C. Apté, F.J. Damerau, D.E. Johnson, F.J. Oles, T. Goetz, T. Hampp, Maximizing text-mining performance, IEEE Intelligent Systems 14 (4) (1999) 63–69.

![](/api/attachments/YFVGSB2P/fulltext/images/4479ee54931ecff0a7b2d17ee31e933fd5b41c1f244da1a69712dbcfe0ac612f.jpg)  
Dennis van Heijst has been a masteral student of Informatics and Economics at Erasmus University. He currently works as an IT-auditor at Ernst and Young.

![](/api/attachments/YFVGSB2P/fulltext/images/e8a3b9fef37b5d2286eed6afdc2a35bc2cf1ade38a589280b5e71e891a603665.jpg)  
Decision Support Systems. ems.

Rob Potharst received his MSc degree in Statistics and Operations Research from the University of Amsterdam. He earned a PhD at Erasmus University Rotterdam with a thesis on decision trees and neural networks. While teaching at the Econometric Institute of the latter university, he specializes in Computational Intelligence techniques in Marketing. Recently, he has published papers in the Intelligent Decision Analysis journal and in  
![](/api/attachments/YFVGSB2P/fulltext/images/e1dc7b76e4ffb0c36ba8bf96d26b61fb967a2589a3e6674b9d64f38debf82b73.jpg)  
Michiel van Wezel works as an assistant professor at the Econometric Institute of the Erasmus School of Economics. His areas of interest are data mining and e-commerce. Michiel received a PhD in computer science from Leiden University and a MSc in computer science from Utrecht University.
