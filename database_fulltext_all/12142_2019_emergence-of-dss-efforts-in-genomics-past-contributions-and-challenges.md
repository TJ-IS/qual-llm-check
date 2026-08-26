---
otero_id: 12142
otero_key: "QGTCE853"
title: "Emergence of DSS efforts in genomics: Past contributions and challenges"
authors: "Arun Sen; Ahmad Al Kawam; Aniruddha Datta"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

# Emergence of DSS efforts in genomics: Past contributions and challenges

Decision Support Systems

Arun Sen, Ahmad Al Kawam, Aniruddha Datta

![](/api/attachments/QGTCE853/fulltext/images/20814358411aeedad454b2dc38c60e0d995626df019c842c6f7a7de779d9228e.jpg)

PII: S0167-9236(18)30168-4

DOI: https://doi.org/10.1016/j.dss.2018.10.011

Reference: DECSUP 13003

To appear in: Decision Support Systems

Received date: 19 May 2018

Revised date: 17 October 2018

Accepted date: 19 October 2018

Please cite this article as: Arun Sen, Ahmad Al Kawam, Aniruddha Datta , Emergence of DSS efforts in genomics: Past contributions and challenges. Decsup (2018), https://doi.org/10.1016/j.dss.2018.10.011

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

Emergence of DSS Efforts in Genomics: Past Contributions and Challenges

Arun Sen<sup>1</sup>, Ahmad Al Kawam<sup>2</sup> and Aniruddha Datta<sup>3</sup>

## Abstract

Large amounts of data in biomedical research (from clinical data to gene expression data) are being generated. Use of these data sets and their associated knowledge are essential to understand the biological mechanisms behind diseases. While patients’ clinical data from EHR can help researchers accurately and appropriately trace the performance of various kinds of medicines on the patients, the microarray data for the same pool of patients can contain valuable information for discovery of disease-associated gene expression patterns and can help classify the patients. However, research in the area of integrating genomic data with clinical data is still in its infancy and is riddled with many challenges. Even though data and knowledge sets are easily available from genome sequences and protein structural data of organisms, they usually are of many different varieties. Integrating them for a better understanding of biological functions at all levels is complicated. If we want to obtain the full benefit of functional genomics, we need to find a seamless way to integrate large amounts of patient datasets with genomic datasets in the field of biomedicine. Few papers in the decision support systems (DSS) literature provide an overview of Genomic Clinical Decision Support (GCDS) challenges that span data, knowledge, input/output, and architecture/implementation. This paper presents a unique effort dedicated to providing a comprehensive listing and a concise description of the DSS methodological challenges that arise from integrating complex and massive-scale genomic data with Clinical Decision Support (CDS) systems.

Keywords: Genomics, Decision Support System, Clinical Decision Support, Data integration, Knowledge base integration, Decision support system architecture

## 1. Introduction

# ACCEPTED MANUSCRIPT

The term “decision support system” (DSS) was first coined by Gorry and Scott Morton [48] in 1971 to describe a system that supports users in unstructured decision-making situations. Bonczek et al. [14] in 1980 defined a DSS framework that includes three interacting components: (a) a user interface for communication with users, (b) a repository that manages problem domain knowledge and data, and (c) a problem processing component that contains problem-solving capabilities which works with the other two components. Even though DSS was created to support models for decision making and planning, most of the DSS activities to-date have focused on tools innovations. Figure 1 gives a glimpse of such tool advances ranging from relational data base systems to expert systems (e.g., DENDRAL [32], MYCIN [132] and INTERNIST [88, 89], Sen and Biswas [127]), statistical packages, web development and enterprise integration. Popular tools such as data warehouses, online analytical processing (OLAP), data mining and business intelligence (BI) were developed in the early 1990’s concentrating With the advent of Electronic Health Records (EHR) systems [24], clinicians are getting accustomed to a special kind of DSS called Clinical Decision Support (CDS). CDS is an effective tool for improving healthcare quality and cost-effectiveness while reducing medical errors [42]. By linking health observati with health knowledge, CDS systems produce evidence-based alerts and recommendations to influence diagnosis, medical procedures, and drug prescription medical data processing tasks to complex analytic tasks to support genetically guided cancer management, risk assessment with family history, and operation on a massive amount of clinical data [129].

The recent advancements in genomics have resulted in an elevated interest in developing genomic decision support systems for improving clinical care [16, 54, 70, and 73]. Many types of genomic data are currently available like sequencing data, gene expression data, genotype data, epigenetic data, etc. A list of some of these data types can be found in Bolser et al [13] and at http://research.omicsgroup.org/index.php/List\_of\_biological\_databases. Several efforts are underway to utilize these large data sets for clinical support. A few representative sample efforts are listed in Table 1.

Table 1: Examples of GCDS target applications [126]

<table><tr><td>GCDS Application</td><td>Definition</td><td>Sources</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>GCDS Application</td><td>Definition</td><td>Sources</td></tr><tr><td>Personalized Medicine</td><td>Gene-drug interactions are used to inform the clinician of the patient&#x27;s response to drug therapy. Alerts the clinician of dangerous gene-drug interactions</td><td>[111]</td></tr><tr><td>Risk Analysis</td><td>Uses the patient&#x27;s genetic information to assess the possibility of developing certain diseases. High risk triggers warnings and prompts increased screening, or avoiding agents.</td><td>[6, 12]</td></tr><tr><td>Diagnosis</td><td>Known genotype-phenotype relations are used to alert the clinician to disease causing variations and this increases diagnosis accuracy, and reduces diagnosis time.</td><td>[3, 11,1 8]</td></tr><tr><td>Newborn Screening</td><td>Genomic analysis is used to enable the early detection and intervention for a select group of conditions. This facilitates the prevention of developmental impairments, delayed physical growth, severe illness, and death.</td><td>[10, 154]</td></tr><tr><td>Somatic/Tumor Treatment</td><td>Knowledge about the mutations in the genetic makeup of tumor cells may have immediate therapeutic implications, which may alter cancer treatment choices.</td><td>[106, 137, 142]</td></tr></table>

Substantial barriers still exist in using genomic information for clinical care [17, 120]. These barriers include existence of multitude of genomic data sources, complexity of genomic analysis, continual growth in the genomic knowledge base, and rigid mechanisms in reporting genomic results [36, 87]. These barriers are compounded by limited physician proficiency in genomics [100], large number of genetic tests available (more than 2500), and lack of genetic professionals who can work with physicians to help assess genetic risk [125, 149].

## ACCEPTED MANUSCRIPT

![](/api/attachments/QGTCE853/fulltext/images/88d469131d09206124e5690d46275f13016a4fdd0693fb35eb417eed2d599727.jpg)  
Figure 1. The Evolution of GCDS and its Underlying Influences

# ACCEPTED MANUSCRIPT

To overcome these barriers, current interest has centered on creating CDS-like systems that could help clinicians understand, interpret, and use genomic information in clinical practices. As a result, efforts in the last 25 years were concentrated towards integrating clinical data with genomic data to develop Genomic Clinical Decision Support (GCDS) systems [46,136, 147] (see Figure 1). In order to advance research in GCDS, integration of genomic information into clinical decision support must be well understood. This paper focuses on presenting a systematic literature review of GCDS efforts to showcase research opportunities. The paper is organized as follows. Section 2 presents a systematic literature review methodology for GCDS. The results of the review are reported in Section 3. In Section 4, we discuss limitations of current GCDS research as seen in our review. We conclude our review in Section 5.

## 2. Method

This systematic literature review was carried out using ideas proposed in Kitchenham et al [71], Peleg [107], Mayvan et al. [85] and Hume et al [61]. The steps are documented as follows.

## 2.1. Research Questions

We propose three research questions (RQs) that we would like to answer with this review. They include:

RQ1 Can we create a classification scheme to review vast GCDS literature?

RQ2 Is there a right way to implement GCDS?

RQ3 What are the limitations of the current GCDS research?

RQ1. Can we create a classification scheme to review vast GCDS literature? GCDS literature is large and diverse. In order to review this varied literature, it is prudent to develop a classification scheme that provides a categorized and consolidated view of the GCDS literature. Following Peleg [107] and Hume et al [61], we apply the DSS framework originally proposed by Bonczek et al. [14,15] and later supported by Dos Santos and Holsapple [26], Pearson and Shim [105], Sen [128], Zhang and Goddard [155], Fogli and Guida [37] and Ferreti and Montibeller [34] to create a classification scheme. Such a scheme will cluster GCDS articles on the basis of something they have in common (i.e., they have shared properties). According to Bonczek et al [14], input/output component includes all facilities that are needed for a decision maker to describe information needs for the DSS and collect information produced by the DSS.

## ACCEPTED MANUSCRIPT

Typically an input/output component is characterized by messages using statements, commands or expressions that allow the decision maker to express his/her problem needs and interact with the DSS. A good deal of power of the DSS comes from the knowledgeability about the problem domain. This knowledge typically includes large volumes of data (needing a data management component) and pertinent knowledge of the problem domain (needing a knowledge management component). The main function of a DSS is to take input messages and use its data and problem knowledge to produce information that supports a decision process. To do this, we need a connection between the knowledge component, the data management component and the input/output component. This connection mechanism is called the problem-processing component (Bonczek et al [15]). It is obvious that depending on the input/output, data, and knowledge management components, the problem processing component will differ in complexity. We group the GCDS literature into four categories – one per DSS component. For example, the data management component of the DSS framework creates the GCDS data management category (see Section 3.1) and groups al CDS articles on genomic data management. Similarly, the knowledge management component creates the knowledge management category (see Section 3.2), the problem processing component creates the problem processing category (see Section 3.3) and finally the input/output component creates the user interface category (sec Section 3.4).

RQ2. Is there a right way to implement GCDS? The objective of any DSS project is to develop an architecture that is implementable. Such an architecture must support the problem processing component, its inter-connections with other DSS components along with coordination and control for integration. In the GCDS domain, large amount of biomedical data like clinical data, gene expression data and genotype data, are getting generated. Using these data sets and their associated knowledge, we want to understand the biological mechanisms behind diseases. However, each data type produced can only describe a certain biological level and therefore cannot solely be used to understand the larger biological context. Hence, integrating the different data types for a better understanding of biological functions at all levels is desired. If we want to obtain the full benefit of functional genomics, we need to find a way to integrate large amounts of patient datasets with genomic datasets. Such integration can be of many different types.

# ACCEPTED MANUSCRIPT

This research studies these integration mechanisms to figure out the ones that are right for a GCDS implementation. Details of such integrations starting from coordination among organizations to softwarebased, standard reports-based and finally service-oriented architectures are presented in Section 3.3.

RQ3. What are the limitations of the current GCDS research? Our review of the GCDS literature is limited due to the ever evolving nature of the GCDS research. This is partly due to the fast development in the underlying genomic research, its associated genomic data and genomic knowledge; along with fasto manage all these, newer and innovative architectures for GCDS are getting proposed. This review discusses these limitations and describes future research challenges in Section 4.

## 2.2 Search Process

We start off our review by collecting papers that deal with GCDS research for the last 25 years (ranging from 1992 to 2017). We do a systematic scan of online academic and conference databases in the healthcare and information systems domains. pture as many GCDS-type research articles as possible. As GCDS research sits at the intersection of healthcare and information system domains, we decided to look at both domains. Using fifteen years of experience in healthcare research, we chose OpenHelix, PubGet, and PubMed databases for collecting GCDS articles. The OpenHelix Search Portal provides a mechanism to search for, and evaluate, online bioscience resources by providing contextual displays of search results. PubGet’s search engine retrieves article citations and full text from resource databases like ArXiv, Karger, and American Society for Microbiology. PubMed comprises more than 28 million biomedical literature related citations from MEDLINE, life science journals, and online books. Using our thirty-year knowledge in the information systems domain, we chose standard databases like ABI/Inform, Google Scholar, ACM Digital and IEEE Xplore for GCDS articles. We then needed to come up with the right keywords or key phrases for the search. To collect the maximal sample of GCDS articles, we first chose the relatively wide key search phrase “decision support.” From Table 2, we found that the search results were quite large. To narrow down the search, we made the key search phrase more specific - “decision support system.” The results were a lot better but were still quite large. In our third iteration, we narrowed the search by using the search phrase “genomic decision support.” The result shown in Table 2, which we deemed manageable, was obtained. In order to be exhaustive, we also used a search phrase “genomic decision support system” in our fourth iteration. We noticed that search results narrowed considerably as now we only looked at papers that build GCDS systems. This was too narrow a perspective for our literature review. Hence, we settled for the key search phrase “genomic decision support” which seemed to be relevant while simultaneously giving us a maximal set of CDS papers. The PubGet, PubMed, ABI/Inform and IEEE Xplore portals together listed 3339 res articles for us to scan. OpenHelix was dropped as it yielded no documents with this key search phrase. Our initial scan of Google Scholar and ACM Digital portals returned a large percentage of the entries which were duplicates of the 3339 articles, along with numerous white papers and blogs. As a result, we decided to also drop these two portals.

Table 2. Number of documents for keywords in each search portal

<table><tr><td>Keyword</td><td>OpenHelix</td><td>PubGet</td><td>PubMed</td><td>ABI/Inform</td><td>Google Scholar</td><td>ACM Digital</td><td>IEEE Xplore</td></tr><tr><td>decision support</td><td>1,290</td><td>39,230</td><td>117,772</td><td>131,284</td><td>1,580,000</td><td>90,154</td><td>46,726</td></tr><tr><td>decision support system</td><td>23</td><td>12,265</td><td>20,087</td><td>41,747</td><td>448,000</td><td>316,682</td><td>40,515</td></tr><tr><td>genomic decision support</td><td>0</td><td>181</td><td>2,881</td><td>167</td><td>270,000</td><td>91,388</td><td>110</td></tr><tr><td>genomic decision support system</td><td>0</td><td>34</td><td>412</td><td>67</td><td>215000</td><td>317172</td><td>82</td></tr></table>

Furthermore, we found that all documents from PubGet, ABI/Inform and IEEE Xplore were observed that these documents came from a large number of different journals and no single journal by itself had a significant number of documents. PubMed search is also quite exhaustive as it not only searches independently and jointly all keywords given in the key phrase , but it also enhances the search string by adding matched MeSH (Medical Subject Headings) terms and others that are underneath these terms. This is referred to as exploding the term.

## 2.3. Inclusion and Exclusion Criteria

Starting with 2881 articles in PubMed, we used two inclusion criteria and two exclusion criteria to further narrow down the list. The inclusion criteria are: (a) the research must study GCDS as an information systems tool; and (b) the research must focus on genomic decision support as its primary motivation.

# ACCEPTED MANUSCRIPT

These two inclusion criteria highlight the articles to be retained in the list. The exclusion criteria are: (a) articles that do not meet the inclusion criteria should be excluded from the list; and (b) articles that have keywords that directly or indirectly point to topics that are not genomic decision support should be excluded from the list. The two exclusion criteria focus on the articles to be removed from the list.

## 2.4. Data Collection

The above inclusion and exclusion criteria were used to do the title level review of the articles in the list. Any paper that did not deal directly with genomic decision support was removed from the list. Papers with titles that have words like “nursing”, “financial”, “ethical” and many others that are not in our purview were removed from the list. We also removed papers whose titles directly or indirectly point to topics that are not genomic decision support. This produced 138 documents. We then performed an d at the abstract and the entire content of the articles. Once again we used the above four criteria to do the analysis. If the paper did not satisfy the inclusion criteria and conforms to the exclusion criteria, it got removed from the list. Example keywords include: “genomic data,” “genomic knowledge,” “understanding genes,” “data integration”, “framework,” “EHR data,” “algorithm” and so on. This iteration reduced the number of documents in the list to 75. Finally, guided by the core GCDS concepts discussed in the above 75 papers, we performed a second search of PubMed. Our search this time was much more focused with core concepts like “development of a framework,” “development of an algorithm,” “development of conceptual data model,” “development of data mining model,” “development of tools integration,” “development of computational tools” “development of visualization tool” and so on. We used these as key phrases along with “genomic decision support” in our search terms for PubMed. Once again, the output list included many irrelevant articles. We removed them from the new list as before. This step produced 60 additional documents that are directly related to one or more GCDS concepts. Thus, the total number of documents to review increased to 135.

## 2.5. Data Analysis

Our initial observation of 135<sup>4</sup> papers shows that the articles cover many issues spanning from metadata management to tools integration. We analyze these documents based on our DSS-framework centered categorization scheme (see Section 2.1) to form groups of documents that will streamline the review process.

## 3. Results

This section summarizes the results of our study. Based on our classification scheme, we group the 135

## 3.1. Genomic Data Management Category

In this section we refer to genomic data as the collection of data generated from the human genome. Genomic data comprises all types of data that are used to capture the variations in the human , and epigenetic data. Genomic data for each patient is produced using a genetic sequencing or microarray technology. Then, the raw genomic data is processed to identify the patient’s important variations. The important variations identified are forwarded to the detailed analysis and interpretation processes. These rely on genomic data stored in resources such as dbSNP [130], OMIM [52], dbGaP [79], ClinVar [74] and many others. During this process, variations are compared with similar variations reported in the literature, and are assessed for their ability to produce phenotypic changes. For example, it was found that women having multiple variations in the BRCA1 and BRCA2 [6] genes have an increased risk (40%-80%) of breast cancer [108]. The analysis procedures and interpretations fall under the knowledge management category (see Section 3.2). Genomic data describing the genome, its components, and their functions is expanding rapidly in size and content. This presents numerous data management options to properly represent, store, update, and grant access to the required information. Storing a massive amount of annotated variant data directly into an EHR system would substantially increase the computational and storage loads on that system. Burdening the system will introduce access latencies, which would have a negative impact on usability.

# ACCEPTED MANUSCRIPT

Consequently, this data needs to be stored outside the EHR system. Hence, choosing the best form for genomic data storage is an important issue. From Figure 2, we see that efforts to support genomic data storage and management have charted mostly an on-line data processing (OLTP) path. OLTP applications typically focus on transactions that are detailed and use up-to-date data. In this method, we find research has concentrated on two approaches: repository technologies and database technologies. We provide a brief review of some representative work in these areas.

Repository Technology Approaches. One way to manage the large genomic data set is by using repository technology. A repository is typically built to share data and is an application layer on top of a file system. Usually a repository system comes with many tools like web user interface, version control, configuration control, check-in/checkout and others. As shown in Figure 2, repository technology has been extensively used since the mid-nineties to manage genomic data. Example repositories include the Short Read Archive (SRA -- https://www.ncbi.nlm.nih.gov/sra), Gene Expression Omnibus (GEO -- https://www.ncbi.nlm.nih.gov/geo/), the 1000 genomes (http://www.internationalgenome.org/), ClinGen (https://www.clinicalgenome.org/about/), OMIM (Online Mendelian Inheritance in Man) [52], KEGG (Kyoto Encyclopedia of Genes and Genomes) [67] , ENCODE (ENCyclopedia Of DNA Elements) [138], dbSNP [130], and SPHINX [114]. SRA stores next generation sequencing data from tores gene expression data. The 1000 genomes portal stores sequences and genotypes for deeply sequenced individuals from different populations around the world. In addition, several knowledge bases use the repository approach to manage the genomic data they store. The OMIM repository is managed by the US National Center for Biotechnology Information (NCBI) offering continuously updated repository of single gene disorders, catalog of human genes and complex disease information with significant single gene contribution. The content of OMIM is based on selection and curation of published peer-reviewed biomedical work. OMIM search results can point to some disease codes like ICD9 and SNOWMED. The KEGG repository integrates genomic, chemical and systematic functional information. The ENCODE repository contains a multitude of data like gene annotations, RNA transcripts, Chromatin structures and modification and many others. The dbSNP is

# ACCEPTED MANUSCRIPT

created to store genomic information extracted from association studies, genetic cartography and evolution biology. The eMERGE-PGx project stores genomic variants in a secure, de-identified, webaccessible repository called SPHINX.

Data Base Technology Approaches. Many genomic informatics projects, like GIMS [23], Gene Ontology-GO [43], TRANSFAC [84], and Ensembl Variant database [86], are underway that use oriented data base using the FastObjects tool and stores the Saccharomyces cerevisiae yeast genome, the GO database is a relational database comprising GO ontologies as well as the annotations of genes and gene products to terms in those ontologies. Housing both the ontologies and the annotations in a single database allows powerful queries of the annotations using the ontology. The TRANSFAC uses Raima Data Manager and Ensembl uses MySQL as the database management system.

## 3.2. Genomic Knowledge Base Management Category

Genomic knowledge is essentially “interpretations of genomic data.” Each type of genomic data (raw, processed/normalized, analyzed and summarized) has its own set of interpretations. These interpretations could be semantic or analytical. We call interpretations semantic if they point to biological insights into of individuals with the variant, number of occurrences, affected females with the variant, age, ethnicity, methods of data capture, family structure, primary data or meta-analysis, submitters, etc.) to complicated genetic (like experimental evidence demonstrating the functional consequence of clinically relevant variants, risks, allele summary, phenotypes, etc.) and clinical interpretations (like clinical significance, mode of inheritance, risk or predisposition, etc.). As currently there is no standard way to express these interpretations, storing and managing them in a knowledge base is challenging. Traditionally, semantic interpretations are captured as metadata, rules, and ontologies. Metadata could be in free form or could be written in a mark-up language such as XML. Rules are compiled from interpretations using established literature from experts or using extensive data analytics work. Ontologies have been used to store genomic interpretations like formal naming and definition of types, properties, and interrelationships of the entities that exist in the genomic domain using classification hierarchy.

Analytical interpretations, on the other hand, can be derived by creating analytical/computational models of genomics data. They are usually curated for different alleles (say) with some level of confidence by experts and can be arranged in hierarchies where each level could have different curation status. Genomic knowledge needs to be transformed into a standard set of interpretations to help trigger alerts and notifications [95]. In a typical CDS system, rules usually follow Arden, GLIF, GELLO, and HL7 standards. Originally, these standards were developed to encode EHR-based rules. To enable them to be used in GCDS, they may need to be extended. We now describe several research methodologies related to genomic knowledge/interpretation.

Metadata Management Approaches. One way to represent semantic interpretations is by using texts. Texts can simply be in free-form with <attribute, value> pairs. ClinVar [74] and others use this style to store study elements, observations, risk information, molecular consequences and others. Interpretations can also be represented using a markup language like XML. Generally, these interpretations are stored in text files or in XML files.

Rule Management Approaches. Finally, a third way to describe semantic interpretations is by developing rules that GCDS needs to manage. An early version of this approach can be seen in GRAIDS (Genetic Risk Assessment in an Intranet and Decision Support) system [29] where referral guidelines were used as rules. Expert systems [31, 140] have also been developed to utilize rules. Most fields of clinical genomics research have not yet reached a level of maturity to produce such rules. Nonetheless, pharmacogenomics is one field that has proven that genotype-phenotype rules could be used in GCDS. Several research groups such as the Clinical Pharmacogenetics Implementation Consortium (CPIC) [152], Pharmacogenomics Knowledgebase (https://www.pharmgkb.org/), the Royal Dutch Association for the Advancement of Pharmacy (DPWG) [135], and the Canadian Pharmacogenomics Network for Drug Safety (CPNDS) [121] have set guidelines

## ACCEPTED MANUSCRIPT

![](/api/attachments/QGTCE853/fulltext/images/ed92b527b280397ad37bec67a636a89548fe824c7f93e3706517b445402fc701.jpg)  
Figure 2. The Evolution of GCDS Capabilities with respect to Genomic Research

for modifying the prescription dosage of certain pharmacogenetics drugs according to the patient’s genetic profile. Examples of such rules are presented in Table 3.

Table 3. Examples of GCDS knowledge base rules and the resulting recommendations

<table><tr><td>Source</td><td>Rule</td><td>Recommendation</td></tr><tr><td>Pharmacogenomics Rules concerning the substance azathioprine.Source: Clinical Pharmacogenetics Implementation Consortium (CPIC)</td><td>Has one allele as TPMT*1 and has the other allele as either TPMT*2 or TPMT*3A or TPMT*3B or TPMT*3C or TPMT*4</td><td>Consider starting at 30-70% of target dose (e.g., 1–1.5 mg/kg/d), and titrate based on tolerance. Allow 2–4 weeks to reach steady state after each dose adjustment.</td></tr><tr><td>Pharmacogenomics Rules concerning the substance azathioprine.Source: Clinical Pharmacogenetics Implementation Consortium (CPIC)</td><td>Has one allele as TPMT*1 and has the other allele as either TPMT*2 or TPMT*3 or TPMT*4 or TPMT*5 or TPMT*6 or TPMT*7 or TPMT*8 or TPMT*9 or TPMT*10 or TPMT*11 or TPMT*12 or TPMT*13 or TPMT*14 or TPMT*15 or TPMT*16 or TPMT*17 or TPMT*18</td><td>Select alternative drug or reduce dose by 50%. Increase dose in response to hematologic monitoring and efficacy.</td></tr><tr><td>Pharmacogenomics Rules concerning the substance azathioprine abacavir:Source: Dutch Pharmacogenetics Working Group (DPWG)</td><td>Has the allele HLA-B*57:01</td><td>An alternate to abacavir should be selected</td></tr><tr><td>Pharmacogenomics Rules concerning the substance azathioprine allopurinol:Source: 2012 American College of Rheumatology Guidelines</td><td>Has the allele HLA-B*5801</td><td>If patient of Korean descent with stage 3 or worse CKD, or of Han Chinese or Thai extraction irrespective of renal function it is recommended to be prescribed an alternative to allopurinol</td></tr></table>

Ontology Management Approaches. A second way to store semantic interpretations is by creating ontologies. Ontologies are generally used if interpretations need to be shared among people, to make analyze domain knowledge. Several ontologies have been created to date ranging from storing biomedical terminologies like in Unified Medical Language System (UMLS) and in Open Biomedical Ontologies [90] to storing biomedical knowledge like in Cell Ontology [90], National Cancer Institute (NCI) Thesaurus [90], Gene Ontology [126], and GWAS Catalog [4, 91]. The Cell Ontology is designed as a structured controlled vocabulary for cell types (http://www.obofoundry.org/ontology/cl.html). This ontology is not organism-specific and covers cell types from microscopic single-celled organisms to mammals. NCI Thesaurus covers vocabulary for clinical care, translational and basic research, along with public information and administrative activities. The Gene Ontology project has developed ontologies that describe gene products. According to its web site

# ACCEPTED MANUSCRIPT

(http://geneontology.org/page/documentation), it describes three structured ontologies that define gene products in terms of their associated biological processes, cellular components and molecular functions in a species-independent manner. The GWAS Catalog (https://www.ebi.ac.uk/gwas/docs/about) was created by the US National Human Genome Research Institute (NHGRI) [93] and the European Bioinformatics Institute (EMBL-EBI). The objective of the catalog was to store a manually curated, literature-derived collection of all published genome-wide association studies assaying at least 100,000 SNPs and all SNPtrait associations. Some repositories like OMIM, KEGG, dbGAP etc. also use the classification aspects of ontology. Ontologies in GCDS need tools to facilitate ontology management activities like creation and maintenance of ontologies [82]; creating annotation of gene products (as part of Gene Ontology); integrating ontology-based data for prostate cancer [90]; and developing recommendation engines for pharmacogenomics guidance to point-of-care [91]. Samwald et al [124] developed web-based ontologies and their semantic reasoning mechanisms to represent, analyze and use pharmacogenomics data.

Predictive Analytics Approaches. Predictive analytics to support analytical interpretations has been around since the early days of genomics. Small GCDS tools have been created using specialized statistical tools like TreeAge Pro 2013 [65], a logistic regression model [33], quantitative decision aids like Adjuvant Online and PREDICT [57, 97], a Bayesian approach [8,9] and Markov modeling [83, 143]. Since its inception, data mining has played an important role in developing classifiers and helping in predictions in genomics research. In the last 10 years, the PubMed website lists the publication of 7787 articles that have used data mining. The problems that have been addressed using data mining techniques range from creating classifiers for cancer by monitoring gene expressions [46] to molecular classification of cancer [134] and genomic pathway modeling [76]. Recently, data mining has also been used in classifying DNA repair genes [40], pathway extraction and reasoning [40, 97], gene prioritization and gene function prediction [47, 104], and precision medicine and drug repositioning [22, 47].

## 3.3. GCDS Problem Processing Category

A problem processing component in GCDS tries to recognize and solve problems during the making of a decision. Once the problem processing component has been requested to process a particular input from

# ACCEPTED MANUSCRIPT

the user, it selects some portion of data and knowledge from its store, and acquires additional knowledge from the user to produce some new knowledge. The processing can change the data held in the database component or can change the knowledge held in the knowledge base component of the GCDS. According to Holsapple [59], a problem processing system has two kinds of abilities: first-order abilities and second-order abilities. The first-order abilities include acquisition, assimilation, selection and generation of knowledge and data. These problem processing abilities have been reviewed extensively while discussing genomic data management (in Section 3.1) and genomic knowledge management (in Section 3.2). The second-order abilities include coordination and control of the first-order abilities. Coordination refers to the problem processing ability of GCDS to arrange knowledge and data flows across GCDS tasks, while control refers to the ability to ensure quality of the processing inside GCDS. Traditionally in the DSS literature these two abilities are managed by communication among participating systems within the DSS. Power [112] emphasizes that communications-driven DSSs use network and communications technologies to assist decision-relevant ollaboration and communication. In these systems, communication technologies are the principal architectural component.

The American College of Medical Genetics and Genomics (ACMG) in a recent position statement [1] states:

The considerable variation in clinical presentation and molecular etiology of genetic disorders, coupled with their relative individual rarity, makes it clear that no single provider, laboratory, medical center, state, or even individual country will typically possess sufficient knowledge to deliver the best care for patients in need of care ... To ensure that our patients receive the most informed care possible, the American College of Medical Genetics and Genomics advocates for extensive sharing of laboratory and clinical data from individuals who have undergone genomic testing. Information that underpins health-care service delivery should be treated neither as intellectual property nor as a trade secret when other patients may benefit from the knowledge being widely available. (p.1)

The above statement focuses our attention on sharing genomic data and genomic knowledge with clinical information gleaned from the EHRs. As we saw in Sections 3.1 and 3.2, sharing of genomic data and knowledge is complicated as they are diverse and stored in many websites and laboratories with many different formats and styles. Comprehensive sharing of genomic data and knowledge with clinical data requires integration of these resources. Interestingly, in the DSS literature, integration of underlying DSS

# ACCEPTED MANUSCRIPT

technologies is the target of all DSS efforts (see Figure 1). ACMG [1] states that: [in order] to accomplish these goals, and to ensure that the tremendous amounts of information now being generated are not wasted, our community must both demonstrate the will to share data broadly and develop the mechanisms [integrations] to do so easily. (p.2 [1])

The GCDS domain has modeled this kind of integration at the software level and also at the organizational level. In the rest of this section, we describe how the GCDS problem processing component deals with integration of genomic data (A), genomic knowledge bases (B) and clinical data from EHR (C). Such integrations include: Multi-genomics data integration (AA), Multi-genomics knowledge integration (BB), Genomic data-Genomic knowledge integration (AB), and Genomic-Clinical integration (ABC). We treat other integration options like AC and BC as subsets of ABC.

Multi-Genomics Data Integration (AA) Approaches. Multiple types of genomic datasets are available such as sequencing data, RNA sequencing data, ChIP-Seq data, genotype data, and numerous types of microarray data. There also exist disease-specific genetic databases where all genomic data related to a specific disease reside. As biological data pose many challenges starting from widely varying formats, common shared identities and names, shared semantics, shared and common access mechanisms to data inconsistencies due to experimental data variations [45, 132], successful data integration of biological data storages is important for successful GCDS research [78]. In order to do comparative analysis, a number of generic frameworks have been developed to facilitate the integration of genomics data from multiple sources. They include conceptual modeling to create integrated schema [12, 55]; database federation like in BioKleisli [19] where underlying databases remain autonomous and distributed throughout the network; web services for data integration [68, 153]; and biology-specific application programming interfaces (API) like BioPerl [133] and Bio\* projects including BioJava [60], BioRuby [49], and Biopython [21]. Recently some data warehouse frameworks have also been proposed like BioMart, Intermine and PathwayTools [139]. BioMart provides a unified user interface to various data sources that are distributed worldwide. It uses a star-schema like data model called reversed star for its data warehouse. InterMine is an open-source framework and has a user-friendly web user interface. It uses a traditional ETL (Extract, Transform and Load) architecture and provides a core data model and a collection of parsers to load data from many data sources like Gene Ontology, KEGG and Protein Data Bank. PathwayTools integrates various genomics data types, from genomes to metabolic pathways. It uses many tools for predictive capabilities and visualizations.

Multi-Genomics Knowledge Integration (BB) Approaches. In this approach, research supports challenges, there are no clear guidelines to combine interpretations from different knowledge bases stored in different repositories and databases to understand and treat complex diseases and genetic disorders. Currently most of the integration is carried out manually [70, 110, 116]. Recently, data mining approaches have been proposed to extract and integrate interpretations from multiple knowledge bases [77, 156].

Genomic Data-Genomic Knowledge Integration (AB) Approaches. In this approach, we assume that the integration is between a genomic data base with its associated genomic knowledge base of interpretations. Many existing projects like OMIM [52, 103], KEGG [66], ENCODE [138], dbSNP [130], SPHINX [114], dbGAP [79] and ClinVar [69] have all used this integration approach. The knowledge base is typically stored in a text file or in an XML-file. The data is accessed via a web user interface. Due to the nature of this integration, the coupling for integration between the two components is strong. We see evidences of this type of integration in Sections 3.1 and 3.2.

Genomics-Clinical Integration (ABC) Approaches. In this approach, research focuses on integration of genomic data and genomic knowledge/interpretation sources with clinical data from the EHR [75]. This integration approach is not unique in GCDS and has been seen in DSS and in CDS research [129]. Unlike AA, BB, and AB integration approaches, coordination and control are more complicated in this category of approaches. The GCDS literature has utilized communication-driven DSS framework in its implementation of coordination and control. They include: organization-based, software-based, standards-based and service-based.

# ACCEPTED MANUSCRIPT

(a) Organization-based coordination. In this type of GCDS coordination, the objective is to create a group of research laboratories/universities (a community) to collaborate so as to collectively create a GCDS framework for the community. It is important to point out that this type of organization-based coordination is quite unique to GCDS. We do not see this kind of coordination in the DSS applications as the integration there focuses only on participating components. Among many efforts [41, 58, 64, 80] that are under way, eMERGE (electronic MEdical Records and GEnomics) project [98] CSER Clinical Sequencing Exploratory Research project [50], and IGNITE project [147] are the mo omprehensive. The eMERGE network was formed in 2007 as a consortium of 5 US institu ns: Marshfield, Northwestern, Mayo, Group Health Seattle, and Vanderbilt. It was later expanded to 20 relevant groups. The eMERGE network has multiple objectives that include use of EHR data for electronic phenotyping, conducting genome-wide association studies using the phenotypes, return of results, integrating findings into EHR, and many others. The CSER (Clinical Sequencing Exploratory Research [7]) network was formed in 2011 and includes a group of six projects funded by the US National Human Genome Research Institute and the US National Cancer Institute. CSER examines the impact of genome-scale testing in diverse clinical settings. The CSER is a collaboration of six US institutions: Baylor College of Medicine (BCM), Brigham and Women’s Hospital/Harvard Medical School (BWH/HMS), Children’s Hospital of Philadelphia (CHOP), Dana-Faber Cancer Institute and University of North Carolina at Chapel Hill. The CSER network is built around the idea that the optimal GCDS for genomic data would consist of a combination of both active and passive components [147]. The active GCDS component would provide alerts to the clinician whereas the passive GCDS would provide more information to the clinician through a PDF file compiled at a genomics lab. The IGNITE network [153] was formed in 2013 with six initial sites: Duke University, Icahn School of Medicine at Mount Sinai, Indiana University, University of Florida, University of Maryland and Vanderbilt University. This project sets to achieve several goals related to utilizing genomic analysis in clinical settings such as expansion and linking of genomic medicine implementation efforts, development of new collaborative projects and methods for genomic

# ACCEPTED MANUSCRIPT

medicine implementation in diverse settings and populations, contributing to the evidence base of outcomes following the use of genomic information for clinical care, and others.

(b) Software-based coordination. The outcome of a genomic analysis process is typically in the form of a free-text report, similar to a pathology report, written by a genomics specialist. This report describes the patient’s genetic profile, indicating information such as the presence of certain variations of interest or the expression levels of important gene isoforms. The report might also contain an analysis of how the patient’s genetic makeup could be contributing to the development of the patient’s dise The objective of the software-based coordination approach for integration is to develop a machi able format of such a report that can be shared among multiple components of GCDS. Software-based coordination about proprietary intricacies of the EHR system. Efforts have been made in the GCDS literature to optimize vendor-provided CDS using customized advanced passive and active decision support [5], and using data warehousing technology to strongly couple genomic data and knowledge with clinical data by developing OLAP-based schema. For example, BioStar [144] utilizes a star schema to integrate genomic databases; while BioStar+ [28] and Paliulis et al [101] utilize a hybrid mechanism that connects independent schemas of clinical data, medication data, gene data, experiment data, and microarray data for integration. Huser et al [62] uses HealthFlow system that implements a process-oriented workflow management. Ardent syntax-based DSS has also been proposed as an integration mechanism for GCDS [123]. A case based fuzzy cognitive map technique has been used to model medical knowledge contained in clinical proactive guidelines and to identify cognitive relationships through a process resembling human reasoning as closely as possible [27]. The objective of the PG4KDS [58] protocol is to institute processes for using pharmacogenetics tests in the EHR records to pre-emptively guide prescribing. Once the genotyping for 230 genes is done, the test results are summarized to a gene-specific diplotype translation report and sent to St. Jude via secure file transfer and stored in databases and then posted in St. Jude’s EHR to be used by its internal CDS. In the 1200 Patients Project [96] a custom Genomic Prescribing System (GPS) [25] has been used which incorporates clinically actionable genomic data into

# ACCEPTED MANUSCRIPT

the EHR. The tool utilizes a star-schema based research warehouse to store PGx literature information for annotation of the genomic results obtained from the genotyping lab. The annotation information is modeled by the star schema with dimension tables like drug, gene, variant, PubMed information and correlation and fact tables with surrogate keys and attributes like control sample size, case sample size, primary disease, age group and others. Although the GPS tool has been created to run independently, it has been integrated with the University of Chicago Medical Hospital’s EPIC EHR system. Data analytics [111] has also been used to study cancer recurrence showing the benefits of software-based coordination architecture in GCDS.

(c) Standard- report based coordination. A third way to coordinate between GCDS components is to create standard reports to be shared. Currently, there is a severe lack of standards for representing genomic analysis outcomes in machine-readable formats. Due to the numerous analysis decisions and the wide variety of analysis outcomes, converging to comprehensive standards for genomic analysis outcome representation is arguably one of the most difficult problems in GCDS [117]. Furthermore, the outcomes should be able to capture information about the analysis process, which includes information about the sequencing process, type of workflow applied, tools used, tool versions, along with other forms of metadata. This information is vital for accounting for the systematic errors and to later enable proper updating of the outcomes. API-based interfaces have been offered by GenoSpace, LLC, Seven Bridges genomics, Inc. and Global Alliance for Genomics and Health (GA4GH) [2]. GA4GH utilizes SMART platform on FHIR to combine clinical data from an EHR system with genomics data from sequencing systems, all via SMART-standardized API calls [146].

(d) Service-based coordination. A fourth way to implement integration between GCDS components and the clinical data is though service-based architecture. Welch et al [151] suggests that because of the huge number of disparate health IT systems, the application of service oriented architecture (SOA) offers several benefits to healthcare. In SOA architecture, each GCDS component acts as a service for genomic decision support. It requires the development of interfaces between the EHR and the GCDS which poses data representation challenges. It also requires the development of coordination mechanisms to manage

# ACCEPTED MANUSCRIPT

running of different GCDS components. Service architecture can provide the agility and scalability needed to keep up with the rapidly evolving genomic data and knowledge bases [150]. Several researchers have attempted to use this approach. Kawamoto et al [69] developed the SEBASTIAN architecture that has been implemented as a Web service. It encapsulates knowledge about data access, data processing and data reporting using standards-based XML messages and has been used in multiple decision support environments. Iavindrasana et al. [63] and Rajasekaran et al. [113] have developed a three-level SOA-based GCDS architecture that supports applications and services to help research and clinical treatment of aneurysms. Picone et al [109] also describes a service-oriented architecture called NeoMark where most of the interactions are done via web user interfaces. Welch et al [150, 151] use an SOA approach to develop WGS-guided CDS within the clinical workflow and within the EHR. Using workflow engine paradigm [102, 141] and SOA architecture, GCDS has also been conceived by Renci Consortium [116]. Reily et al [115] describe MaPSeq as an open source, plugin-based SOA solution that delivers modifiable services to make opportunistic use of multiple institutional and cloud-based computer resources to efficiently complete steps involved in the analysis of large-scale, genomic sequencing data.

## 3.4. GCDS User Interface Management Category

Design of user interface for a GCDS is important. A GCDS user interface can be of two kinds: text-based or graphics-based. Just as in DSS (Holsapple, 2008), the user interface typically manages inputs to and outputs from GCDS. With the advent of many visual tools and web applications, the input and output technologies have advanced from simple data queries to sophisticated report generation using business intelligence techniques and visualizations. The methodologies range from simple query-based retrievals to reporting (like simple reports, web-based reports, and business-intelligence-based reports) and sophisticated visualizations. These are described next.

Query-based Retrieval Approaches. The retrievals in GCDS include queries that provide results written in textual form or in codified textual form. Query retrievals are generally web-based in GCDS. Examples include use of SPARQL (a query language for RDF http://www.w3.org/TR/rdf-sparql-query) in Prostrate Cancer Information System (PCIS) [90]; or use of query development support via API-based protocol as in SMART (Substitutable Medical Applications & Reusable Technologies) on FHIR (Fast Healthcare Interoperability Resource) standard [2].

Reporting Approaches. The user interface can support reports created by a query. Example reports can be seen in query interfaces found in ClinVar [74]; web user interfaces found in Medicine Safety Code (MSC) [91] system, in GeneInsight Clinic software [94] and in Melanoma Rapid Learning Utility (MRLU) system [35, 145]; and user interfaces found in NCGENES project [30]. Many types of business intelligence (BI) interfaces are also in use starting from standard data warehouse query interface [28] to typical EHR user interfaces [118]. For example, Mayo Clinic [20] uses standard business intelligence reporting mechanisms.

Visualization Approaches. Visualization of genomic data is the third approach to disseminate genomic used to display data as a part of the reporting mechanisms for users. Flexible and interactive visualization tools enable scientists to explore the genomic data without knowing what patterns to expect and without doing any statistical and analytical work with the data. In the early days of genomics research, the visualization tools were created to target a specific task like annotating sequence data in Genotator [53], supporting clinical genetic counseling [44]. Recent visualization efforts, on the other hand, are more broadly focused. Geneways [122] which extracts abstracts of articles pertinent to molecular biology, analyzes interactions between molecular substances and visualizes the molecular networks. Genoviz [56] provides a mechanism for incorporating adaptive and dynamic zooming to allow rapid navigation and exploration of genome-scale data sets covering from chromosomes to genes to individual base pairs. Integrative Genomics Viewer [119] supports intuitive real-time exploration of diverse, large-scale genomic data sets ranging from aligned sequence reads, mutations, copy number, RNA interference screens, gene expression, methylation and genomic annotations. CASCADE [131] is an RNA-sequence visualization tool for cancer genomics and SMART Genomics Advisor on the SMART platform [99]. Finally, visualization efforts have progressed into the development of portals like cBioPortal (http://www.cbioportal.org/) and others [72] and browsers [105, 38].

## 4. Limitations of Current GCDS Research

With respect to the research question RQ3 posed in Section 2, we find that even though a large body of literature (as described in Section 3) currently exists in GCDS, there are still many research opportunities [39]. We next describe these limitations as research challenges.

Research Challenges in Data Management. According to Ostell [92], even though it seems like a question in terms of biology, experimental data, the current state of knowledge, and the use to which a particular scientist may wish to put the data. Genomic data (that tend to be raw, processed, interpreted, or in a summarized form) need to be managed. The following concerns are still the biggest challenges in genomic data management methodology.

(a) Standard representation of genomic data. It is still unclear how to correctly represent the genomic data as there are various types of genomic data currently in existence. There is no standard taxonomy of should store for GCDS.

(b) Need to focus on metadata. For any database, this is an important topic. Genomic data comes with a large amount of metadata. These include names of technologies that create the genomic data, algorithms pipeline and reference data. All of these are usually a part of the genomic data set so that the experiment can be reproduced. Even though we have treated metadata as a part of interpretations in Section 3, it is also important for genomic data management as it helps the data integration process. Many issues remain in metadata management. For example, what kind of metadata is needed? What is the metadata acquisition process? Can the acquisition process be standardized? How can metadata be used for genomic data integration (see Section 2)? Should we standardize the metadata or should we use the common meta-model technology (http://www.omg.org/spec/CWM/) to do metadata translation?

(c) Storage of genomic data. Storage of genomic data is very important. We need to know if we want to store genomic sequence, reads, SNPs, or variants or all of them. Even though there are many different

# ACCEPTED MANUSCRIPT

ways to store data, we need to start moving toward relational databases to store data. Currently, it is unclear how to model all genomic data as relations. Storage of genomic data can be improved by data compression. However, as discussed by Masys et al. [81], genomic data compression remains a big problem in the genomic data management area. Efforts are needed to figure out how to create compressed genomic sequences so that storage can be managed.

Research Challenges in Knowledge Management. In order to understand what lies ahead in genomic knowledge management, we need to understand what defines knowledge management. In the genomics field, knowledge management simply includes interpretations as knowledge and a knowledge base to store them. Although it might be beneficial to store all of our acquired genomic knowledge in a centralized knowledge base, in reality this knowledge is spread out in a multitude of archives across the web. The dispersion of genomic knowledge poses retrieval challenges for GCDS. Similar to genomic data representation, genomic knowledge/interpretations also lack standardized representation. Thus, currently GCDS systems may need data retrieval protocols specific to each repository or database, according to its representation. We see the following issues that need more study.

(a) Standard representation of interpretations. Currently interpretations are represented by different genomic sources like ClinVar, Ensembl, dbGaP, and OMIM and are unique to the sources. This creates problems when attempting to access the knowledge stored in the knowledge base. We see two ways to solve this. The first approach is to create global knowledge schema standardization and the second is to develop a common interpretation meta-model. In the global knowledge schema standardization, a standard model for representation of interpretations needs to be created and all genomic data sources need to follow it for their internal representation of interpretations. The second approach is to create a common interpretation meta-model for translation along the lines of the common warehouse meta-model (CWM) in the data warehousing domain (http://www.omg.org/spec/CWM/). The objective of this approach is to let the genomic data sources have their own specific internal representations of interpretations, but if accessed, interpretations need to be translated to a representation espoused by the common interpretation meta-model. The receiving GCDS can then translate the interpretations to its inner representation, if needed.

(b) Knowledge base management. Not much has been said in the GCDS literature about knowledge base management. We define a knowledge base as a machine-readable resource for the dissemination of information (in our case interpretations) stored in it. Many issues typical in knowledge base management are discussed below.

Representation of interpretations. It is unclear how interpretations will be represented in a knowledge base. What language will be good for defining them? Will it be based on rules, ontologies, metadata, or frames (as in the semantic web https://www.obitko.com/tutorials/ontologies-semantic-web/frame-based-models.html) or all of them?

Hierarchy of interpretations. A large number of interpretations needs to be managed by developing interpretation hierarchies. How do we create such a hierarchy? As GCDS navigates through the hierarchies for its inferencing, how do we provide certainty factors with each interpretation? How do we develop these certainty factors?

Storage of interpretations in a knowledge base. As interpretations can be arranged in hierarchies, how can we store atomic interpretations with the curated ones? One can have variant interpretation, clinical interpretation, and actionability interpretation (identification of those human genes that, when significantly altered, confer a high risk for a serious disease https://clinicalgenome.org/working-groups/actionability/). We could adopt a solution from the data warehousing domain and develop storage separately for atomic and curated interpretations. Techniques such as roll up and drill down are needed to traverse hierarchies.

Populating the knowledge base. Once we settle on how to represent interpretations and storage strategies, we need to start instantiating the knowledge base. How should we include in the genomic interpretations quality attributes such as context (like clinical or pharmacogenomics) where the interpretation is useful; confidence level of the experts on interpretation; interpretation tool used (called variants versus expert interpretations) and so on?

Resolution of conflicts. Sometimes knowledge bases can have conflicts. For example, ClinVar can have conflicted interpretations as it allows experts to interpret in any way they want. Sometimes that can raise conflicted interpretations. How do we resolve such conflicts in interpretations? Will the confidence levels described by the curators help in this resolution?

Assimilation of new knowledge. Can the reads of a patient be reworked once the genomic research finds new interpretations of variants that relate to the variants of the patient? How do we develop alerts based on the new knowledge? This is important as GCDS can rework on the reads based on new knowledge.

Research Challenges in Problem-processing. GCDS integration architectures face numerous challenges due to the very limited understanding of how best to implement a GCDS. As we have seen

# ACCEPTED MANUSCRIPT

earlier, there exist many integration approaches ranging from organizational coordination to centralizedworkflow architecture to integration via service-oriented architecture. Interestingly, this kind of variations in approaches can also be seen in the underlying DSS technology. Holsapple [59] lists several architectures like text-oriented DSS, hypertext-oriented DSS, database-oriented DSS, solver-oriented DSS and others. Two DSSs could have identical data, knowledge and user interface systems but can differ in their implementation architectures. Holaspple [59] points out that a generic design for architectures is t, and the user interface techniques with which their problem processing components are conn ected. Obviously, like generic DSS, the four architectures of GCDS need common coordination mechanisms. We focus now on two such coordination issues: architectural standardization and inter-component communication.

(a) Architectural standardization. As we have seen above, standardization is important for representation of genomic data and of genomic interpretations. Coordination becomes much easier if we strive toward architectural standardization. It is essential when we try to integrate genomic data from multiple data sources (AA type), or try to integrate genomic interpretations from multiple knowledge bases (BB type), or try to integrate genomic data with genomic interpretations and clinical data (ABC type). It is still not clear which architecture should be selected for any one of them. Currently researchers choose arbitrary architectures for their project based on their own experience. Arguments can be made to develop a common meta-model for integration that covers genomic data, genomic interpretations and clinical data. Such a meta-model can be used to design proper architectures that serve components of GCDS and help promote integration.

(b) Component communication. Coordination needs communication. Hence, there is a need to set up communication between the components of a GCDS. In order to make communication flexible, the integration architecture needs to be of the service-oriented type. We see two competing styles of SOA used in GCDS architectures – (a) closed system using centralized-workflow [116]; and (b) an open system using DSS-focused decentralized workflow [150, 151]. The workflow-oriented architecture (Renci Consortium [69]) presumes that all resources needed by the workflow engine are within one organization with a clear understanding of all metadata and workflows involved. Such systems are often closed and proprietary. Standardization of such systems is difficult. The DSS-focused architecture, on the other hand, does not worry about centralization and workflows, but follows the communication roadmap of how to support the decision-making process of the clinicians. It uses HL7’s SOA support called RLUS (Retrieve, Locate, and Update Service). The output of this system is CDS rules for the components.

Research Challenges in GCDS User Interfaces. The research challenges that we see in GCDS user interface design are quite similar to issues facing user interface research in information systems. User interfaces increase customization of genomic data display, provide access to relevant genomic knowledge/interpretations, present knowledge and data in a more suitable way for different GCDS users and so on. We list the following research challenges.

(a) Standardization of GCDS user interfaces. Standardization of user interfaces is quite difficult for all kinds of GCDS – starting from simple query interfaces to the ones involving visualization. The difficulty arises due to the absence of standardization of the underlying message construction. In textual data situations, standard codification of messages is not available. In graphical user interfaces (GUI), it is unclear how to standardize application support for web interfaces of the GCDS.

(b) Cognitive modeling of GCDS user interface. User Interfaces vary in GCDS from the AA integration approach to the ABC integration approach. Very little work has been done to understand how GCDS users consume genomic data or genomic interpretations irrespective of the client-server implementation or the Web services implementation of GCDS. User’s cognitive style should be an important factor in the design of GCDS user interfaces. One can look at various problems that the DSS literature has studied such as cognitive biases, individual differences, the user’s ability to create and use visual images, and so on to figure out the cognitive aspects of user interfaces for GCDS.

(c) Usability metrics development for GCDS user interfaces. Usability testing is an essential component of user-centered GCDS design. The point of doing a usability test is to improve GCDS, be that in its

# ACCEPTED MANUSCRIPT

presentation of query results, its navigation and screen layout, its interaction, and its visual design. The Usability literature suggests that one should start testing early in the design/development process and follow through to the final stages of development. GCDS usability testing measures fall into three categories: effectiveness (did the participants complete the GCDS task error free?), efficiency (how much time did it take to complete the GCDS task?) and satisfaction (what is the degree to which participants perceive the GCDS tool to be usable?). No research is currently available in GCDS to answer these questions.

(d) Querying the knowledge base. Querying a knowledge base is an active area of research in the areas of semantic web, artificial intelligence, and robotics. How should we query genomic data source interpretations? What will be the structure of such a query language? Will the query language be used to ask something that is a logical consequence of the interpretations in the knowledge base? Is variant calling a better approach than expert interpretation?

## 5. Conclusions and Limitations

GCDS systems show a promise of improving the quality of healthcare through accurate and patientspecific clinical recommendations. This review paper addresses the informatics challenges standing in the database management, genomic knowledge management, problem-processing architecture emphasizing integration efforts with clinical data, and input/output mechanisms; (b) a review of extant research in each of these areas; and finally (c) a list of outstanding research opportunities.

The review points out that even though enormous progress has been made in the field of GCDS, many research opportunities still remain like details of architecture supporting complete integration of genomic database, genomic knowledge base (interpretations) and clinical data; use of loose coupling via SOA to enhance communication among GCDS components; the need for standardization in GCDS components; complexities in creating and managing knowledge bases; and the development of a common data model for genomic data.

The review also has several limitations. First, even though we have used PubMed as our resource portal, the collection of research articles was dictated by the inclusion and exclusion criteria mentioned in Section 2.3. Such criteria are somewhat ad hoc. There might be other inclusion and exclusion criteria that could have been used to include other research articles that were missed form our list. Second, the title and abstract reviews may not be sufficient to create a robust set of articles for our list. Third, due to page restrictions, the review did not go into a detailed description of each of the GCDS categories due to. For example, DSS-focused architecture espoused by Welch et al [148-151] was not compared in detail with centralized workflow oriented architecture implemented by Renci Consortium [116]. Many such issues also could not be covered.

## References

1 ACMG Board of Directors, 20167"Laboratory and clinical genomic data sharing is crucial to improving genetic health care: a position statement of the American College of Medical Genetics and Genomics," Genetics in Medicine, January 5, pp. 1-2.

2 Informatics Association 22.6 (2015): 1173-1178.

3 Bajaj, Renu, et al. 2011, "Evidence-based genomic diagnosis characterized chromosomal and cryptic imbalances in 30 elderly patients with myelodysplastic syndrome and acute myeloid leukemia." Molecular cytogenetics 4.1: 3.

4 Beck, T., Hastings, R.K., et al. 2014. "GWAS Central: a comprehensive resource for the comparison and interrogation of genome-wide association studies," European Journal of Human Genetics, July, 22, 4, pp. 949-952.

5 Bell, Gillian C., et al. "Development and use of active clinical decision support for preemptive pharmacogenomics." Journal of the American Medical Informatics Association 21.e1 (2013): e93-e99.

6 Berg, Alfred O., et al. 2005, "Genetic risk assessment and BRCA mutation testing for breast and ovarian cancer susceptibility: recommendation statement," Annals of Internal Medicine, 143, 5, p. 355.

7 Berg, Jonathan S., et al. 2013, "Processes and preliminary outputs for identification of actionable genes as incidental findings in genomic sequence data in the Clinical Sequencing Exploratory Research Consortium." Genetics in Medicine 15.11: 860-867.

8 Berry, D. A., Iverson, E. S., et al. 2002, "BRCAPRO Validation, Sensitivity of Genetic Testing of BRCA1/BRCA2, and Prevalence of Other Breast Cancer Susceptibility Genes," Journal of Clinical Oncology, 20, 11, June, pp. 2701-2712.

9 Bianchi, Diana W. 2012, "From prenatal genomic diagnosis to fetal personalized medicine: progress and challenges." Nature medicine 18.7: 1041-1051.

10 Bianchi, F., Galizia, E., Bracci, R. t al. 2007, "Effectiveness of the CRCAPRO program in identifying patients suspected for HNPCC," Clinical Genetics, 71, pp. 158-164.

11 Biesecker, Leslie G., and Robert C. Green. 2014, "Diagnostic clinical genome and exome sequencing." New England Journal of Medicine 370.25: 2418-2425.

12 Birkland, A. and Yona, G., 2006, "BIOZON: a system for unification, management and analysis of heterogeneous biological data," BMC Bioinformatics, February 15, 7, 70, pp. 1-24.

13 Bolser, Dan M. Chibon, Pierre-Yvesi, et al. 2012, “MetaBase—the wiki-database of biological databases, Nueclic Acid Research, 40, January, pp. D1250–D1254.

14 Bonczek RH, Holsapple CW, Whinston AB. 1980, “The evolving roles of models in the decision support systems.” Decision Sciences, 11, 337–56.

15 Bonczek, R., Holsapple, C. and Whinston, A. Foundations of Decision Support Systems, Academic Press, New York, 1981.

16 Carney, Pamela H. "Information technology and precision medicine." Seminars in oncology nursing. Vol. 30. No. 2. WB Saunders, 2014.

17 Castaneda, Christian, et al. "Clinical decision support systems for improving diagnostic accuracy and achieving precision medicine." Journal of Clinical Bioinformatics 5.1 (2015): 4.

18 Choi, Murim, et al. 2009, "Genetic diagnosis by whole exome capture and massively parallel DNA sequencing." Proceedings of the National Academy of Sciences 106.45: 19096-19101.

19 Chung, S. Y and Wong, L. 1999, "Kleisli: a new tool for data integration in biology," Trends in Biotechnology, 17, pp. 351-355

20 Chute, C. G., Beck, Scott A., Fist, T. B. and Mohr, D. N. 2010, The enterprise data trust at Mayo Clinic: a semantically integrated warehouse of biomedical data, J of American Medical Association, 17, pp. 131-135.

21 Cock PJ, Antao T, Chang JT, et al., 2009. "Biopython: freely available Python tools for computational molecular biology and bioinformatics," Bioinformatics, 25, pp. 1422–1423.

22 Collins, F. S. and Varmus, H., 2015, "A new initiative on precision medicine," New England Journal of Medicine, 372, pp. 793-795.

23 Cornell. M., Paton, N. W., et al. 2001, "GIMS – A Data Warehouse for Storage and Analysis of Genome Sequence and Functional Data," Proc. IEEE 2nd International Symposium on Bioinformatics and Bioengineering, November 4-6.

24 Cowie, Martin R., et al. 2107. "Electronic health records to facilitate clinical research," Clinical Research in Cardiology, 106, pp. 1-9.

25 Danahey, K., et al. “Simplifying the use of pharmacogenomics in clinical practice: Building the genomic prescribing system,” Journal of Biomedical Informatics, 75, 2017, pp. 110-121

26 Dos Santos, B., and Holsapple, C. W., "A Framework for Designing Adaptive DSS Interfaces," Decision Support Systems, 5, 1, 1989, pp. 1-11.

27 Douali, Nassim, et al. "Personalized decision support system based on clinical practice guidelines." pHealth. 2015.

28 Du, N., Guo, S., Mahajan, S. D., et al. 2012. "BioStar+: A Data Warehouse Schema for Integrating Clinical and Genomic data From HIV Patients," ACM SIG Bioinformatics Record archive, 2, 3, September , pp. 6-16

29 Emery, J. 2005, "The GRAIDS Trial: The development and evaluation of computer decision support for cancer genetic risk assessment in primary care," Annals of Human Biology, March-April, pp. 218-227.

30 Evans, James, Wilhelmsen, K., Berg, Jonathan and Schmitt, Charles, "A new framework and prototype solution for clinical decision support and research in genomics and other data-intensive fields of medicine,"

31 Evans, S., Henry, M.S., et al. 1995, "Clinical Results Using Informatics to Evaluate Hereditary Cancer Risk," Proceedings of AMIS Annual Symposium on Computation and Applied Medical Care, pp. 834-838.

32 Feigenbaum, E. A., B. G. Buchanan, and J. Lederberg, "On Generality and Problem Solving: a Case Study Using the DENDRAL Program," Machine Intelligence 6, Edinburgh Univ. Press, 1971.

33 Ferguson, J. Scott, et al. "Impact of a bronchial genomic classifier on clinical decision making in patients undergoing diagnostic evaluation for lung cancer." BMC pulmonary medicine 16.1 (2016): 66.

34 Ferreti, V. and Montibeller, G., "Key challenges and meta-choices in designing and applying multi-criteria spatial decision support systems," Decision Support Systems, 84, 2016, pp. 41-52.

35 Finlayson, S. G., Levy, Mia, et al., 2016, Toward rapid learning in cancer treatment selection: An analytical engine for practice-based clinical data, Journal of Biomedical Informatics, 60, pp. 104-113

36 Floyd, James S., and Bruce M. Psaty. "The application of genomics in diabetes: barriers to discovery and implementation." Diabetes care 39.11 (2016): 1858-1869.

37 Systems, 55, 2013, pp. 336-347.

38 Freese, N. H., Norris, D. C., and Loraine, A. E. 2016, "Integrated genome browser: visual analytics platform for genomics," 32.., 14, pp. 2089-2095.

39 Freimuth, R. R., et al. "Implementing Genomic Clinical Decision Support for Drug‐Based Precision Medicine." CPT: pharmacometrics & systems pharmacology 6.3 (2017): 153-155.

40 Freitas, A. A., Vasieva, O., Magalhaes, J. P., 2011. "A data mining approach for classifying DNA repair genes into ageing-related or non-ageingrelated," BMC Genomics, 12, 27, pp. 1-11.

41 Fusaro, Vincent A., et al. "Development of a scalable pharmacogenomic clinical decision support service." AMIA Joint Summits on Translational Science proceedings. AMIA Joint Summits on Translational Science 2013 (2012): 60-60.

42 Garg AX, Adhikari NK, McDonald H, et al. 2005, "Effects of computerized clinical decision support systems on practitioner performance and patient outcomes: a systematic review," JAMA, 293, pp.1223–38.

43 Gene Ontology Consortium, 2004, "The Gene Ontology (GO) database and informatics resource," Nucleic Acids Research, 32, Database issue, pp. D258-D261.

44 Glasspool, D. W., Oettinger, A., et al. 2010, "Interactive Decision Support for Risk Management: a Qualitative Evaluation in Cancer Genetic Counselling Sessions," 25, pp. 312-316.

45 Goble, C. and Stevens, R., 2008, "State of the nation in data integration for bioinformatics," Journal of Biomedical Informatics, 41, pp. 687-693.

46 Golub, T. R., Slomin, D. K., et al. 1999, "Molecular Classification of Cancer: Class Discovery and Class Prediction by Gene Expression Monitoring," Science, 286,15, October, pp. 531- 537.

47 Gonzalez, G. H., Tahsin, T., Goodale, B. C., et al. 2016, "Recent Advances and Emerging Applications in Text and Data Mining for Biomedical Discovery," Briefings in Bioinformatics, 17, 1, pp.33-42.

48 Gorry GA, Scott Morton MS. 1971, “A framework for management information systems. Fall”. Sloan Management Review;. pp. 55–70.

49 Goto N, Prins P, Nakao M, et al. 2010, "BioRuby: bioinformatics software for the Ruby programming language," Bioinformatics. 26, pp. 2617– 2619.

50 Gottesman, Omri, et al. 2013, "The electronic medical records and genomics (eMERGE) network: past, present, and future," Genetics in Medicine. 15,10, pp. 761-771.

51 249–55.

52 Hamosh, Ada, et al. 2005, "Online Mendelian Inheritance in Man (OMIM), a knowledgebase of human genes and genetic disorders." Nucleic acids research 33.suppl 1: D514-D517.

53 Harris, N. L. 1997, "Genotator: A Workbench for Sequence Annotation," Genome Research, 7, pp. 754-762.

54 Hazin, Ribhi, et al. "Ethical, legal, and social implications of incorporating genomic information into electronic health records." Genetics in medicine: official journal of the American College of Medical Genetics 15.10 (2013): 810.

55 Hedeler, C., Wong, H. M., Cornell, M. J., et al. 2007, "e-Fungi: a data resource for comparative analysis of fungal genomes," BMC Genomics, 8, 426, pp. 1-15.

56 Helt, G., Nicol, J. W., et al. 2009, "Genoviz Software Development Kit: Java tool kit for building genomics visualization applications," BMC Bioinformatics, 10, 106, pp. 1-13.

57 Henry, N. L., P. L. Bedard, and A. DeMichele. "Standard and Genomic Tools for Decision Support in Breast Cancer Treatment." American Society of Clinical Oncology educational book. American Society of Clinical Oncology. Meeting. Vol. 37. 2017.

58 Hoffman, J.M., et al., “PG4KDS: A Model for the Clinical Implementation of Pre-emptive Pharmacogenetics” American Journal of Genetics: Part C, March 2014, March 2014, pp. 45-55.

59 Holsapple, C.W. 2008. “DSS Architecture and Types,” Handbook on Decision Support Systems 1, F. Burstein and Clyde W. Holsapple (Editors), Springer.

60 Holland RC, Down TA, Pocock M, et al. 2008, "BioJava: an open-source framework for bioinformatics," Bioinformatics. 24, pp. 2096– 2097.

61 Hume, S., Aerts, J., Sarnikar, S. and Huser, V. 2016. “Current applications and future directions for the CDISC operational data model standard: A methodological review,” Journal of Biomedical Informatics, 60, pp. 352-362.

62 Huser, Vojtech, and James J. Cimino. "Providing pharmacogenomics clinical decision support using whole genome sequencing data as input." AMIA Joint Summits on Translational Science proceedings. AMIA Joint Summits on Translational Science 2013 (2012): 81-81.

63 Iavindrasana, J., Lo Iacono, L. et al. 2008, "The @neurIST project," Global Healthgrid: e-Science Meets Biomedical Informatics T. Solomonides et al. (Eds.), IOS Press.

64 Ji, Yuan, et al. "Preemptive pharmacogenomic testing for precision medicine: a comprehensive analysis of five actionable pharmacogenomic genes using next-generation DNA sequencing and a customized CYP2D6 genotyping cascade." The Journal of Molecular Diagnostics 18.3 (2016): 438-445.

65 Kaimal, Anjali J., Mary E. Norton, and Miriam Kuppermann. "Prenatal testing in the genomic age: clinical outcomes, quality of life, and costs." Obstetrics & Gynecology 126.4 (2015): 737-746.

66 Kanehisa, M., Goto S., et al. 2011, "KEGG for integration and interpretation of large-scale molecular data setsm" Nucleic Acids Research, Novmeber 10, pp. 1-6.

67 Kanehisa, Minoru, and Susumu Goto. 2000, "KEGG: kyoto encyclopedia of genes and genomes." Nucleic acids research 28.1: 27-30.

68 Katayama, T. Nakao M., Takagi T., and Togo,WS, 2010, "Integrated SOAP and REST APIs for interoperable bioinformatics Web services," Nucleic Acids Research, 38, pp. W706–11.

69 Kawamato, K. and Lobach D. F., 2005. "Design, Implementation, Use, and Preliminary Evaluation of SEBASTIAN, a Standards-Based Web Service for Clinical Decision Support," AMIA Symposium Proceedings, pp. 380-384.

70 Khoury, Muin J., et al. "Knowledge integration at the center of genomic medicine." Genetics in Medicine 14.7 (2012): 643-647.

71 Kitchenham, B., Brereton, O. P., et al. 2009. “Systematic literature reviews in software engineering – A systematic literature review,” Information and Software Technology, 51, pp. 7-15.

72 Klonowska, K., Czubak, K., et al. 2013. "Oncogenomic portals for the visualization and analysis of genome-wide cancer data," Oncotarget, 7, 1, pp. 176-192.

73 Kouris, Ioannis, et al. "E-Health towards ecumenical framework for personalized medicine via Decision Support System." Engineering in Medicine and Biology Society (EMBC), 2010 Annual International Conference of the IEEE. IEEE, 2010.

74 Landrum, M. J., Lee, J. M., et al. 2016, "ClinVar: Public archive of interpretations of clinically relelant variants," 44. Database issue, pp. D862- D868.

75 Larson, Eric A., and Russell A. Wilke. "Integration of genomics in primary care." The American journal of medicine 128.11 (2015): 1251-e1.

76 Lee, J. K., Williams, P. D., Cheon, S. 2008, "Data Mining in Genomics," Clinics in Laboratory Medicine, March, 28, 1, pp. 145-165.

77 Liu, Yifeng, Yongjie Liang, and David Wishart. 2015, "PolySearch2: a significantly improved text-mining system for discovering associations between human diseases, genes, drugs, metabolites, toxins and more." Nucleic acids research 43.W1: W535-W542

78 Louie, B., Mork, P., Martin-Sanchez, F., et al. 2007, "Data integration and genomic medicine," 40, pp. 5-16.

79 Mailman, Matthew D., et al. 2007, "The NCBI dbGaP database of genotypes and phenotypes." Nature genetics 39.10: 1181-1186.

80 Martín-Sánchez, Fernando, et al. "Personalised Medicine Possible With Real-Time Integration of Genomic and Clinical Data To Inform Clinical Decision-Making." Studies in health technology and informatics 216 (2015): 1052-1052.

81 Masys, D. R., Jarvik, G. P., et al. 2012. "Technical desiderata for the integration of genomic data into Electronic Health Records," Journal of Biomedical Informatics, 45, pp. 419-422

82 Mathe, Janos L., Ledeczi, A., et al., 2009, "A Model-Integrated, Guideline-Driven, Clinical Decision-Support system," IEEE Software, July/Augusut, pp. 54-61.

83 Matloff, E. T., Shannon, K. M., Moyer, A., and Nananda., F., 2007, "Should Menopausal Women at Increased Risk for Breast Cancer Use Tamoxifen, Raloxifene, or Hormone Therapy?: A Framework for Personalized," Journal of Cancer Education, 22, 10, pp. 10-14.

84 Matys, V., Fricke, E., Geffers, R., Gößling, E., Haubrock, M., Hehl, R., Hornischer, K., Karas, D., Kel, A.E., Kel-Margoulis, O.V. and Kloos, D.U., 2003. TRANSFAC®: transcriptional regulation, from patterns to profiles. Nucleic acids research, 31(1), pp.374-378.

85 Mayvan, B. B., Rasoolzadegan, A. and Yazdi, Z. G. 2017, “The state of the art on design patterns: A systematic mapping of the literature,” The Journal of systems and Software, 125, pp. 93-118.

86 McLaren, W., Pritchard, B. et al. 2010, "Deriving the consequences of genomic variants with the Ensembl API and SNP effect predictor," Bioinformatics, August 15, 26, 16, pp. 2069-2070.

87 Meric-Bernstam, Funda, et al. "A decision support framework for genomically informed investigational cancer therapy." Journal of the National Cancer Institute 107.7 (2015): djv098.

88 Miller, R. A., Pople, H. E., Jr., and Myers, J. D. 1982, “Internist-1, an experimental computer based diagnostic consultant for general internal medicine”, New England Journal of Medicine, 307, pp. 468–476.

89 Miller, R., Masarie, F. E., and Myers, J. D. 1986, “Quick medical reference (QMR) for diagnostic assistance.” MD Computing, 3, pp. 34–48.

90 Min, H., Manion, F. J., et al. 2009, "Integration of prostrate cancer clinical data using an ontology," Journal of biomedical informatics, pp. 1035-1045.

91 Minarro-Gimenez, J.A., Blagec, K., et al. 2014, "An Ontology-Based, Mobile-Optimized System for Pharmacogenomic Decision Support at the Point-of-Care," PLOS ONE, May, 9, 5, pp. 1-9.

92 National Center for Biotechnology Information, 2014. The NCBI Handbook, 2nd Edition, Bethesda, Maryland.

93 National Human Genome research Institute (NHGRI), 2014, "Summary of Themes Discussed in Keynote and Panel Discussions," Genomic Medicine Centers Meeting VII, October 2-3, Bethesda, Maryland

94 Neri, Pamela M., et al. "Usability of a novel clinician interface for genetic results." Journal of biomedical informatics 45.5 (2012): 950- 957.

95 Nishimura, Adam A., et al. "Development of clinical decision support alerts for pharmacogenomic incidental findings from exome sequencing." Genetics in medicine: official journal of the American College of Medical Genetics 17.11 (2015): 939-942.

96 O’Donnell, PH, et al., “The 1200 Patients Project: Creating a New Medical Model System for Clinical Implementation of Pharmacogenomics,” Clinical Pharmacology & Therapeutics, 92, 4, pp. 446-449, October 2012

97 Ohta, T., Pyysalo, S., Rak, R., et al. 2013. "Overview of the Pathway Curation (PC) task of BioNLP Shared Task," Proceedings of the

BioNLP Share Task 2013 Workshop, pp. 67-75.

98 Overby, C. L., Kohane, I., Kannry, J. L., et al. 2013, "Opportunities for genomic clinical decision support interventions," Genetics in Medicine, 15, 10, pp. 817- 823

99 Overby, Casey Lynnette, et al. "Opportunities for genomic clinical decision support interventions." Genetics in medicine: official journal of the American College of Medical Genetics 15.10 (2013).

100 Overby, Casey Lynnette, et al. "Physician attitudes toward adopting genome-guided prescribing through clinical decision support." Journal of personalized medicine 4.1 (2014): 35-49.

101 Paliulis, E. and Ali, H. H. 2014, "An Integrated Model of Human Biomedical and Clinical Data Structures," Computational Advances in Bio and Medical Sciences (ICCABS), IEEE 4th International Conference, June 2, pp. 1-6.

102 Pandey, S., Karunamoorthy, D., and Buyya, R. 2011, "Workflow engine for clouds," Cloud Computing: Principles and Paradigms, Edited by Rajkumar Buyya, James Broberg and Andrzej Goscinski, pp. 321- 344.

103 Patel VL, Allen VG, et al. 1998, “Representing clinical guidelines in GLIF: individual and collaborative expertise”. J Am Med Inform Assoc 5(5):467–83

104 Pavlopoulos, G. A., Malliarakis, D., et al. 2015, "Visualizing genome and systems biology: technologies, tools, implementation techniques and trends, past, present and future," GigaScience, 4, 38, pp. 1-27.

1051995, pp.141-158.

106 genotyping." Genome research 16.9: 1136-1148.

107 Peleg, M. 2013. “Computer-interpretable clinical guidelines: A methodological review,” Journal of Biomedical Informatics, 46, pp. 744- 763.

108 Petrucelli, Nancie, Mary B. Daly, and Gerald L. Feldman. "BRCA1 and BRCA2 hereditary breast and ovarian cancer." (2013).

109 Picone, M., Steger, S., Exarchos, K, et al. 2011, "Enabling Heterogeneous Data Integration and Biomedical Event Prediction Through ICT: The Test Case of Cancer Reoccurrence," H.R. Arabnia and Q.-N. Tran (eds.), Software Tools and Algorithms for Biological Systems, Advances in Experimental Medicine and Biology, Chapter 37, pp. 367- 375.

110 Pillar, Nir, et al. "Actionable clinical decisions based on comprehensive genomic evaluation in asymptomatic adults." Molecular genetics & genomic medicine 3.5 (2015): 433-439.

111 Pittman, J., Huang, E., Dressman, H. et al. 2004, "Integrated modeling of clinical and gene expression information for personalized prediction of disease outcomes," Proceedings of the National Academy of Sciences, 101,22, June 1, pp. 8431-8436

112 Power, D. J. 2008. “Decision Support Systems: A Historical Overview,” Handbook on Decision Support Systems 1, F. Burstein and Clyde W. Holsapple (Editors), Springer.

113 Rajasekarakan, H., Lo Iacono, L., et al., 2008, "@neurIST – Towards a System Architecture for Advanced Disease Management through Integration of Heterogeneous Data, Computing, and Complex Processing Services," 21st IEEE International symposium on computer-Based Medical systems, pp. 361- 366.

114 Rasumussen-Torvik, Laura, J., Stallings, S. C., et al. 2014, "Design and Anticipated Outcomes of the eMERGE-PGx Project: A Multi Center Pilot for Pre-Emptive Pharmacogenomics in Electronic Health Record Systems," Clinical Pharmacology Theory, October, 96, 4, pp. 482-489.

115 Reilly, J., Ahalt, S., McGee, J. eta l. 2015, "MaPSeq, A Service-Oriented Architecture for Genomics Research within an Academic Biomedical Research Institution," Informatics, 2. pp. 20-30.

116 RENCI Technical Report Series, 2014, Technologies for Genomic Medicine, TR 14-02.

117 Richards,S., Aziz,N., Bale,S., Bick,D., Das,S., Gastier-Foster,J., Grody,W.W., Hegde,M., Lyon,E., Spector,E. et al. 2015, "Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology," Genetics in Medicine, 17, pp. 405-424.

118 Roberts, J. Scott, et al. 2005, "Genetic risk assessment for adult children of people with Alzheimer’s disease: the Risk Evaluation and Education for Alzheimer’s Disease (REVEAL) study." Journal of Geriatric Psychiatry and Neurology 18.4: 250-255.

119 Robinson, James T., Thorvaldsdottir, H., et al. 2011, "Intergrative genomics viewer," Nature Biotechnology, 29. pp. 24-26.

120 Rodriguez-Rodriguez, Lorna, et al. "Use of comprehensive genomic profiling to direct point-of-care management of patients with gynecologic cancers." Gynecologic oncology 141.1 (2016): 2-9.

121 Ross, C. J., Visscher, H., Sistonene, J., et al. 2010, "The Canadian Pharmacogenomics Network for Drug Safety: a model for safety pharmacology," July, 20, 7, pp. 681-687.

122 Rzhetsky, A., Iossifov, I., et al. 2004, "GeneWays: a system for extracting, analyzing, visualizing, and integrating molecular pathway data," Journal of Biomedical Informatics, 37, pp. 43-53.

123 Samwald, Matthias, et al. "Pharmacogenomic knowledge representation, reasoning and genome-based clinical decision support based on OWL 2 DL ontologies." BMC medical informatics and decision making 15.1 (2015): 12.

124 Samwald, Matthias, et al. "Towards an interoperable information infrastructure providing decision support for genomic medicine." arXiv preprint arXiv:1109.6626 (2011).

125 Scheuner, Maren T., et al. 1997, "Family history: a comprehensive genetic risk assessment method for the chronic conditions of adulthood." American Journal of Medical Genetics 71.3: 315-324.

126 Schulze-Kremer,S. 1998, "Ontologies for molecular biology," Pacific Symposium on Biocomputing, 3, pp. 695-706.

127 Sen A, Biswas G. 1985, “Decision support systems: an expert systems approach.” Decision Support Syst;1:197–204.

128 Sen, A. 1998, "From DSS to DSP: A taxonomic retrospection,” Communications of the ACM, 41, 5es, May 1998, p. 28. (Full version in ACM Digital Library, Volume 41, No. 5es, 1998, the URL is http://www.acm.org/).

129 Sen, A., Banerjee, A., et al. 2012, "Clinical decision support: Converging toward an integrated architecture." Journal of biomedical informatics, 45, 5, pp. 1009-1017.

130 Sherry, S. T., Ward, M., and Sirotkin, K. 1999, "dbSNP - database for single nucleotide polymorphisms and other classes of minor genetic variation," Genome Research, 9,, pp. 677- 679

131 Shifman, A. R., Johnson, R. M. and Wilhelm, B. T. 2016, "Cascade: an RNA-seq visualization tool for cancer genomics," BMC Genomics, pp. 1-11.

132 Shortliffe, E. H. and Buchanan, B. G. 1975, “A model of inexact reasoning in medicine”, Mathematical Biosciences, 25, pp. 351-379.

133 Stajich JE, Block D, Boulez K, et al. 2002, "The Bioperl toolkit: Perl modules for the life sciences," Genome Research;12, pp. 1611– 1618.

134 Su A. I., Welsh, J.B., Sapinoso, L. M., et al. 2001. "Molecular classification of human carcinomas by use of gene expression signatures," Cancer Research, October, 61, 20, pp. 7388-7393.

135 Swen, J. J., Wilting, I., et al. 2008, "Pharmacogenetics: From Bench to Byte," Clinical Pharmacology & Therapeutics, 83, 5, May, pp. 781- 787.

136 Tarczy-Hornoch, Peter, et al. 2013, "A survey of informatics approaches to whole-exome and whole-genome clinical reporting in the electronic health record." Genetics in Medicine 15.10: 824-832.

137 Taylor, Barry S., et al. 2010, "Integrative genomic profiling of human prostate cancer." Cancer cell 18.1: 11-22.

138 The ENCODE Project Consortium. 2011, "A User's Guide to the Encyclopedia of DNA Elelments (ENCODE), PLoS Biology, April, 9, 11, pp. 1-21.

139 Triplet, T. and Butler, G. 2013. "A review of genomic data warehousing systems," Briefings in Bioinformatics, pp. 1-13.

140 Tsoukas L,I., Liaros, A., et al. 1997, "The use of expert system of composite risk factors in breast cancer screening," Studies in Health Technology and Informatics, 43, February, pp. 859-863.

141 van der Aalst, W. M. P., Aldred, L. and Hofstede, A. H. M. 2004, "Design and implementaion of the YAWL system," Proceedings of the 16th International Conference on Advanced Information systems Engineering (CAiSE 2014), A. Persson and J. Stirna (editors), pp. 142-159.

142 Wagle, Nikhil, et al. 2011, "Dissecting therapeutic resistance to RAF inhibition in melanoma by tumor genomic profiling." Journal of clinical oncology 29.22: 3085-3096.

143 Wakefield, C. E., Watts, K. L., et al. 2011, "Development and pilot testing of an online screening decision aid for men with a family history of prostate cancer," Patient Education and Counseling, 83, pp. 64-72.

144 Wang, L. and Zhange, A. 2005, "BioStar models of clinical and genomic data for biomedical data warehouse design," Internationa Journal of Bioinformatics Research and Applications, 1, 1, pp. 63-80.

145 Warde-Farley, D., Donaldson, S.L., Comes, D., et al. 2010. "The GeneMANIA prediction server: biological network integration for gene prioritization and predicting gene function," Nucleic Acids Research, July, 38 Web Server Issue, W214-220.

146 Warner, Jeremy L., Sandeep K. Jain, and Mia A. Levy. "Integrating cancer genomic data into electronic health records." Genome medicine 8.1 (2016): 113.

147 Weitzel, Kristin Wiisanen, et al. 2016, "The IGNITE network: a model for genomic medicine implementation and research." BMC Medical Genomics 9.1: 1.

148 Welch, B. M., Eilbeck, K., et al., 2014. "Technical desiderata for the integration of genomic data with clinical decision support," Journal of Biomedical Informatics, 51, pp. 3-7.

149 Welch, Brandon M., and Kawamoto, K. 2013. "The need for clinical decision support integrated with the electronic health record for the clinical application of whole genome sequencing information." Journal of Personalized Medicine, 3, 4, pp. 306-325.

150 Welch, Brandon M., Rodriguez-Loya, et al. 2014, "Clinical Decision Support for Whole Genome Sequence Information Leveraging a Service-Oriented Architecture: a Prototype," AMIA Annual Symposium Proceedings, Nov 14, pp. 1188-1197.

151 Welch, Brandon, M., Loya, S. R., Eilbeck, K., Kwaamoto, K. 2014, "A Proposed Clinical Decision Support Architecture Capable of Supporting Whole Genome Sequence Information," Journal of Personalized Medicine, 4, pp. 176-199.

152 Wilke R. A., Ramsey, L.B., et al. 2012, "The clinical pharmacogenomics implementation consortium: CPIC guideline for SLCO1B1 and simvastatin-induced myopathy," Clinical Pharmacology Theory, July, 92. 1, pp. 112-117.

153 Wilkinson, M., Schoof, H., Ernst, R., and Hasses, D. 2005, "BioMOBY Successfully Integrates Distributed Heterogeneous Bioinformatics Web Services. The PlaNet Exemplar Case," Plant Physiology, May, 138, pp. 5-17.

154 Wu, Chen-Chi, et al. 2011, "Newborn genetic screening for hearing impairment: a preliminary study at a tertiary center." PLoS One 6.7: e22314.

155 Zhang, S. and Goddard, S., A software architecture and framework for Web-based distributed Decision Support Systems," Decision Support Systems, 2007, pp. 1133-1150.

156 Žitnik, Marinka, et al. 2013, "Discovering disease-disease associations by fusing systems-level molecular data." Scientific reports 3: 3202.

## Highlights

 Genomic integration

 Genomic data management

 Genomic knowledge management

Effectively integrating clinical data with genomic data to develop Genomic Clinical Decision Support (GCDS) systems

 GCDS literature has challenges like standardization, representation and storage of genomic data and genomic interpreations

# ACCEPTED MANUSCRIPT

Arun Sen is a Full Professor in the Department of Information and Operations Management in Texas A&M University. He holds an M.Tech degree in Electronics (from Calcutta University, India in 1971), an M.S. in Computer Science (from Penn State University in 1976) and a Ph.D. in Information Systems (from Penn State University in 1979). He has published 58 research papers in journals like MIS Quarterly, Information Systems Research, Journal of MIS, Communications of the ACM (CACM), Decision Support Systems, IEEE Transactions on Systems, Man and Cybernetics, Journal of Biomedical Informatics, IEEE Transactions on Software Engineering, IEEE Transactions on Engineering Management, Decision Sciences, Information Systems, Computers and OR, Omega, European Journal of Operations Research, Information and Management, Omega and others. He has numerous articles in conferences and invited presentations. His research interests include areas like healthcare delivery (Medical home, Readmission and Care coordination), Clinical decision support systems, Genomic decision support systems, Economic Analysis of Health Information Exchange, Economic Analysis of Healthcare Information Technology, Software Reuse, Experts Systems including Case-based Reasoning, Data Warehousing (such as adoption and diffusion, metadata management, ETL change management and data warehousing process maturity), and E-Commerce (such as web analytics, website customer segmentation, web service economics and building recommendation engines at the web). He was an Associate Editor of Journal of Database Management. He was a special issue editor for Decision Support Systems, Communications of the ACM, Database and Expert Systems with Application. He served as a chair of INFORMS College on Information Systems, a program chair for the 1996 WITS (Workshop on Information Technology and Systems) Conference and a track chair (Decision Support Systems and AI track) for the 1996 National DSI Conference. Dr. Sen was also a Co-Principal Investigator in a five-year grant (\$7.2 Million) from the Office of National Coordinator in the U.S. Department of Health and Human Services to create Regional Extension Center (CentrEast REC) housed in the Rural and Community Health Institute in Texas A&M College of Medicine.

Ahmad Al Kawam is currently pursuing a Ph.D. degree in Electrical Engineering at Texas A&M University, College Station, TX. He obtained his Bachelor's degree in Computer and Communication Engineering from Rafik Hariri University, Lebanon in 2011 and his Master's degree in Computer Engineering from the Lebanese American University, Beirut, Lebanon in 2014. His research uses computational and statistical methods to perform studies in genomics and healthcare informatics revolving around genomic biomarker discovery, and genomic clinical decision support.

Aniruddha Datta received the B. Tech degree in Electrical Engineering from the Indian Institute of Technology, Kharagpur in 1985, the M.S.E.E. degree from Southern Illinois University, Carbondale in 1987 and the M.S. (Applied Mathematics) and Ph.D. degrees from the University of Southern California in 1991. In August 1991, he joined the Department of Electrical and Computer Engineering at Texas A&M University where he is currently the J. W. Runyon, Jr. ’35 Professor II and Director of the Center for Bioinformatics and Genomic Systems Engineering (CBGSE) .His areas of interest include adaptive control, robust control, PID control and Genomic Signal Processing. He has authored or coauthored 5 books and over 200 journal and conference papers on these topics. He is a Fellow of IEEE, has served as an Associate Editor for the IEEE Transactions on Automatic Control (2001-2003), the IEEE Transactions on Systems, Man and Cybernetics-Part B (2005-2006), the IEEE Transactions on Biomedical Engineering (2013-2015), the EURASIP Journal on Bioinformatics and Systems Biology (2007-2016) , the IEEE Journal of Biomedical and Health Informatics (2014-2016) and is currently serving as an Associate Editor for the IEEE/ACM Transactions on Computational Biology and Bioinformatics, and IEEE Access.
