---
otero_id: 21107
otero_key: "K7CJ8TER"
title: "Enhancing the power of Web search engines by means of fuzzy query"
authors: "Dae-Young Choi"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00095-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enhancing the power of Web search engines by means of fuzzy query

Dae-Young Choi

Dept. of MIS, Yuhan College, 422-769, Koean-donf, Sosa-ku, Puchon City, Kyongki-do, South Korea

## Abstract

Commercial Web search engines such as Yahoo!, Google, etc., have been defined which manage information only in a crisp way (i.e., keyword-based). Their query languages do not allow the expression of preferences or vagueness. They generally return many Web pages irrelevant to user’s query. In order to handle these problems, we propose the Perception Index (PI) that contains attributes associated with a focal keyword restricted by fuzzy term(s) used in fuzzy queries on the Internet. The PI assists the user to reflect his/her perception in the process of query. If we integrate the Document Index (DI) used in commercial Web search engines with the proposed PI, we can handle both crisp terms (keyword-based) and fuzzy terms (perception-based). In this respect, the proposed approach is softer than the keyword-based approach. The PI brings somewhat closer to natural language. It is a further step toward a human-friendly, natural language-based interface for Web searching. Consequently, Internet users can narrow thousands of hits to the few that users really want. In this respect, the PI provides a new tool for targeting queries that users really want. In this paper, we also present a personalized search and ranking based on the PI. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Perception Index (PI); Web search engines; Fuzzy query; Integrated Index (DI+PI); Personalized search and ranking

## 1. Introduction

An advantage of fuzzy set-based modeling is that it is mainly qualitative in nature. Indeed, in many cases, it is enough to use an ordinal scale for the membership degrees. This also facilitates the elicitation of (user/ context dependent) membership functions for which it is enough, in practice, to identify the elements that totally belong and those which do not belong at all to the fuzzy set. Fuzzy set membership functions are convenient tools for modeling user’s preference profiles. Fuzzy queries are often motivated by the expression of preferences or tolerance and of relative levels of importance [3]. Compared to the existing crisp query (i.e., keyword-based), fuzzy query provides a better representation of users’ preferences and the necessary information for rank-ordering the answers according to the degree to which they satisfy the query. In Ref. [31], Zadeh described that ‘‘existing search engines have zero deductive capability. To add a deductive capability to a search engine, the use of fuzzy logic is not an option—it is a necessity’’. In this paper, we propose a method for adding a deductive capability to the existing Web search engines by means of fuzzy query, and also present a personalized search and ranking based on the proposed method.

Owing to the booming development of the Web, users have to face a variety and a large number of Web pages and often waste a lot of time on searching. To alleviate the difficulty, many tools have been developed and used on the Web. Search engines are the most popular tools and usually provide two basic functions. One is to collect the descriptions of Web pages and organize them as an index. The other is to find the most relevant Web pages against the index for user queries. The techniques of information retrieval are commonly used for building search engines [19].

The central concept of information retrieval is the notion of relevance [16]. A user with a given query for information tries to find any specific results that he/ she really wants. There are several models for specifying the representations used for the documents and the queries, as well as the matching of these representations [9]. The most used model is that of the Boolean query based on set theory. Documents are represented as sets of terms and queries are Boolean expressions on terms. The retrieval mechanism does an exact match by classifying documents that satisfy the Boolean query as being relevant, all other documents as being irrelevant. This model is used by virtually all commercial textual-document retrieval systems. However, it is difficult to overcome the limitations of this model, including the inability to handle properly imprecision and subjectivity. The second model is the vector space model [16] where documents and queries are represented as vectors in the space of all possible index terms. The document vectors consist of weights based on term frequencies in the collection, while the query vectors are binary vectors on the terms. The matching is based on a similarity measure between the documents and the query (often involving the cosine of the angle between the query vector and a given document vector). To date, this model leads the others in terms of performance. The third model is the probabilistic model [16] where documents are represented as binary vectors. The queries are vectors of terms with weights based on the estimated probability of relevance of documents with those terms. Like the vector space model, the key advantage is the ability to rank documents on the likelihood of relevance. The fourth model is the generalized Boolean model, where fuzzy set theory allows the extension of the classical Boolean model to incorporate weights and partial matches, and adding the idea of document ranking.

The importance of representations of uncertainty in databases is increasing as more complex applications such as CAD/CAM and geographical information systems (GIS) are being undertaken in object-oriented and multi-media databases. Query languages are designed to express the user’s retrieval requests in either a crisp manner or not. Much of the work in the database area has been in extending query languages to permit the representation and retrieval of imprecise data [6,13–15,17]. There are some current commercial attempts at providing fuzzy query capabilities as front ends to conventional database systems [13].

Until now, however, commercial systems including informational retrieval systems (IRS), data base management systems (DBMS), and Web search engines have been defined which manage information only in a crisp way. Moreover, (crisp) traditional query languages do not allow the expression of preferences or vagueness, which could be desirable for the following reasons [9]:

 to control the size of the results;

 to express soft retrieval conditions;

 to produce a discriminated answer.

Although the commercial Web search engines such as Yahoo!, Google, Lycos, etc., help Internet users get to good information, they do not properly handle fuzzy query. For example, consider a fuzzy query that finds ‘popular national parks in the USA’. In this case, ‘popular’, ‘national parks’ and ‘USA’ are generally processed as keywords in the commercial Web search engines. As a result, search engines return many Web pages (or URLs) irrelevant to user’s query. For example, given a fuzzy query that finds ‘popular national parks in the USA’, Yahoo! returns about 34,200 Web pages (or URLs) and Google returns about 73,100 Web pages (or URLs). Intuitively, we find that there are so many Web pages (or URLs) irrelevant to user’s query. It should be noted that fuzzy term ‘popular’ is a constraint on the focal keyword ‘national parks’ rather than an independent keyword. In other words, the fuzzy term ‘popular’ plays the role of a constraint on the fuzzy query. Thus, using fuzzy term(s), Internet users can narrow thousands of hits to the few that users really want. In this respect, the fuzzy terms in a query provides helpful hints for targeting queries that users really want, and a way for personalized search and ranking. However, commercial Web search engines tend to ignore the importance of fuzzy terms in a query. The expressive power of conventional search engine query interfaces is relatively weak when restricted to keyword-based search (i.e., Document Index (DI)-based search) [7]. At present, the keyword-based search engines present limitations in modeling perceptual aspects of humans. In addition, they are unsuccessful in returning the targeted results. In other words, they generally return many Web pages (or URLs) irrelevant to user’s query. In this respect, we need a new tool to handle both the fuzzy query and the removal of spurious results. In order to tackle these problems, we propose the Perception Index (PI) that contains attributes associated with a focal keyword restricted by fuzzy term(s) in a fuzzy query.

In Section 2, we introduce the integrated index (DI+PI) and suggest a new search mechanism based on the integrated index. In Section 3, we describe fuzzy query based on the integrated index. This section is divided into three parts: types of fuzzy query, query processing based on the integrated index, and user interface based on the integrated index. In Section 4, we summarize some features of the proposed method. In Section 5, we present a personalized search and ranking based on the PI. In Section 6, we suggest some considerations for implementing the proposed method. Finally, we conclude the paper in Section 7.

## 2. Integration of document index with perception index

Large-scale Web search engines such as Yahoo!, Google, Lycos, effectively retrieve entire documents, but they are imprecise, and do not exploit and retrieve the semantic Web document content. We cannot automatically extract such content from general documents yet [11].

Knowledge representation languages that support logic inference can help us achieve more flexible and precise knowledge representation and retrieval. Industry is currently developing many metadata languages to let people index Web information resources with knowledge representations and store them in Web documents. However, these metadata languages are insufficient to satisfy several requirements necessary to allow precise, flexible and scalable information retrieval. A first requirement is that the metadata language must be intuitive and concise enough for people to use easily. Most current knowledge-oriented metadata languages are built above the eXtended Markup Language (XML) [26,27], such as the Resource Description Framework (RDF) [28] and Ontology Markup Language (OML) [29]. The choice of XML as an underlying format lets users use standard XML tools to exchange and parse these metadata languages. However, because XML is verbose, the metadata languages built above it are verbose and difficult to use without specialized editors [11].

To reduce information redundancy, Ontobroker [30], an ontology that guides information retrieval from annotated HTML documents accessible on the Web, provides a notation for embedding attributevalue pairs inside an HTML hyperlink tag. Although the Ontobroker metadata language was designed to reduce information redundancy, statements cannot be displayed by browsers, because they are within HTML tags. Furthermore, like the RDF, the Ontobroker metadata language is a notation for attributevalue pairs. Such a representation is general but hard to read. Only the document authors can index any of its parts, because they index document elements with HTML tags. Others are limited to only those elements that are accessible via URLs. The Ontobroker metadata language and the RDF are general but imprecise, because they are oriented toward representing entire documents and do not propose conventions to represent logic-based features, such as quantifiers and operators. This limits the capacity of their statements [11].

The most important of the tools for information retrieval is the index—a collection of terms with pointers to places where information about documents can be found. The indices are used to [5]:

 provide a quick and easy access to data;

 save time and operations in editing, searching, inserting, deleting of data;

 provide additional services while designing queries, analyzing the content of data, etc.;

 correspond with the user’s view on the con-tents, reducing the effort needed to understand and use it.

The development of effective indexing tools to aid in filtering is one of major classes of problems associated with Web search and retrieval. Removal of spurious information is a particularly challenging problem [8].

Search engines are the most popular tools that people use to locate information on the Web. A search engine works by traversing the Web via the hyperlinks that connect the Web pages, performing text analysis on the pages it has encountered, and indexing the pages based on the keywords they contain. A user seeking information from the Web would formulate his/her information goal in terms of a few keywords composing a query. A search engine, on receiving a query, would match the query against its Document Index (DI). All of the pages that match the user query will be selected into an answer set and be ranked according to how relevant the pages are with respect to the query. Relevancy here is usually based on the number of matching keywords that a page contains [7]. The DI generally consists of keywords that appear in the title of a page or in the text body. Based on the DI, the commercial Web search engines such as Yahoo!, Google, Lycos, etc., help users get to good information. For example, BigBook (or SuperPages) can help users to find ‘Italian restaurants within a 1- mile radius from a specific address’ (US yellow pages services) [10]. This proximity search is processed based on crisp query with keywords (i.e., ‘Italian restaurants’, ‘1-mile’, ‘a specific address’). However, they do not properly process fuzzy queries. For example, find ‘popular national parks in the USA’. In addition, they have problems as follows [7]:

 large answer set;

 low precision;

 ineffective for general-concept queries.

In this paper, we try to tackle these problems. In order to handle these problems, we propose a Perception Index (PI). The remarkable human capability to perform a wide variety of physical and mental tasks without any measurements and any computations is derived from the brain’s crucial ability to manipulate perceptions—perceptions of distance, size, weight, color, speed, time, direction, force, number, truth, likelihood, and other characteristics of physical and mental objects. Familiar examples of the remarkable human capability are parking a car, driving in heavy traffic, playing golf, riding a bicycle, understanding speech, and summarizing a story [24]. In the computational theory of perceptions (CPT) [24,25], words play the role of labels of perceptions and, more generally, perceptions are expressed as propositions in a natural language. Computing with words (CW) techniques are employed to translate propositions expressed in a natural language into what is called the generalized constraint language (GCL). In this language, the meaning of a proposition is expressed as a generalized constraint, X isr R, where X is the constrained variable, R is the constraining relation and isr is a variable copula in which r is a discrete variable whose value defines the way in which R constrains X [23,24]. These perceptions are mainly manipulated based on fuzzy concepts. For processing a fuzzy query, the PI consists of attributes associated with a keyword restricted by fuzzy term(s) in a fuzzy query. In this respect, the restricted keyword is named as a focal keyword, whereas attribute(s) associated with the focal keyword may be regarded as focal attribute(s). The PI can be mainly derived from the contents in the text body of a Web page or from the other sources of information with respect to a Web page. For example, the PI may be consisted of distance, size, weight, color, etc. on a keyword in the text body of a Web page. Using the PI, search engines can process fuzzy concepts (terms). In the sequel, if we integrate the DI used in commercial Web search engines with the proposed PI, search engines can process fuzzy queries. For example, consider a fuzzy query that finds ‘popular national parks in the USA’. In this case, the fuzzy term ‘popular’ is processed by using the PI, whereas keywords ‘national parks’ and ‘USA’ are processed by using the DI. We note that ‘in’ and ‘the’ in the above fuzzy query are examples of stop words ignored by search engines (see hhttp:// www.google.comX) (Table 1).

It should be noted that fuzzy term(s) may be regarded as a constraint on a fuzzy query. For example, consider a fuzzy query that finds ‘popular national parks in the USA’. In this case, the fuzzy term ‘popular’ play the role of a constraint on the fuzzy query. In other words, using fuzzy term(s), Internet users can narrow thousands of hits to the few that users really want. In this respect, the PI provides helpful hints for targeting queries that users really want, and a way for personalized search and ranking.

Table 1  
An example of Integrated Index (DI+PI)

<table><tr><td>Document Index (DI)</td><td>IPs</td><td>Perception Index (PI)</td><td></td><td></td><td></td><td>FPs (Results)</td></tr><tr><td>Keywords</td><td>URLs</td><td>Distance</td><td>Size</td><td>No. of visitors</td><td>...</td><td>Targeted URLs</td></tr></table>

IPs: Intermediate Pointers; FPs: Final Pointers; URLs: Uniform Resource Locators.

The expressive power of conventional search engine query interfaces is relatively weak when restricted to keyword-based search [7]. At present, commercial Web search engines based on the DI (i.e., keyword-based search engines) present limitations in modeling perceptual aspects of humans. In addition, they generally return many Web pages (or URLs) irrelevant to user’s query. Although much Web search engines have been developed, they do not properly handle the fuzzy terms representing human’s perception. In addition, they are unsuccessful in returning the targeted results. In order to tackle these problems, we integrate the DI used in commercial Web search engines with the proposed PI. In the proposed method, given a fuzzy query, search engine processes the fuzzy query based on the integrated index (DI+PI) as follows.

In Fig. 1, if we submit a query with only crisp terms (keyword-based query), this search engine uses only the phase 1. By applying the DI, the phase 1 performs an elimination-based approach to eliminate the URLs, which are impossible to be the answers of the query. In this case, this search engine will return the same results that the existing search engines do. On the other hand, if we submit a query with both crisp terms and fuzzy terms, this search engine uses both phase 1 and phase 2. In this case, by applying the PI, the URLs reflecting fuzzy terms are extracted. More specifically, the phase 2 evaluates the fuzzy terms in detail on the set of intermediate pointers (i.e., the candidate URLs), and then generates the final pointers (FPs) (i.e., targeted results) that user really wants. This search mechanism can be conceptually explained by SQL-like language as follows: SELECT \* FROM {a set of intermediate pointers that satisfies keyword(s) in the DI} [WHERE the value(s) of focal attribute(s) in the PI are satisfied by the user]. We note that commercial Web search engines tend to ignore the importance of [WHERE] part. In this approach, the PI may be regarded as a constraint on the DI.

![](/api/attachments/K7CJ8TER/fulltext/images/de80b7a410493d165dc460ac7ab9ad4bcc23e4b1ff2cc3988005a79e3001b8b8.jpg)  
Fig. 1. A search mechanism based on the integrated index (DI+PI).

## 3. Fuzzy query based on the integrated index (DI+PI)

We assume that a fuzzy term in a fuzzy query is marked with an asterisk. For example, it is expressed as ‘\*popular national parks in the USA’. If a query has fuzzy term(s) marked with asterisk(s), search engine displays a PI associated with a focal keyword restricted by fuzzy term(s). Then user can specify values with respect to the fuzzy terms.

## 3.1. Types of fuzzy query

Fuzzy query is largely divided into simple fuzzy query and compound fuzzy query.

## 3.1.1. Simple fuzzy query

The simple fuzzy query does not include conjunction (‘and’) or disjunction $( \overrightarrow { } O r ^ { \overrightarrow { } } )$ connective(s) between fuzzy terms, or negation (‘not’).

Example 1.. Consider a fuzzy query that finds ‘\*popular national parks in the USA’. In this case, the DI, the PI, and stop words may be as follows: DI={national parks, $\mathrm { U S A } , \hdots , \hdots \hdots$ $\mathrm { P I } { = } \{ N o $ . of vis-$i t o r s , \ldots \rangle$ , stop words={in, the}. We note that a focal keyword ‘national parks’ in the DI is restricted by a fuzzy term ‘popular’. In this case, the fuzzy term ‘popular’ may be manipulated by the number of visitors (i.e., a focal attribute in the PI) per year, and represented as in Fig. 2.

Example 2.. Consider a fuzzy query that finds ‘national parks \*moderate distance from San Francisco’. In this case, the DI, the PI and stop words may be as follows: DI={national parks, San Francisco,. . .}, $\scriptstyle \mathrm { P I } = \{ d i s t a n c e , \ldots \}$ , stop words={from}. We note that a focal keyword ‘San Francisco’ in the DI is restricted by a fuzzy term ‘moderate’. In this case, the fuzzy term ‘moderate’ may be manipulated by the degree of distance (i.e., a focal attribute in the PI) from San Francisco, and represented as in Fig. 3.

## 3.1.2. Compound fuzzy query

The compound fuzzy query includes conjunction (‘and’) or disjunction $( \overrightarrow { } O r ^ { \overrightarrow { } } )$ connective(s) between fuzzy terms, or negation (‘not’).

. Conjunction (‘and’)

Example 3.. Consider a fuzzy query that finds ‘national parks that \*popular and \*moderate distance from San Francisco’. In this case, the DI, the PI, logical operator, and stop words may be as follows: DI={national parks, San Francisco,. . .}, PI={No. of visitors, distance,. . .}, logical operator={and}, stop words={that, from}. We note that a focal keyword ‘San Francisco’ in the DI is restricted by fuzzy terms ‘popular’ and ‘moderate’. In this case, the fuzzy terms ‘popular’ and ‘moderate’ may be manipulated as in Figs. 2 and 3, respectively.

. Disjunction (‘or’)

![](/api/attachments/K7CJ8TER/fulltext/images/6219251421b13a3f0e5a5ad1a21284d56f86e4f07241761fc5c5da10e93f8195.jpg)  
Fig. 2. A membership function of ‘popular’.

![](/api/attachments/K7CJ8TER/fulltext/images/745ae6c7a321939a20bb44d6d5b3504ecfa386ea2bcc9ea7feef3a411f3e7cac.jpg)  
Fig. 3. A membership function of ‘moderate’.

Example 4.. Consider a fuzzy query that finds ‘national parks that \*popular or \*moderate distance from San Francisco’. In this case, the DI, the PI, logical operator, and stop words may be as follows: DI={national parks, San Francisco,. . .}, PI={No. of visitors, distance,. . .}, logical operator={or}, stop words={that, from}. We note that a focal keyword ‘San Francisco’ in the DI is restricted by fuzzy terms ‘popular’ and ‘moderate’. In this case, the fuzzy terms ‘popular’ and ‘moderate’ may be manipulated as in Figs. 2 and 3, respectively.

. Negation (‘not’)

Example 5.. Consider a fuzzy query that finds ‘not \*popular national parks in the USA’. In this case, the DI, the PI, logical operator and stop words may be as follows: DI={national parks, USA,. . .}, PI={No. of visitors,. . .}, logical operator={not}, stop words={in, the}. This fuzzy query is similar to Example 1 but the fuzzy term ‘popular’ is negated. According to Fig. 2, the negated fuzzy term ‘not popular’ may be represented as follows (Fig. 4).

![](/api/attachments/K7CJ8TER/fulltext/images/b0c31e37dabe2dd45ba7f9f67c8e3f0d7f735294da9c5c908504c28d22d65e47.jpg)  
Fig. 4. A membership function of ‘not popular’.

Table 3  
Table 2  
A snapshot of Integrated Index (DI+PI) after processing Q<sub>1</sub>

<table><tr><td>Document Index (DI)</td><td>IPs</td><td colspan="3">Perception Index (PI)</td><td>FPs (Results)</td></tr><tr><td rowspan="5">National parks, USA</td><td> $A_1$ </td><td>Distance</td><td>No. of visitors</td><td>...</td><td> $A_1$ </td></tr><tr><td> $A_2$ </td><td>Distance</td><td>No. of visitors</td><td>...</td><td> $A_2$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $A_{99}$ </td><td>Distance</td><td>No. of visitors</td><td>...</td><td> $A_{99}$ </td></tr><tr><td> $A_{100}+Irrelevant URLs$ </td><td>Distance</td><td>No. of visitors</td><td>...</td><td> $A_{100}+Irrelevant URLs$ </td></tr></table>

IPs: Intermediate Pointers; FPs: Final Pointers; URLs: Uniform Resource Locators.

3.2. Query processing based on the integrated index (DI+PI)

Now, we present how this search engine processes fuzzy queries. Let the set of national parks in the USA be $ \mathrm { A } { = } \{ \mathrm { A } _ { 1 } , ~ \mathrm { A } _ { 2 } { , } { \cdot } { \cdot } , ~ \mathrm { A } _ { 9 9 } , ~ \mathrm { A } _ { 1 0 0 } \}$ and each ${ \bf A } _ { i } , ( i { = } 1 , 2$ . . ., 100) has its own PT (page title) or URL.

Example 6.. Consider a crisp query that finds ‘national parks in the $\mathrm { U S A } ^ { , } \left( \mathrm { Q } _ { 1 } \right)$ . In this case, the PI is not used. So, this search engine uses only the phase 1 in Fig. 1. Thus, the integrated index is made as follows (Table 2). In the crisp query case, this search engine returns the same results that the existing search engines do. We note that IPs and FPs are equal.

Example 7.. Consider a fuzzy query that finds ‘\*popular national parks in the USA’ (Q<sub>2</sub>). In this case, the DI and the PI are used. So, this search engine uses both the phase 1 and the phase 2 in Fig. 1. We assume that $\mathrm { Q } _ { 2 }$ is $\mathrm { A _ { p } , A _ { p } { \in } \{ A _ { 1 } , A _ { 2 } , . . . , A _ { 9 9 } , A _ { 1 0 0 } \} }$ , by using a-cut in Fig. 2. Thus, the integrated index is made as follows (Table 3).

Example 8.. Consider a fuzzy query that finds ‘national parks \*moderate distance from San Fran cisco’ $\left( \mathbf { Q } _ { 3 } \right)$ . In this case, the DI and the PI are used. $\mathrm { S o } ,$ this search engine uses both the phase 1 and the phase 2 in Fig. 1. We assume that $\mathrm { Q } _ { 3 }$ is $\mathrm { A } _ { \mathrm { m } } , \mathrm { A } _ { \mathrm { m } } \in \{ \mathrm { A } _ { 1 } ,$ $\mathrm { A } _ { 2 } , . . . , \mathrm { A } _ { 9 9 } , \mathrm { A } _ { 1 0 0 } \}$ , by using a-cut in Fig. 3. Thus, the integrated index is made as follows (Table 4).

Example 9.. Consider a fuzzy query that finds ‘national parks that \*popular and \*moderate distance from San Francisco’ $\mathrm { ( Q _ { 4 } ) }$ . In this case, the DI and the PI are used. So, this search engine uses both the phase 1 and the phase 2 in Fig. 1. Then the query results with respect to $\mathrm { Q } _ { 4 }$ become $\{ \mathbf { A _ { p } } \} \cap$ $\left\{ \mathsf { A } _ { \mathrm { m } } \right\}$ . For instance, let $\mathrm { A } _ { \mathrm { p } }$ be a set $\left\{ \mathbf { A } _ { 1 } , \mathbf { A } _ { 2 } , \mathbf { A } _ { 3 } \right\}$ and $\mathbf { A } _ { \mathrm { m } }$ be a set $\{ \mathbf { A } _ { 1 } , ~ \mathbf { A } _ { 4 } , ~ \mathbf { A } _ { 5 } \}$ , then $\{ \mathbf { A _ { p } } \} \cap \{ \mathbf { A _ { m } } \} = \{ \mathbf { A } _ { 1 } \}$ Thus, the integrated index is made as follows (Table 5).

Example 10.. Consider a fuzzy query that finds ‘national parks that \*popular or \*moderate distance from San Francisco’ $( \mathrm { Q } _ { 5 } ) .$ . In this case, the DI and the PI are used. So, this search engine uses both the phase 1 and the phase 2 in Fig. 1. Then the query results with respect to $\mathrm { Q } _ { 5 }$ become $\{ \mathbf { A _ { p } } \} \cup \{ \mathbf { A _ { m } } \}$ . For instance, let $\mathrm { A } _ { \mathrm { p } }$ be a set $\left\{ \mathbf { A } _ { 1 } , \mathbf { A } _ { 2 } , \mathbf { A } _ { 3 } \right\}$ and $\mathbf { A } _ { \mathrm { m } }$ be a set $\{ \mathbf { A } _ { 1 } , ~ \mathbf { A } _ { 4 } , ~ \mathbf { A } _ { 5 } \}$ , then $\{ \mathrm { A _ { p } } \} \cup \{ \mathrm { A _ { m } } \} = \{ \mathrm { A } _ { 1 } , ~ \mathrm { A } _ { 2 } , ~ \mathrm { A } _ { 3 } ,$ $\begin{array} { r l } { \mathbf { A } _ { 4 } , } & { { } \mathbf { A } _ { 5 } \} } \end{array}$ . Thus, the integrated index is made as follows (Table 6).

Example 11.. Consider a fuzzy query that finds ‘not \*popular national parks in the $\mathrm { U S A } ^ { \prime } \left( \mathrm { Q } _ { 6 } \right)$ . In this case, the DI and the PI are used. So, this search engine uses both the phase 1 and the phase 2 in Fig. 1. Then the query results with respect to $Q _ { 6 }$ become $\{ \sim \mathrm { A _ { p } } \}$ . For instance, let $\mathrm { A } _ { \mathrm { p } }$ be a set $\left\{ \mathbf { A } _ { 1 } , \mathbf { A } _ { 2 } , \mathbf { A } _ { 3 } \right\}$ , then $\{ \sim \mathrm { A _ { p } } \} =$ $\{ \mathrm { A } _ { 4 } , \mathrm { A } _ { 5 } , . . . , \mathrm { A } _ { 9 9 } , \mathrm { A } _ { 1 0 0 } \}$ if the universal set $\mathrm { A } { = } \{ \mathrm { A } _ { 1 } .$ $\mathrm { A } _ { 2 } , . . . , \mathrm { A } _ { 9 9 } , \mathrm { A } _ { 1 0 0 } \}$ . Thus, the integrated index is made as follows (Table 7).

A snapshot of Integrated Index (DI+PI) after processing $\mathrm { Q } _ { 2 }$

<table><tr><td>Document Index (DI)</td><td>IPs</td><td colspan="3">Perception Index (PI)</td><td>FPs (Results)</td></tr><tr><td>National parks, USA</td><td> $\{A_1,\dots,A_{100}\}+Irrelevant URLs$ </td><td>Distance</td><td>No. of visitors</td><td>...</td><td>URLs w.r.t  $\{A_p\}$ </td></tr></table>

Focal keyword: National parks; Focal attribute: No. of visitors.

Table 4  
A snapshot of Integrated Index (DI+PI) after processing $\mathrm { Q } _ { 3 }$

<table><tr><td>Document Index (DI)</td><td>IPs</td><td colspan="3">Perception Index (PI)</td><td>FPs (Results)</td></tr><tr><td>National parks, San Francisco</td><td> $\{A_1, \dots, A_{100}\} + Irrelevant URLs$ </td><td>Distance</td><td>No. of visitors</td><td>...</td><td>URLs w.r.t  $\{A_m\}$ </td></tr></table>

Focal keyword: San Francisco; Focal attribute: Distance.

3.3. User interface based on the integrated index (DI+PI)

Williams [18] developed a user interface for information retrieval systems to aid users in formulating a query. The system, RABBIT III, supports interactive refinement of queries by allowing users to critique retrieved results with labels such as ‘require’ and ‘prohibit’. Williams claims that this system is particularly helpful to naive users with only a vague idea of what they want and therefore need to be guided in the formulation/reformulation of their queries or who have limited knowledge of a given database or who must deal with a multitude of databases. This process allows users to refine their queries. In a similar sense, we can refine user’s query by means of the phase 2 for processing fuzzy term(s) in Fig. 1. Thus, search engine will return the targeted results that users really want. An important problem relating to personalization concerns understanding how a machine can help an individual user via suggesting recommendations [1]. In our approach, the PI can help the user to specify clearly what he/she really wants. More specifically, the user in the system is asked to specify fuzzy term(s) in a query. In this respect, the PI may be regarded as a recommendation for handling fuzzy term(s) in a query. As a result, search engine returns ‘the targeted results’. Now, we describe user interface for phase 1 and phase 2 in Fig. 1.

## 3.3.1. User interface for phase 1

Initially, user interface for phase 1 lets user specify his/her queries with only crisp terms (keywords), or both crisp terms and fuzzy terms. If user submits a query with only crisp terms, only user interface for phase 1 is used, and search results are returned based on only the DI. On the other hand, if user submits a query with both crisp terms and fuzzy terms, user interface for phase 2 is also displayed to process the fuzzy terms.

## 3.3.2. User interface for phase 2

For the fuzzy query on the Internet, the ‘ease of use’ is important because Internet users are broad spectrum in terms of cultural differences, level of intelligence, etc. In this respect, user interface for phase 2 should provide Internet users with an easy user interface for specifying these fuzzy terms such as ‘popular’, ’moderate’, ‘big’, etc. In addition, we need to reflect cultural differences. For instance, different people generally use different scales (i.e., feet, miles, meter, etc.).

Internet users have their own membership functions with respect to fuzzy terms in a fuzzy query. Consequently, they can give values with respect to fuzzy terms in the user interface for phase 2.

User interface for phase 2 displays a PI associated with a focal keyword. For example, given a fuzzy query that finds ‘\*popular national parks in the USA’, a PI associated with a focal keyword ‘national parks is displayed as shown in Table 3. It should be noted that different people may use different conceptual comprehension (fuzzy terms, membership functions, a-cut), with respect to the same situation. It is the user’s task in this user interface to examine the suggested attributes in the PI, and to specify the values of the focal attributes reflecting user’s query requirements. Using the PI, search results can be restricted within narrow limit. We call it ‘target search by fuzzy terms’. In other words, search engine will return the targeted results that users really want.

Table 5  
A snapshot of Integrated Index (DI+PI) after processing $\mathrm { Q } _ { 4 }$

<table><tr><td>Document Index (DI)</td><td>IPs</td><td colspan="3">Perception Index (PI)</td><td>FPs (Results)</td></tr><tr><td>National parks, San Francisco</td><td> $\{A_1,\dots,A_{100}\}+Irrelevant URLs$ </td><td>Distance</td><td>No. of visitors</td><td>...</td><td>URLs w.r.t  $\{A_p\} \cap \{A_m\}$ </td></tr><tr><td colspan="6">Focal keyword: San Francisco; Focal attributes: Distance and no. of visitors.</td></tr></table>

Table 6  
A snapshot of Integrated Index (DI+PI) after processing $\mathrm { Q } _ { 5 }$

<table><tr><td>Document Index (DI)</td><td>IPs</td><td colspan="3">Perception Index (PI)</td><td>FPs (Results)</td></tr><tr><td>National parks, San Francisco</td><td> $\{A_1, \dots, A_{100}\} + Irrelevant URLs$ </td><td>Distance</td><td>No. of visitors</td><td>...</td><td>URLs w.r.t  $\{A_p\} \cup \{A_m\}$ </td></tr></table>

Focal keyword: San Francisco; Focal attributes: Distance and no. of visitors.

Fuzzy terms are specified in user interface for phase 2. For example, they can be expressed as point value, interval value, multiple values, etc.

. Point value

Example 12.. In Example 1, given a a-cut, the fuzzy term ‘popular’ may be specified by using a focal attribute ‘no. of visitors’. More specifically, it is expressed as a point 3.4 (i.e., ‘no. of visitors’<sub>z</sub>3.4 millions).

. Interval value

Example 13.. In Example 2, given a a-cut, the fuzzy term ‘moderate’ may be specified by using a focal attribute ‘distance’. More specifically, it is expressed as an interval (i.e., distance=[50, 150] in miles).

. Multiple values

A veristic variable [23,24] which can be assigned two or more values in its universe simultaneously will be specified as multiple values.

Example 14.. Let U be the universe of natural languages and let X denote the fluency of an individual in English, French and Italian. Then, X isv (1.0 English+0.8 French+0.6 Italian) means that the degrees of fluency of X in English, French and Italian are 1.0, 0.8 and 0.6, respectively [23,24].

## 4. Some features of the proposed method

Remark 1.. The higher the a in a-cut (0VaV1), the smaller the number of the targeted results. This property provides continual incremental result from ‘the highest constraint (i.e., a=1)’ to ‘the lowest constraint (i.e., a=0)’. Consequently, we can achieve ‘interactive user control of the query processing’ by adjusting the value of a.

Remark 2.. If a=0, search results coincide with the results by applying only the DI (i.e., the existing keyword-based search). In this case, the results of phase 1 in Fig. 1 become search results.

Remark 3.. Even though the same integrated index (DI+PI) is given, different search results are returned by adjusting the value of a or by using different focal attributes in the PI. In the case of ‘using different focal attributes in the PI’, for example, consider a fuzzy query that finds ‘attractive car’, where ‘attractive means ‘comfortable and fast’. In this case, for the fuzzy term ‘attractive’, people may use different focal attributes (i.e., size, speed, etc.) in the PI. In addition, different people may use different conceptual comprehension (fuzzy terms, membership functions, acut), with respect to the same situation. Thus, search engine will return the targeted results that users really want (i.e., personalization). In the meantime, clustering (i.e., grouping similar documents together to expedite information retrieval) is adaptively determined depending on the value of a or the selected focal attributes in the PI.

Remark 4.. For comparing with commercial keywordbased Web search engines, the ratio [the number of FPs/the number of IPs] can be used as a measure of performance evaluation on the proposed method. We note that the number of IPs is the result of phase 1 and the number of FPs is the result of phase 2 in Fig. 1. The smaller the ratio, the better the filtering effect of the proposed method. For example, in the case of fuzzy query $\mathrm { Q } _ { 2 }$ in Example 7,

A snapshot of Integrated Index (DI+PI) after processing $Q _ { 6 }$

<table><tr><td>Document Index (DI)</td><td>IPs</td><td colspan="3">Perception Index (PI)</td><td>FPs (Results)</td></tr><tr><td>National parks, USA</td><td> $\{A_1,\dots,A_{100}\}+Irrelevant URLs$ </td><td>Distance</td><td>No. of visitors</td><td>...</td><td>URLs w.r.t  $\{ \sim A_p\}$ </td></tr></table>

Focal keyword: National parks; Focal attribute: No. of visitors.

(i) Yahoo: The proposed method=34,200: $\mathrm { A } _ { \mathrm { p } } .$ . In this case, the ratio $\mathbf { \Sigma } = [ \mathbf { A _ { p } } / 3 4 \mathbf { , } 2 0 0 ]$

(ii) Google: The proposed method=73,100: $\mathrm { A } _ { \mathrm { p } } .$ . In this case, the rati $\scriptstyle \mathbf { \mu } _ { \mathrm { > } } [ \mathbf { A } _ { \mathrm { p } } / 7 3 , 1 0 0 ]$

Yahoo and Google return 34,200 and 73,100 on the fuzzy query $\mathrm { Q } _ { 2 } .$ , respectively. It should be noted that commercial keyword-based Web search engines use only the phase 1 in Fig. 1.

## 5. Personalized search and ranking

The Web is an impressive success story in terms of both its available information and the growth rate of human users. It now penetrates most areas of our lives, and its success is based on its simplicity. Unfortunately, this simplicity could hamper further Web development [4]. Often, search engines will return many results, but most will be uninteresting to the user. If a search tool can learn preferences or contexts from the user, this information can be used to hone the search or document-ranking process.

As described in Remark 3, in the case of ‘using different focal attributes in the PI’, for example, consider a fuzzy query that finds ‘attractive $\operatorname { c a r } ^ { \prime }$ where ‘attractive’ means ‘comfortable and fast’. In this case, for the fuzzy term ‘attractive’, people may use different focal attributes (i.e., size, speed, etc.) in the PI. In addition, different people may use different conceptual comprehension (fuzzy terms, membership functions, a-cut), with respect to the same situation. Thus, by using the PI, search engine will return the personalized search results that users really want.

Ranking algorithm plays an important role in Web search engines. In the existing Web search engines, however, detailed information regarding ranking algorithms used by major search engines is not publicly available. A simple means to measure the quality of a Web page, proposed by Carriere and Kazman [2], is to count the number of pages with pointers to the page. Google is a representative Web search engine that uses link information. Its rankings are based, in part, on the number of other pages with pointers to the page. In November 1999, Northern Light introduced a new ranking system, which is also based, in part, on link data [32]. In other words, Google and Northern Light rank search results, in part, by popularity. In the meantime, HotLinks ranks search results based on the bookmarks of its registered users. Yahoo’s Inktomi-served results aren’t ranked by popularity [33].

In theory, more popular links indicate more relevant content, but if a user differs from the crowd, simply popularity-based ranking approaches dive deeply into other possibilities on the Web. Consequently, they often give users many Web pages irrelevant to user’s query. In addition, they often tend to return unranked random samples in response to user’s query. In order to tackle these problems, we introduce a new ranking algorithm based on the Perception Index (PI).

Zadeh suggested we can represent linguistic quantifiers as fuzzy subsets of the unit interval [22]. In this representation the membership grade of any proportion $r { \in } [ 0 _ { \cdot }$ , 1], Q(r), is a measure of the compatibility of the proportion r with the linguistic quantifier we are representing by the fuzzy subset Q. For example, if Q is the quantifier ‘most’ then Q(0.9) represents the degree to which 0.9 satisfies the concept ‘most’. Yager identified three classes of linguistic quantifiers that cover most of these used in natural language [20,21].

(i) A quantifier Q is said to be monotonically nondecreasing if $\mathbf { r } _ { 1 } > \mathbf { r } _ { 2 }$ then $Q ( \mathbf { r } _ { 1 } ) { \ge } \mathrm { Q } ( \mathbf { r } _ { 2 } )$

(ii) A quantifier Q is said to be monotonically nonincreasing if $\mathbf { r } _ { 1 } { > } \mathbf { r } _ { 2 }$ then $Q ( \mathbf { r } _ { 1 } ) { \le } \mathrm { Q } ( \mathbf { r } _ { 2 } )$

(iii) A quantifier Q is said to be unimodal if there exists two values aVb both contained in the unit interval such that for r<a, Q is monotonically nondecreasing, for r>b, Q is monotonically nonincreasing, and for $\mathrm { \bf { r } } { \in } [ { \mathrm { { a } } } ,$ , b], Q(r)=1. Fig. 5 shows prototypical examples of these quantifiers.

In a similar way, we can identify three classes of fuzzy terms that cover most of these used in natural language. For example, in Section 3.1, we have represented the fuzzy terms ‘popular’ (monotonically nondecreasing), ‘moderate’ (unimodal), ‘not popular (monotonically nonincreasing), (see Figs. 2 – 4). In this respect, we design a new ranking algorithm based on the PI as follows.

![](/api/attachments/K7CJ8TER/fulltext/images/fcd2ffa484e48c270aecf70e0059d238bb45a8b1cd66407052bf3850769e2afd.jpg)  
(i) Monotonically nondecreasing

![](/api/attachments/K7CJ8TER/fulltext/images/e4e4d2321df342ef94942138da288f2a2e18da4bcf56e8735197c3d64a3af254.jpg)

(ii) Monotonically nonincreasing  
![](/api/attachments/K7CJ8TER/fulltext/images/12b5c458cc272f5c55297f17dc7bbccb286dcf0cc9bae835bcbc53f272a38575.jpg)  
(iii) Unimodal  
Fig. 5. Three types of quantifiers.

## Algorithm 1 (Ranking for one focal attribute).

(i) Monotonically nondecreasing case : The larger the value of focal attribute in the PI, the higher the rank retrieved documents for a given fuzzy query.

(ii) Monotonically nonincreasing case : The larger the value of focal attribute in the PI, the lower the rank retrieved documents for a given fuzzy query.

(iii) Unimodal case : If an interval of focal attribute determined by a-cut is $[ \mathbf { a } _ { \mathrm { i } } , \mathbf { b } _ { \mathrm { i } } ] ,$ , and let $\beta$ denote the midpoint between $\mathbf { a } _ { \mathrm { i } }$ and $\mathsf { b } _ { \mathrm { i } } ,$ then the degree of closeness (nearness) to $\beta$ can be used as a ranking criterion. In other words, the closer $\beta$ is, the higher is the rank retrieved documents for a given fuzzy query.

Example 15. Consider a fuzzy query that finds ‘popular national parks in the USA’. In this case, the fuzzy term ‘popular’ may be represented by a monotonically nondecreasing membership function, (see Fig. 2). We assume that ‘popular national parks in the USA’ are $\mathrm { A } _ { \mathrm { p } }$ by using a-cut. Let the targeted results $\mathrm { A } _ { \mathrm { p } }$ be $\{ \mathsf { A } _ { \mathrm { p } } ^ { 1 } , \mathsf { \bar { A } } _ { \mathrm { p } } ^ { 2 } , . . . , \mathsf { A } _ { \mathrm { p } } ^ { r } \}$ taking values of focal attribute (i.e., no. of visitors) such as Val $( \mathrm { A _ { p } ^ { 1 } } ) { \leq } \mathrm { V a l }$ $( \mathrm { A _ { p } ^ { 2 } } ) { \leq } . . . { \leq } \mathrm { V a l } ~ ( \mathrm { A _ { p } ^ { r } } )$ , then the targeted results $\mathrm { A } _ { \mathrm { p } }$ are ranked as the following order: $\mathrm { A } _ { \mathrm { p } } ^ { r } , . . . , \mathrm { A } _ { \mathrm { p } } ^ { 2 } , \mathrm { A } _ { \mathrm { p } } ^ { 1 }$

Example 16. Consider a fuzzy query that finds ‘national parks moderate distance from San Francisco’. In this case, the fuzzy term ‘moderate’ may be represented by a unimodal membership function, (see Fig. 3). We assume that ‘moderate national parks in the USA’ are $\mathbf { A } _ { \mathrm { m } }$ by using a-cut. Let an interval of focal attribute (i.e., distance) determined by a-cut be $[ \mathbf { a } _ { i } , \ \mathbf { b } _ { i } ] .$ , and let $\beta$ denote the midpoint between $\mathbf { a } _ { \mathrm { i } }$ and $\mathsf { b } _ { \mathrm { i } } ,$ and let the targeted results $\mathbf { A } _ { \mathrm { m } }$ be $\{ \mathbf { A } _ { \mathrm { m } } ^ { 1 } , \mathbf { A } _ { \mathrm { m } } ^ { 2 } , . . . , \mathbf { A } _ { \mathrm { m } } ^ { s } \}$ taking values of the focal attribute such as Val $( \mathbf { A } _ { \mathrm { m } } ^ { 1 } )$ , Val $( \mathrm { A } _ { \mathrm { m } } ^ { 2 } ) , \ldots ,$ Val $( \mathsf { A } _ { \mathrm { m } } ^ { s } )$ . If the degree of closeness (nearness) to $\beta$ is the order Val $( \mathrm { A } _ { \mathrm { m } } ^ { \mathrm { \bar { l } } } )$ , Val $( \mathrm { A } _ { \mathrm { m } } ^ { 2 } ) , \ldots ,$ Val $( \operatorname { A } _ { \mathrm { m } } ^ { s } )$ , then the targeted results $\mathbf { A } _ { \mathrm { m } }$ are ranked as the following order: $\mathrm { A } _ { \mathrm { m } } ^ { 1 } ,$ ${ \bf A } _ { \mathrm { m } } ^ { 2 } , . . . , { \bf A } _ { \mathrm { m } } ^ { s } .$

Example 17. Consider a fuzzy query that finds ‘not popular national parks in the USA’. In this case, the negated fuzzy term ‘not popular’ may be represented by a monotonically nonincreasing membership function (see Fig. 4). We assume that ‘not popular national parks in the USA’ are ${ \sim } \mathbf { A } _ { \mathfrak { p } }$ by using a-cut. Let the targeted results ${ \sim } \mathbf { A } _ { \mathbf { p } }$ be $\{ \mathbf { A } _ { \mathrm { p } } ^ { 1 } , \mathbf { A } _ { \mathrm { p } } ^ { 2 } , . . . , \mathbf { A } _ { \mathrm { p } } ^ { \ t } \}$ taking values of focal attribute (i.e., no. of visitors) such as Val $( \mathrm { A _ { p } ^ { 1 } } ) { \leq } \mathrm { V a l \ ( \mathrm { A _ { p } ^ { 2 } } ) { \leq } . . . { \leq } V a l \ ( \mathrm { A _ { p } ^ { \it t } } ) }$ , then the targeted results ${ \sim } \mathrm { A _ { p } }$ are ranked as the following order: $\mathrm { A _ { p } ^ { 1 } }$ $\mathsf { A } _ { \mathrm { p } } ^ { 2 } , . . . , \mathsf { A } _ { \mathrm { p } } ^ { t }$

Algorithm 2 (Ranking for multiple focal attributes). If we have multiple focal attributes (for instance, $\cdot _ { \mathrm { n o . } }$ of visitors’ and ‘distance’), weighting the importance of focal attributes should be considered. For the weighted case, assume that $\theta _ { 1 } , \ \theta _ { 2 } , . . . . , \ \theta _ { n }$ are ordinal weights. Then we refer to $\Theta { = } ( \Theta _ { 1 } , ~ \Theta _ { 2 } , . ~ . ~ . , ~ \Theta _ { \mathrm { n } } )$ as a weighting, where $\theta _ { i }$ is the weight of attribute i. Intuitively, the targeted results can be ranked according to the ordinal weights. For a respective focal attribute, the rank retrieved documents for a given fuzzy query can be determined based on Algorithm 1.

Example 18. Consider a fuzzy query that finds ‘national parks that popular and moderate distance from San Francisco’. In this case, the fuzzy terms ‘popular’ and ‘moderate’ may be represented by a monotonically nondecreasing membership function and a unimodal membership function, respectively. Using the results of Examples 15 and 16, if the weight of focal attribute ‘no. of visitors’ is more important than the weight of focal attribute ‘distance’, then the targeted results are ranked as the following order: $\mathrm { A } _ { \mathrm { p } , \cdot } ^ { r } \cdot \cdot , \mathrm { A } _ { \mathrm { p } } ^ { 2 } , \mathrm { A } _ { \mathrm { p } } ^ { 1 } , \mathrm { A } _ { \mathrm { m } } ^ { 1 } , \mathrm { A } _ { \mathrm { m } , \cdot } ^ { 2 } . . . , \mathrm { A } _ { \mathrm { m } } ^ { s }$

Now, if we apply Algorithms 1 and 2, the targeted results can be displayed from the highest rank to the lowest rank. Although the existing ranking methods for Web search engines also provide users with their own ranking algorithms based on popularity, bookmark, etc., their approaches look like the behind-thescenes processing. In the proposed approach, user’s search intentions can be explicitly reflected by using the values of focal attributes in the PI. In this respect, we can explicitly describe how to rank the search results by means of the proposed algorithms. Consequently, the proposed algorithms provide a user with the personalized ranking based on user’s search intentions.

## 6. Additional considerations

The work of Lidsky and Kwon [10] is an opinionated but informative resource on search engines. It describes 36 different search engines and rates them on specific details of their search capabilities. For instance, in one study, searches are divided into five categories: (1) simple searches; (2) custom searches; (3) directory searches; (4) current news searches; and (5) Web content. The five categories of search are evaluated in terms of power and ease of use. Variations in ratings sometimes differ substantially for a given search engine. In the meantime, they chose the respective best search engine according to five categories: (1) search indexes and directories; (2) people finders; (3) business finders; (4) usenet search; and (5) metasearch. The data indicate that as the number of people using the Internet and Web has grown, user types have diversified and search engine providers have begun to target more specific types of users and queries with specialized and tailored search tools. In this respect, for the fuzzy query processing, topicspecific (or domain-specific) requirement is necessary because of the following reasons: (1) commonsense knowledge—the present state of AI is not up to formulating a full commonsense database, but full commonsense knowledge is not necessary [12]. In this respect, for the fuzzy query processing, if we design a search engine based on ‘domain-specific’ concept, the degree of freedom on fuzzy terms will be highly reduced. In other words, ‘domain-specific’ concept provides the higher possibility for a well-defined (restricted) condition. For example, given a traveldomain database, consider a fuzzy query that finds ‘popular national parks in the USA’. In this case, the fuzzy term ‘popular’ is used to restrict ‘national parks’, not ‘music’, ‘entertainer’, etc.; (2) indexing overhead—human indexing (for example, Yahoo!, LookSmart, etc.) is currently the most accurate because experts on popular subjects organize and compile the directories and indexes in a way which facilitates the search process. However, the enormous number of existing Web pages and their rapid increases and frequent updating make the indexing a difficult one or an overhead. If we design a search engine based on ‘domain-specific’ concept, the indexing overhead on the PI will be highly reduced; (3) storage requirement—comparing with traditional Web search engines, recommending the PI requires the system to maintain more data. If we design a search engine based on ‘domain-specific’ concept, the storage requirement on the PI will be highly reduced.

## 7. Concluding remarks

The expressive power of conventional search engine query interfaces is relatively weak when restricted to keyword-based search (i.e., Document Index (DI)-based search). At present, the keywordbased search engines present limitations in modeling perceptual aspects of humans. In addition, they are unsuccessful in returning the targeted results. In other words, they generally return many Web pages (or URLs) irrelevant to user’s query. In this respect, we need a new tool to handle both the fuzzy query and the removal of spurious results. In order to tackle these problems, we introduce the Perception Index (PI) that contains attributes associated with a focal keyword restricted by fuzzy term(s) in a fuzzy query. If we integrate the Document Index (DI) used in commercial Web search engines with the proposed PI, we can handle both crisp terms (keyword-based) and fuzzy terms (perception-based). In this respect, the proposed approach is softer than the keywordbased approach (i.e., commercial Web search engines). It is a further step toward a human-friendly, natural language-based interface for Web searching. The proposed method assists the user to reflect his/her perception in the process of query. As a consequence, Internet users can narrow thousands of hits to the few that users really want. In this respect, the PI provides a new tool for targeting queries that users really want, and a way for personalized search and ranking. The use of PI provides helpful hints for solving the problems of ‘large answer set’, ‘low precision’, ‘ineffective for general-concept queries’ suffered by most search engines. In this paper, we also present a personalized search and ranking based on the PI.

## Acknowledgements

The author wishes to thank Prof. L.A. Zadeh for his inspirational address on the perceptual aspects of humans. The idea of Perception Index (PI) is inspired by his papers [23–25] and his comments in the BISC (Berkeley Initiative in Soft Computing) seminars and group meetings. He also thanks Sun-Gyung Jung, plan and control manager/education center of Oracle Korea, Si-Young Choi and Jae-Hyun Choi, for their encouragement. He would like to thank the anonymous referees for their comments and suggestions, which helped to improve this paper. This work was supported by postdoctoral fellowships program from Korea Science and Engineering Foundation (KOSEF), and in part by the BISC program of University of California, Berkeley and the BT advanced communication technology center (BTexact).

## References

[1] N.J. Belkin, Helping people find what they don’t know, Communications of the ACM 43 (8) (2000) 58–61.

[2] J. Carriere, R. Kazman, WebQuery: searching and visualizing the Web through connectivity, Proceedings of the Sixth International Conference on the World Wide Web, 1997.

[3] D. Dubois, H. Prade, F. Sedes, Fuzzy logic techniques in multimedia database querying: a preliminary investigation of the potentials, IEEE Transactions on Knowledge and Data Engineering 13 (3) (2001) 383– 392.

[4] D. Fensel, M.A. Musen, The semantic Web: a brain for humankind, IEEE Intelligent Systems (March/April 2001) 24–25.

[5] A. Juozapavicius, R.E. Blake, Indices and data structures in information systems, Informatica 10 (1) (1999) 71 – 88.

[6] J. Kacprzyk, A. Ziolkowski, Retrieval from databases using queries with fuzzy linguistic quantifier, in: H. Prade, C.V. Negoita (Eds.), Fuzzy Logic in Knowledge Engineering, Verlag TUV, Rheinland, 1986.

[7] B. Kao, J. Lee, C.Y. Ng, D. Cheung, Anchor point indexing in Web document retrieval, IEEE Transactions on SMC (part C) 30 (3) (2000) 364 – 373.

[8] M. Kobayashi, K. Takeda, Information retrieval on the Web, ACM Computing Surveys 32 (2) (2000) 144 – 173.

[9] D.H. Kraft, F.E. Petry, Fuzzy Information systems: managing uncertainty in databases and information retrieval systems, Fuzzy Sets and Systems 90 (2) (1997) 183–191.

[10] D. Lidsky, R. Kwon, Searching the Net, PC Magazine 2 (Dec. 1997) 227–258.

[11] P. Martin, P.W. Eklund, Knowledge retrieval and the world wide web, IEEE Intelligent Systems (May/June 2000) 18– 25.

[12] J. McCarthy, Phenomenal data mining, Communications of the ACM 43 (8) (2000) 75 – 79.

[13] H. Nakajima, T. Sogoh, M. Arao, Development of an efficient fuzzy SQL for a large scale fuzzy relational database, Proceedings of the 5th IFSA World Congress (1993) 517–530.

[14] F. Petry, P. Bosc, Fuzzy Databases: Principles and Applications, Kluwer Academic Publishing, Norwell, MA, 1996.

[15] D. Rasmussen, R.R. Yager, Finding fuzzy and gradual functional dependencies with summary SQL, Fuzzy Sets and Systems 106 (2) (1999) 131– 142.

[16] S. Salton, Automatic Text Processing: The Transformation, Analysis and Retrieval of Information by Computer, Addison-Wesley, Reading, MA, 1989.

[17] C.A. Testemale, Database system dealing with incomplete or uncertain information and vague queries, in: H. Prade, C.V. Negoita (Eds.), Fuzzy Logic in Knowledge Engineering, Verlag TUV, Rheinland, 1986.

[18] M. Williams, What makes rabbit run?, Journal of Man-Machine Studies 2a (1) (1984) 333 – 352.

[19] Y.H. Wu, Y.C. Chen, A.L.P. Chen, Enabling personalized recommendation on the Web based on user interests and behaviors, Proceedings of Eleventh International Workshop on Research Issues in Data Engineering (RIDE 2001), IEEE Computer Society, 2001, pp. 17 – 24.

[20] R.R. Yager, On linguistic summaries of data, in: G. Piatetsky-Shapiro, B. Frawley (Eds.), In Knowledge Discovery in Databases, MIT Press, 1991, pp. 347 – 363.

[21] R.R. Yager, Database discovery using fuzzy sets, International Journal of Intelligence Systems 11 (1996) 691– 712.

[22] L.A. Zadeh, A computational approach to fuzzy quantifiers in natural language, Comput. Math. Appl. 9 (1983) 149– 184.

[23] L.A. Zadeh, Toward a theory of fuzzy information granulation

and its centrality in human reasoning and fuzzy logic, Fuzzy Sets and Systems 90 (2) (1997) 111 –127.

[24] L.A. Zadeh, From computing with numbers to computing with words—from manipulation of measurements to manipulation of perceptions, IEEE Transactions on Circuit and Systems 45 (1) (1999) 105 – 119.

[25] L.A. Zadeh, A new direction in AI—toward a computational theory of perceptions, AI Magazine 22 (1) (2001) 73– 84.

[26] http://www.semanticweb.org/knowmarkup.html.

[27] http://www.w3.org/XML.

[28] http://www.w3.org/RDF.

[29] http://www.oasis-open.org/cover/oml9808.html.

[30] http://ksi.cpsc.ucalgary.ca/KAW/KAW98/fensel1/.

[31] http://www.cs.berkeley.edu/\~nikraves/bisc/sig/internet/ msglaz2.htm.

[32] http://www.searchenginewatch.com/sereport/99/11briefs.html.

[33] http://websearch.about.com/internet/webserch/library/weekly aa052199.htm.

![](/api/attachments/K7CJ8TER/fulltext/images/c0cd539a48e5b699dc65801f3c3e41eab6ca672fc17ec3f3d6ec819deb4ed2bc.jpg)

Dae-Young Choi is an assistant professor in the Department of MIS at Yuhan College in Puchon city, South Korea. He received his BS, MS and PhD degrees in computer sciences from Sogang University, in 1985, 1992, and 1996, respectively. He was a research fellow at the Korea Institute for Defense Analyses from 1985 to 1990. He received postdoctoral fellowship from Korea Science and Engineering Foundation (KOSEF) in 2000. He was with the

BISC Group, Department of EECS, CS Division, University of California, Berkeley, as a visiting scholar, in 2001. He has a national certificate of professional engineer for information processing systems. His research interests include Web search engines, business intelligence, fuzzy systems, group decision support systems and applications of artificial intelligence.
