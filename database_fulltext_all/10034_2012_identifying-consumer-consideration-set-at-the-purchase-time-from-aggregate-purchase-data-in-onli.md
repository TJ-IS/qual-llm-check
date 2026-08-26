---
otero_id: 10034
otero_key: "4G4V4UW5"
title: "Identifying consumer consideration set at the purchase time from aggregate purchase data in online retailing"
authors: "Bin Gu; Prabhudev Konana; Hsuan-Wei Michelle Chen"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.02.015"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identifying consumer consideration set at the purchase time from aggregate purchase data in online retailing

Bin Gu <sup>a,</sup>⁎, Prabhudev Konana <sup>b</sup>, Hsuan-Wei Michelle Chen <sup>c</sup>

<sup>a</sup> Department of Information Systems, W. P. Carey School of Business, Arizona State University, P.O. Box 874606, Tempe, AZ 85287, USA

<sup>b</sup> Department of Information, Risk, and Operations Management, McCombs School of Business, The University of Texas at Austin, CBA 5.202, B6500, Austin, TX 78712, USA

<sup>c</sup> Department of Management Information Systems, College of Business, San Jose State University, 1 Washington Square, San Jose, CA 95192, USA

## a r t i c l e i n f o

Article history: Received 27 March 2010 Received in revised form 7 February 2012 Accepted 28 February 2012 Available online 7 March 2012

Keywords: Consideration set Consumer choice Information search Electronic commerce

## a b s t r a c t

Online retailers provide a substantial amount of product information to their customers. The information includes not only product features and customer reviews, but also information on alternative products that may better <sup>fi</sup>t a consumer's needs. The systematic provision of information on alternative products could have a signi<sup>fi</sup>cant impact on consumers' purchase decision process at online retailers. In this study, we analyze one aspect of the impact — the degree to which consumers consider multiple products at the purchase time. We leverage a popular feature provided by online retailers — “What Do Customers Ultimately Buy after Viewing This Item?” We show that information contained in this feature can be used to identify consumers' product consideration set and choice at the purchase time when combined with product sales data. The identi<sup>fi</sup>cation is exact in analyzing competition between two products. For competition involving three products, the identi<sup>fi</sup>- cation is exact under the assumption that consumer choice follows a discrete choice model. For competition involving more than three products, the information provides a lower bound of the percentage of consumers that consider only one product at the purchase time. We apply the model to 38,400 unique products from Amazon's Electronics category. The results show that more than 78% of consumers purchase a product without considering any other products on Amazon at the purchase time

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Research on electronic commerce has shown that information provided by online retailers, such as product recommendations and consumer reviews, has a signi<sup>fi</sup>cant impact on consumer product choice [8,10,12,23]. In particular, information provided by online retailers includes not only that pertaining to the product under consideration, but also information on alternative products that may better <sup>fi</sup>t a consumer's needs. This systematic provision of information on alternative products at the time of purchase could have an impact on consumers' purchase decision process. In this study, we analyze one aspect of the impact — the degree to which consumers consider multiple products at the purchase time.

Our approach differentiates from prior studies on consumer consideration set in two ways. First, we develop a new methodology to identify consumer consideration set at the purchase time from aggregate data provided by online retailers. Prior studies on consumer consideration set either require detailed individual level clickstream data or leverage individual level purchase data with potentially unrealistic assumptions on the underlying consumer information search behavior [2,24,25,27]. Our approach leverages a new type of aggregate data provided by online retailers and shows that it is feasible to identify consumer consideration sets using the aggregate data under fewer assumptions. Second, our analysis focuses on consumer consideration sets and choices at the purchase time.<sup>1</sup> While it is well known that consumers make purchase decisions in multiple stages, few studies have analyzed the degree to which consumers make product comparisons at the last minute before making purchase decisions. This question is particularly relevant in online retailing environment as consumers are constantly exposed to information on alternative products, such as those provided by context-sensitive display ads. Understanding the consumer choice process at the moment of purchase in such an environment could help businesses and retailers develop better real-time marketing strategies.

Our research is facilitated by the availability of an increasingly popular feature among online retailers — “What Do Customers Ultimately Buy After Viewing This Item?” For example, two of the largest online retailers, Amazon.com and Buy.com, offer this feature prominently on their product pages. We show that, using information from this feature and product sales data, we can exactly identify the size of consumer groups with different consideration sets when analyzing competition between two or three products, and obtain a lower bound on the percentage of consumers that consider no alternative products at the purchase time when analyzing competition involving more than three products.

We apply our model to 38,400 unique products collected from Amazon's Electronics category. We choose Amazon as our research context because it is one of the largest online retailers and has been studied extensively in prior literature [13,18,21]. The results show that more than 78% of the consumers do not consider any other products at the purchase time. The <sup>fi</sup>nding suggests that a majority of the consumers have made decisions before their visits for the purchase and they are not often affected by alternative product information at the purchase time.

The remainder of this paper proceeds as follows. In Section 2, we review the prior literature that relates to our research topic. In Section 3, we present the theories and methodologies to identify consumer consideration sets. We present our data and modeling results along with discussions in Sections 4 and 5, respectively. We conclude our paper in Section 6.

## 2. Literature review

This study is closely related to marketing literature on consumer consideration formation [17,25,27]. These studies have shown that product consideration set signi<sup>fi</sup>cantly in<sup>fl</sup>uences consumer choice. In particular, faced with cognitive limitations, complex choice tasks, and evaluation costs, consumers often resort to a phased decision process [14]. The phased consumer decision-making process involves two stages — consideration stage and choice stage. In the consideration stage, consumers choose a small set of products for evaluation. In the choice stage, consumers evaluate every product in the consideration set and purchase the one with the highest utility. A key challenge in research on the consideration stage is that product consideration is often not observable to researchers, especially in of<sup>fl</sup>ine settings. As a result, a signi<sup>fi</sup>cant amount of effort has been focused on identifying “whether the consideration stage … corresponds to a cognitive stage of consideration in the consumer's decision process, or if it is just a statistical artifact of the data.” [28]. The availability of online clickstream data helps answer the aforementioned question [24]. By analyzing what consumers have viewed and what they ultimately purchase, Moe (2006) [24] <sup>fi</sup>nds that consumers use different decision criteria for the consideration stage and the choice stage.

While clickstream data offers rich information on consumer behavior, such information is often not available to product manufacturers or competing retailers. Further, extracting useful information from clickstream data requires extensive effort in data collection and analysis. A number of studies have thus focused on inferring consumer consideration sets from non-clickstream data (e.g. scanner data). One challenge of such an approach is that researchers must impose potentially unrealistic assumptions to make inference on the underlying consumer consideration process. For example, Roberts and Lattin (1991) [27] and Andrews Srinivasan (1995) [2] assume that a product's probability of being considered is independent of a consumer's consideration of other products, an assumption is unlikely to hold in reality as products with similar characteristics are more likely to be considered together.

Our study extends the extant research on consumer consideration sets on two fronts. First, we show that consumer consideration sets at the purchase time can be identi<sup>fi</sup>ed using a new type of aggregate data provided by the online retailers with few assumptions on the underlying consumer consideration process. Second, prior studies on consumer consideration set have mainly focused on the initial consideration set formed by the consumers. Our analysis instead focuses on consumer consideration sets at the purchase time and identi<sup>fi</sup>es the degree to which consumers make product comparison at the last minute.

This study also contributes to a growing interest in electronic commerce investigating product variety and consumer purchase decisions [7]. The <sup>fi</sup>rst stream of related literature is concerned with the increased product variety introduced by online retailers [1,4,5,26]. These studies suggest that online retailers are able to carry a greater variety of products than their physical counterparts [4,5], thus, expanding the number of products considered by a consumer. In addition, the lower search costs facilitated by product information and consumer recommendation in digital commerce further help consumers discover niche products and expand product consideration [1,7]. Recent studies also <sup>fi</sup>nd that consumers often conduct information search through thirdparty infomediaries (e.g. CNET) before making purchase at an online retailer [16]. We complement this research stream by identifying the degree to which consumers compare multiple products at the time of purchase.

Our research also draws on the literature relating to the impact of growing electronic commerce on consumer behavior [6,30,31]. With the increase of marketing channels facilitated by the advancement of technologies, media, and advertising activities, consumers have often been overloaded with information. The limitation of human cognitive and perceptual capability, however, restricts the number of products that can be considered by a consumer. In particular, literature on consumer behavior <sup>fi</sup>nds that consumers can only hold seven, plus or minus two, chunks of product information, and sometimes variably less, due to short-term memory limitation [3]. The limits in consumers' memory capability force consumers to be more selective in product consideration and information processing [9,20,29]. It also motivates the development of a wide array of consumer decision aids and recommendation systems [19,22,32].

## 3. Theories and methodologies

## 3.1. Revealed preferences in online retailers

Online retailers provide a variety of product sales statistics to help consumers make better decisions. For example, Amazon provides the following statistics to their customers: 1) products “Frequently Bought Together;” 2) “What Do Customers Ultimately Buy After Viewing This Item;” 3) product sales ranks; 4) “Customers Who Bought This Item Also Bought;” and 5) customer reviews. Such statistics reveal consumer preferences in purchasing decisions, enabling researchers and practitioners to infer the underlying purchase process [15,26]. In this study, we show that two statistics — “What Do Customers Ultimately Buy After Viewing This Item” and product sales ranks — can be used to identify consumer consideration and choice at the purchase time.

Fig. 1 provides a screenshot of “What Do Customers Ultimately Buy After Viewing This Item”. The <sup>fi</sup>gure shows that Amazon provides the top 4 products ultimately bought by consumers after viewing a given product and the corresponding percentages of consumers who have done so. While Amazon never reveals the exact calculation of the percentages, discussions with industry insiders suggest that the percentages are calculated from consumer web sessions that result in purchases. Web sessions that do not result in purchases are not included in the calculation. Given this design, the percentages capture consumer decision making at the purchase time, i.e. the last stage of the decision process.

The percentages in Fig. 1 represent conditional probabilities of consumers purchasing product Y after they have viewed X. We show later that consumer consideration sets and their choices can be identi<sup>fi</sup>ed using these conditional probabilities and the sales data when analyzing competition between two or three products. Further, we show that the information provides a lower bound of the percentage of consumers who view only one product when analyzing competition among more than three products.

What Do Customers Ultimately Buy After Viewing This Item?

![](/api/attachments/4G4V4UW5/fulltext/images/a61c2f912ed081febc2bd03fcbd27ff9447ffbfd7a849169cf2445f5e8cad5d2.jpg)  
Fig. 1. An example of “What Do Customers Ultimately Buy After Viewing This Item?” on Amazon.com.

## 3.2. Competition between two products

Product competition often centers between two products that are similar in nature. In such cases, retailers and product manufacturers often focus on analyzing the competition between the two products while ignoring consumers who bought other products.

Consider a market with two products, X and Y. Each consumer purchases one and only one product.<sup>2</sup> Consumers make purchase decisions in two stages. In the Consideration Stage, they form a consideration set that could include one of the two products, or both. In the Choice Stage, they make purchase decisions. Given the assumption that the market contains two products, there exist three customer groups at the purchase time: (i) those who have considered only X, (ii) those who have considered only Y, and (iii) those who have considered both X and Y. We use N X <sup></sup>Y ; N XY<sup></sup> , and N XY to denote the ð Þ<sub>three groups respectively. To identify the size of each group, we note</sub> that Amazon provides the following information:

a. x — the number of consumers who purchased X (we use the lower case to indicate sales and the upper case to indicate views) as estimated from Amazon sales rank of product X

b. y — the number of consumers who purchased Y as estimated from Amazon sales rank of product Y

c. P(x|X) — percentage of customers who purchased product X after viewing X.

d. P(y|X) — percentage of customers who purchased product Y after viewing X.

e. P(x|Y) — percentage of customers who purchased product X after viewing Y.

f. P(y|Y) — percentage of customers who purchased product Y after viewing Y.

Given that the market has only two products and consumers purchase one and only one product, $\mathsf { P } ( \mathbf { x } | \mathbf { X } ) + \mathsf { P } ( \mathbf { y } | \mathbf { X } ) = 1$ and $\mathrm { P } ( \mathbf { x } | \mathrm { Y } ) +$ P(y|Y) = 1. This indicates that only two of the four conditional probabilities carry unique information.

We further note that the probability of purchasing a product after viewing the product can be expressed as a ratio of product sales over the sum of customer groups that have viewed the product. In particular,

$$
P (x | X) = \frac {x}{N (X \bar {Y}) + N (X Y)}.\tag{1}
$$

The equation suggests that the probability of consumers purchasing X after viewing X can be calculated as the sales of X divided by the sum of number of customers who have viewed only X and the number of customers who have viewed both X and Y. Similarly, we have

$$
P (y | Y) = \frac {y}{N (\bar {X} Y) + N (X Y)}\tag{2}
$$

Finally, we note that, since consumers purchase one and only one product, the total number of viewers must equal to the total number of customers.

$$
x + y = N (X \bar {Y}) + N (\bar {X} Y) + N (X Y)\tag{3}
$$

Eqs. (1)–(3) allow us to identify three different groups of consumers: those who viewed both X and Y, those who viewed X only and those who viewed Y only. It is also useful to note that P(y|X) and P(x|Y) are not included in Eqs. (1)–(3) because they are linear functions of P(x|X) and P(y|Y) respectively.

Given Eqs. (1)–(3), we can identify the size of each customer group:

$$
\begin{array}{l} N (X Y) = \frac {x}{p (x | X)} + \frac {y}{p (y | Y)} - x - y = \frac {p (y | X)}{p (x | X)} x + \frac {p (x | Y)}{p (y | Y)} y \\ N (X \bar {Y}) = x + y - \frac {y}{p (y | Y)} \\ N (\bar {X} Y) = x + y - \frac {x}{p (x | X)} \end{array}\tag{4}
$$

Intuitively, $\cdot { \frac { x } { p ( x | X ) } }$ identi<sup>fi</sup>es the total number of consumers who have viewed product X while $\frac { y } { p ( y | Y ) }$ identi<sup>fi</sup>es the total number of consumers who have viewed product Y. The number of consumers who have viewed both products is counted twice in the foregoing calculation. We can, thus, identify these consumers using the difference between the sum of the two and the total number of consumers. In the extreme case where every consumer views only one product, P(x|X) and P(y|Y) will be equal to 1 and N XY , N X <sup></sup>Y , N X Y<sup></sup>  will be equal to 0, x, and y, respectively.

We can also identify the consumer choice decision when they consider both products. To identify the choice process of those who viewed both products, we note that x customers who bought product X can be divided into two groups: those who viewed only product X and those who viewed both products X and Y. Since there are N X <sup></sup>Y  customers in the <sup>fi</sup>rst group, the second group contains x−N X <sup></sup>Y  customers. The choice probability of x among customers that viewed both products is thus

$$
P (x \mid \mathrm{XY}) = \frac {x - N (X \bar {Y})}{N (X Y)} = \frac {\frac {P (x \mid Y)}{P (y \mid Y)} y}{\frac {P (y \mid X)}{P (x \mid X)} x + \frac {P (x \mid Y)}{P (y \mid Y)} y}\tag{5}
$$

Fig. 2 illustrates our approach using sales rank and conditional probability data on two popular software products: Adobe Photoshop

## I. Information from Amazon

<table><tr><td>Viewed\Bought</td><td>Photoshop Element 9</td><td>Bundle 9</td><td>Sales Rank</td></tr><tr><td>Photoshop Element 9</td><td>93%</td><td>7%</td><td>3</td></tr><tr><td>Bundle 9</td><td>23%</td><td>77%</td><td>21</td></tr></table>

II. Derivation of Consumer Groups with Different Consideration Sets

i. Viewed both products $= { \frac { x } { P \left( x \mid X \right) } } + { \frac { y } { P \left( y \mid Y \right) } } - x - y = 2 6 4 . 0 3 ^ { 9 }$

ii. Viewed only Adobe Element $9 \ = x + y - { \frac { y } { P \left( y \mid Y \right) } } = 1 , 4 4 7 . 4 6$

iii. Viewed only Adobe Element 9 + Adobe Premier Elemen $9 =$

$$
N (\bar {X} Y) = x + y - \frac {x}{P (x \mid X)} = 3 6 3. 0 5.
$$

Probability of Viewing both Products Before Purchase = 12.73%.

III. Derivation of Consumer Choice

Probability of buying Adobe Photoshop Element 9 after viewing Both Product

$$
\frac {x - N (X \bar {Y})}{N (X Y)} = 54.63 \%.
$$

9We assume the following power law relationship between product sales and sales rank: Log Sales = 8.046 − 0.613 × Log SalesRank ([20])

Fig. 2. Illustration of consumer consideration and choice of two products.

Element 9 (PS 9) and Adobe Photoshop and Premiere Element 9 (Bundle 9). The former is a popular photo editing software for amateurs, while the latter is a bundled product that includes one copy of Adobe Photoshop Element 9 and one copy of Adobe Premiere Element 9, a popular video editing software. Data from Amazon indicates that fewer than 2% of consumers who viewed either of the products end up purchasing something else. So the competition is mainly between the two products at the purchase time. We, thus, rescale the data to remove consumers who ultimately bought other products and focus on consumers who bought either of the two products.<sup>3</sup> For illustration, we assume that the relationship between sales rank and sales is known. The analysis shows that only 13% of the consumers consider both products. The remaining 87% of consumers consider only one product at the purchase time. Among those who consider both products, 55% choose to purchase PS 9.

## 3.3. Competition among three products

To identify consumer choice and consideration set for more products, we note that there exist $2 ^ { \mathrm { n } } - 1$ consumer groups<sup>4</sup> for a market of n products given all the possible combinations of products for consideration sets. In addition, to exactly identify consumer choice within each consumer group, we need identi<sup>fi</sup>cation of $\begin{array} { r } { \sum _ { \mathrm { k } = 1 } ^ { \mathrm { n } } ( \mathrm { k } - 1 ) ( \mathrm { \frac { n } { k } } ) } \end{array}$ choice probabilities.<sup>5</sup> In total, $\sum \mathbf { \vec { k } } = 1 \mathbf { \vec { k } } ( \mathbf { \vec { k } } )$ variables need to be identi<sup>fi</sup>ed. Since Amazon provides $\mathtt { n } ^ { 2 }$ statistics,<sup>6</sup> such exact identi<sup>fi</sup>cation is only possible for ${ \mathfrak { n } } = 2 .$

The number of variables required for the choice process can be significantly reduced if we use a discrete choice model to model the consumer choice process. The model assumes that each product has a <sup>fi</sup>xed utility in all consumer groups and a consumer's probability of choice of the product is equal to the ratio of the product utility over the sum of the utilities of all products considered by the consumer. This assumption reduces the num ber of variables required for the choice process to $( \mathrm { n } - 1 )$ . In total, $2 ^ { \mathfrak { n } } + \mathfrak { n }$ −2 variables need to be identi<sup>fi</sup>ed in this case. Since Amazon provides $\mathtt { n } ^ { 2 }$ statistics, the identi<sup>fi</sup>cation is feasible for $\mathtt { n } = 3$

Speci<sup>fi</sup>cally, we use the following nine equations. The <sup>fi</sup>rst set of three equations identi<sup>fi</sup>es the conditional probability of purchasing a product after viewing the product. The second set of three equations identi<sup>fi</sup>es the conditional probability of purchasing a different product after viewing a given product. The <sup>fi</sup>nal set of three equations identi<sup>fi</sup>es the ultimate sales for each product. It is useful to note that the second and third sets of equations are non-linear and thus require numeric solution.

$$
\begin{array}{l} P (x | X) = \frac {x}{N (X \bar {Y} \bar {Z}) + N (X Y \bar {Z}) + N (X \bar {Y} Z) + N (X Y Z)} \\ P (y | Y) = \frac {y}{N (\bar {X} Y \bar {Z}) + N (X Y \bar {Z}) + N (\bar {X} Y Z) + N (X Y Z)} \\ P (z | Z) = \frac {z}{N (\bar {X} \bar {Y} Z) + N (X \bar {Y} Z) + N (\bar {X} Y Z) + N (X Y Z)} \\ P (y | X) = \frac {\frac {u _ {y}}{\left(u _ {x} + u _ {y}\right)} N (X Y \bar {Z}) + \frac {u _ {y}}{\left(u _ {x} + u _ {y} + u _ {z}\right)} N (X Y Z)}{N (X \bar {Y} \bar {Z}) + N (X Y \bar {Z}) + N (X \bar {Y} Z) + N (X Y Z)} \\ P (x | Y) = \frac {\frac {u _ {x}}{\left(u _ {x} + u _ {y}\right)} N (X Y \bar {Z}) + \frac {u _ {x}}{\left(u _ {x} + u _ {y} + u _ {z}\right)} N (X Y Z)}{N (\bar {X} Y \bar {Z}) + N (X Y \bar {Z}) + N (\bar {X} Y Z) + N (X Y Z)} \\ P (x | Z) = \frac {\frac {u _ {x}}{\left(u _ {x} + u _ {z}\right)} N (X \bar {Y} Z) + \frac {u _ {z}}{\left(u _ {x} + u _ {y} + u _ {z}\right)} N (X Y Z)}{N (\bar {X} \bar {Y} Z) + N (X \bar {Y} Z) + N (\bar {X} Y Z) + N (X Y Z)} \\ x = N (X \bar {Y} \bar {Z}) + \frac {u _ {x}}{\left(u _ {x} + u _ {y}\right)} N (X Y \bar {Z}) + \frac {u _ {x}}{\left(u _ {x} + u _ {z}\right)} N (X \bar {Y} Z) \\ \quad + \frac {u _ {x}}{\left(u _ {x} + u _ {y} + u _ {z}\right)} N (X Y Z) \\ y = N (X \bar {Y} \bar {Z}) + \frac {u _ {y}}{\left(u _ {x} + u _ {y}\right)} N (X Y \bar {Z}) + \frac {u _ {y}}{\left(u _ {y} + u _ {z}\right)} N (\bar {X} Y Z) \\ \quad + \frac {u _ {y}}{\left(u _ {x} + u _ {y} + u _ {z}\right)} N (X Y Z) \\ z = N (X \bar {Y} \bar {Z}) + \frac {u _ {z}}{\left(u _ {x} + u _ {z}\right)} N (X \bar {Y} Z) + \frac {u _ {z}}{\left(u _ {y} + u _ {z}\right)} N (\bar {X} Y Z) \\ \quad + \frac {u _ {z}}{\left(u _ {x} + u _ {y} + u _ {z}\right)} N (X Y Z) \end{array}
$$

To identify consumer consideration and choice process for three products, we need the identi<sup>fi</sup>cation of 9 parameters — 7 parameters for consumer groups based on their consideration $\mathsf { s e t } \mathsf { s } ^ { 7 }$ and 2 parameters for the utility of the three products.<sup>8</sup> Amazon provides 9 conditional purchase probabilities for three products and 3 data points on product sales. The 9 conditional purchase probabilities, however, are not fully independent. As in the case of two-product market, the sum of conditional purchase probabilities after viewing a given product always equals 1. As such, only 6 of the conditional purchase probabilities carry unique information. Combining the 6 conditional purchase probabilities with the 3 data points on product sales, we can exactly identify the 9 parameters for the consumer consideration and choice process of three products.

Fig. 3 illustrates our approach by extending the earlier twoproduct example to three software products: Adobe Photoshop Element 9 (PS 9), Adobe Photoshop and Premiere Element 9 (Bundle 9), and Adobe Premier Element (PR 9). The data from Amazon

6

I. Information from Amazon

<table><tr><td>Bought Viewed</td><td>Photoshop Element 9</td><td>Photoshop/Premiere Element Bundle 9</td><td>Premiere Element 9</td><td>Sales Rank</td></tr><tr><td>Photoshop Element 9</td><td>92%</td><td>7%</td><td>1%</td><td>3</td></tr><tr><td>Photoshop/Premiere Element Bundle 9</td><td>23%</td><td>76%</td><td>1%</td><td>21</td></tr><tr><td>Premiere Element 9</td><td>34%</td><td>16%</td><td>50%</td><td>135</td></tr></table>

II. Derivation of Consumer Groups with Different Consideration Sets

The derivation is based on numeric solution to the nine non-linear equations outlined in Section 3.3.

i. Viewed Only Adobe Photoshop Element 9 = 1,346.73

ii. Viewed Only Adobe Photoshop / Premier Element Bundle 9 = 312.36

iii. Viewed Only Adobe Premier Element 9 = 136.78

iv. Viewed Both Adobe Photoshop Element 9 and Adobe Photoshop/Premier Element Bundle 9 = 267.23

v. Viewed Both Adobe Photoshop Element 9 and Adobe Premier Element 9 = 116.13

vi. Viewed Both Adobe Photoshop/Premier Element Bundle 9 and Adobe Premier Element 9 = 55.73

vii. Viewed All Three Products = 0

viii. The probability of PS 9 being considered is 78%.

ix. The probability of Bundle 9 being considered is 29%

x. The probability of PR 9 being considered is 14%.

III. Derivation of Consumer Choice

i. Utility of PS 9 = 0.517

ii. Utility of Bundle 9 = 0.428

iii. Utility of PR 9 = 0.055

The above estimated utilities suggest the following choice probability:

1) Probability of buying PS 9 after viewing both PS 9 and Bundle 9 is 54.68%

2) Probability of buying PS 9 after viewing both PS 9 and PR 9 is 90.36%.

3) Probability of buying Bundle 9 after viewing both Bundle 9 and PR 9 is 88.60%.

Fig. 3. Illustration of consumer consideration and choice of three products.

shows that while few customers who have viewed PS 9 or Bundle 9 choose PR 9, the reverse is not true. Half of the customers who viewed PR 9 end up with purchasing PS 9 or Bundle 9.

Our analysis again shows that few consumers consider more than one product at the purchase time. The result indicates that 80.35% of the consumers consider only one product at the purchase time. The result also indicates PR 9 has a much lower utility compared with that for PS 9 or Bundle 9.

## 3.4. Competition among multiple products

To consider competition among more than three products, we use $\mathrm { D } _ { \mathrm { i } }$ to denote the action of viewing product i and d to denote the num ber of consumers who purchase product i. Amazon provides the following information:

a. d<sub>i</sub> — the number of consumers who purchased product i, for all i. b. $\mathrm { P ( d _ { j } | D _ { i } ) }$ — the probability of consumers purchasing j after viewing product i, for all i and j.

We again note that $\begin{array} { r } { \sum _ { \mathrm { j } } \mathrm { P } ( \mathrm { d } _ { \mathrm { j } } | \mathrm { D } _ { i } ) = 1 } \end{array}$ , for all i. This condition indicates that while (b) provides a total number of $\mathtt { n } ^ { 2 }$ statistics, only n(n−1) of them contain unique information.

Given that the conditional probability is between each pair of products, but consumers may consider more than two products in this setting, we cannot exactly identify the size of all possible consideration sets. However, we show now that the aforementioned information is suf<sup>fi</sup>cient to provide a lower bound of the percentage of consumers who consider no alternative products at the purchase time.

Note that the conditional probability of purchasing a product after viewing the product can be expressed as follows:

$$
P (d _ {\mathrm{i}} | D _ {\mathrm{i}}) = \frac {d _ {\mathrm{i}}}{N \left(\cap_ {m \in \{i \}} D _ {m} \cap_ {n \in I - \{i \}} \overline {{D _ {n}}}\right) + \sum_ {j \neq i} N \left(\cap_ {m \in \{i , j \}} D _ {m} \cap_ {n \in I - \{i , j \}} \overline {{D _ {n}}}\right) + \dots + N (\cap_ {m \in I} D _ {m})}\tag{7}
$$

In Eq. (7), $N \big ( \cap _ { m \in \{ i \} } D _ { m } \cap _ { n \in I - \{ i \} } \overline { { D _ { n } } } \big )$ refers to the consumers who <sup>f g -f g</sup>only view product i at the purchase time with I referring to the entire product set. ${ \cal N } \big ( \cap _ { m \in \{ i , j \} } D _ { m } \cap _ { n \in I - \{ i , j \} } \overline { { { D _ { n } } } } \big )$ refers to the consumers who <sup>f g f g</sup>only view products i and j at the purchase time and $\Nu ( \cap _ { m \in I } D _ { m } )$ refers to the consumers who view all the products at the purchase time. Swapping the LHS with the denominator in the RHS, we have

$$
\begin{array}{l} N \Big (\cap_ {m \in \{i \}} D _ {m} \cap_ {n \in I - \{i \}} \overline {{D _ {n}}} \Big) + \sum_ {j \neq i} N \Big (\cap_ {m \in \{i, j \}} D _ {m} \cap_ {n \in I - \{i, j \}} \overline {{D _ {n}}} \Big) \\ + \dots + N (\cap_ {m \in I} D _ {m}) = \frac {d _ {\mathrm{i}}}{p (d _ {\mathrm{i}} | D _ {\mathrm{i}})} \end{array}\tag{8}
$$

Summing Eq. (8) over all i, we have

$$
\begin{array}{l} \sum_ {i} N \Big (\cap_ {m \in \{i \}} D _ {m} \cap_ {n \in I - \{i \}} \overline {{D _ {n}}} \Big) + \sum_ {i} \sum_ {j \neq i} N \Big (\cap_ {m \in \{i j \}} D _ {m} \cap_ {n \in I - \{i j \}} \overline {{D _ {n}}} \Big) \\ + \dots + \sum_ {i} N (\cap_ {m \in I} D _ {m}) = \sum_ {i} \frac {d _ {i}}{p (d _ {i} | D _ {i})} \end{array}\tag{9}
$$

Note that

$$
\sum_ {i} N (\cap_ {m \in I} D _ {m}) = n N (\cap_ {m \in I} D _ {m})\tag{10}
$$

$$
\sum_ {i} \sum_ {j \neq i} N \left(\cap_ {m \in \{i, j \}} D _ {m} \cap_ {n \in I - \{i, j \}} \overline {{D _ {n}}}\right) = 2 \sum_ {\text { all }} i <   j N \left(\cap_ {m \in \{i, j \}} D _ {m} \cap_ {n \in I - \{i, j \}} \overline {{D _ {n}}}\right)\tag{11}
$$

We have

$$
\begin{array}{l} \sum_ {i} N \Big (\cap_ {m \in \{i \}} D _ {m} \cap_ {n \in I - \{i \}} \overline {{D _ {n}}} \Big) + 2 \sum_ {\text { all   } i <   j} N \Big (\cap_ {m \in \{i, j \}} D _ {m} \cap_ {n \in I - \{i, j \}} \overline {{D _ {n}}} \Big) \\ + \dots + n N (\cap_ {m \in I} D _ {m}) = \sum_ {i} \frac {d _ {i}}{p (d _ {i} | D _ {i})} \end{array}\tag{12}
$$

We further note that the sum of all consumer groups with different consideration sets equals the number of total consumers, i.e.

$$
\begin{array}{l} \sum_ {\mathrm{i}} N \Big (\cap_ {m \in \{i \}} D _ {m} \cap_ {n \in I - \{i \}} \overline {{D _ {n}}} \Big) + \sum_ {\text { all   } i <   j} N \Big (\cap_ {m \in \{i, j \}} D _ {m} \cap_ {n \in I - \{i, j \}} \overline {{D _ {n}}} \Big) \\ + \dots + N (\cap_ {m \in I} D _ {m}) = \sum_ {\mathrm{i}} d _ {\mathrm{i}} \end{array}\tag{13}
$$

Subtracting Eq. (13) from Eq. (12), we have

$$
\begin{array}{l} \sum_ {\text { alli } <   j} N \left(\cap_ {m \in \{i, j \}} D _ {m} \cap_ {n \in I - \{i, j \}} \overline {{D _ {n}}}\right) + \dots + (n - 1) N (\cap_ {m \in I} D _ {m}) \\ = \sum_ {i} \left(\frac {d _ {i}}{p (d _ {i} | D _ {i})} - d _ {i}\right) \end{array}\tag{14}
$$

Table 1 Table 1

Note that the total number of customers who consider more than one product is:

$$
\begin{array}{l} \sum_ {\text { all   } i <   j} N \Big (\cap_ {m \in \{i, j \}} D _ {m} \cap_ {n \in I - \{i, j \}} \overline {{D _ {n}}} \Big) + \dots + N (\cap_ {m \in I} D _ {m}) <   \\ \sum_ {\text { all   } i <   j} N \Big (\cap_ {m \in \{i, j \}} D _ {m} \cap_ {n \in I - \{i, j \}} \overline {{D _ {n}}} \Big) + \dots + (n - 1) N (\cap_ {m \in I} D _ {m}) = \sum_ {\mathrm{i}} \left(\frac {d _ {\mathrm{i}}}{p (d _ {\mathrm{i}} | D _ {\mathrm{i}})} - d _ {\mathrm{i}}\right) \end{array}\tag{15}
$$

$\sum _ { \mathrm { i } } \left( \frac { d _ { \mathrm { i } } } { p ( d _ { \mathrm { i } } | D _ { \mathrm { i } } ) } { - } d _ { \mathrm { i } } \right)$ , thus, identi<sup>fi</sup>es the upper bound of the number of customers who consider more than one product. We can therefore express the lower bound of consumers who consider no alternative product as $\begin{array} { r } { \sum _ { \mathrm { i } } \Bigl ( 2 d _ { \mathrm { i } } - \frac { d _ { \mathrm { i } } } { p ( d _ { \mathrm { i } } | D _ { \mathrm { i } } ) } \Bigr ) } \end{array}$ . This bound is tight if few customers consider three products or more at the purchase time. In addition, one advantage of this bound is that it is derived without any assumption on the consideration process.

Fig. 4 uses our earlier example of three Adobe products to identify the lower bound of customers who consider no alternative products at purchase time. The result shows that the bound is 80.03%, very close to the percentage (80.35%) identi<sup>fi</sup>ed in Fig. 3.

## 4. Data and empirical results

## 4.1. Data

We collect data from Amazon's “What Do Customers Ultimately Buy After Viewing This Item?” (see Fig. 1). The data are extracted using automated scripts to access and parse HTML pages from the retailer. For each product, Amazon provides a list of top four products that consumers purchase after viewing the focal product along with their respective purchase probability. In most cases, the same set of four products appears on each other's ultimate purchase list. In a few cases, the products in the ultimate purchase lists do not overlap perfectly, in which case we construct the four-product group based on the procedure outlined in Appendix A. In total, we collected 38,400 unique products under Electronics category in 9600 product groups.

Our data were collected on May 15th, 2008. Table 1 lists summary statistics for our data. In Table 1, C1 refers to the conditional purchase percentage for the most purchased product after viewing the product page. In most cases, the most purchased product is the product being viewed. Similarly, C2 refers to the conditional purchase percentage of

I. Information from Amazon

<table><tr><td>Bought Viewed</td><td>Photoshop Element 9</td><td>Photoshop/Premiere Element Bundle 9</td><td>Premiere Element 9</td><td>Sales Rank</td></tr><tr><td>Photoshop Element 9</td><td>92%</td><td>7%</td><td>1%</td><td>3</td></tr><tr><td>Photoshop/Premiere Element Bundle 9</td><td>23%</td><td>76%</td><td>1%</td><td>21</td></tr><tr><td>Premiere Element 9</td><td>34%</td><td>16%</td><td>50%</td><td>135</td></tr></table>

II. Derivation of Lower Bound of Consumers Who Consider No Alterative Products

i. Lower Bound of Customers Who Consider No Alterative at Purchase Time = ∑2di − d =1.783.65 P(di1Di)

ii. Percentage of Customers Who Consider No Alterative at Purchase Time =

$$
\frac {\sum_ {i} \left(2 d _ {i} - \frac {d _ {i}}{P \left(d _ {i} \mid D _ {i}\right)}\right)}{\sum_ {i} \left(d _ {i}\right)} = 80.03 \%
$$

Fig. 4. Illustration of calculation of lower bound of percentage of consumers who consider no alterative products at purchase time.  
Summary statistics of data.

<table><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>Std dev</td><td>Min</td><td>Max</td></tr><tr><td>Sales rank</td><td>38,400</td><td>345.49</td><td>3337.75</td><td>1</td><td>249,242</td></tr><tr><td>Rank 1 purchase propensity (C1)</td><td>38,400</td><td>69.90%</td><td>0.14</td><td>25%</td><td>99%</td></tr><tr><td>Rank 2 purchase propensity (C2)</td><td>38,400</td><td>12.28%</td><td>0.11</td><td>0.5%</td><td>45%</td></tr><tr><td>Rank 3 purchase propensity (C3)</td><td>38,400</td><td>5.42%</td><td>0.05</td><td>0.5%</td><td>32%</td></tr><tr><td>Rank 4 purchase propensity (C4)</td><td>38,400</td><td>3.28%</td><td>0.03</td><td>0.5%</td><td>17%</td></tr></table>

the second most purchased product after viewing the product page. C3 and C4 follow the same rationales for the third and the fourth most purchased products, respectively. The table shows that over 69% of consumers purchase the <sup>fi</sup>rst product and less than 10% of customers purchase the third or fourth product.

## 4.2. Consideration set

We start our analysis by estimating the lower bound of the number of customers who view no alterative products. We conduct the aforementioned analysis for each group of four products. Fig. 5 shows the mean, standard deviation, and the histogram of the estimation. The results indicate that the average lower bound is 78% across all product groups. Given that the statistic is the lower bound, the actual percentage of customers who viewed no alternative products is likely to be higher. The histogram further shows signi<sup>fi</sup>cant variations across product groups. For some product groups, over 90% of consumers made purchase without viewing any other products; while for other product groups, most consumers view alternative products at the purchase time.

## 4.3. Consumer choice

Besides estimating consumer consideration sets at the purchase time, it is also useful to understand the consumer choice process when they consider more than one product. Prior research has found that consumers use different criteria for the consideration stage and for the choice stage [24]. The <sup>fi</sup>nding indicates that products offering high utilities might not be considered by many consumers. Our approach provides identi<sup>fi</sup>cation of consumer choice when the

## A: Summary Statistics

<table><tr><td>Mean</td><td>Std Dev</td><td>Min</td><td>Max</td></tr><tr><td>78.21%</td><td>21.73%</td><td>0.00%</td><td>98.46%</td></tr></table>

## B: Histogram

Distribution of Lower Bound of Consumers Who Viewed Nc Alterative Products at Purchase Time  
![](/api/attachments/4G4V4UW5/fulltext/images/1731ff517ed737b41a7bfb42543ba716ef1dd03b54140bbeff409c336480ded4.jpg)  
Fig. 5. Descriptive statistics on lower bound of consumers who viewed no alternative products at purchase time

identi<sup>fi</sup>cation of consideration sets is exact (i.e. in the case of two or three products). Given that Table 1 shows that most of the consideration is between the two leading products in each group, we choose to analyze consumer choices between the two leading products using the approach outlined in Section 3.2.

Panel A in Fig. 6 shows the summary statistics of the percentage of consumers who considered a given product in each group and the percentage of consumers who purchase a given product after viewing both products. The average consideration probability is 57%. Note that if each consumer considers only one product, the average consideration probability in a two-product group will be 50%, while if every consumer considers both products, the probability will be 100%. The result provides another indication that few consumers consider more than one product at the purchase time. Panel A also shows that there is a negative correlation between a product's consideration probability and its choice probability when being considered along with an alternative product. The negative correlation suggests <sup>fi</sup>rms may differ in their business strategies — some <sup>fi</sup>rms focus on increasing the probability of their products being considered, while other <sup>fi</sup>rms focus on improving product value proposition relatively to its competitors [24]. Panel B of Fig. 6 shows the scatterplot of the relationship between consideration probability and choice probability. The x-axis represents the probability of a product being considered and the y-axis represents the probability of the product being chosen if compared side by side against the alternative product. The plot indicates that the relationship between the two probabilities vary substantially. For some products, their consideration probability is signi<sup>fi</sup>cantly higher than the choice probability, indicating that the product sales are mainly driven by them being frequently considered by consumers. For other products, their choice probability is signi<sup>fi</sup>- cantly higher than the consideration probability, indicating that, while these products are less known among consumers, they offers higher values compared to the competitors.

4.4. The effects of consideration probability and choice probability on purchase

To compare the relative importance of consideration and choice on product sales, we note that there is a non-linear relationship

Table 2  
A: Summary Statistics and Correlation

<table><tr><td>Variable</td><td>Mean</td><td>Std Dev</td><td>Min</td><td>Max</td><td>Consideration Probability</td><td>Choice Probability</td></tr><tr><td>Consideration Probability</td><td>57.26%</td><td>28.09%</td><td>0.02%</td><td>99.94%</td><td>1.00</td><td>-0.22</td></tr><tr><td>Choice Probability</td><td>50.00%</td><td>34.91%</td><td>0.00%</td><td>99.94%</td><td>-0.22</td><td>1.00</td></tr></table>

## B: Scatter Plot

![](/api/attachments/4G4V4UW5/fulltext/images/84aa4bba32b1065fdb5a3b2d9efa855b45992a269897c28e9b27e945129ae63f.jpg)  
Fig. 6. Scatter plot of consideration probability vs. Choice probability

among consideration, choice, and product sales. As such, we cannot use linear regressions or ANOVA for the analysis. Instead, to demonstrate the effects of consideration and choice on product purchase, we do so separately for the two effects. We <sup>fi</sup>rst assess the in<sup>fl</sup>uence of consideration by removing the in<sup>fl</sup>uence of choice with the assumption that consumers have equal probability of choosing either product in the consideration set. We then calculate the predicted product sales and report the summary statistics of predicted product sales and its correlation with actual sales in Table 2. Since the percentage of variation expected in product sales equals to the square of the correlation, the result suggests that consideration alone explains 98% of the variation. We conduct the same analysis for the choice probability by assuming consumers give equal consideration to products. The result in Table 2 suggests that choice alone explains only 8.4% of the variation.

## 5. Conclusions

In this study, we developed a methodology to identify consumer consideration and choice at the product purchase time. We show that most consumers consider only one product at the purchase time. There are two possible explanations of the result: consumers either do not conduct product search before purchase, or they engage in pre-purchase information search and product comparison well before making the <sup>fi</sup>nal purchase. Given that our analysis is conducted in the electronic category where products are relatively expensive, we believe the second explanation is likely to be true. This <sup>fi</sup>nding is also consistent with recent studies that suggest consumers conduct information search on third-party infomediaries before making product purchase at online retailers [15].

This research shows that that most consumers narrowed down their consideration set to one product at the time of <sup>fi</sup>nal purchase and they are not in<sup>fl</sup>uenced by information on alternative products in the purchase process. Our analysis also reveals that the majority of variations in product sales can be explained by heterogeneity in consumer consideration. Product utility has a limited impact.

Our analysis has a number of implications for product, price, and marketing strategies for retailers and manufacturers. The <sup>fi</sup>nding that many consumers consider only one product when making the <sup>fi</sup>nal product purchase suggests that the provision of information on alternative products has limited in<sup>fl</sup>uence on consumer purchase decision in late stages. Our <sup>fi</sup>ndings also highlight the value of marketing effort to ensure products being considered by consumers.

By developing a model to measure product consideration and choice using only publicly available aggregate purchase statistics provided by online retailers, we also contribute to the literature from a methodological perspective. While prior two-stage consideration choice models require detailed individual level data and often imposes signi<sup>fi</sup>cant restrictions on the underlying consumer behavior, we develop a methodology that shows consumer consideration and choice can be identi<sup>fi</sup>ed using a new type of aggregated information from online retailers with few assumptions on the underlying consumer behavior. This is particularly important for electronic commerce research given that clickstream data are not generally accessible.

Predicted sales based on consideration probability and choice probability.

<table><tr><td>Variable</td><td>Mean</td><td>Std dev</td><td>Min</td><td>Max</td><td>Corr with actual sales</td></tr><tr><td>Predicted sales based on consideration probability</td><td>865.75</td><td>945.17</td><td>0</td><td>4234</td><td>0.99</td></tr><tr><td>Predicted sales based on choice probability</td><td>681.50</td><td>837.30</td><td>1.13</td><td>5894</td><td>0.29</td></tr></table>

Our study also presents a number of future research opportunities. First, we note that information on conditional product sales after viewing the focal product not only provides researchers an opportunity to identify the underlying consumer consideration set at the purchase time, but also provides information that could in<sup>fl</sup>uence the consumer decision process itself. For example, if a retailer shows that most consumers purchase other products after viewing the focus product, it could have a signi<sup>fi</sup>cant impact on consumers' purchase decisions. Therefore, consumer consideration process is a dynamic process in<sup>fl</sup>uenced by prior consumer decisions. It will be valuable for future studies to model the dynamic aspect of the process [11]. Second, our methodology can only be used to identify consumer consideration of substitute products at the purchase time. In reality, consumer purchases not only substitute products but also complementary products. For example, consumers who bought cameras may also need battery, lenses, and memory card to complement the camera purchase. Online retailers such as Amazon provides a substantial amount of information on complementary products as well and it will be valuable to study how consumers form consideration set and make product choice for complementary products [12] and how online information in-<sup>fl</sup>uences the process.

## Acknowledgement

We thank seminar participants at the 2011 International Conference on Information Systems (ICIS) for their valuable comments and suggestions. Prabhudev Konana acknowledges support from the National Science Foundation's Information Technology Research Grant IIS-0218988. All errors remain ours.

## Appendix A. Construction of four-product groups

1. For each product, Amazon identi<sup>fi</sup>es a list of top four products that consumers purchase after viewing the focal product (for parsimony, the list is called “ultimate purchase list” thereafter). Technically, it is possible for the focal product not to make to the list. In practice, the focal product is always one of the four products on the list.

2. For each of the other three products, we visit its product page and obtain its ultimate purchase list.

3. If the product sets of the four ultimate purchase lists are the same, the four products on the lists form a four-product group.

4. If the product sets of the four ultimate purchase lists are not the same, we identify the four products that appear most frequently on the four lists as the four-product group. We then take the following two steps to adjust the conditional purchase probability:

a. If a product (say A) does not appear on the ultimate purchase list of another product (say B), we estimate the conditional purchase probability of purchasing A after viewing B as: $\begin{array} { r } { P ( A | B ) = 1 - \sum _ { x \in \ B { \ r { \mathrm { B } } ^ { ' } \mathrm { { s } } } \ \operatorname* { l i s t } } P ( x | B ) } \end{array}$ . Please note that our underlying assumption is that all the unreported sales after viewing B are attributed to product A. This assumption is deliberately biased towards a larger consideration set since our goal is to identify the lower bound. It is also useful to note that P(A|B) is typically very small, thus our assumption has relatively little impact on the estimation of the lower bound. To test the robustness of our approach, we also conduct analysis with the assumption of $\mathrm { P } ( { \boldsymbol { \mathrm { A } } } | \mathrm { B } ) = 0$ . The results are qualitatively the same.

b. If a product (say E) appears on the ultimate purchase list of another product (say B) but is not in the four-product group, it is necessary to rescale purchase probabilities to <sup>fi</sup>t our model, which assumes that consumers have purchased one of the four products. The rescaling is straightforward. To remove all the consumers who purchase E after viewing B and focus on only consumers who purchase products in the product group, we divide each conditional purchase probability P(x|B) by (1−P(E|B)).

## References

[1] C. Anderson, The Long Tail, Hyperion, New York, 2006.

[2] R.L. Andrews, T.C. Srinivasan, Studying consideration effects in empirical choice models using scanner panel data, Journal of Marketing Research 32 (1) (1995) 30–41.

[3] A.D. Baddeley, Is working memory still working? American Psychologist 56 (11) (2001) 851–864

[4] E. Brynjolfsson, Y.J. Hu, M.D. Smith, Consumer surplus in the digital economy: estimating the value of increased product variety at online booksellers, Manage ment Science 49 (11) (2003) 1580–1596.

[5] E. Brynjolfsson, Y.J. Hu, M.D. Smith, From niches to riches: the anatomy of the long tail, Sloan Management Review 47 (4) (2006) 67–71.

[6] P.-Y. Chen, L.M. Hitt, Measuring switching costs and the determinants of consum er retention in internet-enabled businesses: a study of the online brokerage in dustry, Information Systems Research 13 (3) (2002) 255–274.

[7] E.K. Clemons, G.G. Gao, L.M. Hitt, When online reviews meet hyperdifferentiation Journal of Management Information Systems 23 (2) (2006) 149–171.

[8] C. Dellarocus, Strategic manipulation of internet opinion forums: implications for consumers and <sup>fi</sup>rms, Management Science 52 (10) (2006) 1577–1593.

[9] P.M. DeMarzo, D. Vayanos, J. Zwiebel, Persuasion bias, social in<sup>fl</sup>uence, and unidi mensional opinions, Quarterly Journal of Economics 118 (3) (2003) 909–968

[10] W. Duan, B. Gu, A. Whinston, The dynamics of online word-of-mouth and product sales — an empirical investigation of the movie industry, Journal of Retailing 84 (2) (2008) 233–242.

[11] W. Duan, B. Gu, A. Whinston, Informational cascades and software adoption on the internet: an empirical investigation, MIS Quarterly 33 (1) (2009) 23–48.

[12] D.M. Fleder, K. Hosanagar, Blockbuster culture's next rise or fall: the impact of recommender systems on sales diversity, Management Science 55 (5) (2009) 697–712.

[13] R. Gar<sup>fi</sup>nkel, R. Gopal, B. Pathak, F. Yin, Shopbot 2.0: integrating recommendations and promotions with comparison shopping, Decision Support Systems 46 (1) (2008) 61–69.

[14] D.H. Gensch, A two-stage disaggregate attribute choice model, Marketing Science 6 (3) (1987) 223–239.

[15] A. Ghose, M.D. Smith, R. Telang, Internet exchanges for used books: an empirical analysis of product cannibalization and welfare impact, Information Systems Research 17 (1) (2006) 3-19

[16] B. Gu, J. Park, P. Konana, The impact of external word-of-mouth sources on retailer sales for high involvement products, Information Systems Research 23 (1) (2012) 182–196.

[17] G. Häubl, V. Trifts, Consumer decision making in online shopping environment: the effects of interactive decision aids, Marketing Science 19 (1) (2002) 4–21.

[18] N. Hu, L. Liu, V. Sambamurthy, Fraud detection in online consumer reviews, Decision Support Systems 50 (3) (2011) 614–626.

[19] Y. Jiang, J. Shang, Y. Liu, Maximizing customer satisfaction through an online rec ommendation system: a novel associative classi<sup>fi</sup>cation model, Decision Support Systems 48 (3) (2010) 470–479.

[20] Q. Jones, G. Ravid, S. Rafaeli, Information overload and the message dynamics of online interaction spaces: a theoretical model and empirical exploration, Information Systems Research 15 (2)(2004) 194–210

[21] J. Lee, J.-N. Lee, H. Shin, The long tail or the short tail: the category-speci<sup>fi</sup>c impact of eWOM on sales distribution, Decision Support Systems 51 (3) (2011) 466–479.

[22] T.-P. Liang, Recommendation systems for decision support: an editorial introduction, Decision Support Systems 45 (3) (2008) 385–386.

[23] J.G. Lynch, D. Ariely, Wine online: search costs affect competition on price, quality, and distribution, Marketing Science 19 (1) (2000) 83–103.

[24] W. Moe, An empirical two-stage choice model with varying decision rules applied to internet clickstream data, Journal of Marketing Research 43 (2006) 680–692.

[25] P. Nedungadi, Recall and consumer consideration sets: in<sup>fl</sup>uencing choice without altering brand evaluations, Journal of Consumer Research 17 (12) (1990) 263-276

[26] G. Ostreicher-Singer, A. Sundararajan, Recommendation networks and the long tail of electronic commerce, MIS Quarterly 36 (1) (2012) 65–83.

[27] J.H. Roberts, J.M. Lattin, Development and testing of a model of consideration set composition, Journal of Marketing Research 28 (11) (1991) 429–440

[28] J.H. Roberts, J.M. Lattin, Consideration: review of research and prospects for future insights, Journal of Marketing Research 34 (3) (1997) 406–410.

[29] A.D. Shocker, M. Ben-Akiva, B. Boccara, P. Nedungadi, Consideration set in<sup>fl</sup>uences on consumer decision-making and choice: issues, models, and suggestions, Marketing Letters 2 (3) (1991) 181–197

[30] M. Smith, The impact of shopbots on electronic markets, Journal of the Academy of Marketing Science 30 (4) (2002) 442–450

[31] M. Smith, E. Brynjolfsson, Customer decision making at an internet shopbot: brand still matters The Journal of Industrial Economics 49 (4) (2001) 541–558.

[32] W.-K. Tan, C.-H. Tan, H.-H. Teo, Consumer-based decision aid that explains which to buy: decision con<sup>fi</sup>rmation or overcon<sup>fi</sup>dence bias? Decision Support Systems 53 (1) (2012) 127–141.

![](/api/attachments/4G4V4UW5/fulltext/images/63177d1695863e641bf3793d181cb280b00f9249921dcfddca0e06213b71f364.jpg)

Dr. Bin Gu is an associate professor at the W. P. Carey School of Business, Arizona State University. He received his Ph.D. from the Wharton School, University of Pennsylvania. His research focuses on electronic commerce, online social networks, information economics and IT strategy. His work has appeared in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of Retailing, Decision Support Systems and others. Bin's research won the ISR Best Paper award in 2008 and the Best Paper-in-Track Award of the 2007 International Conference on Information Systems (ICIS).

![](/api/attachments/4G4V4UW5/fulltext/images/1d669c29453c51dd49c86861a20c5de228a8ea40a7fb457dd142806a9e4744fc.jpg)

Dr. Michelle Chen is an assistant professor at the San Jose State University. She received her Ph.D. from the University of Texas at Austin. Her research focuses on Virtual communities and social network, networked economy, electronic marketplaces and Internet marketing, data mining and business intelligence. Her work has appeared in Information Systems Research and others IS journals. Michelle's research won the ISR Best Paper award in 2008.

![](/api/attachments/4G4V4UW5/fulltext/images/72f99c9f262efa087e886e00739eb90e6d58f90c2cd0cb3fd6b5989970f1463d.jpg)

Dr. Prabhudev Konana is Professor of Information Management, Distinguished Teaching Professor, William H. Seay Centennial Professors in Business. and Assistant Director for Center for Research in Electronic Commerce (CREC) at the McCombs School of Business, the University of Texas at Austin. He received his MBA and Ph.D. in management information systems from the University of Arizona, Tucson in 1991 and 1995, respectively. He has an undergraduate degree in chemical engineering from Karnataka Regional Engineering College, India. His research interests are in business value of IT, virtual communities, outsourcing and offshoring. He is also interested in understanding of the impact of IT on developing countries.

Prabhudev's work has appeared in major refereed journals, such as Management Science, MIS Quarterly, Sloan Management Review, Information Systems Research IEEE Transactions on Software Engineering, Communications of the ACM, INFORMS Journal on Computing, IEEE Computer, IEEE Transactions on Computers, Decision Support Systems, IEEE IT Professional, Operations Research Letters, Information Systems, Information Processing Letters, and Journal of Systems and Software. Prabhudev is a member of the Academy of Distinguished Teachers, the highest teaching award at the University of Texas at Austin. He is a recipient of several research awards and grants. He received the prestigious National Science Foundation (NSF) CAREER Award, NSF Information Technology Research grant (with Balasubramanian and Rajagopal) Information Systems Research journal's Best Paper award for 2007, ICIS best paper runner up award, and CBA Foundation Research Excellence Award. He has also received grants from IBM, Intel, and Dell.
