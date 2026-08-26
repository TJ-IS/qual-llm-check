---
otero_id: 19684
otero_key: "NGHX74AC"
title: "Mining product competitiveness by fusing multisource online information"
authors: "Zhao Liu; Chang-Xiong Qin; Yue-Jun Zhang"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113477"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mining product competitiveness by fusing multisource online information

![](/api/attachments/NGHX74AC/fulltext/images/a2f4a93f98104940ab529c9ea3e0259f2596fb8d105bbed3ed464a308a532657.jpg)

Zhao Liu <sup>a,b</sup>, Chang-Xiong Qin <sup>a,b</sup>, Yue-Jun Zhang <sup>a,b,\*</sup>

<sup>a</sup> Business School, Hunan University, Changsha 410082, PR China

<sup>b</sup> Center for Resource and Environmental Management, Hunan University, Changsha 410082, PR China

## A R T I C L E I N F O

Keywords: Multisource online information Product competitiveness Information fusion Comparative opinion mining Ouantile regression model

## A B S T R A C T

In sharp market competition, it is very important for enterprises to maintain high product competitiveness. The rich data on social network sites and e-commerce platforms provide a novel way to research product competi tiveness. Some studies have mined product competitiveness from online reviews. which may be biased. since some fake information may be contained in online reviews, and the information of product competitiveness from the online reviews is limited as well. This paper, thus, proposes a method that integrates multisource online information to analyze product competitiveness, which can correct the deviation of product competitiveness from a single source of online reviews. In addition, this method is based on mutual information and quantile regression models and further explores what the key competitiveness is and how the factors affect product competitiveness at different competitiveness levels. This paper provides a novel decision-making tool to analyze the competitiveness of products such as mobile phones

## 1. Introduction

Product competitiveness is important information for enterprises, as it helps them understand the position of their products in the market [1,2]. Based on the competitiveness information, enterprises could also analyze the deficiencies of their products in some key areas, and improve product competitiveness by formulating corresponding competitive strategies, so as to expand the market share of products and increase corporate profits [3]. Therefore, how to obtain product competitiveness information, which aspects of competitiveness are the most important, and how enterprises should improve their competi tiveness in these areas? Solving these problems is of great significance to the enterprises.

Previous research on product competitiveness usually adopts ques tionnaires or interviews [4,5]. With the development of information technology, an increasing number of people can publicly share their opinions on products to social network sites or e-commerce platforms, and such data stored on the Internet contain a lot of product competi tiveness information. Therefore, in recent years, some scholars have tried to mine product competitiveness from massive online reviews on social network sites or e-commerce platforms [6]. However, most studies are based on a single source of online reviews to analyze product competitiveness [7,8]. On the one hand, due to the possibility of some fake information in online reviews, the product competitiveness ob tained from a single source of online reviews may be biased, which needs to be corrected by integrating other information [9]. On the other hand, the product competitiveness information from a single source of online reviews is limited, so it cannot provide companies with more suggestions for improving product competitiveness. In fact, the interface informa tion provided by most e-commerce platforms is very rich, including not only online reviews but also questions and answers (Q&A) and product attributes. The product competitiveness information extracted from Q&A is usually more credible, because the text structure of Q&A de termines that it is more difficult to fake than online reviews [10]. Moreover, product attributes are the basic elements that affect consumer satisfaction, and which attributes can most affect their satisfaction (i.e., the key competitiveness concerned by consumers) is an important basis for enterprises to improve their product competitiveness, while many studies neglect the information of product attributes. Therefore, based on data from an e-commerce platform,<sup>1</sup> this paper fuses three data sources of online reviews, O&A and product attributes to construct a framework for product competitiveness analysis, which includes extracting product competitiveness information, identifying key competitiveness and analyzing the influence mechanism of key

competitiveness.

This paper mainly makes the following contributions: first of all, to obtain more accurate product competitiveness information, this paper designs an algorithm to correct the deviation of product competitiveness information from a single source of online reviews by extracting product competitiveness information from Q&A, which extends the research on information mined from Q&A. Second, the framework constructed in this paper provides an opportunity for enterprises to identify the key competitiveness of products from the consumer perspective, so that enterprises can improve the key competitiveness of their products based on the consumer perspective. Third, the framework constructed in this paper contributes to understanding the impact pattern of key competi tiveness of products at a micro level, since the influence mechanism of key competitiveness of products at different competitiveness levels is usually different.

The remainder of this paper is organized as follows. First, we review the related literature. Then, we construct a framework to analyze product competitiveness. Next, based on the Jingdong platform, we take mobile phones as a case to verify the framework of this study. We then conclude by discussing the theoretical and managerial implications of this work and the study’s limitations and future work.

## 2. Literature review

## 2.1. Product competitiveness analysis

Product competitiveness is the comprehensive abilities of two or more products in a competition. Porter [1] made the pioneering contribution to the study of product competitiveness. Afterwards, Chen and Miller [12], Hunt and Menon [13] and Chen [14] carried out extensive studies on product competitiveness. The objects of these studies mainly focus on offline products, and the research scope mainly includes product ontology competitiveness and competitive environ ment [15].

In recent years, many scholars explored product competitiveness through online information on social network sites or e-commerce platforms [16], and these studies mainly include statistical analysis and content mining of competitiveness information. Regarding the statistical analysis of competitiveness information, some scholars have analyzed the average ratings and number of online reviews and found that the larger of these statistics indicate more competitive products [17]. Eslami et al. [18] studied the length of online reviews and found that medium length online reviews promoted consumers to decide to buy the product, thus enhancing the competitiveness of product. As for the content mining of competitive information, scholars mainly penetrate into the text content of online reviews to mine the detailed product competitive. For example, Liu et al. [6] and Gao et al. [7] mine the product competitive advantages and disadvantages from online reviews. Compared with the statistical analysis of competitiveness information, the content mining can obtain more detailed and accurate results.

## 2.2. The influencing factors of product competitiveness

Product competitiveness is influenced by many factors, and we can roughly divide them into internal factors and external factors [19]. For internal factors, many studies focus on the impact of innovation on competitiveness. Hambrick [20] and Miller [21] first proposed five di mensions of competitive strategy, and innovation differentiation is the most important dimension. In addition to innovation, the price, cost and brand are also important internal factors that influence product competitiveness. In the fierce market competition, price and cost ad vantages are important factors to maintain a leading position in peer competition [22], and brand is a core factor in promoting the compet itiveness of enterprises [23].

In terms of external factors, the competitive environment is an obvious factor. In particular, competitors are the most important component of the competitive environment, and competitors’ aware ness, motivation, and capability (AMC) can reflect some competitive signals, so some scholars used AMC to predict competitors’ behavior [14,24]. In addtion, public opinion is also a part of the competitive environment, and some scholars found that negative online reviews would reduce product competitiveness [25], especially the first online review [26]. Moreover, capital investment and product launch time will directly affect product competitiveness [20]. For example, no matter how innovative the product is at launch, its competitive advantage will decrease over time and be surpassed by later products.

Although scholars have studied the factors in product competitive ness from different aspects, few studies have explored the impact of product attributes on its competitiveness. In fact, product competitive ness essentially stems from the quality or attributes of product itself, rather than external factors [3]. The influence mechanism of product attributes on product competitiveness have more practical value for the improvement of product competitiveness, and the research on this mechanism should be strengthened.

## 2.3. The methodology of product competitiveness

The research methods for product competitiveness can be divided into qualitative analysis and quantitative analysis. In terms of qualita tive analysis, scholars often use SWOT analysis, based on the internal and external competitive environment, to analyze the product internal strengths and weaknesses, as well as the external opportunities and threats, and thus to develop the strategies to improve product compet itiveness [27,28]. In addition, the five-force model proposed by Porter [1] is also a classic product competitiveness analysis model, which an alyzes five forces (i.e., peer competition, the threats of new entrants, the threats of substitutes, and the bargaining power of suppliers and buyers) to explore the laws of product competition [29]. For quantitative anal ysis, the most widely used method is structural equation model. For instance. many scholars have used structural equation model to explore the relationship between enterprise innovation, product pricing and brand and product competitiveness [30,31]. Moreover, demand func tion and system dynamics model are also commonly used to study product competitiveness [31,32]. Furthermore, due to the characteris tics of multiparty competition, game models are often used in the analysis of product competitiveness [33].

In particular, text mining has gradually become an important method to research product competitiveness in recent years, and it is also a qualitative analysis method. There are two main ways to analyze product competitiveness based on text mining, i.e., topic analysis and comparative opinion mining. Topic analysis is to extract the topic of product attributes from text corpus, and the competitiveness of the product in a specific attribute is characterized by the positive or negative emotions in the topic [8]. Comparative opinion mining is carried out by extracting comparative entity pairs from text corpus, because the product competition relation is implied in the comparative entity pairs [34–36]. Compared with topic analysis, comparative opinion mining has a finer granularity for content mining (see Table 1 for detailed literature summary).

## 3. Methodology

To solve the three problems mentioned above faced by enterprises, this paper designs a framework for the product competitiveness analysis by fusing multisource online information from an e-commerce platform (see Fig. 1). First, we use comparative opinion mining to obtain the products competitiveness information from online reviews and Q&A. We then analyze the key competitiveness of products using the competitiveness index and mutual information (MI) method. Finally, we explore the impact of product attributes on product competitiveness in different competitive levels based on the quantile regression model. The corresponding three research methods are described in detail below.

Table 1  
Literature summary on methodology of product competitiveness.

<table><tr><td>Reference</td><td>Methods</td><td>Research</td><td>Results</td></tr><tr><td>Phadermrod et al. [27]</td><td>SWOT analysis</td><td>It proposes a SWOT analysis method based on customer perception.</td><td>A case study shows that this method can clearly identify the SWOT factors that need to be improved.</td></tr><tr><td>Amin et al. [28]</td><td>SWOT analysis</td><td>It integrates fuzzy logic and SWOT analysis to develop a novel decision-making tool to improve product competitiveness.</td><td>A case study of auto parts verified that this tool can effectively provide product competition strategy.</td></tr><tr><td>Lee et al. [29]</td><td>Five-force model</td><td>It explores the product competitiveness by combining the five-force model and AHP.</td><td>This method is effective to strengthen the ability of competitiveness analysis.</td></tr><tr><td>Gupta et al. [30]</td><td>Structural equation model</td><td>It investigates the relationship between brand competition and innovation in manufacturing industry.</td><td>The innovation in marketing practice of a brand is influenced by its own competitiveness.</td></tr><tr><td>Yonezawa, Richards [31]</td><td>Demand function</td><td>It evaluates the degree of price competition caused by the size of product packaging.</td><td>A smaller size of product packaging will intensify price competition.</td></tr><tr><td>Yan, Ma [32]</td><td>System dynamics model</td><td>It analyses the competitive diffusion behavior of repurchased products in the market.</td><td>The market share of products depends on their time to market and competitiveness.</td></tr><tr><td>Hagiu, Wright [33]</td><td>Game model</td><td>It explores the market competition of untested new products and established products in a platform.</td><td>When platforms extract a fixed share of revenues from all of their sellers, platform and sellers both hope the entry of new products.</td></tr><tr><td>Bi et al. [8]</td><td>Text mining</td><td>It proposes a method to analyze the importance-performance of products from online reviews.</td><td>The method can quickly acquire the intelligence of product competitiveness.</td></tr><tr><td>Jin et al. [35]</td><td>Text mining</td><td>It extracts the competitive expressions from online reviews based on comparative opinion mining.</td><td>The competitive expressions extracted from online reviews are helpful to improve product design.</td></tr><tr><td>Xu et al. [36]</td><td>Text mining</td><td>It develops a method to extract competition information based on comparative opinion mining.</td><td>The method could reveal the comparative relation between competing products.</td></tr></table>

## 3.1. Comparative opinion mining model

Comparative opinion mining is a method for in-depth mining of text content, with the advantage of fine mining granularity [36], which obtains comparison opinions between products $( \mathrm { i . e . , }$ product competi tiveness information) by extracting comparative entity pairs. This paper constructs a four-tuple (P1, P2, aspect, result) for each comparative entity pair, and these four elements represent the comparative subject, comparative object, comparative aspect and comparative result, respectively. Both comparative subject and object are product names, and they constitute the comparative entity names. For example, the consumer commented that “The camera of mobile phone A is better than that of mobile phone $B ^ { * * } ,$ , and we can obtain the four-tuple (‘mobile phone A ‘, ‘mobile phone $w ,$ , ‘camera’, ‘better’). To extract the four-tuple from the online reviews and Q&A, we first need to determine which online reviews and Q&A texts are comparative sentences.

Regarding the comparative sentence discrimination of online re views, this paper, which is partly based on Gao et al. [7], combines the class sequence rule (CSR) and a keyword dictionary to build a pattern library of comparative sentences.<sup>2</sup> It further distinguishes comparative sentences by comparative entity name to improve the discriminating accuracy of online reviews comparative sentences. First, we remove the stop words from an online review text to obtain the following sequence:

$$
s = \left<   w _ {1}, w _ {2}, \dots , w _ {m} \right>\tag{1}
$$

where w denotes the ith word in this online review.<sup>3</sup> Then, we combine s with its category label c (c =comparative sentence, c =noncomparative sentence) into one element $e = ( s , c _ { j } )$ . For a CSR:R → c (c is a category label), if the rule R is a subsequence of s, then it is said that e covers the CSR, and if there is still $c = c _ { j } ,$ it is said that e satisfies the CSR [35].

To construct a suitable comparative sentence pattern library for online reviews, we use the support and confidence to filter the rule R, and the qualified R is a comparative sentence pattern [37]. The support of rule R is defined as the proportion of the online reviews that satisfy the CSR:R → c (c =comparative sentence), and the confidence of rule R is the ratio of satisfying the CSR:R → c to covering the CSR:R → c. Then, rule R should satisfy the following formula:

$$
\operatorname{Sup} (R) > \max (\lambda \times \min (F _ {k}), T)\tag{2}
$$

$$
C o n (R) > T h r\tag{3}
$$

where Sup(R) and Con(R) are the support and confidence of rule R, respectively; λ is a parameter between 0 and 1. T and Thr denote the threshold of support and confidence, respectively, and $F _ { k }$ indicates the ratio of the kth item of R in n online reviews.

Finally, according to formula (2) and (3), all qualified rules R are screened out to form the comparative sentence pattern library for online reviews. If a text of online review does not match any pattern in the comparative sentence pattern library of online reviews, it is discrimi nated as a noncomparative sentence. In contrast, it is necessary to further identify whether the text contains the comparative entity name, and if no comparison entity name is contained, it is judged to be a noncomparative sentence; otherwise, it is considered a comparative sentence.

For the comparative sentence discrimination of Q&A, we need to combine the questions and answers of consumer to determine the text type. Because the comparative features of Q&A $( \mathrm { i . e . , }$ the special expression patterns or words in comparative sentences) mainly appear in the consumer’s question and the consumer answers the comparative result, thus forming a complete comparative sentence. For instance, “Question: Which camera is better between mobile phone A and B? Answer 1: B is better; Answer 2: The former; Answer 3: I don’t know”. First, we convert the corpus of question into a word vector set without stop words as given in Eq. (4):

$$
Q V = \left\{q _ {1}, q _ {2}, \dots , q _ {r} \right\}\tag{4}
$$

![](/api/attachments/NGHX74AC/fulltext/images/4012565b9df55c7dc2abf23411f5bfabd1b0c357dcab02ee4115f885fa9851b7.jpg)

Fig. 1. Multisource information fusion theoretical frame work.

, ② and ③ correspond to online reviews comparative sen tences identification, Q&A comparative sentences identifica tion and comparative elements extraction, respectively, and these three parts constitute the comparative opinion mining. Moreover, ④ and ⑤ correspond to the measurement of key competitiveness and the analysis of factors affecting the key competitiveness, respectively.

where $q _ { i }$ denotes the word vector converted by ith question text, which can be written as $q _ { i } = ( t _ { i 1 } , t _ { i 2 } , \cdots , t _ { i l } ) .$ , and $t _ { i j }$ equals 1 if the question text includes the jth feature word in the bag-of-words of QV and otherwise 0 [34]. Similarly, the corpus of answer can be processed in text form as $A = \{ a _ { 1 } , a _ { 2 } , \cdots , a _ { u } \}$ . Then, we combine support vector machine (SVM) and comparative entity name to discriminate comparative sentences of Q&A. See Appendix A for the detailed algorithm process.

Next, we extract the elements of four-tuple from these comparative sentences. Since the comparative subject and object have been identified in the process of discriminating comparative sentences,<sup>5</sup> we only need to extract the comparative aspect and result from the online reviews and Q&A. The comparative aspect is obtained by a dictionary constructed by domain knowledge [7], and the comparative result is calculated by Eq. (5):

$$
\text { Score } = (- 1) ^ {\nu} \times \text { Sen } \times \text { Str }\tag{5}
$$

where v is the number of negative words of a comparative sentence and Sen indicates the consumers’ opinion in this comparative sentence (1: positive; − 1: negative; 0: neutral). Moreover, Str represents the senti ment strength of the comparative sentence.<sup>6</sup>

## 3.2. The method for measuring key competitiveness

The competitiveness in terms of each aspect of a product is related to the consumers’ opinions, and the products that are often compared as objects may be more competitive [34]. Therefore, this paper constructs the following competitiveness index<sup>7</sup>:

$$
C O M _ {i} ^ {\alpha} = \frac {\sum_ {j} N _ {i j} ^ {\alpha +}}{\sum_ {j} \left(N _ {i j} ^ {\alpha +} + N _ {i j} ^ {\alpha -}\right)} \sum_ {j} \left(W _ {i j} ^ {\alpha +} + W _ {i j} ^ {\alpha -}\right)\tag{6}
$$

where COM<sup>α</sup> denotes the competitiveness index of product i in aspect α. In particular, when the aspect is not distinguished, the calculated competitiveness is the overall competitiveness index in terms of all as pects, which can be written as COM . N<sup>α+</sup> indicates the total number that product i is better than product j in terms of aspect α in online reviews and Q&A, and $N _ { i j } ^ { \alpha \cdot }$ is the opposite. $W _ { i j } ^ { \alpha + }$ and W<sup>α−</sup> are the positive and negative weights, respectively, and can be calculated using Eq. (7) and Eq. (8):

$$
W _ {i j} ^ {\alpha +} = \frac {\left| \sum_ {i ^ {\alpha +} = 1} ^ {x (i ^ {\alpha +})} S c o r e _ {i j} ^ {i ^ {\alpha +}} \right|}{x (i ^ {\alpha +})}\tag{7}
$$

$$
W _ {i j} ^ {\alpha -} = \frac {\left| \sum_ {i ^ {\alpha -} = 1} ^ {x (i ^ {\alpha -})} S c o r e _ {i j} ^ {i ^ {\alpha -}} \right|}{x (i ^ {\alpha -})}\tag{8}
$$

where $x ( i ^ { \alpha + } )$ represents the total number of positive comparative opin ions of product i on aspect α in online reviews and Q&A and $S c o r e _ { i j } ^ { i \alpha + }$ is the comparative result that product i is better than product j in terms of aspect α, while $x ( i ^ { \alpha - } )$ and $\bar { s c o r e _ { i j } ^ { i \alpha - } }$ are the opposite of the previous two.

The key competitiveness of products is defined as the competitive ness in aspects that greatly contribute to the overall competitiveness [8]. This paper adopts the MI to measure the contribution of competitiveness in terms of each aspect to overall competitiveness.<sup>8</sup> When the MI be tween the competitiveness in terms of a specific aspect and the overall competitiveness is greater, it shows that the competitiveness in terms of this aspect is more important for overall competitiveness. MI can be calculated by Eq. (9):

$$
I \left(C O M _ {i}; C O M _ {i} ^ {\alpha}\right) = \sum_ {z \in C _ {i}} \sum_ {y \in C O M _ {i} ^ {\alpha}} p (y, z) \log \left(\frac {p (y , z)}{p (y) p (z)}\right)\tag{9}
$$

where ${ \mathfrak { p } } ( y , z )$ indicates the joint probability density function of COM and COM<sub>i</sub><sup>α</sup>. In addition, p(y) and p(z) represent the marginal probability density functions of COM and COM<sup>α</sup>, respectively.

## 3.3. The method for analyzing the influence of key competitiveness

The product competitiveness of a specific aspect is essentially derived from the corresponding product attributes. For example, the size competitiveness of a mobile phone depends on its attributes of the length, width and thickness. Therefore, the product attributes have a direct impact on the corresponding product competitiveness [31], and this influence mechanism can be used as the basis to improve the key competitiveness of products. In addition, the impact patterns of competitiveness of products at different competitiveness levels may be different. For instance, there are different impact degree for products with high competitiveness and low competitiveness effect by the same factor. To develop a reasonable key competitiveness improvement strategy for products with different competitiveness levels, this paper uses the quantile regression model to explore the effect of product at tributes on the corresponding key competitiveness of products. Compared with the traditional regression model, the quantile regression model has the advantage of exploring the affected degree of the dependent variable at different quantile levels (i.e., the high (low) quantile corresponds to the effect of high (low) competitiveness prod ucts), and the regression results are more robust [40].

First, we calculate the competitiveness index of product i in each aspect through the Eq. (6), and its distribution function can be expressed as $F ( y ) = p ( C O M _ { i } ^ { \alpha } \leq y )$ , so the τth quantile of COM<sup>α</sup> can be written as Eq. (10):

$$
F ^ {- 1} (\tau) = \inf \{y: F (y) \geq \tau \}\tag{10}
$$

Then, we extract the number from the texts of product attributes, and these product attributes are the factors that influence the competitive ness in terms of a certain aspect, which can be expressed as $X _ { i } ^ { \alpha } = ( X 1 _ { i } ^ { \alpha }$ , $X 2 _ { i } ^ { \alpha } , \cdots , X d _ { i } ^ { \alpha } )$ . Therefore, the quantile regression model for these factors on competitiveness in terms of aspect α can be formulated as Eq. (11).

$$
F ^ {- 1} \left(\tau | X _ {i} ^ {\alpha}\right) = \beta_ {0} ^ {\alpha} (\tau) + \beta_ {1} ^ {\alpha} (\tau) X 1 _ {i} ^ {\alpha} + \beta_ {2} ^ {\alpha} (\tau) X 2 _ {i} ^ {\alpha} + \dots + \beta_ {d} ^ {\alpha} (\tau) X d _ {i} ^ {\alpha} + \varepsilon_ {i}\tag{11}
$$

where $\beta _ { 0 } ^ { \alpha } ( \tau ) , \beta _ { 1 } ^ { \alpha } ( \tau ) , \beta _ { 2 } ^ { \alpha } ( \tau ) , \cdots , \beta _ { d } ^ { \alpha } ( \tau )$ are the regression coefficients in the τth quantile and ε denotes the error term. Solving these regression co efficients is equivalent to minimize the problem, as given in Eq. (12) [41].

$$
\min _ {\beta^ {\alpha} (\tau)} \sum_ {i} \rho_ {\tau} (\mu) \left(C O M _ {i} ^ {\alpha} - \beta^ {\alpha} (\tau) X _ {i} ^ {\alpha}\right)\tag{12}
$$

where $\beta ^ { \alpha } ( \tau ) X _ { i } ^ { \alpha }$ is the right side of Eq. (11) after removing the error term; μ is equal to COM<sup>α</sup> − β<sup>α</sup>(τ)X<sup>α</sup>, and $\rho _ { \tau } ( \mu )$ indicates the loss function shown in Eq. (13).

$$
\rho_ {\tau} (\mu) = \left\{ \begin{array}{c c} \tau \mu , & \mu \geq 0 \\ (\tau - 1) \mu , & \mu <   0 \end{array} \right.\tag{13}
$$

## 4. Empirical analysis

The mobile phones market is a typical, highly competitive market with a broad market space around the world. In 2015, the global penetration rate of mobile phones was approximately 63%, of which Europe has the highest penetration rate, at approximately 85% [42]. There are thousands of mobile phones, and to occupy this huge market, the product competitiveness information of competitors and firms themselves is crucial for these mobile phone enterprises. This is in line with the subject of this paper. Therefore, to verify the framework of fusing multisource online information in this paper, we choose mobile phones as a case to analyze its product competitiveness.

## 4.1. Data description

We chose Jingdong, one of the largest e-commerce platforms in China, as the data source for empirical analysis. This platform is the most trusted platform for users to purchase electronic products in China, and it presents a wealth of information on product attributes, online reviews and Q&A, etc. (see Fig. 2). We develop a web crawler to collect infor mation about 409 mobile phones from https://www.jd.com/, including 373,890 online reviews, 634,651 Q&A, and the attributes information for each mobile phone. Since each mobile phone has sold more than 10,000, the data are generally credible. Moreover, we integrate these attributes of the mobile phones into 14 aspects in the first column of Table $2 \ ( \mathrm { i . e . }$ , the comparative aspects in four-tuple), and the third col umn is the comparative aspect dictionary corresponding to each aspect.

Note: The Chinese characters in the box of pictures above have been translated into English.

## 4.2. Extracting the competitiveness information of mobile phones

We adopt the comparative opinion mining to obtain consumer feedback on the competitiveness of mobile phones. First, to distinguish the text type of online reviews and Q&A, we label the comparison category for 1409 online reviews and 2380 Q&A randomly, and then train the CSR and SVM models to obtain appropriate comparative sen tence pattern library for online reviews as well as the classification boundary of comparative sentence of Q&A. Compared with the existing classical comparative sentence discriminant methods, such as Compar ison Keyword Strategy (CKS), Naive Bayes (NB) and Random Forest (RF) [35,38], four evaluating indicators (i.e., Recall, Precision, F-measure and Accuracy [6]) of our method and classical methods on the test set are shown in Table 3.

According to Table 3, the following findings can be identified. First, the performance of our method is obviously better than the others, especially for the online reviews. Although NB and RF also have good performance on Q&A, they are still not as effective as the method in this paper. Second, our method is very accurate at identifying the compari son category of Q&A. The accuracy rate is about 98.2%, and other in dicators are greater than 90%, which indicates that the comparative sentence discrimination algorithm for consumer Q&A in this paper is reasonable. Third, the accuracy rate of our method for online reviews is approximately 93.7%. In particular, the recall and precision rates of our method for noncomparative reviews are 97.5% and 94.9%, respectively, which is significantly better than its discriminating performance on comparative reviews. This is mainly because the grammar of Chinese online reviews is complex, and it is difficult to distinguish comparative sentences, but the grammatical features of noncomparative sentences are relatively easy to identify [36]. As a whole, the overall discrimina tive accuracy of this method for online reviews and Q&A exceeds 95%, which lays a good foundation for the next step of extracting comparative elements.

As for the comparative elements extraction, we put the official mo bile phone name in the product attributes into the product name library. Then, the similarity between the suspected mobile phone name in online reviews and Q&A and the product name library is analyzed to extract the comparative subject and object. Moreover, the comparative aspect is obtained by the keywords in the third column of Table 2. The compar ative result is calculated by Eq. (5), and partial results of four-tuples are reported in Table 4.

![](/api/attachments/NGHX74AC/fulltext/images/b3b6ddce8d247b075341dea0b5260a2b91ee45a1f0cacd5d8436097a974e6a0d.jpg)  
Fig. 2. The product attributes, online reviews and Q&A on Jingdong platform.

## 4.3. Analysis of key competitiveness for mobile phones

Based on the information about four-tuples in the last section, we apply Eq. (6) to calculate the overall competitiveness and the competi tiveness in terms of 14 aspects for mobile phones; the results of these competitiveness values and ranking are shown in Table 5. To verify the rationality of the competitiveness values and ranking of mobile phones measured in this paper, we used the sales volume of mobile phones to validate the results (see Table 6). Since the products with similar price are comparable, this paper clusters the mobile phones in Table 6 into 5 groups according to price (i.e., high, medium-high, medium, medium low and low price groups, see Fig. 3). Tow findings can be obtained a follows.

For one thing, for the mobile phones in the same group, the sales volumes of these mobile phones roughly reflect that the higher the overall competitiveness of mobile phones, the higher their sales, except for the group of low price. The relationship between the sales volume and overall competitiveness of mobile phones in low price group is not obvious, and the possible reason is that the sales volume of mobile phones with low price is influenced by other factors such as brand [28]. For another, regarding the mobile phones among different groups, the mobile phones in medium price group have higher overall competi tiveness and sales volume. This result is consistent with that of Bodur et al. [43], who found that the medium price is most attractive to con sumers. Therefore, based on the sales volume of mobile phones, it can be concluded that the competitiveness and ranking of mobile phones measured in this paper are basically scientific.

Moreover, consumers’ feedback on the competitiveness of mobile phones is usually the most concerned aspect of them, which implies the key competitiveness for mobile phones [8]. However, different types of mobile phone users may have different concerns. For example, elderly phone users may care about the battery performance, while smartphone users may be concerned about camera performance [44]. Therefore, this article divides mobile phones into elderly phones and smartphones, and adopts Eq. (9) to estimate their key competitiveness, respectively. The results are reported in Table 7, and several findings can be highlighted a follows.

First, the comprehensive and price competitiveness are the most important for the overall competitiveness of mobile phones (i.e., key competitiveness). In other words, consumers are very concerned about the comprehensive performance and price of mobile phones. In addition, the pricing strategy of mobile phones should be a key focus for mobile phone enterprises to enhance their product competitiveness [45]. Sec ond, in addition to the comprehensive and price competitiveness, elderly phone users focus on the size, voice and battery competitivenes of mobile phones, while smartphone users care about that of the camera, CPU and appearance. This is because elderly phone users are usually older; thus, they want the phone size to be suitable for carrying, a high phone volume can make them hear more clearly, and excellent battery performance can enable the phone to be used for a long time. Therefore, mobile phones with outstanding competitiveness in terms of these as pects tend to be favored by elderly phone users. However, smartphone users are generally young people, and they prefer to take photos to share on social networks. Moreover, the functions of smartphone are more numerous than those of elderly phone, so consumers hope that smart phones have good CPU performance to run faster. Furthermore, most smartphone users have good aesthetic consciousness; thus, beautiful appearance of the phone is also their concern. Third, storage and weight

Table 2  
The attributes of mobile phones

<table><tr><td>Comparative aspect</td><td>Product attribute</td><td>Comparative aspect dictionary</td></tr><tr><td>Price</td><td>Price</td><td>Price, expensive, cheap and cost performance, etc.</td></tr><tr><td>Appearance</td><td>Body color</td><td>Elegant, color, beautiful and ugly, etc.</td></tr><tr><td>Size</td><td>Length, width and thickness</td><td>Size, thick, thin and long, etc.</td></tr><tr><td>Weight</td><td>Weight</td><td>Weight, heavy and light, etc.</td></tr><tr><td>Operating system</td><td>Operating system</td><td>System, fluent and Android, etc.</td></tr><tr><td>CPU</td><td>CPU brand, frequency and core</td><td>CPU, chip, speed and processor, etc.</td></tr><tr><td>Signal &amp; network</td><td>4G, 3G and 2G</td><td>Signal, network, Wifi and call up, etc.</td></tr><tr><td>Storage</td><td>RAM, ROM and expansion memory</td><td>RAM and ROM, etc.</td></tr><tr><td>Screen</td><td>Screen size, distinguishability and pixel density</td><td>Screen, colorful, clear and display, etc.</td></tr><tr><td>Camera</td><td>Front-facing camera number and pixel, rear camera number and pixel</td><td>Camera, photograph, photo, and diaphragm, etc.</td></tr><tr><td>Voice</td><td>Voice</td><td>Tone quality, trumpet, telephone receiver and loudspeaker, etc.</td></tr><tr><td>Battery</td><td>Battery capacity, disassembly and theoretical talk time</td><td>Battery, endurance, standby and charge, etc.</td></tr><tr><td>Face &amp; fingerprint recognition</td><td>Support face and fingerprint recognition</td><td>Face, endurance, unlock and identification, etc.</td></tr><tr><td>Comprehensive</td><td>-</td><td>Function, quality, entirety and utility, etc.</td></tr></table>

Table 3  
The performance of various comparative sentence discriminant methods.

<table><tr><td>Text type</td><td>Methods</td><td>Recall (%)</td><td>Precision (%)</td><td>F-measure (%)</td><td>Accuracy (%)</td></tr><tr><td rowspan="4">Comparative reviews</td><td>Our method</td><td>77.2</td><td>87.7</td><td>82.1</td><td>93.7</td></tr><tr><td>CKS</td><td>87.0</td><td>24.2</td><td>37.8</td><td>46.5</td></tr><tr><td>NB</td><td>21.7</td><td>34.5</td><td>26.7</td><td>77.6</td></tr><tr><td>RF</td><td>31.5</td><td>30.9</td><td>31.2</td><td>74.0</td></tr><tr><td rowspan="4">Noncomparative reviews</td><td>Our method</td><td>97.5</td><td>94.9</td><td>96.2</td><td>93.7</td></tr><tr><td>CKS</td><td>37.3</td><td>92.5</td><td>53.1</td><td>46.5</td></tr><tr><td>NB</td><td>90.5</td><td>83.4</td><td>86.8</td><td>77.6</td></tr><tr><td>RF</td><td>83.8</td><td>84.2</td><td>84.0</td><td>74.0</td></tr><tr><td rowspan="4">Comparative Q&amp;A</td><td>Our method</td><td>93.6</td><td>98.1</td><td>95.8</td><td>98.2</td></tr><tr><td>CKS</td><td>88.4</td><td>61.0</td><td>72.2</td><td>84.8</td></tr><tr><td>NB</td><td>92.8</td><td>84.2</td><td>88.3</td><td>94.5</td></tr><tr><td>RF</td><td>91.3</td><td>86.3</td><td>88.7</td><td>94.8</td></tr><tr><td rowspan="4">Noncomparative Q&amp;A</td><td>Our method</td><td>99.5</td><td>98.1</td><td>98.8</td><td>98.2</td></tr><tr><td>CKS</td><td>83.8</td><td>96.2</td><td>89.6</td><td>84.8</td></tr><tr><td>NB</td><td>95.0</td><td>97.9</td><td>96.4</td><td>94.5</td></tr><tr><td>RF</td><td>95.9</td><td>97.5</td><td>96.7</td><td>94.8</td></tr><tr><td rowspan="4">All text types</td><td>Our method</td><td>86.1</td><td>93.5</td><td>89.6</td><td>95.9</td></tr><tr><td>CKS</td><td>87.6</td><td>32.7</td><td>47.6</td><td>61.3</td></tr><tr><td>NB</td><td>52.2</td><td>62.7</td><td>56.9</td><td>84.2</td></tr><tr><td>RF</td><td>57.1</td><td>55.1</td><td>56.1</td><td>82.0</td></tr></table>

Note: The bold fonts indicate the performance of the method proposed in this paper on various text types, and the values corresponding to CKS, NB and RF represent the performance of the classical method of Comparison Keyword Strategy, Naive Bayes and Random Forest on various text types.

are not key concerns for all users. In addition, elderly phone users pay less attention to the operating system and face & fingerprint recognition, and smartphone users do not care about signal & network as well as face & fingerprint recognition. Hence, we do not recommend enterprises regard these aspects as the core competitiveness of their products.

Table 4  
The partial results of four-tuples.

<table><tr><td>Mobile phone</td><td>Four-tuples</td></tr><tr><td>M1</td><td>(M1, M3, Price, 2), (M1, M4, Comprehensive, 0), (M1, M7, CPU, 1), etc.</td></tr><tr><td>M2</td><td>(M2, M3, Weight, -1), (M2, M4, Camera, 1.5), (M2, M6, Screen, -3), etc.</td></tr><tr><td>M3</td><td>(M3, M2, Price, 1), (M3, M2, Price, 0), (M3, M13, Battery, 3), etc.</td></tr><tr><td>M4</td><td>(M4, M1, Camera, 2), (M4, M23, Size, -1.5), (M4, M17, Storage, 2.5), etc.</td></tr><tr><td>M5</td><td>(M5, M2, Screen, -1.5), (M5, M26, Screen, 1), (M5, M35, Appearance, 2), etc.</td></tr></table>

Note: To protect the privacy of mobile phone enterprises, we abbreviate the phone name to Mi.

In fact, according to the China Mobile Internet Research Report released by China Internet Network Information Center,<sup>9</sup> communication is the main users’ demand of elderly phones, so voice and battery are their main concerns. As for smartphones, 35.8% of users hope that the smartphones have good comprehensive function, followed by appearance (19.7%) and screen (17.7%); while only a few users care about the network of smartphones. This report is roughly in line with the results of this paper.

## 4.4. The impact factors of key competitiveness for mobile phones

After acquiring the key competitiveness of mobile phones, we use the quantile regression model to study the factors that impact key compet itiveness, to help mobile phone enterprises to improve their competi tiveness in these key aspects. According to the second column of Table 2, this paper takes the product attributes of mobile phones as independent variables that affect the competitiveness of the corresponding aspects. The impact factors of some key competitiveness are listed in Table 8.

Since the dependent variable needs to meet the nonnormality hy pothesis in quantile regression model, we use the Jarque-Bera Statistics to test the normality of competitiveness in price, size and camera [46]. The results show that they all reject the null hypothesis of normal dis tribution at the 1% significance level. According to Eq. (11), the quantile regression results of three kinds of competitiveness are shown in Fig. 4 to Fig. 6. The solid lines in the figures represent the regression coefficients at different quantiles, and the gray areas demonstrate the 95% confi dence intervals.

Regarding the price competitiveness, two findings from Fig. 4 are obtained. First, the price competitiveness of elderly phones is not directly reflected through the price, because its regression coefficient is close to zero and not significant. The reason is that the prices of elderly phones are very cheap compared to smartphones, and the consumers are not sensitive to the perception of low price (the average price of elderly phones collected in this paper is 205 RMB, while the average price of smartphones is 2244 RMB). Second, consumers are sensitive to the price of smartphones, and the sensitivity for smartphones with a high competitiveness level is higher than that of smartphones with a low competitiveness level. The regression coefficients of price competitive ness of smartphones are about 0 and − 0.3 at 0–0.2 quantiles and 0.75–1 quantiles, respectively. It indicates that the price change of a low competitive smartphone has little impact on its price competitiveness, while 1 RMB increase in the price of high-competitive smartphone may result in a decrease in its price competitiveness index by 0.3. This im plies that the price competitiveness advantage of a cheaper high-end

<table><tr><td></td><td>Overall</td><td>Price</td><td>Appearance</td><td>Size</td><td>Weight</td><td>Operating system</td><td>CPU</td><td>Signal &amp; network</td><td>Storage</td><td>Screen</td><td>Camera</td><td>Voice</td><td>Battery</td><td>Face &amp; fingerprint recognition</td><td>Comprehensive</td></tr><tr><td>M1</td><td>172/1</td><td>58/1</td><td>24/23</td><td>36/6</td><td>6/13</td><td>34/4</td><td>70/1</td><td>10/8</td><td>2/21</td><td>47/1</td><td>58/3</td><td>1/97</td><td>22/12</td><td>24/1</td><td>109/3</td></tr><tr><td>M2</td><td>159/2</td><td>43/3</td><td>33/5</td><td>30/8</td><td>4/22</td><td>41/2</td><td>52/3</td><td>15/2</td><td>2/23</td><td>45/2</td><td>50/4</td><td>9/26</td><td>38/1</td><td>12/13</td><td>116/1</td></tr><tr><td>M3</td><td>159/3</td><td>22/21</td><td>27/10</td><td>40/4</td><td>8/7</td><td>34/5</td><td>30/20</td><td>12/6</td><td>2/25</td><td>40/6</td><td>39/13</td><td>13/11</td><td>25/6</td><td>7/36</td><td>91/6</td></tr><tr><td>M4</td><td>154/4</td><td>33/8</td><td>16/49</td><td>16/53</td><td>1/47</td><td>30/9</td><td>43/9</td><td>9/10</td><td>4/14</td><td>33/17</td><td>39/14</td><td>4/60</td><td>23/7</td><td>8/27</td><td>109/2</td></tr><tr><td>M5</td><td>149/5</td><td>13/53</td><td>25/17</td><td>14/60</td><td>0/50</td><td>12/72</td><td>31/18</td><td>1/66</td><td>2/28</td><td>38/12</td><td>35/20</td><td>18/2</td><td>20/19</td><td>13/10</td><td>88/8</td></tr><tr><td>M6</td><td>146/6</td><td>13/56</td><td>25/18</td><td>25/18</td><td>5/17</td><td>27/20</td><td>39/10</td><td>9/11</td><td>6/6</td><td>29/24</td><td>67/2</td><td>14/6</td><td>20/20</td><td>8/31</td><td>93/4</td></tr><tr><td>M7</td><td>144/7</td><td>18/33</td><td>15/53</td><td>24/22</td><td>6/10</td><td>31/7</td><td>37/12</td><td>6/27</td><td>4/13</td><td>32/18</td><td>43/11</td><td>3/74</td><td>22/14</td><td>20/2</td><td>74/16</td></tr><tr><td>M8</td><td>138/8</td><td>32/9</td><td>33/4</td><td>24/23</td><td>1/41</td><td>16/52</td><td>51/4</td><td>4/41</td><td>0/35</td><td>38/10</td><td>38/17</td><td>13/9</td><td>12/52</td><td>10/19</td><td>78/11</td></tr><tr><td>M9</td><td>137/9</td><td>41/5</td><td>11/74</td><td>17/49</td><td>3/27</td><td>31/8</td><td>28/21</td><td>7/21</td><td>5/9</td><td>18/51</td><td>33/24</td><td>2/86</td><td>21/18</td><td>7/42</td><td>86/9</td></tr><tr><td>M10</td><td>132/10</td><td>11/64</td><td>11/73</td><td>21/33</td><td>3/27</td><td>27/21</td><td>24/34</td><td>3/54</td><td>2/22</td><td>39/8</td><td>29/32</td><td>2/90</td><td>14/44</td><td>11/17</td><td>67/23</td></tr><tr><td>M11</td><td>132/11</td><td>39/6</td><td>28/9</td><td>23/26</td><td>3/24</td><td>24/24</td><td>27/22</td><td>5/35</td><td>5/10</td><td>42/3</td><td>19/60</td><td>13/8</td><td>18/26</td><td>2/78</td><td>77/13</td></tr><tr><td>M12</td><td>129/12</td><td>19/28</td><td>12/72</td><td>16/52</td><td>2/33</td><td>27/19</td><td>15/70</td><td>9/13</td><td>2/22</td><td>8/107</td><td>44/8</td><td>13/7</td><td>23/10</td><td>16/6</td><td>61/30</td></tr><tr><td>M13</td><td>129/13</td><td>17/36</td><td>36/1</td><td>44/2</td><td>2/37</td><td>15/56</td><td>36/13</td><td>4/47</td><td>4/13</td><td>18/50</td><td>38/15</td><td>13/10</td><td>30/2</td><td>12/14</td><td>78/12</td></tr><tr><td>M14</td><td>127/14</td><td>9/86</td><td>25/15</td><td>44/1</td><td>14/1</td><td>29/12</td><td>11/91</td><td>5/31</td><td>6/7</td><td>32/19</td><td>27/36</td><td>13/13</td><td>14/43</td><td>10/21</td><td>65/25</td></tr><tr><td>M15</td><td>127/15</td><td>31/12</td><td>25/19</td><td>22/30</td><td>2/32</td><td>51/1</td><td>45/6</td><td>0/72</td><td>2/26</td><td>24/33</td><td>24/49</td><td>1/95</td><td>13/45</td><td>14/8</td><td>90/7</td></tr><tr><td>M16</td><td>124/16</td><td>22/23</td><td>26/13</td><td>28/10</td><td>4/20</td><td>17/47</td><td>34/15</td><td>6/29</td><td>0/35</td><td>22/39</td><td>25/43</td><td>6/44</td><td>11/60</td><td>4/60</td><td>77/14</td></tr><tr><td>M17</td><td>120/17</td><td>32/10</td><td>21/28</td><td>20/38</td><td>9/4</td><td>30/11</td><td>43/7</td><td>1/70</td><td>4/12</td><td>21/43</td><td>43/9</td><td>3/72</td><td>22/15</td><td>13/9</td><td>75/15</td></tr><tr><td>M18</td><td>118/18</td><td>11/69</td><td>13/66</td><td>24/25</td><td>2/35</td><td>18/43</td><td>31/19</td><td>15/4</td><td>3/19</td><td>24/31</td><td>33/25</td><td>3/70</td><td>19/24</td><td>13/12</td><td>62/29</td></tr><tr><td>M19</td><td>117/19</td><td>28/14</td><td>13/64</td><td>20/36</td><td>1/43</td><td>30/10</td><td>55/2</td><td>4/44</td><td>7/3</td><td>27/28</td><td>31/29</td><td>5/51</td><td>19/23</td><td>8/32</td><td>68/20</td></tr><tr><td>M20</td><td>117/20</td><td>49/2</td><td>32/6</td><td>13/69</td><td>4/21</td><td>10/79</td><td>35/14</td><td>5/33</td><td>2/24</td><td>22/40</td><td>38/18</td><td>4/59</td><td>10/67</td><td>7/40</td><td>92/5</td></tr><tr><td>M21</td><td>117/21</td><td>41/4</td><td>18/43</td><td>13/68</td><td>1/41</td><td>15/58</td><td>26/32</td><td>3/49</td><td>8/2</td><td>13/74</td><td>44/7</td><td>7/37</td><td>21/17</td><td>4/64</td><td>80/10</td></tr><tr><td>M22</td><td>116/22</td><td>14/46</td><td>22/27</td><td>17/46</td><td>0/50</td><td>14/62</td><td>20/49</td><td>3/53</td><td>0/35</td><td>28/26</td><td>70/1</td><td>9/22</td><td>15/37</td><td>11/18</td><td>64/28</td></tr><tr><td>M23</td><td>115/23</td><td>5/125</td><td>23/25</td><td>24/21</td><td>12/2</td><td>27/22</td><td>20/50</td><td>3/50</td><td>0/35</td><td>35/15</td><td>33/26</td><td>9/24</td><td>18/25</td><td>17/4</td><td>57/41</td></tr></table>

The competitiveness and ranking of mobile phones in each aspect.  
the number after ‘/’ is the competitiveness ranking. Note: The first row represents the overall competitiveness of mobile phones and the competitiveness of mobile phones in 14 aspects. The number before ‘/’ indicates the competitiveness index (rounded to an integer), and

Table 6  
The sales volume and product price of mobile phones.

<table><tr><td>MP</td><td>SV</td><td>PP</td><td>MP</td><td>SV</td><td>PP</td><td>MP</td><td>SV</td><td>PP</td></tr><tr><td>M1</td><td>145.8</td><td>2499</td><td>M9</td><td>78.9</td><td>1099</td><td>M17</td><td>84</td><td>1299</td></tr><tr><td>M2</td><td>145.5</td><td>1899</td><td>M10</td><td>49</td><td>3199</td><td>M18</td><td>26</td><td>3299</td></tr><tr><td>M3</td><td>137.7</td><td>6199</td><td>M11</td><td>98</td><td>999</td><td>M19</td><td>54.9</td><td>1898</td></tr><tr><td>M4</td><td>121.9</td><td>2499</td><td>M12</td><td>58</td><td>899</td><td>M20</td><td>39.5</td><td>1598</td></tr><tr><td>M5</td><td>12.5</td><td>4998</td><td>M13</td><td>133</td><td>2378</td><td>M21</td><td>113.2</td><td>1199</td></tr><tr><td>M6</td><td>78</td><td>3349</td><td>M14</td><td>2.7</td><td>5999</td><td>M22</td><td>36</td><td>3688</td></tr><tr><td>M7</td><td>37</td><td>2599</td><td>M15</td><td>33.2</td><td>3169</td><td>M23</td><td>2.3</td><td>6999</td></tr><tr><td>M8</td><td>119</td><td>1598</td><td>M16</td><td>143.6</td><td>1199</td><td></td><td></td><td></td></tr></table>

Note: MP, SV and PP represent mobile phone, sales volume (Unit: 10<sup>4</sup> piece) and product price (Unit: RMB), respectively.

![](/api/attachments/NGHX74AC/fulltext/images/a3c5a0da865ed7452642d695d7cbac29c29a239221e1d6c3a0f1c9d407e1c1b0.jpg)  
High price Medium-high price Medium price Medium-low price Low price

Fig. 3. The sales volume and competitiveness ranking in five price groups.

smartphone will be obvious [47].

As for the size competitiveness, we have the following findings. First, as a whole, the width and thickness have positive and negative in fluences on the size competitiveness of mobile phones, respectively, while the effect of the length on size competitiveness is not significant (see first row of Fig. 5). This outcome indicates that wide and thin phones are more competitive in size, but the length does not affect consumers’ judgment regarding the size competitiveness of mobile phones. Second, the width has a negative impact on size competitiveness of elderly phones at medium and high competitiveness levels, while the thickness has no significant effect on the size competitiveness of elderly phones (see the second row of Fig. 5). These results show that the users of elderly phones at medium and high competitiveness levels prefer narrow phones, but they do not care about phone thickness [48]. Third, the width has a positive influence on the size competitiveness of smartphones at medium and high competitiveness levels and a negative influence on that of medium-high competitiveness smartphones (see the third row of Fig. 5). Moreover, compared with other competitiveness levels of smartphones, the thickness has a greater negative impact on the size competitiveness of smartphones at a high competitiveness level, and its regression coefficient is about − 0.4. This shows that when the thickness of high-end smartphones increases 1 mm, the size competi tiveness index may decrease by 0.4.

Besides, two findings about the camera competitiveness of smart phones can be obtained. First, the front-facing camera pixel has a sig nificant positive impact on the camera competitiveness of the smartphones, especially for smartphones at high competitiveness level, but the number of front-facing cameras does not affect this competi tiveness (see the first row of Fig. 6). This is because the front-facing camera is often used for selfies, and most consumers may prefer a high-definition selfie to share with friends on social networks, but a front-facing camera with multiple modes is not their concern [49]. Second, the rear camera pixel and number have a bigger positive in fluence on the camera competitiveness of the smartphones with medium and high competitiveness, respectively (see the second row of Fig. 6).

Table 7  
The rank of importance of the competitiveness for elderly phones and smartphones.

<table><tr><td colspan="2">Whole</td><td colspan="2">Elderly phone</td><td colspan="2">Smartphone</td></tr><tr><td>Competitiveness</td><td>MI</td><td>Competitiveness</td><td>MI</td><td>Competitiveness</td><td>MI</td></tr><tr><td>Comprehensive</td><td>5.2118</td><td>Comprehensive</td><td>3.7971</td><td>Comprehensive</td><td>5.0752</td></tr><tr><td>Price</td><td>4.3681</td><td>Price</td><td>2.2010</td><td>Price</td><td>4.9820</td></tr><tr><td>Size</td><td>4.2064</td><td>Size</td><td>2.1503</td><td>Camera</td><td>4.9701</td></tr><tr><td>Appearance</td><td>4.1481</td><td>Voice</td><td>1.9434</td><td>CPU</td><td>4.9610</td></tr><tr><td>CPU</td><td>4.1103</td><td>Battery</td><td>1.8792</td><td>Appearance</td><td>4.8818</td></tr><tr><td>Camera</td><td>4.0852</td><td>Appearance</td><td>1.7641</td><td>Screen</td><td>4.8808</td></tr><tr><td>Screen</td><td>4.0292</td><td>Screen</td><td>1.5967</td><td>Size</td><td>4.8530</td></tr><tr><td>Battery</td><td>3.8451</td><td>CPU</td><td>1.4685</td><td>Operating system</td><td>4.5934</td></tr><tr><td>Operating system</td><td>3.5959</td><td>Camera</td><td>1.4624</td><td>Battery</td><td>4.5495</td></tr><tr><td>Voice</td><td>3.3112</td><td>Signal &amp; network</td><td>1.3526</td><td>Voice</td><td>3.8705</td></tr><tr><td>Face &amp; fingerprint recognition</td><td>2.7571</td><td>Operating system</td><td>1.0099</td><td>Face &amp; fingerprint recognition</td><td>3.6854</td></tr><tr><td>Signal &amp; network</td><td>2.6545</td><td>Face &amp; fingerprint recognition</td><td>0.8066</td><td>Signal &amp; network</td><td>3.3123</td></tr><tr><td>Weight</td><td>2.0580</td><td>Weight</td><td>0.7262</td><td>Weight</td><td>2.7722</td></tr><tr><td>Storage</td><td>1.7790</td><td>Storage</td><td>0.5234</td><td>Storage</td><td>2.4356</td></tr></table>

Note: MI means mutual information, which reflects the importance of competitiveness in a specific aspect. The two columns for “Whole” represent the rank of competitive importance for all mobile phones, including elderly phones and smartphones. The columns corresponding to “Elderly phones” and “Smartphones” indicate the rank of competitive importance for elderly phones and smartphones, respectively.

Table 8  
The impact factor of key competitiveness for mobile phones.

<table><tr><td>Competitiveness</td><td>Independent variable (Symbol)</td><td>Elderly phone</td><td>Smartphone</td></tr><tr><td>Price</td><td>Price</td><td>√</td><td>√</td></tr><tr><td>Size</td><td>Length; Width; Thickness</td><td>√</td><td>√</td></tr><tr><td>Camera</td><td>Front-facing camera number and pixel (camera_f_n, camera_f_p); Rear camera number and pixel (camera_r_n, camera_r_p)</td><td></td><td>√</td></tr></table>

Note: According to data availability of elderly phone and smartphone, $\surd$ denote the case that analyses the impact of product attributes on corresponding competitiveness.

This result implies that the rear camera pixel of mid-range smartphones should be as high as possible, and high-end smartphones should have more camera modes, because these users may prefer taking photos in multiple scenes.

## 5. Conclusions

## 5.1. Summary of results

Based on the comparative opinion mining method, this paper in tegrates three data sources of product attribute information, online re views and Q&A to construct a research framework for analyzing product competitiveness. We take mobile phones as a case to verify the perfor mance of this framework. First of all, the results of extracting competitiveness information of mobile phones from online reviews and Q&A show that the performance of the method in this paper is better than that of other relevant methods. Second, based on the competi tiveness information of mobile phones, we find that the key competi tiveness of elderly phones is price, size and voice competitiveness, and the key competitiveness of the smartphones includes price, camera and CPU competitiveness, while storage and weight competitiveness are less important for both the elderly phones and smartphones. Third, when analyzing the impact factors of key competitiveness, the results show that the price has no significant influence on the price competitiveness of elderly phones but a significant negative influence on smartphones at high competitiveness level. Moreover, the width has a negative influ ence on elderly phones with middle and high competitiveness, while for smartphones with middle and high competitiveness, the effect is the opposite. Furthermore, we also find that the front-facing camera pixel and rear camera number both have larger positive influences on the camera competitiveness of smartphones with high competitiveness, but the number of front-facing cameras does not affect the camera competitiveness of smartphones.

## 5.2. Theoretical implications

The theoretical implications of this paper are multifold. First, the framework constructed in this paper provides a novel insight to study product competitiveness. On the one hand, since online reviews may have some fake information, but the Q&A contains less fake information [10], this paper combines these two data sources to alleviate the infor mation bias of single-source online reviews, and it can analyze product competitiveness more accurately. On the other hand, we can mine product competitiveness information more comprehensively by inte grating multiple data sources.

![](/api/attachments/NGHX74AC/fulltext/images/7046bb2eb9a88e187721d1554039b064a8383d4c75f65a95fd3e443edf7f2f51.jpg)  
Whole

![](/api/attachments/NGHX74AC/fulltext/images/b90875406318d6aedeb86daea0b19e5cbd10a961302e8cb8ed3d2ba50dba3048.jpg)  
Fig. 4. The price competitiveness.

![](/api/attachments/NGHX74AC/fulltext/images/329253183d76ab704b784cae9c505d832fc66914d5a3dced0b3b4c53044787fe.jpg)  
Smartphones

![](/api/attachments/NGHX74AC/fulltext/images/09324873825262338916847686c8d6f8e968923e7871f1addec481e42b2483c7.jpg)  
Fig. 5. The size competitiveness.

Second, the algorithm designed in this paper extracts the competi tiveness information from the Q&A to enrich the existing comparative opinion mining research, while most scholars focus on mining online review texts, to the best of our knowledge, and few scholars mine Q&A based on comparative opinion mining. However, Q&A contains a wealth of information that can be used for exploring product competitiveness.

Finally, based on the quantile regression model, this paper analyzes the factors that influence the key competitiveness of products at different competitiveness levels, and its research perspective is micro scopic. Compared with the structural equation model to study the fac tors affecting product competitiveness, it can provide more detailed recommendations for improving product competitiveness.

## 5.3. Managerial implications

Based on the conclusions of this study regarding mobile phones competitiveness, we have the following management implications. First, this paper designs a research framework integrating multisource online information to analyze the competitiveness of products, which can provide detailed competitive insights for products that similar with mobile phones, such as computers, refrigerators and washing machines. Then, we can provide targeted recommendations to improve the competitiveness of these products.

Second, the results of this study show that different types of con sumers usually have different focuses on products. It is recommended that enterprise managers need to not only accurately identify consumer groups but also put effort into the focus of consumers to accurately improve products competitiveness [8]. In addition, it is not necessary for enterprises to design each product attribute to the highest configuration to minimize costs [50]. For example, mobile phone enterprises are not recommended to improve the competitiveness of mobile phones by increasing storage, because consumers do not pay much attention to mobile phone storage.

Third, according to the results of this paper, the effect of impact factors on products at different competitiveness levels is quite various. Enterprises should make full use of these impact factors to develop the competitive strategies. For instance, we recommend that enterprises should develop pricing strategies based on the price sensitivity of

![](/api/attachments/NGHX74AC/fulltext/images/282034865590584771b014073df67c529780230776a82dc1b24aef1dbe0c4eb7.jpg)

![](/api/attachments/NGHX74AC/fulltext/images/83f4cb34898d0c0720e91b1235e6f16386e7beb19049dfb354e6ad982665904c.jpg)

![](/api/attachments/NGHX74AC/fulltext/images/7c0b6be42dfc8e556c113f7f6cca1de55c6d545233c6781d2b1eb32f0c6a018b.jpg)

![](/api/attachments/NGHX74AC/fulltext/images/a97fb848a6f378668a942d8b90e26b10b72527b1cde9c4e78fa88fa543080a59.jpg)  
Fig. 6. The camera competitiveness of smartphones  
consumer to different positioned products.

## 5.4. Limitations and future research

This paper also has some limitations. First, the comparative opinion mining needs to build some dictionaries through domain knowledge, which increases the degree of dependence on manual work. Future studies would reduce the artificial dependence of comparative opinion mining. Second, many e-commerce platforms cannot provide Q&A at present, and there are information inconsistencies between different platforms. Thus, when the data are available on different platforms, we would integrate the multisource online information on multi-platform to explore product competitiveness in the future. Third, the research framework proposed in this paper mainly mines Chinese online infor mation, and it is also our future research direction to build a research framework for product competitiveness analysis in multilingual online information.

## Acknowledgments

We gratefully acknowledge the financial support from the National Natural Science Foundation of China (nos. 71774051), National Pro gram for Support of Top-notch Young Professionals (no. W02070325), Changjiang Scholars Program of the Ministry of Education of China (no. Q2016154), Science Fund Distinguished Young Scholars of Hunan province (nos. 2018JJ1010) and Hunan Youth Talent Program.

Appendix A. The algorithm of distinguishing the text type of Q&A

<table><tr><td>Input:</td><td>Q: The text set of consumer questions, A: The text set of consumer answers</td></tr><tr><td>Output:</td><td>The labels of consumer Q&amp;A (comparative sentence or non-comparative sentence)</td></tr><tr><td>1.</td><td> $QV = \text{Word2Vector}(Q); // \text{Corresponding to Eq. (4).}$ </td></tr><tr><td>2.</td><td>// Training SVM models to obtain the classification boundary of comparative //sentences and noncomparative sentences in Q&amp;A.</td></tr><tr><td>3.</td><td>Svm = SVM(QV);</td></tr><tr><td>4.</td><td>Fori in range(0,len(QV)):</td></tr><tr><td>5.</td><td>label_1 = Svm(QV[i]);</td></tr><tr><td>6.</td><td>If label_1 is preliminary comparative sentence:</td></tr><tr><td>7.</td><td>// Try to extract the comparative subject (P1), comparative object (P2) and // comparative aspect (aspect) in the Q&amp;A.</td></tr><tr><td>8.</td><td>P1, P2, aspect ← find in Q[i];</td></tr><tr><td>9.</td><td>Forj in A:</td></tr><tr><td>10.</td><td>IfP1or P2 is in j:</td></tr><tr><td>11.</td><td>Then return comparative sentence;</td></tr><tr><td>12.</td><td>Else ifP1and P2 is not in j:</td></tr><tr><td>13.</td><td>return non-comparative sentence;</td></tr><tr><td>14.</td><td>Else:</td></tr><tr><td>15.</td><td>return non-comparative sentence;</td></tr></table>

## References

[1] M.E. Porter, Competitive Strategy: Techniques for Analyzing Industries and Competitors, Free Press, New York, 1980 (pp. 86-87).

[2] M.J. Chen, D. Miller, Reconceptualizing competitive dynamics: a multidimensional framework, Strategic. Manage. J. 36 (5) (2014) 758–775, https://doi.org/ 10.1002/smj.2245.

[3] H.F. Huang, Y. He, J. Chen, Competitive strategies and quality to counter parallel importation in global market, Omega 86 (2019) 173–197, https://doi.org 10.1016/j.omega.2018.07.009.

[4] V. Kumar, A.R. Saboo, A. Agarwal, B. Kumar, Generating competitive intelligence with limited information: a case of the multimedia industry, Prod. Oper. Manag. 29 (1) (2020) 192–213, https://doi.org/10.1111/poms.13095.

[5] J.O. Schwarz, C. Ram, R. Rohrbeck, Combining scenario planning and business wargaming to better anticipate future competitive dynamics, Futures 105 (2019) 133–142, https://doi.org/10.1016/j.futures.2018.10.001.

[6] Y. Liu, C. Jiang, H. Zhao, Assessing product competitive advantages from the perspective of customers by mining user-generated content on social media, Decis. Support. Syst. 123 (2019) 113079, https://doi.org/10.1016/j.dss.2019.113079.

[7] S. Gao, O. Tang, H. Wang, P. Yin, Identifying competitors through comparative relation mining of online reviews in the restaurant industry, Int. J. Hosp. Manag. 71 (2018) 19–32, https://doi.org/10.1016/j.ijhm.2017.09.004.

[8] J. Bi, Y. Liu, Z. Fan, J. Zhang, Wisdom of crowds: conducting importanceperformance analysis (IPA) through online reviews, Tourism. Manage. 70 (2019) 460–478, https://doi.org/10.1016/j.tourman.2018.09.010.

[9] Y. Wu, E.W.T. Ngai, P. Wu, C. Wu, Fake online reviews: literature review, synthesis, and directions for future research, Decis. Support. Syst. 132 (2020) 113280, https://doi.org/10.1016/j.dss.2020.113280.

[10] S. Moon, M. Kim, P.K. Bergey, Estimating deception in consumer reviews based on extreme terms: Comparison analysis of open ys. closed hotel reservation platforms J. Bus. Res. 102 (2019) 83–96. https://doi,org/10.1016/i,ibusres.2019.05.016.

[11] Z. Xiang, Q. Du, Y. Ma, W. Fan, A comparative analysis of major online review platforms: implications for social media analytics in hospitality and tourism, Tourism. Manage. 58 (2017) 51–65, https://doi.org/10.1016/j tourman 2016.10.001

[12] M.J. Chen, D. Miller, Competitive attack, retaliation and performance: an expectancy-valence framework, Strategic. Manage. J. 15 (1994) 85–102, https:// doi.org/10.1002/smj.4250150202.

[13] S.D. Hunt, A. Menon, Metaphors and competitive advantage: evaluating the use of metaphors in theories of competitive strategy, J. Bus. Res. 33 (2) (1995) 81–90. https://doi.org/10.1016/0148-2963(94)00057-L.

[14] M.J. Chen, Competitor analysis and interfirm rivalry: toward a theoretical integration, Acad. Manag. Rev. 21 (1) (1996) 100–134, https://doi.org/10.5465/ amr.1996.9602161567.

[15] S. Boubaker, W. Saffar, S. Sassi, Product market competition and debt choice, J. Corp. Financ. 49 (2018) 204–224, https://doi.org/10.1016/j. jcorpfin.2018.01.007.

[16] S. Jang, J. Chung, V.R. Rao, The importance of functional and emotional content in online consumer reviews for product sales: evidence from the mobile gaming market, J. Bus. Res. (2019), https://doi.org/10.1016/j.jbusres.2019.09.027.

[17] K. Kaushik, R. Mishra, N.P. Rana, Y.K. Dwivedi, Exploring reviews and review sequences on e-commerce platform: A study of helpful reviews on Amazon.in, J. Retail. Consum. Serv. 45 (2018) 21, https://doi.org/10.1016/j. jretconser.2018.0.8.008.

[18] S.P. Eslami, M. Ghasemaghaei, K. Hassanein, Which online reviews do consumers find most helpful? A multi-method investigation, Decis. Support. Syst. 113 (2018) 32–42, https://doi.org/10.1016/j.dss.2018.06.012.

[19] X. Luo, Product competitiveness and beating analyst earnings target, J. Acad. Market. Sci, 38 (3) (2010) 253–264. https://ssrn.com/abstract=2341869.

[20] D.C. Hambrick, High profit strategies in mature capital goods industries: a contingency approach. Acad. Manag, J. 26 (1983) 687–707. https://doi,org/ 10.5465/255916.

[211 D. Miller. Relating Porter's business strategies to environment and structure: analysis and performance implications, Acad. Manag. J. 31 (1988) 280–308, https://doi.org/10.5465/256549.

[22] M. Hunold, R. Kesler, U. Laitenberger, Rankings of online travel agents, channel pricing, and consumer protection, Market. Sci. 39 (1) (2020) 92–116, https://doi. org/10.1287/mksc.2019.1167.

[23] P. Desmichel, B. Kocher, Luxury single- versus multi-brand stores: the effect of consumers' hedonic goals on brand comparisons, J. Retailing, 96 (2) (2020) 203–219. https://doi.org/10.1016/i.iretai,2019.09.002

[24] J.J. Marcel, P.S. Barr, I.M. Duhaime, The influence of executive cognition on competitive dynamics, Strategic. Manage. J. 32 (2010) 115–138, https://doi.org/ 10.1002/smi 870

[25] B. Helversen, K. Abramczuk, W. Kope´c, R. Nielek, Influence of consumer reviews on online purchasing decisions in older and younger adults, Decis. Support. Syst. 113 (2018) 1–10, https://doi.org/10.1016/j.dss.2018.05.006.

[26] X. Li, L.M. Hitt, Self-selection and information role of online product reviews, Inform. Syst. Res. 19 (4) (2008) 456–474, https://doi.org/10.1287 isre.1070.0154

[27] B. Phadermrod, R.M. Crowder, G.B. Wills, Importance-performance analysis based SWOT analysis, Int. J. Inform. Manage. 44 (2019) 194–203, https://doi.org 10.1016/i.jiinfomgt.2016.03.009

[28] S.H. Amin, J. Razmi, G. Zhang, Supplier selection and order allocation based on fuzzy SWOT analysis and fuzzy linear programming, Expert Syst. Appl. 38 (2011) 334–342, https://doi.org/10.1016/j.eswa.2010.06.071.

[29] H. Lee, M.S. Kim, Y. Park, An analytic network process approach to operationalization of five forces model, Appl. Math. Model. 36 (2012) 1783–1795, https://doi.org/10.1016/j.apm.2011.09.012.

[30] S. Gupta, N.K. Malhotra, M.R. Czinkota, P. Foroudi, Marketing innovation: a consequence of competitiveness, J. Bus. Res. 69 (12) (2016) 5671–5681, https:/ doi.org/10.1016/i.ibusres.2016.02.042.

[31] K. Yonezawa, T.J. Richards, Competitive package size decisions, J. Retailing. 92 (4) (2016) 445–469, https://doi.org/10.1016/i.iretai.2016.06.001.

[32] H.S. Yan, K.P. Ma, Competitive diffusion process of repurchased products in knowledgeable manufacturing, Eur. J. Oper. Res. 208 (2011) 243–252, https://doi. org/10.1016/j.ejor.2010.09.005.

[33] A. Hagiu, J. Wright, Platforms and the exploration of new products, Manag. Sci. 66 (4) (2020) 1527–1543, https://doi.org/10.1287/mnsc.2018.3272.

[34] S. Sun, C. Luo, J. Chen, A review of natural language processing techniques for opinion mining systems, Inform. Fusion. 36 (2017) 10–25, https://doi.org/ 10.1016/j.inffus.2016.10.004.

[35] J. Jin, P. Ji, R. Gu, Identifying comparative customer requirements from product online reviews for competitor analysis, Eng. Appl. Artif. Intell. 49 (2016) 61–73, https://doi.org/10.1016/j.engappai.2015.12.005.

[36] K. Xu, S.S. Liao, J. Li, Y. Song, Mining comparative opinions from customer reviews for competitive intelligence, Decis. Support. Syst. 50 (4) (2011) 743–754, https:/ doi.org/10.1016/j.dss.2010.08.021.

[37] M. Azmi, G.C. Runger, A. Berrado, Interpretable regularized class association rules algorithm for classification in a categorical data space, Inform. Sciences. 483 (2019) 313–331, https://doi.org/10.1016/j.ins.2019.01.047.

[38] N. Jindal, B. Liu, Identifying Comparative Sentences in Text Documents, in: Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, New York, 2006, pp. 244–251, https://doi.org/10.1145/1148170.1148215.

[39] J. Mielniczuk, P. Teisseyre, Stopping rules for mutual information-based feature selection, Neurocomputing 358 (2019) 255–274, https://doi.org/10.1016/j. neucom.2019.05.048

[40] R. Koenker, G. Bassett. Regression Ouantiles. Econometrica 46 (1) (1978) 33–501 https://doi.org/10.2307/1913643

[41] V. Chernozhukov, C. Hansen, An IV model of quantile treatment effects, Econometrica 73 (1) (2005) 245–261, https://doi.org/10.1111/j.1468-0262. 2005.00570.x

[42] M. Danquah, A.M. Iddrisu, Access to mobile phones and the wellbeing of non-farm enterprise households: evidence from Ghana, Technol. Soc. 54 (2019) 1–9, https:/ doi.org/10.1016/j.techsoc.2018.01.012.

[43] H.O. Bodur, N.M. Klein, N. Arora, Online price search: impact of price comparison sites on offline price evaluations, J. Retailing. 91 (1) (2015) 125–139. https://doi org/10.1016/j.jretai.2014.09.003.

[44] M.R. Dotson, J. Büschken, G.M. Allenby, Explaining preference heterogeneity with mixed membership modeling, Market. Sci. 39 (2) (2020) 407–426, https://doi.org 10.1287/mksc 2019.1185

[45] C. Giachetti, G. Marchi, Successive changes in leadership in the worldwide mobile phone industry: the role of windows of opportunity and firms’ competitive action, Res. Policy 46 (2) (2017) 352–364, https://doi.org/10.1016/j.respol.2016.09. 003.

[46] M.J. Conyon, L. He, Firm performance and boardroom gender diversity: a quantile regression approach, J. Bus. Res. 79 (2017) 198–211, https://doi.org/10.1016/j. jbusres.2017.02.006.

[47] J.P. Dub´e, Z. Fang, N.M. Fong, X. Luo, Competitive Price targeting with smartphone coupons, Market. Sci. 36 (6) (2017) 944–975, https://doi.org 10.2139/ssrn. 2694320

[48] M. Ding, J.R. Hauser, S. Dong, et al., Unstructured direct elicitation of decision rules, J. Market. Res. 48 (2011), https://doi.org/10.1509/jmkr.48.1.116, 116–112.

[49] J.P. Eggers, M. Grajek, T. Kretschmer, Experience, consumers, and fit: disentangling performance implications of Preentry technological and market experience in 2G Mobile telephony, Organ. Sci. 31 (2) (2020) 245–265, https:// doi.org/10.1287/orsc.2019.1311

[50] S. Tong, X. Luo, B. Xu, Personalized mobile marketing strategies, J. Acad. Market. Sci, 48 (2020) 64–78. https://doi.org/10.1007/s11747-019-00693-3
