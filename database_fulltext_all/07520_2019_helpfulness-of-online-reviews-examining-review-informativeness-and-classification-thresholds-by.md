---
otero_id: 7520
otero_key: "5932FVNX"
title: "Helpfulness of online reviews: Examining review informativeness and classification thresholds by search products and experience products"
authors: "Xinyu Sun; Maoxin Han; Juan Feng"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113099"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Helpfulness of online reviews: Examining review informativeness and classification thresholds by search products and experience products

![](/api/attachments/5932FVNX/fulltext/images/cdab1cc257a0b8612ed911a81e3f6249c378c939aaffb0f80f7237b00675cb37.jpg)

Xinyu Sun<sup>a</sup>, Maoxin Han<sup>a,⁎</sup>, Juan Feng<sup>b</sup>

<sup>a</sup> School of Management, Xi'an Jiaotong University, Xi'an 710049, China

<sup>b</sup> College of Business, City University of Hong Kong, Hong Kong

## A R T I C L E I N F O

Keywords: Online reviews Search products Experience products Review informativeness Classification threshold Helpfulness prediction

## A B S T R A C T

Information overload often makes it dificult for consumers to identify helpful online product reviews through the traditional “helpful votes” function; therefore, it has become particularly important to eficiently identify helpful reviews. By differentiating search products from experience products. this research examines the impact of diferent measurements of review informativeness on review helpfulness, and proposes diferent classification thresholds to individually identify the helpfulness of online reviews for search products and for experience products, respectively. Further, our study applies machine learning algorithms to predict the performance of the classification based on our proposed review informativeness measurements and classification thresholds. All experiments were conducted using a dataset from JD.com, one of the largest online electronic marketplaces in China. Our results ofer guidelines to design diferent helpfulness classification standards for search products and for experience products.

## 1. Introduction

Nowadays, many e-commerce platforms enable consumers to post online product reviews; these reviews reflect consumer consumption experiences and reduce uncertainties in online shopping [1,32]. However, the explosive growth and expansion of online shopping has created a significant amount of online product reviews, making it dificult for consumers to select helpful ones [25,65]. Therefore, to assist consumers in making informed purchasing decisions, it becomes essential for platforms to identify helpful reviews eficiently. This paper proposes a new way to classify helpful reviews, incorporating measurements of review informativeness and classification thresholds for diferent product types.

Nelson [44] classified products into search products and experience products. Search products, such as electronics, possess attributes which are easily understood through an online search before purchase. Ex perience products, such as skin care products, possess attributes that are dificult to evaluate before purchase [23,24,57]. Product type (i.e., search products and experience products) developed by Nelson [44] has been widely adopted in the research on consumer behavior [16]. In our paper, review helpfulness represents the degree to which an online review reduces consumer uncertainty in online shopping [10,11]. Extant literature demonstrates that product type moderates consumers judgment of review helpfulness [17]. Thus, we integrate product type developed by Nelson [44] into our study.

In addition, previous literature has identified review length as an important variable in predicting review helpfulness [8,10,17,42]. Obviously, “longer reviews contain more product details, and more details about how and where the product was used in specific contexts” [43]; however, this does not mean that the longer a review is, the more helpful it is. One reason for this is that long reviews can contain lots of useless text content, which weakens the classification performance. Huang et al. [20] and Hong et al. [17] indicated that lengthy reviews might not obtain more helpful votes than do reviews of short or medium length.

In this paper, we propose to refine the variable of “review length” according to the review informativeness. Ghose and Ipeirotis [15] determined that review informativeness positively related to review helpfulness. More specifically, we use two variables, the number of attributes and the average length of attributes, to replace the commonly observed variable “review length.” Furthermore, we diferentiate attributes based on the content of the review, that is, whether the attributes are about the product or the platform. Ultimately, the original variable “review length” is replaced by four variables: the number of product attributes, the number of platform attributes, the average length of product attributes, and the average length of platform attri butes.

Next, we adopted a “threshold” approach to identify helpful reviews. As opposed to existing studies that apply one threshold to products of all types [41,49,65], our study calculates the optimal classification thresholds for both search products and experience products. We show that our proposed classification thresholds can significantly improve the performance of helpfulness classification.

![](/api/attachments/5932FVNX/fulltext/images/abcc9963491b8d8f4e060023b2adce337e4abf2eb6d9ac80cec365e0bfd735ec.jpg)  
Fig. 1. Research framework.

In this study, we obtained a dataset from JD.com, including six product categories, covering search products and experience products. We then constructed review informativeness metrics and used regres sion models to examine the impact of the review informativeness metrics on review helpfulness for search products and experience products. Further, we calculated the classification thresholds according to sepa rate product types. Finally, we studied the prediction power of our proposed review informativeness and classification thresholds using a dataset containing 9691 reviews. Our analysis indicates that we can accurately predict review helpfulness. Fig. 1 presents our research framework.

Our results show that, in general, review informativeness significantly influences the helpfulness of reviews. The average length of product attributes, however, only afects the helpfulness of reviews for experience products, and not that of reviews for search products. We further show that the optimal classification threshold for search products is larger than that for experience products. Moreover, we applied our experiment results to predict review helpfulness. These confirm that adopting review informativeness and setting diferent classification thresholds can significantly improve the accuracy of identifying helpful reviews.

The rest of the paper is structured as follows. We introduce relevant literature in Section 2. We then establish hypotheses in Section 3. In Section 4, we explain our methods and provide text analysis. In Section 5, we adopt regression models to explain the relationship between review informativeness and review helpfulness in search products and experience products. We also explore optimal thresholds according to diferent product types. In Section 6, we verify the prediction power of the proposed review informativeness and classification thresholds by using machine learning algorithms. We conclude our paper in Section 7.

## 2. Literature review

## 2.1. Informativeness and review helpfulness

To identify helpful reviews for consumers, a growing body of literature has examined variables which can significantly influence review helpfulness [5,6,8–12,15,17,19–21,27,28,31,36,41–43,46, 47,49,50,52,54,57,60,62,63,65,67,69]. Hong et al. [17] divided these variables into two parts: reviewer-related variables and review-related variables. Studies show that, compared to the reviewer-related variables, review-related variables have a stronger power to predict review helpfulness [15]. Various review-related variables have been explored, such as text sentiment [12,31,41,54,60], rating [8,43,57], text readability [15.47], and review length [8.10.17.42].

Based on prior classification results, review length, defined as the number of words an online review contains, has been viewed as one of the most essential variables in predicting review helpfulness [8,10,17,42]. Obviously, “longer reviews contain more product details, and more details about how and where the product was used in specific contexts” [43]. That is, longer reviews help consumers to make deci sions. However, long reviews often contain a great deal of useless or tedious content, which weakens the classification performance of review length. Huang et al. [20] found that there exists a threshold in the review length when measuring its efect on review helpfulness. Beyond this threshold, its positive efect diminishes or is even non-existent. Hong et al. [17] indicated that the medium-length reviews are more likely to obtain the reviewer's helpful votes than the short and long reviews. To avoid the negative impact of pointless but lengthy in formation, some researchers employ informativeness to identify helpful reviews [15].

Informativeness has been viewed as a key variable to predict review helpfulness [15]. Wang et al. [61] proposed that review helpfulness could be reflected by the aggregate perceived utility of the information in the review. Liang et al. [33] found that consumers are more likely to give helpful votes to informative and readable reviews. Book et al. [4] and Liu and Park [36] proposed that informativeness could be represented by review content, such as the details [7], concepts [49], sentiments [61], or features [1]. Singh and Tucker [55] found that an informative review consists of multidimensional attributes, such as product forms, product function, and platform service. Following this stream of literature, our paper introduces “informativeness,” represented by a series of keywords describing attributes from diferent dimensions, to study review helpfulness.

Our paper builds upon the literature that utilizes attributes to represent informativeness [4,49]. Attributes have been used to analyze product sales [1], consumer preference [64], and product design and improvement [50]. In terms of review helpfulness, Singh et al. [57] suggested that reviews containing attributes influence consumer's per ception of review helpfulness. Ngo-Ye et al. [47] determined the number of attributes in a text regression model to predict review helpfulness. However, these studies have primarily concentrated on product attributes. On the other hand, Singh and Tucker [55] demonstrated the importance of platform attributes to analyze online reviews. Thus, our study extends this line of inquiry by combining product and platform attributes to predict review helpfulness.

The number of attributes, captured by how many attributes are present in the review text, can measure the “width” of information. It has been used in the literature to predict review helpfulness [49] or to assess the semantic information carried by a review [4]. However, the measurement of information involves not only its width but also its “depth” [2,11]. Compared to the rudimentary descriptions of attributes, detailed descriptions better present consumer's opinions and reduce uncertainty in online shopping [52]. Both metrics are important to the classification performance of review helpfulness. Drawing from this line of the existing literature, our study uses both “the number of attributes” and “the average length of attributes” to analyze review helpfulness.

## 2.2. Classification threshold

Classification threshold, an important part of a binary classification system, influences the performance of classification algorithms [48]. Specially, in terms of review helpfulness, an inappropriate classification threshold may mistakenly sort helpful reviews or unhelpful reviews into their opposites, resulting in weak classification performance [15].

To select an optimal classification threshold, Ghose and Ipeirotis [15] designed experiments and found that the optimal threshold, defined as the ratio of helpful votes to total votes, equals 0.6. This threshold was also adopted by Krishnamoorthy [29] as well as Malik and Hussain [41]. Our paper, however, does not directly apply thi threshold for the following reasons. First, the threshold selection should align with the traits of data set [48]. Unlike Amazon.com, many ebusiness platforms, such as JD.com and taobao.com, only provide helpful votes. Therefore, the optimal classification threshold from Ghose and Ipeirotis [15] may not apply to our study. Furthermore, product type moderates consumer's judgment for review helpfulness [17,62], which is not considered in Ghose and Ipeirotis [15] and can therefore result in diferent classification thresholds for search product and experience product, respectively. Based on the above reasons, our paper extends this literature by setting diferent classification thresholds for diferent product types.

## 3. Research hypotheses

## 3.1. Product type

To reduce uncertainties in online shopping, consumers search for information about products before purchase [45]. Depending on whether consumers can evaluate a product before purchase, Nelson [44] classifies product type into search products and experience products, and this research paradigm has been widely adopted in the research on consumer behavior [16]. In the context of online reviews, it is relatively easy to obtain information and to compare product attributes of search products [23,24,57]. In contrast, for experience products, such as skin care products or apparel, it is more dificult to obtain information and to compare the product attributes, because consumers usually need to physically see, smell, touch, or use them [23,24,57], and diferent consumers are likely to form heterogeneous opinions based on a single product attribute [18]. Such intrinsic diferences between search products and experience products also influence consumers' information processing [43]. For example, Ullah et al. [59] found that in the early stages of a product launch, early online reviews for experience products have greater proportions of emotional content compared to reviews for search products. Luan et al. [37] investigated consumers' search behavior in online reviews (using eye-tracking equipment) by separating product types into search products and experience products. They found that consumers of search products prefer attribute-based reviews, and consumers of experience products prefer experience-based reviews. Weathers et al. [62] showed that the relative importance of diagnostics and credibility vary across diferent product types.

In our study, review helpfulness represents the degree to which online reviews reduce consumer uncertainty from online shopping [10,11]. As stated earlier, extant literature demonstrates that product type moderates consumers' judgment for review helpfulness [17]. In particular, because attributes of a search product (such as the capability of storage, the size of the screen, and the performance of the CPU) are relatively objective, and easily compared and evaluated, consumers are likely to form relatively homogeneous opinions for search products through an information search [18,22,23]. In contrast, attributes for an experience product (such as the feel of a fabric, or the taste of certain food) are hard to compare and evaluate, and consumers are more likely to produce heterogeneous evaluations [18]. Thus, it is more dificult for online reviews to provide new insights or valuable information for search products than for experience products. Moreover, product reviews for experience products often contain real and personalized usage experiences [30]. Such detailed and comprehensive reviews for experience products provide more helpful information and better facilitate the consumer's decision-making process than do reviews for search products. Therefore, consumers are more likely to value reviews for experience products diferently compared to reviews for search products. In summary, search products and experience products demonstrate diferent relationships between informativeness and review helpfulness. Consequently, the classification for helpful reviews for a search product is likely to be diferent from the classification for helpful reviews for an experience product.

## 3.2. Hypothesis 1: product attributes

A product may possess many diferent attributes [1,55]. Smart phones, for example, embed many functions, including watching movies, taking pictures, playing games, and so on. The product descrip tions provided by sellers rarely cover all such attributes. Thus, consumers are inclined to search pertinent attribute-related information from online reviews [22]. When reviews contain detailed descriptions about multiple product attributes, consumers are able to comprehensively understand the products from diferent perspectives, and the uncertainty of online shopping can be reduced [49]. Furthermore, consumers tend to give a helpful vote to product reviews with more product attributes. Hence, we have the following hypothesis (Fig. 2): H1. (a): The number of product attributes significantly relates to review helpfulness.

![](/api/attachments/5932FVNX/fulltext/images/9f45dc2d6c506518a34d742598030ab2fa174dd9efe467fd42a65bb73b05ef13.jpg)  
Fig. 2. The hypotheses framework.

The impact of the average length of product attributes on review helpfulness is diferent for products of diferent types. In particular, as attributes of search products are easily compared and evaluated [16,43], consumer opinions about the attributes of search products and, in turn, the content of the product reviews, are possibly similar [18]. That is, a longer product attribute in the review does not necessarily imply that the review is more insightful [22]. Thus, consumers seem not to view search product reviews as helpful purely based on the average length of product attributes. For example, the capacity of a memory card is objective, and it is easy to compare and evaluate. A long description of the capacity attributes is likely to express repetitive opinions and can hardly provide new insight that could be helpful to consumers.

In contrast, an experience product, such as a skin-care product or a piece of music, needs to be seen, heard, touched, or felt before it can be fully understood [34]. The attributes of experience products are difi cult to compare and evaluate, and consumers are likely to have per sonalized usage experiences [22]. A review containing detailed descriptions for attributes and personal experiences is helpful to consumers of experience products. Furthermore, consumers are in clined to assign a helpful vote to the reviews containing longer product attributes [30]. For example, reviewers may have diferent opinions about the fit of a pair of running shoes because the sizes and shapes of their feet vary. When reviewers describe the fit in detail based on their feet conditions, consumers can better understand this attribute and are more likely to give a helpful vote. Hence, we make the following

hypothesis (Fig. 2):

H1. (b): The average length of product attributes significantly relates to review helpfulness for experience products, but has no significant influence on review helpfulness for search products.

## 3.3. Hypothesis 2: platform attributes

The services provided by the platform, such as shipping [53] and marketing promotions [70], influence consumer purchase decisions. Reviews that contain various platform-related information can reduce uncertainty [19] and facilitate consumers' decision making. For example, buyers of fragile products hope to know whether there is special protection packaging. A review that contains detailed shipping method information will be helpful to these customers. Furthermore, with an increase in the number of service categories, it is impossible for consumers to fully comprehend platform-related information purely through the descriptions provided by the platform [55]. For instance, reviews that contain customers' previous return experiences can be informative compared to the oficial return rules ofered by the platform, which can be lengthy and have many conditions attached. Thus, online reviews then become an important information resource about platform attributes. A product review with a large number of platform attributes helps consumers understand platform-related services and reduces the uncertainty of online shopping. Thus, we make the following hypothesis (Fig. 2):

H2. (a): The number of platform attributes significantly relates to review helpfulness.

To attract more consumers, online platforms provide a number of services [53,70,71]. Diferent consumers may use diferent experiences or criteria to evaluate the services, so the evaluations of platform services are more likely to be heterogeneous [18,22]. For example, given the same shipping speed (such as 5–7 days), some consumers may view it as high-speed while others may feel it is too slow. In this case, a review with detailed descriptions about the platform attributes will provide more information and will be more likely to be viewed as helpful by other consumers. Thus, we propose the following hypothesi (Fig. 2):

H2. (b): The average length of platform attributes significantly relates to review helpfulness.

## 3.4. Hypothesis 3: classification threshold

We have adopted a common approach in machine learning to identify whether a review is helpful. More specifically, we want to determine a threshold value ( ) for the number of “helpful votes” (τ) received by a certain review, such that if τ≥ , the review is classified as helpful; otherwise, it is classified as not helpful [15]. We expect that the classification threshold for search products will be larger than that for experience products, that is, τ<sub>search</sub> > τ<sub>experience</sub>. This is because, compared to experience product attributes, search product attributes are objective and easy to compare [16,22,43]. It is more likely that consumers reach homogenous conclusions about the product attributes, such as the capacity of the storage, the size of the screen, and the performance of CPU. Therefore, the descriptions of these attributes are more likely to be similar, and consumers rarely obtain new and helpful insight from them [18]. As a result, a review needs to receive a relatively large number of helpful votes to meet consumers' expectations for a helpful review. In contrast, attributes for an experience product are subjective, and consumers usually form heterogeneous evaluations based on their own experience or judgment [22]. Thus, a review for an experience product is more likely to contain valuable and unique usage experience [30] which can be helpful to consumers. Even if it receives a small number of helpful votes, consumers are likely still to view it as helpful. Thus, we set a higher classification threshold for reviews of search products than for reviews of experience products. We thus have the following hypothesis (Fig. 2):

H3. The classification threshold of search products is higher than that of experience products, that is, τ<sub>search</sub> > τ<sub>experience</sub>.

## 4. Data processing

## 4.1. Data selection and pre-processing

We collected product review data from JD.com, one of the largest and most influential business-to-consumer e-commerce platforms in China [35].

Based on previous studies [3,26,37,62,68], we chose cell phones, televisions, and laptops as search products, and facial skin care, rice cookers, and running shoes as experience products. Fig. 3 illustrates an example of product reviews on JD.com. Three types of data were collected: (1) reviewer-related variables (e.g., whether the review was provided anonymously, whether a user image was provided, whether the reviewer was a JD Plus member, and the JD user experience value); (2) review-related variables (e.g., rating, the number of helpful votes, elapsed time, and image count); and (3) review text.

We obtained 13,152 product reviews through the use of a web spider. We then pre-processed the raw dataset, which included deleting the repetitive, incomplete, and invalid data and then transforming the non-numerical data into numerical data. After pre-processing, 9691 reviews remained. Table 1 presents a series of variables.

## 4.2. Text analysis

## 4.2.1. Enrich existing lexicons

Firstly, we utilized a lexicon-based method to identify the attributes contained in the reviews. In addition to existing standard lexicons, such as ICTCLAS (Institute of Computing Technology, Chinese Lexical Analysis System), we also added additional lexicon that included specialized terminology (such as PPI, sensitive skin type, CPU) from product instruction manuals and popular words or abbreviations used on the Internet (for example, 6 means smooth in Chinese), from diferent Chinese input methods (such as Sougo, Baidu, Tencent, etc.). Table 2 gives us examples of lexicons about product attributes and platform attributes.

## 4.2.2. Construct metrics of informativeness

Our approach involved extracting attributes from the review text. Past research has shown that a product can be represented and described by its attributes [53]. Therefore, a review rich with product attributes can be understood easily and can improve reading speed, comprehension, and retention [56]. We proposed two types of informativeness metrics to measure the attributes in a review: the number of attributes, and the average length of attributes.

Specifically, “the number of attributes” reflects the total number of attributes present in the review content [49]. Denoting c(s ) as the number of attributes in sentence $s _ { j } ,$ the number of attributes for review r is measured as follows:

$$
c o u n t (r) = \sum_ {j = 1} ^ {n} c (s _ {j})\tag{1}
$$

where n is the number of sentences in review r and $s _ { 1 } , . . . , s _ { n }$ are the sentences that appear in review r.

Previous studies have also found that there is a positive relationship between review length and review helpfulness [17,54]. We observed many reviews containing multiple attributes within one sentence in our dataset. Thus, unlike most traditional measurements of length in the literature [20], we measured the average length of attributes, where l $( s _ { j } )$ is the length of sentence s (in words), and $\mathbf { 1 } ( s _ { j } )$ is a dummy variable equal to one if $s _ { j }$ has at least one attribute and zero otherwise, that is:

$$
\operatorname{length} (r) = \sum_ {j = 1} ^ {n} l \left(s _ {j}\right) \cdot \mathbf {1} \left(s _ {j}\right) / \operatorname{count} (r)\tag{2}
$$

Table 3 presents a series of descriptions of review informativeness, and Table 4 shows an example of the measurements. After data cleaning, we calculate review informativeness for each review based on Eqs. (1) and (2). The summary statistics are shown in Table 5.

## 5. Explanatory analysis

## 5.1. Informativeness efects on review helpfulness

One of our objectives was to investigate whether and how the impact of review informativeness on review helpfulness for search products is diferent from that on experience products.

We thus used the number of helpful votes (#helpful votes) to present review helpfulness, which is also our dependent variable. The independent variables were the four attributes variables (of review informativeness): the number of product attributes, the average length of product attributes, the number of platform attributes, and the average length of platform attributes. The control variables included reviewerrelated variables $( \mathrm { i . e . , }$ , anonymous, user image, JD Plus membership, and JD user experience value) and review-related variables (i.e., rating, image count, and elapsed time). As illustrated in Table 6, there were 9691 valid reviews in our analysis.

To test the relationship between review informativeness and review helpfulness, we ran four regression models to test Hypotheses 1 and 2.

![](/api/attachments/5932FVNX/fulltext/images/d2df3e1b1095f90cecb7af1b2a980f09170cffe1ce2659a004622ca2754d6ce7.jpg)  
Fig. 3. An example of product reviews on JD.com.

Model 1 was the benchmark model, and contained only the control variables. In Model $^ { 2 , }$ we added the number of product attributes and the average length of product attributes; the estimations of $\beta _ { 1 }$ and $\beta _ { 2 }$ were examined for Hypotheses 1(a) and 1(b). In Model 3, we added the number of platform attributes and the average length of platform attributes; the estimations of $\beta _ { 3 }$ and $\beta _ { 4 }$ were examined for Hypotheses 2(a) and 2(b). Model 4 included all the independent variables, shown as Eq. (3).

$$
\begin{array}{l} \text {   \#helpfulvotes   } = \alpha + \beta_ {1} \cdot \text {   the   number   of   product   attributes   } + \beta_ {2} \\ \quad \cdot \text {   the   average   length   of   product   attributes   } + \beta_ {3} \\ \quad \cdot \text {   the   number   of   platform   attributes   } + \beta_ {4} \\ \quad \cdot \text {   the   average   length   of   platform   attributes   } + \beta_ {5} \\ \quad \cdot \text {   anonymity   } + \beta_ {6} \cdot \text {   user   image   } + \beta_ {7} \cdot \text {   JD   Plus   member   } + \beta_ {8} \\ \quad \cdot \ln (\text {   JD   user   experience   value  }) + \beta_ {9} \cdot \text {   rating   } + \beta_ {1 0} \\ \quad \cdot \text {   image   count   } + \beta_ {1 1} \cdot \ln (\text {   elapsed   time  }) + \varepsilon \end{array} \tag {3}\tag{3}
$$

We chose the standard negative binomial regression as our esti mation method due to the distribution of helpful votes [67].

As shown in Table $^ { 6 , }$ in Model 2, we examined the efects of the number of product attributes and the average length of product attri butes on review helpfulness. For search products, the coeficient of the number of product attributes is statistically significant $( \beta _ { 1 } = 0 . 1 9 9 ,$ $p = 0 . 0 0 0 )$ , while the coeficient of the average length of product attributes is insignificant $( \beta _ { 2 } = 0 . 0 1 4 , ~ p = 0 . 4 9 0 )$ , indicating that for search products, reviews containing more product attributes are helpful while reviews with lengthy attribute descriptions are not. For experience products, the coeficients of both the number of product attributes and the average length of product attributes are statistically significant $( \beta _ { 1 } = 0 . 2 3 3 , p = 0 . 0 0 0 ~ \mathrm { a n d } \beta _ { 2 } = 0 . 0 3 3 , p = 0 . 0 0 5 )$ , indicating that for experience products, reviews containing more product attributes as well as lengthy descriptions are helpful. Thus, Hypotheses 1(a) and 1(b)

are supported.

In Model 3, we examined the efects of the number of platform attributes and the average length of platform attributes on review helpfulness. Their coeficients are statistically significant in both the search and experience products $( \beta _ { 3 } = 0 . 0 9 0 , p = 0 . 0 3 3 , \beta _ { 4 } = 0 . 1 3 9 , p = 0 . 0 0 1$ and $\beta _ { 3 } = 0 . 2 2 4 , p = 0 . 0 0 0 , \beta _ { 4 } = 0 . 1 4 0 , p = 0 . 0 0 0 ) ,$ , indicating that the number of platform attributes and the average length of platform attributes influence review helpfulness for both product types. In other words, facing the uncertainty of platform-related attributes, like shipping and service, consumers find it helpful to browse reviews containing various and detailed descriptions of platform attributes. Thus, Hypotheses 2(a) and 2(b) are supported.

Model 4 considered all the variables. The significance of the variables in Model 4 is consistent with Models 2 and 3, confirming the robustness of our experiment. We also compare the performance of diferent models through Information Criterion, including AIC and BIC. Table 6 shows that Model 4 produces the lowest AIC and BIC, which means that Model 4 has a stronger power to identify review helpfulness than two of the other models. Moreover, Model 4 has the largest $R ^ { 2 } .$ That is, Model 4 has a better fit than the three other models. In summary, our proposed variables are efective in identifying helpful reviews.

In an online market where the transactions usually happen anonymously, the display of a user's image reveals the user's identity [14], and communication among users with identification can enhance information acquisition eficiency [39]. Our results indicate that “user image” significantly and positively influences review helpfulness for both search products and experience products, and findings are consistent with existing literature [27].

In the presence of numerous information sources, consumers tend to trust information from users with high degrees of expertise. Cao et al. [5], Racherla and Friske [51], and Luo et al. [38] have indicated that reviewer experience, or reviewer expertise, afect the perceived helpfulness of a review. Our results indicate that the JD user experience

The explanation of variables.

<table><tr><td>Variables</td><td>Names</td><td>Explanations</td><td>Type</td></tr><tr><td rowspan="4">Reviewer-related variables</td><td>Anonymity</td><td>Whether users show their nicknames to the public;0: anonymity; 1: otherwise.</td><td>Binary</td></tr><tr><td>User image</td><td>Whether users show their image to the public;0: hiding their images; 1: otherwise.</td><td>Binary</td></tr><tr><td>JD Plus member</td><td>Whether user is Plus members of JD.com;0: non Plus member; 1: Plus member</td><td>Binary</td></tr><tr><td>JD user experience value</td><td>The membership points users have accumulated since registering with JD.com</td><td>Continuous</td></tr><tr><td rowspan="4">Review-related variables</td><td>Rating</td><td>Users&#x27; rating from 1 to 5 stars</td><td>Discrete</td></tr><tr><td>Image count</td><td>The number of images posted in the review from 0 to 9</td><td>Discrete</td></tr><tr><td>Elapsed time</td><td>The number of days since the review was posted</td><td>Continuous</td></tr><tr><td># Helpful votes</td><td>Cumulative value of user voting when they think reviews are helpful</td><td>Discrete</td></tr><tr><td>Review text</td><td>Review text</td><td>The product textual evaluations written by reviewers</td><td>Text</td></tr></table>

Table 2  
Most frequent product and platform attributes.

<table><tr><td colspan="3">Search product attributes</td><td colspan="3">Experience product attributes</td><td rowspan="2">Platform attributes</td></tr><tr><td>Cell phone</td><td>Laptop</td><td>Television</td><td>Rice cooker</td><td>Running shoes</td><td>Skin care</td></tr><tr><td>Appearance</td><td>Camera</td><td>Audio</td><td>Capacity</td><td>Air</td><td>Alcohol</td><td>Repayment</td></tr><tr><td>Battery</td><td>Carbon fiber</td><td>Base</td><td>Clean</td><td>Anti-slip</td><td>Blain</td><td>After-sale</td></tr><tr><td>Camera</td><td>CPU</td><td>Blue light</td><td>Digital controls</td><td>Craftwork</td><td>Clean face</td><td>Before-sale</td></tr><tr><td>Charge</td><td>Disk</td><td>Bluetooth</td><td>Form</td><td>Cushioning</td><td>Cream</td><td>Coupon</td></tr><tr><td>CPU</td><td>Interface</td><td>Craftwork</td><td>Function</td><td>Design</td><td>Dry</td><td>Courier</td></tr><tr><td>Recognition</td><td>Keyboard</td><td>Curve</td><td>Mode</td><td>Elasticity</td><td>Foam</td><td>Service</td></tr><tr><td>Unlock</td><td>Memory</td><td>Frame</td><td>Non-stick pan</td><td>Heel</td><td>Fresh</td><td>Deliver</td></tr><tr><td>Function</td><td>Metal</td><td>HD</td><td>Porridge</td><td>Material</td><td>Lotion</td><td>Discount</td></tr><tr><td>Game</td><td>Portability</td><td>Movie</td><td>Power saving</td><td>Outer sole</td><td>Moisture</td><td>Free delivery</td></tr><tr><td>Operation</td><td>PPI</td><td>Network</td><td>Rice</td><td>Rubber</td><td>Oily</td><td>Free gift</td></tr><tr><td>Price</td><td>Software</td><td>Remote-control</td><td>Rice crust</td><td>Shoe string</td><td>Price</td><td>Free interest</td></tr><tr><td>Signal</td><td>Standby</td><td>Screen</td><td>Soup</td><td>Size</td><td>Scent</td><td>JD Bean</td></tr><tr><td>Assistant</td><td>Touch board</td><td>Software</td><td>Stainless steel</td><td>Style</td><td>Skin</td><td>Order</td></tr><tr><td>System</td><td>Touch screen</td><td>Sound</td><td>Steam</td><td>Ventilation</td><td>Smell</td><td>Refund</td></tr><tr><td>Waterproof</td><td>Video card</td><td>Video</td><td>Warm</td><td>Weight</td><td>Texture</td><td>Repair</td></tr></table>

Table 3  
Descriptions of review informativeness.

<table><tr><td>Variables</td><td>Names</td><td>Explanations</td><td>Type</td></tr><tr><td rowspan="4">Review informativeness</td><td>The number of product attributes</td><td>The number of product attributes in the review</td><td>Discrete</td></tr><tr><td>The average length of product attributes</td><td>The average length of a sentence describing product attributes in the review</td><td>Continuous</td></tr><tr><td>The number of platform attributes</td><td>The number of platform attributes in the review</td><td>Discrete</td></tr><tr><td>The average length of platform attributes</td><td>The average length of a sentence describing platform attributes in the review</td><td>Continuous</td></tr></table>

Table 4  
Attributes identification and attributes measurements.

<table><tr><td>Review sentence</td><td>Review</td><td>Attributes</td><td>The number of attributes</td><td>The average length of attributes</td><td>Category</td></tr><tr><td>1</td><td>不得不说手机运行很稳定(I have to say the cell phone is very stable.)</td><td>手机cell phone</td><td>1</td><td>11</td><td>Product</td></tr><tr><td>2</td><td>京东的物流还是很快的(The logistics of JD.com are fast.)</td><td>物流logistics</td><td>1</td><td>10</td><td>Platform</td></tr><tr><td>3</td><td>手机播放音乐立体感不错(The phone plays music with a good stereo effect.)</td><td>音乐music</td><td>1</td><td>11</td><td>Product</td></tr><tr><td>4</td><td>尤其是指纹解锁超级快(The fingerprint unlock is particularly super-fast.)</td><td>指纹解锁fingerprint unlock</td><td>1</td><td>10</td><td>Product</td></tr><tr><td>5</td><td>售后和客服都非常耐心(After-sales and customer service personnel are very patient.)</td><td>售后after-sales客服customer service</td><td>2</td><td>5</td><td>Platform</td></tr><tr><td>6</td><td>电池以及屏幕一直都是软肋(The battery and screen have always been the weakness.)</td><td>电池battery屏幕screen</td><td>2</td><td>6</td><td>Product</td></tr><tr><td>7</td><td>优惠券为我省了很多钱(The coupons save a lot of money.)</td><td>优惠券coupons</td><td>1</td><td>10</td><td>Platform</td></tr></table>

Table 5  
Summary statistics for search and experience products.

<table><tr><td rowspan="2">Variables</td><td colspan="4">Search products</td><td colspan="4">Experience products</td></tr><tr><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td>The number of product attributes</td><td>1.68</td><td>2.51</td><td>0</td><td>31</td><td>1.38</td><td>1.66</td><td>0</td><td>15</td></tr><tr><td>The average length of product attributes</td><td>4.96</td><td>4.95</td><td>0</td><td>52</td><td>4.79</td><td>4.18</td><td>0</td><td>32</td></tr><tr><td>The number of platform attributes</td><td>0.73</td><td>1.40</td><td>0</td><td>18</td><td>0.54</td><td>0.94</td><td>0</td><td>10</td></tr><tr><td>The average length of platform attributes</td><td>2.52</td><td>3.97</td><td>0</td><td>46</td><td>2.18</td><td>3.45</td><td>0</td><td>28</td></tr><tr><td>Anonymity</td><td>0.94</td><td>0.23</td><td>0</td><td>1</td><td>0.96</td><td>0.21</td><td>0</td><td>1</td></tr><tr><td>User image</td><td>0.47</td><td>0.50</td><td>0</td><td>1</td><td>0.46</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td>JD Plus member</td><td>0.38</td><td>0.49</td><td>0</td><td>1</td><td>0.42</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>In (JD user experience value)</td><td>10.06</td><td>1.05</td><td>0</td><td>15.91</td><td>9.61</td><td>1.22</td><td>0</td><td>15.57</td></tr><tr><td>Rating</td><td>4.58</td><td>1.12</td><td>1</td><td>5</td><td>4.84</td><td>0.65</td><td>1</td><td>5</td></tr><tr><td>Image count</td><td>1.19</td><td>1.96</td><td>0</td><td>9</td><td>0.86</td><td>1.50</td><td>0</td><td>9</td></tr><tr><td>In (elapsed time)</td><td>4.16</td><td>0.84</td><td>0</td><td>6.94</td><td>3.91</td><td>1.47</td><td>0</td><td>6.63</td></tr><tr><td># Helpful votes</td><td>3.62</td><td>38.68</td><td>0</td><td>1,504</td><td>1.01</td><td>3.13</td><td>0</td><td>62</td></tr></table>

Note: The observations for search and experience products are 5384 and 4307, respectively.

Table 6  
The regression results of the impact of informativeness on review helpfulness.

<table><tr><td rowspan="2">Variables</td><td colspan="4">Search products</td><td colspan="4">Experience products</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td>The number of product attributes</td><td></td><td>0.199***</td><td></td><td>0.167***</td><td></td><td>0.233***</td><td></td><td>0.253***</td></tr><tr><td>The average length of product attributes</td><td></td><td>0.014</td><td></td><td>0.007</td><td></td><td>0.033***</td><td></td><td>0.081***</td></tr><tr><td>The number of platform attributes</td><td></td><td></td><td>0.090**</td><td>0.082**</td><td></td><td></td><td>0.224***</td><td>0.085***</td></tr><tr><td>The average length of platform attributes</td><td></td><td></td><td>0.139***</td><td>0.090***</td><td></td><td></td><td>0.140***</td><td>0.189***</td></tr><tr><td>Anonymity</td><td>-0.244</td><td>-0.217</td><td>-0.421</td><td>-0.313</td><td>-0.204</td><td>-0.109</td><td>-0.283</td><td>0.048</td></tr><tr><td>User image</td><td>0.245</td><td>0.366**</td><td>0.396**</td><td>0.468***</td><td>0.279***</td><td>0.380***</td><td>0.099</td><td>0.179***</td></tr><tr><td>JD Plus member</td><td>0.082</td><td>0.176</td><td>0.127</td><td>0.188</td><td>-0.126</td><td>-0.022</td><td>0.028</td><td>0.075</td></tr><tr><td>In (JD user experience value)</td><td>-0.214</td><td>-0.071</td><td>-0.061</td><td>-0.020</td><td>-0.119***</td><td>-0.145***</td><td>-0.113***</td><td>-0.106***</td></tr><tr><td>Rating</td><td>-0.511***</td><td>-0.532***</td><td>-0.548***</td><td>-0.550***</td><td>-0.439***</td><td>-0.425***</td><td>-0.318***</td><td>-0.242***</td></tr><tr><td>Image count</td><td>0.583***</td><td>0.534***</td><td>0.555***</td><td>0.506***</td><td>0.293***</td><td>0.199***</td><td>0.278***</td><td>0.169***</td></tr><tr><td>In (elapsed time)</td><td>0.955***</td><td>0.814***</td><td>0.896***</td><td>0.818***</td><td>0.175***</td><td>0.152***</td><td>0.233***</td><td>0.200***</td></tr><tr><td>_cons</td><td>-0.256</td><td>-1.739*</td><td>-1.903</td><td>-2.421**</td><td>2.212***</td><td>1.747***</td><td>0.694*</td><td>-0.877**</td></tr><tr><td>Pseudo R2</td><td>0.099</td><td>0.125</td><td>0.121</td><td>0.136</td><td>0.041</td><td>0.071</td><td>0.110</td><td>0.169</td></tr><tr><td>AIC</td><td>11,648.1</td><td>11,323.8</td><td>11,374.0</td><td>11,185.1</td><td>10,126.2</td><td>9814.8</td><td>9409.0</td><td>8791.7</td></tr><tr><td>BIC</td><td>11,707.4</td><td>11,396.3</td><td>11,446.5</td><td>11,270.8</td><td>10,183.5</td><td>9884.8</td><td>9479.1</td><td>8874.5</td></tr><tr><td>N</td><td>5384</td><td>5384</td><td>5384</td><td>5384</td><td>4307</td><td>4307</td><td>4307</td><td>4307</td></tr></table>

Note:

$$
p <   0. 1.
$$

<sup>⁎⁎</sup> p < 0.05.

⁎⁎⁎ $p \ < \ 0 . 0 1 .$

![](/api/attachments/5932FVNX/fulltext/images/7ea30f5cec0d75220ecc06a7e4ed61a0aeffb65ae9d578b75e267a96c7f3e9eb.jpg)  
Fig. 4. The Area Under Curve of diferent thresholds in diferent product types.

significantly afects the review helpfulness.

Personal demographics, such as gender and geographical origin, significantly enhance the credibility of a message [40]. The disclosure of demographics helps reduce uncertainty [58]. Fogg et al. [13] have determined that reviews written by anonymous reviewers receive few helpful votes. Our results show an insignificant relationship between reviewer's anonymity and review helpfulness. We feel this result is due to diferent designs of this online platform. Unlike TripAdvisor or

Amazon.com, JD.com does not support the function of searching personal demographic information through clicking a reviewer's profile. Therefore, in JD.com, the diference between anonymous reviewers and non-anonymous reviewers is too weak to influence consumer's judgment for review helpfulness. Similar arguments apply to the variable of JD Plus membership. This variable is insignificant in our model. This is likely because JD.com does not ofer a virtual community for JD Plus members, and thus membership does not influence users' perceptions of information credibility, which is diferent from the membership concepts featured in previous literature such as Luo et al. [38].

## 5.2. Classification threshold's efect on helpfulness

We used a classification threshold (τ) to determine whether a review was helpful. Specifically, in our analysis, if the number of helpful votes a review receives is higher than the classification threshold, we regard this review as a helpful one. Otherwise, it is not helpful. Therefore, the choice of the classification threshold decides the performance of classification. We extended the study of Ghose and Ipeirotis [15] by considering diferent classification thresholds for search products and experience products. First, we randomly picked 500 reviews for search products and experience products, respectively. Second, we employed two undergraduate students to judge whether each review is helpful or not without showing any information about the number of helpful votes, and we recorded such manual classification results. Third, we compared the consistency of these two manual classification results using the kappa statistic denoted by κ. The experiment shows that κ is in the range of 0.6 to $0 . 8 \left( \mathrm { i . e . , } \kappa _ { s e a r c h } = 0 . 7 8 6 9 , \kappa _ { \mathrm { e x p e r i e n c e } } = 0 . 7 6 3 8 \right)$ , which demonstrates that all 500 classification results are consistent. Fourth, to keep the dataset balanced, we set limit lines for thresholds (i.e., $\tau _ { s e a r c h } \leq 7 , \tau _ { \mathrm { e x p } e r i e n c e } \leq 4 )$ and then separated reviews into helpful and non-helpful ones by comparing #helpful votes with diferent thresholds. We recorded them as threshold classification results. Fifth, to identify the optimal threshold, we performed the Receiver Operating Characteristic (simply, ROC) analysis to compare manual classification results with threshold classification results. Area Under Curve (simply, AUC) represents the performance of classification. The larger the value of AUC is, the better the classification performance is. Fig. 4 presents the values of AUC in diferent thresholds. Our analysis indicates that if we set thresholds (i.e., $\tau _ { s e a r c h } = 4 , \tau _ { \mathrm { e x p } e r i e n c e } = 2 )$ , the performances of classifications increase. In other words, the classification threshold for search products is higher than that for experience products (i.e., τ > τ ). Thus, Hypothesis 3 is supported.

Table 7  
Performance metrics of helpfulness classification.

<table><tr><td>Product type</td><td>Threshold</td><td>Performance metrics</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td rowspan="2">Search products</td><td rowspan="2">4</td><td>Accuracy</td><td>89.4%</td><td>91.2%</td><td>90.9%</td><td>93.4%</td></tr><tr><td>AUC</td><td>0.806</td><td>0.843</td><td>0.845</td><td>0.894</td></tr><tr><td rowspan="2">Experience products</td><td rowspan="2">2</td><td>Accuracy</td><td>79.3%</td><td>82.1%</td><td>82.0%</td><td>86.4%</td></tr><tr><td>AUC</td><td>0.649</td><td>0.745</td><td>0.755</td><td>0.860</td></tr><tr><td rowspan="2">All products</td><td rowspan="2">3</td><td>Accuracy</td><td>70.6%</td><td>73.9%</td><td>74.2%</td><td>78.5%</td></tr><tr><td>AUC</td><td>0.683</td><td>0.775</td><td>0.747</td><td>0.823</td></tr></table>

Notes: Model 1 is our baseline model and only contains control variables. Model 2 incorporates the number of attributes. Model 3 incorporates the average length of attributes. Model 4 covers all attributes

![](/api/attachments/5932FVNX/fulltext/images/9d68e3bc69798c0eba482b391823e14bedb6cd0490314c0dbd8e236163900cb6.jpg)

![](/api/attachments/5932FVNX/fulltext/images/381e8628bf3dc183b67281d36718ef05942d81f54cf0a2d0046ebbb98a39be81.jpg)  
Fig. 5. Performance metrics of helpfulness classification.

![](/api/attachments/5932FVNX/fulltext/images/98909f6bbf458af2d2fa7b6bdb72b579447758f9a457570cce235d6c8b1b5097.jpg)  
Fig. 6. The comparison of prediction results between review length and in formativeness

Notes: Model A is the baseline model including review-related variables and reviewer-related variables: Model B only incorporates review length: Model C only incorporates informativeness  
![](/api/attachments/5932FVNX/fulltext/images/0a28227e68467655c3e9695baffa261fe7697c0750ba62fec9b62416e8293943.jpg)  
Fig. 7. The joint impact of informativeness metrics  
Notes: Model 1 is our baseline model and only contains control variables. Model 2 incorporates the number of attributes. Model 3 incorporates the average length of attributes. Model 4 covers all attributes.

## 6. Prediction analysis

## 6.1. Main prediction analysis

The early section illustrates the efect of review informativeness on review helpfulness and gives optimal classification thresholds for search and experience products. Here, we check the predictive power of review informativeness and proposed thresholds in helpfulness classification. Considering the limited space, we only show the results calculated by Random Forests which is widely applied in the helpfulness classification [6,31]. Ten-fold cross-validation is utilized to calculate the classification performance metrics, including AUC and Accuracy. We display the results in Table 7 and Fig. 5.

After comparing the performance metrics for diferent attributes and thresholds, we reach the following conclusions. First, Model 2, Model 3, and Model 4 have better performance metrics than Model 1, which implies that review informativeness can increase the power of the prediction. Second, we compare our models to the benchmark models where all products are pooled together (without diferentiating search products from experience products), the optimal classification threshold value for all products is 3. Fig. 5 shows that, by applying the optimal classification threshold of 2 (for experience products) and 4 (for search products), all four models outperform the benchmark model.

## 6.2. Additional prediction analysis

To highlight our paper's contributions, we compare classification performance between review length and review informativeness. We conduct prediction experiments through applying Random Forest. Fig. 6 shows the superiority of our four variables in the helpfulness classification.

Moreover, we analyze the joints impact of informativeness metrics based on the previous experiment results. The results, shown in Fig. $^ { 7 , }$ demonstrate that combining two measurements together (Model 4, combining the number of attributes and the average length of attributes) ofers a better prediction about the review helpfulness, compared to a single measure (Model $^ { 2 , }$ using solely the number of attributes; and Model $^ { 4 , }$ using solely the average length of attributes).

## 7. Conclusion and future work

In this paper, we examine the impact of informativeness on review helpfulness, and propose diferent classification thresholds to classify helpful reviews by considering the diferences between search products and experience products.

To the best of our knowledge, our study is the first to introduce and systematically explore the role of informativeness in enhancing review helpfulness. Compared to extant literature that studies the impact of review length $[ 7 , 9 , 1 6 , 3 9 ]$ , our metrics of informativeness can avoid interference from pointless, tedious information and allow for the identification of meaningful information that contains attributes. We have also employed regression and machine learning techniques to demonstrate the superiority of our measures of attributes. In summary, informativeness, as variables to identify helpful reviews, significantly improve the accuracy of predicting review helpfulness compared to the measurement of review length in previous literature.

This paper is the first to propose diferent classification thresholds for search products and experience products, respectively. Most prior research has not considered the impact of product type on review helpfulness [15,28,40]. Our paper explains why the classification threshold of a search product is larger than that of an experience product. Experiment 2 and the prediction model also demonstrate the superiority of our purposed classification thresholds. Our results about the classification thresholds provide guidelines for future research on review helpfulness.

Our paper designs four attribute variables to measure review informativeness based on whether it is platform-based or product-based, and whether it refers to the number of attributes or the average length of attributes. The experiment results show that our proposed attribute variables demonstrate strong prediction power for review helpfulness, ultimately helping consumers make better purchase decisions. Furthermore, based on the classification performance, combining the impact of both the number of attributes and the average length of attributes on review helpfulness is much better than a single measure of attributes.

From a practical perspective, this study updates lexicons that can help manufacturers extract attributes that reflect consumers' usage experiences. By analyzing attributes, manufacturers can more quickly understand consumer's preference, and, thus, design better products [48,52,53]. In fact, this approach may be more accurate and eficient than questionnaire surveys. Moreover, traditionally, consumers may need to browse a great many repetitive and outdated online reviews before they can extract useful information. Our analysis about attributes and classification thresholds helps to automatically identify helpful reviews for them. It ofers guidelines to design a better online review system or recommendation system to help consumers obtain useful information more eficiently.

This study is not without limitations. Our data were obtained from a single website (i.e., JD.com), and it would be helpful to discover whether the conclusions hold for data from other online markets. In addition, the current model does not incorporate sentiment analysis, which has been shown to have reasonably good predictability for review helpfulness [66]. It would be valuable in the future to explore how product and platform attribute sentiments could influence review helpfulness.

## Funding

This research was supported by the Natural Science Foundation of Shaanxi Province (2017JM7009), the Soft Science Research Program of Shaanxi (2018KRZ005), MOE Project of Humanities and Social Science (14YJCZH167), the National Science Foundation of China (31701150; 11501414), the Fundamental Research Funds for the Central Universities (CXTD2017003), China; and the Hong Kong Research Grant Council (11507218, 11500216, 11501414).

## References

[1] N. Archak, A. Ghose, P.G. Ipeirotis, Deriving the pricing power of product features by mining consumer reviews, Management Science 57 (8) (2011) 1485–1509.

[2] L. Baruh, Z. Cemalcılar, When more is more? The impact of breadth and depth of information disclosure on attributional confidence about and interpersonal attraction to a social network site profile owner, Cyberpsychology: Journal of Psychosocial Research on Cyberspace 12 (1) (2018).

[3] A. Benlian, R. Titah, T. Hess, Diferential efects of provider recommendations and consumer reviews in e-commerce transactions: an experimental study. Journal of Management Information Systems 29 (1) (2012) 237–272.

[4] L.A. Book, S. Tanford, W. Chang, Customer reviews are not always informative: the impact of efortful versus heuristic processing, Journal of Retailing and Consumer Services 41 (2018) 272–280.

[5] Q. Cao, W. Duan, Q. Gan, Exploring determinants of voting for the “helpfulness” of online user reviews: a text mining approach, Decision Support Systems 50 (2) (2011) 511–521.

[6] R. Caruana, A. Niculescu-Mizil, An empirical comparison of supervised learning algorithms using diferent performance metrics, Proc. 23rd International Conference Machine Learning (ICML ’06), 2006, pp. 161–168.

[7] Y. Chi, X. Tang, Y. Lian, X. Dong, Y. Liu, A supernetwork-based online post in formative quality evaluation model, Knowledge-Based Systems 168 (2019) 10–24.

[8] A.Y.K. Chua, S. Banerjee, Understanding review helpfulness as a function of reviewer reputation, review rating, and review depth, Journal of the Association fo Information Science and Technology 66 (2) (2015) 354–362.

[9] A.Y.K. Chua, S. Banerjee, Helpfulness of user-generated reviews as a function of review sentiment, product type and information quality, Computers in Human Behavior 54 (2016) 547–554.

[10] S.P. Eslami, M. Ghasemaghaei, K. Hassanein, Which online reviews do consumers find most helpful? A multi-method investigation, Decision Support Systems 113 (2018) 32–42

[11] R. Filieri, What makes online reviews helpful? A diagnosticity-adoption framework to explain informational and normative influences in e-WOM. Journal of Business Research 68 (6) (2015) 1261–1270

[12] R. Filieri, F. McLeay, B. Tsui, Z. Lin, Consumer perceptions of information help fulness and determinants of purchase intention in online consumer reviews of services. Information & Management 55 (2018) 956–970

[13] B.J. Fogg, J. Marshall, O. Laraki, A. Osipovich, C. Varma, N. Fang, J. Paul, A. Rangnekar, J. Shon, P. Swani, M. Treinen, What makes web sites credible? A report on a large quantitative study, Proceedings of the SIGCHI Conference on Human Factors in Computing, 2001, pp. 61–68.

[14] C. Forman, A. Ghose. B. Wiesenfeld. Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Information Systems Research 19 (3) (2008) 291–313.

[15] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics. JEEE Transactions on Knowledge and Data Engineering 23 (10) (2011) 1498–1512.

[16] T. Girard. P. Dion, Validating the search, experience, and credence product classi fication framework Journal of Business Besearch 63 (9–10) (2010) 1079–1087

[17] H. Hong, D. Xu, G.A. Wang, W. Fan, Understanding the determinants of online review helpfulness: a meta-analytic investigation, Decision Support Systems 102 (2017) 1–11.

[18] Y.K. Hong, P.A. Pavlou, Product fit uncertainty in online markets: nature, efects, and antecedents, Information Systems Research 25 (2) (2014) 328–344.

[19] Y.-H. Hu, K. Chen, Predicting hotel review helpfulness: the impact of review visibility, and interaction between hotel stars and review ratings International Journa of Information Management 36 (6) (2016) 929–944

[2o] A.H. Huang. K. Chen. D.C. Yen. T.P. Tran. A study of factors that contribute to online review helpfulness, Computers in Human Behavior 48 (2015) 17–27.

[21] A.H. Huang, D.C. Yen, Predicting the helpfulness of online reviews: a replication, International Journal of Human Computer Interaction 29 (2) (2013) 129–138

[22] L. Huang, C.-H. Tan, W. Ke, K.-K. Wei, Comprehension and assessment of product reviews: a review-product congruity proposition, Journal of Managemen Information Systems 30 (3) (2013) 311–343

[23] L. Huang, C.-H. Tan, W. Ke, K.-K. Wei, Do we order product review informatio display? How? Information & Management 51 (7) (2014) 883–894.

[24] F.R. Jiménez, N.A. Mendoza, Too popular to ignore: the influence of online reviews on purchase intentions of search and experience products. Journal of Interactive Marketing 27 (3) (2013) 226–235

[25] Q. Jones, G. Ravid, S. Rafaeli, Information overload and the message dynamics of online interaction spaces: a theoretical model and empirical exploration. Information Systems Research 15 (2) (2004).194–210

[26] Y. Kang, L. Zhou, RubE: rule-based methods for extracting product features from online consumer reviews, Information & Management 54 (2) (2017) 166–176.

[27] S. Karimi, F. Wang, Online review helpfulness: impact of reviewer profile image, Decision Support Systems 96 (2017) 39–48.

[28] N. Korfiatis, E. García-Bariocanal, S. Sánchez-Alonso, Evaluating content quality and helpfulness of online product reviews: the interplay of review helpfulness vs. review content, Electronic Commerce Research and Applications 11 (3) (2012) 205–217.

[29] S. Krishnamoorthy, Linguistic features for review helpfulness prediction, Expert Systems with Applications 42 (7) (2015) 3751–3759.

[30] E.-J. Lee, S.Y. Shin, When do consumers buy online product reviews? Efects of review quality, product type, and reviewer’s photo, Computers in Human Behavior 31 (2014) 356–366.

[31] P.-J. Lee, Y.-H. Hu, K.-T. Lu, Assessing the helpfulness of online hotel reviews: a classification-based approach. Telematics and Informatics 35 (2) (2018) 436–445

[32] M. Li, C.-H. Tan, K.-K. Wei, K. Wang, Sequentiality of product review information provision: an information foraging perspective, MIS Quarterly 41 (3) (2017) 867–892.

[33] S. Liang, M. Schuckert, R. Law, How to improve the stated helpfulness of hotel reviews? A multilevel approach, International Journal of Contemporary Hospitalit Management 31 (2) (2019) 953–977

[34] J.-S. Lim, A. Al-Aali, J.H. Heinrichs, Impact of satisfaction with e-retailers’ touch points on purchase behavior: the moderating efect of search and experience product type, Marketing Letters 26 (2) (2014) 225–235.

[35] X.W. Liu, M. Schuckert, R. Law, Utilitarianism and knowledge growth during status seeking: evidence from text mining of online reviews, Tourism Management 66 (2018) 38–46.

[36] Z. Liu, S. Park, What makes a useful online review? Implication for travel product websites, Tourism Management 47 (2015) 140–151.

[37] J. Luan, Z. Yao, F. Zhao, H. Liu, Search product and experience product online reviews: an eye-tracking study on consumers’ review search behavior, Computers in Human Behavior 65 (2016) 420–430.

[38] C. Luo, X. Luo, Y. Xu, M. Warkentin, C.L. Sia, Examining the moderating role of sense of membership in online review evaluations, Information & Management 52 (3) (2015) 305–316.

[39] M. Ma, R. Agarwal, Through a glass darkly: information technology design, identity verification, and knowledge contribution in online communities, Information Systems Research 18 (1) (2007) 42–67.

[40] J.E. Maddux, R.W. Rogers, Efects of source expertness, physical attractiveness, and supporting arguments on persuasion - a case of brains over beauty, Journal of Personality and Social Psychology 39 (2) (1980) 235–244.

[41] M.S.I. Malik, A. Hussain, Helpfulness of product reviews as a function of discrete positive and negative emotions, Computers in Human Behavior 73 (2017) 290–302.

[42] M.S.I. Malik, A. Hussain, An analysis of review content and reviewer variables that contribute to review helpfulness, Information Processing & Management 54 (1) (2018) 88–104.

[43] S.M. Mudambi, D. Schuf, What makes a helpful online review? A study of customer reviews on amazon.com, MIS Quarterly 34 (1) (2010) 185–200.

[44] P. Nelson, Information and consumer behavior, Journal of Political Economy 78 (2) (1970) 311–329.

[45] P. Nelson, Advertising as information, Journal of Political Economy 82 (4) (1974) 729–754.

[46] T.L. Ngo-Ye, A.P. Sinha, The influence of reviewer engagement characteristics on online review helpfulness: a text regression model. Decision Support Systems 61 (2014) 47–58.

[47] T.L. Ngo-Ye, A.P. Sinha, A. Sen, Predicting the helpfulness of online reviews using a scripts-enriched text regression model, Expert Systems with Applications 71 (2017) 98–110.

[48] P. Pendharkar, A threshold varying bisection method for cost sensitive learning in neural networks, Expert Systems with Applications 34 (2) (2008) 1456–1464.

[49] A. Oazi, K.B. Shah Sved, R.G. Rai, E. Cambria, M. Tahir, D. Alghazzawi, A concept level approach to the analysis of online review helpfulness, Computers in Human Behavior 58 (2016) 75–81.

[50] J. Qi, Z. Zhang, S. Jeon, Y. Zhou, Mining customer requirements from online reviews: a product improvement perspective, Information & Management 53 (8) (2016) 951–963.

[51] P Racherla W Friske Perceived 'usefulness' of online consumer reviews: an exploratory investigation across three services categories, Electronic Commerce Research and Applications 11 (6) (2012) 548–559.

[52] M. Salehan, D.J. Kim, Predicting the performance of online consumer reviews: a sentiment mining approach to big data analytics, Decision Support Systems 81 (2016) 30–40.

[53] X.-F. Shao, Free or calculated shipping: impact of delivery cost on supply chains moving to online retailing, International Journal of Production Economics 191 (2017) 267–277.

[54] M. Siering, J. Muntermann, B. Rajagopalan, Explaining and predicting online review helpfulness: the role of content and reviewer-related signals, Decision Support Systems 108 (2018) 1–12.

[55] A. Singh, C.S. Tucker, A machine learning approach to product review disambiguation based on function, form and behavior classification, Decision Support Systems 97 (2017) 81–91.

[56] A.S. Singh, C.S. Tucker, Investigating the heterogeneity of product feature pre ferences mined using online product data streams, ASME 2015 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference, American Society of Mechanical Engineers, 2015.

[57] J.P. Singh, S. Irani, N.P. Rana, Y.K. Dwivedi, S. Saumya, P.K. Roy, Predicting the “helpfulness” of online consumer reviews, Journal of Business Research 70 (2017) 346–355.

[58] L.C. Tidwell, J.B. Walther, Computer-mediated communication efects on dis closure, impressions, and interpersonal evaluations: getting to know one another a bit at a time. Human Communication Research 28 (3) (2002) 317–348.

[59] R. Ullah, N. Amblee, W. Kim, H. Lee, From valence to emotions: exploring the distribution of emotions in online product reviews, Decision Support Systems 81 (2016) 41–53.

[60] R. Ullah, A. Zeb, W. Kim, The impact of emotions on the helpfulness of movie reviews, Journal of Applied Research and Technology 13 (3) (2015) 359–363.

[61] X. Wang, L. Tang, E. Kim, More than words: do emotional content and linguistic style matching matter on restaurant review helpfulness? International Journal of Hospitality Management 77 (2019) 438–447.

[62] D. Weathers, S.D. Swain, V. Grover, Can online product reviews be more helpful? Examining characteristics of information content by product type, Decision Support Systems 79 (2015) 12–23.

[63] J. Wu, Review popularity and review helpfulness: a model for user review effectiveness, Decision Support Systems 97 (2017) 92–103.

[64] S. Xiao, C.-P. Wei, M. Dong, Crowd intelligence: analyzing online product reviews for preference measurement, Information & Management 53 (2) (2016) 169–182.

[65] D. Yin, S.D. Bond, H. Zhang, Anxious or angry: efects of discrete emotions on the perceived helpfulness of online reviews, MIS Quarterly 38 (2) (2014) 539–560.

[66] D. Yu, Y. Mu, Y. Jin, Rating prediction using review texts with underlving sentiments, Information Processing Letters 117 (2017) 10–18.

[67] Y. Zhang, Z. Lin, Predicting the helpfulness of online product reviews: a multi lingual approach. Electronic Commerce Research and Applications 27 (2018) 1–10

[68] X. Zheng, S. Zhu, Z. Lin, Capturing the essence of word-of-mouth for social commerce: assessing the quality of online e-commerce reviews by a semi-supervised approach, Decision Support Systems 56 (2013) 211–222.

[69] S. Zhou, B. Guo, The order efect on online review helpfulness: a social influence perspective, Decision Support Systems 93 (2017) 77–87.

[70] D.H. Zhu, Z.J. Zhang, Y.P. Chang, S. Liang, Good discounts earn good reviews in return? Efects of price promotion on online restaurant reviews, International Journal of Hospitality Management 77 (2019) 178–186.

[71] H. Zhu, C.X.J. Ou, W.J.A.M. van den Heuvel, H. Liu, Privacy calculus and its utility for personalization services in e-commerce: an analysis of consumer decision: making, Information & Management 54 (4) (2017) 427–437.

Xinyu Sun is distinguished Research Fellow at the Department of Industrial Engineering of Xi'an Jiaotong University, P. R. China. He heads a competence laboratory on Forecasting and Big Data Intelligence. He received his degree of industrial engineering as well as his PhD from Xi'an Jiaotong University. His main interest fields are the quanti tative analysis of electric commerce, data mining and supply chain management. His previous research has been published in the Transportation Research Part B, European Journal of Operational Research and International Journal of Production Research

Maoxin Han is a Ph.D. student in the School of Management at the Xi'an Jiaotong University, China. His research interests include text analytics, online review, business intelligence and machine learning.

Juan Feng is a professor in the Department of Information Systems in the College of Business at the City University of Hong Kong, She holds a B.A. in economics from Renmin University of China, and a Ph.D. in Business Administration from Pennsylvania State University, with a dual degree in Operations Research. She has published in journals such as Management Science, Information System Research. Marketing Science, Decision Support Systems, etc. She is Associate Editor for Information System Research, and Senior Editor for E-Commerce Research and Applications.
