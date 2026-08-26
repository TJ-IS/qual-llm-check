---
otero_id: 14484
otero_key: "6B8QF5C7"
title: "Managing knowledge on the Web – Extracting ontology from HTML Web"
authors: "Timon C. Du; Feng Li; Irwin King"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.02.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Managing knowledge on the Web – Extracting ontology from HTML Web

Timon C. Du <sup>a,</sup>⁎, Feng Li <sup>b</sup>, Irwin King <sup>c</sup>

<sup>a</sup> Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong, Hong Kong

<sup>b</sup> School of Business Administration, South China University of Technology, China

<sup>c</sup> Department of Computer Science and Engineering, The Chinese University of Hong Kong, Hong Kong

## a r t i c l e i n f o

Article history: Received 20 May 2008 Received in revised form 9 February 2009 Accepted 18 February 2009 Available online 9 March 2009

Keywords: Ontology Semantic Web Knowledge management applications Intelligent Web services

## a b s t r a c t

In recent years, the Internet has become one of the most important sources of information, and it is now imperative that companies are able to collect, retrieve, process, and manage information from the Web. However, due to the sheer amount of information available, browsing web content by searches using keywords is inef<sup>fi</sup>cient, largely because unstructured HTML web pages are written for human comprehension and not for direct machine processing. For the same reason, the degree of web automation is limited. It is recognized that semantics can enhance web automation, but it will take an inde<sup>fi</sup>nite amount of effort to convert the current HTML Web into the Semantic Web. This study proposes a novel ontology extractor, called OntoSpider, for extracting ontology from the HTML Web. The contribution of this work is the design and implementation of a six-phase process that includes the preparation, transformation, clustering, recognition, re<sup>fi</sup>nement, and revision for extracting ontology from unstructured HTML pages. The extracted ontology provides structured and relevant information for applications such as e-commerce and knowledge management that can be compared and analyzed more effectively. We give detailed information on the system and provide a series of experimental results that validate the system design and illustrate the effectiveness of OntoSpider.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Managing knowledge on the World Wide Web has become an important issue given the large volume of information that is now available on the Internet. However, the management of this knowledge is a dif<sup>fi</sup>cult task both because of the dynamic nature of the Internet. Many solutions have been proposed to solve this problem. One approach is to develop a system to automate the knowledge management process [24], but there is no clear method of applying such a system due to dif<sup>fi</sup>culties with the storage, capture, retrieval, and distribution of knowledge [2,11,12]. Fortunately, a better solution exists in the use of ontology that de<sup>fi</sup>nes terms and the relationships between them to enhance the machine-understandability of online content [21]. However, constructing ontology manually is a very time consuming and error prone task, and thus the development of a method to extract ontology automatically from current Web resources such as HyperText Markup Language (HTML) documents is an attractive prospect.

Currently, most Web content is written in HTML, which follows a rigid format in displaying content because web pages for the syntaxbased HTML Web are written for human comprehension. As the volume of information on the Web grows, the time needed to locate and digest information increases tremendously. Thus, when a user types keywords into a conventional search engine, the volume of search results is often too large to locate useful information, and the situation may be even worse if the keyword search does not provide highly relevant results.

Compared with the HTML Web, the knowledge contained in ontology is relatively easier to extract by analyzing the schema <sup>fi</sup>les in the structure of web documents. For example, Delteil et al. [17] built ontology from RDF annotations by systematically generating the most speci<sup>fi</sup>c generalization of all of the possible sets of resources. Similarly, Sabou et al. [40] created ontology from the OWL-S <sup>fi</sup>le for use in describing a Web service and Segev and Gal [41] used the relationships between ontologies and contexts for multilingual information system.

This study proposes an extractor that acquires ontology from HTML websites. The extractor adopts a six-phase process that includes preparation, transformation, clustering, recognition, re<sup>fi</sup>nement, and revision. The process is semi-automatic, and relies on the involvement of an ontology engineer. The extractor fetches and annotates web pages from remote websites; removes the trivial parts, hyperlinks, and segments from the pages; clusters and identi<sup>fi</sup>es concept instances in the content; extracts concepts from the concept instances; and manages the ontology base. In the system design, the ontology engineer is responsible for managing the ontology, determining the threshold values and weights, and conducting revisions for concept construction. The extracted knowledge can be applied in many problem domains, such as identifying potential buyers and sellers or determining negotiation strategies in bargaining.

The remainder of this paper is organized as follows. Section 2 gives an overview of related work on ontology extraction and Web resources. Section 3 presents the model in detail and Section 4 demonstrates the prototype. Conclusions and suggestions for future work are provided in Section 5.

## 2. Ontology extraction

Ontology engineering involves various tasks, such as editing, evolving, and versioning, mapping, alignment, merging, and reusing, and extraction. Editing tasks provide an editor for the manual composition of ontology [5], whereas evolution uses a management system to modify ontology to preserve its consistency [37]. Versioning involves the creation of a system to handle changes in different versions of ontology. Assigning the symbols used in one vocabulary to another and establishing a collection of binary relationships between the vocabularies of two ontology sets are the work of mapping [29,30] and alignment [38], respectively. Merging refers to the creation of a single ontology from two or more sources [36], and reusing is the sharing and reusing of representational components built by others [8]. Learning involves extracting ontological elements from an input and building ontology from them. Finally, extraction aims to construct a sharable ontology in a (semi-) automatic fashion [23,42].

Extraction may involve linguistic techniques, statistical techniques, machine learning, and hybrid techniques, depending on the information retrieval technology used. Linguistic techniques encompass methods that are rooted in the understanding of natural language, such as the use of syntactic analysis or linguistic patterns to recognize the relationship between terms. For example, ASIUM uses syntactic analysis to extract syntactic frames from text [20], and Hasti uses a small ontology kernel to exploit the morph-syntactic and semantic analysis of input texts to extract lexical and ontological knowledge from Persian texts [43].

Statistical techniques extract new concepts or the relationships between concepts by calculating several statistical measures. These measures are based on the assumptions that frequent terms in a domain-speci<sup>fi</sup>c corpus are important concepts in that domain, and that the frequent co-occurrence of terms in a domain-speci<sup>fi</sup>c corpus indicates that there is a relevant relationship among them. This kind of co-occurrence is also called “collocation,” and refers to the occurrence of two or more words within a well-de<sup>fi</sup>ned unit of information (for example, a sentence or document) [27,32]. An example of such a statistical technique is the attempt to catch term–term statistical references by using singular value decomposition, which is a method of matrix decomposition [33]. Similarly, Text-To-Onto [34] and CRCTOL [28] use the frequency of word co-occurrences to detect non-taxonomic relationships.

The machine-learning approach offers a set of techniques and algorithms for acquiring knowledge in an automated way. These techniques are usually adopted together with either linguistic or statistical techniques or both. Pattern- or template-matching is also widely used. Templates are usually syntactic or semantic, and have general or speci<sup>fi</sup>c purposes that indicate a certain kind of relationship. These templates are usually provided by users or are extracted from samples by using linguistic or statistical techniques. For example, Kietz et al. assumed that most of the concepts and conceptual structures of a domain should be included in ontology, whereas the terminologies of the domain should be described in documents [31]. OntoLearn constructs and enriches ontologies by using machinelearning techniques, using WordNet and domain websites to build core domain ontology by pruning all of the non-domain or nonterminological candidate terms.

Table 1 summarizes the various approaches to ontology extraction. Auxiliary web resources are usually the main constituents of an ontology, which an ontology engineer then enriches with various domain-speci<sup>fi</sup>c sources. Most of the existing approaches enrich the “seed” or “core” ontology with these web resources. For example, WEB-KB developed ontology by using three independent classi<sup>fi</sup>ers that differentiate representations for page classi<sup>fi</sup>cation, namely, the words that occur in the title and HTML headings of a page, words from other pages that occur in hyperlinks that point to the page, and words that occur anywhere else on the page [13]. Text-To-Onto and OntoLearn classify unstructured web resources [34] and Agirre constructed signatures (word sense disambiguation) for each concept in WordNet by exploiting web content via a search engine (AltaVista, http://www.altavista.com/) [1]. Faatz and Steinmetz enriched an existing ontology by querying the World Wide Web via Google [19].

Table 1  
Summary of related work.

<table><tr><td>Name</td><td>Method</td><td>Language</td><td>Auxiliary source</td></tr><tr><td>Agirre et al. [1]</td><td>Statistical</td><td>Unstructured</td><td>Ontology</td></tr><tr><td>Arasu and Garcia-Molina [3]</td><td>Machine learning</td><td>Semi-structured</td><td>None</td></tr><tr><td>Buttler et al. [10]</td><td>Machine learning</td><td>Semi-structured</td><td>None</td></tr><tr><td>Craven et al. [13]</td><td>Joint method</td><td>Semi-structured</td><td>Both</td></tr><tr><td>Crescenzi et al. [14]</td><td>Machine learning</td><td>Semi-structured</td><td>None</td></tr><tr><td>Davulcu et al. [16]</td><td>Machine learning</td><td>Semi-structured</td><td>Samples</td></tr><tr><td>Faatz and Steinmetz [19]</td><td>Statistical</td><td>Unstructured</td><td>Ontology</td></tr><tr><td>Faure and Poibeau [20]</td><td>Linguistics</td><td>Unstructured</td><td>Both</td></tr><tr><td>Heyer et al. [27]</td><td>Statistical</td><td>Unstructured</td><td>Samples</td></tr><tr><td>Jiang and Tan [28]</td><td>Statistical</td><td>Unstructured</td><td>Both</td></tr><tr><td>Kietz et al. [31]</td><td>Joint method</td><td>Unstructured</td><td>Both</td></tr><tr><td>Maddi et al. [33]</td><td>Statistical</td><td>Unstructured</td><td>Samples</td></tr><tr><td>Maedche and Staab [34]</td><td>Joint method</td><td>Unstructured</td><td>Both</td></tr><tr><td>Navigli and Velardi [35]</td><td>Joint method</td><td>Unstructured</td><td>Both</td></tr><tr><td>Shamsfard and Abdollahzadeh [42]</td><td>Linguistics</td><td>Unstructured</td><td>Both</td></tr><tr><td>Han and Elmasri [25]</td><td>Machine learning</td><td>Semi-structured</td><td>Both</td></tr><tr><td>This study</td><td>Machine learning</td><td>Semi-structured</td><td>None</td></tr></table>

The extraction of concepts from web resources without auxiliary resources is based on the extraction of objects from web pagewrappers. For example, ROADRUNNER discovers patterns in dataintensive sites, storing data in a back-end database and then producing HTML pages using scripts from the content of the database [14]. Omini extracts objects from web pages that contain multiple object instances, OntoMiner utilizes HTML regularities in web documents to discover concept instances, and Tanaka et al. extracted ontology from web tables, where the table structures were interpreted by humans [45].

## 3. Extracting ontology from the Web

This study proposes a knowledge extractor that assists ontology engineers to acquire information from the HTML Web. It develops an integrated system for extracting knowledge, an ontology extraction process, and a knowledge extractor for use by ontology engineers. A six-phase approach that comprises preparation, transformation, clustering, recognition, re<sup>fi</sup>nement, and revision is proposed to build ontology by extracting information from websites.

Some assumptions have been made. The <sup>fi</sup>rst is that the websites investigated are “ontology-directed,” that is, they are designed to represent a topic or a concept. For example, a university website is an “ontology-directed” website that is organized according around the ontology of “University,” “Admissions,” “Academic,” “Research,” “Campus Life” and so on. The second assumption is that the pages within the websites are written in HTML, rather than XML, which means that the schema (meta-data) of the sites has yet to be de<sup>fi</sup>ned. The third assumption is that the web pages are publicly accessible and that the websites are not in the hidden Web or the deep Web [6] such that users have to type in keywords or a password to access them. The fourth is that the web pages have a textual content, and that HTML multimedia, including images, video clips, and other non-HTML documents, will not be considered. The <sup>fi</sup>nal assumption is that the web pages are written in English, as we do not wish to address multilingual and translation issues here.

## 3.1. An integrated system for extracting knowledge

A system, called OntoSpider, is proposed for forming ontology by extracting information from HTML web pages. The system users are an ontology engineer and a system administrator. The duty of the system administrator is to maintain Java plug-in components, such as a MySQL database interface plug-in and a HTML DOM tree parser plug-in. The ontology engineer is responsible for extracting, managing, and releasing the ontology by managing the ontology base, pattern base, and concepts, and for importing and exporting the ontology. The system mainly comprises a website database and an ontology knowledge base, as shown in Fig. 1. The website database stores the web pages in well-formed HTML format documents after completing a preparation phase and a transformation phase. In the preparation phase, the web pages of the selected website are fetched and annotated from a remote website and stored in a repository. In the transformation phase, trivial pages, hyperlinks, and segments associated with the homepage are then <sup>fi</sup>ltered out. Each web page is represented by a tdimensional vector after stemming and the elimination of stop words.

The documents are then clustered to allow ef<sup>fi</sup>cient pattern recognition. The pages are clustered according to the similarity of their vectors using an instance clustering technique. In each clustered set, or set of instances of the same concept, a pattern is recognized and used to identify further instances in the coming recognition phase. Since recognizing instances is more complicated than clustering them, this phase results in better precision and recall (as is explained later).

The re<sup>fi</sup>nement process improves the concepts generated in the recognition phase. In the ontology re<sup>fi</sup>nement phase, the concepts are extracted from concept instances and their relationships are re<sup>fi</sup>ned. Finally, the ontology engineer revises any mis-de<sup>fi</sup>ned or ambiguous elements and con<sup>fi</sup>rms the ontology. The <sup>fi</sup>nalized ontology is retained as the ontology base. The output of the system is ontology.

## 3.2. The ontology extraction process

Fig. 2 shows the interaction of the six phases and the two databases, which are explained in detail in the following section.

## 3.2.1. Web page preparation

The system <sup>fi</sup>rst prepares documents by downloading web pages from a remote website and storing them in a local repository. Whether or not a page belongs to a web site is determined in the repository. A web page is deemed to belong to a website if the URL begins with the URL of the homepage of a website with the same root path, website. $P S = \{ p _ { i } { \mid } ( p _ { i } . p U R L )$ .indexOf(website.hpage $p U R L ) = 0 , i = 1 , 2 , . . . , m \}$ where website. $P s = \{ p _ { i } | i = 1 ~ 2 , . . . , m \}$ represents a web page, website. $H s = \{ h _ { i } | i = 1 , 2 , . . . , m \}$ is a hyperlink, and website.hpage is the homepage of the website. The URL of web page p is denoted by p.pURL, and the source page, destination page, and anchor text of the hyperlink are denoted by h.srcURL, h.dstURL, and h.aText, respectively.

A hyperlink is deemed to belong to a website if and only if both the source page and destination page of the hyperlink belong to the site, that is, website $H S = \{ h _ { i } | h _ { i } . s r c U R I$ L website.Ps, h<sub>i</sub>.dstURL website.Ps, $i = 1 , 2 , . . . , n \}$

In the remainder of the preparation phase, the system fetches the corresponding web page from the remote server, converts the page into a text-based well-formed HTML web page by referring to the method in [10], stores the well-formed web page in the website repository, parses the outgoing hyperlinks of the page, reuses the unvisited hyperlinks as a new URL, and repeats steps (1)–(5) if any unvisited web pages remain, otherwise it stops.

The outgoing hyperlinks outH(p) of web page p are a set of hyperlinks that are parsed from the content of page p and assigned a destination page that is not the hyperlink itself, that is, out $\mathsf { H } ( p ) = \left\{ h _ { i } \right| h _ { i } .$ dstURL $\neq p . p U R L , h _ { i } . s r c U R L = p . p U R L , i = 1 , 2 , . . . , m \}$ . To obtain a text-based well-formed HTML web page, the embedded multimedia objects need to be removed. In addition, in accordance with the HTML 4 speci<sup>fi</sup>cations (http://www.w3.org/TR/html4/), tags for displaying multimedia content are either removed from the page or replaced by a textual value for the attribute “ALT,” such as “APPLET,” “OBJECT,” and “IMG.” In addition, the complex elements “SCRIPT” and “STYLE” are removed and the page's style tags, such as “CENTER” and “HR,” are deleted.

The contents of the page are then summarized using the words (or phrases) that occur within it. As the “TITLE” and “META” tags are used to provide information about the entire document, we take advantage of the additional information that they contain. Hyperlinks also provide clues about the association of web pages, and can be used to associate, organize, search, or analyze Web content in a similar way to that used by Google [9]. However, in [22] and [7] it was found that in summarizing a web page, the hyperlinked terms that occur in the incoming hyperlinks of the page are slightly less useful than the web page itself. This study therefore uses the terms that appear in both the incoming hyperlinks and the page for ontology extraction. The web page annotation module in the preparation phase uses the content of the incoming hyperlinks of the page to increase the validity of the web page annotation. In this process, the web page is annotated according to the string of terms (rather than just a single term) that occur most frequently in the “TITLE” and “META” tags or in the incoming hyperlinks. If no commonly adopted string of terms can be used to name the page, then all of the strings of terms are kept and the ontology engineer selects the most appropriate in a later phase. The similarity between strings Str1 and Str2 is de<sup>fi</sup>ned by Dice's coef<sup>fi</sup>cient [18] as follows, where NumOfTerm(Str1) indicates the total terms in string 1 and CommonTerm(Str1, Str2) refers to the number of common terms used in Str1 and Str2.

![](/api/attachments/6B8QF5C7/fulltext/images/4b9731d327b6275dfe814084b3b746ec2ddca2f711ef27bcd3301da7367cab37.jpg)  
Fig. 1. System architecture.

![](/api/attachments/6B8QF5C7/fulltext/images/4de84bccf7a73d4b5db829a8fa8f47e0f6f6c3c584344a65d0fb8fece5c4fd7a.jpg)  
Fig. 2. The six-phase approach to ontology extraction

$$
\operatorname{Sim} (\text { Str1 }, \text { Str2 }) = \frac {2 \times \text { CommonTerm } (\text { Str1 } , \text { Str2 })}{\text { NumOfTerm } (\text { Str1 }) + \text { NumOfTerm } (\text { Str2 })}.\tag{1}
$$

## 3.2.2. Web page transformation

The downloaded website is re<sup>fi</sup>ned by removing irrelevant parts, such as broken links, missing web pages, and decorations (navigation panels, advertisement bars, and copyright or other general information panels) [16]. Compared with broken links and missing links, which can be easily identi<sup>fi</sup>ed and removed (such as “HTTP 404 Not Found” or “HTTP 403 (Forbidden)”), the removal of decorations takes more effort. A web page is normally partitioned into <sup>fi</sup>ve sections, top, left, center, right, and bottom, which are commonly de<sup>fi</sup>ned by the HTML “TABLE” tag (we base our partition of a web page on this tag because the “TABLE” tag is used not only for relational information display but also to create any type of multiple-column layout to facilitate easy viewing). Note that irrelevant text normally appears in the top, left, right, or bottom, and that similar phrases of text occur in the same section of a group of web pages.

Following this idea, an HTML web page can be parsed into an ordered DOM tree that includes a “HEAD” and a “BODY,” as shown in Fig. 3. A “BODY” sub-tree can be further decomposed into <sup>fi</sup>ve sections in the “TABLE” pattern: two “TR” sub-trees that are regarded as the top section (section A), the middle part (sections B, C, and D), and the bottom part (section E). In the middle part, section B is the left-hand column and section D is the right-hand column. In the case where the top, left, right, or bottom parts of the web page all have text (exclude section C) and are identical to the corresponding section of the parent page, they are considered to be duplications. We thus prune them from the pages and delete their hyperlink records from the database. The downloaded web pages are worked through in an iterated process and duplications are removed using the breadth-<sup>fi</sup>rst approach.

## 3.2.3. Instance clustering

After completing the preparation and re<sup>fi</sup>nement phases, each web page is presented as a t-dimensional vector for clustering. Formally, the process is de<sup>fi</sup>ned as follows. The hyperlink chain $H C ( p _ { i } , p _ { j } )$ is a list of link chains $h c ( p _ { i } , p _ { j } )$ from web page p to web page $p _ { j } \colon H C ( p _ { i } , p _ { j } ) =$ $\{ h c _ { k } ( p _ { i } , p _ { j } ) , k = 1 , 2 , . . . , \bar { m } \}$ . Link chain $h c _ { k } ( p _ { i } , p _ { j } )$ is denoted alternatively by $( h _ { 1 } , . . . , \ h _ { k } , . . . , \ h _ { n } )$ , where h .srcURL=p .pURL, $h _ { k - 1 } . d s t U R L = h _ { k } .$ srcURL $( 2 \leq k \leq n )$ , and $h _ { n } . d s t U R L = p _ { j } . p U R L$ , or (p<sub>1</sub>,…, $p _ { k } , . . . , \ p _ { n } )$ where $p _ { 1 } . p U R L = p _ { i } . p U R L , p _ { k }$ outP(p ) (2≤k≤n), and $p _ { n } . p U R L = p _ { j } .$ pURL. The ontology Onto is presented as the set $O n t o = ( C s , R s ) _ { \mathrm { ~ } }$ , where Cs is a set of the concepts $C s = \{ c _ { i } | i = 1 , 2 , . . . , n \}$ and Rs is a set of the relationships between concepts c and $c _ { j }$ that is expressed by $R s = \{ r$ $( c _ { i } , c _ { j } , t _ { i , j } ) | \ c _ { i } , c _ { j } \ C s , i \ne j \}$ , in which $t _ { i , j }$ represents the type of relationship. Object c1 is an instance of concept $c _ { i } ,$ the properties and attributes of which are de<sup>fi</sup>ned in concept class $c _ { i } ,$ and has a unique identity (called an “individual” or an “instance of class” in OWL Web Ontology Language guidance (http://www.w3.org/2004/OWL/ and http:// www.w3.org/TR/owl-guide/). The link ${ r i } ( c _ { i } , c _ { j } , t _ { i , j } )$ is an instance of relationship $r ( c _ { i } , c _ { j } , t _ { i , j } )$ if the two objects ci and ci of concepts $c _ { i }$ and $c _ { j }$ are linked by $r i ( c i _ { i } , c i _ { j } , t _ { i , j } )$ . If this is the case, then $c _ { i }$ is semantically related to $c _ { j }$ through relationship $t _ { i , j } .$

![](/api/attachments/6B8QF5C7/fulltext/images/ea1a94ca1265ad988cdd608559c330499f103fd6859e62ec836f56ab39fcc207.jpg)  
Fig. 3. An example (http://www.cse.cuhk.edu.hk) of the Web page partitioning algorithm

We further assume that instances of a concept have the same Web structure. As each instance represents a web page, if two web pages p and p are instances of the same concept, then they are considered to share the same chain of hyperlinks from the home page of the website. In other words, the intersection of two hyperlink chains HC(website. hpage,p ) and HC(website.hpage,p ) is not null, that is, HC(website. hpage,p )∩HC(website.hpage,p )≠Ф. For example, two seminars “A Video-Assisted Approach to the Structural Health Monitoring of Highway Bridges” and “Some Shape Deformation Operations with Applications in Footwear CAD” of the concept instance “Seminars” have a common hyperlink chain (home page, news, and joint seminars).

Note that a typical vector space model does not consider the structure of a document [15]. Thus, to represent a web page, the tdimensional vector space model must be extended for document encoding, as in HTML the structure of a web page provides useful information about the organization of a document. The vector can better represent the content of a web page by taking the structural information of the page into account. For instance, the terms that appear in the inbound HTML elements “TITLE” and “META” or in the incoming hyperlinks of the page are valuable in identifying the total content of a web document. The terms in “H1” can also be used to identify the topic of the section that is going to be introduced. In this case, the frequency of a term in different tags will be counted. In considering the de<sup>fi</sup>nition of HTML tags, a term is weighted by the summation of its frequency. This method was proposed in [13] and [15], in which tags were differentiated into three groups: linkText, plaintext, and (pageText+SectionText). In [13], it was shown that when tag information is considered during information retrieval, the precision and recall ratio are improved, and a similar <sup>fi</sup>nding was reported in [15]. Based on these considerations and the HTML 4 speci<sup>fi</sup>cations, we classify HTML elements into <sup>fi</sup>ve classes: linkText, pageText, sectionText, emphasizedText, and plaintext, as shown in Table 2. The linkText class contains the terms that occur in the text of the incoming hyperlinks to a web page, and provide descriptive information about the page. The terms in the pageText class provide additional information about the web page, such as the text in the “TITLE” element and the “keyword” and “description” attributes of the “META” tag. The META tag is considered as a pageText element due to the new HTML speci<sup>fi</sup>cation. The terms in the sectionText class describe the topic structure of a document (such as the terms used in H1, H2, H3, H4, H5, or H6), whereas the terms in the emphasizedText class include tags emphasized by the developer in the document content (such as terms shown in B, BIG, EM, I, STRONG, or U). Any term not included in these four classes remains in the plainText class. In general, the weights of the groups in terms of the information that they convey about a web page descend in order from emphasizedText, linkText, sectionText, pageText, to plaintext.

Table 2  
The <sup>fi</sup>ve classes and associated HTML elements.

<table><tr><td>No.</td><td>Class name</td><td>HTML elements</td></tr><tr><td>1</td><td>linkText</td><td>A (Incoming Hyperlink)</td></tr><tr><td>2</td><td>pageText</td><td>TITLE, META</td></tr><tr><td>3</td><td>sectionText</td><td>H1, H2, H3, H4, H5, H6</td></tr><tr><td>4</td><td>emphasizedText</td><td>B, BIG, EM, I, STRONG, U</td></tr><tr><td>5</td><td>plainText</td><td>None of the above</td></tr></table>

In the t-dimensional term vector, the value of each term is calculated by summing the weighted frequencies that occur in the aforementioned <sup>fi</sup>ve classes. For example, if the frequency of a term in the <sup>fi</sup>ve classes is TermFr $e q = ( t f _ { 1 } , t f _ { 2 } , t f _ { 3 } , t f _ { 4 } , t f _ { 5 } )$ , where $t f _ { i }$ represents the term frequencies in class i, then the class importance factor is de<sup>fi</sup>ned as $C l a s s W e i g h t { = } \left( c w _ { \scriptscriptstyle { l } } , c w _ { \scriptscriptstyle { 2 } } , c w _ { \scriptscriptstyle { 3 } } , c w _ { \scriptscriptstyle { 4 } } , c w _ { \scriptscriptstyle { 5 } } \right) ,$ , where $c w _ { i }$ is the weighted factor of class i. The ontology engineer then weighs the information provided by the different sections based on his or her experience. The weighted frequency of each term is calculated by

$$
w f = \text { TermFreq } \cdot \text { ClassWeight } = \sum_ {i = 1} ^ {5} t f _ {i} \times c w _ {i},\tag{2}
$$

and the vector is then normalized by

$$
w _ {i} = w f _ {i} \left/ \sum_ {j = 1} ^ {n} w f _ {j}, \left. \right.\tag{3}
$$

where $w _ { i }$ is the weight of term i in the document and n is the total number of terms in that document. The class weights are determined by the ontology engineer to assess the important of each class using methods such as the analytic hierarchy process (AHP) [39]. The vector additionally eliminates the effect of differing document lengths by [4]

$$
w _ {i} ^ {\prime} = w _ {i} \Bigg / \sqrt {\sum_ {j = 1} ^ {n} w _ {j} ^ {2}}.\tag{4}
$$

The web pages are then clustered by their similarities, as two web pages that are similar are considered to be instances of the same concept. The syntactical similarity of two web pages $p _ { i }$ and $p _ { j }$ is expressed by the cosine of the angle between the two vectors [4]

$$
\operatorname{sim} \left(p _ {i}, p _ {j}\right) = p _ {i} \cdot p _ {j} / | p _ {i} | \times | p _ {j} | = \sum_ {k} w _ {i, k} \times w _ {j, k} / \sqrt {\sum_ {k} w _ {i , k} ^ {2}} \times \sqrt {\sum_ {k} w _ {j , k} ^ {2}}.\tag{5}
$$

The measurement of the structural similarity between two web pages is more complicated. As we assume that instances of the same concept have a similar structure, we need to identify the hyperlink chains from the home page to the child web pages. To simplify the calculation of similarity, we visit the web pages of a site using a breadth-<sup>fi</sup>rst traversal method and calculate the content similarity of their child web pages. Web pages are considered to be structurally similar only if they share the same hyperlink chain from the home page to the parent web page.

## 3.2.4. Instance recognition

The next step is to recognize the patterns of the clustered web pages and use frequently occurring patterns to identify non-clustered web pages, a process that improves the web page recall. The patterns are used to modify the t-dimensional vector, which is then used to represent the web pages and to calculate the similarity between them (recognized instances in the cluster) and unrecognized web pages (web pages that have not yet been assigned to a cluster). Note that in this step the structural similarity remains the same, and the breadth-<sup>fi</sup>rst approach is again used to traverse the web pages (now expressed in t-dimensional vectors). If the similarity value between the vectors is above a pre-de<sup>fi</sup>ned threshold, then the unassigned web page is added to the relevant cluster.

Table 3  
An example for analytical matrix for <sup>fi</sup>ve classes.

<table><tr><td>Class name</td><td>linkText</td><td>pageText</td><td>sectionText</td><td>emphasizedText</td><td>plaintext</td></tr><tr><td>linkText</td><td>1</td><td>1</td><td>3</td><td>5</td><td>7</td></tr><tr><td>pageText</td><td>1</td><td>1</td><td>3</td><td>5</td><td>7</td></tr><tr><td>sectionText</td><td>1/3</td><td>1/3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>emphasizedText</td><td>1/5</td><td>1/5</td><td>1/2</td><td>1</td><td>2</td></tr><tr><td>plaintext</td><td>1/7</td><td>1/7</td><td>1/3</td><td>1/2</td><td>1</td></tr></table>

## 3.2.5. Ontology refinement

Using the foregoing steps, most web pages can be successfully clustered into groups, and their concepts can then be extracted by annotating the clustered web pages and breaking them down into concepts (concept instances). Relationships between concepts are traced by referring to the relationships between concept instances. We process the hyperlinks (relationships) using four rules: hyperlinks between un-clustered web pages remain, hyperlinks between clustered pages (concepts) are represented by a relationship class, hyperlinks between clustered web pages (concepts) and un-clustered web pages are kept as un-clustered web pages, and hyperlinks within clustered web pages (concepts) are ignored.

We then re<sup>fi</sup>ne the relationships (hyperlinks) based on the assumption that relationships in the ontology are symmetric and transferable. That is, we assume that a hyperlink represents a relationship instance. For example, the hyperlink “Computer Vision Laboratory” on a professor's homepage represents a relationship instance of ri(academicStaff,laboratory,memberOf). A relationship is deemed to be symmetric if the relationship between concept $c _ { i }$ and $c _ { j }$ can be represented by the relationship between concept $c _ { i }$ and $c _ { j } .$ Similarly, a relationship is deemed to be transferable if concep $c _ { i }$ links to $c _ { j }$ and $c _ { j }$ links to $c _ { k } ,$ as then $c _ { i }$ is linked to $c _ { k } .$ We further assume that there is only one kind of relationship between concepts $c _ { i }$ and $c _ { j } ,$ that is, multiple relationships between $c _ { i }$ with $c _ { j }$ are not allowed.

Because the relationships are symmetric, if relationships $r ( c _ { i } , c _ { j } , t _ { i , j } )$ and $r ( c _ { j } , c _ { i } , t _ { j , j } )$ both exist, then one of them will be removed. In addition, because the relationships are transferable, indirect relationships will also be removed. For example, if relationships $r ( c _ { i } , c _ { j } , t _ { i , j } ) , r ( c _ { j } ,$ $c _ { k } , t _ { j , k } ) ,$ , and $r ( c _ { i } , c _ { k } , t _ { i , k } )$ all exist, then either $r ( c _ { i } , c _ { k } , t _ { i , k } )$ or both $r ( c _ { i } , c _ { j } , t _ { i , j } )$ and $r ( c _ { j } , c _ { k } , t _ { j , k } )$ will be removed.

Web page annotation accuracy.

<table><tr><td>Name of web site</td><td>Number of pages</td><td>Correct annotation using only the TITLE tag</td><td>Correct annotation</td></tr><tr><td> $Department A^{(a)}$ </td><td>138</td><td>61(44.2%)</td><td>87(63.0%)</td></tr><tr><td> $Department B^{(b)}$ </td><td>106</td><td>3(2.8%)</td><td>84(79.2%)</td></tr><tr><td> $Department C^{(c)}$ </td><td>106</td><td>93(87.7%)</td><td>98(92.5%)</td></tr><tr><td> $Department D^{(d)}$ </td><td>368</td><td>67(18.2%)</td><td>182(49.5%)</td></tr><tr><td> $Newspaper^{(e)}$ </td><td>902</td><td>872(96.7%)</td><td>872(96.7%)</td></tr></table>

<sup>(a)</sup> http://www.cs.yale.edu, at 20:44:5.27, 14, June, 2006.  
<sup>(b)</sup> http://www.acae.cuhk.edu.hk/en, at 7:14:54.952, 11, March, 2006.  
<sup>(c)</sup> http://www.media.mit.edu, at 15:59:47.338, 6, May, 2006.  
<sup>(d)</sup> http://www.se.cuhk.edu.hk, at 9:29:57.852, 29, May, 2006.  
<sup>(e)</sup> http://www.ChinaDialy.com/sports/, at 20:20:19.609, 1, March, 2007.

Table 5 Web page transformation.

<table><tr><td rowspan="2">Name of web site</td><td rowspan="2">Total pages</td><td rowspan="2">Affected pages</td><td rowspan="2">Removed bytes</td><td rowspan="2">Averaged correct ratio</td><td rowspan="2">Averaged incorrect ratio</td><td colspan="2">Before process</td><td colspan="2">After process</td></tr><tr><td>Concept</td><td>Relationship</td><td>Concept</td><td>Relationship</td></tr><tr><td>Department A</td><td>138</td><td>91</td><td>74,498(= 745,473–670,975</td><td>51.28%</td><td>0%</td><td>138</td><td>1691</td><td>55</td><td>481</td></tr><tr><td>Department B</td><td>106</td><td>103</td><td>17,279(= 584,470–567,191)</td><td>66.34%</td><td>0%</td><td>106</td><td>1344</td><td>64</td><td>328</td></tr><tr><td>Department C</td><td>106</td><td>104</td><td>16,317(= 582,162–565,845)</td><td>26.28%</td><td>0%</td><td>106</td><td>1662</td><td>59</td><td>559</td></tr><tr><td>Department D</td><td>368</td><td>198</td><td>252,505(= 1,932,806–1,680,301</td><td>49.83%</td><td>0%</td><td>343</td><td>3741</td><td>269</td><td>1265</td></tr><tr><td>Newspaper</td><td>902</td><td>844</td><td>208,674(= 4,140,672–3,931,998)</td><td>71.71%</td><td>0%</td><td>569</td><td>6610</td><td>304</td><td>3450</td></tr></table>

## 3.3. Revision by the ontology engineer

The ontology engineer plays a key role in ontology extraction. First, he or she needs to know the purpose of the work. For example, the knowledge may be used to identify possible buyers and sellers in ecommerce applications, or the additional information extracted from websites may be used to strengthen the bargaining power in negotiations with a buyer or seller.

![](/api/attachments/6B8QF5C7/fulltext/images/b919e949a450691f2726659af61d5bac8059be39a7fd4fbbed92043c160de71d.jpg)

![](/api/attachments/6B8QF5C7/fulltext/images/3d8c0ce0c23acb40f950a0734c19e4273cf3d6a1dafb9c6f7d2b6ea7273ef666.jpg)

![](/api/attachments/6B8QF5C7/fulltext/images/6ec8f0a01e742281790f905b486a36cf084882c16905b895a5e9e00c6d291891.jpg)

The ontology engineer needs to be actively involved in the ontology extraction process because the proposed system is only semi-automatic. The engineer's duties include selecting the names of web pages in the preparation phase when there is no explicit name in the page title, weighing the class importance in the clustering phases, determining the threshold values and resolving any ambiguity in the recognition phase, and modifying the ontology in the revision phase. In general, the extraction of concepts from un-clustered web pages is left to the discretion of the ontology engineer to simplify the process. The ontology engineer will also need to conduct an ontology revision of the constructed concepts. The engineer is thus responsible for extracting an ontology that is con<sup>fi</sup>ned to the knowledge of domain experts.

![](/api/attachments/6B8QF5C7/fulltext/images/13243927d9535799443f41ff692b9ddc9c26db2603f67c801b66dd41148234f7.jpg)

![](/api/attachments/6B8QF5C7/fulltext/images/dfb38a6329c81e24b32d5994962a6623f19c6360e76d4cd5d7eb2f1f6fcac297.jpg)

![](/api/attachments/6B8QF5C7/fulltext/images/4198989602e71df53574532ad3516505fbdb7f9f8f23bf8215d9fb3c15e95c09.jpg)  
Fig, 4. Performance measures of the precision and recall of concepts with and without using structural information (hyperlinks) after the application of recognition

## 4. System development and demonstration

The developed knowledge extractor allows ontology engineers to acquire information for various purposes. In this section, we detail the construction of OntoSpider to demonstrate the use of the system. The system was built and compiled using the Java platform (J2SE Development Kit 5.0, http://java.sun.com/j2se/1.5.0/index.jsp) and the Xerces2 Java parser 2.5.0 plug-in (http://xml.apache.org/ xerces2- j/) for the formulation and parsing of well-formed web documents. The database is a MySQL 4.1 database server (http://dev.mysql.com/ downloads/ mysql.4.1.html). In the following sections, we work through each phase to demonstrate the system.

![](/api/attachments/6B8QF5C7/fulltext/images/95698043e5ef0c789673fefa8f71b282184f058cf29cd90d15f7591af0eaa828.jpg)

First, we assume that an ontology engineer uses the pairwise comparison of analytic hierarchy process to determine the class weights, as shown in Table 3. The class weights for linkText, pageText, sectionText, emphasizedText, and plaintext are 0.37, 0.37, 0.135, 0.077, and 0.047, respectively. We then demonstrate the annotation of the web pages in the preparation phase using four academic departmental Web sites and one newspaper website, as shown in Table 4, where the threshold of determining the similarity of two strings of terms is set at 0.8 (experiments with different threshold values are provided later). We compare the results for web pages annotated by the “TITLE” tag only with the results in which the web page structure, including “TITLE,” “META,” and the anchor text of incoming hyperlinks, is considered. We <sup>fi</sup>nd that the accuracy is higher when the web page structure is considered.

![](/api/attachments/6B8QF5C7/fulltext/images/d3542689cd4c938df40170e73e772d3ef501c63bad976addb06e38d1e4219453.jpg)

![](/api/attachments/6B8QF5C7/fulltext/images/8e21931fffa656e0f13a733f2d4863c2c8367e254e61fcca29c42bec9ddd76d2.jpg)

![](/api/attachments/6B8QF5C7/fulltext/images/02e56f3c82785ec7a1f948bbc3f581d393557e31ee4d6761d9dc8a7ef8b44469.jpg)

![](/api/attachments/6B8QF5C7/fulltext/images/435347c4f5b1ea548af7404402f336f7ff572c9cd4dc7143a275c2bc05d31954.jpg)

![](/api/attachments/6B8QF5C7/fulltext/images/18757f7214ea05601dc8a610920e52c13587ea2b0cc99c91a860c25f4a85a984.jpg)  
Fig. 5. Precision/recall ratios after the application of instance re<sup>fi</sup>nement.

Table 6 Similarity between the web sites of Department A and other related departments.  
![](/api/attachments/6B8QF5C7/fulltext/images/b1072750d575a8d3ef9129930e085ababa4dbebb7f0f538c076af6698415b00c.jpg)  
Fig. 6. A snapshot of OntoSpider's GUI.

Table 5 shows the statistical results of the web page transformation. We list the total number of bytes removed from the web pages, the number of web pages affected, and the average correct ratio and average incorrect ratio of all of the web pages. The correct ratio of one web page is de<sup>fi</sup>ned as the ratio of trivial sections detected on the web page. The average correct ratio for an entire website is achieved by averaging the correct ratio for each page on the site. Similarly, the incorrect ratio is the ratio of incorrectly removed sections to total sections of a web page, and the average incorrect ratio of an entire site is the average of the incorrect ratio for each web page.

In the clustering and recognition phases, structural similarity is taken into consideration. Two performance indexes that are commonly used in information retrieval research, recall and precision, are used for the performance measurement. Recall describes the fraction of concept instances correctly retrieved, and precision measures the fraction of correctly retrieved concept instances for the same concept. In Fig. 4, we present both the recall and precision scores for web page clustering when the similarity threshold values are set in the range of 0.4 to 1.0. The <sup>fi</sup>gure shows the results using the website of Department A as an example. It clearly shows that, using the same threshold value, web page clustering using structural information alone results in a lower recall (average of 0.2085) but a signi<sup>fi</sup>cantly higher precision (average 0.8725). Thus, when information about a website's structure is included, the precision of the instance clustering is greatly improved. This is especially true for the recognition of certain general instances of concepts, such as “News,” “Seminars,” or “Events.” A low recall rate can be improved in the re<sup>fi</sup>nement phase.

Fig. 5 shows the recall and precision results for the recognition of instances on the Department A web site (visited on June 16, 2006) after applying re<sup>fi</sup>nement when the threshold values are set between

0.4 and 1.0. It can be seen that both the recall ratio and precision ratio show a greater improvement (recall of 0.8539 and precision of 0.7005) when the threshold is set at 0.7. When structural similarity is considered, the precision ratio is maintained at a high level (higher than 0.7037 on averages) but the instance recognition recall ratio is improved (higher than 0.6180 on averages).

The output of the <sup>fi</sup>rst <sup>fi</sup>ve phases generates many ontology classes and the instances associated with them. To help the ontology engineer to manage the extracted ontology, a graphical interface is built that provides loading, editing, and recoding functions for OntoSpider (see Fig. 6). The left-hand window of Fig. 6 shows the hierarchical ontology and the right-hand window the concepts (organized ontology) and their corresponding web pages. A toolbar provides ef<sup>fi</sup>cient ontology export functions, such as conversion and editing. The interface also provides functions for browsing through the concept hierarchy, incoming hyperlinks, and outgoing hyperlinks, and mapping them to the corresponding web pages. By using this interface, an ontology engineer can manage knowledge by editing the concept node of the ontology interactively, for example by renaming a concept, deleting a concept node, appending a new concept node, or identifying a node as the node of a concept instance. The ontology engineer can also delete or append a new relationship between two concept nodes by using the editor. OntoSpider then saves the ontology in the ontology base or exports it into a common ontology description language, such as RDF, DAML, or OWL.

<table><tr><td>Department</td><td>Similarity (%)</td></tr><tr><td> $Department\ B: chemical\ engineering^{(a)}$ </td><td>40.61</td></tr><tr><td> $Department\ C: civil\ engineering^{(b)}$ </td><td>52.81</td></tr><tr><td> $Department\ D: computer\ science^{(c)}$ </td><td>48.24</td></tr><tr><td> $Department\ E: electrical\ and\ electronic\ engineering^{(d)}$ </td><td>60.34</td></tr><tr><td> $Department\ F: industrial\ engineering\ and\ engineering\ management^{(e)}$ </td><td>51.16</td></tr><tr><td> $Department\ G: mechanical\ engineering^{(f)}$ </td><td>69.66</td></tr><tr><td colspan="2">(a) http://www.ceng.ust.hk/.</td></tr><tr><td colspan="2">(b) http://www.ce.ust.hk/home.asp.</td></tr><tr><td colspan="2">(c) http://www.cs.ust.hk/.</td></tr><tr><td colspan="2">(d) http://www.ee.ust.hk/.</td></tr><tr><td colspan="2">(e) http://www.ieem.ust.hk/.</td></tr><tr><td colspan="2">(f) http://www.me.ust.hk/.</td></tr></table>

![](/api/attachments/6B8QF5C7/fulltext/images/d20a4896362efeffc3c0567e18775dfc37f767812ebd5695b34d0526d433e7ee.jpg)  
Fig. 7. Ontology “Department” published in the SHOE project (http://www.cs.umd.edu/projects/plus/SHOE/onts/cs1.1.html).

As has been discussed, ontologies are useful for knowledge management and electronic commerce. For example, before bargaining with buyers (or sellers), a company might want to compare the websites of the buyers to obtain more information on their products and other company information. OntoSpider could be used to measure the similarity between the websites in such cases.

To illustrate the application of OntoSpider, we again use academic websites as an example, and assume that the similarity of two departments can be measured by the research interests of the academic staff. Table 6 shows the results of a comparison of the website of Department A with the sites of other departments. Similarity is measured by the t-dimensional vector that OntoSpider extracts from the research interests elements and is calculated using Eqs. (2)–(5). The table shows that Department A is best matched to Department G (a similarity score of 69.66%), even though in fact there is a signi<sup>fi</sup>cant difference between the departmental names.

We compare the output from OntoSpider with that of the SHOE project of the University of Maryland (covering 15 computer science departments in the United States), which allowed users to annotate HTML web pages to manually build an ontology. The ontology published by the SHOE project is presented in Fig. 7. We use

Comparison of ontology extracted by OntoSpider and SHOE.

<table><tr><td>OntoSpider</td><td>SHOE</td><td>OntoSpider</td><td>SHOE</td></tr><tr><td>Link</td><td>N.A.</td><td>Course and Research</td><td>Work</td></tr><tr><td>Job Vacancy</td><td>N.A.</td><td>Program</td><td>Schedule</td></tr><tr><td>Honor and Award</td><td>N.A.</td><td>No</td><td>Software</td></tr><tr><td>Program</td><td>Schedule</td><td>No</td><td>Conference</td></tr><tr><td>Staff</td><td>Person</td><td>Publication</td><td>Publication</td></tr><tr><td>Admission</td><td>N.A.</td><td>Staff</td><td>Person</td></tr><tr><td>Research</td><td>Publication</td><td></td><td></td></tr><tr><td>Facility</td><td>N.A.</td><td></td><td></td></tr><tr><td>Student</td><td>Person</td><td></td><td></td></tr><tr><td>News</td><td>N.A.</td><td></td><td></td></tr></table>

![](/api/attachments/6B8QF5C7/fulltext/images/efb7b701218475cb808e133228ddd662d95c20f7b265d1a5909706c59ed7ddee.jpg)  
Fig. 8. The ontology for “Department” extracted from Department A's web site

OntoSpider to extract ontology from similar websites of several computer science-related departments in Hong Kong and compare the output with that of SHOE, which served as a testbed for Semantic Web ideas [26]. As shown in Table 7, OntoSpider extracts many concepts automatically that were also presented by SHOE (although with different names), but also provides concepts such as “Links,” “Job Vacancies,” “Honors and Awards,” and “News” that are not in SHOE. This is probably because these concepts are not particular to computer science departments. There are several other major distinctions between OntoSpider and the SHOE project. First, the

![](/api/attachments/6B8QF5C7/fulltext/images/456caadec305a4cb95949595494c2835fde730caa026d8aa23076993ed1a475f.jpg)  
Fig. 9. Examples of the limitations of OntoSpider.

SHOE project developed a knowledge annotator to assist users to add, edit, or remove instances or ontologies manually, whereas OntoSpider annotates HTML pages and retrieves ontology semiautomatically. Second, the SHOE project allows users to specify ontological information and a series of templates for classi<sup>fi</sup>cation and relation declaration, and then uses mobile agents to extract the markup from a remote web page, whereas OntoSpider downloads web pages and analyzes them locally and seamlessly. Finally, the SHOE project aims to convert a HTML web page into a semantic web page, whereas the objective of OntoSpider is to manage knowledge found on the HTML Web.

Despite its many useful applications, ontology extraction has some limitations. Fig. 8 shows an example of the original ontology for “Department” that was extracted from the website of Department A using OntoSpider. The dotted blocks in the <sup>fi</sup>gure indicate incorrect concept nodes and relationships. The <sup>fi</sup>gure highlights that there are four main limitations to OntoSpider. The <sup>fi</sup>rst is the direct link problem in blocks 1 and 5, which is caused by the fact that some websites allow direct hyperlink points to related pages. For example, one department pages highlighting news about a professor winning an award, the hyperlink for the professor points to the professor's web page directly without following the ontology hierarchy of department – staff – professors. The second limitation is the command button problem in block 2, which arises from the fact that some web pages provide a command button for browsing through the page. For example, in Fig. 9, a command button is available for browsing through alumni reunion photos, but the relationship between the photo pages is treated as a parent–child relationship where it should be a sibling relationship. The third limitation is the semantic problem in block 3, in that the relationship between concepts in contexts that are related to lexical semantics, natural language, and linguistics cannot be interpreted. However, this is out of the scope of this study. The <sup>fi</sup>nal problem is the document formatting problem in block 4, which occurs because information on context format is not taken into account in this study. For example, Fig. 9 shows that the correct relationship between the topics “Arti<sup>fi</sup>cial Intelligence” and “Mathematical Theories of Human Vision” on the “Research Area” web page is a parent–child relationship, as “Mathematical Theories of Human Vision” is a subset of “Arti<sup>fi</sup>cial Intelligence.” However, the output from OntoSpider treats them as siblings, even though the relationship between the two terms can be understood from the format of the web pages.

## 5. Conclusion

Web semantics can be used to enhance decision quality in many applications. For example, in e-commerce, it can be applied to locate buyers and sellers, to acquire additional information on negotiation partners from websites before negotiations, to compare the similarities of two companies' websites, and so on. In this study, we propose an ontology retrieval system called OntoSpider for acquiring Web semantics, and develop a six-phase approach to extracting ontology from HTML websites using OntoSpider. The approach uses information on the terms, hyperlinks, and tags in a web page to perform a semi-automatic extraction process that involves the phases of preparation, transformation, clustering, recognition, re<sup>fi</sup>nement, and revision. In the ontology retrieval process, the ontology engineer determines the parameters and revises the concepts, and is thus key to ensuring that a useful ontology is retrieved.

The approach has clear practical application, in that it allows organizations to retrieve information from dynamic web pages for use in many areas. Knowledge engineers could also use the approach to update their corporation's knowledge base. The approach could further be used to modify search engines to provide search results that are based on the similarity of websites, rather than on the similarity of pages alone or on keywords. Finally, the approach could be applied to search blogs for word-of-mouth marketing and e-commerce applications, such as locating suppliers and buyers or negotiating a business contract.

This study is not without its limitations. We note that lexical semantics, natural language, and linguistics will all affect the quality of the results. For example, it is dif<sup>fi</sup>cult to cluster “News,” as it involves complex knowledge. Furthermore, the outcomes differ when there are misplaced links or words. That is, the quality of the approach is affected by the quality of the page content. We leave these limitations to be addressed in a future study. Another avenue that merits future exploration is how individual ontologies shared by various users can be merged to form a global ontology.

## Acknowledgment

This project is partially supported by the Li & Fung Institute of Supply Chain Management & Logistics.

## References

[1] E. Agirre, O. Ansa, E. Hovy, D. Martinez, Enriching very large ontologies using the WWW, Proceedings of the ECAI 2000 Workshop on Ontology Learning, 2000, pp. 25–30.

[2] M. Alavi, D.E. Leidner, Review: knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25 (1) (March 2001) 107–136.

[3] A. Arasu, H. Garcia-Molina, Extracting structured data from web pages, Proceedings of the 2003 ACM SIGMOD International Conference on Management of Data, 2003, pp. 337–348.

[4] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, ACM Press, New York, 1999.

[5] S. Bechhofer, I. Horrocks, C. Goble, R. Stevens, OilEd: a reasonable ontology editor for the semantic Web, Lecture Notes in Computer Science 2174 (2001) 396–408.

[6] M.K. Bergman, The Deep Web: Surfacing Hidden Value, September 24, 2001 http:// www.brightplanet.com/pdf/deepwebwhitepaper.pdf.

[7] A. Blum, T. Mitchell, Combining labeled and unlabeled data with co-training, Proceedings of the Eleventh Annual Conference on Computational Learning Theory, 1998, pp. 92–100.

[8] E.P. Bontas, M. Mochol, R. Tolksdorf, Case studies on ontology reuse, Proceedings of I-KNOW '05 Graz, Austria, June 29 – July 1, 2005, pp. 345–353.

[9] S. Brin, L. Page, The anatomy of a large-scale hypertextual web search engine, Computer Networks and ISDN Systems 30 (1–7) (1998) 107–117.

[10] D. Buttler, L. Liu, C. Pu, A fully automated object extraction system for the World Wide Web, Proceedings of the 2001 International Conference on Distributed Computing Systems, 2001, pp. 361–370.

[11] R. Chalmeta, R. Grangel, Methodology for the implementation of knowledge management systems, Journal of the American Society for Information Science and Technology 59 (5) (March 2008) 742–755.

[12] C. Chou, T. Du, V. Lai, Continuous auditing with a multi-agent system, Decision Support Systems 42 (4) (January 2007) 2274–2292.

[13] M. Craven, D. DiPasqua, D. Freitag, A. McCallum, T. Mitchell, K. Nigam, S. Slattery, Learning to construct knowledge bases from the world wide web, Arti<sup>fi</sup>cial Intelligence 118 (1–2) (2000) 69–113.

[14] V. Crescenzi, G. Mecca, P. Merialo, ROADRUNNER: towards automatic data extraction from large web sites, Proceedings of the Twenty-seventh VLDB Conference, 2001, pp. 109–118.

[15] M. Cutler, Y. Shih, W. Meng, Using the structure of HTML documents to improve retrieval, Proceedings of the USENIX Symposium on Internet Technologies and Systems, 1997, pp. 241–251.

[16] H. Davulcu, S. Vadrevu, S. Nagarajan, OntoMiner: bootstrapping ontologies from overlapping domain speci<sup>fi</sup>c web sites, Proceedings of the Thirteenth International World Wide Web Conference, 2004, pp. 500–501.

[17] A. Delteil, C. Faron-Zucker, R. Dieng, Learning ontologies from RDF annotations, in: A. Maedche, S. Staab, C. Nedellec, E. Hovy (Eds.), Proceedings of IJCAI-01 Workshop on Ontology Learning OL-2001, Seattle, August 2001.

[18] L.R. Dice, Measures of the amount of ecologic association between species, Ecology 26 (1945) 297–302.

[19] A. Faatz, R. Steinmetz, Ontology enrichment with texts from the WWW, Semantic Web Mining WS02, Helsinki Finland 2002

[20] D. Faure, T. Poibeau, “First experiments of using semantic knowledge learned by ASIUM for information extraction task using INTEX Proceedings of the Fourteenth European Conference on Arti<sup>fi</sup>cial Intelligence, 2000, pp. 7–12.

[21] D. Fensel, Ontologies: A Silver Bullet for Knowledge Management and Electronic Commerce, Springer, New York, 2001.

[22] E.J. Glover, K. Tsioutsioliklis, S. Lawrence, D.M. Pennock, G.W. Flake, Using web structure for classifying and describing web pages, Proceedings of WWW2002, 2002, pp. 562–569.

[23] A. Gomez-Perez, D. Manzano-Macho, An overview of methods and tools for ontology learning from texts, Knowledge Engineering Review 19 (3) (2005) 187–212.

[24] Z. Guo, J. Shef<sup>fi</sup>eld, A paradigmatic and methodological examination of knowledge management research: 2000 to 2004 Decision Support Systems 44 (3) (February 2008)673-688

[25] H. Han, R. Elmasri, Learning rules for conceptual structure on the Web, Journal of Intelligent Information Systems 22 (3) (2004) 237–256.

[26] J. He<sup>fl</sup>in, J. Hendler, A portrait of the semantic Web in action, IEEE Intelligent Systems 16 (2) (2001) 54–59.

[27] G. Heyer, M. Lauter, U. Quasthoff, T. Wittig, C. Wolff, Learning relations using collocations, Proceedings of the IJCAI Workshop on Ontology Learning, 2001, pp.19–24.

[28] X. Jiang, A.H. Tan, Mining ontological knowledge from domain-speci<sup>fi</sup>c text documents, Proceedings of the Fifth IEEE International Conference on Data Mining, 2005, pp. 665–668.

[29] Y. Kalfoglou, M. Schorlemer, Ontology mapping: the state of the art, Knowledge Engineering Review 18 (2003) 1–31.

[30] S. Kaza, H. Chen, Evaluating ontology mapping techniques: an experiment in public safety information sharing, Decision Support Systems 45 (4) (November 2008) 714–728.

[31] J.U. Kietz, R. Volz, A. Maedche, Extracting a domain-speci<sup>fi</sup>c ontology from a corporate Intranet, Proceedings of the Fourth Conference on Computational Natural Language Learning and of the Second Learning Language in Logic Workshop, 2000, pp. 167–175.

[32] T.P. Liang, Y.F. Yang, D.N. Chen, Y.C. Ku, A semantic-expansion approach to personalized knowledge recommendation, Decision Support Systems 45 (3) (June 2008) 401–412.

[33] G.R. Maddi, C.S. Velvadapu, S. Srivastava, J.G. Lamadrid, Ontology extraction from text documents by singular value decomposition, Proceedings of the ADMI, 2001.

[34] A. Maedche, S. Staab, Ontology learning for the semantic Web, IEEE Journal of Intelligent Systems 16 (2) (2001) 72–79.

[35] R. Navigli, P. Velardi, Learning domain ontologies from document warehouses and dedicated web sites, Computational Linguistics 30 (2) (2004) 151–179

[36] N. Noy, M.A. Muse, PROMPT: algorithm and tool for automated ontology merging and alignment, Proceedings of the Seventeenth National Conference on Arti<sup>fi</sup>cial Intelligence and Twelfth Conference on Innovative Applications of Arti<sup>fi</sup>cia Intelligence, 2000, pp. 450–455.

[37] N.F. Noy, M. Klein, Ontology evolution: not the same as schema evolution, Knowledge and Information Systems 6 (4) (July 2004) 428–440.

[38] N. Noy, H. Stuckenschmidt, Ontology alignment: an annotated bibliography, in: Y. Kalfoglou, M. Schorlemmer, A. Sheth, S. Staab, M. Uschold (Eds.), Semantic Interoperability and Integration, IBFI, Schloss Dagstuhl, 2005.

[39] T.L. Saaty, Fundamentals of the Analytic Hierarchy Process, RWS Publications, PA 2000.

[40] M. Sabou, C. Wroe, C. Goble, G. Mishne, Learning domain ontologies for web service descriptions: an experiment in bioinformatics, Proceedings of the WWW 2005, 2005, pp. 190–198.

[41] A. Segev, A. Gal, Enhancing portability with multilingual ontology-based knowledge management, Decision Support Systems 45 (3) (June 2008) 567–584.

[42] M. Shamsfard, A. Abdollahzadeh, The state of the art in ontology learning: a framework for comparison, Knowledge Engineering Review 18 (4) (2003) 293–316.

[43] M. Shamsfard, A.A. Barforoush, Learning ontologies from natural language texts, International Journal of Human-Computer Studies 60 (1) (2004) 17–63.

[45] M. Tanaka, T. Ishida, Ontology extraction from tables on the Web, Proceedings of the 2006 Symposium on Applications and the Internet, 2006, pp. 284–290.

![](/api/attachments/6B8QF5C7/fulltext/images/492f806e760f32530f6903fd3d2822d265fddee846eb181af562826919bcc13d.jpg)

Timon C. Du received his BS degree in Mechanical Engineering from the National Chung-Hsing University, Taiwan. He obtained his Master's and PhD degrees in Industrial Engineering from Arizona State University. Currently, Dr. Du is a Professor at The Chinese University of Hong Kong. His research interests include e-business, data mining, collaborative commerce, and semantics webs. He has published papers in many leading international journals such as Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, Communications of the ACM, IIE Transactions, Information & Management, and others.

![](/api/attachments/6B8QF5C7/fulltext/images/8c8c2f5a753fba3f94e8ac9d59effbcdd886d3154605049f41c456fd825380ad.jpg)

Feng Li received his BS and MS degrees in control science and engineering in 1997 and 2000, respectively; and PhD in system engineering in 2004 from the Huazhong University of Science and Technology, China. Currently, he is a lecturer of school of business administration at South China University of Technology, China. His research interests include semantic Web, decision support system, and arti<sup>fi</sup>cial intelligence.

![](/api/attachments/6B8QF5C7/fulltext/images/aaabc2abeedba39864ad2c33748c10f85f9cb1c010d08281f52c468f1ff76e21.jpg)

Irwin King's research interests include machine learning, web intelligence & social computing, and multimedia processing. In these areas, he has published over 150 combined refereed journal and conference manuscripts. In addition, he has contributed over 20 book chapters and edited volumes. He is currently with the Chinese University of Hong Kong. He received his BSc degree from California Institute of Technology and his MSc and PhD degree in Computer Science from the University of Southern California. He is an Associate Editor of the IEEE Transactions on Neural Networks, a member of ACM and International Neural Network Society (INNS), a senior member of IEEE, and a Vice-President and also a Governing Board Member of the Asian Paci<sup>fi</sup>c Neural Network Assembly (APNNA).
