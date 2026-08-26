---
otero_id: 13758
otero_key: "JS3XWQ5A"
title: "Using Web resources to construct multilingual medical thesaurus for cross-language medical information retrieval"
authors: "Wen-Hsiang Lu; Ray S. Lin; Yi-Che Chan; Kuan-Hsi Chen"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.07.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Using Web resources to construct multilingual medical thesaurus for cross-language medical information retrieval

Wen-Hsiang Lu <sup>a,⁎</sup>, Ray S. Lin <sup>b</sup>, Yi-Che Chan <sup>a</sup>, Kuan-Hsi Chen <sup>a</sup>

<sup>a</sup> Department of Computer Science and Information Engineering, National Cheng Kung University, Taiwan <sup>b</sup> Stanford Medical Informatics, Stanford, CA, United States

Available online 27 July 2007

## Abstract

Due to the language barrier, non-English users are unable to retrieve the most updated medical information from the U.S. authoritative medical websites, such as PubMed and MedlinePlus. However, currently, there is no any cross-language medical information retrieval (CLMIR) system that can help Chinese-speaking consumers cross the language barrier in finding useful English medical information. A few CLMIR systems utilize MeSH (Medical Subject Headings) to help overcome the language barrier. Unfortunately, the traditional Chinese version of MeSH is currently unavailable.

In this paper, we employ a semi-automatic term translation method to construct a Chinese–English MeSH by exploiting abundant multilingual Web resources, including Web anchor texts and search–result pages. Through this method, we have developed a Chinese–English Mesh Compilation System to assist knowledge engineers in compiling a Chinese–English medical thesaurus with more than 19,000 entries. Furthermore, this thesaurus has been used to develop a prototypical system for crosslanguage medical information retrieval, MMODE, which can help consumers retrieve top-quality English medical information using Chinese terms.

© 2007 Elsevier B.V. All rights reserved.

Keywords: Cross-language medical information retrieval; Multilingual medical thesaurus; Web mining; Web anchor text; Search–result page

## 1. Introduction

A number of Web resources provide the public and healthcare professionals with the most up-to-date findings in medical research, such as PubMed and MedlinePlus. Although access to such top-quality resources is free and unlimited for users all around the world, most of these resources are available in English only. Non-English users therefore often encounter a great language barrier when trying to access medical information from these websites. In addition, most non-English consumers are not familiar with medical terminology even in their first (native)

language. This raises the language barrier even higher in medical information retrieval. For example, most Chinese consumers know the Chinese layperson's term “ ” (dementia for aged people) but not the medical term “ ” (Alzheimer's disease). Currently, it is almost impossible for such consumers to retrieve healthcare information they need from Medline-Plus. Thus, matching Chinese medical terms, especially layperson's terms, to English medical terms becomes a critical challenge in assisting non-English users in finding useful medical information. Unfortunately, there is no system that provides Chinese–English cross-language medical information retrieval (CLMIR) now.

A multilingual medical thesaurus plays a crucial role in CLMIR according to the experience of the CliniWeb [9] and other CLMIR systems [20,21]. In 1998, Hersh et al. [9] designed a multilingual concept-matching system, called SAPHIRE International, which utilizes the non-English terms in the Unified Medical Language System (UMLS) Metathesaurus derived from multilingual MeSH, to allow users to enter query terms in non-English languages (German, French, Russian, Spanish and Portuguese) to find English clinical Web pages in CliniWeb. Besides this, the MuchMore<sup>1</sup> project also developed a prototypical system for cross-lingual information organization and access in the medical domain. Several methods in this project were developed for enriching a multilingual medical thesaurus from a general dictionary, a specialized multilingual thesaurus (MeSH), and comparable corpora [6].

Until now, most existing medical thesauri have been manually compiled. However, manual lexicography is time-consuming and not cost-effective. MeSH is the most significant medical thesaurus in English and has been manually translated into many languages, but the Traditional Chinese version of MeSH is still not available. In this paper, we employ an effective Webbased term translation method to semi-automatically map Chinese medical terms to MeSH and construct a bilingual medical thesaurus for Chinese–English CLMIR [16]. Fortunately, we have compiled over 19,000 entries (about 42,000 concepts in MeSH) for the Chinese–English MeSH, via translation of English medical terms in MeSH into Chinese using an integrated Web-based term translation method. In past years, we have proposed an integrated Web-based method that explores two kinds of Web resources, i.e. Web anchor texts [14,15] and search–result pages [22] to effectively alleviate the problems of multilingual translation for diverse unknown (new) Web query terms. In this present study, there are two major goals. First, we expect that the presented semi-automatic term translation method is able to help knowledge engineers reduce manual effort in the difficult task of compiling a Chinese–English MeSH. Second, we utilize the Chinese–English MeSH to develop a practical CLMIR system that can assist laypersons in the retrieval of top-quality English medical information by submitting Chinese terms.

## 2. Related works

## 2.1. Monolingual term mapping

For monolingual medical information retrieval, laypersons often encounter a problem in that their search terms are not always compatible with the professional terms found in medical documents. A number of research projects have focused on dealing with such a problem [5,11,13]. Leroy and Chen have developed a Medical Concept Mapper to help users find medical information by providing them with appropriate medical search terms. However, currently, the problems of cross-language term mapping have not been emphasized in the medical domain.

## 2.2. Parallel-corpus-based term translation

In the research area of machine translation (MT), a number of works have often used statistical techniques to automatically extract term translations from parallel text corpora, which contain aligned bilingual sentence pairs [8]. Although this method can achieve high translation accuracy, the unavailability of large-size parallel corpora in the medical domain is still a difficult problem.

## 2.3. Comparable-corpus-based term translation

Less attention has been devoted to extracting term translation from comparable corpora, which contains texts with similar topics collected independently in respective language communities. Fung and Yee [7] used a vector–space model and took a bilingual lexicon (called seed words) as feature sets to estimate the similarity between a word and its translation candidates. Chiao and Zweigenbaum [4] adopted a similar method to find French–English translation equivalents for new medical terms. Comparable corpora are easier to obtain now. However, how to achieve better performance for higher translation coverage is still a challenging task.

2.4. Query translation in cross-language information retrieval

In early works in the field of cross-language information retrieval (CLIR), dictionary- and MT-based approaches were pervasively employed by some CLIR systems [10,18]. However, these techniques usually achieved unsatisfactory results due to their limitations, such as phrase translation and translation ambiguity [1,2]. Kwok proposed a unique work combining dictionary-, MT- and corpus-based approaches [12]. His combined approach achieved good performance for long queries, but worse results for short “title” queries. As he pointed out, a prominent factor for CLIR failure was due to the lack of existing translations of unknown key terms.

Another major approach to dealing with query translation is based on the corpus-based approach which uses parallel/comparable corpora to extract translations [23]. Although certain domain-specific translations can be extracted by these techniques, the unavailability of adequate parallel corpora for various subject domains and multiple languages is still a major problem. To alleviate such problem, Nie et al. [17] developed some feasible techniques for automatically extracting parallel pages from bilingual/multilingual Web sites. They used search engines to find potential candidates by the clues that certain terms embedded in the link's anchor text often indicate the language of the linked page, and the fact that parallel text pages usually have similar file names and text length. Their techniques can provide a simpler and more reasonable way to construct general parallel corpora for diverse subject domains. Other works also took link structures into consideration when selecting candidates of parallel pages [19,24]. However, it is still not easy to collect large amounts of parallel corpora in the medical domain.

## 2.5. Web-based term translation

As mentioned above, the conventional methods suffer from the problems in the lack of large-size parallel corpora and in the shortage of translation coverage of comparable corpora in the medical domain. On the one hand some researchers have developed feasible techniques for automatically collecting parallel pages from bilingual websites [17,19,24], and, on the other hand, some researchers have tried to explore other Web resources. First, we have utilized two kinds of Web resources: Web anchor texts [14,15] and search–result pages [3,22] as comparable corpora. Web anchor texts are effective for extracting translations of popular terms whereas search result pages are useful to extract translations of unknown terms. Both Web resources are thus complementary in accuracy and coverage rate for extraction of multilingual translations, and fortunately, are easy to be obtained. Zhang and Vines [25] also exploited search result pages to translate unknown terms.

In this paper, we try to employ an integrated Webbased method to effectively deal with cross-lingual mapping of medical terms from Web anchor texts and search result pages. In the following sections, we will introduce these two kinds of Web resources and describe how to effectively utilize these resources.

## 3. Semi-automatic construction of multilingual medical thesaurus

Fig. 1 shows the architecture of the integrated Webbased term translation method through mining Web anchor texts and search–result pages for semi-automatically compiling the Chinese–English MeSH and developing a CLMIR system.

## 3.1. Anchor-text mining

## 3.1.1. Anchor text

An anchor text is the descriptive part of an out-link of a Web page used to provide a brief description of the linked Web page. There are a variety of anchor texts in multiple languages that might link to the same pages from all over the world. For a source (unknown) term appearing in the anchor text of a Web page, it is likely that its corresponding target translations may appear together in other anchor texts linking to the same page.

![](/api/attachments/JS3XWQ5A/fulltext/images/c87ec389ebcd7a4f058de3c8f23b60d69261df434584d9e793d8b0c7226b99fd.jpg)  
Fig. 1. The architecture of constructing multilingual medical thesaurus using Web resources.

Such a bundle of anchor texts pointing together to the same page is called as an anchor-text set.

## 3.1.2. Mining procedure

(1) Corpus collection: To make good use of Web anchor texts, we collected 1,980,816 traditional Chinese Web pages in Taiwan, and then extracted 109,416 pages (URLs), whose anchor–text sets contained both traditional Chinese and English terms, as the anchor–text-set corpus for extraction of the Chinese–English translation of medical terms.

(2) Translation candidate extraction: Three keyword extraction methods have been used to extract Chinese key terms from anchor–text corpus: PATtree-based, Query-log-based, and Tagger-based methods [6]. After key term extraction we select top k (k = 50) high-frequency terms as translation candidates.

(3) Translation selection: Use anchor-text mining to estimate the similarity based on the following model.

## 3.1.3. Probabilistic inference model

Based on a multilingual anchor-text corpus, we may determine the probable target translations for a source term by using a probabilistic model. This model assumes that a translation candidate had a higher chance of being a translation only if it frequently co-occurred with the source term in the same anchor text sets. Furthermore, it assumes that the translation candidates in the anchor texts of the pages with higher authority may be more reliable. Hence, the similarity between a source English term E and a Chinese translation candidate C was estimated as:

$$
\begin{array}{l} S _ {A T} (\mathrm{E}, \mathrm{C}) \\ = \frac {\sum_ {i = 1} ^ {n} P (\mathrm{E} | U _ {i}) P (\mathrm{C} | U _ {i}) P (U _ {i})}{\sum_ {i = 1} ^ {n} [ P (\mathrm{E} | U _ {i}) + P (\mathrm{C} | U _ {i}) - P (\mathrm{E} | U _ {i}) P (\mathrm{C} | U _ {i}) ] P (U _ {i})}, \end{array}\tag{1}
$$

where $U _ { i }$ represents a web page, $P ( U _ { i } )$ is the probability used to estimate the authority of $U _ { i } ,$ and its definition is $P ( U _ { i } ) = L ( U _ { i } ) / \Sigma _ { j = I , n } \ L ( U _ { j } )$ , where $L ( U _ { j } )$ indicates the number of in-links of page $U _ { j } .$ The values of $P ( \mathrm { E } | U _ { i } )$ and $P ( \mathrm { C } | U _ { i } )$ were estimated by calculating the probability of E and C appearing in the anchor-text set of the $U _ { I } { \bf \bar { s } } ,$ , respectively. The probabilistic inference model was proposed to model the authority of pages, which cannot be represented by conventional methods and yet was shown to be important in increasing the accuracy of term translation [15].

## 3.2. Search-result mining

Even if we can collect large numbers of pages from the Web and build up a corpus of anchor-text sets, the translation coverage of diverse query terms is still limited to our collected corpus. To enhance the coverage rate of term translation in medicine domains, we have exploited search-result pages.

To explore Web search results, we utilize co-occurrence relations and context information between a source English term and Chinese translation candidates to enhance the coverage rate of translation extraction of unknown terms. We adopted the chi-square test and context-vector analysis that could achieve better performance.

## 3.2.1. Search–result pages

According to our observations, many Chinese search– result pages from search engines contain rich snippets of summaries with a mixture of Chinese and English texts. Therefore, when we search explicitly for English terms (e.g. “Alzheimer's disease”) in Chinese-language pages from Google, it is likely that the search result will include relevant snippets containing its Chinese translation “ ” (Alzheimer's disease), or even the layperson's term “ ” (dementia for aged people).

## 3.2.2. Mining procedure

(1) Corpus collection: To obtain the search–result pages of source English medical terms, we submitted them to search engines (e.g. Google). Basically, we collected page frequency of term occurrence and only the first 100 retrieved snippets to extract contextual terms as feature vectors for computing similarity between target translation candidates and source terms.

(2) Translation candidate extraction: Methods of extracting Chinese translation candidates from the search–result pages are the same as the methods adopted in the anchor-text mining except that the candidate number is set to k = 20 in order to reduce the computational load.

(3) Translation selection: Use search–result mining to estimate the similarity based on the following models.

## 3.2.3. Chi-square test

On the basis of co-occurrence analysis, chi-square test $( \chi ^ { 2 } )$ is adopted to estimate semantic similarity between the source term E and the target candidate C [8]. The similarity measure is defined as

![](/api/attachments/JS3XWQ5A/fulltext/images/f117bdccaa94aaa14ad63f3d7853a7824761b5ef1810cbcf67045ef1672015da.jpg)  
Fig. 2. The Chinese–English MeSH Compilation System.

$$
S _ {\chi^ {2}} (\mathrm{E}, \mathrm{C}) = \frac {N \times (a \times d - b \times c) ^ {2}}{(a + b) \times (a + c) \times (b + d) \times (c + d)},\tag{2}
$$

where a, b, c and d are the numbers of pages retrieving from search engines by submitting Boolean queries: “E and $\mathrm { C } ^ { \infty } , \mathrm { ^ { 6 6 } E }$ and not $C ^ { \mathfrak { n } } ,$ , “not E and $C ^ { \mathfrak { n } } ,$ , and “not E and not C”, respectively; N is the total number of pages, i.e., $N { = } a { + } b { + } c { + } d .$

## 3.2.4. Context-vector analysis

Due to the nature of Chinese pages often containing English texts, the source English term E and the Chinese translation candidate C may share common contextual terms in the search–result pages. The similarity between E and C will be computed based on their context feature vectors in the vector–space model. The conventional TFIDF weighting scheme is used and defined as

$$
w _ {t _ {i}} = \frac {f (t _ {i} , p)}{\max _ {j} f (t _ {j} , p)} \times \log \left(\frac {N}{n}\right),\tag{3}
$$

where $f ( t _ { i } , p )$ is the frequency of term $t _ { i }$ in search–result page $p ,$ N is the total number of Web pages, and n is the number of the pages containing $t _ { i } .$ Finally, we use the cosine measure to estimate the similarity as:

$$
S _ {C V} (\mathrm{E}, \mathrm{C}) = \frac {\Sigma_ {i = 1} ^ {m} w _ {e _ {i}} \times w _ {c _ {i}}}{\sqrt {\Sigma_ {i = 1} ^ {m} (w _ {e _ {i}}) ^ {2} \times \Sigma_ {i = 1} ^ {m} (w _ {c _ {i}}) ^ {2}}}.\tag{4}
$$

## 3.3. Combined method

The anchor–text-based method is effective for extracting translations of high-frequency Web query terms, but the search–result-based method has higher coverage of translations for unknown query terms, and the parallel-page-based method has higher translation accuracy. In order to combine the advantages of these two methods, we use a linear combination of inverse ranks to compute the similarity measure as follows:

$$
S _ {\text { Combined }} (\mathrm{E}, \mathrm{C}) = \sum_ {m} \frac {\alpha_ {m}}{R _ {m} (\mathrm{E} , \mathrm{C})},\tag{5}
$$

where $\alpha _ { m }$ is an assigned weight for each similarity measure $S _ { m } ,$ and $R _ { m } \mathrm { ( E , ~ C ) }$ represents the similarity rank of each target candidate C with respect to its source term E and is assigned to be from 1 to k (candidate number) according to similarity measure $S _ { m } ( \mathrm { E } , \mathrm { C } )$ in decreasing order.

## 3.4. The Chinese–English Mesh Compilation System

On the basis of our integrated Web-based term translation method, we have developed an efficient tool, called the Chinese–English MeSH Compilation System, to help reduce manual effort in compiling the Chinese– English MeSH. Fig. 2 shows the system consisting of three major parts. Part 1 displays the English MeSH term and its Chinese translation after compilation. Part 2 provides knowledge engineers efficient compilation with checkboxes as well as text-input button.

![](/api/attachments/JS3XWQ5A/fulltext/images/ae162f087523e3601f9f1e908dc7d174cbfa7e4ea8a2ffc03931087bd82164df.jpg)

![](/api/attachments/JS3XWQ5A/fulltext/images/7268e242d81aea489b104e291694721090596b2534b920c86f0aca096eff409f.jpg)  
Fig. 3. An example meta-search results displayed by MMODE, where the given query was “ ” and its corresponding English medical term “Fibroadenoma” was translated via looking up the Chinese–English MeSH.

Additionally, some auxiliary resources are added to augment the lack of translations in Part 3. The interface suggests about 30 translation candidates, which increases the chance of covering more layperson's terms. For instance, “Down's Syndrome” has Chinese translations “ ” or “ ”, and is popularly called “ ” (see Fig. 2).

Two knowledge engineers utilized the Chinese–English MeSH Compilation System to first semi-automatically compile over 19,000 medical terms (including all of the 9,646 disease terms) as the initial Chinese–English MeSH.

## 4. Cross-language medical information retrieval

In this section, we introduce how to utilize the Chinese–English MeSH to develop a practical CLMIR system that can help Chinese-speaking consumers to retrieve top-quality English medical information.

## 4.1. Cross-language concept matching method

To effectively handle query translation in matching Chinese query terms with the Chinese–English MeSH concepts, we present two simple cross-language concept matching methods in the following.

## 4.1.1. Approximate string matching

Basically, for each Chinese query term, we can find its corresponding English MeSH concept easily when it appears exactly in the Chinese–English MeSH. However, up to now, there have been no standard rules for translating English medical terms into Chinese. Thus, many English medical terms in MeSH often have multiple different Chinese translations or corresponding layperson's terms. For example, the English term “adrenoleukodystrophy” has several Chinese translations: “ ”, “ ”, “ ”, “ ”, and “ ”, etc. Certainly, matching diverse Chinese layperson's terms with the corresponding terms in the Chinese–English MeSH is a challenge. Fortunately, there might be partially similar substrings among these different Chinese translations. Thus, we adopt the Dice Coefficient to calculate the similarity by counting the number of character bigrams co-occurring in both Chinese query terms and Chinese MeSH concepts.

$$
S _ {\mathrm{ASM}} (q, c) = \frac {2 \times N _ {q c}}{N _ {q} + N _ {c}},\tag{6}
$$

where $N _ { q }$ and $N _ { c }$ are the number of character bigrams in the query term q and the MeSH concept $c ,$ and $N _ { q c }$ is the number of character bigrams overlapping in both q and c. We predefined a threshold to filter out some impossible concept matching.

## 4.1.2. Context vector matching

In some cases, it is ineffective to use the above approximate string matching method to deal with the mapping of some layperson's terms with completely different orthographic forms from their corresponding medical terms, e.g. the layperson's term “ / Mongolism” and its corresponding medical term “ /Down's syndrome”. To solve such a thorny problem, we will apply the context–vector analysis method described in Section 3.2 to obtain context vectors of such Chinese layperson's terms and English MeSH concepts, and then compute the cross-language concept similarity between them. The concept similarity will be estimated using Eq. (4).

## 4.2. CLMIR system

In our initial CLMIR work, we first utilized the Chinese–English MeSH (over 19,000 medical translation pairs) to develop MMODE<sup>2</sup>, a cross-language medical information retrieval system to help Chinesespeaking consumers retrieve healthcare information, including research literature, popular news, related Web pages, and related images from U.S. authoritative medical websites.

The user interface of MMODE is shown in Fig. 3. The users can enter Chinese disease terms and select a preferred English translation by navigating through the bilingual MeSH concept hierarchy to clarify their information needs. The system will return the retrieved medical articles instantly from different English websites. Users can choose among the PubMed, Medline-Plus, and NLH QA services. In addition to the documents, the system also presents related images retrieved from Google. Moreover, the MMODE system labels the medical terms in the retrieved documents with their corresponding Chinese translations in order to help users understand the English articles better.

For the example in Fig. 2, a user navigated the MeSH tree and identified his query as “ ” (Fibroadenoma). The system returned related documents from PubMed and related images from Google. Medical terms in the retrieved documents, such as cell, cytology, pathology, and Fibroadenoma, were labeled with their respective Chinese translation.

## 5. Experiments

5.1. Evaluation of construction of the Chinese–English MeSH

To determine the effectiveness of the presented Webbased term translation method to reduce the effort of knowledge engineers in building the Chinese–English MeSH by providing correct translation candidates, we first conducted a preliminary experiment to evaluate the accuracy of automatically translating the English MeSH terms into Chinese, and then conducted another experiment to evaluate the efficiency of the Chinese– English MeSH Compilation System.

## 5.1.1. Effectiveness evaluation

We randomly selected two test sets of 300 disease terms from 9646 terms in MeSH's disease concept. The average top-n inclusion rate was adopted as an evaluation metric. For a set of query terms, its top-n inclusion rate was defined as the percentage of source terms whose correct translations could be found in the first n extracted translations.

Table 1 shows that for the test set 1, the overall candidate matching (including exact and partial matching) achieved 23.6%, 51.66%, and 63.9% for the top-1, top-5, and top-10 inclusion rates, respectively. Although the top-1 inclusion rate is low, top-10 inclusion rate is relatively high. The inclusion rates in top-5 and top-10 are fairly stable across the two data sets. Therefore, the presented method is still effective to provide knowledge engineers with possibly correct translations in compiling the Chinese–English MeSH. Table 2 shows some examples of Chinese translations of English MeSH terms that were successfully extracted.

## 5.1.2. Efficiency evaluation

We also wanted to investigate whether our developed Chinese–English MeSH Compilation System could help knowledge engineers reduce manual effort in compiling the Chinese–English MeSH. We conducted an efficiency evaluation by counting the number of Chinese translations compiled for English MeSH concepts during one hour. Four tests were performed for each test user, including two tests using the Chinese– English MeSH Compilation System and the other two without the use of the system. The test English MeSH concepts were randomly selected from 9646 terms in MeSH's disease concept. There were two graduate students (users A, B) and one professional physician (user C) participating in the tests. User C only took half an hour for each test since he had less free time considering his busy workload.

Inclusion rates of Chinese translation for two test sets of 300 MeSH disease terms

<table><tr><td>Test set</td><td>Candidate matching</td><td>Top-1</td><td>Top-5</td><td>Top-10</td></tr><tr><td rowspan="3">DName-1</td><td>Exact</td><td>3.3%</td><td>10.0%</td><td>15.3%</td></tr><tr><td>Partial</td><td>20.3%</td><td>41.6%</td><td>48.6%</td></tr><tr><td>Overall</td><td>23.6%</td><td>51.6%</td><td>63.9%</td></tr><tr><td rowspan="3">DName-2</td><td>Exact</td><td>6.6%</td><td>11.3%</td><td>15.0%</td></tr><tr><td>Partial</td><td>26.0%</td><td>41.0%</td><td>48.3%</td></tr><tr><td>Overall</td><td>32.6%</td><td>52.3%</td><td>63.3%</td></tr></table>

Table 2  
Examples of correct Chinese translations extracted for English MeSH terms

<table><tr><td>English MeSH term</td><td>Extracted Chinese translation (correct)</td></tr><tr><td>Pierre Robin Syndrome</td><td>皮爾羅賓症後群</td></tr><tr><td>Chorioretinitis</td><td>脈絡膜視網膜炎</td></tr><tr><td>Cerebral Ventricle Neoplasms</td><td>腦室腫瘤</td></tr><tr><td>Empty Sella Syndrome</td><td>空虛鞍部症候群</td></tr></table>

Table 3 shows that users B and C compiled more Chinese translation using the Chinese–English MeSH Compilation System, but user A seemed to obtain the opposite results. The average number ((27 + 49 + 78) / 3 = 51.3) among the three users using the system is larger than that ((29 +35+74)= 46) without the use of the system. To understand the efficiency difference between the three users, we made some analyses after interviewing the users. The possible reasons are explained in the following. First, the Chinese–English Compilation System is a Web-based interface, so a user's bandwidth may affect the test results. Second, users may need to take a little time to get used to the interface of the system in the first one or two tests. Third, the randomly selected test concepts may have differing degrees of difficulty for each user with his unique compilation habit. For example, some users may take a considerable amount of time to compile one difficult concept translation whereas others may just pass on it.

Table 3  
Results of compiling the Chinese–English MeSH with versus without the Chinese–English Compilation System

<table><tr><td rowspan="2">UserID</td><td rowspan="2">Test set</td><td colspan="2">With our system</td><td rowspan="2">Test set</td><td colspan="2">Without our system</td></tr><tr><td>Count</td><td>Average</td><td>Count</td><td>Average</td></tr><tr><td rowspan="2">A</td><td>TS1</td><td>28</td><td>27</td><td>TS3</td><td>27</td><td>29</td></tr><tr><td>TS2</td><td>26</td><td></td><td>TS4</td><td>31</td><td></td></tr><tr><td rowspan="2">B</td><td>TS3</td><td>50</td><td>49</td><td>TS1</td><td>38</td><td>35</td></tr><tr><td>TS4</td><td>48</td><td></td><td>TS2</td><td>32</td><td></td></tr><tr><td rowspan="2">C</td><td>TS1</td><td>69</td><td>78</td><td>TS3</td><td>63</td><td>74</td></tr><tr><td>TS2</td><td>87</td><td></td><td>TS4</td><td>85</td><td></td></tr></table>

Table 4  
Results of monolingual and crosslingual retrieval

<table><tr><td>Method</td><td>P</td><td>R</td><td>F</td><td>MAP</td></tr><tr><td>Monolingual (original English query)</td><td>0.211</td><td>0.598</td><td>0.312</td><td>0.341</td></tr><tr><td>SYSTRAN (MT)</td><td>0.068</td><td>0.166</td><td>0.097</td><td>0.086</td></tr><tr><td>Medical bilingual Dictionary</td><td>0.070</td><td>0.199</td><td>0.098</td><td>0.086</td></tr><tr><td>MMODE (Chinese–English MeSH)</td><td>0.171</td><td>0.482</td><td>0.253</td><td>0.233</td></tr></table>

## 5.2. Evaluation of CLMIR system

## 5.2.1. The corpus

To determine the effectiveness of our MMODE system in CLMIR, we conducted preliminary experiments based on the medical corpus from the MuchMore project (see the Introduction section), which is a multinational research project on the development of CLMIR technologies. The corpus in MuchMore is a parallel corpus of English–German scientific medical abstracts obtained from the Springer Link website. The corpus consists approximately of 1 million tokens for each language. Abstracts were compiled from 41 medical journals. Each of the journals constitutes a relatively homogeneous sub-domain in medicine. We only used the English part of the corpus, including 9000 English medical abstracts.

## 5.2.2. Test queries

MuchMore also provides 25 English–German bilingual test queries and the sets of abstracts that are relevant to each of the query. This serves as the benchmark for CLMIR. We had the 25 English queries translated into Chinese by a Chinese physician.

Table 5  
Effective example for CLMIR using MMODE

<table><tr><td colspan="3">Chinese test query: 心室頻脈的治療</td></tr><tr><td>Method</td><td>Translated results</td><td>MAP</td></tr><tr><td>Monolingual(original English query)</td><td>Treatment ofventricular tachycardia</td><td>0.380</td></tr><tr><td>SYSTRAN (MT)</td><td>Ventricle frequencyarteries treatment</td><td>0.000</td></tr><tr><td>Medical bilingual dictionary</td><td>ventricular arrhythmiaventricular fibrillationventricular flutter</td><td>0.115</td></tr><tr><td>MMODE(Chinese-English MeSH)</td><td>Tachycardia, ventricular;Tachycardia, supraventricular;Therapeutics;</td><td>0.325</td></tr></table>

Table 6 Ineffective example for CLMIR using MMODE

<table><tr><td colspan="3">Chinese test query: 植入性心臟去震顫器(ICD)的適應症使用</td></tr><tr><td>Method</td><td>Translated results</td><td>MAP</td></tr><tr><td>Monolingual(original English query)</td><td>Indication for implantablecardioverter defibrillator (ICD)</td><td>0.175</td></tr><tr><td>SYSTRAN (MT)</td><td>Implanting heart trembling ICDindication use</td><td>0.125</td></tr><tr><td>Medical bilingualdictionary</td><td>Implant implantation heartcardi(o)-</td><td>0.000</td></tr><tr><td>MMODE(Chinese-English MeSH)</td><td>Defibrillators, implantab; Use;</td><td>0.026</td></tr></table>

## 5.2.3. Evaluation metric

To evaluate the performance of our developed CLMIR system, we used mean average precision (MAP) as a metric, which has become customary for use in several tasks of the Text Retrieval Conference (TREC). MAP contains both recall and precision oriented aspects and emphasizes returning more relevant documents earlier:

$$
\mathrm{MAP} = \frac {\sum_ {r = 1} ^ {N} (P (r) \times \operatorname{rel} (r))}{R}\tag{7}
$$

where r is the rank, N is the number of retrieved documents, R is the number of relevant documents, rel() is a binary function of the relevance of a given rank, and P() is precision at a given cut-off rank. For reference, we also evaluated the performance with the other measures such as precision (P), recall (R), and F-measure (F).

## 5.2.4. Performance

To determine the effectiveness of the MMODE with the proposed techniques of cross-language concept matching in CLMIR, we compared it against other conventional techniques of query translation in CLIR. The monolingual retrieval results using the original English queries were taken as our baseline for performance comparison with the results of crosslingual retrieval. Additionally, we also evaluated the performance of CLMIR using a medical bilingual dictionary<sup>3</sup>, and the well-known commercial machine translation system SYSTRAN. Table 4 shows the results. The MMODE performed better than the others and achieved the best MAP value at 0.233 (about 68% (0.233/ 0.341) of monolingual performance). The conventional query translation techniques (i.e. dictionary- and MTbased approaches) were not effective for CLMIR. Although our proposed technique of medical query translation performed well by employing the Chinese–

English MeSH and cross-language concept matching methods, however, it still suffered from many difficulties. To realize its potential limitations for future improvements, we made further detailed performance comparison and analyses in the following.

Table 5 shows the effective results by using the MMODE to deal with query translation. MMODE performed better in matching Chinese disease terms with MeSH medical concepts based on our proposed cross-language concept matching methods. In contrast, SYSTRAN often generated incorrect translations because it was not able to correctly disambiguate the meaning of a medical term when the term has more than one meaning in general-purpose bilingual dictionaries. For example, the term “ ” in Chinese test query was incorrectly identified as a complete term and was translated as “frequency”. In fact, the correct term was “ ” and its translation is “tachycardia”. As for using medical bilingual dictionary, it performed worse than MMODE but better than SYSTRAN since it could translate the Chinese term “ ” into the English translation, “ventricular”, correctly, but couldn't obtain the correct translation, “tachycardia”, for the Chinese term “ ”.

Table 6 shows the ineffective results. English acronyms were not matched correctly using MMODE, such as the term “ICD”. Solving this problem is vitally important because many acronyms appearing frequently in medical documents play the role of keywords. Besides this, a number of incorrect translations are extracted because it is difficult to remove English common terms from search results. The problem can be mitigated in the future by using MeSH as a filter to remove these noise candidates.

## 5.3. Discussions

Although the performance of exact translation using our Web-based term translation method was not satisfying, more than 60% of the partially correct translations could be extracted from the top ten candidates. This is still very useful in saving labor time of knowledge engineers in compiling the Chinese–English MeSH. Two part-time knowledge engineers through the Chinese–English MeSH Compilation System have compiled over 19,000 entries of the Chinese–English MeSH (about 42,000 entries in total) over a period of three months. Actually, this system saved them a lot of time and manual effort in finding Chinese translations.

The major advantage of our Web-based term translation method is that we have no need to use a bilingual medical dictionary while Chiao's [4] work utilized 4,963 seed pairs using comparable-corpus-based method. Thus, our method is language-independent and easy to extend to other language pairs if the source and the target languages often appear in the same text (e.g. Korean–English and Japanese–English). However, this method might be limited if the two languages are seldom mixed in the text (e.g. French–English).

There are several directions for improvement in the future. For example, the difference between top-10 (63.9%) and top-1 (23.6%) inclusion rates is around 40%, showing the magnitude of potential improvement in top-1 inclusion rate. We observed that most errors resulted from the problems of Chinese word segmentation, medical term recognition, and similarity computation of low-frequency terms. Our future work should focus on these issues in order to improve translation performance for medical terms.

## 6. Conclusions

Without the assistance of a bilingual medical dictionary/thesaurus, most non-English consumers are not able to search or read English medical documents even if they can read English. In this paper, we present a practical CLMIR system MMODE which can help Chinese-speaking consumers cross the language barrier and easily retrieve healthcare information from English websites by providing Chinese–English MeSH trees for navigation, and a simple Chinese translation of medical terms in the retrieved documents. Moreover, with the help of retrieval of medical Web images, consumers may also get useful medical information without language barriers. In the future, we will further conduct more solid user studies to evaluate the effectiveness of MMODE.

## References

[1] L.A. Ballesteros, W.B. Croft, Phrasal translation and query expansion techniques for cross-language information retrieval, Proceedings of the 20th Annual International ACM SIGIR Conference, 1997, pp. 84–91.

[2] L.A. Ballesteros, W.B. Croft, Resolving ambiguity for crosslanguage retrieval, Proceedings of the 21st Annual International ACM SIGIR Conference, 1998, pp. 64–71.

[3] P.J. Cheng, J.W. Teng, R.C. Chen, J.H. Wang, W.H. Lu, L.F. Chien, Translating unknown queries with web corpora for crosslanguage information retrieval, Proceedings of the 27th Annual International ACM SIGIR Conference, 2004, pp. 146–153.

[4] Y.C. Chiao, P. Zweigenbaum, Looking for French–English translations in comparable medical corpora, Journal of the American Society for Information Science 8 (2002) 150–154.

[5] J.J. Cimino, Vocabulary and health care information technology: state of the art, Journal of the American Society for Information Science 46 (1995) 777–782.

[6] H. Déjean, E. Gaussier, F. Sadat, Bilingual terminology extraction: an approach based on a multilingual thesaurus applicable to comparable corpora, Proceedings of COLING, Tapei, Taiwan, 2002.

[7] P. Fung, L.Y. Yee, An IR Approach for Translating New Words from Nonparallel, Comparable Texts, Proceeding of 36th ACL, 1998, pp. 414–420.

[8] W.A. Gale, K.W. Church, Identifying Word Correspondances in Parallel Texts, Proceedings of DARPA Speech and Natural Language Workshop, 1991.

[9] W.R. Hersh, L.C. Donohoe, SAPHIRE International: A Tool for Cross-Language Information Retrieval, Proceedings of American Medical Informatics Association Annual Symposium (AMIA), 1998, pp. 673–677.

[10] D.A. Hull, G. Grefenstette, Querying across Languages: A Dictionary-based Approach to Multilingual Information Retrieval, Proceedings of the 19th Annual International ACM SIGIR Conference, 1996, pp. 49–57.

[11] M. Joubert, M. Fieschi, J.J. Robert, F. Volot, D. Fieschi, UMLSbased conceptual queries to biomedical information databases: an overview of the project ARIANE, Journal of the American Society for Information Science 5 (1) (1998) 52–61.

[12] K.L. Kwok, NTCIR-2 Chinese, Cross Language Retrieval Experiments Using PIRCS, Proceedings of NTCIR workshop meeting, 2001.

[13] G. Leroy, H.C. Chen, Meeting medical terminology needs — the ontology-enhanced medical concept mapper, IEEE Transactions on Information Technology in Biomedicine 5 (4) (2001) 261–270.

[14] W.H. Lu, L.F. Chien, H.J. Lee, Translation of Web queries using anchor text mining, ACM Transactions on Asian Language Information Processing 1 (2) (2002) 159–172.

[15] W.H. Lu, L.F. Chien, H.J. Lee, Anchor text mining for translation of Web queries: a transitive translation approach, ACM Transactions on Information Systems 22 (2) (2004) 242–269.

[16] W.H. Lu, S.J. Lin, Y.C. Chan, K.H. Chen, Semi-Automatic Construction of the Chinese–English MeSH Using Web-Based Term Translation Method, Proceedings of American Medical Informatics Association Annual Symposium (AMIA), 2005.

[17] J.Y. Nie, P. Isabelle, M. Simard, R. Durand, Cross-language information retrieval based on parallel texts and automatic mining of parallel texts from the Web, Proceedings of the 22nd Annual International ACM SIGIR Conference, 1999, pp. 74–81.

[18] D.W. Oard, A comparative study of query and document translation for cross-language information retrieval, Proceedings of AMTA Conference on Machine Translation, 1998, pp. 472–483.

[19] P. Resnik, Mining the Web for Bilingual Text, Proceedings of the 37th Annual Meeting of the Association for Computational Linguistics, 1999.

[20] G. Rosemblat, D. Gemoets, A.C. Browne, T. Tse, Machine translation-supported cross-language information retrieval for a consumer health resource, Proceedings of American Medical Informatics Association Annual Symposium (AMIA) (2003) 564–568.

[21] T.D. Tran, N. Garcelon, A. Burgun, P. Le Beux, Experiments in cross-language medical information retrieval using a mixing translation module, Medinfo (2004) 946–949.

[22] J.H. Wang, W.H. Lu, L.F. Chien, Toward Web mining of crosslanguage query translations in digital libraries, International Journal on Digital Libraries 4 (4) (2004).

[23] J. Xu, R. Weischedel, C. Nguyen, Evaluating a probabilistic model for cross-lingual information retrieval, Proceedings of the 24th Annual International ACM SIGIR Conference, 2001, pp. 105–110.

[24] C.C. Yang, K.W. Li, Automatic construction of English/Chinese parallel corpora, Journal of the American society for Information Science and Technology 54 (8) (2003) 730–742.

[25] Y. Zhang, P. Vines, Using the Web for automated translation extraction in cross-language information retrieval, Proceedings of the 27th Annual International ACM SIGIR Conference, 2004, pp. 162–169.

![](/api/attachments/JS3XWQ5A/fulltext/images/327096185ac4df90394413ec174b58a37efa5b14a5664e2ed1ce5193ad82196e.jpg)  
Wen-Hsiang Lu is an Assistant Professor in the Department of Computer Science and Information Engineering (CSIE) at National Cheng Kung University, Tainan, Taiwan. Dr. Lu received the B.S., M.S., and Ph.D. degrees in computer science and information engineering from National Chiao Tung University, Hsinchu, Taiwan. His current research focuses on web mining, information retrieval, natural language processing, and medical informatics.  
Yi-Che Chan is a Master's student in the Department of Computer Science and Information Engineering (CSIE) at National Cheng Kung University, Tainan, Taiwan. His research interests include web mining, natural language processing, and multilingual information retrieval.

![](/api/attachments/JS3XWQ5A/fulltext/images/bb465a3f692a9e1160a1534e00c51adc7a900f780467f07de5b19c401d3695ec.jpg)

![](/api/attachments/JS3XWQ5A/fulltext/images/c76ef322691b850c12d1889ec8255b721df5709ccaec378b21ec298959d61f2d.jpg)  
Ray S. Lin is a PhD student in Biomedical Informatics at Stanford University, Stanford, CA. He got his bachelor's and master's training in computer science from National Taiwan University, Taipei, Taiwan. His research interests include medical decision support, machine learning, and cross-language information retrieval.

![](/api/attachments/JS3XWQ5A/fulltext/images/d8b4374ae0b178ce28b7d8f73aadeb7a0882182a2792db2973f005656f893118.jpg)  
Kuan-Hsi Chen is a Master's student in the Department of Computer Science and Information Engineering (CSIE) at National Cheng Kung University, Tainan, Taiwan. His research interests include web mining, information retrieval, and natural language processing.
