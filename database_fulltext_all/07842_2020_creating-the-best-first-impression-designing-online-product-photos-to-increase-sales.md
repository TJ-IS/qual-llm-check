---
otero_id: 7842
otero_key: "RKBXM4D4"
title: "Creating the best first impression: Designing online product photos to increase sales"
authors: "Huosong Xia; Xiaoting Pan; Yanjun Zhou; Zuopeng (Justin) Zhang"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113235"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Creating the best first impression: Designing online product photos to increase sales

![](/api/attachments/RKBXM4D4/fulltext/images/c654f7d3604ddd070f5e85b3eb27fe7df5308ea78b70f0a634a73268597abe93.jpg)

Huosong Xia<sup>a,1</sup>, Xiaoting Pan<sup>a</sup>, Yanjun Zhou<sup>a</sup>, Zuopeng (Justin) Zhang b,<sup>⁎</sup>

<sup>a</sup> School of Management, Wuhan Textile University, Wuhan 430073, China

<sup>b</sup> Coggin College of Business, University of North Florida, Jacksonville, FL 32224, USA

## A R T I C L E I N F O

Keywords: Product photos E-commerce Online sales First Sight Consumer reviews

## A B S T R A C T

Efectively displaying goods in search results is valuable for B2C merchants to earn clicks from consumers and even increase sales. Taking down jackets and trousers sold on Tmall—China's largest B2C e-commerce plat form—as the example, this paper collects data about three factors that influence consumers' first impression on their search results: the price of a product, the quantity of historical reviews, and a photo of the product. Among these factors, previous research shows that a product photo contains four attributes: brand logo, promotional information, street scenes, and model display. Focusing on these attributes, we apply a decision tree to explore customer purchasing patterns, which allows us to further investigate the influence of product photo attributes on sales volume by using a hierarchical regression model. Our research finds that among the products from the list of their search results, customers prefer those with many good historical reviews and low prices. In addition, gender that diferentiates men's from women's clothing has a moderating efect on the relationship between photo attributes and product sales. The purchase decision of consumers shopping for men's clothing is susceptible to the influence of the product photo. Furthermore, diferent from the traditional view which shows that brands can reduce perceived risks and increase sales, this study finds that men's clothing sales are negatively afected by brand logo attribute in product photos. Finally, using models cannot significantly increase product sales among consumers shopping for either men's or women's clothing.

## 1. Introduction

Electronic commerce today is often considered as a common business format. The traditional business-to-consumer (B2C) model has increasingly become a hotbed of fierce competition. A simple search for goods on a B2C e-commerce website will generate a lot of information on the resulted search page. Consumers' first impression on the search results is usually believed to have a great impact on their subsequent behavior and attitudes [1–3]. Previous studies show that consumers' purchase intentions are affected by various information system related factors in the e-commerce context, such as website quality [4,5], website design [6–8], and the display of product details [9,10]. However, when B2C e-commerce platforms become mature (such as Tmall, JD, and Amazon), they tend to employ the similar framework and functions; their store features and availability are not too much different. Therefore, online stores need to diferentiate themselves to attract customers with their unique features to catch their first best impressions. Online images are commonly used as a visual cue to draw consumers' attention to enhance their perception of product understanding, which directly impacts their purchasing decisions [3,11–13].

The visual attention conveyed by pictures becomes a key factor in human decision-making [14,15], but the diverse set of attributes in a picture may distract consumers' attention, causing them to focus on some particular attributes, which will decrease their ability to perceive important product information [16]. If online merchants cannot attract consumers' first impression with their unique characteristics when they browse the product search results, their competitiveness may be severely reduced [17]. For consumers, the dispersed attention due to distracted attributes will limit their capability of exploring and understanding the product information, thus reducing their purchasing intentions [13]. Therefore, how to properly design e-commerce product photos is a key challenge for all e-commerce companies.

Prior literature in the field of marketing and information systems has studied how to display commodity information to promote consumption. Existing studies in this area mainly focus on the following two research streams: (1) design of product description pages and (2)

design of merchandise display forms. The first research stream has analyzed how to design product description pages to enhance users' perceived usefulness and perceived ease of use [18,19], such as allowing comments in product descriptions [20] and strengthening the design of web and picture aesthetics [1]. The second stream has investigated how consumers' purchasing decisions are afected by different types of merchandise display forms [21], including text in formation [22], static photos [23], and virtual product experiences such as videos and interactions [24,25]. However, prior studies have not fully explored the relationship between product images and sales per formance in the e-commerce environment.

Our study attempts to address this research gap by investigating the following two key research questions.

1. Do the attributes in product photos afect the sales performance of B2C e-commerce products?

2. What attributes should be highlighted in product photos to improve the products' sales performance?

To answer these research questions, we conduct our study based on the Chinese e-commerce market, which is the world's largest e-commerce market that accounts for 40% of the global e-commerce transactions [26]. Specifically, our research collected two sets of data by searching down jackets and trousers from Tmall, the largest B2C online platform in China that integrates tens of thousands of global merchants and brands. The data collected allows us to examine the resulted search pages to check if product photos (1) use models, (2) are taken in outdoor scenes, (3) has a logo, and(or) (4) contain promotion information, and then to investigate the impact of these photo attributes on the sales performance of the products. It is worthwhile to note that our research analysis and findings are limited due to the focus on the Chinese market. Prior studies have shown the diferences and similarities of consumer behavior from diferent countries and regions in the e-commerce field. For instance, when processing visual information, Wes terners tend to pay more attention to the focal objects of marketing stimulus than Easterners, whereas Easterners will pay more attention to the overall information [27]. Furthermore, significant diferences have been identified between Chinese and American consumers in their vi sual processing of models' smiling facial expressions in product photos, even though there is no significant distinction in their ways of processing the promotional messages and logos presented in a text format [28]. Despite these diferences of consumer behavior on the e-commerce market, prior research confirms the significance of studying the online Chinese market as it can inform policy-making for e-commerce development in both developed and less-developed areas [29].

The rest of the paper proceeds as following. Next section presents a related literature review and summarizes the theoretical basis. Section 3 proposes the research hypothesis. Section 4 shows the data collection and preprocessing steps. Section 5 details the analysis and demonstrates the results. Last section concludes the paper with the highlights on managerial and theoretical contributions as well as the limitations and future research directions.

## 2. Prior literature and theoretical foundation

## 2.1. Product photos and their use in marketing

Consumer attention is a very valuable resource. In the field of marketing, a lot of research indicates that attention can directly or indirectly afect consumers' shopping behavior [15]. While the text and pictures in advertisements can attract consumers' visual attention, pictures can convey much richer content than words, and thus have a positive and prominent impact on consumer's memory and judgment [30].

Product photos are one of the most significant factors afecting consumers' attitudes and intentions toward online shopping [31].

Researchers have shown that product images have a positive impact on the perception of trust, enabling consumers to increase their willingness to purchase products in an e-commerce environment [32]. Product photos are an important way to help consumers enhance their product understanding; two indicators can be used to evaluate the performance of such understanding: consumer's actual knowledge of a product and perceived diagnostics [21]. The actual knowledge of a product is the extent to which a consumer actually understands the product information. It must include not only product-related attribute information, such as logos, but also stimulating shopping cues, such as pro motions. Perceived diagnostics is defined as the extent to which the presented information forms of goods can contribute to consumers perception of products in an e-commerce environment [33]. From these two perspectives—consumer's actual knowledge of a product and per ceived diagnostics, this paper studies how product photo attributes afect product sales through influencing the performance of consumers product understanding. As prior research has shown that sales are im pacted by product prices and the number of historical reviews [34–36], we also take these two confounding factors into consideration.

## 2.2. Limited attentional capacity theories

Attention plays an important role in influencing consumers' capabilities of information processing, decision-making, and behavioral intentions [37]. A large number of studies have shown that attention is directly related to a consumer's shopping behavior [15]. The Limited Attentional Capacity Theories have evolved from cognitive psychology. Kahneman [38] pointed out in his research that attention, a scarce psychological cognitive resource, is a process of assigning cognitive ability to a subject or task. According to the theory, a person's total attention capacity is limited at a certain time, i.e., paying attention to one thing must be at the expense of the attention to another. For example, in the marketing field, Garaus [39] showed that exposure to both mobile advertising and other marketing materials can reduce shoppers' focus on target stimuli and decrease their shopping desires. In the business environment, Stille [40] indicated that due to limited attention, purchasers are unable to process all of the business information in the store. Zhu [16] demonstrated that a store's decision to highlight certain attributes of its product afects its consumers' attitude toward the purchase of the product. In the field of e-commerce and information systems. Koufaris [18] found that due to the limitations of online consuming time and information processing resources, the duration of consumers' attention is short, so concentration is crucial for them to efectively complete their purchases. Markus [21] believed that if people's attention is distracted by more visual cues, they will suffer from the overload of personal working memory, that is, the information overload that will afect their product perception and purchasing intention. Therefore, we adopt this basic premise in our research: due to the limited attention, consumers cannot handle multiple information streams simultaneously in an e-commerce environment [41]. While the merchandise display frameworks on e-commerce platforms are roughly the same. photos of the same type of merchandises have different characteristics in diferent stores. Therefore, in the field of information systems, the relationship between sales and specific attributes in product photos provides a unique perspective for the application of this theory.

## 3. Hypothesis and research model

## 3.1. Impact of consumers' actual product knowledge on sales

Logo is one of the most important brand elements of a product. It can convey the brand image, attract consumers' attention, afect consumer's attitudes and “brand attachment”, and help consumers understand product information. A brand logo has its uniqueness and merits; the exposure of a brand logo influences consumers' attitudes and understanding of its products on a subconscious level [42]. Logo attribute in the product photos can be used as a stimulus to attract con sumers' attention, thereby distributing the limited attention of con sumers to these products. Therefore, we hypothesize as follows.

![](/api/attachments/RKBXM4D4/fulltext/images/1fed5653b0cda8324cb800db71dbdec697af5a356d4845502adf6f765806afcf.jpg)  
Fig. 1. The research model.

H1a. Controlling for the price and the quantity of historical comments, a product photo containing a brand logo can significantly increase the sales of the product.

Price promotion is relatively common in the marketing practice. Somesh [43] believed that when facing promotions, consumers are enabled to perceive the quality and value of products based on relevant information and to deepen their understanding of product information to obtain actual product knowledge, which has a positive efect on consumers' perceived value. Raju [34] pointed out that price promotion can attract potential consumers' attention and stimulate them to make positive purchasing decisions. However, according to some studies, not all promotions are equally satisfactory to consumers. For example, Manning [44] found that price promotions cannot significantly improve the number of purchases by consumers. Zhu [45] showed that price promotions can lead to an increase in consumer trafic but only slight improvement in sales. Malika [46] demonstrated that lowering product prices will reduce consumers' perception of product quality, which will have a negative impact on sales. Considering that consumers are faced with a large number of products when browsing a product search page, we believe that the promotion information in the product photos will attract consumers' attention, reduce the cost of information retrieval, increase their browsing time of the products, and influence their pur chase decisions. Therefore, we propose the following hypothesis.

H1b. Controlling for price and the quantity of historical comments, a product photo containing promotion information can significantly increase the sales volume of a product.

## 3.2. Impact of perceived diagnostics on sales

In the online shopping context, perceived diagnostics reflect the perceived ability of merchants to convey relevant product information to consumers, which helps customers understand and believe in the quality and performance of products sold online. From the perspective of signaling theory, Braddy [47] found that when consumers are not directly exposed to a product, they usually derive inferences from the available signals to form cognitive perceptions. Because customers cannot try clothes in online stores, models wearing them in product photos become an important signal that influences consumers' perception. In the case when the cognitive experience is weakened, knowing that “someone is shopping for me (shown by a model)” can help consumers better evaluate products and reduce transaction uncertainty. In this study, we default that if a model is chosen to be included in product photos, the model will be able to meet the needs of a seller to display the product features with the best efect, so we do not consider the impact of diferent types of model on sales, for instance, the influence of a prettier model versus a less pretty model on sales. Therefore, we next propose the following hypothesis.

H2a. Controlling for the price and the quantity of historical comments, displaying clothing with models can significantly improve the sales volume of the product.

The background of product photos should also be considered in the context of perceived diagnostics. When customers can imagine the using of products in their daily lives, their understanding of the products can be suficiently enhanced [48]. For clothes, customers may prefer to see the way they wear them on the street. Based on the most popular Stimulus–Organism–Response (SOR) framework in consumer behavior research [49], we believe that real streetscapes may generate contextual stimuli that afect the consumer response system and mobilize their purchase intentions. Therefore, we propose the following hypothesis.

H2b. Controlling for the price and the quantity of historical comments, showing clothing in a streetscape can significantly increase the sales volume of the product.

According to the above four hypotheses, H1a and H1b consider the impact of the design of the main product display on sales volume from the perspective of consumers' actual product knowledge. H2a and H2b describe the influence from the perspective of perceived diagnostics. At the same time, the product price and the number of historical comments that appear along with the main photo of the product in the search results are taken as control variables. The model of this paper is shown in Fig. 1.

## 4. Data collection and preprocessing

This section presents our data collection process and the preprocessing steps to get the data ready for analysis. We first summarize the mains steps and corresponding method for collecting our sample data, and then describe how we annotate the sample photos to incorporate the four features of photos.

Table 1  
Data collection process.

<table><tr><td>Main steps</td><td>Method</td></tr><tr><td>Step 1: Get data source</td><td>Add the parameter “jump logo to” to the URL of the search results to indicate page turning</td></tr><tr><td>Step 2: Grab data</td><td>Use regular expressions to grab product titles, store name, price, number of comments, monthly sales, and product photo address</td></tr><tr><td>Step 3: Store data</td><td>Use the Pandas library to store the above six-dimensional data in a two-dimensional table one by one</td></tr><tr><td>Step 4: Download photos</td><td>Write product photos to document by line in binary form</td></tr></table>

## 4.1. Data collection

The data of this study was collected from a landmark Chinese B2C platform—Tmall (tmall.com), which is China's largest e-commerce platform.

Using down jackets and trousers as examples, this study collects data to analyze the efect of attributes of product photos on sales. As the real-life shopping experience demonstrates, customers will not browse the product search results indefinitely. In order to avoid the interference of confounding factors, such as the order of products in the search results, and to ensure the credibility of the research results, we used “down jacket man”, “down jacket woman”, “trouser man” and “trouser woman” as the keywords and took the first five pages of the search results as data samples. Specifically, the Python program was used to obtain six dimensions of data on the front page of the Tmall search list, including the product photo URL, the product price, historical reviews, monthly sales, store name, and product name. The main steps and important parameters in the process of data collection are shown in Table 1.

The data of down jackets was collected in November 2017 and then imported into Excel. Finally, 546 samples of down jackets were ob tained, among which 273 were women's jackets and 273 men's jackets. The DOM structure of the page was slightly diferent due to the presence of advertisements in the list of search results. As a result, there were 40 samples with missing URLs in the data sets, including 20 men's and 20 women's jackets. So, the number of valid samples of down jackets was 506 with 253 for men and 253 for women, respectively. Trousers' data was collected in September 2019. As many attributes of the product photos of trousers need to be individually confirmed, we manually collected the following information: product photos, historical reviews, and monthly sales. A total of 500 valid samples of trousers were obtained, including 250 for men and 250 for women. Sample statistics for men's and women's clothing groups are shown in Table 2. The summary of statistics of the focal variables is shown in Table 3.

## 4.2. Data preprocessing

In the stage of data preprocessing, the most important work was to annotate the images to get the sample values of VL, VP, VM, and ${ \mathrm { V S } } ,$ related to the product photos in Fig. 1. In order to improve eficiency, when marking VL and VM, i.e., a brand logo and clothing models in a product's photo, SDK for Python programming along with the Baidu AI Platform was used for logo recognition<sup>2</sup> and face recognition.<sup>3</sup> Baidu AI Platform claims to be the world's leading AI service platform. In order to ensure the accuracy of the automatic marking, after the samples were marked, the variables were checked manually. The remaining variables, VP and VS, i.e., the promotional information and street scenes in a product's photo, were marked manually. Formulas (1) to (4) introduce the specific marking methods of the four variables, respectively.

$$
V L = \left\{ \begin{array}{l l} 1 & \text {   logo   is   contained   in   product   pictures } \\ 0 & \text {   other   situations } \end{array} \right.\tag{1}
$$

1 promotion information is contained product pictures in VP = 0 other situations

(2)

$$
V M = \left\{ \begin{array}{l l} 1 & \text { using   models   to   display   clothing } \\ 0 & \text { other   situations } \end{array} \right.\tag{3}
$$

$$
V S = \left\{ \begin{array}{l l} 1 & \text { using   street   scene   to   display   clothing } \\ 0 & \text { other   situations } \end{array} \right.\tag{4}
$$

In order to understand the criteria for variable tagging more directly, all 24 possible annotation situations should be shown. However, due to space constraints, only two extremes are demonstrated here, namely (1) VL = 1, VP = 1, VM = 1, and $\mathrm { V S } = 1 { } _ { ; }$ , and $( 2 ) \mathrm { \ V L } = 0 ,$ VP = 0, VM = 0, and ${ \mathrm { V S } } \ = \ 0 .$ . The former is the case when all four elements are present, shown in Fig. 2(a) and the latter is the case where none of the elements are present, shown in Fig. 2(b).

In order to explore the pattern of customers' choice from their search results, besides studying the influence of product photo elements on sales volume with a hierarchical regression model, we establish a classification model for the sales volume of diferent product characteristics with a data mining method. To proceed, we divide the price of goods, the number of historical comments, and the number of monthly transactions into diferent boxes to discretize them. Specifically, the upper quartile, median, and lower quartile of the above three variables were used as the thresholds. The three continuous variables were divided into four intervals. According to the position of the interval on the number axis, new values of 1, 2, 3, or 4 were assigned from left to right respectively. The labeled and separated samples were imported into SPSS Statistic 24.0, and the missing values were deleted to complete the data preprocessing. The changes from the raw data (translated) to the preprocessed data (translated) are shown in Tables 4 and 5, where Table 4 is part of the raw data collected and Table 5 is the preprocessed data added on the basis of the raw data. Details can be found in Appendix A.

## 5. Data analysis and results

This section details our data analysis and results. We first analyze customer purchasing patterns based on a decision tree, and then investigate the design elements of product photos with a hierarchical regression model.

## 5.1. Analysis of customer purchase patterns based on a decision tree

We discuss the pattern of customers' choices from their search results with a decision tree model in this subsection. Decision tree is one of the most classical algorithm models in the field of machine learning and data mining and can ofer good decision support capabilities. First, as a supervised classification model, a decision tree classifies discrete samples based on information entropy [50]. The basic idea of the algorithm is to classify the samples by the fields with the greatest information gain until the termination conditions are satisfied and a tree structure is formed. Therefore, in a decision tree, the uncertainty of information decreases from top to bottom, which can significantly reduce the influence of the inherent noise in data, so that the result of the algorithm has a high level of objectivity and accuracy. Second, a decision tree can summarize the decision rules from the data of various independent (input) variables and dependent variables (goals) and present these rules with the structure of a tree graph. This is important to help us understand the specific attributes that afect sales, which is defined as a white box property [51]. Finally, this algorithm runs relatively fast. The application based on decision trees includes target marketing, loss prediction, medical diagnosis, and so on. The limitation of a decision tree model is that it is not suitable for dealing with highdimensional data. When the number of attributes is too large, some decision trees are easy to over-fitting. In this study, the number of selected attributes is relatively small, which avoids the occurrence of over-fitting. The calculation of the information gain is described briefly as follows.

Table 2  
Descriptive statistics for men's and women's clothing groups.

<table><tr><td rowspan="2">Variables</td><td colspan="4">Men&#x27;s</td><td colspan="4">Women&#x27;s</td></tr><tr><td>Min</td><td>Max</td><td>Mean</td><td>Std.</td><td>Min</td><td>Max</td><td>Mean</td><td>Std.</td></tr><tr><td>Product price</td><td>12</td><td>2870</td><td>325.72</td><td>352.11</td><td>19</td><td>2624</td><td>394</td><td>410.15</td></tr><tr><td>Monthly sales</td><td>53</td><td>26,000</td><td>1170.84</td><td>2041.44</td><td>11</td><td>170,000</td><td>2970.11</td><td>11,588.29</td></tr><tr><td>Historical reviews</td><td>7</td><td>390,000</td><td>3139.27</td><td>20,092.79</td><td>0</td><td>1,370,000</td><td>17,537.68</td><td>89,485.70</td></tr></table>

Table 3  
The summary of statistics of the focal variables.

<table><tr><td>Attributes</td><td>Men&#x27;s (quantity)</td><td>Women&#x27;s (quantity)</td></tr><tr><td>VL</td><td>403</td><td>348</td></tr><tr><td>VP</td><td>136</td><td>168</td></tr><tr><td>VM</td><td>354</td><td>379</td></tr><tr><td>VS</td><td>336</td><td>319</td></tr></table>

Table 4  
Raw data (sample).

<table><tr><td></td><td>Title</td><td>Shop</td><td>Price</td><td>Deal</td><td>Review</td><td>Picture</td></tr><tr><td>1</td><td>Advanced light down jacket</td><td>Uniqlo official flagship store</td><td>499</td><td>607</td><td>1697</td><td>Coding of product photos</td></tr></table>

For any one group of information sources: $U = \mathbf { \left[ u _ { 1 } , \boldsymbol { u _ { 2 } . . . u _ { n } } \right] } ,$ there exists information entropy, i.e., the uncertainty of information $H ( U ) = \sum _ { i = 1 } ^ { \mathrm { n } } P ( u _ { i } ) { \cdot } \log _ { 2 } { \frac { 1 } { P ( u _ { i } ) } } = - \sum _ { i = 1 } ^ { \mathrm { n } } P ( u _ { i } ) { \cdot } \log _ { 2 } P ( u _ { i } )$ Therefore, any sample set $\overset { \mathbf { \scriptscriptstyle 1 } } { S } = ( o u t = C _ { k } , i n = \overset { \mathbf { \scriptscriptstyle 1 } - \mathbf { 1 } } { T _ { n m } } )$ indicates that the target variable C has k values, the input variable T has n dimensions, and each dimension has m values. According to the formula for computing information entropy, the information entropy of the sample set S can be written as $H ( S ) = - \sum _ { \mathrm { i } = 1 } ^ { k } P ( C _ { \mathrm { i } } ) { \cdot } \log _ { 2 } P ( C _ { \mathrm { i } } )$ . Similarly, the conditional entropy $H ( S \mid T _ { i } ) = \sum _ { j = 1 } ^ { m } H ( S \mid T _ { i j } ) = - \sum _ { j = 1 } ^ { m } P ( S \mid T _ { i j } ) { \cdot } \log _ { 2 } P ( S \mid T _ { i j } )$ is defined for the input variable T (i = 1,2…n), which demonstrates the information gain $G ( T _ { \mathrm { i } } ) ~ = ~ H ( C ) ~ - ~ H ( C | T _ { i } )$ of the input variable. The greater the information gain of the input variable, the greater its contribution to the classification of its target variable throughout the tree structure.

![](/api/attachments/RKBXM4D4/fulltext/images/e8c379b9cc25d7d35791458a205e1421dc6e920bcdc4a300c1881413de96483e.jpg)

![](/api/attachments/RKBXM4D4/fulltext/images/3dc162a0a8b53d05a61e19451452cabe30d6fa6ecb7681ffd9ce5f4db00b4960.jpg)  
(a)

![](/api/attachments/RKBXM4D4/fulltext/images/b6413a62d15d97cad066ef4496a9d0b6268142eb800d9619cb71b90ec05ee46b.jpg)

![](/api/attachments/RKBXM4D4/fulltext/images/9afee19428ed99e1132217ef8859412b1d6ed6198de1230a27fdd8c82e3b8d6b.jpg)  
(b)  
Fig. 2. Two situations of photo marking.

Table 5  
Preprocessed data added on the basis of the raw data (sample).

<table><tr><td></td><td>Brand</td><td>Promotional ads</td><td>Background</td><td>Models</td><td>Discrete prices</td><td>Discrete transaction</td><td>Discrete comments</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>4</td><td>4</td></tr></table>

This study develops a model of discrete sales with six variables, including discrete prices, historical comments, and the labeled variables VL, VP, VM, and VS with a C5.0 algorithm selected by SPSS Modeler v.14. The result is shown in Figs. 3 and 4. The decision tree is transformed to rules. The primary rules of the decision tree model of the men's down jacket and trousers are shown in Table 6 and the main rules of the decision tree model for the women's down jacket and trousers are shown in Table 7.

The above results infer that consumers shopping for men's clothing preferred the products with more historical reviews in the list of product search results (see Rule 1 and 5 in Table 6). In the case when the price is not low, the promotion information in the product photo will have a negative efect on the sales volume (see Rule 4 and 6 in Table 6). For down jackets, when the number of historical reviews was the highest, customers preferred name-brand clothing (see Rule 2 in Table 6); otherwise, when price was given as the priority, customers did not pay attention to the presence of models and street backgrounds in the main photos. For trousers, when there were very few historical reviews, customers tended to buy products with street backgrounds in photos (see Rule 7 in Table 6).

Customers shopping for women's clothing also preferred the products with more historical reviews (see Rule 1 and 6 in Table 7). Moreover, when there were a large number of historical reviews, women's clothing shoppers emphasized price. Low prices tended to lead to high sales (see Rule 2 and 7 in Table 7). For the highest-priced goods, the promotional and advertising information contained in the product photos were counterproductive to sales (see Rule 5 and 9 in Table 7). For down jackets, when the price was low, customers preferred a product photo taken in a street scene (see Rule 3 in Table 7); when the price was high, customers valued clothing brands (see Rule 4 in Table 7). For trousers, when there were more historical reviews, customers preferred product photos without street scenes (see Rule 8 in Table 7).

## 5.2. Analysis of design elements of product photos based on hierarchical regression

This subsection analyzes the design of a product photo using a hierarchical regression model. In particular, we study which elements of a product's photo can increase its sales volume. In Section 5.1, the choice pattern of consumers shopping for men's and women's clothing in product search results was found using a decision tree model; the factors they considered and their priorities had many similarities. For example, the two most important factors for customers shopping for men's and women's clothing were the quantity of comments and the price, but promotions and advertisements included in photos of high priced goods were regarded as negative factors. Studies have shown that men and women exhibit significant diferences in norms and values, resulting in them having diferent goals, decisions, and behaviors in the Internet environment [52]. Therefore, before establishing a hierarchical regression model, it is necessary to verify the rationality of dividing the samples into two categories—men's or women's clothing—according to gender. Based on this rationale, we took gender as a fixed factor to perform covariance analysis on the number of monthly transactions. The product design elements including VL, VP, VS, and VM, as well as the product price and the number of historical comments that might influence monthly transactions, which were controlled as covariant. The results are shown in Table 8, which shows that gender that diferentiates men's from women's clothing did have an impact on monthly sales (F = 48.13, P < .001). So, it is necessary to separate men's and women's data sets during data collection and then model the two data sets separately.

The essence of exploring how to increase sales by webpage photo design is to explore what elements of the product photos can lead to more sales. Therefore, based on a hierarchical regression model, we regarded product price and the quantity of historical reviews as controlling variables on the first layer and took the four variables of pro duct markings—VL, VP, VS, and VM—as independent variables on the second layer. Taking the monthly sales volume of products as the dependent variable, we developed models with men's and women's clothing data sets, respectively and added a collinearity test at the same time. The results are shown in the following tables.

According to the comparison between Tables 9 and 10, there was no significant collinearity (VIF ≈ 1) in the six variables involved in the model for men's clothing shoppers. In the product search results, the number of historical reviews and price did have a significant impact on the final sales volume and should be considered as control variables when studying the design of product photos. The interpretation function of the regression model was significantly improved (in Model 2, the adjusted R is 0.4 and 0.33) after the four variables associated with the product photo were added. Specifically, for both down jackets and trousers, VS, i.e., photos taken in street scenes, had a positive impact on sales volume, and the product photos containing the brand logo (VL) had a negative impact on sales. Displaying clothing with models (VM) showed no significant efect on the final sales volume.

Tables 11 and 12 show that there was no obvious collinearity (VIF ≈ 1) in the six variables involved in the regression model for women's clothing. For the control variables, the number of historical reviews and the price of the products had a significant impact on monthly sales. As control variables, they were contributing to the explanation of monthly sales volume. In Model 2, four new variables representing the design elements of products were added, i.e., VL, VP, VM and VS, and we found that there were no significant efects on the monthly sales.

The above results proved that, from a strictly statistical perspective, there were significant diferences between the responses of men's and women's clothing shoppers to the product search results when choosing down jacket and trousers. When controlling for product price and the number of historical reviews, men's clothing shoppers were significantly afected by product photos when choosing down jackets and trousers, but women's clothing shoppers' final purchase decisions seemed to be irrelevant to product photos. The validations of the hypotheses are shown in Table 13.

## 6. Discussions and conclusions

Following upon the data analysis results, we discuss their implica tions and highlight the theoretical and practical contributions of our research in this section. Finally, we conclude the paper with limitations and future research directions.

## 6.1. Discussion of data analysis results

Based on the real transactional data collected from Tmall, the study explores how to improve sales by designing the product photos in the search list. Taking down jacket and trousers as examples, we analyze if brand logos, promotion information, clothing models, and street scenes

![](/api/attachments/RKBXM4D4/fulltext/images/c5d366aa90b40b63cef6edf036b2edd7633d7c25dd5127db2e47e79c5ded91fd.jpg)

(a) Men's down jacket  
![](/api/attachments/RKBXM4D4/fulltext/images/275c4453c05cc3fd0063d16701f38b4c53f72c3a5e6668c6565c7aed8a8c5e99.jpg)  
(b) Men's trousers  
Fig. 3. Sales decision tree model of men's down jacket and trousers.

![](/api/attachments/RKBXM4D4/fulltext/images/df24b2e4c80af00add31aef80aec80267961e3281ef7dd927799455095078811.jpg)

(a) Women's down jacket  
![](/api/attachments/RKBXM4D4/fulltext/images/bd68e0bac865d474c162ac302c9ad0bd25417b5498ad2ff8fb96e25765568307.jpg)  
(b) Women's trousers  
Fig. 4. Sales decision tree model of women's down jacket and trousers.

Table 8  
Table 6  
Main rules for the decision tree model of men's down jacket and trousers.

<table><tr><td>ID</td><td>Rules</td></tr><tr><td>1</td><td> $count(d_vol \geq 3 | d_review \geq 3) = 93 > count(d_vol \geq 3 | d_review \leq 3)$ </td></tr><tr><td>2</td><td> $count(d_vol \geq 3 | d_review = 3 \cap d_prc \leq 2) = 29 > count(d_vol \geq 3 | d_review = 3 \cap d_prc \leq 2)$ </td></tr><tr><td>3</td><td> $count(d_vol \geq 3 | d_review = 3 \cap d_prc \leq 2) = 31 > count(d_vol \geq 3 | d_review = 3 \cap d_prc \geq 3)$ </td></tr><tr><td>4</td><td> $count(d_vol \geq 3 | d_review = 3 \cap d_prc = 3 \cap VP = 1) = 4 < count(d_vol \geq 3 | d_review = 3 \cap d_prc = 3 \cap VP = 0)$ </td></tr><tr><td>5</td><td> $count(d_vol \geq 3 | d_review \geq 3) > count(d_vol \geq 3 | d_review < 3)$ </td></tr><tr><td>6</td><td> $count(d_vol \geq 3 | d_review = 3 \cap VP = 1) < count(d_vol \geq 3 | d_review = 3 \cap VP = 0)$ </td></tr><tr><td>7</td><td> $count(d_vol = \geq 3 | d_review = 1 \cap VS = 1) < count(d_vol = \geq 3 | d_review = 1 \cap VS = 0)$ </td></tr></table>

Note: Count is a count function, d\_vol, d\_review, and d\_prc are the discrete monthly sales, historical reviews, and prices respectively. VP means if the product photo contains promotional information. VS denotes if the photo is taken in streetscape. VL represents if the produc photo contains the brand logo.

Table 7  
Main rules of the decision tree model of women's down jacket and trousers.

<table><tr><td>ID</td><td>Rules</td></tr><tr><td>1</td><td>count(d_vol ≥ 3|d_review ≥ 3) = 86 &gt; count(d_vol ≥ 3|d_review ≤ 3)</td></tr><tr><td>2</td><td>count(d_vol ≥ 3|d_review = 3 ∩ d_prc ≤ 2) = 31 &gt; count(d_vol ≥ 3|d_review = 3 ∩ d_prc ≥ 3)</td></tr><tr><td>3</td><td>count(d_vol ≥ 3|d_review = 3 ∩ d_prc ≤ 2 ∩ VS = 1) = 23 &gt; count(d_vol ≥ 3|d_review = 3 ∩ d_prc ≤ 2 ∩ VS = 0)</td></tr><tr><td>4</td><td>count(d_vol ≥ 3|d_review = 3 ∩ d_prc = 3 ∩ VL = 1) = 8 &gt; count(d_vol ≥ 3|d_review = 3 ∩ d_prc = 3 ∩ VL = 0)</td></tr><tr><td>5</td><td>count(d_vol ≥ 3|d_review = 3 ∩ d_prc = 4 ∩ VP = 1) = 0 &lt; count(d_vol ≥ 3|d_review = 3 ∩ d_prc = 4 ∩ VP = 0)</td></tr><tr><td>6</td><td>count(d_vol ≥ 3|d_review ≥ 3) = 86 &gt; count(d_vol ≥ 3|d_review ≤ 3)</td></tr><tr><td>7</td><td>count(d_vol ≥ 3|d_review = 4 ∩ d_price ≤ 2) &gt; count(d_vol ≥ 3|d_review = 4 ∩ d_price ≥ 3)</td></tr><tr><td>8</td><td>count(d_vol ≥ 3|d_review = 3 ∩ VS = 1) &lt; count(d_vol ≥ 3|d_review = 3 ∩ VS = 0)</td></tr><tr><td>9</td><td>count(d_vol ≥ 3|d_review = 4 ∩ d_price = 3 ∩ VP = 1) &lt; count(d_vol ≥ 3|d_review = 4 ∩ d_price = 3 ∩ VP = 0)</td></tr></table>

Note: count is a count function, d\_vol, d\_review, and d\_prc are the discrete monthly sales, historical reviews, and prices, respectively. VP means if the product photo contains promotional information. VS denotes if the photo is taken in streetscape. VL represents if the product photo contains the brand logo.

Covariance analysis on the influence of gender that diferentiates men's from women's clothing on monthly turnover (main efect method).

<table><tr><td>Variable</td><td>Square sum</td><td>Freedom</td><td>F</td><td>Sig.</td></tr><tr><td>Gender</td><td>29,114,004.69</td><td>1</td><td>48.13</td><td>0.000</td></tr><tr><td>VL</td><td>6,511,178.83</td><td>1</td><td>10.76</td><td>0.001</td></tr><tr><td>VP</td><td>2,636,659.21</td><td>1</td><td>4.36</td><td>0.036</td></tr><tr><td>VS</td><td>7,534,330.21</td><td>1</td><td>12.45</td><td>0.000</td></tr><tr><td>VM</td><td>408,323.48</td><td>1</td><td>0.675</td><td>0.412</td></tr><tr><td>Product prices</td><td>13,342,489.28</td><td>1</td><td>22.06</td><td>0.000</td></tr><tr><td>The number of historical reviews</td><td>16,190,151.20</td><td>1</td><td>26.77</td><td>0.000</td></tr></table>

Note: VP means that the product photo contains promotional information. VS represents that photo is taken in streetscape. VL indicates that the product photo contains the brand logo. VM denotes that photo contains model.

## Table 9

Hierarchical regression results of men's down jacket.

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td colspan="3">Layer 1</td></tr><tr><td>Product price</td><td>-0.39***(1.05)</td><td>-0.36***(1.08)</td></tr><tr><td>Product reviews quantity</td><td>0.35***(1.05)</td><td>0.32***(1.14)</td></tr><tr><td colspan="3">Layer 2</td></tr><tr><td>VL</td><td></td><td>-0.16**(1.12)</td></tr><tr><td>VP</td><td></td><td>0.10*(1.04)</td></tr><tr><td>VM</td><td></td><td>0.04(1.34)</td></tr><tr><td>VS</td><td></td><td>0.15**(1.37)</td></tr><tr><td>Freedom</td><td>2242</td><td>4238</td></tr><tr><td>Adjusted R2</td><td>0.33</td><td>0.40</td></tr><tr><td>ΔR2</td><td>0.34***</td><td>0.08***</td></tr><tr><td>ΔF</td><td>61.44***</td><td>8.26***</td></tr></table>

Parentheses are VIF values.  
<sup>⁎⁎⁎</sup> P < .001.  
<sup>⁎⁎</sup> P < .01.  
<sup>⁎</sup> P < .05.

Table 10  
Hierarchical regression results of men's trousers.

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td colspan="3">Layer 1</td></tr><tr><td>Product price</td><td>-0.36***(1.04)</td><td>-0.31***(1.12)</td></tr><tr><td>Product reviews quantity</td><td>0.35***(1.04)</td><td>0.34***(1.08)</td></tr><tr><td colspan="3">Layer 2</td></tr><tr><td>VL</td><td></td><td>-0.14*(1.11)</td></tr><tr><td>VP</td><td></td><td>0.05(1.03)</td></tr><tr><td>VM</td><td></td><td>0.06(1.01)</td></tr><tr><td>VS</td><td></td><td>0.14*(1.06)</td></tr><tr><td>Freedom</td><td>2246</td><td>4242</td></tr><tr><td>Adjusted R2</td><td>0.29</td><td>0.33</td></tr><tr><td>ΔR2</td><td>0.30***</td><td>0.05***</td></tr><tr><td>ΔF</td><td>52.44***</td><td>4.28***</td></tr></table>

Parentheses are VIF values.  
<sup>⁎⁎⁎</sup> P < .001.  
<sup>⁎</sup> P < .05.

shown in a product photo afect its final sales volume. Prior research finds that the price of goods and the number of historical comments that customers see in a list of search results have an impact on their purchasing intentions, so we consider them as control variables in our study.

Using a decision tree model and the sample classification perspective of decreasing information gain, we find that there were two obvious similarities between the purchasing patterns of men's and women's clothing shoppers when buying the sample goods. First, both men's and women's clothing shoppers took the number of historical reviews and product prices as important references for making choices at first glance. This finding is similar to that of Raju et al. [34] and Flovd et al. [36], which found that the number of historical reviews and low prices help increase online product sales. Second, enriching existing research on promotions and sales which claimed that not all promo tional information can stimulate sales [43,44,46], our study confirms that if the price of a product was too high, the promotion information in the main photo of the product had a negative efect on the sales volume of the product. Consumers are clearly wary of goods that are sold at high prices and promoted heavily. They may worry about buying fake goods or perceive a game of sellers raising then lowering the price.

Table 11  
Hierarchical regression results of women's down jacket.

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td colspan="3">Layer 1</td></tr><tr><td>Product price</td><td>-0.19**(1.04)</td><td>-0.19**(1.06)</td></tr><tr><td>Number of product reviews</td><td>0.45***(1.04)</td><td>0.44***(1.08)</td></tr><tr><td colspan="3">Layer 2</td></tr><tr><td>VL</td><td></td><td>0.04(1.04)</td></tr><tr><td>VP</td><td></td><td>-0.01(1.01)</td></tr><tr><td>VM</td><td></td><td>0.01(1.08)</td></tr><tr><td>VS</td><td></td><td>0.09(1.10)</td></tr><tr><td>Freedom</td><td>2250</td><td>4246</td></tr><tr><td>Adjusted R2</td><td>0.22</td><td>0.21</td></tr><tr><td>ΔR2</td><td>0.22***</td><td>0.01</td></tr><tr><td>ΔF</td><td>36.05***</td><td>0.72</td></tr></table>

Parenthesis VIF value.  
<sup>⁎⁎⁎</sup> P < .001.  
<sup>⁎⁎</sup> P < .01.

Table 12  
Hierarchical regression results of women's trousers.

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td colspan="3">Layer 1</td></tr><tr><td>Product price</td><td>-0.32***(1.33)</td><td>-0.29***(1.53)</td></tr><tr><td>Number of product reviews</td><td>0.42***(1.33)</td><td>0.43***(1.38)</td></tr><tr><td colspan="3">Layer 2</td></tr><tr><td>VL</td><td></td><td>-0.01(1.17)</td></tr><tr><td>VP</td><td></td><td>-0.07(1.11)</td></tr><tr><td>VM</td><td></td><td>-0.01(1.09)</td></tr><tr><td>VS</td><td></td><td>0.09(1.21)</td></tr><tr><td>Freedom</td><td>2247</td><td>4243</td></tr><tr><td>Adjusted R2</td><td>0.412</td><td>0.42</td></tr><tr><td>ΔR2</td><td>0.42***</td><td>0.01</td></tr><tr><td>ΔF</td><td>88.23***</td><td>1.48</td></tr></table>

Parenthesis VIF value.  
<sup>⁎⁎⁎</sup> P < .001.

Conducting the analysis with a hierarchical regression model, we also discover obvious diferences between men's and women's clothing shoppers in the choice of products. Specifically, controlling the price of goods and the quantity of historical comments, we find that the models, streetscapes, logos, and promotional information in product photos had no significant influence on women's clothing shoppers when they wanted to buy a down jacket or trousers, but the sales volume of men's products was positively afected by the streetscape element in product photos. In addition, although previous studies believed that brands have high commercial values [53,54], we found that the brand logo in the product photos had a negative relationship with sales volume and displaying clothing with models did not significantly boost sales. In summary, H1a, H1b, and H2a are not supported. H2b is partially supported.

Logos in the main photos of products cannot efectively help in crease sales. The possible reason is that logos are directly associated with brands and there are lots of brands available on the B2C platform Tmall with strong brands and weak brands co-existing simultaneously, where our sample data was collected. Strong brands have higher brand awareness and brand values [53], which can enhance their consumers brand loyalty [54]. In contrast, weak brands are dificult to derive their brand efect and thus have comparative disadvantages. However, prior research shows that brand awareness has no significant impact on customers' product purchase intentions in the e-commerce environment [31]. In particular, the brand of a product does not increase online consumers' desire to purchase due to the complementary promoting efect between ofline and online stores [55]. Furthermore, the role of brands to Chinese consumers is weakened in comparison to their Western counterparts, such as those from the United States, Germany, and Singapore, as Chinese consumers have more experience in dealing with counterfeit products and they sometimes purchase counterfeit products intentionally, especially clothing goods. They care more about the attributes of the products themselves, such as low prices and styles, rather than their brands [55].

The possible reason why H1b is not supported is that the promotion of diferent types of products has diferent incentives for people to consume, and the down jacket is generally more expensive than the trousers. Although men's down jackets are likely to be purchased by women, male customers still account for a considerable proportion [56]. Studies have shown that men and women have diferent motivations for spending time in an online environment; men are more rational than women, and women pay more attention to impression [52,56,57], which may indicate that consumers shopping for men's clothing will pay more attention to the price factor in actual product knowledge than those shopping for women's clothing in the process of browsing pictures of products. Therefore, the promotion of men's down jacket has a positive impact on consumers, but the promotion of men's trousers has nothing to do with consumer shopping, and for both down jacket and trousers, promotion cannot afect the purchase decisions of consumers shopping for women's clothing.

The reason why H2a is not supported may be that as the primary instrument of displaying products, the main photo of a product is the most important part for merchants. In order to achieve the ideal display efect, using a repeated modification of a model in several photos for diferent products has in fact become an open secret in the industry. At the same time, the physical characteristics of models are also diferent from those of ordinary consumers. Therefore, the impression formed by customers shopping for both women and men's clothing greatly reduce the perceived diagnostics, which makes the display of a model not a significantly influential factor in the purchase decision. Furthermore, the mainstream B2C platforms now support uploading images in customer reviews, which attracts some customers to upload photos of themselves in the clothing. This trend will further reduce models' in fluence on online purchase intention.

Table 13

<table><tr><td>Hypotheses</td><td>Men&#x27;s clothing customer</td><td>Women&#x27;s clothing customer</td></tr><tr><td>H1a: Controlling for the price and the quantity of historical comments, a product photo containing a brand logo can significantly increase the sales of the product.</td><td>Not supported (decrease the sales)</td><td>Not supported</td></tr><tr><td>H1b: Controlling for the price and the quantity of historical comments, a product photo containing promotion information can significantly increase the sales volume of the product.</td><td>Not Supported</td><td>Not supported</td></tr><tr><td>H2a: Controlling for the price and the quantity of historical comments, displaying clothing with a model can significantly improve the sales of the product.</td><td>Not supported</td><td>Not supported</td></tr><tr><td>H2b: Controlling for the price and the quantity of historical comments, showing clothing in a streetscape can significantly increase the sales volume of the product.</td><td>Supported</td><td>Not supported</td></tr></table>

Using the streetscape to show the efect of clothing, the result finds that men's clothing shoppers and sales showed a positive relationship, while women's clothing shoppers did not. The possible explanation is that using streetscape helps consumers shopping for men's clothing understand and believe that online products are appropriate in real life, which increases their product experience and perceived diagnostics. In contrast, women's clothing shoppers focused more on the efect presented by the product itself, avoiding the interference of other elements other than the product itself.

## 6.2. Theoretical implications

First, this research extends limited attention capacity theory to marketing and information system fields by applying it to explore the relationship between attributes in product photos and sales. In the ecommerce environment, product photos are used not only to present the basic information of products, but also to attract the attention of consumers and stimulate their intentions for consumption. Therefore, it is very important to explore the relationship between attributes in products photo and sales. This study strengthens the important role of image attributes in the e-commerce environment. Specifically, we find that some particular attributes in the product photos do afect the sales performance of B2C e-commerce sellers, reinforcing prior research's findings that pictures can attract the attention of consumers [3,15,31,58].

Second, previous studies have primarily focused on the ways to attract consumer attention and stimulate them to purchase from the perspectives of system quality [59], website design [8], and product details [10,25]. However, they did not explicitly consider the important fact that in electronic shopping websites, product photos bring the first impression to their consumers, attract their attention, and then lead to their perceptions and reactions. We are one of the first studies to examine the role of attributes in product photos from the perspective of data mining. In this paper, the display efect of product photos is measured by two factors—consumers' practical knowledge of a product and perceived diagnostics. The results show that diferent attributes in product photos have diferent efects on sales. As a result, we derive a more comprehensive understanding of the factors that afect sales, revealing some previously overlooked yet important elements in designing online product photos.

Third, considering the diferences in behavior between consumers shopping for men's and women's clothing in the e-commerce environment, consumers were grouped by gender that diferentiates them into men's or women's clothing shoppers in the research process. The results show that when controlling for product price and the quantity of historical comments, gender that diferentiates men's from women's clothing had a regulating efect on the relationship between the design elements of clothing product photos and the sales volume of products, which enriches the application of social role theory in the research field of online consumer purchase behavior [60,61].

## 6.3. Practical implications

The findings from this study make some practical recommendations for developing efective marketing strategies. First, sellers should be aware that a customer's purchase intention was positively afected by the number of product reviews and low prices at the first glance of goods in a search result list. Therefore, it is necessary for sellers to encourage consumers to give comments after their purchases. In terms of the relevant pricing strategy, if a product is not high-end, its selling price should not be too high to give customers a negative impression.

Second, sellers must understand the impact of product photo attributes on product sales for high-end products. According to the decision tree model, if a product is high-end with a high price, the promotional information contained in the product photos will have a negative efect on the sales volume. Therefore, sellers should control the frequency of promotional activities when marketing high-priced goods and avoid adding unnecessary promotional information in the product photos, which may cause customers' vigilance and negatively afect sales.

Third, although our research results show that displaying clothing with models had no significant positive impact on sales volume, we cannot deny the value of models as a visually attractive element to catch customers' attention [5]. Therefore, when designing product photos, sellers can display the properties of a commodity with their models to present its overall beauty from multiple aspects, such as the styles, fabric, and size of clothing.

Finally, the results of this study show that among all the design elements of product photos, product photos taken in streetscape are helpful in increasing the sales volume, while the logos may have a negative impact. Therefore, sellers should strive to incorporate street scenes into their product pictures and avoid using logos when designing product photos. Such a design can improve consumers' purchase intentions.

## 6.4. Limitations and future research directions

This study has several limitations. First, this study investigates the four photo attributes—models, streetscapes, promotional information, and logos—independently. As they may jointly afect sales volume, future research should study if there is an optimal combination of them according to the product type or customer type. Second, the study only explores the impact of the attributes on sales volume when they are present (or not present) in product photos. Future research should further study the design considerations of these attributes in product photos, for instance, the impact of diferent types of models (e.g., prettier versus less pretty models) on sales volume. Third, this study mainly takes Tmall.com in the Chinese market as the source of research data. Therefore, our research results and implications are exploratory in nature and only limited to the Chinese market. Future research needs to include additional sources of data, such as data from Europe or USA. Finally, taking down jackets and trousers as the examples in our study, the sample size was relatively small compared with the current trend in big data analysis. Future research needs to include a large number of products to produce comprehensive findings.

## Author contributions

All authors make approximately equal contributions from diferent aspects, including the conceptual design of the study, development and completion of the research, and writing, revising, and editing of the paper.

## Acknowledgments

This research has been supported by the National Natural Science Foundation of China (71571139; 71871172). We deeply appreciate the suggestions from fellow members of Xia's project team and Research Center of Enterprise Decision Support, Key Research Institute of Humanities and Social Sciences in Universities of Hu Bei Province (DSS20150215 & DSS20150108).

Appendix A. Raw data and preprocessed data

<table><tr><td></td><td>Title</td><td>Shop</td><td>Price</td><td>Deal</td><td>Review</td><td>pic</td></tr><tr><td>0</td><td>Women&#x27;s premium light down jacket 173,353 Uniqlo UNIQLO.</td><td>Uniqlo&#x27;s official flagship store.</td><td>499</td><td>607</td><td>1697</td><td>//img.alicdn.com/bao/uploaded/i4/372854151/TB2Ia.KaYL9F1JjSZJiXXcDGpXa_!!372854151.jpg</td></tr><tr><td>1</td><td>BSD Bosideng thin style lady sports fashion light hat simple down jacket B1601510.</td><td>Bosideng official flagship store.</td><td>358</td><td>105</td><td>890</td><td>//img.alicdn.com/bao/uploaded/i2/196993935/TB2iqeWsVXXXXc1XXXXXXXXXXX-196993935.jpg</td></tr><tr><td>2</td><td>MOCO winter large wool collar thickened down jacket women&#x27;s medium-and long-style MA1641EIN09 Moanke.</td><td>Moco official flag-ship store.</td><td>2589</td><td>265</td><td>408</td><td>//img.alicdn.com/bao/uploaded/i1/849905958/TB216_fdNaJ.eBjSsziXXaJ_XxA-849905958.jpg</td></tr><tr><td>3</td><td>Yaloo/Yalu down jacket women&#x27;s short hooded down jacket slim and slim winter coat YQ1101680.</td><td>Yalu official flag-ship store.</td><td>399</td><td>135</td><td>338</td><td>//img.alicdn.com/bao/uploaded/i4/158748311/TB2l7Uybp_AQeBjSZPhXXt5pXa_!!158748311.jpg</td></tr><tr><td>4</td><td>JNBY/Jiangnan cloth new fashionable short style down jacket 5H9712160 in autumn 2017.</td><td>Jiangnan cloth clothing official flagship store.</td><td>1090</td><td>173</td><td>10</td><td>//img.alicdn.com/bao/uploaded/i2/839919086/TB25wS7ceIPyuJjSspcXXiApXa_!!839919086.jpg</td></tr><tr><td>5</td><td>Gold velvet down jacket women&#x27;s medium-long style 2017 new winter wear Korean version fashion big hairy collar tide thickens South Korea over the knee.</td><td>Qige flagship store.</td><td>799.9</td><td>1372</td><td>537</td><td>//img.alicdn.com/bao/uploaded/i1/928417138/TB1n2DDIN3IL1JjSZPfXXcrUVXa_!!0-item_pic.jpg</td></tr><tr><td>6</td><td>Iger ES winter fashion cartoon than bear print long down jacket women 160,335,106.</td><td>Iger&#x27;s official flag-ship store.</td><td>719</td><td>53</td><td>60</td><td>//img.alicdn.com/bao/uploaded/i3/TB1KufzNFXXXXcMXFXXXXXXXXXX_!!0-item_pic.jpg</td></tr><tr><td>7</td><td>Vero Moda2017 winter new style feather collar white duck down short down jacket woman | 317,423,503.</td><td>Veromoda official flagship store.</td><td>1699</td><td>80</td><td>3</td><td>//img.alicdn.com/bao/uploaded/i4/TB12X2_OFXXXXgXFXXXXXXXXXX_!!0-item_pic.jpg</td></tr><tr><td>8</td><td>Disy2017 winter new down jacket women&#x27;s medium and long style Korean bread coat fox fur grass large fur collar coat.</td><td>Disy Deiss flagship store.</td><td>2080</td><td>152</td><td>37</td><td>//img.alicdn.com/bao/uploaded/i3/352469034/TB1N1JRnjqhSKJjSspnXXc79XXa_!!0-item_pic.jpg</td></tr><tr><td>9</td><td>[special area full complimentary] ONLY2017 autumn velvet button button cap loose down jacket woman | 117,312,517.</td><td>Only official flag-ship store.</td><td>1699</td><td>104</td><td>27</td><td>//img.alicdn.com/bao/uploaded/i1/173275708/TB1D3LfgnSPY1JjSZPcXXXIwpXa_!!0-item_pic.jpg</td></tr><tr><td>10</td><td>Pre-sale of Handu House 2017 Korean women&#x27;s winter wear new thin medium-and long-style trendy down jacket NF8417 suit.</td><td>Handu Yishe flag-ship store.</td><td>578</td><td>365</td><td>115</td><td>//img.alicdn.com/bao/uploaded/i3/693060164/TB1t_HSqBcHL1JjSZJiXXcKcpXa_!!0-item_pic.jpg</td></tr><tr><td>11</td><td>EIN/said that the white down jacket for women is medium-long, loose and light over the knee, and the new Korean version of 2017 winter clothes is a trend of slimming.</td><td>Ein flagship store.</td><td>2575</td><td>57</td><td>40</td><td>//img.alicdn.com/bao/uploaded/i3/797538549/TB1Squ5d6uhSKJjSspaXXXFgFXa_!!0-item_pic.jpg</td></tr><tr><td>12</td><td>Ochirly Oshili new women&#x27;s wear medium-length hooded wool collar loose long-sleeved down jacket 1HN4330910.</td><td>Ochirly official flagship store.</td><td>745</td><td>76</td><td>50</td><td>//img.alicdn.com/bao/uploaded/i4/1751100168/TB1W4OpbzJTMKJjSZFPXXbHUFXa_!!0-item_pic.jpg</td></tr><tr><td>13</td><td>ERAL/Elaiyi 2017 winter new simple down jacket slim medium-length hooded 16,151-FDAB.</td><td>Alaiyi official flag-ship store.</td><td>489</td><td>66</td><td>21</td><td>//img.alicdn.com/bao/uploaded/i4/397341302/TB1sKzQdfBNTKJjSszcXXbO2VXa_!!0-item_pic.jpg</td></tr><tr><td>14</td><td>DAZZLE new sweet magic color lotus leaf edge baseball collar waist long down jacket 2M4K30517.</td><td>Dazzle official flag-ship store.</td><td>1708</td><td>39</td><td>5</td><td>//img.alicdn.com/bao/uploaded/i3/454291526/TB1cegnkclHL1JjSZFBXXaiGXXa_!!0-item_pic.jpg</td></tr></table>

<table><tr><td></td><td>Title</td><td>Shop</td><td>Price</td><td>Deal</td><td>Review</td><td>Brand</td><td>Promotional ads</td><td>Background</td><td>Models</td><td>Discrete prices</td><td>Discrete transaction</td><td>Discrete comments</td></tr><tr><td>0</td><td>Women&#x27;s premium light down jacket 173,353 Uniqlo UNIQLO.</td><td>Uniqlo&#x27;s official flagship store.</td><td>499</td><td>607</td><td>1697</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>4</td><td>4</td></tr><tr><td>1</td><td>BSD Bosideng thin style lady sports fashion light hat simple down jacket B1601510.</td><td>Bosideng official flagship store.</td><td>358</td><td>105</td><td>890</td><td>1</td><td>0</td><td>1</td><td>1</td><td>2</td><td>4</td><td>4</td></tr><tr><td>2</td><td>MOCO winter large wool collar thickened down jacket women&#x27;s medium-and long-style MA1641EIN09 Moanke.</td><td>Moco official flagship store.</td><td>2589</td><td>265</td><td>408</td><td>1</td><td>0</td><td>0</td><td>0</td><td>4</td><td>1</td><td>2</td></tr><tr><td>3</td><td>Yaloo/Yalu down jacket women&#x27;s short hooded down jacket slim and slim winter coat YQ1101680.</td><td>Yalu official flagship store.</td><td>399</td><td>135</td><td>338</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>1</td><td>4</td></tr><tr><td>4</td><td>JNBY/Jiangnan cloth new fashionable short style down jacket 5H9712160 in autumn 2017.</td><td>Jiangnan cloth clothing official flagship store.</td><td>1090</td><td>173</td><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>2</td><td>4</td></tr><tr><td>5</td><td>Gold velvet down jacket women&#x27;s medium-long style 2017 new winter wear Korean version fashion big hairy collar tide thickens South Korea over the knee.</td><td>Qige flagship store.</td><td>799.9</td><td>1372</td><td>537</td><td>1</td><td>0</td><td>1</td><td>1</td><td>4</td><td>1</td><td>3</td></tr><tr><td>6</td><td>Iger ES winter fashion cartoon than bear print long down jacket women 160,335,106.</td><td>Iger&#x27;s official flagship store.</td><td>719</td><td>53</td><td>60</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>3</td><td>4</td></tr></table>

<table><tr><td>Veromoda official flagship store.</td><td>1699</td><td>80</td><td>3</td><td>1</td><td>0</td><td>0</td><td>1</td><td>3</td><td>1</td><td>4</td></tr><tr><td>Disy Deiss flagship store.</td><td>2080</td><td>152</td><td>37</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td>2</td><td>3</td></tr><tr><td>Only offi-cial flagship store.</td><td>1699</td><td>104</td><td>27</td><td>1</td><td>0</td><td>1</td><td>1</td><td>4</td><td>3</td><td>3</td></tr><tr><td>Handu Yishe flag-ship store.</td><td>578</td><td>365</td><td>115</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>4</td><td>3</td></tr><tr><td>Ein flagship store.</td><td>2575</td><td>57</td><td>40</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>4</td><td>3</td></tr><tr><td>Ochirly of-ficial flag-ship store.</td><td>745</td><td>76</td><td>50</td><td>1</td><td>0</td><td>0</td><td>1</td><td>4</td><td>4</td><td>3</td></tr><tr><td>Alaiyi offi-cial flagship store.</td><td>489</td><td>66</td><td>21</td><td>1</td><td>0</td><td>0</td><td>1</td><td>3</td><td>4</td><td>3</td></tr><tr><td>Dazzle offi-cial flagship store.</td><td>1708</td><td>39</td><td>5</td><td>1</td><td>0</td><td>0</td><td>1</td><td>4</td><td>3</td><td>2</td></tr></table>

## References

[1] Z. (Jack) Jiang, W. Wang, B.C.Y. Tan, J. Yu, The determinants and impacts of aesthetics in users' first interaction with websites, J. Manag, Inf. Syst. 33 (2016) 229–259. https://doi.org/10.1080/07421222.2016.1172443.

[2] G.H. Iten, A. Troendle, K. Opwis, Aesthetics in context—the role of aesthetics and usage mode for a website’s success, Interact. Comput. 30 (2018) 133–149, https:/ doi.org/10.1093/iwc/iwy002.

[3] A.J. King, A.J. Lazard, S.R. White, The influence of visual complexity on initial user impressions: testing the persuasive model of web design \*, Behav. Inf. Technol. 0 (2019)1-14, https://doi.org/10.1080/0144929X.2019.1602167.

[4] X. Chen, O. Huang, R.M. Davison, The role of website quality and social capital in building buvers' lovalty, Int. J. Inf. Manag. 37 (2017) 1563–1574, https://doi,org 10.1016/i jjinfomgt 2016.07 005

[5] Y. Liu, H. Li, F. Hu, Website attributes in urging online impulse purchase: an empirical investigation on consumer perceptions, Decis. Support. Syst. 55 (2013) 829–837, https://doi.org/10.1016/j.dss.2013.04.001.

[6] D. Cyr, Modeling web site design across cultures: relationships to trust, satisfaction, and E-Loyalty, J. Manag. Inf. Syst. 24 (2008) 47–72, https://doi.org/10.2753/ MIS0742-1222240402.

[7] D.V. Parboteeah, J.S. Valacich, J.D. Wells, The influence of website characteristics on a consumer’s urge to buy impulsively, Inf. Syst. Res. 20 (2009) 60–78, https:/ doi.org/10.1287/isre.1070.0157.

[8] Q. Wang, S. Yang, M. Liu, Z. Cao, Q. Ma, An eye-tracking study of website complexity from cognitive load perspective, Decis. Support. Syst. 62 (2014) 1–10, https://doi.org/10.1016/j.dss.2014.02.007.

[9] J. Bucko, L. Kakalejčík, M. Ferencová, Online shopping: factors that afect consumer purchasing behaviour, Cogent Bus. Manag. 5 (2018) 1–15, https://doi.org/10. 1080/23311975.2018.1535751

[10] M. Chen, Improving website structure through reducing information overload, Decis. Support. Syst. 110 (2018) 84–94, https://doi.org/10.1016/j.dss.2018.03. 009.

[11] R. Pieters, M. Wedel, Attention capture and transfer in advertising: brand, pictorial, and text-size efects, J. Mark. 68 (2004) 36–50, https://doi.org/10.1509/jmkg.68. 2.36,27794.

[12] G. Lindgaard, G. Fernandes, C. Dudek, J. Browñ, Attention web designers: vou have 50 milliseconds to make a good first impression!. Behay, Inf, Technol. 25 (2006) 115–126. https://doi.org/10.1080/01449290500330448

[13] J.H. Ahn. Y.S. Bae, J. Ju, W. Oh. Attention adiustment, renewal, and equilibrium seeking in online search: an eve-tracking approach, J. Manag, Inf, Syst, 35 (2018) 1218–1250. https://doi,org/10.1080/07421222,2018.1523595.

[14] H. Khachatrvan, A. Rihn, B. Behe, C. Hall, B. Campbell, J. Dennis, C. Yue, Visual attention, buving impulsiveness, and consumer behavior, Mark. Lett. 29 (2018) 23–35, https://doi.org/10.1007/s11002-018-9446-9.

[15] J. Romaniuk, C. Nguyen, Is consumer psychology research ready for today’s attention economy? J. Mark. Manag, 33 (2017) 909–916, https://doi.org/10.1080 0267257X,2017.1305706.

[16] Y. Zhu, A. Dukes, Prominent attributes under limited attention, Mark. Sci. 36 (2017) 683–698, https://doi.org/10.1287/mksc.2017.1037.

[17] A. Benlian, Web personalization cues and their diferential efects on user assessments of website value, J. Manag. Inf. Syst. 32 (2015) 225–260, https://doi.org/10. 1080/07421222.2015.1029394

[18] M. Koufaris, Applying the technology acceptance model and flow theory to online consumer behavior, Inf. Syst. Res. 13 (2002) 205–223, https://doi.org/10.1287/ isre.13.2.205.83

[19] S. Cai, Y. Xu, Designing not just for pleasure: efects of web site aesthetics on consumer shopping value, Int. J. Electron. Commer. 15 (2011) 159–187, https:// doi.org/10.2753/JEC1086-4415150405.

[20] Z. Wang, H. Li, Q. Ye, R. Law, Saliency efects of online reviews embedded in the description on sales: moderating role of reputation, Decis. Support. Syst. 87 (2016) 50–58. https://doi.org/10.1016/i.dss.2016.04.008

[21] LM. Markus, A. Maichzak, L. Gasser, The effects of presentation formats and task complexity on online consumers' product understanding. MIS O. 28 (2004) 695–704.

[22] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Inf. Syst. Res, 19 (2008) 291–313. https://doi,org/10.1287/isre,1080.0193.

[23] S. Zhang, D. Lee, P.V. Singh, K. Srinivasan, How Much Is an Image Worth? Airbnb Property Demand Estimation Leveraging Large Scale Image Analytics, https://ssrn. com/abstract=2976021 , Accessed date: 25 May 2017https://doi.org/10.2139/ ssrn.2976021.

[24] C. Yi, Z.J. Jiang, I. Benbasat, Enticing and engaging consumers via online product presentations: the efects of restricted interaction design, J. Manag. Inf. Syst. 31 (2015) 213–242, https://doi,org/10.1080/07421222,2014.1001270.

[25] P. Xu, L. Chen, R. Santhanam, Will video be the next generation of e-commerce product reviews? Presentation format and the role of product type, Decis. Support Syst. 73 (2015) 85–96, https://doi.org/10.1016/j.dss.2015.03.001.

[26] Y. Panova, A. Tan, O.-P. Hilmola, M.H. Puvindran, X. Hongsheng, W. Li, Evaluation of e-commerce location and entry to China – implications on shipping and trade, J. Shipp. Trade. 4 (2019), https://doi.org/10.1186/s41072-019-0045-6.

[27] M.N. Kastanakis, B.G. Voyer, The efect of culture on perception and cognition: a conceptual framework, J. Bus. Res. 67 (2014) 425–433, https://doi.org/10.1016/j jbusres.2013.03.028.

[28] Q. Wang, M. Wedel, L. Huang, X. Liu, Efects of model eye gaze direction on consumer visual processing: evidence from China and America, Inf. Manag. 55 (2018) 588–597, https://doi.org/10.1016/j.im.2017.12.003.

[29] D.C.W. Phang, K. Wang, Q. Wang, R.J. Kaufman, M. Naldi, How to derive causal insights for digital commerce in China? A research commentary on computational social science methods, Electron. Commer. Res. Appl. 35 (2019) 100837, , https:// doi,org/10.1016/i.elerap.2019.100837

[30] C. Lang, H. Barton, Just untag it: exploring the management of undesirable Facebook photos, Comput. Human Behav. 43 (2015) 147–155, https://doi.org/10. 1016/j.chb.2014.10.051.

[31] S.F. Liu, H.H. Liu, J.H. Chang, H.N. Chou, Analysis of a new visual marketing craze: the efect of LINE sticker features and user characteristics on download willingness and product purchase intention, Asia Pacific Manag, Rey. 24 (2018) 263–277 https://doi.org/10.1016/j.apmrv.2018.10.001.

[32] K. Grill-Spector, N. Kanwisher, Visual recognition: as soon as vou know it is there you know what it is, Psychol. Sci. 16 (2005) 152–160, https://doi.org/10.1111/j.

0956-7976.2005.00796.x.

[33] Z. Jiang, I. Benbasat, Virtual product experience: efects of visual and functional control of products on perceived diagnosticity and flow in electronic shopping, J. Manag. Inf. Syst. 21 (2004) 111–147, https://doi.org/10.1080/07421222.2004. 11045817.

[34] J.S. Raju, The efect of price promotions on variability in product category sales, Mark. Sci. 11 (1992) 207–220, https://doi.org/10.1287/mksc.11.3.207.

[35] B. von Helversen, K. Abramczuk, W. Kopeć, R. Nielek, Influence of consumer reviews on online purchasing decisions in older and younger adults, Decis. Support. Syst. 113 (2018) 1–10, https://doi.org/10.1016/j.dss.2018.05.006.

[36] K. Floyd, R. Freling, S. Alhoqail, H.Y. Cho, T. Freling, How online product reviews afect retail sales: a meta-analysis, J. Retail. 90 (2014) 217–232, https://doi.org/10. 1016/i.iretai,2014.04.004

[37] L. (Cathy) Yang, O. Toubia, M.G. de Jong, Attention, information processing, and choice in incentive-aligned choice experiments, J. Mark. Res. 55 (2018) 783–800 https://doi.org/10.1177/0022243718817004.

[38] H. Egeth, D. Kahneman, Attention and Efort, (1975), https://doi.org/10.2307/ 1421603.

[39] M. Garaus, U. Wagner, A.M. Bäck, The efect of media multitasking on advertising message efectiveness, Psychol. Mark. 34 (2017) 138–156, https://doi.org/10. 1002/mar.20980.

[40] K.M. Stilley, J.J. Inman, K.L. Wakefield, Planning to make unplanned purchases? The role of in-store slack in budget deviation, J. Consum. Res. 37 (2010) 264–278 https://doi.org/10.1086/651567.

[41] G. RepovŠ, A. Baddeley, The multi-component model of working memory: explorations in experimental cognitive psychology, Neuroscience 139 (2006) 5–21 https://doi.org/10.1016/i.neuroscience.2005.12.061.

[42] Sääksjärvi, van den Hende, Mugge, How exposure to logos and logo varieties fosters brand prominence and freshness, J. Prod. Brand. Manag. 24 (2015) 736–744.

[43] S.K. Sinha, P. Verma, Impact of sales promotion’s benefits on perceived value: does product category moderate the results? J. Retail. Consum. Serv. 52 (2020) 101887, , https://doi.org/10.1016/i.iretconser.2019.101887

[44] K.C. Manning, D.E. Sprott, Multiple unit price promotions and their efects on quantity purchase intentions, J. Retail. 83 (2007) 411–421, https://doi.org/10. 1016/j.jretai.2007.03.011.

[45] Z. Huawei, H. Minxue, F. Guoqun, Why does price promotion only bring popularity but not sales, Econ. Manag, 32 (2010) 86–91.

[46] M. Chaudhuri, R.J. Calantone, C.M. Voorhees, S. Cockrell, Disentangling the efects of promotion mix on new product sales: an examination of disaggregated drivers and the moderating efect of product class, J. Bus. Res. 90 (2018) 286–294, https:/ doi.org/10.1016/j.jbusres.2018.05.020.

[47] P.W. Braddy, A.W. Meade, C.M. Kroustalis, Online recruiting: the efects of organizational familiarity. website usability. and website attractiveness on viewers impressions of organizations, Comput. Human Behav. 24 (2008) 2992–3001, https://doi.org/10.1016/j.chb.2008.05.005.

[48] S. Molinillo, F. Liébana-Cabanillas, R. Anaya-Sánchez, D. Buhalis, DMO online platforms: image and intention to visit, Tour. Manag. 65 (2018) 116–130, https:/ doi.org/10.1016/j.tourman.2017.09.021.

[49] T.K.H. Chan, C.M.K. Cheung, Z.W.Y. Lee, The state of online impulse-buying research: a literature analysis, Inf. Manag. 54 (2017) 204–217, https://doi.org/10. 1016/i.im.2016.06.001.

[50] N.Z. Aydinoǧlu, L. Cian, Show me the product, show me the model: efect of picture type on attitudes toward advertising, J. Consum. Psychol. 24 (2014) 506–519, https://doi.org/10.1016/i.icps.2014.04.002.

[51] B. van Riessen, R.R. Negenborn, R. Dekker, Real-time container transport planning with decision trees based on ofline obtained optimal solutions, Decis. Support. Syst. 89 (2016) 1–16, https://doi.org/10.1016/j.dss.2016.06.004.

[52] X. Lin, D. Zhang, Y. Li, Delineating the dimensions of social support on social networking sites and their efects: a comparative model, Comput. Human Behav. 58 (2016) 421–430, https://doi.org/10.1016/j.chb.2016.01.017.

[53] M. Chica, Ó. Cordón, S. Damas, V. Iglesias, J. Mingot, Identimod: modeling and

managing brand value using soft computing, Decis. Support. Syst. 89 (2016) 41–55, https://doi.org/10.1016/j.dss.2016.06.007.

[54] A. Bilgihan, Gen y customer loyalty in online shopping: an integrated model of trust, user experience and branding, Comput. Human Behav. 61 (2016) 103–113, https://doi.org/10.1016/j.chb.2016.03.014.

[55] E.K. Clemons, J. Wilson, C. Matt, T. Hess, F. Ren, F. Jin, N.S. Koh, Global diferences in online shopping behavior: understanding factors leading to trust, J. Manag. Inf. Syst. 33 (2016) 1117–1148, https://doi.org/10.1080/07421222.2016.1267531.

[56] Z. Zhi, Insight report on medium and high-end menswear consumers, China Mark 12 (2014) 52–54.

[57] N. Li, G. Kirkup, Gender and cultural diferences in internet use: a study of China and the UK, Comput. Educ. 48 (2007) 301–317, https://doi.org/10.1016/j compedu.2005.01.007.

[58] K. Wu, J. Vassileva, Y. Zhao, Z. Noorian, W. Waldner, I. Adaji, Complexity or simplicity? Designing product pictures for advertising in online marketplaces, J. Retail. Consum. Serv. 28 (2016) 17–27, https://doi.org/10.1016/j.jretconser.2015. 08.009.

[59] Y. Zheng, K. Zhao, A. Stylianou, The impacts of information quality and system quality on users' continuance intention in information-exchange virtual commu nities: an empirical investigation, Decis. Support. Syst. 56 (2013) 513–524, https:// doi.org/10.1016/i.dss.2012.11.008

[60] R.E. Guadagno, N.L. Muscanell, B.M. Okdie, N.M. Burk, T.B. Ward, Even in virtual environments women shop and men build: a social role perspective on Second Life, Comput. Human Behav. 27 (2011) 304–308, https://doi.org/10.1016/j.chb.2010. 08.008.

[61] Y.M. Hwang, K.C. Lee, Using an eye-tracking approach to explore gender diferences in visual attention and shopping attitudes in an online shopping environment, Int. J. Hum. Comput. Interact. 34 (2018) 15–24, https://doi.org/10.1080/ 10447318.2017.1314611.

Huosong Xia graduated from Huazhong University of Science and Technology in China Huosong Xia is a professor in the school of management at Wuhan Textile University. He was a visiting scholar at Eller College of Management of the University of Arizona. USA from 2006 to 2007. His main research interests are knowledge management, data mining, e-Commerce, and logistics information system. His publications have appeared in over 100 referred papers in journals, book chapters, and conferences, such as Journal of Knowledge Management, International Journal of Knowledge Management, Journal of Knowledge Management Practice, International Journal of Management, Journal of Systems Science and Information, Journal of Convergence Information Technology, Journal of Grey System, Financial Innovation (Springer), and World Journal of Social Science Research. He has obtained research funding from 4 projects with National Social Science Foundation of China and National Science Foundation of China

Xiaoting Pan graduated from Wuhan Textile University with a master's degree. He is interested in data mining and knowledge management.

Yanjun Zhou is a master candidate in the school of management at Wuhan Textile University. His main research interests are knowledge management, data mining, e-Commerce, and logistics information system.

Zuopeng (Justin) Zhang is a faculty member in the Coggin College of Business at University of North Florida. He was previously an Associate Professor of Management, Information Systems, and Analytics at State University of New York at Plattsburgh. He received his Ph.D. in Business Administration with a concentration on Management Science and Information Systems from Pennsylvania State University, University Park. His research interests include economics of information systems, knowledge management, electronic business, business process management, information security, and social net working. He is the editor-in-chief of the Journal of Global Information Management, an ABET program evaluator, and an IEEE senior member.
