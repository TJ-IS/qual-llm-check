---
otero_id: 11816
otero_key: "66JBMBFH"
title: "Product classification in the Internet business—a fuzzy approach"
authors: "B.K. Mohanty; B. Bhasker"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.10.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Product classification in the Internet business—a fuzzy approach

B.K. Mohanty\*, B. Bhasker

Indian Institute of Management, Off Sitapur Road, Lucknow 226 013, India

Received 10 October 2002; received in revised form 1 October 2003; accepted 7 October 2003 Available online 18 November 2003

## Abstract

In this paper, a methodology has been introduced as a decision support tool to the consumers in the Internet business. This decision support tool takes into account the multiple attributes of the product, analyses them with respect to the consumer’s desire, and finally classifies these products into different hierarchical levels as per the consumer’s level of preference. The product attributes, which are in general conflicting, imprecise, and non-commensurable in nature, are well handled here by using the concepts of fuzzy logic. Concepts of linguistic quantifier are used to quantify the qualitatively defined items and also to classify the products into different preference levels as required by the customer. Classification of the products into preference levels in any business, particularly, in the business through the Internet, gives a boost to the customer and helps him in a final product choice. The procedure described here can be used by virtual buying agents for generating a hierarchical classification based on buyer’s preference. At the end, a numerical example is illustrated to highlight the procedure. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Internet; Fuzzy sets; Linguistic quantifier; Hierarchical level; Product attributes; Product classification

## 1. Introduction

In any business, particularly through the Internet, a customer normally develops in his/her mind some sort of ambiguity, given the choice of similar alternative products. The ambiguity is mainly due to two reasons. Firstly, how to make a final product choice to purchase, and, secondly, on what basis the other products will be rejected. In order to answer the above questions, the customer may like to classify the products in different preference levels, preferably through some numerical strength of preference. Achievement of this classification will serve as a decision aid to the customer in the sense that, while purchasing a product, he/she will come to know the information on what preference level the product is chosen and what are the other available products in the network which are either superior or inferior to the chosen product. This will remove the ambiguity in the customer’s mind as far as the product choice is concerned. In addition to this, the customer will also know how far he/she is compromising with reference to the best available products (zero compromise, in case he/she purchases the best product) and to what extent his choice is inferior to the best product.

Jango, a personal shopping agent, and Dealtime by www.dealtime.com are the early efforts to provide agent based shopping support to the customers. These agents basically collect the price and the desirable product features from the Internet for a specified product. Once the customer has determined the product he/she is interested in, these agents offer a great assistance in identifying the best available deal on the Internet. The problem of determining the suitable product by the buyers in the vast Internet market place is a challenging one. The next level of the agents such as ‘‘decision guide’’ by www.ActiveBuyersGuide.com assists the customers in identifying a suitable product based on the product features provided by the buyers. The tool provides a list of matching products according to the customer’s specified attributes. However, the ‘‘decision guide’’ has its own limitations. In this tool, a customer can hardly define his/her desires level of satisfactions of the product attributes at different attribute echelons. In the ‘‘decision guide’’, a buyer can express only the importance of the product attributes or indicate a range by defining minimum and maximum attribute levels. These inputs enable the system to provide a list of products that fall within the specified domain. There may be a set of products that may have slight deviation from the domain but may offer a better overall desirability to the customers. Thus, the satisfaction level that the buyer is likely to derive from a deviated product becomes latent and thereby making it difficult to observe the products in totality and to assess the superiority of the listed products of the customer’s domain to that of the deviated products. This is necessary because at times a customer may like to compromise to a desirable extent and choose a product from the deviated list. The ‘‘decision guide’’ does not account for the customer’s compromising attitude, often implicitly present in most of the customer’s mind, depending on the type and scenario of the market. The work in our paper considers the flexibility in behavior exhibited by customers.

Ryu [7] has given an Electronic Shopping problem in which the products are classified based on the product attributes. Depending on the attribute specifications by the consumer, this procedure searches for the desired product in the Internet. If the product is available with the prescribed attribute specifications, the customer has got the desired product. In case of non-availability, the procedure chooses the next available product, which is closest to the targeted product. Closeness of the products are measured and compared through the product attribute values. The author has defined in Ref. [7] the term attribute flexibility, in order to classify different products with different attribute values into the same preference class. These flexibility values are chosen subjectively. This is a very rich idea for product classifications in the Internet business. The main drawback in the methodology is the subjectivity of choosing the flexible values of the product attributes.

There are other similar papers available, e.g., in Ref. [5], the authors define a ‘‘shopping program’’ that aims at the selection of a desirable product in the Internet. In the situation of non-availability of the product, the program suggests a product selection that is closest to the requested product in the taxonomy hierarchy as an alternative. The details about the product selection procedure are given in Ref. [5]. The real shortcoming in this approach is that the search is conducted in a single generic product hierarchy.

In our paper, we have introduced a methodology, based on fuzzy logic, which helps in resolving the above mentioned problems. With the help of fuzzy logic, the subjective assumption of flexibility values in the product attributes is replaced by its objective counterparts. We have interpreted the flexibility here in the following sense. If two different products have different values in a particular attribute, say for the attribute $A _ { i } , ( A _ { i } , \mu _ { A _ { I i } } )$ and $( A _ { i } , \mu _ { A _ { 2 i } } ) ,$ , where $\mu _ { A _ { i i } } ( j = 1 , 2 )$ are the membership values of the ith attribute and jth product, both the products can be classified into the same class, provided that the customer has some compromising attitude towards that attribute which is of less satisfaction level. The extent to which the customer can compromise is taken as the flexibility value of the attribute concerned.

Example 1.1. Let us take two cars with costs as (2, 0.8) and (2.5, 0.6) (0.8 and 0.6 being the membership values of the two cars having the cost 2 and 2.5, respectively). If the flexibility value for the attribute cost is 0.2 (say), the costs 2 and 2.5 are considered at par and kept in the same preference class. This is because for the attribute cost their differences in membership values (satisfaction levels) are not beyond 0.2.

From the above example, it is very clear that the customer at times compromises depending on the availability of the desired product and the current business scenario.

Let us assume that a number of alternative products are available in the Internet. Each product consists of multiple numbers of attributes, which are in general conflicting, imprecise and non-commensurable in nature. A consumer would ideally like to select a product that matches his/her specifications of the product attributes. In general, consumers express the product attributes vaguely, i.e., in fuzzy or linguistically defined terms. Concepts of fuzzy logic have been used here to quantify the qualitatively defined product attributes.

Example 1.2. In a car-purchasing problem, the attributes of the product CAR may be

 Cost (in US\$)

 Re-sale value (in US\$)

 Mileage (in miles/gal)

 Comfort (a qualitative term)

 Maintenance cost (in US\$)

In the customer’s view, these attributes are defined as:

 The cost of the CAR should be around US\$20,000.

 Re-sale value should be high.

 More or less the mileage should be about 20 miles/gal.

 The car should be comfortable.

 Maintenance cost must be low.

In the above statements, the italic words are fuzzy terms.

The above statements represent the customer’s view points in a realistic day-to-day language but are vague in computational sense. Without loss of generality, the membership functions of the above fuzzy terms can be represented as fuzzy numbers. The literature on fuzzy numbers is available in Refs. [2,3].

Let us assume that a customer wants to purchase a CAR whose cost will be around US\$20,000. The term around US\$20,000 is a fuzzy word and its fuzzy number representation is given in Fig. 1.

Let us assume that in the Internet, there are three cars with costs US\$15,000, US\$20,000 and US\$25,000. From the figure, the satisfaction levels (of the customer) for these CARs are respectively 0.5, 1.0 and 0.5.

![](/api/attachments/66JBMBFH/fulltext/images/80f41e4974e0ab256d402a3e1c7a204de6d361179b54874f56f3b7d4ef2d3107.jpg)  
Fig. 1.

From the above, it is very clear that using the fuzzy membership values of the fuzzy set cost, we can derive the satisfaction levels numerically. Note that for K number of products, we can have at most K different satisfaction levels for each attribute. This particular attribute’s satisfaction level varies from one product to another. The set of satisfaction levels just obtained is an exhaustive list with respect to the attribute cost. This is because all the available products in the network are considered. This set of satisfaction levels give us an idea about how a particular attribute is satisfied in all the available products. However, the available products may not be up to the fullest satisfaction levels, as desired by the customer with respect to all the product attributes. In this situation, a customer very often will like to compromise and will attempt to search for a best satisfactory product that satisfies ‘‘most’’ of the attributes rather than all the attributes. Further, the term ‘‘all’’ may often be viewed too restrictive, in many practical cases, it may be well replaced by some milder requirements, e.g., most, almost all, etc., specified by a linguistic quantifier. In our case, without loss of generality, in the same sense, an attribute is satisfied in most of the products, rather than in all the available products. Obviously, in this context, the linguistic term ‘‘most’’ is more realistic than the rigid term ‘‘all’’. Let us denote the degree of satisfaction of a particular attribute in most of the products as $\mu _ { \mathrm { m o s t } }$

Kacprzyk and Yager’s [4] concept of linguistic quantifier is used here to represent the linguistic term most as a fuzzy set. The term most articulates a generic fuzzy set {most, $\mu _ { \mathrm { m o s t } } \}$ that represents a satisfaction level for most of the products. This shows that it is impossible to have the products beyond this level $\mu _ { \mathrm { m o s t } }$ in a given profile. This implies that customers need to compromise and to accept even up to the level of $\mu _ { \mathrm { m o s t } }$ . After obtaining the compromise or flexibility values for all the attributes, we have used Ryu’s [7] algorithm to classify the products into different hierarchical levels.

In Section 2, we have explained the use of fuzzy sets in the product attributes and how the customers view them fuzzily. Section 3 is devoted to the procedure of hierarchical classification of the products, determination of the flexibility values of the attributes and the derivation of the linguistic quantifiers. In Section 4, we have illustrated a numerical example to enlighten the procedure. Some concluding remarks and the scope for future research are made in Section 5.

## 2. Fuzzy logic in product attributes

In any product purchase, normally, a customer considers the multiple attributes of the product. Some of the attributes are defined precisely and some of them are in the imprecise form. In many realistic decisions, the customers specify the product attributes imprecisely.

Example. In the product CAR, take the product attributes: cost, re-sale value, mileage, comfort and maintenance cost. Very often, a customer views these attributes in the following way.

 Cost: Cost should be around US\$20,000.

 Re-sale value: After 3–4 years, the re-sale value should be OK.

 Mileage: Mileage should be normal.

 Comfort: Overall, the car should be comfortable.

 Maintenance cost: Maintenance cost should not be very high.

Note that the customers view all these attributes vaguely or fuzzily but in a realistic way. In fact, the day-to-day business languages are often in the above form.

At times, the customer wants to make some trade-off in the attribute specifications, mostly in a situation when there is a conflict amongst the product attributes. This becomes more complicated when the attributes are non-commensurable and defined imprecisely. Trade-off relation also requires the attributes to be commensurable. Fuzzy logic helps in solving the above complex problem and arriving at a solution, as per the customer’s requirements. Fuzzy logic also helps in representing the imprecisely defined attributes as fuzzy numbers. Fig. 2(a) and (b) represents the product attributes cost and mileage.

In the above figure, the cost US\$20,000 corresponds to the fullest satisfaction level $( \mu _ { \mathrm { c o s t } } ( 2 0 , 0 0 0 ) { = } 1 )$ The satisfaction level $\left( \mu _ { \mathrm { c o s t } } \right)$ gradually comes down if the cost of the CAR either decreases or increases from the amount US\$20,000. Finally, it becomes zero satisfaction when the cost of the CAR is either US\$10,000 or US\$30,000 $( \mu _ { \mathrm { { c o s t } } } ( 1 0 0 0 0 ) = 0$ and $\mu _ { \mathrm { c o s t } } ( 3 0 0 0 0 ) { = } 0 )$ . This is shown in the Fig. 2(a). Similarly, for the attribute mileage, if a customer feels the normal mileage of a CAR should be 20 miles/gal, the fullest satisfaction for the mileage is at the point 20 miles $( \mu _ { \mathrm { m i l e a g e } } ( 2 0 ) = 1 )$ and slowly decreases if it is either below or above the point 20 miles. At points 15 and 25, we have the zero satisfaction $( \mu _ { \mathrm { m i l e a g e } } ( 1 5 ) = 0$ and $\mu _ { \mathrm { m i l e a g e } } ( 2 5 ) = 0 )$ . This is shown in Fig. 2(b).

![](/api/attachments/66JBMBFH/fulltext/images/233875a84b336a5fb6aa6ec172af89e639a40a1198507a49297c3f30824665c3.jpg)

![](/api/attachments/66JBMBFH/fulltext/images/df82380fe57b2a06399d1e4b3b5d664d626fc26adbd611832b62bdc76120be17.jpg)  
Fig. 2.

Though the mileage and the cost are non-commensurable attributes, it can be compared by comparing their respective membership values $\mu _ { \mathrm { c o s t } }$ and l<sub>mileage</sub>. Conflict amongst the attributes poses difficulty to the customers in making a consensus decision while selecting the product. Thus, there is a need for trade-off, i.e., have a gain in terms of one attribute and loss in terms of the other attribute(s). The concept of the fuzzy logic helps here to solve the above problems by aggregating the product attributes in a reasonable way.

## 3. Product classification procedure

In this section, we classify the available products into different preference hierarchical levels. This is done as per the procedure given in Ref. [7]. Major contribution of this paper is to objectively articulate the attribute flexibility values. The concept based on linguistic quantifier approach [4] is used here for the purpose.

Linguistic quantifier ‘‘most’’ is used in our paper, only to model the problem in a realistic fashion. In conventional approaches of business decision making, normally, a customer wants to find a product satisfying all the desired attributes as per his/her requirement. These approaches do not suggest how far the products which are available in the network best suits to the consumer needs. Our paper suggests the same, by using the linguistic quantifier ‘‘most’’ and for each attribute, by deriving an attribute level over all the available products. This attribute level represents the limit to which a customer should compromise or maintain flexibility for that particular attribute. This helps us to articulate the appropriate attributes and their flexibility values objectively.

## 3.1. Linguistic quantifier

In conventional approaches to fuzzy multiple attribute product selection problems, normally, a customer wants to fully satisfy every attribute as per his or her specifications. However, as the attributes in most of the products are conflicting, non-commensurable and fuzzily defined, it is very difficult to satisfy all the attributes simultaneously. It is more realistic to satisfy most of the attributes rather than all the attributes. The literature on aggregate operator are available in Refs. [1,6].

The linguistic quantifier ‘‘most’’ (fuzzy subset) needs to be defined properly in this context. Following the procedure described in Ref. [4], we have considered ‘‘most’’ as a fuzzy set with the following membership function

$$
\mu_ {\text { most }} (x) = \left[ \begin{array}{c c} 1 & x \geq 0. 8 \\ (x - 0. 3) / (0. 5) & 0. 3 \leq x \leq 0. 8 \\ 0 & x \leq 0. 3 \end{array} \right.\tag{3.1}
$$

The variable x represents the number of attributes. That is, here, the logic is, if number of attributes are more than or equal to 80% (not necessarily 80%, it can be any number depending on the situation), the concept ‘‘most’’ is fully justified. Similarly, if the number of attributes is less than or equal to 30%, the concept ‘‘most’’ is not at all justified. If the number of attributes are between 30% and 80%, accordingly, the degree of satisfaction is defined in the above expression.

## 3.2. Classification procedure

Let us assume that K products $\left\{ { { P } _ { 1 } } , { { P } _ { 2 } } , { { P } _ { 3 } } , . . . , { { P } _ { K } } \right\}$ are available in the Internet. Let each product $P _ { i } \left( i = 1 \right.$ $2 , . . . , K )$ has m number of attributes

$$
\left(A _ {i j}\right) i = 1, 2, \dots , K \text { and } j = 1, 2, \dots , m
$$

$A _ { i j }$ represents the jth attribute of the ith product.

Let $s _ { 1 } , s _ { 2 } , . . . , s _ { m }$ represent the customer’s attribute wise requirements in the form of fuzzy sets. Thus, we have the fuzzy sets along with the membership functions as:

$$
\left\{\left(s _ {1}, \mu_ {s _ {1}}\right) \right\}, \left\{\left(s _ {2}, \mu_ {s _ {2}}\right) \right\}, \dots \left\{\left(s _ {m}, \mu_ {s _ {m}}\right) \right\}.
$$

where $\mu _ { s _ { i } } ( j = 1 , 2 , 3 , . . . , m )$ represents the membership value of the customer’s specifications on the attribute $j .$ For example, if $s _ { 1 }$ and $s _ { 2 }$ represent the attributes cost and mileage of the product CAR, a customer’s satisfaction level in the form of fuzzy sets are shown in Fig. 2(a) and (b), respectively.

Take the jth attribute specification of a customer, $s _ { \mathrm { j } } ,$ and see how far the available products are compatible with this attribute specification. This can be obtained from the following K equations

$$
\mu_ {s _ {j}} (A _ {i j}) \quad (i = 1, 2, 3 \dots K)\tag{3.2}
$$

The average satisfaction level for attribute $\cdot _ { j } ,$ in all the products is given by

$$
\mathrm{AV} _ {j} = \frac {1}{K} \sum_ {i = 1} ^ {K} \mu_ {s _ {j}} (A _ {i j})\tag{3.3}
$$

where $\mathrm { A V } _ { j }$ represents the average value of product satisfaction for the attribute j.

Now, evaluate the extent to which the attribute j is satisfied over most of the products. As per the procedure given in Ref. [4], we can obtain the satisfaction level of the attribute $j ,$ in most of the products, say, $R _ { j } ,$ as:

$$
R _ {j} = \mu_ {\text { most }} (\mathrm{AV} _ {j})\tag{3.4}
$$

We call $R _ { j }$ a representative factor of the jth attribute over the available products. In other words, we can tell that $R _ { j }$ is the degree of satisfaction of attribute j over most of the available products. Similarly, we can have $R _ { i } \ ( i { = } 1 , \ 2 , \ 3 , \ . \ . . , \ m , \ i { \ne } \ j )$ for other product attributes.

The $R _ { i } { ' } \mathrm { s }$ play an important role in determining the degree to which a customer needs to compromise or maintain flexibility for the ith attribute. This is calculated as follows:

$$
e _ {i} = \left\{ \begin{array}{l l} 0 & \mu_ {s _ {i}} \leq R _ {i} \\ \left| \mu_ {s _ {i}} - R _ {i} \right| & \mu_ {s _ {1}} > R _ {i} \end{array} \right.\tag{3.5}
$$

where $e _ { i }$ represents the flexibility value of the ith attribute.

Eq. (3.5) represents that there is no need to compromise if the chosen product’s desired level of satisfaction $\mu _ { s _ { i } }$ is less than $R _ { i }$ (satisfaction level of the most of the available products). This is shown in the first part of the equation with $e _ { i } = 0 .$ However, if the selected product’s desired satisfaction level $\mu _ { s _ { i } }$ is greater than $R _ { i } ,$ a customer needs to compromise (or maintain flexibility). Numerically, the amount of flexibility should be $\vert \mu _ { s _ { i } } - R _ { i } \vert$ . This is shown in the 2nd part of Eq. (3.5).

If the customer desires to have the fullest satisfaction level in all its attributes $( \mu _ { s _ { i } } = 1 , i = 1 , 2 , . . . , m )$ then we have the flexibility values as:

$$
e _ {i} = \left(1 - R _ {i}\right) \quad i = 1, 2 \dots m
$$

The process of product classification begins with a set of products $P { = } \{ P _ { 1 } , \ P _ { 2 } , \ . . . , \ P _ { K } \}$ and a set of representative attributes from Eq. (3.4) $\{ R _ { 1 } , R _ { 2 } , . . . ,$ $R _ { m } \}$ . If the customer’s attributewise preferences are in the order of $1 , 2 , . . . , m ,$ , the product classification can be obtained in the following steps.

Step 1. Initially take the customer’s most preferred attribute (1st attribute) and his/her product specification in the form of a fuzzy set $( s _ { 1 } , \mu _ { s _ { I } } )$

Step 2. For each product, evaluate the 1st attribute’s level of satisfaction $\mu _ { s _ { \scriptscriptstyle I } } ( A _ { i l } ) ~ ( i = 1 , ~ 2 ,$ $\cdots , K )$ to the derived representative factor $R _ { 1 }$ Step 3. Find the attribute flexibility $e _ { 1 }$ using Eq. (3.5).

Step 4. From the product set $P ,$ for attribute 1, select the product set $P _ { 1 1 } .$ , satisfying the attribute 1 at least to the level of $R _ { 1 }$ , i.e., after allowing the flexibility $e _ { 1 }$ .

Now, by taking the attribute 2 and again applying the same procedure on $P _ { 1 1 }$ , we can narrow down the choice set to $P _ { 1 2 }$ . In the same way, this is obtained after due consideration to the value $e _ { 2 } .$ . Repeating the process, up to the mth attribute, we have a final set $P _ { 1 m }$ of products as the most preferred products in the network.

In the second step, we take the product set as $P - P _ { 1 m } .$ The process is repeated again and, in this case, the second preference level products are $P _ { 2 m } .$ This process is continued till we arrive at a product set which are indifferent to each other and no preference can be made as per the customer’s specifications.

## 4. Numerical example

Let us assume that the customers requirement for a product CAR are expressed in terms of the attributes cost, maintenance cost (monthly) and mileage (miles/gal) and are in the form of fuzzy sets as shown in Fig. 3.

From the above figures, the fuzzy sets for cost, maintenance cost and mileage are as follows:

Cost={0/10,000, 0.8/15,000, 1.0/20,000, 0.8/ 25,000, 0.6/30,000, 0.4/40,000, 0.1/50,000, 0/ 60,000}

Maintenance={0/40, 0.4/50, 0.63/100, 0.65/150, 1.0/200, 0.8/300, 0.4/400, 0.2/500}

Mileage={0/9, 0.1/10, 0.4/12, 0.5/15, 0.6/16, 0.73/ 17, 0.8/19, 1.0/20, 0.9/21, 0.8/22, 0.72/25, 0.7/26}

![](/api/attachments/66JBMBFH/fulltext/images/13694ab21fb200b4c37fe2d5c490f0ba2167ac92271bc4dc70d11b3657304653.jpg)

B  
![](/api/attachments/66JBMBFH/fulltext/images/ae44d8b772abb9b751bf5eab6553c0ad061e34dbcc330fd6f3b77753c401f508.jpg)

![](/api/attachments/66JBMBFH/fulltext/images/5c6dbbc3dcbeddaa2a79610218a389354dc3c38d85015605f50e09b3e1347600.jpg)  
Fig. 3.

In the Internet, let us say, for example, that there are eight types of ‘‘cars’’ available. The data on these cars are given in the following table.

<table><tr><td>Car type</td><td>Cost in US$</td><td> $\mu_{cost}$ </td><td>Maintenance cost in US$</td><td> $\mu_{maintenance}$ </td><td>Mileage (in miles/gal)</td><td> $\mu_{mileage}$ </td></tr><tr><td> $P_1$ </td><td>30,000</td><td>0.6</td><td>100</td><td>0.63</td><td>19</td><td>0.8</td></tr><tr><td> $P_2$ </td><td>40,000</td><td>0.4</td><td>50</td><td>0.4</td><td>25</td><td>0.72</td></tr><tr><td> $P_3$ </td><td>20,000</td><td>1</td><td>300</td><td>0.8</td><td>17</td><td>0.73</td></tr><tr><td> $P_4$ </td><td>50,000</td><td>0.1</td><td>100</td><td>0.63</td><td>22</td><td>0.8</td></tr><tr><td> $P_5$ </td><td>50,000</td><td>0.1</td><td>150</td><td>0.65</td><td>25</td><td>0.72</td></tr><tr><td> $P_6$ </td><td>40,000</td><td>0.4</td><td>200</td><td>1</td><td>22</td><td>0.8</td></tr><tr><td> $P_7$ </td><td>15,000</td><td>0.8</td><td>500</td><td>0.2</td><td>12</td><td>0.4</td></tr><tr><td> $P_8$ </td><td>25,000</td><td>0.8</td><td>300</td><td>0.8</td><td>20</td><td>1</td></tr></table>

Using Eq. (3.3), we have

$$
\begin{array}{r l} \mathrm{AV} _ {\text { cost }} & = (0. 6 + 0. 4 + 1 + 0. 1 + 0. 1 + 0. 4 \\ & + 0. 8 + 0. 8) / 8 = 0. 5 2 \end{array}
$$

$$
\begin{array}{r l} \mathrm{AV} _ {\text { maintenance }} & = (0. 6 3 + 0. 4 + 0. 8 + 0. 6 3 + 0. 6 5 + 1 \\ & + 0. 2 + 0. 8) / 8 = 0. 6 4 \end{array}
$$

$$
\begin{array}{r l} \mathrm{AV} _ {\text { mileage }} & = (0. 8 + 0. 7 2 + 0. 7 3 + 0. 8 + 0. 7 2 + 0. 8 \\ & + 0. 4 + 1) / 8 = 0. 7 5 \end{array} \tag {4.1}
$$

From Eqs. (3.1) and (3.4), we can calculate the representative factors of the attributes cost, maintenance and mileage as:

$$
\begin{array}{l} R _ {\text { cost }} = \mu_ {\text { most }} (0. 5 2) = (0. 5 2 - 0. 3) / 0. 5 = 0. 4 4 \\ R _ {\text { maintenance }} = \mu_ {\text { most }} (0. 6 4) = (0. 6 4 - 0. 3) / 0. 5 = 0. 6 8 \\ R _ {\text { mileage }} = \mu_ {\text { most }} (0. 7 5) = (0. 7 5 - 0. 3) / 0. 5 = 0. 9 \end{array} \tag {4.2}
$$

By assuming that the customer desires to have the fullest satisfaction level in the attributes cost, maintenance and mileage, from Eq. (3.5), the flexibility values are as follows.

$$
\begin{array}{l} e _ {\text { cost }} = 1 - 0. 4 4 = 0. 5 6 \\ e _ {\text { maintenance }} = 1 - 0. 6 8 = 0. 3 2 \\ e _ {\text { mileage }} = 1 - 0. 9 = 0. 1 \end{array}\tag{4.3}
$$

Following the procedure [7], we have classified the available products in the Internet in the following steps.

Step 1. Take all the products

$$
P = \left\{P _ {1}, P _ {2}, P _ {3}, P _ {4}, P _ {5}, P _ {6}, P _ {7}, P _ {8} \right\}
$$

Step 2. If the customer’s priority is in the order of cost, maintenance and mileage, select the products from the product list which satisfy the customer’s requirement after allowing the flexibility for cost 0.56. This will arrive in the following list.

$$
P _ {1 1} = \left\{P _ {1}, P _ {3}, P _ {7}, P _ {8} \right\}
$$

Step 3. From the current list, again, select the products which satisfy the customer’s maintenance requirements. Of course, the flexibility value here is 0.32. Thus, we have the product list as:

$$
P _ {1 2} = \left\{P _ {3}, P _ {8} \right\}
$$

Step 4. Similarly, by considering the mileage requirement and allowing the flexibility of 0.1, we have

$$
P _ {1 3} = \{P _ {8} \}
$$

Now, we have obtained the first level preference product as $\{ P _ { 8 } \}$

Step 5. Next, in order to have the second level preference products take the initial product set as

$$
P ^ {2} = P - P _ {1 3} = \left\{P _ {1}, P _ {2}, P _ {3}, P _ {4}, P _ {5}, P _ {6}, P _ {7}, \right\}
$$

Step 6. Repeat the same procedure as it was from Steps 1–5 along the attributes in the order of cost, maintenance and mileage. The final list of the products in the second preference level is

$$
P _ {2 3} = \{P _ {3} \}
$$

Similarly the 3rd, 4th and 5th preference level products are:

$$
P _ {3 3} = P _ {1}, P _ {7}
$$

$$
P _ {4 3} = \{P _ {6} \}
$$

$$
P _ {5 3} = \{P _ {2}, P _ {4}, P _ {5} \}
$$

## 5. Conclusion

The shift to Internet commerce from the traditional commerce has given an increased choice to buyers due to the growth in the number of vendor sites offering products with varying options. Given the ambiguous and imprecise way in which buyers typically express their preferences, finding the products that match the customer’s preferences to some degree and ranking them is a very complex and a time consuming process. In the absence of an automated procedure, the only option left to the buyer is to scan manually a limited number of products prior to arriving at a final decision. In the buyer’s case, this may lead to a greater degree of chance of regret.

In our paper, a new technique is defined considering the product attributes, product classification and the linguistic quantifier. The procedure developed in the paper throws light to the customers as a support for Internet shopping. Although many other web-based marketing decision guides are available, our methodology has a different dimension and is based on the concepts of fuzzy logic.

The methodology described in our paper helps the customer in the following way.

1. In general, a product consists of multiple number of attributes which are conflicting, non-commensurable and fuzzy in nature. Our paper takes into account these aspects of multiple product attributes and helps the customer in choosing an appropriate product.

2. Based on the customer’s fuzzy choice of the product attributes, products are classified into hierarchical preference levels. This classification is an aid to the customer in making a final choice of the product. Thus, a buyer can select a product being fully aware of the hierarchical preference order. The hierarchical product classification acts as a decision aid to the customer, in the sense that the customer himself/herself will come to know the information about where his/her chosen product stands in the product profile. This will also help him/her to upgrade his/her product choice to a different level should the situation so demands.

3. The linguistic quantifier ‘‘most’’ is used here in order to quantify the qualitatively defined terms. This quantification helps a customer to assess the amount of compromise or flexibility he/she needs to maintain in the market profile. In other words, a customer needs to emphasize, how his/ her objective best fits to most of the available products.

4. Weighted preference of the attributes by the customers, if any, can be well handled here by appropriately defining fuzzy membership functions of the product attributes.

In our numerical example, we have taken the first attribute (cost) as the most important attribute. This is only for the illustration purpose. The selection of the first attribute prior to the initiation of the hierarchical classification may be a topic for future research. In addition to this, the articulation of numerical strength of preference amongst the hierarchical levels may be a further aid to customer in his/ her product choice. We suggest this also for future research.

## Acknowledgements

We thank the anonymous referees for their valuable suggestions which have considerably improved the presentation of the paper.

## References

[1] K.K. Aggrawal, M.P. Kumar, B.K. Mohanty, Estimating operational profile in software reliability: a fuzzy approach, J. Intell. Fuzzy Syst. 1 (1994) 307 – 311.

[2] D. Dubois, H. Prade, Addition of interactive fuzzy numbers, IEEE Trans. Automat. Contr. AC-26 (1981) 926 – 936.

[3] D. Dubois, H. Prade, Operations on fuzzy numbers, Int. J. Syst. Sci. 9 (1978) 613.

[4] J. Kacprzyk, R.R. Yager, Linguistic quantifiers and belief qualifications in fuzzy multicriteria and multi-stage decision making, Control Cybern. 13 (1984) 155 – 173.

[5] R.M. Lee, G.R. Widmeyer, Shopping in the electronic market place, J. Manage. Inf. Syst. 2 (1986) 21 – 35.

[6] B.K. Mohanty, Assigning weights to multiple criteria—a fuzzy approach, J. Fuzzy Math. 6 (1998) 209– 222.

[7] Y.U. Ryu, A hierarchical constraint satisfaction approach to product selection for electronic shopping support, IEEE Trans. Syst. Man Cybern., Part A, Syst. Humans 29 (1999) 525 – 532.

![](/api/attachments/66JBMBFH/fulltext/images/f9f7ffafdc88e6127d63d431352835a651d7761574b99fec7ff1ac6747a7adaf.jpg)

Dr. B.K. Mohanty is a Professor in the Decision Science Group at Indian Institute of Management, Lucknow, India. He received M.Sc in Mathematics from Berhampur University, Orissa, India and PhD in Operations Research from IIT Kharagpur, India. Prior to joining IIM, Lucknow, he served in Tata Research Development and Design Centre, Pune as Member, Technical Staff, as an Associate Professor at Xavier Institute of

Management, Bhubaneswar and as a scientist at CFTRI, Mysore. His research interests include in the areas of Fuzzy logic applications in Multiple Criteria Decision Making, Data Mining and Internet Business.

![](/api/attachments/66JBMBFH/fulltext/images/c205356fd4d05559246112c7f1d0015a8612d996880bdbb6b7df3a8359f15b79.jpg)

Dr. Bharat Bhasker is a Professor in the area of Information Technology & Systems, at IIM Lucknow, India. He holds a Bachelor’s degree in Electronics & Communications Engineering from University of Roorkee, India. Master’s degree and Doctorate in Computer Science from Virginia Polytechnic Institute and State University, USA. Prior to joining IIM Lucknow, he was with MDL Information Systems and Sybase Inc., California, USA

and was the architect of the massively parallel DBMS, Sybase MPP. He also served as Visiting Professor of Information Systems, Business Management School, University of Maryland, University of California, and University of Texas, USA. His research interests include Distributed Database Management, Data Mining, Personal Recommendation Systems, Agent based Electronic Shopping. He has also authored a book on Electronic Commerce.
