---
otero_id: 6482
otero_key: "Z2K8D8FV"
title: "Privacy Protection in Data Mining: A Perturbation Approach for Categorical Data"
authors: "Xiao-Bai Li; Sumit Sarkar"
year: "2006"
journal: "Information Systems Research"
doi: "10.1287/isre.1060.0095"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/Z2K8D8FV/fulltext/images/b6f452c180b41414cb1511c73199d931831654f495dc63261ed44fb0f314f9e5.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Privacy Protection in Data Mining: A Perturbation Approach for Categorical Data

Xiao-Bai Li, Sumit Sarkar,

## To cite this article:

Xiao-Bai Li, Sumit Sarkar, (2006) Privacy Protection in Data Mining: A Perturbation Approach for Categorical Data. Information Systems Research 17(3):254-270. http://dx.doi.org/10.1287/isre.1060.0095

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2006, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/Z2K8D8FV/fulltext/images/8044db29d880b4083dd01defe9c6deae93e3bc160022e9269c43010c0a35f2e3.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Privacy Protection in Data Mining: A Perturbation Approach for Categorical Data

Xiao-Bai Li

College of Management, University of Massachusetts Lowell, Lowell, Massachusetts 01854, bob\_li@uml.edu

Sumit Sarkar

School of Management, University of Texas at Dallas, Richardson, Texas 75080, sumit@utdallas.edu

o respond to growing concerns about privacy of personal information, organizations that use their cus tomers’ records in data-mining activities are forced to take actions to protect the privacy of the individuals involved. A common practice for many organizations today is to remove identity-related attributes from the customer records before releasing them to data miners or analysts. We investigate the effect of this practice and demonstrate that many records in a data set could be uniquely identified even after identity-related attributes are removed. We propose a perturbation method for categorical data that can be used by organizations to pre vent or limit disclosure of confidential data for identifiable records when the data are provided to analysts for classification, a common data-mining task. The proposed method attempts to preserve the statistical properties of the data based on privacy protection parameters specified by the organization. We show that the problem can be solved in two phases, with a linear programming formulation in Phase I (to preserve the first-order margina distribution), followed by a simple Bayes-based swapping procedure in Phase II (to preserve the joint distri bution). Experiments conducted on several real-world data sets demonstrate the effectiveness of the proposed method.

Key words: privacy; data confidentiality; data mining; linear programming; Bayesian estimation; data swapping History: Salvatore T. March, Senior Editor; Amit Basu, Associate Editor. This paper was received on November 3, 2004, and was with the authors 8 <sup>1</sup> months for 2 revisions.

## 1. Introduction

In recent years, we have observed an explosion of digital data generated and collected by individuals and organizations, due to the widespread use of computers and the Internet, and advances in storage and database systems. In tandem with this unprecedented growth of technologies to collect and store data, techniques for data mining have gained popularity in a wide variety of domains, including database marketing, credit and loan evaluation, medical diagnostics, fraud detection, and Web usage analysis. While successful business applications of data mining are encouraging, there are increasing concerns about invasions of and potential threats to privacy of personal information by information technology in general, and by data mining in particular. A survey by Time/CNN (Greengard 1996) revealed that 93% of respondents believed companies selling personal data should be required to gain permission from the individuals. In another study (Culnan 1993), more than 70% of participants responded negatively to questions related to the secondary use of private information. In 1990, Lotus attempted to release a CD-ROM with data on about 100 million U.S. households. However, the product generated such strong public protests regarding privacy issues that Lotus was forced to withdraw the project (Rotenberg 1992). Recent studies point to similar growing concerns with privacy (Wang et al. 1998, Stanford Student Computer and Network Privacy Project 2002).

To resolve the conflict between data mining and privacy protection, researchers in the data-mining community have proposed various methods. Agrawal and Srikant (2000) considered building a decision tree classifier from data where the confidential values have been perturbed. Evfimievski et al. (2002) presented a framework for mining association rules from transaction data that have been randomized to preserve individuals’ privacy. Other studies on privacy preserving mining can be found in Estivill-Castro and Brankovic (1999), Atallah et al. (1999), and Verykios et al. (2004). This stream of research tends to approach the privacy issue from a data miner’s standpoint, focusing on techniques for mining those data sets where confidential values are deleted or perturbed due to privacy concerns. We believe, however, it is more important to approach the issue from the standpoint of an organization that owns data, because the primary concern of a data miner is to discover useful knowledge from the data, while an organization has to set privacy protection as its first priority. Another problem with this stream of research is that a proposed method typically applies to a specific data-mining task (e.g., classification). Whether or not such a method can also be used to effectively preserve some basic properties of the data, such as summary statistics, is seldom addressed. In practice, both data mining—such as classification— and summary statistics can be important to an organization. Therefore, it is desirable to have a privacy protection technique that works for both purposes.

The issue of protecting confidential data is not new. There has been extensive research in the area of statistical databases (SDB) on how to provide summary statistical information without disclosing individuals’ confidential data. The privacy issue arises in SDB when summary statistics are derived using data on very few individuals (or a single individual). In this case, releasing summary statistics leads to disclosure of individual confidential data. The methods for preventing such disclosure can be broadly classified into two categories: query restriction, which prohibits queries that would reveal confidential data; and data perturbation, which alters individual data in a way such that the summary statistics remain approximately the same. Adam and Wortmann (1989) have presented an excellent survey of these methods. In general, both query restriction and data perturbation methods have been extensively investigated and employed (see, for example, Liew et al. 1985, Cox 1995, Muralidhar et al. 1999, Duncan and Mukherjee 2000, Sarathy and Muralidhar 2002).

The privacy issues in data mining are somewhat different from those in SDBs. First, the main purpose of an SDB is to provide summary statistics, while data mining focuses on tasks such as classification and mining association rules. A data-mining technique essentially relies on discovering relationships between data attributes. Preserving such relationships may or may not be consistent with preserving summary statistics. Second, in an SDB a user normally cannot retrieve a complete relational table and can use only a few limited query types, often restricted to viewing aggregate statistics, to retrieve information. In data mining, relational (not contingency) tables containing individual records have to be released to data miners in order to perform the above data-mining tasks. Therefore, query restriction methods are no longer applicable and data perturbation becomes the primary approach for privacy protection in data mining. Finally, many data-mining tasks involve processing and analyzing categorical attributes (e.g., the class attribute in classification and all attributes in association rules mining). Although there are studies that deal with categorical data in the SDB research (Cox 1995, Chowdhury et al. 1999, Fienberg and McIntyre 2004), most of them are directed at data presented in a summarized contingency table, with an emphasis on preserving summary statistics. Garfinkel et al. (2002) proposed a privacy protection method that applies to data in a relational table, but the method is limited to cases where confidential attributes are binary. There do exist a few approaches in SDB that are applicable to data-mining settings; these are discussed in some detail in §2.

In this study, we investigate the privacy problem where individual records in a data set can be uniquely identified without using identity-related attributes. We propose a data perturbation method that can be used by organizations to prevent disclosure of individuals’ confidential information, while providing the data to analysts for data mining. The proposed method attempts to preserve the statistical distributions of the data based on privacy protection parameters specified by the organization. We show that the problem can be solved in two phases: in Phase I, a linear programming formulation is used to preserve the marginal distribution; and in Phase II, a simple Bayesbased swapping procedure is employed to preserve the joint distribution. The proposed method applies to categorical data (either as originally represented, or as converted from numeric values).

The rest of the paper is organized as follows. In §2, we describe the privacy problem investigated in this study and discuss related research work. Section 3 provides a conceptual formulation of the problem. Section 4 describes details of our methodology.

Results of experiments conducted on real-world data are presented in §5. We conclude the paper and provide directions for future research in §6.

## 2. The Privacy Protection Problem and Related Work

## 2.1. Background

Typically, there are three parties involved in the privacy problem in data mining: (1) the data owner (the organization that owns the data) who has complete access to the data and wants to discover knowledge from the data without compromising the confidentiality of the data; (2) individuals who provide their personal information to the data owner and want their privacy protected; and (3) the data miner (insider or outsider) who, with access only to the data released by the data owner, performs data mining for the data owner. In this study, we focus on situations where the data owner hires the data miner as a third party due to the need for data-mining expertise or resources, and has to consider the data miner as a potential data snooper. The data owner can also be a not-for-profit organization (e.g., government agency) that is obligated to release the data, more likely in summarized or perturbed forms, to the public or some professional organizations. In that case, anyone who has the access to the released data can be regarded as a potential data snooper (Adam and Wortmann 1989, Fienberg et al. 1998).

There is a common misconception in many organizations that if the identity-related attributes—such as social security number, name, and phone number— are removed from the released data there will be no leak in individuals’ confidential data to the third party. The fact is, a data set with identity-related attributes removed would still contain many unique records, which can be often identified by a method such as a GROUP BY query or a sorting algorithm. With some additional information, the data snooper can easily find an individual’s confidential data. To demonstrate the problem, let us look at a hypothetical, but realistic, example.

A life insurance company wants to know the relationship between the amount of death benefit (confidential) and a set of demographic attributes (nonconfidential), in order to launch an effective marketing initiative.

A consultant is hired to conduct such analysis. The company provides him with a data set consisting of its 100,000 customer records. To prevent disclosure of confidential data, attributes such as account number, name, and phone number are deleted. In addition, the values of some attributes are grouped. For example, the amount of death benefit is grouped into a few categories; the location attribute only shows which state the customer resides in, instead of the complete street address. The data released to the consultant includes the death benefit amount (grouped) and six demographic attributes: age (5), gender (2), location (50), education (5), occupation (10), and marital status (5), where the number of categories for each attribute is shown in parentheses. The company would believe that no confidential data could be disclosed from this processed data set. A simple calculation, however, shows a different picture. The total number of category combinations for the six attributes is $5 \times 2 \times$ $5 0 \times 5 \times 1 0 \times 5 = 1 2 5 , 0 0 0 .$ Assuming each category combination is presented with equal likelihood, then each of the 100,000 customers will be a unique record. In real situations, of course, the assumption of the uniform distribution across all dimensions is rather unrealistic. More likely, some customers will share the same attribute values, but others will have unique values. These unique individuals will be exposed to the risk of confidentiality disclosure. Suppose the consultant has noted that there is a unique record with {Age 60–69, Gender Female, Location FL, Education Bachelor, Occupation Retired, Marital status <sub>=</sub> Widowed}, which matches the demographic data of one of his relatives. If he knew this relative has an account with the company, then he has effectively discovered the amount range of his relative’s death benefit. This disclosure could have serious financial, legal, or even criminal implications.

## 2.2. Related Work

The data in the problem described above are all categorical. A popular approach to privacy protection for categorical data is data swapping, which involves exchange of confidential categorical values among individual records. The notion of data swapping was introduced by Schlörer (1981) (who used the term “data transformation”) and Dalenius and Reiss (1982). These studies discussed disclosure measures for categorical data, and proposed a data utility measure called the t-order statistics; this measure refers to statistical quantities computed from the values of exactly t attributes. The properties of data swapping, such as the conditions to preserve the t-order statistics in swapping, were discussed in these studies. However, no specific algorithms for data swapping were given. In fact, Dalenius and Reiss (1982) indicated that, based on their earlier studies, an algorithm for exactly preserving the t-order statistics in data swapping is computationally intractable when t is large.

To make data swapping practical, Reiss (1984) proposed a data-swapping method that approximately preserves the t-order statistics. The method first computes the t-order statistics, which consists of a set of contingency tables of different orders, from the original data set. It then constructs a new data set where individual attribute values are selected according to probability distributions computed from the original contingency tables. One problem with this method, as Adam and Wortmann (1989) pointed out, is that the errors for summary statistics based on the swapped data potentially can be very high. From a data-mining perspective, there is another critical problem with this method—the requirement for computing all contingency tables up to order t, based on the original data. Let $A _ { j } \ ( j = 1 , \ldots , t )$ be the t attributes involved. Then, the size of a t-order contingency table is $\begin{array} { r } { S _ { t } = \prod _ { j = 1 } ^ { t } | A _ { j } | , } \end{array}$ where $| A _ { j } |$ is the number of categories of ${ \dot { A } } _ { j } .$ The total number of statistics that can be derived from the table is $2 ^ { S _ { t } } - 1$ (Denning and Schlörer 1983). A datamining algorithm typically involves using some quantities that are closely related to the t-order statistics where both t and $| A _ { j } |$ could be large. In this sense, this method is computationally very expensive, even as an approximate method.

Fienberg et al. (1998) and Gouweleeuw et al. (1998) proposed data swapping and perturbation methods for categorical data in somewhat different settings. Instead of considering the complete data set, these studies assume that only a sample of the complete set is released. Obviously, releasing a perturbed (or even unperturbed) sample has lower disclosure risk than releasing the complete data set, because less information is released. However, as far as data utility is concerned, data-mining results based on a sample, even unperturbed, could be substantially different from those based on the complete set (Li and

Jacob 2005). In terms of methodology, the approach proposed by Gouweleeuw et al. (1998) works essentially on individual or blocks of attributes independently, therefore, “the precise effect on more complicated analyses, such as regression models, can be difficult to assess” (Fienberg and McIntyre 2004, p. 24). Observing that the multivariate cumulative distribution function (c.d.f.) for a categorical data set is equivalent to the table of conditional probabilities based on the contingency table of the respective order, Fienberg et al. (1998) proposed a loglinear model-based perturbation method that generates sample data based on the empirical multivariate c.d.f. computed from the original data. While the method appears more rigorous than generic data swapping in Dalenius and Reiss (1982) and Reiss (1984) from a viewpoint of statistical inference, it also faces the problem of high computational cost when higher-order statistics have to be considered, as in data mining, since it essentially involves computing the same contingency tables as those in Reiss (1984).

A data-swapping method using decision trees was proposed in Estivill-Castro and Brankovic (1999). This method aims at maintaining the same decision rules while perturbing the data. The basic idea is to first build a decision tree on the original data, and then randomly swap the class values, which is confidential, within those leaves that include records with different classes. This method is computationally inexpensive, and could be quite useful in classification applications. Some critical issues remain to be addressed, however. First, this method does not provide adequate protection for records in a leaf with homogeneous class. Suppose, in the example in §2.1, there are five (instead of one) records with values $\displaystyle \{ \mathrm { A g e } = 6 0 – 6 9 _ { \cdot } $ , Gender  Female, Location FL, Education Bachelor, Occupation Retired, Marital status <sub>=</sub> Widowed}, and they all have the same grouped death benefit amount. A decision tree algorithm will assign these five records into the same leaf. If this leaf contains only these five records, then none of them will be perturbed. As a result, the consultant would still be able to find his relative’s death benefit amount. Another problem with this method is that the proportion of records that can be used in swapping depends on the magnitude of classification errors because perturbation takes place only in leaves with multiple class values (where errors occur). If the decision tree built on the original data has a very low error rate, then only a small portion of the data could be perturbed.

Sullivan and Fuller (1990) proposed a different approach to perturbing categorical data. Their idea is to transform categorical data first into binary (0– 1) values and then into standard normal values. Perturbation is then performed by adding normally distributed noise to the transformed data. For a data set with J categorical attributes $A _ { j } \ ( j = 1 , \ldots , J )$ , the binary conversion would create $\begin{array} { r } { \dot { \sum } _ { j = 1 } ^ { J } | A _ { j } | - 2 J } \end{array}$ additional attributes in the data set. This could lead to storage and computation time problems for a large data set. More importantly, while adding normal noise does keep the transformed data normal, the original joint distribution is generally not expected to be preserved when the data are transformed back, as noted by the authors themselves (Sullivan and Fuller 1990). The other drawbacks of this method include difficulty in understanding and setting parameters, and high computation cost due to calculations of a distance measure during perturbation, which practically limits the capacity of this algorithm to a few thousand records (Brand and Giessing 2002).

In summary, among the existing methods, the one proposed by Reiss (1984) appears to be most relevant to our problem. Most of the methods described above are directed at an SDB setting and the main concern of these methods centers on maintaining summary statistics of limited order while perturbing data. When applied to a data-mining setting, these methods are either computationally expensive or unable to preserve relationships between attributes. The perturbation method proposed in this study is intended to overcome these problems. That is, our algorithm attempts to preserve relationships between attributes with a reasonable computation cost. Furthermore, we would like to point out that none of the aforementioned methods has made a distinction between records with different disclosure risks. For each of these methods, the same swapping or perturbation mechanism is applied to all data items. In a real-world data set, however, the disclosure risks for different records are often different. For example, an identifiable record will be more vulnerable to disclosure than an unidentifiable record. Therefore, it is desirable to provide different degrees of perturbation for different types of records. We adopt this strategy in our approach.

## 3. Problem Formulation

To formulate the privacy protection problem described in §2.1 rigorously, we first define some terms. We assume that there is only one confidential attribute in the data, but the definitions below can be easily applied to data with multiple confidential attributes; we discuss in $\ S 6$ how our approach can be extended to cases with multiple confidential attributes. The definitions are explained using a reduced life insurance example shown in Table 1, which has one confidential attribute (Amount) and three nonconfidential attributes.

Definition 1. A full pattern is a category combination that involves all attributes. A nonconfidential pattern is a category combination that involves all nonconfidential attributes.

For example, the category combination {Age <sub>=</sub> 30–39, Gender Female, Location CA, Amount Med}, as shown in Record 1, is a full pattern, while the part {Age <sub>=</sub> 30–39, Gender <sub>=</sub> Female, Location <sub>=</sub> CA} is a nonconfidential pattern.

Definition 2. A record is identifiable if its full pattern can be completely determined by its nonconfidential pattern. A record is uniquely identifiable if it is identifiable and there does not exist another record that has the same full pattern. A group of records are collectively identifiable if each member record is identifiable and all members of the group have the same full pattern; in this case, each member of the group is also said to be collectively identifiable.

Table 1 An Illustrative Example

<table><tr><td>Number</td><td>Age</td><td>Gender</td><td>Location</td><td>Amount</td><td>Identifiable status</td></tr><tr><td>1</td><td>30–39</td><td>Female</td><td>CA</td><td>Med</td><td>U</td></tr><tr><td>2</td><td>30–39</td><td>Female</td><td>NY</td><td>Low</td><td>V1</td></tr><tr><td>3</td><td>30–39</td><td>Female</td><td>NY</td><td>Low</td><td>V1</td></tr><tr><td>4</td><td>30–39</td><td>Male</td><td>CA</td><td>Med</td><td>V2</td></tr><tr><td>5</td><td>30–39</td><td>Male</td><td>CA</td><td>Med</td><td>V2</td></tr><tr><td>6</td><td>30–39</td><td>Male</td><td>NY</td><td>High</td><td>U</td></tr><tr><td>7</td><td>40–49</td><td>Female</td><td>CA</td><td>Med</td><td>U</td></tr><tr><td>8</td><td>40–49</td><td>Female</td><td>NY</td><td>Med</td><td></td></tr><tr><td>9</td><td>40–49</td><td>Female</td><td>NY</td><td>High</td><td></td></tr><tr><td>10</td><td>40–49</td><td>Male</td><td>CA</td><td>Low</td><td>U</td></tr><tr><td>11</td><td>40–49</td><td>Male</td><td>NY</td><td>High</td><td>V3</td></tr><tr><td>12</td><td>40–49</td><td>Male</td><td>NY</td><td>High</td><td>V3</td></tr><tr><td>13</td><td>50–59</td><td>Female</td><td>NY</td><td>Low</td><td>U</td></tr><tr><td>14</td><td>50–59</td><td>Male</td><td>CA</td><td>Med</td><td></td></tr><tr><td>15</td><td>50–59</td><td>Male</td><td>CA</td><td>High</td><td></td></tr><tr><td>16</td><td>50–59</td><td>Male</td><td>NY</td><td>High</td><td>U</td></tr></table>

In Table 1, a record marked U is uniquely identifiable, and a record with V is collectively identifiable (V1, V2, and V3 denote three different groups). An unmarked record is unidentifiable. Next, we define a term related to collectively identifiable and unidentifiable records.

Definition 3. A set of records that share the same nonconfidential pattern is called a same nonconfidential pattern group, or SNP group.

For example, Records 2 and 3 form an SNP group, and Records 8 and 9 form another SNP group. Clearly, a record is either uniquely identifiable, or it belongs to an SNP group.

There are two major types of disclosure about individuals (Duncan and Lambert 1989). They are identity disclosure (or reidentification), which occurs when a data snooper is able to match a record in a data set to an individual, and value (or attribute) disclosure, which occurs when a snooper is able to predict the confidential values of an individual record. Let U be the set of all uniquely identifiable records. Obviously, a record in U can be identified definitively. One way to avoid this identity disclosure is to remove all records (or all confidential values) in U from the released data, which is similar to cell suppression in SDBs. However, as we will see in $\ S 5 ,$ set U often accounts for a significant proportion of the original data. Removing U from the released set could have a serious negative impact on data utility. In this study, we assume that the data owner’s goal is not to prevent or reduce identity disclosure by removing set U from the released set; instead, the goal is to limit value disclosure for those records in U by perturbing the confidential values of a specified proportion, $p ,$ of the records in U.

For a collectively identifiable record, its identity disclosure risk is lower than that of a uniquely identifiable record. However, it is not important for a data snooper to identify which member record in a collectively identifiable group is the target record because all members in the group are identical. In terms of value disclosure, a collectively identifiable record has the same risk as a uniquely identifiable record. For an unidentifiable record, its value disclosure risk is lower than that of an identifiable record in that the confidential value of the unidentifiable record cannot be obtained deterministically even when all of its nonconfidential values are known. However, an unidentifiable record could still be subjected to a high risk of value disclosure if the confidential value distribution of the related SNP group is significantly different from that of the complete data set. Similar to set U, we consider limiting value disclosure for collectively identifiable and unidentifiable records by perturbing the confidential values of a specified proportion, q, of high-risk records. In general, the disclosure risk of a record in an SNP group is high when the records in the group are highly homogenous (with collectively identifiable groups being the extreme case), and the risk is low when the confidential value distribution in the group is close to the overall distribution (since knowing the nonconfidential pattern of a record in such a group does not help much in determining its confidential value). To measure the value disclosure risk for a record in an SNP group with this desired property, we introduce a distance measure, based on the classical chi-square statistic, defined below:

Definition 4. Let C be the number of categories of the confidential attribute in a data set. Let M and m be the number of records in the full data set and in an SNP group, respectively. Similarly, let $M _ { k }$ and $m _ { k }$ $( k = 1 , \ldots , C )$ be the frequency counts of the kth confidential categories, respectively. The distance between the confidential attribute distributions in the full data set and in the SNP group can be measured by

$$
X ^ {2} = \sum_ {k = 1} ^ {C} \frac {[ m _ {k} - (m / M) M _ {k} ] ^ {2}}{(m / M) M _ {k}}.\tag{1}
$$

Clearly, $X ^ { 2 }$ attains its minimum value of zero if and only if $m _ { k } / m = M _ { k } / M , k = 1 , \ldots , C .$ . This property perfectly satisfies a requirement for the risk measure described above—the disclosure risk should be at the minimum when the frequency distribution of the confidential values in an SNP group is the same as the overall distribution. Moreover, since $( m / M ) M _ { k }$ is the expected count of the kth confidential value in the SNP group, $X ^ { 2 }$ follows a $\chi ^ { 2 }$ distribution with $C - 1$ degrees of freedom. So, we can determine whether the two distributions are significantly different in a probabilistic sense, with a prespecified significance level .

We now turn to our problem formulation. The objective of the problem is to maintain the joint distribution of all attributes, while satisfying the privacy protection policy set by the data owner. It is usually not possible to completely preserve the joint distribution. Since the marginal distribution of the confidential attribute is used in summary statistics, preserving this becomes an important goal in itself. The problem, then, is

## Minimize

(G1) the distance between the original and perturbed marginal distributions of the confidential attribute; and

(G2) the distance between the original and perturbed joint distributions;

subject to

(C1) U is perturbed with proportion p;

(C2) for each SNP group, if $X ^ { 2 } > \chi _ { \alpha } ^ { 2 } ( C - 1 )$ , then a proportion q of the records in this group are perturbed; otherwise, no record in this group is perturbed.

The significance level  indicates the threshold probability of concluding that the distributions are different when they are in fact the same. The proportions $p$ and $q ,$ and significance level $\alpha ,$ can be viewed as parameters indicating the trade-off between disclosure risk and data quality. In general, a larger $p ,$ q, or $\alpha$ value will lead to a better protection of confidential data but cause the perturbed distributions to move farther away from the original distributions (and thus lead to a less reliable data-mining outcome), while a smaller $p , q ,$ or  will have an opposite effect. However, if these parameters are set overly large, disclosure risk can actually increase. Suppose that these parameters are set such that all confidential values are perturbed. If a data snooper has learned this information, then he can exclude the currently released values in his search for the true values. In particular, when the confidential attribute is binary $( C = 2 )$ , all of the original values can be discovered by simply reversing the perturbed values. Dinur and Nissim (2003) discussed, for a data set with all attributes binary, how to determine the minimum proportion of data that should be perturbed. The result of their study may be helpful for determining parameters p and $q$ although their study does not consider the identifiability of a record. We believe parameters $p$ and q should be determined based on the characteristics of individual data sets.

It is easy to see that solutions to satisfy (C1) and (C2) can always be found. Given that the above problem involves optimizing multiple objectives, we adopt a two-phase strategy to solve the problem, as stated below:

Phase I: Minimize (G1), subject to constraints (C1) and (C2).

Phase II: Minimize (G2), subject to constraints (C1), (C2), and the following additional constraint:

(C3) The marginal distribution of the perturbed confidential data is preserved during Phase II.

## 4. The Perturbation Approach

## 4.1. Phase I: Preserving the Marginal

## Distributions

Consider set U first. Let $N _ { k }$ (a known quantity) be the number of records in U originally having the kth confidential category. Let $n _ { k h }$ be the number of records in U changed from the kth to the hth category; that is, $n _ { k h } { \bf s }$ are decision variables whose values are to be determined by the Phase I optimization procedure. If the marginal distribution remains the same after perturbation, then

$$
\sum_ {h = 1, \dots , C; h \neq k} n _ {k h} = \sum_ {h = 1, \dots , C; h \neq k} n _ {h k}, \quad k = 1, \dots , C.
$$

If this condition cannot be satisfied, then there exists either a slack (if $\sum n _ { k h } < \sum n _ { h k } )$ or a surplus $( \mathrm { i f } \sum n _ { k h } >$ $\sum n _ { h k } )$ quantity. Let $s _ { k } ^ { - }$ and $s _ { k } ^ { + }$ , both nonnegative, be such a slack and a surplus variable, respectively. Then, the Phase I problem can be formulated as a linear programming (LP) problem, as follows:

$$
\min \sum_ {k = 1} ^ {C} (s _ {k} ^ {-} + s _ {k} ^ {+}),\tag{2a}
$$

$$
\text { s.t. } \sum_ {k = 1} ^ {C} \sum_ {h = 1, \dots , C; h \neq k} n _ {k h} = p \sum_ {k = 1} ^ {C} N _ {k},\tag{2b}
$$

$$
\sum_ {h = 1, \dots , C; h \neq k} n _ {k h} - \sum_ {h = 1, \dots , C; h \neq k} n _ {h k} + s _ {k} ^ {-} - s _ {k} ^ {+} = 0,
$$

$$
k = 1, \ldots , C,\tag{2c}
$$

$$
\sum_ {h = 1, \dots , C; h \neq k} n _ {k h} \leq N _ {k}, \quad k = 1, \dots , C.\tag{2d}
$$

This problem always has a feasible solution since constraint (2b) merely requires the proportion of perturbed records to be $p ,$ and appropriate values can always be found for slack and surplus variables, $s _ { k } ^ { - }$ and $s _ { k } ^ { + } .$ , to satisfy (2c). When the optimal value of objective function (2a) is zero, the marginal distribution of the confidential attribute is completely preserved; otherwise, it is impossible to preserve the marginal distribution. The optimal solution for some $n _ { k h }$ may be fractional. In this case, we simply round it to an integer, which should not be an issue because $n _ { k h }$ is large in data-mining problems. It is possible to have multiple optimal solutions. Of course, in most implementations, an LP solver returns the first one it finds.

Applying formulation (2) to the records in set U in the life insurance example, we have the following LP problem (here, p is set to 0.5):

$$
\begin{array}{l l} \min & s _ {1} ^ {-} + s _ {1} ^ {+} + s _ {2} ^ {-} + s _ {2} ^ {+} + s _ {3} ^ {-} + s _ {3} ^ {+}, \\ \text {s.t.} & n _ {1 2} + n _ {1 3} + n _ {2 1} + n _ {2 3} + n _ {3 1} + n _ {3 2} = 3 (= 0. 5 \times 6), \\ & n _ {1 2} + n _ {1 3} - n _ {2 1} - n _ {3 1} + s _ {1} ^ {-} + s _ {1} ^ {+} = 0, \\ & n _ {2 1} + n _ {2 3} - n _ {1 2} - n _ {3 2} + s _ {2} ^ {-} + s _ {2} ^ {+} = 0, \\ & n _ {3 1} + n _ {3 2} - n _ {1 3} - n _ {2 3} + s _ {3} ^ {-} + s _ {3} ^ {+} = 0, \\ & n _ {1 2} + n _ {1 3} \leq 2, \\ & n _ {2 1} + n _ {2 3} \leq 2, \\ & n _ {3 1} + n _ {3 2} \leq 2, \end{array}
$$

where subscripts 1, 2, and 3 index the three confidential values, and all variables are nonnegative. An optimal solution to this LP problem is $n _ { 1 2 } = 1 , n _ { 2 3 } = 1$ $n _ { 3 1 } = 1$ , and all of the remaining variables, including slack and surplus variables, are equal to zero. Based on this solution, we should perturb one $' \mathrm { L o w } ^ { \prime \prime }$ record to “Med,” one “Med” record to “High,” and one “High” record to “Low.” The optimal objective function value reaches zero, indicating the marginal distribution of the confidential attribute is preserved.

Now consider the collectively identifiable and unidentifiable records. Let W be the set of records selected for perturbation based on constraint (C2). Which record(s) in an SNP group should be selected into W is again related to the disclosure risk. Ideally, for an SNP group we should select those records such that the marginal distribution of the remaining records in the group is as close to the overall marginal distribution as possible because these records will not be perturbed. For an SNP group of m records, this selection computation involves comparing $C _ { q m } ^ { m }$ choices. Alternatively, a random sampling method can be used. Once W is chosen, the LP formulation described above can be applied to perturbing all records in W by setting $p = 1$

## 4.2. Phase II: Preserving the Joint Distribution

Let X be the set of nonconfidential attributes, which is not subject to perturbation. Let Y be the confidential attribute. Let P X Y  and $\tilde { P } ( { \bf x } , Y )$ be the original and perturbed joint distributions, respectively. Let $D ( P ( { \bf \dot { X } } , Y ) , \tilde { P } ( { \bf X } , { \bf \dot { Y } } ) )$ be the distance between PX Y  and $\widetilde { P } ( \mathbf { X } , Y )$ , to be minimized in Phase II. Using the well-known I-Divergence (also known as Kullback-Leibler distance) measure, this distance can be defined as

$$
D (P (\mathbf {X}, Y), \widetilde {P} (\mathbf {X}, Y)) = \sum_ {i} P (\mathbf {X} _ {i}, Y _ {i}) \log \frac {P (\mathbf {X} _ {i} , Y _ {i})}{\widetilde {P} (\mathbf {X} _ {i} , Y _ {i})},\tag{3}
$$

where i ranges over all possible full patterns. It follows that ${ \cal D } ( P ( { \pmb x } , Y ) , \tilde { P } ( { \pmb x } , Y ) )$ is minimized if and only if (Kullback 1959)

$$
P (\mathbf {X} _ {i}, Y _ {i}) = \tilde {P} (\mathbf {X} _ {i}, Y _ {i}), \quad \forall i,\tag{4}
$$

which is equivalent to

$$
P (Y _ {i} \mid \mathbf {X} _ {i}) = \widetilde {P} (Y _ {i} \mid \mathbf {X} _ {i}), \quad \forall i,\tag{5}
$$

since $\widetilde { P } ( \mathbf { X } _ { i } ) = P ( \mathbf { X } _ { i } )$ for each i (nonconfidential data are not perturbed). This condition is unlikely to hold because, for pattern i, perturbing its true confidential value $y _ { i t }$ to a different value $y _ { i r }$ will cause $P ( Y _ { i } =$ $y _ { i t } \left| \mathbf { X } _ { i } \right)$ to decrease and $P ( Y _ { i } = y _ { i r } \mid \mathbf { X } _ { i } )$ to increase. That is,

$$
P (Y _ {i} = y _ {i t} \mid \mathbf {X} _ {i}) > \tilde {P} (Y _ {i} = y _ {i t} \mid \mathbf {X} _ {i}), \quad \mathrm{and}\tag{6a}
$$

$$
P (Y _ {i} = y _ {i r} \mid \mathbf {X} _ {i}) <   \tilde {P} (Y _ {i} = y _ {i r} \mid \mathbf {X} _ {i}).\tag{6b}
$$

Let I be the index set for all records available for perturbation. Define two positive quantities for each $i \in I$ as below:

$$
\Delta P _ {i} (t) = P (Y _ {i} = y _ {i t} | \mathbf {X} _ {i}) - \tilde {P} (Y _ {i} = y _ {i t} | \mathbf {X} _ {i}),\tag{7a}
$$

$$
\Delta P _ {i} (r) = \tilde {P} (Y _ {i} = y _ {i r} | \mathbf {X} _ {i}) - P (Y _ {i} = y _ {i r} | \mathbf {X} _ {i}).\tag{7b}
$$

Our goal now is to select and perturb a set of records, indexed by $I _ { \ast } ,$ whose size is determined by constraints (C1) and (C2), such that

$$
\sum_ {i \in I _ {*}} \{\Delta P _ {i} (t) + \Delta P _ {i} (r) \}\tag{8}
$$

is the minimum among all possible sets that satisfy (C1) and (C2). However, it is difficult to evaluate $\tilde { P } ( \cdot )$ because it changes every time a related record is perturbed. To simplify the problem, we take the minimax approach, which considers the worst case scenario for each $\tilde { P } ( \cdot )$ . That is, instead of minimizing (8), we perturb a set of records, indexed by $I _ { \ast } ,$ such that

$$
\sum_ {i \in I _ {*}} \max \{\Delta P _ {i} (t) + \Delta P _ {i} (r) \}\tag{9}
$$

is the minimum among all possible sets that satisfy (C1) and (C2). It follows from Equations (7a) and (7b) that

$$
\begin{array}{c} \max \{\Delta P _ {i} (t) + \Delta P _ {i} (r) \} \\ = P (Y _ {i} = y _ {i t} | \mathbf {X} _ {i}) + 1 - P (Y _ {i} = y _ {i r} | \mathbf {X} _ {i}). \end{array}\tag{10}
$$

This implies that, to minimize expression (9), we should select and perturb record i for which

$$
P (Y _ {i} = y _ {i t} \mid \mathbf {X} _ {i}) - P (Y _ {i} = y _ {i r} \mid \mathbf {X} _ {i})\tag{11}
$$

is as small as possible. The intuition behind this criterion is that we should perturb a record’s confidential value from its true value to a new value when the conditional probability with the true value is low and that with the new value is high.

It is interesting to note that this criterion for perturbing confidential attributes follows a probabilistic principle similar to that for constructing a decision rule in classification problems. When using Bayesian decision theory to minimize classification error, an object should be assigned to the class having the maximum conditional probability $P ( Y \mid \mathbf { x } )$ , where Y denotes the class attribute (a random variable), and x represents the observed attribute values of the object (Duda et al. 2001). Therefore, minimizing the distance between the true and perturbed joint distributions in our perturbation problem is consistent with minimizing error in classification problems, when the confidential attribute is considered as the class attribute.

To estimate the conditional probability in (11), one should naturally consider the full-order conditional estimator (that makes no assumptions of any kind), which estimates $P ( Y _ { i } \mid \mathbf { X } _ { i } )$ based on the ith full and nonconfidential patterns in the data. For example, based on Records 8 and 9 in Table 1, the full-order estimator yields estimates P(High  40–49, Female, $\mathrm { N Y } ) = 1 / 2$ , P(Med  40–49, Female, $\mathrm { N Y } ) = 1 / 2 ,$ and P(Low 40–49, Female, $\mathrm { N Y } = 0 .$ . The estimator is not useful, however, in terms of minimizing the distance between the joint distributions. More precisely, for identifiable patterns, the value associated with criterion (11) using the full-order conditional estimator is constant no matter which, and how, identifiable records are perturbed. In fact, estimating the probabilities for values of confidential attributes of identifiable patterns is problematic since only a single full pattern exists with the corresponding nonconfidential pattern. Motivated by this reasoning, we consider using the simple Bayes estimator, which avoids high-order computation by assuming conditional independence (i.e., $P ( X _ { l } \mid Y , X _ { j } ) = P ( X _ { l } \mid Y ) \ \forall j \neq l ,$ for a given Y value) to estimate $\dot { P ( Y _ { i } \mid \mathbf { X } _ { i } ) }$

Let J be the number of nonconfidential attributes. The simple Bayes estimator for $P ( Y _ { i } \mid \mathbf { X } _ { i } )$ , the posterior probability of $Y _ { i }$ given $\mathbf { \boldsymbol { x } } _ { i } ,$ is given by

$$
P (Y _ {i} \mid \mathbf {X} _ {i}) = \frac {P (Y _ {i})}{P (\mathbf {X} _ {i})} \prod_ {j = 1} ^ {J} P (X _ {i j} \mid Y _ {i}), \quad \forall i,\tag{12}
$$

where $X _ { i j }$ is the jth attribute of $\mathbf { X } _ { i } ,$ . Substituting expression (12) into (11), we obtain the difference in posterior $d _ { i } ( t , \boldsymbol { r } )$ , due to perturbing record $i ^ { \prime } \mathrm { s }$ confidential value from $y _ { i t }$ to $y _ { i r } ,$ , as

$$
d _ {i} (t, r) = K _ {i} \left\{\hat {P} \left(y _ {i t}\right) \prod_ {j = 1} ^ {J} \hat {P} \left(x _ {i j} \mid y _ {i t}\right) - \hat {P} \left(y _ {i r}\right) \prod_ {j = 1} ^ {J} \hat {P} \left(x _ {i j} \mid y _ {i r}\right) \right\},\tag{13}
$$

where x and $y$ are the observed values of random variables X and $Y ; { \hat { P } } ( \cdot )$ is the estimate of $P ( \cdot ) ;$ and $K _ { i } = 1 / \hat { P } ( \mathbf { x } _ { i } )$ is a constant (normalizing factor) for the ith pattern. The Phase II problem can now be stated as

$$
\min \sum_ {i} d _ {i} (t, r),\tag{14a}
$$

s.t. constraints (C1), (C2), and (C3)

(14b)

The above problem can be formulated as an integer program (Li and Sarkar 2005). However, we do not attempt to solve the problem with a traditional integer programming technique, due to the high computational cost. The generic representation of problem (14) is adequate to understand our computational procedure described in §4.3.

## 4.3. Computational Procedure

Observing that the value of objective function (14a) can be reduced by making a swap between the confidential values of different records, we develop an iterative swapping procedure to solve problem (14). To reduce the computational complexity, we restrict our search space to the class of pair-wise swaps, each involving only two records, defined below:

Definition 5. A swap of two records refers to an exchange of the confidential values of the two records. That is, a swap between record $( \mathbf { x } _ { a } , y _ { a } )$ and record $( \mathbf { x } _ { b } , y _ { b } )$ , where $y _ { a } \neq y _ { b } ,$ sets the first record to $( \mathbf { x } _ { a } , y _ { b } )$ and the second to $( \mathbf { x } _ { b } , y _ { a } )$

Clearly, a swap defined this way always preserves the marginal distribution of Y (constraint (C3)). To satisfy the other two constraints in (14b), we define an admissible swap as follows:

Definition 6. A swap is admissible if constraints (C1) and (C2) remain satisfied after the swap.

We have developed a set of rules for determining whether a swap is admissible. These rules are closely related to the implementation of the computational algorithm and are discussed in Appendix A. Furthermore, we define a measure, called cost, as below:

Definition 7. The cost of an admissible swap between records i and j is defined as

$$
c _ {i j} = \left[ d _ {i} \left(t _ {i}, r _ {i}\right) - d _ {i} \left(t _ {i}, h _ {i}\right) \right] + \left[ d _ {j} \left(t _ {j}, r _ {j}\right) - d _ {j} \left(t _ {j}, h _ {j}\right) \right],\tag{15}
$$

or equivalently, by substituting Equation (13) into (15),

$$
c _ {i j} = d _ {i} (h _ {i}, r _ {i}) + d _ {j} (h _ {j}, r _ {j}),\tag{16}
$$

where t refers to the original confidential value, and h and r refer to confidential values before and after the swap, respectively. The cost of an inadmissible swap is an arbitrarily large number.

Note that the confidential value for a record before a swap may be different from that record’s original confidential value as the record may have been perturbed in Phase I or in some swap in a prior iteration.

In Equation (15), $d _ { i } ( t _ { i } , h _ { i } )$ represents the difference in the posterior probability for the confidential attribute value for record i before the swap as compared to the original value, while $d _ { i } ( t _ { i } , \boldsymbol { r } _ { i } )$ represents the difference after the swap. If $d _ { i } ( t _ { i } , r _ { i } ) < d _ { i } ( t _ { i } , h _ { i } )$ , then the conditional probability of the modified confidential value after the swap is closer to that of the original value than that before the swap. So, perturbing record i from $h _ { i }$ to $r _ { i }$ helps minimize the objective value in problem (14) if $d _ { i } ( t _ { i } , r _ { i } ) - d _ { i } ( t _ { i } , h _ { i } )$ is negative. A similar observation is made for perturbing record j. Therefore, a swap involving records i and j will cause the value of objective function (14a) to decrease if the cost in Equation (15) is negative. On the other hand, a swap associated with a positive cost will cause the objective value to increase. Under the restriction of pair-wise swaps, therefore, minimizing differences in probability, as expressed in (14a), can be stated in terms of optimizing the cost, i.e.,

$$
\min \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} s _ {i j},\tag{17a}
$$

where variable $s _ { i j }$ is defined as

$$
\begin{array}{r l} s _ {i j} = - c _ {i j} & \text { if } c _ {i j} <   0, \\ = 0 & \text { otherwise }. \end{array}\tag{17b}
$$

The constraints for this problem are the same as in problem (14). The optimization problem can now be translated into a process of eliminating negative costs via swapping. When all of the costs are nonnegative, Equation (17a) reaches the optimal value of zero.

## Table 2 Computational Algorithm

1. Find an initial perturbed set by solving the linear programming problem in §4.1.

2. For each record i in U and W, compute posterior probabilities $\hat { P } ( y _ { i k } \mid \mathbf { x } _ { i } ) ( k = 1 , \ldots , C )$ based on Equation (12).

3. Swapping procedure:

a. Identify all admissible swaps, and compute the cost associated with each of these swaps based on Equation (16).

b. Let  be a list of all swaps with a negative cost. Sort  in ascending order (i.e., the most negative one first).

c. Perform swapping sequentially for the items in the sorted . Suppose the current swap involves records and . Then, if any of the remaining swaps in  also involves record or $\beta ,$ remove that swap from .

4. Repeat Step 3 until all costs are nonnegative.

The computational algorithm is outlined in Table 2. Steps 3 and 4 of the algorithm use a repeated sorting procedure to efficiently perform an exhaustive search for optimal swaps. Because there are at most $N ( N -$ 1/2 pairwise swaps available, the algorithm is guaranteed to converge to the optimal value of zero (with a polynomial time order). Keep in mind, however, the optimal solution to problem (17) is not guaranteed to be the optimal to problem (14).

Next, we discuss the computational complexity of the algorithm. The LP problem in Step 1 involves $2 C +$ 1 constraints, CC 1 decision variables, and 2C slack and surplus variables, where C is the number of confidential categories. C is unlikely to be large in practice. Computing posterior probabilities in Step 2 is of order $O ( N J C )$ , which is approximately linear in N because N is dominantly larger than C and J (number of nonconfidential attributes). Computing the costs in Step 3(a) is of order $O ( N ^ { 2 } )$ , and sorting the costs in Step 3(b) is of OL log L, where $L \ ( = \rvert \mathcal { L } | )$ is the number of swaps having a negative cost. Step 3(c) is also of OL log L since performing swaps on the sorted list is linear in L, while searching for redundant records is of Olog L. So, the time complexity for Step 3 is of $O ( N ^ { 2 } + L \log L )$ . There are at most $\dot { N } ( N - 1 ) / \bar { 2 }$ total swaps available. Step 3 eliminates N /2 swaps (each committed swap will never be reversed since such a reverse would cause a positive cost), so it will take at most N <sub>−</sub> 1 loops of Step 3 to converge. Therefore, the time complexity for the Phase II swapping procedure is of order $O ( N ^ { 3 } + N L \log L )$ . We note that the actual time complexity is usually substantially lower because a large proportion of swaps are inadmissible (e.g., more than 90% in our experiments).

The results of applying the algorithm to the life insurance example are shown in Table 3, where $p = 0 . 5$ and $q = 0 . 5 .$ . Calculations for posterior probabilities in Columns 2, 3, and 4 are illustrated in Appendix B. The Phase I perturbed column shows the perturbation results based on the LP solution described in §4.1. As shown earlier, the marginal distribution of the confidential attribute (Amount) remains unchanged. The Phase II swaps are shown with arrows. For example, the Amount value for Record 1 is perturbed from $\bar { \iota } _ { \mathrm { ( M e d ^ { \prime \prime } } }$ to “High” in Phase I. A swap between Record 1 and 7 (which is not perturbed in Phase I) is made in Phase II, which resets Record 1’s value to “Med” and perturbs the value for Record 7 from “Med” to “High.” The objective function value, the sum of $d _ { i } \mathbf { s } ,$ is reduced from 4.0718 to 2.4237 after such swaps. It can be verified that the solution shown in the Phase II perturbed column is the optimum for objective (17a), as well as for objective (14a).

## 5. Experimental Evaluation

The proposed method is evaluated using three realworld data sets. The Association for Information Systems has a Web site that conducts annual surveys of MIS faculty salary offers (Galletta 2004). We selected the salary data from 1999 to 2002 (attributes are consistent for these four years and somewhat different for the other years). The data set consists of 509 records of faculty members who received offers during the period. There are 13 attributes, including salary offered, position, course load, number of years teaching, region, year indicator, etc. The identityrelated attributes such as name and e-mail address, if submitted, were deleted from the published data. Salary was considered as the confidential attribute and was chosen as the class attribute. Numeric salary values were grouped into three categories. After running a sorting algorithm on the data, we found that 502 out of 509 records were identifiable and 478 of them were uniquely identifiable. So, it is not difficult to discover the salary of a survey participant.

Table 3 Computational Results for the Example

<table><tr><td>No.</td><td> $p(Low | \mathbf{x})$ </td><td> $p(Med | \mathbf{x})$ </td><td> $p(High | \mathbf{x})$ </td><td>Original amount</td><td>Phase I perturbed</td><td> $d(t, r)$ </td><td>Phase II perturbed</td><td> $d(t, r)$ </td></tr><tr><td>1</td><td>0.2269</td><td>0.7563</td><td>0.0168</td><td>Med</td><td>High</td><td>0.7395</td><td>Med</td><td>0</td></tr><tr><td>6</td><td>0.2842</td><td>0.1895</td><td>0.5263</td><td>High</td><td></td><td>0</td><td>Low</td><td>0.2421</td></tr><tr><td>7</td><td>0.1698</td><td>0.7547</td><td>0.0755</td><td>Med</td><td></td><td>0</td><td>High</td><td>0.6792</td></tr><tr><td>10</td><td>0.0476</td><td>0.6349</td><td>0.3175</td><td>Low</td><td></td><td>0</td><td>Med</td><td>-0.5873</td></tr><tr><td>13</td><td>0.6090</td><td>0.0902</td><td>0.3008</td><td>Low</td><td>Med</td><td>0.5188</td><td>Low</td><td>0</td></tr><tr><td>16</td><td>0.1130</td><td>0.0502</td><td>0.8368</td><td>High</td><td>Low</td><td>0.7238</td><td>High</td><td>0</td></tr><tr><td>2</td><td>0.7431</td><td>0.1651</td><td>0.0917</td><td>Low</td><td>Med</td><td>0.5780</td><td>Med</td><td>0.5780</td></tr><tr><td>4</td><td>0.0826</td><td>0.8257</td><td>0.0917</td><td>Med</td><td>High</td><td>0.7339</td><td>High</td><td>0.7339</td></tr><tr><td>11</td><td>0.0769</td><td>0.0684</td><td>0.8547</td><td>High</td><td>Low</td><td>0.7778</td><td>Low</td><td>0.7778</td></tr><tr><td>Sum</td><td></td><td></td><td></td><td></td><td></td><td>4.0718</td><td></td><td>2.4237</td></tr></table>

Note. In this example, the significance level was set to 0.5, which is larger than conventional values, to ensure that sufficient SNP groups are perturbed.

The second data set, collected from Blake et al. (1998), was originally extracted from the U.S. Census Bureau databases. It contains 48,842 records, each with 15 attributes (6 numeric and 9 categorical). These attributes provide an individual’s demographic information such as age, gender, race, education, occupation, marital status, income, etc. The income attribute, which has two categories, was considered confidential and also chosen as the class attribute. In order to apply the proposed algorithm, the numeric attributes in the data set were converted to categorical ones based on the equal-frequency binning method implemented in the Weka data-mining package (Witten and Frank 2000). Using the sorting algorithm, we found that 35,818 out of 48,842 records were identifiable and 19,567 of them were uniquely identifiable.

The third data set was taken from Lerman et al. (1991). It includes survey data of 1,473 married women about their contraceptive method choice (CMC). There are 10 attributes, including contraceptive method choice (confidential, with three categories), wife’s age, wife’s education, husband’s education, number of children, occupation, religion, etc. The two numeric attributes, wife’s age and number of children, were converted to categorical ones using Weka. Out of 1,473 records, 692 were identifiable, and 486 were uniquely identifiable.

The effectiveness of the proposed method is evaluated based on its performance in two important data mining and data warehousing tasks: classification analysis and summary statistics. The C4.5 decision tree induction system (Quinlan 1993) was used for classification. To evaluate classification performance, we randomly divided each data set into two parts: approximately 70% for training and 30% for testing.

The training sets serve as the original set for perturbation, while the testing sets are not perturbed. The relevant summary statistics in our problem are the categorical frequency distributions of the confidential attributes. More precisely, for each data set we calculate the average error rate on frequency distributions as below:

$$
\text { Error   rate } = \frac {1}{C} \sum_ {k = 1} ^ {C} \frac {| \widetilde {F} _ {k} - F _ {k} |}{F _ {k}},\tag{18}
$$

where $F _ { k }$ and $\widetilde { F } _ { k }$ are the frequency count for the kth category of the confidential attribute in the original and perturbed data set, respectively, and C is the number of the confidential categories.

Four perturbation methods were used in the experiments: a random perturbation, two swapping methods based on Reiss (1984), and the proposed method. We coded a program that randomly perturbs the confidential values approximately proportional to the original marginal distribution, but without considering the joint distribution of the data. The Reiss (1984) method is selected because it appears to be the most relevant one to our problem among the existing methods (as discussed in §2.2). Because preserving arbitrarily high-order statistics is computationally very expensive, we considered two relatively efficient implementations, one that attempts to preserve the 2-order statistics and another that attempts to preserve the 3-order statistics, in the swapped data. The source program for Reiss (1984) is not available, so we encoded the algorithms ourselves, as described in Appendix C. All methods are applied subject to constraints (C1) and (C2) in §3, so that comparisons can be made based on the same disclosure risk. For each data set, the same perturbation parameters (p, q, and  were applied for all four methods. These parameters were set such that 50% of the records were actually perturbed in each case. We generated perturbed data sets using the four methods, and then computed performance measures. The results of the random perturbation and Reiss (1984) methods vary somewhat with different random number seeds. Therefore, these three algorithms were run five times, respectively, each run using a different seed. The average results are reported in Table 4. The perturbation time in the third column of Table 4 refers to the time taken to generate the perturbed data. The error rate for summary statistics are calculated based on Equation (18), and the classification results are derived on the reserved test data set.

Table 4 Experimental Results

<table><tr><td>Data set</td><td>Method</td><td>Perturbation time (sec.)</td><td>Proportion perturbed (%)</td><td>Classification error rate (%)</td><td>Summary stat error rate (%)</td></tr><tr><td rowspan="5">Offer</td><td>Original</td><td></td><td></td><td>34.31</td><td></td></tr><tr><td>Random*</td><td>0.29</td><td>50.00</td><td>55.62</td><td>11.11</td></tr><tr><td>Reiss 2-order*</td><td>0.32</td><td>50.00</td><td>57.66</td><td>4.56</td></tr><tr><td>Reiss 3-order*</td><td>0.41</td><td>50.00</td><td>55.64</td><td>4.85</td></tr><tr><td>Proposed</td><td>0.36</td><td>50.00</td><td>40.15</td><td>0.69</td></tr><tr><td rowspan="5">Census</td><td>Original</td><td></td><td></td><td>16.32</td><td></td></tr><tr><td>Random*</td><td>6.97</td><td>50.00</td><td>51.64</td><td>67.62</td></tr><tr><td>Reiss 2-order*</td><td>15.66</td><td>50.00</td><td>41.80</td><td>37.79</td></tr><tr><td>Reiss 3-order*</td><td>37.59</td><td>50.00</td><td>37.02</td><td>37.18</td></tr><tr><td>Proposed</td><td>29.65</td><td>50.00</td><td>29.98</td><td>31.14</td></tr><tr><td rowspan="5">CMC</td><td>Original</td><td></td><td></td><td>45.96</td><td></td></tr><tr><td>Random*</td><td>0.44</td><td>50.00</td><td>55.89</td><td>7.70</td></tr><tr><td>Reiss 2-order*</td><td>0.52</td><td>50.00</td><td>53.07</td><td>3.09</td></tr><tr><td>Reiss 3-order*</td><td>0.82</td><td>50.00</td><td>54.09</td><td>3.90</td></tr><tr><td>Proposed</td><td>0.72</td><td>50.00</td><td>49.65</td><td>0.00</td></tr></table>

∗The average results over five runs are reported for the Random method and the two Reiss methods.

For all the data sets, the proposed method clearly outperforms the other three methods on error measures for both classification and summary statistics. The error rates for summary statistics in the census data are high for all methods. This is because the marginal distribution of the confidential attribute in this data is quite unbalanced (about 23% to 77%). For such unbalanced data, it is not possible for any method to preserve the marginal distribution if the perturbation proportion is large. The proposed method, however, does lead to the least difference in the marginal distributions. In practice, it is the small minority class that is particularly sensitive in such highly unbalanced data (e.g., a small proportion of HIV cases in a set of patient records). In such cases, it is not necessary to apply an overly large perturbation proportion. We note that the performance of the two methods based on Reiss (1984) were very close on both error measures. The only situation where the 3-order method is significantly better is the classification of census data. However, the run times for the 3-order method are considerably longer than the 2-order method (and also longer than the proposed method).

We generally expect a positive relationship between preserving summary statistics and preserving classification accuracy. This is borne out by the performance of our method (as well as all the other methods) across the three data sets. As we see in Table 4, the relative deterioration of classification performance is the least for the CMC data and the most for the census data, which is the same ordering for the summary statistics performance. We would like to point out that the ability of our method to maintain the summary statistics does not depend as much on the perturbation proportion, provided the distribution of the confidential attribute is not overly unbalanced for a given perturbation proportion. On the other hand, the classification performance typically deteriorates with higher perturbation proportions.

To further investigate the relationships between the performance and the degree of perturbation, and between the performance and the proportion of data that are identifiable, we performed additional experiments on the CMC data. In addition to the original training data, which has about 39% uniquely identifiable records (and therefore 61% of SNP group records), we prepared two more data sets: one with 25% uniquely identifiable records, created by randomly deleting some uniquely identifiable records in the original set; the other with 75% uniquely identifiable records, created by randomly deleting some records from the SNP groups. Each data set was then perturbed by the four methods with six different perturbation proportions: 25%, 37.5%, 50%, 62.5%, 75%, and 90%, which were obtained by setting parameters p, q, and  appropriately. The results for classification and summary statistics are shown in Figures 1 and 2, respectively.

The proposed method clearly outperforms the other methods in every experiment. For classification, an increase in perturbation proportion causes the distance between the joint distributions to increase, which leads to higher error rates. However, our method is able to keep error rates relatively low until about two-thirds of the records are perturbed. We observe that the proportion of uniquely identifiable records does not have a significant impact on classification performance. This is understandable because classification rules produced by decision trees often rely only on a subset of the available attributes. Such rules may be generated even if all records in the data

Error rate (%)

Error rate (%)

Error rate (%)

## Figure 1 Classification Error Rates

(a) 25% uniquely identifiable records (error rate for unperturbed set = 46.42%)  
![](/api/attachments/Z2K8D8FV/fulltext/images/ad1884bf0a6527fda1acbb383874b0c8e63d41c943adce6b18763db0d46e1cbf.jpg)

Figure 2 Error Rates for Summary Statistics  
(a) 25% uniquely identifiable records  
![](/api/attachments/Z2K8D8FV/fulltext/images/523fa5b762dac734bc86e021e2fa2650451be26a217bc9ed61fc40f7fb500569.jpg)  
(b) 39% uniquely identifiable records (original training set)

(b) 39% uniquely identifiable records (this is original training set; error rate = 45.96%)  
![](/api/attachments/Z2K8D8FV/fulltext/images/da4f0c674f76a8174e88e7d0ba78fcf62e7d61793d8b961719ba6422d32a1d44.jpg)  
(c) 75% uniquely identifiable records (error rate for unperturbed set = 44.11%)

![](/api/attachments/Z2K8D8FV/fulltext/images/1ff131a461b73a4006fe43f59e8c79c167e01af8083765ce1d9230a06bf13f23.jpg)  
(c) 75% uniquely identifiable records

![](/api/attachments/Z2K8D8FV/fulltext/images/2cbf3943074622fe664b07d731d2d7064987f16284fffe959ba2524c1f074a1b.jpg)

set are uniquely identifiable. Therefore, the proportion of records that are unique, in terms of category combinations involving all attributes, is not necessarily a factor. Our method essentially preserves the marginal distributions of the confidential attribute for all perturbation proportions and all ratios of uniquely identifiable to SNP group records, as shown in Figure 2 (small errors associated with our method are mostly caused by rounding fractional values to integers, as discussed in §4.1). This is because the distribution of the confidential attribute for the CMC data does not include a category that is too dominant, and the LP formulation in Phase I of our method is able to preserve the distribution for all perturbation proportions considered. On the other hand, Figure 2 shows that the performances of the other methods on summary statistics are clearly affected by the perturbation proportions.

![](/api/attachments/Z2K8D8FV/fulltext/images/61518a06b13476311278b02e7ad9d60503cbb0fba39ad154e5383aa1495f7f80.jpg)

## 6. Discussion and Extensions

The proposed method can be extended to handle multiple categorical confidential attributes. If there are little or no correlations between the confidential attributes, the proposed method can be applied directly by running the computational procedure multiple times, each run perturbing one confidential attribute in turn. When the confidential attributes are correlated, we suggest two ways in which our method can be extended. The first way is to consider all confidential attributes together as one compound attribute. Suppose, for instance, the Location attribute in the life insurance example is also confidential. A compound attribute called “Location Amount” can be created, which would have six categories, formed by different combinations of Location and Amount values. The transformed data set would have two nonconfidential and one (compound) confidential attributes. The proposed method can then be applied to this transformed data set. The second approach to handle multiple confidential attributes is somewhat simpler. The proposed method can be applied by running the computational procedure multiple times, each run perturbing one confidential attribute while considering the other confidential attributes as nonconfidential. Assume, again, that Location is confidential. The procedure to perturb the Amount values is the same as described in this paper (where Location is considered nonconfidential). To perturb the Location values, the Amount attribute is used as if it is nonconfidential. Because the Bayes estimates for one confidential attribute involve using the remaining confidential attributes (as well as all nonconfidential attributes), the relationships between confidential attributes are expected to be reasonably preserved.

We have assumed in this work that the confidential attributes are represented using prespecified categories. This is the case in many medical and health management applications (e.g., medical treatments), social science applications (e.g., sexual orientation, criminal records, etc.), as well as business and financial applications, where the grouping of originally numeric attributes is predetermined (e.g., income level specified using multiple choices in a survey). In other applications, confidential attributes may be presented in numeric forms. How the values of numeric attributes are grouped will clearly have an impact on the proportion of records in a data set that are identifiable. Similarly, merging categorical values can also reduce the proportion of identifiable records (Iyengar 2002). The disadvantage of grouping and merging is that they also reduce data quality. This is a related problem that needs further investigation.

## Acknowledgments

The authors wish to thank the associate editor and three anonymous reviewers for their insightful comments and suggestions, which have improved the paper considerably.

## Appendix A. Rules for Admissible Swaps

Let U<sup>r</sup> and U<sup>u</sup> be the set of perturbed and unperturbed records in U, respectively. For the life insurance example in Table 3, after Phase I, $\dot { \mathbf { U } } ^ { r } = \{ 1 , 1 3 , 1 6 \} , \mathbf { U } ^ { u } = \{ 6 , 7 , 1 0 \}$ (and $\pmb { W } = \{ 2 , 4 , 1 1 \} )$ . We do not consider any record that is not in U or W because, based on constraint (C2), the confidentia value of these records should remain the same in the perturbation process. To describe the set of rules for admissible swaps, we first define a term:

Definition 8. A cross-category swap is a swap between two records that have different original confidential values.

The essential property of the admissible swap is that, after such a swap, perturbation proportions for set U should remain unchanged, and all records in W should still be perturbed. Whether this property will hold depends on whether the swap is cross-category, and to which set of U<sup>r</sup>, U<sup>u</sup>, and W the two records involved in the swap belong. We enumerated all possible scenarios and identified the following rules:

Rule 1. No swap between two records in $\mathbf { U } ^ { u }$ is allowed. This is obvious because the swap will cause <sub></sub>U<sup>u</sup><sub></sub> to decrease and U<sup>r</sup> to increase.

Rule 2. No swap between W and U<sup>u</sup> is allowed. If we allow such a swap, then an unperturbed record in U<sup>u</sup> will be perturbed. Because U<sup>r</sup> is not involved in the swap, the ratio U<sup>r</sup> / U<sup>u</sup> will change.

Rule 3. No cross-category swap between a record in U<sup>r</sup> and a record in U<sup>u</sup> is allowed. To explain this rule, let a and b be the true and current categories for the record in U<sup>r</sup> , respectively. Let c be the (true and current) category for the record in U<sup>u</sup>. We have $a \neq b$ since the record in U<sup>r</sup> is a perturbed one, a <sub>=</sub> c since this is a cross-category swap, and b <sub>=</sub> c by Definition 5. If this swap is made, then the first record will have a perturbed value of c, and the second record will have a perturbed value of b. Because the first record is still a perturbed one but the second record is changed from unperturbed to perturbed, U<sup>r</sup> is increased by one and U<sup>u</sup> is decreased by one.

Rule 4. A cross-category swap can be made only if the four involved categories (i.e., the first record’s true and current categories, and the second record’s true and current categories) belong to four different categories. Let a and b be the first record’s true and current categories, respectively, and let c and d be the second record’s true and current categories, respectively. We have $a \neq c$ because this is a crosscategory swap, and $b \neq d$ by Definition 5. If both $a = b$ and $c = d _ { , }$ then this is the case described in Rule 1; if $a = b$ or $c = d$ but not both, then this is the case described in Rule 3. Therefore, $a \neq b$ and $c \neq d$ . If $a = d ,$ then the first record’s confidential attribute is reset to its true value after the swap, which will cause either U<sup>r</sup> or $| \mathbf { W } |$ to decrease. Therefore, 0 $\iota \neq d .$ Similarly, $c \neq b .$ We have established that $a , b , c ,$ and d must each be distinct.

## Appendix B. Calculations of Probabilities for Columns 2, 3, and 4 in Table 3

Consider Record 1. The prior (marginal) probabilities for the three confidential categories are

$$
P (\text { Low }) = 4 / 1 6, \quad P (\text { Med }) = 6 / 1 6, \quad \text { and } \quad P (\text { High }) = 6 / 1 6.
$$

We then compute the conditional probabilities for $\{ { \mathrm { A g e } } =$ 30–39}, given a certain Amount value:

$$
P (3 0 - 3 9 \mid \text { Low }) = 2 / 4, \quad P (3 0 - 3 9 \mid \text { Med }) = 3 / 6, \quad \text { and }
$$

$$
P (3 0 - 3 9 \mid \text { High }) = 1 / 6.
$$

Similarly, the conditionals for {Gender <sub>=</sub> Female} and {Location <sub>=</sub> CA} are

$$
P (\text { Female } \mid \text { Low }) = 3 / 4, \quad P (\text { Female } \mid \text { Med }) = 3 / 6, \quad \text { and }
$$

$$
P (\text { Female } \mid \text { High }) = 1 / 6;
$$

$$
\begin{array}{c} P (\mathrm{CA} \mid \text { Low }) = 1 / 4, \quad P (\mathrm{CA} \mid \text { Med }) = 5 / 6, \quad \text { and } \\ P (\mathrm{CA} \mid \text { High }) = 1 / 6. \end{array}
$$

Finally, we compute the posterior probabilities based on Equation (12):

$$
\begin{array}{c} P (\text { Low } \mid 3 0 - 3 9, \text { Female }, \text { CA }) = (1 / P) (4 / 1 6) (2 / 4) (3 / 4) (1 / 4) \\ = (3 / 1 2 8) / P, \end{array}
$$

$$
\begin{array}{r l} P (\text {Med} \mid 3 0 - 3 9, \text {Female}, \text {CA}) & = (1 / P) (6 / 1 6) (3 / 6) (3 / 6) (5 / 6) \\ & = (5 / 6 4) / P, \quad \text {and} \end{array}
$$

$$
\begin{array}{c} P (\text {High} \mid 3 0 - 3 9, \text {Female}, \text {CA}) = (1 / P) (6 / 1 6) (1 / 6) (1 / 6) (1 / 6) \\ = (1 / 5 7 6) / P. \end{array}
$$

The term $P = P ( 3 0 - 3 9$  Female CA cancels out when normalizing the posteriors:

$$
\begin{array}{l} P (\text { Low } \mid 3 0 - 3 9, \text { Female }, \text { CA }) \\ = \frac {(3 / 1 2 8) P}{(3 / 1 2 8) P + (5 / 6 4) P + (1 / 5 7 6) P} = 0. 2 2 6 9. \end{array}
$$

Similarly, we obtain

$$
\begin{array}{c} P (\text {Med} \mid 3 0 - 3 9, \text {Female}, \text {CA}) = 0. 7 5 6 3, \quad \text {and} \\ P (\text {High} \mid 3 0 - 3 9, \text {Female}, \text {CA}) = 0. 0 1 6 8. \end{array}
$$

## Appendix C. Implementation of Swapping Algorithms in Reiss (1984)

The swapping algorithm for preserving the 2-order statistics is implemented based on the description by Reiss (1984, pp. 23–24) and the example in Appendix A of that paper. Our implementation is simpler because only the confidential attribute is perturbed in our problem. The algorithm to preserve the 3-order statistics, which is not explicitly described in Reiss (1984), was implemented by converting the 3-order problem into an equivalent 2-order one. Dimensions other than the confidential one are considered in pairs as compound attributes $( \mathrm { e . g . , \ ^ { \prime \prime } A g e + G e n d e r ^ { \prime \prime } }$ in our example in §3), and statistics derived for each such compound attribute and the confidential attribute. Thereafter, the procedure is analogous to the 2-order algorithm. In addition, the above algorithms were applied separately to the set of uniquely identifiable records (U) and the set of SNP group records selected for perturbation (W), instead of to the entire data set as initially described in Reiss (1984).

## References

Adam, N. R., J. C. Wortmann. 1989. Security-control methods for statistical databases: A comparative study. ACM Comput. Surveys 21(4) 515–556.

Agrawal, R., R. Srikant. 2000. Privacy-preserving data mining. Proc. 2000 ACM SIGMOD Internat. Conf. Management of Data. ACM Press, New York, 439–450.

Atallah, M., E. Bertino, A. Elmagarmid, M. Ibrahim, V. Verykios. 1999. Disclosure limitation of sensitive rules. Proc. IEEE Knowledge and Data Engineering Exchange Workshop (KEDX’99). IEEE Computer Science Society, Washington, D.C., 45–52.

Blake, C., E. Keogh, C. J. Merz. 1998. UCI repository of machine learning databases. Department of Information and Computer Science, University of California, Irvine, CA. http://www.ics. uci.edu/ mlearn/MLRepository.html.

Brand, R., S. Giessing. 2002. Report on preparation of the data set and improvements on Sullivan’s algorithm. http://neon.vb. cbs.nl/casc/.

Chowdhury, D. S., G. T. Duncan, R. Krishnan, S. F. Roehrig, S. Mukherjee. 1999. Disclosure detection in multivariate categorical databases: Auditing confidentiality protection through two new matrix operators. Management Sci. 45(12) 1710–1723.

Cox, L. H. 1995. Network models for complementary cell suppression. J. Amer. Statist. Assoc. 90(432) 1453–1462.

Culnan, M. 1993. “How did they get my name?”: An exploratory investigation of consumer attitudes toward secondary informa tion use. MIS Quart. 17(3) 341–363.

Dalenius, T., S. P. Reiss. 1982. Data swapping: A technique for disclosure control. J. Statist. Planning Inference 6(1) 73–85.

Denning, D. E., J. Schlörer. 1983. Inference control for statistical databases. Computer 16(7) 69–82.

Dinur, I., K. Nissim. 2003. Revealing information while preserving privacy. Proc. 22nd ACM SIGMOD-SIGACT-SIGART Sympos. Principles Database Systems. ACM Press, New York, 202–210.

Duda, R. O., P. E. Hart, D. G. Stork. 2001. Pattern Classification. John Wiley & Sons, New York.

Duncan, G. T., D. Lambert. 1989. The risk of disclosure for microdata. J. Bus. Econom. Statist. 7(2) 201–217.

Duncan, G. T., S. Mukherjee. 2000. Optimal disclosure limitation strategy in statistical databases: Deterring tracker attacks through additive noise. J. Amer. Statist. Assoc. 95(451) 720–729.

Estivill-Castro, V., L. Brankovic. 1999. Data swapping: Balancing privacy against precision in mining for logic rules. M. Mukesh, A. M. Tjoa, eds. Data Warehousing and Knowledge Discovery (DaWak’99). Springer-Verlag, Berlin, Germany, 389–398.

Evfimievski, A., R. Srikant, R. Agrawal, J. Gehrke. 2002. Privacy preserving mining of association rules. Proc. 8th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining. ACM Press, New York, 217–228.

Fienberg, S. E., J. McIntyre. 2004. Data swapping: Variations on a theme by Dalenius and Reiss. J. Domingo-Ferrer, V. Torra, eds. Privacy in Statistical Databases. Springer-Verlag, Berlin, Germany, 14–29.

Fienberg, S. E., U. E. Makov, R. J. Steele. 1998. Disclosure limitation using perturbation and related methods for categorical data. J. Official Statist. 14(4) 485–502.

Galletta, D. 2004. MIS faculty salary survey results. http://www. pitt.edu/ galletta/salsurv.html.

Garfinkel, R., R. Gopal, P. Goes. 2002. Privacy protection of binary confidential data against deterministic, stochastic, and insider threat. Management Sci. 48(6) 749–764.

Greengard, S. 1996. Privacy: Entitlement or illusion? Personnel J. 75(5) 74–88.

Gouweleeuw, J. M., P. Kooiman, L. C. R. J. Willenborg, P.-P. de Wolf. 1998. Post randomization for statistical disclosure control: Theory and implementation. J. Official Statist. 14(4) 463–478.

Iyengar, V. S. 2002. Transforming data to satisfy privacy constraints. Proc. 8th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining. ACM Press, New York, 279–288.

Kullback, S. 1959. Information Theory and Statistics. John Wiley & Sons, New York.

Lerman, C., J. W. Molyneaux, S. Pangemanan Iswarati. 1991. The determinants of contraceptive method and service point choice. Secondary Analysis of the 1987 National Indonesia Contra-

ceptive Prevalence Survey, Vol. I. Fertility and Family Planning. East-West Population Institute, Jakarta, Indonesia.

Li, X.-B., V. S. Jacob. 2005. Adaptive data reduction for large-scale transaction data. Working paper, School of Management, University of Texas at Dallas, Richardson, TX.

Li, X.-B., S. Sarkar. 2005. A data perturbation approach to privacy protection in data mining. Working paper, School of Management, University of Texas at Dallas, Richardson, TX.

Liew, C. K., U. J. Choi, C. J. Liew. 1985. A data distortion by probability distribution. ACM Trans. Database Systems 10(3) 395–411.

Muralidhar, K., R. Parsa, R. Sarathy. 1999. A general additive data perturbation method for database security. Management Sci. 45(10) 1399–1415.

Quinlan, J. R. 1993. C4.5: Programs for Machine Learning. Morgan Kaufmann, San Mateo, CA.

Reiss, S. P. 1984. Practical data-swapping: The first steps. ACM Trans. Database Systems 9(1) 20–37.

Rotenberg, M. 1992. Protecting privacy. Comm. ACM 35(4) 164.

Sarathy, R., K. Muralidhar. 2002. The security of confidential numerical data in databases. Inform. Systems Res. 13(4) 389–403.

Schlörer, J. 1981. Security of statistical databases: Multidimensional transformation. ACM Trans. Database Systems 6(1) 95–112.

Stanford Student Computer and Network Privacy Project. 2002. A study of student privacy issues at Stanford University. Comm. ACM 45(3) 23–25.

Sullivan, G., W. A. Fuller. 1990. Construction of masking error for categorical variables. Proc. Section Survey Res. Methods, American Statistical Association, Alexandria, VA, 435–439.

Verykios, V. S., A. K. Elmagarmid, E. Bertino, Y. Saygin, E. Dasseni. 2004. Association rule hiding. IEEE Trans. Knowledge Data Engrg. 16(4) 434–447.

Wang, H., M. K. O. Lee, C. Wang. 1998. Consumer privacy concerns about Internet marketing. Comm. ACM 41(3) 63–70.

Witten, I. H., E. Frank. 2000. Data Mining: Practical Machine Learn ing Tools and Techniques with Java Implementations. Morgan Kaufmann, San Francisco, CA.
