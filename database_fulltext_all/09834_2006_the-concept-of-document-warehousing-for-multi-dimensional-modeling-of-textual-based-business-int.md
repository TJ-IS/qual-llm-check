---
otero_id: 9834
otero_key: "H85Y8ND5"
title: "The concept of document warehousing for multi-dimensional modeling of textual-based business intelligence"
authors: "Frank S.C. Tseng; Annie Y.H. Chou"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.02.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The concept of document warehousing for multi-dimensional modeling of textual-based business intelligence<sup>B</sup>

Frank S.C. Tseng <sup>a,\*</sup>, Annie Y.H. Chou <sup>b,1</sup>

<sup>a</sup>Department of Information Management, National Kaohsiung First University of Science and Technology, 1 University Road, YenChao, Kaohsiung, Taiwan 824, ROC

<sup>b</sup>Department of Computer and Information Science, Chinese Military Academy, Taiwan

Available online 17 June 2005

## Abstract

During the past decade, data warehousing has been widely adopted in the business community. It provides multidimensional analyses on cumulated historical business data for helping contemporary administrative decision-making. Nevertheless, it is believed that only about 20% information can be extracted from data warehouses concerning numeric data only, the other 80% information is hidden in non-numeric data or even in documents. Therefore, many researchers now advocate that it is time to conduct research work on document warehousing to capture complete business intelligence. Document warehouses, unlike traditional document management systems, include extensive semantic information about documents, cross-document feature relations, and document grouping or clustering to provide a more accurate and more efficient access to text-oriented business intelligence. In this paper, we discuss the basic concept of document warehousing and present its formal definitions. Then, we propose a general system framework and elaborate some useful applications to illustrate the importance of document warehousing. The work is essential for establishing an infrastructure to help combine text processing with numeric OLAP processing technologies. The combination of data warehousing and document warehousing will be one of the most important kernels of knowledge management and customer relationship management applications. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Data warehousing; Document warehousing; Knowledge management; OLAP

## 1. Introduction

Data warehousing [18] and data mining techniques [17] are gaining popularity as organizations realize the benefits of being able to perform multi-dimensional analyses of cumulated historical business data to help contemporary administrative decision-making [2,4,15, 17,22]. This inspires enterprises to eagerly delve into useful business intelligence (BI) from both internal and external data. Business intelligence is supposed to provide decision-makers with the tactical and strategic information they need for understanding, managing, and coordinating the operations and processes in organizations.

However, much of the efforts have only touched the tip of the information iceberg. While the techniques regarding data warehouses, multi-dimensional models, on-line analytical processing (OLAP), or even ad hoc reports have served enterprises well; they do not completely address the full scope of business intelligence. It is believed that [42], for the business intelligence of an enterprise, only about 20% information can be extracted from formatted data stored in relational databases. The remaining 80% information is hidden in unstructured or semi-structured documents. This is because the most prevalent medium for expressing information and knowledge is text. For instances, market survey reports, project status reports, meeting records, customer complaints, e-mails, patent application sheets, and advertisements of competitors are all recorded in documents.

Despite that, documents in the Web, enterprise repositories, and public document management systems are all growing as well. Therefore, knowledge workers, managers, and executives still have to spend much of the working moment reading dozens, if not hundreds, of various types of electronic documents spread over the Internet. There is just too much text to digest in daily life. The fast-growing and tremendous amount of documents has far exceeded the human ability for comprehension without powerful tools. As a result, when doing important decision-making, some relevant documents may be ignored, and some irrelevant documents may be considered by intuition. We believe that leaving out information induced from relevant documents or keeping information by intuitively guessing from irrelevant documents may be detrimental, causing disaster from the strategy weaved by incomplete information.

To alleviate this phenomenon, Grigsby [14], McCabe et al. [26] and Sullivan [33] have advocated that documents should be properly warehoused according to some well-defined concepts for expanding the scope of business intelligence to include textual information. Ishikawa and colleagues [19–21] even advocated this by implementing a prototype system to support management of compound documents, keyword-based and content-based retrieval. They used ECA rules to classify multimedia documents, and SOM (Self-Organizing Map) to cluster a set of collected texts into the number of groups in the retrieval space of manageable dimensions.

Hence, we think one of the next challenges of the information community will be the study of topics about document warehousing and text mining to help enterprises in obtaining complete business intelligence. Although research work regarding text mining have been conducted widely (for examples, the gentle readers are referred to Refs. [44,23–25,40,34]), however, the issues regarding document warehousing are rarely addressed. We have proposed a multidimensional indexing structure, called D-tree in Ref. [36] to study the performance measurement for constructing document warehouses. Some theoretical analyses on the properties of indexing a document warehouse were also elaborated in Ref. [35]. With document warehouses, the documents of enterprises can be well organized for effective analysis, or feature extraction to create distilled and fruitful business intelligence.

Since there are usually many diverse concepts involved in a document, a document is multi-dimensional in nature. Document warehouses, unlike traditional document management systems, include extensive semantic information about documents, cross-document feature relations, and document grouping or clustering to provide more accurate and more efficient access to text-oriented business intelligence. To facilitate flexible and effective multi-dimensional on-line analytical document processing and browsing, a multi-dimensional query language for querying document warehouses is indispensable. In Ref. [37], we have devised a multi-dimensional query expression for querying document warehouses to provide users an easy and efficient way of performing online analytical processing on documents.

Although issues about document warehousing have been addressed in Refs. [14,26,33], there are still no formal definitions established up to now. In this work, we will first discuss the concept of document warehousing and formally define the related terms. Then, we propose a framework for document warehousing and elaborate some applications of document warehousing to sketch an attractive roadmap of using document warehouses.

As Web applications proliferate tremendously, there will be a great deal of need for rapid text processing and browsing. Document warehousing does not only provide an infrastructure for developing tools for business executives to systematically organize, understand, and properly categorize their documents to help strategic decision-making, but also integrate all kinds of related documents being browsed instantly.

Document warehousing also provides an important platform for on-line analytical processing (OLAP) in text level for the interactive analysis of multi-dimen sional documents of various granularities, which facilitates effective text mining, integrates documents into the business intelligence infrastructure, and provides the means to search for and target specific information the way we now do with numeric data. Furthermore, as the construction of data warehouses can be viewed as an important step for data mining, the construction of document warehouses can be regarded as an indispensable preprocessing step for text mining. We realize that, no matter how wonderful the mechanism a system adopts, it cannot do much without good content organization of the domain on which it is to work. Moreover, we often recognize that, once a good content organization is available, many different mechanisms might be employed equally well to implement effective systems. A well-organized document warehouse just provides various mechanisms a wonderful content organization to work on.

In this paper, based on our prior works [35–37], we further illustrate the general architecture of a document warehouse and its applications. The work is essential for establishing an infrastructure to help combine text processing with numeric OLAP processing technologies. We believe such an infrastructure can help extend numeric data analysis for combination with text processing technologies to make data warehousing and document warehousing one of the most important kernels of knowledge management and customer relationship management applications. By combining document warehousing and data warehousing, documents can be integrated into the business intelligence infrastructure and can provide the means to search for and target specific information the way we now do with numeric data.

Although the content of documents are often more than text and may include some graphics or even multimedia data, in this paper, we only consider the textual parts of documents. In the future, we will extend our work to encompass the entirety of documents, which may be called multimedia warehousing [19–21].

Our paper is organized as follows. In Section 2, the important concepts of document warehousing are formally presented. Then, based on these definitions, we will propose a general architecture for constructing document warehouses in Section 3. Then, some of the applications of document warehouses will be discussed in Section 4. Finally, we conclude and propose some future work in Section 5.

## 2. An introduction to document warehousing

In the following, we give some definitions about document, dimension, document tuple, and document cube for document warehousing.

Definition 1. A document $T = \{ k _ { 1 } , ~ k _ { 2 } , ~ . ~ . ~ . ~ , ~ k _ { i } \}$ is a logical unit of text characterized by a set of keywords $\{ k _ { 1 } , k _ { 2 } , \ldots , k _ { i } \}$

To organize documents into structures, we need the concept of dimension defined as follows.

Definition 2. A dimension D is a tree structure of m levels, $m \geq 1$ , which is used for representing the hierarchical relationships among a set of keywords. A node in a dimension D is called a member, and each internal node contains a special child called summary member, denoted <sup>d</sup>\*<sup>T</sup>, which is used for denoting the total concept of the other children of the internal node.

When drawing a dimension, we usually leave out a summary member, since it has the same meaning with its parent node. Besides, the keywords in a dimension are not limited to only those contained in document contents. Any property or metadata of a document file (e.g., those defined in Dublin Core Metadata Element Set [38]) can also be regarded as a keyword in a dimension for constructing document cubes. Furthermore, if documents are organized into predefined categories, the category hierarchy to which a document belongs can also be regarded as a dimension. That is, text is not unstructured as is often assumed, which has been pointed out by Sullivan [33]. The concept of dimension can be employed to model the structure inherently hidden in text.

According to the keyword sources, dimensions can be distinguished into the following types:

1. Ordinary dimension. A dimension contains keywords used for scanning the document contents.

2. Metadata dimension. A dimension contains keywords used for scanning document file properties or metadata. For example, in Dublin Core Metadata Element Set, there are title, creator, subject, description, publisher, contributor, date, type, format, identifier, source, language, relation, coverage, and rights; all can be regarded as metadata dimensions.

3. Category dimension. A dimension contains keywords corresponding to the nodes in a category hierarchy, such as Wordnet [27,41], in which all considered documents should be multi-categorized. A document is related to such dimension or if not it can be determined manually or automatically assigned by document categorization tools.

To simplify our discussion, we mainly use ordinary dimensions, together with the metadata dimension time (i.e., date), in the following examples.

Definition 3. For a dimension D, the ith-level member set, denoted D(i), is defined as $D ( i ) { = } \{ a | a$ is a member in the ith level of D, but a is not a summary member}. Besides, we use D(0) to denote the union of all non-summary members in D, which is the union of all ith level member sets in D. That is, $D ( 0 ) { = } \cup _ { 1 \leq i \leq h }$ D(i), where h is the height of D. In practice, each D(i) has a specific name, which will be called the ith-level name.

Practically, a dimension can be constructed from a relational table, with each level corresponding to an attribute in the relation and the attribute names usually used as the corresponding level names. To illustrate the above definitions, we give an example as follows. Besides, any keyword in a dimension can be implemented as a set of synonyms to encompass more semantics.

Example 1. Suppose there is a relation Region representing the regions of Taiwan as shown in Table 1(a).

Table 1  
A relation Region and its alternative for constructing dimension R

<table><tr><td colspan="4">(a)</td></tr><tr><td colspan="3">Location</td><td>City</td></tr><tr><td colspan="3">South</td><td>Tainan</td></tr><tr><td colspan="3">South</td><td>Kaohsiung</td></tr><tr><td colspan="3">South</td><td>Pingtong</td></tr><tr><td colspan="3">North</td><td>Taipei</td></tr><tr><td colspan="3">North</td><td>Taoyun</td></tr><tr><td colspan="3">North</td><td>Hsinchu</td></tr><tr><td colspan="4">(b)</td></tr><tr><td>Tag</td><td>Parent</td><td>Level</td><td>Keyword</td></tr><tr><td>1</td><td>1</td><td>1</td><td>(All Region)</td></tr><tr><td>2</td><td>1</td><td>2</td><td>South</td></tr><tr><td>3</td><td>1</td><td>2</td><td>North</td></tr><tr><td>4</td><td>2</td><td>3</td><td>Tainan</td></tr><tr><td>5</td><td>2</td><td>3</td><td>Kaohsiung</td></tr><tr><td>6</td><td>2</td><td>3</td><td>Pingtong</td></tr><tr><td>7</td><td>3</td><td>3</td><td>Taipei</td></tr><tr><td>8</td><td>3</td><td>3</td><td>Taoyun</td></tr><tr><td>9</td><td>3</td><td>3</td><td>Hsinchu</td></tr></table>

Another alternative is shown in Table 1(b). This relation can be used to construct a dimension, denoted R as depicted in Fig. 1, where the first level corresponds to the dimension itself, which is commonly denoted $^ { * * } ( A l l ~ R e g i o n ) ^ { * }$ , and the second and third levels are derived from the attributes Location, and City, respectively. All nodes in Fig. 1 with label <sup>d</sup>\*<sup>T</sup> are summary members. That is, the summary member in the second level has the same meaning with all regions in Taiwan, which represents {South, North}. Besides, the summary members under South and North have the same corresponding meaning with South and North, which denote {Tainan, Kaohsiung, Pingtong} and {Taipei, Taoyun, Hsinchu}, respectively. By omitting all the summary members, Fig. 1 is redrawn in Fig. 2. According to the illustration of dimension R, we know that R(1) = {(All Region)}, R(2) = {South, North}, and R(3) = {Tainan, Kaohsiung, Pingtong, Taipei, Taoyun, Hsinchu}, and $R ( 0 ) { = } \left\{ \left( A l l R e g i o n \right) \right.$ , South, North, Tainan, Kaohsiung, Pingtong, Taipei, Taoyun, Hsinchu}.

For a dimension D, there are two basic operations called drill-down and roll-up, which are formally defined as follows.

Definition 4. For a dimension D, expanding an internal node to obtain all of its children is called drill-down, and shrinking a set of children to obtain their common parent is called roll-up.

![](/api/attachments/H85Y8ND5/fulltext/images/56a75ba64c28f0e4cbd0131b60232d896e9e1df528cee0c0eba39442e714388e.jpg)  
Fig. 1. An illustration of dimension R.

This can be further clarified by the following definitions.

Definition 5. For any two n-tuple of keywords $A = ( a _ { 1 } , a _ { 2 } , \ldots , a _ { i } , \ldots , a _ { n } )$ and $B = ( b _ { 1 } , b _ { 2 } , . . . , b _ { i } ,$ $\ldots , b _ { n } )$ defined on n dimensions $( D _ { 1 } , D _ { 2 } , \ldots , D _ { i } ,$ $\ldots , D _ { n } )$ , where $a _ { i }$ and $b _ { i } \in D _ { i } ( 0 )$ , we define B is a member of drilling down A along dimension $D _ { i }$ (or A is a member of rolling up B along dimension $D _ { i } ) _ { \dag }$ denoted $A \prec _ { i } B$ , if and only if there exists exactly an i, $1 \leq i \leq n$ , such that $b _ { i }$ is a child of $a _ { i }$ in $D _ { i } ,$ and $b _ { j } = a _ { j }$ for all $j \neq i$

Definition 6. For a document T with unique identifier $i d _ { T } ,$ a document index of T defined on n dimensions $( D _ { 1 } , \ D _ { 2 } , \ . . . , \ D _ { n } )$ is denoted $x { = } ( i d _ { T } , ~ K _ { T } )$ , where $K _ { T } { = } ( K _ { 1 } , K _ { 2 } , \ldots , K _ { i } , \ldots , K _ { n } )$ is an n-tuple of keyword sets, such that each $K _ { i }$ contains a set of keywords, and for all keywords $k _ { i j } \in K _ { i } , \ k _ { i j } \in T$ and $k _ { i j } \in D _ { i } ( 0 )$ , for all $1 \leq i \leq n$

For simplicity, the first and second components of a document index $x { = } ( i d _ { T } , K _ { T } )$ will be denoted $x ^ { 1 }$ and $x ^ { 2 } \ ( \mathrm { i . e . , } \ x ^ { 1 } = i d _ { T }$ and $\scriptstyle x ^ { 2 } = K _ { T } )$ , respectively. When all $| K _ { i } | = 1$ , the document index is also called a base document index, and each $K _ { i }$ can also be denoted by its only element for convenience (That is, in such cases, a $K _ { T } = ( \{ k _ { 1 } \} , \ \{ k _ { 2 } \} , \ \ldots , \ \{ k _ { i } \} , \ \ldots , \ \{ k _ { n } \} )$ can be abbreviated as $K _ { T } { = } ( k _ { 1 } , k _ { 2 } , \ldots , k _ { i } , \ldots , k _ { n } ) )$ . If there are at least one $K _ { i } ,$ such that $| K _ { i } | > 1$ , and the sizes of the other $K _ { j } \mathrm { ' s }$ all equal to 1, then the document index is also called a composite document index. Finally, if there are some $K _ { i } ,$ , such that $| K _ { i } | = 0$ , then the document index is also called a degenerate document index. In the following, a degenerate document index with some $| K _ { i } | = 0$ will be generalized by using the top level member set of the corresponding dimension, $D _ { i } ( 1 )$ , to substitute the missing keyword set $K _ { i }$

Example 2. Suppose there is a complaint e-mail issued from a customer as shown in Fig. 3. Then, a base document index of T defined on the above two dimensions (R, P) can be obtained as $x = ( \mathrm { A } 0 0 0 1$ 4 ({Kaohsiung}, {TV})), where A0001 is the unique identifier of T.

![](/api/attachments/H85Y8ND5/fulltext/images/5bb3fcb9c5496ee7d77552e6a99d50267a1c4c0dfc3ee6195467443d81b10a9b.jpg)  
Fig. 2. A concise illustration of dimension R.

<table><tr><td>To whom it may concern:We have bought a TV from your Kaohsiung branch last weekend. However, we found the screen is severely unstable. Please give us the phone number of your service center. Thank you for your kindly help.Sincerely,Frank S.C. Tseng</td></tr></table>

Fig. 3. A complaint e-mail issued by a customer (A0001).

The basic component of a document cube is called a cell, which is defined as follows.

Definition 7. A cell defined on n dimensions $( D _ { 1 } , D _ { 2 } $ $\ldots , D _ { n } )$ is denoted $c = ( t _ { c } , X _ { c } )$ , where $t _ { c } = ( c _ { 1 } , c _ { 2 } , \dots ,$ $c _ { i } , \ldots , c _ { n } ) , c _ { i } \in D _ { i } ( 0 ) \cup \{ { ^ { * * } } \} , 1 { \leq } i { \leq } n$ , and $X _ { c } = \{ x _ { I } ,$ $x _ { 2 } , \ldots , x _ { j } , \ldots , x _ { m } \}$ is a set of document indices of the form $x _ { j } = ( i d _ { T j } , \ ( K _ { 1 } , K _ { 2 } , \ \ldots , \ K _ { n } ) )$ , where $i d _ { T j }$ is the unique identifier of some document $T _ { j }$ and $K _ { i } \cap$ $D _ { i } ( 0 ) { \neq } \emptyset , \ 1 { \leq } i { \leq } n$ . The set of all such document unique identifiers $i d _ { T j }$ involved in the cell $c = ( t _ { c } ,$

$X _ { c } )$ is denoted $I D ( c ) = \{ x _ { j } ^ { I } | \forall x _ { j } \in X _ { c } \}$ . That is, a document with unique identifier in ID(c) can be directly accessed from the cell c.

Definition 8. A cell $c = ( t _ { c } , X _ { c } )$ , where $t _ { c } = ( c _ { 1 } , c _ { 2 } , \dots ,$ $c _ { i } , \ldots , c _ { n } )$ , defined on n dimensions $( D _ { 1 } , D _ { 2 } , \dots ,$ $D _ { n } )$ is called an m-d cell, $0 \leq m \leq n$ , if and only if there are exactly m non-summary member $\begin{array} { r l } { c _ { i } } & { { } \left( \mathrm { i . e . } \right. } \end{array}$ 2 $c _ { i } \neq { } ^ { 6 \ast \gamma } )$ . If $m = n$ and $c _ { i } \in D _ { i } ( h _ { i } )$ , where $h _ { i }$ is the height of $D _ { i } ,$ for all $1 \leq i \leq n ,$ , then c is also called a base cell; otherwise c is called a non-base cell.

Definition 9. An n-dimensional i-d cell $a = ( ( a _ { 1 } , a _ { 2 } ,$ $\dots , a _ { n } ) , X _ { a } )$ is a parent of another n-dimensional i-d cell $b = ( ( b _ { 1 } , \ b _ { 2 } , \ \dots , \ b _ { n } ) , \ X _ { b } )$ , if and only if the following conditions hold:

![](/api/attachments/H85Y8ND5/fulltext/images/216de4a3f6007966168a7f178fe8c99f9b53eaa27a753fae3a441256009dc2b1.jpg)  
Fig. 4. A sample illustration of a document cube.

1. There exists exactly one k, such that $a _ { k }$ is the parent of $b _ { k }$ in $D _ { k } ,$ , and $a _ { l } = b _ { l }$ , for all $l \neq k , 1 \leq l \leq n$

2. $I D ( b ) \subseteq I D ( a )$ , where $U D ( a )$ and $I D ( b )$ are the sets of all document unique identifiers involved in cells a and $^ { b , }$ respectively.

Definition 10. A document cube $D C = ( S , \ ( D _ { 1 } , \ D _ { 2 } ,$ $\dots , D _ { n } ) )$ , where S is a set of documents defined on n dimensions $( D _ { 1 } , D _ { 2 } , \dots , D _ { n } ) .$ , is a cube composed of all cells $c _ { i } { = } ( t _ { c i } , \ X _ { c i } )$ with $t _ { c _ { i } } \in \times _ { 1 \leq j \leq n } D _ { j } ( 0 )$ and $I D ( c _ { i } ) \subseteq S$

Based on the above definitions, a set of documents S can be multi-dimensionally indexed by a document cube $D C = ( S , \ ( D _ { 1 } , \ D _ { 2 } , \ . \ . . , \ D _ { n } ) )$ , which allows users to browse documents by rolling up and drilling down along some dimensions D<sub>i</sub> for different granularities and perspectives, obtaining further insight into relationships among documents. A sample illustration of a document cube DC = (S, (R, P, T)) is shown in Fig. 4, where R and P represent the aforementioned dimensions region and product, respectively. Besides, we assume T is a dimension representing time.

## 3. A framework for document warehousing

Designing a comprehensive architecture for document warehousing can be challenging because document warehousing covers a wide spectrum of concepts as we have shown in Section 2. Fortunately, there is already a general architecture being established for data warehousing in Ref. [2]. Based on the architecture, we extend the constructs to include more features for documents warehousing. The proposed architecture is shown in Fig. 5.

Based on this architecture, we outline the general process of extraction, transformation, loading, dimensional modeling, and construction of a document warehouse in Fig. 6. In this process, documents stored in different document sources are respectively transformed and loaded into the document base. At the same time, some of the metadata are retrieved or generated into the metadata repository. Besides, the document may be further integrated and categorized into groups in the document base according to their metadata or keywords. Then, by applying the dimensional modeling process, fruitful document cubes can be created for on-line analytical processing in text level based on certain business models. Notice that a document cube does not need space to store the document contents; it only contains the dimension information and the file pointers, which can be used to trace back the original document contents stored in the document base. Finally, the processed result can be presented via hyper-linked Web presentations.

![](/api/attachments/H85Y8ND5/fulltext/images/523b2b9b945e7a825f90997e9d76afb3849ebaeff8e4111bfa2d8ff28287eb20.jpg)  
Fig. 5. The proposed architecture of document warehouses.

![](/api/attachments/H85Y8ND5/fulltext/images/5f869233a4041902e8698dadbed0d6e35c8845ad2d2c7300b377fa9c2347bb13.jpg)  
Fig. 6. The general process of extraction, transformation, loading, dimensional modeling, and construction of a document warehouse.

The major components of a document warehouse are explained as follows.

## 3.1. Document sources

The source of documents for a document warehouse is supplied from:

1. Internal sources: In an organization, there are documents in various formats spread throughout the organization on any kind of document repositories. The files may be in XML formats, MS Word formats, e-mail or even plain text.

2. External sources: Documents may also come from the Internet, including Web pages, FTP sites, commercially available document bases, private documents shared by private servers or document repositories associated with an organization’s suppliers or customers.

## 3.2. Front-end component

The front-end component performs all the necessary pre-processing of documents, such as text summarization [12,16], text feature extraction [10], document categorization [3], or other text mining procedures [24,25,34], and then store the obtained features or patterns into the meta-data or store the summarized result as another summarized document.

## 3.3. Warehouse administrator

The warehouse administrator performs all the operations associated with the management of the documents in the warehouse. The operations include:

1. Enrich the metadata of all stored documents: Some of the document metadata (e.g., those defined in Dublin Core Metadata Element Set [38]) may be missing and should be added manually by the warehouse administrator.

2. Perform necessary text mining operations or generate the summarization for documents either manually or by software tools (e.g., IBM Intelligent Miner for Text [44]).

3. Create the dimensions and document indexes for constructing document cubes.

4. Archive documents and related data/metadata.

## 3.4. Back-end components

The back-end component performs all the operations responsible for the management of user queries. It is typically composed of a set of document access tools, a multi-dimensional document query interface [37], document warehouse monitoring tools, and customized tools.

## 3.5. Highly summarized documents

This part stores all the summarization derived from multiple documents, which belong to the same cluster or categorization. Some of such achievements have already been conducted [9,13].

The simplest format of a highly summarized document can be represented by a set of keywords appeared in the original document. Keywords of a document can be derived by computing the traditional tf\*idf weights [28,29], pivoted cosine weights [31], or one derived by any term-weighting scheme.

The proposed metadata design

<table><tr><td>Attribute name</td><td>Description</td></tr><tr><td>Title</td><td>A name given to the resource.</td></tr><tr><td>Creator</td><td>An entity primarily responsible for making the content of the resource.</td></tr><tr><td>Subject</td><td>A topic of the content of the resource.</td></tr><tr><td>Description</td><td>An account of the content of the resource.</td></tr><tr><td>Publisher</td><td>An entity responsible for making the resource available.</td></tr><tr><td>Contributor</td><td>An entity responsible for making contributions to the content of the resource.</td></tr><tr><td>Date</td><td>A date of an event in the lifecycle of the resource.</td></tr><tr><td>Type</td><td>The nature or genre of the content of the resource.</td></tr><tr><td>Format</td><td>The physical or digital manifestation of the resource.</td></tr><tr><td>Identifier</td><td>An unambiguous reference to the resource within a given context.</td></tr><tr><td>Source</td><td>A reference to a resource from which the present resource is derived.</td></tr><tr><td>Language</td><td>A language of the intellectual content of the resource.</td></tr><tr><td>Relation</td><td>A reference to a related resource.</td></tr><tr><td>Coverage</td><td>The extent or scope of the content of the resource.</td></tr><tr><td>Rights</td><td>Information about rights held in and over the resource.</td></tr><tr><td>...</td><td>...</td></tr><tr><td>Keywords</td><td>The keyword set derived from the resource.</td></tr><tr><td>Summarization</td><td>A brief summary generated from the resource by a summarization tool.</td></tr><tr><td>File_Path</td><td>A file pointer used to address the resource.</td></tr></table>

## 3.6. Metadata

The metadata of a document warehouse stores all the metadata derived from all documents. All the processes in the proposed architecture will use the metadata interchangeably. In the paper, we propose to design the metadata as Table 2 describes. That is, the metadata can be stored in a traditional relational table, which contains attributes for all the elements defined in the Dublin Core Metadata Element Set [38] and some additional attributes. For simplicity, we only list three extra attributes in Table 2, where <sup>d</sup>Summarization<sup>T</sup>, <sup>d</sup>Keywords<sup>T</sup>, and <sup>d</sup>File<sup>\_</sup>Path<sup>T</sup> are used to store the summarization of the document, the keyword set derived from the original document, and the file path used to show the pathway back to the document from which the metadata are derived. Such file path is inherently unique and can be used to describe the mapping between the document sources and a common view of the information within the document warehouse.

Some of the metadata can be obtained or derived directly from the document itself. For example, documents stored in Microsoft Word format has some summary information associated with the file itself and we can retrieve them directly from the stream by employing Structured Storage [39]. Structured Storage provides file and data persistence in COM by handling a single file as a structured collection of objects known as storages and streams.

## 4. Data modeling of document warehouses

The dimensional modeling technique [18,22] adopted widely in data warehouse modeling can be extended for document warehouses. Every dimensional model is composed of one central table with a composite key, called the fact table, which uses foreign keys to link to a set of dimension tables. This characteristic <sup>d</sup>star-like<sup>T</sup> structure is also called a star schema. Such multi-dimensional data model for text permits the definition of any dimension of interest as defined in Definition 2. In Fig. 7, we show a star schema for modeling document warehouses.

![](/api/attachments/H85Y8ND5/fulltext/images/19372c3e2ddcdd2f5ca46c34213b1d01c8fef97c23a8dafe456d67687c24e2f4.jpg)  
Fig. 7. An example star schema of a document warehouse.

## 4.1. Dimensions

As we have discussed in Section 2, dimensions can be distinguished into the following types:

1. Ordinary dimension. A document can be highly summarized by a set of keywords. Therefore, we can construct an ordinary dimension containing a set of keywords to allow users to pinpoint the desired documents directly.

2. Metadata dimension. That is, those elements defined in Dublin Core Metadata Element Set: title, creator, subject, description, publisher, contributor, date, type, format, identifier, source, language, relation, coverage, and rights, can all be regarded as metadata dimensions. Some of the dimensions might be hierarchies or simply related data.

3. Category dimension. For example, a hierarchy such as Wordnet or its subset, or user-defined hierarchies can be employed as category dimensions. Notice that, there may be more than one category dimensions used to construct a document cube, since a document can be multi-categorized into different categories from various points of view.

In Table 1, we have presented two representations for the dimension Region. Both representations can be easily obtained from each other by conversion. The structure of Table 1a is easier understood by people, and that of Table 1b is more efficient for computer processing. For dimensional modeling, we assume each dimension $D _ { i }$ is internally stored in the relation Di(Tag, Parent, Level, Keyword) conforming to the structure of Table 1b, such that the underlined attribute Tag represents the primary key, and Di.Parent is a foreign key and is referenced to Di.Tag. For example, the dimensions Product and Time in Fig. 4 can be represented as shown in Fig. 8.

Under such circumstances, for a dimension D, D(0) is the whole relation, and the other ith level member sets D(i) can be easily obtained by the SQL statements <sup>b</sup>SELECT Tag, Keyword FROM D WHERE Level = i<sup>Q</sup>, for 1 V i V n.

## 4.2. The fact table

In general, the central fact table may be composed of the following attributes:

1. A composite key, which is composed of a set of foreign keys to the following dimensions:

(a) Ordinary dimensions: For example, the dimension Keyword shown in Fig. 7 is an ordinary dimension.

<table><tr><td colspan="4">Product</td></tr><tr><td>Tag</td><td>Parent</td><td>Level</td><td>Keyword</td></tr><tr><td>1</td><td>1</td><td>1</td><td>(All Product)</td></tr><tr><td>2</td><td>1</td><td>2</td><td>Appliance</td></tr><tr><td>3</td><td>1</td><td>2</td><td>Communication</td></tr><tr><td>4</td><td>1</td><td>2</td><td>Computer</td></tr><tr><td>5</td><td>2</td><td>3</td><td>TV</td></tr><tr><td>6</td><td>2</td><td>3</td><td>Refrigerator</td></tr><tr><td>7</td><td>3</td><td>3</td><td>Cellular Phone</td></tr><tr><td>8</td><td>3</td><td>3</td><td>Radio</td></tr><tr><td>9</td><td>4</td><td>3</td><td>Monitor</td></tr><tr><td>10</td><td>4</td><td>3</td><td>Printer</td></tr></table>

<table><tr><td>Tag</td><td>Parent</td><td>Level</td><td>Keyword</td></tr><tr><td>1</td><td>1</td><td>1</td><td>(All Time)</td></tr><tr><td>2</td><td>1</td><td>2</td><td>2003</td></tr><tr><td>3</td><td>1</td><td>2</td><td>2004</td></tr><tr><td>4</td><td>2</td><td>3</td><td>Q1, 2003</td></tr><tr><td>5</td><td>2</td><td>3</td><td>Q2, 2003</td></tr><tr><td>6</td><td>2</td><td>3</td><td>Q3, 2003</td></tr><tr><td>7</td><td>2</td><td>3</td><td>Q4, 2003</td></tr><tr><td>8</td><td>3</td><td>3</td><td>Q1, 2004</td></tr><tr><td>9</td><td>3</td><td>3</td><td>Q2, 2004</td></tr><tr><td>10</td><td>3</td><td>3</td><td>Q3, 2004</td></tr><tr><td>11</td><td>3</td><td>3</td><td>Q4, 2004</td></tr></table>

Fig. 8. Dimensions product and time represented in relations.

(b) Metadata dimensions: For example, the dimensions Title, Date, Creator, . . . , and Rights as shown in Fig. 7 are metadata dimensions.

(c) Category dimensions. Notice that, there are no category dimensions shown in Fig. 7.

2. Attributes used to derive the measures in a document cube. The document count (i.e., the attribute count of fact table in Fig. 7) can be regarded as the default measure in a document cube. Another possible measure has been defined in Ref. [26] as the weight of the term frequency of the corresponding keyword.

3. A column Document<sup>\_</sup>ID represents the document identifier, which is a foreign key link to the relation S(Document<sup>\_</sup>id, File<sup>\_</sup>path) as shown in Fig. 7. That is, the set S in Fig. 7 can be regarded as a dimension containing all the document identifiers and the corresponding file paths, where Document<sup>\_</sup>id is the primary key and file<sup>\_</sup>path is used for storing the file path or URI of the documents.

Therefore, the fact table can be stored in the relation Fact<sup>\_</sup>Table(Document<sup>\_</sup>id, D1<sup>\_</sup>tag, D2<sup>\_</sup>Tag, . . . , Di<sup>\_</sup>Tag, . . . , Dn<sup>\_</sup>Tag, Count), where Docmen-$t \_ i d$ is a foreign key which is referenced to S.Docment<sup>\_</sup>id, and each Di<sup>\_</sup>Tag is a foreign key matching the primary key $D _ { i }$ Tag of dimension $D _ { i }$ . For each document T (with identifier $i d _ { T } )$ in $S ,$ the document index ${ x = } ( i d _ { T } , K _ { T } )$ , where $K _ { T } { = } ( K _ { 1 } , K _ { 2 } , \ldots , K _ { i } , \ldots ,$ $K _ { n } )$ , can be used to generate $\{ i d _ { T } \} \times \left( \times _ { 1 \leq i \leq n } K _ { i } \right)$ as the set of initial tuples in the Fact<sup>\_</sup>Table.

Note that the initial tuples generated by the above process may cause redundancies. We formulate this by the following definition.

Definition 11. A document index defined on n dimensions $( D _ { 1 } , D _ { 2 } , \dots , D _ { n } ) , x = ( i d _ { T } , K _ { T } )$ , where $K _ { T } { = } ( K _ { 1 } ,$ $K _ { 2 } , \ldots , K _ { i } , \ldots , K _ { n } )$ is minimal, if and only if for two keywords $k _ { x }$ and $k _ { y } \in K _ { i } , k _ { x } \neq k _ { y }$ , there is no ancestry relationship between $k _ { x }$ and $k _ { y }$ in $D _ { i } ,$ for all $1 \leq i \leq n$ That is, k<sub>x</sub> is not an ancestor of $k _ { y }$ in $D _ { i } ,$ , and vice versa.

For a non-minimal document index $x { = } ( i d _ { T } , K _ { T } ) .$ 4 where $K _ { T } { = } ( K _ { 1 } , K _ { 2 } , \ldots , K _ { i } , \ldots , K _ { n } )$ , we can always reduce x into a minimal document index, denoted x˙ , by iteratively finding pairs of keywords $k _ { x }$ and $k _ { \nu }$ in $K _ { i } ,$ for all $1 \leq i \leq n$ , such that $k _ { y }$ is a descendant of $k _ { x } ,$ , and then eliminating the ancestor $k _ { x }$ and retaining the descendant $k _ { y } .$ . Such process can be denoted as x<sup>i</sup> x˙. It helps to reduce the storage cost of a document index without loss of indexing information, since the documents indexed by an ancestor can be recursively derived by rolling up the indexed documents from its lowest descendants along the corresponding dimension.

Example 3. Suppose there is a non-minimal document index of T (with unique identifier A001), defined on dimensions (R,P), x = (A0001, ({South, Kaohsiung}, {TV})), then after x<sup>i</sup> x˙, we obtain $\scriptstyle { \dot { \boldsymbol { x } } } = ( \operatorname { A 0 0 0 1 }$ ({Kaohsiung}, {TV})), since, according to the dimension R, the documents indexed by South can be derived from Tainan, Kaohsiung, and Pingtong.

## 4.3. The construction of document cubes

To construct a document cube, the process is somehow different from that in data cubes. Although a document index derived according to metadata and category dimensions are the same as that in data cubes, the process to generate a document index with respect to an ordinary dimension is prone to be time-consuming. This is because computing a measure in a data cube is just numerical computation. However, to compute a document index (defined in Definition 6), we have to scan the document content to match the keywords in any ordinary dimension. Therefore, it is necessary to develop another indexing structure to accommodate the document indices derived from ordinary dimensions. We have already proposed an indexing structure, called D-tree, to meet this objective in Refs. [35,36], where the performance evaluation of the indexing structure was also studied.

## 5. Applications of document warehouses

In this section, we present two applications of document warehouses. The first one is a document warehouse for organizing the complaint e-mails to provide better customer relationship management. The other one is for preparing a document warehouse indexing a set of journal papers falling in different categories, published in different journals on different date times.

## 5.1. An application for customer relationship management

Suppose there is a company manufacturing appliances, communication equipments and computer peripherals, and it has established branches in the north and south regions. The objective is to warehouse customer complaint e-mails for customer relationship management.

After modeling the document cube, we obtain two metadata dimensions (Creator and Date) and three ordinary dimensions (Region, Product, and Time) as shown in Fig. 9.

We briefly describe these dimensions as follows:

1. Ordinary dimension. The dimensions Region and Product are as shown in Figs. 2 and 10, respectively. The dimension Time is the purchase time described in the e-mail.

2. Metadata dimension. The dimension Creator stores the e-mail addresses of customers and dimension Date stores the date of receiving of e-mails.

3. Category dimension. There are no category dimensions shown in this example. However, the e-mail documents could be further categorized either manually or automatically by software tools into hierarchical categories.

The fact table is composed of the following attributes:

1. A composite key, which is composed of a set of foreign keys to the aforementioned dimensions.

2. The attribute count is regarded as the default measure in this document cube.

3. A column Document<sup>\_</sup>ID served as a foreign key and is referenced to the relation S(Document<sup>\_</sup>ID, file<sup>\_</sup>path).

![](/api/attachments/H85Y8ND5/fulltext/images/ecf9d0159aa7072dbf90cf3f97d62749802130126c3d117c9cc573a565776a22.jpg)  
Fig. 9. An example star schema for complaint e-mail management.

![](/api/attachments/H85Y8ND5/fulltext/images/de500d3abad5a879c8d4d0b25c639a006aefb32c4436b5241f4ae8ef48746293.jpg)  
Fig. 10. A concise illustration of dimension P.

After constructing the document cube, we can perform on-line analytical processing on the obtained document cube as illustrated in Fig. 11. Notice that, each of the count shown in Fig. 11 is actually a hyperlink, which links to a page containing the original e-mails.

## 5.2. An application for journal paper warehousing

Suppose there is a university laboratory, which intends to warehouse research journal papers according to some predefined categories.

After modeling the document cube, we establish one category dimension Category and two metadata dimensions: Source and Times, as shown in Fig. 12, where Category represents the predefined categories, Source stores the journal names of the selected papers, and Times regards the publishing data times.

We briefly describe these dimensions as follows:

1. Ordinary dimension. There is no ordinary dimension in this example. However, users may add a dimension containing all of the keywords in the selected journal papers, and organize the keywords into hierarchies, either manually or automatically by some text processing tools.

2. Metadata dimension. The dimension Source stores the journal names, which are published under some communities (e.g., ACM, IEEE, Elsevier, and Kluwer). The dimension Times stores the date of publishing, which is organized according to the Year–Month hierarchy.

3. Category dimension. The dimension Category stores the predefined categories, i.e., computeraided engineering, data mining and knowledge discovery, data model, data structures, data warehousing, database management, . . ., and so forth. These predefined categories are all organized into the same level to simplify the illustration. Notice that all papers are multi-categorized into theses categories. That is, a paper may fall into two or more categories.

The fact table is composed of the following attributes:

1. A composite key, which is composed of a set of foreign keys to the aforementioned dimensions.

2. The attribute count is regarded as the default measure in this document cube.

3. A column Document<sup>\_</sup>ID served as a foreign key and is referenced to the relation S(Document<sup>\_</sup>ID, file<sup>\_</sup>path).

<table><tr><td colspan="2">2004/Quarter 1</td><td colspan="2">Region</td></tr><tr><td colspan="2">Product</td><td>North</td><td>South</td></tr><tr><td rowspan="3">Appliance</td><td>TV</td><td>5</td><td>2</td></tr><tr><td>Refrigerator</td><td>3</td><td>7</td></tr><tr><td>DVD Player</td><td>7</td><td>9</td></tr><tr><td rowspan="2">Computer</td><td>Laptop Computer</td><td>8</td><td>1</td></tr><tr><td>Desktop Computer</td><td>2</td><td>3</td></tr><tr><td rowspan="2">Communication</td><td>Radio</td><td>6</td><td>1</td></tr><tr><td>Cellular Phone</td><td>5</td><td>7</td></tr></table>

Fig. 11. On-line analytical processing over the example document cube.

![](/api/attachments/H85Y8ND5/fulltext/images/9b441dc25f7a23531b7fc8edbb0c70cc9d40a01527d2467f23cfb7e1a1017510.jpg)  
Fig. 12. An example star schema for journal paper warehousing.

<table><tr><td colspan="17">Column Axes: Row Axes: Last Times Selected: 2004</td></tr><tr><td>Source</td><td colspan="2">Category</td><td colspan="14">(All Times)</td></tr><tr><td>Submit Query</td><td colspan="16">Reset</td></tr><tr><td></td><td>All Source</td><td>ACM</td><td>ACM Transactions on Database Systems</td><td>ACM Transactions on Design Automation of Electronic Systems</td><td>Elsevier</td><td>Data and Knowledge Engineering</td><td>Decision Support Systems</td><td>Expert Systems with Applications</td><td>Information Sciences</td><td>IEEE</td><td>IEEE Transactions on Knowledge and Data Engineering</td><td>IEEE Transactions on Parallel and Distributed Systems</td><td>Kluwer</td><td>Data Mining and Knowledge Discovery</td><td>Distributed and Parallel Databases</td><td>Information Retrieval</td></tr><tr><td>All Category</td><td>53</td><td>1</td><td></td><td>1</td><td>33</td><td>21</td><td>8</td><td>3</td><td>1</td><td>8</td><td>8</td><td></td><td>11</td><td></td><td>2</td><td>4</td></tr><tr><td>Computer-Aided Engineering</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Data Mining and Knowledge Discovery</td><td>16</td><td></td><td></td><td></td><td>6</td><td>1</td><td>3</td><td>1</td><td>1</td><td>5</td><td>5</td><td></td><td>5</td><td></td><td></td><td></td></tr><tr><td>Data Model</td><td>3</td><td></td><td></td><td></td><td>3</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Data Structure</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Data Warehousing</td><td>4</td><td></td><td></td><td></td><td>4</td><td>1</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Database Management</td><td>7</td><td></td><td></td><td></td><td>3</td><td>2</td><td></td><td></td><td>1</td><td>3</td><td>3</td><td></td><td>1</td><td></td><td>1</td><td></td></tr><tr><td>Discrete Mathematics</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Distributed Computing</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2</td><td></td><td>1</td><td>1</td></tr><tr><td>Heterogeneous Data Integration</td><td>3</td><td></td><td></td><td></td><td>3</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Information Retrieval</td><td>10</td><td></td><td></td><td></td><td>6</td><td>4</td><td>1</td><td>1</td><td></td><td>2</td><td>2</td><td></td><td>2</td><td></td><td></td><td>2</td></tr><tr><td>Integrated Circuits</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Knowledge Management</td><td>8</td><td></td><td></td><td></td><td>7</td><td>5</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>Logic Design</td><td>1</td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Machine Learning</td><td>4</td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td>2</td><td></td><td></td><td>1</td></tr><tr><td>Metadata Management</td><td>3</td><td></td><td></td><td></td><td>3</td><td>2</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Natural Language Processing</td><td>4</td><td></td><td></td><td></td><td>3</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>Object-Oriented Technology</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td></td></tr><tr><td>Operating Systems</td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Performance and Reliability</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Programming Language</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Workflow Management</td><td>4</td><td></td><td></td><td></td><td>3</td><td>2</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td></td></tr><tr><td>XML and Web Technology</td><td>13</td><td></td><td></td><td></td><td>10</td><td>8</td><td>1</td><td>1</td><td></td><td>2</td><td>2</td><td></td><td>1</td><td></td><td></td><td>1</td></tr></table>

Fig. 13. On-line analytical processing over the example document cube.

To prove the concept proposed in this paper, we have implemented this example to allow users to perform on-line analytical processing on the obtained document cube as illustrated in Fig. 13. The dimension Times is used for slicing the document cube. Notice that, each of the count shown in Fig. 13 is actually a hyperlink, which links to a Web page containing the detailed paper listing as shown in Fig. 14 (when slicing the Times dimension by <sup>d</sup>2004<sup>T</sup> and clicking the count intersected by <sup>d</sup>Elsevier<sup>T</sup> and <sup>d</sup>Data Mining and Knowledge Discovery<sup>T</sup>). If all of the paper files were stored in the publisher’s Web sites for a long time period, then this document warehouse does not need to copy and store the physical files locally. That is, such a document warehouse effectively saves storage space and provides very fast document access without degradation in performance even as the size of the warehouse grows.

## 6. Conclusion and future directions

## 6.1. Conclusion

While data warehouses and the numeric-centric business intelligence technologies have served most of the enterprises well, they do not fully address the complete scope of business intelligence. In this paper, we advocate the importance of constructing document warehouses to support text-centric business intelligence, and propose an architecture for document warehousing. When documents are warehoused, users can perform ad hoc on-line analytical processing (OLAP) over text in a document warehouse, just as the way users can perform OLAP over summarized data in a data warehouse.

The concept of document warehousing is not only providing the ability to very fast document access without degradation in performance even as the size of the warehouse grows, but also offering a set of versatile applications for content management of enterprise business intelligence. In business, document warehousing can help administrators organize meeting reports, gazettes, or even customer complaint e-mails, where the company personnel, products, and time may be regarded as the dimensions, such that documents related to some employees, or products in some time, at somewhere can be retrieved or browsed instantly. In recent years, we have seen most data warehouse applications applied in Customer Relationship Management (CRM), a promising trend in business affairs. However, a data warehouse creation only supports the numeric analyses of customer behaviors. To obtain the reason why customers buy (or did not buy) some products, we need to establish a document warehouse. By data warehousing, users can realize business phenomena regarding who, what, when, where, and which clearly. Nevertheless, to discover why the phenomena occurred, a document warehouse should be employed [33].

The pinpointed papers in DC are from Source Journal: Elsevier published on : 2004 fall in Category: Data Mining and Knowledge Discovery

<table><tr><td>Doc_id</td><td>File Path</td><td>from Source</td><td>Published on</td><td>in Category</td></tr><tr><td rowspan="2">15</td><td rowspan="2">Clustering classifiers for knowledge discovery.pdf</td><td rowspan="2">Data and Knowledge Engineering</td><td rowspan="2">Jun. 2004</td><td>Data Mining and Knowledge Discovery</td></tr><tr><td>Machine Learning</td></tr><tr><td rowspan="2">43</td><td rowspan="2">A causal mapping approach to constructing Bayesian networks.pdf</td><td rowspan="2">Decision Support Systems</td><td rowspan="2">Nov. 2004</td><td>Data Mining and Knowledge Discovery</td></tr><tr><td>Knowledge Management</td></tr><tr><td rowspan="2">52</td><td rowspan="2">Critical factors influencing the adoption of data warehouse technology a study of the banking industry in Taiwan.pdf</td><td rowspan="2">Decision Support Systems</td><td rowspan="2">Apr. 2004</td><td>Data Mining and Knowledge Discovery</td></tr><tr><td>Data Warehousing</td></tr><tr><td>53</td><td>Data mining of Bayesian networks using cooperative coevolution.pdf</td><td>Decision Support Systems</td><td>Dec. 2004</td><td>Data Mining and Knowledge Discovery</td></tr><tr><td>71</td><td>Mining class outliers concepts algorithms and applications in CRM.pdf</td><td>Expert Systems with Applications</td><td>Dec. 2004</td><td>Data Mining and Knowledge Discovery</td></tr><tr><td rowspan="2">72</td><td rowspan="2">Algorithms for mining association rules in bag databases.pdf</td><td rowspan="2">Information Sciences</td><td rowspan="2">Oct. 2004</td><td>Data Mining and Knowledge Discovery</td></tr><tr><td>Database Management</td></tr></table>

Fig. 14. The detailed paper listing after the count in the intersection of <sup>d</sup>Elsevier<sup>T</sup> and <sup>d</sup>Data Mining and Knowledge Discovery<sup>T</sup> was clicked.

When documents are warehoused, the task of version control will become very easy, since users can directly trace the documents based on some criteria along the time dimension. Such merits also make document warehousing an exhilarating organization for on-line topic detecting and event tracking [1] of news. Besides, document clustering can be achieved directly via visualizations. Users can also develop some document summarization tools [9,16,30] to summarize a cluster of related documents. To sum up, data warehousing and document warehousing are not only one of the most important infrastructures of knowledge management, but also the kernel of customer relationship management. Both are used for respectively organizing documents and formatted data in a multi-dimensional basis. We compare their similarities and differences in Table 3.

## 6.2. Future works

In our future work, we will conduct more techniques for document warehousing. The preliminary components may include the following modules.

1. Employ XML Schema [43] to define document metadata. We advocate using the Extensible Markup Language (XML) to be the intermediate media for document interchange.

2. Incorporate automatic text summarization [12,14, 23], key feature extraction [10], or even document classification and categorization [3] techniques for document warehousing. Develop related text summarization techniques to extract the most important 10\~20% content for users to digest the documents more easily and propose how to bind a document summary with its corresponding documents for document warehousing.

3. Automatic document metadata decomposition and the mechanisms for storing the obtained metadata into native XML or XML-enabled databases [5–7]. This helps users manage document warehouses more efficiently.

Table 3  
A comparison between document warehousing and data warehousing

<table><tr><td></td><td>Document warehousing</td><td>Data warehousing</td></tr><tr><td>Similarities</td><td>1. Both have the same construction process.We may employ star schema or snowflake [22] to design the modeling process.2. Both gather business document/data from heterogeneous resources.3. Users can do on-line analytical processing over the established result.</td><td></td></tr><tr><td>Differences</td><td>1. Intend to obtain text-oriented business intelligence.2. Resources gathered from market survey reports, project status reports, meeting records, customer complaints, e-mails, patent application sheets, and advertisements of competitors.3. It filters out unnecessary documents and intends to help users to address problems regarding why.4. Enriched with text mining techniques to summarize documents or categorize documents.5. Document sources should be integrated in file systems, or native XML databases [6,7].</td><td>1. Intend to obtain numeric-oriented business intelligence.2. Resources gathered from internal databases of POS (point-of-sale) systems, ERP (enterprise resource planning) systems, accounting systems, or financial management systems.3. It aggregates numerical data according to various dimensions, and intends to help users to address problems regarding who, what, when, where, and which.4. Enriched with data mining techniques to summarize, classify, cluster formatted data or find the associations.5. Data sources can be integrated in relational databases.</td></tr></table>

Besides, although the dimension concepts defined in this paper are organized into hierarchical structures, it is however assumed that when scanning a document, the system will ignore the hierarchical relationships among keywords in the document. Based on this work, we wish to incorporate some natural language processing technologies to enhance the linguistic analysis and annotation results of document parsing, and elaborate the work of adopting domain-specific ontology [8,11,25,32] with more refined concepts to be built in the corresponding dimensions of a document cube. Ontological analysis can help clarify the structure of knowledge regarding a set of related documents. Given a set of related documents corresponding to a specific domain, the ontology forms the semantic heart of any system of knowledge representation, and their document cube forms the syntactic centroid of any system of concept organization.

Finally, since the construction of a document warehouse has to scan a large amount of documents, which is a task prone to time-consumption, the parallel architecture for such a process will be investigated further in the future.

## References

[1] J. Allan, R. Pepka, V. Lavrenko, On-line new event detection and tracking, Proceedings of the 21st Annual International ACM SIGIR Conference on Research, 1998, pp. 37–45.

[2] S. Anahory, D. Murray, Data Warehousing in the Real World: A Practical Guide for Building Decision Support Systems, Addison-Wesley Longman, Harlow, England, 1997.

[3] A. Appiani, F. Cesarini, A. Colla, M. Diligenti, M. Gori, S. Marinai, G. Soda, Automatic document classification and indexing in high-volume applications, International Journal on Document Analysis and Recognition 4 (2) (2002) 69– 83.

[4] M.J.A. Berry, G. Linoff, Data Mining Techniques: For Marketing, Sales, and Customer Support, John Wiley & Sons, New York, 1997.

[5] E. Bertino, B. Catania, Integrating XML and databases, IEEE Internet Computing 5 (4) (2001) 84 – 88.

[6] E. Bertino, E. Ferrari, XML and database integration, IEEE Internet Computing 5 (6) (2001) 75 – 76.

[7] Champion, M, Native XML vs. XML-Enabled: the Difference Makes a Difference, http://www.softwareag.com/xml/library/ champion<sup>\_</sup>nativexml.htm, Software AG: The XML Company.

[8] B. Chandrasekaran, J.R. Josephson, V.R. Benjamins, What are ontologies, and why do we need them? IEEE Intelligent Systems 14 (1) (1999 Jan./Feb.) 20– 26.

[9] H.H. Chen, S.J. Huang, A summarization system for Chinese news from multiple sources, Proceedings of the 4th Interna-

tional Workshop on Information Retrieval with Asia Language, 1999, pp. 1 – 7.

[10] F.F. Feng, W.B. Croft, Probabilistic techniques for phrase extraction, Information Processing & Management 37 (2) (2001 Mar.) 199 – 220.

[11] N. Fridman, C.D. Hafner, The state of the art in ontology design, AI Magazine 18 (3) (1997) 53 – 74.

[12] J. Goldstein, M. Kantrowitz, V. Mittal, J. Carbonell, Summarizing text documents: sentence selection and evaluation metrics, Proceedings of SIGIR, 1999, pp. 121 – 128.

[13] J. Goldstein, V.O. Mittal, J.G. Carbonell, J.P. Callan, Creating and evaluating multi-document sentence extract summaries, Proceedings of the 9th International Conference on Information and Knowledge Management, 2000, pp. 165 – 172.

[14] Grigsby, M., The Internet Document Warehouse: Content Management for the Back Office, Technical Report, IMERGE Consulting, Inc., 2001. http://www.imergeportal. com/publishedarticles.asp.

[15] R. Hackathorn, Data warehousing energizes your enterprise, Datamation 1 (1995 Feb.) 38– 42.

[16] U. Hahn, I. Mani, The challenges of automatic summarization, IEEE Computer 33 (11) (2000 Nov.) 29 – 36.

[17] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Morgan Kaufmann Publishers, 2001.

[18] W.H. Inmon, Building the Data Warehouse, John Wiley and Sons, New York, NY, 1993.

[19] H. Ishikawa, K. Kubota, Y. Noguchi, K. Kato, M. Ono, N. Yoshizawa, A. Kanaya, A document warehouse: a multimedia database approach, Proceedings of the IEEE 9th International Workshop on Database and Expert Systems Applications (DEXA’98) Vienna, Austria, Aug. 26–28, 1998, pp. 90 – 94.

[20] H. Ishikawa, K. Kubota, Y. Noguchi, K. Kato, M. Ono, N. Yoshizawa, Y. Kanemasa, Document warehousing based on a multimedia database system, IEEE International Conference on Data Engineering, 1999, pp. 168 – 173.

[21] H. Ishikawa, M. Ohta, K. Kato, Document warehousing: a document-intensive application of a multimedia database, Proceedings of the IEEE 11th International Workshop on Research Issues in Data Engineering, Heidelberg, Germany, April 01–02, 2001, pp. 25 – 31.

[22] R. Kimball, The Data Warehouse Toolkit: Practical Techniques for Building Dimensional Data Warehouses, John Wiley & Sons, Inc., 1996.

[23] K. Knight, Mining online text, Communications of the ACM 42 (11) (1999).

[24] S.-H. Lin, C.-S. Shih, M.C. Chen, J.-M. Ho, M.-T. Ko, Y.-M. Huang, Extracting classification knowledge of Internet documents with mining term associations: a semantic approach, Proceedings of ACM SIGIR Conference on Research and Development in Information Retrieval, 1998, pp. 241– 249.

[25] S. Loh, L.K. Wives, J.P. de Oliverira, Concept-based knowledge discovery in texts extracted from the web, SIGKDD Explorations 2 (1) (2000 Jun.)1998.

[26] M.C. McCabe, J. Lee, A. Chowdhury, D. Grossman, O. Frieder, On the design and evaluation of a multi-dimensional approach to information retrieval, Proceedings of the 23th Annual International ACM SIGIR Conference, 2000, pp. 363–365.

[27] G.A. Miller, Wordnet: an online lexical database, International Journal of Lexicography 3 (4) (1990) 235 – 312.

[28] G. Salton, Automatic Text Processing, Addison-Wesley Publishing Company, 1988.

[29] G. Salton, M. Gill, Introduction to Modern Information Retrieval, McGraw-Hill, 1983.

[30] S. Sekine, C. Nobata, A Survey of Multi-Document Summarization, Proceedings HLT-NAACL Text Summarization Workshop and Document Understanding Conference (DUC 2003), pp. 65–72.

[31] A. Singhal, C. Buckley, M. Mitra, Pivoted document length normalization, Procedings of the 19th Annual International ACM SIGIR Conference, 1996, pp. 21 – 29.

[32] V. Sugumaran, V.C. Storey, Ontologies for conceptual modeling: their creation, use, and management, Data and Knowledge Engineering 42 (2002) 251 – 271.

[33] D. Sullivan, Document Warehousing and Text Mining: Techniques for Improving Business Operations, Marketing and Sales, John Wiley & Sons, Inc., 2001.

[34] Ah-Hwee Tan, Text mining: the state of the art and the challenges, Proceedings of the PAKDD 99—Workshop on Knowledge Discovery from Advanced Databases, Beijing, 1999, pp. 50–70.

[35] F.S.C. Tseng, W.P. Lin, A study on indexing structure and its properties for constructing document warehouses, Proceedings of the 20th Workshop on Combinatorial Mathematics and Computation Theory, Taiwan, 2003 (Aug.), pp. 18 – 27.

[36] F.S.C. Tseng, W.P. Lin, D-Tree: A Multi-Dimensional Indexing Structure for Constructing Document Warehouses, Journal of Information Science and Engineering, in press.

[37] F.S.C. Tseng, Design of a Multi-Dimensional Query Expression for Document Warehouses, Information Sciences, accepted and in press.

[38] http://dublincore.org/, Dublin Core Metadata Initiative.

[39] http://msdn.microsoft.com/library/default.asp?url=/library/en-us/ stg/stg/structured<sup>\_</sup>storage<sup>\_</sup>start<sup>\_</sup>page.asp, Structured Storage.

[40] http:otn.oracle.com/products/text/x/tech<sup>\_</sup>Overviews/imt<sup>\_</sup>817. html, Oracle Corporation. InterMedia Text 8.1.6.

[41] http://www.globalwordnet.org, The Global Wordnet Association.

[42] http://www.survey.com, <sup>b</sup>Development Snapshot: Warehouse Data of the Future,<sup>Q</sup> Application Development Trends, Feb. 2000.

[43] http://www.w3.org/XML/schema.

[44] http://www-3.ibm.com/software/data/iminer/fortext, IBM Intelligent Miner for Text: Text Analysis Tools version 2.10.0.

Frank S.C. Tseng received his B.S., M.S. and Ph.D. degrees, all in computer science and information engineering from National Chiao Tung University, Taiwan, ROC, in 1986, 1988, and 1992, respectively. He is one of the winners of Acer Long Term Ph.D. dissertation prize in 1992. From 1993 to 1995, he served the military in the General Headquarters of ROC Air Force. He joined the faculty of the Department of Information Management, Yuan-Ze University, Taiwan, ROC, on August 1995. From 1996 to 1997, he was the chairman of the department. He is currently with the Department of Information Management, National Kaohsiung First University of Science and Technology, as an associate professor. His research interests include heterogeneous database systems, XML technologies for Internet computing, data warehousing, data mining, and document warehousing. He has published extensively in journals such as the VLDB Journal, IEEE Transactions on Knowledge and Data Engineering, Data and Knowledge Engineering, Journal of Systems and Software, Distributed and Parallel Databases: An International Journal, Journal of Information Science, Information Sciences, and Journal of Information Science and Engineering. Dr. Tseng is a member of the IEEE Computer Society and the Association for Computing Machinery. He was listed in Marquis Who’s Who in Medicine and Healthcare in May 2004.

Annie Y.H. Chou received her B.S. degree in applied mathematics, M.S. degree in computer science and information engineering, and Ph.D degree in computer and information science, all from National Chiao Tung University, Taiwan, ROC, in 1987, 1989, and 1996, respectively. From 1989 to 1992, she was an assistant researcher of Chunghua Telecom Laboratories, Taiwan, ROC. She joined the faculty of the Department of Computer and Information Science, Chinese Military Academy, in August 1997. She is presently the chairman of the department. Her research interests include mathematical analysis of computer algorithms, file organization design, data warehousing and data mining, and internet computing. She was a member of the Phi Tau Phi Scholastic Honor Society. Dr. Chou has had papers published in the Computer Journal and Journal of Information Science and Engineering.
