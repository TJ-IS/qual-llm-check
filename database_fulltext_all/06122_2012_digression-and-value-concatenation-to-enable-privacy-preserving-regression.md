---
otero_id: 6122
otero_key: "NM2GNZ6M"
title: "Digression and Value Concatenation to Enable Privacy-Preserving Regression"
authors: "Xiao-Bai Li; Sumit Sarkar"
year: "2012"
journal: "MIS Quarterly"
doi: "10.25300/misq/2014/38.3.03"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DIGRESSION AND VALUE CONCATENATION TO ENABLE PRIVACY-PRESERVING REGRESSION<sup>1</sup>

Xiao-Bai Li

Department of Operations and Information Systems, Manning School of Business, University of Massachusetts Lowell, Lowell, MA 01854 U.S.A. {xiaobai\_li@uml.edu}

Sumit Sarkar Naveen Jindal School of Management, University of Texas at Dallas, Richardson, TX 75080 U.S.A. {sumit@utdallas.edu}

Regression techniques can be used not only for legitimate data analysis, but also to infer private information about individuals. In this paper, we demonstrate that regression trees, a popular data-analysis and datamining technique, can be used to effectively reveal individuals’ sensitive data. This problem, which we call a regression attack, has not been addressed in the data privacy literature, and existing privacy-preserving techniques are not appropriate in coping with this problem. We propose a new approach to counter regression attacks. To protect against privacy disclosure, our approach introduces a novel measure, called digression, which assesses the sensitive value disclosure risk in the process of building a regression tree model. Specifically, we develop an algorithm that uses the measure for pruning the tree to limit disclosure of sensitive data. We also propose a dynamic value-concatenation method for anonymizing data, which better preserves data utility than a user-defined generalization scheme commonly used in existing approaches. Our approach can be used for anonymizing both numeric and categorical data. An experimental study is conducted using realworld financial, economic, and healthcare data. The results of the experiments demonstrate that the proposed approach is very effective in protecting data privacy while preserving data quality for research and analysis.

Keywords: Privacy, data analytics, data mining, regression, regression trees, anonymization

## Introduction

Predictive analytics techniques using personal data have been deployed by organizations in a variety of domains, including marketing research, financial analysis, human behavior study, and healthcare research. While these techniques are generally used by organizations to better understand and serve their customers, there are growing concerns about invasions to privacy from the use of these techniques.

In a widely circulated article, Charles Duhigg, a New York Times reporter, wrote how Target Corporation used predictive analytics to conduct targeted marketing (Duhigg 2012). Perhaps the most intriguing story in the article is how Target identified pregnant customers. The analytics team started with the shopping records of Target’s baby gift registry, where customers had voluntarily disclosed their due dates. The team discovered a set of products, such as unscented lotion and soap, and calcium and zinc supplements, that pregnant women bought in large quantities during different periods of their pregnancy. These items enabled Target to calculate a “pregnancy prediction” score and estimate the due date for other customers with similar purchase behaviors, and to send coupons timed to specific stages of the pregnancy. The model worked very well—perhaps too well—in that

Target seemed to know things that even close family members of a targeted woman did not know. In one instance, a father whose teenage daughter was receiving coupons for baby products walked into a Target store and complained, “She’s still in high school, and you’re sending her coupons for baby clothes and cribs? Are you trying to encourage her to get pregnant?” It turns out the man later apologized to the store manager that he was not aware of his daughter’s pregnancy. This story took the media by storm, with more than one million views on the Internet within days (KDnuggets 2012). Reaction from the public was mostly negative. As one privacy expert put it, “This is the exciting possibility of Big Data, but for privacy, it is a recipe for disaster” (Ohm 2012).

In this case, Target was using its in-house data for analysis. When personal data is shared with a third party, privacy concerns become even more serious. However, sharing and selling of personal data are common today. As an example, the Center for Medicare and Medicaid Services, a federal agency, sells individual Medicare and Medicaid claims data to third parties for analysis (http://www.resdac.org/). The Center’s operations follow the guidelines of the Health Insurance Portability and Accountability Act (HIPAA). However, studies have shown that the HIPAA rules may be insufficient in protecting patient privacy (Sweeney 2002). In fact, secondary use of private data has long been a cause for serious concern, and studies have found the majority of the public react negatively to their use (Angst and Agarwal 2009; Culnan 1993).

This research concerns regression, which is one of the most widely used predictive techniques in business environments. Specifically, our research investigates a privacy disclosure problem involving the use of a popular regression technique called regression trees. Introduced by Breiman et al. (1984), regression trees build prediction models based on recursive partitioning of data. In contrast to the classic linear regression model, regression trees are nonparametric in nature and thus very effective in dealing with nonlinear and nonmonotonic relationships in data. They can easily handle both numeric and categorical predictor variables. The regression tree models can be converted into a set of rules that are easy to understand and interpret. These desirable features have led to their wide use in predictive data mining and analysis. An excellent example is the regression tree diagram published by The New York Times during the 2008 democratic primary election (Cox 2008). The regression tree used a set of demographic, geographic, economic, and political variables to predict the number of votes (counties) that Barack Obama and Hillary Clinton would win. The tree diagram not only showed prediction outcomes, but also clearly described the decision rule leading to each outcome.

Regression trees, however, can also be used as a tool to effectively reveal private information about individuals. We call this use of regression trees for mining personal information a regression attack. To understand such situations, we first distinguish the attributes of data on individuals from a privacy perspective. Typically, the attributes can be classified into three categories (LeFevre et al. 2008; Li et al. 2007; Machanavajjhala et al. 2006): (1) explicit identifiers, which can be used to directly identify an individual, including name, social security number, and phone number; (2) sensitive attributes, which contain private information that an individual typically does not want revealed, such as income, medical test results, and sexual orientation; and (3) nonsensitive attributes, such as age, gender, education, and occupation. The values of nonsensitive attributes can often be obtained from public sources. Some nonsensitive attributes can be used to identify individuals by matching data from different sources, resulting in identity disclosure. Such attributes are collectively called a quasi-identifier (QI) in the literature. For example, Sweeney (2002) found that 87 percent of the population in the United States can be uniquely identified with three attributes— gender, date of birth, and five-digit zip code—which are accessible from voter registration records available to the public. In data privacy research and practice, the explicit identifiers are typically removed from the data (a process referred to as de-identification). Data anonymization is applied to QI attributes to further prevent or limit the identity disclosure. With identity information properly protected, the sensitive attributes are typically released with their original values. For instance, this scheme of handling the three types of attributes is adopted by HIPAA. We follow the same scheme in this study.

In analyzing privacy disclosure risk, the literature recognizes two types of disclosure: identity disclosure (or reidentification) and value disclosure (Duncan and Lambert 1989; Lambert 1993). Reidentification occurs when a data intruder is able to match a record in a de-identified dataset to an actual individual. The finding that 87 percent of the U.S. population can be uniquely identified by gender, date of birth, and zip code is an example of reidentification. Value disclosure occurs when an intruder is able to predict the sensitive value(s) of an individual record, with or without knowing the identity of the individual. For example, suppose all new faculty members in a unionized college receive the same starting salary and the college releases the average salary of new faculty. Then the release discloses the salary of each new faculty member, even though the individuals are not identified. Thus, a technique that protects against identity disclosure does not necessarily prevent value disclosure.

The Target example discussed earlier is not an identitydisclosure problem because Target already had the explicit identifiers of the customers (due to their using Target credit cards or purchasing Target items online, etc.); so there was no reidentification issue involved. Instead, the problem is about value disclosure, that is, predicting the status and timing of the pregnancy based on the information independent of the identities. Suppose a retail store does not have an in-house analytics team and hires a third-party consulting firm to perform a similar study. Even if the customer data provided by the store are anonymized, the consulting firm can still build a predictive model for value disclosure. Consequently, the group of customers whose demographic and purchase profiles fit the prediction model well will be subject to high disclosure risk. Once a customer is determined as belonging to this group, the sensitive information of the customer is very likely to be compromised even when it is not possible to identify the record in the group that represents this customer (i.e., reidentification is not feasible).

While regression analysis and regression trees are widely used in data mining and business analytics, the regression attack problem has not been addressed in the data privacy literature. As we elaborate later, existing privacy-preserving data-analysis and data-mining techniques are not appropriate for dealing with this problem; some of them could even make a regression attack easier. To fill this research gap, we propose a regression-tree-based approach that can be used by organizations to protect individuals’ private information against regression attacks while preserving the utility of the released data for legitimate data analysis. We introduce a novel measure, called digression, to assess the valuedisclosure risk in constructing regression trees for data partitioning; specifically, an algorithm is developed that uses the measure for pruning the tree to limit disclosure of sensitive data. The approach can be used with one or more numeric sensitive attributes, and can handle both numeric and categorical QI attributes.

To anonymize QI attribute values, a common practice is to generalize the QI values using a predefined generalization hierarchy (Aggarwal and Yu 2008; Samarati and Sweeney 1998). Using a predefined hierarchy for generalization, while effective in preventing reidentification, is quite inflexible and can lead to undesirable information loss. We propose a dynamic value-concatenation method, which merges categorical values based on the hierarchical structure of the regression tree itself. This method has the potential to significantly improve the utility of the anonymized data. Both the disclosure risk (digression) measure and associated treepruning algorithm, and the value-concatenation method, are new to the literature. The proposed approach, which we call MART (Multivariate Anonymization with Regression Trees), is computationally very efficient and is much faster than traditional k-anonymity algorithms. It is, therefore ,wellsuited for applications with large datasets.

The rest of the paper is organized as follows. In the next section, we provide a small example to illustrate the regression attack problem. We then discuss prior and current research related to the problem. Following that, we develop the regression-tree-based data partitioning technique and the dynamic value-concatenation method. We then describe a set of experiments conducted on real-world data to demonstrate the effectiveness of our approach. The final section elaborates the implications of this research and provides directions for future research.

## An Illustrative Example

A regression attack can be accomplished by building a regression tree using the sensitive attributes as the response variables and the QI attributes as predictors. The regression tree can then be used to systematically reveal or infer individuals’ sensitive information based on the values of the QI attributes. This can be done even after the dataset is anonymized using well-known anonymization techniques.

Consider an example dataset containing information on 14 individuals, as shown in Table 1. There are two numeric QI attributes (Age and Years of Education (YearsEdu)), one categorical QI attribute (Occupation, with four categories), and two numeric sensitive attributes (Income and Asset). Given this dataset, a privacy intruder can build a regression tree based on the methods of Breiman et al. (1984) and De’ath (2002), using the two sensitive attributes as the responses. The resulting tree is shown in Figure 1, where a leaf node (rectangle) represents a partitioned subset (the records included in the subset are listed and the ranges of the Income and Asset values for the node are shown below the node). A split criterion is specified along with the edge representing the split. With this tree, it is easy for the intruder to infer an individual’s sensitive information from Table 1 even though the identity information is not included. For example, if the intruder knew that an individual with less than 15 years of education and age more than 43 years is included in the dataset, then the intruder will find that this record is located in node 4, which includes record numbers 3, 4, and 5. The ranges of the Income and Asset values for the records in this node are very narrow. Moreover, the intruder may further split this node into child nodes to get more specific Income and Asset values if the intruder has more specific information about the age, occupation, or years of education for the target individuals.

<table><tr><td colspan="6">Table 1. Illustrative Example: Original Data</td></tr><tr><td>No.</td><td>Age</td><td>YearsEdu</td><td>Occupation</td><td>Income ($000)</td><td>Asset ($000)</td></tr><tr><td>1</td><td>27</td><td>12</td><td>unskilled</td><td>38</td><td>65</td></tr><tr><td>2</td><td>39</td><td>14</td><td>unskilled</td><td>42</td><td>70</td></tr><tr><td>3</td><td>46</td><td>14</td><td>unskilled</td><td>45</td><td>79</td></tr><tr><td>4</td><td>59</td><td>12</td><td>technical</td><td>50</td><td>84</td></tr><tr><td>5</td><td>64</td><td>13</td><td>unskilled</td><td>51</td><td>88</td></tr><tr><td>6</td><td>33</td><td>16</td><td>technical</td><td>59</td><td>94</td></tr><tr><td>7</td><td>35</td><td>16</td><td>unskilled</td><td>52</td><td>85</td></tr><tr><td>8</td><td>42</td><td>18</td><td>professional</td><td>74</td><td>137</td></tr><tr><td>9</td><td>45</td><td>18</td><td>technical</td><td>66</td><td>116</td></tr><tr><td>10</td><td>30</td><td>18</td><td>managerial</td><td>69</td><td>124</td></tr><tr><td>11</td><td>48</td><td>16</td><td>technical</td><td>68</td><td>129</td></tr><tr><td>12</td><td>62</td><td>16</td><td>unskilled</td><td>60</td><td>110</td></tr><tr><td>13</td><td>56</td><td>17</td><td>managerial</td><td>72</td><td>133</td></tr><tr><td>14</td><td>51</td><td>20</td><td>professional</td><td>77</td><td>143</td></tr></table>

![](/api/attachments/NM2GNZ6M/fulltext/images/637b3ae16e20074bc69b35b7fe46ae36eb0b3945dc0732db78d73e3226f99fca.jpg)  
Figure 1. A Regression Tree Built on Data in Table 1

Regression trees are not the only means for an intruder to snoop for sensitive information. For instance, the intruder can issue an ad hoc query to directly search for any targets if the intruder knows a few attribute values of the targets. However, because regression trees partition the data based on the relationships between the QI and sensitive attributes, regression attacks can compromise the data privacy more systematically and intrusively in several aspects. With regression trees, sensitive values can often be revealed using only a small number of the QI attributes, whereas an ad hoc query often requires more attributes, depending on the sequence in which the attributes are considered. For instance, the regression tree in Figure 1 uses two QI attributes (YearsEdu and Age) to predict the sensitive values of the first two records, but an ad hoc query may involve all three QI attributes if the search starts with the Occupation attribute. Furthermore, a regression attack can simultaneously identify a large number of target individuals. Finally, a regression tree shows which targets’ sensitive values can be determined more easily and which QI attributes are the critical attributes for disclosure. So, even if the intruder did not have enough information for positive disclosure, regression trees can help the intruder identify potential targets, or gather additional data on important QI attributes. For example, the regression tree in Figure 1 indicates that YearsEdu may be the most important attribute for finding the sensitive attribute values. In short, a regression attack can find structural information for privacy disclosure that an ad hoc query cannot; it is a systematic, efficient, and proactive technique for revealing private information.

Some of the existing anonymization approaches are vulnerable to regression attacks. We describe the problem here with a well-known technique called k-anonymity (Samarati and Sweeney 1998). A k-anonymity approach aims at anonymizing the values of the QI attributes such that the values of these attributes for any individual match those of at least k – 1 other individuals in the same dataset. With k-anonymity, a dataset is partitioned into groups with at least k records in each group; the QI attribute values are then anonymized using the same generalized value within a group to make the records in the group indistinguishable. For a numeric attribute, kanonymity replaces the original values in a group with the group range. For a categorical attribute, it generalizes the values based on a user-defined hierarchy. Figure 2 shows a generalization hierarchy for the Occupation attribute in the data in Table 1 (the value of the root node can be any expression that covers all Occupation values; we use the symbol \* following the convention in the k-anonymity literature).

When the data is intended for regression analysis, a regression tree technique appears to be a natural choice for dividing the data into groups for k-anonymity. LeFevre et al. (2008) propose a method called regression Mondrian based on this idea. Table 2 shows the anonymized data using regression Mondrian on the example data. When k = 2, the dataset is partitioned into six groups (separated by both dashed-lines and solid-lines); when k = 4, it is partitioned into three groups (separated by solid-lines only). It can be observed from Table 2 that for many of the 2-anonymized groups, the sensitive Income and Asset values are very close within the groups. As a result, the intruder can still obtain the sensitive information fairly accurately for the individuals in these groups even though the intruder may not be able to positively identify the individuals (which is indicative of value disclosure). For example, if the intruder knew that an individual has less than 15 years of education and is older than 43 years, the intruder can still find the same sensitive information from the anonymized data as from the original data using a regression attack (this is because the attack based on the anonymized data makes the same partition of the data as in Table 2). Similar situations also occur for some of the 4- anonymized groups (e.g., the narrow Income range for the group with records numbered 10, 13, 8, and 14). Further, because a regression tree technique attempts to partition the data such that the values of a response attribute are close to each other within a group (to increase prediction accuracy), the use of regression trees for k-anonymity could actually make a regression attack easier.

As mentioned earlier, a limitation of k-anonymity relates to its use of user-defined generalization hierarchies for categorical attributes. In this example, if the Occupation attribute in a group contains “unskilled” and any other value, the value will have to be replaced by the general symbol \*, based on the predefined hierarchy in Figure 2. For instance, the original Occupation values for records #6 and #7 are “technical” and “unskilled,” respectively. When k = 2, they are grouped together (Node 7 in Figure 1). The generalized value for “technical” and “unskilled” is the symbol \* based on the hierarchy in Figure 2. This causes the utility of the released data to deteriorate significantly.

In general, the tradeoff between data utility and anonymity is associated with all privacy-preserving data-sharing techniques. Our approach addresses this issue directly and, as shown subsequently, leads to a better tradeoff than existing techniques.

## Related Work

Information privacy has been studied extensively from different perspectives in multiple disciplines (Smith et al. 2011). This work focuses on the analysis and design aspects of privacy-preserving technology (Aggarwal and Yu 2008; Garfinkel et al. 2007; Sweeney 2002). Figure 3 provides a conceptual view of the technology in the process of collecting, processing, and utilizing data, with privacy-related activities highlighted. A central idea behind all approaches along this line of technology is to process and alter the data such that, while the identifying and sensitive information for the individuals in the data are well protected, the utility of the data is reasonably preserved in the data released for research and analysis.

![](/api/attachments/NM2GNZ6M/fulltext/images/046be081f8b9f9f85e3d749267d07b4971aceb62a37b4fc57bcaba96a9f8f1e0.jpg)  
Figure 2. Generalization Hierarchy for Occupation Attribute

<table><tr><td colspan="9">Table 2. Illustrative Example: k-Anonymized Data</td></tr><tr><td rowspan="2">No.</td><td colspan="3">k = 2</td><td colspan="3">k = 4</td><td rowspan="2">Income ($000)</td><td rowspan="2">Asset ($000)</td></tr><tr><td>Age</td><td>YearsEdu</td><td>Occupation</td><td>Age</td><td>YearsEdu</td><td>Occupation</td></tr><tr><td>1</td><td>[27-39]</td><td>[12-14]</td><td>unskilled</td><td>[27-64]</td><td>[12-14]</td><td>*</td><td>38</td><td>65</td></tr><tr><td>2</td><td>[27-39]</td><td>[12-14]</td><td>unskilled</td><td>[27-64]</td><td>[12-14]</td><td>*</td><td>42</td><td>70</td></tr><tr><td>3</td><td>[46-64]</td><td>[12-14]</td><td>*</td><td>[27-64]</td><td>[12-14]</td><td>*</td><td>45</td><td>79</td></tr><tr><td>4</td><td>[46-64]</td><td>[12-14]</td><td>*</td><td>[27-64]</td><td>[12-14]</td><td>*</td><td>50</td><td>84</td></tr><tr><td>5</td><td>[46-64]</td><td>[12-14]</td><td>*</td><td>[27-64]</td><td>[12-14]</td><td>*</td><td>51</td><td>88</td></tr><tr><td>6</td><td>[33-35]</td><td>16</td><td>*</td><td>[33-62]</td><td>[16-18]</td><td>*</td><td>59</td><td>94</td></tr><tr><td>7</td><td>[33-35]</td><td>16</td><td>*</td><td>[33-62]</td><td>[16-18]</td><td>*</td><td>52</td><td>85</td></tr><tr><td>9</td><td>[45-62]</td><td>[16-18]</td><td>*</td><td>[33-62]</td><td>[16-18]</td><td>*</td><td>66</td><td>116</td></tr><tr><td>11</td><td>[45-62]</td><td>[16-18]</td><td>*</td><td>[33-62]</td><td>[16-18]</td><td>*</td><td>68</td><td>129</td></tr><tr><td>12</td><td>[45-62]</td><td>[16-18]</td><td>*</td><td>[33-62]</td><td>[16-18]</td><td>*</td><td>60</td><td>110</td></tr><tr><td>10</td><td>[30-56]</td><td>[17-18]</td><td>managerial</td><td>[30-56]</td><td>[17-20]</td><td>skilled</td><td>69</td><td>124</td></tr><tr><td>13</td><td>[30-56]</td><td>[17-18]</td><td>managerial</td><td>[30-56]</td><td>[17-20]</td><td>skilled</td><td>72</td><td>133</td></tr><tr><td>8</td><td>[42-51]</td><td>[18-20]</td><td>professional</td><td>[30-56]</td><td>[17-20]</td><td>skilled</td><td>74</td><td>137</td></tr><tr><td>14</td><td>[42-51]</td><td>[18-20]</td><td>professional</td><td>[30-56]</td><td>[17-20]</td><td>skilled</td><td>77</td><td>143</td></tr></table>

A significant development in the literature on data privacy is the k-anonymity framework, proposed by Samarati and Sweeney (1998). As described earlier, the k-anonymity approach uses generalization and suppression methods to alter the values of QI attributes such that the values of these attributes for any individual matches those of at least k – 1 other individuals. In this way, the reidentification risk for an individual is reduced. K-anonymity is a general-purpose technique for privacy-preserving data publishing. Its original framework is not designed to preserve the relationships between the sensitive attributes and the QI attributes. From a data utility perspective, therefore, it may not be effective when the anonymized data is used for predictive data mining and analysis.

Privacy issues have been studied extensively in the predictive data mining and data analysis area (e.g., Aggarwal and Yu 2008; Agrawal and Srikant 2000). A number of studies develop privacy-preserving data-mining approaches under the k-anonymity framework. For instance, a top-down refinement method for classification problems is proposed in Fung et al. (2007). A set of k-anonymity-based algorithms for various data-mining tasks, developed by Friedman et al. (2008), covers classification, clustering, and association rule mining (but not regression).

Besides k-anonymity, Li and Sarkar (2009) investigate the problem of using classification trees for privacy disclosure and propose a method to protect against such a “classification attack.” The sensitive data considered in that study is categorical and the related approach is applicable to classification analysis only. This study, however, considers sensitive numeric data and the approach we propose is intended for regression application. In another paper, Li and Sarkar (2011) propose a multivariate partitioning method for anonymizing data, which can be used for regression analysis. That work focuses on protecting privacy against record linkage, an identity-disclosure problem. It does not consider the valuedisclosure risk under regression attacks. Furthermore, the method proposed in Li and Sarkar (2011) assumes that all data attributes are of numeric type. Our proposed approach, however, allows nonsensitive attributes to be of type numeric, categorical, or both. As such, it is conceptually more general, and more widely applicable for real-world scenarios.

![](/api/attachments/NM2GNZ6M/fulltext/images/8bcc27ed4b7647c879d93f1665dbbcd229dfb1d78280f7354de759b191b00ef9.jpg)  
Figure 3. A Conceptual View of Privacy-Preserving Technology

For regression applications, LeFevre et al. (2008) and Fu et al. (2010) propose k-anonymity based approaches using regression trees (along with approaches using classification trees for classification applications). The method proposed by LeFevre et al. first builds a regression tree with the minimum leaf size k, and then applies generalization and suppression schemes to satisfy the k-anonymity requirement. The objective of the study by Fu et al. is to preserve the regression tree model while anonymizing data. Their study focuses on the conditions that result in the same tree structure when the original or anonymized data are used, and the computational procedure to satisfy these conditions. Neither of these two studies, however, has considered sensitive value disclosure that is vulnerable to a regression attack.

The k-anonymity approach focuses on reidentification risk only and does not consider value-disclosure risk. It generalizes different but similar QI attribute values into the same value within a group. The new values produced by the generalization operation are still correct with respect to the generalized categories. The sensitive attribute values (which can be numeric or categorical) remain unchanged in kanonymity. However, these values become more similar within a group. As a result, individuals in a group, who have the same generalized QI values, are subject to high risk of value disclosure.

To address this issue, a privacy principle called l-diversity has been proposed (Machanavajjhala et al. 2006). The l-diversity principle requires that a sensitive attribute should include at least l well-represented values in the k-anonymized data. For example, a typical instantiation of l-diversity requires that, for each group, at most 1/l of the records have the most frequent sensitive value. The notion of l-diversity, however, does not consider the overall distribution of the sensitive attribute. So, when the overall distribution is unbalanced, the l-diversity requirement may be difficult to satisfy. Furthermore, since the overall distribution is usually public information, the sensitive value disclosure risk can be high when the distribution of the l-diversified data deviates significantly from the overall distribution. To overcome these problems, another privacy principle called t-closeness has been proposed (Li et al. 2007). This principle requires that, for each group, the distance between the distributions of the sensitive attribute in the group and the overall distribution cannot be larger than a threshold value t.

The l-diversity and t-closeness approaches, however, focus on situations where sensitive attributes are categorical. The ldiversity measure is not appropriate for evaluating the disclosure risk of numeric values. For example, every record in the example dataset in Table 1 has a distinct Income or Asset value, so the anonymized data in Table 2 would satisfy any l-diversity requirement. However, it is clear that the sensitive value disclosure risks for most records are high even though the l-diversity requirement is satisfied. The tcloseness measure, although also designed mainly for categorical attributes, can deal with a single numeric attribute. However, it is not appropriate for multiple correlated numeric attributes because the measure is defined for each attribute independently. Furthermore, the t-closeness measure concerns value-disclosure risk only; it does not explicitly consider the prediction error issue. As a result, the anonymized data might not be suitable for regression analysis. In short, because regression attacks involve multiple numeric sensitive attributes and are tied to prediction tasks, the l-diversity and t-closeness approaches are not appropriate to counter regression attacks.

There has been considerable research in the area of statistical databases (SDB) on inference disclosure control (Adam and Wortmann 1989; Denning and Schlörer 1983). Inference disclosure is similar to regression attacks in that they both attempt to reveal sensitive values without requiring identity disclosure. However, an SDB is designed to provide summary statistics, not individual records, to the user. An SDB user cannot retrieve a complete dataset and is typically limited to a few types of queries to obtain aggregate statistics. Therefore, inference control in SDB focuses on query restriction and output perturbation to prevent or limit inference disclosure by queries. This study considers situations where a dataset containing individual records is released to a third party for regression and other predictive analyses. Clearly, inference control methods such as query restriction and output restriction are not applicable to our problem.

Several studies in the area of privacy-preserving association rule mining refer to the use of association rules to infer sensitive information as an “inference” or “inference attack” problem (Atzori et al. 2008; Menon and Sarkar 2007; Oliveira and Zaiane 2006; Verykios et al. 2004). In a broad sense, such an inference attack resembles a regression attack because they both attempt to find sensitive relationships across attributevalues without requiring identity disclosure and in both cases the disclosure of sensitive information is not necessarily deterministic. However, those studies typically assume that some association rules discovered from the data are confidential to the organization that owns the data and need to be protected when the data is shared. The problem thus is about confidentiality of organizational knowledge rather than indi vidual privacy. Further, association rule mining requires all attributes to be categorical; thus, techniques developed to deal with such inference problems are not applicable to regression problems, which concern predictions of numeric values.

Similar problems have also been discussed in some privacy studies on social network analysis and graph mining (Cormode et al. 2010; Heatherly et al. 2013; Zheleva and Getoor 2009). The problems studied in these works examine inferences that can be made without identity disclosure (e.g., the attributes of individuals or the existence of links across entities). As is the case for association rule mining, all confidential attributes/values considered are categorical; none of these studies involves prediction of numeric attributes with regression, and nor do they consider regression attacks.

In summary, the data privacy literature has not addressed the regression attack problem. Given the widespread use of regression techniques, it is important to develop an approach to counter such an attack.

## MART: Multivariate Anonymization with Regression Trees

The notion of regression trees was introduced by Breiman et al. (1984). Similar to classification trees (also known as decision trees), regression trees adopt a divide-and-conquer strategy to build prediction models. We call a regression tree with a single response (dependent) variable a univariate regression tree and one with multiple response variables a multivariate regression tree. Given the problem upon which this study focuses, it is natural to set the sensitive attributes as response variables and use the QI and other nonsensitive attributes as regression predictors.

## ∆-Digression: A Value-Disclosure Risk Measure

A commonly used splitting criterion for growing regression trees is the sum of squared errors (SSE). Consider the single response attribute case. Let n be the number of records in node t. Let y (t) $( i = 1 , . . . , n _ { t } )$ be the value of the response attribute in the $i ^ { \mathrm { { t h } } }$ record in node $t ,$ and be the mean ofy( )t the response attribute values in node t. The univariate SSE at node t is defined as

$$
e (t) = \sum_ {i = 1} ^ {n _ {t}} \left[ y _ {i} (t) - \bar {y} (t) \right] ^ {2}\tag{1}
$$

When a node is split, the combined SSE for the child nodes is always smaller than the SSE for the parent node. Suppose node t is split into m child nodes, $t _ { 1 } , . . . , t _ { m } .$ The reduction in SSE, which is $e ( t ) - [ e ( t _ { 1 } ) + \ldots + e ( t _ { m } ) ]$ , serves as a criterion to select the splitting attribute and splitting value. The algorithm searches over all possible trial-splits for each nonresponse attribute, and the trial-split that maximizes the reduction in SSE is selected to split the data. The process continues until a stopping criterion (e.g., the minimum leaf size) is met. This produces a complete regression tree.

There are limited studies of multivariate regression trees in the literature. The splitting criteria proposed in these studies are some multivariate versions of the SSE. We use a measure, based on De’ath (2002) and LeFevre et al. (2008), that directly extends the univariate SSE to the multivariate case. For a problem with r response attributes, let $\mathbf { y } _ { i } ( t ) = [ y _ { i 1 } ( t ) , . . . ,$ $y _ { i r } ( t ) ] ^ { \prime }$ be the values of the response attributes in the $i ^ { \mathrm { { t h } } }$ record in node t, and be the mean vector of the response attri-y( )t butes in node t. All response values are normalized to the range [0, 1] to remove the impact of the varying scales in different response attributes. The multivariate SSE at node t is defined as

$$
e (t) = \sum_ {i = 1} ^ {n _ {t}} [ \mathbf {y} _ {i} (t) - \overline {{{\mathbf {y}}}} (t) ] ^ {\prime} [ \mathbf {y} _ {i} (t) - \overline {{{\mathbf {y}}}} (t) ]\tag{2}
$$

With this measure, a multivariate regression tree can be built in a manner similar to a univariate regression tree. Multivariate regression trees attempt to minimize prediction errors for the multiple responses. This explains why each subset partitioned by the multivariate regression tree in Figure 1 contains data points that are close to each other in the Income and Asset values.

An important stage in constructing a regression tree is pruning. For a traditional regression tree, the purpose of pruning is to avoid the over-fitting problem. Therefore, the usual pruning method in regression trees aims at minimizing the prediction error. We consider, in our problem, both prediction error and disclosure risk while selecting nodes for pruning. Clearly, the sensitive value disclosure risk of a record at a node is high when the variation in the sensitive attribute values of the records at the node is low. Based on the t-closeness principle (Li et al. 2007), the risk is low when the conditional distributions (conditioned on the nonsensitive attributes) of the sensitive attributes at the node are close to the overall distributions of the sensitive attributes. The tcloseness principle assumes that the overall distributions are public information. In other words, when anonymized data is released, it is expected that the overall parameters, such as the means and covariances of the response attributes for the entire dataset, are the same as or close to the original parameter values. Indeed, in many cases, such original parameters are released with the data.

To measure the disclosure risk in terms of the closeness between a conditional distribution and the overall distribution, we propose a measure, based on the scatter matrix of the response attributes. The scatter matrix, which is the covariance matrix multiplied by the sample size, includes sum of squared errors (or variance) and cross-product (or covariance) components. It is an important measure of variation in each attribute and of relationships between different attributes (we choose to use scatter matrix instead of the covariance matrix merely for convenience, because regression trees use SSE instead of variance for measuring errors and the risk-utility tradeoff measure we propose involves comparing the risk measure with SSE). A significant difference between the scatter matrix on the data at a node and the overall scatter matrix can reveal useful information about the data at the node. The measure below evaluates this “digression” of the scatter structure from the overall scatter matrix.

Definition 1. Let S be the scatter matrix of the response attributes on the entire dataset and $S _ { j k }$ be the $( j , k )$ element of S. Let S(t) be the scatter matrix calculated on the subset data at node t and $s _ { j k } ( t )$ be its (j, k) element. Let D(t) be a scatter difference matrix with its $( j , k )$ element being $d _ { j k } ( t ) = S _ { j k } - s _ { j k } ( t )$ The node digression in scatter, denoted as $\Delta ( t )$ , is defined as the determinant of $\mathbf { D } ( t ) ;$ that is,

$$
\Delta (t) = | \mathbf {D} (t) |\tag{3}
$$

The determinant of a scatter matrix is a single number that captures the characteristics of both variance and covariance information in a scatter matrix (Johnson and Wichern 2002, p. 125). The node digression measures the amount of deviation between the variance–covariance structure on the subset at the node and that on the entire dataset (when there is only one attribute, the node digression simply measures the variance aspect of the deviation). A small digression indicates a small deviation from the overall distribution, which implies a low disclosure risk and thus is desirable. If there are no perfect correlations between response attributes (which is almost always the case in real-world data), then the node digression has the following property:

Lemma 1. The node digression is always a positive number, that $i s ,$

$$
\Delta (t) = | \mathbf {D} (t) | > 0, \forall t\tag{4}
$$

The proofs of this lemma and all other mathematical properties are provided in the Appendix. Since the node digression is meant to measure the deviation of the covariance matrix on the subset at the node from that on the entire dataset, it is not meaningful for the measure to be negative (in a sense similar to the notion of variance or standard deviation). Lemma 1 justifies the node digression measure from this aspect. The result also enables us to define a digression measure for a group of nodes, and compare it with data quality measures.

When a node is split, the response values in its child nodes typically become closer to each other. Therefore, the parent node digression should be smaller than the digression of a child node. To formally describe this property, we first define some terms.

Definition 2. A branch $B _ { t }$ is a subsection of a tree that starts at an internal node, t, and includes all of its leaf or non-leaf descendant nodes.

In Figure 1, branch $B _ { 5 }$ consists of nodes 5 (the root of $B _ { 5 } )$ , 6, 7, 8, 9, 10, and 11.

Definition 3. Let $B _ { t }$ be a branch having m leaves $( \ell = 1 , . . . ,$ m). The branch digression of $B _ { t }$ is defined as the sum of its leaf node digressions; that is,

$$
\Delta (B _ {t}) = \sum_ {\ell = 1} ^ {m} \Delta (\ell)\tag{5}
$$

We will use the term Δ-digression to generally refer to both the node digression and branch digression. The branch digression has the following property with respect to the node digression.

Lemma 2. The node digression for a leaf  is always greater than that for its parent node t. Hence, the branch digression for B is always greater than the node digression for t; that is,

$$
\Delta (\ell) > \Delta (t), \forall \ell , t \Rightarrow \Delta (B _ {t}) > \Delta (t), \forall t\tag{6}
$$

Lemma 2 states that a split of a node always increases digression. In other words, Δ-digression increases monotonically in the depth of the node (with respect to its ancestor nodes). So, pruning a branch into a leaf always reduces digression.

Next, we define the error for a node t and a branch $B _ { t } .$ In fact, the node error $e ( t )$ is simply the SSE of node t as defined in Equations (1) and (2).

Definition 4. The branch error $e ( B _ { t } )$ is defined as the sum of its leaf node errors:

$$
e (B _ {t}) = \sum_ {\ell = 1} ^ {m} e (\ell)\tag{7}
$$

It is well known that a split always reduces errors; that is, $e ( B _ { t } ) < e ( t )$ (Breiman et al. 1984). To assess the tradeoff between disclosure risk and regression error due to a split, we propose the following measure:

Definition 5. The error-digression measure for an internal node t is defined as

$$
q _ {t} = \frac {e (t) - e (B _ {t})}{\Delta (B _ {t}) - \Delta (t)}\tag{8}
$$

We describe next how this criterion is used in the proposed pruning algorithm.

## Error-Digression Pruning

During the pruning process, we want the increase in error to be as small as possible to preserve prediction accuracy; at the same time, we want the decrease in digression as large as possible (which implies that the scatter matrix at the leaf node after pruning is as close to the overall scatter matrix as possible) to reduce disclosure risk. So, to achieve the best tradeoff between error and digression, the branch having the smallest $q _ { t }$ value should be pruned first.

The proposed pruning algorithm is recursive in nature. At each iteration, it calculates the value of $\setminus q _ { t }$ for each branch in the current tree. The branch that has the smallest value of $\dot { } q _ { t }$ is pruned. The process continues until some prespecified stopping criterion is satisfied. An obvious choice of a stopping criterion is the minimum number of records in a leaf. As mentioned earlier, however, this parameter, like the k parameter in k-anonymity, only measures reidentification risk. To measure the probability of sensitive value disclosure risk, we propose using a measure for testing the equality of two covariance matrices, based on the likelihood ratio test statistic (Morrison 1990, p. 292), as shown below:

$$
L _ {t} = n _ {t} \left(\log \left| \widetilde {\Sigma} \right| - \log \left| \widetilde {\Sigma} _ {t} \right| + \operatorname{trace} \left(\widetilde {\Sigma} _ {t} \widetilde {\Sigma} ^ {- 1}\right) - r\right)\tag{9}
$$

Given: an unpruned regression tree, k (the minimum number of records in a leaf), and α (the significance level for the likelihood ratio test).

1. For each internal node t, calculate the q<sub>t</sub> value based on Equation (8) and the $L _ { t }$ value based on Equation (9).

2. Select the node t\* having the smallest q value. If $n _ { t ^ { \star } } < k$ or the p-value for $L _ { t ^ { \star } }$ is smaller than α, then prune the corresponding branch into a leaf.

3. Repeat Steps 1 and 2 until all nodes satisfy the minimum size and significance level criteria.

## Figure 4. The Error-Digression Pruning (EDP) Algorithm

where $\widetilde { \Sigma }$ and $\widetilde { \Sigma } _ { t }$ are the sample covariance matrices for the entire dataset and the subset at node t, respectively, and r is the number of response attributes. The $L _ { t }$ statistic follows a chi-squared distribution with $r ( r + 1 ) / 2$ degrees of freedom. Therefore, the disclosure risk of the records in node t can be evaluated based on the p-value associated with $L _ { t } .$ We also use an adjusted $L _ { t }$ for small node size (Morrison 1990, p. 292).

The proposed error-digression pruning (EDP) algorithm is provided in Figure 4. This algorithm, like usual decision tree algorithms, runs very fast. The time complexity is of O(N log N) for tree growing and $O ( | T | ^ { 2 } )$ for tree pruning, where N is the number of records in the dataset and |T| is the number of internal nodes in the unpruned tree T. In summary, the MART algorithm has the same time complexity as that of a typical regression tree algorithm, which is much faster than a traditional k-anonymity algorithm (Samarati and Sweeney 1998; Sweeney 2002).

We explain the EDP procedure using the example shown in Figure 1 and Table 1. We provide details of the computations for node 9. The node and branch errors are

$$
e (9) = 0. 0 5 3 7 \text {   and   } e (B _ {9}) = 0. 0 1 5 5
$$

The node and branch digressions are

$$
\Delta (9) = 0. 0 4 9 4 \text {   and   } \Delta (B _ {9}) = 0. 1 0 1 7
$$

The error-digression ratio and the p-value of the likelihood ratio test statistic (denoted $p _ { 9 } )$ are

$$
q _ {9} = 0. 7 2 9 7 \text {   and   } p _ {9} = 0. 0 0 8 9
$$

Note that the response attribute values are normalized when calculating these measures. For the other internal nodes, we have

$$
q _ {2} = 2. 0 3 9 2, q _ {6} = 2. 9 4 9 2, q _ {5} = 1 2. 5 0 7 8
$$

and

$$
p _ {2} = 0. 0 3 6 5, p _ {6} = 0. 1 0 6 5, p _ {5} = 0. 1 3 1 0
$$

Suppose $k = 2$ and $\alpha = 0 . 0 5$ Then, node 9 will be pruned first, followed by node 2. This will result in a pruned tree that includes nodes 1, 2, 5, 6, 7, 8, and 9, with leaf nodes 2, 7, 8, and 9. So, given the minimum node size value k, the results of the EDP procedure are often different from those of kanonymity. For instance, with k-anonymity there are six groups when k = 2, while the EDP procedure partitions the data into four groups (leaves) as described above. This, however, does not imply that the proposed method will always produce groups of larger size than a k-anonymity approach. The user can set a small k parameter along with a reasonable α value.

## Categorical Value Concatenation

After the data are partitioned into subsets, the QI attribute values are altered to protect against reidentification. For numeric QI attributes, traditional k-anonymity approaches replace the original QI values in a subset with the range values of the attributes in the subset (Samarati and Sweeney 1998; Sweeney 2002). LeFevre et al. (2008) also suggest alternative values such as mean and median for replacement. In this study, we focus on anonymizing categorical QI attributes. Numeric QI attribute values can be anonymized using one of the existing replacement methods.

For categorical QI attributes, traditional k-anonymity approaches use generalization and suppression methods for anonymization. Typically, a user-defined generalization hierarchy is required. The use of predefined hierarchies may be ineffective in preserving data utility. For example, with the predefined hierarchy shown in Figure 2, many categorical values in the anonymized data are essentially suppressed (Table 2). To overcome this problem, we propose a dynamic value-concatenation method that merges categorical values based on the hierarchical structure of regression trees.

We adopt the binary split method used in Breiman et al. (1984) for splitting a categorical attribute. Many decision tree algorithms use a multi-way split method for categorical attributes, which routes each category into a branch. This method is not effective for our purpose. For the illustrative example, suppose such a multi-way split is made on the Occupation attribute at a node having all four Occupation values. The node will be divided into four branches, one for each Occupation value. A generalization based on this hierarchy will force the suppression of all values. Binary splits, on the other hand, allow more flexibility for generalization. For example, the node may be divided into two branches, one with the Occupation value “unskilled,” and the other with the rest of the three Occupation values. Consequently, a generalization not involving suppression may be performed for the records in the second branch (even based on the prespecified hierarchy in Figure 2).

For an attribute with c categories, there are $2 ^ { c - 1 } - 1$ possible binary partitions of these categories (e.g., there are seven different ways to partition the four Occupation attribute values in our example into two groups). When c is large, it is computationally prohibitive to find the best partition. However, for regression trees, Breiman et al. show that there is an efficient way to order the categories in a certain sequence so that there are only c – 1 (instead of $2 ^ { c - 1 } - 1 )$ possible partitions. This method is used in our splitting algorithm.

The value-concatenation method is very easy to implement. It simply concatenates all categorical values that appear at a leaf of the pruned tree and then treats the concatenated value as one category. If there is a single category in the leaf, then no concatenation is needed. The results of using the valueconcatenation method for the data in Table 1 are shown in Table 3. It is clear that data quality is better preserved with this method than with the predefined generalization hierarchy (see Figure 2 and Table 2). The semantics of the concatenated values are also clear. For example when k = 4, the occupation for the four records in the last group are “managerial” or “professional.” It is not necessary to provide a generalized term for the category.

It is important to note that the value-concatenation method does not cause higher reidentification risk than the userdefined hierarchy even though it can provide more detailed information in the released data. Based on the k-anonymity principle, the reidentification risk is the same for the anonymized data in Table 3 as for that in Table 2. Given the parameter k (as a constraint), the objective of a k-anonymitybased approach is to minimize information loss caused by generalization and suppression. So, for the same k, an anonymized dataset with more detailed information in the QI attributes (e.g., Table 3) has better data quality than that with less detailed information (e.g., Table 2).

## Experimental Study

An experimental study was conducted on three real-world financial, economic, and healthcare datasets (these applications are well-documented as having some privacy implications). The proposed approach is compared with a current state-of-the-art technique. Performances are evaluated in terms of reidentification and value-disclosure risks under regression attacks, as well as data quality for performing regression analysis using two regression methodologies, linear regression and regression trees.

Because the experimental evaluation is conducted in the context of regression analysis, we select the response attributes such that they are most likely to be the output variables for prediction. Furthermore, the response attributes in each dataset are considered as the sensitive attributes since this is how regression attacks would be conducted. This is appropriate for assessing the tradeoff between anonymizing QI information and preserving data quality for regression analysis. Suppose a nonsensitive attribute is set as a response. If the relationship between a sensitive attribute that is not a response and this nonsensitive response is insignificant and negligible, then it is likely that the sensitive attribute will not appear (or will appear very infrequently) as a splitting attribute for the tree. Consequently, it will be difficult to evaluate the impact of anonymization on the relationships between this sensitive attribute and the other nonsensitive attributes. We describe the data below.

Offer. The Association for Information Systems conducts annual surveys of MIS faculty salary offers (Galletta 2004). We selected the offer data from 1999 to 2002 (attributes are consistent for these four years and somewhat different for the other years). This dataset consists of 509 applicants who received offers during the period. There are 13 attributes, with 3 of them numeric and 10 categorical. The attributes are salary offered, position, course load, number of years teaching, education, public or private, campus type, campus region, school’s highest degree, accreditation, respondent accepted offer or not, respondent revealed identity or not, and the year of survey. Salary offered and course load were considered as the response (and sensitive) attributes.

<table><tr><td colspan="9">Table 3. An Illustrative Example: Anonymized Data Using Value-Concatenation</td></tr><tr><td rowspan="2">No.</td><td colspan="3">k = 2</td><td colspan="3">k = 4</td><td rowspan="2">Income ($000)</td><td rowspan="2">Asset ($000)</td></tr><tr><td>Age</td><td>YearsEdu</td><td>Occupation</td><td>Age</td><td>YearsEdu</td><td>Occupation</td></tr><tr><td>1</td><td>[27-39]</td><td>[12-14]</td><td>unskilled</td><td>[27-64]</td><td>[12-14]</td><td>unskilled+technical</td><td>38</td><td>65</td></tr><tr><td>2</td><td>[27-39]</td><td>[12-14]</td><td>unskilled</td><td>[27-64]</td><td>[12-14]</td><td>unskilled+technical</td><td>42</td><td>70</td></tr><tr><td>3</td><td>[46-64]</td><td>[12-14]</td><td>unskilled+technical</td><td>[27-64]</td><td>[12-14]</td><td>unskilled+technical</td><td>45</td><td>79</td></tr><tr><td>4</td><td>[46-64]</td><td>[12-14]</td><td>unskilled+technical</td><td>[27-64]</td><td>[12-14]</td><td>unskilled+technical</td><td>50</td><td>84</td></tr><tr><td>5</td><td>[46-64]</td><td>[12-14]</td><td>unskilled+technical</td><td>[27-64]</td><td>[12-14]</td><td>unskilled+technical</td><td>51</td><td>88</td></tr><tr><td>6</td><td>[33-35]</td><td>16</td><td>unskilled+technical</td><td>[33-62]</td><td>[16-18]</td><td>unskilled+technical</td><td>59</td><td>94</td></tr><tr><td>7</td><td>[33-35]</td><td>16</td><td>unskilled+technical</td><td>[33-62]</td><td>[16-18]</td><td>unskilled+technical</td><td>52</td><td>85</td></tr><tr><td>9</td><td>[45-62]</td><td>[16-18]</td><td>unskilled+technical</td><td>[33-62]</td><td>[16-18]</td><td>unskilled+technical</td><td>66</td><td>116</td></tr><tr><td>11</td><td>[45-62]</td><td>[16-18]</td><td>unskilled+technical</td><td>[33-62]</td><td>[16-18]</td><td>unskilled+technical</td><td>68</td><td>129</td></tr><tr><td>12</td><td>[45-62]</td><td>[16-18]</td><td>unskilled+technical</td><td>[33-62]</td><td>[16-18]</td><td>unskilled+technical</td><td>60</td><td>110</td></tr><tr><td>10</td><td>[30-56]</td><td>[17-18]</td><td>managerial</td><td>[30-56]</td><td>[17-20]</td><td>managerial+professional</td><td>69</td><td>124</td></tr><tr><td>13</td><td>[30-56]</td><td>[17-18]</td><td>managerial</td><td>[30-56]</td><td>[17-20]</td><td>managerial+professional</td><td>72</td><td>133</td></tr><tr><td>8</td><td>[42-51]</td><td>[18-20]</td><td>professional</td><td>[30-56]</td><td>[17-20]</td><td>managerial+professional</td><td>74</td><td>137</td></tr><tr><td>14</td><td>[42-51]</td><td>[18-20]</td><td>professional</td><td>[30-56]</td><td>[17-20]</td><td>managerial+professional</td><td>77</td><td>143</td></tr></table>

Alcohol. This dataset was taken from Kenkel and Terza (2001), who study factors affecting individuals’ drinking behaviors. It includes data on 2,467 male individuals, each with 17 attributes (3 numeric and 14 categorical): age, race, education, marital status, region, employment type, income, drinking frequency, having health insurance or not, insurance type, insurance source, having activity limit or not, having diabetes or not, having heart condition or not, having stroke history or not, visiting same doctor or not, and doctor’s advice on drinking. The attribute drinking frequency was the response attribute in the original study (Kenkel and Terza 2001). We have added the attribute income as the second response (and sensitive) attribute.

Credit. This is a credit evaluation dataset (Bache and Lichman 2013). It has 1,000 records of customers, with 20 attributes (7 numeric and 13 categorical), used by a bank to evaluate credit applications. Some attributes are demographic or economic in nature, and include age, gender, marital status, length of employment, occupation type, housing status, housing liability, length of residence, other personal property status, foreign worker or not, and having a phone number or not. Other attributes are banking and credit related, and include checking account status, savings account status, credit history, credit purpose, number of existing credits at this bank, other debtors, credit duration, installment, and credit amount. The attributes credit duration, installment, and credit amount were considered as the response (and sensitive) attributes.

## Experiment Design and Performance Measures

We compare our proposed MART method with the regression Mondrian (RM) method proposed by LeFevre et al. (2008), which is, to our knowledge, the only existing data anonymization method that considers multi-response regression. As discussed earlier, there are two key differences between MART and RM: (1) MART considers sensitive value disclosure while RM does not; and (2) for categorical QI attributes, MART uses dynamic value-concatenation while RM uses generalization that requires a user-defined hierarchy. We defined a generalization hierarchy for each categorical attribute in a dataset, based on the ideas provided by LeFevre et al. For simplicity, we assume all nonsensitive attributes are QI attributes and thus are subject to anonymization. For numeric QI attributes, we replace the original values by the group averages for both MART and RM methods. The values of sensitive attributes are not changed, following the kanonymity protocol.

In the k-anonymity studies, reidentification risk is measured by minimum group size k, which often serves as a control measure to facilitate comparisons on the other risk and utility measures. We followed this common practice and used three typical group size values for RM and MART: k = 10, 20, and 30. The performances of the two techniques are then evaluated on a sensitive value disclosure risk and a data utility measure, which are described next.

To assess the sensitive value disclosure risk, we use a measure called relative squared distance (RSD), based on Liew et al. (1985). The RSD for a sensitive attribute $Y _ { j }$ is defined as

$$
R S D _ {j} = \frac {1}{M} \left[ \sum_ {t = 1} ^ {M} \left(\sum_ {i = 1} ^ {n _ {t}} \left[ y _ {i j} ^ {t} - \bar {y} _ {j} ^ {t} \right] ^ {2} / \sum_ {i = 1} ^ {n _ {t}} \left[ y _ {i j} ^ {t} - \bar {Y} _ {j} \right] ^ {2}\right) \right]\tag{10}
$$

where M is the total number of groups (leaves), $n _ { t }$ is the number of records in group $t , \ y _ { i j } ^ { t }$ is the value of $Y _ { j }$ in the $i ^ { \mathrm { { t h } } }$ record in group $t , \ \bar { y } _ { j } ^ { \ i }$ is the mean of the $Y _ { j }$ values in group t, and $\overline { { Y } } _ { j }$ is the overall mean of the $Y _ { j }$ values (all values are normalized). The rationale for this measure is that once an intruder has used a regression attack and identified a target group $t ,$ the intruder will most likely use the group average y <sup>t</sup> to estimate $y _ { i j } ^ { t }$ . So the numerator evaluates the closeness of the disclosure. The denominator represents the closeness when $\overline { { Y } } _ { j }$ is used, which can be assumed as public information. Clearly, a larger RSD value implies a smaller disclosure risk (i.e., more difficult for the intruder to determine the sensitive values after identifying the group). For multiple attributes, the RSD measure is calculated as the average of the individual RSD<sub>j</sub>.

Data utility is measured by the mean absolute percentage error (MAPE), defined for a response attribute $Y _ { j }$ as

$$
M A P E _ {j} = \frac {1}{H} \sum_ {i = 1} ^ {H} \left| \frac {y _ {i j} - \hat {y} _ {i j}}{y _ {i j}} \right|\tag{11}
$$

where H is the number of records in the test set (we describe how to separate test data from training data next), $y _ { i j }$ is the value of the $j ^ { \mathrm { t h } }$ response attribute for the $i ^ { \mathrm { { t h } } }$ record in the test set, and $\hat { y } _ { i j }$ is the estimate $\mathrm { \Upsilon } \mathrm { f } y _ { i j }$ based on the regression model built on the anonymized training data. For multiple responses, the MAPE value is calculated as the average of the individual MAPE . As MAPE measures the relative distance between the predictions of the model built from the anonymized data and the values in the test data, a smaller MAPE value is desirable.

Two regression methods, linear regression and regression trees, were used in the experiment for testing the performance in data quality. We built regression models using the anonymized data and then evaluated the utility of the regression models based on prediction accuracy. Specifically, we designed a 10-fold cross-validation experimental methodology, which is similar to the experimental scheme used by LeFevre et al., described below.

1. Divide the entire dataset into 10 equal-sized blocks using random sampling. The experiment will run 10 times, each using one of the blocks in turn as a test set and the remaining data as a training set.

2. For each run, reserve a block and call it the original test set; call the remaining data the original training set. Apply an anonymization technique (i.e., MART or RM) to the original training set to obtain an anonymized training set. During this process, a tree structure for partitioning data is created.

3. Build a regression model (i.e., a linear regression equation or a regression tree) using the anonymized training set.

4. Partition the original test set using the tree structure created in Step 2. Anonymize the partitioned test data to obtain an anonymized test set.

5. Test the regression model built in Step 3 using the anonymized test set and compute prediction accuracy or error accordingly.

6. Repeat Steps 2 through 5 for each of the 10 blocks. Report the average results over the 10 cross-validation runs.

## Experimental Results

The results of the experiments are shown in Table 4. As mentioned above, we report the average MAPE results over the 10 cross-validation runs. For comparison, we also report the average MAPE results using the original data. It is observed that, for the same group size, the RSD values with MART are larger than those with RM in all datasets. This indicates that given the same reidentification risk, MART produces anonymized data with lower value-disclosure risk for the sensitive attributes than RM does. This can be explained by the use of the Δ-digression measure in MART for reducing the value-disclosure risk.

With respect to data utility, the MAPE value resulting from MART is smaller than that from RM in each scenario, using either linear regression or regression trees, which indicates that overall MART outperforms RM for regression analysis. One reason for this is that MART uses the dynamic valueconcatenation method to generalize categorical QI attribute values, which is better in preserving data quality than the predefined generalization hierarchies. The differences in the MAPE results between MART and RM are relatively small in some cases but fairly large in others. To examine if the differences are statistically significant, we performed a paired t test (Mitchell 1997) for each scenario, using significance levels of α = 0.05 and $a = 0 . 1$ The results are shown in Table 4. Overall, the differences are statistically significant in about half of the comparisons at $\alpha = 0 . 0 5$ and in more than half at $\alpha = 0 . 1$

<table><tr><td colspan="6">Table 4. Results of Primary Experiments</td></tr><tr><td>Data</td><td>Method</td><td>Group Size</td><td>RSD</td><td>Linear Regression MAPE</td><td>Regression Tree MAPE</td></tr><tr><td rowspan="7">Offer</td><td>Original</td><td></td><td></td><td>0.1520</td><td>0.1528</td></tr><tr><td>RM</td><td rowspan="2">10</td><td>0.5861</td><td>0.1678</td><td>0.1674</td></tr><tr><td>MART</td><td>0.6258</td><td>0.1670</td><td>0.1657</td></tr><tr><td>RM</td><td rowspan="2">20</td><td>0.6493</td><td>0.1700</td><td>0.1703*</td></tr><tr><td>MART</td><td>0.7098</td><td>0.1673</td><td>0.1670*</td></tr><tr><td>RM</td><td rowspan="2">30</td><td>0.6919</td><td>0.1745**</td><td>0.1751**</td></tr><tr><td>MART</td><td>0.7598</td><td>0.1673**</td><td>0.1672**</td></tr><tr><td rowspan="7">Alcohol</td><td>Original</td><td></td><td></td><td>5.7562</td><td>6.3045</td></tr><tr><td>RM</td><td rowspan="2">10</td><td>0.6121</td><td>6.3465</td><td>7.0129**</td></tr><tr><td>MART</td><td>0.7160</td><td>6.2149</td><td>6.4172**</td></tr><tr><td>RM</td><td rowspan="2">20</td><td>0.6705</td><td>6.5732</td><td>7.2324**</td></tr><tr><td>MART</td><td>0.7533</td><td>6.3593</td><td>6.8005**</td></tr><tr><td>RM</td><td rowspan="2">30</td><td>0.6725</td><td>6.9313**</td><td>7.9977**</td></tr><tr><td>MART</td><td>0.8768</td><td>6.5498**</td><td>6.8842**</td></tr><tr><td rowspan="7">Credit</td><td>Original</td><td></td><td></td><td>0.3710</td><td>0.3873</td></tr><tr><td>RM</td><td rowspan="2">10</td><td>0.5209</td><td>0.4664**</td><td>0.4662</td></tr><tr><td>MART</td><td>0.5894</td><td>0.4595**</td><td>0.4657</td></tr><tr><td>RM</td><td rowspan="2">20</td><td>0.6301</td><td>0.4647**</td><td>0.4671</td></tr><tr><td>MART</td><td>0.6664</td><td>0.4604**</td><td>0.4665</td></tr><tr><td>RM</td><td rowspan="2">30</td><td>0.6402</td><td>0.4664**</td><td>0.4719*</td></tr><tr><td>MART</td><td>0.7080</td><td>0.4624**</td><td>0.4683*</td></tr></table>

\*\*The results of the two methods are statistically significantly different at α = 0.05.  
\*The results of the two methods are statistically significantly different at α = 0.1.

Both RM and MART algorithms ran very fast and completed the procedures within one or two seconds. They are much faster than the traditional k-anonymity algorithms (Samarati and Sweeney 1998; Sweeney 2002). The runtimes for the two algorithms were almost the same, which is expected because they use similar regression tree algorithms.

## Experiment on a Large Dataset

We have provided a computational complexity analysis indicating that the proposed MART algorithm is suitable for large data applications. The datasets used in the primary experiment above are small or moderate in size. To test the performance of MART in a large data setting, we conducted an additional experiment using a census dataset (Bache and Lichman 2013), which contains 95,130 individual records with 42 attributes (8 numeric and 34 categorical).

We use a classical k-anonymity algorithm developed by Sweeney (2002) as the baseline algorithm for comparison. We also included the RM algorithm for completeness (RM uses regression trees as well and is as efficient as MART). While the computational times for MART and RM do not depend much on the number of QI attributes, most of the traditional k-anonymity algorithms, including the baseline approach, have exponential time complexity in the number of QI attributes. Therefore, it is practically very difficult to run the baseline with many QI attributes. Consequently, from the 42 attributes, we selected age, gender, race, education, occupation, and marital status in the Census data to be the QI attributes (these are also frequently considered as QI attributes in other k-anonymity studies). The wage attribute was considered as the response (and sensitive) attribute. Because it is very time consuming to run the baseline algorithm, we only tested for group size k = 30. Also, we performed a 2-fold cross validation procedure (instead of 10-fold cross validation). Given the large size of this data, we believe the results would not differ much if a different group size and number of folds were used.

<table><tr><td colspan="5">Table 5. Results of Experiment on Census Data</td></tr><tr><td>Method</td><td>Time (second)</td><td>RSD</td><td>Linear Regression MAPE</td><td>Regression Tree MAPE</td></tr><tr><td>Original</td><td></td><td></td><td>0.8135</td><td>0.8161</td></tr><tr><td>Baseline</td><td>8345.0</td><td>0.8098</td><td>0.8904**</td><td>0.8876**</td></tr><tr><td>RM</td><td>10.1</td><td>0.5492</td><td>0.8286**</td><td>0.8267**</td></tr><tr><td>MART</td><td>10.5</td><td>0.8234</td><td>0.8192**</td><td>0.8236**</td></tr></table>

\*\*The results of the pairwise comparisons across the three methods are all statistically significantly different at α = 0.05.

The results of the experiment on the Census data are shown in Table 5. It is very clear that MART and RM run much faster than the baseline and are well-suited for large data applications. MART is slightly slower than RM because of the extra computation related to the digression values. MART and RM also outperform the baseline in terms of data quality for both linear regression and regression trees. This is because the baseline algorithm is not designed to preserve the relationships between the predictors (QI attributes) and the responses (sensitive attributes) for regression analysis. Furthermore, the RSD value with MART is considerably larger than that with RM, indicating that MART produces anonymized data with lower value-disclosure risk for the sensitive attributes than RM does. The RSD value with MART is also slightly better than that of the baseline. This experiment used only a single response variable (wage). Therefore, the results also demonstrate that the proposed approach is effective for a regression problem with one response variable.

## Discussion

While MART outperforms RM in all of the experiments, the performance of these approaches vary considerably in terms of data utility (MAPE) across the different datasets when compared to those on the original data. For the Offer data, the MAPE results produced by MART and RM are very close to those based on the original data. For the Alcohol data, the results are a little further apart. For the Credit data, however, the error results based on the anonymized data by MART and RM are considerably larger than those on the original data. This suggests that it is relatively hard to preserve data utility for the Credit data when it is anonymized. A likely explanation is that the relationships between the responses (sensitive attributes) and the predictors (QI attributes) are very sensitive to changes in the QI values in the Credit data. There is another factor, however, that impacts the ability to preserve data utility. In the reported experiments, we have assumed that all of the nonsensitive attributes in the data were the QI attributes and thus were subject to anonymization. This assumption is reasonable for the purpose of experimental evaluation because it avoids potential bias due to the selection of the QI attributes, and is used in a consistent manner for the different approaches. In practical situations, it is usually unnecessary to anonymize all nonsensitive attributes. To further investigate this scenario, we randomly selected half the nonsensitive attributes as the QI attributes and then anonymized them using MART. The resulting MAPE values dropped to about 0.42 (from around 0.46 \~ 0.47 when all the nonsensitive attributes are anonymized), which is much closer to the MAPE values on the original data (about 0.37 \~ 0.38). This suggests that the utility of anonymized data depends on the strength of the relationships between the sensitive and nonsensitive attributes and on the number of nonsensitive attributes being anonymized. Therefore, when using MART, the user can begin by anonymizing all nonsensitive attributes. If this causes considerable deterioration in data utility, then the user can restrict the QI attributes to achieve acceptable levels of data utility.

The size of the dataset also impacts the ability to preserve data utility. For example, for the large dataset (Census data) the MAPE results from MART and RM are very close to those based on the original data. Given a k value, a dataset with larger size allows more groups. Subsequently, there will be more variation in the QI attribute values across the groups, and the generalization of the QI values within each group will have a relatively small impact on the characteristics of the entire dataset. As a result, it should be easier to preserve the data utility for larger datasets when they are anonymized.

When there is an outlier (i.e., an extreme value) in a predictor/ QI attribute, traditional regression trees may create a leaf node containing only the outlier. This situation will usually not occur in MART because the final group size will be greater than one. However, if the group size k is considered only at the pruning stage, it is possible that the outlier will be merged with other nodes at a very high level in the tree, potentially resulting in a group size much larger than k. This can increase the prediction error considerably. One way to address this problem is for the user to first inspect whether there exist outliers in the data. If outliers are detected, a larger stopping size, say m $( 1 < m \leq k )$ , should be specified to grow the regression tree. This will force MART to select the splits that ensure at least m records in each child node, avoiding any node that contains only an outlier.

## Conclusions and Implications for Future Research and Practice

Regression techniques have been widely used not only as a tool for business analytics in private and public domains, but also as a research method in management and social science studies, which often involve using personal data. Therefore, the regression attack problem we investigate is vitally important. This kind of an attack has not been examined in prior research, and extant approaches to preserve privacy are not designed to address this issue. To fill this research gap, we have presented a novel approach for protecting against sensitive value disclosure from such an attack. We have also proposed a dynamic value-concatenation method to limit reidentification risk.

We have shown analytically that the proposed Δ-digression measure has some important properties that help to evaluate value-disclosure risk when multiple numeric sensitive attributes are targeted. In addition, the proposed valueconcatenation method better preserves data utility than userdefined generalization schemes used in existing approaches. Our experimental study demonstrates that the proposed approach is very effective in protecting data privacy and preserving data quality. Our approach can be applied to applications that have numeric and/or categorical data types. That enhances the breadth of applicability of our approach, which has been a limitation for several related approaches that attempt to restrict disclosure of private information.

Future research could investigate alternative methods to anonymize the partitioned data. Particularly, the proposed valueconcatenation method can be extended to include frequency information into the concatenated categories. For example in Table 3, when k = 4, the Occupation values for the five records in the first group can be coded as “unskilled4+technical1” (based on the original count in Table 1). When the data is anonymized with this weightedvalue-concatenation method, the frequency distributions of the categorical attributes can be completely preserved (it is easy to code a program that decomposes the concatenated values). This method would work well for data released for simple publishing purposes such as summary statistics reporting. However, it can be difficult to use for more advanced analysis such as regression, because there will be significantly more concatenated categories than the original ones. Therefore, developing a weighted value-concatenation method for predictive data mining and analytics is an interesting challenge deserving further study.

This work has important implications for future research beyond a strict regression setting. It will be useful to develop an integrated framework to deal with “predictive data mining attacks” that considers both classification attacks (Li and Sarkar 2009) and regression attacks. In this framework, reidentification risks can be assessed independent of the type of the sensitive attributes (i.e., numeric or categorical). The assessment for value-disclosure risks will depend on the type of the sensitive attributes: the digression measure proposed in this work can be used for sensitive numeric attributes while the entropy-based divergence measure proposed by Li and Sarkar (2009) can be used for sensitive categorical attributes. The most challenging situation is when the sensitive attributes include correlated numeric and categorical data. This problem clearly warrants more extensive research.

Our work has significant practical implications. Using the approach proposed in this work, organizations can assess the disclosure risks of the data to be released and take actions to reduce the risks. The first step is to identify the sensitive attributes in the data. In general, the sensitive attributes contain private information that an individual typically does not want revealed. Given a dataset, the sensitive attributes are those that cannot be found from public or external sources and they typically constitute the centerpiece of the information in the data (e.g., salary in a salary survey). After identifying the sensitive attributes, the proposed MART algorithm can be applied to the data to identify which nonsensitive attributes are the important QI attributes that can be used to reidentify individuals. MART also provides a measure to assess the value-disclosure risk for the individuals in a group and the value of the measure increases as the group size decreases. Therefore, the risks of both identity disclosure and value disclosure can be controlled by adjusting the group size. As a final step, the proposed value-concatenation method, which provides better data utility than the traditional generalization method, can be applied to anonymize the grouped data for release.

## Acknowledgments

The authors are grateful to the senior editor, associate editor, and the three anonymous reviewers for their insightful comments and suggestions that have improved the paper considerably. Xiao-Bai

Li’s research was supported in part by the National Library of Medicine of the National Institutes of Health under Grant Number R01LM010942. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

## References

Adam, N. R., and Wortmann, J. C. 1989. “Security-Control Methods for Statistical Databases: A Comparative Study,” ACM Computing Surveys (21:4), pp. 515 -556.

Aggarwal, C. C., and Yu, P. S. (Eds.). 2008. Privacy-Preserving Data Mining: Models and Algorithms, New York: Springer.

Agrawal, R., and Srikant, R. 2000. “Privacy-Preserving Data Mining,” in Proceedings of 2000 ACM SIGMOD International Conference on Management of Data, New York: ACM Press, pp. 439-450.

Angst, C. M., and Agarwal, R. 2009. “Adoption of Electronic Health Records in the Presence of Privacy Concerns: The Elaboration Likelihood Model and Individual Persuasion,” MIS Quarterly (33:2), pp. 339-370.

Atzori, M., Bonchi, F., Giannotti, F., and Pedreschi, D. 2008. “Anonymity Preserving Pattern Discovery,” The VLDB Journal (17:4), pp. 703-727.

Bache, K., and Lichman, M. 2013. “UCI Machine Learning Repository,” Center for Machine Learning and Intelligent Systems, School of Information and Computer Science, University of California, Irvine (http://archive.ics.uci.edu/ml).

Breiman, L., Friedman, J. H., Olshen, R. A., and Stone, C. J. 1984. Classification and Regression Trees, Belmont, CA: Wadsworth.

Cormode, G., Srivastava, D., Yu, T., and Zhang, Q. 2010. “Anonymizing Bipartite Graph Data Using Safe Groupings,” The VLDB Journal (19:1), pp.115-139.

Cox, A. 2008. “Decision Tree: The Obama-Clinton Divide,” The New York Times, April 16 (http://www.nytimes.com/imagepages/ 2008/04/16/us/20080416\_OBAMA\_GRAPHIC.html).

Culnan, M. 1993. “‘How Did They Get My Name?’: An Exploratory Investigation of Consumer Attitudes toward Secondary Information Use,” MIS Quarterly (17:3), pp. 341-363.

De’ath, G. 2002. “Multivariate Regression Trees: A New Technique for Modeling Species-Environmental Relationships,” Ecology (83:4), pp. 1105-1117.

Denning, D. E., and Schlörer, J. 1983. “Inference Control for Statistical Databases,” Computer (16:7), pp. 69-82.

Duhigg, C. 2012. “How Companies Learn Your Secrets,” The New York Times Magazine, February 16, p. 10.

Duncan, G. T., and Lambert, D. 1989. “The Risk of Disclosure for Microdata,” Journal of Business and Economic Statistics (7:2), pp. 201-217.

Friedman, A., Schuster, A., and Wolff, R. 2008. “Providing k-Anonymity in Data Mining,” International Journal on Very Large Data Bases (17:4), pp. 789-804.

Fu, Y., Chen, Z., Koru, G., and Gangopadhyay, A. 2010. “A Privacy Protection Technique for Publishing Data Mining Models and Research Data,” ACM Transactions on Management Information Systems (1:1), Article 7, pp. 7:1-7:20.

Fung, B. C. M., Wang, K., and Yu, P. S. 2007. “Anonymizing Classification Data for Privacy Preservation,” IEEE Transactions on Knowledge and Data Engineering (19:5), pp. 711-725.

Galletta, D. 2004. “MIS Faculty Salary Survey Results,” (http://www.pitt.edu/\~galletta/salsurv.html).

Garfinkel, R., Gopal, R., and Thompson, S. 2007. “Releasing Individually Identifiable Microdata with Privacy Protection against Stochastic Threat: An Application to Health Information,” Information Systems Research (18:1), pp. 23-41.

Heatherly, R., Kantarcioglu, M., Thuraisingham, B. 2013. “Preventing Private Information Inference Attacks on Social Networks,” IEEE Transactions on Knowledge and Data Engineering (25:8), pp. 1849-1862.

Johnson, R. A., and Wichern, D. W. 2002. Applied Multivariate Statistical Analysis. Upper Saddle River, NJ: Prentice Hall.

Kenkel, D. S., and Terza, J. V. 2001. “The Effect of Physician Advice on Alcohol Consumption: Count Regression with an Endogenous Treatment Effect,” Journal of Applied Econometrics (16:2), pp. 165-184.

KDnuggets. 2012. “New Poll: Was Target Wrong in Using Analytics to Find Pregnant Women?” (http://www.kdnuggets. com/2012/02/index.html).

Lambert, D. 1993. “Measures of Disclosure Risk and Harm,” Journal of Official Statistics (9:2), pp. 313-331.

LeFevre, K., DeWitt, D. J., and Ramakrishnan, R. 2008. “Workload-Aware Anonymization Techniques for Large-Scale Datasets,” ACM Transactions on Database Systems (33:3), Article 17, pp. 17:1-17:47.

Li, N., Li, T., and Venkatasubramanian, S. 2007. “t-Closeness: Privacy Beyond k-Anonymity and l-Diversity,” in Proceedings of the 23<sup>rd</sup> IEEE International Conference on Data Engineering, IEEE Computer Society, Washington, DC, pp. 106-115.

Li, X.-B., and Sarkar, S. 2009. “Against Classification Attacks: A Decision Tree Pruning Approach to Privacy Protection in Data Mining,” Operations Research (57:6), pp. 1496-1509.

Li, X.-B., and Sarkar, S. 2011. “Protecting Privacy Against Record Linkage Disclosure: A Bounded Swapping Approach for Numeric Data,” Information Systems Research (22:4), pp. 774-789.

Liew, C. K., Choi, U. J., and Liew, C. J. 1985. “A Data Distortion by Probability Distribution,” ACM Transactions on Database Systems (10:3), pp. 395-411.

Machanavajjhala, A., Gehrke, J., Kifer, D., and Venkitasubramaniam, M. 2006. “l-Diversity: Privacy Beyond k-Anonymity,” in Proceedings of 22<sup>nd</sup> IEEE International Conference on Data Engineering, IEEE Computer Society, Washington, DC, pp. 24-35.

Marcus, M., and Minc, H. 1992. A Survey of Matrix Theory and Matrix Inequalities, New York: Dover.

Menon, S., and Sarkar, S. 2007. “Minimizing Information Loss and Preserving Privacy,” Management Science (53:1), pp. 102-116.

Mitchell, T. M. 1997. Machine Learning. New York: McGraw-Hill.

Morrison, D. F., 1990. Multivariate Statistical Methods, New York: McGraw-Hill.

Ohm, P. 2012. “Don’t Build a Database of Ruin,” Harvard Business Review HRB Blog Network, August 23 (http://blogs.hbr.org/ cs/2012/08/dont\_build\_a\_database\_of\_ruin.html).

Oliveira, S. R. M., and Zaiane, O. R. 2006. “A Unified Framework for Protecting Sensitive Association Rules in Business Collaboration,” International Journal of Business Intelligence and Data Mining (1:3), pp. 247-287.

Samarati, P., and Sweeney, L. 1998. “Protecting Privacy When Disclosing Information: k-Anonymity and its Enforcement through Generalization and Suppression,” in Proceedings of the IEEE Symposium on Research in Security and Privacy, IEEE Computer Society, Washington, DC.

Smith, H. J., Dinev, T., and Xu, H. 2011. “Information Privacy Research: An Interdisciplinary Review,” MIS Quarterly (35:4), pp. 989-1015.

Sweeney, L. 2002. “k-Anonymity: A Model for Protecting Privacy,” International Journal on Uncertainty, Fuzziness and Knowledge-Based Systems (10:5), pp. 557-570.

Verykios, V. S., Elmagarmid, A. K., Bertino, E., Saygin, Y., and Dasseni, E. 2004. “Association Rule Hiding,” IEEE Transactions on Knowledge and Data Engineering (16:4), pp. 434-447.

Zheleva, E., and Getoor, L. 2009. “To Join or Not to Join: The Illusion of Privacy in Social Networks with Mixed Public and Private User Profiles,” in Proceedings of the 18<sup>th</sup> International Conference on World Wide Web, New York: ACM Press, pp. 531-540.

## About the Authors

Xiao-Bai Li is a professor in the Department of Operations and Information Systems at the University of Massachusetts Lowell. He received his Ph.D. from the University of South Carolina in 1999. His research focuses on data mining, information privacy, and information economics. He has received funding for his research from National Institutes of Health (NIH) and National Science Foundation (NSF). His work has appeared in Information Systems Research, Management Science, Operations Research, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Automatic Control, Communications of the ACM, Decision Support Systems, INFORMS Journal on Computing, among others.

Sumit Sarkar is the Charles and Nancy Davidson Chair and Professor of Information Systems in the Naveen Jindal School of Management at the University of Texas at Dallas. He received his PhD from the Simon School of Business at the University of Rochester. His research interests are in personalization and recommendation technologies, sponsored search, data privacy, information quality, data integration, and software release strategies. His research has appeared in Management Science, Information Systems Research, ACM Transactions on Database Systems, Operations Research, IEEE Transactions on Knowledge and Data Engineering, and The INFORMS Journal on Computing, among others. He has served as the conference co-chair for the Workshop on Information Technology and Systems in 1999, the program co-chair for the International Conference on Information Systems in 2001, and the conference co-chair for the IEEE International Conference on Services Computing in 2009. He has been a visiting faculty member at the National University of Singapore and the Indian School of Business, and a visiting scientist at IBM Research Laboratories.

## Appendix

## Proofs

Proof of Lemma 1. Let M be the total number of subsets partitioned by the tree, and $n _ { t } \left( t = 1 , . . . , M \right)$ be the number of records in subset t. Consider any two responses $Y _ { j }$ and $Y _ { k } .$ Let $y _ { i j } ^ { t } ( i = 1 , . . . , n _ { t } )$ be the value of $Y _ { j }$ in the $i ^ { \mathrm { { t h } } }$ record in subset $t , \bar { y } _ { j } ^ { t }$ be the mean of the $Y _ { j } \mathrm { , }$ values in subset $t ,$ and $\overline { { Y } } _ { j }$ be the overall mean of the $Y _ { j }$ values. Notation for $Y _ { k }$ is denoted similarly. Consider

$$
y _ {i j} ^ {t} - \bar {Y} _ {j} = \left(\bar {y} _ {j} ^ {t} - \bar {Y} _ {j}\right) + \left(y _ {i j} ^ {t} - \bar {y} _ {j} ^ {t}\right) \text {   and   } y _ {i k} ^ {t} - \bar {Y} _ {k} = \left(\bar {y} _ {k} ^ {t} - \bar {Y} _ {k}\right) + \left(y _ {i k} ^ {t} - \bar {y} _ {k} ^ {t}\right)
$$

Multiplying the left and right hand sides of the above two equations respectively, we have

$$
\left(y _ {i j} ^ {t} - \overline {{Y}} _ {j}\right) \left(y _ {i k} ^ {t} - \overline {{Y}} _ {k}\right) = \left(\bar {y} _ {j} ^ {t} - \overline {{Y}} _ {j}\right) \left(\bar {y} _ {k} ^ {t} - \overline {{Y}} _ {k}\right) + \left(\bar {y} _ {j} ^ {t} - \overline {{Y}} _ {j}\right) \left(y _ {i k} ^ {t} - \bar {y} _ {k} ^ {t}\right) + \left(y _ {i j} ^ {t} - \bar {y} _ {j} ^ {t}\right) \left(\bar {y} _ {i k} ^ {t} - \overline {{Y}} _ {k}\right) + \left(y _ {i j} ^ {t} - \bar {y} _ {j} ^ {t}\right) \left(y _ {i k} ^ {t} - \bar {y} _ {k} ^ {t}\right)\tag{A1}
$$

Summing over all the records (first within a subset and then over all subsets), and noting that the summations for the middle two terms in the right-hand side of (A1) equal zero, we get

$$
\sum_ {t = 1} ^ {M} \sum_ {i = 1} ^ {n _ {t}} \left(y _ {i j} ^ {t} - \overline {{Y}} _ {j}\right) \left(y _ {i k} ^ {t} - \overline {{Y}} _ {k}\right) = \sum_ {t = 1} ^ {M} \sum_ {i = 1} ^ {n _ {t}} \left(\overline {{y}} _ {j} ^ {t} - \overline {{Y}} _ {j}\right) \left(\overline {{y}} _ {k} ^ {t} - \overline {{Y}} _ {k}\right) + \sum_ {t = 1} ^ {M} \sum_ {i = 1} ^ {n _ {t}} \left(y _ {i j} ^ {t} - \overline {{y}} _ {j} ^ {t}\right) \left(y _ {i k} ^ {t} - \overline {{y}} _ {k} ^ {t}\right)\tag{A2}
$$

The term on the left is the scatter $S _ { j k }$ defined in Definition 1. The first term on the right is the between-subset scatter while the second term on the right is the sum of within-subset scatters, which can be written as $\textstyle \sum _ { t = 1 } ^ { M } S _ { j k } ( \ell )$ (following notation in Definition 1). Let $t ^ { \prime }$ be the node under consideration. Then,

$$
d _ {j k} \left(t ^ {\prime}\right) = S _ {j k} - s _ {j k} \left(t ^ {\prime}\right) = \sum_ {t = 1} ^ {M} \sum_ {i = 1} ^ {n _ {t}} \left(\bar {y} _ {j} ^ {t} - \bar {Y} _ {j}\right) \left(\bar {y} _ {k} ^ {t} - \bar {Y} _ {k}\right) + \sum_ {t \neq t ^ {\prime}} s _ {j k} (t)\tag{A3}
$$

If the response values $y _ { i j } ^ { t ^ { \prime } }$ and $y _ { i k } ^ { t ^ { \prime } } { \left( i = 1 , \ldots , n _ { t ^ { \prime } } \right) }$ are re placed by $\overline { { y } } _ { j } ^ { t ^ { \prime } }$ and $\overline { { y } } _ { k } ^ { t ^ { \prime } }$ respectively, then

$$
s _ {j k} \left(t ^ {\prime}\right) = \sum_ {i = 1} ^ {n _ {t ^ {\prime}}} \left(y _ {i j} ^ {t ^ {\prime}} - \bar {y} _ {j} ^ {t ^ {\prime}}\right) \left(y _ {i k} ^ {t ^ {\prime}} - \bar {y} _ {k} ^ {t ^ {\prime}}\right) = 0\tag{A4}
$$

In this case, the sum of within-subset scatters can still be written as $\textstyle \sum _ { t = 1 } ^ { M } s _ { j k } ( t )$ , and $d _ { j k } ( t ^ { \prime } )$ in (A3) can be expressed in a form analogous to (A2). In other words, $\mathbf { D } ( t ^ { \prime } )$ is the scatter matrix when the response values in node tN are replaced by the subset averages. Since the determinant of a scatter matrix is always positive, this completes the proof. G

Proof of Lemma 2. Let $B _ { t }$ be a branch rooted at t with m leaves. Let $n _ { \ell } ( \ell { = } 1 , . . . , m )$ be the number of records in leaf R. Let $y _ { i j } ^ { \ell } \big ( i = 1 , . . . , n _ { \ell } \big )$ be the value of $Y _ { j }$ in the $i ^ { \mathrm { t h } }$ record in leaf $\ell , \ \bar { y } _ { j } ^ { \ell }$ be the mean of the $Y _ { j }$ values in leaf R, and $\bar { y } _ { j }$ be the mean of the $Y _ { j }$ values in $B _ { t } ^ { \prime }$ s root node t. Denote these quantities similarly for another attribute $Y _ { k } .$ . Following the same algebraic manipulation in the proof of Lemma 1, we have

$$
\sum_ {\ell = 1} ^ {m} \sum_ {i = 1} ^ {n _ {\ell}} \left(y _ {i j} ^ {\ell} - \bar {y} _ {j}\right) \left(y _ {i k} ^ {\ell} - \bar {y} _ {k}\right) = \sum_ {\ell = 1} ^ {m} \sum_ {i = 1} ^ {n _ {\ell}} \left(\bar {y} _ {j} ^ {\ell} - \bar {y} _ {j}\right) \left(\bar {y} _ {k} ^ {\ell} - \bar {y} _ {k}\right) + \sum_ {\ell = 1} ^ {m} \sum_ {i = 1} ^ {n _ {\ell}} \left(y _ {i j} ^ {\ell} - \bar {y} _ {j} ^ {\ell}\right) \left(y _ {i k} ^ {\ell} - \bar {y} _ {k} ^ {\ell}\right)\tag{A5}
$$

The term on the left is $s _ { j k } ( t )$ while the second term on the right can be written as $\Sigma _ { \ell = 1 } ^ { m } s _ { j k } ( \ell )$ . Denote the first term on the right (the between-leaf scatter) as $b _ { j k } .$ . Then, (A5) can be written as

$$
s _ {j k} (t) = b _ {j k} + \sum_ {\ell} s _ {j k} (\ell)\tag{A6}
$$

Now, consider any leaf $\cdot \ell ^ { \prime }$ . Equation (A6) can be written as

$$
s _ {j k} (t) = b _ {j k} + \sum_ {\ell \neq \ell^ {\prime}} s _ {j k} (\ell) + s _ {j k} (\ell^ {\prime})\tag{A7}
$$

Rearranging (A7) and adding $S _ { j k }$ to both sides, we have

$$
S _ {j k} - s _ {j k} \left(\ell^ {\prime}\right) = S _ {j k} - s _ {j k} (t) + b _ {j k} + \sum_ {\ell \neq \ell^ {\prime}} s _ {j k} (\ell)
$$

That is

(A8)

$$
d _ {j i} \left(\ell^ {\prime}\right) = d _ {j k} (t) + b _ {j k} + \sum_ {\ell \neq \ell^ {\prime}} s _ {j k} (\ell)\tag{A9}
$$

Let $\mathbf { D } ( { \boldsymbol { \ell } } ^ { \prime } )$ , D(t), and b be the matrices with their $( j , k )$ element being $d _ { j k } ( \ell ^ { \prime } ) , d _ { j k } ( t )$ , and $b _ { j k } + \sum _ { \ell \neq \ell ^ { \prime } } s _ { j k } ( \ell )$ , respectively. Then,

$$
\mathbf {D} \left(\ell^ {\prime}\right) = \mathbf {D} (t) + \mathbf {b}\tag{A10}
$$

It follows from the Minkowski determinant theorem (Marcus and Minc 1992) that

$$
\left| \mathbf {D} \left(\ell^ {\prime}\right) \right| = \left| \mathbf {D} (t) + \mathbf {b} \right| \geq \left| \mathbf {D} (t) \right| + | \mathbf {b} |\tag{A11}
$$

Based on the same argument as in the proof of Lemma 1, b is a form of scatter matrix and thus $| \mathbf { b } | > 0$ . Therefore,

$$
| \mathbf {D} (\ell^ {\prime}) | > | \mathbf {D} (t) |
$$
