---
otero_id: 8422
otero_key: "HDM7C58B"
title: "A research case study: Difficulties and recommendations when using a textual data mining tool"
authors: "Abeer A. Al-Hassan; Faleh Alshameri; Edgar H. Sibley"
year: "2013"
journal: "Information & Management"
doi: "10.1016/j.im.2013.05.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: A Research Case Study: Difficulties and Recommendations when Using a Textual Data Mining Tool

Authors: Abeer A. Al-Hassan, Faleh Alshameri, Edgar H. Sibley

![](/api/attachments/HDM7C58B/fulltext/images/059ebe6b0907878f076335136324efe89e004110d806927ab7c2174431f815de.jpg)

PII: S0378-7206(13)00061-X

DOI: http://dx.doi.org/doi:10.1016/j.im.2013.05.010

Reference: INFMAN 2642

To appear in: INFMAN

Received date: 1-6-2012

Revised date: 23-12-2012

Accepted date: 27-5-2013

Please cite this article as: A.A. Al-Hassan, F. Alshameri, E.H. Sibley, A Research Case Study: Difficulties and Recommendations when Using a Textual Data Mining Tool, Information & Management (2013), http://dx.doi.org/10.1016/j.im.2013.05.010

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A Research Case Study: Difficulties and Recommendations when Using a Textual Data Mining Tool

Abeer A. Al-Hassan,

Assistant Professor,

Kuwait University, Kuwait

abeer@cba.edu.kw

Faleh Alshameri,

Assistant Professor,

Howard University, Washington, DC, USA

fal-shameri@howard.edu

Edgar H. Sibley

University Professor and Eminent Scholar, Emeritus

George Mason University, USA

esibley@gmu.edu

## Abstract

Although many interesting results have been reported by researchers using numeric data mining methods, there are still questions that need answering before textual data mining tools will be considered generally useful due to the effort needed to learn and use them.

In 2011, we generated a dataset from the legal statements (mainly privacy policy and terms of use) on the websites of 475 of the US Fortune 500 Companies and used it as input to see what we could detect about the organizational relationships between the companies by using a textual data mining tool. We hoped to find that the tool would cluster similar corporations into the same industrial sector, as validated by the company’s self-reported North American Industry Classification System code (NAICS). Unfortunately, this proved only marginally successful, leading us to ask why and to pose our research question: What problems occur when a datamining tool is used to analyze large textual datasets that are unstructured, complex, duplicative, and contain many homonyms and synonyms?

In analyzing our large dataset we learned a great deal about the problem and fortunately, after significant effort, determined how to “massage” the raw dataset to improve the process and learn

## 2

how the tool can be better used in research situations. We also found that NAICS, as selfreported by companies, are of dubious value to a researcher—a matter briefly discussed.

## Keywords:

Corporate Websites, Legal statements, Policy statements, Terms of Use, Textual Data Mining, Clustering, Industry Classification, NAICS, SIC, Privacy Statement.

## The review Process and our Acknowledgement

In order to have this paper reviewed (one of its authors is a co-Editor in Chief), the paper was initially sent to seven members of the Board of Editors with instructions to send their comments to Dr. Patrick Chau who would then mail them to the authors with reviewers’ names deleted, a one way blind review. The paper then went through further rounds of reviews and rework.

The authors would like to express their thanks to the Editors. Their comments, while tough, were very constructive and helped to improve our paper substantially.

## 1. Introduction

Electronic commerce is now an important part of national and international trade and thus more controls are needed to ensure effective website design and an efficient way of servicing customers. Today a person needing to buy a product will on his or her own behalf, or working as a purchasing agent for an organization, search the website of vendors to find a satisfactory and cost-effective product that is available and guaranteed by a vendor with whose products the buyer is familiar. However, as the electronic marketplace expands world-wide, the buyer needs to learn more about the organization and how it operates because the customer may live in a different country or be accessing the website of a small and relatively little-known company. Thus the material on a company website should be provided to satisfy the needs of worldwide customers whose search should be easy to perform; the data, of course, should be accurate and easy to understand. In our attempt to assess the “value” of a website, we decided to use a textual data mining tool. This led us to ask questions about the problems and potential of mining the contents of websites and to try to determine the difficulty in mining rather sparse and yet complex data. We therefore initially hoped to prove the following research hypothesis:

The material on an organization’s website discloses its sector of industry, where the industry is known by downloading the Corporation’s self-defined NAICS (which is normally included on its website).

Since almost every corporation uses the website as a way to advertize its wares, we felt that mining the whole site to determine whether the clusters would form into sets of industries would prove too simple a task and that the result of such a research effort would be trivial. Instead, we We therefore downloaded these parts of 475 of the US Fortune 500 company website attachments and their NAICS. Specifically, we used a data mining tool (CLUTO<sup>2</sup>) on the dataset consisting of all the available downloads<sup>3</sup>, hoping to find the results clumped into corporations considered to be in the same industry (i.e., performing business activities that have been categorized into easily understandable sectors, such as the computer industry). Governments and international bodies are interested in such categorization and the best known schemes today are the Standard Industry Code (SIC) and the North American Industry Classification System (NAICS).

Our attempt to determine the relationship between the legal attachment statements of FORTUNE 500 corporations and their (self-defined) industry code (NAICS) required some form of cluster analysis. At this point, we attempted to validate the results by checking to what extent the companies within a cluster had the same NAICS codes, and found that they did not perform as we expected. On examination of the NAICS, we realized that they did not seem to be what we expected--a surprising finding that led us to ask several questions about the process that a corporation takes to decide on its set of codes.

## 1.1 Our Purpose and the Research Questions

We wished to determine the value of textual data-mining by clustering the datasets formed by downloading only the legal portions of the websites of major corporations in the hopes of finding that they would be grouped according to their industrial classification, as stated by their selfdefined NAICS. This led to one major and one minor research question:

Is it possible or reasonable to evaluate the effectiveness of the textual data mining process by finding how closely the clumps resulting from the use of the data mining tool on data downloaded from a corporate website is explained by the corporation’s self-reported NAICS code?

And, because of our answer to this, it was necessary to add:

What has to be done to the downloaded data to allow a tool to clump the data meaningfully?

## 1.2 The Significance of our Results

The results of our work on the major question led us to a discussion of how to reduce the time and effort expended in obtaining useful information using a textual data mining tool on a complex and unformatted set of downloaded data.

The second or minor question led us to further asking:

What were the problems in stating a company’s SICs or NAICS codes? And

Are the data produced for international and local export/import analysis accurate (due to the lack of breakdown of the information delivered by individual corporations)?

These two seemed important questions and led to us to consider them as questions for our next major research project.

## 1.3 The Structure of the Paper

In section 2, we briefly discuss the portion of a typical website that deals with the legal aspects. This is followed (in section 3) by a description of the NAICS coding system and a discussion of textual data mining (section 4), leading to a discussion of our overall research methodology (Section 5). Section 6 provides an analysis of our results and section 7 our conclusions. Our references and eight appendices complete the paper.

## 2. The Contents of a Corporate Website

## 2.1 Legal Issues Affecting a Corporate Website

Most websites collect personal information from their visitors, and this gives rise to potential privacy infringement. Local, regional, and national governments have noted this and drafted laws to protect the individual; examples include the EU data protection law and US and its states’ data privacy laws that attempt to protect individuals from the misuse of personal information. These regulate the collection, storage, use, and cross-border transfer of data until its final disposal [8].

Most Fortune 500 organizations use the US Federal Trade Commission’s Fair Information Practice Principles (FIPP) [6] as a blueprint for their privacy policies. The FIPP has five core principles: Notice/Awareness, Choice/Consent, Access/Participation, Integrity/Security and Enforcement/Redress [7].

Many US laws, such as the Gramm-Leach-Bliley Act [3], which requires financial institutions to explain their information-sharing practices and ways of protecting sensitive information received from their customers, and the Health Insurance Portability and Accountability Act (HIPAA) [13], which addresses the storage and privacy of personal health data, have followed the FIPP core principles, as has the US Children’s Online Privacy Protection Act (COPPA) [2], which requires websites to post clear rules on what, if any, information it collects from children who visit their site. However, there is no standard template for such legal issues, though most websites have similar parts and some may also have portions written to ensure compliance with the laws of states in which they do business.

## 2.2 Components of the Privacy Policy Statement

The corporate privacy policies are explained in an attachment that says how the company protects the information that it collected from its visitors or potential customers. Its major purpose is to show any policies and practices when dealing with personal and private data that are collected from people and organizations, thereby making sure that they have a legal basis for their defense if sued for any release of private information, as well as giving all customers the right to decide whether to participate by providing their information or opt out of the process.

## 2.3 Components of the Terms of Use

Terms of Use are posted on a website to establish rules on operations that may be performed by the firm, its customers, and its partners. The website generally includes a statement of the service provided by its owner, used to disclaim any implied warranties [14] as well as a declaration of the site owner and visitors’ rights and responsibilities. Most sites require that their users/visitors accept the terms of use before being allowed to access other parts of the site, a practice considered to be a valid contract that is legally binding. It is important to note that sites differ in the complexity of these terms, depending on the nature of the corporation; such as it being commercial or public, etc.

The sections in a typical Terms of Use Agreement normally include:

Company Name/Website Information Changes to Terms Scope of Use and User Email Intellectual Property Links No Warranties

See Appendix 2 for an example of a Terms of Use Statement.

## 3. Industry Classification and the NAICS

The U.S. government developed and published SIC codes in 1935 for “collecting, analyzing, and publishing statistical data related to the U.S. business economy.” [12]. However, in 1997, under the auspices of the US Office of Management and Budget, a more modern set of codes were announced to replace the SIC: the NAICS system, developed in a joint effort of the USA, Canada, and Mexico.<sup>4</sup>

The codes are self-reported by an organization to help classify its products and services and report its primary economic activities; thus data is intended to be used to compare organizations in the same industry (with the same code) and across organizations and industries in different countries. The US government agencies involved in developing the classification system were the Bureau of Economic Analysis, the Bureau of Labor Statistics, and the Census Bureau. Other government regulatory and administrative agencies use NAICS codes, as do some state and local governments.

NAICS codes use a hierarchical numeric classification system, with the first two digits intended to designate the industry sector and subsequent digits providing more specific industry categories, as shown in Appendix 3. There are obvious similarities between the industry sectors. NAICS codes are not much more specific than SIC codes because the fifth digit was added to allow some second-tier industry groupings in the SIC to become major sectors and to add some new industry sectors, such as the Information industry. The sixth digit was added for countryspecific industries. Thus, with a few exceptions, NAICS codes are common across the US, Canada, and Mexico up to the fifth digit.

The NAICS codes can be viewed as a hierarchy of industries. The Information Sector is a tree or hierarchy, as illustrated in Appendix 4, where the tree has been “pruned” to show only some of its parts. Most of the large Information Sector Organizations among the Fortune 500 companies include their NAICS on their websites, though we removed two codes, 99999005 and 54161303, because they contributed little to the type of website.<sup>5</sup>

## 4. Textual Data Mining

Due to the rise in the use of the web, researchers have started to develop new ways to identify and extract data clutter from the large volumes of data now available. This makes it easier for users to navigate, summarize, and organize the information in a way that allows them to discover “interesting” relationships in the data.

Data mining tools provide a variety of computational techniques that can extract new information efficiently and effectively from large and often semi-formatted datasets. Their clustering algorithms organize the information into a number of groups that show the characteristics of the data as well as the relationships among the groups. Determining the most important features of the textual datasets therefore improves the analysis and extraction methods and provides a meaning to them [4, 5].

Data clustering [9] is one important technique for grouping similar data items. By organizing massive texts into meaningful clusters, people can observe the data from a “birds’eye” view. Clustering methods try to identify inherent groupings of textual documents so that the clusters exhibit high intra-cluster similarity and low inter-cluster similarity. Textual data mining [5] infers structure from natural language text. Documents may be labeled by keywords, and knowledge discovery is performed by analyzing the co-occurrence frequencies of the various keywords attached to the documents. In general, textual data mining is the natural extension of numeric data mining to unstructured or partially structured text data. Text clustering is an automatic process that divides and sorts text units into groups. The purpose of the clustering is to distinguish and classify the similarity among the physical or abstract objects. As a typical nonsupervised learning problem, text clustering methods include partition-based, hierarchical, density-based, grid-based, and model-based.

CLUTO is a software package that clusters textual datasets (those closest to each other) based on the similarity of words and phrases. It has been used for research in life sciences, law, and IS, and can classify large amounts of data efficiently. By reducing the role of the researcher in the analysis of data, it reduces bias and, by providing tools for visualizing the clustering, helps the user understand the relationships among the clusters, objects, and features, according to the frequency and similarity of the words in the document. It analyzes the clusters to determine their interrelationships by identifying all the words that occur within each cluster. The features help in understanding the documents assigned to each cluster and provide some idea of their content. The CLUTO algorithms were built for very large datasets and dimensions. We used its k-way repeated bisections clustering method, by which the objects are partitioned into two clusters, one of the clusters is selected and similarly bisected, and the process is then repeated until there are sufficient clusters to show similarities and differences in the groupings.

## 5. Our Overall Research Methodology

First, we downloaded the legal statements of 100 of the Fortune 500’s websites<sup>6</sup> and used CLUTO to perform a 10–way split. Examination of this data suggested that there were similarities between organizational types in each cluster (such as medical, insurance, and oil), but that some were obviously a mixture of several industries. We therefore increased the number of sites to 200 and again mined the results; this split the groups into smaller and more similar firms, but it was not easy to ensure lack of bias in making a judgment on the degree of similarity. We then increased the number of sites in increments of 100, ultimately ending with a population of 475 available websites; these were the datasets on which we finally performed our experiments. Second, we experimented to find the appropriate number of clusters needed to give good results in our experiments.

Third, we attempted to improve the clustering by removing inappropriate material from the dataset. This involved removing words such as cookie (that occurs on most websites) or phrases like limited liability (which only slightly discriminates one site from another).

Fourth, we looked for other ways that the datasets were “fogged” by words used in different ways by the various corporations (e.g., a company using its name or an abbreviation of it) that could make two corporations appear to be in the same industry though they really were not.<sup>7</sup>

Fifth, once we established an unbiased dataset, we added the self-defined NAICS codes for each company in the hope that we would find that companies had clustered into groupings that were in the same industry.

Each of these phases is now further discussed.

## 5.1 Downloading the Dataset of Legal Attachments

Our samples were drawn using the CNN Money - Fortune and Money’s annual ranking of America’s largest corporations: the Fortune 500 for 2011 [1]. When downloading the website information, we found that not all of the Fortune 500 corporation websites had a Terms of Use and/or Privacy Statement. Also, some had other attachments, such as titles, disclaimers, copyright notices. Twenty-five websites did not contain any legal attachment statement. Accordingly, the input to our data mining tool was that from just 475 websites, with a sequential number assigned to each company as a unique identifier (primary key). The privacy statement length (the number of words on each document) differed substantially: from 113 to 21, 489 words, with a median of 2,998 and a mean of 3,523 (Figure 1).

The total number of words in the dataset was 1,673,509 after the removal of all common highfrequency and stop words (i.e., a, the, of, for, with, etc, which are deemed irrelevant to the clustering though they appear frequently). The number of stop words depends on the dataset.<sup>8</sup> (See Appendix 5 for the stop list that we used at the start of our mining effort.)

![](/api/attachments/HDM7C58B/fulltext/images/aba79d391860db8ac842e3ed4cf79fa24c0114f5dc69b44ebb4985dbe75147b6.jpg)  
Figure 1: The length of each document in the dataset

## 5.2 Determining the Appropriate Number of Clusters for our Dataset

In textual data mining, the optimal clustering number could vary from one to the number of documents. The literature on data clustering has discussed the selection of an optimal value for k and StatSoft states that there is no unique way of determining it. Multiple variance statistical literature [10] gives a general formula to find the number of clusters: k= sqrt (n/2); where k is the number of clusters and n is the number of observations. Thus with n (the number of corporations) = 475, k should be 15. We therefore decided to cluster the results from our experiment using a k from 5 to 15; however, after 10, all cluster splitting stopped adding any value, and we stopped further analysis after 10. This effect is shown in the material of Appendices 7 and 8.

Figure 2 gives an example of the CLUTO output when k was 8. The number of companies in each cluster ranged from 34 to 100. All of the 475 objects were clustered (i.e., all documents were placed in a cluster). The figure shows each cluster number (cid), the number of objects in each cluster (size), the internal similarity between the objects of each cluster (ISim), the standard deviation of the average internal similarities (ISdev), the external similarity of the objects of each cluster with the rest of the objects (ESim), and the standard deviation of the external similarities (ESdev).  
The clusters are ordered in increasing (ISim-ESim) order; i.e., the clusters have compact populations with those close to one another having smaller cid values.

<table><tr><td colspan="6">8-ways clustering: [I2 = 1.25e+002] [475 of 475]</td></tr><tr><td>Cid</td><td>Size</td><td>ISim</td><td>ISdev</td><td>ESim</td><td>ESdev</td></tr><tr><td>0</td><td>34</td><td>+0.173</td><td>+0.061</td><td>+0.028</td><td>+0.009</td></tr><tr><td>1</td><td>50</td><td>+0.088</td><td>+0.027</td><td>+0.028</td><td>+0.011</td></tr><tr><td>2</td><td>50</td><td>+0.067</td><td>+0.019</td><td>+0.026</td><td>+0.007</td></tr><tr><td>3</td><td>44</td><td>+0.055</td><td>+0.013</td><td>+0.017</td><td>+0.007</td></tr><tr><td>4</td><td>54</td><td>+0.065</td><td>+0.013</td><td>+0.031</td><td>+0.007</td></tr><tr><td>5</td><td>81</td><td>+0.065</td><td>+0.011</td><td>+0.034</td><td>+0.007</td></tr><tr><td>6</td><td>100</td><td>+0.060</td><td>+0.012</td><td>+0.033</td><td>+0.008</td></tr><tr><td>7</td><td>62</td><td>+0.047</td><td>+0.010</td><td>+0.026</td><td>+0.009</td></tr></table>

Figure 2: The 8 cluster output for the dataset

The clusters can be represented as a leaf node on a tree. Figure 3 shows the hierarchical tree for the clusters. To construct this tree, the CLUTO algorithm repeatedly merges a particular pair of clusters, which was selected so that the resulting cluster at that point optimized the clustering function. The tree is shown with its root on the first column, and the tree grows from left to right. The leaves of the tree represent the clusters, which number from 0 to 7 (k=8). The internal nodes are numbered from 1 to 2\*(k-1), with the root being the highest numbered node (14 for k=8).

```txt
Hierarchical Tree that optimizes the I2 criterion function...

Size ISim XSim Gain
14 [ 475, 3.38e-002, 0.00e+000, -8.8"
Descriptive: health 1.0"
Frq. Phrases 1: inform 475,
Frq. Phrases 2: includ.limit
Frq. Phrases 3: fit.particu:
----
12 [ 84, 7.65e-002, 2.68e-002, -5.7"
Descriptive: health 9.7"
Frq. Phrases 1: access 84, :
Frq. Phrases 2: product.ser
Frq. Phrases 3: fit.particu:
----
----0 [ 34, 1.73e-001, 3.54e-002, +0.0"
Descriptive: health 22.5"
Frq. Phrases 1: provid 34, :
Frq. Phrases 2: inform.prov
Frq. Phrases 3: fit.particu:
----
----1 [ 50, 8.76e-002, 3.54e-002, +0.0
```  
Figure 3: Part of the hierarchical tree for the clusters

CLUTO also analyzes each cluster and displays the set of features that discriminate each of the clusters. In Figure 4, the second line contains ten of the most descriptive features (i.e., average similarity between the objects of the cluster and the words most used in the cluster after stop words had been removed) with line three having the ten discriminating words (i.e., the percentage of the dissimilarity between the cluster and the rest of the objects that this feature can explain). The features in these two lists are shown in decreasing order. For example, for cluster 0, the feature “health” explains 22.5% of the average similarity between the objects of the 0th cluster. Of course, the percentages of the discriminating features are smaller than the corresponding percentages of the descriptive features because some the features of the cluster can also be present in a small fraction of the objects that do not belong in the cluster.

The discriminating words are used as a key to determine the general topic title for each cluster; i.e., as a surrogate for the topic title.

<table><tr><td>8-way clustering solution-Descriptive &amp; Discriminating Features</td></tr><tr><td>Cluster 0, Size: 34, ISim: 0.173, ESim: 0.028Descriptive: health 22.5%, phi 9.1%, health.inform 7.8%, health.careDiscriminating: health 15.9%, phi 7.1%, health.inform 5.8%, health,careFrq.Phrases1: provide 34, inform 34, data 34, access 34, protect 34,Frq.Phrases2: inform.provide 32, product.service 30, inform.collect 30Frq.Phrases3: fit.particular.purpos 22, merchant.fit.particular 20</td></tr><tr><td>Cluster 1, Size: 50, ISim: 0.088, ESim: 0.028Descriptive: bank 4.6%, insur 4.1%, limit.share 1.3%, finance 1.3%Discriminating: bank 4.2%, insur 2.9%, limit.shar 1.3% finance 0.8%Frq.Phrases1: inform 50, access 50, provide 49, service 48, include 48,Frq.Phrases2: product.service 47, inform.provide 43, inform.include 39Frq.phrases3: Physic.electron.procedure 26, electron.procedure.safeguard 26</td></tr></table>

Figure 4: Part of the output showing the discriminating words

## 5.3 Removing Other Inappropriate Terms from the Dataset

While examining the results, we realized that there were words and phrases (such as privacy statements and links) that were used in many datasets and “fogged” the results. It was obvious that we needed to cleanse the data by deleting these words and phrases. This involved a discussion between the researchers about the apparent overlapping of industries as shown in the discriminating words of the clusters. The words that we found to be most misleading are shown in Appendix 6.

## 5.4 The Removal of Corporate Names as Obfuscators

It also became obvious by examining the descriptive words in a cluster that some parts of a Company Name (which is often repeated in its dataset) distorted the results. For example, the “American Financial Group” would be clustered on the terms American, Financial, and Group. However, this meant that the corporation would likely be clustered with the “Altria Group” because it contained the term Group. We therefore deleted company names from the datasets.

We felt we now had a database that represented the information on the Corporate Websites, though it was rather sparse in content as so many “fog” words had been removed. We therefore tried to determine an optimal value for k by modifying its value between 5 and 10 splits. (See Appendix 7 for the hierarchy.) Once we had the splits and observed the clusters that CLUTO had formed, we were ready to look at their NAICS and decide whether they were the same as or similar to other companies in the same cluster.

## 5.5 Comparing the Clusters by Industry via their selected NAICS

Because we identified the data in the clusters as belonging to one corporation, we were able to attach the company’s self-defined set of NAICS to its dataset (via the key we had attached to each company) by mapping the identifiers into the first two digits of their self-defined NAICS code<sup>9</sup> to help in analyzing results. It was then possible to see how many corporations fit into each member of the set of NAICS and give this as a percentage of the total in that particular cluster. This allowed us to compute the percentages of companies that had the same NAICS within a cluster. Appendix 8 provides an example of a cluster including each company’s NAICS, as well as an analysis of Cluster 0 (34 companies) and Cluster 2 (181 companies) and their splits from 5- way to 10-way.

## 6. Analysis and Discussion of Results

As we began our analysis, we focused on all the clusters and their splits in the hierarchy with the number of times they split. We looked at each cluster in our 5-way split and traced its behavior from that point to 10-way clustering. We therefore were able to see the number of companies in similar industries that fell in the same cluster. We also could determine the potential of each company to be a member of a different cluster (based on some characteristics that that company had in common with other clusters). Moreover, we scrutinized percentages of companies with the same NAICS in the same cluster and then looked at the anomalies and re-read their legal attachment statements in an attempt to identify the reason that they were placed in a particular cluster.

There are obvious overlaps and similarities of corporations in the same industry but, as NAICS are self-reported and not reviewed by anyone outside the organization, there was no guarantee that they collectively made good sense. The fact t hat they are used by US governmental and other statistical bodies despite their potential deficiency raises serious policy questions that require further examination.

## 6.1 Observations on the Data in Cluster 0

For the 34 companies in cluster 0 shown in Table 1 in Appendix 8, 30 contained one or more of the following NAICS: 32, 33, 44, 53, or 62 with percentages that were significant enough to map the companies’ legal attachment statements to “What does the NAICS represent.”

The companies that were anomalies and did not have any NAICS in common were Northrup Grumman, Pepco Holding, Walmart, and Target. In reading the four companies’ Legal Attachment Statements, we found that Walmart and Target did have pharmacies/drug stores but we could not see any NAICS that would tie them to other companies. Northrup Grumman is a manufacturing company with the NAICS 33. As for Pepco, the only common NAICS was 54 (marketing).

The Legal Attachment statement of Northrup Grumman contained only 454 words and, after removing the stop words and company name, had only 236 words. However, the terms data and information were repeated many times in the attachment and the Clustering Results for the Freq. Phrases in Cluster 0 included data and inform, apparently explaining why Northrup Grumman was placed in the cluster. For Pepco Holding Inc., the Legal Attachment statement had 2,034 words, but it used the acronym PHI (Pepco Holding Inc), which also stood for Personal Health Information when used on websites of many health-related companies. Again, this made the term foggy! Finally, Target was a candidate for other clusters because it had pharmacy, retail, and grocery store components.

## 6.2 Observations on Clusters 1-4

We checked every cluster in order to provide a comprehensive understanding of all the datasets.<sup>10</sup> However, there was only one other cluster (1) that contained 50 companies and had significant results: it did not split between 5- and 10-way clustering. Seventy-eight percent (78%) of its companies had a common NAICS 52 (Finance and Insurance), which meant that 39 out of 50 companies had these two activities according to their self-defined NAICS. From the 11 companies that did not have an NAICS of 52, four were car dealers (AutoNation, Car Max, Group1 Automotive and Sonic Automotive), and included such activities as consumer lending, though their NAICS codes did not reflect this. Nordstrom was also included in Cluster 1, and offered their customers credit cards, but did not report NAICS 52 as one of their activities. Principal Financial also offered online banking and other financial activities that made its legal attachment statement align with those of similar companies, but it did not report itself as an NAICS 52 company. Commercial Metals offered banking and credit cards services and a credit union so it was not surprising that its legal attachment included many descriptive and discriminating terms that appeared in attachments of other members of the cluster. Frontier Oil and Holly also had identical legal attachment statements; Holly is a subset of Frontier-Holly Inc. so it makes sense that they would be in the same cluster. Finally, Pluto Group and Century Link seemed to be the anomalies in the cluster; they had repeated terms that contributed to their selection to appear in cluster 1.

For Clusters 2, 3, and 4 in 5-way clustering, we began to see the shortcomings of our approach. Due to problems resulting from the fact that there was no validity check made by any official agency on the self-defined NAICS and that there was no proposed standard for the legal statements, the use of a data mining tool appeared to be of dubious value. It became very hard to understand how the clusters in 2, 3, and 4 behaved. They were much larger clusters, containing 181, 94, and 116 companies, respectively. In these three clusters, significant percentages ranged amongst the following two digit NAICS: 21, 22, 32, 33, 42, 44, 51, 52, and 55. For example, Cluster 2, 3, and 4 all contained NAICS 42 (Wholesale Trade) with significant percentages 44, 31, and 48%.

Apparently, another problem we faced was that the Fortune 500 companies are large and perform many activities that place them in more than one cluster. For example, Kimberly Clark selfdefined its activities as NAICS 21, 22, 23, 31, 32, 33, 42, 48, 52, 54, and 55.

We also observed that large clusters split unevenly; e.g., cluster 2 (with 181 companies) split into 81 and 100 with the 81 cluster splitting further into 24 and 57 companies. The percentages of the NAICS split in similar proportions, though we had hoped that the NAICS would stay together in one of the splits. For example, while the cluster with 181 companies included NAICS ID 42 at 37%, we were hoping that when this set split into 81 and 100 that the NAICS would “clump” into one of these two sets (to keep companies with same NAICS tied together). Unfortunately, this was not the case. Appendix 7 shows how the clusters bifurcated as more clusters were formed. Thus, the split produced a simple tree form.

## 7. Conclusions

## 7.1 Overall Comments

One of our reviewers commented: “This paper is essentially a case study of a research project; the authors describe the progress of the project and the changes that were required as they proceeded, It is quite illuminating for those considering similar projects; it highlights some of the difficulties they may encounter and offers some solutions.“ Another said “I think one can learn much more from this study about NACIS and organizational self-reporting than about relationships between the organizations.”

From our extensive analysis of the outputs of CLUTO, we became convinced that it could be effective in providing results that can be valuable in addressing research questions about large textual databases. The complementary use of CLUTO with manual content analysis supports the use of data mining tools in analyzing large textual databases. However, because of our difficulty in determining the accuracy of the self-defined NAICS codes, we were led to ask some questions that we had not seemed important when we started the research:

• Who (or at what level) in the company is told to select and report on the codes?

• How many classification codes should a company report?

• How do the corporate responders decide on the classification?

• Is there a team or official with ultimate responsibility to check and agree to the set of codes?

• Does the set of codes selected represent the image that the corporation wishes to project?

• Whose interests may the classification represent?

This problem is exacerbated by the fact that there is no objective external validation of the classifications selected.

## 7.2 Comments on the Process

We were interested in understanding the problems in using data-mining techniques on large and rather sparsely populated datasets. Specifically, we downloaded the Privacy and Terms of Use statements made by members of the Fortune 500 companies on their websites in 2011. Our hope was that we would be able to cluster the companies into an approximation to their industry group (as defined by their NAICS codes).

At first, we found that there was poor grouping with some of the discriminating words showing little similarity between corporations in a cluster so that we felt we were finding only random clustering. However, when the discriminating words were examined, it was apparent that several of them (like children, copyright, link, and cookie) appeared in almost all websites--and thus did not discriminate, but should be considered as stop words. We therefore went through several cycles of investigation, resulting in improved clustering but still finding some overlaps because of common words in the Company Name that did not correlate with industry categories (like electric, general, or corporation).

A problem we faced while analyzing results was our inability to make a claim with high confidence. As a result, we feared that some hidden factor had been missed or was not fully considered. Unfortunately, our research seemed to produce fuzzy results that depended on the reasoning of the analyst in order to ensure its quality. Examples of decisions that had to be made included:

• What constitutes a legal attachment statement (i.e., what to extract from website)?

• How did the company select its NAICS?

We saw that companies varied substantially in their choice of NAICS, even though we felt they performed similar activities. Indeed, as we analyzed their NAICS, we realized that self-reported NAICS were inconsistent. For example, when we ran a search for the industry for NAICS ID 33 using the United States Census Bureau of NAICS for 2007 [11], we found that the multi-digit NAICS included 331, 3311, 3312 , 332, etc., but that 338 did not exist and 339999 represented all miscellaneous manufacturing. Moreover, while company VF self-defined itself as 42432006 (Men’s & Boys Clothing Merchant Wholesale), 54151109 (Custom Computer Programming Svsc), and 54161303 (Marketing Consulting Svcs), we could not understand how these activities, which are not homogenous and seem unrelated, represent its industrial niche.

However, we did find that for one or two major clusters of industries constructed by the data mining tool, there were several NAICS that represented the group at a significant level. It is possible then that the differences were due to a lack of a standard way of assessing and therefore defining the NAICS and/or the fact that we chose a relatively sparse dataset from the standpoint of industry distinction–their Legal Attachments.

## 7.3 Major findings

Initially we posed the question: What problems occur when a data-mining tool is used to analyze large textual datasets that are unstructured, complex duplicative and contain many homonyms and synonyms? During our analysis of the rather large textual dataset we encountered many “strange” findings which we were able to clarify by applying manual analysis. The unstructured, complex, duplicative nature of the large datasets provided results that seemed inconsistent until we could tell why the software provided the results. We found it necessary to make adjustments to the datasets to reduce errors caused by:

• Similar words, synonyms, and phrases such as Cookies, and Links which acted as discriminating leading to the clustering of unrelated industries.

• Common words occurring in the names of organizations that also resulted in clustering of unrelated industries (e.g., General Electric, General Foods, and General Motors), requiring elimination of company names from the datasets.

• Companies that we considered to be in the same industry were indeed clustered together but on examination of the results we found that their NAICS (self defined) were surprisingly different.

Such problems can be simply avoided with some manual intervention at the start of analysis. As to the NAICS part of this problem, the “self reported nature” of those codes allow errors when comparing two industries and a controlled process should be provided by a standardizing agency. Having refined their analysis of the data through multiple iterations, what is the value of the authors’ experience?

Through the analysis we became convinced that textual mining requires careful understanding of the meaning of the words in the datasets and that the way the words are used in the sentences plays an important part in the accuracy of the results; i.e., ontology plays an important role in textual data mining and new tools should incorporate ways to exploit ontology. The authors believe that textual data mining is still in its infancy and that some stages still needs human intervention.

Thus we did read all the legal Attachment Statements and removed common words, repeated words in the dataset, and acronyms that were common but different, such as PHI (Personal Health Information or Pepco Holding Inc.). We cannot however claim that the application of our research model to a different dataset would be valuable, though we hope it would be useful, especially in Big Data and social media analysis.

## 7.4 Suggestions for Future Research

Our effort was obviously limited in that it used only one of many data mining tools. The study should probably be repeated with several data mining tools and the same datasets to provide a comparative analysis and see if the results vary across tools. Also, it would be interesting to replicate the experiment with other datasets, such as those downloaded from a social website (e.g., Facebook) or to replicate the effort using the entire set of elements of the Fortune 500 websites--a very large database and an exhausting task.

Clustering and numeric data mining methods have been used in business and related research to find statistical patterns for marketing, but it seems that the ability to use more textual data in such studies (and ultimately in practice) would be possible if the method could be more automated (without the effort we had to make to reduce the problems of synonyms, for example). Maybe the addition of an ontology tool could remove some of the problems--a possible solution to the problems and worth investigation.

The problem of deciding whether a particular set of NAICS or SIC codes properly describe the industry of a particular corporation has already been discussed. But this was not the prime reason for our effort, though we are planning to make it the subject of future work.

## 8. References

[1] Annual Ranking of Americas Largest Corporations 2011. CNN Money. [online] Available at: (http://money.cnn.com/magazines/fortune/fortune500/2011/full\_list) [accessed $1 5 ^ { \mathrm { t h } }$ April 2011].

[2] Children’s Online Protection Privacy Act of 1998. Federal Trade Commission [online] available at: (http://www.ftc.gov/ogc/coppa1.htm) [Accessed $2 7 ^ { \mathrm { t h } }$ July 2011].

[3] Conference Report and Text of The Gramm-Leach-Bliley Bill, 1999. US Senate Committee on Banking, Housing, and Urban Affairs. [Online] Available at: (http://banking.senate.gov/conf) [Accessed 11<sup>th</sup> October 2011].

[4] Deng, J., Hu, J., Chi, H., and Wu, J. (2010) An Improved Fuzzy Clustering Method for Text Mining, Proceedings of the 2010 Second International Conference on Networks Security, Wireless Communications and Trusted Computing, 1, 65-69.

[5] El Fangary, L. (2009) Applying an Enhanced Algorithm for Mining Incremental Updates on an Egyptian Newspaper Website, INC, IMS and IDC, 2009. NCM '09. Fifth International Joint Conference on, 1131 – 1135.

[6] Federal Trade Commission, 2007. Fair Information Practice Principles [online] Available at: (http://www.ftc.gov/reports/privacy3/fairinfo.shtm) [Accessed 27<sup>th</sup> July 2011].

[7] Federal Trade Commission, 2007. Fair Information Practice Principles:[online] Available at: (http://www.ftc.gov/reports/privacy3/fairinfo.shtm#Choice/Consent) [Accessed 27<sup>th</sup> July 2011].

[8] Freenetlaw, 2011. Free Privacy Statement. [online] Available at: (http://www.freenetlaw.com/free-privacy-statement/?gclid=CMOou42-1qoCFQrf4AodZlU49g) [Accessed 27<sup>th</sup> July 2011].

[9] Liu, Y., Wu, C., and Liu, M. (2011) Research of fast SOM clustering for text information, Expert Systems with Applications, 38, 9325-9333.

[10] Mardia,K., Kent, J., Bibby, M 1980, Multivariate Analysis: Probability and Mathematics Statistics, 7<sup>th</sup> reprinting, 1979 Academic Press 2000.

[11] NAICS Definition, North American Standard Classification System, 2007 NAICS. United States Census Bureau [online] Available at: (http://www.census.gov/cgibin/sssd/naics/naicsrch) [Accessed 3<sup>rd</sup> January 2011].

[12] North American Standard Classification System, 2007 NAICS. United States Census Bureau [online] Available at: ( http://www.census.gov/eos/www/naics/) [Accessed 25th October 2011].

[13] OCR Privacy Brief: Summary of the HIPPA Privacy Rule, 2003. United States Department of Health Services [online] (http://www.hhs.gov/ocr/privacy/hipaa/understanding/summary/privacysummary.pdf) [Accessed 15<sup>th</sup> August 2011].

[14] Terms of Use – Registered and non-registered users 2011. Findlegalforms.com [online] available at: (http://www.findlegalforms.com/forms/terms-of-use-agreement/) [Accessed 15<sup>th</sup> August 2011].

## Appendices

## Appendix 1: A Typical Organization’s Privacy Statement

In general all Corporations include the five core principles of the FIPP. Here are the parts extracted from the site of the 3M Corporation<sup>11</sup> and their mapping to the FIPP:

1. 3M Global Internet Privacy Policy

2. Web Site Privacy Statements

3. Your Consent

4. Limitations on the Collection, Use and Disclosure of Personal Information

5. Information Collected on 3M Internet Sites and How It May be Used

6. Sharing Personal Information

7. Security of Personal Information

8. Links to Third Party Internet Sites

9. Access to Personal Information

10. Retention of Personal Information

11. Children and Parents

12. Questions about this Policy or our Privacy Statements

13. Changes to this Policy and our Privacy Statements

These thirteen sections map to the FIPP as follows:

• 1, 2, 5, 6, 8, and 10 all fall under Notice/Awareness

• 3 and 4 map to Choice/Consent

• 9 maps to Access/Participation

• 7 maps to Integrity/Security

11 deals with children’s access and 3M generally states that it should be contacted if a customer or user feels violated. Thus these map to Enforcement /Redress

## Appendix 2: A Typical Organization’s Terms of Service

Again there is no standard of what is common, but here is an example: Google’s Terms of Service<sup>12</sup> when accessed in 2011.

Note a modified version was issued in January 2012.

1. Your relationship with Google

2. Accepting the Terms

3. Language of the Terms

4. Provision of the Services by Google

5. Use of the Services by you

6. Your passwords and account security

7. Privacy and your personal information

8. Content in the Services

9. Proprietary rights

10. License from Google

11. Content license from you

12. Software updates

13. Ending your relationship with Google

14. EXCLUSION OF WARRANTIES

15. LIMITATION OF LIABILITY

16. Copyright and trade mark policies

17. Advertisements

18. Other content

19. Changes to the Terms

20. General legal terms

Appendix 3: The Industry Sectors of the NAICS

<table><tr><td>Sector</td><td>Description</td></tr><tr><td>11</td><td>Agriculture, Forestry, Fishing and Hunting</td></tr><tr><td>21</td><td>Mining</td></tr><tr><td>22</td><td>Utilities</td></tr><tr><td>23</td><td>Construction</td></tr><tr><td>31-33</td><td>Manufacturing</td></tr><tr><td>42</td><td>Wholesale Trade</td></tr><tr><td>44-45</td><td>Retail Trade</td></tr><tr><td>48-49</td><td>Transportation and Warehousing</td></tr><tr><td>51</td><td>Information</td></tr><tr><td>52</td><td>Finance and Insurance</td></tr><tr><td>53</td><td>Real Estate and Rental and Leasing</td></tr><tr><td></td><td rowspan="2">Professional, Scientific, and Technical Services</td></tr><tr><td>54</td></tr><tr><td>55</td><td>Management of Companies and Enterprises</td></tr><tr><td></td><td>Administrative and Support and Waste</td></tr><tr><td>56</td><td>Management and Remediation Services</td></tr><tr><td>61</td><td>Education Services</td></tr><tr><td>62</td><td>Health Care and Social Assistance</td></tr><tr><td>71</td><td>Arts, Entertainment, and Recreation</td></tr><tr><td>72</td><td>Accommodation and Food Services</td></tr><tr><td></td><td rowspan="2">Other Services (except Public Administration)</td></tr><tr><td>81</td></tr><tr><td>92</td><td>Public Administration</td></tr></table>

Source: North American Standard Classification System, 2007 NAICS. United States Census Bureau [online] Available at: http://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2007 [Accessed 25 October 2011]

Appendix 4: The NAICS hierarchy for the Information Sector and Entries from Selected Organizations in the Industry Sector  
![](/api/attachments/HDM7C58B/fulltext/images/45572627522c383176b3acdced245f98abbcc4c02c7097db4cb3da64237affa5.jpg)

<table><tr><td>Fortune500Company</td><td>NAICS Code</td></tr><tr><td>Intel</td><td>33441302 Semiconductors &amp; Related Devices Manufacturing42343014 Computer &amp; Software Merchant Whls44312007 Computer &amp; Software Stores52391003 Misc Intermediation</td></tr><tr><td>Dell</td><td>51119911 All Other Publishers33411103 Electronic Computer Manufacturing33411201 Computer Storage Device Manufacturing33411301 Computer Terminal Manufacturing33411901 Other Computer Peripheral Equip Manufacturing44312007 Computer &amp; Software Stores44312001 Computer &amp; Software Stores54151905 Other Computer Related Svcs</td></tr><tr><td>IBM</td><td>32311009 Commercial Lithographic Printing33411101 Electronic Computer Manufacturing33411103 Electronic Computer Manufacturing33411104 Electronic Computer Manufacturing33411201 Computer Storage Device Manufacturing33411301 Computer Terminal Manufacturing33411902 Other Computer Peripheral Equip Manufacturing33411901 Other Computer Peripheral Equip Manufacturing51791916 All Other Telecommunications42399010 All Other Durable Goods Merchant Whls44312001 Computer &amp; Software Stores54151105 Custom Computer Programming Svcs51121001 Software Publishers54151204 Computer Systems Design Svcs51821013 Data Processing &amp; Related Svcs81121206 Computer &amp; Office Machine Repair54151904 Other Computer Related Svcs54151903 Other Computer Related Svcs81131030 Commercial Machinery Repair &amp; Maintenance</td></tr><tr><td>Microsoft</td><td>51113001 Book Publishers33411101 Electronic Computer Manufacturing33411901 Other Computer Peripheral Equip Manufacturing51791916 All Other Telecommunications42399019 All Other Durable Goods Merchant Whls44312007 Computer &amp; Software Stores52311002 Investment Banking &amp; Securities Dealing55111201 Offices Of Other Holding Companies54151104 Custom Computer Programming Svcs51121001 Software Publishers51821013 Data Processing &amp; Related Svcs54161816 Other Management Consulting Svcs</td></tr><tr><td>Google</td><td>51821011 Data Processing &amp; Related Svcs51821018 Data Processing &amp; Related Svcs</td></tr></table>

Some IS members of the Fortune 500 Corporations with their self-reported NAICS

Appendix 5: Initial Stop Words for Our Dataset

<table><tr><td>a</td><td>becomes</td><td>every</td><td>however</td><td>off</td><td>such</td><td>well</td></tr><tr><td>about</td><td>becoming</td><td>everyone</td><td>ie</td><td>often</td><td>system</td><td>were</td></tr><tr><td>above</td><td>been</td><td>everything</td><td>if</td><td>on</td><td>take</td><td>what</td></tr><tr><td>after</td><td>before</td><td>everywhere</td><td>in</td><td>once</td><td>than</td><td>whatever</td></tr><tr><td>afterwards</td><td>behind</td><td>except</td><td>inc</td><td>only</td><td>that</td><td>when</td></tr><tr><td>again</td><td>being</td><td>few</td><td>into</td><td>onto</td><td>the</td><td>whenever</td></tr><tr><td>all</td><td>below</td><td>fill</td><td>is</td><td>or</td><td>their</td><td>where</td></tr><tr><td>almost</td><td>between</td><td>find</td><td>it</td><td>other</td><td>them</td><td>whereas</td></tr><tr><td>alone</td><td>beyond</td><td>for</td><td>its</td><td>others</td><td>themselves</td><td>wherever</td></tr><tr><td>already</td><td>both</td><td>former</td><td>itself</td><td>otherwise</td><td>then</td><td>whether</td></tr><tr><td>also</td><td>bottom</td><td>formerly</td><td>last</td><td>our</td><td>there</td><td>which</td></tr><tr><td>although</td><td>but</td><td>found</td><td>least</td><td>ours</td><td>these</td><td>while</td></tr><tr><td>always</td><td>by</td><td>from</td><td>less</td><td>ourselves</td><td>they</td><td>who</td></tr><tr><td>am</td><td>call</td><td>front</td><td>ltd</td><td>out</td><td>this</td><td>whole</td></tr><tr><td>an</td><td>can</td><td>full</td><td>many</td><td>over</td><td>those</td><td>whom</td></tr><tr><td>and</td><td>cannot</td><td>further</td><td>may</td><td>per</td><td>though</td><td>whose</td></tr><tr><td>another</td><td>can&#x27;t</td><td>get</td><td>me</td><td>please</td><td>through</td><td>why</td></tr><tr><td>any</td><td>could</td><td>give</td><td>more</td><td>put</td><td>thus</td><td>will</td></tr><tr><td>anyhow</td><td>couldn&#x27;t</td><td>go</td><td>much</td><td>see</td><td>to</td><td>with</td></tr><tr><td>anyone</td><td>detail</td><td>had</td><td>must</td><td>she</td><td>together</td><td>within</td></tr><tr><td>anything</td><td>do</td><td>has</td><td>my</td><td>should</td><td>too</td><td>without</td></tr><tr><td>anyway</td><td>done</td><td>hasn&#x27;t</td><td>myself</td><td>show</td><td>top</td><td>would</td></tr><tr><td>anywhere</td><td>down</td><td>have</td><td>neither</td><td>since</td><td>toward</td><td>yet</td></tr><tr><td>are</td><td>due</td><td>he</td><td>never</td><td>so</td><td>towards</td><td>you</td></tr><tr><td>around</td><td>during</td><td>hence</td><td>next</td><td>some</td><td>un</td><td>your</td></tr><tr><td>as</td><td>each</td><td>her</td><td>no</td><td>somehow</td><td>until</td><td>yours</td></tr><tr><td>at</td><td>either</td><td>here</td><td>nor</td><td>someone</td><td>up</td><td>yourself</td></tr><tr><td>back</td><td>else</td><td>herself</td><td>not</td><td>something</td><td>us</td><td>yourselves</td></tr><tr><td>be</td><td>elsewhere</td><td>him</td><td>nothing</td><td>sometime</td><td>very</td><td></td></tr><tr><td>became</td><td>etc</td><td>himself</td><td>now</td><td>sometimes</td><td>via</td><td></td></tr><tr><td>because</td><td>even</td><td>his</td><td>nowhere</td><td>somewhere</td><td>was</td><td></td></tr><tr><td>become</td><td>ever</td><td>how</td><td>of</td><td>still</td><td>we</td><td></td></tr></table>

Appendix 6: Other Words and Phrases “Removed” for Data Mining

<table><tr><td>children</td><td>legal notice</td><td>privacy statement</td></tr><tr><td>collected information</td><td>Limited liability</td><td>security</td></tr><tr><td>conditions</td><td>link</td><td>security and privacy</td></tr><tr><td>cookie</td><td>linked</td><td>Site information</td></tr><tr><td>cookies</td><td>links</td><td>sites</td></tr><tr><td>copyright</td><td>look</td><td>Spyware</td></tr><tr><td>copyrights</td><td>merchant fit particular</td><td>terms</td></tr><tr><td>data privacy</td><td>online</td><td>terms of condition</td></tr><tr><td>Disclaimer</td><td>online privacy policy</td><td>terms of use</td></tr><tr><td>Email address</td><td>opt out</td><td>third parties</td></tr><tr><td>ethic</td><td>opt-out</td><td>third party</td></tr><tr><td>External Links</td><td>party</td><td>third-party</td></tr><tr><td>forward</td><td>person</td><td>Trademark</td></tr><tr><td>forward look</td><td>Personal identification information</td><td>Trademarks</td></tr><tr><td>Forward looking statements</td><td>personal information</td><td>Viruses</td></tr><tr><td>Forward-looking statements</td><td>Pharming</td><td>Warranties</td></tr><tr><td>Fraud</td><td>Phishing</td><td>warranty</td></tr><tr><td>identification form</td><td>policies</td><td>web site</td></tr><tr><td>Identity theft</td><td>policy</td><td>web sites</td></tr><tr><td>Inform third Party</td><td>privacy</td><td>website</td></tr><tr><td>Information Collected</td><td>Privacy notice</td><td>websites</td></tr><tr><td>information disclosure</td><td>privacy policy</td><td></td></tr><tr><td>legal disclosure</td><td>Privacy protection</td><td></td></tr></table>

Appendix 7: The splitting of Clusters from 5 to 10 for Our Dataset

This figure shows how the Clusters split in going from a k of 5 to 10 – thus cluster 0 remained the same 34 organizations throughout, while cluster 3 0f 181 organizations split into two clusters of 81 and 100; and then the cluster of 81 split into 24 and 57.

![](/api/attachments/HDM7C58B/fulltext/images/af2a037032bad166c18ec99ab05a64be98d4a4530609233d01a287267a6703fa.jpg)

## Appendix 8: The Percentages of Companies that Contained the Same Two Digit NAICS in a Cluster

This appendix shows some tables for which we calculated percentages of clustering that compared favorably with their NAICS. Note: that only companies that earned up to 10% are recorded in the table.

Table 1: cluster 0 {34 companies}split from 5-way to 10-way.  
Only one Table was needed for Cluster 0 {34 companies} because it did not split.

<table><tr><td>2 Digit NAICS</td><td>Number of Companies</td><td>% of Total</td><td>Names of Industry that 2 Digit NAICS represents</td></tr><tr><td>42</td><td>4</td><td>12%</td><td>Wholesale Trade</td></tr><tr><td>45</td><td>4</td><td>12%</td><td>Sporting Goods, Hobby, Book, and Music Stores</td></tr><tr><td>81</td><td>4</td><td>12%</td><td>Other Services (Except Public Administration)</td></tr><tr><td>32</td><td>6</td><td>18%</td><td>Wood Product Manufacturing</td></tr><tr><td>33</td><td>6</td><td>18%</td><td>Primary Metal Manufacturing</td></tr><tr><td>44</td><td>8</td><td>24%</td><td>Retail Trade</td></tr><tr><td>62</td><td>12</td><td>35%</td><td>Health Care</td></tr><tr><td>52</td><td>21</td><td>62%</td><td>Finance and Insurance</td></tr></table>

Tables 2 to 6: Cluster 2 split from 5-way to 10-way.

Table 2: Cluster 2 {181 companies} at 5-way split.

<table><tr><td>2 Digit NAICS</td><td>Number of Companies</td><td>% of Total</td><td>Names of Industry that 2 Digit NAICS represents</td></tr><tr><td>55</td><td>20</td><td>11%</td><td>Management of Companies and Enterprises</td></tr><tr><td>31</td><td>22</td><td>12%</td><td>Manufacturing</td></tr><tr><td>32</td><td>24</td><td>13%</td><td>Wood Product Manufacturing</td></tr><tr><td>45</td><td>31</td><td>17%</td><td>Sporting Goods, Hobby, Books, and Music Stores</td></tr><tr><td>51</td><td>37</td><td>20%</td><td>Information</td></tr><tr><td>52</td><td>41</td><td>23%</td><td>Finance and Insurance</td></tr><tr><td>33</td><td>49</td><td>27%</td><td>Primary Metal Manufacturing</td></tr><tr><td>44</td><td>57</td><td>31%</td><td>Retail Trade</td></tr><tr><td>42</td><td>79</td><td>44%</td><td>Wholesale Trade</td></tr></table>

Note: the 181 companies did not split further in 6-way but did in 7-way

Table 3 and Table 4: 7-way clustering where the 181 companies split occurs into 81 and 100  
Table 3: Cluster 2 {81 companies} at 7-way split.

<table><tr><td>2 Digit NAICS</td><td>Number of Companies</td><td>% of Total</td><td>Names of Industry that 2 Digit NAICS represents</td></tr><tr><td>45</td><td>8</td><td>10%</td><td>Sporting Goods, Hobby, Books, and Music Stores</td></tr><tr><td>32</td><td>10</td><td>12%</td><td>Wood Product Manufacturing</td></tr><tr><td>55</td><td>12</td><td>15%</td><td>Management of Companies and Enterprises</td></tr><tr><td>31</td><td>14</td><td>17%</td><td>Manufacturing</td></tr><tr><td>44</td><td>17</td><td>21%</td><td>Retail Trade</td></tr><tr><td>51</td><td>19</td><td>23%</td><td>Information</td></tr><tr><td>33</td><td>20</td><td>25%</td><td>Primary Metal Manufacturing</td></tr><tr><td>52</td><td>23</td><td>28%</td><td>Finance and Insurance</td></tr><tr><td>42</td><td>30</td><td>37%</td><td>Wholesale Trade</td></tr></table>

Table 4: Cluster 2 {100 companies} at 7-way split.

<table><tr><td>2 Digit NAICS</td><td>Number of Companies</td><td>% of Total</td><td>Names of Industry that 2 Digit NAICS represents</td></tr><tr><td>32</td><td>13</td><td>13%</td><td>Wood Product Manufacturing</td></tr><tr><td>51</td><td>18</td><td>18%</td><td>Information</td></tr><tr><td>52</td><td>18</td><td>18%</td><td>Finance and Insurance</td></tr><tr><td>45</td><td>23</td><td>23%</td><td>Sporting Goods, Hobby, Books, and Music Stores</td></tr><tr><td>33</td><td>28</td><td>28%</td><td>Primary Metal Manufacturing</td></tr><tr><td>44</td><td>39</td><td>39%</td><td>Retail Trade</td></tr><tr><td>42</td><td>48</td><td>48%</td><td>Wholesale Trade</td></tr></table>

Note: the 81 companies did not split in 8-way and 9-way but did at 10-way

Table 5 and Table 6: 10 -way clustering where the 81 companies split. into 24 and 57 Table 5: Cluster 2 {24 Companies} at 10 way split.

<table><tr><td>2 Digit NAICS</td><td>Number of Companies</td><td>% of Total</td><td>Names of Industry that 2 Digit NAICS represents</td></tr><tr><td>22</td><td>4</td><td>17%</td><td>Utilities</td></tr><tr><td>32</td><td>4</td><td>17%</td><td>Wood Product Manufacturing</td></tr><tr><td>48</td><td>4</td><td>17%</td><td>Transportation and Warehousing</td></tr><tr><td>31</td><td>5</td><td>21%</td><td>Manufacturing</td></tr><tr><td>44</td><td>5</td><td>21%</td><td>Retail Trade</td></tr><tr><td>33</td><td>6</td><td>25%</td><td>Primary Metal Manufacturing</td></tr><tr><td>55</td><td>7</td><td>29%</td><td>Management of Companies and Enterprises</td></tr><tr><td>52</td><td>8</td><td>33%</td><td>Finance and Insurance</td></tr><tr><td>42</td><td>9</td><td>38%</td><td>Wholesale Trade</td></tr></table>

Table 6: Cluster 2 {57 Companies} at 10 way split.

<table><tr><td>2 Digit NAICS</td><td>Number of Companies</td><td>% of Total</td><td>Names of Industry that 2 Digit NAICS represents</td></tr><tr><td>45</td><td>6</td><td>11%</td><td>Sporting Goods, Hobby, Books, and Music Stores</td></tr><tr><td>32</td><td>7</td><td>12%</td><td>Wood Product Manufacturing</td></tr><tr><td>31</td><td>10</td><td>18%</td><td>Manufacturing</td></tr><tr><td>44</td><td>13</td><td>23%</td><td>Retail Trade</td></tr><tr><td>33</td><td>15</td><td>26%</td><td>Primary Metal Manufacturing</td></tr><tr><td>52</td><td>15</td><td>26%</td><td>Finance and Insurance</td></tr><tr><td>51</td><td>17</td><td>30%</td><td>Information</td></tr><tr><td>42</td><td>22</td><td>39%</td><td>Wholesale Trade</td></tr></table>
