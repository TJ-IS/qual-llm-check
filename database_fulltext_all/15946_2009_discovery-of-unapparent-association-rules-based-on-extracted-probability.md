---
otero_id: 15946
otero_key: "3XC8R6UN"
title: "Discovery of unapparent association rules based on extracted probability"
authors: "Chia-Wen Liao; Yeng-Horng Perng; Tsung-Lung Chiang"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.04.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Discovery of unapparent association rules based on extracted probability

Chia-Wen Liao <sup>a,</sup>⁎, Yeng-Horng Perng <sup>b</sup>, Tsung-Lung Chiang <sup>c</sup>

<sup>a</sup> Department of Civil Engineering, China University of Technology, Taipei, Taiwan

<sup>b</sup> Department of Architecture, National Taiwan University of Science and Technology, Taipei, Taiwan

<sup>c</sup> Department of Civil Engineering, National Taiwan University, Taipei, Taiwan

## a r t i c l e i n f o

Article history: Received 11 March 2007 Received in revised form 3 March 2009 Accepted 2 April 2009 Available online 15 April 2009

Keywords: Association rule Extracted probability Occupational fatalities Construction industry

## a b s t r a c t

Association rule mining is an important task in data mining. However, not all of the generated rules are interesting, and some unapparent rules may be ignored. We have introduced an “extracted probability” measure in this article. Using this measure, 3 models are presented to modify the con<sup>fi</sup>dence of rules. An ef<sup>fi</sup>cient method based on the support-con<sup>fi</sup>dence framework is then developed to generate rules of interest. The adult dataset from the UCI machine learning repository and a database of occupational accidents are analyzed in this article. The analysis reveals that the proposed methods can effectively generate interesting rules from a variety of association rules

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Association rules are used to discover relationships, and potential associations, of items or attributes among huge amounts of data. The discovery of association rules is an important data mining task for which many algorithms have been proposed [8,15,16,24]. However, not all of the generated association rules are interesting [19], and some unapparent rules may be ignored.

When the ratio of transactions containing a certain item is very high, a great many association rules concerning the item can be generated from the transaction database. For example, if the ratio of transactions containing A and B are 90% and 50% respectively, the ratio of transactions containing both A and B is at least 40%, as shown in Fig. 1. In the case of the example, the con<sup>fi</sup>dence of $B \Rightarrow A$ is at least 90% $( = 4 0 \% / 5 0 \% )$ . Even though the minimum con<sup>fi</sup>dence threshold is rather high, the association rule B ⇒ A probably holds in the database due to the value of support. For this reason, a great many rules concerning item A can be generated, whether they are interesting or not. It is costly and unnecessary to deal with so many rules [6].

On the contrary, if the ratio of transactions in a database containing C and D are 10% and 5% respectively, as shown in Fig. 2, the rule $D \Rightarrow C$ is probably excluded from association rules for its low con<sup>fi</sup>dence. Nevertheless, if the con<sup>fi</sup>dence of both rules (D ⇒ C and B ⇒ A) is the same. the rule $D \Rightarrow C$ is more interesting in that it is less inevitable. In practice, the con<sup>fi</sup>dence of $D \Rightarrow C$ is frequently not high enough to be obvious. As a result, as the rules with high con<sup>fi</sup>dence are numerous, some interesting but unobvious rules can be ignored. To handle this problem, in this article, a new measure called “extracted probability” will be introduced. This new measure, together with the support and con<sup>fi</sup>dence measures, will lead to an ef<sup>fi</sup>cient method for mining association rules. Two example datasets and a UCI census dataset are used to test our approach to association rule mining. Finally, the proposed method is then applied to analyze fatal occupational injuries in the Taiwan construction industry.

## 2. Related work on association rules

## 2.1. Association rule preliminaries

Association rules can be used to discover relationships and potential associations from huge amounts of data. These rules can be effective in uncovering unknown relationships, and provide some results that can be the basis for forecasting and decision making [7, 9,10,17,24].

A well-known Apriori algorithm [1,4,20,25] has been proposed to discover meaningful itemsets ef<sup>fi</sup>ciently and to construct association rules in a transaction database. Association rule mining can be de<sup>fi</sup>ned as follows [2,14,28]. Let $I = \{ i _ { 1 } , i _ { 2 } , i _ { 3 } , . . . i _ { m } \}$ be a set of m distinct literals, or items. Let D be a set of transactions, called a transaction database, where each transaction T consists of a set of items such that $T \subseteq I .$ Given an itemset $X \subseteq I ,$ a transaction T contains X if and only $\mathrm { i f } X \subseteq T .$ An itemset X in a transaction database D has a support, denoted as support (X). This is the ratio of transactions in D containing X. An association rule is the implication $X \Rightarrow Y ,$ where $X \subseteq I , Y \subseteq I$ and X ∩ $Y { = } \phi .$ An association rule $X \Rightarrow Y$ holds in D with support s% if the probability of a transaction in D containing X and Y is s%, i.e.

$$
\text { Support } (X \Rightarrow Y) = \text { Support } (X \cup Y)\tag{1}
$$

An association rule $X \Rightarrow Y$ holds in D with con<sup>fi</sup>dence c% if the probability of a transaction in D which contains X also contains Y is also c%, i.e.

$$
\text { Confidence } (X \Rightarrow Y) = \text { Support } (X \cup Y) / \text { Support } (X)\tag{2}
$$

To generate association rules is to discover all the association rules that have support greater than, or equal to, a minimum support (minsupp) threshold and con<sup>fi</sup>dence greater than, or equal to, a minimum con<sup>fi</sup>dence (minconf) threshold. The association rules must satisfy two conditions:

$$
\text { Support } (X \Rightarrow Y) \geq \text { minsupp }\tag{3}
$$

$$
\text { Confidence } (X \Rightarrow Y) \geq \text { minconf }\tag{4}
$$

## 2.2. Related work

Interestingness measures play an important role in data mining. Interestingness can be categorized into three classi<sup>fi</sup>cations: objective, subjective and semantics-based. An objective measure is based only on the raw data. No knowledge about the user or application is required. Most objective measures are based on theories in probability, statistics, or information theory. Therefore, they have strict principles and foundations and their properties can be formally analyzed and compared. A subjective measure takes into account both the data and the user of these data. To de<sup>fi</sup>ne a subjective measure, access to the user's domain or background knowledge about the data is required. A semantic measure considers the semantics and explanations of the patterns. Due to involving domain knowledge from the user, semantic measures are considered a special type of subjective measure [5,11].

Association rules are one of the most common patterns that can be evaluated by interestingness measures, and the support and con-<sup>fi</sup>dence measures are the original interestingness measures proposed for association rules. In this article, we focus on the objective interestingness measure based on probability.

Probability-based objective measures that evaluate the generality and reliability of association rules have been thoroughly studied [12,18,22,23,27]. For an association rule $X \Rightarrow Y ,$ Support (X) or Support $( X \cup Y )$ is used to represent the generality of the rule, and Con<sup>fi</sup>dence $( X \Rightarrow Y )$ or a correlation factor (e.g. Con<sup>fi</sup>dence (X ⇒ Y)−Support (Y) or Con<sup>fi</sup>dence $( X \Rightarrow Y )$ /Support (Y)) is used to represent the reliability of the rule. Some measures include either generality or reliability, and others combine both. Little has been discussed about any other possible measures aside from generality or reliability. In general, a rule with high generality and reliability is considered interesting. The problem is that, relatively, a rule with high generality probably has high reliability, especially for a rule with extremely high generality. As a result, a variety of repetitive or meaningless rules may be generated as interesting rules. In this article, a rule with higher probability is considered less interesting.

![](/api/attachments/3XC8R6UN/fulltext/images/4dd2154741c5429dd4f7601f014983685a16e765c8ab02f3dae35e67bb858f2a.jpg)  
Fig. 1. Example rule B ⇒ A.

![](/api/attachments/3XC8R6UN/fulltext/images/7bcce4fc59e17b921e5244d242d1eba67c1c5f4668e1bee73a9543c6e50afc98.jpg)  
Fig. 2. Example rule D ⇒ C.

## 3. Discovery of unapparent association rules

## 3.1. Extracted probability

As mentioned above, the association rules must satisfy two conditions, one of which is its con<sup>fi</sup>dence greater than, or equal to, a minimum con<sup>fi</sup>dence (minconf) threshold. Consequently, Eqs. (2) and (4) yield Support (X ∪ Y)/Support (X)≥minconf, then

Support $( X \cup Y ) { \big . }$ z minconf × Support X

$$
\text { And   Support } (Y) \geq \text { Support } (X \cup Y), \text { then }\tag{5}
$$

$$
\text { Support } (Y) \geq \text { minconf } \times \text { Support } (X)\tag{6}
$$

Suppose that the number of D is $N _ { T }$ the number of transactions in $D$ containing X is $N _ { X } ,$ the number of transactions in D containing Y is $N _ { Y }$ and the number of transactions in D containing X and Y is $N _ { X Y }$ Then Eqs. (5) and (6) become Eqs. (7) and (8), respectively

$$
N _ {X Y} \geq \text { minconf } \times N _ {X}\tag{7}
$$

$$
N _ {Y} \geq \text { minconf } \times N _ {X}\tag{8}
$$

Let $N _ { m c } =$ minconf× $N _ { X } .$ . Then Eqs. (7) and (8) become Eqs. (9) and (10) respectively.

$$
N _ {X Y} \geq N _ {\mathrm{mc}}\tag{9}
$$

$$
N _ {Y} \geq N _ {\mathrm{mc}}\tag{10}
$$

Eq. (10) indicates that $X \Rightarrow Y$ cannot satisfy the minimum con<sup>fi</sup>dence threshold unless $N _ { Y }$ is greater than, or equal to, $N _ { m c }$ . The probability that $N _ { X Y }$ is greater than, or equal $\mathrm { t o } , N _ { m c }$ that is, the probability that X ⇒ Y can satisfy the minimum con<sup>fi</sup>dence threshold, is presented from Eq. (9). It is de<sup>fi</sup>ned as “extracted probability” and shown in Eq. (11).

$$
\begin{array}{l} P _ {X \Rightarrow Y} = \frac {C _ {N _ {X}} ^ {N _ {Y}} \times C _ {0} ^ {N _ {T} - N _ {Y}} + C _ {N _ {X} - 1} ^ {N _ {Y}} \times C _ {1} ^ {N _ {T} - N _ {Y}} + \dots + C _ {N _ {m c}} ^ {N _ {Y}} \times C _ {N _ {X} - N _ {m c}} ^ {N _ {T} - N _ {Y}}}{C _ {N _ {X}} ^ {N _ {T}}} \\ = \sum_ {i = 0} ^ {N _ {X} - N _ {m c}} \frac {C _ {N _ {X} - i} ^ {N _ {Y}} \times C _ {i} ^ {N _ {T} - N _ {Y}}}{C _ {N _ {X}} ^ {N _ {T}}} \end{array} \tag {11}
$$

![](/api/attachments/3XC8R6UN/fulltext/images/352741d717f7d92583c4fe37d861cb7819f7062baf6232c00b49d3fd71a28626.jpg)  
Fig. 3. Contour map of extracted probability for minimum con<sup>fi</sup>dence=80%.

where C<sup>a</sup> is referred to as the number of combinations of a objects taken b at a time and $\begin{array} { r } { C _ { b } ^ { a } = \frac { a ! } { b ! \times ( a - b ) ! } . } \end{array}$ In probability theory, one considers any population of a distinct objects. Then there are $C _ { b } ^ { a }$ ways of choosing b of the objects.

For example, consider that $N _ { T } N _ { X }$ and N are 7, 2 and 3, respectively. Suppose that minconf is 50%. Based on Eq. (9), $N _ { X Y }$ must be greater than, or equal to, 1 $( N _ { \mathrm { m c } } { = } 5 0 \% { \times } 2 { = } 1 )$ . In other words, $N _ { X Y }$ can be 1 or 2. Then the extracted probability is the sum of the probability of $N _ { X Y } = 1$ and $N _ { X Y } = 2 ,$ as presented in Eq. (11). That is:

$$
P = \frac {C _ {1} ^ {3} \times C _ {1} ^ {7 - 3}}{C _ {2} ^ {7}} + \frac {C _ {2} ^ {3} \times C _ {0} ^ {7 - 3}}{C _ {2} ^ {7}} = \sum_ {i = 0} ^ {2 - 1} \frac {C _ {2 - i} ^ {3} \times C _ {i} ^ {7 - 3}}{C _ {2} ^ {7}}
$$

## 3.2. Contour map of extracted probability

Given a minimum con<sup>fi</sup>dence and the support of both itemsets, Eq. (11) can be used to acquire the extracted probability of the rule. Then we can obtain a contour map of extracted probability.

There are several important limits and regions in the contour map of extracted probability. Take a minimum con<sup>fi</sup>dence of 80% for example, as shown in Fig. 3. Line 1 is drawn from Eq. (6). Zone A, which is below Line 1, is a region in which no rules can satisfy the minimum con<sup>fi</sup>dence threshold. On the contrary, Zone B, which is above Line 2, is a region in which the con<sup>fi</sup>dence of all rules is greater than, or equal to, a minimum con<sup>fi</sup>dence threshold certainly. In Zone C, the extracted probability of the rules lies between 0 and 1. Obviously the closer a rule is to Line 1, the less the probability that it can be generated from the database.

The map can be employed to determine whether a rule is inevitable or not due to the value of support. As mentioned in the introduction, if the support of A and B are 90% and 50% respectively, the extracted probability of B⇒ A for the minimum con<sup>fi</sup>dence of 80% is 100%, which is shown as Point a in Fig. 3. It can be seen that the contour map of extracted probability can reveal the probability that a certain rule can satisfy a given minimum con<sup>fi</sup>dence under any support of both itemsets. According to the map of different con<sup>fi</sup>dence thresholds, as shown in Fig. 4, the results show that the lower the minimum con<sup>fi</sup>dence is, the larger the area with high extracted probability is. In other words, when the con<sup>fi</sup>dence threshold is lower, the generated association rules are more likely to be inevitable rules.

![](/api/attachments/3XC8R6UN/fulltext/images/a622790e53c59ad1787cfe1733b9c93ed15dc05b83d4b3899f30842351f154a7.jpg)

(b) minconf =80 %  
![](/api/attachments/3XC8R6UN/fulltext/images/c3582266f8dd232b0370cb46ae7093557309edd4e698671ab371300178bde0a7.jpg)

(c) minconf =90%  
![](/api/attachments/3XC8R6UN/fulltext/images/8931377347bf663ac686a1d33c42e5fe802955534b3f8e6cdc3300a098c00373.jpg)  
Fig. 4. Contour map of extracted probability for minimum con<sup>fi</sup>dence=70%, 80% and 90%.

![](/api/attachments/3XC8R6UN/fulltext/images/8e7a1cab817839d74808f651d3eb39834ac0085ac5bf77c7f4ac480768f8247c.jpg)

![](/api/attachments/3XC8R6UN/fulltext/images/fed717bf0f0ee99226a7e7239aadf7f49f004d994cf886174e8b71ac423e66fc.jpg)  
Fig. 5. Contour map of extracted probability for different ranges of support.

In addition, the map can be applied to discuss the in<sup>fl</sup>uence of the support range of attributes on generated rules. From the map, we can obtain the average probability of rules for a given range of support. The value of average probability implies whether a database with that range of support is inclined to generate inevitable rules. As shown in Fig. 5, the average probability of rules in area A is almost zero, and the average probability of rules in area B is 0.5. It can be seen that the rules generated by a database with support of area A seem to be less inevitable than those generated by a database with support of area B.

## 3.3. Modified confidence

As shown in Fig. 4, based on the same support of both itemsets, the extracted probability decreases with advancing con<sup>fi</sup>dence threshold. If the minconf is set too high, very few association rules may be generated, and a lot of interesting but unapparent rules can be excluded. If the minconf is set too low, too many association rules may be generated, and a lot of uninteresting even redundant rules can be included. To solve the problems, this article presents a method to modify the con<sup>fi</sup>dence of rules.

The extracted probability of each rule is different so that this article adopts a correlation coef<sup>fi</sup>cient to modify the value of con<sup>fi</sup>dence. That is, the modi<sup>fi</sup>ed con<sup>fi</sup>dence is the initial con<sup>fi</sup>dence multiplied by the coef<sup>fi</sup>cient, expressed as Eq. (12).

$$
\operatorname{Conf} _ {\text { corr }} (\mathrm{X} \Rightarrow \mathrm{Y}) = \mathrm{C} \times \operatorname{Conf} _ {\text { pri }} (\mathrm{X} \Rightarrow \mathrm{Y})\tag{12}
$$

where $\mathsf { C o n f } _ { \mathrm { c o r r } } \left( X \Rightarrow Y \right)$ and $\mathsf { C o n f _ { p r i } } \ ( X \ \Rightarrow \ Y ) \mathsf { a r e }$ the modi<sup>fi</sup>ed con<sup>fi</sup>dence and the initial con<sup>fi</sup>dence respectively, and C is the correlation coef<sup>fi</sup>cient related to the minimum con<sup>fi</sup>dence and the support of X and Y.

Considering association rules with weak extracted probability is more interesting, the con<sup>fi</sup>dence of rules with weak extracted probability reduces less than that of rules with strong extracted probability. This article proposes three modi<sup>fi</sup>ed models — linear, quadratic, and logarithmic models, as shown in Fig. 6. All the correlation coef<sup>fi</sup>cients decrease as the extracted probability increases. The logarithmic model tends to reinforce the con<sup>fi</sup>dence reduction of the rules with strong extracted probability.

The support-con<sup>fi</sup>dence framework is generally used as a basis for association rules mining. Based on the support-con<sup>fi</sup>dence framework (denoted as the primary method), an ef<sup>fi</sup>cient method modifying the con<sup>fi</sup>dence of rules is developed to generate association rules. We then compare the proposed method with the primary method in this article.

## 3.4. Experimental results

In order to discuss the effect on generated rules of different types of databases, two example Boolean databases of different ranges of support were established for this article. One of the databases (denoted as database-1) includes 12 items with support between 7% and 86%, and the other one (denoted as database-2) includes 14 items with support between 7% and 55%. Both databases include 100 transactions.

On condition that the minimum support and the minimum con<sup>fi</sup>dence are 5% and 90% respectively, a total of 97 association rules are generated from database-1. The generated rules are plotted on the contour map of extracted probability, as shown in Fig. 7. It can be seen that the extracted probabilities of most generated rules are greater than 0.3 and reach a peak of 0.6. The dashed box is a zone in which the interesting association rules with weak extracted probability lie. Furthermore, the association rules generated by the proposed methods are also shown on the left side in Fig. 7. It shows that 10 association rules are left by the linear model, 3 association rules are left by the quadratic model, and no association rules are left by the logarithmic model.

![](/api/attachments/3XC8R6UN/fulltext/images/038f6b423194d24ad28f974c1e451e8f532efd4af36ae44c38d6584038fe9b10.jpg)  
Fig. 6. Correlation coef<sup>fi</sup>cient for the linear, quadratic, and logarithmic models

![](/api/attachments/3XC8R6UN/fulltext/images/e0e757858eb16a4cc9d4ee44ef6730b887d7ba5ff8cc3d8b390b61a242c4ffc2.jpg)  
Fig. 7. Association rules for database-1

Using the same conditions, a total of 54 association rules are generated from database-2. Similarly, the generated rules are plotted on the contour map of extracted probability, as shown in Fig. 8. It can be seen that the extracted probabilities of all rules are smaller than 0.1. Moreover, the results show that 48 association rules are left by the linear and the quadratic models, and 14 association rules are left by the logarithmic model.

For a database containing many items with high support ratios, the extracted probability of association rules is probably high. Conversely, for a database containing many items with low support ratios, the extracted probability of association rules is probably low. From the examples displayed above, it can be seen that the linear model and the quadratic model can obtain better results for databases with higher support ratios (e.g. database-1), and the logarithmic model can obtain better ones for databases with lower support ratios (e.g. database-2). The cases demonstrate how the proposed methods can <sup>fi</sup>nd interesting association rules with weak extracted probability according to the characteristics of a database.

Furthermore, we compared the extracted probability proposed in this article with the interest measurement [5]. In the probability theory, $p ( X \cup Y ) \approx p ( X ) p ( Y )$ denotes that X is approximately independent of Y. This means that $X \Rightarrow Y$ cannot be extracted as a rule if $p ( X \cup Y ) \approx p ( X ) p ( Y )$ . A statistical de<sup>fi</sup>nition of dependence for X and Y is: Interest $( X , Y ) = p ( X \cup Y ) / p ( X ) p ( Y )$ . The further the value is from 1, the greater the dependence. Or the further the value |Interest(X, Y) − 1| is from 0, the greater the dependence. For 1 N mininterest N 0, if |Interest(X, Y) 1| mininterest, then $X \Rightarrow Y$ is a rule of interest [28]. In database-1, the extracted probability of the rules whose value of |Interest (X, Y) − 1| is close to 0 is higher, as shown in Fig. 9. That is, the rules pruned by interest measurement are probably pruned by the proposed method for their high extracted probability. Similar results are attained in database-2, but their tendency is not as strong as that in database-1, as shown in Fig. 10. This accounts for the fact that the value of |Interest (X, Y) − 1| of only one rule in database-2, but 28 rules in database-1, is lower than 10%, since mininterest is seldom de<sup>fi</sup>ned as a value greater than10%. After all, the extracted probability can be also used to prune the rules whose itemsets are independent of each other, as interest measurement can.

![](/api/attachments/3XC8R6UN/fulltext/images/ce3ea41fd412e79e9e5bf52accb7652fda03ea25b5021daeccb891ef23c5ba19.jpg)  
Fig. 8. Association rules for database-2.

![](/api/attachments/3XC8R6UN/fulltext/images/870745176ac8472d5ed2d27c8f10450276f9eee1d18005267e58a49d9848b9b9.jpg)  
Fig. 9. |Interest (X, Y) −1| and extracted probability of rules for database-1.

![](/api/attachments/3XC8R6UN/fulltext/images/7b4df9a10df4e3b9e433777c63d9883e41b749deba0fef79a3c6fd6eb817d682.jpg)  
Fig. 10. |Interest (X, Y)−1| and extracted probability of rules for database-2

![](/api/attachments/3XC8R6UN/fulltext/images/b04832d10879ee99e6d4f0a462e9439611942c6f3872c4535764b713b3d96ca9.jpg)  
Fig. 11. Distribution of extracted probability for rules generated from UCI Adult dataset

![](/api/attachments/3XC8R6UN/fulltext/images/c2cf64274b05ac85703b70b901ba73d00f011a1d78b5e7c00311acf6da1385b2.jpg)  
Fig. 12. Distribution of con<sup>fi</sup>dence for rules generated from UCI adult dataset.

## 3.5. UCI Adult dataset test

For elaborating on the semantics of the resulting rules, we use the Adult dataset from the UCI machine learning repository [3]. The data were extracted from the U.S. census bureau database, and it contains 48842 instances with 14 attributes like age, work class, education, etc. This article divides each attribute into several categories and removes the two attributes fnlwgt and education-num [13]. For cases with missing values, all items corresponding to the attributes with the missing values were set to the highest frequent value.

On condition that the minimum support and the minimum con<sup>fi</sup>dence are 1% and 60% respectively, a total of 179658 association rules are generated for any itemset with a maximum of 5 items. The value of extracted probability of 122623 rules is nearly one (≧0.99), which accounts for 68% of all generated rules, as shown in Fig. 11. The rules are sorted by the value of extracted probability, and Rule No. is determined in sequence. The result shows that most of the generated rules are inevitable. On the other hand, the resulting rules left by interest measurement and the proposed methods are shown in Fig. 12. The rules are sorted by the value of con<sup>fi</sup>dence in Fig. 12, and Rule No. is determined in sequence. Less than 27% of rules are left by the proposed methods, and about 50% of rules are left by interest measurement for mininterest=10%.

An interesting but unapparent rule, {education:Prof-school} ⇒ {income:N50 K}, is picked out for illustrating the semantics of the resulting rules. The support, con<sup>fi</sup>dence and extracted probability of that rule are 1.3%, 76.5% and 0% respectively. When sorted by the value of con<sup>fi</sup>dence, the rule has been risen from Rule No. 120261 to 16628 by the logarithmic model but merely to 49595 by interest measurement for mininterest=10%. It shows that the generated rule based on extracted probability is not only less inevitable, but also less probably excluded from association rules for its low con<sup>fi</sup>dence.

Table 1  
1-item support analysis of factors.

<table><tr><td colspan="3">Factor</td><td>Percent (%)</td></tr><tr><td rowspan="13">Cause of injury</td><td>CAU1</td><td>Falls</td><td>51.9</td></tr><tr><td>CAU2</td><td>Collapses</td><td>16.0</td></tr><tr><td>CAU3</td><td>Electric shocks</td><td>10.5</td></tr><tr><td>CAU4</td><td>Falling objects</td><td>5.4</td></tr><tr><td>CAU5</td><td>Struck by and against</td><td>4.9</td></tr><tr><td>CAU6</td><td>Caught in between, and clamped</td><td>2.4</td></tr><tr><td>CAU7</td><td>Drowning</td><td>2.4</td></tr><tr><td>CAU8</td><td>Traffic accidents</td><td>1.1</td></tr><tr><td>CAU9</td><td>Explosions</td><td>0.9</td></tr><tr><td>CAU10</td><td>Fires</td><td>0.5</td></tr><tr><td>CAU11</td><td>Falls on the same level</td><td>1.6</td></tr><tr><td>CAU12</td><td>Contacting hazardous materials and/or extreme temperatures</td><td>1.1</td></tr><tr><td>CAU13</td><td>Others</td><td>1.3</td></tr><tr><td rowspan="2">Whether the project is public</td><td>PUB1</td><td>Yes</td><td>45.0</td></tr><tr><td>PUB2</td><td>No</td><td>55.0</td></tr><tr><td rowspan="4">Month</td><td>MON1</td><td>January, February, March</td><td>19.6</td></tr><tr><td>MON2</td><td>April, May, June</td><td>26.4</td></tr><tr><td>MON3</td><td>July, August, September</td><td>30.2</td></tr><tr><td>MON4</td><td>October, November, December</td><td>23.8</td></tr><tr><td rowspan="2">Whether it rains</td><td>RAI1</td><td>Yes</td><td>34.8</td></tr><tr><td>RAI2</td><td>No</td><td>65.2</td></tr><tr><td rowspan="2">Mean accumulated rainfall</td><td>ACC1</td><td>Under 10 mm</td><td>19.5</td></tr><tr><td>ACC2</td><td>Over 10 mm</td><td>15.3</td></tr></table>

![](/api/attachments/3XC8R6UN/fulltext/images/81b70fee21c1627fd2c5ad8807dec8601b32dfe2ea3b16a271f03ac50ef70002.jpg)  
Fig. 13. Association rule mining results for occupational injuries in the Taiwan construction industry.

When examining all rules, we found that a total of 147341 rules, about 82%, are concerned with {capital-gainb=0}, {capital-lossb=0} and {native-country:United-States}. This can be attributed to all the three attributes having support higher than 90%. Consequently, the result proves that a database with wide range of support seems to generate more inevitable rules. At the same time, we also found some generated rules obviously inevitable. Take two rules for example: {relationship:Husband}⇒{marital-status:Married-civ-spouse} (con-<sup>fi</sup>dence=1.0, support=0.4, extracted probability=1) and {relationship: Husband}⇒{sex:Male} (con<sup>fi</sup>dence = 1.0, support = 0.4, extracted probability = 0). The modi<sup>fi</sup>ed con<sup>fi</sup>dence of the above rules is zero and one respectively. It shows that the proposed method can be applied to aid in determining whether a rule is inevitable based on the probability theory. It cannot exclude all rules with inevitable semantics from association rules. In other words, this article is not intended to discover all interesting rules but unapparent rules.

## 4. Application

The proposed method is then applied to a real-world accident database to illustrate how it can effectively generate interesting rules in practice.

## 4.1. Accident database

This article analyzed 1062 cases of fatal occupational injuries in the construction industry during the period from 2000 to 2005. All fatality cases were extracted from the database collected by the Council of Labor Affairs of Taiwan. Each accident can be described in terms of a causal sequence of events and factors extending back in time from the accident [26]. Moreover, being one of the relevant factors selected in this article, the information about rainfall density was extracted from the database collected by the Central Weather Bureau of Taiwan.

A total of 5 attributes are considered in our analysis, including cause of injury, whether the project is public or not, month of year, whether it rains or not, and the mean accumulated rainfall. Each attribute was classi<sup>fi</sup>ed into several useful categories as shown in Table 1.

Table 2  
Association rules generated by the primary method (for minimum con<sup>fi</sup>dence=80%).

<table><tr><td rowspan="2">Rule ID</td><td colspan="7">Association rules</td><td rowspan="2">Confidence(%)</td><td rowspan="2">Extracted probability(%)</td></tr><tr><td colspan="5">X</td><td> $\Rightarrow$ </td><td>Y</td></tr><tr><td>1</td><td>CAU1</td><td>&amp;</td><td>PUB2</td><td>&amp;</td><td>MON1</td><td> $\Rightarrow$ </td><td>RAI2</td><td>80.3</td><td>0.2</td></tr><tr><td>2</td><td>CAU1</td><td>&amp;</td><td>PUB1</td><td>&amp;</td><td>MON4</td><td> $\Rightarrow$ </td><td>RAI2</td><td>80.0</td><td>3.3</td></tr></table>

Note: 1. Rules 1 and 2 are denoted as Rules P and Rule Q respectively.

Association rules generated by the logarithmic model (for minimum con<sup>fi</sup>dence=70%).

<table><tr><td rowspan="2">Rule ID</td><td colspan="7">Association rules</td><td>Modified confidence</td><td>Extracted probability</td></tr><tr><td>X</td><td></td><td></td><td></td><td></td><td>⇒</td><td>Y</td><td>(%)</td><td>(%)</td></tr><tr><td>1</td><td>CAU5</td><td></td><td></td><td></td><td></td><td>⇒</td><td>PUB1</td><td>78.635</td><td>0.009</td></tr><tr><td>2</td><td>CAU2</td><td>&amp;</td><td>RAI1</td><td></td><td></td><td>⇒</td><td>PUB1</td><td>78.075</td><td>0.002</td></tr><tr><td>3</td><td>CAU2</td><td>&amp;</td><td>MON2</td><td></td><td></td><td>⇒</td><td>PUB1</td><td>77.38</td><td>0.027</td></tr><tr><td>4</td><td>CAU2</td><td>&amp;</td><td>ACC2</td><td></td><td></td><td>⇒</td><td>PUB1</td><td>75.925</td><td>0.232</td></tr><tr><td>5</td><td>CAU2</td><td>&amp;</td><td>MON1</td><td></td><td></td><td>⇒</td><td>PUB1</td><td>75.085</td><td>0.121</td></tr><tr><td>6</td><td>CAU2</td><td>&amp;</td><td>ACC1</td><td></td><td></td><td>⇒</td><td>PUB1</td><td>75.085</td><td>0.121</td></tr><tr><td>7</td><td>CAU1</td><td>&amp;</td><td>MON4</td><td></td><td></td><td>⇒</td><td>PUB2</td><td>74.92</td><td>0.007</td></tr><tr><td>8</td><td>CAU2</td><td>&amp;</td><td>MON3</td><td></td><td></td><td>⇒</td><td>PUB1</td><td>73.985</td><td>0.032</td></tr><tr><td>9</td><td>CAU1</td><td>&amp;</td><td>MON3</td><td>&amp;</td><td>RAI2</td><td>⇒</td><td>PUB2</td><td>73.895</td><td>0.146</td></tr><tr><td>10</td><td>CAU1</td><td>&amp;</td><td>MON4</td><td>&amp;</td><td>RAI2</td><td>⇒</td><td>PUB2</td><td>73.73</td><td>0.051</td></tr><tr><td>11</td><td>PUB2</td><td>&amp;</td><td>MON2</td><td>&amp;</td><td>RAI2</td><td>⇒</td><td>CAU1</td><td>73.63</td><td>0.001</td></tr><tr><td>12</td><td>CAU3</td><td>&amp;</td><td>PUB2</td><td>&amp;</td><td>RAI1</td><td>⇒</td><td>MON3</td><td>73.39</td><td>0*</td></tr><tr><td>13</td><td>CAU2</td><td></td><td></td><td></td><td></td><td>⇒</td><td>PUB1</td><td>72.95</td><td>0*</td></tr><tr><td>14</td><td>CAU1</td><td>&amp;</td><td>RAI2</td><td></td><td></td><td>⇒</td><td>PUB2</td><td>72.85</td><td>0*</td></tr><tr><td>15</td><td>PUB2</td><td>&amp;</td><td>MON4</td><td>&amp;</td><td>RAI2</td><td>⇒</td><td>CAU1</td><td>72.54</td><td>0.001</td></tr><tr><td>16</td><td>CAU5</td><td>&amp;</td><td>RAI2</td><td></td><td></td><td>⇒</td><td>PUB1</td><td>72.42</td><td>0.121</td></tr><tr><td>17</td><td>CAU1</td><td>&amp;</td><td>MON2</td><td>&amp;</td><td>RAI2</td><td>⇒</td><td>PUB2</td><td>71.52</td><td>0.094</td></tr><tr><td>18</td><td>PUB2</td><td>&amp;</td><td>MON2</td><td></td><td></td><td>⇒</td><td>CAU1</td><td>70.95</td><td>0*</td></tr><tr><td>19</td><td>CAU1</td><td>&amp;</td><td>MON3</td><td></td><td></td><td>⇒</td><td>PUB2</td><td>70.455</td><td>0.002</td></tr><tr><td>20</td><td>CAU1</td><td>&amp;</td><td>ACC1</td><td></td><td></td><td>⇒</td><td>PUB2</td><td>70.235</td><td>0.079</td></tr><tr><td>21</td><td>CAU1</td><td>&amp;</td><td>PUB2</td><td></td><td></td><td>⇒</td><td>RAI2</td><td>70.18</td><td>0.144</td></tr><tr><td>22</td><td>CAU1</td><td></td><td></td><td></td><td></td><td>⇒</td><td>PUB2</td><td>70.07</td><td>0*</td></tr><tr><td>23</td><td>PUB2</td><td>&amp;</td><td>MON4</td><td></td><td></td><td>⇒</td><td>CAU1</td><td>70.04</td><td>0*</td></tr></table>

Note: 1. Rule 12 is denoted as Rule R. 2. ⁎Extracted probabilityb0.001%.

## 4.2. Results

In general, an association rule is considered relevant if it at least satis<sup>fi</sup>es minimum support, and con<sup>fi</sup>dence thresholds de<sup>fi</sup>ned by users. The minimum support employed in this analysis is 2%. Different con<sup>fi</sup>dence thresholds, including 90%, 80%, 70%, and 60%, are adopted for comparison. Afterwards, the proposed method is used to sieve out the interesting association rules from the database. The results of association rule mining are shown in Fig. 13.

On condition that the minimum con<sup>fi</sup>dence is 90%, no association rules are generated. On condition that the minimum con<sup>fi</sup>dence is 80%, a total of 2 association rules are generated by the primary method (denoted as Rule P and Rule Q). As the extracted probabilities of the 2 rules are not low enough, as shown in Table 2, both rules are eliminated by the quadratic and the logarithmic model. It can be shown that the 2 rules are inevitable association rules. In semantics, it can be seen in both rules that most occupational falls happened when there was no rain in spring and winter. This may be because there is frequently no rain in those two seasons. In fact, days with no rain account for 70% and 75% of spring and winter respectively. It shows once again that the two rules are not interesting association rules.

On condition that the minimum con<sup>fi</sup>dence is 70%, a total of 37 association rules are generated by the primary method. When the logarithmic model is adopted to modify the con<sup>fi</sup>dence, 23 association rules are left, as shown in Table 3. In particular, the probabilities of 6 out of the 23 association rules are smaller than 0.001%. It can be seen that the derived results are out of the ordinary and considerably interesting. When we examine the 6 association rules, the result in rule 12 (denoted as Rule R), concerned with the connection between electric shocks and meteorological phenomena, is rather interesting. It can be seen in Rule R that 73.4% of occupational injuries involve electric shocks, happen on private jobs and occur on rainy days in autumn. In fact, rainy days account for 43% of days in autumn. The result shows that Rule R is an interesting association rule undeniably. By the way, the extracted probabilities of Rule P and Rule Q have risen to 24% and 16% respectively. As the extracted probability of rule P and Q strongly varies with con<sup>fi</sup>dence threshold, the 2 rules can be noted as merely inevitable association rules.

Subsequently, for the purpose of con<sup>fi</sup>rming that Rule R is interesting, the minimum con<sup>fi</sup>dence of 60% is employed. When the logarithmic model is adopted, the modi<sup>fi</sup>ed con<sup>fi</sup>dence of Rule R has risen to second. The result con<sup>fi</sup>rms that Rule R is an interesting association rule indeed.

For the further interpretation, we examine the rules generated by the primary method at a minimum con<sup>fi</sup>dence of 60%. The relationship between minimum con<sup>fi</sup>dence thresholds and the extracted probabilities of each rule are shown in Fig. 14. It can be seen that the extracted probability declines with the advancing minimum con-<sup>fi</sup>dence threshold. The curve will end in the maximum con<sup>fi</sup>dence threshold that each rule can satisfy. When a curve lingers in the region of low probabilities for a longer distance, the possibility that the corresponding rule has low extracted probability is stronger. In other words, those rules are considered more probably interesting association rules.

In Fig. 14, it can be seen that the extracted probability of the association rules generated by the logarithmic model (denoted by thick lines) changes slightly using a minimum con<sup>fi</sup>dence threshold above 60%. Most extracted probabilities of Rules P and Q are over 0.1, as shown in Fig. 15. By contrast, little of the corresponding curves of Rules P and Q linger in the region of low probabilities. Even though satisfying the relative maximum con<sup>fi</sup>dence thresholds, Rules P and Q are inadequate for interesting association rules so that they are eliminated by the logarithmic model. Besides, the corresponding curve of Rule R ends in a middle-to-high con<sup>fi</sup>dence threshold (73%), and it lingers in the extracted probability smaller than 0.1 area of the graph for a long distance (from minimum con<sup>fi</sup>dence of 41% to 73%), as shown in Fig. 15. The result shows that Rule R can be an interesting association rule, and it conforms to the result derived from the logarithmic model.

![](/api/attachments/3XC8R6UN/fulltext/images/3192fd597940c2679f2b029cd651eff8d14fa27b132e708ec32532008b150a60.jpg)  
Fig. 14. Extracted probability curves of the primary method and logarithmic model.

![](/api/attachments/3XC8R6UN/fulltext/images/90a5c11724ffaebbca4c121671117f464860cae3aecfbfee41d475e0a0ca433c.jpg)  
Fig. 15. Extracted probability curves of Rules P, Q and R.

## 5. Conclusions

In this article, we have introduced an “extracted probability” measure for mining association rules. Using this measure, 3 models are presented to modify the con<sup>fi</sup>dence of rules. An ef<sup>fi</sup>cient method based on the support-con<sup>fi</sup>dence framework is then developed to generate association rules of interest. The numbers of association rules obtained by the proposed method are fewer than those obtained by the support-con<sup>fi</sup>dence framework. In addition, a contour map of extracted probability is proposed to examine the results of association rule mining, and it can be employed to determine the probability that the rules are inclined to be inevitable association rules in a database according to the support range of attributes. Finally, the analysis of fatal occupational injuries in this article reveals that the proposed methods can effectively generate interesting rules from a variety of association rules. Similar methods may also be useful in other areas.

However, the readers must note that this article is not intended to discover all interesting rules but, rather, unapparent rules. There may be other measures of interestingness that can result in other interesting rules. It is widely accepted that no single measure is superior to all others or suitable for all applications. Since this article incorporates neither the context of the domain of application nor the goals and background knowledge of the user, it is desirable to develop new methods to facilitate the user's involvement. As all 3 models yield modi<sup>fi</sup>cations of different degree, which models should be adopted depends on the user's mining requirements. Furthermore, it is very important to consider the numeric values of the thresholds. As no natural boundary of the thresholds exists, and it was not discussed in this article, further works or other methods such as fuzziness will be required [21].

## References

[1l R. Agrawal T. Imielinski A. Swami Mining association rules between sets of items in large databases, Proceedings of the 1993 ACM SIGMOD International Conference on Management of Data, USA, Washington, DC, 1993, pp. 207–216.

[2] E. Baralis, G. Psaila, Designing templates for mining association rules, Journal of Intelligent Information Systems 9 (1997) 7–32

[3] C.L. Blake and C.J. Merz, UCI Repository of Machine Learning Databases, http:// www.ics.uci.edu/\~mlearn/MLRepository.html.

[4] D. Boley, M. Gini, R. Gross, E.H.S. Han, K. Hastings, G. Karypis, V. Kumar, B. Mobasher, J. Moore, Partitioning-based clustering for web document categorization, Decision Support Systems 27 (1999) 329–341.

[5] S. Brin, R. Motwani, C. Silverstein, Beyond market baskets: generalizing association rules to correlations, Proceedings of the 1997 ACM SIGMOD International Conference on Management of Data, USA, Tucson, AZ, 1997, pp. 265–276.

[6] S. Brin, R. Motwani, J.D. Ullman, S. Tsur, Dynamic itemset counting and implication rules for market basket data, Proceedings of the 1997 ACM SIGMOD Internationa Conference on Management of Data, USA, Tucson, AZ, 1997, pp. 255–264

[7] Y.M. Chae, S.H. Ho, K.W. Cho, D.H. Lee, S.H. Ji, Data mining approach to policy analysis in a health insurance domain, International Journal of Medical Informatics 62 (2001) 103–111.

[8] G. Chen, H. Liu, L. Yu, Q. Wei, X. Zhang, A new approach to classi<sup>fi</sup>cation based on association rule mining, Decision Support Systems 42 (2006) 674–689.

[9] Y.-L. Chen, K. Tang, R.-J. Shen, Y.-H. Hu, Market basket analysis in a multiple store environment, Decision Support Systems 40 (2005) 339–354.

[10] M.N.M. García, L.A.M. Quintales, F.J.G. Penãlvo, M.J.P. Martín, Building knowledge discovery-driven models for decision support in project management, Decision Support Systems 38 (2004) 305–317.

[11] L. Geng, H.J. Hamilton, Interestingness measures for data mining: a survey, ACM Computing Surveys 38 (2006) 1–32.

[12] B. Gray, M.E. Orlowska, CCAIIA: clustering categorical attributes into interesting association rules, Proceedings of the Second Paci<sup>fi</sup>c-Asia Conference on Knowledge Discovery and Data Mining (PAKDD-98), Australia, Melbourne, 1998, pp. 132-143.

[13] M. Hahsler, B. Grün, K. Hornik, Arules — a computational environment for mining association rules and frequent item sets. Journal of Statistical Software 14 (15) (2005) 1–25.

[14] N.C. Hsieh, An integrated data mining and behavioral scoring model for analyzing bank customers, Expert Systems with Applications 27 (2004) 623–633.

[15] Y.-H. Hu, Y.-L. Chen, Mining association rules with multiple minimum supports: a new mining algorithm and a support tuning mechanism, Decision Support Systems 42 (2006) 1–24.

[16] Z. Huang, J. Li, H. Su, G.S. Watts, H. Chen, Large-scale regulatory network analysis from microarray data:modi<sup>fi</sup>ed Bayesian network learning and association rule mining, Decision Support Systems 43 (2007) 1207–1225.

[17] N. Jukić, S. Nestoroy, Comprehensive data warehouse exploration with qualified association-rule mining, Decision Support Systems 42 (2006) 859–878.

[18] N. Lavrac, P. Flach, B. Zupan, Rule evaluation measure: a unifying view, Proceedings of the 9th International Workshop on Inductive Logic Programming (ILP-99), Springer-Verlag, Bled, Slovenia, 1999, pp. 174–185.

[19] B. Liu, Y. Ma, C.K. Wang, P.S. Yu, Scoring the data using association rules, Applied Intelligence 18 (2003)119–135

[20] B. Padmanabhan, A. Tuzhilin, Knowledge re<sup>fi</sup>nement based on the discovery of unexpected patterns in data mining, Decision Support Systems 33 (2002) 309–321.

[21] W. Pedrycz, F. Gomide, Fuzzy Systems Engineering: Toward Human-Centric Computing, John Wiley & Sons, Inc., Hoboken, New Jersey, 2007.

[22] P. Tan, V. Kumar, Interestingness measure for association patterns: a perspective, Technical Report # TR00-036, Department of Computer Science, University of Minnesota. 2000.

[23] P. Tan, V. Kumar, J. Srivastava, Selecting the right interestingness measure for association patterns, Proceedings of the 8th International Conference on Knowledge Discovery and Data Mining (KDD 2002) Canada Edmonton 2002, pp. 32–41

[24] Y.J. Tsay, J.Y. Chiang, CBAR: an ef<sup>fi</sup>cient method for mining association rules, Knowledge-Based Systems 18 (2005) 99–105.

[25] M.S. Tsechansky, N. Pliskin, G. Rabinowitz, A. Porath, Mining relational patterns from multiple relational tables, Decision Support Systems 27 (1999) 177–195.

[26] A.M. Williamson, A.-M. Feyer, D.R. Cairns, Industrial differences in accident causation, Safety Science 24 (1996) 1–12

[27] Y.Y. Yao, N. Zhong, An analysis of quantitative measure associated with rules, Proceedings of the Third Paci<sup>fi</sup>c-Asia Conference on Knowledge Discovery and Data Mining (PAKDD-99), Beijing, China, 1999, pp. 479–488.

[28] C. Zhang, S. Zhang, Association Rule Mining: Models and Algorithms, Springer, New York, 2002.

Miss Liao received her B.S. degree in Civil Engineering from National Central University, Jhongli, Taiwan and the M.S. degree in Construction Engineering from National Taiwan University of Science and Technology, Taipei, Taiwan. She is the PhD candidate in Architecture from National Taiwan University of Science and Technology, Taipei, Taiwan.

Dr. Perng received his B.S. degree in Architecture from National Cheng Kung University, Tainan, Taiwan, the M.S. Degree in Architecture from National Cheng Kung University, Tainan, Taiwan, and the Ph.D. degree in Construction Management from the University of Texas at Austin.

Mr. Chiang received his B.S. degree in Civil Engineering from National Central University, Jhongli, Taiwan and the M.S. degree in Civil Engineering from National Taiwan University Taipei, Taiwan
