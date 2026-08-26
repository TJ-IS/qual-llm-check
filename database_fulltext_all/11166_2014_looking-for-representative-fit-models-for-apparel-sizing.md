---
otero_id: 11166
otero_key: "5E8J6JAM"
title: "Looking for representative fit models for apparel sizing"
authors: "G. Vinué; T. León; S. Alemany; G. Ayala"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.07.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This paper is concerned with the generation of optimal <sup>fi</sup>t models for use in apparel design. Representative <sup>fi</sup>t models or prototypes are important for de<sup>fi</sup>ning a meaningful sizing system. However, there is no agreement among apparel manufacturers and each one has their own prototypes and size charts i.e. there is a lack of standard sizes in garments from different apparel manufacturers. We propose two algorithms based on a new hierarchical partitioning around medoids clustering method origi nally developed for gene expression data. We are concerned with a different application; therefore, the dissimilarity between the objects has to be different and must be designed to deal with anthropometric features. Furthermore, one of the algorithms incorporates a different rule to split the clusters, which, in our case, provides better results. Our procedures not only make it possible to obtain optimal prototypes, but also to detect outliers. These outliers should be removed before de<sup>fi</sup>ning prototypes so that the companies' market share can be optimized. All the analyses are performed using the anthropometric database obtained from a survey of the Spanish female population.

# Looking for representative <sup>fi</sup>t models for apparel sizing

G. Vinué <sup>a,</sup>⁎, T. León <sup>a</sup>, S. Alemany <sup>b</sup>, G. Ayala <sup>a</sup>

<sup>a</sup> Department of Statistics and O.R., Avda, Vicent Andrés Estellés, 1. 46100-Burjasot, University of Valencia, Valencia, Spain <sup>b</sup> Biomechanics Institute of Valencia, Universidad Politécnica de Valencia, Valencia, Spain

## a r t i c l e i n f o

Article history: Received 15 February 2013 Received in revised form 23 July 2013 Accepted 23 July 2013 Available online 1 August 2013

Keywords: HIPAM Hierarchical tree Partitioning around medoids Fit models Mean split silhouette INCA statistic

## a b s t r a c t

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Clothing <sup>fi</sup>t is the major aim in the design and manufacture of clothing to ensure user comfort and better appearance. It is a complex issue in<sup>fl</sup>uenced by the customer's anthropometry, fashion and social trends [16,30]. The development of ready-to-wear (RTW) clothes involves estimating the body measurements of the target population to provide patterns based on a basic size, sizing charts and grading parameters. However, most apparel manufacturers create and adjust their own size charts. They usually use sales studies, returned merchandising reports and small customer surveys and, based on this information, create their size charts i.e. they use a trial and error methodology [12]. This methodology cannot be used when a company explores a (completely) new market. Additionally, each company has its own sizing system, so garments with the same size-label <sup>fi</sup>t differently. This results in a poor <sup>fi</sup>t, unsold garments and a less competitive business. Many people return bought clothes because they are not satis<sup>fi</sup>ed [2,10]. A major challenge is to develop an ef<sup>fi</sup>cient method of sales forecasting to predict the future demand of a product and to avoid unsold stock [17,21,44,45]. Apparel <sup>fi</sup>rms would gain a competitive advantage if they could enhance their organizational capabilities. The use of new information technology (IT) should play a critical role to that end [32]. In particular, Radio-Frequency IDenti<sup>fi</sup>cation (RFID) allows <sup>fi</sup>rms to track and trace products and could minimize inventory shrinkage [56].

In customer surveys, certain models, called the <sup>fi</sup>t model and/or prototypes, represent the basic size [3]. The <sup>fi</sup>t model represents the body dimensions selected by each company to de<sup>fi</sup>ne the proportional relationships needed to achieve the <sup>fi</sup>t the company has determined [52]. Most apparel companies develop their own sizing systems by using a different <sup>fi</sup>t model which covers their whole target market [51]. In other words, apparel companies only aim to <sup>fi</sup>t one body type, generating base patterns and grade rules from the measurements and proportions of their <sup>fi</sup>t model [5]. However, there might be many body types within a target market and this single idealized <sup>fi</sup>t model may not adequately describe the various shapes of the other body types within each size [4, page 133]. Furthermore, there is little information to help choose a <sup>fi</sup>t model whose body size and shape are consistent with the target market [5]. Our paper proposes a methodology to identify representative <sup>fi</sup>t models. A good <sup>fi</sup>t model is the basis for de<sup>fi</sup>ning an accurate sizing system.

The use of anthropometric databases to enhance apparel <sup>fi</sup>tting has been mainly aimed at de<sup>fi</sup>ning new sizing systems. Three types of approaches can be distinguished for creating a sizing system: traditional step-wise sizing, multivariate approaches and optimization methods. Traditional methods select two independent dimensions (named key or control and secondary dimension, respectively) and choose an inter-size interval to determine the optimal number of sizes that accommodates the highest percentage of population. This approach is too simplistic because it is not possible to cover the different body types of the population, perhaps due to the fact that other relevant anthropometric dimensions are not considered.

![](/api/attachments/5E8J6JAM/fulltext/images/5785c6924e8de3adcd6807c164753dd6f2b8f453e56736cd9a4f3e4e9444d2cd.jpg)  
Fig. 1. Marginal dissimilarity proposed in [35].

Several multivariate methodologies have been proposed for de<sup>fi</sup>ning a sizing system. Principal component analysis (PCA) has been widely used as a dimensionality reduction technique using the <sup>fi</sup>rst two principal components to generate the bivariate distribution in which to de<sup>fi</sup>ne the sizing chart [11,22–24,33,41]. Partitioning clustering methods, especially the k-means algorithm, have been used to classify the target population into different morphologies by using every anthropometric measurement available as an input [13,37,55]. Other alternatives combining data mining and decision trees have also been proposed [7,25].

The <sup>fi</sup>rst reference using an optimization was [46], where an integer programming method was used to determine the number of sizes in order to optimize garment sales. A modi<sup>fi</sup>cation of Tryfos' proposal was introduced in [35], where the objective function is related with quality of <sup>fi</sup>t (instead of sales) and a nonlinear optimization technique was used.

Good accommodation percentages are achieved using multivariate techniques or optimization. However, it is dif<sup>fi</sup>cult to translate a selection method to the consumer using straightforward labeling.

None of the aforementioned approaches aims to identify <sup>fi</sup>t models. As far as we know, no statistical method has been developed with this goal in mind. On the other hand, body models as a representation of part of the population pose a classic problem in ergonomics for designing products and working environments. Percentiles have been widely used in this context. However, these quantities are not additive and provide a univariate accommodation [36,39,54]. Nowadays, the most commonly used method is based on PCA: <sup>fi</sup>rst, only the <sup>fi</sup>rst two principal components are selected. Then, a normality ellipse (or circle if the data are standardized) covering a given percentage of the population (usually 95%) is calculated. Finally, eight subjects are identi<sup>fi</sup>ed at the intersections with the major axes and at the so-called octant points. They are estimates of extreme patterns of the data [8,19,20,26,40,54]. The limitations of this procedure are described in [18]. We are faced with the usual drawback of using PCA and the variation not considered may correspond to people with a dif<sup>fi</sup>cult accommodation [18]. Recently, a new alternative based on archetypal analysis has been proposed [14]. Nevertheless, all these approaches used in ergonomics are not useful for obtaining <sup>fi</sup>t models because they look for boundary cases and the <sup>fi</sup>t models must be central individuals.

Table 2  
Summary statistics for the variables considered

<table><tr><td>Measurement (cm)</td><td>Minimum</td><td>First quantile</td><td>Median</td><td>Mean</td><td>Third quantile</td><td>Maximum</td></tr><tr><td>Neck to ground length</td><td>116.4</td><td>132.9</td><td>136.8</td><td>137</td><td>140.8</td><td>161.9</td></tr><tr><td>Bust circumference</td><td>73</td><td>87.4</td><td>93.3</td><td>95.02</td><td>100.7</td><td>145.7</td></tr><tr><td>Chest circumference</td><td>45.91</td><td>90.78</td><td>96.37</td><td>97.92</td><td>103.7</td><td>150.30</td></tr><tr><td>Waist circumference</td><td>58.60</td><td>75.6</td><td>83.10</td><td>84.98</td><td>92.40</td><td>167.6</td></tr><tr><td>Hip circumference</td><td>72.8</td><td>98.3</td><td>103.3</td><td>104.9</td><td>109.9</td><td>170.8</td></tr></table>

The <sup>fi</sup>nal evaluation of <sup>fi</sup>t in the apparel development process needs models representing the target population to test every new design before the production phase. These models are the dress form, the human <sup>fi</sup>t model and the virtual <sup>fi</sup>t model. Of these three, the role of the human <sup>fi</sup>t model is the most important. Companies aim to improve the quality of <sup>fi</sup>t by scanning their <sup>fi</sup>t models and deriving dress forms from those scans [4,43]. The current practice in apparel <sup>fi</sup>t analysis is based on using expert panels [6]. An expert panel is an experienced work team that judges the garment <sup>fi</sup>t. As far as the apparel industry is concerned, <sup>fi</sup>t analysis is carried out using a live <sup>fi</sup>t model.

Research has recently been carried out to check the reliability of using virtual 3D scan models instead of <sup>fi</sup>t models to improve garment <sup>fi</sup>t [6,9]. These virtual 3D models come from scanned live <sup>fi</sup>t models. They can be used in a similar way to <sup>fi</sup>t models but have certain advantages. Emerging technology for body scanning offers many bene<sup>fi</sup>ts in different areas of apparel design and manufacturing [6,42]. Indeed, the tailoring procedure followed by designers requires the scanning of real persons to generate 3D clothes from 2D patterns [34,48]. In this way, a representative <sup>fi</sup>t model of the target population, whether a live <sup>fi</sup>t model or a 3D scan model, is critical for improving the garment <sup>fi</sup>t. The major aim of <sup>fi</sup>t analysis is to de<sup>fi</sup>ne <sup>fi</sup>t models for different sizes [9].

In this article we propose a new approach for de<sup>fi</sup>ning optimal prototypes for apparel design. We introduce two classi<sup>fi</sup>cation algorithms based on the hierarchical partitioning around medoids (HIPAM) clustering algorithm [49], modi<sup>fi</sup>ed to deal with anthropometric data. The outputs of both algorithms include a set of representative subjects or medoids taken from the original data set which constitute our prototypes. The HIPAM algorithm is a divisive hierarchical clustering method based on the PAM algorithm. Hierarchical clustering methods seek to build a hierarchy of clusters. In particular, divisive methods begin with one cluster and split this group recursively. Usually, but not always, in the last step there are as many groups as observations. Partitioning clustering methods classify the objects into k clusters, where k is usually <sup>fi</sup>xed in advance (k can also be data-adaptively selected). The Partitioning Around Medoids (PAM) algorithm [29] is a robust partitioning algorithm which seeks to <sup>fi</sup>nd k representative subjects (also known as medoids) from the data set in such a way that the sum of the within-cluster dissimilarities is minimized.

HIPAM starts with one large cluster and, at each level, a given cluster is partitioned using PAM. It splits the parent cluster at a given node of the classi<sup>fi</sup>cation tree by taking into account a cluster structure measure. The number of child clusters is obtained by maximizing the silhouette width (ASW) [29]. Different dissimilarity measures can be used. We will use a dissimilarity measure, hereafter referred to as $d _ { M O } ,$ which is a modi<sup>fi</sup>ed version of a previous dissimilarity proposed in [35]. Unlike the original HIPAM, we aggregate the marginal dissimilarities (corresponding to each feature) using an Ordered Weighted Averaging (OWA) operator [53] instead of the sum of their squares.

Table 1  
Aggregation weights associated with the anthropometric variables

<table><tr><td>Chest circumference</td><td>Neck to ground length</td><td>Waist circumference</td><td>Hip circumference</td><td>Bust circumference</td></tr><tr><td>0.42805</td><td>0.24580</td><td>0.12430</td><td>0.10180</td><td>0.10005</td></tr></table>

Table 4  
Table 3  
Counts and number of clusters with more than two women obtained using the algorithms $H I P A M _ { M O }$ and $H I P A M _ { I M O } .$

<table><tr><td>Bust class</td><td>[78,82]</td><td>[82,86]</td><td>[86,90]</td><td>[90,94]</td><td>[94,98]</td><td>[98,102]</td><td>[102,107]</td><td>[107,113]</td></tr><tr><td>Count</td><td>287</td><td>732</td><td>1028</td><td>952</td><td>818</td><td>633</td><td>547</td><td>356</td></tr><tr><td>Num. medoids  $HIPAM_{MO}$ </td><td>5</td><td>3</td><td>10</td><td>5</td><td>4</td><td>4</td><td>9</td><td>2</td></tr><tr><td>Num. medoids  $HIPAM_{IMO}$ </td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>5</td></tr></table>

We propose two different algorithms. The <sup>fi</sup>rst one, $H I P A M _ { M O } ,$ is a HIPAM that uses the dissimilarity $d _ { M O } .$ The second algorithm, $H I P A M _ { I M O } ,$ is a HIPAM algorithm that uses $d _ { M O }$ and the INCA (index number clusters atypical) statistic criterion [28] to decide the number of child clusters and as a stopping rule.

Our approach detects outliers. Our target population is not the whole population but the so-called standard population. Usually, the industry leaves out non-typical individuals i.e. the outliers, in order to optimize market share. Several procedures have previously been proposed in the garment literature to identify outliers [23,33]. For instance, in [23] subjects whose heights and weights deviated by three standard deviations from the mean were regarded as abnormal data. However, there is a lack of consistency in explaining how the abnormal data were removed. Many papers can be found in which outlier detection is not detailed, for instance [7,25]. Outlier detection in garment design should be emphasized.

We will analyze a data set obtained from the anthropometric study of the Spanish female population commissioned by the Spanish Ministry of Health in 2006 [1]. Supplementary material for our study can be found at http://www.uv.es/vivigui/research.html.

Functions of the smida package [49,50] written in the R language [38] have been used for the implementation of our algorithms. The smida package can be downloaded from the authors website: http:// www.stats.gla.ac.uk/\~microarray/book/smida.html.

Section 2 provides the background and Section 3 contains our approach. Section 4 shows the apparel design application. The data set is described in Section 4.1 and the experimental results are given in Section 4.2. Section 5 ends the paper with some conclusions.

## 2. Background

Let us remember some de<sup>fi</sup>nitions that will be needed later. The dissimilarity measure d was proposed in [35], while the INCA statistic was de<sup>fi</sup>ned in [28]. For each person we have a feature p-vector $\boldsymbol { x } = ( x _ { 1 } , . . . , x _ { p } )$ corresponding to his/her body measurements.

## 2.1. The dissimilarity measure

We need a dissimilarity measure in order to apply the HIPAM algorithm. In our application, we have to measure the mis<sup>fi</sup>t between an individual and the prototype. The dissimilarity measure $d _ { M O }$ was introduced in [27] by modifying the original proposal given in [35]. The marginal dissimilarity of the i-th feature (or component) between individuals x and y was de<sup>fi</sup>ned in [35] as

$$
d _ {i} (x, y) = \left\{ \begin{array}{l l} a _ {i} ^ {l} \left(l n (y _ {i}) - b _ {i} ^ {l} - l n (x _ {i})\right), & \text { if } l n (x _ {i}) <   l n (y _ {i}) - b _ {i} ^ {l} \\ 0, & \text { if } l n (y _ {i}) - b _ {i} ^ {l} <   l n (x _ {i}) <   l n (y _ {i}) + b _ {i} ^ {h} \\ a _ {i} ^ {h} \left(l n (x _ {i}) - b _ {i} ^ {h} - l n (y x _ {i})\right), & \text { if } l n (x _ {i}) > l n (y _ {i}) + b _ {i} ^ {h} \end{array} \right.\tag{1}
$$

for constants a $, b ^ { l } , a ^ { h }$ and $b ^ { h } . ~ b _ { i }$ corresponds to the range in which there is a perfect <sup>fi</sup>t and $a _ { i }$ gives us the mis<sup>fi</sup>t rate. This distance function is illustrated in Fig. 1.

A global dissimilarity was proposed in [35] as the sum of the squared marginal dissimilarities i.e.

$$
d (x, y) = \sum_ {i = 1} ^ {p} \left(d _ {i} (x _ {i}, y _ {i})\right) ^ {2}\tag{2}
$$

It seems natural to consider other possible dissimilarity measures as

$$
d (x, y) = \max _ {i = 1} d _ {i} (x _ {i}, y _ {i}).\tag{3}
$$

The dissimilarity measure given in Eq. (3) focuses on the worse <sup>fi</sup>t. The two examples just proposed are aggregations of the marginal dissimilarities $d _ { i } ( x _ { i } , y _ { i } ) ( { \mathrm { w i t h } } i = 1 , . . . , p )$ . Many possible aggregation operators could be considered. An Ordered Weighted Averaging (OWA) aggregating operator will be our choice and it will be remembered. Let $a _ { 1 } , . . . , a _ { p }$ be the values to be aggregated. The OWA operators [53] provide a parameterized family of mean type aggregation operators that includes their minimum, maximum and average. As an important feature of these operators, the arguments to be aggregated are ordered according to their value, and the aggregation weights are associated with a particular position in this re-ordering instead of being associated with a speci<sup>fi</sup>c argument. From the original $a _ { 1 } , . . . , a _ { p }$ we consider the ordered values $a _ { ( 1 ) } \geq \ldots \geq a _ { ( p ) }$ and, given the weights $w _ { 1 } , . . . , w _ { p } ,$ the OWA aggregated value is $\sum { \bf \Xi } _ { i } ^ { n } = { \bf \Xi } _ { 1 } w _ { i } a _ { i } .$ . A common method for determining the aggregation weights is to obtain the desired OWA operator under a given level of orness. The orness measure, introduced by Yager [53], characterizes the degree to which the aggregation is like a min or max operation. To be speci<sup>fi</sup>c, this value allows us to adjust the importance to be attached to the arguments, depending on their ranks:

$$
\operatorname{orness} (W) = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} (n - i) w _ {i}.\tag{4}
$$

We have used a simple procedure to generate the set of weights $W = ( w _ { 1 } , . . . , w _ { n } )$ originally proposed in [31]. They are obtained as a mixture of the binomial $B i ( n - 1 , p )$ and the discrete uniform probability distributions, that is to say, $w _ { i } = \lambda \pi _ { i } + ( 1 - \lambda ) / n$ , where $\pi _ { i }$ is the binomial probability for each $i = 0 , . . . , n - 1$ . If x and y are two feature vectors, then the dissimilarity measure used later will be denoted as $\delta ( x , y )$ i.e.

Size of the clusters with more than two women obtained by $H I P A M _ { M O }$ and $H I P A M _ { I M O } .$

<table><tr><td>Bust class Algorithm</td><td>[78,82]</td><td>[82,86]</td><td>[86,90]</td><td>[90,94]</td><td>[94,98]</td><td>[98,102]</td><td>[102,107]</td><td>[107,113]</td></tr><tr><td> $HIPAM_{MO}$ </td><td>88 65 25 67 42</td><td>201 304 227</td><td>309 94 70 94 71 113 191 27 27 24</td><td>318 277 114 160 83</td><td>280 282 83 173</td><td>163 181 170 119</td><td>141 31 19 39 65 20 99 53 72</td><td>202 154</td></tr><tr><td> $HIPAM_{IMO}$ </td><td>98 79 110</td><td>234 289 209</td><td>366 329 333</td><td>318 339 295</td><td>331 292 195</td><td>182 229 222</td><td>213 140 194</td><td>140 130 21 47 18</td></tr></table>

![](/api/attachments/5E8J6JAM/fulltext/images/7af4ca5ff5b13f5972fbe3345b4d491f3f75672af5505587d605b5b9e7ecdb18.jpg)

![](/api/attachments/5E8J6JAM/fulltext/images/d1ac77c19504066cf63c21d7219ee6de0c175fceb3f46894bb37cb02732b37f0.jpg)  
Fig. 2. Bust vs. hip in the medoids obtained using $H I P A M _ { M O }$ (left) and $H I P A M _ { I M O }$ (right).

$$
\delta (x, y) = \sum_ {i = 1} ^ {n} w _ {i} d _ {i} (x _ {i}, y _ {i}).
$$

The orness used is $0 . 7 .$ . This orness is close to 1 in order to highlight marginal mis<sup>fi</sup>t. Table 1 displays the aggregation weights associated with the variables in our database.

## 2.2. INCA statistic

Let us review a recent measure of cluster structure [28], the index number clusters atypical statistic (INCA). We have n points classi<sup>fi</sup>ed into k clusters $C _ { 1 } , . . . , C _ { k }$ of sizes $n _ { 1 } , . . . , n _ { k } .$ The observations in the i-th cluster can be considered as a random sample of a continuous random vector $Y _ { i \cdot }$ Given a new point $y _ { 0 } ,$ we have two possibilities: (i) it could be an element of one of the previously de<sup>fi</sup>ned clusters $C _ { j } , j = 1 , . . . , k ,$ or (ii) it is an outlier (with respect to the previous clusters) and it should be classi<sup>fi</sup>ed in a new cluster. If the point does not belong to a given cluster, then the new cluster would have as its center a convex combination of the previous centers i.e. the center of the new cluster would be $\sum { \ K } _ { i } ^ { k } { = } _ { 1 } { \alpha } _ { i } E ( Y _ { i } )$ , where the weights $\alpha _ { i }$ are determined by minimizing an objective function and $E ( Y _ { i } )$ denotes the expected value of $Y _ { i \cdot }$ Given the point $y _ { 0 } ,$ we evaluate the function

$$
W (y _ {0}) = \min _ {(\alpha_ {1}, \ldots , \alpha_ {k}): \sum_ {i = 1} ^ {k} \alpha_ {i} = 1} L (y _ {0}),\tag{5}
$$

![](/api/attachments/5E8J6JAM/fulltext/images/e66f85ccb74b75b198de314a7bc45151ed0d8cc3808a1070b136b831ecdd64f5.jpg)

where

$$
L \left(y _ {0}\right) = \sum_ {i = 1} ^ {k} \alpha_ {i} \phi_ {i} ^ {2} \left(y _ {0}\right) - \sum_ {1 \leq i <   j \leq k} \alpha_ {i} \alpha_ {j} \Delta_ {i j} ^ {2}\tag{6}
$$

being

$$
\phi_ {i} ^ {2} (y _ {0}) = \frac {1}{n _ {i}} \sum_ {l \in C _ {i}} \delta^ {2} (y _ {0}, y _ {l}) - V _ {\delta} (C _ {i}),\tag{7}
$$

$$
V _ {\delta} (C _ {i}) = \frac {1}{2 n _ {i} ^ {2}} \sum_ {l, m \in C _ {i}} \delta^ {2} (y _ {l}, y _ {m}),\tag{8}
$$

$$
\Delta_ {i j} ^ {2} = \frac {1}{n _ {i} n _ {i}} \sum_ {l \in C _ {i}, m \in C _ {j}} \delta^ {2} (y _ {l}, y _ {m}).\tag{9}
$$

Let us remove a particular $C _ { j } .$ Then for each y point of the data set, the value $W ( y )$ can be calculated with all groups except the j-th $C _ { j } ,$ and this value will be denoted as $W _ { C _ { i } } ( y ) . \mathrm { I f } W _ { C _ { i } } = m a x _ { z \not \in C _ { i } } W _ { C _ { i } } ( z )$ , then: (i) the y point of $C _ { j }$ is correctly classi<sup>fi</sup>ed in C if $W _ { C _ { i } } ( y ) { > } W _ { C _ { i } }$ and, (ii) it is not correctly classi<sup>fi</sup>ed in $C _ { j }$ if $W _ { C _ { j } } ( y ) { \le } \dot { W } _ { C _ { j } }$ . If N denotes the total number of units in $C _ { j }$ which are correctly classi<sup>fi</sup>ed, then the INCA index, $I N C A _ { k } ,$ is de<sup>fi</sup>ned as the probability of correctly classi<sup>fi</sup>ed individuals and is estimated by using

![](/api/attachments/5E8J6JAM/fulltext/images/dd7e99c36c6b9b7d04db6e4c692c038e305fdf8818c0729be319086b4a183bdd.jpg)  
Fig. 3. The <sup>fi</sup>rst two principal components of the medoids in the [86,90[ class obtained using both algorithms

Table 5  
Percentages of outliers in each class.

<table><tr><td>Bust class Algorithm</td><td>[74,78]</td><td>[86,90]</td><td>[102,107]</td><td>[113,119]</td><td>[119,125]</td><td>[125,131]</td></tr><tr><td> $HIPAM_{MO}$ </td><td>30%</td><td>0.77%</td><td>1.5%</td><td>6.5%</td><td>23%</td><td>78%</td></tr><tr><td> $HIPAM_{IMO}$ </td><td>17%</td><td>-</td><td>-</td><td>14%</td><td>9%</td><td>100%</td></tr></table>

$$
I N C A _ {k} = \frac {1}{k} \sum_ {j = 1} ^ {k} \frac {N _ {j}}{n _ {j}}\tag{10}
$$

It was proposed in [28] that k should be selected as the value of k preceding the <sup>fi</sup>rst largest slope decrease. If the $I N C A _ { k }$ are small for all $k ,$ then we have a single cluster.

## 3. Our algorithms

We propose two divisive algorithms. Their output is a classi<sup>fi</sup>cation tree, where each node corresponds to a cluster and the end nodes de<sup>fi</sup>ne the <sup>fi</sup>nal partition. The highest or top node, T, corresponds to the whole database.

Let us brie<sup>fl</sup>y describe the algorithm $H I P A M _ { M O } ,$ which is essentially the original HIPAM algorithm, except for the dissimilarity measure d . For more details see [47,49,50]. For a given node $P ,$ the algorithm must decide whether it is advisable to split this (parent) cluster into new (child) clusters, or to stop. If $| P | \leq 2 ,$ , then it is an end (or terminal) node; otherwise, a PAM is applied to P with $k _ { 1 }$ groups, where $k _ { 1 }$ is chosen by maximizing the ASW (average silhouette width) of the new partition. After a post-processing step, where further partitioning or collapsing procedures for the $k _ { 1 }$ clusters are allowed in order to try to improve the ASW, a partition $C = \{ C _ { 1 } , . . . , C _ { k } \}$ is <sup>fi</sup>nally obtained from P. Note that k is not necessarily equal to $k _ { 1 }$ . Next, the average silhouette width of $C \left( { \mathrm { 0 r } A S W _ { C } } \right)$ is obtained, and the same steps used to generate C are applied to each $C _ { i }$ to obtain a new partition. If we denote the ASW of the new partition with $i = 1 , . . . ,$ k using SS $( \operatorname { i f } | C _ { i } | \leq 2$ then $S S _ { i } = 0 )$ then the Mean Split Silhouette (MSS) is de<sup>fi</sup>ned as the mean of the $S S _ { i } s . \mathrm { I f } \ M S S ( k ) < A S W _ { C } ,$ , then these new k child clusters of the partition

![](/api/attachments/5E8J6JAM/fulltext/images/31dfe3efd8243d5147a864aae5a858687ff2754d6ede21e3c0cfabba549e8e30.jpg)

Table 6  
Measurements used to de<sup>fi</sup>ne the sizes in the European Normative to sizing system.

<table><tr><td>Bust</td><td>78-82</td><td>82-86</td><td>86-90</td><td>90-94</td><td>94-98</td><td>98-102</td><td>102-107</td><td>107-113</td></tr><tr><td>Waist</td><td>62-66</td><td>66-70</td><td>70-74</td><td>74-78</td><td>78-82</td><td>82-86</td><td>86-91</td><td>91-97</td></tr><tr><td>Hip</td><td>86-90</td><td>90-94</td><td>94-98</td><td>98-102</td><td>102-106</td><td>106-110</td><td>110-115</td><td>115-120</td></tr></table>

C are included in the classi<sup>fi</sup>cation tree. Otherwise, P is a terminal node. The algorithm $H I P A M _ { I M O }$ is summarized in Algorithm 1. The two algorithms differ mainly in terms of the use of the INCA criterion.

1. At each node P, if there is k such that INC $\Upsilon _ { k } > 0 . 2$ , then we select the k prior to the <sup>fi</sup>rst largest slope decrease.

2. On the other hand, if INC $\Upsilon _ { k } > 0 . 2$ for all k, then P is a terminal node.

However, this procedure does not apply either to the top node T or to the generation of the new partitions from which the MSS is calculated. In this case, even when all $I N C A _ { k } > 0 . 2$ , we <sup>fi</sup>x $k = 3$ as the number of groups to divide and proceed.

## 4. Application to apparel sizing

Note that $H I P A M _ { M O }$ and $H I P A M _ { I M O }$ return clusters characterized by their medoids, typical objects of these clusters. These medoids could be used as representative <sup>fi</sup>t models of the target market. Furthermore, the algorithms enable us to identify outliers. Note that this is particularly important in the apparel sizing context, where the target population is not the whole population.

## Algorithm 1 $. H I P A M _ { I M O }$

## 1. Initialization of the tree:

Let the top cluster with all the elements be T.

1.1. Initial clustering: Apply a PAM to T with the number of clusters,

$k _ { 1 } ,$ provided by the INCA statistic with the following rule:

if $I N C A _ { k _ { 1 } } { < } 0 . 2 \forall k _ { 1 }$ then

$$
k _ {1} = 3
$$

else

$k _ { 1 }$ as the value preceding the <sup>fi</sup>rst largest slope decrease. end if

An initial partition with $k _ { 1 }$ clusters is obtained.

1.2. Post-processing: Apply several partitioning or collapsing procedures to the $k _ { 1 }$ clusters to try to improve the ASW. A partition with k clusters from T is obtained.

![](/api/attachments/5E8J6JAM/fulltext/images/9269f3d2742fd22fb96d13490ae8d5e70a1f0ca69cd97d3a3c87307740110edd.jpg)  
Fig. 4. Bust vs. hip in the outliers obtained using $H I P A M _ { M O }$ (left) and $H I P A M _ { I M O }$ (right).

Hip measurements corresponding to the <sup>fi</sup>t models obtained b $H I P A M _ { M O }$ . The total number of <sup>fi</sup>t models for each bust class is displayed in parentheses and bold in the column corresponding to the expected measurements.

<table><tr><td>Hip class</td><td>[86,90]</td><td>[90,94]</td><td>[94,98]</td><td>[98,102]</td><td>[102,106]</td><td>[106,110]</td><td>[110,115]</td><td>[115,120]</td><td>&gt;120</td></tr><tr><td>Bust class</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[78,82]</td><td>1 (5)</td><td>2</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[82,86]</td><td>0</td><td>1 (3)</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[86,90]</td><td>0</td><td>1</td><td>2 (10)</td><td>4</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[90,94]</td><td>0</td><td>0</td><td>1</td><td>1 (5)</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[94,98]</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1 (4)</td><td>2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[98,102]</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0 (4)</td><td>1</td><td>1</td><td>0</td></tr><tr><td>[102,107]</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>3 (9)</td><td>3</td><td>1</td></tr><tr><td>[107,113]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0 (2)</td><td>1</td></tr></table>

## 2. Local HIPAM:

while there are active clusters do

Generation of the candidate clustering partition: PHASE I FOR HIPAM<sub>IMO</sub>

Evaluation of the candidate clustering partition: PHASE II FOR HIPAM<sub>IMO</sub>

end while

Subroutine 1. PHASE I FOR $H I P A M _ { I M O }$

For each cluster, P, of a partition:

1.

if |P| ≤ 2 then

STOP (P is a terminal node).

else

if IN $\hphantom { - } \mathrm { R } _ { k _ { 1 } } { < } 0 . 2$ ∀k<sub>1</sub> then

STOP (P is a terminal node).

else

2. Initial clustering: Apply a PAM to P with the number of clusters, $k _ { 1 } ,$ provided by the INCA statistic as the value preceding the <sup>fi</sup>rst largest slope decrease. An initial partition with $k _ { 1 }$ clusters is obtained.

3. Post-processing: Apply several partitioning or collapsing procedures to the $k _ { 1 }$ clusters to try to improve the ASW.

The candidate partition, $C = \{ C _ { 1 } , . . . , C _ { k } \}$ , from P is obtained.

end if

end if

## Subroutine 2. PHASE II FOR $H I P A M _ { I M O }$

Let the candidate clustering partition be $C = \{ C _ { 1 } , . . . , C _ { k } \}$ obtained from P.

1. Calculate the ASW of C, ASW .

2. For each $C _ { i } ,$ generate a new partition using steps 1.1. and 1.2. of the initialization of the tree and calculate its $S S _ { i } .$

3. 3.

$$
\text { if } M S S (k) = \frac {1}{k} \sum_ {i = 1} ^ {k} S S _ {i} <   A S W _ {C} \text { then }
$$

C is accepted.

else

C is rejected. STOP (P is a terminal node).

end if

## 4.1. Our data

National authorities and industrial groups from the clothing sector in different countries (for instance, USA, UK, Australia and Spain, among others) have been fostering various national anthropometric surveys in recent years. In 2006 the Spanish Ministry of Health commissioned a 3D anthropometric study of the Spanish female population. This survey was aimed at generating anthropometric data from Spanish women for the clothing industry [1]. A sample of 10,415 Spanish females from 12 to 70 years old was randomly chosen from the of<sup>fi</sup>cial Postcode Address File. These women were scanned using a Vitus Smart 3D body scanner from Human Solutions. From the 3D mesh, 95 anthropometric measurements were calculated semi-automatically, combining automatic measures based on geometric characteristic points with a manual review. The garment design was based on the ISO 20685 standard. From these 95 body measurements the <sup>fi</sup>ve most relevant features in garment development were calculated: bust circumference, chest circumference, neck to ground length, waist circumference and hip circumference. These are the main primary and secondary dimensions used by pattern makers for sizing [15]. In particular, for upperbody garments bust circumference is the primary dimension, while the others are secondary. We have selected non-pregnant women without any cosmetic surgery aged between 20 and 65 years old from the whole database, resulting in a sample size of 6013 women. Summary statistics of these characteristics can be found in Table 2.

Waist measurements corresponding to the <sup>fi</sup>t models obtained by $H I P A M _ { M O }$ . The total number of <sup>fi</sup>t models for each bust class is displayed in parentheses and bold in the column corre sponding to the expected measurements.

<table><tr><td>Waist class</td><td>[62,66]</td><td>[66,70]</td><td>[70,74]</td><td>[74,78]</td><td>[78,82]</td><td>[82,86]</td><td>[86,91]</td><td>[91,97]</td><td>&gt;97</td></tr><tr><td>Bust class</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[78,82]</td><td>0 (5)</td><td>4</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[82,86]</td><td>0</td><td>1 (3)</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[86,90]</td><td>0</td><td>0</td><td>2 (10)</td><td>3</td><td>3</td><td>2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[90,94]</td><td>0</td><td>0</td><td>0</td><td>1 (5)</td><td>0</td><td>4</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[94,98]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 (4)</td><td>2</td><td>2</td><td>0</td><td>0</td></tr><tr><td>[98,102]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 (4)</td><td>3</td><td>1</td><td>0</td></tr><tr><td>[102,107]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 (9)</td><td>4</td><td>5</td></tr><tr><td>[107,113]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 (2)</td><td>2</td></tr></table>

![](/api/attachments/5E8J6JAM/fulltext/images/623de8a26876f7115018b8ad1f7809a436e29b02d8ecee33b624a6b2e01ac84b.jpg)

![](/api/attachments/5E8J6JAM/fulltext/images/4f60b5dd74a0ad4285b722975c1bdaee81d5df56a29aae2591f920c6ed7b6991.jpg)  
Fig. 5. For each bust class, the left bar of Fig. 5(a) (resp. Fig. 5(b)) refers to the hip (resp. waist) of the <sup>fi</sup>t models obtained by $H I P A M _ { M O }$ while the right bar refers to the expected hip (resp. waist).

Hip measurements corresponding to the <sup>fi</sup>t models obtained by $H I P A M _ { I M O } .$ The total number of <sup>fi</sup>t models for each bust class is displayed in parentheses and bold, in the column corresponding to the expected measurements.

<table><tr><td>Hip class</td><td>[86,90]</td><td>[90,94]</td><td>[94,98]</td><td>[98,102]</td><td>[102,106]</td><td>[106,110]</td><td>[110,115]</td><td>[115,120]</td><td>&gt;120</td></tr><tr><td>Bust class</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[78,82]</td><td>0 (3)</td><td>2</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[82,86]</td><td>0</td><td>0 (3)</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[86,90]</td><td>0</td><td>0</td><td>0 (3)</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[90,94]</td><td>0</td><td>0</td><td>0</td><td>1 (3)</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[94,98]</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1 (3)</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>[98,102]</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1 (3)</td><td>1</td><td>0</td><td>0</td></tr><tr><td>[102,107]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1 (3)</td><td>1</td><td>0</td></tr><tr><td>[107,113]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>2 (5)</td><td>1</td></tr></table>

## 4.2. Experimental results

Two preliminary pre-segmentations have been performed. The <sup>fi</sup>rst uses bust circumference and the second is based on geographical location. Instead of a global clustering, we will perform clustering on each de<sup>fi</sup>ned class.

## 4.2.1. Database and bust circumference

Upper body garments are typically sized by segmenting bust circumference (primary dimension) in regular 5-cm intervals to create “sizing tables”, the main tool used by pattern makers. The interval range varies between different professionals and countries, depending on the target population and the garment style. We have partitioned the database into twelve classes taking into account bust circumference values according to the sizes de<sup>fi</sup>ned in the European Normative to sizing system [15]. There are a few elements in the classes corresponding to women with a bust circumference of less than 78 cm or larger than 113 cm. In what follows, only the classes corresponding to the 8 central bust sizes with counts of more than 250 per class will be taken into account. The intervals used appear in Table 6. The algorithms $H I P A M _ { M O }$ and $H I P A M _ { I M O }$ have been applied to each class. Table 3 details the number of clusters with more than two elements and Table 4 displays their corresponding sizes.

Waist measurements corresponding to the <sup>fi</sup>t models obtained by $H I P A M _ { I M O } .$ . The total number of <sup>fi</sup>t models for each bust class is displayed in parentheses and bold, in the column corresponding to the expected measurements.

<table><tr><td>Waist class</td><td>[62,66]</td><td>[66,70]</td><td>[70,74]</td><td>[74,78]</td><td>[78,82]</td><td>[82,86]</td><td>[86,91]</td><td>[91,97]</td><td>&gt;97</td></tr><tr><td>Bust class</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[78,82]</td><td>0 (3)</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[82,86]</td><td>0</td><td>1 (3)</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[86,90]</td><td>0</td><td>0</td><td>1 (3)</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[90,94]</td><td>0</td><td>0</td><td>0</td><td>0 (3)</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>[94,98]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 (3)</td><td>1</td><td>2</td><td>0</td><td>0</td></tr><tr><td>[98,102]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 (3)</td><td>2</td><td>1</td><td>0</td></tr><tr><td>[102,107]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 (3)</td><td>2</td><td>1</td></tr><tr><td>[107,113]</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 (5)</td><td>5</td></tr></table>

![](/api/attachments/5E8J6JAM/fulltext/images/94c3a0552d6a904707eb83de87d54d709160c0d65b1cb59f4410eb3a2afe4919.jpg)

![](/api/attachments/5E8J6JAM/fulltext/images/5b75efdcef80cc5bf6634dcafd99cb27d08f4a2c1f7d32fbfb6ce1014f320435.jpg)  
Fig. 6. For each bust class, the left bar of Fig. 6(a) (resp. Fig. 6(b)) refers to the hip (resp. waist) of the <sup>fi</sup>t models obtained b $H I P A M _ { I M O }$ while the right bar refers to the expected hip (resp. waist).

The main difference between the two algorithms lies in the rule which determines the number of clusters. In this example, HIPAM has fewer clusters (around 3) and these clusters are more balanced in terms of the number of elements assigned to each group. Fig. 2 shows the scatter plots of bust versus hip circumference, one of the critical dimensions for determining body morphotypes, together with the representation of the medoids in the clusters with more than two elements obtained using both algorithms for each class. $H I P A M _ { M O }$ shows closer medoids for each class. Some of them are really quite close or even overlapping. $H I P A M _ { I M O }$ shows more distributed medoids. Considering the <sup>fi</sup>tting tolerances of clothing, the $H I P A M _ { I M O }$ algorithm provides a more cost-effective performance. It obtains a set of morphotypes to improve garment <sup>fi</sup>t by de<sup>fi</sup>ning a subset of sizes for each bust size or by offering different garment models and designs that take into consideration the different body types. These results were compared with the PCA-based sizing method, which is the most commonly used approach for generating sizes from anthropometric data [22,23,55]. Fig. 3 shows the locations of the medoids in the [86, 90[ cm class over the <sup>fi</sup>rst and second principal component. The <sup>fi</sup>rst component groups the four body circumferences considered (bust, chest, waist and hip) and the second component is mainly represented by the neck to ground variable. These <sup>fi</sup>rst two principal components represent 60% of the variance.

Regarding outliers, the $H I P A M _ { I M O }$ algorithm <sup>fi</sup>nds 82 while $H I P A M _ { M O }$ <sup>fi</sup>nds 92. Forty of them are considered outliers by both algorithms. Table 5 shows the percentage of outliers obtained by both algorithms for each class. Fig. 4 shows the scatter plots of bust vs. hip, together with the outliers according to $H I P A M _ { M O }$ and HIPAM-. We observe that $H I P A M _ { I M O }$ only identi<sup>fi</sup>es outliers in the four bust classes corresponding to small and large sizes. Clothing industry practice for the mass production of clothing is to optimize sizes by addressing only the most pro<sup>fi</sup>table. Extreme sizes are usually offered as “special sizes” by companies focusing on this target market. Thus, results provided by $H I P A M _ { I M O }$ are quite well aligned to this aim.

Some other scatter plots showing medoids and outliers returned by $H I P A M _ { M O }$ and $H I P A M _ { I M O }$ can be found in the Supplementary Material. In addition, a comparison between the outliers detected by our algorithms and the outliers detected by a common method used in the apparel sizing literature to the same end and an R package that focuses on identifying multivariate outliers are also given in the Supplementary Material.

Summary statistics of the groups located in the south and north of Spain.

<table><tr><td>Measurement (cm)</td><td>Minimum</td><td>First quantile</td><td>Median</td><td>Mean</td><td>Third quantile</td><td>Maximum</td></tr><tr><td colspan="7">Summary statistics for the southern group</td></tr><tr><td>Neck to ground length</td><td>118.2</td><td>134.5</td><td>137.4</td><td>137.6</td><td>140.9</td><td>155.8</td></tr><tr><td>Bust circumference</td><td>90.00</td><td>90.90</td><td>91.70</td><td>91.85</td><td>92.80</td><td>93.90</td></tr><tr><td>Chest circumference</td><td>89.63</td><td>93.20</td><td>94.75</td><td>94.83</td><td>96.10</td><td>101.63</td></tr><tr><td>Waist circumference</td><td>68.90</td><td>78.92</td><td>81.55</td><td>81.98</td><td>84.67</td><td>95.00</td></tr><tr><td>Hip circumference</td><td>91.60</td><td>99.78</td><td>103.05</td><td>103.38</td><td>106.75</td><td>117.20</td></tr><tr><td colspan="7">Summary statistics for the northern group</td></tr><tr><td>Neck to ground length</td><td>123.6</td><td>131.8</td><td>136.0</td><td>135.8</td><td>139.4</td><td>152.4</td></tr><tr><td>Bust circumference</td><td>90.00</td><td>91.20</td><td>92.45</td><td>92.15</td><td>93.12</td><td>93.90</td></tr><tr><td>Chest circumference</td><td>85.47</td><td>94.31</td><td>95.32</td><td>95.58</td><td>97.17</td><td>101.39</td></tr><tr><td>Waist circumference</td><td>71.40</td><td>78.38</td><td>81.65</td><td>81.33</td><td>83.72</td><td>92.20</td></tr><tr><td>Hip circumference</td><td>88.60</td><td>98.12</td><td>102.20</td><td>102.42</td><td>106.12</td><td>117.60</td></tr></table>

Table 12  
Measurements of the prototypes from the southern group (<sup>fi</sup>rst and second rows) and the northern group (third and fourth rows), obtained with $H I P A M _ { M O } .$

<table><tr><td>Code</td><td>Chest</td><td>Neck to ground</td><td>Waist</td><td>Hip</td><td>Bust</td></tr><tr><td>ANTAS052</td><td>93.8267</td><td>139.0</td><td>81.1</td><td>103.3</td><td>92.0</td></tr><tr><td>CHIPI018</td><td>96.0296</td><td>137.5</td><td>81.2</td><td>101.1</td><td>91.6</td></tr><tr><td>BILB085</td><td>97.4198</td><td>131.8</td><td>86.6</td><td>103.9</td><td>93</td></tr><tr><td>ELGOI111</td><td>94.3988</td><td>141.9</td><td>81.0</td><td>108.0</td><td>91</td></tr></table>

This additional material also contains an anthropometric analysis of the outliers provided by our algorithms and a study about the possibility of using a HIPAM algorithm to de<sup>fi</sup>ne an apparel sizing system.

A direct comparison between our method and other procedures commonly used in the literature is not straightforward because, as previously mentioned, their aim is not to identify <sup>fi</sup>t models, but to create sizing systems. Therefore, an interesting and valuable analysis of our methodology's performance could be a comparison between the anthropometric measurements of the <sup>fi</sup>t models identi<sup>fi</sup>ed by our algorithms and the measurements established by the European Normative to sizing system [15]. The results of this comparison are shown in the following section.

## 4.2.2. Comparison with standard adopted method

Let us compare the main measurements (bust, hip and waist circumference) of the <sup>fi</sup>t models obtained by $H I P A M _ { M O }$ and HIPAM-<sub>IMO</sub> with the corresponding standard measurements de<sup>fi</sup>ned by the European Normative to sizing system. This standard establishes several sizes according to the combinations of bust, waist and hip measurements. See Table 6 for the eight sizes considered in our approach. Tables 7 and 8 (resp. Tables 9 and 10) display the hip and waist measurements corresponding to the <sup>fi</sup>t models obtained by $H I P A M _ { M O }$ (resp. $H I P A M _ { I M O } )$ . In each table, the total number of <sup>fi</sup>t models for each bust class is displayed (in parentheses and bold). These quantities appear in the column corresponding to the expected measurements according to the European standard. Fig. 5 (resp. Fig. 6) also shows the results of $H I P A M _ { M O }$ (resp. $H I P A M _ { I M O } )$ as bar charts for hip and waist measurements. For both $H I P A M _ { M O }$ and $H I P A M _ { I M O }$ the same conclusions are reached. For each bust size, the waist measurement of the <sup>fi</sup>t models is always greater than expected. This feature is not so extreme for the hip measurement, but it does also tend to be greater. What is more, for some bust sizes none of the <sup>fi</sup>t models has the expected hip or waist size, see e.g. bust size [98,102[ for the results of $H I P A M _ { M O }$ or bust size [78,82[ for the results of $H I P A M _ { I M O } .$ . These results suggest that the European standard sizes do not correspond to the real measurements of the current population (at least for Spanish women). Our methodology makes it possible to discover more realistic <sup>fi</sup>t models in terms of the different morphotypes of the population, and it will therefore help to improve garment <sup>fi</sup>t.

## 4.2.3. Obtaining medoids for different regions

Two Spanish regions will be considered, one located in the south and the other in the north. We have not taken into account all the bust classes for this study. Instead, the largest class has been selected, corresponding to bust size [90, 94[ cm. We have therefore dealt with 166 women from the southern group and 64 from the northern group. Table 12 displays the identi<sup>fi</sup>cation codes and main measurements of the medoids obtained by applying $H I P A M _ { M O }$ and Fig. 7 shows the 3D representations of the current medoids. Regarding the clustering results provided by $H I P A M _ { I M O } ,$ the measurements of the medoids in the main variables are shown in Table 13 and their 3D representations can be seen in Fig. 8.

![](/api/attachments/5E8J6JAM/fulltext/images/4813df10676e488f5cf296bbb3a663f68048194025fada18f286922140915762.jpg)  
Fig. 7. Front and lateral 3D representations of the medoids obtained with $H I P A M _ { M O }$ from southern group (<sup>fi</sup>rst row) and the northern group (second row).

Measurements of the prototypes from the southern group (<sup>fi</sup>rst to third rows) and the northern group (fourth to sixth rows), obtained with $H I P A M _ { I M O } .$

<table><tr><td>Code</td><td>Chest</td><td>Neck to ground</td><td>Waist</td><td>Hip</td><td>Bust</td></tr><tr><td>ABAD024</td><td>94.0821</td><td>139.1</td><td>80.1</td><td>101.7</td><td>92.4</td></tr><tr><td>PRTOS159</td><td>95.0924</td><td>140.3</td><td>79.0</td><td>108.2</td><td>91.5</td></tr><tr><td>MALAG004</td><td>93.9341</td><td>131.5</td><td>86.0</td><td>101.8</td><td>91.1</td></tr><tr><td>ELGOI020</td><td>94.4474</td><td>134.7</td><td>73.1</td><td>96.3</td><td>90.5</td></tr><tr><td>ERNAD110</td><td>97.1320</td><td>139.6</td><td>83.8</td><td>108.8</td><td>93.4</td></tr><tr><td>BILB132</td><td>94.3286</td><td>128.7</td><td>87.3</td><td>101.2</td><td>93.3</td></tr></table>

$H I P A M _ { M O }$ <sup>fi</sup>nds two medoids while $H I P A M _ { I M O }$ <sup>fi</sup>nds three for the two regions. The anthropometry of the two medoids obtained with the $H I P A M _ { M O }$ for the southern group (ANTAS052 and CHIPI018) is very similar. However, there is signi<sup>fi</sup>cant anthropometric variability; for instance, the range for the neck to ground variable is 37 cm. See the statistics for the southern group in Table 11. In contrast, $H I P A M _ { I M O }$ provides three medoids with high anthropometric differences. Neck to ground differs by 8.8 cm between PRTOS159 and MALAG004 and hip circumference differs by 6.5 cm between ABAD24 and PRTOS159. As the aim of looking for good prototypes for apparel design consists of representing anthropometric diversity, medoids should represent a subset of the population with different <sup>fi</sup>tting requirements. For the northern group the two medoids resulting from $H I P A M _ { M O }$ are more diverse. The neck to ground variable differs by 10.1 cm and waist circumference differs by 5.6 cm. Even so, $H I P A M _ { I M O }$ shows more anthropometric distance between medoids. The difference in waist circumference between ELGOI020 and ERNAD110 is 10.7 cm and neck to ground between BILB132 and ERNAD110 differs by 10.9 cm. The results obtained by applying the two methods to obtain medoids from two different regions show that the $H I P A M _ { I M O }$ algorithm performs better at <sup>fi</sup>nding representative models for apparel sizing.

These medoids have been found using <sup>fi</sup>ve anthropometric variables. These prototypes, as well as other economic or marketing considerations, will help the decision makers in their task.

## 5. Conclusions

Providing quality <sup>fi</sup>t in apparel is the major aim in the design and manufacture of clothing to ensure user comfort and better appearance. The de<sup>fi</sup>nition of an effective and accurate ready-to-wear sizing system is a complex task that is highly dependent on the de<sup>fi</sup>nition of good <sup>fi</sup>t models. However, almost every company uses different prototypes and there are therefore signi<sup>fi</sup>cant differences in the sizing and <sup>fi</sup>t of garments from different apparel manufacturers. It is important to <sup>fi</sup>nd good prototypes to improve the <sup>fi</sup>t analysis process. The methodology proposed above, based on the HIPAM algorithm method, provides new insights into the need to de<sup>fi</sup>ne representative and accurate physical <sup>fi</sup>t models. The HIPAM algorithm is a clustering method which applies partitioning and collapsing steps iteratively to create a classi<sup>fi</sup>cation tree where the last level (end nodes) is a classi<sup>fi</sup>cation. This algorithm includes the advantages of hierarchical and partitioning clustering methods.

We have introduced two algorithms based on the HIPAM algorithm that was originally proposed to deal with gene expression data. Our application is different, thus the choice of an appropriate dissimilarity measure is a major issue. Therefore, our <sup>fi</sup>rst algorithm replaces the original distances with a dissimilarity measure that is suitable for anthropometric data. However, the differences between the original HIPAM and our second algorithm are greater. The HIPAM method uses the average silhouette width (ASW) as a measure of cluster structure and the maximisation of the ASW as the criterion to split a cluster into sub-clusters. The use of ASW is reasonable, but a splitting criterion based on this alone could be too restrictive. For that reason, although the ASW is used to evaluate the cluster structure, we have incorporated a different rule to partition the clusters: the INCA criterion.

![](/api/attachments/5E8J6JAM/fulltext/images/015adf3e61f0d4a6f024bf139a327824108e061601c1a1d59055f89fad19fb08.jpg)  
Fig. 8. Front and lateral 3D representations of the medoids obtained with $H I P A M _ { I M O }$ from the southern group (<sup>fi</sup>rst row) and northern group (second row).

Our approach has been evaluated by analyzing a data set from a 3D anthropometric study of the Spanish female population commissioned by the Spanish Ministry of Health in 2006 and comparing the results with the European standard. From our point of view, although HIPAM shows better performance for <sup>fi</sup>nding representative prototypes, both HIPAM<sub>MO</sub> and $H I P A M _ { I M O }$ provide consistent results. They identify good prototypes and also allow us to detect outliers.

We are developing an R package in which we make both algorithms available. Our approach concurs with the following statement by Kaufman and Rousseeuw about which clustering algorithm to choose: “Sometimes several algorithms are applicable, and a priori arguments may not suf<sup>fi</sup>ce to narrow down the choice to a single method” (see [29, page 37]). Both algorithms should provide reasonable, and eventually different, sets of <sup>fi</sup>t models. These prototypes could be shown to experts in a practical situation to help them to make a decision.

A typical yet important drawback with apparel companies is that they de<sup>fi</sup>ne a single <sup>fi</sup>t model for the whole target market. In other words, apparel companies only attempt to <sup>fi</sup>t one body type, developing base patterns and grade rules according to the proportions of their <sup>fi</sup>t model. However, there might be many body types within a target market and this one idealized <sup>fi</sup>t model may not represent the variety of shapes within the size. Our method de<sup>fi</sup>nes several <sup>fi</sup>t models within each bust class that helps accurately represent the variation in size and shape for each bust size. We offer apparel manufacturers a robust statistical tool to determine representative <sup>fi</sup>t models based on the characteristics of their target population. Other related bene<sup>fi</sup>ts provided by our method are the reduction of both the costs and time associated with garment manufacture and the number of <sup>fi</sup>t sessions required, which represents a very signi<sup>fi</sup>cant advance in practice.

## Acknowledgments

This paper has been partially supported by the following grants: TIN2009-14392-C02-01, TIN2009-14392-C02-02. We would like to thank the Biomechanics Institute of Valencia for providing us with the data set and the Spanish Ministry of Health and Consumer Affairs for having commissioned and coordinated the “Anthropometric Study of the Female Population in Spain”. We would also like to thank the anonymous referee for some very valuable comments and suggestions, which helped to greatly improve this paper.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2013.07.007.

## References

[1] S. Alemany, J.C. González, B. Nácher, C. Soriano, C. Arnáiz, H. Heras, Anthropometric survey of the Spanish female population aimed at the apparel industry, Proceedings of the 2010 Intl. Conference on 3D Body scanning Technologies, Hometrica Consulting, Lugano, Switzerland, 2010.

[2] G. Anderson, If The Clothes Fit, Buy 'Em. , URL http://www.retailwire.com/discussion/ 10058/if-the-clothes-<sup>fi</sup>t-buy-em2004.

[3] L. Anderson, E. Brannon, P. Ulrich, A. Presley, D. Woronka, M. Grasso, S. Gray, Understanding Fitting Preferences of Female Consumers: Development an Expert System to Enhance Accurate Sizing Selection, Tech. rep., National Textile Center Annual Report, 1999.

[4] S. Ashdown, Sizing in Clothing: Developing Effective Sizing Systems for Readyto-Wear Clothing, Woodhead Publishing in Textiles. 2007

[5] Susan Ashdown, S. Loker, Improved apparel sizing: <sup>fi</sup>t and anthropometric 3D scan data Tech, rep. National Textile Center Annual Report 2005

[6] S.P. Ashdown, S. Loker, K. Schoenfelder, L. Lyman-Clarke, Using 3D scans for <sup>fi</sup>t analysis, Journal of Textile and Apparel, Technology and Management 4 (1) (2004) 1–12

[7] R. Bagherzadeh, M. Lati<sup>fi</sup>, A. Faramarzi, Employing a three-stage data mining procedure to develop sizing system, World Applied Sciences Journal 8 (8) (2010) 923–929.

[8] A. Bittner, F. Glenn, R. Harris, H. Iavecchia, R. Wherry, CADRE: a family of mannikins for workstation design, in: S.S. Asfour (Ed.), Trends in Ergonomics/Human Factors IV North Holland 1987 pp. 733-740

[9] E. Bye, E. McKinney, Fit analysis using live and 3D scan models, International Journal of Clothing Science and Technology 22 (2) (2010) 88–100.

[10] C.-M. Chen, Fit evaluation within the made-to-measure process, International Journal of Clothing Science and Technology 19 (2) (2007) 131–144.

[11] W. Chen, Z. Zhuang, S. Benson, L. Du, D. Yu, D. Landsittel, L. Wang, D. Viscusi, R.E. Shafer, New respirator <sup>fi</sup>t test panels representing the current Chinese civilian workers, Annals of Occupational Hygiene 53 (3) (2009) 297–305.

[12] Y. Chen, X. Zeng, M. Happiette, P. Bruniaux, R. Ngb, W. Yu, Optimisation of garment design using fuzzy logic and sensory evaluation techniques, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 22 (2009) 272–282.

[13] M.-J. Chung, H.-F. Lin, M.-J.J. Wang, The development of sizing systems for Taiwanese elementary- and high-school students, International Journal of Industrial Ergonomics 37 (2007) 707–716.

[14] I. Epifanio, G. Vinué, S. Alemany, Archetypal analysis: contributions for estimating boundary cases in multivariate accommodation problem, Computers and Industrial Engineering 64 (2013) 757–765

[15] European Committee for Standardization, European Standard EN 13402-2: Size System of Clothing. Primary and Secondary Dimensions, 2002.

[16] J. Fan, W. Yu, L. Hunter, Clothing Appearance and Fit: Science and Technology, Woodhead Publishing in Textiles, 2004.

[17] C. Frank, A. Garg, Forecasting womens apparel sales using mathematical modeling, International Journal of Clothing Science and Technology 15 (2) (2003) 107–125.

[18] M. Friess, Multivariate accommodation models using traditional and 3D anthropometry, Tech. rep. SAE, 2005.

[19] M. Friess, B. Bradtmiller, 3D head models for protective helmet development, Tech. rep. SAE, 2003.

[20] C.C. Gordon, T. Churchill, C.E. Clauser, B. Bradtmiller, J.T. McConville, I. Tebbetts, R.A. Walker, 1988 Anthropometric Survey of U.S. Army personnel: summary statistics interim report, Tech. rep., US Army Natick Research, Development and Engineering Center, March 1989.

[21] Z. Guo, W. Wong, M. Li, A multivariate intelligent decision-making model for retail sales forecasting, Decision Support Systems 55 (1) (2013) 247–255.

[22] D. Gupta, B. Gangadhar, A statistical model for developing body size charts for garments, International Journal of Clothing Science and Technology 16 (5) (2004) 458–469.

[23] C.-H. Hsu, Data mining to improve industrial standards and enhance production and marketing: an empirical study in apparel industry, Expert Systems with Applications 36 (2009) 4185–4191.

[24] C.-H. Hsu, Developing accurate industrial standards to facilitate production in apparel manufacturing based on anthropometric data, Human Factors and Ergonomics in Manufacturing 19 (3) (2009) 199–211.

[25] C.-H. Hsu, M.-J.J. Wang, Using decision-tree based data mining to establish a sizing system for the manufacture of garments, International Journal of Advanced Manufacturing Technology 26 (2005) 669–674.

[26] J.A. Hudson, G.F. Zehner, R.D. Meindl, The USAF multivariate accommodation method, Proceedings of the Human Factors and Ergonomics Society Annual Meeting 42 (10) (October 1998) 722–726.

[27] M. Ibáñez, G. Vinué, S. Alemany, A. Simó, I. Epifanio, J. Domingo, G. Ayala, Apparel sizing using trimmed PAM and OWA operators, Expert Systems with Applications 39 (12) (2012) 10512–10520, (URL http://www.sciencedirect.com/science/article/ pii/S0957417412003909)

[28] I. Irigoien, C. Arenas, INCA: new statistic for estimating the number of clusters and identifving atypical units, Statistics in Medicine 27 (2008) 2948–2973.

[29] L. Kaufman, P.J. Rousseeuw, Finding Groups in Data: An Introduction to Cluster Analysis, John Wiley, New York, 1990.

[30] K. Labat, M. DeLong, Body cathesis and satisfaction with <sup>fi</sup>t of apparel, Clothing and Textiles Research Journal 8 (2) (1990) 43–48.

[31] T. León, P. Zuccarello, G. Ayala, E. de Ves, J. Domingo, Applying logistic regression to relevance feedback in image retrieval systems, Pattern Recognition 40 (2007) 2621–2632.

[32] J. Luo, M. Fan, H. Zhang, Information technology and organizational capabilities: a longitudinal study of the apparel industry, Decision Support Systems 53 (1) (2012) 186–194.

[33] A. Luximon, Y. Zhang, Y. Luximon, M. Xiao, Sizing and grading for wearable products, Computer-Aided Design 44 (2012) 77–84.

[34] In: N. Magnenat-Thalmann (Ed.), Modeling and Simulating Bodies and Garments, Springer, 2010.

[35] C. McCulloch, B. Paal, S. Ashdown, An optimization approach to apparel sizing, Journal of the Operational Research Society 49 (1998) 492–499.

[36] L.W.F. Moroney, U.S.N. MSC, M.J. Smith, Empirical reduction in potential user population as the result of imposed multivariate anthropometric limits, Tech. rep. Naval Aerospace Medical Research Laboratory, September 1972.

[37] R. Ng, S.P. Ashdown, A. Chan, Intelligent size table generation, Proceedings of the Asian Textile Conference (ATC), 9th Asian Textile Conference, Taiwan, 2007.

[38] R Development Core Team, R: A Language and Environment for Statistical Computing, R Foundation for Statistical Computing, Vienna, Austria, 2013, ISBN 3-900051-07-0. , URL http://www.R-project.org.

[39] K. Robinette, J. McConville, Alternative to percentile models, Tech. rep. SAE, 1981.

[40] J.C. Robinson, K.M. Robinette, G.F. Zehner, User's guide to the anthropometric database at the computerized anthropometric research and design (card) laboratory (U) Tech, rep, Systems Research Laboratories Inc, February 1992

[41] C. Salusso-Deonier, M. DeLong, F. Martin, K. Krohn, A multivariate method of classifying body form variation for women's apparel, Clothing and Textiles Research Journal 4 (1) (1985–1986) 38–45.

[42] C.D. Smith Outling, Process, <sup>fi</sup>t, and appearance analysis of three-dimensional to two-dimensional automatic pattern unwrapping technology. (Master's thesis) Graduate Faculty of North Carolina State University, 2007.

[43] H.K. Song, S.P. Ashdown, An exploratory study of the validity of visual <sup>fi</sup>t assessment from three-dimensional scans, Clothing and Textiles Research Journal 28 (4) (2010) 263–278.

[44] Z.-L. Sun, T.-M. Choi, K.-F. Au, Y. Yu, Sales forecasting using extreme learning machine with applications in fashion retailing, Decision Support Systems 46 (2008) 411–419.

[45] S. Thomassey, A. Fiordaliso, A hybrid sales forecasting system based on clustering and decision trees, Decision Support Systems 42 (2006) 408–421.

[46] P. Tryfos, An integer programming approach to the apparel sizing problem, Journal of the Operational Research Society 37 (10) (1986) 1001–1006.

[47] M.J. van der Laan, K.S. Pollard, A new algorithm for hybrid hierarchical clustering with visualization and the bootstrap, Journal of Statistical Planning and Inference 117 (2003) 275–303.

[48] P. Volino, N. Magnenat-Thalmann, Accurate garment prototyping and simulation, Computer-Aided Design & Applications 2 (5) (2005) 645–654.

[49] E. Wit, J. McClure, Statistics for Microarrays: Design, Analysis and Inference, John Wiley & Sons, Ltd., 2004

[50] E. Wit, J. McClure, Statistics for Microarrays: Inference, Design and Analysis. R package version 0.1, 2006. , (URL http://www.stats.gla.ac.uk/ microarray/ book/smida.html).

[51] J. Workman, Body measurement speci<sup>fi</sup>cations for <sup>fi</sup>t models as a factor in clothing size variation, Clothing and Textiles Research Journal 10 (1) (1991) 31–36.

[52] J. Workman, E. Lentz, Measurement speci<sup>fi</sup>cations for manufacturers' prototype bodies, Clothing and Textiles Research Journal 18 (4) (2000) 251–259.

[53] R. Yager, On ordered weighted averaging aggregation operators in multi-criteria decision making, IEEE Transactions on Systems Man and Cybernetics 18 (1988) 183–190.

[54] G.F. Zehner, R.S. Meindl, J.A. Hudson, A Multivariate Anthropometric Method For Crew Station Design: Abridged, Tech. rep. Kent State University, April 1993.

[55] R. Zheng, W. Yu, J. Fan, Development of a new Chinese bra sizing system based on breast anthropometric measurements, International Journal of Industrial Ergonomics 37 (2007) 697–705.

[56] W. Zhou, S. Piramuthu, Preventing ticket-switching of RFID-tagged items in apparel retail stores, Decision Support Systems 55 (2013) 802–810.

Guillermo Vinué was born in Valencia (Spain) in 1985. He graduated in Mathematics (2008) at the University of Valencia and he is actually a PhD student in Statistics and Optimization at the Department of Statistics and Operations Research at the University of Valencia, Spain. His research interests are concerned on computational statistics with applications in Anthropometry.

Teresa León was born in Madrid (Spain) in 1965. She graduated in Mathematics (1987) at the University of Valencia and, at the same university, received her PhD in Operations Research (1991). She is a Titular Professor at the Department of Statistics and Operations Research at the University of Valencia, Spain. Her present research interests are mainly concerned on fuzzy set theory, medical image analysis and functional data analysis

Sandra Alemany was born in Valencia (Spain) in 1974. She graduated in Mechanical Engineering (1998). She is currently a senior researcher of the Instituto de Biomecánica de Valencia, expert on 3D anthropometry and its application to product design mainly in the industrial sectors of footwear and clothing. Her current activity is focused on the application of advance 3D shape analysis methods to enhance the ergonomic design process of consumer goods.

Guillermo Ayala was born in Cartagena (Spain) in 1962. He graduated in Mathematics (1985) and received his PhD in Statistics (1988), both at the University of Valencia. He is currently a Professor at the Department of Statistics and Operations Research at the University of Valencia, Spain. His research interests are in the areas of medical image analysis and applications of stochastic geometry in computer vision.
