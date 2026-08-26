---
otero_id: 22031
otero_key: "NDXMECBR"
title: "A domain-driven approach to improving search effectiveness in traditional online catalogs"
authors: "Theresa I. Jefferson; Thomas J. Nagy"
year: "2002"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00116-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A domain-driven approach to improving search effectiveness in traditional online catalogs

Theresa I. Jefferson<sup>a,\*</sup>, Thomas J. Nagy<sup>b</sup>

<sup>a</sup>Engineering Management and Systems Engineering, George Washington University, Washington, DC 20052, USA <sup>b</sup>Management Science Department, George Washington University, Washington, DC 20052, USA

Received 2 June 2000; received in revised form 3 February 2001; accepted 24 May 2001

## Abstract

Search performance can be greatly improved by using domain knowledge to assist users in developing a problem specification tailored to the information contained in the system. A methodology is presented for utilizing intelligent information retrieval techniques and domain-specific knowledge to improve user searching. For databases involving a relatively narrow domain, a ‘‘system thesaurus’’ combined with expert systems technology can be used to create an intelligent front end to assist the user in retrieving information with greater precision and recall. Evaluation of the prototype showed greatly improved search effectiveness and satisfaction over the traditional catalog system. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Intelligent information retrieval; Expert systems; Search effectiveness; Empirical evaluation

## 1. Introduction

The Internet has brought digital libraries to our desktops, resulting in the availability of hundreds of articles containing information on every conceivable subject. Web search engines have made user searching a reality, with current research focusing on the use of natural language processing and relevance [8]. However, there is still a large volume of information in traditional catalog systems. Users of these systems are often unable to retrieve the information they desire due to their inability to describe the information they need in a format that matches the way in which the information is stored. While many of these legacy systems are migrating to the web, it is not always possible, due to political and/or economic reasons. In addition, the targeted users may be located in geographical regions with unreliable communication and technically obsolete computer systems. For this reason, our research developed a methodology for utilizing intelligent information retrieval techniques and domainspecific knowledge to improve searching in traditional catalog systems. The prototype is able to run under DOS on a computer with a low level of system resources (386 MHz computer with 4MB RAM).

There are a number of documented problems with traditional systems. Most use a thesaurus to assist in coding documents with appropriate keywords during data entry. Often the keywords assigned are either too broad or too specific. Information retrieval from a clearinghouse system, which is made up of records from a number of different sources, is even more complex due to the lack of standardization among many different thesauri and indexing vocabularies [4].

The probability that both a searcher and an IS will apply the same term for a given concept is quite low between 10 and 20% [3]. Therefore, unless a user has a good idea of the subject terms used by the system, traditional methods of searching are seldom successful, resulting in the retrieval of too much or too little information. Even if the user is able to articulate needs, transforming those needs into a search strategy that will retrieve relevant references is not a simple task.

Previous research in online catalog search behavior has shown that users experience difficulty in performing subject searches in catalog systems [6]. There are a number of reasons:

1. it is extremely difficult for users to express their information needs in a specific yet exhaustive way;

2. standard query languages do not take into consideration user variability;

3. users have limited knowledge of the organization and contents of the database;

4. users have limited experience in creating and modifying search strategies.

When we produce systems that contain knowledge of the domain of the data and have the ability to assist users in creating search strategies, we are able to shift some of the burden of the retrieval specification from the user to the system.

## 2. The research

The purpose of our research was to develop a methodology for utilizing intelligent information retrieval techniques and domain-specific knowledge to improve searching in traditional online catalogs. It focused on the development of an intelligent front end targeted at databases with finite domains. In order to use this method, it is necessary to construct a system thesaurus that contains topic terms describing the main categories and subcategories of the database in the form broader, narrower, and related terms along with a complete list of synonyms for the database. These synonyms must represent derivations in keyword coding as well as in user vocabulary. The prototype, intelligent data analyzer (called IDA), was developed using the Prolog programming language and consisted of six features:

1. user and query modeling;

2. search strategy formulation;

3. document ranking;

4. review and evaluation of search results;

5. search modifications and relevance feedback;

6. system refinement on the basis of statistics of continued use.

A prototype of the system was developed for a catalog that focused on drug information. This catalog exhibited all of the features that make searching in online systems problematic, as well as some additional complications: it is from a clearinghouse with data originating from numerous sources; it has a multilingual database; it has an extremely diverse user base. Searching without an intermediary was not feasible. Information requesters obtained references by a consultation with an administrator, i.e. either the librarian or an assistant. The administrator used notes from the conversation with the requester to determine a search strategy for the database. Ideally, the catalog should not need an intermediary but be directly accessible by the users. For the purpose of this paper, we will refer to the catalog as drug information system (DIS).

## 2.1. The drug information system (DIS)

DIS is a bibliographical catalog system that contains information (author, title, abstract, keywords, etc.) about published documents in the drug abuse literature. DIS was designed using a software package called Micro CDS/ISIS, shareware with a strong and powerful search engine copyrighted by the United Nations. Using this package, the database is searched for documents of interest. All of the fields in DIS are searchable. Some have been designated as search fields, such as the keywords title. Micro CDS/ISIS creates inverted files for these fields, allowing fast and efficient searching. Searches are also possible on fields not designated as search fields, e.g. abstract. Such searches are free text ones and these take considerably longer to produce answers. When a user queries DIS, the system provides a listing of relevant documents and their location, as well as abstracts of the documents.

The data from DIS comes from a variety of international organizations. Routines have been developed to convert the electronic data to the appropriate form. However, the organizations do not use the same thesaurus and keyword vocabulary, therefore the keywords and descriptor fields in the response do not usually contain consistent data.

The DIS data is entered in both Spanish and English. Some records are completely Spanish, some are completely English, and some are a combination of both languages (e.g. title and keywords in English and abstract in Spanish). Unfortunately, not all the users are bilingual.

## 2.2. The intelligent data analyzer (IDA)

As described before, IDA consists of six modules: (1) user and query modeling; (2) search strategy formulation; (3) document ranking; (4) review and evaluation of search results; (5) search modifications and relevance feedback; (6) system refinement on the basis of statistics of continued use. In part one, the system creates a query through a computer–user dialog. The user comes to the system with the question ‘‘What can you tell me about this?’’. The goal of the system is to define this in terms of the data in the database and construct a query dependent on the information available. For example, the user may want information about deviant behavior. The system would then indicate that it has a variety of information currently in the database concerning the general topic of deviant behavior and the specific topics of violence, sexual deviance, and criminal activities. The system finds this information by referencing the system thesaurus, using broader, narrower and synonymous terms, and data currently residing in the DIS database. It is possible that there are additional narrower terms for deviant behavior not included in DIS, such as corruption, but since information does not currently exist in the database concerning corruption, that term is not shown to the user. If at a later date, information concerning corruption is added to the database, then this term will be displayed.

The interface system bases its rules on the main categories and subcategories of the database.

The system requests information from the user on their field or perspective and then uses this information to help find the data that is of interest to them. For example, if the user is in law enforcement and selects the topic cocaine usage, the system will focus the search on areas such as criminal sentencing and crime rates. However, the same query from a social worker would cause the system to focus on topics such as violence in the family, effects of cocaine use and socioeconomic class, and treatment outcomes.

Through an extended dialog with the user, the system arrives at a problem description that consists of a free text description, search topics, user perspective, and a set of problem qualifiers, such as desired document types, recall amount, and depth of search (e.g. searching on titles, keywords, abstracts, or combinations of fields).

Based on the formulation of this conceptual topic, a search list is constructed. The rule base of the expert system establishes the search parameters. This set was formulated on a combination of drug-related thesauri that have already been developed and keywords used in the database. The search is performed on fields specified by the user. If he or she elects to enter a free text description, the description will be filtered for search terms and these will then be used as the key for the search, using the root and the Spanish translation, if applicable. The user can request a broad search, which examines all fields within the database, or a more restricted search based on keywords only. Search topics and user perspectives are used to construct a list of terms based on those selected by the user, their thesaurus definitions (e.g. broader, narrower, related and synonyms), and the Spanish translations of the terms. The results are presented in the order that the system determines most valuable. The user can modify his or her search and reconstruct the topic based upon the results. The goal is to enable the user to view the results of the search and respond, ‘‘I would like to see documents like to this one’’, or ‘‘None of the documents are adequate. . .’’. The user can also obtain a rough English translation of abstracts, titles, etc. that were input in Spanish.

The final part of the system concerns refinement on the basis of statistics of continued use, i.e. statistical learning. This means that the system contains its own database and logs statistics concerning the requests and results of its sessions. These statistics are then used to refine answers.

## 3. Methodology

The main requirement of the prototype is that it assists novice users in retrieving relevant information. Based on the literature search and user characteristics, it was determined that the prototype should utilize a domain-driven approach and build upon existing intelligent information retrieval methodologies. A summary of the design parameters and a justification for the approach selected is provided.

The prototype builds upon the techniques of intelligent information retrieval and incorporates a statistical-based approach to term weighting. This approach has been effective in several web applications, including the Thomas system supported by the Library of Congress. Until recently, most commercially available ‘‘front ends’’ of database information retrieval systems have not been very intelligent. Although, vendors assert that their products assist the user in the various steps of online searching by incorporating the expertise of trained, experienced, search intermediaries, most of them are limited to providing assistance in areas that are not especially valuable for subject searching of online systems (e.g. automatic dial-up, login, database selection, and query translation into the host system’s command language). The majority of these front ends do no more than automate the routing and query language conversions performed by intermediaries.

During the last 6 years, a new wave of commercially available products have come on the scene. These include data miners, such as IBM’s Intelligent Miner Toolkit, Powersoft’s InfoMaker, and Crystal Service’s Crystal Reports. Because these information-discovery systems have only recently gained widespread attention, they tend to be more suited for analysts with strong mathematical or statistical backgrounds and are limited in their targeted databases. Within a relatively short time, we expect to see better user interfaces, especially intelligent information agents. Commercial vendors are also beginning to offer some non-Boolean searching interfaces, such as West Publishing’s Win, Mead Data’s Freestyle, Verity, Inc.’s TopicSearcher and Search97, Bellcore’s Latent Semantic Indexing

System, and HNC’s Match Plus System. These packages are being incorporated into Web Browsers.

Our prototype builds on techniques that have been developed in the area of intelligent information retrieval, such as term weighting, term stemming, query expansion, and relevance feedback. These techniques have been the focus of a great deal of research and have been shown to produce better retrieval sets than traditional Boolean systems.

## 3.1. Query expansion

Query expansion involves finding synonyms for the terms in the query and either allowing the user to select from and add them or include all the synonyms automatically. This has been found to result in larger relevant retrieval sets. A similar type of query expansion involves displaying related terms to the user and permitting them to select those that they would like to include. This was shown to be effective in systems, such as CANSEARCH and CITE. Additional terms are included in the query through the Boolean ‘‘or’’. Since the DIS system is multilingual and has a large number of synonymous keywords (due to its clearinghouse nature), the query expansion technique for the prototype involves both automatic inclusion of synonyms and user selection of related terms. Term weighting was used for related and synonymous terms. The prototype also includes both broader and narrower terms, based on the system thesaurus. This is intended to eliminate the need to manually broaden or narrow the search: users often have trouble performing this operation. By using term weighting, records containing broader or narrower definitions of a user-selected term will only be retrieved when there is no exact match.

## 3.2. Term stemming

Stemming is the technique used to remove common word endings, such as -s and -ed during query processing. Once these have been removed, the system can retrieve documents containing variants of the query words. Stemming has been shown to improve system effectiveness. One of the most effective stemming algorithms consists of rules that remove increasingly large parts of the word ending. However, this can result in irrelevant retrieval, for example using this algorithm both ‘‘policy’’ and ‘‘police’’ stem to ‘‘polic’’. Therefore, the prototype builds on Croft’s Inquiry system, which uses term weighting to reduce irrelevant retrieval.

## 3.3. Relevance feedback

Relevance feedback has been shown to improve recall dramatically. It allows the user to view documents and ask the system to find similar ones. Rather than explicitly generating new searches, all the user has to do is recognize relevant material. The method then provides users a way to effectively expand their queries with minimal effort. This approach comes from the knowbot technique and a research effort by Think Machines of Cambridge, MA, called wide area information servers (WAIS). WAIS presents result to the user and allows them to scan document titles to determine which are most appropriate; through the similar to function, the user requests WAIS to retrieve information similar to the one chosen. Since the users will not always have a definitive goal when structuring their query, it is essential that the prototype include this ability.

## 3.4. Domain-driven approach

The decision was made to incorporate a domaindriven approach. The targeted users are infrequent users, and as such they do not have a good understanding of the information in the database. This makes it very difficult to perform effective searches. Also, users typically approach the system with ill-defined requests. Research has shown that a knowledge-based IS outperform a traditional system, because of its search heuristics, knowledge about the subject area, classification scheme, and query mechanisms [5]. Since the success of online systems depends on both the searching expertise of the user and the users’ knowledge of the subject domain, many researchers and developers have recognized the importance of building systems that are knowledgeable about the subject area of the domain [7]. However, the successful implementation of such systems has been very limited due to the need for domain knowledge.

The prototype attempts to solve this problem by developing a rule base that contains knowledge about the subject area, based on the system thesaurus, which maps terms to document indexing through synonyms. This can also overcome the multilingual aspect of the data. The prototype allows the user to select top-terms from a list of the main thesaurus. The next step consists of selecting more specific ones from a graphical tree menu showing the thesaurus from broader to narrower. This idea has been used successfully in a number of prototypes, such as Croft’s I<sup>3</sup>R System and the KIM project at the University of Aberdeen, Scotland.

Our prototype goes beyond these systems by requiring a thesaurus term to match either exactly or be synonymous to an indexed term before it is displayed to the user. The prototype system categorizes users by their perspective: users view the same information differently, based upon their functions.

## 3.5. Statistical learning

A desirable characteristic is to generate system refinement-based statistics found through continued use. A new approach, recommendation-based systems, is being employed successfully in virtual electronic communities. This method collects recommendations (ratings) from a community of users, and selects an item by finding what people have liked in the past. These systems do not depend on content analysis.

Our prototype statistical learning feature builds on the concepts used in such systems by enabling ratings from similar types of users to influence document selection.

## 4. System overview

The IDA system allows users to specify the information they need, and then to refine and modify their search in a variety of ways. It enhances both the precision and recall of the search by eliminating retrieval of too much or too little information and reduces retrieval of non-relevant information. The system is domain driven, because the topics presented for user selection depend on the data in the DIS database. An expert-driven portion of the system involves: matching DIS keywords to the IDA thesaurus, synonym matching, Spanish/English term translation, assessing document relevance through a scoring procedure, search modification and additional document retrieval. Figs. 1 and 2 illustrate the flow of the IDA program.

![](/api/attachments/NDXMECBR/fulltext/images/ea54e2d90148df782f5f6510271979fc687924426c39c874383d428a987ba77b.jpg)  
Fig. 1. IDA program flow.

## 4.1. User-defined parameters

The user is asked to specify the number of documents desired for review (recall) and the DIS fields to search (depth).

## 4.2. Methodology for data retrieval

The system retrieves data in three ways: user perspective; thesaurus topic areas; search description.

## 4.2.1. User perspective

The user is asked to choose from a number of fields (including not applicable). This perspective is used to focus the search and retrieval of documents. If the users’ perspective has any thesaurus terms related to it, the system will ask the user if they would like to include these terms. Related terms and perspectives are searched on the terms, synonyms, and Spanish translations.

![](/api/attachments/NDXMECBR/fulltext/images/35650c0f213eedc39c2d060cfc298db5ad0cf613073c7eebb1e1830d9f09e445.jpg)  
Fig. 2. IDA program elements.

## 4.2.2. Thesaurus topic areas

The system allows the user to choose from the main thesaurus topic areas of the DIS database. For a given topic, the system will construct a menu tree based on the thesaurus definition of the term and data currently available in the database. The user selects a search topic from the menu tree. The system searches for the topic, utilizing the thesaurus approach to retrieve records, based on broader, narrower, and synonymous definitions of the topic. If the selected topic has any thesaurus terms related to it, the system asks the user if they would like to include these terms.

## 4.2.3. Search description

The user can elect to describe the search objective by completing the sentence, I would like information concerning. . ., in 20 words or less. The system parses this sentence to filter all applicable search terms. These ‘‘description terms’’ are used to search the database. The system also searches on Spanish translations and the English and Spanish root for each term. The search depth is used to describe the database fields searched for descriptive terms. The user can choose to search on any combination of the title, keywords, or abstract fields.

## 4.3. Document recall

The documents recalled are each given a score based upon their conformity to the search parameters as well as the document rating for a given perspective. The system will retrieve the full document information from DIS for the number of documents requested by the user. The documents will then be presented for review in the order that the system determines most useful.

## 4.4. Document presentation

The user can browse through the documents selected by the system. There are a number of options available:

1. view a rough English translation;

2. display document retrieval justification and score;

3. print/download records;

4. retrieve additional documents similar to a retrieved record;

5. retrieve additional documents using current search parameters;

6. search for modifications based on user perspective and thesaurus topics;

7. search for modifications based on search description.

## 4.5. User session summary

When the user elects to modify the search parameters or exit the system, he or she is given the option of obtaining a session summary. This provides a final synopsis of the user perspective, search description, search topics, and a listing of the document retrieved.

## 4.6. Statistical learning

When exiting from the system, the user can evaluate the results of the search. He or she will be asked to rate the documents retrieved on a scale of 0–10, with 10 being best. The system uses the document rating to calculate a score for the records, using a moving average. This is stored with the record to enable a user with the same perspective and similar topics to benefit from previous user experience.

## 5. Evaluation

Two categories of evaluation techniques were used: empirical and system tests.

## 5.1. System evaluation

System testing was performed to examine (1) the logical accuracy and sufficiency of the knowledge base, (2) the completeness and predictive consistency of the knowledge base, and (3) the adequacy of the inference engine. Adelman suggests that since the knowledgebased systems often traverse chains of if–then rules, if the if–then rules are treated as logical expressions, it is possible to check the rules for logical errors [2]. Manual tests for rule anomalies and knowledge base completeness were tested throughout the design process. In particular, testing evaluated the use of a system thesaurus to perform query expansion and retrieve relevant records based on multilingual, synonymous, broader and narrower term definition, the ability to perform relevance feedback, the statistical learning feature, the update process, term weighting, and term stemming. Using printouts of the DIS index terms, and DIS records, along with the ISDD thesaurus, probable solutions were derived for hypothetical queries. The system was then tested using the queries. The system solutions were compared to the probable solutions and checked for precision and recall. When there was more than a slight discrepancy, the knowledge and rule base were examined and, as necessary, modified.

The purpose of the testing was for verification, finding mistakes and omissions in the rule base, and developing extensions to the rule base. To make this a feasible evaluation method, hypothetical queries focused on bounded subject areas, where the corresponding record data was relatively small. Since the systems ability to process large amounts of data exceeds the human ability, it was judged that the system was functioning properly if it could function adequately on bounded queries. ‘‘Non-bounded’’ queries (those concerning a large number of records) were tested for reasonableness of the responses.

## 5.2. Empirical evaluation

Empirical methods were used for testing attributes that require judgment. These include performance and usability. In the evaluation of a knowledge-based system, subjective methods are necessary for assessing the system from the users’ perspective.

## 5.3. Experimental design

A questionnaire was developed to record users opinions of the IFE system versus a traditional system. This questionnaire was consistent with recommendations by Adelman and Ulivila [1], focusing on ease of use, willingness to utilize the systems, and perceptions concerning task performance. Total 32 subjects, 25 George Washington University students, three George Washington University library personnel, and four DIS staff members participated in the experiment.

Step 1. The participant was led through an example session using the IDA interface.

Step 2. The participant performed a search using it. Step 3. The participant was led through an example session using the Micro CDS/ISIS interface.

Step 4. The participant performed a search using it.

Step 5. The participant completed the questionnaire.

## 5.4. Evaluation criteria

Each of the questions had five response options (1: low; 5: high).

## 5.4.1. General questions

G1. Ease of use.

G2. Amount of preparation/documentation needed to conduct the first search.

G3. General feelings of satisfaction.

G4. Willingness to use the system again.

G5. Overall performance (recall and precision).

## 5.4.2. Specific criteria

S1. Ability to communicate domain information (type of data contained in the database).

S2. Search strategy development.

S3. Multilingual capabilities (user interface, search terms, and/or display formats.

S4. Presentation of query results.

S5. Search modification.

S6. Search results after initial search (extent to which documents presented satisfy search parameters).

S7. Search results after search modification (extent to which documents presented satisfy search parameters).

S8. System features.

## 5.5. Hypotheses

The following null hypotheses were developed for the system evaluation. Each corresponds to one of the evaluation criteria.

Hypothesis 1. The users’ perceptions concerning ease of use are not significantly different for the IDA system and the traditional system (G1).

Hypothesis 2. The amount of preparation/documentation needed to conduct the first search does not differ significantly between the IDA system and the traditional systems (G2).

Hypothesis 3. There is no significant difference in the users’ general feelings of satisfaction for using the IDA system and the traditional system (G3).

Hypothesis 4. There is no significant difference in the users’ willingness to use the ID system or the traditional system again (G4).

Hypothesis 5. Users do not indicate any significant difference in the overall performance (precision and recall) of the IDA system and the traditional system (G5).

Hypothesis 6. There is no significant difference in the ability to communicate domain information between the IDA system and the traditional system (S1).

Hypothesis 7. There is no significant difference in the users’ preference for search strategy formulation in the IDA system and the traditional system (S2).

Hypothesis 8. Users do not indicate any significant difference in the multilingual capabilities of the IDA system and the traditional system (S3).

Hypothesis 9. Users do not indicate any significant difference in the presentation of query results of the IDA system and the traditional system (S4).

Hypothesis 10. There is no significant difference in search modifications for the IDA system and the traditional system (S5).

Hypothesis 11. Users do not indicate any significant difference in their search results after initial search between the IDA system and the traditional system (S6).

Hypothesis 12. Users do not indicate any significant difference in their search results after search modification between the IDA system and the traditional system (S7).

Hypothesis 13. There is no significant difference between the system features of the IDA system and the traditional system (S8).

## 5.6. Results

This section presents the results obtained from the subjective evaluation. The paired difference tests were calculated using $H _ { \mathrm { o } } : \mu _ { 1 } - \mu _ { 2 } = 0$ and $H _ { \mathrm { a } }$ $\mu _ { 1 } - \mu _ { 2 } > 0 .$ . The results of the statistical analysis are presented in Tables 1 and 2. All of the null hypotheses were rejected.

## 5.7. Conclusions

Users ranked the IDA system higher than the traditional one for each of the criteria evaluated. In general, based on the rejection of the null hypotheses for G1, G2, G4 and S8, we feel that the IDA system can be considered more usable than the traditional one.

The rejection of the null hypotheses for G3, G5, S6 and S7 suggests that the IDA system achieved higher levels of performance. The rejection of the null hypothesis for S1, S2, S3, S4 and S5 suggests that users preferred the IDA system.

## 6. Findings of the research

The purpose of this research was to develop an intelligent front end IDA for a traditional catalog system. The focus was on creating a system that uses domain knowledge to assist users in developing a problem specification limited to information that is contained in the system. It was a requirement that the system be able to run using minimum computer resources.

This research developed a methodology for mapping existing thesauri and indexed terms from a bibliographical database to a ‘‘system thesaurus’’,

Table 1  
Statistics for general criteria question

<table><tr><td></td><td>Question</td><td>Mean</td><td>S.D.</td><td>95% CI</td><td>Hypothesis</td><td>Test statistic</td><td>Significance level (P)</td></tr><tr><td rowspan="3">G1</td><td>System 1 (IDA)</td><td>4.09</td><td>0.09</td><td>[3.79, 4.42]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td>t=7.28</td><td>&lt;0.001</td></tr><tr><td>System 2 (traditional)</td><td>2.31</td><td>0.97</td><td>[1.96, 2.66]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td></td><td></td></tr><tr><td>System 1 – system 2</td><td>1.78</td><td>1.39</td><td>[1.28, 2.28]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">G2</td><td>System 1 (IDA)</td><td>4.06</td><td>0.72</td><td>[3.80, 4.32]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td>t=7.43</td><td>&lt;0.001</td></tr><tr><td>System 2 (traditional)</td><td>2.44</td><td>0.98</td><td>[2.08, 2.79]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td></td><td></td></tr><tr><td>System 1 – system 2</td><td>1.63</td><td>1.24</td><td>[1.18, 2.07]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">G3</td><td>System 1 (IDA)</td><td>4.47</td><td>0.62</td><td>[4.25, 4.69]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td>t=8.54</td><td>&lt;0.001</td></tr><tr><td>System 2 (traditional)</td><td>2.64</td><td>1.13</td><td>[2.23, 3.02]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td>F=3.30</td><td>&lt;0.005</td></tr><tr><td>System 1 – system 2</td><td>1.84</td><td>1.221</td><td>[1.40, 2.28]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">G4</td><td>System 1 (IDA)</td><td>4.47</td><td>0.62</td><td>[4.25, 4.69]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td>t=6.82</td><td>&lt;0.001</td></tr><tr><td>System 2 (traditional)</td><td>2.95</td><td>1.16</td><td>[2.52, 3.36]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td></td><td></td></tr><tr><td>System 1 – system 2</td><td>1.53</td><td>1.27</td><td>[1.07, 1.99]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">G5</td><td>System 1 (IDA)</td><td>4.22</td><td>0.61</td><td>[3.99, 4.44]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td>t=8.54</td><td>&lt;0.001</td></tr><tr><td>System 2 (traditional)</td><td>2.41</td><td>1.04</td><td>[2.03, 2.78]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td>F=2.94</td><td>&lt;0.005</td></tr><tr><td>System 1 – system 2</td><td>1.81</td><td>1.15</td><td>[1.40, 2.23]</td><td></td><td></td><td></td></tr></table>

Table 2  
Statistics for specific criteria questions

<table><tr><td></td><td>Question</td><td>Mean</td><td>S.D.</td><td>95% CI</td><td>Hypothesis</td><td>Test statistic</td><td>Significance level (P)</td></tr><tr><td rowspan="3">S1</td><td>System 1 (IDA)</td><td>3.90</td><td>0.91</td><td>[3.57, 4.24]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td></td><td></td></tr><tr><td>System 2 (traditional)</td><td>2.29</td><td>1.01</td><td>[1.90, 2.68]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td>t=5.82</td><td>&lt;0.001</td></tr><tr><td>System 1 – system 2</td><td>1.61</td><td>1.54</td><td>[1.05, 2.18]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">S2 (average rating/system)</td><td>System 1 (IDA)</td><td>4.13</td><td>0.59</td><td>[3.91, 4.34]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td>t=6.49</td><td>&lt;0.001</td></tr><tr><td>System 2 (traditional)</td><td>2.61</td><td>1.16</td><td>[2.19, 3.04]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td></td><td></td></tr><tr><td>System 1 – system 2</td><td>1.55</td><td>1.33</td><td>[1.06, 2.04]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">S3</td><td>System 1 (IDA)</td><td>4.10</td><td>0.94</td><td>[3.75, 4.46]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td></td><td></td></tr><tr><td>System 2 (traditional)</td><td>2.66</td><td>1.20</td><td>[2.20, 3.11]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td>t=6.64</td><td>&lt;0.001</td></tr><tr><td>System 1 – system 2</td><td>1.46</td><td>1.29</td><td>[0.96, 1.97]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">S4</td><td>System 1 (IDA)</td><td>4.09</td><td>0.78</td><td>[3.81, 4.37]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td></td><td></td></tr><tr><td>System 2 (traditional)</td><td>2.78</td><td>1.26</td><td>[2.33, 3.24]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td>t=7.42</td><td>&lt;0.001</td></tr><tr><td>System 1 – system 2</td><td>1.31</td><td>1.47</td><td>[0.78, 1.84]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">S5</td><td>System 1 (IDA)</td><td>4.09</td><td>0.82</td><td>[3.80, 4.39]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td></td><td></td></tr><tr><td>System 2 (traditional)</td><td>2.31</td><td>1.20</td><td>[1.88, 2.75]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td>t=6.64</td><td>&lt;0.001</td></tr><tr><td>System 1 – system 2</td><td>1.78</td><td>1.52</td><td>[1.23, 2.33]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">S6</td><td>System 1 (IDA)</td><td>4.06</td><td>0.88</td><td>[3.75, 4.38]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td></td><td></td></tr><tr><td>System 2 (traditional)</td><td>2.47</td><td>0.98</td><td>[2.11, 2.82]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td>t=7.42</td><td>&lt;0.001</td></tr><tr><td>System 1 – system 2</td><td>1.60</td><td>1.21</td><td>[1.16, 2.03]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">S7</td><td>System 1 (IDA)</td><td>4.06</td><td>0.80</td><td>[3.77, 4.35]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td></td><td></td></tr><tr><td>System 2 (traditional)</td><td>2.46</td><td>1.17</td><td>[2.01, 2.92]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td>t=5.89</td><td>&lt;0.001</td></tr><tr><td>System 1 – system 2</td><td>1.50</td><td>1.35</td><td>[0.98, 2.02]</td><td></td><td></td><td></td></tr><tr><td rowspan="3">S8</td><td>System 1 (IDA)</td><td>4.16</td><td>0.81</td><td>[3.87, 4.45]</td><td> $H_o: \mu_1 - \mu_2 = 0$ </td><td></td><td></td></tr><tr><td>System 2 (traditional)</td><td>2.57</td><td>1.10</td><td>[2.15, 2.10]</td><td> $H_a: \mu_1 - \mu_2 > 0$ </td><td>t=7.18</td><td>&lt;0.001</td></tr><tr><td>System 1 – system 2</td><td>1.63</td><td>1.25</td><td>[1.17, 2.10]</td><td></td><td></td><td></td></tr></table>

which operated as a semantic network, representing the derivations in thesauri and indexed terms as synonyms.

This approach was applied to a specific problem, the DIS database, which focuses on drug information. The methodology developed here could be easily adapted to any online catalog with a finite domain for which thesauri exist or can be developed for a major topic area.

The system was evaluated in a randomized experiment. This evaluation determined that the system met or surpassed all goals. Users compared the process of retrieving information from the DIS database with the IDA system and the traditional system directly. For each of the criteria, the ratings for retrieval using IDA were statistically better than the ratings for retrieval without IDA.

The strong positive results of this research indicate that systems that incorporate a domain-driven approach increase the productivity of user searching.

During the experiment, all of the participants followed the same procedure: using the IDA system first and the traditional system second. Also subjects were allowed to select their own topics for searching. It would be interesting to determine if either of these factors would have made a difference in the outcomes of the experiment.

The experiment was conducted with only 32 subjects. This was due mainly to constrained access to the traditional system (DIS). The subjects chosen were simply those at hand during the time available. The experiment did not take into consideration the subjects’ previous knowledge of database systems and Boolean logic, or their experience in conducting online searches. It is reasonable to assume that the librarians knew more about searching and that the DIS staff knew more about the content of the catalog.

Due to the very small number of non-students, separate analysis were not conducted for each category (i.e. students, librarians, staff members).

## References

[1] L. Adelman, J.W. Ulivila, Evaluating expert system technology, in: S.J. Andriole, S.M. Halpin (Eds.), Information Technology for Command and Control: Methods and Tools for Systems Development and Evaluation, IEEE Press, New York, pp. 537–547.

[2] L. Adelman, Evaluating Decision Support and Expert Systems, Wiley, New York, 1992.

[3] M.J. Bates, Rethinking subject cataloging in the on-line environment, Library Resources and Technical Services 33 (4), 1989, pp. 400–411.

[4] A.Y. Chamis, Online Database Search Strategies and Thesaural Relationship Models (Vocabulary Switching, Compatibility), Dissertation, Case Western Reserve University, Cleveland, OH, 1984, DAI-2287.

[5] H. Chen, An Artificial Intelligence Approach to the Design of Online Information Retrieval Systems, Dissertation, Graduate School of Business Administration, New York University, New York, 1990.

[6] S.E. Doyen, Effects of Conceptual Instruction on Subject-Searching Performance in a Computerized Library Catalog (On-Line Catalog Search), Dissertation, University of Cincin nati, Cincinnati, OH, 1989, DAI-3399.

[7] B. Nielsen, What they say they do and what they do, Information Technology and Libraries 5 (1), 1986, pp. 28–29.

[8] G.R. Notess, Search engines in the Internet age, Online 23 (3), 1999, pp. 20–22.

![](/api/attachments/NDXMECBR/fulltext/images/c303118f571da2176d2babce793599d17db39cd4f06834a4fd8276ee0f15348f.jpg)  
Theresa I. Jefferson is an assistant Prof. of engineering management and systems engineering at the George Washington University. Her research, teaching, and consulting has emphasized strategic information systems, electronic commerce, intelligent information retrieval, information visualization, and systems engineering.

![](/api/attachments/NDXMECBR/fulltext/images/9bb47e3dd4956a7e061549135d562e1af992ab22d3e1859e6ec8ce5547898046.jpg)

Thomas J. Nagy is an associate Prof. of expert systems in the Management Science Department at the George Washington University. His educational background includes a PhD from the University of Texas at Austin, 2 years as a research fellow at University of California, Berkeley, and as a postdoctoral fellow in public health at Johns Hopkins University. His research interests include human factors, user interfaces and motivation and persuasion.
