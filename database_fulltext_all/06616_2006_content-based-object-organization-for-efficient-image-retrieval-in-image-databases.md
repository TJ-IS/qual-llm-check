---
otero_id: 6616
otero_key: "6E3SCU3G"
title: "Content-based object organization for efficient image retrieval in image databases"
authors: "S.H. Kwok; J. Leon Zhao"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.04.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Content-based object organization for efficient image retrieval in image databases

S.H. Kwok <sup>a,b,⁎,1</sup>, J. Leon Zhao <sup>b,c,1</sup>

<sup>a</sup> Department of Information Systems, College of Business Administration, California State University, Long Beach, 1250 Bellflower Boulevard, Long Beach, CA 90840-8506, United States

<sup>b</sup> Department of Information and Systems Management, HKUST Business School, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong SAR, China

<sup>c</sup> Department of Management Information Systems, Eller College of Management, The University of Arizona, Tucson, Arizona 85721, United States

Received 10 June 2005; received in revised form 26 February 2006; accepted 24 April 2006 Available online 15 June 2006

## Abstract

Much research has focused on content-based image retrieval (CBIR) methods that can be automated in image classification and query processing. In this paper, we propose a blob-centric image retrieval scheme based on the blobworld representation. The blobcentric scheme consists of several newly proposed components, including an image classification method, an image browsing method based on semantic hierarchy of representative blobs, and a blob search method based on multidimensional indexing. We present the database structures and their maintenance algorithms for these components and conduct a performance comparison of three image retrieval methods, the naive method, the representative-blobs method, and the indexed-blobs method. Our quantitative analysis shows significant reduction in query response time by using the representative-blobs method and the indexed-blobs method.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Blob-centric image representation; Content-based image retrieval; Image database management; MB<sup>+</sup>-trees; Multi-dimensional indexing; Object-oriented image organization

## 1. Introduction

Research in information retrieval, database management, computer vision, and image processing is converging towards providing content-based access to image databases. Researchers in multimedia databases have outlined the main problems in image database management [7,11,15,17], including the semantic issues in image representation and organization, the methods of identifying and indexing image objects, browsing and searching images using sophisticated querying techniques such as imprecise queries, user-directed query processing, and similarity measures.

Common feature-based Query-by-Image-Content (QBIC) systems, such as IBM QBIC [5,18], and Photobook [21] incorporate various distance metrics and matching algorithms. Other systems that identify images using low-level properties such as color, texture and shape [16] include Virage [8], Candid [13], Chatbot [20]. All the above systems use the color-layout matching model, in which images are retrieved if and only if they contain the exact combination of low-level features specified in the query. Although low-level features are easily obtainable, the quality of the results retrieved based on these low-level features is often not satisfactory because the user may have difficulty in translating their needs into the appropriate values in these low-level features [15].

Research trends in content-based image retrieval (CBIR) have shifted to object-oriented techniques, for example region-based image retrieval [4,14,22]. These new techniques extract portions of the images and encapsulate their low-level features in data objects that take into account of spatial features as well. Based on these objects, images can then be classified and categorized in new ways that are not possible in the existing commercial image database systems. A major advantage of the object-oriented techniques is ease of query formulation and interpretation. Using the image objects, the user can formulate queries in more flexible ways such as using combinations of different sample objects, rather than using low-level features directly.

An object-oriented image representation called blobworld has been developed at the University of California at Berkeley [3,2]. In a blobworld, portions of image that are relatively homogeneous in image features are extracted from an existing image and are represented as objects, referred to as blobs. The most representative blobs are then used to identify similar images with automatic matching and classification algorithms. This approach has been experimentally applied to several image collections in a digital library and has been found to be promising.

Applying this new method to image databases is of great interest because the blob representation allows automatic categorization and querying of images. In this paper, we propose a blob-centric image retrieval scheme in image databases. The blob-centric scheme consists of several newly proposed components, including an image classification method, an image browsing method based on semantic hierarchy of representative blobs, and a blob search method based on multidimensional indexing. In this paper, we also develop the database structures and the maintenance algorithms for image classification, semantic hierarchy, and blob indexing.

We further conduct a performance comparison of image retrieval efficiency for three possible methods, the naive method, the representative-blobs method, and the indexed-blobs method. Our research focuses on large-scale image databases where efficient retrieval is a challenging issue.

The rest of the paper is organized as follows: Section 2 describes several important concepts from previous research such as the blobworld representation etc. In Section 3, we propose the idea of representative blobs for the purposes of reducing the complexity of image matching. Section 4 applies the MB<sup>+</sup>-tree indexing to the blobcentric image database structure and presents the querying algorithms for the blob-centric image querying approach based on sample blobs. Section 5 delineates the concept of semantic hierarchy for supporting image browsing and introduces the data structures and maintenance algorithms. In Section 6, we model three querying methods, i.e., the naive method, the representative-blobs method, and the indexed-blobs method, and conduct a performance analysis on the efficiency of these three methods. Finally, Section 7 summarizes the contributions of our study and highlights our future research directions.

## 2. Motivation and problem description

## 2.1. Blobworld image representation

The blobworld [3,2] provides a transformation from the raw pixel data to a small set of localized coherent regions in color and texture. The resulting image regions are referred to as blobs, which can then be used for classifying and comparing images. Using the blobworld representation, the user is also given an opportunity to view the object representation of the sample image(s) along with the query results. This is an important and unique merit of the system. In comparison, most other content-based image database systems do not offer the user this visual feature in query processing; consequently, the outcome of many queries in these systems can be quite inexplicable.

In blobworld representation, each object may be visualized by an ensemble of 2-D ellipses, or “blob,” each of which possesses a number of attributes. The number of blobs in an image is typically less than ten. Each blob represents a region of the image which is roughly homogeneous with respect to color or texture. A blob is described by its dominant colors, mean texture descriptors, and spatial centroid and scatter matrix.

An example image containing an airplane in the sky is shown in Fig. 1. The blobworld representation of the image with four blobs (the second picture from the left) is also given. Of the four blobs, two represent the airplane, and the other two represent the sky. Assume that two out of four blobs are selected as sample blobs; blob 1 (the third picture) and blob 2 (the fourth picture). A query can then be specified using a combination of these sample blobs. The data structure of blob 2 that consists of color, texture, shape descriptor is given in Table 1. It is noteworthy that the two colors — color1 and color2 can be converted into HSV (Hue, Saturation, and Value) cone coordinates for use in query processing. The exact meanings of these feature factors can be found in [3,2].

![](/api/attachments/6E3SCU3G/fulltext/images/b7a2bb55fff121a4b4b550d75110e7a1344e53ed872bc076bf8fc25b0630fbe6.jpg)  
Fig. 1. The blobworld representation.

## 2.2. Image matching using blobworld

The image database system [3,2] defines an “atomic query” as one which specifies a particular blob to match, e.g., “like-blob-1”. A “compound query” is defined as either an atomic query or a conjunction or disjunction of atomic queries, e.g., “like-blob-1 and like-blob-2”. Once a query is specified, the system scores each image in the database based on how closely it satisfies the query. The score $\mu _ { i }$ for each atomic query (like-blob-i) is calculated as follows [3,2]:

1. Find the feature vector $\nu _ { i }$ for the desired blob $b _ { i \cdot }$ This vector consists of the stored color, texture, position, and shape descriptors.

2. For each blob $b _ { j }$ in the database image:

(a) Find the feature vector v for $b _ { j }$

(b) Find the Mahalanobis distance between $\nu _ { i }$ and $\nu _ { j }$ using the diagonal covariance matrix $\Sigma ^ { - \textup { d } }$ (feature weights) set by the user: $d _ { i j } { = } [ ( \nu _ { i } { - } \nu _ { j } ) ^ { T }$ $\dot { \Sigma } ^ { - 1 } ( \nu _ { i } - \nu _ { j } ) ] ^ { \tilde { 1 / 2 } }$

(c) Measure the similarity between $b _ { i }$ and $b _ { j }$ using $\mu _ { i j } = \mathrm { e } ^ { \frac { - d _ { i j } } { 2 } }$ . This score is 1 if the blobs are identical in all relevant features; it decreases as the match becomes less perfect.

## 3. Take $\mu _ { i j } { = } \operatorname* { m a x } _ { j } \mu _ { i j } .$

The compound query score for the database image is calculated using fuzzy logic operations [6,12]. For example, if the query is “like-blob-1 and (like-blob-2 or like-blob-3),” the overall score for the image is $\{ \mu _ { 1 } ,$ max $\{ \mu _ { 2 } , \mu _ { 3 } \} \}$ . The user can also specify a weighting $\sigma _ { i }$ for each atomic query. If “like-blob-i” is part of a disjunction in the compound query, the weighted score is $\mu _ { i } ^ { \prime } { = } \sigma _ { i } \mu _ { i } ;$ if it is in a conjunction, the weighted score is $\mu _ { i } { = } 1 - { \sigma } _ { i } \cdot ( 1 - \mu _ { i } )$

## 2.3. Automatic image classification using blobworld

Experiments by Belongie et al. [1] demonstrated automatic classification using blobworld representation and the blob-based image matching technique given in the last subsection. The idea is to classify a large set of images into relatively homogeneous collections so that users can browse the particular collections according to their needs.

The authors have introduced the concepts of “representative blobs” and decision trees for classifying images. However, no specifics have been reported in the literature on the particular algorithms and techniques used in their image classification process. The results of the experiments show that for blobworld, the average precision is about 47% and for color histograms [5,20], the average is about 50%.

However, we observe that even though the success rate of automatic classification algorithm reported for the blobworld representation is low (47%), the quality of automatic image classification can be improved by carefully selecting representative blobs to make the image collections more homogeneous. For instance, the plane collection can be further partitioned into several categories such as single plane, flying plane, parked plane, groups of planes, etc. Then, better representative blobs can be selected from each category. This way, the result of automatic classification should have a much higher success rate.

```yaml
blob 2 has the following properties:
color1: 0.58 0.24 0.48 color2: 0.59 0.35 0.86
color1 weight: 0.69 color2 weight: 0.31
texture: 0.18 0.10 0.71
mean_xy: -0.70 0.53
shape: 0.6 0.0 0.6
Standard deviations for matching this blob:
color std: 0.10
contrast std: 0.50 anisotropy std: Inf phi std: Inf
x std: Inf y std: Inf
area std: 0.10 ecc std: Inf orient std: Inf
```

![](/api/attachments/6E3SCU3G/fulltext/images/4af035accd1c12cd33c4474f734a2d4ffcb0ebf726f7a42e96180105c2846a45.jpg)  
Fig. 2. Partitioning the two-dimensional space into disjoint regions.

## 2.4. MB<sup>+</sup>-tree for multi-dimensional indexing

A multi-dimensional index structure called $\mathrm { M B ^ { + } }$ -tree was proposed to assist CBIR in image and video databases [23]. Although there are many methods for indexing in multi-dimensional space, such as the grid file [19], the R-tree [9], and many variations thereafter, they are not optimized for queries prevalent in multimedia databases. In this study, we choose the $\mathrm { M B } ^ { + }$ -tree as the basis for organizing the image data objects as it has been designed for query types in multimedia databases such as the nearest-neighbor query. In this subsection, we outline the structure of $\mathrm { M B ^ { + } }$ -tree in two dimensions, which can be easily extended to the multidimensional (N N 2) cases. The reader is referred to [23] for additional details.

Without loss of generality, let us assume the twodimensional space is

$$
D = [ 0, X _ {\mathrm{max}} ] \times [ 0, Y _ {\mathrm{max}} ]
$$

The space is partitioned into M vertical strips by vertical lines at

$$
[ 0, x _ {1}, x _ {2}, \dots , x _ {M} ].
$$

We call the X dimension the first dimension. Further, each vertical strip, say the mth strip is then partitioned independently into $N _ { m }$ regions by horizontal lines at

$$
\left[ 0, y _ {\mathrm{m}, 1}, y _ {\mathrm{m}, 2}, \dots , y _ {m, N _ {m}} \right].
$$

Each region $D _ { m , n } \mathrm { = } [ x _ { m , \ x m + 1 } ) \times [ y _ { m , n } , \ y _ { m , n + 1 } ) ;$ , 0 ≤ $n \leq N _ { m - 1 }$

Fig. 2 illustrates how a two-dimensional space is partitioned into disjoint regions. Note that the number of regions for each strip varies. The regions are then ordered by the subscripts in each dimension, successively. That ${ \mathrm { i s } } ,$ region $D _ { i , \bullet }$ precedes region $D _ { i + I , \bullet }$ , and regions $D _ { i , j } { \mathrm { p r e - } }$ cedes region $D _ { i , j + \bullet }$ , where the symbol • indicates any

$$
D _ {0, 0} \angle D _ {0, 1} \angle D _ {1, 0} \angle D _ {1, 1} \angle D _ {1, 2} \angle D _ {2, 0} \angle D _ {2, 1} \angle D _ {3, 0}
$$

![](/api/attachments/6E3SCU3G/fulltext/images/1621f9a7308066114f3989727f96e3c3051df383a1620c15d068e1764aa6f33c.jpg)  
Fig. 3. An example of MB<sup>+</sup>-tree.

integer. For example, the regions in Fig. 3 are ordered as follows:

Using the linear order, a balanced tree can be built on the set of all regions as shown in Fig. 3. This tree is called the multi-dimensional $\mathrm { B } ^ { + }$ -tree, or simply $\mathrm { M B } ^ { + }$ -tree. In an $\mathrm { M B ^ { + } }$ -tree, each node $D _ { m , n }$ is a rectangle and is represented in a non-leaf node by its upper-right point $( x _ { m + 1 } , y _ { m , n + 1 } )$ and the lower-left point $( x _ { m } , y _ { m , n } )$ . To save space, the leaf node is represented by its lower-left point $( x _ { m } , y _ { m , n } )$

Since the $\mathrm { M B ^ { + } }$ -tree is similar to the $\mathrm { B } ^ { + }$ -tree except that the values of nodes are represented differently, the algorithms for a $\mathrm { B } ^ { + }$ -tree can be easily adopted for an $\mathrm { M B } ^ { + }$ -tree, and therefore, the details of the maintenance algorithms are omitted. Later in the paper, we show how the $\mathrm { M B ^ { + } }$ -tree can be used to expedite the CBIR under the new data structures we propose.

## 3. Image classification through representative blobs

To support more effective image browsing and contentbased search, we propose to organize images into categories (that could be overlapping) linked to representative blobs. In this section, we introduce the concepts of representative blob, blob group, image category, and the related algorithms for initialization and update of blob groups.

## 3.1. Representative blobs and blob groups

A representative blob is an image blob used to represent a group of blobs for the purpose of categorizing the images known as blob groups. Careful selection of representative blobs is necessary in image classification in order to achieve a high precision. We propose an algorithm for extracting representative blobs from all blobs in the image database as given in Algorithm 1.

Algorithm 1. Selection of representative blobs and creation of blob groups.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs:
N: the total number of blobs
 $S_{b}$ : the set of blobs  $b_{i} \in S_{b}$ , where i = 1 to N,
 $S_{v}$ : the set of the corresponding feature vectors  $v_{i} \in S_{v}$ , where i = 1 to N,
 $\zeta$ : the similarity range
NOT_FINISH: status indicator

Outputs:
k: the total number of blob groups
 $S_{bg}$ : a set of blob group  $S_{bg} = \{1, 2, ..., N\}$ $S_{r}$ : a set of representative blobs and their feature vectors  $S_{r} = \{(b_{1} v_{1}), (b_{2} v_{2}), ..., (b_{k} v_{k})\}$
</div>

$j \colon$ the first unmarked blob in the set of blob group $S _ { \mathrm { b g } }$ Assumption: $S _ { b } { \neq } 0 , N { \geq } 2$ 1. Initialization:

i) Sort all blobs $b _ { i } \in S _ { b }$ according to their IDs, where $i = 1$ to N.

ii) Place all feature vectors $\nu _ { i } \in S _ { \nu } , i = 1$ to N into the feature space as feature points.

iii) Set $S _ { \mathrm { b g } } [ 1 ] { = } S _ { \mathrm { b g } } [ 2 ] { = } \ldots { = } S _ { \mathrm { b g } } [ N ] { = } 0 .$

iv) Set $k { = } 1$

v) $N O T \_ F I N I S H { = } \mathrm { T r u e }$

2. Initialization of the first feature sphere for $\nu _ { 1 }$ using the similarity range $\zeta$ as radius (See Fig. 3.2A)

i) $S _ { \mathrm { r } } [ 1 ] = ( b _ { 1 } \nu _ { 1 } ) ;$ copy $b _ { 1 }$ from $S _ { b }$ and $\nu _ { 1 }$ from $S _ { \mathrm { v } }$ and insert them into the set of representative blobs $S _ { \mathrm { r } }$ .

ii) Set $S _ { \mathrm { b g } } [ 1 ] = k ;$ indicate the corresponding blob belongs to the first blob group

iii) Set ${ j = 2 } ;$ point to the second blob, the next unmarked blob.

## 3. Creation of blob groups

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
While (NOT_FINISH) {
i) Look for all blobs belonging to the current blob group that refers to  $v_{k}$ 
For i=j to N {
If (( $v_{i}$  is enclosed in the feature sphere of  $S_{r}[k] \cdot v$ ) AND ( $S_{bg}[i]=0$ ))
Set  $S_{bg}[i]=k$ ; Mark the blob to indicate its belonging blob group}
ii) Initialize and create the next blob group by identifying the first zero in  $S_{bg}$ 
While (( $j \leq N$ ) AND ( $S_{bg}[j] \neq 0$ )) { $j=j+1;\}$ 
If ( $j \leq N$ ){// create a new blob group
Set  $k=k+1$ ; point to the current representative blob.
 $S_{r}[k]=(b_{j}v_{j})$ ; copy  $b_{j}$  from  $S_{b}$  and  $v_{j}$  from  $S_{v}$ , and insert them into the set of representative blobs  $S_{r}$ .
Set  $S_{bg}[j]=k$ ; mark the blob referring to the new blob group.}
If ( $j \geq N$ ){//this is the last blob
NOT_FINISH=False}
else  $j=j+1\}$
</div>

The essential idea of Algorithm 1 is as follows: We order the blobs in a blob set according to their IDs. The first blob in the set is taken as a representative blob, and all other blobs that are close to it in terms of vector distance are removed from the set. The threshold value of the vector distance is measured by a given variable ζ. This process is done iteratively until the blob set becomes empty. The marked blobs are placed into the same group of the representative blobs identified by their markers. It is possible that one blob may belong to more than one group. The algorithm can be easily modified to make the groups unique or non-overlapping. However, this should be a design decision since it will affect the error rate and missing rate at the same time. Fig. 4A illustrates the concepts of feature space, feature points, and feature spheres used in the algorithm.

The similarity range $\zeta$ is an application variable that can be determined for specific application through experiments or optimization algorithms. The analytical model for the optimization algorithms or experiments requires special treatment and will be developed in a separate study.

Algorithm 2. Update the representative blobs and blob groups for a new blob.

Given:

$N ;$ the total number of blobs (known)

$k \mathrm { : }$ the total number of blob groups (known)

$S _ { \mathrm { b } } { \mathrm { : } }$ the set of blobs

$S _ { \mathrm { v } } \mathrm { : }$ the set of feature vectors

Inputs:

$b \colon$ a new blob

$\nu \mathrm { : }$ the feature vectors of the new blob

Outputs:

$S _ { \mathrm { r } } \mathrm { : }$ the new set of representative blob $S _ { \mathrm { b g } } { \mathrm { : } }$ the new set of blob group

1. Set up:

i) $S _ { \mathrm { b } } [ N + 1 ] = b ;$ Insert b into $S _ { \mathrm { b } }$

ii) $S _ { \mathrm { b g } } [ N + 1 ] = 0 ;$ initialize a new blob group pointer for the new blob

iii) $S _ { \mathrm { v } } [ N + 1 ] = \nu ;$ Insert the feature vector of the new blob into $S _ { \mathrm { r } }$

iv) $N { = } N { + } 1$ ; Increase the total number of blobs by one v) Set i = 1

## 2. Add b into a blob group or create a new blob group

While ((v is NOT enclosed in the feature sphere of $S _ { \mathrm { r } }$ [i] · v) AND (i ≤ k)) {i = i + 1

if (i N k) {//find NO corresponding blob group and create a new blob group

Set $S _ { \mathrm { r } } [ k ] { = } ( b \nu )$

Set $S _ { \mathrm { b g } } [ N ] { = } k \}$

else Set $S _ { \mathrm { b g } } [ N ] { = } i ;$ Mark the blob to indicate its belonging blob group}

To update the image database when a new blob is added. The new blob is compared with all representative blobs using Algorithm 2. If the new blob is not enclosed in an existing sphere as shown in Fig. 4B, a new representative blob is created for it. Otherwise, the blob is inserted into the corresponding group as indicated in Fig. 4C.

![](/api/attachments/6E3SCU3G/fulltext/images/bb5c68b42c320aeead33cd65c51c4645f6b0a213b5c698ad7df9743713a909d3.jpg)  
Fig. 4. Selection of representative blobs using feature vectors on two-dimensional feature space: A. Four representative blobs found. B. Inserting a new feature vector and finding another representative blob. C. Inserting a new feature vector and grouping it into an existing category.

Algorithms 1 and 2 deal with the selection and update of representative blobs and blob groups. However, we need to create a linkage between the blobs and their corresponding images, which forms the foundation of the data structures for image querying and browsing as developed in later sections.

## 3.2. Blob-image linkage representation

The blobs in each group can be linked to their images so that the images can be traced from the blobs using blob-to-image pointers. We also refer to the images linked to the blobs in a group as an image category. All images in the same category are ranked in descending order of the normalized Mahalanobis distance $\mu$ between the representative blob of the category and the blob corresponding to the image in question. To avoid recomputation, we store the $\mu$ values in the blob chain along with the image IDs. This is depicted in Fig. 5. We will develop algorithms for semantic-based browsing and index-based searching based on image categories linked to the blob groups.

## 4. An object-oriented image query approach

We assume that the user specifies a content-based image query by selecting one or more sample blobs, either from the collection of representative blobs or from blobs generated in some sample images. Our task is to determine a set of images in the database that matches the features of the given sample blobs. Since the number of images in the database can be very large, we assume that this matching process must be done automatically through a computational algorithm in order to ensure a reasonable response time.

Next, we propose a blob-centric approach for image matching. In order to minimize the response time, we utilize the $\mathrm { M B ^ { + } }$ -tree indexing method as discussed in Section 2. We illustrate (1) how the indexing method is applied to the blobworld representation, (2) how a sample blob is used to find similar blobs, (3) how the similar blobs lead to matching images, and (4) how multiple sample blobs are taken into account to determine matching images for the query.

## 4.1. Applying the $M B ^ { + }$ -tree indexing to the blobworld

We use the feature vector to index the blobs. Consequently, the blob-centric method requires a multidimensional index. However, to simplify the presentation, we illustrate graphically the blob-centric querying method for the two-dimensional case first, and then present the algorithm for the multi-dimensional case.

![](/api/attachments/6E3SCU3G/fulltext/images/cf59a07af9111e05673dc2cd6ec5aa08e9c655fc3fc409684eed8ea36c26ffb5.jpg)  
Fig. 5. Blobs in blob chains are ranked according to the $\mu$ values.

Assuming a sample blob b has a feature vector $< x , y >$ as marked with the <sup>⁎</sup> symbol in Fig. 6. The dots in the twodimensional space indicate the representative blobs in the image database. Create a similarity space by drawing a two dimensional rectangle around the sample blob bx, $y > ,$ which can be represented by the left lower corner and the upper right corner of the rectangle $\{ < x - \Delta x , y - \Delta y > , < x +$ $\Delta x , y + \Delta y { > } \big  $ as illustrated in Fig. 6. Note that $\Delta x$ and $\Delta y$ are referred to as the similarity radiuses on the x and $y$ dimensions, respectively. The values of $\Delta x$ and $\Delta y$ can be determined either theoretically or experimentally. In this paper, we assume that they are given.

One of the important features of an $\mathrm { M B ^ { + } }$ -tree is that it allows a linear search in a multidimensional space. For instance, to determine all regions overlapping with the similarity space of the blob denoted by <sup>⁎</sup> in Fig. 6, one needs only to determine the region containing the lower left corner of the similarity space and that containing the upper right corner. Then, the $\mathrm { M B ^ { + } }$ -tree index can be used to determine all relevant regions between the two regions through a linear search. The use of $\mathrm { \bf ~ M B } ^ { + }$ -tree can therefore reduce the search cost dramatically.

![](/api/attachments/6E3SCU3G/fulltext/images/8bd06d4f74e780ea452891aa1fcb7022ddfccfe55c591656cbac5184cdcaa2c7.jpg)  
Fig. 6. Similarity query using the ${ \mathrm { { M B } } } ^ { + } { \cdot } { \mathrm { { t r e e . } } }$

## 4.2. Retrieving similar images for a sample blob

To reduce search cost, the procedure presented next takes advantage of the $\mathrm { M B } ^ { + }$ -tree to determine the regions that overlap with the similarity space of $^ { b , }$ and compute for the similar blobs with respect to only the blobs in these regions.

Given:

(1) A sample blob b and its feature vector $< x , y > ;$

(2) A set of representative blobs B and their feature vectors $\{ < x _ { i } , y _ { i } > \}$ ; and

(3) An MB<sup>+</sup>-tree on the feature vectors over the representative blobs in B.

Objective: Determine the representative blobs in B similar to blob b.

Step 1: determine the regions that overlap with the similarity space of b:

Determine the similar regions in the two-dimensional space by searching the $\mathrm { M B } ^ { + }$ -tree and computing the regions overlapping with the similarity space using the following principle.

(1) Search the $\mathrm { { M B } ^ { + } { - } \mathrm { { t r e e } } }$ to find the region $D _ { \mathrm { { L } } }$ that contains the lower left corner of the similarity space, namely, $< x - \Delta x , \ y - \Delta y >$ . As a generic principle, a point $< x ^ { \prime } , y ^ { \prime } >$ falls in a region $\begin{array} { r } { \mathopen { } \mathclose \bgroup \left\{ < x _ { 1 } , y _ { 1 } > \aftergroup \egroup \right. } \end{array}$ $< x _ { \mathrm { u } } , y _ { \mathrm { u } } > \} \ \mathrm { i f } \ x _ { 1 } \leq x ^ { \prime } \leq x _ { \mathrm { u } }$ and $y _ { 1 } \leq y ^ { \prime } \leq y _ { \mathrm { u } } ,$ , where $< x _ { 1 } ,$ $y _ { 1 } >$ is the lower left corner of the region and ${ < x _ { \mathrm { u } } , }$ $y _ { \mathrm { u } } >$ is the right corner of the region. This search is done by tracing the $\mathrm { M B ^ { + } }$ -tree until the overlapping region is found.

(2) Search the $\mathrm { M B ^ { + } }$ -tree to find the region $D _ { \mathrm { U } }$ that contains the upper right corner of the similarity space, namely, $< x + \Delta x , y + \Delta y >$

(3) Scan the leaf nodes of the $\mathrm { M B } ^ { + }$ -tree from $D _ { \mathrm { { L } } }$ to $D _ { \mathrm { U } }$ to find all regions overlapping with the similarity space. Note that a region $D = [ x _ { 1 } , x _ { 2 } ) \times$ $[ y _ { 1 } , y _ { 2 } )$ overlaps with the similarity space $b =$ $[ x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } ) \times [ y _ { 1 } ^ { \prime } , y _ { 2 } ^ { \prime } )$ if the following conditions are true:

$$
\left[ \left(x _ {1} ^ {\prime} <   x _ {2}\right), \left(x _ {2} ^ {\prime} > x _ {1}\right) \right] \text {   and   } \left[ \left(y _ {1} ^ {\prime} <   y _ {2}\right), \left(y _ {2} ^ {\prime} > y _ {1}\right) \right].
$$

Step 2. Determining the similar blobs:

For each similar region found, determine the similar blobs by applying the Mahalanobis distance function (see Section 2) to all blobs stored in the region.

Step 3. Determining the similar images:

For each similar blob found, retrieve similar images following the blob-to-image pointers in the blob/image hierarchy.

## 4.3. Search algorithm for multidimensional feature vectors

The multi-dimensional cases are similar to the twodimensional case except that the $\mathrm { M B ^ { + } }$ -tree is now multidimensional. We present the Algorithm 3 below by extending the procedure in Section 4.2.

Algorithm 3. Retrieve similar images for a sample blob.

Inputs:

$b \colon$ a sample blob

$B \colon$ the set of representative blobs

$C \mathrm { : }$ the threshold constant of the Mahalanobis distance

$D \colon$ a region in the vector space

$D _ { \mathrm { { S } } } \mathrm { { : } }$ the set of regions that overlap with the similarity space of b.

$n \mathrm { : }$ the number of dimensions

$P _ { i } \colon$ the set of blob-to-image pointers to a representative blob $b _ { i }$

$r { : }$ the similarity radius

$\nu \mathrm { : }$ the feature vector of the sample blob

Outputs:

$B _ { \mathrm { S } } \mathrm { : }$ the subset of representative blobs of B that are similar to b

$\textstyle { M _ { \mathrm { S } } } \colon$ the set of images that are similar to b

1. Determine the region $D _ { \mathrm { { L } } }$ that contains the lowest corner of the similarity space:

Let $\phi _ { \mathrm { L } } = < x _ { i } - \Delta x _ { i } , i = 1$ to $n >$ be the lowest corner of the similarity space of b.

Use the $\mathrm { M B ^ { + } }$ -tree to find the region $D _ { \mathrm { { L } } }$ that contains point $\varPhi _ { \mathrm { L } }$ by searching the non-leaf nodes (The search algorithm is similar to that of a $\mathrm { B } ^ { + }$ -tree found in many database textbooks, and therefore omitted here).

2. Determine the region $D _ { \mathrm { U } }$ that contains the highest corner of the similarity space:

Let $\phi _ { \mathrm { U } } = < { y } _ { i } - \Delta { y } _ { i } , i = 1$ to $n >$ be the highest corner of the similarity space of b.

Use the $\mathrm { M B } ^ { + }$ -tree to find the region $D _ { \mathrm { U } }$ that contains point $\varPhi _ { \mathrm { U } }$

3. Find all regions overlapping with the similarity space:

For each region D from $D _ { \mathrm { { L } } }$ to $D _ { \mathrm { U } }$ among leaf nodes of the $\mathrm  M B ^ { + } { - } t r e e \ \left\{ \begin{array} { l l } { \right. } \end{array}$

For each dimension $i , ( i = 1$ to n) {

If Not ${ [ ( x _ { 1 } ^ { \prime } < x _ { 2 } ) }$ and $\left( x _ { 2 } ^ { \prime } > x _ { 1 } \right) ] \left\{ \begin{array} { r l r l } \end{array} \right.$

Found=False;}

If $( \mathrm { F o u n d = T r u e } )$ insert $D$ into $D _ { \mathrm { { S } } } \} \}$

4. Determine the similar blobs and images:

For each region $D \subset D _ { \mathrm { { S } } }$ {

For each $b _ { i }$ in $D \ \left\{ \begin{array} { l l } \end{array} \right.$

$$
d = \left[ \left(v _ {i} - v\right) ^ {T} \sum^ {- 1} \left(v _ {i} - v\right) \right] ^ {1 / 2}
$$

$$
\text {   If   } (d <   C) \{
$$

![](/api/attachments/6E3SCU3G/fulltext/images/c3eeeafd2491020da93568c0138aaac7ba30f16d9e951a67acc965192647b16c.jpg)  
Fig. 7. Semantic-based data organization of an image database.

insert $b _ { i }$ into $B _ { \mathrm { S } }$

insert $P _ { i }$ into $M _ { \mathrm { S } } \} \}$

## 5. Semantic-based data organization for image browsing

In Sections 3 and 4, we developed concepts and algorithms for deriving representative blobs and the image categories and for querying the image database using the multi-dimensional index. In this section, we combine the results in these two previous sections and develop a semantic-based data organization to support image browsing.

## 5.1. Image organization through semantic hierarchy

To organize images in an image database, blobs in the blobworld representation as defined in Section 2 are used to represent image objects. We propose a semantic-based data organization with a three-level model: the semantic hierarchy level, the representative blobs level, the image category level as shown in Fig. 7. The objective of this semantic-based data organization is to support semantic based browsing and index-based search of the image database. The three-level model is achieved by structuring the images into categories, linking them to the corresponding representative blobs, and then coupling the representative blobs to the semantic hierarchy.

The top level of the semantic-based data organization is the semantic hierarchy, which is a tree structure displaying the possible semantics of the representative blobs in the image database. The depth of the semantic tree is dependent of the contents of the image database. For instance, the semantic hierarchy in Fig. 7 contains three semantic levels, the root, the semantic class such as Animals and Vehicles, and semantic entities such as Tiger, Eagle, and Zebra below Animals. The semantic hierarchy provides a user-interface for the user to browse images.

The representative blobs in the second level are linked to the leaf nodes of the semantic hierarchy and provide the connections to the image categories. The feature vectors of the representative blobs are stored in the data organization and can be used for maintaining the image database, including the set of representative blobs, and the image categories.

The third level of the data organization contains the image categories that are generated using the algorithms depicted in Section 4. An image category contains a list of image IDs corresponding to the blobs in the group ranked according to their values of normalized Mahalanobis distance $\mu .$ When the user browses the image database using the data organization, the image IDs are used for retrieving the images physically located on the secondary storage.

The high-level description of the creation of the semantic image database is given below:

Step 1 Generate the semantic hierarchy based on some Metadata or dictionary for the domain of the image database contents.

Step 2 Generate blobworld representation for all images (see Section 2).

Step 3 Generate representative blobs and the corresponding blob groups (see Section 3.1).

Step 4 Create the image categories by linking images to the blob groups (see Section 3.2).

Step 5 Link the representative blobs to the semantic hierarchy.

Step 6 Insert the representative blobs to the $\mathrm { { M B } ^ { + } { - } \mathrm { { t r e e } } }$

## 5.2. Creation of the semantic hierarchy

The semantic hierarchy is domain and application dependent and therefore needs to be designed by domain experts. These types of knowledge cannot be generated automatically and therefore it must be a manual process. However, because this semantic hierarchy most likely remains stable overtime, efficiency is not an issue in this case.

The linking process between the leaf nodes of the semantic hierarchy and the representative blobs must also be done manually. This is because it is not possible to determine the suitable links between a leaf node of the semantic hierarchy and a given representative blob through a computational algorithm. We assume that this linking task can be done by viewing the images of the representative blobs and relate them to the semantic hierarchy. Although this manual process can be tedious, the links remain stable over time once they are established.

## 5.3. Update to the semantic-based data organization

From time to time, additional images are added to the image database. Algorithm 4 provides a method for updating the database.

Algorithm 4. Adding new images into the semantic image database.

Given:

$S _ { \mathrm { r } } \mathrm { : }$ the set of representative blobs

Inputs:

$b _ { \mathrm { n } } \mathrm { : }$ blobs of the new image I

$\nu _ { \mathrm { n } } \mathrm { : }$ sets of feature vectors of the new image I

$n \mathrm { : }$ the total number of blobs

Outputs:

$G _ { \mathrm { s i m i l a r } } .$ the most similar group.

1. For j=1 to n {Compare $b _ { j }$ with blobs in $S _ { \mathrm { r } }$ on the blob index (see Sections 2 and 4) using $\nu _ { j }$ and find the most similar group, $G _ { \mathrm { s i m i l a r } }$

If NO similar group is found {

A new group is created

$b _ { j }$ is the representative blob of the new group.

$b _ { j }$ is inserted into the blob index.

$\}$ Else {

Insert the $b _ { j }$ into the blob chain of $G _ { \mathrm { s i m i l a r } }$

i) Compute the Mahalanobis distance, $\mu$ value between the blob $b _ { j }$ and the representative blob of $G _ { \mathrm { s i m i l a r } }$

ii) Insert $b _ { j }$ into the blob chain according to the calculated $\mu$ value and the pre-calculated $\mu$ values in the blob group.}}

![](/api/attachments/6E3SCU3G/fulltext/images/9e000341efaabca851dcf9094fd6492320e763558bcae1c94f7f9861558aa93d.jpg)  
Fig. 8. Example 1 — insert an image with I.D. 001 into the image database.

Next, we provide an example to show how the data organization is updated as depicted in Fig. 8.

For example, insert a two-object image (I.D. 001) into the image database. The image, the blobworld representation, and the two selected blobs are shown at the top of Fig. 8. Using $\mathrm { M B ^ { + } }$ -tree indexing, we find that blob 1 and blob 2 are similar to the sky and the airplane representative blobs, respectively, in terms of their $\mu \mathrm { \ v a l u e s } \mathrm { ~ - ~ } \mu _ { b l o b l }$ and $\mu _ { b l o b 2 } .$ . Therefore, blob 1 and blob 2 are added to the sky and the airplane groups accordingly. These two blobs are inserted to their respective blob chains according to their $\mu$ values. Note that the $\mu$ values for the blobs are stored to avoid recomputation as indicated in Section 3. The ID of the image is also stored in the blob chain for ease of its retrieval.

## 5.4. Image retrieval by browsing

Section 4 provides the algorithms for CBIR when one or more sample images are provided by the user. However, very often the user might not have the desired sample images, and therefore the image retrieval approach using samples fails. Consequently, it is imperative that the image database management system provides an image browsing facility. The threelevel model developed in this section is designed for this purpose and can be used with the following procedure:

1. The user can start by traversing the semantic hierarchy and locate the interesting semantic classes and semantic entities.

2. Subsequently, the user can move down to the leaf nodes of the semantic hierarchy and view the images corresponding to the representative blobs in order to select the relevant ones.

3. The images in the image categories of the selected representative blobs are then retrieved using the image IDs stored in the blob chain.

4. The relevant images can be finally selected to complete the browsing process.

## 6. Performance analysis of the image retrieval techniques

In this section, we evaluate and analyze three CBIR methods, the naive method, the representative-blobs method, and the indexed-blobs method in order to compare their performances in terms of IO-bound property, and cost. The definitions and setups of the evaluations are given in Sections 6.1 and 6.2. The objective is to show the potential reduction in search costs by using representative-blobs and the MB<sup>+</sup>-tree.

## 6.1. The IO-bound property

In order to model the three image retrieval techniques in a simple manner, we need to determine the IO-bound property of the CBIR. This IO-bound property is not obvious because the computation for comparing blobs is also intensive.

Assume that the feature vectors of all representative blobs are pre-computed and stored on disk. An analytical model for measuring the complexity of a query is given below:

The number of operations can be approximated by $p \times \{ m \times [ 3 9 n + \mathrm { O } ( n \log n ) ] \}$ }, where

p — the number of images in the database

m — the number of blobs per query (mN1 for compound query)

n — the average number of blobs per image

39n — by observation, there are 39n basic operations required

O(nlog n) — the upper bound of heap sort, which is used to determine the minimum.

Let a single blob query (m = 1) operates on a collections of 50,000 images in which each image has n=10 blobs on average. The system would require $5 0 , 0 0 0 \times \{ 1 \times [ 3 9 \times$ $1 0 + ( 1 0 \mathrm { l o g } 1 0 ) ] \} \approx 2 1 \times 1 0 ^ { 6 }$ operations. Running this example on a 200 MHz CPU and assuming one instruction per cycle, the above query can be completed in about 0.1 s. On the other hand, to retrieve the feature vectors of all blobs once with an IO bandwidth of 5 Megabytes (which is very high) will take 29.6 s (≈ 296 [bytes/ blob]×500,000[blobs]/5,000,000 [Megabytes/s]).

The analysis indicates that the image retrieval problem is indeed IO-bound because the cost of retrieving all IO pages is several magnitudes higher than the CPU cost. Therefore, we will ignore the CPU cost in the performance analysis that follows.

## 6.2. Cost functions

The naive method simply takes the sample blob(s) given by the user and compares it with all blobs stored in the database. This requires a scan of all blobs derived from all images in the database. Therefore, the cost function is simply:

$$
\begin{array}{c} \text { Total   IO   Cost } = \text { BlobSize*NumBlobsPerImage* } \\ \text { NumImages / TransRate } \end{array}\tag{1}
$$

Note that although the user may provide multiple sample blobs, the total IO cost is independent of the

Table 2

number of sample blobs, assuming the computation algorithm does not require repetitive access to the same blobs.

The representative-blobs method assumes that all blobs in the database are classified into groups and a representative blob is selected from each group. In the image retrieval process, the sample blob(s) are compared only with the representative blobs in order to reduce the cost of image retrieval. We assume that if the classification is done properly, the quality of the image retrieval results can be satisfactory. A content-based image query requires a scan of all representative blobs, and the cost function for the representative-blobs method is:

$$
\begin{array}{c} \text { Total   IO   Cost } = \text { BlobSize } * \text { RatioRepBlobs } * \\ \text { NumImages / TransRate } \end{array}\tag{2}
$$

where RatioRepBlobs is equal to the number of representative blobs divided by the number of images in the database, i.e., NumRepBlobs/NumImages.

In both the naive and the representative-blobs methods, all blobs are retrieved from the secondary storage to main memory. This can result in severely slow response time. To expedite the image retrieval process, the $\mathrm { \Delta M B ^ { + } }$ -tree can be used to reduce the number of blobs accessed. The indexing search method presented in Section 4 is suitable for this purpose. Next, we develop a cost model for the indexed-blobs method.

The number of regions need to be retrieved for a blobbased image retrieval depends on the size of regions, the size of the similarity space, the feature vector of the sample blob(s) (which determines the location of the similarity space), and the number of sample blobs. We assume that the size of the similarity space is fixed. Because an accurate model for this probabilistic problem is quite complex, we determine an upper bound solution, instead.

For simplicity, we assume that size of the similarity space of the sample blob is smaller than the size of the regions in the vector space of representative blobs. This is a reasonable assumption because for a representative blob to be similar to the sample blob, the Mahalanobis distance must be small on all dimensions. Therefore, the number of regions that can overlap with the similarity space can be either one when the similarity space falls in a region, or two when the similarity space straddles two regions, and so on.

As a result, the maximal number of regions the similarity space can touch is $2 ^ { n }$ , where n is the number of dimensions of the feature vector. This is because when each side of similarity space is shorter than the corresponding side of the regions in the index space, the similarity space can touch at most two regions along each dimension.

Consequently, the following inequality holds for the indexed-blobs method:

$$
\begin{array}{r l} \text { Total   IO   Cost } & \leq \text { PageSize*MaxNumPagesPerQuery } / \\ & \quad \text { TransRate } + \text { SeekTime* } \\ & \quad \text { MaxNumPagesPerQuery } \end{array} \tag {3}
$$

where MaxNumPagesPerQuery = 2<sup>n</sup>, assuming all representative blobs of a region can be stored in one page and the maximum number of regions that needs to be searched is $2 ^ { n }$ as discussed above. The SeekTime is added because one seek is needed for each page retrieved. Note that we also assume that the MB<sup>+</sup>-tree is small enough to be stored in main memory, and therefore the search cost for the index is ignored.

## 6.3. Performance analysis

We conducted a comparative analysis of the three blobbased image retrieval methods. The performance study examines the effects of several important parameters on the efficiency of the three methods. The results can indicate the applicability of each method and demonstrate the advantage of using representative blobs and applying an indexing method in blob-based image retrieval.

The default parameter values used in the performance analysis are given in Table 2. According to [10], the industry standard SCSI bus for nCUBE/2 multiprocessor system results in an effective IO bandwidth from 0.25 to 4 Megabytes per second. Therefore, we use 1 Megabytes per second as the default value for TransRate. We will also analyze the effect of various values in IO bandwidth.

Fig. 9 shows that there is a tremendous difference in total IO cost between the naive method and representative method because the number of representative blobs is 50,000 while the number of stored blobs in the naive method is 4,500,000. Therefore, using the representative method can reduce the query response time by 90 times. In essence, the representative-blobs method pre-computes and classifies all blobs into groups so that the cost required to compare the sample blob and the stored blobs is reduced. Of course, the true cost reduction in specific cases depends on the ratio of representative blobs and the total stored blobs in the naive method. But it is conceivable that this reduction can be very large for an image database in an application area where the number of blobs in each group is large. The figure also indicates that when the IO bandwidth is small to medium, the naive method is too slow to be satisfactory.

Default parameter values for the simulation

<table><tr><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>TransRate</td><td>1</td><td>Megabytes/s</td></tr><tr><td>BlobSize</td><td>296</td><td>Bytes</td></tr><tr><td>NumBlobsPerImage</td><td>9</td><td></td></tr><tr><td>NumImages</td><td>500,000</td><td></td></tr><tr><td>SeekTime</td><td>2</td><td>ms</td></tr><tr><td>PageSize</td><td>4</td><td>Kilobytes</td></tr><tr><td>RatioRepBlobs</td><td>0.1</td><td>NumRepBlobs/NumImages</td></tr><tr><td>MaxNumPagesPerQuery</td><td> $2^6$ </td><td></td></tr></table>

Naive ApproachRepresentative BlobsWith Index  
![](/api/attachments/6E3SCU3G/fulltext/images/ece0d8801fe70ce1e7062fbacf28ec20d3d8d775ef7998badbd48d309f00b3db.jpg)  
Fig. 9. Total IO cost as a function of data transfer rate.

The comparison in total IO cost between the representative-blobs method and the index method indicates also a great deal of savings when an index is used. This is because the multi-dimensional index preserves a natural order of the representative blobs based on the value in the feature vector. As a result, only a small number of the representative blobs need to be retrieved. Although the curve for the index method is for a single sample blob, it is obvious that the cost for the index method is still several magnitudes smaller than the representative-blobs method when a few sample blobs are applied for the query.

![](/api/attachments/6E3SCU3G/fulltext/images/b7d0f2f09120b3c20f402c5a1794b5ef80c9a721c7ed278aee8b74a5025dda52.jpg)  
Fig. 10. Total IO cost as a function of total number of images.

![](/api/attachments/6E3SCU3G/fulltext/images/2ec1baf15afcee85616a89d936c26c44796f3590e36f6e1454ddd2fe36d018e8.jpg)  
Fig. 11. Total IO cost as a function of the ratio of representative blobs and images.

Fig. 10 indicates that the upper bound of the retrieval cost for the index method is independent of the number images (and the number of representative blobs) in the database. This is an important merit of the index method as it indicates that the performance of the index method does not degrade with the growth of the image database. On the other hand, the performance of the naive and the representative-blobs method become worse when the image database grows.

Fig. 11 indicates a similar trend as in Fig. 10 with a different perspective. The representative-blobs method is sensitive to the ratio of the number of representative blobs and the number of images because it requires a scan of all representative blobs for each query. But, the naive method and the index method are insensitive to this parameter.

Fig. 12 shows that the index method is sensitive to the page size because although each query accesses a fixed number of pages, the total IO cost increases when the page size becomes larger. This leads to an important finding, i.e., the size of blob pages should not be too large in order to control the IO cost. It is an interesting research problem to determine the optimal page size for a typical image data application, but it is beyond the scope of this paper.

![](/api/attachments/6E3SCU3G/fulltext/images/9555ba9460b748f68e2bfe4409aa4e9eb9b5d13a0fbaeff464e3ada5eeae31af.jpg)  
Fig. 12. Total IO cost as a function of page size.

## 7. Conclusions

CBIR is one of the most important research areas in image databases. One major development in this area was the automatic identification and classification paradigms using region-based object extraction techniques such as the blobworld approach [3,2]. In a blobworld, portions of image that are relatively homogeneous in image features are extracted from an existing image and are represented as objects, referred to as blobs. The most representative blobs are then used to identify similar images with automatic matching and classification algorithms. However, no attempt has been made in applying the blobworld paradigm in a large-scale image database to support efficient querying and browsing.

In this paper, we proposed a blob-centric image retrieval scheme in image databases that is comprised of several new ideas in image database organization and CBIR using the blobworld representation. Our objective was to develop an image data organization and its related algorithms to support similarity-based image browsing and querying. Another important thrust of our study was to improve the query response time by means of representative-blobs and multi-dimensional indexing. Our main contributions can be outlined as follows:

1. We introduced the concepts of representative blob, blob group, and image category and developed the algorithms for their initialization and maintenance. The purpose of representative blobs is to reduce the search space while providing sufficient quality in image browsing and querying. We also applied the MB<sup>+</sup>-tree index to the blobworld paradigm and developed automatic algorithms for computing similarity-based queries using sample images and blobs.

2. We also developed a semantic-based data organization that allows the user to browse the image database without having to provide sample images. The initialization and maintenance algorithms for the data organization are also given. We suggested that finer classification of the representative blobs can potentially improve the accuracy of automatic classification of images.

3. To assess the potentials on efficiency improvement by applying the representative blobs and the MB<sup>+</sup>-tree indexing, we derived IO-bound cost models for three approaches, the naive method, the representative-blobs method, and the indexed-blobs method. Our research focused on large-scale image databases where efficient retrieval is a challenging issue. The quantitative analysis showed that over 90% reduction in query response time can be achieved in a large image database containing 500,000 images by using the representative-blobs method and the indexed-blobs method.

Some pending further improvements and enhancements on the proposed image retrieval scheme include studies of (1) object representation and formation techniques — what features should or should not be included in object representation for efficient retrieval and management; (2) object category — how to derive the object category and how to determine the relationships among representative blobs and their blob groups. Specific related techniques include shape similarity matching, color object searching, image object recognition, image content representation, visual object tracking, edge comparison, image registration and so on.

## Acknowledgement

We would like to thank C. Carson for providing the programs of the blobworld representation and explanations of some of the intricate points of their approach and system.

## References

[1] S. Belongie, C. Carson, H. Greenspan, J. Malik, Color- and texturebased image segmentation using EM and its application to contentbased image retrieval, Proceedings of the Sixth Internationa Conference on Computer Vision, 1998, pp. 675–682.

[2] C. Carson, M. Thomas, S. Belongie, J.M. Hellerstein, J. Malik, Blobworld: a system for region-based image indexing and retrieval, Proceedings of the Third International Conference on Visual Information and Information Systems, 1999, pp. 509–516.

[3] C. Carson, S. Belongie, H. Greenspan, J. Malik, Blobworld: image segmentation using expectation–maximization and its application to image querying, IEEE Transactions on Pattern Analysis and Machine Intelligence 24 (8) (2002) 1026–1038.

[4] J. Feng, L. Mingjing, Z. Hong-Jiang, Z. Bo, Relevance feedback in region-based image retrieval, IEEE Transactions on Circuits and Systems for Video Technology 14 (5) (2004) 672–681.

[5] M. Flickner, H. Sawhney, W. Niblack, J. Ashley, H. Qian, B. Dom, M. Gorkani, J. Hafner, D. Lee, D. Petkovic, D. Steele, P. Yanker, Query by image and video content: the QBIC system, Computer 28 (9) (1995) 23–32.

[6] I. Gondra, D.R. Heisterkamp, P. Jing, Improving image retrieval performance by inter-query learning with one-class support vector machines, Neural Computing & Applications 13 (2) (2004) 130–139

[7] W.I. Grosky, R. Mehrotra, F. Golshani, H.V. Jagadish, R. Jain, W. Niblack, Research directions in image database management, Proceedings of the Eighth International Conference on Data Engineering, 1992, pp. 146–148.

[8] A. Gupta, R. Jain, Visual information retrieval, Communications of the ACM 40 (5) (1997) 70–79.

[9] A. Guttman, R-trees: a dynamic index structure for spatial searching, Sigmod Record (Acm Special Interest Group on Management of Data) 14 (2) (1984) 47–57.

[10] K.A. Hua, L. Chiang, C.M. Hua, Dynamic load balancing in multicomputer database systems using partition tuning, IEEE Transactions on Knowledge and Data Engineering 7 (6) (1995) 968–983.

[11] K. Idrissi, G. Lavoue, J. Ricard, A. Baskurt, Object of interestbased visual navigation, retrieval, and semantic content identification system, Computer Vision and Image Understanding 94 (1–3) (2004) 271–294.

[12] J.-S.R. Jang, C.-T. Sun, E. Mizutani, Neuro-Fuzzy and Soft Computing: A Computational Approach to Learning and Machine Intelligence, Prentice Hall, 1997.

[13] P.M. Kelly, M. Cannon, D.R. Hush, Query by image example: the CANDID approach, Proceedings of the SPIE — the International Society for Optical Engineering, 1995, pp. 238–248.

[14] B. Ko, H. Byun, FRIP: a region-based image retrieval tool using automatic image segmentation and stepwise Boolean AND matching, IEEE Transactions on Multimedia 7 (1) (2005) 105–113.

[15] S.H. Kwok, An architecture for Web-based image mining and management systems, Journal of Computer Information Systems (JCIS) XXXXIV (1) (2003) 40–47.

[16] D.-H. Lee, H.-J. Kim, A fast content-based indexing and retrieval technique by the shape information in large image database, Journal of Systems and Software 56 (2) (2001) 165–182.

[17] V. Mezaris, I. Kompatsiaris, M.G. Strintzis, Region-based image retrieval using an object and relevance feedback, Eurasip Journal on Applied Signal Processing 2004 (6) (2004) 886–901.

[18] W. Niblack, R. Barber, W. Equitz, M. Flickner, E. Glasman, D. Petkovic, P. Yanker, C. Faloutsos, G. Taubin, The QBIC project: querying images by content using color, texture, and shape, Proceedings of the SPIE — the International Society for Optical Engineering, 1993, pp. 173–187.

[19] J. Nievergelt, H. Hinterberger, K.C. Sevcik, The grid file: an adaptable, symmetric multikey file structure, ACM Transactions on Database Systems 9 (1) (1984) 38–71.

[20] V.E. Ogle, M. Stonebraker, Chabot: retrieval from a relational database of images, Computer 28 (9) (1995) 40–48.

[21] A. Pentland, R.W. Picard, S. Sclaroff, Photobook: content-based manipulation of image databases, International Journal of Computer Vision 18 (3) (1996) 233–254.

[22] B.G. Prasad, K.K. Biswas, S.K. Gupta, Region-based image retrieval using integrated color, shape, and location index, Computer Vision and Image Understanding 94 (1–3) (2004) 193–233.

[23] Y. Qi, A. Vellaikal, S. Dao, MB+/−tree: a new index structure for multimedia databases, Proceedings of the International Workshop on Multi-Media Database Management Systems, 1995, pp. 151–158

![](/api/attachments/6E3SCU3G/fulltext/images/74d9f92252823a9f716a4eb227108533e1d6b0f736d5446dc49e6108cc5f3b2c.jpg)

Dr. Kwok received a BEng (Hons) in Electronic and Communications Engineering (1992) from the University of North London. He received his Diploma of Imperial College (DIC) (1997) from the Imperial College of Science, Technology and Medicine, and his Ph.D. is in Digital Image Processing (1997) from the University of London. He is currently Associate Professor of the Department of Information Systems, College of Business Administration California State

University, Long Beach, and Visiting Associate Professor of the Department of Information and Systems Management at the Hong Kong University of Science and Technology (HKUST). He was visiting scholar and a research assistant in the Department of Electronic and Information Engineering at the Hong Kong Polytechnic University (1994−1995). His research interests include digital watermarking, digital rights management, copyright and intellectual property protection, knowledge management, and electronic commerce applications.

![](/api/attachments/6E3SCU3G/fulltext/images/d1435ecb29d67279b29d2d94b9fee1984214d5a70c4d5123e4633ebd225b7fa9.jpg)

Dr. J. Leon Zhao is Professor and Honeywell Fellow of MIS, Eller College of Management, University of Arizona. He received his Ph.D. from the Haas School of Business, UC Berkeley, and taught previously at College of William and Mary and Hong Kong University of Science and Technology. He holds a PhD in business administration from Haas School of Business, UC Berkeley, MS in engineering from the University of California, Davis, and a bachelor's degree from Beijing

Institute of Agricultural Mechanization. He has published more than 80 articles in major academic conferences and journals including Management Science, Information Systems Research, INFORMS Journal on Computing, Journal of Management Information Systems, Communications of the ACM, IEEE Transactions on Knowledge and Data Management, and IEEE Transaction on Engineering Management. He serves on the editorial boards of seven academic journals including Information Systems Research and Decision Support Systems. In addition, he has edited (or is currently editing) 9 special issues for various MIS journals. He is a co-chair of the Second Workshop on e-Business, 2003, the 15th Workshop on Information Technology and Systems, 2005, and the IEEE International Conference on Services Computing, 2006. He is a recipient of the 2005 IBM Faculty Award for his work in Business Process Management and Service-Oriented Computing.
