---
otero_id: 21265
otero_key: "YAWAQ92R"
title: "Unsupervised clustering for nontextual web document classification"
authors: "Samuel W.K. Chan; Mickey W.C. Chong"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00035-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Unsupervised clustering for nontextual web document classification

Samuel W.K. Chan\*, Mickey W.C. Chong

Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong, Hong Kong, China

Received 19 January 2001; accepted 2 July 2002

Available online 26 March 2003

## Abstract

While the breath of vocabulary used in long documents may mislead the traditional keyword-based retrieval systems, the demands for techniques in nontextual Web classification and retrieval from a large document collection are mounting. Only a few prototype systems have attempted to classify hypertext on the basis of nontextual elements in order to locate unfamiliar documents. As a result, a large portion of Web documents having pictorial information in nature is far beyond the reach of most current search engines. In this research, we devise a novel quantitative model of nontextual World Wide Web (WWW) classification based on image information. An intelligent content-sensitive, attribute-rich image classifier is presented. An image similarity measure is used to deduce the likelihood among images. Different image feature vectors have been constructed and evaluated. Evaluation shows images judged to be similar by human form interesting clusters in our unsupervised learning. Comparison with other clustering technique, such as Hierarchical Agglomerative Clustering (HAC), demonstrates that our approach is found useful in content-based image information retrieval. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Unsupervised clustering; Image classification; Neural networks

## 1. Introduction

Last decade has witnessed one of the dramatic progresses in the area of communication technology. In respect to the well-established information superhighways, researchers have found themselves at the centre of an information revolution ushered in by this Internet age. World Wide Web provides a fast and efficient channel to disseminate information. With the advent of relative economic and large online storage capacities, comprehensive sources of text and image can be stored and made available. It is also hypothesized that images, as one of the major nontextual media, will have taken up more than 70% of Internet traffic in the next decade [19]. In order to scale up the effectiveness of Information Retrieval (IR) in this cyberspace, the stress on content using heterogeneous knowledge in enhancing retrieval functionality is emphasized [2,5]. Current IR can be regarded as a combination of traditional techniques with advanced browsing facilities. However, they support neither content sensitive nor classification of nontextual information. It is indisputable that the challenges in classification of nontextual documents and the demands for the content-based image retrieval, particularly in Web applications, are both mounting.

In recent years, many content-based image retrieval systems have been developed, such as QBIC system [17] and WBIIS system [26], to name a few. The common technique for content-based image retrieval systems is to extract a signature for every image based on its pixel values, color or shape, and to define a classification mechanism for image comparison. Two major classes of signatures are commonly found. First, with the increasing availability of devices supporting acquisition and visualization of color images, a growing attention is being focused on color as a key feature in the signature to characterize the content of archived images. Color histogram technique is a simple but lowlevel method which provides basic indexing and retrieval tasks [8,25]. However, its major tradeoff is that spatial features are completely lost and the spatial relations between parts of an image cannot be thoroughly utilized. On the other hand, different from color histogram techniques, region-based image classification systems attempt to overcome the drawbacks in color-based approach by representing images at object level. As object shape is one of the important features of images, a number of shape representations have been used in many image classification systems. Moment invariant and other simple features, such as line, edge, region and area, are used for shape representation [17].

In this paper, we advocate the integration of various image features into a high-level cognition classification model using a self-organization map. We describe a framework that encompasses both lowlevel features, including color, line segment and region fragment, without demanding any particular image knowledge source to be dominant. A new approach to image feature vector formation and an image similarity measure which is much more appropriate for content-based image clustering are presented. Different levels of abstraction and high-level features, such as the image domain knowledge based on the image templates stored in our image repository, are employed. In addition, since different users may perceive image patterns of the same objects differently and, consequently, may categorize the same objects into different groups, we provide an interactive user interface to capture the user preferences on different image features. These high-level user preferences with a set of image templates encapsulated with a wide range of low-level image features are most appropriately viewed as complementary in our domain of nontextual Web document classification. In the next section, we first review the related work and compare our approach with the existing ones. The overview of system architecture is then discussed in Section 3. The technical details in extracting image signatures are described in Section 4. Details on how image pads can be compared and similarity measures can be deduced are also explained. In Section 5, we introduce a clustering algorithm using neural networks. We employ a self-organization map with associated learning scheme for image classification. Experimental results on different composition of image features are discussed in Section 6 with a comparison with the traditional Hierarchical Agglomerative Clustering (HAC) technique, followed by a conclusion.

## 2. Related work

Cortelazzo et al. [9] describe a trademark shape description based on chain-coding and string-matching technique. In their system, chain codes are not normalized and shape distance is measured using string matching. More recently, a knowledge-based image analyzer is proposed and implemented using object-oriented approach [3,4]. Their system captures the visual knowledge and has been applied in diagnosing medical images in cervical cancer cells. Working toward the text-based classification, Kohonen group has created and maintained a WEBSOM server that demonstrates its ability to categorize several thousand Internet newsgroup items [12]. The SOM-generated categories are found to be comparable to those generated by human subjects [5,20]. Although some other innovative approaches have been proposed [10,27], their main concern emphasizes on the power in image understanding without regarding the iconic characteristic and the relatively low resolution of the Web images. Most of them rely solely on one or a few image attributes. There is an indication on the necessity of generating a better image signature and similarity measure for a sophisticated image information retrieval.

Zhu and Chen [30] report an aerial photograph image retrieval system. The system supports three main functionality, including similarity analysis, region segmentation and image categorization. The system successfully integrates image-processing techniques, such as the Gabor filter with information analysis algorithms like the Self-Organization Map (SOM). The system also enables users to specify their queries by clicking on images and translates their highlevel queries into low-level features. However, they also accept that one major drawback in their system is the insufficiency of image features, since they can only handle one low-level feature, texture, in their system. Similarly, Ma and Manjunath [16] propose a system which includes texture feature extraction, image segmentation, grouping and a texture thesaurus model for search and indexing. Novel features of the system include a fast image segmentation scheme based on texture edge flow and the use of a hybrid neural network algorithm for developing the image texture thesaurus. Similar to the work of Zhu and Chen [30], they have proposed the Gabor texture feature extraction scheme and provided a similarity measure based on the Kohonen map. In addition, similar to parsing text documents using a dictionary or thesaurus, the information within images can be classified and indexed via the use of a texture thesaurus. The texture thesaurus is domain dependent and can be designed to meet the particular need of a specific image data type by exploring the training data. Although the system only relies on one and only one image feature, texture, it is an undeniable achievement of this work that it has brought to light a bold new idea for using a texture thesaurus for browsing a domain specific images.

The QBIC [11] and the Photobook [21] are notable examples of image content-based retrieval systems which make use of several image attributes. The key image features included in their systems are color, texture, shape and motion of images. In addition, a data model is proposed in order to distinguish between scenes and objects. In QBIC, it allows a user to compose a query based on a variety of different visual properties, such as color, shape and texture, which are semi-automatically extracted from images. It partially used the R\*-tree as an image indexing method. In the similar vein, the VisualSeek [23] is another content-based image query system that enables querying by color regions and spatial layout. They devised an image similarity function which contains both color feature and spatial components. However, the devised index structures of each image features were not integrated into a unique content based indexing. The VIPER [18] is another image retrieval system that employs both the color and spatial information. First, they extract a set of dominant colors and then the spatial information bounded by the dominant colors is derived. Similarity is measured in terms of color and spatial information. Two images can be classified as similar if they have a few clusters with the same color that fall in the same image space. Inspired by the above approaches, our system takes a further step in unsupervised clustering of nontextual Web document classification. The following features are the major characteristics of our system. First, unlike most existing content-based image retrieval (CBIR) systems which solely focus either on accurate and speedy retrieval, we concentrate on images and icons, particularly in the Web documents, which are usually smaller in size. It is not too difficult to imagine that human tends to perceive or classify image objects instantly if the images are not big enough. The main reason behind is that human perception relies on different levels of image resolution. Our concept of image pads, which captures both high level of abstraction supported by a set of low-level image details, enable our system to support efficient similarity search in the Web applications. Second, while there is a lot of image retrieval systems which are based on low-level image features, users may perceive patterns on the same objects differently and, consequently, may have different expectation under the same queries. In our system, in addition to implementing a more generic displacement insensitive measure in image comparison with a wide variety of low-level image features, we allow users to incorporate their own preferences in each image attributes so that they can tailor-make their own profiles in image perception. Our system supports three major functionality, including image signatures extraction based on a variety of low level image features, similarity analysis and categorization under user preferences using self organization map.

## 3. System architecture

In this section, we present four main types of application objects in order to provide the intelligent classification capabilities. The four major types include image partition objects, feature extraction objects, classification objects and user interface objects as shown in Fig. 1.

![](/api/attachments/YAWAQ92R/fulltext/images/10c68a4bac20f215c239534fbc8520df14cdbe4e2beb65a7f0cebb1141b29737.jpg)  
Fig. 1. System architecture of the image classifier.

In order to have an efficient image classifier, we first partition all the images which extract from the World Wide Web into a quad-tree image representation in our image partition objects. The quad-tree concept which is a pyramidal image partition has been introduced as a spatial decomposition technique, without regard to the representation of gray-scale intensities at each level. It is on the basis of successive subdivision of the image into quadrants hierarchically. Each partitioned region of an image is further subdivided into four subregions. Mathematically speaking, a pyramidal image partition P is the set of images $P { = } \{ A _ { 1 } , A _ { 2 } ,$ $A _ { 3 } , . . . , A _ { n } \}$ , in each of which image intensity may be denoted as a function with three arguments: a level designator $A _ { i }$ and the two spatial indices of the ith image. That is image $i n t e n s i t y { = } f ( m , n , i )$ , where m and n are spatial indices and i is the level in the pyramid P. Note that the most obvious spatial information exists in the images can be found from the image pads at the upper half of the pyramid, i.e., with significantly lower resolution, while significant details are obtained at the lower half. Using a simple averaging approach, a sequence of 2-D arrays of varying resolution can be created as shown in Fig. 2. In our experiment, we partition all the input images from two different levels of resolution $A _ { 1 } , A _ { 2 }$ with total 20 image pads each having $1 6 \times 1 6$ pixels.

Before proceeding to the image classification objects using the Self-Organizing Map (SOM), we restrict ourselves, among the many possible features that can be extracted from an image, to ones that are global and low-level image signatures. The image signatures involve color, edge, region and texture. A novel algorithm is devised and implemented in order to calculate the similarity between two image pads. The algorithm is not on the basis of Euclidean distance which then provides a nondisplacement sensitive measure in image comparison. The similarity algorithm is applied to various color-based, edge-based and region-based image pads as shown in Fig. 3.

![](/api/attachments/YAWAQ92R/fulltext/images/498e54365aa25a6a8d8ac1546db834b3433c5f594488fa84f27aa2ed0c80f1f0.jpg)  
Fig. 2. Pyramidal image representation with each image pad having 16  16 pixels.

![](/api/attachments/YAWAQ92R/fulltext/images/f9cdb2ca724833657d7b251b69077eac48266bc693498dc893b182833c5541ec.jpg)  
Fig. 3. Image feature extraction objects

By using an image similarity measure method embedded in the feature extraction objects, each input image pad in the partition P is compared with the corresponding image pad in the n template images as shown in Fig. 4. The comparison will be repeated for every image pad in order to identify the image similarity measures for color-based, edge-based and region-based images. As a result, there will have n similarity values which reflect the likelihood among the images in that particular image pad. Each of these image signatures reflects the different aspect of the image. The objective of the classification objects is to cluster the image on the basis of the image signatures as well as the image feature ranking upon user selection. The image feature ranking allows users to modify the composition of the image vectors in order to fine-tune the relative saliency in the human image perception through the user interaction objects. By using a self-organizing feature map (SOM) model proposed by Kohonen [13], the image signatures which usually have more than a few hundred dimensions are then clustered in the classification objects. The classification objects analyze the image signatures and yield connection weights between layers in the map. According to the property of the SOM as thoroughly discussed in Section 4, the connection weights capture the characteristics of the signatures of the input images. Since SOM is on topological feature-preserving basis and compresses the input signature vector in connection weights, of which greatly reduce the size of the input, it is more sophisticated in dimension reduction particularly for the input vectors having a large dimension such as in image classification. As a result, similar images will form a subgroup on the map according to their similarity. Further discussion on the detailed architecture and the algorithm used in the image classifier can be found in the following sections.

![](/api/attachments/YAWAQ92R/fulltext/images/aec5db9fdcbb81fd50e3d2886fec4a52912d7b1c0a769239e87972348a8e6d60.jpg)  
Fig. 4. Image similarity measure between image pads.

## 4. Image signatures extraction

Classification of images by color is generally accounting for the fact that color is the salient feature. In order to quantify the specification of color, we employ the concept of color spaces which define as a formal method of representing the visual sensations of color. A color is represented by a three-dimensional vector corresponding to a position in a color space. Research has been done with a number of different color spaces [6]. The well-known color models are hardware oriented, such as RGB (red, green, blue) model for color monitors and a broad class of color video cameras; the CMY (cyan, magenta, yellow)

model for color printers; and the YIQ model, which is the standard for color TV broadcast. However, all these models are not suitable for classification and retrieval applications. User-oriented models, such as HSV (Hue, Saturation, Value) and HSI (Hue, Saturation, Intensity), are the most popular models. They allow for the manipulation of a color’s features in the same manner in which humans perceive color. In this research, the HSV space which is a bijection of the red–green–blue (RGB) space is adopted. HSV is considered more appropriate than others since it separates the color components (HS) from the luminance component (V) and is less sensitive to illumination changes. The hue describes the actual wavelength of the color, such as blue versus green, while the saturation is a measure of how pure a color is. The hue and saturation components are intimately related to the way in which human beings perceive color while value/intensity component is decoupled from the color information in the image. At the same time, distances in HSV space correspond in a more consistent manner to the perceptual differences in color than in the RGB space. The color information extracted in the rough classification using color grouping exhibits more or less the overall structure of the image. In our image feature extraction objects, the first step in extracting the color attributes is to calculate the RGB values of each pixel in the image pads, and then convert the values to its HSV components. The pseudo-code in Java class for calculating the HSV values is shown in Fig. 5.

```txt
/* Get the average value of HSV in this image segment
* @return the value of HSV by dividing the image
* segment */
public double[] getHSV() {
    Load PIXELS[] from image block
    For each Pixel in PIXELS[] {
    Get RGB value of Pixel
    Convert RGB into HSV
    If Pixel.getSaturation() = 0.0 {
    AccVALUE += Pixel.getValue();
    } else {
    // H value is meaningful only when S > 0
    AccHUE += Pixel.getHue();
    AccSATURATION += Pixel.getSaturation;
    } // Endif
    }
    // Calculate average HSV from AccHSV
    AvgHUE = (double)AccHUE / no_of_pixels;
    AvgSATURATION = (double)AccSATURATION / no_of_pixels;
    AvgVALUE = (double)AccVALUE / no_of_pixels;
}
```  
Fig. 5. Java class in calculating the HSV value in each image pad.

```txt
/* Get the DCT coefficients of this image segment
* and return the values */
public double[] getDCT(int SampleSize) {
    dbSubSource1 = SegmentImage.getData().getDataBuffer();

    // Calculate DCT on the sample area and store
    values into aDCT
    DiscreteCosine(dbSubSource1, aDCT1,
    SegmentWidth, SampleSize, 1);

    // Extract values inside the sample area
    // and put into aResult
    for (int k = 0, i = 0; i < SampleSize; i++)
    for (int j = 0; j < SampleSize; j++, k++)
    aResult[k] = aDCT1[i * SegmentWidth + j];
    return aResult;
}
```  
Fig. 6. Java class in calculating the DCT coefficients in image pads.

Other than the color information encoded in the image, Discrete Cosine Transform (DCT) coefficients are also extracted from each image pad in order to compare the texture similarity of images. Loosely speaking, DCT reflects the overall structure of the images and provides details regarding their spatial frequency content. The low frequency components can characterize the coarseness of the image. It is also the reason why the low frequency components of the image signal will only be emphasized in our DCT coefficients extraction while the high frequency image information, such as edges and lines, will be tackled in the later edge extraction process. Our DCT methods start by breaking the images into $1 6 \times 1 6$ pixel blocks or $3 2 \times 3 2$ pixel blocks where all the pixel blocks are analyzed separately in the feature extraction objects. After the transformation, each block is compressed into 4 bytes. Since the DCT is lossy operation, the resulting output will no longer be identical in their information carrying roles before the transformation. The larger the coefficients, the more alike the transformed image are to the original image. As the result, the coefficients reflect the image textual. As described in Fig. 6 below, the DCT coefficients are calculated for all the image pixels in the image pad. The detailed pseudo-code for analyzing the textual analysis using DCT is shown as follows.

In addition, most image information used to describe an image is closely related to the similarity measure. There is a lot of on-going work in developing new measures for comparing images for various objectives in image retrieval and evaluation [29]. However, most of them rely on the Euclidean distance between two sets of object pixels as a means of evaluating the numerical difference between two images. Different from other Euclidean distance measure in image comparison, we employ an Image Similarity Measure (ISM), which makes use of intensity center of an image as the key parameter for computing the similarity values [7]. The algorithm provides a displacement insensitive measure in image comparison. In order to calculate the ISM, an intensity center $\scriptstyle \mu = \left( \mu _ { r } , \mu _ { s } \right)$ of an image is first defined, such that,

$$
\min \left(\sum_ {i = 1} ^ {\mu_ {r}} \sum_ {j = 1} ^ {m} \partial g (i, j) - \sum_ {i = \mu_ {r}} ^ {m} \sum_ {j = 1} ^ {m} \partial g (i, j)\right)\tag{1}
$$

$$
\min \left(\sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {\mu_ {s}} \partial g (i, j) - \sum_ {i = 1} ^ {m} \sum_ {j = \mu_ {s}} ^ {m} \partial g (i, j)\right)\tag{2}
$$

where $\partial g ( i , j ) = | g _ { a } ( i , j ) - g _ { b } ( i , j ) |$ is the absolute difference between the two images a and b, calculated pixel by pixel. The algorithm takes two image matrices and calculates the similarity between two image matrices as shown in Table 1. The input to the algorithm is the two images that are being compared. The difference image matrix is calculated for any pixel in image A relative to the same pixel in image B. Clustering is performed, based on the difference matrix, by comparing the surrounding pixels within a predefined window with the intensity center $( \mu _ { r } , \ \mu _ { s } )$ in order to get the minimum distance between the compared pixels. This process is repeated until all the pixels of the difference image within the predefined window have been processed. From the average minimal pixel distance, the final dissimilarity for the whole image is calculated.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 1
Algorithm of image similarity measure

INPUT Image A and Image B gray-level matrices
DETERMINE size of window, N
COMPUTE difference matrix based on A &amp; B
SEARCH the intensity center as described in Eqs. (1) and (2)
INITIALIZE sum
DO WHILE pixel  $(i, j)$  within the window
COMPUTE
 $F(i, j) \leftarrow \frac{\partial g(i, j)}{1 + \lambda} \left\{ \lambda^{2}(i - \mu_{r})^{2} + \lambda^{2}(j - \mu_{s})^{2} + \partial g^{2}(i, j) \right\}^{\frac{1}{2}}$ 
CALCULATE sum  $\leftarrow$  sum +  $f^{2}(i, j)$ 
ENDDO
OUTPUT
ISM(A, B)  $\leftarrow \frac{1}{N} \sqrt{sum}$
</div>

In our simulation, two different types of gray-scale images are used to compare the similarity measures with a set of predefined image templates. Both edge images and intensity-based region images are involved. Edges provide useful information about an image. Edge detection methods are used as a first step to identify complex object boundaries by marking potential edge points corresponding to places in an image where rapid changes in brightness occur. An edge detector is a high-pass filter which outputs an edge image with mainly high frequency information using differential operators. Differential operators measure the rate of change in a function, in this case, the image brightness function. A large change in image brightness over a short spatial distance indicates the presence of an edge. Convolution masks have been used with considerable success for the task of differential operation and is one of the classical image processing algorithms commonly used for identifying image features. A convolution mask is a discrete approximation to a two-dimensional convolution integral. The convolution operation replaces a pixel’s value with the sum of that pixels value and its neighbors, each weighted by a factor. The weighting factors are called the convolution kernel. To convolve an image area, a sliding kernel matrix operates over each row of pixels in the matrix image. At each point, the kernel values multiply the image values under it, sum the result, and replace the pixel at the center of the kernel with the value. In this research, we employ the Sobel kernel, which looks for edges in both horizontal and vertical directions, and then combine this information into a single metric. The masks are shown as follows:

$$
\left[ \begin{array}{c c c} - 1 & - 2 & - 1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{array} \right] \quad \left[ \begin{array}{c c c} - 1 & 0 & 1 \\ - 2 & 0 & 2 \\ - 1 & 0 & 1 \end{array} \right]
$$

In the system, the Sobel filter followed by a threshold operation is applied to generate the edge images. Sobel edge detector yields the magnitude and direction of edges by applying the row and column masks. On the other hand, as opposed to the edge detection using convolution kernel, we apply the regional approaches which attempt to segment an image into regions according to regional image data similarity (or dissimilarity). For example, images containing light objects on a dark background or dark objects on a light background can be segmented by means of a simple threshold operation. The following relationship exists between the input image f(m, n) and the output image g(m, n):

$$
g (m, n) = \left\{ \begin{array}{l l} I _ {1} & 0 \leq f (m, n) <   S \\ I _ {2} & S \leq f (m, n) \leq f _ {\max} \end{array} \right.\tag{3}
$$

where $I _ { 1 }$ and $I _ { 2 }$ are two arbitrary values with $I _ { 1 } \ne I _ { 2 }$ (usually $I _ { 1 } = 0 , \ I _ { 2 } = 1$ are selected), and S is the intensity threshold to be used. By choosing a suitable $S ,$ pixels with value $I _ { 1 }$ in the output image represent the objects and those with the value $I _ { 2 }$ represent the background. Moreover, we also employ a region growing technique, called pixel aggregation, in identifying the possible regions in the gray-scale images. Pixel aggregation starts with a set of seed points. Regions are grown by appending those similar neighboring pixels to the seeds. Seeds are selected from the gray level histogram with the most predominant values. Although typical region analysis must be carried out with a set of descriptors based on intensity and spatial properties, such as moments, only intensity-based regions are used in our simulations to compare with the existing templates in order to devise the region-based similarity measures. In sum, Table 2 details the possible attributes extracted in the formation of our heterogeneous image signatures. It is not difficult to visualize the dimension of our image signature vectors can be very huge, and it is out of the capacities of most current clustering algorithms. In the next section, we shall discuss how the vectors can be classified using a neural network model.

Possible image attributes in the heterogeneous image signature database

<table><tr><td>Image attributes</td><td>Property values</td></tr><tr><td>Color</td><td>Hue, saturation, value</td></tr><tr><td>Texture</td><td>DCT coefficients</td></tr><tr><td>Edge</td><td>Similarity with templates</td></tr><tr><td>Region</td><td>Similarity with templates</td></tr></table>

## 5. Classification using self-organization map (SOM)

It has been postulated that human brain uses spatial mapping to model complex data structure internally. Much of the cerebral cortex is arranged as a twodimensional plane of interconnected neurons but it is able to deal with concepts in much higher dimensions. The characterization of topological feature-preserving maps has received special attention in the literature [14,15,24]. In particular, Amari [1] studied a continuous-time dynamical version of this map extensively to investigate the topological relation between the self-organizing map and the input space governed by the density p(x), the resolution and stability of the map and the convergence speed.

The self-organization map, developed by Kohonen [13], is an unsupervised two-layer neural network used for classification and dimensional reduction. It is a biologically motivated method for constructing a structured representation of data from an often highdimensional input space. The goal of the SOM is to create a mapping between the input stimulus space and the output space. It is well-known for its unsupervised learning, organizing and visualizing information. An advantage of SOM over other clustering algorithms is its ability to visualize high-dimensional data using a two-dimensional grid while preserving similarity between data points as much as possible. SOM performs data compression, from multidimensional data to a much lower-dimensional space, on the vectors to be stored in the network using a technique known as vector quantization. Vector quantization is the most important technique in competitive learning. The main idea is to categorize or distribute a given set of input vectors into classes, and then represent any vector just by the class into which it falls. The algorithm employs a set of neurons which are arranged in a network of a certain dimensionality. The implementations of Kohonen’s algorithm are predominantly in a two-dimensional plane which is shown in Fig. 7.

![](/api/attachments/YAWAQ92R/fulltext/images/ed37c92e605a7c54caaf53a91a00c7e078b5d3ca6d5243e40318564ec7d42231.jpg)  
Fig. 7. Self-organization map in which there is one and only one layer of neurons and all inputs are connected to all nodes in the map.

The network shown is a one-layer, two-dimensional Kohonen network. The most obvious point to note is that the neurons are not arranged in layers as in a backpropagation network, but rather on a flat grid. All inputs connect to every node in the network. Feedback is restricted to lateral interconnections to immediate neighbouring nodes. The learning algorithm organizes the nodes in the grid into local neighbourhoods that act as feature classifiers on the input data. The topographic map is autonomously organized by a cyclic process of comparing input patterns to vectors stored at each node. No training response is specified for any training input.

In our experiment, each image is characterized by the 20 image pads, having the attributes as shown in Table 2. Each of them forms a signature vector and stores in the heterogeneous image signature database. In order to classify the images according to their categories, the vectors are then feed forward to a self-organization map (SOM) as shown in Fig. 7. The details of the training algorithm are shown in Table 3.

SOM has two properties found useful in our classification objects. First, it quantises the space like any other vector quantisation methods, and constitutes an image classification. The topology preserving property of SOM, coupled with our extracted image attributes, constitutes a powerful and human stimulated image classifier. Second, our attribute-rich and huge dimension image signature vector can be visualized and clustered through the map while the other clustering techniques may suffer from the high dimensionality generated from the images. As can be seen in the following section, its performance is much better than other classification technique.

<table><tr><td>Learning algorithm of the self-organization neural network</td></tr><tr><td>(1) Initialize networkDefine  $w_{ij}(t)$  to be the weight from input  $i$  to node  $j$  at time  $t$ .Initialize weights from the  $n$  inputs to the nodes, as shown in Fig. 7 with small random values. Set the initial radius of the neighborhood around node  $j$ ,  $N_j(0)$ , to be large.(2) Present inputPresent input  $x_0(t)$ ,  $x_i(t)$ , ...,  $x_{n-1}(t)$ , where  $x_i(t)$  is the input to node  $i$  at time  $t$ .(3) Calculate distancesCompute the distance  $d_j$  between the input and each output node  $j$ , given by $d_j^2 = \sum_{i=0}^{n-1} (x_i(t) - w_{ij}(t))^2$ (4) Select minimum distanceDesignate the output node with minimum  $d_j$  to be  $j^*$ (5) Update weightsUpdate weights for node  $j^*$  and its neighbours, defined by the neighbourhood function,  $N_j^*(t)$ . New weights are  $w_{ij}(t+1) = w_{ij}(t) + \eta(t)(x_i(t) - w_{ij}(t))$  for all  $j$  in  $N_j^*(t)$  and  $0 \leq i \leq n-1$ . The term  $\eta(t)$  is a gain ( $0 < \eta(t) < 1$ ) that decreases in time, thus, slowing the weight adaptation. The neighbourhood  $N_j^*(t)$  decreases in size as time goes on, thus, localizing the area of weight change.(6) Repeat by going to step (2) for a number of iterations.</td></tr></table>

## 6. Experiments and evaluation

To study the performance of the above-described image classifier, we have implemented a system having a hundred target images. Each target image downloaded from the WWW is $6 4 \times 6 4$ in size with maximum gray level of 256 and all are in GIF format. In our experiment, one target image is selected from each domain as an image template. While the target images and templates are stored in Image Graphical Database, all the image signature vectors generated will be accumulated in the Image Signature Vector Repository. Fig. 8 shows the UML state diagram of the image classifier.

As shown in Fig. 8, the size 64  64 target image is first partitioned into four $A _ { 1 }$ image pads which are then further subdivided into sixteen $A _ { 2 }$ image pads. All image primitives of each image pad are extracted through different methods in various activities. The activity Calculate Color is to identify the average HSV, activity Calculate DCT is to compute the DCT coefficients while activity Calculate IS Measure is to compare the similarity measures between the target image and the templates. The activity Image Convolution is responsible to process both vertical and horizontal convolution of each target image before determining the similarity. Without any bias between different image signatures, normalization which is done in such a way that all values of the image primitives lie between [0, 1] is performed before the training in SOM. The normalized image vectors are accumulated in our Image Signature Vector Repository as shown in Fig. 8. Before generating the topological classification in the SOM, other training parameters, such as the number of epochs and the dimension of grid layer in the SOM, have to be defined. These parameters are adjusted in order to locate the optimal result. A CSV format file is then created as an output which is then subject to further comparison and evaluation.

![](/api/attachments/YAWAQ92R/fulltext/images/92e63936f6102491832a32f3f14c7811eaf1ba8931f2b8e1423536b773e11fba.jpg)  
Fig. 8. State diagram of the image classifier.

Different users may perceive image patterns on the same objects differently and, consequently, may categorize the same objects into different groups. In our system, in addition to implementing a more generic displacement insensitive measure in image comparison with a wide variety of low level image features, we allow users to incorporate their own preferences in each image attributes so that they can tailor-make their own profiles in image perception. We provide an interactive user interface to capture the user preferences on different image features. Fig. 9 shows the user interface of the system. Basically, the interface is divided into three major components: Image browser, File list panel and Control panel. Users can view all images through the browser. At the same time, it allows users to add and remove images in the file list panel. The amendment will be reflected instantly in the browser. More importantly, through the control panel, users can adjust different weights for different image primitives in the combo boxes as shown in Fig. 9. This is one step forward towards the stimulation of the performance of image classification in a humanlike manner and understanding how users achieve similarity within that domain and then building a system that duplicates human performance. These high-level user preferences with a set of image templates encapsulated with a wide range of low level image features are more usefully viewed as complementary in our domain of nontextual Web document classification.

![](/api/attachments/YAWAQ92R/fulltext/images/36bbdc3283a1672253508cbfddf2ed81e0d137dda83bb07f7204d9ac3ad454dd.jpg)  
Fig. 9. User interface of the unsupervised image classifier.

In our experiment, hundred images from seven categories are retrieved through the Web. The categories include fruit, scenery, mobile phone, Clinton, flower, airplane and cartoon as shown in Appendix A. Images P01, P23, P35, P56, P61, P79 and P93 are selected as the image templates in our experiment. In the training of SOM, the weight factors for color and image similarity are set to be three and one, respectively, while the other is set to zero in the level of low resolution. However, the weight factor for color is set to three and the rest is set to one in high-resolution level as in $4 ^ { 2 } \ A _ { 2 }$ image pads. Without any bias, the contributions from color and noncolor attributes are equal. The SOM with 1600 neurons organized on a two-dimension lattice with 40  40 grid is used for the training. The number of neurons used here is empirically determined by considering the number of similar clusters in the training sets. After the adaptation phase in the training of the SOM in 5750 epochs, the connection weights are fixed. Each 636-dimension image signature vector is presented to the network and the winning unit is labeled with the code of the corresponding image. After the presentation of all the 100 image signature vectors with 2000 subimages, a SOM is obtained. The map reflects a certain order which is a representative of the similarities and the differences between the images. As shown in Fig. 10, the images are clustered in a way that emphasizes the grouping between images. The SOM captures the family relationships among the images which are likely to be grouped together under the same category.

![](/api/attachments/YAWAQ92R/fulltext/images/1ff6519a2d29a9438f0ac1fff35b31afb4447ff34ce3a63997ae3c7b19640bfa.jpg)  
Fig. 10. Image clusters formed after the training in SOM in 40  40 grid.

In the image map, it is not difficult to find out that the images with light background, such as the categories of mobile phone and cartoon are grouped together while the opposite regions correspond to images with dark backgrounds. Due to the different background in the category fruit, they are further split into two parts located at the upper left-hand and lower right-hand side in the map. The subdivision is mainly due to different texture of the background in these images. The complexity of scenery-categorized image signatures makes them be positioned at different regions in the map. Generally speaking, the images with brighter background are located at the upper portion of the map with further subdivision based on their categories. Fig. 11 shows another map generated in which color attribute HSV of the $4 ^ { 2 } A _ { 2 }$ image pads is reduced. In the training, weight factor of the HSV is set to be one with the others unchanged. The vectors become stable after 6500 epochs in a grid of $4 0 \times 4 0$ Similarly, images with bright background P33–P48 and P85 –P95 are clustered together at the lower right side of the map. However, the map cannot distinguish the category fruit, scenery and flower well as in Fig. 10. Color seems to be most dominant attribute in clustering WWW images which are iconic-based and have a relatively low resolution.

The human perception of images is subjective and, in fact, different persons may have different perception criteria. While it is recognized that images are best described through color, lines and shapes of objects in the scene, one of the main objectives in this paper is to argue that integration of these different

![](/api/attachments/YAWAQ92R/fulltext/images/eed25d52d6a6ae228acdda2004f84160b129c65300a73288e44e3c48448f7aaf.jpg)  
Fig. 11. Clusters formed in SOM while the weights of color attribute are reduced.

image features via a self-organization map enhances the human perception in image classification. In order to justify the performance of our system in utilizing a wide range of image features, we repeat the experiment for every single image features. Since line segment, region fragment and color are the fundamental aspects of human perception, we compare the SOMs generated from all these three image features individually. Fig. 12 shows the SOM generated from a single input image attribute of line segment. The images being considered in the same categories under human perception are grouped under the same clusters. This classification is done manually in our laboratory. The 100 images are groups into 43 image clusters, each of them having one to seven images. It is worth to mention that more than half of the clusters have only one image. While it is possible in SOM that same set of image vectors might come up with slightly different clusters, our experiment indicates that the classification using a single image feature from line segments is unsatisfactory as compared with the result we obtained in Fig. 10.

Figs. 13 and 14 illustrate another experiments which measure the contribution from region fragments and color attributes respectively. There are 35 and 28 image clusters in Figs. 13 and 14, respectively. While the results look more acceptable than the result we obtained in Fig. 12, the percentage of single-image clusters remains high. Images under the categories mobile phone, fruit and flower are scattered around in the map, even through they all have a clear background and foreground colors as shown in Fig. 13. As compared with the SOM generated solely from line segments and region fragments, the SOM

![](/api/attachments/YAWAQ92R/fulltext/images/1e83c54dd73763ad8ad8edcc8accf1afa8e201371ffded038082e39bb21bde53.jpg)  
Fig. 12. Clusters generated in SOM with a sole input image attribute from line segment.

![](/api/attachments/YAWAQ92R/fulltext/images/a326dd230ea26cdca5e263dd82751514e1bbbdb8763b540203a3fac43ad32a5f.jpg)  
Fig. 13. Clusters generated in SOM with a sole input image attribute from region fragments.

from color attribute provides a more reasonable result, with at least the entire group of images under the category fruit located at the second quadrant of the map as shown in Fig. 14. Similarly, the images under the category airplane can also be found situated at the fourth quadrant of the map. However, while color is believed to be the most dominant image attribute than all others, our approach using more than one image features is a superior approach in image classification. Fig. 10 shows that images with similar background, in terms of color, region fragments and line segments, are grouped together. The clusters generated are more concise with fewer singletons as compared with Fig. 14. This comparison shows our content-sensitive, attribute-rich image classifier provides an efficient classification, particularly in Webbased applications. In addition to classifying visually similar images, a potential advantage of this approach is that it provides an efficient indexing mechanism to narrow down the search space, through the weights trained in the SOM.

On the other hand, in order to evaluate the performance of the classification ability of the selforganization map, we compare our result obtained from the SOM with a classical Hierarchical Agglomerative Clustering (HAC) algorithm. HAC is an iterative procedure in which clusters are merged into one bigger cluster according to a distance function. Two clusters with least discrepancy are first identified and merged together.

In our application, we start with some trivial clusters in which each cluster represents a single image. Two closest clusters according to the distance function are first been identified. They are merged into a single cluster. The process repeats until the desired number of clusters is reached. In fact, there are many different measures for combining the clusters. The one that we employed in the experiment is group-average clustering in which the combined dissimilarity of two clusters is the average of all dissimilarities between members of each cluster [22,28]. This function measures the cluster dissimilarity using a weighted squared distance between the two cluster centers $\mu _ { i }$ and $\mu _ { j }$

![](/api/attachments/YAWAQ92R/fulltext/images/6565c5bc77af4e32e45a5ec82d49b93bc6aa617f0059806882381f568520d4fd.jpg)  
Fig. 14. Clusters generated in SOM with a sole input image attribute from color.

$$
\frac {2 n _ {i} n _ {j}}{n _ {i} + n _ {j}} \left\| \mu_ {i} - \mu_ {j} \right\| ^ {2}\tag{4}
$$

where $n _ { i }$ and $n _ { j }$ represent the cardinalities of clusters i and $j .$ Fig. 15 shows dendrogram produced by the HAC algorithm using the between-groups linkage cluster method. In the HAC dendrogram, the images in categories mobile and cartoon are grouped together at the upper branch. The main reason behind is the bright background in these images. It is also worth to note that images of Clinton P49, P50, P51, P52 and P56 are clustered together. However, images under the category scenery are scattered into different branches of the tree. While images P17 to P20 having similar image signatures are clustered together, there is a lot of misclassification using the HAC algorithm. Same phenomenon occurs in the images under flower category. The situation becomes even worse if the same distance measure with other cluster method is used in the HAC as shown in Fig. 16.

When the two results obtained in SOM and HAC are compared, it can be observed that the image under categories mobile phone and cartoon cannot be distinguished sharply in both algorithms. While the images in fruit are under examined, we can find out that both algorithms separate the images into two major subgroups by differentiating their image background. Interestingly, they all show the same clustering of Clinton images. However, the classification result in SOM seems to be much better than the one in HAC. While the HAC is a linear method in which relative distances between clusters reflects some dissimilarity among images, the Kohonen algorithm realizes a projection on a surface spanned by the network topology. This is completely defined by the relation of order between the neurons: a simple onedimensional relation or a bidimensional one. The method of self-organizing maps is an original dimension reduction method. It has no real statistical analog and, thus, can be very useful for specific applications where linear methods fail. From a computational point of view, HAC is a global operation while the Kohonen algorithm is sequential process which does not require any global information. Global order between the data will reappear in the map after a small number of iterations if there is any local modification occur.

![](/api/attachments/YAWAQ92R/fulltext/images/26ed437f71cb543cf94934d9e81c2c5e1567b80d16e27efaeee805d5284b488f.jpg)  
Fig. 15. Dendrogram using between-groups linkage cluster method.

![](/api/attachments/YAWAQ92R/fulltext/images/91c1a5822d4e4e0ea688108ca1d91433a874e8152fa473d809adf7e6c08fb34c.jpg)  
Fig. 16. Dendrogram using within-groups linkage cluster method.

## 7. Conclusion

With the proliferation of multimedia computing into the ubiquitous computers, image data will certainly be another important medium in future computing. Though there has been considerable research in the area, the investigations have been carried out in restricted domains and addressed only certain aspect of the content-based information retrieval. In this research, we have presented an approach to classify images based on a self-organization map. The agent integrates different image primitives into the classification procedure without demanding any particular primitive to be dominant. We have evaluated the approach using hundred images. The system implemented and the results generated provide discrimination clusters. Evaluation shows that similar images will fall onto the same region, in such a way that it is possible to retrieve images under family relationships. This approach performs particularly well in the classification for nontextual WWW documents, which inherently have high-dimensional input spaces.

## Acknowledgements

The work described in this paper was fully supported by a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China (Project No: CUHK4171/01E) and a direct research grant of the Chinese University of Hong Kong.

![](/api/attachments/YAWAQ92R/fulltext/images/85f79acf997fa4b953479542ca3d2e26780a9d2ee02a981d78405119b92f1806.jpg)

## References

[1] S.-I. Amari, Field theory of self-organizing neural nets, IEEE Transactions on Systems, Man and Cybernetics SMC-13 (1983) 741 – 748.

[2] S.W.K. Chan, Using heterogeneous linguistic knowledge in local coherence identification for information retrieval, Journal of Information Science 26 (5) (2000) 313– 328.

[3] S.W.K. Chan, K.S. Leung, W.S.F. Wong, An expert system for the detection of cervical cancer cells using knowledge-based image analyzer, Artificial Intelligence in Medicine 8 (1996) 67 – 90 (Elsevier Science).

[4] S.W.K. Chan, K.S. Leung, W.S.F. Wong, Object-oriented knowledge based system for image diagnosis, Applied Artifi cial Intelligence 10 (1996) 407 – 438 (Taylor & Francis).

[5] S.W.K. Chan, J.L.L. Yeung, M.W.C. Chong, An image classification agent using hierarchical overlapped self-organization map, Proceedings of the Symposium on Computational Intelligence, ICSC Congress on Intelligent Systems and Applications (ISA’2000), University of Wollongong, Australia, 2000.

[6] E.J. Charles, A. Finkelstein, D.H. Salesin, Fast multi-resolution image querying, Proceedings of SIGGRAPH 95 (1995) 277– 286.

[7] K.J. Cios, I. Shin, Image recognition neural network: IRNN, Neurocomputing 7 (1995) 159– 185.

[8] J.M. Corridoni, A. Del Bimbo, P. Pala, Image retrieval by color semantics, Multimedia Systems 7 (1999) 175 – 183.

[9] G. Cortelazzo, G.A. Mian, G. Vezzi, P. Zamperoni, Trademark shapes description by string matching techniques, Pattern Recognition 27 (8) (1994) 1005– 1018.

[10] M. Das, R. Manmatha, E.M. Riseman, Indexing flower patent images using domain knowledge, IEEE Intelligent Systems 14 (5) (1999) 24 – 33.

[11] M. Flickner, H. Sawhney, W. Niblack, J. Ashley, Query by image and video content: the QBIC system, IEEE Computer 28 (9) (1995) 23 – 33.

[12] T. Honkela, S. Kaski, T. Kohonen, K. Lagus, Self-organizing maps of very large document collections: justification for the WEBSOM method, Proceedings of the 21st Annual Conference of the Gesellschaft fur Klassifikation e.V, (Classification, Data Analysis, and Data Highways), Springer-Verlag, Berlin, Germany, 1998, pp. 245 – 252.

[13] T. Kohonen, The self-organization map, Proceedings of the IEEE 78 (1990) 1464– 1480.

[14] T. Kohonen, Physiological interpretation of the self-organizing map algorithm, Neural Networks 6 (7) (1993) 895 – 905.

[15] Z.-P. Lo, Y. Yu, B. Bavarian, Analysis of the convergence properties of topology preserving neural networks, IEEE Transactions on Neural Networks 4 (2) (1993) 207–220.

[16] W.-Y. Ma, B.S. Manjunath, A texture thesaurus for browsing large aerial photographs, Journal of the American Society for Information Science 49 (7) (1998) 633– 648.

[17] W. Niblack, R. Barber, W. Equitz, M. Flickner, E. Glasman, D. Petkovic, P. Yanker, C. Faloutsos, G. Taubin, QBIC project: querying images by content using color, texture and shape, Proceedings of SPIE 1908 (1993) 173 – 187.

[18] B.C. Ooi, K.L. Tan, T.S. Chua, W. Hsu, Fast image retrieval using color-spatial information, The VLDB Journal 7 (2) (1998) 115 – 128.

[19] A. Ortega, F. Carignano, S. Ayer, M. Vetterli, Soft caching: web cache management techniques for images, IEEE Signal Processing Society 1997 Workshop on Multimedia Signal Processing, IEEE, WY, USA, 1997, pp. 475– 480.

[20] R.E. Orwig, H. Chen, J.F. Nunamaker, A graphical, self-organizing approach to classifying electronic meeting output, Journal of the American Society for Information Science 48 (2) (1997) 157– 170.

[21] A. Pentland, R.W. Picard, S. Sclaroff, Photobook: tools for content based manipulation of image databases, Proceedings of the International Society for Optical Engineering 2185 (1994) 34– 47.

[22] B.D. Ripley, Pattern Recognition and Neural Networks, Cambridge Univ. Press, Cambridge, UK, 1996.

[23] J.R. Smith, S.-F. Chang, VisualSEEK: a fully automated content-based image query system, Proceedings of the ACM Multimedia (1996) 87 – 98

[24] V. Tolat, An analysis of Kohonen’s self-organizing maps using a system of energy functions, Biological Cybernetics 64 (1990) 155– 164.

[25] V. Vinod, H. Murase, Focused retrieval of color images, Pattern Recognition 30 (10) (1997) 1787– 1797.

[27] J.Z. Wang, J. Li, D. Chan, G. Wiederhold, Semantics-sensitive retrieval for digital picture libraries, D-Lib Magazine 5 (1999) 11.

[26] J.Z. Wang, G. Wiederhold, O. Firschein, X.W. Sha, Contentbased image indexing and searching using Daubechies’ wavelets, International Journal of Digital Libraries 1 (4) (1998) 311– 328.

[28] J.H. Ward, Hierarchical grouping to optimize an objective function, Journal of the American Statistical Association 58 (1963) 236– 244.

[29] D.L. Wilson, A.J. Baddeley, R.A. Owens, A new metric for grey-scale image comparison, International Journal of Computer Vision 24 (1) (1997) 1 –29.

[30] B. Zhu, H. Chen, Validating a geographical image retrieval system, Journal of the American Society for Information Science 51 (7) (2000) 625 – 634.

Samuel W.K. Chan received his MSc degree in 1986 from the University of Manchester, UK, his MPhil degree in 1991 from the Chinese University of Hong Kong and his PhD degree in 1998 from the University of New South Wales, Australia—all in Computer Science. Before joining the Chinese University of Hong Kong, he has been working in computational intelligence since 1989. His current research interests are in applying machine learning techniques in image and text, data mining, information retrieval and multimedia information processing with emphasis on image and text. He has published articles in IEEE Transactions on Neural Networks, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man and Cybernetics, Journal of Information Science, Machine Translation, International Journal of Computer Processing of Oriental Languages, Artificial Intelligence in Medicine, Applied Artificial Intelligence and others.
