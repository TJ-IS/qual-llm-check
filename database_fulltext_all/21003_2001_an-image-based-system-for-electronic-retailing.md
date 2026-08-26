---
otero_id: 21003
otero_key: "RK5AQ38J"
title: "An image-based system for electronic retailing"
authors: "Aryya Gangopadhyay"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00105-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An image-based system for electronic retailing

Aryya Gangopadhyay

Department of Information Systems, UniÕersity of Maryland Baltimore County, 1000 Hilltip Circle, ACIV 481, Baltimore, MD 21250, USA

## Abstract

The purpose of this paper is to describe a methodology for enhancing search and retrieval of product information using content-based image retrieval in an electronic retailing application. Content-based image retrieval techniques have been applied to various applications such as medical information systems, environmental modeling, and satellite image analysis. Such techniques, however, can also be useful in electronic commerce applications such as electronic retailing, by enhancing product search and computer-assisted sales. In this paper, we describe an application of CBIR in electronic retailing using color and texture matching techniques. We describe a prototype system in the context of the apparel industry. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Content-based image retrieval; Electronic retailing; Electronic commerce; Image analysis; Computer-assisted sales

## 1. Introduction

Electronic retailing e-tailing is one of the keyŽ . applications of electronic commerce e-commerce .Ž . It entails providing an electronic storefront to allow customers to search for products, submit orders online, and have orders shipped directly to their receiving address. E-tailing has become popular in both business-to-business B2B as well as business-to-Ž . consumer B2C e-commerce. An example of e-tail-Ž . ing in B2B e-commerce is Grainger http: Ž <sup>rr</sup>www. grainger.com , a major player in the maintenance, . repair, and operations MRO market with a US\$200Ž . billion annual sales of hard-good supplies ranging from zip screws to industrial pumps 18 . An exam-<sup>w</sup> <sup>x</sup> ple of a B2C e-tailer is Amazon.com, which has been dubbed the Ae-tailing kingB, because of its fast-paced growth in on-line revenues.

The process of e-tailing consists of several steps: attracting customers to the electronic market place Ž . attract , informing customers about the relevant content at the Website inform , customizing product Ž . <sup>r</sup> service offerings to suit customer needs customize ,Ž . market making through transactional support using catalogs, auctions, exchanges, and barter models Ž . transact , providing payment and financing functions for online transactions pay , providing post-Ž . sales support such as customer service and order tracking through customer interaction platforms in-Ž teract , shipping of orders deliver , and personaliza- . Ž . tion of e-commerce Websites to analyze patterns of behavior to ensure better interaction in the future Ž . personalize 24 . Many of these activities, including <sup>w</sup> <sup>x</sup> inform, customize, interact, and personalize require efficient content management, which deals with combining, cleansing, normalizing, aggregating, integrating, and updating product and service information available through an e-commerce Website.

In this paper, we describe a methodology that can be applied to a number of different aspects of content management for an e-commerce application. These include providing an efficient search mechanism through product catalogs, enabling an electronic sales agent to identify alternative product choices, and receive expert advice to make the AbestB selections. Traditionally, human sales agents have performed these functions in brick-and-mortar stores. There are several advantages of automating such tasks. For example, an electronic sales agent is not restricted to limited hours of operation, is capable of helping multiple customers concurrently, is able to process larger volumes of information in less amount of time, is less obtrusive, is less expensive, is not susceptible to mental setbacks if a sale does not go through, and can perform at a high level of efficiency for an indefinite period of time. On the other hand, an automated sales agent is not as flexible, and may miss non-programmable cues that a human sales agent can pick up in special circumstances. There are further uses of a system such as this. For example, companies can manage visual information in electronic formats instead of relying on printed catalogs. Fashion designers can store and retrieve previous designs electronically, as well as create new designs efficiently. Such a system can also be helpful in global sourcing, which is an important issue in the textile and apparel industry 16 . Various members of<sup>w</sup> <sup>x</sup> the supply chain including fabric manufacturers, cutand-sew plants, and retailers often need to look for different suppliers from large printed catalogs for different resources such as fiber, fabric, and apparel. An automated system for searching can significantly improve supply chain efficiency through streamlining communication and mid-course correction of production and procurement plans.

The methodology we describe in this paper utilizes visual information, which is an important characteristic for many products such as apparel, designer costumes, interior designs of homes and automobiles, and landscaping. It is difficult to express visual information in non-visual terms such as textual descriptions. Hence, there is a need for the ability to store, index, search, and retrieve visually rich product information using their visual features such as color, texture, and shape, instead of having to rely on textual annotations. In order to accomplish this objective, we draw upon the research and development in the area of content-based image retrieval Že.g., Refs. 2,5,6,11,13 . While CBIR methodologies<sup>w</sup> <sup>x</sup> have been applied in a wide range of domains such as environmental modeling, medical applications, and satellite image analysis, this is one of the first applications of CBIR in the domain of electronic commerce in general and electronic retailing in particular.

## 2. Previous work on CBIR

In recent years, research and development in the content-based image retrieval have mainly focused on image features, such as color, shape, texture and spatial relationships. In addition, many content-based image retrieval systems and methods have been developed for various applications, such as geographic information systems and medical image databases.

To analyze image features, Ref. 30 uses color<sup>w</sup> <sup>x</sup> histograms to identify objects and propose a histogram intersection method for the color indexing of multicolored objects. In addition, Refs. 25,26 use<sup>w</sup> <sup>x</sup> the binary set representations method for the automated extraction of color and texture of the image. This method is for the automated extraction of regions and representation of their color contents. Since color histograms lack spatial information, Ref. 21,27<sup>w</sup> <sup>x</sup> provide a color-based method for images that integrate color histograms and spatial relationships among features of the image.

Texture is also an important element to human vision and for detecting patterns or spatial arrangement of pixels 8 . Texture is characterized by direc-<sup>w</sup> <sup>x</sup> tionality, coarseness, granularity, and contrast 7 .<sup>w</sup> <sup>x</sup> The most widely used collection of features is the image texture described in Ref. 4 , which has been<sup>w</sup> <sup>x</sup> used in subsequent studies for texture analysis. Ref. <sup>w</sup> <sup>x</sup> 25 describes a texture set approach for indexing in order to extract spatially localized texture information.

The retrieval of shape is one of the most challenging aspects in content-based image retrieval. Image indexing methods have been developed based on shape, and minimum bounding rectangles MBRsŽ . are used to extract features from shapes 15 . Others<sup>w</sup> <sup>x</sup>

Že.g., Ref. 8 use area, circularity, major axis orien- <sup>w</sup> <sup>x</sup>. tation and a set of algebraic moment invariants for features. In addition, the shape-based technique allows users to ask for objects similar in shape to a query.

One of the popular spatial indexing methods for point and region data is the R-tree method, which is <sup>w</sup> <sup>x</sup> <sup>)</sup> a height-balanced data structure 10 . The R -tree 3<sup>w</sup> <sup>x</sup> is an indexing method that efficiently supports multidimensional points and spatial data. Both R-tree and R<sup>)</sup>-tree have been used most often for the spatial data objects search in multi-dimensional space. In addition, the 2D strings method used for identifying spatial relationships among the objects and its variants has been used 5 .<sup>w</sup> <sup>x</sup>

As we discussed above, current image retrieval systems typically support image features, such as color, shape, texture, and spatial relationships. However, current content-based image retrieval systems ignore many important features, such as scale independence, orientation, and topological relationships. Only a few content-based image retrieval systems partially support these aspects for their image retrieval system, such as Photobook, VisualSEEk, and COIR.

Prominent examples for content-based image retrieval systems include QBIC, Virage, Photobook, Chabot, VisalSEEk, WebSEEk, SaFe, and COIR. QBIC 19 and Virage 1 are systems for image<sup>w</sup> <sup>x</sup> <sup>w x</sup> retrieval based on image features, such as color, shape and texture. The QBIC system uses image analysis to process queries for an image database. These two systems support image matching and keyword-based retrieval functionality on the whole image. Photobook 22 proposes a compact representa- <sup>w</sup> <sup>x</sup> tion method, which is called semantic-preserving image compression, to preserve essential image similarities and to quick search in a large number of images. Chabot 20 describes a method for meta-<sup>w</sup> <sup>x</sup> data, keywords, concepts, and color distributions to retrieve image. Chabot supports concept definition functionality for content-based image analysis and proposes the integration of relational database system with content-based techniques. In these systems, features of the whole image are used, but spatial relationships are not supported. These systems provide querying of whole images and extracted regions by color, shape and texture.

VisualSEEk 26 provides an image retrieval <sup>w</sup> <sup>x</sup> method using color, shape, texture and spatial relationships for individual regions. For browsing and searching of visual information on the Web, they also developed WebSEEk 28 image search engine,<sup>w</sup> <sup>x</sup> which provides an essential function of cataloging the visual information on the Web. In order to search for images by arrangements and visual features of regions, they developed SaFe 29 , which is a system<sup>w</sup> <sup>x</sup> for image searching that integrates spatial and feature querying. SaFe proposes a full method for extraction and indexing of region data. The system requires users to specify region sizes and locations accurately, since it uses the quadtree structure, which is based on the exact location of centroid.

COIR 12 provides an object-based similarity<sup>w</sup> <sup>x</sup> matching method. In this system, color, shape, and spatial relationships of objects are used for image retrieval. However, this system is limited to supporting only spatial relationships: left, right, above, and below and possible combinations of any of the four.

## 3. Methodology

In this section, we first describe the system architecture. Next, we present how shapes, colors, and textures are used in characterizing the visual features of products. Next, we discuss how these features are used to define similarities among products. Lastly, we illustrate how the methodology can be applied in electronic retailing. The methodology is presented in the context of an apparel retailer selling men’s wear such as dress shirts, trousers, sports jackets, sweaters, and shoes.

The methodology can be used in a number of ways. It can be applied to activities relevant to downstream members in a supply chain, including fashion designers, market forecasters and retailers, and as well as upstream members such as apparel, textile, and fiber manufacturers. Fig. 1 shows an integrated architecture of the proposed system that can be applied across channel partners in an apparel industry. The system would allow fashion designers to interactively develop new designs by retrieving the appropriate combinations of color, texture, and shapes through mix and match. Designers can specify the percentage of color in designing a print pattern. Color images are converted into gray scales before computing the texture features.

![](/api/attachments/RK5AQ38J/fulltext/images/18266c39635d4cf7d52963a4e377946c607c0c8e3b751a9660f8ef5d1790ad21.jpg)  
Fig. 1. Generic system architecture in apparel industry.

End-users potential customers can use an elec-Ž . tronic catalog to browse through the apparels, search for a particular combination of color, and texture, and can interactively retrieve objects that are similar to the ones that have already been retrieved. We describe the interactions of end-users in terms of browsing and searching, where browsing refers to the activity of scanning through various items on display and searching implies that the user is looking for one or more items with a specific set of criteria in mind. The system is designed on the premise that good search mechanism would maximize recall and precision, while a good browsing mechanism would expose the largest range of items in stock with the minimum amount of effort.

## 4. System architecture

The system consists of three modules: image processing module, database module, and applications module. The purpose of the image processing module is to analyze an image and obtain geometric features such as perimeter, area, minimum diameter, and maximum diameter, color histogram, and pixel intensities. The geometric features are used to compute shape parameters, which are subsequently loaded in a database. The image processing module also generates color histograms and pixel intensities and stores them as ASCII text files, which are then loaded into an Oracle database version 8i using theŽ . SQL<sup>)</sup> LDR utility. Subsequent processing of data is done using PL<sup>r</sup>SQL procedures and functions stored at the database server. The applications module contain the user interface for interacting with end-users and has been implemented in Oracle Developer and is being ported to the Web using Oracle Developer server. The overall system architecture is shown in Fig. 2.

## 4.1. Image processing

Image processing is done using the WiT visual programming software 17 . To generate the shape of <sup>w</sup> <sup>x</sup> an image, its bitmapped image is read from the file system and it is fed as an input to an operator called getData, which outputs a vector containing the graphical object specified in an interactive manner. The graphical object is specified using a rectangular window within the image indicating the region of interest. The output of getData is fed into another operator called getBlobsRoi, which performs a connectivity analysis on run lengths within the rectangular area of interest. The algorithm for getBlobsRoi scans from top to bottom and left to right of the selected region, and collects run lengths represented as non-zero pixels within the region. Next, another operator called getFeatures computes feature vectors from the blob vector obtained from the getBlobsRoi operator. Lastly, the getPerimeter operator determines the perimeter length, area, maximum and minimum radii, from which the shape parameters are computed. The histogram is obtained in a similar manner with an operator called histogram, which computes the frequency distribution of values in an input image. Texture data is obtained using the getArray operator that extracts a two-dimensional array of pixel values from an input image. A session through the image analysis phase is shown in Fig. 3, where the top left corner shows the results of each operator, the window at the center shows the script, and on the right side is the result of the getPerimeter operator.

![](/api/attachments/RK5AQ38J/fulltext/images/29cab8b655938f1ef4b11dd3923d51d60288fe526f9ef5261c943741579981a0.jpg)  
Fig. 2. System architecture.

## 4.2. Characterizing Õisual features

The visual features of an object can be characterized by shape, distribution of color, and texture. In the context of apparel, shapes can be used to characterize printed patterns. We use two parameters to characterize shape: surface regularity and roundness. In addition, it is also possible to specify relative locations and topologies of smaller component shapes to create composite shapes. We use color histogram to characterize the color distribution of a print. For texture analysis, we use contrast, coarseness, and directionality. Besides shape, color, and texture, it is also possible to specify the sizes of printed patterns using area and perimeter. We describe the details of the computation of shape, color, and texture parameters in the following subsections.

## 4.2.1. Characterization by shape

Most real-life objects are irregular in shape, and hence there is no universal approach to quantify the shape of an arbitrarily shaped object. However, the shape of an object can be parameterized with the help of some measurable properties. A good choice of a parameter should yield a known value in the ideal case 33 . We have selected four shape parame-<sup>w</sup> <sup>x</sup> ters that describe two orthogonal shape characteristics of an object: surface regularity irregularity Ž . and roundness elongation . These shape parameters Ž . are adopted from previous work e.g., Ref. 14,23,33 .Ž <sup>w</sup> <sup>x</sup>

![](/api/attachments/RK5AQ38J/fulltext/images/b56856e7467fb3f6164e7d0120b650bed5f8d4bf5c04b10b4c16e1becb464dd8.jpg)  
Fig. 3. Image analysis.

If the object is a perfect circle, all of the shape parameters would equal to 1 33 . The shape parame-<sup>w</sup> <sup>x</sup> ters are described in more detail below.

4.2.1.1. Surface regularity. Surface regularity refers to the smoothness of the surface of an object. Surface regularity is described by two shape parameters: surface regularity Ž . Ž . and form factor , defined in Eqs. 1 and 2 , respectively.Ž . Ž .

$$
\sigma = \sqrt {\left(a / a _ {\mathrm{c}}\right)}\tag{1}
$$

$$
\phi = 4 \pi * \text { Area   /   perimeter } ^ {2}\tag{2}
$$

Surface regularity in Eq. 1 is measured in terms Ž . of the amount of area covered as compared to a circle of equal perimeter: a and $a _ { \mathrm { c } }$ are the areas of the image object and a circle with equal perimeter, respectively. The form factor in Eq. 2 is high forŽ . objects that have a high area to perimeter ratio. Form factor and surface regularity are positively correlated.

4.2.1.2. Roundness elongation( ). Roundness ${ \bf \Xi } ( \rho )$ is inversely proportional to elongation and is described by Eq. 3Ž .

$$
\rho = (4 * \text { Area }) / \pi (\text { diameter } _ {\max}) ^ {2}.\tag{3}
$$

Roundness is high for objects that are wellrounded in every direction. Thus, objects with long extremeties will have relatively low roundness. Elongation is described by the aspect ratio, Ždefined in Eq. 4 . The aspect ratio is large for objects that areŽ .. elongated in one or more directions.

$$
\alpha = \text { diameter } _ {\max} / \text { diameter } _ {\min}.\tag{4}
$$

The diamete $\mathrm { r } _ { \mathrm { m a x } }$ in Eq. 4 is computed as theŽ . distance between two extreme boundary points, while diamete $\dot { \mathrm { \ m i n } }$ in Eq. 4 is obtained by computing the Ž . minor axis of an ellipse whose area is equal to that of the object and whose major axis is equal to the maximum diameter.

All shape parameters are ratios, a consequence of which is that if the shape of an object remains constant but its size changes, then the values of the parameters would vary relatively slowly as compared to when the shape varies but the size remains constant. Thus, two objects with the same shape but different sizes will be detected to be more similar than two objects with different shapes but the same size. The shape computations are done from runlength coding of images as described in Ref. 9 ,<sup>w</sup> <sup>x</sup> using the WiT 5.3 image processing software. Table 1 shows the shape parameters of some sample prints. The last column composite in Table 1 is computedŽ . as the average of the four shape parameters. Since aspect ratio is inversely proportional to roundness, we took its inverse in computing the average so that the two parameters roundness and aspect ratio doŽ . not cancel each other.

## 4.2.2. Characterization by color

For each image we create, a color histogram, which is a count of the number of pixels for each of the 256 color bins. Color-based search requires comparing the histograms of a sample image with that of a target image. We compare the histograms of the image selected by the user we refer to it as theŽ example image and the target image by using the . methodology described in Barber et al. 2 . Let<sup>w</sup> <sup>x</sup> $H _ { \mathrm { e } }$ and $H _ { \mathrm { t } }$ be the histograms of the example and target images, respectively. The element by element difference between $H _ { \mathrm { e } }$ and $H _ { \mathrm { t } }$ is the difference histogram $H _ { \mathrm { d } } .$ . The similarity <sup><</sup> <sup><</sup> S between the example image and the target image is computed by the following formula

$$
| S | = H _ {\mathrm{d}} ^ {\mathrm{T}} \mathbf {M} H _ {\mathrm{d}}\tag{5}
$$

where $H _ { \mathrm { d } } ^ { \mathrm { T } }$ is the transpose of $H _ { \mathrm { d } }$ , and M is the symmetric color similarity matrix $m _ { i , j }$ representing

Table 1 Shape parameters

<table><tr><td>Print</td><td>σ</td><td> $\phi$ </td><td>ρ</td><td>α</td><td>Composite</td></tr><tr><td></td><td>0.91</td><td>0.83</td><td>0.665</td><td>1.6</td><td>0.76</td></tr><tr><td></td><td>0.91</td><td>0.81</td><td>0.658</td><td>2.2</td><td>0.71</td></tr><tr><td></td><td>0.89</td><td>0.79</td><td>0.62</td><td>3.02</td><td>0.65</td></tr><tr><td></td><td>0.93</td><td>0.86</td><td>0.69</td><td>2.56</td><td>0.72</td></tr></table>

![](/api/attachments/RK5AQ38J/fulltext/images/6eab14c32c1119651be71440eb8bfb88225a543d023436c12cfa394880e468aa.jpg)  
Fig. 4. Ensemble using color similarity.

the similarity between colors i and j in the color spectrum. This method accounts for the perceptual difference between any two pairs of colors as well as the difference between the different shades of a given color.

In order to reduce the amount of on-line processing, we preprocess the color similarity of all images and generate a similarity matrix based on color, which is stored as a triple image , image , sim ,² : where $\begin{array} { r } { 1 < i < N - 1 , i + 1 < j < N , } \end{array}$ and $i \neq j ,$ , and N represents the number images in the database. Fig. 4 shows a list of other dress items that are most similar in color among all other items in the same category Ž . to the sample image. Although only five items are shown in Fig. 4, the similarity matrix is computed for all images in the system.

## 4.2.3. Characterization by texture

The texture of an image is characterized by its contrast, coarseness, and directionality properties, which are derived from the first-order statistics of the edge distribution 31,32 . Contrast is a measure<sup>w</sup> <sup>x</sup> of local variations of intensity, with higher variation of intensity representing higher contrast. Coarseness is measured with the number of texture elements in a fixed-size window, with a smaller number of texture elements representing higher coarseness.

$$
\left| s (x, y) \right| = \sqrt {\left(f _ {x} (x , y) ^ {2} + f _ {y} (x , y) ^ {2}\right)}\tag{6}
$$

$$
\Theta (x, y) = \tan^ {- 1} \left(f _ {y} (x, y) / f _ {x} (x, y)\right) + \pi / 2\tag{7}
$$

$$
f _ {x} (x, y) = f _ {x} (x + 1, y) - f _ {x} (x - 1, y)\tag{8}
$$

$$
f _ {y} (x, y) = f _ {y} (x, y + 1) - f _ {y} (x, y - 1)\tag{9}
$$

In Eq. 6 , Ž . $s ( x , y )$ represents strength, which is a relative difference in pixel intensity along the x and y axes, respectively. $f _ { x } ( x , y )$ is the difference in pixel intensity along the x axis and $f _ { \mathrm { v } } ( x , y )$ is the difference in pixel intensity along the y-axis. Coarseness and contrast represent the density of edge and mean of edge strengths, respectively. $\Theta ( x , y )$ represents directionality, which is computed by developing a histogram of edge directions and detecting the number of clusters. If the histogram yields no distribution, it would mean that there is no directionality in the pattern. Fig. 5 shows an ensemble of other dress items that are most similar in texture to the one shown in the sample image.

![](/api/attachments/RK5AQ38J/fulltext/images/e774df29151b6982fd4f23d4584b0793c8a3a74c5a4674edeacee2bb6020284b.jpg)  
Fig. 5. Ensemble using texture only.

## 5. Applications module

The applications module is a Web-based system for interacting with end-users, who can browse through product offerings, search for products based on color and texture similarity, as well as shapes and sizes of prints. The system uses color as the default feature to be used in the absence of a user-defined feature. There are two ways that the system interacts with a user: assist the user to identify apparels based on visual characteristics and provide technical guidance by suggesting pieces of apparel that the user may want to consider along with an item selected by them. As an example of the technical guidance in purchasing decision, if a user is purchasing a dress shirt, the system suggests matching ties, trousers, jackets, and sweaters that could also be purchased as a bundle. It should be noted that the matching pieces of apparels are based on contrast as well as similarities. A sample session through the system is shown in Fig. 6.

The left hand side of Fig. 6 shows a sample of products available in the page. These products are shown as thumbnail images and categorized into groups such as ties, shirts, jackets, trousers, etc. For each category, 16 products are shown in order to fit as many items as possible in one page. If the user wants to browse through additional items, they can retrieve the next batch of 16 by pressing on the button Next Batch. Since only images are shown, the user can browse through a larger number of products at once than is found in most Web pages. Once the user has selected a certain item, and intends to examine it in more detail, an enlarged image is displayed on the right side of the screen. Additional information such as product price and textual descriptions of the material, etc., can also be obtained at this point. The user can then request for other pieces of apparels that will match with the one selected, or other pieces of apparel that are similar to the one selected, based on shape, color, and texture features.

## 6. Conclusion

In this paper, we have described a content-based image retrieval system for fashion, textile, and clothing industry. The system supports color, texture, and shape-based search for apparels, and enables AcrosssellingB of products. The system has been implemented for electronic retailing, but can also be used in other parts of supply chain management such as design synthesis, forecasting of consumer demands, and inventory management by supply chain members. Such a system is also potentially useful for customer relationship management and personalization. In addition to business-to-consumer e-commerce, an electronic catalog can also use this methodology for business-to-business e-commerce by providing a visual communication medium for products with visually rich attributes that are difficult to express in textual descriptions.

![](/api/attachments/RK5AQ38J/fulltext/images/23ec0d533a87f44b0c4eed82828aad8ea93ee0948c9926f810cfd77fc17e5c3b.jpg)  
Fig. 6. Sample session through the system.

The future plans for the system is to extend it with an interactive virtual apparel platform that would store physical characteristics of potential virtual shoppers and provide an interactive Avirtual fitting roomB with different backgrounds. Such a system can also be useful for other supply chain members to plan production schedules based on demand forecasts that can minimize inventory cost and maximize profit.

## Acknowledgements

This research has been partially supported by a grant from the Graduate School, University of Maryland, Baltimore County in 1999–2000.

## References

<sup>w</sup> <sup>x</sup> 1 J.R. Bach, C. Fuller, A. Gupta, A. Hampapur, B. Horowitz, R. Humphrey, R. Jain, C.-F. Shu, The virage image search engine: an open framework for image management. Storage and Retrieval for Still Image and Video Databases. IEEE Computer Society Press, Washington DC, 1996, pp. 357–378.

<sup>w</sup> <sup>x</sup> 2 R. Barber, W. Equitz, C. Faloutsos, M. Flickner, W. Niblack, D. Petkovic, P. Yanker, Query by content for large on-line image collections. in: B. Furht, M. Milenkovic Eds. , AŽ . Guided Tour of Multimedia Systems and Applications. SPIE, Bellingham, 1995, pp. 76–87.

<sup>w</sup> <sup>x</sup> 3 N. Beckmann, H.-P. Kriegel, R. Schneider, B. Seeger, The R<sup>)</sup>-tree: an efficient and robust access method for point and rectangles. Proceedings of Annual Meeting of the Special Interest Group for Management of Data. ACM Press, New York, 1990, pp. 322–331.

<sup>w</sup> <sup>x</sup> 4 P. Brodatz, Textures; A Photographic Album for Artists and Designers. Dover Publications, New York, 1966.

<sup>w</sup> <sup>x</sup> 5 S.K. Chang, E. Jungert, Symbolic Projection for Image Information Retrieval and Spatial Reasoning. Academic Press, San Francisco, 1996.

<sup>w</sup> <sup>x</sup> 6 S.K. Chang, Q.Y. Shi, C.W. Yan, Iconic indexing by 2D strings. IEEE Transactions on Pattern Analysis and Machine Intelligence 9 7 1987 413–428 August .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 W. Equitz. Retrieving images from a database using texturealgorithms from the QBIC system. Technical Report IBMŽ 1993 ..

<sup>w</sup> <sup>x</sup> 8 C. Faloutsos, W. Equitz, M. Flickner, W. Niblack, D.

Pekovic, R. Barber. Efficient and Effective Querying by Image Content, Technical Report IBM 1993 . Ž .

<sup>w</sup> <sup>x</sup> 9 A. Gangopadhyay, Efficient retrieval of images based on content. Proceedings of the Annual Meeting of the Decision Sciences Institute. Decision Sciences Institute, Atlanta, GA, 1999, pp. 516–518 November .Ž .

<sup>w</sup> <sup>x</sup> 10 A. Guttman, R-trees: a dynamic index structure for spatial searching. Proceedings of Annual Meeting of the Special Interest Group for Management of Data. ACM Press, New York, 1984, pp. 47–57.

<sup>w</sup> <sup>x</sup> 11 J. Hafner, H.S. Sawhney, W. Equitz, M. Flickner, W. Niblack, Efficient color histogram indexing for quadratic form distance functions. IEEE Transactions on Pattern Analysis and Machine Intelligence 17 7 1995 729–736 July .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 K. Hirata, Y. Hara, H. Takano, S. Kawasaki, Content-oriented integration in hypermedia systems. Proceedings of Conference on Hypertext. ACM Press, New York, 1996, pp. 11–21.

<sup>w</sup> <sup>x</sup> 13 R.D. Holmes, E. Jungert, Symbolic and geometric connectivity in graph methods for route planning in digitized maps. IEEE Transactions on Pattern Analysis and Machine Intelligence 14 5 1992 549–565 May .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 M.A. Ireton, C.S. Xyedeas, Classification of shape for content retrieval of images in a multimedia database. Proceedings of the Sixth International Conference on Digital Processing of Signals in Communication. IEE, UK, 1991, pp. 111–116.

<sup>w</sup> <sup>x</sup> 15 H.V. Jagadish, A retrieval technique for similar shapes. Proceedings of Annual Meeting of the Special Interest Group for Management of Data. ACM Press, New York, 1991, pp. 208–217.

<sup>w</sup> <sup>x</sup> 16 T.K. Lau, I. King, Montage: an image database for the fashion, textile, and clothing industry in Hong Kong, in: R. Chin, T.-C. Pong Eds. , Computer Vision—ACCV’98. Ž . Springer, New York, 1998, pp. 410–417.

<sup>w</sup> <sup>x</sup> 17 Logic Vision, Wit Visual Programming Software: Operator Reference Manual. Logic Vision, Burnaby, 1999.

<sup>w</sup> <sup>x</sup> 18 A. Neumann, A better mousetrap catalog, Business 2.0, 2000, pp. 96–100 Business 2.0, San Francisco, February .Ž .

<sup>w</sup> <sup>x</sup> 19 W. Niblack, R. Barber, W. Equitz, M. Flickner, E. Glassman, D. Petkovic, P. Yanker, C. Faloutsos, G. Taubin, The QBIC Project: querying images by content using color, texture, and shape. Proceedings of the SPIE Conference on Storage and Retrieval for Image and Video Databases. SPIE, Bellingham, 1993, pp. 173–181.

<sup>w</sup> <sup>x</sup> 20 V.E. Ogle, M. Stonebraker, Chabot: retrieval from a relational database of images. IEEE Computer 28 9 1995Ž . Ž . 40–48 September .Ž .

<sup>w</sup> <sup>x</sup> 21 G. Pass, R. Zabih, J. Miller, Comparing images using color coherence vectors. Proceedings of the ACM Multimedia Conference. ACM Press, New York, 1996, pp. 65–73.

<sup>w</sup> <sup>x</sup> 22 A. Pentland, R.W. Picard, S. Sclaroff, Photobook: tools for content-based manipulation of image databases. Proceedings of the SPIE Storage and Retrieval Image and Video Databases II. SPIE, Bellingham, 1994, pp. 73–75.

<sup>w</sup> <sup>x</sup> 23 J.C. Russ, The Image Processing Handbook. CRC Press, Boca Raton, 1995.

<sup>w</sup> <sup>x</sup> 24 M. Sawhney, J. Davis, The eCommerce engine: how it works, Business 2.0, 2000, pp. 92–96 Business 2.0, San Ž Francisco, February ..

25 J.R. Smith, S.-F. Chang, Automated Image Retrieval Using Color and Texture, Columbia Technical Report 1995 .Ž .

<sup>w</sup> <sup>x</sup> 26 J.R. Smith, S.-F. Chang, VisualSEEK: a fuly automated content-based image query system. Proceedings of the ACM Multimedia Conference. ACM Press, New York, 1996, pp. 87–98.

<sup>w</sup> <sup>x</sup> 27 J.R. Smith, S.-F. Chang, Tools and techniques for color image retrieval. International Symposium on Electronic Imaging: Science and Technology—Storage and Retrieval for Image and Video Database. SPIE, Bellingham, 1996, pp. 426–437.

<sup>w</sup> <sup>x</sup> 28 J.R. Smith, S.-F. Chang, Visually searching the web for content. IEEE Multimedia. IEEE Computer Society Press, Washington DC, 1997, pp. 1–10.

<sup>w</sup> <sup>x</sup> 29 J.R. Smith, S.-F. Chang, SaFe: a general framework for integrated spatial and feature image search. IEEE Signal Processing Society 1997 Workshop on Multimedia Signal Processing. IEEE Computer Society Press, Washington DC, 1997, pp. 11–20.

<sup>w</sup> <sup>x</sup> 30 M.J. Swain, D.H. Ballard, Color indexing. International Journal of Computer Vision 7 1 1991 11–32 January .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 31 H. Tamura, S. Mori, T. Yamawaki, Texture features corre-

sponding to visual perception. IEEE Transactions of Systems, Man, and Cybernetics, SMC-8 6 1978 460–473Ž . Ž . Ž . June .

32 F. Tomita, S. Tsuji, Computer Analysis of Visual Textures. Kluwer Academic Publishing, Boston, 1990.

<sup>w</sup> <sup>x</sup> 33 D. Unwin, Introductory Spatial Analysis. Methuen, London, 1981.

![](/api/attachments/RK5AQ38J/fulltext/images/069e34a78bfe3dfe484e14a9e2f609bef94bf23e1310ac45904dd2a28cd049c5.jpg)

Aryya Gangopadhyay is an Assistant Professor of Information Systems at the University of Maryland Baltimore County USA . His research interestsŽ . include Electronic Commerce, multimedia databases, data warehousing and mining, and geographic information systems. He has authored and co-authored two books, many book chapters, numerous papers in journals such as IEEE Computer, IEEE Transactions on Knowledge and Data Engineering,

Journal of Management Information Systems, Journal of Global Information Management, Electronic Markets The International Journal of Electronic Commerce and Business Media, and Topics in Health Information Management, as well as presented papers in many national and international conferences.
