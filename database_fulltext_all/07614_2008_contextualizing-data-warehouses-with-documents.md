---
otero_id: 7614
otero_key: "MNQ4CEQH"
title: "Contextualizing data warehouses with documents"
authors: "Juan Manuel Pérez-Martínez; Rafael Berlanga-Llavori; María José Aramburu-Cabo; Torben Bach Pedersen"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.12.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Contextualizing data warehouses with documents

Juan Manuel Pérez-Martínez <sup>a,⁎</sup>, Rafael Berlanga-Llavori <sup>a,1</sup> María José Aramburu-Cabo <sup>a,1</sup>, Torben Bach Pedersen <sup>b,2</sup>

<sup>a</sup> Jaume I University, Spain

<sup>b</sup> Aalborg University, Denmark

Available online 7 February 2007

## Abstract

Current data warehouse and OLAP technologies are applied to analyze the structured data that companies store in databases. The context that helps to understand data over time is usually described separately in text-rich documents. This paper proposes to integrate the traditional corporate data warehouse with a document warehouse, resulting in a contextualized warehouse. Thus, the user first selects an analysis context by supplying some keywords. Then, the analysis is performed on a novel type of OLAP cube, called an R-cube, which is materialized by retrieving and ranking the documents and corporate facts related to the selected context. © 2006 Elsevier B.V. All rights reserved.

Keywords: OLAP; Text-rich XML documents; Information retrieval

## 1. Introduction

Current data warehouse and OLAP technologies can be efficiently applied to analyze the huge amounts of structured data that companies produce. These organizations also produce many documents and use the Web as their largest source of external information. Examples of internal and external sources of information include the following: purchase-trends and market-research reports; demographic and credit reports; popular business journals; industry newsletters; technology reports; etc. Although these documents cannot be analyzed by current OLAP technologies, mainly because they are unstructured and contain a large amount of text, they are highly valuable information that can help companies analyze their data. Because XML has become the standard for data exchange over the Internet [25], nowadays it is easy to find some of these documents in XML formats. Furthermore, existing XML tagging techniques [22] can be applied to give some structure to plain documents by identifying the different document sections, and exportation tools from most proprietary systems to XML-like formats are available now.

In this paper we present an architecture that integrates a corporate warehouse of structured data with a warehouse of text-rich XML documents. The resulting contextualized warehouse is a new type of decision support system that allows users to obtain strategic information by analyzing data under different contexts. For example, if we have a document warehouse with financial news articles, we can analyze the evolution of the sales measures of our corporate warehouse in the context of a period of crisis described by the relevant news. Thus, it is easier to find out which products were affected by the crisis.

Here, we define a context as a set of textual fragments that can provide analysts with strategic information important for decision-making tasks. Since the document warehouse may contain documents about many different topics, we apply modern Information Retrieval (IR) [2] techniques to select the context of analysis from the document warehouse. In order to build a contextualized OLAP cube, the analyst will specify the context under analysis by supplying a sequence of keywords. Each fact in the resulting cube will have a numerical value representing its relevance with respect to the specified context, thereby its name R-cube (Relevance cube). Moreover, each fact in the R-cube will be linked to the set of relevant documents that describe its context. In this paper we extend an existing multidimensional data model to represent these two new dimensions (relevance and context), and we study how the traditional OLAP operations are affected by them.

The relevance and context dimensions provide information about facts that can be very useful for analysis tasks. The relevance dimension can be used to explore the most relevant portions of an R-cube. For example, it can be used to identify the period of a political crisis, or the regions under economical development. The usefulness of the context dimension is twofold. First, it can be used to restrict the analysis to the facts described in a given subset of documents (e.g., the most relevant documents). Second, the user will be able to gain insight into the circumstances of a fact by retrieving its related documents.

The main contributions of this paper are: (1) an architecture that integrates a corporate warehouse with a document warehouse, resulting in a contextualized warehouse; (2) a formal definition of the multidimensional data model and the unary algebra operations to manage R-cubes; and (3) a prototypical system that shows the usefulness of the approach.

The rest of the paper is organized as follows: Section 2 discusses related work. In Section 3 we present the architecture of a contextualized warehouse and how the analysis cubes (R-cubes) are built. The multidimensional data model for R-cubes is presented in Section 4. In Section 5 we propose an algebra for R-cubes. A prototypical contextualized warehouse is shown in Section 6. Finally, Section 7 addresses conclusions and future work.

## 2. Related work

In [9] the importance of external contextual information to understand the results of historical analysis operations was emphasized: “External contextual information is information outside the corporation that nevertheless plays an important role in understanding information over time.” Since contextual information is usually available as documents (e.g., on-line news, company reports, etc.), which cannot be managed by relational systems, few approaches regarding contextual information in a data warehouse can be found in the literature. With the emergence of XML as the lingua franca of the Web, semi-structured information is now widely available, and several methods have been proposed to combine XML and data warehouses.

The problem of gathering and querying web data is not trivial, mainly because data sources are dynamic and heterogeneous. In this context, some works are focused on the construction of repositories for XML [26] and web documents [4]. The main issues addressed by them include efficient storage, indexing, query processing, data acquisition, change control and schema integration of data extracted from heterogeneous web sources.

In [17] OLAP operations are extended to involve dimensions and/or measures coming from external XML data. Unfortunately, this approach only deals with highly-structured XML data, thus being unsuitable for text-rich XML documents. Other approaches propose to apply OLAP-like operators to aggregate information of XML structured documents. For example, [3] proposes to extend XQuery [25] with grouping constructs to evaluate OLAP-style aggregation queries on XML documents, and [15] provides mechanisms to perform text aggregations on the XML textual contents. Nevertheless, these approaches do not regard the factual data included in XML texts, and they lack the mechanisms to relate corporate data warehouses with external XML documents.

The work presented in [21] proposes to annotate external information sources (e.g., documents, images, etc.) by means of an ontology that comprises all the values of the data warehouse's dimensions. In this way, each OLAP report can be associated with the external sources annotated with the same dimension values. This approach has several limitations that have been solved in our work. First, it is necessary to manually annotate all the documents, which is unfeasible for large collections. Second, this approach does not provide any mechanisms to actually integrate the corporate cubes with their contexts. Third, it does not provide a formal framework for calculating both document and fact relevance with respect to user queries.

Nowadays, any application required to manipulate large collections of documents applies Information Retrieval technology [2]. Recent proposals in the field of IR include Language Modeling [20] and Relevance

Modeling [11]. Language Modeling represents each document as a language model. Thus, documents are ranked according to the probability of obtaining the query keywords when taking random samples from their corresponding language models. Relevance Modeling estimates the joint probability of the query's keywords over the set of documents deemed relevant for that query. Language and Relevance Modeling outperform traditional IR models in many cases. One of the current hot topics in IR research is retrieval of XML data [5,8]. These approaches combine both keyword-based and structural retrieval conditions.

Our approach relies on Relevance Modeling mainly because of two reasons. First, Relevance Modeling provides a formal background based on the Probability Theory, which is also well-suited for OLAP operations. Second, contrary to Language Modeling, Relevance Modeling deals with sets of relevant documents instead of single documents, which seems more appropriate for representing the contexts of the facts in a data warehouse.

This paper is based on the results of previous work by the authors. In [18] we presented a model for text-rich XML documents. Over this model, several information extraction techniques have been developed to identify the facts described in the documents [7,12]. In [18] we also showed how to apply Relevance Modeling to estimate the relevance of facts extracted from documents, and in [19] we outlined its multi-dimensional implementation. In this paper we propose an approach to contextualizing corporate cubes with the facts extracted from documents, resulting in a new multi-dimensional model called R-cube.

## 3. Contextualized warehouses

A contextualized warehouse is a decision support system that allows users to combine all their sources of structured and unstructured data, and to analyze the integrated data under different contexts. Fig. 1 shows the proposed architecture for the contextualized warehouse. Its main components are a corporate warehouse, a document warehouse and the fact extractor module. The corporate warehouse is a traditional data warehouse that integrates the company's structured data sources [9,10]. The unstructured data coming from external and internal sources are stored in the document warehouse as XML documents. The fact extractor module relates the facts of the corporate warehouse with the documents that describe their contexts. In a contextualized warehouse, the user specifies an analysis context by supplying a sequence of keywords. The analysis is performed on a new type of OLAP cube, called an R-cube, which is materialized by retrieving the documents and facts related to the selected context. In this section, we first present an IR model for the document warehouse, then we describe the fact extractor module, and finally we show the R-cubes construction process.

![](/api/attachments/MNQ4CEQH/fulltext/images/e3101febbd6af59886dbd2e6dbbe18234117a1f5d605491b39de46264d1ba1a3.jpg)  
Fig. 1. Contextualized warehouse architecture.

## 3.1. An IR model for the document warehouse

The document warehouse is a repository of text-rich XML documents containing relevant information for analysis purposes. These documents are collected from the company internal and external unstructured information sources. This paper does not address the problems of data acquisition, filtering, change control and schema integration of XML data extracted from heterogeneous sources. These are studied in other works like [26]. In this section we adapt the IR model proposed in [18] to retrieve the documents that describe the analysis context. Our model, uses the traditional tree representation of XML documents and maps the elements of the original documents into nodes of the corresponding document trees.

Definition 1. Let $C o l { = } \{ d \}$ be the set of all the document nodes d of all the documents in the document warehouse. With $d ^ { \prime } \sqsubset d$ we denote that the node $d ^ { \prime }$ is a descendant of d. Let Text(d) represent the sequence of words contained in all the nodes under $d .$

In the document warehouse, a query is a tuple (XPath, Q), where: XPath is a path expression [25] that states a restriction on the structure of the documents; and $Q { = } q _ { 1 } q _ { 2 } . . . q _ { n }$ is an IR condition, consisting of a sequence of keywords $q _ { i } .$

We define XPath(d) as a boolean function over the set of document nodes of the warehouse, XPath: $C o l  \{ T r u e \}$ , False}. XPath(d) returns True if the document node d is selected by the path expression XPath, and False otherwise.

The query (XPath, Q) returns the set $R Q$ of the document nodes that maximize the Relevance to the IR condition $\mathcal { Q } ,$ which is defined as follows:

$$
\begin{array}{c} R Q = \left\{d \in C o l | X P a t h (d) \wedge | T e x t (d) \cap Q | \geq m \right. \\ \wedge \nexists d ^ {\prime} \sqsubset d (P (Q | d ^ {\prime}) \geq P (Q | d)) \} \end{array}
$$

Thus, $R Q$ is the set of document nodes that are selected by the XPath expression, contain at least m query keywords and maximize the relevance with respect to their subtrees.

The relevance of the document node d to the IR condition Q is calculated by the probability $P ( Q | d )$ of observing the query keywords in the document node. By following [11], we assume that the query keywords $q _ { i }$ are independent, and use formulas (1) and (2) for calculating P(Q|d).

$$
P (Q | d) = \prod_ {q _ {i} \in Q} P (q _ {i} | d)\tag{1}
$$

$$
P (q _ {1} | d) = \lambda \frac {T F (q _ {i} , d)}{| d | _ {t}} + (1 - \lambda) \frac {c t f _ {q _ {i}}}{c o l l \_ s i z e _ {t}}\tag{2}
$$

In formula (2), $T F ( q _ { i } , d )$ returns the frequency of the query keywords $q _ { i }$ in Text(d) (the number of occurrences of $q _ { i }$ in d and all its child nodes), $| d | _ { t }$ is the total number of words in $T e x t ( d ) , c t f _ { q _ { i } }$ is the number of times that $q _ { i }$ occurs in all the documents of the warehouse, and coll\_size is the total number of words in all the documents of the warehouse. The λ factor is called the smoothing parameter [11], as it avoids probabilities equal to zero when a document does not contain all the query keywords.

The approach described above ensures that the document nodes in the result have the proper granularity level to describe the IR condition Q. For example, let (XPath, Q) be a query in the document warehouse. First, the path expression XPath selects a subset of the document subtrees of the warehouse. Let d be a document node representing an article, and let $d ^ { \prime } \sqsubset d$ be a node depicting the second paragraph of this article. Both d and $d ^ { \prime }$ were selected by XPath. Let us consider that $d ^ { \prime }$ is more relevant than d for the given IR condition $\mathcal { Q } ,$ i.e., $P ( Q | d ) { < } P ( Q | d ^ { \prime } )$ . This setting could happen, for example, when all the query keywords only occur in the second paragraph of the article. Thus, $d ^ { \prime }$ and $d$ will have the same frequencies for the query keywords. That is, $T F ( q _ { i } , d ) { = } T F ( q _ { i } , d ^ { \prime } ) \forall q _ { i } { \in } \mathcal { Q }$ . However, the article d comprises all the words contained in $d ^ { \prime }$ plus all the words of the rest of paragraphs. Then, $| d | _ { t } { > } | d ^ { \prime } | _ { t } , P ( q _ { i } | d ) { < }$ $P ( q _ { i } | d ^ { \prime } ) \forall q _ { i } \in Q .$ , see formula (2), and $P ( Q | d ) { < } P ( Q | d ^ { \prime } )$ see formula (1). Since the second paragraph is actually the document portion that better describes the information required by Q (i.e., it obtains the maximum relevance in the subtree), the entire article d will not be included in $R Q ,$ , but we will instead insert the more specific and relevant paragraph $d ^ { \prime } .$

In the rest of the paper we will use the term “document” to mean “document node”, as the document nodes returned by a query are just text fragments describing the context under analysis.

## 3.2. The fact extractor module

Building a contextualized warehouse mainly means relating each fact of the corporate warehouse to its context. The fact extractor tool uses the dimensions defined in the corporate warehouse to detect the facts described in the documents. Next, we describe this process in detail by means of an example.

Let us consider the corporate warehouse of an international provider of vegetable oil by-products. The main products of this company include: fo1, fo2 (used as preservatives in the food sector), and he1 and he2 (used in the elaboration of healthcare products). The company keeps in its corporate warehouse a historical record of its sales, the quantity sold (Quantity measure) and its cost (Amount measure), per product and customer. Thus, the dimensions of the corporate warehouse are Time, Products and Customers. The Products are classified into Sectors (food and healthcare). Finally, Customers are organized into Countries and Regions (e.g., Southeast Asia, Central America, etc.).

Our example company also maintains a document warehouse of business newspapers gathered from the Internet in XML format. Fig. 2 shows a fragment of an example document of this warehouse. The document depicts a context for the sales of food sector products to customers of the Southeast Asian region, made during the second half of 1998. Notice that context's descriptions are very useful, as they contain detailed information about the facts of the corporate warehouse. For example, the document in Fig. 2 could help us to understand a sales drop.

By applying specific information extraction techniques [12,7], and considering the three analysis dimensions of the corporate warehouse, the dimension values Southeast Asia, food, and 1998/2nd half can be identified in the document fragment. The fact extractor tool builds all the valid facts for them, in this case, (Products.Sector= food, Custumers.Region = Southeast Asia, Time.Half\_year= 1998/2nd half ). As it can be noticed, some of these dimension values are not completely precise and belong to non-base dimension categories. For example, the Southeast Asia dimension value belongs to the category Region of the Customers dimension. We may also find documents where some dimensions are not mentioned, resulting in incomplete facts. For each fact, the fact extraction tool also calculates the number of times that its dimension values occur in the document fragment (i.e., the fact dimension values frequency). This frequency value determines the importance of the fact in the document, and will be used to estimate the relevance of the fact.

It is worth mentioning that the fact extractor module also regards synonyms (e.g., aliment and food) and other terms semantically related to the dimension values of the corporate warehouse, in order to identify valid facts. Our current implementation of the fact extractor module is an adaptation of the work [7], which is aimed at identifying complex instances from texts to populate an ontology. In our case, the ontology is formed by the corporate dimensions, and the instances are the multidimensional facts.

Let us now consider the second sentence of the example document in Fig. 2. It depicts two facts: (Company=Chicken SPC, Time.Year= 1997, Export= \$10,100,00), (Company=Chicken SPC, Time.Half\_year= 1998/2nd half, Export=\$1,300,00). Chicken SPC Inc. could be a potential customer or competitor of our example oil provider company. In this way, the document warehouse also provides highly valuable strategic information about some facts that are not available in the corporate warehouse or in external databases. However, these new facts will not be identified by our fact extraction module, since our process is guided by the corporate warehouse schema (i.e., the Company dimension is not available in the schema). Furthermore, most often documents contain already aggregated measure values (total exports in the facts of the previous example). The main problem here is to automatically infer the implicit aggregation function that has been applied (i.e., average, sum, etc.) Alternatively, the system could ask the user to determine the aggregation function by showing the document contents. In this context, different IR and information extraction-based methods for integrating documents and databases are discussed in [1]. Specifically, [1] proposes a strategy to extract from documents information related to (but not present in) the facts of the warehouse.

![](/api/attachments/MNQ4CEQH/fulltext/images/bac179c17c2f4a55ee5f9c82de843414709eef82277f6d032335c51ef90eb44a.jpg)  
Fig. 2. Example fragment of a business journal.

## 3.3. Building R-cubes

In this section we explain how the analysis cubes are materialized from the contextualized warehouse. We call them R-cubes and they include two special systemmaintained dimensions, namely the relevance and context dimensions.

In order to create an R-cube the analyst must supply a query of the form (Q, XPath, MDX), which states the following restrictions: (XPath, Q) is the query for retrieving a context from the document warehouse, and MDX are conditions over the dimensions and measures of analysis [24].

The query process takes place as follows:

1. The IR condition Q and the path expression XPath are evaluated in the documents' warehouse, obtaining the set of relevant documents RQ.

2. The fact extractor component parses the documents fragments obtained in step (1) and returns the set of facts described by each document fragment, along with their frequency. Notice that we do not parse entire documents, but only the document fragments in RQ.

3. Next, or in parallel to steps (1) and (2), the MDX conditions are evaluated on the corporate warehouse.

4. Then, each document is assigned to those facts whose dimension values can be “rolled-up” or “drilled-down” to some (possibly imprecise or incomplete) fact described by the document.

5. Finally, the relevance of each fact is calculated, resulting in an R-cube.

Continuing the running example, let us consider the analysis of the sales of food products under the context of a financial crisis reported by the business articles of the document warehouse. Thus, given Q = “financial, crisis”, XPath = “/business\_newspaper/economy/article//” and MDX = (Products.[food], Customers.Country, Time. [1998].Month, SUM(Measures.Amount)>0) as query conditions, the contextualized warehouse will return the R-cube presented in Table 1. This R-cube includes the set of facts of the corporate warehouse that satisfy the stated MDX conditions, along with their relevance values with respect to the IR condition (relevance dimension, depicted as R), and the set of text fragments where each fact occurs (context dimension, Ctxt).

As Table 1 shows, the relevance is a numeric value that measures the importance of each fact in the context established by the initial query conditions. The most relevant facts of our example R-cube involve the sales made to Japanese and Korean customers during the months of October and November 1998. We could obtain the details described in the documents by performing a drill-through operation on the context dimension [24]. By studying these documents we can find out that the Southeast Asian financial crisis reported by the document of Fig. 2, is a valid explanation for the sales drop. Each document $d _ { i }$ of the context dimension has also associated a relevance value (represented by the superscript) which measures how this document describes the analysis context.

Unlike OLAP-XML federations like those proposed in [17], R-cubes are materialized once, when the query is fetched to the contextualized warehouse, and will be incrementally updated when new relevant documents and data satisfying the original query are added to the system. The main advantage of this approach is that preaggregations can be performed over R-cubes, enabling fast analysis operations.

## 3.3.1. Fact relevance calculus

Next, we summarize the approach presented in [18] to calculate the relevance of a fact with respect to an IR condition. Intuitively, a fact will be relevant for a context if the fact is found in a document which is also relevant for the context.

Given the set of relevant documents RQ returned by the document warehouse, the relevance of a fact is estimated as the probability of observing it in $R Q { \mathrm { : } }$

$$
P (f | R Q) = \frac {\sum_ {d \in R Q} P (f | d) P (Q | d)}{\sum_ {d \in R Q} P (Q | d)}\tag{3}
$$

In formula (3), $P ( f | d )$ is the probability of finding the fact $f$ in a relevant document $d \in R Q .$ . This probability is estimated by formula (4). As we defined in Section 3.1, $P ( Q | d )$ is the probability of observing the query keywords in this document (see formula (1)).

$$
P (f | d) = F F (f, d) / | d | _ {f}\tag{4}
$$

In formula (4), $F F ( f , d )$ returns the frequency of the fact $f ^ { \ast } \mathrm { s }$ dimension values in the document d. That is, the number of times that the dimension values of the fact f occur in the document $d .$ $| d | _ { f }$ is the total number of dimension values found in the document $d .$

An interesting property of this approach is that the sum of the relevance values of all the facts in an R-cube is equal to one. However, notice that although all document collections are not suitable for every analysis tasks (e.g., an analysis on a financial crisis with a document collection about products manufacturing processes), the sum of the facts relevance values will be kept equal to one.

The denominator of formula (3) measures the overall relevance of the documents that satisfy the IR condition $\mathcal { Q } ,$ that is, the sum of the probabilities of observing the query keywords in each document of $R Q .$ . Thus, we propose formula (5) as a measure of the quality of an Rcube for the selected context:

$$
Q u a l i t y = \sum_ {d \in R Q} P (Q | d)\tag{5}
$$

## 4. A multidimensional data model for R-cubes

In this section we define a formal data model for the R-cubes. We extend an existing multidimensional model [16] with two new special dimensions to represent both the relevance of the facts and their context. For each component of the extended data model, we show its definition and give some examples.

Table 1 Example R-cube

<table><tr><td>F</td><td>Products.ProductId</td><td>Customers.Country</td><td>Time.Month</td><td>Amount</td><td>R</td><td>Ctxt</td></tr><tr><td> $f_1$ </td><td>fo1</td><td>Cuba</td><td>1998/03</td><td>4, 300, 000$</td><td>0.05</td><td> $d_3^{0.005}$ ,  $d_7^{0.005}$ </td></tr><tr><td> $f_2$ </td><td>fo2</td><td>Japan</td><td>1998/02</td><td>3, 200, 000$</td><td>0.1</td><td> $d_5^{0.02}$ </td></tr><tr><td> $f_3$ </td><td>fo2</td><td>Korea</td><td>1998/05</td><td>900, 000$</td><td>0.2</td><td> $d_4^{0.04}$ </td></tr><tr><td> $f_4$ </td><td>fo1</td><td>Japan</td><td>1998/10</td><td>300, 000$</td><td>0.4</td><td> $d_1^{0.04}$ ,  $d_2^{0.08}$ </td></tr><tr><td> $f_5$ </td><td>fo2</td><td>Korea</td><td>1998/11</td><td>400, 000$</td><td>0.25</td><td> $d_2^{0.08}$ ,  $d_6^{0.01}$ </td></tr></table>

Each row represents a fact. The R and the Ctxt columns (dimensions) depict the relevance value and the context of the facts, respectively. Eac $d _ { i } ^ { r }$ denotes a document fragment of the collection whose relevance with respect to $\mathcal { Q }$ is r.

## 4.1. Dimensions

A dimension $D$ is a two-tuple $D = ( C _ { D } , \Xi _ { D } )$ , where $C _ { D } { = } \{ C _ { j } \}$ is a set of categories $C _ { j } .$

Example 1. In [16] everything that characterizes a fact is considered to be a dimension, even those attributes modeled as measures in other approaches. Fig. 3 shows the dimensions for the running example.

Each category $C _ { j } { = } \{ e \}$ is a set of dimension values. $\sqsubseteq _ { D }$ is a partial order on $\cup _ { j } C _ { j }$ (the union of all dimension values in the individual categories). Given two values $e _ { 1 } , e _ { 2 } \in \cup _ { j } C _ { j } ,$ then $e _ { 1 } \subseteq _ { D } e _ { 2 }$ if $e _ { 1 }$ is logically contained in $e _ { 2 } .$ The intuition is that each category represents the values of a specific granularity level. We will write $e \in D ,$ meaning that e is a dimension value of $D , \operatorname { i f } e \in \cup _ { j } C _ { j }$

There are two special categories present in all dimensions: ${ \top } _ { D }$ and $\perp _ { D } \in C _ { D }$ (the top and bottom categories). The category $\perp _ { D }$ has the values with the finest granularity. All these values do not logically contain other category values and are logically contained by the values of other coarser categories. The category $\intercal _ { D } = \{ \intercal \}$ represents the coarsest granularity. For all $e \in D , e \subseteq _ { D } { \intercal }$

The partial order $\sqsubseteq _ { D }$ on dimension values is generalized to relate dimension categories as follows: given $C _ { 1 } , C _ { 2 } \in C _ { D }$ , then if $C _ { 1 } \leq _ { D } C _ { 2 } \mathrm { i f } \exists e _ { 1 } \in C _ { 1 } ,$ $e _ { 2 } \in C _ { 2 } , e _ { 1 } \{ \equiv _ { D } e _ { 2 }$ . We will write ⊑ and ≤ instead $\boldsymbol { \mathrm { o f } } \subseteq _ { D }$ and $\le _ { D }$ when it is clear that ⊑ and ≤ represent the partial order of the dimension D.

Example 2. The Customers dimension has the categories $\mathrm { \perp _ { C u s t o m e r s } = C o u n t r y \le R e g i o n \le \mathrm { T _ { C u s t o m e r s } , } }$ with the dimension values Country ={Japan, Korea, Cuba,…} and Region= {Southeast Asia, Central America,…}. The partial order on category values is: Japan ⊑ Southeast Asia⊑ ⊺, Korea ⊑ Southeast Asia, Cuba⊑ Central America ⊑ ⊺, etc.

## 4.1.1. The relevance dimension

The relevance dimension depicts the importance of each fact of the R-cube in the selected context (i.e., the IR condition Q). Therefore, it can be used to identify the portions of an R-cube that are more interesting for the context of analysis.

Different approaches can be followed to state the $r e \mathrm { - }$ levance dimension R. The simplest one is to define it just with the bottom and top categories: $\begin{array} { r } { \bot _ { R } =  { \mathrm { R e l e v a n c e } } \le _ { R } \top _ { R } . } \end{array}$ Since we model the relevance as a probability value, the values of the Relevance category are real numbers in the interval [0,1]. Like in [13], we propose to introduce an intermediate category to study relevance values from a higher qualitative abstraction level. In this new category, the relevance values will be classified into groups (Relevance Degrees) like irrelevant, relevant or very relevant.

As the relevance values are normalized to sum to one, a relevance index of 0.02 may be irrelevant if the rest of relevance values are significantly greater, or relevant if the maximum value of relevance obtained was, for example, 0.03. Thus, we need to define a dynamic partial order $\boldsymbol { \underline { { \underline { { \mathbf { \Pi } } } } } } \gamma$ to map the values $r$ of the base Relevance category to values of the Relevance Degree category depending on the value of ${ \dot { \boldsymbol { r } } } / \gamma .$ . We will use γ as a normalization factor. Note that $\gamma$ should measure the global relevance of a particular result. Typical measures are γ= MAX(r), γ = AVG(r) or γ = Quality.

Definition 2. The relevance dimension is a two-tuple $\scriptstyle R = ( C _ { R } , \subseteq \gamma )$ where: $C _ { R } { = }$ {Relevance, Relevance Degree, ⊺ } is the set of categories; Relevance = [0,1] is the base category $\perp { \boldsymbol { R } } ;$ Relevance Degree∈ ℘([a,b]) is a partition of the interval of Real numbers [a,b]; and $\sqsubseteq _ { R } ^ { \gamma }$ is the partial order $r { \equiv } \gamma _ { r d , }$ , if $r \in \mathrm { R }$ elevance, rd ∈ Relevance Degree and $r / { \gamma } \in r d .$

Example 3. Let us consider $\scriptstyle \gamma = M A X ( r )$ (the maximum value of relevance obtained in the R-cube), and five different degrees of relevance, Relevance Degree = {very irrelevant = [0,0.25), irrelevant = [0.25,0.45), neu-$\operatorname { t r a l } = [ 0 . 4 5 , 0 . 5 5 ) , \operatorname { r e l e v a n t } = [ 0 . 5 5 , 0 . 7 5 )$ , very relevant = $[ 0 . 7 5 , 1 ) \}$ , which define a partition of [0,1]. In the example of Table $1 \ M A X ( r ) = 0 . 4$ , then $0 . 0 5 { \overset { - } { \mathop { = } } } { } { \overset { 0 . 4 } { R } }$ very irrelevant, $0 . 1 \underline { { \subseteq } } _ { R } ^ { 0 . 4 }$ irrelevant, $0 . 2 { \scriptstyle \equiv } _ { R } ^ { 0 . 4 }$ neutral, $0 . 4 \underline { { \underline { { \bf \Pi } } } } _ { R } ^ { 0 . \dot { 4 } }$ very relevant and $0 . 2 5 { \underline { { \underline { { \mathbf { \Pi } } } } } } _ { R } ^ { 0 . 4 }$ relevant.

![](/api/attachments/MNQ4CEQH/fulltext/images/8a8e2d2606559a44728e292599fef4958e743882febe271598dde4be29349080.jpg)  
Fig. 3. Dimensions of the example case of study.

## 4.1.2. The context dimension

The context of each fact is detailed by the documents of the warehouse. We represent these documents in the context dimension.

Definition 3. The context dimension is a two-tuple $C t x t { = } ( C _ { C t x t } , \subseteq _ { C t x t } ) .$ , where $C _ { C t x t } { = } \{ C o l , \top _ { C t x t } \}$ is the set of categories. The category $\perp _ { C t x t } = C o l = \{ d \}$ is the set of the documents d of the warehouse.

Example 4. In our example, $\{ d _ { 1 } ^ { 0 . 0 4 } , d _ { 2 } ^ { 0 . 0 8 } , d _ { 3 } ^ { 0 . 0 0 5 } , d _ { 4 } ^ { 0 . 0 4 } ,$ $d _ { 5 } ^ { 0 . 0 2 } , \stackrel { \bullet } { d } _ { 6 } ^ { 0 . 0 1 } , \ d _ { 7 } ^ { 0 . 0 0 5 } \} \subset \mathrm { C t x t }$ are the documents of the warehouse which describe the context of the facts presented in the R-cube. The superscript denotes the relevance $P ( Q | d )$ of the document $d$ to the context of analysis (the IR condition Q).

The context dimension as defined in Definition 3 is flat, i.e., it has no hierarchies. It would be possible to define a hierarchy for the context dimension by considering the hierarchical structure of the XML documents. However, the IR model of the document warehouse returns the document fragments that maximize the relevance with respect to the selected context. As a consequence, the document warehouse always returns the documents at the optimal granularity level and there is no need to define a hierarchy for the context dimension.

## 4.2. Fact-dimension relations

The fact-dimension relations link facts with dimension values. Following [16], given a set of facts $F { = } \{ f \}$ and a dimension $D ,$ the fact-dimension relation between $F$ and D is the set $F D = \{ ( f , e ) \}$ , where $f { \in } F$ and $e { \in } D$

A fact is characterized by the dimension value $e ,$ written $f \sim \gamma _ { \cal D } e , \mathrm { i f } \equiv e ^ { \prime } \in { \cal D } , ( f , e ^ { \prime } ) \in F { \cal D } \wedge e ^ { \prime } \subseteq _ { \cal D } e .$ In order to avoid missing values it is required that $\forall f \in F , \exists$ $e \in D , \ ( f , e ) \in F D$ . If the dimension value that characterizes a fact is not known, the pair $( f , \intercal )$ is added to FD.

Example 5. In the example of Table 1, we have the facts $F { = } \{ f _ { 1 } , \ f _ { 2 } , \ f _ { 3 } , \ f _ { 4 } , \ f _ { 5 } \} . \ F D _ { C \mathrm { u s t o m e r s } }$ is the factdimension relation that links each fact with its value in the dimension Customers. Thus, $F D _ { \mathrm { { C u s t o m e r s } } } { = }$ $\{ ( f _ { 1 } , \ { \mathrm { C u b a } } )$ , ( f<sub>2</sub>, Japan), $( f _ { 3 } ,$ , Korea), $( f _ { 4 } , \ \mathrm { J a p a n } )$ $( f _ { 5 } , \mathrm { \ K o r e a } ) \}$ , and for $f _ { 3 } , \ f _ { 3 } \mathrm { { \sim } \gamma _ { C u s t o m e r s } }$ Korea and $f _ { 3 } { \mathrm { \sim } } \mathrm {  } _ { \mathrm { C u s t o m e r s } }$ Southeast Asia.

Example 6. The fact-dimension relation $F D _ { \mathrm { A m o u n t } }$ links each fact with is value in the dimension Amount, $F D _ { \mathrm { A m o u n t } } { = } \{ ( f _ { 1 } , ~ 4 , 3 0 0 , 0 0 0 \mathbb { S } ) , ~ ( f _ { 2 } , ~ 3 , 2 0 0 , 0 0 0 \mathbb { S } ) $ $( f _ { 3 } , 9 0 0 , 0 0 0 \ S ) , ( f _ { 4 } , 3 0 0 , 0 0 0 \ S ) , ( f _ { 5 } , 4 0 0 , 0 0 0 \ S ) \}$

## 4.2.1. The relevance fact-dimension relation

The relevance fact-dimension relation links each fact with its relevance value.

Definition 4. The relevance fact-dimension relation is the set $F R = \{ ( f , r ) \}$ where $f { \in } F$ is a fact and $r \in R$ its relevance. We require each fact to have a unique relevance value, $\forall f \in F , \ \exists ! \ r \in R , \ ( f , r ) \in F R$ . The sum of the relevance values of all the facts in F is equal to one, $\scriptstyle \sum ( f , r ) \in F R ^ { r = 1 }$

Let rd ∈ Relevance Degree and γ, we will write $f { \stackrel { } { \sim } } \to \stackrel { \gamma } { R }$ rd, meaning that the relevance degree of the fact f is rd when global relevance measure $\gamma$ is applied, if $\exists r \in R , \ ( f , r ) \in F R$ and $r \subseteq \mathbb { \ Y }$ rd.

Example 7. For the running example we have $F R =$ $\{ ( f _ { 1 } , 0 . 0 5 ) , ( f _ { 2 } , 0 . 1 ) , ( f _ { 3 } , 0 . 2 ) , ( f _ { 4 } , 0 . 4 ) , ( f _ { 5 } , 0 . 2 5 ) \}$ and by taking $\gamma { = } M A X ( r ) { = } 0 . 4 , f _ { 1 } { \sim } { \gamma } _ { R } ^ { 0 . 4 }$ very irrelevant, $f _ { 2 } { \sim } {  } _ { R } ^ { 0 . 4 }$ irrelevant, $f _ { 3 } {  } _ { R } ^ { 0 . 4 }$ neutral, $\dot { f } _ { 4 } { \sim } {  } _ { R } ^ { 0 . \dot { 4 } }$ very relevant and $f _ { 5 } {  } _ { R } ^ { 0 . 4 }$ relevant. That is, $f _ { 5 }$ is relevant, but $f _ { 2 }$ may be irrelevant for the selected context.

## 4.2.2. The context fact-dimension relation.

The context fact-dimension relation links each fact with the documents that describe its context.

Definition 5. We define the context fact-dimension relation as the set $F C t x t { = } \{ ( f , d ) \}$ where $f { \in } F$ is a fact described by the document $d \in C t x t ,$ , also written $f { \sim } {  } _ { C t x t } ~ c$ d. We denote by $R Q$ the set of documents relevant for the analysis that describe the facts in $F , R Q { = } \cup _ { ( f , d ) \in C t x t } \{ d \}$

Example 8. In the example, $F C t x t { = \{ ( f _ { 1 } , ~ d _ { 3 } ^ { 0 . 0 0 5 } ) } .$ $( f _ { 1 } , d _ { 7 } ^ { 0 . 0 0 5 } ) , ( f _ { 2 } , d _ { 5 } ^ { 0 . 0 2 } ) , ( f _ { 3 } , d _ { 4 } ^ { 0 . 0 4 } ) , ( f _ { 4 } , d _ { 1 } ^ { 0 . 0 4 } ) , ( f _ { 1 } , d _ { 2 } ^ { 0 . 0 8 } ) ,$ $( f _ { 5 } , \ d _ { 2 } ^ { 0 . 0 8 } ) , \ ( f _ { 5 } , \ d _ { 6 } ^ { 0 . 0 1 } ) \}$ . Thus, the set of documents relevant for the analysis is $R Q { = } \{ d _ { 1 } ^ { 0 . 0 4 } , ~ d _ { 2 } ^ { 0 . 0 8 } , ~ d _ { 3 } ^ { 0 . 0 0 5 } ,$ $d _ { 4 } ^ { 0 . 0 4 } , d _ { 5 } ^ { 0 . 0 2 } , d _ { 6 } ^ { 0 . 0 1 } , d _ { 7 } ^ { \bar { 0 . } 0 0 5 } \}$ . The documents $\bar { d } _ { 1 } ^ { 0 . 0 4 } , \bar { d } _ { 2 } ^ { 0 . 0 8 }$ depict the context of the fact $f _ { 4 } ,$ , then $f _ { 4 } { \sim } {  } _ { C t x t } d _ { 1 } ^ { 0 . 0 4 }$ and $f _ { 4 } {  } { \mathrm { s u b } }$ Ctxt $d _ { 2 } ^ { 0 . 0 8 }$

## 4.3. R-cubes: relevance-extended multidimensional objects

We extend the definition of multi-dimensional object [16] to include the relevance and context dimensions discussed before.

Definition 6. A relevance-extended multidimensional object (or R-cube) is a four-tuple $\operatorname { R M } = ( F , D , F D , Q )$ where: $F { = } \{ f \}$ is a set of facts; $D { = } \{ D _ { i } , i { = } 1 , . . . , n \}$ $\cup \left\{ R , C t x t \right\}$ is a set of dimensions, $R , C t x t \in D$ are the relevance and context dimensions previously defined; $F D { = } \{ F D _ { i } , i { = } 1 , . . . , n \}$ ∪ (FR,FCtxt) is a set of factdimension relations, one for each dimension $D _ { i } { \in } D ; F R$ $F C t x t \in F D$ are the relevance and context fact-dimension relations defined above; and $\mathcal { Q }$ is an IR condition. In the model, we represent the relevance of each fact with respect to the context established by the IR condition $Q .$

We measure the analysis quality of an R-cube for the selected context by $\scriptstyle { \mathcal { Q } } u a l i t y = \sum _ { d \in R Q } P ( Q | d )$ . That is, the overall relevance to the IR condition Q of the documents that describe the facts of the R-cube.

Example 9. The sales shown in Table 1 constitute the set of facts $F$ of the R-cube. The set of dimensions is $D =$ {Products, Customers, Time, Amount} $\cup \left\{ R , C t x t \right\}$ . In the previous examples we have shown the definition of some of these dimensions along with their corresponding fact-dimension relations. The IR condition used for stating the context of analysis was $Q { = } { ^ { \mathrm { { \sc f i n a n c i a l , c r i s i s } } } } ^ { \mathrm { { * } } }$ The quality of the R-cube is $Q u a l i t y { = } 0 . 2$

## 5. The R-cubes algebra

In this section we present an algebra for the R-cubes by extending the definition of the unary operators presented in [16] to regard the relevance and context of the facts. For each operator, we show its definition, and discuss how the relevance and context are updated in the result by giving some examples.

Along the definitions we will assume an R-cube $R M = ( F , D , F D , Q )$ , where $D = \{ D _ { i } , i = 1 , . . . , n \} \cup \{ R _ { * }$ $C t x t \}$ ${ \mathit { F D } } { = } \{ { \mathit { F D } } _ { i } { , } i { = } 1 , ~ { \ldots } n \} \cup \{ { \mathit { F R } } { , } { \mathit { F C t x t } } \}$ and whose quality is Quality. The set of documents relevant for the analysis query $\mathcal { Q }$ in the R-cube is denoted by $R Q .$

## 5.1. Selection operator

The selection operator restricts the facts in the cube to the subset of facts that satisfy some given conditions.

Definition 7. Let $p \colon \ D _ { 1 } \times . . . \times D _ { n } \times R \times C t x t \longrightarrow$ {true, false} be a predicate on the dimensions in $D .$ The relevance-extended selection operator, ${ \bf { \sigma } } _ { G } ,$ is defined as $\sigma _ { R } [ p ] ( \mathrm { R M } ) { = } ( F ^ { \prime } , D ^ { \prime } , F D ^ { \prime } , Q ^ { \prime } )$ , where:

$$
\begin{array}{l} F ^ {\prime} = \{f \in F | \exists (e _ {1}, \ldots , e _ {n}, r, d) \in D _ {1} \times \ldots \times D _ {n} \\ \qquad \times R \times C t x t (p (e _ {1}, \ldots , e _ {n}, r, d) \wedge f \sim_ {1} e _ {1} \\ \qquad \wedge \ldots \wedge f \sim_ {n} e _ {n} \wedge f \sim_ {R} r \wedge f \sim C t x t d) \}, \\ \qquad D ^ {\prime} = D, \\ \qquad F D ^ {\prime} = \{F D _ {i} ^ {\prime}, i = 1 \ldots n \} \cup \{F R ^ {\prime}, F C t x t ^ {\prime} \} \\ \qquad F D _ {i} ^ {\prime} = \{(f ^ {\prime}, e) \in F D _ {i} | f ^ {\prime} \in F ^ {\prime} \}, \\ \qquad F C t x t ^ {\prime} = \{(f ^ {\prime}, d) \in F C t x t | f ^ {\prime} \in F ^ {\prime} \}, \\ \qquad R Q ^ {\prime} = \{d | \exists (f ^ {\prime}, d) \in F C t x t ^ {\prime} \} \\ \qquad F R ^ {\prime} = \{(f ^ {\prime}, r ^ {\prime}) | \exists (f ^ {\prime}, r) \in F R \wedge f ^ {\prime} \in F ^ {\prime} \wedge r ^ {\prime} \\ \qquad = \beta r + \delta (f ^ {\prime}) \} \\ \qquad \beta = \frac {Q u a l i t y}{Q u a l i t y ^ {\prime}} \geq 1, Q u a l i t y ^ {\prime} = \sum_ {d \in R Q ^ {\prime}} P (Q | d), \\ \delta (f ^ {\prime}) = \sum_ {\{d \in R Q ^ {\prime} | \exists (f, d) \in F C t x t \backslash F C t x t ^ {\prime} \}} (\frac {P (f ^ {\prime} | d)}{Q u a l i t y ^ {\prime}} \\ \qquad - \frac {P (f ^ {\prime} | d)}{Q u a l i t y ^ {\prime}}) P (Q | d) \geq 0, \\ P (f ^ {\prime} | d) ^ {\prime} = \frac {F F (f ^ {\prime} , d)}{\sum_ {(f , d) \in F C t x t ^ {\prime}} F F (f , d)}, \\ P (f ^ {\prime} | d) = \frac {F F (f ^ {\prime} , d)}{\sum_ {(f , d) \in F C t x t} F F (f , d)}, \\ Q ^ {\prime} = Q \end{array}
$$

The set of facts in the resulting R-cube is restricted to those facts characterized by the dimension values where $_ p$ is true. The fact-dimension relations are restricted accordingly. In particular, the documents that do not describe selected facts are removed from the $F C t x t$ fact-dimension relation and from $R Q .$ . In this way, the quality of the R-cube will decrease if a relevant document is discarded. As formally discussed in Theorem 1 of Appendix $\mathbf { A } ,$ the relevance values of the facts after the selection are increased by a factor of $\beta .$ The $\beta$ factor represents the relative increment of importance of the selected documents when other documents of the warehouse are discarded. In addition, if a fact $f ^ { \prime }$ is described in documents which also describe non-selected facts, its relevance is also incremented by $\delta ( f ^ { \prime } )$ . This increment represents the increase of importance of the selected fac $f ^ { \prime }$ in the documents, when the non-selected facts are no longer taken into account. Thus, it is ensured that the sum of the relevance values of the facts in the resulting R-cube remains equal to one.

Example 10. We can apply the relevance-extended selection operator to dice the R-cube to study the sales made to Southeast Asian customers. Since conditions on the relevance dimension are supported, we could also restrict the analysis to those facts considered as relevant or very relevant. Thus, $p { = } ( \mathrm { C u s t o m e r s . R e g i o n { = } S o u t h { - } }$ R.Relevance Degree= very relevant or relevant). Table 2 shows the resulting R-cube. The set of facts is restricted to $F ^ { \prime } { = } \{ f _ { 4 } , f _ { 5 } \}$ . The resulting fact-dimension relations are: $F = \{ ( f _ { 4 } , f o 1 ) , ( f _ { 5 } , f o 2 ) \} , F = \{ ( f _ { 4 } , J a p a n ) , ( f _ { 5 } , K o r -$ $e a ) \} , \ F = \{ ( f _ { 4 } , \ 1 9 9 8 / 1 0 ) , \ ( f _ { 5 } , \ 1 9 9 8 / 1 1 ) \} , \ F D _ { \mathrm { A m o u n t } ^ { \prime } } =$ $\{ ( f _ { 4 } , 3 0 0 , 0 0 0 \mathbb { S } ) , ( f _ { 5 } , 4 0 0 , 0 0 0 \mathbb { S } ) \}$ . The stated restriction also affects the set of documents that describe the facts of the R-cube, $F C t x t ^ { \prime } = \{ ( f _ { 4 } , ~ d _ { 1 } ^ { 0 . 0 4 } ) , ~ ( f _ { 4 } , ~ d _ { 2 } ^ { 0 . 0 8 } ) , ~ ( f _ { 5 } ,$ $d _ { 2 } ^ { 0 . 0 8 } ) , ( f _ { 5 } , d _ { 6 } ^ { 0 . 0 1 } ) \}$ , and then $R Q ^ { \prime } { = } \{ d _ { 1 } ^ { 0 . 0 4 } , ~ d _ { 2 } ^ { 0 . 0 8 } ,$ $d _ { 6 } ^ { 0 . 0 1 } \} \subset R Q .$ Since some documents relevant for the analysis context are discarded, the quality of the resulting R-cube decreases to $Q u a l i t y ^ { \prime } { = } 0 . 1 3 ~ ( { < } Q u a l { - }$ $i t y { = } 0 . 2 )$ . Notice that all the facts related to $d _ { 1 } , d _ { 2 }$ and $d _ { 6 }$ in FCtxt were selected by the operation. That is, in this case, all the documents in the resulting R-cube only describe selected facts. Consequently, the relevance of the facts is increased in a $\beta$ factor, $\beta { = } Q u a l i t y / Q u a l i t y ^ { \prime } { = }$ 1.54. The resulting relevance fact-dimension relation is $F R ^ { \prime } { = } \{ ( f _ { 4 } , 0 . 6 1 5 ) , ( f _ { 5 } , 0 . 3 8 5 ) \}$

Example 11. Let us now consider the result of the previous example. If we select the sales made during the month of November 1998 $( { \mathrm { i . e . , } } p { = } ( \mathrm { T i m e . M o n t h { = } } 1 9 9 8 /$ 11)) from the R-cube shown in Table 2, the new set of facts is $F ^ { \prime } { = } \{ f _ { 5 } \}$ , and the context fact-dimension relation becomes $F C t x t ^ { \prime } = \{ ( f _ { 5 } , \mathrm { d } _ { 2 } ^ { 0 . 0 8 } ) , ( f _ { 5 } , \mathrm { d } _ { 6 } ^ { 0 . 0 1 } ) \}$ , resulting $R Q ^ { \prime } =$ $\{ \mathbf { d } _ { 2 } ^ { 0 . 0 8 } , \ \mathbf { d } _ { 6 } ^ { 0 . 0 1 } \}$ and $Q u a l i t y ^ { \prime } { = } 0 . 0 9$ , then $\beta { = } 0 . 1 3 /$ $0 . 0 9 { = } 1 . 4 4 4$ . Document $d _ { 6 }$ only describes $f _ { 5 } ,$ , the selected fact. However, document $d _ { 2 }$ describes both the selected fact, $f _ { 5 } ,$ and the discarded one, $f _ { 4 } ,$ , since in the input Rcube we had that $\{ ( f _ { 4 } , d _ { 2 } ^ { 0 . 0 8 } ) , \bar { ( f _ { 5 } , d _ { 2 } ^ { 0 . 0 8 } ) } \} \subset F C t \bar { \times } t$ . The relevance of $f _ { 5 }$ in the input R-cube was 0.385, $( f _ { 5 } ,$ $0 . 3 8 5 ) \in F R$ . Then, in the resulting R-cube, the relevance of f will be recalculated as $\beta 0 . 3 8 5 \substack { + \delta ( f _ { 5 } ) }$ . Let $F F ( f _ { 4 } , \ d _ { 2 } ) = F F ( f _ { 5 } , \ d _ { 2 } ) = 3$ , the dimension values of the fact $f _ { 4 }$ appear three times in document $d _ { 2 } ,$ , likewise, the frequency of the dimensions values of the fact $f _ { 5 }$ in $d _ { 2 }$ is three. Thus, we have that $P ( f _ { 5 } | d _ { 2 } ) = 3 / ( 3 + 3 ) = 0 . 5$ and $P ( f _ { 5 } | d _ { 2 } ) ^ { \prime } = 3 / 3 = 1$ . The relevance of document $d _ { 2 }$ to the IR condition is $P ( Q | d _ { 2 } ) { = } 0 . 0 8$ . Then, $\delta ( f _ { 5 } ) { = } ( P ( f _ { 5 } |$ $d _ { 2 } ) ^ { \prime } - P ( f _ { 5 } | d _ { 2 } ) ) P ( Q | d _ { 2 } ) / \mathrm { Q u a l i t y ^ { \prime } } = 0 . 4 4 4$ . In this way, we finally have that $\beta 0 . 3 8 5 + \delta ( f _ { 5 } ) { = } 1$ , and the resulting relevance fact-dimension relation is $F R ^ { \prime } { = } \left\{ \left( f _ { 5 } , 1 \right) \right\}$

The $\beta$ factor measures the quality lost in the resulting R-cube. Good restrictions will result in low $\beta$ values, since they preserve the relevant facts of the R-cube and discard the non-relevant ones. However, sometimes, we may be interested in a particular region of the cube. A high $\beta$ value (a low Quality′) will warn the user of a meaningless result.

Example 12. When the selection operator is applied to the example R-cube of Table 1, with the predicate $p =$ (Customers.Region = Central America), the set of facts in the resulting R-cube is restricted to $F ^ { \prime } { = } \{ f _ { 1 } \}$ , the context fact-dimension relation becomes $F C t x t ^ { \prime } { = } \{ (  f _ { 1 }$ 2 $d _ { 3 } ^ { 0 . 0 0 5 } ) , ( f _ { 1 } , d _ { 7 } ^ { 0 . 0 0 5 } ) \}$ and $R Q ^ { \prime } = \{ d _ { 3 } ^ { 0 . 0 0 5 } , ~ d _ { 7 } ^ { 0 . 0 0 5 } \}$ . Consequently, the quality is reduced to $Q u a l i t y ^ { \prime } { = } 0 . 0 1$ , resulting $\beta { = } 0 . 2 / 0 . 0 1 { = } 2 0$ . The high $\beta$ value points to a considerable lost quality, meaning that the analysis result is not significant in the selected context (as the financial crisis mainly affected the Southeast Asian countries).

## 5.2. Aggregate formation operator

The aggregate formation operator evaluates an aggregation function on the R-cube. Following [16], we assume the existence of a family of functions $g \colon 2 ^ { F } \to D _ { n + 1 }$ that receive a set of facts and compute an aggregation by taking the data from the requested factdimension relation $( \mathrm { e . g . , S U M } _ { i }$ takes the data from $F D _ { i } ,$ and performs the sum).

The Group operator defined in [16] groups the facts characterized by the same dimension values. Given the dimension values. Given the dimension values $( e _ { 1 } ,$ $. . . , e _ { n } ) { \in } D _ { 1 } \times . . . . \times D _ { n } , G r o u p ( e _ { 1 } , . . . , e _ { n } ) = \{ f \in F | f \sim \gamma _ { 1 } e _ { 1 } \} $ $\land . . . \land f \sim \Rightarrow _ { n } e _ { n } \}$

Example 13. In the example R-cube of Table 1, we can group those sales made to Southeast Asian customers during the second half of 1998 as follows: given the dimension values (⊺, Southeast Asia, 1998/2nd half, $\mathrm { 7 ) } \in \mathrm { \sf { I } } _ { \mathrm { { P r o d u c t s } } } \times \mathrm { { R e g i o n } } \times \mathrm { { H a l f \_ y e a r } \times \mathrm { { 7 } } _ { \mathrm { { A m o u n t } } } , }$ Group (⊺, Southeast Asia, 1998/2nd half, $\intercal ) = \{ f _ { 4 } , f _ { 5 } \}$

Quality′ = 1.54.

Result of applying $\sigma _ { R }$ on the example R-cube of Table 1, p = (Customers.Region = Southeast Asia, R.Relevance Degree = very relevant or relevant)

<table><tr><td> $F'$ </td><td>Products.ProductId</td><td>Customers.Country</td><td>Time.Month</td><td>Amount</td><td>R</td><td>Ctxt</td></tr><tr><td> $f_4$ </td><td>fo1</td><td>Japan</td><td>1998/10</td><td>300,000$</td><td>0.615</td><td> $d_1^{0.04}$ ,  $d_2^{0.08}$ </td></tr><tr><td> $f_5$ </td><td>fo2</td><td>Korea</td><td>1998/11</td><td>400,000$</td><td>0.385</td><td> $d_2^{0.08}$ ,  $d_6^{0.01}$ </td></tr></table>

Definition 8. Given a new dimension $D _ { n + I } ,$ an aggregation function $g \colon 2 ^ { F } {  } D _ { n + I } ,$ , and a set of grouping categories $\{ C _ { i } { \in } C _ { D _ { i } } , i { = } 1 { \ldots } n , C _ { D _ { i } } { \neq } C _ { R } , C _ { C t x t } \}$ , the relevance-extended aggregate formation operator, $\alpha _ { R } ,$ is defined as $\alpha _ { R } [ D _ { n + 1 } , g , C _ { 1 } , . . . , C _ { n } ] ( \mathrm { R M } ) { = } ( F ^ { \prime } , D ^ { \prime } , F D ^ { \prime }$ Q′), where:

$$
\begin{array}{l} F ^ {\prime} = \{G r o u p (e _ {1}, \ldots , e _ {n}) | (e _ {1}, \ldots , e _ {n}) \in C _ {1} \times \ldots \\ \qquad \qquad \times C _ {n} \wedge G r o u p (e _ {1}, \ldots , e _ {n}) \neq \phi \}, \\ D ^ {\prime} = \{D _ {i} ^ {\prime}, i = 1 \ldots n \} \cup \{D _ {n + 1} \} \cup \{R, C t x t \}, \\ D _ {i} ^ {\prime} = (C _ {D _ {i}} ^ {\prime}, \sqsubseteq_ {D _ {i}} ^ {\prime}), \\ C _ {D _ {i}} ^ {\prime} = \{C _ {i j} \in C _ {D _ {i}} | C _ {i} \leq_ {D i} C _ {i j} \}, \sqsubseteq_ {D _ {i}} ^ {\prime} = \sqsubseteq_ {D _ {i | C ^ {\prime} D _ {i}}} ^ {\prime}, \\ F D ^ {\prime} = \{F D _ {i} ^ {\prime}, i = 1 \ldots n \} \cup \{F D _ {n + 1} \} \\ \qquad \cup \{F R ^ {\prime}, F C t x t ^ {\prime} \}, \\ F D _ {i} ^ {\prime} = \{(f ^ {\prime}, e _ {i} ^ {\prime}) | \exists (e _ {1}, \ldots , e _ {n}) \in C _ {1} \times \ldots \times C _ {n}, \\ f ^ {\prime} = G r o u p (e _ {1}, \ldots , e _ {n}) \in F ^ {\prime} \wedge e _ {i} = e _ {i} ^ {\prime} \}, \\ F D _ {n + 1} = \bigcup_ {(e _ {1}, \ldots , e _ {n}) \in C _ {1} \times \ldots \times C _ {n}} \{(G r o u p (e _ {1}, \ldots , e _ {n}), \\ g (G r o u p (e _ {1}, \ldots , e _ {n})) | G r o u p (e _ {1}, \ldots , e _ {n}) \neq \phi \} \\ F R ^ {\prime} = \{(f ^ {\prime}, r ^ {\prime}) | \exists (e _ {1}, \ldots , e _ {n}) \in C _ {1} \times \ldots \times C _ {n} \\ \qquad \wedge f ^ {\prime} = G r o u p (e _ {1}, \ldots , e _ {n}) \in F ^ {\prime} \\ \qquad \wedge r ^ {\prime} = \sum_ {(f, r) \in F R, f \in G r o u p (e _ {1}, \ldots , e _ {n})} r \}, \\ F C t x t ^ {\prime} = \{(f ^ {\prime}, d ^ {\prime}) | \exists (e _ {1}, \ldots , e _ {n}) \in C _ {1} \times \ldots \times C _ {n} \\ \qquad \wedge f ^ {\prime} = G r o u p (e _ {1}, \ldots , e _ {n}) \in F ^ {\prime} \\ \qquad \wedge d ^ {\prime} \in \bigcup_ {(f, d) \in F C t x t, f \in G r o u p (e _ {1}, \ldots , e _ {n})} \{d \} \}, \\ R Q ^ {\prime} = R Q, Q u a l i t y = Q u a l i t y ^ {\prime}, \\ Q ^ {\prime} = Q \end{array}
$$

Each fact in the resulting R-cube represents a group of facts of the original R-cube (those characterized by the same values in the grouping category). The aggregation function is evaluated over each group of facts and the result is stored in the new dimension $D _ { n + I } .$ The dimensions $D _ { i } , \ldots D _ { n }$ are restricted to the ancestor categories of the corresponding grouping category. The FCtxt fact-dimension relation now relates each new fact with the documents that were associated with any of the original facts of the corresponding group. Notice that the set of documents relevant to the analysis query RQ does not change. Likewise, the quality of the R-cube is not modified. As discussed in Section 3, we estimate the relevance of the facts by the frequency of their dimension values in the relevant documents. Consequently, the relevance of each group is the sum of the relevance values of the original facts in the group (see Theorem 2 in Appendix A). We update the FR factdimension relation accordingly. Thus, the sum of the relevance values of the facts in the resulting R-cube remains equal to one.

Example 14. In the example R-cube of Table 1, we can compute the total amount of sales per Region and Half\_year by applying the aggregate formation operator as follows:

Let $\mathrm { T o t a l } { = } ( C _ { \mathrm { T o t a l } } , \subseteq _ { \mathrm { T o t a l } } )$ be a new dimension to store the result of the sum, with the categories $C _ { \mathrm { T o t a l } } { = } \{ \mathrm { T o t a l } $ Amount, $\intercal _ { \mathrm { { T o t a l } } } \} , \perp _ { \mathrm { { T o t a l } } } = \mathrm { { T o t a l } }$ $\mathrm { A m o u n t } \leq \mathsf { T } _ { \mathrm { T o t a l } } .$ . Let $\mathbf { S U M _ { A m o u n t } }$ be the aggregation function that performs the sum of the values of the Amount dimension. Since we want to evaluate the sum per Region and Half\_year, the grouping categories are $\{ \mathsf { T } _ { \mathrm { P r o d u c t s } } ,$ Region, Half\_year, $\tau _ { \mathrm { A m o u n t } } \}$ . Table 3 shows the result of applying the aggregate formation operator $\alpha _ { R }$ [Total, $\mathbf { S U M _ { A m o u n t } } ,$ ⊺<sub>Products</sub>, Region, Half\_year, $\mathsf { T } _ { \mathrm { A m o u n t } } ]$ to the R-cube of Table 1.

In the resulting R-cube, there is a new fact for each combination $( e _ { 1 } , . . . , e _ { 2 } )$ of dimension values in the given grouping categories, $( e _ { 1 } , . . . , ~ e _ { 2 } ) { \in } \mathsf { T } _ { \mathrm { P r o d u c t s } } \times \mathrm { R e g i o n } \times$ Half\_year × $\mathsf { T } _ { \mathrm { A m o u n t } } .$ In the example, the possible combinations are (⊺, Central America, 1998/1st half, ⊺), (⊺, Southeast Asia, 1998/1st half, ⊺) and (⊺, Southeast Asia, 1998/2nd half, ⊺). Each new fact represents the group of original facts characterized by the corresponding combination of grouping category values. Thus, in the resulting R-cube, we have the facts $\{ f _ { 1 } \} = G r o u p ( \intercal$ , Central America, 1998/1st half, ⊺), $\{ f _ { 2 } ,$ $f _ { 3 } \} { = } G r o u p ( \mathbb { T } ,$ , Southeast Asia, 1998/1st half, ⊺) and { f , $f _ { 5 } \} { = } G r o u p ( \mathrm { 7 } ,$ , Southeast Asia, 1998/2nd half, ⊺), obtaining $F ^ { \prime } { = } \{ \{ f _ { 1 } \} , \{ f _ { 2 } , f _ { 3 } \} , \{ f _ { 4 } , f _ { 5 } \} \}$

The resulting R-cube has seven dimensions. The Ctxt and R dimensions are not modified. The dimension Products′ and Amount′ have been restricted to their top categories, ${ \bar { \Gamma } } _ { \mathrm { P r o d u c t s } }$ and $\mathsf { T } _ { \mathrm { A m o u n t } } ,$ respectively. The dimension Customers′ is reduced, so that only the categories $\mathrm { R e g i o n { \leq } \bar { \ l } _ { C u s t o m e r s } }$ are kept. The Time′ dimension is also reduced to the categories Half\_year ≤ $\mathrm { Y e a r } \le \mathsf { T } _ { \mathrm { T i m e } } .$ . The new dimension Total stores the result of the aggregation.

Result of applying α [Total, SUM , ⊺ , Region, Half\_year, ⊺ ] on the example R-cube of Table 1

<table><tr><td> $F'$ </td><td> $\mathsf{T}_{\text {Products}}$ </td><td>Customers&#x27;.Region</td><td>Time&#x27;.Half_year</td><td> $\mathsf{T}_{\text {Amount}}$ </td><td>Total</td><td>R</td><td>Ctxt</td></tr><tr><td> $\{f_1\}$ </td><td>T</td><td>Central America</td><td>1998/1st half</td><td>T</td><td>4,300,000$</td><td>0.05</td><td> $d_3^{0.005},d_7^{0.005}$ </td></tr><tr><td> $\{f_2,f_3\}$ </td><td>T</td><td>Southeast Asia</td><td>1998/1st half</td><td>T</td><td>4,100,000$</td><td>0.3</td><td> $d_5^{0.02},d_4^{0.04}$ </td></tr><tr><td> $\{f_4,f_5\}$ </td><td>T</td><td>Southeast Asia</td><td>1998/2nd half</td><td>T</td><td>700,000$</td><td>0.65</td><td> $d_1^{0.04},d_2^{0.08},d_6^{0.01}$ </td></tr></table>

The fact dimension-relations $F D _ { \mathrm { { P r o d u c t s ^ { \prime } } } } , F D _ { \mathrm { { C u s t o m e r s ^ { \prime } } } } ,$ $F D _ { \mathrm { T i m e ^ { \prime } } }$ and $F D _ { \mathrm { A m o u n t ^ { \prime } } }$ , now link each new fact with the dimension values that characterize the corresponding group of original facts. For example, for the new fact $\{ f _ { 4 } ,$ $f _ { 5 } \}$ , we have that $( \{ f _ { 4 } , f _ { 5 } \} , \ 7 ) { \in } F D _ { \mathrm { P r o d u c t s } ^ { \prime } } , \ ( \{ f _ { 4 } , f _ { 5 } \}$ Southeast $\mathrm { A s i a } ) { \in } F D _ { \mathrm { C u s t o m e r s ^ { \prime } } } , ~ ( \{ f _ { 4 } , ~ f _ { 5 } \}$ , 1998/2nd hal $\mathrm { f } ) \in F D _ { \mathrm { T i m e ^ { \prime } } }$ and $( \{ f _ { 4 } , \ f _ { 5 } \} , \ 7 ) \in F D _ { \mathrm { A m o u n t ^ { \prime } } }$ . The $F C t x t ^ { \prime }$ fact dimension-relation links each new fact with the documents that were related with the original facts of the corresponding group. For example, in the original Rcube we had $\{ ( \stackrel {  } { f _ { 4 } } , \stackrel {  } { d _ { 1 } ^ { 0 . 0 4 } } ) , ( f _ { 4 } , \stackrel {  } { d _ { 2 } ^ { 0 . 0 8 } } ) , ( f _ { 5 } , \stackrel {  } { d _ { 2 } ^ { 0 . 0 8 } } ) .$ , ( f<sub>5</sub>, $d _ { 6 } ^ { 0 . 0 1 } ) \} \subset F C t x t .$ , then, in the resulting R-cube we have $\{ ( \{ f _ { 4 } , ~ f _ { 5 } \} , ~ d _ { 1 } ^ { 0 . 0 4 } ) , ~ ( \{ f _ { 4 } , ~ f _ { 5 } \} , ~ d _ { 2 } ^ { 0 . 0 8 } ) , ~ ( \{ f _ { 4 } , ~ f _ { 5 } \} , ~ d _ { 6 } ^ { 0 . 0 1 } ) \}$ $\subset F C t x t ^ { \prime }$ . Thus, the aggregate formation operation never modifies the set of documents relevant for the analysis, $\mathrm { i . e . , } R Q ^ { \prime } { = } R Q$ . Then, the quality of the R-cube remains, $\mathrm { i . e . , } Q u a l i t y ^ { \prime } \mathrm { = } Q u a l i t y \mathrm { = } 0 . 2$ . The relevance of the new facts is the sum of the relevance values of the original facts in the corresponding group. In the example, we have that $( \{ f _ { 4 } , \ f _ { 5 } \} , \ 0 . 6 5 ) \in F R ^ { \prime }$ , since $\{ ( f _ { 4 } , 0 . 4 )$ $( f _ { 5 } , 0 . 2 5 ) \} \subset F R$ . Finally, the new $F D _ { \mathrm { T o t a l } }$ fact-dimension relation links each new fact with the result of applying the aggregation function $\mathbf { S U M _ { A m o u n t } }$ to the corresponding group of facts. Since $\{ ( f _ { 4 } , 3 0 0 , 0 0 0 \mathbb { S } ) , ( f _ { 5 } , 4 0 0 , 0 0 0$ $\ S ) \} { \subset } F D _ { \mathrm { A m o u n t } } ,$ then $( \{ f _ { 4 } , f _ { 5 } \} , 7 0 0 , 0 0 0 \$ ) 6 F D _ { \mathrm { \tiny ~ T o t a l } } .$

The resulting R-cube clearly shows that the most relevant fact is $\{ f _ { 4 } , f _ { 5 } \}$ . That is, the financial crisis had the strongest impact in the Southeast Asian region during the second half of the year, which would explain the corresponding sales fall. We could gain insight into the context of this fact by performing a drill-through operation [24], thus retrieving the textual contents of the documents that explain the details of the crisis.

## 5.3. Projection operator

The projection operator removes some of the cube dimensions. Next, we give the formal definition of the relevance-extended projection operator. It is basically the projection operator defined in [16], but restricted to avoid the removal of the relevance and the context dimensions. In this way, we can conclude that since the result of the three operations over R-cubes is always an R-cube, the R-cubes algebra presented here is closed.

Definition 9. Given the dimensions $D _ { 1 } , . . . , D _ { k } { \in } D \backslash$ {R, Ctxt}, the relevance-extended projection operator, $\pi _ { R } ,$ is defined as $\pi _ { R } [ D _ { 1 } , . . . , D _ { k } ] ( { \mathrm { R M } } ) = ( F ^ { \prime } , D ^ { \prime } , F D ^ { \prime }$ Q′): F = F′, $D ^ { \prime } { = } \{ D _ { 1 } { , } . . . , ~ D _ { k } \} \cup \{ R  ,$ Ctxt}, $F D ^ { \prime } =$ $\{ F D _ { 1 } , . . . , F D _ { k } \} \cup \{ F R , F C t x t \}$ , and $Q ^ { \prime } { = } Q . \ R Q ^ { \prime } { = } R Q$ and $Q u a l i t y ^ { \prime } { = } Q u a l i t y$

Example 15. By following with the Example 14, we can apply the relevance extended-projection operator to remove the Products and Amount dimensions. The result is equivalent to the one that would be obtained with the traditional roll-up operation.

Thus, by applying π [Customers, Time, Total] on the R-cube of Table 3, we obtain a new R-cube with the same set of facts, the dimensions, Customers, Time, Total, R and Ctxt as returned by the aggregation operator, along with their corresponding fact-dimension relations. Since the FCtxt fact-dimension relation is not modified, $R Q ^ { \prime } { = } R Q$ and the quality of the resulting Rcube remains, i.e., $Q u a l i t y ^ { \prime } { = } Q u a l i t y { = } 0 . 2$

The drill-down operation is equivalent to evaluating an aggregate formation on lower categories [16]. Since more detailed data is required, a reference to the original R-cube is needed.

Finally, note that an R-cube is an special multidimensional object [16]. Thus, an R-cube can also be queried by using the algebra proposed in the base model. In this case, the result may no longer be an R-cube, as the relevance or the context dimension may be projected away, or the fact relevance may not be updated. However, these operators could be applied to perform interesting analysis. For example, the context dimension may be used as a grouping category to calculate aggregations over the facts described in each document.

## 6. The prototype

In order to validate the usefulness of our approach, we have developed a prototype. The resulting contextualized warehouse allows users to analyze stock market indexes with the advantage of having each measure value associated to a news extract that explains it. This section gives an overview of the main aspects involved in the design of the system. First, we describe the document and corporate warehouses of the prototype. Afterwards, we show the usefulness of the prototype by means of an example usage case, and explain the analysis process by means of a sequence of screen-shots. Finally, we summarise some implementation issues.

The document warehouse consists of a digital collection of some well-known international business newspapers. We inserted in the prototype a total of 132 articles from the issues published during 1990. Among other things, these articles report the trends of markets during that period. It is usual to find news explaining how stock markets are affected by some financial circumstances, e.g.: “The reaction of German market to the rise of interest rates is expected to be …”.

The corporate warehouse keeps a historical record of market indexes as measured by Morgan Stanley Capital International Perspective [14]. In our experiments we have only considered the indexes of the year 1990, resulting, at the lowest dimension categories, in 1396 facts. As Fig. 4 shows, the corporate cube has two dimensions. The Market dimension is organized into two categories: Market (U.S., Japan, etc.) and Region (North America, Asia, etc.). The Date dimension is organized into Day, Month, Quarter and Year. The fact (Japan, 1990/05, 1332.24) depicts that the average index in the Japanese market during May 1990 was 1332.24.

Like in traditional data warehouses, an OLAP interface allows analysts to query the corporate warehouse. Among other things, it is possible to study the average index of the different markets, pivot to order by date, roll-up to calculate the average per region, or dice the cube to select the index values of the second quarter of 1990 in Germany (see Fig. 4).

Let us suppose that there are recent news about a conflict happening in the Middle East. During the last decades conflicts have been frequent in this area, so the analyst decides to use the prototype to study the reaction of the stock markets to the Iraq war of 1990. After entering the keyword “Iraq” in the toolbar and clicking on “Search Context”, the system presents to the user a list of documents about Iraq ranked by relevance (see the left side of

Fig. 5). By selecting a document, its contents appear in the right part of the window, and the paragraph that contains the keyword is highlighted. Then, the analyst can refine the query by adding or removing keywords, and by specifying a minimum relevance threshold. It is also possible to provide some user feedback by clicking on the check boxes associated to the documents that better describe the Iraq conflict of 1990. Once the set of documents that describe the context under analysis has been obtained, the “Contextualize” button is used to continue the analysis in the OLAP window shown in Fig. 6.

Now this window presents an R-cube that includes the relevance and the context values assigned to each fact of the original cube. Dark colours depict very relevant facts, whereas light colours mark the irrelevant ones. By rolling up to the Region and Quarter levels and ordering the facts by relevance, the analyst discovers that the most relevant facts involve the Asian markets and the third quarter of 1990. Then, the analyst decides to execute a drill-down operation to study the average index per month in the Asian countries. The most relevant facts correspond to Japan and the months of August and September. As can be seen in Fig. 6, the Japanese market index had a sharp fall during these months, a fall of 100 points, whereas the average falls in the rest of markets were of about 10 points. By selecting the fact that represents the average index of the Japanese market in August, the system presents the documents that describe the context of this fact (see the right side of the window shown in Fig. 6). In the highlighted paragraph of the first document, the analyst discovers that “… plant engineering companies fell as their projects in Iraq and Kuwait were frozen because of the economic sanction of Japan against Iraq”. Thus, the analyst concludes that it could be a good idea to watch

![](/api/attachments/MNQ4CEQH/fulltext/images/bb5db5cb2c77f68c980c6652679de630e14a3b0109122a17e84ca170d9b390d9.jpg)  
Fig. 4. OLAP window.

![](/api/attachments/MNQ4CEQH/fulltext/images/bd56beba93a97ee788ae6561d6d7c28e5e2dae9a3622d955e1dc080a9981a274.jpg)  
Fig. 5. IR window.

Japanese investments now that there is a new conflict in the Middle East which could be as important for the financial markets as the Iraq war of 1990.

The prototype has been implemented as a set of Python modules. In order to evaluate keyword-based searches over the XML collection, the document warehouse keeps a inverted file index [2] and implements the Relevance Modelling logic of the IR model presented in Section 3.1. Stemming and proper noun recognition tasks are executed by the Tree Tagger tool [23]. The corporate cubes and OLAP operations have been supported by implementing the data model and algebra operators of the base multidimensional model [16]. The Fact Extractor module provides the methods to build the R-cube by looking for date, stock market, and region references in the paragraphs of the documents. Finally, analysis capabilities over R-cubes have been provided by implementing the data model and algebra operators discussed in this paper.

![](/api/attachments/MNQ4CEQH/fulltext/images/43e1b4621e376d0ba735966db55badf58d4c43f63c5957d6ca741c8cd31725c5.jpg)  
Fig. 6. OLAP window showing an R-cube.

## 7. Conclusions and future work

A contextualized warehouse is a new decision support system that allows users to combine all their sources of structured data and unstructured documents, and to obtain strategic information by analyzing the integrated data under different contexts. In a contextualized warehouse, the user specifies an analysis context by supplying some keywords. Then, the analysis is performed on an R-cube which is materialized by retrieving the documents and facts related to the selected context.

R-cubes are characterized by two special dimensions, namely the relevance and context dimensions. The relevance is a numeric value that measures the importance of each fact in the context of analysis. The context dimension relates each fact with the documents that explain its circumstances. In order to formalize the definition of R-cubes, we have extended a multidimensional data model [16] and studied how the relevance and context dimensions should be addressed by the unary algebra operators. This algebra remains to be completed with binary operators. For this purpose, data fusion mechanisms [6] can be applied to combine the relevance of the involved facts.

In this paper, the usefulness of contextualized data warehouses has been shown by means of a prototype. Testing the performance of the system with larger data sets, and studying query evaluation techniques for Rcubes, like pre-aggregation strategies, will be future work.

In this work we have shown how the dimension values found in documents can be applied in the process of relating them with the corporate facts that have the same dimension values. Trying to analyze the facts extracted from the documents without considering the corresponding corporate facts is an even more challenging task. In this case, the analysis may involve facts that are incomplete (not all the dimensions may be quoted in the documents contents) and/or imprecise (if the dimension values found belong to non-base granularity levels). The R-cubes base model supports incompleteness and imprecision [16]. For the future, we plan to exploit these features to analyze the facts described in the documents that are not available in the corporate warehouse.

## Acknowledgements

This project has been partially supported by the Danish Research Council for Technology and Production under grant no. 26-02-0277, the Spanish National Research Project TIN2005-09098-C05-04, and the Fundación Bancaixa Castelló.

## Appendix A. Theorems and proofs

Theorem 1. Let $R M = ( F , D , F D ,$ Q) be an R-cube and $R M ^ { \prime } = ( F ^ { \prime } , ~ D ^ { \prime }$ , FD′, Q′) the R-cube obtained after applying the selection operation $\sigma _ { R } / p ]$ over RM, $\sigma _ { R } / p ]$ $( R M ) = R M ^ { \prime }$ . The relevance of the facts $f ^ { \prime } \in F ^ { \prime }$ can be calculated as $P ( f ^ { \prime } | R \mathcal { Q } ^ { \prime } ) = \beta P ( f ^ { \prime } | R \mathcal { Q } ) + \delta ( f ^ { \prime } )$ , where:

$$
\begin{array}{c} \beta = \frac {\text {Quality}}{\text {Quality} ^ {\prime}} \geq 1, \\ \delta (f ^ {\prime}) = \sum_ {\{d \in R Q ^ {\prime} | \exists (f, d) \in F C t x t \backslash F C t x t ^ {\prime} \}} \quad (\frac {P (f ^ {\prime} | d) ^ {\prime}}{\text {Quality} ^ {\prime}} \\ - \frac {P (f ^ {\prime} | d)}{\text {Quality} ^ {\prime}}) P (Q | d) \geq 0 \\ P (f ^ {\prime} | d) ^ {\prime} = \frac {F F (f ^ {\prime} , d)}{\sum_ {(f , d) \in F C t x t ^ {\prime}} F F (f , d)}, \\ P (f ^ {\prime} | d) = \frac {F F (f ^ {\prime} , d)}{\sum_ {(f , d) \in F C t x t} F F (f , d)} \end{array}
$$

Proof. Let $f ^ { \prime } \in F ^ { \prime }$ , as discussed in Section 3.3, we estimate its relevance $P ( f ^ { \prime } | R Q ^ { \prime } )$ by:

$$
P (f ^ {\prime} | R Q ^ {\prime}) = \frac {\sum_ {d \in R Q ^ {\prime}} P (f ^ {\prime} | d) ^ {\prime} P (Q | d)}{\sum_ {d \in R Q ^ {\prime}} P (Q | d)}
$$

Notice that the probability $P ( f ^ { \prime } | d ) ^ { \prime }$ of observing the fact $f ^ { \prime }$ in a document d when considering the restricted set of facts $F ^ { \prime } ,$ , is different from the probability $P ( f ^ { \prime } | d )$

of observing the fact $f ^ { \prime }$ in d when considering the superset $F .$

Since the documents $d \in R O ^ { \vert { R O ^ { \prime } } }$ do not describe any fact of $F ^ { \prime }$ , the probability of observing a fact $f ^ { \prime } \in F ^ { \prime }$ in a document is $d \in R O ^ { | } R O ^ { \prime }$ is $P ( f ^ { \prime } | d ) ^ { \prime } { = } 0$ . Thus, we can write:

$$
P (f ^ {\prime} | R Q ^ {\prime}) = \frac {\sum_ {d \in R Q} P (f ^ {\prime} | d) ^ {\prime} P (Q | d)}{\sum_ {d \in R Q ^ {\prime}} P (Q | d)}
$$

Let $R Q _ { 1 }$ be the subset of documents that only describe facts in $F ^ { \prime }$ $R Q _ { 1 } = \{ d \in R Q | \exists ( f , ~ d ) \in F C t x t$ $\backslash F C t x t ^ { \prime } \}$ ; and $R Q _ { 2 }$ the subset of document that at least describe a fact that was in $F$ but not in $F ^ { \prime } , R Q _ { 2 } =$ $\{ d \in R Q | \exists ( f , d ) \in F C t x t \backslash F C t x t ^ { \prime } \}$ . The subsets $R Q _ { 1 }$ and $R Q _ { 2 }$ as defined above constitute a partition of $R Q .$ , i.e. $R Q _ { 1 } \cap R Q _ { 2 } { = } \emptyset$ and $R Q _ { 1 } \cup R Q _ { 2 } { = } R Q$ , then:

$$
\begin{array}{l} P (f ^ {\prime} | R Q ^ {\prime}) = \frac { \sum_ {d \in R Q _ {1}} P (f ^ {\prime} | d) ^ {\prime} P (Q | d)}{ \sum_ {d \in R Q ^ {\prime}} P (Q | d)} \\ + \frac { \sum_ {d \in R Q _ {2}} P (f ^ {\prime} | d) ^ {\prime} P (Q | d)}{ \sum_ {d \in R Q ^ {\prime}} P (Q | d)} \end{array}
$$

Since the documents in $R Q _ { 1 }$ only describe facts in $F ^ { \prime }$ , we have that $\begin{array} { r } { \forall d \in R Q _ { 1 } \ , P ( f ^ { \prime } | d ) ^ { \prime } = \frac { F F ( f ^ { \prime } , d ) } { \sum _ { ( f , d ) \in \mathrm { C t x t ^ { \prime } } } F F ( f , d ) } = } \end{array}$ ${ \frac { F F ( f ^ { \prime } , d ) } { \sum _ { ( f , d ) \in { \mathrm { C t x t } } } F F ( f , d ) } } = P ( f ^ { \prime } | d )$ <sup>ð Þ</sup>, and consequently:

$$
\begin{array}{l} P (f ^ {\prime} | R Q ^ {\prime}) = \frac {\sum_ {d \in R Q _ {1}} P (f ^ {\prime} | d) P (Q | d)}{\sum_ {d \in R Q ^ {\prime}} P (Q | d)} \\ + \frac {\sum_ {d \in R Q _ {2}} P (f ^ {\prime} | d) ^ {\prime} P (Q | d)}{\sum_ {d \in R Q ^ {\prime}} P (Q | d)} \end{array}
$$

The previous formula can be rewritten as follows:

$$
\begin{array}{l} P (f ^ {\prime} | R Q ^ {\prime}) = (\frac {\sum_ {d \in R Q _ {1}} P (f ^ {\prime} | d) P (Q | d)}{\sum_ {d \in R Q ^ {\prime}} P (Q | d)} \\ \quad + \frac {\sum_ {d \in R Q _ {2}} P (f ^ {\prime} | d) P (Q | d)}{\sum_ {d \in R Q ^ {\prime}} P (Q | d)} + \frac {\sum_ {d \in R Q _ {2}} P (f ^ {\prime} | d) ^ {\prime} P (Q | d)}{\sum_ {d \in R Q ^ {\prime}} P (Q | d)} \\ \quad - \frac {\sum_ {d \in R Q _ {2}} P (f ^ {\prime} | d) P (Q | d)}{\sum_ {d \in R Q ^ {\prime}} P (Q | d)}) \frac {\sum_ {d \in R Q} P (Q | d)}{\sum_ {d \in R Q} P (Q | d)} \end{array}
$$

Since $R Q _ { 1 } \cup R Q _ { 2 } = R Q ,$ , we have that:

$$
\begin{array}{l} P (f ^ {\prime} | R Q ^ {\prime}) = \frac { \sum_ {d \in R Q} P (f ^ {\prime} | d) P (Q | d)}{ \sum_ {d \in R Q} P (Q | d)} \frac { \sum_ {d \in R Q} P (Q | d)}{ \sum_ {d \in R Q ^ {\prime}} P (Q | d)} \\ + \frac { \sum_ {d \in R Q _ {2}} (P (f ^ {\prime} | d) ^ {\prime} - P (f ^ {\prime} | d)) P (Q | d)}{ \sum_ {d \in R Q ^ {\prime}} P (Q | d)} \end{array}
$$

The relevance $P ( Q | d )$ of the documents $d \in R Q \supseteq R Q ^ { \prime }$ do not change because the IR condition Q is maintained. In this way, $\begin{array} { r } { \beta = \frac { Q u a l i t y } { Q u a l i t y ^ { \prime } } = \frac { \sum _ { d \in R Q } P ( Q | d ) } { \sum _ { d \in R O ^ { \prime } } P ( Q | d ) } \overset { \sim } { = } 1 } \end{array}$ (notice that $| R Q | \geq | R Q ^ { \prime } | )$ . On the other hand, $P ( f ^ { \prime } | d ) ^ { \prime } { \ge } P ( f ^ { \prime } | d )$ because $| \{ ( f , ~ d ) \in F C t x t ^ { \prime } \} | \leq | \{ ( f , ~ d ) \in F C t x t \} |$ and $\begin{array} { r } { \sum ( f , \ d ) { \in } F C t x t ^ { \prime } F F ( f , \ d ) { \le } \sum _ { ( f , \ d ) { \in } F C t x t } F F ( f , \ d ) } \end{array}$ . Finally, the previous formula can be expressed as:

$$
\begin{array}{l} P (f ^ {\prime} | R Q ^ {\prime}) = \beta P (f ^ {\prime} | R Q) + \delta (f ^ {\prime}) \\ \delta (f ^ {\prime}) = \sum_ {\{d \in R Q ^ {\prime} | \exists (f, d) \in F C t x t \setminus F C t x t ^ {\prime} \}} \quad (\frac {P (f ^ {\prime} | d) ^ {\prime}}{Q u a l i t y} \\ - \frac {P (f ^ {\prime} | d)}{Q u a l i t y ^ {\prime}}) P (Q | d) \geq 0 \end{array}
$$

Theorem 2. Let $\{ C _ { i } \in C _ { D _ { i } } , i = I . . . n _ { f } ^ { \Zag }$ be a set of grouping categories, and let $G r o u p ( e _ { I } , ~ . . . , ~ e _ { n } )$ be the group of facts of the cube characterized by the category values $( e _ { I } , ~ . . . , ~ e _ { n } ) { \in } C _ { I } \times . . . \times C _ { n } .$ The relevance value of the group $P ( G r o u p ( e _ { I } , ~ . . . , ~ e _ { n } ) | R Q )$ is determined by the following formula:

$$
P (G r o u p (e _ {1}, \dots , e _ {n}) | R Q) = \sum_ {f _ {i} \in G r o u p (e _ {i}, \dots , e _ {n})} P (f _ {i} | R Q)
$$

Proof. Consider the fact f characterized by the dimension values $( e _ { 1 } , . . . , e _ { 2 } )$ . By applying the formula (4), the probability $P ( f | d )$ of finding the fact f in the document d can be estimated as follows:

$$
\begin{array}{l} P (f | d) = \frac {F F (f , d)}{| d | _ {f}} = \sum_ {f _ {i} \in G r o u p (e _ {1}, \dots , e _ {n})} \frac {F F (f _ {i} , d)}{| d | _ {f}} \\ = \sum_ {f _ {i} \in G r o u p (e _ {1}, \dots , e _ {n})} P (f _ {i} | d) \end{array}
$$

That is, $P ( f | d )$ can be calculated by adding the dimension values frequency of each fact of $G r o u p ( e _ { 1 } , ~ . . . , ~ e _ { n } )$ in the document d. Notice that $\forall f _ { i } \in G r o u p ( e _ { 1 } , . . . , e _ { n } ) , f _ { i } \sim \neg _ { 1 } \ e _ { 1 } \land . . . \land f _ { i } \sim \neg _ { n } \ e _ { n } .$

Thus, with the previous result, the fact relevance calculus formula (3) can be expressed as:

$$
\begin{array}{l} P (f | R Q) = \frac {\sum_ {d \in R Q} P (f | d) P (Q | d)}{\sum_ {d \in R Q} P (Q | d)} \\ = \sum_ {d \in R Q} \frac {\left(\sum_ {f _ {i} \in G r o u p (e _ {1} , \dots , e _ {n})} P (f _ {i} | d)\right) P (Q | d)}{\sum_ {d \in R Q} P (Q | d)} \\ = \sum_ {f _ {i} \in G r o u p (e _ {1}, \dots , e _ {n})} \left(\frac {\sum_ {d \in R Q} P (f _ {i} | d) P (Q | d)}{\sum_ {d \in R Q} P (Q | d)}\right) \\ = \sum_ {f _ {i} \in G r o u p (e _ {1}, \dots , e _ {n})} P (f _ {i} | R Q) \end{array}
$$

## References

[1] A. Badia, Text warehousing: present and future, in: J. Darmont, O. Boussaid (Eds.), Processing and Managing Complex Data for Decision Support, Idea Group, 2006, pp. 96–121.

[2] R.A. Baeza-Yates, B.A. Ribeiro-Neto, Modern Information Retrieval, ACM Press/Addison-Wesley, 1999.

[3] K. Beyer, D. Chambérlin, L.S. Colby, F. Özcan, H. Pirahesh, Y. Xu, Extending XQuery for analytics, Proc. of SIGMOD, ACM Press, New York, 2005, pp. 503–514.

[4] S. Bhowmick, S.K. Madria, W.-K. Ng, E.-P. Lim, Web warehousing: design and issues, Proc. of DWDM, Springer-Verlag, London, 1998, pp. 93–104.

[5] T.T. Chinenyanga, N. Kushmerick, An expressive and efficient language for XML information retrieval, in: G. Mecca, J. Siméon (Eds.), Proc. of WebDB, ACM Press, New York, 2001, pp. 1–6.

[6] W.B. Croft, Combining approaches to information retrieval, Advances in Information Retrieval, Kluwer Academic Publishers, Boston, 2000, pp. 1–36.

[7] R. Danger, I. Sanz, R. Berlanga, J. Ruiz-Shulcloper, A proposal for the automatic generation of instances from unstructured text, in: J.F. Martínez, J.A. Carrasco-Ochoa (Eds.), Proc. of CIARP, Springer-Verlag, 2004, pp. 462–469.

[8] N. Fuhr, K. Grojohann, XIRQL: a query language for information retrieval in XML documents, in: W.B. Croft, D.J. Harper, D.H. Kraft, J. Zobel (Eds.), Proc. of SIGIR, ACM Press, New York, 2001, pp. 172–180.

[9] W.H. Inmon, Building the Data Warehouse, John Wiley & Sons, New York, 1996.

[10] R. Kimball, The Data Warehouse Toolkit, John Wiley & Sons, New York, 2002.

[11] V. Lavrenko, W.B. Croft, Relevance-based language models, Proc. of SIGIR, ACM Press, New York, 2001, pp. 120–127.

[12] D.M. Llidó, R. Berlanga, M.J. Aramburu, Extracting temporal references to assign document event-time periods, in: H.C. Mayr, J. Lazansky, G. Quirchmayr, P. Vogel (Eds.), Proc. of DEXA, Springer-Verlag, Berlin, 2001, pp. 62–71.

[13] B.R. Moole, A probabilistic multidimensional data model and algebra for OLAP in decision support systems, Proc. of IEEE SoutheastCon, 2003.

[14] Morgan Stanley Capital International Inc., http://www.msci.com.

[15] B.-K. Park, H. Han, I.-Y. Song, XML-OLAP: a multidimensional analysis framework for XML warehouses, in: A.M. Tjoa, J. Trujillo (Eds.), Proc. of DaWaK, Springer-Verlag, Berlin, 2005, pp. 32–42.

[16] T.B. Pedersen, C.S. Jensen, C.E. Dyreson, A foundation for capturing and querying complex multidimensional data, Information Systems 26 (5) (2001).

[17] D. Pedersen, K. Riis, T.B. Pedersen, XML-extended OLAP querying, Proc. of SSDBM, IEEE Computer Society, Washington, 2002, pp. 195–206.

[18] J.M. Pérez, R. Berlanga, M.J. Aramburu, A document model based on relevance modeling techniques for semi-structured information, in: F. Galindo, M. Takizawa, R. Traunmüller (Eds.), Proc. of DEXA, Springer-Verlag, Berlin, 2004, pp. 318–327.

[19] J.M. Pérez, T.B. Pedersen, R. Berlanga, M.J. Aramburu, IR and OLAP in XML document warehouses, in: D.E. Losada, J.M. Fernández-Luna (Eds.), Proc. of ECIR, Springer-Verlag, Berlin, 2005, pp. 536–539.

[20] J.M. Ponte, W.B. Croft, A language modeling approach to information retrieval, Research and Development in Information Retrieval, ACM Press, 1998, pp. 275–281.

[21] T. Priebe, G. Pernul, Towards integrative enterprise knowledge portals, Proc. of CIKM, ACM Press, New York, 2003, pp. 216–223.

[22] I. Sanz, R. Berlanga, M.J. Aramburu, Gathering metadata from web-based repositories of historical publications, Proc of DEXA, IEEE Comp. Society, 1998, pp. 473–478.

[23] H. Schimd, Probabilistic part-of-speech tagging using decision trees, Proc. of Intl. Conf. on New Methods in Language Processing, 1994.

[24] G. Spofford, MDX Solutions with Microsft SQL Server Analysis Services, John Wiley & Sons, New York, 2001.

[25] W3C, Extensible Markup Language (XML) 1.0, http://www.w3. org/TR/REC-xml. 2004.

[26] Xyleme, A dynamic warehouse for XML data of the Web, IEEE Data Engineering Bulletin 24 (2) (2001).

![](/api/attachments/MNQ4CEQH/fulltext/images/f0414dd953373580ae1828c4f899cbca9504550c30fc9c4f6e440f00e8729002.jpg)  
Juan Manuel Pérez-Martínez obtained a B.S. degree from the Universitat Jaume I (Spain) in 2000, where he is registered for a Ph.D. Currently he is associate lecturer at the same university. He is author of a number of communications in international conferences such as DEXA, ECIR, etc. His research interests are information retrieval, multidimensional databases, and web-based technologies. Contact him at Juanma.Perez@lsi.uji.es.

![](/api/attachments/MNQ4CEQH/fulltext/images/7dda9b1d7b6bb87f188eed1e69069dc256eaec261124cb3b66c4831f69774588.jpg)

Rafael Berlanga-LLavori is an associate professor in the Computer Science career at University Jaume I, Spain for 12 years. He received the B.S. degree from Universidad de Valencia in Physics, and the Ph.D. degree in Computer Science in 1996 from the same university. He is author of several articles in international journals, such as Information Processing and Management, Concurrency: Practice and Experience, Applied Intelli-

gence, among others, and numerous communications in international conferences such as DEXA, ECIR, CIARP, etc. His current research interests are knowledge bases, information retrieval, and temporal reasoning. Contact him at berlanga@lsi.uji.es.

![](/api/attachments/MNQ4CEQH/fulltext/images/09f8741f8bdcbe1a0c1d9edf70b298e36808e0b2fb5a2a5c087dcbf19c313c39.jpg)

María José Aramburu-Cabo is an associate professor in the Computer Science career at University Jaume I, Spain. She obtained the B.S degree from Universidad Politécnica de Valencia in Computer Science in 1991, and a Ph.D. from the School of Computer Science of the University of Birmingham (UK) in 1998. She is author of several articles in international journals, such as Information Processing and Management, Concurrency:

Practice and Experience, Applied Intelligence, and numerous communications in international conferences such as DEXA, ECIR, etc. Her main research interests include document databases, and their applications. Contact her at aramburu@icc.uji.es

![](/api/attachments/MNQ4CEQH/fulltext/images/19e61da85bfcd3ab91cfad8aaeac82c837a9a963816ab7d97731ebece99bbaea.jpg)

Torben Bach Pedersen is an associate professor of Computer Science at Aalborg University, Denmark. His research interest includes multidimensional databases, OLAP, data warehousing, federated databases, data streams, and location-based services. He has published more than 60 scientific papers on these issues in journals and conferences such as The VLDB Journal, Information Systems, IEEE Computer, VLDB, ICDE, SSDBM,

SSTD, IDEAS, ACM-GIS, ECIR, Hypertext, DOLAP, and DaWaK. He is a member of the Editorial Board of the International Journal on Data Warehousing and Mining, and has served on more than 30 program committees including VLDB, ICDE, EDBT, SSDBM, and DaWaK. Before joining Aalborg University, he worked in the software industry for more than six years. He received the Ph.D. and M.S. degrees in Computer Science from Aalborg University and Aarhus University, respectively. He is a member of the IEEE, the IEEE Computer Society, and the ACM. Contact him at tbp@cs.aau.dk.
