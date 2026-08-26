---
otero_id: 16110
otero_key: "QE9VVXYD"
title: "Pricing and disseminating customer data with privacy awareness"
authors: "Xiao-Bai Li; Srinivasan Raghunathan"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.10.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Xiao-Bai Li <sup>a,</sup>⁎, Srinivasan Raghunathan 1

<sup>a</sup> Department of Operations & Information Systems, University of Massachusetts Lowell, United States

<sup>b</sup> School of Management, University of Texas at Dallas, United States

## a r t i c l e i n f o

Article history: Received 15 January 2013 Received in revised form 6 September 2013 Accepted 21 October 2013 Available online 29 October 2013

Keywords: Privacy Pricing Incentive compatibility Data mining Data analytics

## a b s t r a c t

Organizations today regularly share their customer data with their partners to gain competitive advantages. They are also often requested or even required by a third party to provide customer data that are deemed sensitive. In these circumstances, organizations are obligated to protect the privacy of the individuals involved while still bene<sup>fi</sup>ting from sharing data or meeting the requirement for releasing data. In this study, we analyze the tradeoff between privacy and data utility from the perspective of the data owner. We develop an incentive-compatible mechanism for the data owner to price and disseminate private data. With this mechanism, a data user is motivated to reveal his true purpose of data usage and acquire the data that suits to that purpose. Existing economic studies of information privacy primarily consider the interplay between the data owner and the individuals, focusing on problems that occur in the collection of private data. This study, however, examines the privacy issue facing a data owner organization in the distribution of private data to a third party data user when the real purpose of data usage is unclear and the released data could be misused.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In recent years, there has been a rapid increase in collecting and sharing personal data, owing to widespread use of the Internet and database technologies. Along with this unprecedented growth of activities to collect and share data, data mining and analytics technologies have gained popularity in a wide variety of domains, including database marketing, credit and loan evaluation, web usage/clickstream analysis, medical research and crime analysis. As a result, the buying and selling of customer data have become a multibillion-dollar business [29]. While organizations have bene<sup>fi</sup>ted from information sharing and successful application of data mining and analytics, there are increasing concerns about invasions to privacy caused by these practices.

Data marketers such as Acxiom, LexisNexis and ChoicePoint (acquired by Reed Elsevier in 2008) are among the major players in the business of buying and selling consumer data. These companies collect and combine personal data from multiple public and private sources and sell them to retailers, banks, insurance <sup>fi</sup>rms, and government agencies. Protecting individual privacy is essential for the survival and success of these businesses. Credit bureaus, such as Equifax, Experian and TransUnion, are another category of <sup>fi</sup>rms that are heavily involved in the business of buying and selling consumer data, albeit in a more regulated environment. In addition to disseminating data to external parties, it is a common practice for organizations to share customer data among af<sup>fi</sup>liations and supply-chain partners.

Non-pro<sup>fi</sup>t organizations have also taken advantage of the value of personal information. The College Board, which organizes standardized tests for college admission, provided about 1700 colleges and universities with lists of students who matched requested SAT and PSAT test score ranges and other demographic information, at a cost of 28 cents per student [29]. The Center for Medicare and Medicaid Services, a federal agency, sells individual Medicare and Medicaid claims data to third parties, which include an individual's medical, demographic, geographic, and <sup>fi</sup>nancial information (http://www.resdac.org/). The center's operations follow the guidelines of the Health Insurance Portability and Accountability Act (HIPAA). However, studies have shown that the HIPAA rules may be insuf<sup>fi</sup>cient in protecting patient privacy [2,27].

Privacy-related data sharing and distribution also take place without a direct monetary context, particularly when governments are involved. In 2005, the Department of Justice (DOJ) asked Google Inc. to turn over millions of users' search queries in order to pursue a study into Internet pornography. Google rejected the DOJ's demand, citing that this would undermine the users' trust in Google's ability to keep their information private. This incident aroused intense public debates. A poll [12] revealed that 51% of the respondents believed Google should not release search data to the DOJ, while 43% thought otherwise. The case eventually ended up with a federal judge ruling that Google should provide 50,000 URLs to the DOJ, with individual URLs being randomly selected [7]. The amount of the data is signi<sup>fi</sup>cantly smaller than that of requested by the DOJ initially, and no identity attributes were included.

Clearly, it is not easy for an organization to make a right decision that provides adequate protection for the privacy of the individuals involved while still bene<sup>fi</sup>ting from sharing or selling the data, or meeting the requirement for data release. A main source of dif<sup>fi</sup>culty is that the real purpose of the data user is usually unknown to the data owner organization and thus the released data could be misused. For example, the Google search query data initially requested by the DOJ can be used either to study general browsing patterns or to help investigate individual cases. Similarly, the same consumer data acquired from a data provider like Acxiom could be used either for macro-level marketing research or for personalized target marketing.

This study takes an economics-based approach to the privacy problem in data sharing and dissemination. We consider a data sharing or disseminating activity as an economic transaction where personal data is viewed as an economic good. The tradeoff between privacy and data utility is analyzed and modeled from the standpoint of a data owner organization. We develop a pricing mechanism for the data owner to collect and distribute sensitive data. This mechanism takes into consideration the differences in the utility of different types of data users for data of different sensitivity levels and provides incentive for a data user to reveal his true purpose of data usage and acquire the data that suits to that purpose. To the best of our knowledge, this work is the <sup>fi</sup>rst economics-based study that addresses the privacy issue facing a data owner regarding how to disseminate sensitive data to a third party data user. This is a main contribution of the paper.

The rest of the paper is organized as follows. Section 2 presents a review of related research work. In Section 3, we formulate our privacy problem, present our decision models, and discuss their analytical properties. We then provide an illustrative example in Section 4, followed by practical insights in Section 5. Section 6 concludes the paper by discussing limitations of this work and offering directions for future research.

## 2. Literature review

Information privacy has been studied extensively from different perspectives at individual, organizational and societal levels [3,22,26]. There are typically three parties involved in the privacy problem in data dissemination: (i) the data owner (the organization that owns the data) who wants to bene<sup>fi</sup>t from disseminating data while ful<sup>fi</sup>lling the obligation of protecting privacy; (ii) individuals who provide their personal data to the data owner and want their privacy protected; and (iii) the third party data user who acquires data from the data owner; this third party can be either a legitimate user or a privacy invader.

From a privacy viewpoint, the attributes (or variables) in data involving people can be classi<sup>fi</sup>ed into three categories: (i) identifying attributes, which explicitly describe the identity of an individual, such as social security number, name, phone number and credit card number; (ii) confidential attributes, which contain private information that an individual typically does not want revealed, such as salary, medical test results, and sexual orientation; and (iii) quasi-identifier attributes [27], which are normally not considered as con<sup>fi</sup>dential by individuals, such as age, gender, race, education, and occupation. However, the values of these attributes can often be used to match the values of identifying attributes from different data sources, resulting in disclosure of individual identities. For instance, Sweeney [27] found out that 87% of the population in the United States can be uniquely identi<sup>fi</sup>ed with three attributes – gender, date of birth, and 5-digit zip code – which are accessible from voter registration records available to the public. The identifying attributes alone typically do not cause privacy problems. For example, the name, phone number and address of an individual can usually be found from a white-page telephone book. Privacy concerns arise when the identifying or quasi-identi<sup>fi</sup>er attributes are released together with con<sup>fi</sup>dential attributes. In this paper, we use the term sensitivity to refer to the risk of disclosing both identity and con<sup>fi</sup>dential attributes.

In the area of data privacy research, computing technology-based approaches attempt to resolve the con<sup>fl</sup>ict between privacy protection and data sharing at operational levels. The majority of these approaches use a data masking technique, such as perturbation, swapping, generalization, and suppression, to alter the original data such that, while the individuals in the data are well protected, the utility of the data is also reasonably preserved in the masked version for distribution [1,11,21,27,30]. There are two related limitations in technology-based approaches. First, these approaches conservatively assume that a data user should be considered as a potential privacy invader. When this is not true, that is, when the released data are used for legitimate purposes, data utility is more or less weakened due to masking of data to protect privacy. Second, these approaches typically assume that the data released will be used to <sup>fi</sup>nd aggregate information or collective patterns in the data. Therefore, identifying attributes are almost always removed or encrypted in the released data processed by a technologybased method. However, in some data sharing and mining applications, such as in database marketing, disease outbreak detection, and crime analysis, individual identities and sensitive data have to be released in order for the data to be useful. Technology-based approaches are generally not applicable to such situations. It is dif<sup>fi</sup>cult to overcome these limitations with a technology-based approach alone because the problems involve not only operational-level but also policylevel issues.

Economics-based studies focus more on the policy-level privacy issues. Laudon [17] introduces the idea of a regulated National Information Market (NIM) that could allow personal information to be bought and sold like a commodity. In NIM, individuals would decide whether or how much their personal information can be released for secondary use, and data collectors and users would pay for the collection and use of this information. However, no mechanism to implement NIM is provided by Laudon [17] and the idea has not been put into practice so far.

Based on a comprehensive review of the literature [14], the main body of economics-based privacy research generally deals with the relationship between a data owner and individuals, focusing on problems occurring in the collection of private data. In particular, an interesting study [13] concerns monetary incentive related to privacy. The study <sup>fi</sup>nds that individuals are generally willing to trade off their privacy for economic bene<sup>fi</sup>ts. The study also provides the experimental results in terms of dollar value for secondary use of personal information. The <sup>fi</sup>ndings of this study validate the assumption that personal data can be viewed as economic goods and the transaction of such data can be analyzed with economics tools.

Gar<sup>fi</sup>nkel et al. [10] propose a mechanism that integrates a data masking technique into an economic model. The mechanism allows individuals to dynamically specify and revise their privacy protection levels, which are tied to their compensation amount to be paid by the data user. The mechanism is, however, closely related to a speci<sup>fi</sup>c data masking technique [11] and thus is somewhat limited in its application domains. The mechanism we propose is more general and is not tied to any speci<sup>fi</sup>c technology-based approach.

In summary, economics-based research focuses on analysis and modeling of privacy problems at the individual level. There is a lack of privacy research at the organizational level [3]. To <sup>fi</sup>ll in this gap, this research develops an economics mechanism to address the privacy issue that arises at policy and organizational level when the data owner organization disseminates individuals' data to a third party data user, after individual data have been collected. This is new to the literature. This work provides economics analysis and models that facilitate the implementation of Laudon's idea of information market. The proposed mechanism alleviates the limitations of the technologybased approach mentioned above. Our approach should be viewed as a mechanism to complement, rather than to substitute, the existing technology-based approaches. In fact, our approach requires that technology exists to mask data and offer them at different protection levels. Practically, a data owner can use this mechanism together with a technology-based approach to simultaneously protect individual privacy and enable effective data usage, at both policy and operational levels.

Our approach is based on the vertical differentiation framework in economics and marketing [23,24,9]. In that framework, a seller offers products with multiple quality levels at different prices to consumers who are heterogeneous in their valuation of quality. Since the seller does not know about an individual customer's type, she has to design an incentive-compatible quality-price combination so that a customer self-selects the product targeted for that customer. In our model, the sensitivity level of the information offered is analogous to the product quality. In addition to sensitivity, however, we also consider the amount of data as a choice variable for a data consumer. Particularly, due to the nature of our data privacy problem, our model departs from the “single crossing” condition that is typically assumed in the conventional vertical differentiation model. As a result, the models we develop are richer than those in the basic vertical differentiation literature.

## 3. The proposed pricing scheme

Like the basic vertical differentiation framework, we assume that the data owner acts as a monopoly. This is indeed true in most data sharing cases, because customer data owned by an organization is typically tied to the organization's business and thus is unique in its characteristics. We consider situations where the data acquired by the data consumer cannot be resold to another party. This is a reasonable scenario because the data owners can include this condition in the contract with the data consumer [5,6]. We should also point out that the term “consumer” in existing privacy studies typically refers to the individuals who want their privacy protected, while in this study the “consumer” refers to the third party data user. As such, we will use the term “(third party) data user” and “data consumer” interchangeably in this paper.

Many data analysis and data mining tasks focus on <sup>fi</sup>nding aggregate information, or discovering collective patterns in the data and relationships between attributes. For these tasks, identifying attributes are generally not useful because it is unlikely that a collective pattern will be related to identities. For example, it might be interesting to study the relationship between a disease and age and occupation, but not that between the disease and patient name. In other cases, such as in database marketing, disease outbreak detection, and crime investigation, the data user is interested in tracing and linking individuals with certain characteristics. In these cases, the data user has a higher incentive to acquire identifying information. Note that both types of data analysis involve using con<sup>fi</sup>dential attributes. Otherwise, privacy concerns are negligible.

Based on the account above, in our modeling and mechanism design, we consider two types of data consumers: a type A data user who is more interested in Aggregate information and patterns in data rather than personal information, and a type I data user who is more interested in Individual identity and personal information. The two types of data users are de<sup>fi</sup>ned in a relative sense — the setup merely assumes that the type I user is more interested in individual information than the type A user. In practice, of course, there can be more than two types of data users in terms of the levels of interest in personal information. We consider this simple two-type setting in order to make the analysis manageable. The results of the analysis based on this simpli<sup>fi</sup>ed scenario can provide practically valuable insights, as we elaborate later. We note that restricting to two types of consumers is common in the related literature [9,16]. We discuss issues and possible approaches concerning situations with more than two types of consumers in the <sup>fi</sup>nal section.

## 3.1. The cost models

The cost of personal data to the data owner can be classi<sup>fi</sup>ed into three categories. The <sup>fi</sup>rst is the cost of collecting data, such as discounts offered to customers with membership cards, coupons and sweepstake prizes to draw survey participants, and <sup>fi</sup>nancial incentives for customers to provide more personal information when they purchase products online [4,13]. From a data distribution viewpoint, this type of cost can be considered sunk cost. The second category is the cost of processing (including masking) the data for distribution. This cost is negligible since it is small and is essentially <sup>fi</sup>xed. The third type of cost is tied to the loss in privacy incurred by disseminating the data. When personal data is disseminated to a third party, the individual subjects involved should be compensated for their privacy loss. This type of cost has been considered in many privacy studies [10,16,17]. We adopt in this study the compensation scheme proposed by Laudon [17], which allows individuals to provide their personal data to a data collector with <sup>fi</sup>nancial compensation. The compensation amount, of course, varies with different individuals and the type of information the individuals provide.

With the cost of the data determined by the above compensation scheme, we consider two methods of selecting and releasing data for the data owner. With the <sup>fi</sup>rst method, individual records are randomly selected and disseminated by the data owner to the data user, when only a subset of the data is released. Sometimes, the data user may be interested in only a segment of the individuals with a certain characteristic. In this case, the pool of the data should be reduced to include only those individuals with such a characteristic, and random sampling would still apply to the reduced pool. For instance, suppose the data owner has a data set that includes all customers in a region who have bought a new product. A data user may be interested only in the customers who bought the product using a promotion coupon. In this case, the pool should include only those customers who used the coupon, and random sampling would be applied within this pool. With random sampling, each unit has an equal chance of being selected.

Let the amount of data be represented by the number of individual records, denoted by x. Let the sensitivity level of data be represented by the number and type of attributes. Based on the compensation scheme above, the sensitivity level s can be measured for a speci<sup>fi</sup>ed set of attributes (requested by the data user). Let c be the mean unit cost for an attribute value of a record. Then, with random sampling the total cost of x records at sensitivity level s can be written as

$$
c (s, x) = \int_ {0} ^ {x} \int_ {0} ^ {s} c d u d v = c s x.\tag{1}
$$

That is, the above cost function in the case of random selection is linear in the following sense.

Linear cost function. For a given sensitivity level, the cost of data with random sampling is an increasing linear function of the amount of the data. Similarly, for a given amount of data, the cost of data is increasing linearly in the sensitivity of the data.

Next, we consider the second method, called ordered selection, which selects individual records based on the cost of the individuals, in ascending order from the least expensive one to the most. The above discussion regarding the pool of the data also applies to this case. With ordered selection, each additional unit of amount or sensitivity will cost more for the data owner. As such, the cost function will be convex in the following sense.

Convex cost function. For a given sensitivity level, the cost of data with ordered selection is an increasing and convex function of the amount of the data. Similarly, for a given amount of data, the cost of data is increasing and convex in the sensitivity of the data.

The convexity of the cost function can be expressed as:

$$
\partial C (s, x) / \partial x > 0, \partial C ^ {2} (s, x) / \partial x ^ {2} \geq 0, \partial C (s, x) / \partial s > 0, \partial C ^ {2} (s, x) / \partial s ^ {2} \geq 0.\tag{2}
$$

Note that the linear function is mathematically a special case of the convex function.

## 3.2. The utility models

In contrast to the linear or convex behavior of the cost function, the utility of data typically exhibits a concave behavior. This means, in our problem context, as the amount and sensitivity of data increase, the data consumer's utilities increase, but at a decreasing rate. This observation is well-grounded on the results of numerous prior analytical and empirical studies in the same or a similar context [23,24,9,19]. A typical example is the use of poll to estimate public opinion. It is well-known that estimation accuracy increases (i.e., the margin of error decreases) with sample size; however, the improvement in estimation accuracy diminishes as the sample size continues to increase [25]. In terms of sensitivity, the more detailed break-down (by age, gender, race, income, etc.) the poll offers – i.e., the more sensitive the data is – the more valuable the poll results are. But the added value generally diminishes as the break-down becomes more detailed (e.g., a break-down of income into ten groups will not likely to be <sup>fi</sup>ve times as valuable as into two groups). Similar observations have been made in studies involving data mining tasks such as classi<sup>fi</sup>cation, feature selection and association rules mining [15,18,8]. Based on these observations, we state the utility function behavior below (we will discuss later how the analysis will be affected if utility functions are linear or even convex).

Increasing concave utility function. A data consumer’s utility is (i) an increasing and concave function of the amount of the data, and (ii) an increasing and concave function of the sensitivity of the data.

Let $U _ { t } ( s , x )$ be the utility of user t, where $t \in \{ A , I \}$ is the type of the user. Then,

$$
\begin{array}{l} \partial U _ {t} (s, x) / \partial x > 0, \partial U _ {t} ^ {2} (s, x) / \partial x ^ {2} <   0, \partial U _ {t} (s, x) / \partial s > 0, \\ \partial U _ {t} ^ {2} (s, x) / \partial s ^ {2} <   0, t \in \{A, I \}. \end{array}\tag{3}
$$

We assume that the utility of the data user is zero if no data is provided by the data owner or if the sensitivity level of the data is zero (one could interpret zero sensitivity level data as perfectly protected data such as encrypted data). That is,

$$
U _ {t} (s, 0) = 0 \text { and } U _ {t} (0, x) = 0.\tag{4}
$$

Because the type I consumer is more interested in more sensitive data than the type $A$ consumer, it is reasonable to argue that given an increase (decrease) in sensitivity level of data, the increase (decrease) in utility for a type I data consumer is greater than or equal to that for a type A consumer. This “single crossing” condition is quite common in similar prior studies [9,24]. The condition can be expressed as

$$
\partial U _ {I} (s, x) / \partial s > \partial U _ {A} (s, x) / \partial s.\tag{5}
$$

$$
\text { since } U _ {I} (0, x) = U _ {A} (0, x) = 0, \text { inequality   (5)   implies   that }
$$

$$
U _ {I} (s, x) \geq U _ {A} (s, x).\tag{6}
$$

Different sensitivity levels mentioned above can be achieved by using a technology-based approach to mask the data with different values of a model parameter, such as the k parameter in k-anonymity [27], the upper and lower bounds in data swapping [20], and the variance of noise in data perturbation [21]. Since such a parameter is typically continuous, the sensitivity variable s is considered continuous. Conceptually, we divide s into two types, $s _ { H }$ and s , with $s _ { H }$ having higher sensitivity levels than that of $\dot { s } _ { L } .$ In our modeling, we distinguish $s _ { H }$ and $s _ { L }$ in a very practical way. The released data is said to be of $s _ { H }$ type if it contains explicit identifying attributes; otherwise, it is of $\dot { \boldsymbol { s } } _ { L }$ type. Clearly, the data with explicit identi<sup>fi</sup>ers and con<sup>fi</sup>dential attributes are more sensitive than those without. Both $s _ { H }$ and $S _ { L }$ data must also contain con<sup>fi</sup>dential attributes in order to be sensitive. For the s<sub>H</sub> type, different degree of sensitivity represents different set of explicit identifying attributes and/or different scale of masking to the con<sup>fi</sup>dential attributes. Similarly for the s type, different degree of sensitivity represents different scale of masking to the quasi-identi<sup>fi</sup>er and con<sup>fi</sup>dential attributes. Therefore, both $s _ { H }$ and $S _ { L }$ are continuous variables and variable s in the cost and utility functions above can be legitimately replaced with s<sub>H</sub> or s<sub>L</sub>.

It turns out that the utility function for a type I user behaves rather differently given $s _ { H }$ or $s _ { L }$ data. The type I user is interested in individual identity and personal information. This is available in the $s _ { H }$ data; so the utility function with $s _ { H }$ is concave and monotonic increasing, as described earlier. With the $s _ { L }$ data, which does not have explicit identi<sup>fi</sup>ers such as name and phone number, the user has to use the quasi-identi<sup>fi</sup>er attributes, such as age, gender and zip code, to match the records in the data with those in an external source (e.g., voter registration records) to re-identify the individuals [27,30]. So, there is a cost involved for the type I user (but not for the type A user) in order to use the $S _ { L }$ data. This cost is increasing and convex with respect to the number of records because, given a <sup>fi</sup>xed $s _ { L }$ level, it is increasingly more dif<sup>fi</sup>cult to re-identify additional individuals (and some individuals may not be reidenti<sup>fi</sup>ed at all). As a result, the net utility (after deducting this cost) will <sup>fi</sup>rst increase with the number of records, and then decrease after a certain point. The utility function will exhibit an inverted U-shaped behavior.

Non-monotonic concave utility function. The utility of a type I data consumer for the $s _ { L }$ data, $U _ { I } ( s _ { L } , x )$ , is a non-monotonic concave function of x; it first increases with x, and then declines after x is greater than its maximizing point.

Consequently, with the s data there will be “double crossing” between the utility function of a type I user and that of a type A user. This behavior departs from the “single crossing” condition that is assumed in the conventional vertical differentiation models. As a result, the properties associated with the “single crossing” condition (e.g., Eqs. (3), (5) and (6)) will hold only up to a certain point. Beyond that point, new analysis will be required and the corresponding results will be different from those of the conventional models. (It can also be argued that the utility will never decrease even in this case, because the data user can stop using more data once the utility reaches its maximum. We point out that, as shown later in the paper, the analysis and the subsequent models remain the same even if we assume the utility function stops at the maximum.)

## 3.3. The pricing models

The proposed mechanism works as follows. In response to a request of data from a third party user, the data owner <sup>fi</sup>rst selects different sensitivity types to offer. The data owner then offers a menu of different price schedules with different sensitivity types, based on incentive compatibility and individual rationality conditions to be discussed later. This will effectively force the data user to reveal his type. The user then selects the corresponding price, and attempts to maximize his net payoff. The sequence of these events is shown in Fig. 1, which include four stages. The models for optimal pricing are developed in a reverse order. We <sup>fi</sup>rst derive the optimal amount of data for the two types of users respectively, with the chosen price function. The pricing models are then formulated to maximize the data owner's bene<sup>fi</sup>t, given the users' optimal values.

## 3.3.1. Price function and optimal data quantities

We use the popular “two-part tariff” pricing scheme in our model ing, as stated below.

![](/api/attachments/QE9VVXYD/fulltext/images/78a5ac8acb537ebab2bec7bcc9cc677858a604f0e1a03a924cb6276e695111d0.jpg)  
Fig. 1. Sequence of events.

Two-part tariff pricing. For a given sensitivity level, the price of the data includes a fixed charge and a variable charge that is an increasing linear function of the amount of data.

Let $R ( s , x )$ be the total price charged for x amount of data with sensitivity level s. The price function can be written as

$$
R (s, x) = \alpha_ {s} + \beta_ {s} x,\tag{7}
$$

where α and $\beta _ { s }$ are the <sup>fi</sup>xed and variable price respectively and both are function of s. The “two-part tariff” pricing is widely used in practice. It serves particularly well for our purposes because the <sup>fi</sup>xed charge represents the “access $\mathrm { f e e } ^ { \prime \prime }$ or effort that the data user must pay in order to obtain the data at all. Due to the characteristics of sensitive data, this <sup>fi</sup>xed charge may be non-monetary, such as the effort to obtain a security clearance or a judge order [28]. Although this kind of <sup>fi</sup>xed charge is not paid to the data owner directly, it reduces the risk from potential privacy violation penalties by governments. It is thus considered as a bene<sup>fi</sup>t to the data owner.

Table 1 summarizes the notation used in this paper.

The net payoff for a user of type t that chooses to acquire x amount of data with sensitivity level s is $U _ { t } ( s , x _ { s } ) \ : - \ : R ( s , x _ { s } )$ . Given the concave utility in (3) and two-part tariff pricing in (7), the net payoff has a unique non-corner maximum for the type A and type I users, respectively (if the cost function is linear and the utility function is linear or convex, then the maximum net payoff will generally occur at the upper bound of x, which is less interesting analytically). In stage 4, the user's objective is to maximize his net payoff:

$$
\max _ {x _ {s} ^ {t}} U _ {t} \left(s, x _ {s} ^ {t}\right) - \alpha_ {s} - \beta_ {s} x _ {s} ^ {t}, t \in \{A, I \}.\tag{8}
$$

The optimal solution $\boldsymbol { x } _ { s } ^ { t * }$ can be obtained from the <sup>fi</sup>rst-order condition below:

$$
\left. \frac {\partial U _ {t} (s , x _ {s} ^ {t})}{\partial x _ {s} ^ {t}} \right| _ {x _ {s} ^ {t} = x _ {s} ^ {t *}} = \beta_ {s}, t \in \{A, I \}.\tag{9}
$$

## 3.3.2. Constraints

Constraints are speci<sup>fi</sup>ed in terms of individual rationality (IR) and incentive compatibility (IC) for different data users.

Table 1 Table of notation.

<table><tr><td> $x, x_{s}^{t}$ </td><td>Amount of data; and amount of data acquired by user type  $t \in \{A, I\}$  for a given sensitivity level s</td></tr><tr><td> $s_{L}, s_{H}$ </td><td>Sensitivity type of data</td></tr><tr><td> $U_{A}(s, x), U_{I}(s, x)$ </td><td>Utility of type A and type I data consumers respectively</td></tr><tr><td> $C(s, x)$ </td><td>Total cost of data for data owner</td></tr><tr><td> $R(s, x)$ </td><td>Total price charged to data consumer</td></tr><tr><td> $\alpha_{s}$ </td><td>Fixed charge for a given sensitivity level s</td></tr><tr><td> $\beta_{s}$ </td><td>Rate of variable charge for a given sensitivity level s</td></tr></table>

3.3.2.1. Individual rationality constraints. The net payoff for the type A user to use low sensitivity data must be non-negative:

$$
U _ {A} \left(s _ {L}, x _ {L} ^ {A}\right) - R \left(s _ {L}, x _ {L} ^ {A}\right) \geq 0\tag{10}
$$

Similarly, the net payoff for the type I user to use high sensitivity data must be non-negative:

$$
U _ {I} \left(s _ {H}, x _ {H} ^ {I}\right) - R \left(s _ {H}, x _ {H} ^ {I}\right) \geq 0.\tag{11}
$$

3.3.2.2. Incentive compatibility constraints. The price should be set such that a type A user's net payoff using low sensitivity data is greater than or equal to that using high sensitivity data:

$$
U _ {A} \left(s _ {L}, x _ {L} ^ {A}\right) - R \left(s _ {L}, x _ {L} ^ {A}\right) \geq U _ {A} \left(s _ {H}, x _ {H} ^ {A}\right) - R \left(s _ {H}, x _ {H} ^ {A}\right).\tag{12}
$$

For a type I user, the incentive for high sensitivity data should be greater than or equal to that for low sensitivity data:

$$
U _ {I} \left(s _ {H}, x _ {H} ^ {I}\right) - R \left(s _ {H}, x _ {H} ^ {I}\right) \geq U _ {I} \left(s _ {L}, x _ {L} ^ {I}\right) - R \left(s _ {L}, x _ {L} ^ {I}\right).\tag{13}
$$

The data owner wants $R ( s _ { L } , x _ { L } ^ { A } )$ and $R \big ( s _ { H } , x _ { H } ^ { I } \big )$ in the above constraints as large as possible. In the traditional incentive compatibility mechanism setting, it has been shown that only (10) and (13) will be binding. In our problem, the type I user's utility function is non-monotonic concave with the $S _ { L }$ data. Therefore, which constraints will be binding depend on the <sup>fi</sup>rst order conditions for $U _ { A } ( s _ { L } , \ x _ { L } ^ { A } )$ and $U _ { I } ( S _ { L } , \ x _ { L } ^ { I } )$ determined by (9). Proposition 1 below provides the binding IR and IC constraints with different scenarios.

Proposition 1. Maximizing $R ( s _ { L } , x _ { L } ^ { A } )$ and $R ( s _ { H } , x _ { H } ^ { I } )$ results in the following binding IR and IC constraints:

(i) $I f \ U _ { I } ( S _ { L } , \ x _ { L } ^ { I * } ) / \partial x _ { L } ^ { I * } > U _ { A } ( S _ { L } , \ x _ { L } ^ { A * } ) / \partial x _ { L } ^ { A * }$ , then (10) and (13) will be binding; i.e.,

$$
R \left(s _ {L}, x _ {L} ^ {A}\right) = U _ {A} \left(s _ {L}, x _ {L} ^ {A}\right),\tag{14}
$$

$$
\begin{array}{l} R \Big (s _ {H}, x _ {H} ^ {I} \Big) = U _ {I} \Big (s _ {H}, x _ {H} ^ {I} \Big) - U _ {I} \Big (s _ {L}, x _ {L} ^ {I} \Big) + U _ {A} \Big (s _ {L}, x _ {L} ^ {A} \Big) \\ \qquad + \beta_ {L} \Big (x _ {L} ^ {I} - x _ {L} ^ {A} \Big). \end{array}\tag{15}
$$

(ii) I $^ { \varsigma } U _ { I } ( s _ { L } , x _ { L } ^ { I * } ) / \partial x _ { L } ^ { I * } = U _ { A } ( s _ { L } , x _ { L } ^ { A * } ) / \partial x _ { L } ^ { A * }$ <sup>∗</sup>, then (10), (11) and (13) will be binding; i.e., (14) and (15) will hold, and binding (11) can be written as

$$
R \left(s _ {H}, x _ {H} ^ {I}\right) = U _ {I} \left(s _ {H}, x _ {H} ^ {I}\right).\tag{16}
$$

(iii) I $^ { : } U _ { I } ( S _ { L } , \ x _ { L } ^ { I * } ) / \partial x _ { L } ^ { I * } < U _ { A } ( S _ { L } , \ x _ { L } ^ { A * } ) / \partial x _ { L } ^ { A * }$ , then (10) and (11) will be binding; i.e., (14) and (16) will hold

The proofs of all propositions are provided in the Appendix A.

## 3.3.3. The model for optimal prices

In stage 2, the data owner's objective is to maximize her total net bene<sup>fi</sup>t:

$$
\max _ {\alpha_ {s}, \beta_ {s}} \alpha_ {s} + \beta_ {s} x _ {s} ^ {t *} - C (s, x _ {s} ^ {t *}), t \in \{A, I \},\tag{17}
$$

subject to the binding constraints speci<sup>fi</sup>ed in Proposition 1 for type A and type I users respectively. These constraints ensure that in stage 3 type A and type I users select $S _ { L }$ and $s _ { H }$ respectively. We consider in order the three scenarios described in Proposition 1.

Scenario (i) For type A user, substituting (14) into (17), the data owner's optimal solution for $\beta _ { L }$ can be obtained by

$$
\frac {\partial}{\partial \beta_ {L}} \left[ U _ {A} \left(s _ {L}, x _ {L} ^ {A *}\right) - C \left(s _ {L}, x _ {L} ^ {A *}\right) \right] = 0.
$$

That is,

$$
\frac {\partial U \left(s _ {L} , x _ {L} ^ {A *}\right)}{\partial x _ {L} ^ {A *}} \frac {\partial x _ {L} ^ {A *}}{\partial \beta_ {L}} - \frac {\partial C \left(s _ {L} , x _ {L} ^ {A *}\right)}{\partial x _ {L} ^ {A *}} \frac {\partial x _ {L} ^ {A *}}{\partial \beta_ {L}} = 0.
$$

Substituting (9) into the above equation, we have

$$
\beta_ {L} ^ {*} = \partial C \left(s _ {L}, x _ {L} ^ {A *}\right) / \partial x _ {L} ^ {A *},\tag{18}
$$

$$
\alpha_ {L} ^ {*} = U _ {A} \left(s _ {L}, x _ {L} ^ {A *}\right) - \left[ \partial C \left(s _ {L}, x _ {L} ^ {A *}\right) / \partial x _ {L} ^ {A *} \right] x _ {L} ^ {A *},\tag{19}
$$

where $x _ { L } ^ { A * }$ is determined by (9). For type I user, substituting (15) into (17), the data owner's optimal solution for $\beta _ { H }$ can be obtained by

$$
\begin{array}{l} \frac {\partial}{\partial \beta_ {H}} \left[ U _ {I} \left(s _ {H}, x _ {H} ^ {I ^ {*}}\right) - U _ {I} \left(s _ {L}, x _ {L} ^ {I ^ {*}}\right) + U _ {A} \left(s _ {L}, x _ {L} ^ {A ^ {*}}\right) \right. \\ \left. + \beta_ {L} ^ {*} \left(x _ {L} ^ {I ^ {*}} - x _ {L} ^ {A ^ {*}}\right) - C \left(s _ {H}, x _ {H} ^ {I ^ {*}}\right) \right] = 0. \end{array}
$$

Given a <sup>fi</sup>xed $\beta _ { L }$ value, ${ \cal U } _ { I } ( s _ { L } , x _ { L } ^ { I * } ) , { \cal U } _ { A } ( s _ { L } , x _ { L } ^ { A * } )$ , and $\beta _ { L } ^ { * } ( x _ { L } ^ { I * } -$ $x _ { L } ^ { A * } )$ will not change with respect to a small change in $\beta _ { H } .$ So the above expression simpli<sup>fi</sup>es to

$$
\frac {\partial}{\partial \beta_ {H}} \left[ U _ {I} \left(s _ {H}, x _ {H} ^ {I *}\right) - C \left(s _ {H}, x _ {H} ^ {I *}\right) \right] = 0.
$$

Thus, similar to (18), we have

$$
\beta_ {H} ^ {*} = \partial C \left(s _ {H}, x _ {H} ^ {I *} \right. / \partial x _ {H} ^ {I *}.\tag{20}
$$

It follows from (15), (17), (18) and (20) that

$$
\begin{array}{l} \alpha_ {H} ^ {*} = U _ {I} \Big (s _ {H}, x _ {H} ^ {I *} \Big) - U _ {I} \Big (s _ {L}, x _ {L} ^ {I *} \Big) + U _ {A} \Big (s _ {L}, x _ {L} ^ {A *} \Big) \\ \qquad + \frac {\partial C \Big (s _ {L} , x _ {L} ^ {A *} \Big)}{\partial x _ {L} ^ {A *}} \Big (x _ {L} ^ {I *} - x _ {L} ^ {A *} \Big) \\ \qquad - \frac {\partial C \Big (s _ {H} , x _ {H} ^ {I *} \Big)}{\partial x _ {H} ^ {I *}} x _ {H} ^ {I *}, \end{array}\tag{21}
$$

where $x _ { L } ^ { A * } , x _ { L } ^ { I * }$ <sup>∗</sup> and $x _ { H } ^ { I * }$ are determined by (9).

Scenarios (ii) and (iii) For type A user, optimal solutions α<sup>∗</sup> and $\beta _ { L } ^ { * }$ are the same as in (18) and (19). For type I user, β<sub>H</sub><sup>⁎</sup> is the same as in (20). It follows from (16), (17) and (20) that

$$
\alpha_ {H} ^ {*} = U _ {I} \left(s _ {H}, x _ {H} ^ {I *} \right. - \left[ \partial C \left(s _ {H}, x _ {H} ^ {I *} \right. / \partial x _ {H} ^ {I *} \right] x _ {H} ^ {I *}.\tag{22}
$$

For all three scenarios above, Proposition 2 below states a relationship between $\beta _ { L } ^ { * }$ and $\beta _ { H } ^ { * }$

Proposition 2. The optimal variable price for low sensitivity data $\beta _ { L } ^ { * }$ is always smaller than the optimal variable price for high sensitivity data $\beta _ { H } ^ { * }$

Note that there is no analogous relationship between $\alpha _ { H } ^ { * }$ and $\alpha _ { L } ^ { * } ;$ ; $\mathrm { i } . \mathrm { e } . , \alpha _ { H } ^ { * }$ can be larger or smaller than $\alpha _ { L } ^ { * }$

## 3.3.4. The model for optimal sensitivity levels

The data owner's problem in stage 1 is to maximize the expected net bene<sup>fi</sup>t with respect to different sensitivity types $s _ { L }$ and $s _ { H \cdot }$ This objective can be written as

$$
\begin{array}{l} \max _ {s _ {L}, s _ {H}} p \left(\alpha_ {L} ^ {*} + \beta_ {L} ^ {*} x _ {L} ^ {A *} - \frac {\partial C \left(s _ {L} , x _ {L} ^ {A *}\right)}{\partial x _ {L} ^ {A *}} x _ {L} ^ {A *}\right) + (1 - p) \\ \times \left(\alpha_ {H} ^ {*} + \beta_ {H} ^ {*} x _ {H} ^ {I *} - \frac {\partial C \left(s _ {H} , x _ {H} ^ {I *}\right)}{\partial x _ {H} ^ {I *}} x _ {H} ^ {I *}\right), \end{array}\tag{23}
$$

where $p$ is the probability that a data user is type A. We assume that the data owner can estimate this input parameter fairly accurately, based on the historical data (e.g., the proportion of the data releases with/without personal identi<sup>fi</sup>ers). Substituting (18) and (20) into (23), this objective simpli<sup>fi</sup>es to

$$
\max _ {s _ {L}, s _ {H}} p \alpha_ {L} ^ {*} + (1 - p) \alpha_ {H} ^ {*},\tag{24}
$$

where $\alpha _ { L } ^ { * }$ and $\alpha _ { H } ^ { * }$ are functions of $S _ { L }$ and $s _ { H } ,$ as shown in (19), (21) and (22). The optimal solution (s<sup>∗</sup>, s<sup>∗</sup> ) can be found from the <sup>fi</sup>rst-order conditions of (24) with respect to s and $s _ { H } .$ . We note that the data owner can choose to make only one type of data available. In this case, Eq. (24) can be easily adapted for $S _ { L }$ and $s _ { H }$ separately. We discuss scenarios when offering only one type of data in the next section with an example.

## 4. An illustrative example

As a benchmark, we <sup>fi</sup>rst consider a case where both s and s types are provided. It is also possible for the data owner to make only one type of data available. We discuss this situation and compare it with the benchmark in the second part of this section, using the same example.

## 4.1. Offering both low- and high-sensitivity data

Consider a type A data user whose utility function is

$$
U _ {A} \left(s, x _ {s} ^ {A}\right) = s ^ {1 / 2} \left[ x _ {s} ^ {A} - \frac {1}{2} \left(x _ {s} ^ {A}\right) ^ {2} \right], 0 \leq s \leq 1, 0 \leq x _ {s} ^ {A} \leq 1.\tag{25}
$$

It is easy to verify that this function satis<sup>fi</sup>es (3). To ease the illustration, we consider the linear cost function as in (1), which is, as mentioned earlier, a special case of the convex cost function in (2). The idea for the convex case is the same but mathematical manipulations become more cumbersome. For the linear case, Eqs. (18) and (20) simplify to

$$
\beta_ {L} ^ {*} = c s _ {L} \text { and } \beta_ {H} ^ {*} = c s _ {H}.\tag{26}
$$

We <sup>fi</sup>rst compute $x _ { s } ^ { A * }$ , the optimal solution to the user's net payoff $P ( \cdot ) { \mathrm { : } }$

$$
P _ {A} \left(x _ {s} ^ {A}\right) = s ^ {1 / 2} \left[ x _ {s} ^ {A} - \frac {1}{2} \left(x _ {s} ^ {A}\right) ^ {2} \right] - \alpha_ {s} - \beta_ {s} x _ {s} ^ {A}.
$$

Setting $\partial P _ { A } / \partial x _ { s } ^ { A } = 0$ and using (26), we have

$$
x _ {s} ^ {A *} = 1 - \frac {\beta_ {s}}{s ^ {1 / 2}} = 1 - c s ^ {1 / 2}.\tag{27}
$$

$$
U _ {A} \left(s, x _ {s} ^ {A *}\right) = s ^ {1 / 2} \left[ \left(1 - c s ^ {1 / 2}\right) - \frac {1}{2} \left(1 - c s ^ {1 / 2}\right) ^ {2} \right] = \frac {1}{2} s ^ {1 / 2} - \frac {c ^ {2}}{2} s ^ {3 / 2}.\tag{28}
$$

Substituting (26), (27) and (28) into (19), we have

$$
\alpha_ {L} ^ {*} = \frac {c ^ {2}}{2} s _ {L} ^ {3 / 2} - c s _ {L} + \frac {1}{2} s _ {L} ^ {1 / 2}.\tag{29}
$$

Now, consider a type I data user whose original utility function is

$$
U _ {I} \left(s, x _ {s} ^ {I}\right) = k s ^ {1 / 2} \left[ x _ {s} ^ {I} - \frac {1}{2} \left(x _ {s} ^ {I}\right) ^ {2} \right], 0 \leq s \leq 1, 0 \leq x _ {s} ^ {I} \leq 1, k > 1.\tag{30}
$$

Again, this utility satis<sup>fi</sup>es (3). Note that the condition $k > 1$ ensures that the relationship between $U _ { A } ( s , x _ { s } ^ { A } )$ and $U _ { I } ( s , x _ { s } ^ { I } )$ satisfy (5) and (6). For low sensitivity data, there is a re-identi<sup>fi</sup>cation cost. We <sup>fi</sup>rst consider a scenario (i) case, which has a re-identi<sup>fi</sup>cation cost of $k s _ { L } ^ { 1 / 2 } ( x _ { L } ^ { I } ) ^ { 2 } / 1 2$ for the type I user. Then, the utility with $S _ { L }$ is

$$
U _ {I} \left(s _ {L}, x _ {L} ^ {I}\right) = k s _ {L} ^ {1 / 2} \left[ x _ {L} ^ {I} - \frac {7}{1 2} \left(x _ {L} ^ {I}\right) ^ {2} \right], 0 \leq s _ {L} \leq 1, 0 \leq x _ {L} ^ {I} \leq 1, k > 1,\tag{31}
$$

(which peaks at $x = 6 / 7$ , before reaching boundary $x = 1 )$ . Eq. (30) will be used for the $s _ { H }$ data only. Following the same procedure above, we can get results below for this user:

$$
x _ {H} ^ {I *} = 1 - \frac {c}{k} s _ {H} ^ {1 / 2}, x _ {L} ^ {I *} = \frac {6}{7} \left(1 - \frac {c}{k} s _ {L} ^ {1 / 2}\right).\tag{32}
$$

$$
U _ {I} \left(s _ {H}, x _ {H} ^ {I *}\right) = \frac {k}{2} s _ {H} ^ {1 / 2} - \frac {c ^ {2}}{2 k} s _ {H} ^ {3 / 2}, U _ {I} \left(s _ {L}, x _ {L} ^ {I *}\right) = \frac {3 k}{7} s _ {L} ^ {1 / 2} - \frac {3 c ^ {2}}{7 k} s _ {L} ^ {3 / 2}.\tag{33}
$$

$$
\begin{array}{l} \alpha_ {H} ^ {*} = \frac {c ^ {2}}{2 k} s _ {H} ^ {3 / 2} - c s _ {H} + \frac {k}{2} s _ {H} ^ {1 / 2} - \frac {3 c ^ {2}}{7 k} s _ {L} ^ {3 / 2} + \frac {c ^ {2}}{2} s _ {L} ^ {3 / 2} - \frac {c}{7} s _ {L} - \frac {3 k}{7} s _ {L} ^ {1 / 2} \\ \qquad + \frac {1}{2} s _ {L} ^ {1 / 2}. \end{array}\tag{34}
$$

![](/api/attachments/QE9VVXYD/fulltext/images/43c347a52b37baff18dd29d392d0b26ee19ff36588d934921bf7f673965e1619.jpg)  
Fig. 2. Utility, cost and price for low sensitivity data – scenario (i).

Substituting (29) and (34) into (24), we have

$$
\begin{array}{l} \max _ {s _ {L}, s _ {H}} p \left(\frac {c ^ {2}}{2} s _ {L} ^ {3 / 2} - c s _ {L} + \frac {s _ {L} ^ {1 / 2}}{2}\right) + (1 - p) \\ \times \left(\frac {c ^ {2}}{2 k} s _ {H} ^ {3 / 2} - c s _ {H} + \frac {k}{2} s _ {H} ^ {1 / 2} - \frac {3 c ^ {2}}{7 k} s _ {L} ^ {3 / 2} + \frac {c ^ {2}}{2} s _ {L} ^ {3 / 2} - \frac {c}{7} s _ {L} - \frac {3 k}{7} s _ {L} ^ {1 / 2} + \frac {s _ {L} ^ {1 / 2}}{2}\right). \end{array}
$$

The <sup>fi</sup>rst-order conditions for this problem lead to the following results:

$$
\left(s _ {H} ^ {*}\right) ^ {1 / 2} = k / (3 c),\tag{35}
$$

$$
\left(s _ {L} ^ {*}\right) ^ {1 / 2} = \frac {(2 k + 1 2 p k) - \left[ (2 k + 1 2 p k) ^ {2} - (2 1 k - 1 8 + 1 8 p) (7 k - 6 k ^ {2} + 6 p k ^ {2}) \right] ^ {1 / 2}}{c (2 1 k - 1 8 + 1 8 p)}.\tag{36}
$$

Substituting (35) and (36) into (26) through (34), the optimal solutions $\beta _ { s ^ { * } } ^ { * } , \alpha _ { s ^ { * } } ^ { * } , x _ { s ^ { * } } ^ { t }$ <sup>∗</sup> and $U \big ( S ^ { \ast } , x _ { S ^ { \ast } } ^ { t } \big ) \big ( S ^ { \ast } \in \{ S _ { L } ^ { \ast } , S _ { H } ^ { \ast } \} , t \in \{ A , I \} \big )$ can be expressed in terms of known parameters $p , c$ and k.

Le $: p = 0 . 5 , c = 1 , k = 1 . 2 5 ,$ . Then $( s _ { L } ^ { * } ) ^ { 1 / 2 } = 0 . 2 6 3 , ( s _ { H } ^ { * } ) ^ { 1 / 2 } = 0 . 4 1 7 ,$ and

$$
\left. \beta_ {L} ^ {*} \right| _ {s _ {L} ^ {*}} = 0. 0 6 9, \left. \beta_ {H} ^ {*} \right| _ {s _ {H} ^ {*}} = 0. 1 7 4, \left. \alpha_ {L} ^ {*} \right| _ {s _ {L} ^ {*}} = 0. 0 7 1, \left. \alpha_ {H} ^ {*} \right| _ {s _ {H} ^ {*}} = 0. 0 9 9,
$$

$$
x _ {L} ^ {A *} | _ {s _ {L} ^ {*}} = 0. 7 3 7, x _ {L} ^ {I *} | _ {s _ {L} ^ {*}} = 0. 6 7 7, x _ {H} ^ {I *} | _ {s _ {H} ^ {*}} = 0. 6 6 7.
$$

Figs. 2 and 3 show the utility, cost and price functions for data with sensitivity levels s<sup>∗</sup> and $s _ { H } ^ { * } ,$ respectively. These are the two optimal scenarios out of numerous possible scenarios for the data owner $( s _ { L }$ and $s _ { H }$ are continuous). The two <sup>fi</sup>gures cannot be plotted together because they are based on two data sets with different sensitivity levels. As shown in Fig. $2 , U _ { A } ( x )$ and $R ( x )$ are tangent at $x = 0 . 7 3 7$ . This is the only point where the type A user has a non-negative net payoff. To provide some positive incentives for the user, the data owner may set a <sup>fi</sup>xed charge slightly smaller than $\alpha _ { L } ^ { * } | _ { s _ { r } ^ { * } } = 0 . 0 7 1$ or a variable charge slightly smaller than $\beta _ { L } ^ { * } | _ { s : } = 0 . 0 6 9 . \ \mathrm { F i g . } ^ { ^ { \circ } 2 } 3$ <sup>¼</sup>shows that the type A user <sup>j L ¼</sup>cannot afford to buy the high sensitivity data as his utility function is lower than the price function for such data over the entire range of x. The type I user can have positive incentive with either types of data since his utilities are higher than the type A user. The maximum net payoff occurs at $x = 0 . 6 7 7$ for the low sensitivity data and $\mathtt { a t } x = 0 . 6 6 7$ for the high sensitivity data, both resulting in the same amount of net payoff (as shown by the equal maximum gap between $U _ { I } ( { \boldsymbol { x } } )$ and $R ( x )$ in the two <sup>fi</sup>gures). In order to facilitate the type I self-revelation, the data owner can set a slightly lower price for the high sensitivity data, as long as it is higher than the type A user's utility. Note that the absolute values of the variables are not important. For example, $x = 0 . 7 3 7$ can be interpreted as 737 records or 737,000 records. Similarly, sensitivity values should be interpreted in a relative sense.

![](/api/attachments/QE9VVXYD/fulltext/images/96294164058614ca6f46f2231ba9acfe3a2afe7e825032c0a3f60972a388f5fa.jpg)  
Fig. 3. Utility, cost and price for high sensitivity data – scenario $( \mathrm { i } ) .$

![](/api/attachments/QE9VVXYD/fulltext/images/1fceb2f9716c8eab6271168a08095e73d31936e2af6d4e24d418dcf932e6c2ed.jpg)  
Fig. 4. Utility, cost and price for low sensitivity data – scenario (iii).

We now consider a scenario (iii) case. Let the re-identi<sup>fi</sup>cation cost for the type I user be $k s _ { L } ^ { 1 / 2 } ( x _ { L } ^ { I } ) ^ { 2 } / 3$ . Then, the utility with s is

$$
U _ {I} \left(s _ {L}, x _ {L} ^ {I}\right) = k s _ {L} ^ {1 / 2} \left[ x _ {L} ^ {I} - \frac {5}{6} \left(x _ {L} ^ {I}\right) ^ {2} \right], 0 \leq s _ {L} \leq 1, 0 \leq x _ {L} ^ {I} \leq 1, k > 1.\tag{37}
$$

It can be veri<sup>fi</sup>ed that ${ \cal U } _ { I } ( s _ { L } , \ x _ { L } ^ { I * } ) / \partial x _ { L } ^ { I * } < { \cal U } _ { A } ( s _ { L } , \ x _ { L } ^ { A * } ) / \partial x _ { L } ^ { A * }$ . Using the analytical results derived earlier for scenario (iii), we obtain the following optimal solutions:

$$
x _ {L} ^ {I *} = \frac {3}{5} \left(1 - \frac {c}{k} s _ {L} ^ {1 / 2}\right), U _ {I} \left(s _ {L}, x _ {L} ^ {I *}\right) = \frac {3 k}{1 0} s _ {L} ^ {1 / 2} - \frac {3 c ^ {2}}{1 0 k} s _ {L} ^ {3 / 2},\tag{38}
$$

$$
\alpha_ {H} ^ {*} = \frac {c ^ {2}}{2 k} s _ {H} ^ {3 / 2} - c s _ {H} + \frac {k}{2} s _ {H} ^ {1 / 2},\tag{39}
$$

$$
\left(s _ {L} ^ {*}\right) ^ {1 / 2} = 1 / (3 c).\tag{40}
$$

The solutions for the other decision variables are the same. The utility, cost and price functions with the same $c , p$ and k values are shown in Figs. 4 and 5 for data with sensitivity levels $s _ { L } ^ { * }$ and $s _ { H } ^ { * } ,$ respectively. It is observed from Fig. 4 that $R ( x )$ for the low sensitivity data dominates the type I user's utility $U _ { I } ( x )$ . So, the data owner is able to raise the price for the high sensitivity data to match the maximum utility of the type I user (Fig. 5) and still induce proper self-selection. If the $U _ { I } ( x )$ curve in Fig. 4 is higher such that it tangents with R(x), we have a scenario (ii) case (this actually occurs when $U _ { I } ( s _ { L } , x _ { L } ^ { I } ) =$ $k s _ { L } ^ { 1 / 2 } [ x _ { L } ^ { I } - ( 1 2 1 / 1 6 0 ) ( x _ { L } ^ { I } ) ^ { 2 } ] )$

For all scenarios, the type A user will have no incentive to use the high sensitivity data while the type I user will have no incentive to use the low sensitivity data. It is observed that both <sup>fi</sup>xed and variable charges for the high sensitivity data are considerably larger than those for the low sensitivity data. As mentioned earlier, the <sup>fi</sup>xed charge could include non-monetary element such as the effort to obtain a security clearance or a judge order to access such data at all. The high barrier presents little or no problem for a legitimate investigator but can serve as a “protection shield” to prevent a privacy invader to access high sensitivity data.

![](/api/attachments/QE9VVXYD/fulltext/images/7f020e5c948ed96f2ce43c8d9e72a7a87bf12b5477945e8fb663017c5038d1c2.jpg)  
Fig. 5. Utility, cost and price for high sensitivity data – scenario (iii).

## 4.2. Offering either low- or high-sensitivity data

We consider the scenario (i) case <sup>fi</sup>rst. When offering only one type of data, only the IR constraints, as described in Section 3.3.2, should be considered; there is no IC constraint. When offering only low sensitivity data, the data owner can set the price such that it is affordable to both type A and type I users (denoted as L2) or to type I user only (denoted as L1). Note that any prices affordable to type A will be affordable to type I because of the higher utility of type I; so it is not possible to have a price affordable to type A only. In the L2 case, $\alpha _ { L 2 } ^ { * }$ and $\beta _ { L 2 } ^ { * }$ have the same expressions as in Eqs. (26) and (29), respectively, because they are derived based on the IR constraints only. So,

$$
\alpha_ {L 2} ^ {*} = \frac {c ^ {2}}{2} s _ {L 2} ^ {3 / 2} - c s _ {L 2} + \frac {1}{2} s _ {L 2} ^ {1 / 2}.\tag{41}
$$

The data owner's expected net payoff is

$$
\begin{array}{l} E (P _ {L 2}) \\ = p \left(\alpha_ {L 2} ^ {*} + \beta_ {L 2} ^ {*} x _ {L 2} ^ {A *} - \frac {\partial C \left(s _ {L 2} , x _ {L 2} ^ {A *} \right.}{\partial x _ {L 2} ^ {A *}} x _ {L 2} ^ {A *} \right) \\ \quad + (1 - p) \left(\alpha_ {L 2} ^ {*} + \beta_ {L 2} ^ {*} x _ {L 2} ^ {I *} - \frac {\partial C \left(s _ {L 2} , x _ {L 2} ^ {I *} \right.}{\partial x _ {L 2} ^ {I *}} x _ {L 2} ^ {I *} \right). \\ = p \alpha_ {L 2} ^ {*} + (1 - p) \alpha_ {L 2} ^ {*} = \alpha_ {L 2} ^ {*}. \end{array}\tag{42}
$$

Substituting (41) into (42) and taking the <sup>fi</sup>rst-order condition with respect to $s _ { L 2 } ,$ we have

$$
\left(s _ {L 2} ^ {*}\right) ^ {1 / 2} = 1 / (3 c).\tag{43}
$$

Next, consider the L1 case; i.e., offering the low sensitivity data to type I user only. The data owner's net payoff is maximized when the related IR constraint is bounding:

$$
\alpha_ {L 1} ^ {*} + \beta_ {L 1} ^ {*} x _ {L 1} ^ {I *} = U _ {I} \left(s _ {L 1}, x _ {L 1} ^ {I *}\right).\tag{44}
$$

Substituting the relevant expressions in (26), (32) and (33), which are derived independent of the IC constraints, into (44), we have

$$
\alpha_ {L 1} ^ {*} = \frac {3 c ^ {2}}{7 k} s _ {L 1} ^ {3 / 2} - \frac {6 c}{7} s _ {L 1} + \frac {3 k}{7} s _ {L 1} ^ {1 / 2}.\tag{45}
$$

Table 2

The data owner's expected net payoff is

$$
\begin{array}{l} E (P _ {L 1}) = (1 - p) \Big (\alpha_ {L 1} ^ {*} + \beta_ {L 1} ^ {*} x _ {L 1} ^ {I}   ^ {*} - \Big [ \partial C \Big (s _ {L 1}, x _ {L 1} ^ {I}   ^ {*} \Big) / \partial x _ {L 1} ^ {I}   ^ {*} \Big ] x _ {L 1} ^ {I}   ^ {*} \Big) \\ = (1 - p) \alpha_ {L 1} ^ {*}. \end{array}\tag{46}
$$

Substituting (45) into (46) and taking the <sup>fi</sup>rst-order condition with respect to $s _ { L 1 }$ , we have

$$
\left(s _ {L 1} ^ {*}\right) ^ {1 / 2} = k / (3 c).\tag{47}
$$

When offering only high sensitivity data, the data owner can set the price such that it is affordable to both type A and type I users (denoted as H2) or to type I user only (denoted as H1). In the H2 case, the data owner's net payoff is maximized when

$$
\alpha_ {H 2} ^ {*} + \beta_ {H 2} ^ {*} x _ {H 2} ^ {A *} = U _ {A} \left(s _ {H 2}, x _ {H 2} ^ {A *}\right).\tag{48}
$$

Substituting (26), (27) and (28), which are derived independent of the IC constraints, into (48), we have

$$
\alpha_ {H 2} ^ {*} = \frac {c ^ {2}}{2} s _ {H 2} ^ {3 / 2} - c s _ {H 2} + \frac {1}{2} s _ {H 2} ^ {1 / 2}.\tag{49}
$$

Similar to (42), the data owner's expected net payoff is

$$
E (P _ {H 2}) = p \alpha_ {H 2} ^ {*} + (1 - p) \alpha_ {H 2} ^ {*} = \alpha_ {H 2} ^ {*}.\tag{50}
$$

Substituting (49) into (50) and taking the <sup>fi</sup>rst-order condition with respect to $s _ { H 2 } ,$ we have

$$
\left(s _ {H 2} ^ {*}\right) ^ {1 / 2} = 1 / (3 c).\tag{51}
$$

It turns out that $s _ { H 2 } ^ { * }$ is the same as $s _ { L 2 } ^ { * }$ in (43). This occurs because no boundary between $s _ { L }$ and $s _ { H }$ is speci<sup>fi</sup>ed (if a boundary value between 1/(3c) and $k / ( 3 c )$ is speci<sup>fi</sup>ed, then $s _ { H 2 } ^ { * }$ will be equal to the boundary value).

Now consider the H1 case; i.e., offering the high sensitivity data to type I user only. The data owner's net payoff is maximized when

$$
\alpha_ {H 1} ^ {*} + \beta_ {H 1} ^ {*} x _ {H 1} ^ {I} ^ {*} = U _ {I} \left(s _ {H 1}, x _ {H 1} ^ {I} ^ {*}\right).\tag{52}
$$

Substituting the relevant expressions in (26), (32) and (33) into (52), we have

$$
\alpha_ {H 1} ^ {*} = \frac {c ^ {2}}{2 k} s _ {H 1} ^ {3 / 2} - c s _ {H 1} + \frac {k}{2} s _ {H 1} ^ {1 / 2}.\tag{53}
$$

The data owner's expected net payoff is

$$
E (P _ {H 1}) = (1 - p) \alpha_ {H 1} ^ {*}.\tag{54}
$$

Substituting (53) into (54) and taking the <sup>fi</sup>rst-order condition with respect to $s _ { H 1 } ,$ , we have

$$
\left(s _ {H 1} ^ {*}\right) ^ {1 / 2} = k / (3 c).\tag{55}
$$

Again, it turns out that $s _ { H 1 } ^ { * }$ is the same as $s _ { L 1 } ^ { * }$ in (47), because no boundary between $S _ { L }$ and $s _ { H }$ is speci<sup>fi</sup>ed.

Table 2 provides the results of different data offering strategies using the same parameters $( p = 0 . 5 , c = 1 , k = 1 . 2 5 )$ . It is observed that when offering one type of data to both type A and type I users (Strategies 2 and 4), the optimal sensitivity value is the same $( s ^ { * } =$ 0.333) even though they are labeled as $s _ { L } ^ { * }$ and s<sup>∗</sup> respectively. If a boundary value is speci<sup>fi</sup>ed to divide between $S _ { L }$ and $s _ { H } ,$ the s<sub>L</sub><sup>∗</sup> and $s _ { H } ^ { * }$ values will be different in general. Similarly, when offering one type of data to type I user only (Strategies 3 and 5), the optimal sensitivity value is the same. In this situation, however, the expected net payoff values are different. This is caused by the “re-identi<sup>fi</sup>cation cost” associated with $s _ { L }$ (but not with s ). In practice, the data owner should be able to divide between $s _ { L }$ and $s _ { H }$ data so that the s<sup>∗</sup> and s<sup>∗</sup> values will be different.

Results of different data offering strategies (p = 0.5, c = 1, k = 1.25).

<table><tr><td>Strategy</td><td> $(s_{L}^{*})^{1/2}$ </td><td> $(s_{H}^{*})^{1/2}$ </td><td> $\alpha_{L}^{*}$ </td><td> $\alpha_{H}^{*}$ </td><td> $E(P)$ </td></tr><tr><td>1. Offer  $s_{L}$  to type A and  $s_{H}$  to type I</td><td>0.2626</td><td>0.4167</td><td>0.0714</td><td>0.0994</td><td>0.0854</td></tr><tr><td>2. Offer  $s_{L2}$  to both type A and type I</td><td>0.3333</td><td></td><td>0.0741</td><td></td><td>0.0741</td></tr><tr><td>3. Offer  $s_{L1}$  to type I only</td><td>0.4167</td><td></td><td>0.0992</td><td></td><td>0.0496</td></tr><tr><td>4. Offer  $s_{H2}$  to both type A and type I</td><td></td><td>0.3333</td><td></td><td>0.0741</td><td>0.0741</td></tr><tr><td>5. Offer  $s_{H1}$  to type I only</td><td></td><td>0.4167</td><td></td><td>0.1157</td><td>0.0579</td></tr></table>

It can be observed that the data owner has the largest expected net payoff with Strategy 1 — offering s<sub>L</sub> to type A user and $s _ { H }$ to type I user for the example parameter values. Next, we analyze how the result changes with parameters p, k and c.

It follows from (41), (42), (43), (49), (50) and (51) that $E ( P _ { L 2 } )$ and $E ( P _ { H 2 } )$ do not depend on p and k. The expected net payoff with Strategy 1 is

$$
E (P _ {L \& H}) = p \alpha_ {L} ^ {*} + (1 - p) \alpha_ {H} ^ {*}.\tag{56}
$$

Since α<sup>∗</sup> b α<sup>∗</sup> in this example, $E ( P _ { L 8 H } )$ decreases as p increases. When $p = 1 ,$ , Eq. (36) simpli<sup>fi</sup>es to $( s _ { L } ^ { * } ) ^ { 1 / 2 } = 1 / ( 3 c )$ , resulting in $E ( P _ { L 8 H } ) = E ( P _ { L 2 } ) = E ( P _ { H 2 } ) = 0 . 0 7 4 1$ . Therefore, Strategy 1 is at least as good as Strategy 2 and Strategy 4 for any $p \in [ 0 , 1 ]$ and $k > 1$

It is also observed that in general Strategy 1 is better than Strategy 3 and Strategy 5 (offering data to type I only). However, the situation may be different when p is very small (i.e., the probability of the user being type I is very large). As p decreases, E(P ), $E ( P _ { L 1 } )$ and $E ( P _ { H 1 } )$ all increase. When p reaches a certain critical value, s<sup>∗</sup> will be zero, which implies that the data owner will not offer s<sub>L</sub> data. To <sup>fi</sup>nd out this critical value of ${ \dot { p } } ,$ set $s _ { L } ^ { * }$ in (36) to zero and solve for p, we have

$$
p = 1 - \frac {7}{6 k}.\tag{57}
$$

For this example, $k = 1 . 2 5 . 5 0 ,$ , when $p \leq 1 / 1 5 ,$ , the data owner no longer offers $s _ { L }$ data, and Strategy 1 is the same as Strategy 5. That is, for $k = 1 . 2 5 , \mathrm { i f } p \leq 1 / 1 5 ,$ , then it is optimal for the data owner to offer one type of data and target only the type I user for this data. It is also clear from (57) that an increase in k increases the critical value of p below which it is optimal to offer only one data type.

Finally, consider parameter c (mean unit cost). It is clear from (35), (36), (43), (47), (51) and (55) that the optimal sensitivity level for any strategy is inversely proportional to c. Substituting s<sup>∗</sup> in these equations into (29), (34), (41), (45), (49) and (53), respectively, we <sup>fi</sup>nd that the optimal <sup>fi</sup>xed price for any strategy is also inversely proportional to c; i.e.,

$$
\alpha_ {s} ^ {*} \propto 1 / c, \quad s = \left\{s _ {L} ^ {*}, s _ {H} ^ {*}, s _ {L 1} ^ {*}, s _ {H 1} ^ {*}, s _ {L 2} ^ {*}, s _ {H 2} ^ {*} \right\}.\tag{58}
$$

It follows from (42), (46), (50), (54) and (56) that the data owner's net payoff for any strategy depends on α<sup>∗</sup> but not on $\beta _ { s } ^ { * } .$ . Consequently, as c increases (or decreases), the data owner's net payoffs for all strategies decrease (or increase) proportionally. That is, a change in c will not affect the results in relative comparison between different strategies.

We have analyzed different strategies for scenario (i). The same process of analysis can be applied to scenarios (ii) and (iii). We will not pursue that exercise due to the length constraints. We should point out that the result that the best strategy for the data owner is to offer both types of data is derived based on the utility functions given in this example. The result could be different with different utility functions.

## 5. Practical insights

The buying and selling of customer data are a common practice in database marketing. There are in general two types of data usages in database marketing. In the early analysis stage, the focus is on the use of statistical and data mining techniques to develop models of customer behavior. This corresponds to type A usage. The results of the data analysis are then used in the later stage to select target customers for communications, which can be considered as type I usage. The identifying attributes, such as name, phone number and email address, are typically not useful at the analysis stage but are necessary at the communication stage. The models developed in this study offer valuable insights for data owners who provide the data for database marketing (e.g., Acxiom and credit bureaus). For example, the data owners can offer a lower price (α<sup>∗</sup> and $\beta _ { L } ^ { * } )$ for data without identifying attributes, to be used for analysis/modeling purposes, and a higher price (α<sup>∗</sup> and β<sup>∗</sup> ) for data with identifying attributes, used for communications with individuals. In this way, the data buyer's purpose is self-revealed, and the buyer will have no incentive to buy the data that is not designed for that purpose. Note that α<sup>∗</sup>, β<sup>∗</sup>, α<sup>∗</sup> and β<sup>∗</sup> are optimal prices to the data buyers given their intended purposes. Without this optimality, even if the high sensitivity data are priced higher than the low sensitivity data, the data user does not necessarily end up buying what the user initially intended to buy.

On the buyer's side, the marketers can also bene<sup>fi</sup>t from this pricing scheme. They can buy a large amount of de-identi<sup>fi</sup>ed data at lower price for data analysis and mining, and then acquire a smaller amount of data with identifying attributes based on the results of the data analysis. This enables the marketers to focus on the customers who are more suitable targets, and thus reduce the cost of marketing and the risk of privacy infringement.

The models developed in this study also provide helpful insights for data owners in determining the cost of collecting private data. Since the cost is tied to the price in the model, sensitivity analyses can be performed to more accurately evaluate the cost of data with respect to privacy variables. The College Board, for example, provides students' standardized test score data to colleges and universities at a minor charge [29]. The data is offered at a highly aggregated level due to privacy concern. Consequently, colleges and universities buy excessive amount of data and mail more brochures than necessary to prospective students. However, it is quite likely that many students are not very sensitive about letting universities know their detailed test score information. If the College Board provides a <sup>fi</sup>nancial incentive for students to permit more detailed disclosure of their test data, and likewise charges a higher price for acquiring and using such data, it will be economically more ef<sup>fi</sup>cient for both the universities and the students to <sup>fi</sup>nd their matches.

The proposed incentive-compatible mechanism also helps understand the rationale behind the decision on the DOJ vs. Google case. In this event, the DOJ stated that its purpose of getting data is to <sup>fi</sup>nd patterns in Internet pornography and it had no intention to investigate individual cases. As such, the DOJ played a type A user's role here. The judge ruled that Google provides to the DOJ a small sample set of URLs, which contain website contents but not Google users' identities and thus are of low sensitivity. The judge, however, denied the DOJ's motion to acquire users' search queries from Google's databases, which contain both user identities and website contents and thus are of high sensitivity. This decision is consistent with the proposed incentive-compatible mechanism.

## 6. Future research

Our model considers two types of data consumers, resulting in two corresponding sets of optimal prices and choices. If there are more than two types of data consumers, the other types will be forced to choose from one of the two prices offered, causing non-optimal choices (on the positive side, restricting to two types enables incentivecompatible self-selection even if data users' utility functions are not estimated very accurately). Our modeling framework can be extended to more than two types by adding corresponding IR and IC constraints for the additional types, and adjusting estimated distribution for the type proportion. However, the problem of <sup>fi</sup>nding an optimal set of sensitivity levels might not have a feasible solution when the number of types is greater than two. Moorthy [23] shows that for the market segmentation problem some conditions regarding the relationships in utility functions and type proportions must be satis<sup>fi</sup>ed in order to guarantee the existence of the optimal solution. Perhaps due to this dif<sup>fi</sup>culty, related economics studies typically assume two types of consumers [16,9]. Our problem with more than two types will be more dif<sup>fi</sup>cult than that in Moorthy [23] since it involves two decision variables (s and x) as opposed to only one in Moorthy [23].

## Acknowledgements

Xiao-Bai Li's research was supported in part by the National Library of Medicine of the National Institutes of Health under Grant Number R01LM010942. The content is solely the responsibility of the authors and does not necessarily represent the of<sup>fi</sup>cial views of the National Institutes of Health.

## Appendix A. Proofs of propositions

Proof of proposition 1. Maximizing $R ( s _ { L } , x _ { L } ^ { A } )$ ) will cause at least one of the constraints (10) and (12), which involves $R ( s _ { L } , x _ { L } ^ { A } )$ , to be binding. Similarly, maximizing $R ( s _ { H } , x _ { H } ^ { I } )$ will cause one of constraints (11) and (13) to be binding.

(i) If $U _ { I } ( S _ { L } , \ x _ { L } ^ { I * } ) / \partial x _ { L } ^ { I * } > U _ { A } ( S _ { L } , \ x _ { L } ^ { A * } ) / \partial x _ { L } ^ { A * }$ , then this is the traditional scenario. ${ \mathsf { S } } 0 ,$

$$
U _ {I} \left(s _ {L}, x _ {L} ^ {I}\right) > U _ {A} \left(s _ {L}, x _ {L} ^ {A}\right) \text { and } U _ {I} \left(s _ {H}, x _ {H} ^ {I}\right) > U _ {A} \left(s _ {H}, x _ {H} ^ {A}\right),\tag{A.1}
$$

where $x _ { s } ^ { t } ( t \in \{ A , I \} , s \in \{ s _ { L } , s _ { H } \} )$ is within a small neighborhood of $x _ { s } ^ { t * } .$ Now, suppose (11) is binding; i.e., $R ( s _ { H } , x _ { H } ^ { I } ) = U _ { I } ( s _ { H } , x _ { H } ^ { I } ) .$ Then, it must be that $R ( s _ { L } , x _ { L } ^ { I } ) \geq U _ { I } ( s _ { L } , x _ { L } ^ { I } )$ ), because otherwise the type I user will select the $S _ { L }$ data, which is designed for the type A user. However, if $R ( s _ { H } , x _ { H } )$ and $R ( s _ { L } , x _ { L } )$ are set this way, then it follows from (A.1) that neither of them will be attainable by $U _ { A } ( \cdot )$ . Therefore, (11) is not binding and (13) is binding. That ${ \mathrm { i } } s ,$

$$
R \left(s _ {H}, x _ {H} ^ {I}\right) = U _ {I} \left(s _ {H}, x _ {H} ^ {I}\right) - U _ {I} \left(s _ {L}, x _ {L} ^ {I}\right) + R \left(s _ {L}, x _ {L} ^ {I}\right).\tag{A.2}
$$

Next, because (11) is not binding, (10) must be binding. Otherwise, the data owner can increase $R ( s _ { L } , x _ { L } )$ and $R ( s _ { H } , x _ { H } )$ by the same small amount, which would keep the IC constraints $( 1 2 )$ and (13) always satis<sup>fi</sup>ed. Continue increasing $R ( s _ { L } , x _ { L } )$ and $R ( s _ { H } , x _ { H } )$ in this way, eventually one of the IR constraints (10) and (11) will be binding. Since (11) will not be binding, (10) must be binding. Therefore, (14) holds. It follows from the price function (7) that

$$
R \left(s _ {L}, x _ {L} ^ {I}\right) = R \left(s _ {L}, x _ {L} ^ {A}\right) + \beta_ {L} \left(x _ {L} ^ {I} - x _ {L} ^ {A}\right).\tag{A.3}
$$

Substituting (14) and (A.3) into (A.2), we have (15).

(ii) Given that $U _ { I } ( s _ { L } , x _ { L } ^ { I } )$ is non-monotonic concave and $U _ { A } ( s _ { L } , x _ { L } ^ { A } )$ is increasing concave, condition $U _ { I } ( s _ { L } , x _ { L } ^ { I * } ) / \partial x _ { L } ^ { I * } = U _ { A } ( s _ { L } , x _ { L } ^ { A * } ) / \partial x _ { L } ^ { A * }$ will occur only once. It follows from (9) that $\beta _ { L } = U _ { I } ( s _ { L } , x _ { L } ^ { I * } ) / $ $\partial x _ { L } ^ { I * } = U _ { A } ( s _ { L } , \bar { x _ { L } ^ { A * } } ) / \partial x _ { L } ^ { A * }$ ; that is,

$$
R \left(s _ {L}, x _ {L} ^ {A *}\right) = U _ {A} \left(s _ {L}, x _ {L} ^ {A *}\right),\tag{A.4}
$$

$$
R \left(s _ {L}, x _ {L} ^ {I *}\right) = U _ {I} \left(s _ {L}, x _ {L} ^ {I *}\right).\tag{A.5}
$$

With (A.4), Eq. (14) holds. Substituting (A.4) and (A.5) into (12) and (13) respectively, we have

$$
U _ {A} \left(s _ {H}, x _ {H} ^ {A *}\right) - R \left(s _ {H}, x _ {H} ^ {A *}\right) \leq 0,\tag{A.6}
$$

$$
U _ {I} \left(s _ {H}, x _ {H} ^ {I *} \right.) - R \left(s _ {H}, x _ {H} ^ {I *}\right) \geq 0.\tag{A.7}
$$

As $R ( s _ { H } , x )$ increases, (A.7) will eventually be binding while (A.6) will be further away from binding. Therefore, (13) will be binding and (12) will not. Also, with (A.7) binding, (16) holds.

(iii) If ${ \cal U } _ { I } ( s _ { L } , \ x _ { L } ^ { I * } ) / \partial x _ { L } ^ { I * } < { \cal U } _ { A } ( s _ { L } , \ x _ { L } ^ { A * } ) / \partial x _ { L } ^ { A * }$ , then $\beta _ { L }$ from (9) based on $U _ { A } ( s _ { L } , x _ { L } ^ { A } )$ will be greater than that based on $U _ { I } ( s _ { L } , x _ { L } ^ { I } ) .$ . So, the price function based on the former will dominate that based on the latter; that is, $R ( s _ { L } , x _ { L } ^ { A } ) > R ( s _ { L } , x _ { L } ^ { I } )$ . As a result, to maximize prices, both (10) and (11) must be binding, which is the best possible choice for the data owner out of all feasible binding alternatives. Note that when both (10) and (11) binding, $R ( s _ { L } ,$ $x _ { L } )$ is not attainable by $U _ { I } ( S _ { L } , x _ { L } ^ { I } )$ and $R ( s _ { H } , x _ { H } )$ is not attainable by $U _ { A } ( s _ { H } , x _ { H } ^ { A } )$ ). So the right hand sides of the IC constraints (12) and (13) are negative and both constraints are satis<sup>fi</sup>ed. In other words, the data consumers will have no incentive to select the price designed for the other type.

Proof of proposition 2. It follows from (9) that $\beta _ { L } ^ { * }$ is the slope of $U _ { A } ( s _ { L }$ $x _ { L } ^ { A } ) \mathsf { a t } x _ { L } ^ { A * } .$ . On the other hand, it follows from (18) that $\beta _ { L } ^ { * }$ is also the slope of $C ( s _ { L } , x _ { L } ^ { A } ) \operatorname { a t } x _ { L } ^ { A * }$ . In other words, if we “raise” the convex curve $C ( s _ { L } , x _ { L } ^ { A } )$ such that it eventually tangents with the concave curve $U _ { A } ( s _ { L } , x _ { L } ^ { A } )$ , then $x _ { L } ^ { A * }$ is the tangent point and $\beta _ { L } ^ { * }$ is the slope of the price line that passes $x _ { L } ^ { A * }$ . Thus,

$$
\partial U _ {A} \Big (s _ {L}, x _ {L} ^ {A} \Big) / \partial x _ {L} ^ {A} | _ {x _ {L} ^ {A} = x _ {L} ^ {A *}} = \beta_ {L} ^ {*} = \partial C \Big (s _ {L}, x _ {L} ^ {A} \Big) / \partial x _ {L} ^ {A} | _ {x _ {L} ^ {A} = x _ {L} ^ {A *}}.\tag{A.8}
$$

Similarly, it follows from (9) and (20) that

$$
\partial U _ {I} \Big (s _ {H}, x _ {H} ^ {I} \Big) / \partial x _ {H} ^ {I} | _ {x _ {H} ^ {I} = x _ {H} ^ {I}}. = \beta_ {H} ^ {*} = \partial C \Big (s _ {H}, x _ {H} ^ {I} \Big) / \partial x _ {H} ^ {I} | _ {x _ {H} ^ {I} = x _ {H} ^ {I}}.\tag{A.9}
$$

Consider x $_ { L } ^ { A * } \leq$ x<sup>I∗</sup>. Let $x _ { L } ^ { A * } \leq x \leq x _ { H } ^ { I * }$ . It follows from (2) that $\partial C ( s _ { L } , x ) /$ ∂x $< \partial C ( s _ { H } , x ) /$ ∂x. Thus, by comparing the right sides of (A.8) and (A.9), we have

$$
\partial C \left(s _ {L}, x _ {L} ^ {A}\right) / \partial x _ {L} ^ {A} | _ {x _ {L} ^ {A} = x _ {L} ^ {A *}} <   \partial C \left(s _ {H}, x _ {H} ^ {I}\right) / \partial x _ {H} ^ {I} | _ {x _ {H} ^ {I} = x _ {H} ^ {I *}} \Rightarrow \beta_ {L} ^ {*} <   \beta_ {H} ^ {*}.
$$

Now, $\mathrm { i f } \ x _ { L } ^ { A * } > x _ { H } ^ { I * } ,$ , let $x _ { L } ^ { A * } \geq x \geq$ x<sup>I∗</sup>. It follows from (3) that $\partial U _ { A } ( s _ { L } , x ) /$ $\partial x < \partial U _ { I } ( s _ { H } , x ) / \partial x$ . Thus, by comparing the left sides of (A.8) and (A.9), we have

$$
\partial U _ {A} \Big (s _ {L}, x _ {L} ^ {A} \Big) / \partial x _ {L} ^ {A} | _ {x _ {L} ^ {A} = x _ {L} ^ {A *}} <   \partial U _ {I} \Big (s _ {H}, x _ {H} ^ {I} \Big) / \partial x _ {H} ^ {I} | _ {x _ {H} ^ {I} = x _ {H} ^ {I *}} \Rightarrow \beta_ {L} ^ {*} <   \beta_ {H} ^ {*}.
$$

## References

[1] N.R. Adam, J.C. Wortmann, Security-control methods for statistical databases: a comparative study, ACM Computing Surveys 21 (4) (1989) 515–556.

[2] X. Bai, R. Gopal, M. Nunez, D. Zhdanov, A decision methodology for managing operational ef<sup>fi</sup>ciency and information disclosure risk in healthcare processes, Decision Support Systems 57 (2014) 406–416.

[3] F. Bélanger, R.E. Crossler, Privacy in the digital age: a review of information privacy research in information systems, MIS Quarterly 4 (35) (2011) 1017–1041.

[4] H.K. Cheng, K. Dogan, Customer-centric marketing with Internet coupons, Decision Support Systems 44 (3) (2008) 606–620.

[5] Centers for Medicare and Medicaid Services, Agreement for use of Centers for Medicare and Medicaid Services (CMS) data containing individual identi<sup>fi</sup>ers, Retrieved May 5, 2013 http://www.resdac.org/sites/resdac.org/<sup>fi</sup>les/RIF\_DataUseAgreement.pdf

[6] College Board, Guidelines for the release of data, Retrieved May 5, 2013 http://www. collegeboard.com/prod\_downloads/research/RDGuideforReleaseData.pdf.

[7] DOJ vs. Google, Ruling on Department of Justice vs. Google Inc. case, Retrieved April 23, 2007 http://www.google.com/press/images/ruling\_20060317.pdf 2006

[8] M.A.H. Farquad, I. Bose, Preprocessing unbalanced data using support vector machine, Decision Support Systems 53 (1) (2012) 226–233.

[9] D. Fudenberg, J. Tirole, Game Theory, The MIT Press, Cambridge, MA, 1991.

[10] R. Gar<sup>fi</sup>nkel, R.D. Gopal, M. Nunez, D.O. Rice, Secure electronic markets for private information, IEEE Transactions on Systems, Man, and Cybernetics, Part A 36 (3) (2006) 461–471.

[11] R. Gopal, R. Gar<sup>fi</sup>nkel, P. Goes, Con<sup>fi</sup>dentiality via camou<sup>fl</sup>age: the CVC approach to disclosure limitation when answering queries to databases, Operations Research 50 (3) (2002) 501–516.

[12] KDnuggets, Google subpoena: child protection vs. privacy, Retrieved April 23, 2007 http://www.kdnuggets.com/polls/2006/google\_subpoena.htm 2006.

[13] I.-H. Hann, K.L. Hui, S.Y.T. Lee, I.P.L. Png, Online Information Privacy: Measuring the Cost-Bene<sup>fi</sup>t Trade-Off, Proceedings of the 23rd International Conference on Information Systems, Association for Information Systems, 2002, pp. 13–42.

[14] K.L. Hui, I.P.L. Png, The Economics of Privacy, in: T. Hendershott (Ed.), Handbooks in Information Systems, Vol. 1, Elsevier, 2006, pp. 471–498.

[15] H. Ishibuchi, T. Nakashima, M. Nii, Genetic-Algorithm-Based Instance and Feature Selection, in: H. Liu, H. Motoda (Eds.), Instance Selection and Construction for Data Mining, Kluwer Academic, Norwell, MA, 2001, pp. 95–112.

[16] J. Jaisingh, J. Barron, S. Mehta, A. Chaturvedi, Privacy and pricing personal information, European Journal of Operational Research 187 (3) (2008) 857–870

[17] K.C. Laudon, Markets and privacy, Communications of the ACM 39 (9) (1996) 92–104.

[18] X.-B. Li, A scalable decision tree system and its application in pattern recognition and intrusion detection, Decision Support Systems 41 (1) (2005) 112–130.

[19] X.-B. Li, V.S. Jacob, Adaptive data reduction for large-scale transaction data, European Journal of Operational Research 188 (3) (2008) 910–924.

[20] X.-B. Li, S. Sarkar, Protecting privacy against record linkage disclosure: a bounded swapping approach for numeric data, Information Systems Research 22 (4) (2011).774-789

[21] X.-B. Li, S. Sarkar, Class-restricted clustering and microperturbation for data privacy, Management Science 59 (4) (2013) 796–812.

[22] Y. Li, Empirical studies on online information privacy concerns: literature review and an integrative framework, Communications of the Association for Information Systems 28 (1) (2011)(Article 28).

[23] K. Moorthy, Market segmentation, self-selection, and product line design, Marketing Science 3 (4) (1984) 288–307.

[24] M. Mussa, S. Rosen, Monopoly and product quality, Journal of Economic Theory 18 (2)(1978) 301-317

[25] L. Stokes, T. Belin, What is a Margin of Error? in: F. Scheuren (Ed.), What Is a Survey? American Statistical Association, Alexandria, VA. 2004, pp. 63–67.

[26] H.J. Smith, T. Dinev, H. Xu, Information privacy research: an interdisciplinary review, MIS Quarterly 35 (4) (2011) 989–1015

[27] L. Sweeney, k-anonymity: a model for protecting privacy, International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems 10 (5) (2002) 557–570.

[28] L. Sweeney, Privacy-preserving surveillance using database from daily life, IEEE Intelligent Systems 20 (5) (2005) 83–84.

[29] R. Whiting, Who's Buying and Selling Your Data? Everybody, Information Week, July 10 2006, 30–32.

[30] D. Zhu, X.-B. Li, S. Wu, Identity disclosure protection: a data reconstruction approach for privacy-preserving data mining, Decision Support Systems 48 (1) (2009) 133–140.

Xiao-Bai Li is a Professor of MIS in the Department of Operations and Information Systems, Manning School of Business at the University of Massachusetts Lowell. He received his Ph.D. in management science from the University of South Carolina. Dr. Li's research focuses on data mining, information privacy, and information economics. He has received funding for his research from National Institutes of Health (NIH) and National Science Foundation (NSF). His work has appeared or is forthcoming in Decision Support Systems, Information Systems Research, Management Science, MIS Quarterly, Operations Research, IEEE Transactions (TKDE, TSMC, TAC), Communications of the ACM, INFORMS Journal on Computing, and European Journal of Operational Research, among others.

Srinivasan Raghunathan is a Professor of Information Systems in the School of Management, The University of Texas at Dallas. He obtained B.Tech degree in Electrical Engineering from IIT, Madras, Post Graduate Diploma in Management from IIM, Calcutta, and Ph.D. in Business Administration from the University of Pittsburgh. His current research interests are in the economics of information security and the value of collaboration in supply chains. His papers have been published in journals such as Management Science, Operations Research, Information Systems Research, Decision Analysis, Journal of MIS, Decision Support Systems, IEEE transactions, IIE transactions, European Journal of Operational Research, and Production and Operations Management, among others.
