---
otero_id: 20521
otero_key: "GEN4P2JZ"
title: "Consumer preference analysis based on text comments and ratings: A multi-attribute decision-making perspective"
authors: "Bin Zhu; Dingfei Guo; Long Ren"
year: "2022"
journal: "Information & Management"
doi: "10.1016/j.im.2022.103626"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Consumer preference analysis based on text comments and ratings: A multi-attribute decision-making perspective

![](/api/attachments/GEN4P2JZ/fulltext/images/c495338f4d0a7270590f414d238cf50907afe2461b00ca31f15a1e07cd38ca13.jpg)

Bin Zhu <sup>a,b</sup>, Dingfei Guo <sup>a</sup>, Long Ren <sup>c,\*,b</sup>

<sup>a</sup> School of Management and Economics, Beijing Institute of Technology, Beijing, 100081, China

<sup>b</sup> Yangtze Delta Region Academy of Beijing Institute of Technology, Jiaxing, Zhejiang, 314019, China

<sup>c</sup> School of Information Technology and Management, University of International Business and Economics, Beijing, 100029, China

## A R T I C L E I N F O

Keywords: Decision analysis Consumer preference Pairwise comparisons Hesitant judgment Sentiment analysis Recommendation

## A B S T R A C T

With the popularity of social media, extracting consumer preferences from online consumer-generated content is of vital importance for product/service providers to develop tailored marketing strategies. However, existing approaches face difficulties analyzing consumer preferences over different attributes of alternatives (restaurants, hotels, etc.), which hinders product/service providers from comprehensively understanding consumer choice decisions. To address this issue, we solve for the consumer preferences over the attributes represented by attribute weights based on consumers’ historical data, including text comments and overall ratings. Specifically, for each comment and a corresponding rating, we first employ sentiment analysis to calculate values of the attributes, and then develop a quadratic programming model to solve for the weights. Based on a stream of a consumer’s text comments and overall ratings, we can correspondingly obtain a stream of weights indexed by the comment time. We then model this stream of weights as hesitant judgments and employ a hesitant multiplicative programming method to solve for the final weights that fit the consumer’s preferences over attributes at the highest satisficing level. In the application of recommendation, our approach not only provides insights into the consumer’s preferences but also has higher prediction power compared with some state-of-the-art methods.

## 1. Introduction

With the popularity of information technology and social media, consumer-generated content, such as ratings, text comments, and video content, pave new avenues for managers who want to know their cus tomers more efficiently. Extracting preference information from tremendous consumer-generated content is of vital significance for product/service providers as well as platform owners. For instance, platform owners could employ the content to design more efficient marketing strategies, e.g., recommendations, market segmentation, and more targeted sales promotion. In particular, text comments embody rich information such as consumer preferences and sentiments, which cannot be neglected by platform managers who are interested in con sumer preference analysis.

Figure 1 provides an example of consumer comments regarding a hotel in Shanghai taken from the website Ctrip.com.<sup>1</sup> Ctrip.com founded in 1999 is currently the largest online travel agency in China and one of the largest travel service providers in the world.<sup>2</sup> The figure shows two reviews with text comments and corresponding ratings. The first con sumer, from China, rated the hotel as 4.3 stars (Excellent). She com mented, “Very convenient when you have to travel early the day after. Close to Pudong airport and free shuttle bus”. By analyzing the con sumer’s preferences embedded in the comments, we know that she was satisfied with the hotel’s location, but we know nothing about her preferences over other attributes, such as price and facilities. The second consumer, from the United States, rated the hotel as 4.5 stars, although he was obviously unsatisfied with the location (“Wish it was close to a subway stop...”) and the facilities (“The tv was old...”). So why did he still give a high overall rating?

In the literature, consumer preference analysis has drawn tremen dous attention from different disciplines, especially in marketing [2,11] and recommender systems [1,10,13,16]. In marketing, conjoint analysis [5,6] has been employed extensively. It is often used to analyze the preferences of a group of consumers. This method has wide applications in marketing, such as the estimation of consumers’ reservation prices [8] and market segmentation [4]. For more discussions on the applications of conjoint analysis, see [3,20] and the references therein. However, conjoint analysis faces difficulties analyzing individual preferences over attributes because as a statistic-based method it requires much data for the analysis. Recommender systems, such as the well-known collabo rative filtering [1] and content-based approaches [13], can filter out alternatives that a consumer might like on the basis of content generated by similar consumers. However, these approaches usually focus on predicting the overall ratings of alternatives rather than analyzing the preferences over attributes. Thus they have difficulties explaining the predicted ratings. In business practice, consumer preferences over at tributes of alternatives are important for business operators to improve the quality of alternatives and to meet consumer satisfaction. For example, one consumer may care more about the location of a hotel, while another may care more about its facilities. This preference infor mation is essential for hotels to find their target consumers and improve customer satisfaction.

![](/api/attachments/GEN4P2JZ/fulltext/images/07370fe92489d4a417e8c739c0fba80531ae98bc0d92694539ada7df679613a7.jpg)  
Fig. 1. An illustration of consumer comments on Ctrip.com.

Another stream of literature uses the techniques of multi-attribute decision making (MADM) [21,23] to analyze consumer preferences. In particular, a property named “preference consistency/consensus” is often utilized to analyze consumer preferences. This property is derived from the decision axiom of transitivity, which allows for reasoning about unknown preferences based on existing preferences. For example, Lee et al. [10] propose a collaborative-filtering recommender system by utilizing a mobile Web usage mining technique for consumer preference analysis. Since the collected preference information is insufficient and somewhat conflicting, a specific consensus-based model is employed to generate an ordinal scale-based consumer profile. Ren et al. [14] develop a data-driven optimization approach to analyze consumer preferences represented by pairwise comparisons. They use the overall rating information of consumers to model the pairwise comparisons and apply preference consistency to obtain consumer preferences over different movie categories. Based on both preference consistency and preference consensus, Ren et al. [15] employ robust optimization techniques and social network information to analyze consumer pref erences. These approaches have advantages when analyzing preferences based on limited consumer-generated content, but they have not yet delved into analyzing consumer preferences at the attribute level.

Motivated by the aforementioned business practice and literature gap, we propose a consumer preference analysis method based on con sumers’ reviews, including both ratings and text comments. We deal with this problem from the perspective of MADM. Specifically, we first employ sentiment analysis to calculate the attribute values of alterna tives from each text comment. Based on the obtained attribute values and their corresponding ratings, we establish an optimization model to solve for the attribute weights. Based on the historical ratings and text comments generated by a consumer, we can obtain a stream of attribute weights indexed by the comment time. From the perspective of MADM, the preferences derived from the consumer’s historical reviews gener ated over time could be inconsistent, due to errors or biases. Thus, we model the stream of weights as “hesitant judgments” and introduce a hesitant multiplicative programming method (HMPM, [25]) to solve for the weights that fit the consumer’s preferences at the highest satisficing level. In addition, we provide a real-world example utilizing the online dataset from Ctrip.com to show the efficiency of our approach. Our method provides insights into consumer preferences, and it is more ac curate at predicting ratings than some state-of-the-art methods, such as matrix factorization [9], user-based recommendation [24], and item-based recommendation [19].

We contribute to developing an approach that solves the problem of analyzing individual consumer preferences over attributes of alterna tives. This approach overcomes the limitation of conjoint analysis because it uses limited consumer-generated content to analyze individ ual preferences via an MADM technique. It overcomes the limitation of recommender systems because it can explain consumers’ ratings of al ternatives through the preference analysis of attributes. It also over comes the limitation of existing MADM-based consumer preference analysis methods, because it uses text comments in addition to ratings to analyze preferences over attributes, rather than only obtaining overall ratings.

The rest of this paper is structured as follows. Section 2 introduces how to construct hesitant judgments based on consumer reviews. In Section 3, we introduce the procedure of consumer preference analysis. In particular, we show how to use sentiment analysis to calculate attribute values. In Section 4, we develop a prioritization model to solve for the attribute weights and introduce the HMPM to solve for the sat isficing weights. Section 6 provides numerical studies with a real-world dataset. Section 7 concludes the paper.

![](/api/attachments/GEN4P2JZ/fulltext/images/a986fa743e8656271b205029331bc0925ab4ebc8a4f95183e1208ec181d08fa4.jpg)  
Fig. 2. The process of calculating attribute values.

## 2. Hesitant judgments of consumers

In this section, we introduce how to construct hesitant judgments based on consumer reviews. Given a set of alternatives $\mathbf { A } = \{ a _ { 1 } , a _ { 2 } , . . . ,$ $\textstyle { a _ { n } } \}$ for consumers to choose, Definition 1 introduces a pairwise comparison.

Definition 1. [18] When a pairwise relation p is applied on a set of objects, $\mathbf { e . g . , } p _ { i j } ,$ it is referred to as a pairwise comparison in which the dominance of object i over object j is expressed numerically on an ab solute scale.

Saaty [17] provides a scale from 1–9 as a benchmark for a decision maker to illustrate judgments over pairwise comparisons of objects, such as attributes. For example, $p _ { 1 2 } = 2$ indicates that attribute i is twice as good as attribute j. We follow this scale in this paper.

When there are several possible values for $p _ { i j } ,$ , it can be referred to as a hesitant judgment. Assume there are n attributes related to an alter native, and $w _ { i } , i = 1 , 2 , . . . , n$ , are the corresponding attribute weights with respect to a consumer. According to Zhu and Xu [25], a consistency property for hesitant judgments is as follows:

$$
\frac {w _ {i}}{w _ {j}} = p _ {i j} ^ {1} \text {   or...or   } p _ {i j} ^ {T}, i, j = 1, 2,..., n,\tag{1}
$$

where $\textstyle \sum _ { i = 1 } ^ { n } w _ { i } = 1 , w _ { i } \geq 0 , i = 1 , 2 , . . . , n _ { \mathrm { ~ } }$ , and T is the Tth possible value of $P _ { i j } .$

Based on each review that includes a text comment and a corre sponding rating, we establish an optimization model to solve for the weights w , $i = 1 , 2 , . . . , n .$ These weights can be used to obtain a set of pairwise comparisons $p _ { i j } , i , j = 1 , 2 , . . . , n$ . Furthermore, all possible weights derived from all reviews of a consumer can be used to obtain a set of possible values for each $p _ { i j } , i , j = 1 , 2 , . . . , n .$ . Assume there are T reviews for a consumer. Denote the weights derived from the tth review by $w _ { i } ^ { t } , t = 1 , 2 , . . . , T .$ We can get a hesitant judgment related to attributes i and $j ,$ denoted by

$$
P _ {i j} = \frac {w _ {i} ^ {1}}{w _ {j} ^ {1}} \text { or...or } \frac {w _ {i} ^ {T}}{w _ {j} ^ {T}}.
$$

## 3. Consumer preference analysis procedure with text comments and ratings

We first introduce a consumer preference analysis procedure, and then introduce how to calculate attribute values from text comments via sentiment analysis.

We assume that a consumer rates an alternative based on its per formance of attributes and her preferences over the attributes. The al ternatives should be of the same category, such that they are characterized by the same limited attributes, where the alternatives can be hotels, restaurants, digital products, etc. We assume that the rating values of alternatives are represented by an additive utility function. Thus, we aggregate the attribute values and weights to obtain the rating values, where the weights are referred to as the consumer preferences over attributes of alternatives. Based on historical reviews generated over time by a consumer, we can analyze the attribute preferences from each review. From the perspective of MADM, although the intrinsic attribute preferences of the consumer are constant, the preferences derived from each review can be inconsistent, due to consumer errors (for example, a low overall rating from a clicking error) or biases (for example, a consumer dated different friends when evaluating different restaurants) when generating reviews. We model the stream of obtained attribute preferences, i.e., the stream of weights, as hesitant judgments (please refer to the next section for details).

The procedure of preference analysis for a consumer is as follows:

Step 1: Collect the reviews, including text comments and ratings of alternatives generated from a consumer from webs.

Step 2: Based on each text comment, use sentiment analysis to calculate the attribute values embedded in the comment.

Step 3: Based on the values derived from a text comment and the rating corresponding to it, solve for the attribute weights by an opti mization model, and then solve for a stream of weights based on all the text comments and corresponding ratings indexed by time.

Step 4: Establish hesitant judgments based on the stream of weights indexed by time.

Step 5: Based on the hesitant judgments, use the HMPM to solve for the satisficing weights that fit the consumer’s preferences over attributes at the highest satisficing level.

Next, we introduce Steps 1 and 2 in detail. Steps 3–5 are shown in Section 4. We illustrate the process of calculating attribute values in Fig. 2. There are three phases as follows:

In Phase 1, we crawl data from webs, including ratings and crawled text comments (CTC), which are the input of Phase 2. For illustration, we choose restaurants as alternatives to analyze consumer preferences. For the selection of the attributes of restaurants, we follow the released training set<sup>3</sup> provided by AI CHALLENGE 2018, launched by Meituan. Each attribute consists of several sub-attributes, as shown in Table 1. Moreover, this set contains rich text comments, each of which is labeled with sentiment polarities for the restaurant’s sub-attributes. We refer to the text comments in this set as training text comments (TTC).

In Phase 2, we start with data cleaning to clean the CTC. With respect to the TTC and cleaned CTC, we then choose Jieba<sup>5</sup> for word segmen tation and choose a stop-words $\mathrm { l i s t } ^ { 6 }$ to remove stop words, which out puts processed CTC and TTC. We use the well-known CBOW model [12] as a word embedding technique, to vectorize the processed TTC and CTC, which outputs the word embedding of TTC and word embedding of CTC, respectively.

In Phase 3, we use an aspect-based sentiment analysis [22] to calculate the attribute values. This model can output the sentiment polarities of given sub-attributes from text comments. We train this model with the word embedding of TTC and the sub-attribute labels in the training set. We set the word embedding of CTC as the input of this trained model and then output the sentiment polarities of sub-attributes. We assign values of 1, 2, and 3 to the sentiment polarities as negative, neutral, and positive, respectively. The values of sub-attributes under each attribute are averaged to obtain each attribute value.

![](/api/attachments/GEN4P2JZ/fulltext/images/69448833d26db4250022539a0478fe28eb035987e16994e24c27e7b41b9af446.jpg)  
(a) Distribution of location values

![](/api/attachments/GEN4P2JZ/fulltext/images/8d1b9822416a5f102fd20c155cd43a2f9bdb80bddfa097bcb1c3338a40ec7e91.jpg)  
(b) Distribution of service values

![](/api/attachments/GEN4P2JZ/fulltext/images/b6c15efd3c793db5f1c34213ae2942850038428ea832105b93a2260e1cadfcdc.jpg)  
(c) Distribution of price values

![](/api/attachments/GEN4P2JZ/fulltext/images/63b7a16dda51bc1285ab6df3c43045eb7652ad07397d36645facc3a2048d6ae9.jpg)  
(d) Distribution of environment values

![](/api/attachments/GEN4P2JZ/fulltext/images/23da51e434adc3badd304b6d5eb8abb0791755816d3a695f93ec0e762d0df363.jpg)  
(e) Distribution of dish values  
Fig. 3. A boxplot of the relative importance of different attributes.

Table 1  
Attributes and sub-attributes of restaurants.

<table><tr><td>Attribute</td><td>Sub-attribute</td></tr><tr><td>Location</td><td>traffic conveniencedistance from business districteasy to find</td></tr><tr><td>Service</td><td>wait timeservers attitudeparking convenienceserving speed</td></tr><tr><td>Price</td><td>price levelprice/performediscount</td></tr><tr><td>Environment</td><td>decorationnoisespacecleanliness</td></tr><tr><td>Dish</td><td>portiontastelookpopularity</td></tr></table>

## 4. Prioritization approach

Based on the obtained attributes and their values, we develop a prioritization approach to solve for the satisficing weights of attributes. Specifically, we first establish an optimization model to produce the weights based on each text comment and its corresponding rating. We then model hesitant judgments by the consistency property, as shown in Definition 1, and utilize the HMPM to obtain the satisficing weights.

## 4.1. An optimization model to obtain attribute weights

Assume that there are T text comments and corresponding ratings.

Table 2  
The impact of κ on attribute weights.

<table><tr><td>κ</td><td> $w_1$ </td><td> $w_2$ </td><td> $w_3$ </td><td> $w_4$ </td><td> $w_5$ </td></tr><tr><td>0.5</td><td>0.036</td><td>0.139</td><td>0.036</td><td>0.343</td><td>0.445</td></tr><tr><td>1</td><td>0.042</td><td>0.141</td><td>0.042</td><td>0.338</td><td>0.437</td></tr><tr><td>1.5</td><td>0.048</td><td>0.143</td><td>0.048</td><td>0.333</td><td>0.429</td></tr><tr><td>2</td><td>0.053</td><td>0.145</td><td>0.053</td><td>0.329</td><td>0.421</td></tr><tr><td>2.5</td><td>0.057</td><td>0.146</td><td>0.057</td><td>0.325</td><td>0.414</td></tr><tr><td>3</td><td>0.062</td><td>0.148</td><td>0.062</td><td>0.321</td><td>0.407</td></tr><tr><td>3.5</td><td>0.066</td><td>0.150</td><td>0.066</td><td>0.317</td><td>0.401</td></tr><tr><td>4</td><td>0.070</td><td>0.151</td><td>0.070</td><td>0.314</td><td>0.395</td></tr><tr><td>4.5</td><td>0.073</td><td>0.153</td><td>0.073</td><td>0.311</td><td>0.390</td></tr><tr><td>5</td><td>0.077</td><td>0.154</td><td>0.077</td><td>0.308</td><td>0.385</td></tr></table>

Table 3  
A sample of a consumer’s hesitant judgments.

<table><tr><td>No.</td><td> $\epsilon_{12}$ </td><td> $\epsilon_{13}$ </td><td> $\epsilon_{14}$ </td><td> $\epsilon_{15}$ </td><td> $\epsilon_{23}$ </td><td> $\epsilon_{24}$ </td><td> $\epsilon_{25}$ </td><td> $\epsilon_{34}$ </td><td> $\epsilon_{35}$ </td><td> $\epsilon_{45}$ </td></tr><tr><td>1</td><td>0.465</td><td>0.230</td><td>0.825</td><td>0.337</td><td>0.719</td><td>0.677</td><td>0.566</td><td>0.669</td><td>0.576</td><td>0.028</td></tr><tr><td>2</td><td>0.567</td><td>0.897</td><td>0.630</td><td>0.988</td><td>0.093</td><td>0.339</td><td>0.822</td><td>0.825</td><td>0.295</td><td>0.505</td></tr><tr><td>3</td><td>0.985</td><td>0.613</td><td>0.358</td><td>0.961</td><td>0.800</td><td>0.224</td><td>0.488</td><td>0.497</td><td>0.722</td><td>0.370</td></tr><tr><td>4</td><td>0.494</td><td>0.029</td><td>0.443</td><td>0.679</td><td>0.504</td><td>0.534</td><td>0.911</td><td>0.383</td><td>0.413</td><td>0.832</td></tr><tr><td>5</td><td>0.707</td><td>0.534</td><td>0.432</td><td>0.439</td><td>0.443</td><td>0.451</td><td>0.312</td><td>0.733</td><td>0.517</td><td>0.971</td></tr></table>

Table 4  
The impact of d on the attribute weights.

<table><tr><td>d</td><td> $w_1$ </td><td> $w_2$ </td><td> $w_3$ </td><td> $w_4$ </td><td> $w_5$ </td></tr><tr><td>0.5</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr><tr><td>1</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr><tr><td>1.5</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr><tr><td>2</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr><tr><td>2.5</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr><tr><td>3</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr><tr><td>3.5</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr><tr><td>4</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr><tr><td>4.5</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr><tr><td>5</td><td>0.106</td><td>0.110</td><td>0.186</td><td>0.292</td><td>0.306</td></tr></table>

## Table 5

A description of crawled data.

<table><tr><td></td><td>Description</td></tr><tr><td>Number of consumers</td><td>459</td></tr><tr><td>Number of text comments</td><td>11518</td></tr><tr><td>Time period</td><td>1/1/2019 - 2/20/2020</td></tr><tr><td>Average rating</td><td>4.058</td></tr></table>

## Table 6

Number of different sentiment polarities derived from text comments.

<table><tr><td></td><td>Positive</td><td>Neutral</td><td>Negative</td><td>Not mentioned</td></tr><tr><td>Location—traffic convenience</td><td>1750</td><td>94</td><td>182</td><td>9492</td></tr><tr><td>Location—distance</td><td>2528</td><td>89</td><td>91</td><td>8810</td></tr><tr><td>Location—easy to find</td><td>1475</td><td>355</td><td>647</td><td>9041</td></tr><tr><td>Service—wait time</td><td>731</td><td>617</td><td>420</td><td>9750</td></tr><tr><td>Service—servers attitude</td><td>2921</td><td>537</td><td>285</td><td>7775</td></tr><tr><td>Service—parking convenience</td><td>436</td><td>92</td><td>128</td><td>10862</td></tr><tr><td>Service—serving speed</td><td>1036</td><td>313</td><td>397</td><td>9772</td></tr><tr><td>Price—price level</td><td>1782</td><td>1583</td><td>1082</td><td>7071</td></tr><tr><td>Price—price/performance</td><td>1778</td><td>273</td><td>241</td><td>9226</td></tr><tr><td>Price—discount</td><td>624</td><td>901</td><td>125</td><td>9868</td></tr><tr><td>Environment—decoration</td><td>3845</td><td>680</td><td>162</td><td>6831</td></tr><tr><td>Environment—noise</td><td>3049</td><td>423</td><td>263</td><td>7783</td></tr><tr><td>Environment—space</td><td>3040</td><td>1035</td><td>710</td><td>6733</td></tr><tr><td>Environment—cleanness</td><td>2961</td><td>402</td><td>248</td><td>7907</td></tr><tr><td>Dish—portion</td><td>2417</td><td>537</td><td>569</td><td>7995</td></tr><tr><td>Dish—taste</td><td>8372</td><td>2197</td><td>194</td><td>755</td></tr><tr><td>Dish—look</td><td>2671</td><td>246</td><td>147</td><td>8454</td></tr><tr><td>Dish—popularity</td><td>1792</td><td>157</td><td>147</td><td>9422</td></tr></table>

Table 7  
Mean and standard deviation of attribute values.

<table><tr><td></td><td>Location</td><td>Service</td><td>Price</td><td>Environment</td><td>Dish</td></tr><tr><td>Mean</td><td>2.632</td><td>2.435</td><td>2.362</td><td>2.680</td><td>2.714</td></tr><tr><td>Standard deviation</td><td>0.327</td><td>0.354</td><td>0.308</td><td>0.246</td><td>0.228</td></tr><tr><td>Number</td><td>453</td><td>455</td><td>453</td><td>456</td><td>459</td></tr></table>

![](/api/attachments/GEN4P2JZ/fulltext/images/8323d953381dfd13016ca166203f7902b7b435498d91a2e53f66b94140c9d526.jpg)

![](/api/attachments/GEN4P2JZ/fulltext/images/0d0c1a600910a787595679db6843cd217362b2d5c17f143e8e0ba08d2af65a2b.jpg)  
(a) Distribution of location values

![](/api/attachments/GEN4P2JZ/fulltext/images/4ed2ff77af8a2542c246c89323037343bbd6b401ee155c77dde6a554135aaa30.jpg)  
(c) Distribution of price values

(b) Distribution of service values  
![](/api/attachments/GEN4P2JZ/fulltext/images/4aaec7ea7bd413360f5578f256be1b141ece60d6b4e4f0ab1f30d129e4ed8170.jpg)  
(d) Distribution of environment values

![](/api/attachments/GEN4P2JZ/fulltext/images/6b05ceec8b56a6c7ebf6ca544c5504dc26fe971e7ad980fe098911118806c9c8.jpg)  
(e) Distribution of dish values  
Fig. 4. Distributions of attribute values.

Table 8  
An illustration of attribute values and ratings of a consumer.

<table><tr><td>No.</td><td>Consumer</td><td>Location</td><td>Service</td><td>Price</td><td>Environment</td><td>Dish</td><td>Rating</td></tr><tr><td>1</td><td>Max</td><td> $s_{1}^{1}$ </td><td> $s_{2}^{1}$ </td><td> $s_{3}^{1}$ </td><td>1</td><td>1</td><td>0.8</td></tr><tr><td>2</td><td>Max</td><td> $s_{1}^{2}$ </td><td> $s_{2}^{2}$ </td><td> $s_{3}^{2}$ </td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>Max</td><td>1</td><td> $s_{2}^{3}$ </td><td> $s_{3}^{3}$ </td><td>1</td><td>1</td><td>1</td></tr><tr><td>4</td><td>Max</td><td> $s_{1}^{4}$ </td><td> $s_{2}^{4}$ </td><td> $s_{3}^{4}$ </td><td>1</td><td> $s_{5}^{4}$ </td><td>1</td></tr><tr><td>5</td><td>Max</td><td>0.667</td><td> $s_{2}^{5}$ </td><td> $s_{3}^{5}$ </td><td>1</td><td>1</td><td>1</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>36</td><td>Max</td><td>0.333</td><td> $s_{2}^{36}$ </td><td> $s_{3}^{36}$ </td><td>0.333</td><td>1</td><td>1</td></tr><tr><td>37</td><td>Max</td><td> $s_{1}^{37}$ </td><td> $s_{2}^{37}$ </td><td> $s_{3}^{37}$ </td><td>1</td><td>1</td><td>1</td></tr><tr><td>38</td><td>Max</td><td> $s_{1}^{38}$ </td><td>0.667</td><td> $s_{3}^{38}$ </td><td>0.889</td><td> $s_{5}^{38}$ </td><td>1</td></tr><tr><td>39</td><td>Max</td><td> $s_{1}^{39}$ </td><td> $s_{2}^{39}$ </td><td> $s_{3}^{39}$ </td><td>0.833</td><td>0.833</td><td>1</td></tr><tr><td>40</td><td>Max</td><td>1</td><td> $s_{2}^{40}$ </td><td> $s_{3}^{40}$ </td><td>1</td><td>1</td><td>1</td></tr></table>

Table 9  
An illustration of a consumer’s attribute preferences.  
Table 10

<table><tr><td>ID</td><td>Location</td><td>Service</td><td>Price</td><td>Environment</td><td>Dish</td></tr><tr><td>Max</td><td>0.1875</td><td>0.1875</td><td>0.1875</td><td>0.2186</td><td>0.2188</td></tr><tr><td>Max</td><td>0.1786</td><td>0.1786</td><td>0.1786</td><td>0.2321</td><td>0.2321</td></tr><tr><td>Max</td><td>0.2143</td><td>0.1786</td><td>0.1786</td><td>0.2143</td><td>0.2143</td></tr><tr><td>Max</td><td>0.1852</td><td>0.1852</td><td>0.1852</td><td>0.2593</td><td>0.1852</td></tr><tr><td>Max</td><td>0.1786</td><td>0.2143</td><td>0.1786</td><td>0.2143</td><td>0.2143</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td>Max</td><td>0.1852</td><td>0.1852</td><td>0.1852</td><td>0.1852</td><td>0.2593</td></tr><tr><td>Max</td><td>0.1786</td><td>0.1786</td><td>0.1786</td><td>0.2321</td><td>0.2321</td></tr><tr><td>Max</td><td>0.1815</td><td>0.2162</td><td>0.1815</td><td>0.2392</td><td>0.1815</td></tr><tr><td>Max</td><td>0.1803</td><td>0.1803</td><td>0.1803</td><td>0.2295</td><td>0.2295</td></tr><tr><td>Max</td><td>0.2143</td><td>0.1786</td><td>0.1786</td><td>0.2143</td><td>0.2143</td></tr></table>

MSE, MAE, and RMSE of solutions derived from different methods.

Denote the tth $( t \in \{ 1 , 2 , . . . , T \} )$ calculated attribute values and their corresponding rating by $Q ^ { t } = \{ s _ { 1 } ^ { t } , s _ { 2 } ^ { t } , . . . , s _ { n } ^ { t } , r ^ { t } \}$ , where $s _ { 1 } ^ { t } , s _ { 2 } ^ { t } , . . . , s _ { n } ^ { t }$ are the values of attributes, and $r ^ { t }$ is the corresponding rating. Denote the tth vector of weights by $\mathbf { w } ^ { t } = \{ w _ { 1 } ^ { t } , w _ { 2 } ^ { t } , . . . , w _ { n } ^ { t } \}$ . Since we assume consumers have an additive utility function and the rating is the utility value, we have

<table><tr><td>Methods</td><td>MSE</td><td>MAE</td><td>RMSE</td></tr><tr><td>Our approach</td><td>4.8145</td><td>1.4178</td><td>2.2182</td></tr><tr><td>Matrix factorization</td><td>15.9350</td><td>3.5868</td><td>3.8970</td></tr><tr><td>User-based recommendation</td><td>18.8386</td><td>4.0495</td><td>4.2849</td></tr><tr><td>Item-based recommendation</td><td>15.9202</td><td>3.4079</td><td>3.9032</td></tr></table>

$$
w _ {1} ^ {t} s _ {1} ^ {t} + w _ {2} ^ {t} s _ {2} ^ {t} +, \dots , + w _ {n} ^ {t} s _ {n} ^ {t} = r ^ {t}, t = 1, 2, \dots , T.\tag{2}
$$

Note that a text comment usually only mentions some of the attributes as shown in Table 1. For instance, in the first text comment in Fig. 1, the consumer does not mention the price attribute. If an attribute value is missing, we set it as a decision variable. Denote the set of missing attribute values in vector $Q ^ { t }$ as S.

We set attribute weights as decision variables and take the con straints of the weights into account. Accordingly, we develop the following optimization model to solve for $\mathbf { w } ^ { t } \mathbf { \cdot }$ :

$$
\begin{array}{l l} P 1: & \min _ {w _ {1} ^ {t}, w _ {2} ^ {t}, \dots , w _ {n} ^ {t}, S} \quad \frac {1}{2} \left(r ^ {t} - w _ {1} ^ {t} s _ {1} ^ {t} - w _ {2} ^ {t} s _ {2} ^ {t} -, \dots , - w _ {n} ^ {t} s _ {n} ^ {t}\right) ^ {2} + \frac {\kappa}{2} \sum_ {i = 1} ^ {n} \left(w _ {i} ^ {t}\right) ^ {2} \\ & \text {   s.t.   } \quad \sum_ {i = 1} ^ {n} w _ {i} ^ {t} = 1, w _ {i} ^ {t} \geq 0, i = 1, 2, \dots , n. \end{array}
$$

The first term in the objective function follows the additive utility, and the second term is a regularization term with a parameter κ. The exis tence of the regularization term avoids the issue of over-fitting. In addition, the weights are non-negative and sum up to 1.

Based on a consumer’s historical reviews, we can obtain a stream of weights by solving P1, that is, $\mathbf { w } ^ { t } = \{ w _ { 1 } ^ { t } , w _ { 2 } ^ { t } , . . . , w _ { n } ^ { t } \} , t = 1 , 2 , . . . , T .$ For any two attributes, i and $^ { 1 , }$ the pairwise comparison of these two attributes is equal to a hesitant judgment denoted by

$$
P _ {i j} = \frac {w _ {i} ^ {1}}{w _ {j} ^ {1}} o r \dots o r \frac {w _ {i} ^ {T}}{w _ {j} ^ {T}}.\tag{3}
$$

Denote a vector of weights by $\mathbf { w } = \{ w _ { 1 } , w _ { 2 } , . . . , w _ { n } \}$ and let $K _ { i j } ( \mathbf { w } ) = w _ { i }$ $- \mathbf { \nabla } w _ { j } ( w _ { i } ^ { 1 } / w _ { j } ^ { 1 } \mathbf { \nabla } o r . . . o r \mathbf { \nabla } w _ { i } ^ { T } / w _ { j } ^ { T } )$ . According to the consistency property (Eq. (1)), if $K _ { i j } ( \mathbf w ) = 0 , i , j = 1 , 2 , . . . . , n ,$ the hesitant judgments satisfy the consistency property. Since this consistency property is often not met in practice, a fuzzy equality is defined as follows:

$$
K _ {i j} (\mathbf {w}) \simeq 0 \Longleftrightarrow w _ {i} - w _ {j} \left(w _ {i} ^ {1} \Big / w _ {j} ^ {1} o r \dots o r w _ {i} ^ {T} \Big / w _ {j} ^ {T}\right) \simeq 0,\tag{4}
$$

where ≃ indicates “approximately equal $\mathrm { { t o } } ^ { \mathfrak { n } } .$ . According to Zhu and Xu [25], the HMPM is to solve the following optimization problem:

$$
\begin{array}{l l} P 2: & \max _ {\lambda} \quad \lambda \\ & \text { s.t. } \quad d \lambda + K _ {i j} (\mathbf {w}) \leq d, \\ & \quad d \lambda - K _ {i j} (\mathbf {w}) \leq d, \\ & \quad i, j = 1, 2,..., n, i <   j, \\ & \sum_ {i = 1} ^ {n} w _ {i} = 1, w _ {i} \geq 0, i = 1, 2,..., n. \end{array}
$$

According to Eq. (4), P2 can be further transformed into the following form:

$$
\begin{array}{l l} P 3: & \max _ {\lambda} \quad \lambda \\ & \text { s.t. } \quad d \lambda + w _ {i} - w _ {j} \left(w _ {i} ^ {1} / w _ {j} ^ {1} \text {   or...or   } w _ {i} ^ {T} / w _ {j} ^ {T}\right) \leq d, \\ & d \lambda - w _ {i} + w _ {j} \left(w _ {i} ^ {1} / w _ {j} ^ {1} \text {   or...or   } w _ {i} ^ {T} / w _ {j} ^ {T}\right) \leq d, \\ & i, j = 1, 2,..., n, i <   j, \\ & \sum_ {i = 1} ^ {n} w _ {i} = 1, w _ {i} \geq 0, i = 1, 2,..., n, \end{array}
$$

where λ is used to measure the satisfaction degree of consumers to the solution. The higher the degree of the hesitant judgment to satisfy the consistency property, the bigger the value of the λ. The parameter d can affect the values of λ because it controls a membership degree that measures the fuzzy equality (Eq. (4)). We refer to the obtained $w _ { i } , i = 1$ $2 . . . , n ,$ as satisficing weights. Thus, the HMPM can produce the weights that fit consumer preferences at the highest satisficing level.

## 5. Discussion

In this section, we investigate the impact of two parameters of our approach: the parameter κ in the quadratic programming model P1, and the parameter d in the HMPM. We assume that there are five attributes for an alternative.

## 5.1. Impact of parameter κ

The κ is a parameter to avoid over-fitting in P1. To investigate the impact of κ, we randomly generate the ratings with two random number generators. The first generator determines whether some attribute rating is missing or not. The second generator determines the rating values for each attribute as well as the overall rating. For example, the rating vector $R = \{ 1 , 2 , 1 , 4 , s _ { 5 } , 4 \}$ } includes the rating values of four attributes and the overall rating, where $\scriptstyle { s _ { 5 } }$ indicates that the value of the fifth attribute is missing. Then we plug the generated rating vector into $P 1 ^ { \prime }$ as follows:

$$
\begin{array}{l l} P 1 ^ {\prime}: & \min _ {w _ {1}, w _ {2}, \dots , w _ {5}, S} \quad \frac {1}{2} (4 - w _ {1} \cdot 1 - w _ {2} \cdot 2 -, \dots , - w _ {5} s _ {5}) ^ {2} + \frac {\kappa}{2} \sum_ {i = 1} ^ {5} (w _ {i}) ^ {2} \\ & \text {   s.t.   } \quad \sum_ {i = 1} ^ {5} w _ {i} = 1, w _ {i} \geq 0, i = 1, 2, \dots , 5. \end{array}
$$

With the variations of $\kappa ,$ Table 2 summarizes the obtained attribute weights. In addition, Fig. 3 illustrates the obtained attribute weights.

From Table 2 and Fig. 3 above, we can find that although the changes in κ (κ ∈ [0.5, 5]) can change the values of attribute weights, it will not change the ranking results of attributes, that is, $a _ { 5 } \succ a _ { 4 } \succ a _ { 2 } \succ a _ { 1 } \sim a _ { 3 }$ However, when κ increases, the importance of the regularization term (last term in the objective function in P1<sup>′</sup> ) increases accordingly, reducing the differences among the obtained weights. Specifically, as κ increases from 0.5 to $^ { 5 , }$ the weight of $w _ { 5 }$ decreases from 0.445 to 0.385. On the other side, the importance of $w _ { 2 }$ increases from 0.139 to 0.154. We select κ = 1 in our numerical studies.

## 5.2. Impact of parameter d

The d is a parameter that can influence the satisfaction degree of consumers to the attribute weights derived from the HMPM. We employ some random number generators to produce preference information. For example, Table 3 shows randomly generated hesitant judgments of a consumer, where each column indicates five possible values for pairwise comparison of two attributes.

We then plug the data in Table 3 into P3 with $d \in [ 0 . 5 , 5 ]$ ]. The results are shown in Table 4.

Clearly, the values of attribute weights are independent of the value of d. Thus, we select $d = 1$ in our numerical studies for convenience.

## 6. Numerical studies

In this section, we analyze consumer preferences over attributes of alternatives for restaurants and apply this approach to the recommendation. We then compare it with some state-of-the-art approaches. To analyze consumer preferences over restaurant attributes, we crawl data from Ctrip.com. We crawl text comments and ratings from 459 con sumers from January 1, 2019, to February 20, 2020. The details are shown in Table 5

Based on sentiment analysis, we summarize the results, as shown in

Table $6 .$ The table shows the statistical results of different sentiment polarities of sub-attributes. For example, the number of positive emo tions of traffic convenience, which is a sub-attribute of the attribute location, is 1751. Note that the sub-attribute taste is the most mentioned attribute; discount is the least mentioned one. In addition, consumers usually mention only some of these sub-attributes. In other words, there are usually missing attributes in each comment.

The average attribute values calculated based on the values of subattributes for each attribute are shown in Table 7. The values of these five attributes all approximately follow normal distributions, as shown in Fig. 4.

For the convenience of calculation, we normalize both the attribute values and corresponding ratings into the interval [0,1]. For illustration, we give an example in Table 8. In detail, each row of the table shows the attribute values and a corresponding rating derived from a review by a consumer named Max (Id. 168 in the dataset). s<sup>t</sup> is the missing value of attribute i derived from the tth review.

We plug the information in each row of Table 8 into the optimization problem P1 introduced in Section 5. For example, the optimization problem related to the first row is as follows:

$$
\begin{array}{l l} \min _ {w _ {1} ^ {1}, w _ {2} ^ {1}, \ldots , w _ {n} ^ {1} s _ {1} ^ {1}} & \frac {1}{2} \big (0. 8 - w _ {1} ^ {1} s _ {1} ^ {1} - w _ {2} ^ {1} s _ {2} ^ {1} - w _ {3} ^ {1} s _ {3} ^ {1} - w _ {4} ^ {1} \cdot 1 - w _ {5} ^ {1} \cdot 1 \big) ^ {2} + \frac {\kappa}{2} \sum_ {i = 1} ^ {5} \left(w _ {i} ^ {1}\right) ^ {2} \\ \text {   s.t.   } & \sum_ {i = 1} ^ {5} w _ {i} ^ {1} = 1, w _ {i} ^ {1} \geq 0, i = 1, 2,..., n, \end{array}
$$

where $\kappa = 1 .$

Table 9 summarizes the obtained weights for the consumer Max. Based on this table, we can construct hesitant judgments $P _ { i j } , i , j = 1 , 2 ,$ 5. For example, $P _ { 1 2 } = \{ w _ { 1 } ^ { t } / w _ { 2 } ^ { t } \big | t = 1 , 2 , . . . , 4 0 \}$ , where w<sup>1</sup> $/ w _ { 2 } ^ { 1 } = 0 . 1 8 7 5$ $/ 0 . 1 8 7 5 = 1 , . . . , w _ { 1 } ^ { 4 0 } / w _ { 2 } ^ { 4 0 } = 0 . 2 1 4 3 / 0 . 1 7 8 6 = 1 . 1 9 9 9$ . Based on con structed hesitant judgments, we use the HMPM, as shown in P2, to obtain the satisficing weights of Max as $\mathbf { w } = \{ 0 . 1 9 8 5 , 0 . 1 9 6 5 , 0 . 1 9 7 4 ,$ 0.2025.0.2051} Clearly, Max mainly focuses on the attributes of “Environment” and “Dish”, rather than “Service”. In addition, we list a number of solutions of the obtained weights of some consumers in Table A.1 in Appendix A.

Next, we recommend restaurants for the target consumer Max based on the idea of user-based recommendation. Specifically, we search for the top 10 consumers who have similar attribute preferences from all 459 consumers and then average their ratings of restaurants. Finally, we select the top-rated restaurants for recommendation, following the approach in the case study of [14,15]. For more technical details of this case study, please refer to Appendix A.

We compare our approach with matrix factorization, item-based recommendation, and user-based recommendation. The principle of user-based/item-based recommendation is to recommend based on the similarity of ratings among consumers/restaurants. Based on the rating information in our crawled dataset, we randomly divide it into a training set (80%) and a testing set (20%). The comparisons among our approach and these recommendation methods with respect to the mean squared error (MSE), mean absolute error (MAE), and root mean squared error

(RMSE) [7] are shown in Table 10.

Table 10 shows that our approach is superior to these traditional recommendation methods with respect to each measure. More impor tantly, our approach can explain why consumers like one restaurant more than another through their preferences over attributes, which overcomes the shortcomings of these compared recommendation methods.

## 7. Conclusion

Consumer preferences over attributes of alternatives are essential fo product/service providers to comprehensively understand consumers choices and develop marketing strategies. Existing methods face diffi culties analyzing consumer preferences at the attribute level. This study addressed this issue, which contributes an innovative idea for consumer preference analysis from the MADM perspective to extant literature. More specifically, we model a consumer’s choice decision as an MADM problem, where sentiment analysis is used to calculate the attribute values. We then develop a quadratic programming model to obtain the consumer’s attribute weights based on text comments and ratings. With the consumer’s historical ratings and text comments, we can derive a stream of attribute weights indexed by time. In particular, we model these attribute weights as hesitant judgments and use the HMPM to derive the final weights that fit the consumer’s preferences over attri butes at the highest satisficing level. Since this modeling bridges the gap between online consumer preference analysis and decision-making methods based on hesitant preference information, we may open new opportunities for research in this direction. With limited online data represented in both consumer comments and rating scores, our approach could be employed by online platforms or business operators to deter mine why one item is preferred by an individual consumer, what are the favorite products/services among a group of consumers, and which consumers have similar preferences for some specific attributes. These analyses have managerial implications for product improvement, mar ket segmentation, and targeted recommendations.

## CRediT authorship contribution statement

Bin Zhu: Conceptualization, Methodology, Writing – original draft. Dingfei Guo: Visualization, Writing – review & editing. Long Ren: Formal analysis, Writing – original draft, Writing – review & editing.

## Acknowledgments

The authors are grateful to the anonymous reviewers and editors for their constructive and detailed comments on the manuscript. This research is supported by the National Natural Science Foundation of China, China (No. 72002033), National Social Science Foundation of China (No. 21FGLB040), Beijing Municipal Social Science Foundation (No. 20GLC046), Beijing Natural Science Foundation (No. M21025, No. 9222027), and Program for Young Excellent Talents, UIBE (No. 19YQ08). This support is gratefully acknowledged.

## Appendix A

Table A.1 gives the satisficing weights of 20 consumers among the 459 consumers for illustration.

Table A1  
Satisficing weights of consumers.

<table><tr><td>ID</td><td> $w_1$ </td><td> $w_2$ </td><td> $w_3$ </td><td> $w_4$ </td><td> $w_5$ </td></tr><tr><td>1</td><td>0.134</td><td>0.244</td><td>0.207</td><td>0.134</td><td>0.281</td></tr><tr><td>2</td><td>0.179</td><td>0.179</td><td>0.231</td><td>0.231</td><td>0.179</td></tr><tr><td>3</td><td>0.245</td><td>0.111</td><td>0.245</td><td>0.245</td><td>0.155</td></tr><tr><td>4</td><td>0.147</td><td>0.147</td><td>0.147</td><td>0.324</td><td>0.235</td></tr><tr><td>5</td><td>0.224</td><td>0.106</td><td>0.224</td><td>0.224</td><td>0.224</td></tr><tr><td>6</td><td>0.224</td><td>0.224</td><td>0.106</td><td>0.224</td><td>0.224</td></tr><tr><td>7</td><td>0.224</td><td>0.224</td><td>0.224</td><td>0.106</td><td>0.224</td></tr><tr><td>8</td><td>0.224</td><td>0.224</td><td>0.224</td><td>0.106</td><td>0.224</td></tr><tr><td>9</td><td>0.276</td><td>0.086</td><td>0.276</td><td>0.086</td><td>0.276</td></tr><tr><td>10</td><td>0.224</td><td>0.224</td><td>0.224</td><td>0.106</td><td>0.224</td></tr><tr><td>11</td><td>0.194</td><td>0.130</td><td>0.274</td><td>0.226</td><td>0.178</td></tr><tr><td>12</td><td>0.224</td><td>0.224</td><td>0.106</td><td>0.224</td><td>0.224</td></tr><tr><td>14</td><td>0.224</td><td>0.106</td><td>0.224</td><td>0.224</td><td>0.224</td></tr><tr><td>15</td><td>0.342</td><td>0.233</td><td>0.123</td><td>0.123</td><td>0.178</td></tr><tr><td>16</td><td>0.227</td><td>0.227</td><td>0.190</td><td>0.128</td><td>0.227</td></tr><tr><td>17</td><td>0.050</td><td>0.300</td><td>0.175</td><td>0.175</td><td>0.300</td></tr><tr><td>18</td><td>0.276</td><td>0.276</td><td>0.086</td><td>0.086</td><td>0.276</td></tr><tr><td>19</td><td>0.277</td><td>0.058</td><td>0.277</td><td>0.167</td><td>0.222</td></tr><tr><td>20</td><td>0.073</td><td>0.304</td><td>0.073</td><td>0.246</td><td>0.304</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

## Appendix B

Denote a vector of weights of consumer x as $\pmb { \nu } ( \pmb { x } ) = \{ w _ { 1 } ( \pmb { x } ) , w _ { 2 } ( \pmb { x } ) , w _ { 3 } ( \pmb { x } ) , w _ { 4 } ( \pmb { x } ) , w _ { 5 } ( \pmb { x } ) \}$ . The distance between consumer x and consumer y (x ∕= y) is

$$
d (\mathbf {w} (x), \mathbf {w} (y)) = \sqrt {\sum_ {i = 1} ^ {5} \left(w _ {i} (x) - w _ {i} (y)\right) ^ {2}},\tag{B.1}
$$

which is defined as the Euclidean distance. The similarity between two consumers is defined as follows:

$$
s (\mathbf {w} (x), \mathbf {w} (y)) = 1 - d (\mathbf {w} (x), \mathbf {w} (y))\tag{B.2}
$$

When two consumers have the same weights on these five attributes, the distance between them is $^ { 0 , }$ while the similarity between them is 1. Based on our approach, Table B.1 shows an example of a similarity matrix, where a number of consumers are randomly selected.

We calculate the attribute preferences of all 459 consumers and select the top 10 consumers who are closest to Max: Id. 337, Id. 176, Id. 170, Id. 169, Id. 336, Id. 333, Id. 174, Id. 2, Id. 334, and Id. 173. Following [14,15], we compute the relative weights of consumer j on Max as $\frac { s ( \mathbf { w } ( x ) , \mathbf { w } ( j ) ) } { \sum _ { i \neq x } s ( \mathbf { w } ( x ) , \mathbf { w } ( i ) ) } ,$ where x denotes the consumer with Id. Max. For instance, the relative weight of the consumer with Id. 169 on Max is computed as

$$
\frac {1}{1 + 1 + 1 + 1 + 0 . 9 7 9 + 0 . 9 7 5 + 0 . 9 6 8 + 0 . 9 4 5 + 0 . 9 4 5 + 0 . 9 4 5} = 0. 1 0 2.
$$

An efficient recommender system recommends films that are more likely to be watched by the target consumer. Therefore, we select the films that have never been rated (watched) by consumer Max but that have been watched by the nearest 10 consumers. By aggregating the ratings of the top 10 consumers with respect to their weights on consumer Max mentioned above, we provide a recommendation list based on aggregation results. The list i as follows: Bayanleba: Haiwei Seafood, Osaka: Wutian Sushi, Hangzhou: Angelo’s Italian Caffe, Hangzhou: Ouba Cake, Hangzhou: Yong Sushui Jiangmen: Xiaolufu Sugar. Kvoto: Arabica Coffee.

We use the mean squared error (MSE), mean absolute error (MAE), and root mean squared error (RMSE) as measures to compare our approach with matrix factorization, item-based recommendation, and user-based recommendation. The comparison results are shown in Table 10. In addition, the

Table B.1  
An illustration of a similarity matrix of consumers.

<table><tr><td>Id.</td><td>Max</td><td>169</td><td>333</td><td>170</td><td>334</td><td>2</td><td>172</td><td>173</td><td>174</td><td>175</td><td>335</td><td>336</td><td>176</td><td>337</td></tr><tr><td>Max</td><td>1.000</td><td>1.000</td><td>0.975</td><td>1.000</td><td>0.945</td><td>0.945</td><td>0.934</td><td>0.945</td><td>0.968</td><td>0.938</td><td>0.944</td><td>0.979</td><td>1.000</td><td>1.000</td></tr><tr><td>169</td><td>1.000</td><td>1.000</td><td>0.975</td><td>1.000</td><td>0.945</td><td>0.945</td><td>0.934</td><td>0.945</td><td>0.968</td><td>0.938</td><td>0.944</td><td>0.979</td><td>1.000</td><td>1.000</td></tr><tr><td>333</td><td>0.975</td><td>0.975</td><td>1.000</td><td>0.975</td><td>0.953</td><td>0.953</td><td>0.959</td><td>0.953</td><td>0.970</td><td>0.949</td><td>0.959</td><td>0.996</td><td>0.975</td><td>0.975</td></tr><tr><td>170</td><td>1.000</td><td>1.000</td><td>0.975</td><td>1.000</td><td>0.945</td><td>0.945</td><td>0.934</td><td>0.945</td><td>0.968</td><td>0.938</td><td>0.944</td><td>0.979</td><td>1.000</td><td>1.000</td></tr><tr><td>334</td><td>0.945</td><td>0.945</td><td>0.953</td><td>0.945</td><td>1.000</td><td>1.000</td><td>0.941</td><td>1.000</td><td>0.976</td><td>0.993</td><td>0.926</td><td>0.953</td><td>0.945</td><td>0.945</td></tr><tr><td>2</td><td>0.945</td><td>0.945</td><td>0.953</td><td>0.945</td><td>1.000</td><td>1.000</td><td>0.941</td><td>1.000</td><td>0.976</td><td>0.993</td><td>0.926</td><td>0.953</td><td>0.945</td><td>0.945</td></tr><tr><td>172</td><td>0.934</td><td>0.934</td><td>0.959</td><td>0.934</td><td>0.941</td><td>0.941</td><td>1.000</td><td>0.941</td><td>0.942</td><td>0.942</td><td>0.955</td><td>0.954</td><td>0.934</td><td>0.934</td></tr><tr><td>173</td><td>0.945</td><td>0.945</td><td>0.953</td><td>0.945</td><td>1.000</td><td>1.000</td><td>0.941</td><td>1.000</td><td>0.976</td><td>0.993</td><td>0.926</td><td>0.953</td><td>0.945</td><td>0.945</td></tr><tr><td>174</td><td>0.968</td><td>0.968</td><td>0.970</td><td>0.968</td><td>0.976</td><td>0.976</td><td>0.942</td><td>0.976</td><td>1.000</td><td>0.970</td><td>0.937</td><td>0.971</td><td>0.968</td><td>0.968</td></tr><tr><td>175</td><td>0.938</td><td>0.938</td><td>0.949</td><td>0.938</td><td>0.993</td><td>0.993</td><td>0.942</td><td>0.993</td><td>0.970</td><td>1.000</td><td>0.923</td><td>0.948</td><td>0.938</td><td>0.938</td></tr><tr><td>335</td><td>0.944</td><td>0.944</td><td>0.959</td><td>0.944</td><td>0.926</td><td>0.926</td><td>0.955</td><td>0.926</td><td>0.937</td><td>0.923</td><td>1.000</td><td>0.957</td><td>0.944</td><td>0.944</td></tr><tr><td>336</td><td>0.979</td><td>0.979</td><td>0.996</td><td>0.979</td><td>0.953</td><td>0.953</td><td>0.954</td><td>0.953</td><td>0.971</td><td>0.948</td><td>0.957</td><td>1.000</td><td>0.979</td><td>0.979</td></tr><tr><td>176</td><td>1.000</td><td>1.000</td><td>0.975</td><td>1.000</td><td>0.945</td><td>0.945</td><td>0.934</td><td>0.945</td><td>0.968</td><td>0.938</td><td>0.944</td><td>0.979</td><td>1.000</td><td>1.000</td></tr><tr><td>337</td><td>1.000</td><td>1.000</td><td>0.975</td><td>1.000</td><td>0.945</td><td>0.945</td><td>0.934</td><td>0.945</td><td>0.968</td><td>0.938</td><td>0.944</td><td>0.979</td><td>1.000</td><td>1.000</td></tr></table>

definitions of these measures are as follows:

$$
\mathrm{MSE} = \frac {\sum_ {u , i \in T} \left(r _ {u , i} - \widehat {r} _ {u , i}\right) ^ {2}}{| T |}, \quad \mathrm{MAE} = \frac {\sum_ {u , i \in T} \left| r _ {u , i} - \widehat {r} _ {u , i} \right|}{| T |}, \quad \mathrm{RMSE} = \sqrt {\frac {\sum_ {u , i \in T} \left(r _ {u , i} - \widehat {r} _ {u , i}\right) ^ {2}}{| T |}}\tag{B.3}
$$

where $r _ { i } ( u )$ is the actual rating of the uth consumer on the ith alternative, $\widehat { r } _ { u , i }$ is the predicted rating, and T is number of ratings.

## References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Trans. Knowl. Data Eng, 17 (2005) 734–749

[2] A. Ghose, P.G. Ipeirotis, B. Li, Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content, Mark. Sci. 31 (2012) 493–520.

[3] S. Ghose, O. Lowengart, Consumer choice and preference for brand categories, J. Mark, Anal. 1 (2013) 3–17.

[4] P.E. Green, A.M. Krieger, Segmenting markets with conjoint analysis, J. Mark. 55 (1991) 20–31.

[5] P.E. Green, V. Srinivasan, Conjoint analysis in consumer research: issues and

[6] P.E. Green, V. Srinivasan, Conjoint analysis in marketing: new developments with implications for research and practice, J. Mark. 54 (1990) 3–19.

[7] G. James, D. Witten, T. Hastie, R. Tibshirani, An Introduction to Statistical Learning vol. 112, Springer, 2013.

[8] K. Jedidi, Z.J. Zhang, Augmenting conjoint analysis to estimate consumer reservation price, Manage. Sci. 48 (2002) 1350–1368.

[9] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommender systems, Computer 42 (2009) 30–37

[10] S.K. Lee, Y.H. Cho, S.H. Kim, Collaborative filtering with ordinal scale-based implicit ratings for mobile music recommendations, Inf. Sci. 180 (2010) 2142–2155.

[11] J. Liu, X. Liao, W. Huang, X. Liao, Market segmentation: a multiple criteria approach combining preference analysis and segmentation decision, Omega 83 (2019) 1–13.

[12] T. Mikolov, G. Corrado, C. Kai, J. Dean, Efficient estimation of word representations in vector space. Proceedings of the International Conference on Learning Representations (ICLR 2013). 2013.

[13] M.J. Pazzani, D. Billsus, Content-based recommendation systems. The Adaptive Web, Springer, 2007, pp. 325–341.

[14] L. Ren, B. Zhu, Z. Xu, Data-driven fuzzy preferences analysis from an optimization perspective, Fuzzy Sets Syst. 377 (2019) 85–101.

[15] L. Ren, B. Zhu, Z. Xu, Robust consumer preference analysis with a social network

[16] P. Resnick, H.R. Varian, Recommender systems, Commun. ACM 40 (1997) 56–58

[17] T.L. Saaty, The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation, McGraw-Hill, NY, USA, 1980.

[18] T.L. Saaty, The possibility of group choice: pairwise comparisons and merging functions. Social Choice Welfare 38 (2012) 481–496.

[19] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative filtering recommendation algorithms. Proceedings of the 10th International Conference on World Wide Web, 2001, p. 285295.

[20] P.M. West, P.L. Brockett, L.L. Golden, A comparative analysis of neural network and statistical methods for predicting consumer choice, Mark, Sci. 16 (1997) 370-391.

[21] Z. Xu. Uncertain Multi-Attribute Decision Making: Methods and Applications Springer, 2015.

[22] W. Xue, T. Li, Aspect based sentiment analysis with gated convolutional networks. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, 2018, pp. 2514–2523.

[23] S.H. Zanakis, A. Solomon, N. Wishart, S. Dublish, Multi-attribute decision making: a simulation comparison of select methods, Eur. J. Oper. Res. 107 (1998) 507–529

[24] Z.D. Zhao, M.S. Shang, User-based collaborative-filtering recommendation algorithms on Hadoop. Third International Conference on Knowledge Discovery and Data Mining, 2010, pp. 478–481.

[25] B. Zhu, Z. Xu, Analytic hierarchy process-hesitant group decision making, Eur. J. Oper. Res. 239 (2014) 794–801.

Bin Zhu received the PhD degree in Management Science and Engineering from Southeast University, Nanjing, China, in 2014. From December 2014 to December 2016, he was a Postdoctoral Researcher at School of Economics and Management, Tsinghua University, Beijing, China. He is currently an associate professor at School of Management and Eco nomics, Beijing Institute of Technology. His research interests focus on decision analysis, optimization, and consumer preference analysis. He has published numerous articles in European Journal of Operational Research, IEEE Transactions on Cybernetics, IEEE Transactions on Fuzzy Systems, Information Sciences, Fuzzy Sets and Systems, etc.

Dingfei Guo, Master of Science in Management, School of Management and Economics, Beijing Institute of Technology, haidian district, Beijing. Her research interests include consumer preference analysis, decision analysis

Long Ren receives the PhD degree in Management Science from Tsinghua University in 2018. He is now an associate professor in School of Information Technology and Man agement, University of International Business and Economics. He has published several articles in journals of Information Sciences, Expert Systems with Applications, IEEE Transactions, International Journal of Production Economics, Transportation Research Part E, and Transport Policy. His research interest lies in consumer preference analysis, operations management, and optimization. He is also a member of INFORMS, SIAM, and POMS.
