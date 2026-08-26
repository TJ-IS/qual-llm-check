---
otero_id: 5524
otero_key: "8H2HGRAN"
title: "Secure and useful data sharing"
authors: "Rathindra Sarathy; Krishnamurty Muralidhar"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.10.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 204 – 220

www.elsevier.com/locate/dsw

# Secure and useful data sharing

Rathindra Sarathy <sup>a,\*</sup>, Krishnamurty Muralidhar <sup>b</sup>

<sup>a</sup> Department of Management Science and Information Systems, College of Business Administration, Oklahoma State University, Stillwater OK 74078-4011, United States

<sup>b</sup> School of Management, Gatton College of Business and Economics, University of Kentucky, Lexington KY 40506-0034, United States

Available online 24 December 2004

## Abstract

Data sharing among organizations, both government and business, has increased with the advent of the Internet. The study is motivated by the need to address increased confidentiality and privacy concerns that arise with the use of the Internet, while realizing the benefits of data sharing. In this study, we develop a research issues framework based on a survey of existing literature. The framework is used to identify OR/MS research opportunities in disclosure prevention, record-linkage, and in th assessment of the impact of data sharing. Addressing these issues could enable organizations to securely share data. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Data sharing; E-commerce; E-government; Privacy; Confidentiality

## 1. Introduction

Data sharing is fast becoming an important feature of today’s organizations. The dramatic increase in the use of communication networks, changes in architectures of enterprise information systems, as well as the increasing availability of data in computerized form, all have contributed to the popularity of data sharing. Perhaps the biggest impact on data sharing can be attributed to the widespread use of the Internet and Internet-related technologies for e-commerce and egovernment. An organization may share data within its organizational units, with affiliates, with outsourcing service providers (such as payroll processing companies and telemarketers), with strategic partners for supply chain efficiencies, and within the electronic marketplace. Government agencies use the Internet for disseminating data, collecting information, conducting transactions with citizens and other businesses, and enabling research for social benefit.

In e-commerce, data can be shared for transactions, operations, and analysis. A fundamental reason for sharing data in e-commerce is to conduct business transactions. Sharing data to complete transactions is inherent in Electronic Data Interchange (EDI), business-to-business marketplaces, as well as consumer purchases over the web. Similarly, e-government involves sharing data for transactions with citizens, other agencies and outside vendors and businesses.

Data can also be shared for operational purposes. Data sharing is a fundamental enabler of coordination among supply chain partners [2,35]. Some of the types of information that are shared among supply chain partners include inventory sales, demand forecasts, order status, and production schedules. The focus of such sharing is the optimization of businesses processes over the entire chain to benefit all the participants in the chain.

A third and important type of data sharing is for analysis, business intelligence, and decision-support. In this context, sharing data increases information available for analysis. For example, banks share data with affiliates and telemarketers [7]. Retailers allow suppliers to access their inventory data for analysis purposes [35]. E-businesses routinely capture data about a website visitor’s browsing habits. When combined with data from call centers, business and sales data in the organizations’ database, and customer demographic data from market research companies, customer profiles can be improved to develop better marketing campaigns [43]. Many industry-wide initiatives are also being undertaken for sharing data on a massive scale [10]. In egovernment, the most common type of sharing to support analysis is data dissemination. Government agencies such as the U.S. Census Bureau disseminate data for purposes of analysis and research. Additionally, many of these agencies engage in recordlinkage, a computer-based process that combines multiple sources of existing data, to exploit relationships between these datasets and obtain greater insights into social phenomena.

The term <sup>b</sup>E-commerce<sup>Q</sup> is defined in many ways but is most often associated with conducting business transactions over the Internet. Similarly, <sup>b</sup>E-Government<sup>Q</sup> is associated with providing services to citizens. In this study, we do not consider data sharing to complete transactions, since it is reasonable to expect that only data necessary to complete transactions has to be shared. Therefore, there are substantially fewer intellectual problems concerning data sharing to complete transactions that require Operations Research/Management Science (OR/MS) approaches. In the remainder of the paper, we use the term <sup>b</sup>data sharing<sup>Q</sup> to refer to sharing for support of operations or analysis. Such sharing uses essentially the same infrastructure as that used to complete transactions, and is also important to the success of e-commerce and e-government.

The objective of our study is to identify potential OR/MS research opportunities to facilitate useful but secure data sharing. The study is motivated by confidentiality and privacy concerns that arise from data sharing in both commercial organizations and government agencies [45]. At present, one of two extreme approaches is prevalent: either data is being shared without concern for (or knowledge of) security issues and benefits, or data is not being shared due to security concerns. OR/MS researchers can play an important role in developing approaches that provide a sensible compromise between these extremes.

There is a substantial body of research relating to data dissemination, disclosure prevention (we will also use the terms <sup>b</sup>data protection<sup>Q</sup> and <sup>b</sup>disclosure control<sup>Q</sup> interchangeably with disclosure prevention), data utility, and inferential security in the statistical literature, especially in the government context. However, the Internet offers expanded modes of data sharing with multiple partners (rather than just oneway data dissemination) and data sharing through querying of databases (rather than just sharing static datasets). Additionally, in the business context, there are more choices on how data can be shared. Enabling secure and useful data sharing that takes into account these aspects requires OR/MS approaches and solutions in combination with statistical approaches. Following [26], we define OR/MS broadly to include both mathematical programming and statistical models.

The remainder of this paper is organized as follows: In the next section, we discuss the impact of the Internet on data sharing in terms of opportunities as well as confidentiality and privacy issues. In Section 3, we develop a research framework for secure and useful data sharing. Based on the framework, we identify OR/MS opportunities in disclosure prevention, record-linkage and in the assessment of the impact of data sharing (Sections 4, 5, and 6, respectively). The final section presents our conclusions.

## 2. The impact of the Internet on data sharing

The Internet has had a significant impact on the ability of organizations to share data by providing a relatively inexpensive networking infrastructure. In addition, rapidly maturing internet-based hardware and software technologies and standards enable diverse organizations to share data easily and efficiently across great distances. Technologies such as XML provide the ability to link and query heterogeneous sources of data across the Internet. From the perspective of data collection, the Internet has increased the number of sources of data. Online surfing habits are valuable to the conduct of ecommerce, especially when combined with off-line sources of data. Internet-based technologies provide better means to consolidate data (through data exchange or data linkage) and an inexpensive way to disseminate data. Additionally, with the increase in ecommerce and e-government, organizations and society are increasingly comfortable in using the Internet to conduct transactions for products and services.

Unfortunately, the Internet has also increased confidentiality and privacy concerns. In data sharing, privacy and confidentiality violations can occur in many ways, such as when data is shared unethically or illegally, through unauthorized access, and through interception of non-secure transmission, among others. The remedies for such situations are usually legislative, legal, technology-based, or standardsbased and are not the focus of this study. Even if these issues are successfully addressed, privacy and confidentiality threats to data sharing can arise through inferential disclosure. Privacy violations occur when, through sharing of data, the identity of an individual is revealed through inference (identity disclosure). Confidentiality violations occur when, through sharing of the data, the value of a confidential attribute belonging to a particular individual is revealed through inference (value disclosure). In both cases, disclosure could be either exact (where the identity of an individual is known with certainty or the exact value is revealed) or it could also be partial (where a particular record is linked to an individual with a certain probability or the value is estimated with a certain level of accuracy). The enhanced ability of organizations to collect data from diverse sources, consolidate, and share or disseminate the data through the Internet has enabled them to create an almost complete profile for an individual. This, in turn, leads to an increased risk of disclosure of sensitive information about that individual.

Thus, the Internet has a dual impact on data sharing by enabling it on one hand and increasing the risk of disclosure on the other. This <sup>b</sup>dual personality<sup>Q</sup> of the Internet has given rise to the recent public debate on data sharing. Not surprisingly, many organizations favor unrestricted data sharing of all data and view restrictions sought by privacy advocates as reducing the usefulness of data for analysis. If this debate is not resolved, it could lead to legislative intervention, which would be unlikely to satisfy either side. OR/MS can play a valuable role in ensuring that data sharing is both useful to organizations and is secure (so that it satisfies privacy advocates).

## 3. A research framework for secure and useful data sharing

In this section, we present a research framework for secure and useful data sharing. As stated earlier, we focus on data sharing for analysis purposes. The framework was developed to satisfy four major objectives:

1. Identify the major data sharing contexts through a survey of data sharing practices in both governmental and commercial organizations.

2. Identify the primary data sharing issues within, and across, contexts.

3. Provide a mechanism to categorize existing research related to data sharing.

4. Provide insights into the problem and identify research opportunities for the application of OR/ MS techniques.

The framework will also benefit the practice of data sharing in both government and commercial organizations. In this section, we explain each component of the framework and explain how the framework satisfies the four objectives. A graphical view of the framework is presented in Fig. 1.

## 3.1. Data sharing contexts

We define four data sharing contexts based on a survey of several sources of data dealing with business and government data sharing practices.

Context

![](/api/attachments/8H2HGRAN/fulltext/images/c5543b833b3a30a5aa955f5d4267260818f5b607d8462ba3586618268f3ea051.jpg)  
Fig. 1. Research framework for secure and useful data sharing.

Two of these arise in the government context and the other two in the context of business (commercial) organizations. Security and usefulness issues that arise in other contexts (such as sharing of data between not-for-profit organizations) are similar to the ones considered in these four contexts. The sources of data consisted of academic journals, journals dealing with government statistics, trade literature dealing with business data sharing practices, newspapers, websites, among others. In the interests of brevity, and to retain the focus of this paper, we refer to only some of these sources in our discussion.

## 3.1.1. Government data dissemination context

Many government agencies disseminate data to interested parties (citizens, researchers, businesses, and others) for purposes of analysis. This data may have been collected as a result of transactions between the government and its citizens or businesses (such as data provided to the Internal Revenue Service) or through a survey conducted by a government agency (such as data collected by the Census Bureau). In some of these cases, disseminating data in appropriate form is mandated. In other cases, government disseminates data because it believes that it is of interest to citizens/businesses [16].

While facilitating the physical dissemination of data, the Internet has had a significant impact on security in this context [5]. Since it is now possible to gather (or obtain) data regarding individuals through the Internet, the risk that a particular record will be identified as belonging to an individual (re-identification risk) has increased considerably. Government agencies are extremely concerned about this possibility and their over-riding concern is to prevent disclosure of confidential information when the data is released [44]. The released data is usually stripped of all identifying information (de-identified). Records that have a high probability of identity disclosure are usually not released, even if this reduces the value of the data for analysis purposes. Similarly, even those numerical attributes that are not confidential are almost always modified prior to release; otherwise, it would lead to identify disclosure. Given these safeguards, the data sharing problem in the government data dissemination context is: <sup>b</sup>Subject to the lowest possible risk of disclosure, what is the best method of disseminating data so that the released data is useful for analysis purposes?<sup>Q</sup> It should be noted that the safeguards above do not completely eliminate the risk of inferential disclosure.

An appropriate data abstraction (a conceptual model of data relevant to the issues at hand) in the government dissemination context is a de-identified multivariate dataset (as shown in Fig. 1). The multivariate dataset has no personally identifiable data, and consists of categorical and numerical variables (attributes). The security concerns are that the identity of one or more individuals could be revealed (privacy violations) through inferences based on the released data (re-identification risk) and/or values of confidential attributes could be inferred (exact or partial disclosure). The usefulness of the disseminated data is measured in terms of how closely the modified disseminated data represents original data. This is referred to as data utility. The security and usefulness of the released data are fundamentally dependent on the relationships among the multiple variables in the released dataset. Thus, viewing the shared data as a de-identified multivariate dataset is an appropriate abstraction in this context.

## 3.1.2. Government record-linkage context

A recent GAO report [23] observed that, <sup>b</sup>Federally sponsored linkage projects conducted for research and statistical purposes have many potential benefits, such as informing policy debates, tracking program outcomes, helping local government or business planning, or contributing knowledge that, in some cases, might benefit millions of people.<sup>Q</sup> The linkage referred to in the above statement is record-linkage, <sup>b</sup>a computer-based process that combines multiple sources of existing data<sup>Q</sup>. Record-linkage between governmental (such as the Immigration and Naturalization Services) and law enforcement agencies has gained greater importance since the terrorist attacks in 2001. As an example, recent GAO reports [22,23] discusses the linking of trainees’ records from Department of Labor training programs with the employment and earnings records from the Social Security Administration to estimate the long-term impact of training programs. The question of interest in the government record-linkage context can be stated as: <sup>b</sup>How can we link records between different government agencies so that analysis of the linked records will benefit society without disclosing confidential information?<sup>Q</sup>

The underlying security and usefulness issues in the record-linkage context can be understood by using a record abstraction. A record is associated with an individual entity and usually consists of one or more key attributes and one or more non-key attributes. The key identifies an entity uniquely and is used as the basis for combining records from one or more sources. If the non-key attributes are made up of only non-confidential attributes then sharing such information presents no security issues. However, as pointed out in the GAO report [23], this is usually not the case for record-linkage between government agencies. If some of the non-key confidential attributes are shared, preserving the confidentiality of the records while retaining the usefulness of the linked records for research and analysis is an important issue that needs to be addressed. Even in the absence of security issues, record-linkage is often a challenge since common identifiers may not be stored in the same manner in all the data sources being combined.

## 3.1.3. Business data provider context

The Internet increases the availability of data regarding individuals. Many companies now collect data regarding the surfing and shopping habits of individuals over the Internet. The collected data represents a rich source of information valuable for marketing research and other analyses. Some of these companies may subsequently re-sell the data. While businesses such as credit agencies provide specific data (such as credit-worthiness) about individuals to other authorized businesses, the data provider (reseller) has substantially more information that can be disseminated to practically anyone who pays the price. Some e-businesses are built on this model.

The objectives of secure and useful data sharing differ depending on the specific service provided by the data provider. In some cases, the requested data relates to specific individuals and may contain confidential information. In such cases, the data provider must first identify (link) the particular record in the database based on the identifiers provided in the request, and then disseminate information regarding this individual without violating confidentiality. Here, the question is, <sup>b</sup>How can data regarding individuals be shared without disclosing confidential information?<sup>Q</sup> The abstraction of the data is a record and the security issue relates to the protection of the confidential information (similar to the government record-linkage context with confidential data).

By contrast, when group-level data is being provided to a client, the data sharing concern is, <sup>b</sup>How can we share data about a group while preserving anonymity and/or confidentiality of individuals belonging to that group?<sup>Q</sup> While this question is similar to that of government data dissemination, the data abstraction is that of a de-identified multivariate subset (for simplicity, we will refer to this just as a <sup>b</sup>subset<sup>Q</sup>, in future), rather than a multivariate dataset. A subset abstraction reflects the requirements of the client, varies depending on the needs of the client, and could be based on any ad hoc criteria. By contrast, data dissemination usually involves only a fixed dataset selected to reflect the characteristics of the entire dataset. Furthermore, a subset may possess economic value (unlike the multivariate dataset in the government context, which is used primarily to serve a social purpose). It can also act as a unit of negotiation, which is central to the data exchange context discussed next.

## 3.1.4. Business data exchange context

Perhaps the most interesting and complex situation involves data exchange among businesses. In this type of data sharing, each organization in the sharing arrangement provides data to others and may, in turn, receive data from other sharing partners. The data that is shared could be either confidential or non-confidential. For example, data could be shared explicitly for the purpose of creating a more comprehensive profile of existing customers. In other cases, the organizations may be interested in analyzing customer behavior patterns at the grouplevel. In the first case, the organization would be interested in receiving data regarding specific individuals (and the data abstraction would be the record) while in the second case, the relationships between variables in a given subset are of interest (and the data abstraction would be a subset). It is also possible that the organizations receiving the data are interested in the general characteristics of all the customers of the providing organization. In this case, the de-identified multivariate dataset will be the appropriate abstraction. Thus, all three types of data abstraction are possible in the business data exchange context.

Fig. 2 illustrates a simple example of the data exchange context, the sharing of customer data between two financial institutions. Savings and investments in CDs represent numerical data from organization 1 that are confidential as far as organization 2 is concerned. Investments in Stocks and Bonds are attributes from organization 2 that are confidential from the perspective of organization 1. The remaining variables are non-confidential and may be categorical (Cat) or numerical (Num).

From this example it can be seen that if the two organizations are focused on the common customers, then they could engage in record-linkage. Linking records will provide a better profile of individual customers and offer the potential to cross-sell services.

<table><tr><td rowspan="3"></td><td colspan="9">Sharing Data Between Organizations (Customer Database)</td></tr><tr><td colspan="3">Attributes Unique to Organization 1</td><td colspan="3">Common Attributes</td><td colspan="3">Attributes Unique to Organization 2</td></tr><tr><td>Savings</td><td>CD</td><td>S1 (Cat)</td><td>S3 (Num)</td><td>Soc Sec #</td><td>S6 (Cat)</td><td>S7 (Num)</td><td>Stocks</td><td>Bonds</td></tr><tr><td rowspan="20">Data from organization 1</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td>xxx</td><td></td><td></td><td></td></tr><tr><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td></td><td></td><td></td></tr><tr><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td></td><td></td><td></td></tr><tr><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td></td><td></td><td></td></tr><tr><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td></td><td></td><td></td></tr><tr><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td></td><td></td><td></td></tr><tr><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td></td><td></td><td></td></tr><tr><td>XXX</td><td>XXXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td></td><td></td><td></td></tr><tr><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td>XXX</td><td></td><td></td><td></td></tr></table>

Fig. 2. Example of data sharing between two organizations

In this example, Social Security numbers can be used as a basis for defining common customers whose data will be shared. Since the data abstraction is that of a record, the data sharing objectives in this situation are similar to the business data provider context. Since the identity of the common customers is known to both organizations, privacy of the individuals in the linked record is not an issue. However, if the confidential attributes are shared, confidentiality is an issue. In this type of scenario, organizations usually either do not share (potentially) useful data or share data without (adequately) protecting confidentiality.

The two organizations may also be interested in sharing the data regarding non-overlapping customers. In this situation, record-linkage may not be possible. Therefore, there is no need to share identifying information. This would be similar to exchanging de-identified datasets, and therefore there exists a potential for privacy violations through inference. It can be seen that the appropriate data abstraction in this case is that of a de-identified subset. The size of this subset and the attributes included in it may be based on security and value trade-offs between the exchanging parties, and may pose an interesting mathematical modeling problem.

Finally, the organizations may share information about each others’ customer population as a whole without identifying the customers. An example of this situation would be insurance companies sharing data with each other to understand the characteristics of claims and to identify fraudulent claims. In this case, the data abstraction would be a de-identified multivariate dataset and it may be appropriate to use tools and techniques that have been developed in the context of data dissemination.

## 3.2. Importance of data abstractions

In the previous section, we identified three types of data abstraction in data sharing: the de-identified multivariate dataset, subset, and individual record. The purpose of the data abstraction is to allow us to identify the elements of the problem and focus on issues independent of the context. For example, the tools and techniques that are necessary when the data abstraction is that of a subset are quite different from the tools and techniques necessary when the data abstraction is an individual record, even if the context is the same. A tool (such as query restriction, discussed in Section 4.2) could be used in multiple contexts (data provider or data exchange) as long as the abstraction in both these cases is the same (subset). Also, by focusing on issues, and tools and techniques developed to address these issues, data abstractions also allow us to organize the existing literature related to data sharing, as discussed below.

## 3.3. Classifying existing research

Existing research related to data sharing can be classified broadly into data dissemination, query restriction, and record matching. The specific research articles relevant to this study are discussed in detail in Sections 4, 5, and 6. Excellent summaries can be found in [1,11,20,24,28,37,46–49].

Data dissemination research can be further classified into research relating to: (a) masking procedures, (b) tabular data suppression, (c) camouflage, and (d) record-linkage. It is also possible to categorize existing research based on its purpose as: research to develop tools and techniques to prevent disclosure (query restrictions, masking procedures, and camouflage procedures), and research to develop tools and techniques to link records (record-linkage and record matching).

The purpose of query restriction, masking, data suppression, and camouflage techniques is the same: to prevent disclosure of confidential information while providing access to data. Other research in this area includes techniques to assess the need for, or the effectiveness of, disclosure prevention mechanisms [14,17,18,41]. We classify all disclosure prevention techniques and related research under the general category of <sup>b</sup>Disclosure Prevention Mechanisms<sup>Q</sup>. We further sub-classify these techniques based on their approach to preventing disclosure as concealment (where disclosure prevention is achieved by concealing or masking the true value), suppression (where disclosure prevention is achieved by controlling the amount of information presented), or camouflage (where disclosure is achieved by providing interval responses that hide the true values).

Similarly, both record-linkage and record matching have the same purpose. The objective of record matching is to merge records from different sources, while the results of the record-linkage are used to assess the re-identification risk (or identity disclosure). In either case, they use similar approaches and attempt to solve the same problem (to <sup>b</sup>match<sup>Q</sup> or <sup>b</sup>link<sup>Q</sup> records from multiple sources). Hence, we classify existing research in these areas into one category called <sup>b</sup>Record-Linkage<sup>Q</sup> and use two subcategories (<sup>b</sup>Re-identification<sup>Q</sup> and <sup>b</sup>Consolidation<sup>Q</sup>) to identify the different purposes for which these techniques can be used.

Existing research has focused largely on mandatory dissemination of data or providing access to data that is already a part of the database (query restriction or record matching). In these cases, there has been no explicit need for assessing the impact of the additional data obtained through data sharing. As we discuss in much greater detail in Section 6 (<sup>b</sup>Assessing the Impact of Shared Data<sup>Q</sup>), it is necessary to develop tools and techniques to evaluate the impact of shared data, when sharing is optional.

Fig. 1 incorporates this classification of the existing research in the third level under the category <sup>b</sup>Tools and Techniques<sup>Q</sup>. The figure also provides linkages (shown by arrows) that indicate the usefulness of a specific tool to a given abstraction (and through the abstraction, to a specific context). Solid arrows show links between tools and abstractions currently addressed in the literature. Dashed arrows show <sup>b</sup>missing<sup>Q</sup> links (links that the current research does not address).

## 3.4. Research models

The contribution to the existing literature has come from different modeling perspectives, namely, OR/MS models (both statistical and mathematical programming models) and computer science/database models. The main contribution has been from using statistical models for data dissemination. The contribution of mathematical programming models has been limited (mainly in suppression and camouflage techniques and, to a smaller extent, in masking). The contributions of the computer science and database models have been primarily in the areas query restrictions and string comparison in data merging. In Fig. 1, we identify the contribution of the different fields to the existing literature (shown by solid arrows from the individual model areas to the specific tools and techniques). Consistent with the specific objective of this study, opportunities for OR/

Tools and Techniques

![](/api/attachments/8H2HGRAN/fulltext/images/56d1c1052c2443efd46afa1afc401726d21d8c9af8d5d249033f90b025b3c9ed.jpg)  
Fig. 3. OR/MS research opportunities in data sharing.

MS researchers are identified by dashed arrows in the research framework. The research opportunities (highlighted in Fig. 3) are discussed in detail in the following sections.

## 4. OR/MS opportunities in disclosure prevention

A good discussion of several of the existing mechanisms for disclosure prevention can be found in [46]. The selection of a specific mechanism for protecting the data would depend on the type of data being shared. For example, concealment techniques (such as perturbation) are better suited for protecting numerical data, while suppression techniques (such as query restrictions) may be better suited for protecting categorical data. It may be necessary to combine different methodologies for preventing disclosure, in a given situation. It may even be necessary to consider different sharing approaches for different types of data. In the following sub-sections, we identify some important problems that can be potentially addressed by OR/MS researchers. We discuss concealment first because the largest body of research can be found in this area.

## 4.1. Concealment mechanisms

Often also referred to as masking, concealment involves modifying (or masking) the original values of the attributes prior to release. Since the individual data points have been modified, users could be provided either access to aggregate data or individual data points (microdata). A variety of different approaches have been proposed including controlled rounding [31], micro-aggregation [29], perturbation [21,37,42], PRAM [46], synthetic data generation [39,40], swapping [36], among others. Most masking techniques are better suited for numerical data although a few techniques for masking categorical data released in tabular form have been proposed [21]. The primary challenge for these techniques is to create a masked set of data that conforms to security and data utility specifications. In general, masking procedures have been developed using a statistical perspective rather than using mathematical programming. The few exceptions include mathematical programming approaches to micro-aggregation [29], controlled rounding [31,46], and approaches for suppression in tabular data [46]. In the next sections, we identify potential avenues for OR/MS research that are specific to the masking problem, and then discuss issues related to adapting these techniques to data sharing.

## 4.1.1. Mathematical programming approaches to data swapping

Data swapping is one of the disclosure prevention techniques that has been developed using a statistical perspective, but that can be approached using mathematical programming. In data swapping, the objective is to exchange the confidential values between records, so that when the data is released, it would not be possible to re-identify the entity to which the records belong. Swapping is usually performed on ordered data sets [36]. First, the data is ordered based on a given attribute. A record with rank i is swapped with a record chosen randomly from a candidate set of records whose ranks are $i \pm ( p ^ { * } N )$ where N is the total number of records and p is a specified swapping <sup>b</sup>level<sup>Q</sup>. The process is repeated until every value of every attribute is swapped [36]. The problem with the current approach is that if $p$ is small (values that are in close proximity are swapped), it results in low levels of security. If p is large (the swapping is performed between records that are not in close proximity), it changes relationships between the attributes [46] and lowering data utility. There is a need to develop new procedures that can provide an adequate level of both security and accuracy.

The swapping problem can be formulated as a mathematical programming problem as follows: <sup>b</sup>Given a set of confidential and non-confidential attributes, how do we swap the data values for the confidential attributes so as to preserve the characteristics of the dataset to be the same before and after perturbation?<sup>Q</sup> The model may involve non-linearity in the objective function, constraints, or both, and a large number of 0–1 integer variables. Solving the problem using a mathematical programming model may allow the masked data to achieve both a very high level of security and also maintain relationships between attributes, which is not possible with existing swapping techniques. Since the problem may involve a large number of integer variables, it may be necessary to use heuristic rather than optimal approaches. However, it is possible that heuristic solutions based on mathematical programming will yield better solutions than those obtained from current statistically based algorithms.

Furthermore, optimal solutions, while possible only for small datasets, may still have useful applications. For small datasets, statistically based approaches result in high levels of sampling error that could make the resulting dataset useless for analytical purposes. Mathematical programming based approaches may limit the sampling error to an acceptable level. Consequently, the optimization approach to swapping may be a viable alternative in the government dissemination context, where the size of the released data set (compared to the size of traditional databases) is relatively small. Also, in the business data exchange context where the partners sharing data are allowed to query others’ databases, query results containing confidential attributes may be small enough to permit optimal solutions to the swapping problem. We believe that this particular avenue of research would be interesting to OR/MS researchers.

## 4.1.2. Mathematical modeling approaches to data perturbation

Similar to data swapping, it may also be possible to approach data perturbation from a mathematical programming perspective. Current statistical approaches to perturbation are capable of maintaining certain specified characteristics, for instance, either product moment or rank order correlation, but rarely both [42]. Second, as discussed in the previous section, they result in reduced data utility for small datasets due to sampling error.

A mathematical programming formulation for the perturbation problem would be as follows: <sup>b</sup>Given a set of confidential attributes and a set of nonconfidential attributes, what should be the values of the perturbed attributes such that the characteristics of the original and perturbed data are the same, while simultaneously minimizing disclosure risk?<sup>Q</sup> Alternatively, security may be specified, and we may try to minimize differences in statistical characteristics of the original and perturbed data. The statistical properties of the database may provide natural upper and lower bounds for the perturbed values. Unlike swapping, perturbation does not require the use of integer 0–1 variables, and both small, as well as relatively large problems, may be solved to optimality. Furthermore, the formulation may be altered to suit particular requirements such as maintaining specific moments of the distribution, or specific multivariate relationships (or both).

## 4.1.3. Adapting masking techniques to data sharing

Existing techniques for masking have been developed in the context of disseminating government data, and not in the context of sharing data. The data abstraction that is assumed in these techniques is that of a single de-identified multivariate dataset or subset, consisting of both confidential and non-confidential attributes. The objective of masking in these cases would be to preserve the characteristics of the disseminated data to be the same before and after masking, while simultaneously preventing risk of both identity and value disclosure.

The general case of business data exchange between two sharing partners discussed earlier presents a greater challenge. As Fig. 2 illustrates, there are two different data sets (and in the general case, multiple datasets) and not just one. The objective of masking techniques in this case would be to reduce the risk of disclosure by masking both datasets, while simultaneously preserving the relationships that may exist between both datasets. Specifically, it raises the question as to how should masking be performed for the overlapping records/attributes and non-overlapping records/attributes. For example, consider the special case where only records common to both organizations are shared. If organization A masks the confidential records independent of organization B’s data, the resulting merged dataset will not maintain the true relationships. In order to mask the common data such that relationships are preserved, both organizations would need prior knowledge regarding relationships between the attributes that are not common. It may even require the involvement of an independent third party who has access to both sets of data, to perform the masking. These issues are unique to the data exchange context and have not been addressed in the existing masking literature.

Sharing of non-overlapping records may also be of interest in some data sharing situations (for example, data regarding individuals who are not currently our customers but who purchase related products). In this case, the data abstraction is that of a multivariate dataset and it may be possible to directly apply existing techniques. Thus, the application of masking techniques to the general data exchange context is an important area of research. Techniques that perform effectively in the data dissemination context may not perform as effectively in the data exchange context. The selection of a specific masking requires that the data abstraction be clearly understood. Finally, it must be stressed that there continue to be opportunities for improved masking techniques, even in the data dissemination context.

## 4.2. OR/MS opportunities in data suppression

Unlike concealment techniques, which provide users access to masked microdata, suppression techniques control the amount of information presented to users. Information is typically presented in the form of aggregate data. Suppressing responses to queries applies to those data sharing contexts where the partners in the sharing are allowed access to a database that contains the confidential data. In practice the primary suppression mechanism is likely to be query restriction. Hence, the development of efficient query restriction mechanisms is very important for data sharing. Queries are typically restricted based on: (a) Set size, where responses resulting in set sizes less than a specified number are denied; (b) Query types, where only certain types of queries are permitted and others are prohibited (for example, queries involving relationships between attributes); and (c) the number of attributes in a query. Adam and Wortmann [1] provide an excellent discussion of a variety of query restriction mechanisms.

## 4.2.1. Assessing information content for inferential disclosure in tabular data

Query restriction approaches are primarily concerned with the question, <sup>b</sup>If a response is provided to this query, would it result in disclosure of a particular value (i.e., exact disclosure)?<sup>Q</sup> Earlier studies have shown that even if strict query restrictions are in place to prevent exact disclosure through individual queries, they do not prevent partial disclosure [1,38]. That is, they may not prevent accurate estimates of individual confidential values. The disclosure risk arises because existing query restriction mechanisms do not consider the information content in the set of records on which the mathematical or statistical operations are performed in responding to the query [18]. Therefore, the query restriction should also be concerned with the following question, <sup>b</sup>If a response is made to this query, what is the best prediction of (one or more) confidential variables that can be achieved using (one or more) non-confidential variables?<sup>Q</sup> This question addresses inferential disclosure directly.

The information content in responding to a query that creates categorical tables has been evaluated in [17,18]. These studies use linear programming and two newly developed matrix operators to assess disclosure risk. The response to that query is suppressed if such an assessment suggests the possibility of disclosure. These studies also provide computational evidence to suggest that such a mechanism could potentially work in an on-line database environment. However, it is not clear whether this procedure can be used effectively for queries that create data tables based on numerical variables, rather than just categorical variables. Future research could focus on evaluating the effectiveness of this procedure, and/or modifying the procedure for effective utilization in the context of data sharing.

## 4.2.2. Assessing information content for relationships

When query restriction is used, disclosure could still occur when responses to queries involving relationships between confidential attributes and non-confidential attributes (both numerical and categorical) are used to predict values of confidential variables [38]. A recent study suggests the use of canonical correlation to assess the potential for inferential, partial disclosure in a static database [41]. Extending the canonical correlation approach, or developing a new method of evaluating disclosure potential in subsets resulting from ad hoc queries, can provide the basis for an alternative to existing query restriction mechanisms. It is important to note that such a method must be performed <sup>b</sup>on the fly<sup>Q</sup> for every query that is issued by users. The new procedure must be fast so that query response time is not adversely affected. The characteristics of this problem, namely, a statistical/optimization approach to evaluating information content, and the need for efficient algorithms to assess the information content, make it a good candidate for OR/MS approaches.

## 4.2.3. Heuristic approaches to query auditing

Query restriction procedures try to eliminate disclosure that could potentially occur through a single query. Query auditing attempts to prevent disclosure that occurs as a result of a user issuing a sequence of queries [9,15]. In query auditing, linear programming techniques can be used to detect exact or interval disclosure arising from list of queries issued by a particular user [6,27]. Existing query auditing procedures only allow for only simple queries (such as SUM, MEAN, MIN, and MAX). Since the problem is NP hard, optimal search procedures cannot be implemented for large databases. Heuristic procedures for query auditing may allow for: application in large databases, evaluation of ad hoc queries when they are issued, and evaluation of more complex queries. There is a trade-off, however, between inferential disclosure risk and efficiency when heuristic auditing procedures are used. Developing new (heuristic) procedure(s) that can be implemented for large-scale databases, while providing an acceptable disclosure risk, is necessary to improve the ability of organizations to share date.

## 4.2.4. Subset identification for query auditing

Existing query auditing approaches are concerned with the question, <sup>b</sup>If a response is provided to this query, then based on responses to queries issued earlier, would it result in disclosure of a particular value?<sup>Q</sup> An interesting alternative is to approach query auditing from the perspective of identifying subsets that could potentially result in disclosure. That is, we modify the question as, <sup>b</sup>What is the smallest subset that results from responding to this query and responses to all other queries issued earlier?<sup>Q</sup> This subset can then be assessed for inferential disclosure. In relative terms, identifying subsets is an easier problem than the original query audit problem. A combined approach based on identifying subsets and evaluating information content represents possibly the best approach for solving the query audit problem.

## 4.3. Camouflage

A third approach to disclosure prevention is confidentiality via camouflage (CVC) [24,28], which can be considered a compromise between suppression and concealment. Query restrictions and query auditing result in denials of response if a query has the potential to compromise confidential information. Camouflage avoids this problem by always providing an interval response that is guaranteed to contain the true confidential value. Simultaneously, it attempts to avoid the bias in some masking methods, where the characteristics of the masked data are different from the original data. The interval response is computed from a collection of camouflage vectors, and is the sharpest interval that satisfies security specifications. CVC is a good candidate for OR/MS techniques, since queries are represented as mathematical operations on data, and the problem is reduced to one of optimizing intervals through mathematical programming and/or solving systems of equations. One advantage of the camouflage approach is that it can be used both for numerical as well as categorical data [24].

There are several issues in using existing CVC approaches for data sharing. First, it is not clear, in either the government or business context, that users would find interval responses useful. Studies to establish its usefulness in these contexts are required. Second, the CVC method relies on user specifications of what constitutes disclosure, for each data point. While this may not be a problem for small data sets, it may present a serious problem for databases consisting of a large number of entities and/or a large number of confidential numerical attributes. Third, it requires multiple values to be stored for each confidential value that may again present a problem for large databases. Fourth, in its current state of development, it is applicable to queries involving only a single confidential attribute and only to a select set of query types. Lastly, its effectiveness in controlling inferential security is unclear. Palley and Simonoff [38] showed that even when users are only allowed access to statistical queries (much as CVC does), users might obtain good estimates of confidential values based on non-confidential values. Therefore, a snooper could completely ignore the responses to confidential attributes provided by CVC and estimate confidential values using non-confidential attributes. Addressing these issues and enhancing the capabilities of CVC presents significant opportunities for OR/MS researchers.

## 5. OR/MS opportunities in record-linkage

As defined in Section 3.3, record-linkage refers to the ability to link records from multiple sources.

Record-Linkage is an important method for sharing individual records, when such sharing is permitted. In situations where sharing of individual records is prohibited, record-linkage is an important means for evaluating re-identification risk. We discuss recordlinkage from both perspectives.

As seen in Section 3, linking data from different sources is important to both the government and business contexts, and is an important form of data sharing. In Fig. 2, one or both parties may wish to create a more comprehensive profile of those records that are in common with the other organization’s records. If both parties use the same key attribute(s) for these records, and share only attributes that are not confidential to the other party, there are no major issues, since the matching and merging of the records can be automated. However, there are many situations where (i) no common candidate keys are present and the records cannot be automatically linked with certainty [11,12] or (ii) common keys exist, but linking data on the basis of these common keys raises privacy issues [23], or (iii) both factors are present; that is, there is uncertainty in the linkage and confidential data has to be shared. We discuss each of these situations in turn.

Winkler [47] observes, <sup>b</sup>Modern record-linkage represents a collection of methods from three different disciplines: computer science, statistics and operations research<sup>Q</sup>. Winkler identifies three needs in record linkage: Efficient string comparison procedures (which have been the subject of research in computer science), estimating matching parameters and error rates (through research in statistics) and a means for forcing 1–1 matching (which requires efficient assignment algorithms and relies on OR/MS).

Fellegi and Suntner’s [19] seminal work on recordlinkage is the basis for most research in this area. In the face of uncertainty of whether 2 records can be matched and linked (either because the two sources of data have no common identifiers, or because the identifiers are different), they provide a Bayesian formula for calculating a matching probability and deciding whether there is a match or not. Dey et al. [13] use a probability measure (different from [19]) as the basis for developing efficient techniques of recordlinkage in a heterogeneous on-line database environment while a cost-minimization formulation for a matching procedure that combines automated and human matching is provided in [10]. This study concludes that given the size of the problem, heuristic procedures are needed although the problem can be formulated as an LP. In the query-based online environment, since the matching has to be completely automated, other issues such as communication, storage, and computational overhead are relevant [12]. They indicate several future areas for research, including the development of models to perform costbenefit tradeoffs and to use non-probabilistic measures of similarity.

Another form of sharing could involve the sharing of confidential attributes for common data between the two parties in Fig. 2. While privacy is not an issue, each party providing the data wishes to maintain the confidentiality of one or more attributes of data that they share. In this situation, in addition to the recordlinkage issue discussed above, data protection for the confidential data has to be considered. Thus, an important area of research is to explore disclosure prevention mechanisms that can result in the same level of matching efficiency. This is relevant since the similarity measures for matching are based on the characteristics of the shared data, which could be confidential, numerical data. The purpose of recordlinkage in this context can be twofold: the party receiving the data wishes to improve the profile of the customer using the non-confidential data, and then perform aggregate analysis or group-level analysis using the confidential data. The disclosure prevention mechanism must maintain the relationships between the confidential and non-confidential attributes, while simultaneously not having an adverse impact on matching efficiency or security. These are open issues for research.

In the context of government record-linkage and business data exchange, the potential for recordlinkage is an important source of risk, and more so with the advent of the Internet. Record-linkage is an attempt to link data belonging to the same entity available in multiple sources. A successful linkage will allow a snooper to not only identify an individual in an unauthorized fashion (privacy violation) but may also allow the snooper to identify or infer confidential values (confidentiality violation). In data exchange and record-linkage arrangements, parties receiving the data may use such data (whether in modified or unmodified form) to identify or estimate values of data that they did not receive from the data provider (due to confidentiality and privacy considerations). Thus the data provider faces security risks from providing such data and needs to be able to appropriately assess the risk posed by engaging in data sharing. This is an important area of research, complicated by the fact that in the data exchange context, the data receiver may not indicate what data is available in their possession, to the data provider. Researchers at the Census Bureau have conducted extensive work in assessing security risk to disseminated data arising from probabilistic record-linkage [47–49]. The assessment of the risk involves both probabilistic modeling of record matches and efficient assignment algorithms. Extending this work to the data exchange context remains an open area of research [30].

## 6. OR/MS opportunities in assessing the impact of shared data

One of the critical needs in analyzing the data sharing problem is to mathematically formalize the impact that the shared data will have on organizational decisions. This is the first step in the ability of the organization to evaluate the benefits of data sharing. Such modeling also helps to identify those situations where data sharing is beneficial. However, as shown in Fig. 1, currently there is no research that attempts to model the impact of data sharing.

One reason for the lack of research could be the relative complexity of the problem. In the general data exchange context, modeling the impact of data sharing requires evaluation of the usefulness (for analysis) of the data that is received. Three levels of usefulness can be identified related to data sharing:

(a) Data utility—When confidential data cannot be shared in an unmodified form, data quality refers to ability to perform the same types of analysis and obtain the same result with the modified data as with the unmodified data.

(b) Richness of data—When data is shared and there is a choice relating to what data is shared, richness refers to the quantity and quality of relationships that the data receiver obtains from the data they receive. It includes the relationships within and between the data that is received as well as the data that is possessed.

(c) Data value—The economic and/or social benefits that arise from the analysis of received data represents the eventual value that is derived from the data. This could include reduced crime in a government setting, for example, or increased market share in the context of a business.

Each measure of usefulness has specific purposes and offers different challenges in their evaluation. The issue of data utility has been researched in the context of data dissemination [46]. Canonical correlation measures developed for assessing disclosure risk for numerical variables [8,41] have potential in assessing richness of data. However, assessing data value is a greater challenge. Interestingly, some work in the context of supply chains may provide a starting point in this regard.

Recently, there has been considerable research in modeling the information sharing process in supply chains [2–4,32–35] and assessing the value of such information sharing [25]. These studies model the sharing of demand information between a supplier and retailer. In the supply chain situation, the data that is being shared is limited (only demand information), the purpose of data sharing is clear (forecasting, inventory control), the data is not confidential, and the data is shared between business partners. Yet, the fact that the business partners have a choice as to whether share the data or not distinguishes it from sharing data to complete transactions. Modeling this situation enables the sharing partners to evaluate the impact of information sharing in a supply chain. Thus, the supply chain based models above can be considered as special (narrow) cases of data sharing for improving operational efficiency, and as first attempts to model the impact of data sharing.

Adapting the supply chain models to assess data value for the general case of data sharing will not be easy. Some of the shared data may be confidential, requiring the consideration of security as part of the modeling process. When protection mechanisms are used, the utility of the protected data may also have to be considered. Finally, data may be shared not just between direct business partners, but potentially even among competitors. This would require further modeling, perhaps based on game theory.

In other words, modeling the data sharing problem may involve higher levels of complexity than existing models of information sharing in a supply chain. However, the approach for modeling remains the same: to identify the data being shared, the purpose of sharing the data, the characteristics of the data, and the source of the data. Existing models of security and data utility could be used in conjunction with the supply chain models to address the more complex general context of business data exchange. We consider this to be one of the most important problems that must be addressed by OR/ MS researchers.

## 7. Conclusions

While there is little doubt that data sharing can be highly beneficial to organizations, it is equally certain that unrestricted data sharing will reduce the privacy and/or confidentiality of individuals. Current debate on data sharing centers largely around the sharing of data on individuals. However, this represents one (record) abstraction of the data. Our research framework shows that other data abstractions, which do not involve sharing personally identifiable data about individuals, can also be very useful.

Existing literature related to data sharing is focused either on one context (data dissemination) or on one issue (suppression and merging). Our research framework allows researchers to view the relevant research not just in terms of contexts or issues, but establishes a link (data abstraction) between the different issues and the contexts. The framework also relates the existing research from different modeling perspectives (mathematical programming, statistical, and database) to the data sharing issues. This allows us to identify new research streams and opportunities for OR/MS researchers. These research streams involve practically all aspects of the data sharing problem including disclosure prevention mechanisms, recordlinkage, and perhaps most importantly, assessing the impact of the shared data on organizational decision making.

Finally, in this study, we have explored the important role that OR/MS has to play in enabling secure and useful data sharing in both the government and business contexts. Such a role should come as no surprise since:

(a) Disclosure prevention mechanisms are essentially data transformation techniques,

(b) Analytical queries are usually mathematical operations performed on data,

(c) Much of the inferential security and analytical utility measures are quantitative in nature,

(d) Trade-offs between security and usefulness can be modeled mathematically, and

(e) The selection and assignment of data to sharing partners can be modeled as decision variables.

OR/MS research into many of these issues is in its infancy. There is a substantial need in practice for such issues to be addressed successfully.

## References

[1] N.R. Adam, J.C. Wortmann, Security-control methods for statistical databases: a comparative study, ACM Computing Surveys 21 (4) (1989) 515– 556.

[2] G. Cachon, M. Fisher, Supply chain inventory management and the value of shared information, Management Science 46 (8) (2000) 1032– 1048.

[3] G. Cachon, M. Lariviere, Contracting to assure supply: how to share demand forecasts in a supply chain, Management Science 47 (5) (2001) 629– 646.

[4] G. Cachon, P. Zipkin, Competitive and cooperative inventory policies in a 2 stage supply chain, Management Science 45 (7) (1999) 936–953.

[5] A. Cavoukian, Data mining: staking a claim on your privacy, Publication of the Information and Privacy Commissioner, Ontario, Canada, 1998.

[6] F.Y. Chin, G. Ozsoyoglu, Auditing and inference control in statistical databases, IEEE Transactions on Software Engineering 8 (6) (1982) 574– 582.

[7] K. Cline, Planning for privacy, Banking Strategies 76 (6) (2000) 110.

[8] T. Dalenius, Towards a methodology for statistical disclosure control, Statistisktidskrift 5 (1) (1977) 429 – 444.

[9] D.E. Denning, R.J. Schlorer, Inference control for statistical databases, Computer 16 (7) (1983) 69–82.

[10] B. DePompa, There’s gold in the databases, Information Week (1996 January 8) 54.

[11] D. Dey, Record matching in data warehouses: a decision model for data consolidation, Operations Research 51 (2) (2003) 240– 255.

[12] D. Dey, V. Mookerjee, Techniques for efficient record linkage in heterogeneous databases, Working paper (2003).

[13] D. Dey, S. Sarkar, P. De, A probabilistic decision model for entity matching in heterogeneous databases, Management Science 44 (10) (1998) 1379– 1395.

[14] G.T. Duncan, D. Lambert, Disclosure-limited data dissemination, Journal of the American Statistical Association 81 (1) (1986) 10– 18.

[15] G.T. Duncan, S. Mukherjee, Optimal disclosure limitation strategy in statistical databases: deterring tracker attacks through additive noise, Journal of the American Statistical Association 95 (3) (2000) 720– 729.

[16] G.T. Duncan, R.W. Pearson, Enhancing access to microdata while protecting confidentiality: prospects for the future, Statistical Science 6 (3) (1991) 219 – 239.

[17] G.T. Duncan, R. Krishnan, R. Padman, S.F. Roehrig, Exact and heuristic methods for cell suppression in multi-dimensional linked tables, NISS Technical Report (2004).

[18] S. Dutta Chowdhury, G.T. Duncan, R. Krishnan, S.F. Roehrig, S. Mukherjee, Disclosure detection in multivariate categorical databases: auditing confidentiality protection through two new matrix operators, Management Science 45 (12) (1999) 1710–1723.

[19] J.P. Fellegi, A.B. Suntner, A theory for record linkage, Journal of the American Statistical Association 69 (6) (1969) 1183– 1210.

[20] S.E. Fienberg, Confidentiality and data protection through disclosure limitation: evolving principles and technical advances, Philippine Statistician 49 (1–4) (2000) 1 – 12.

[21] S.E. Fienberg, U.E. Makov, R.J. Steele, Disclosure limitation using perturbation and related methods for categorical data, Journal of Official Statistics 14 (2) (1998) 347 – 360.

[22] GAO, The Challenge of Data Sharing: Results of a GAOsponsored Symposium on Benefit and Loan programs, United States General Accounting Office Report, GAO-01-67 (2000) (http://www.gao.gov/new.items/d0167.pdf).

[23] GAO, Record Linkage and Privacy: Issues in Creating New Federal Research and Statistical Information, United States General Accounting Office Report, GAO-01-126SP (2001) (http://www.gao.gov/new.items/d01126sp.pdf).

[24] R. Garfinkel, R. Gopal, P. Goes, Privacy protection of binary confidential data against deterministic, stochastic, and insider threat, Management Science 48 (6) (2002) 749– 764.

[25] S. Gavirneni, R. Kapuscinski, S. Tayur, Value of information in capacitated supply chains, Management Science 45 (1) (1999) 16– 24.

[26] A.M. Geoffrion, R. Krishnan, Prospects for operations research in the e-business era, Interface 31 (2) (2001) 6 – 36.

[27] R. Gopal, P. Goes, R. Garfinkel, Interval protection of confidential information in a database, INFORMS Journal on Computing 10 (3) (1998) 552– 571.

[28] R. Gopal, R. Garfinkel, P. Goes, Confidentiality via camouflage: the CVC approach to disclosure limitation when answering queries to databases, Operations Research 50 (3) (2002) 501– 516.

[29] S.L. Hansen, S. Mukherjee, A polynomial algorithm for optimal univariate microaggregation, IEEE Transactions on Knowledge and Data Engineering 15 (4) (2003) 1043–1044.

[30] J.B. Kadane, Some statistical problems in merging data files, Journal of Official Statistics 17 (3) (2001) 422 – 433.

[31] J.P. Kelly, B.L. Golden, A.J. Assad, E.K. Baker, Controlled rounding for tabular data, Operations Research 38 (5) (1990) 760–772.

[32] H. Lee, S. Whang. Information Sharing in a Supply Chain, Research Paper No. 1549, Graduate School of Business, Stanford University, 1998.

[33] H. Lee, S. Whang, Supply chain integration in the age of ebusiness, Supply Chain Management Review 3 (3) (1999) 16 – 19.

[34] H. Lee, S. Whang, Supply Chain Integration over the Internet, http://www.commerce.net/research/ebusiness-strategies/2k1 2k1<sup>\_</sup>2k1<sup>\_</sup>r.pdf (2001).

[35] H.S. Lee, K.C. So, C.S. Tang, The value of information sharing in a two-level supply chain, Management Science 46 (5) (2000) 626–643.

[36] R.A. Moore, Controlled Data Swapping Techniques for Masking Public Use Microdata Files, Census Bureau Research Report Series (RR96-04) (1996).

[37] K. Muralidhar, R. Parsa, R. Sarathy, A general additive data perturbation method for database security, Management Science 45 (10) (1999) 1399–1415.

[38] M.A. Palley, J.S. Simonoff, The use of regression methodology for the compromise of confidential information in statistical databases, ACM Transactions on Database Systems 12 (4) (1987) 593–608.

[39] D.B. Rubin, Multiple imputation for nonresponse in surveys, John Wiley, New York, 1987.

[40] D.B. Rubin, Statistical disclosure limitation, Journal of Official Statistics 9 (2) (1993) 461 – 468.

[41] R. Sarathy, K. Muralidhar, The security of confidential numerical data in databases, Information Systems Research 13 (4) (2002) 389–403.

[42] R. Sarathy, K. Muralidhar, R. Parsa, Perturbing non-normal confidential attributes: the copula approach, Management Science, 48 (12) (2002), 1613–1627.

[43] E. Schonberg, T. Cofino, R. Hoch, M. Podlaseck, S.L. Spraragen, Measuring success, Communications of the ACM 43 (8) (2000) 53, (Internet/Web/Online Service Information).

[44] G.R. Simpson, Census Bureau Blurs Data to Keep Names Confidential, Wall Street Journal Online (http://www.wsj.com) (Feb. 14, 2001).

[45] H.J. Smith, Privacy policies and practices: inside the organizational maze, Communications of the ACM 36 (12) (1993) 105– 122.

[46] L. Willenborg, T. de Waal, Elements of statistical disclosure control, Springer-Verlag, New York, 2001.

[47] W.E. Winkler, Advanced methods for record linkage, Census Bureau Research Report Series (RR94/05), (1994).

[48] W.E. Winkler, The state of record linkage and current research problems, Census Bureau Research Report Series (RR99/04), (1999).

[49] W.E. Winkler, Record linkage software and methods for merging administrative lists, Census Bureau Research Report Series (RR01/03), (2001).

Rathindra Sarathy is Professor in the Department of Management Science and Information Systems at Oklahoma State University. He received his PhD from Texas A and M University. His research interests include database confidentiality, distributed databases, and e-commerce. His work has appeared in journals such as ACM Transactions on Database Systems, Decision Sciences, European Journal of Operations Research, Information Systems Research, and Management Science.

Krish Muralidhar is Gatton Research Professor at the School of Management, University of Kentucky. He received his PhD from Texas A and M University. His research interest are in the areas of database confidentiality, simulation, and statistical analysis. His research has appeared in journals such as ACM Transactions and Database System, Decision Sciences, Information Systems Research, Journal of Management, and Management Science.
