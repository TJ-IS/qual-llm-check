---
otero_id: 11908
otero_key: "STJNC9F6"
title: "Financial Concept Element Mapper (FinCEM) for XBRL interoperability: Utilizing the M 3 Plus method"
authors: "Ugochukwu Etudo; Victoria Yoon; Dapeng Liu"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.04.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Financial Concept Element Mapper (FinCEM) for XBRL interoperability: Utilizing the M3 Plus method

ELSEVIER Decision Support Systems

Ugochukwu Etudo, Victoria Yoon, Dapeng Liu

![](/api/attachments/STJNC9F6/fulltext/images/5663e598f390d8ca352334f4bee2992d3e80f92fb70a872720e2e30b1636e577.jpg)

PII: S0167-9236(17)30065-9

DOI: doi: 10.1016/j.dss.2017.04.006

Reference: DECSUP 12830

To appear in: Decision Support Systems

Received date: 13 June 2016

Revised date: 2 March 2017

Accepted date: 13 April 2017

Please cite this article as: Ugochukwu Etudo, Victoria Yoon, Dapeng Liu , Financial Concept Element Mapper (FinCEM) for XBRL interoperability: Utilizing the M3 Plus method. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi: 10.1016/j.dss.2017.04.006

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

Financial Concept Element Mapper (FinCEM) for XBRL Interoperability: Utilizing the M<sup>3</sup> Plus Method

Ugochukwu Etudo

etudouo@vcu.edu

Victoria Yoon\*

vyyoon@vcu.edu

Dapeng Liu

liud22@.vcu.edu

Department of Information Systems Virginia Commonwealth University 301 W. Main St. P. O. Box 844000 Richmond, VA 23284-4000

Corresponding Author

# Financial Concept Element Mapper (FinCEM) for XBRL Interoperability: Utilizing the M<sup>3</sup> Plus Method

## Abstract

The use of eXtensible Business Reporting Language (XBRL) to represent financial reports (particularly 10-K and 10-Q filings) is a requirement of all public companies in the United States. The intention of the XBRL mandate is to streamline the financial reporting pipeline by providing full automaticity with respect to the collection, collation and analysis of financial information on the Web. However, the current lack of acceptable XBRL interoperability prevents the realization of the mandate’s potential. This paper reports on a comprehensive solution to this problematic situation. The proposed design artifact, called FinCEM, is undergirded by channel theory and seeks to capture and leverage the semantics of XBRL calculation linkbases towards improved XBRL interoperability. The design artifact is instantiated and evaluated against XBRL filings from companies included in the S&P 100. The artifact, which operates automatically and without human intervention, is shown to provide significant improvements over alternative approaches as it attains high accuracy with respect to its core information retrieval task. Keywords: eXtensible Business Reporting Language, XBRL Interoperability, XBRL Calculation Linkbases, Ontology, Semantic Web

## 1. Introduction

In the past decade and a half, eXtensible Business Reporting Language (XBRL) has been adopted as a standard in 22 countries. European countries dominate the push towards XBRL with some 13 nations actively participating. Other notable XBRL jurisdictions include the United States, China, Australia, Korea, and Japan [1]. To be sure, each implementing jurisdiction has had varying levels of success with their unique requirements of the standard. Since its inception, XBRL has made significant progress towards realizing its vision of streamlining the Web-based financial reporting pipeline with an end goal of full automation. The standard contributes to this streamlining by enabling software agents to act on behalf of the consumers of financial reporting data [2]. However, in order for XBRL to serve as a data

# ACCEPTED MANUSCRIPT

representation framework that enables full automation in Web-based financial reporting, it must meet a key requirements<sup>1</sup> of standardizing financial reporting concepts, remaining interoperable while not placing an undue burden on filing entities. The standardization requirement is provided for in the XBRL standard by the development of domain specific XBRL taxonomies. In the US jurisdiction, the US $\mathrm { G A A P } ^ { 2 }$ Financial Reporting Taxonomy (UGT) was initially developed and is frequently updated by the Financial Accounting Standards Board (FASB) subject to approval from the US Securities and Exchange Commission (US SEC). The UGT currently contains 15,000 element definitions for financial reporting concepts, calculation hierarchies and other elements of XBRL taxonomies to be used as a common and comprehensive standard. This approach, in theory, enables the automated consumption of firm disclosures adhering to the standard [3]. However, inherent to the XBRL standard is the notion of extensibility. A trade-off must be made in the creation of taxonomies; although strict standardization enables crosssectional comparability across filers, it impedes the ability of the filers to report idiosyncratic (i.e. firmspecific) business situations. As a necessity for the ubiquitous acceptance of XBRL technology in the US jurisdiction, XBRL remains extensible while striving for standardization [4]. As a result, filers are permitted to extend the base taxonomy (i.e. UGT) with their own, non-standard elements to satisfy their

Unfortunately, the use of non-standard elements greatly jeopardizes the ability of the standard to meet its interoperability requirement. For any three distinct companies’ XBRL financial statements, only 11.92% of their financial information is comparable; in addition, when UGT standard elements are considered alone, interoperability increases only to 17.35% of the financial information represented in the filings [5]. Prior academic research within the domain recognizes the presence of conceptual ambiguity in XBRL filings and attempts have been made to translate XBRL data into ontological structures to resolve the element conflicts [6, 7, 8]. Recent studies [9, 10] present ontology-based approaches to integrate the XBRL filings of multiple companies, enabling investors to perform comparative performance analyses

across companies. Although this work provides a useful starting point for leveraging the promise of XBRL to investors and other stakeholders, there exists a need for a more effective resolution of element heterogeneity across XBRL filings in the US jurisdiction.

In response to the aforementioned need, this study aims to resolve the element heterogeneity issue in XBRL filings thereby improving XBRL interoperability in the US jurisdiction towards full automation of the business reporting pipeline. We modeled the problem of XBRL interoperability using channel theory. The application of this theory leads us to posit that within XBRL calculation linkbases there exist calculation hierarchies that are both necessary and sufficient to express the meaning of any given financial concept. Our specific research question is: How can the hierarchical information contained within XBRL calculation linkbases be used to discriminate between financial concepts in an XBRL filing to the extent that it can constitute an adequate solution to the problem of XBRL interoperability? We developed a framework, Financial Concept Element Mapper (FinCEM), which uses XBRL calculation linkbases to automatically resolve semantic heterogeneity across multiple XBRL filings. In developing our design artifact, we used the XBRL filings of companies in Standard and Poor’s 100 (S&P 100) list. These XBRL filings are accessed through the SEC’s Electronic Data-Gathering, Analysis, and Retrieval (EDGAR) system. The evaluation results show that our design artifact is capable of mapping a financial concept to the set of heterogeneous XBRL elements used to represent it within a corpus of XBRL filings. Our fully automated framework thus represents a significant contribution towards the realization of XBRL interoperability. To our knowledge, the academic literature has neither recognized nor leveraged the full potential of calculation linkbase hierarchies to delineate the meaning of a financial concept expressed in XBRL. The remainder of the paper is organized as follows. Section 2 provides a brief overview of XBRL. Section 3 presents prior work. Section 4 presents the theoretical underpinning for our design choices, the conceptual architecture (FinCEM), the core method (M<sup>3</sup> Plus), and the implementation of our design artifacts. Section 5 shows the results of evaluating the artifact and presents an analysis of these results. Finally, Section 6 concludes the paper.

## 2. The XBRL Standard

XBRL is a machine-readable format for reporting, disseminating, and presenting financial information. Its semantics are expressed using the XML standard for data representation [10]. Designed to enable comparison and evaluation of financial information by automated software agents, XBRL is an alternative to arbitrary financial reporting on the Web. Prior to XBRL, Web-based financial reports were represented in HyperText Markup Language (HTML) and in Portable Document Format (PDF). Specifically, XBRL document. XBRL also specifies relationships between financial terms and other reporting concepts by taking advantage of the XLink specification of the XML standard.

An XBRL report is comprised of taxonomies and an instance document. XBRL taxonomies consist of an XML schema document and a number of XML Link doc ents.<sup>3</sup> Within the XML schema to one and only one financial concept. A financial concept corresponds to a known business reporting construct to which a numerical may be assigned for a specified period or moment in time. XBRL concepts are at minimum described by a name and a type. A concept belongs to one of a defined listing of types. A type specifies the manner in which a fact (usually a currency denominated number) corresponding to a concept may be asserted. A monetary type concept, for example, would have a monetary type. Accordingly, any automated agent parsing an XBRL report would expect a monetary value for every fact corresponding to such a concept. In addition to element definitions of reporting concepts, XBRL taxonomies also specify the relationships between concepts, their documentation, and their labeling. XBRL uses XML Linking Language (XLink) to express these relationships. An XBRL linkbase taxonomy (linkbase) collects these relationships. There are five types of linkbases: calculation, definition, presentation, label, and reference. While the first three linkbase taxonomy documents define inter-concept relationships, the last two linkbase taxonomy documents associate concepts with additional documentation. A calculation linkbase is a collection of calculation relationships between XBRL

concepts. A presentation linkbase defines how a concept is presented relative to another concept, and a definition linkbase describes relationships between two concepts such as “general-special” or “requireselement.” A label linkbase provides human-understandable strings for concepts to support multiple languages.

XBRL taxonomies, taken together, validate the assertions in an XBRL instance document. The provides references to all taxonomy documents associated with an instance document. In other words, the XBRL instance document associates a reporting fact with its semantics in a linked taxonomy. A reporting fact may be read as “net income is \$100,000” which is a value for a concept within some context. See [9] for further details.

## 3. Literature Review

The review below is in two parts. The first part examines extant work on XBRL interoperability. The second part of the review details how our contribution is situated within the broader semantic integration literature, highlighting the novelty of our design artifact within that space.

## 3.1. XBRL Interoperability

We adopted the eight components of information systems design theory (ISDT) in [12, 13, 14] as a framework with which to categorize prior research in the domain of XBRL interoperability. The eight components of an ISDT are: (1) purpose and scope (2) constructs (3) principles of form and function (4) artifact mutability (5) testable propositions (6) justificatory knowledge (7) principles of implementation (8) expository instantiation. The ISDT component, purpose and scope, is a recognition of the belief that any output of design necessarily has purpose or goals. Concomitantly the purpose of a design implies a scope within the context of that design. Constructs are the building blocks of an IS design and, taken together within the context of any particular design, form its causa materialis. Towards its purpose, within its scope, and resulting from its causa materialis, the principles of form and function characterize a design. In IS DSR, principles of form and function take the form of a high-level architecture of the design

# ACCEPTED MANUSCRIPT

product that simultaneously communicates the purpose of the design and its form. Artifact mutability deals with the “emergent properties and behavior” (p. 326) embodied in the design. It is closely linked with the generalizability of a design because it covers its potential, alternative applications. Design science research should be guided by testable propositions, the fifth component of an ISDT. These propositions would claim that artifacts designed in a certain way should produce certain outcomes. A hallmark of “good” design research is its testability against stated objectives and requirements [12]. Linking purpose and scope, constructs, and principles of form and function is the justificatory and explanatory knowledge (the sixth component), “kernel theories” that afford the researcher the ability to structure constructs in a useful way. Principles of implementation deal with the manner in which the design is brought into material being by human actors who wish to use it for its stated ends. Finally, expository instantiation covers the manner in which a design is materialized towards the end of theory exposition. Expository instantiation enables for a rigorous evaluation of the design output with respect to its requirements and purpose. Table 1 provides a summary of our analysis of the literature. Following this we explore some findings from the analysis.

<table><tr><td>Paper</td><td>Purpose and Scope</td><td>Constructs</td><td>Principles of Form and Function</td><td>Justificatory Knowledge</td><td>Principles of Implementation</td></tr><tr><td>Bao et al. [13]</td><td>one-to-one mapping of XBRL elements</td><td>OWL 2 DL; XBRL;</td><td>Creating shared ontology for XBRL specification</td><td>Ontology Modelling</td><td>Unclear</td></tr><tr><td>Radzimski et al. [14]</td><td>mapping of XBRL elements to well defined concepts and linked open data</td><td>SPARQL; RDF; Sesame; LOD; XBRL; Silk;</td><td>Semanric representation of XBRL; Links to LOD;</td><td>Ontology Modelling</td><td>Unclear</td></tr><tr><td>Wunner et al. [8]</td><td>directly addresses XBRL interoperability</td><td>Part-of-speech tagging (POS); (NLP); RDFS</td><td>Heuristics and Machine Learning</td><td>IR and NLP;</td><td>Semi-Automatic</td></tr><tr><td>Chowdhuri et al. [9]</td><td>directly addresses XBRL interoperability</td><td>RDF; XBRL; ReDeFer; SWRL; SPARQL;</td><td>Heuristics and Machine Learning</td><td>IR and NLP;</td><td>Semi-Automatic</td></tr><tr><td>Zhu &amp; Madnick [15]</td><td>directly addresses XBRL interoperability</td><td>Context Interchange Framework (COIN); XBRL;</td><td>Heuristics and Machine Learning</td><td>IR and NLP;</td><td>Semi-Automatic</td></tr><tr><td>Declerk &amp; Krieger [16]</td><td>one-to-one mapping of XBRL elements</td><td>XBRL; PDF; Text Mining; (OWL); (XML); Description Logic (DL); (RDF; RDFS)</td><td>Creating shared ontology for XBRL specification</td><td>Ontology Modelling</td><td>Manual</td></tr><tr><td>Garcia &amp; Gil [17]</td><td>mapping of XBRL elements to well defined concepts and linked open data</td><td>RDF; XML Semantics Reuse Methodology; OWL; Ontology; Semantic Web; WoD</td><td>Creating shared ontology for XBRL specification</td><td>Ontology Modelling</td><td>Semi-Automatic</td></tr><tr><td>Livieri et al. [18]</td><td>one-to-one mapping of XBRL elements</td><td>(KPIs); Ontology; XML; Basic Competency Questions (BCQs); Complex Competency Questions (CCQs); XBRL; OWL; W3C Time ontology;</td><td>Creating shared ontology for XBRL specification</td><td>Ontology Modelling</td><td>Unclear, likely manual</td></tr><tr><td>O'Rain et al. [19]</td><td>mapping of XBRL elements to well defined concepts and linked open data</td><td></td><td>Semantic representation of XBRL</td><td>Ontology Modelling</td><td>Unclear, likely manual</td></tr><tr><td>Debreceny et al. [3]</td><td>directly addresses XBRL interoperability</td><td></td><td>Heuristic based approach</td><td>Practitioner-in-use</td><td>Manual</td></tr><tr><td>Spies [7]</td><td>one-to-one mapping of XBRL elements</td><td>OWL; XBRL; UML; Common Warehouse Metamodel (CWM); Ontology Definition Metamodel (ODM)</td><td>Creating shared ontology for XBRL specification</td><td>Ontology Modelling</td><td>Unclear</td></tr><tr><td>Etudo &amp; Yoon [20]</td><td>Directly addresses XBRL interoperability</td><td>RDF; CBRL; SPARQL;</td><td>Heuristics and Machine Learning</td><td>IR &amp; NLP</td><td>Automatic</td></tr></table>

Table 1 – Summary of Related Work

Purpose & Scope: We have identified and labeled three general variations of purpose and scope that have emerged in the literature: one-to-one variation, Linked Open Data (LOD) variation, and direct solution variation. One-to-one variation is characterized by research towards the representation of XBRL semantics in a Semantic Web language such as OWL or RDF [7, 16, 19, 21]. LOD variation proposes the generation of RDF or OWL representations of XBRL for inclusion in the Web of Data using an LOD approach [17, 20, 22]. The purpose and scope of ISDTs in the direct solution variation centers on providing a direct solution to the problem of XBRL interoperability, using semantic technologies only as enabling constructs. Semantics in these works are used to represent relationships between XBRL concepts on the basis of similarity [8, 9, 18]. One-to-one and LOD variation are limited solutions to XBRL interoperability. Interoperability, in these two variations, is simply what follows from a good representation of XBRL semantics. The assumption that interoperability follows from a “good” representation of XBRL semantics is not tested in these works.

Constructs: There is a great deal of overlap with respect to the constructs used to build the various ISDTs that we reviewed. While we only searched for scholarly work using the term “XBRL interoperability” in the title, abstract, or keywords, we found that, with the exception of [16], all the articles under review make use of an ontology representation language or some subset of the suite of Semantic Web technologies [21] in developing their respective design theories. This state of affairs is fairly intuitive as Semantic Web technologies naturally lend themselves to problems of data interoperability; “Semantic Web languages, e.g., RDF and OWL, are inherently built with a graph-based open data model and naturally support integration” [13].

Principles of Form & Function: As researchers have sought to leverage Semantic Web technologies (Semantic Web languages in particular) to create interoperable XBRL reports, two approaches to form and function have appeared [22]. The two are, (1) creating a shared ontology for the XBRL specification [7, 16, 19, 20, 21] and (2) using heuristics, machine learning, and NLP to produce representations of mappings between XBRL concepts. The creation of upper level ontologies is central to the first approach, creating a shared ontology for the XBRL specification. Upper level ontologies provide a high-level, shared conceptualization of a domain. The approaches that adopt the creation of a shared ontology of the XBRL specification, without exception, provide no guidance as to how XBRL conceptual equivalence should be established between XBRL instances and taxonomies on one hand and the shared ontology on the other hand. This is not a trivial oversight. The absence of such guidance stunts the potential of the approach for eliminating XBRL interoperability problems.

The second approach to form and function involves using heuristics and machine learning to infer mappings between XBRL elements and their conceptual equivalents. Using various measures of similarity, the studies in [8, 9, 18] document approaches to primarily identifying relationships of

equivalence between XBRL elements and financial concepts of interest. This second approach is more in keeping with the objective of XBRL interoperability.

Principles of Implementation: We do not find any convincing account of an automatic approach to XBRL interoperability. Those papers which use the first approach to form and function lack a robust discussion of the manner in which the resultant shared ontologies can be implemented over a corpus of XBRL documents and the manner in which those ontologies can be changed over time to match reporting practices (see artifact mutability). The papers that take the second approach to form and function do provide, by their very nature, details with respect to principles of implementation. All three of the papers taking the second approach [8, 9, 18] are semi-automatic, requiring human intervention at some point in their real-world implementations. Indeed, the problem of semantic integration has yet to be met with fully automatic approaches [22].

Testable Propositions & Expository Instantiations: Many of the papers reviewed either fail to instantiate their proposed methods, or provide too little detail in that regard [7, 16, 18, 21, 22]. For those studies where the proposed approaches are instantiated, we note that the instantiation does not test their central propositions [19, 20].

The above analysis results in three main gaps in the literature that our work, as presented herein, aims to fill. First, with respect to the shared ontology approach, there is no guidance given, in any of the reviewed papers as to how to establish relationships of equivalence between the XBRL filings and the upper level ontology. In this paper we make an account of, instantiate, and evaluate a method and overarching framework that establishes these relationships of equivalence between the XBRL filing and an upper level ontology. [7] is an exception to this limitation. The authors do provide a mechanism to these ends, but their design suffers from other limitations. The second limitation identified is that where principles of implementation are concerned, the existing literature lacks clarity regarding how proposed designs may be put to use. In addition, we find that there are no fully automatic designs for the mitigation of the problem of XBRL interoperability. Finally, the third limitation is concerned with the lack of sound theoretical underpinnings with respect to existing approaches to the problem of XBRL interoperability.

# ACCEPTED MANUSCRIPT

Research in this domain has been largely a-theoretical.

In order to fill the aforementioned gap, we significantly extend the ontology-based approaches by Chowdhuri et al. [9] and Etudo & Yoon [20] to develop a comprehensive framework, called FinCEM. The improvements can be summarized along five categories: automaticity, theoretical underpinning, robustness of structural information, learning, and performance. The work by Chowdhuri et al. [9], OXFD, is a semi-automatic method, which requires manual tagging of reported quantities for financial elements. Manual tagging of reported quantities for financial elements in generating a training data set requires a significant amount of time and effort. In order to more efficiently address the semantic heterogeneity issues, FinCEM eliminates the manual tagging of reported quantities for financial elements. The design artifact by Etudo and Yoon [10], $\mathbf { M } ^ { 3 } .$ , is an automatic method just as FinCEM; however, FinCEM is superior to $\mathbf { M } ^ { 3 }$ in other accounts. With respect to theoretical underpinning, $\mathbf { M } ^ { 3 }$ Plus draws upon Channel Theory, which gives the theoretical basis of using structural information for XBRL interoperability. Both OFXD and $\mathbf { M } ^ { 3 }$ lack theoretical foundations.

Additionally, the novelty/superiority of proposed solutions can be assessed with respect to the robustness of structural information. The structure of an ontology can be described in terms of a graph, where each class is a node and the relationships between the classes are edges between the nodes. The structural similarity generally refers to the similarity between two classes in terms of their interconnecting nodes and edges. One type of edges used in any ontology is isSubClassOf, which represents hierarchical relationships between nodes. Generated from XBRL calculation linkbases, our calculation linkbase ontology extensively uses isSubClassOf to represent hierarchical relationships between financial concepts and their respective sub-concepts, as well as the associated calculation rules. Therefore, in this study, the structural similarity specifically refers to the similarity between two classes in terms of parents (super classes), children (subclasses), and sibling classes. The comprehensive structural approach refers to the use of all structural information, including children similarity, sibling similarity, and parent similarity, in resolving heterogeneous representations of the same financial concept. OFXD does not use structural information. $\mathbf { M } ^ { 3 }$ Plus and $\mathbf { M } ^ { 3 }$ share their reliance on structural information. However, $\mathbf { M } ^ { 3 }$ is quite limited in that it only takes into account the similarity between children classes in the calculation linkbase hierarchy. Drawing upon Channel Theory, M Plus extends this idea by including parent and sibling $\mathbf { M } ^ { 3 }$ similarity measurements. Further, with respect to learning, there is no other learning approach in the domain. FinCEM allows the $\mathbf { M } ^ { 3 }$ Plus method to recursively traverse the document space and learn new equivalence relationships when the existing FinOnt structure does not suffice. Neither OFXD nor M have $\mathbf { M } ^ { 3 }$ this capability. Finally, the performance of $\mathbf { M } ^ { 3 }$ Plus is evaluated with a larger test dataset over two years. We demonstrate in this paper the significant enhancements the method enjoys when employing the more robust set of structural similarity measures.

## 3.2 Semantic Integration Approaches and FinCEM

Semantic integration in the academic literature is set against the backdrop of integrating independently conceived knowledge bases. Given two such knowledge bases, many methods opt to generate a unifying knowledge model that serves to express equivalent relationships between them. This backdrop has led to the problem of semantic integration being conceived of as an essential duality. The essential duality, per [23], is that information flow crucially involves both concepts and instances of concepts. This is the essence of channel theory as it applies to our proposed solution. The case of semantic integration across XBRL filings is framed in this manner. We see our contribution as a novel exposition and a validation of this kernel theory. Research in the semantic integration domain, generally, either implicitly or in a few cases explicitly, notably [24], adopts this model. Contributions in the semantic integration domain are therefore generally of the form of novel operationalizations of these ideas. Our work is no exception. Below, we outline the positioning of our contribution as novel in this space.

Our proposed solution FinCEM uses an ontology-based semantic integration method called $\mathbf { M } ^ { 3 }$ Plus. The specific approach used in $\mathbf { M } ^ { 3 }$ Plus falls into the category of structure based semantic integration methods. A structure-based semantic integration method utilizes the structural information in interrelating information from diverse sources. We identify three types of structure based semantic integration methods

# ACCEPTED MANUSCRIPT

in the literature: (1) Similarity Flooding (SF), (2) Anchor-PROMPT, and (3) Anchor Flood [25]. Similarity Flooding [26] is based on the notion of similarity propagation, which is the assumption that when any two elements from different ontologies are found to be similar, then the similarity of their adjacent elements increases. A fix point computation is carried out over a similarity propagation graph to derive similarity scores. In this approach, the only limit to the characteristics of elements that may be used to compute similarity is the expressivity of the language or framework in which the ontology was defined. Conversely, the $\mathbf { M } ^ { 3 }$ Plus approach determines structural similarity by aggregating only the lexical similarity of neighboring concepts/elements<sup>4</sup>. The Anchor-PROMPT method [27] takes two elements from each ontology as anchors. These two elements have been determined to be equivalent across the tobe-merged ontologies. It then represents in a directed graph all possible pathways between the two elements in each ontology. Given this representation, it computes similarity between elements on the same level across the graphs (where each graph comes from one of the two ontologies). The pairwise anchoring technique means Anchor-PROMPT is not robust in situations where the to-be-merged ontologies have radically different hierarchical depths. Further, the approach takes into account “slots” or object properties defined against ontological elements. Our approach shows good performance without leveraging slots. Finally, [28] describe their Anchor-Flood approach, which is in many ways a hybrid of the other two discussed here. It accordingly also differs from $\mathbf { M } ^ { 3 }$ Plus by taking into account instance data and object properties where M<sup>3</sup> Plus does not.

Above we outlined the key differences between $\mathbf { M } ^ { 3 }$ Plus and existing structure based semantic integration methods. First, we noted that $\mathbf { M } ^ { 3 }$ Plus uses a much sparser set of structural indicators. It relies only on hierarchical IS-A relationships where other approaches also take into account slots or object property definitions. In addition, we noted that $\mathbf { M } ^ { 3 }$ Plus, absent hierarchical information, only takes into account the lexical similarity of ontology element names while providing acceptable performance. Other approaches in the literature (SF in particular) can take into account metadata associated with ontological or schema elements. The next section details the theoretical foundation of our design artifact, its relevance to our domain, and its central contribution to our design process and artifact.

## 4. Theoretical Framework

Channel theory (also referred to as information flow theory or IF-theory) informs our design artifact. We introduce channel theory below and discuss its relevance to our problem situation.

## 4.1 Representational Systems

The lack of interoperability in XBRL is rooted in the heterogeneous representations of financial concepts across XBRL filings. XBRL is a representation language. When nested in the context of US GAAP and end user interpretation of the representation, the XML-based syntactical representations in XBRL express some target concept in the world of financial reporting. We assume that XBRL does this perfectly, such that the representation of any given concept in any given XBRL filing is accurate and complete. Channel theory provides a precise means through which we can frame this problem. Framing the problem in terms of channel theory results in a sound basis on which to design candidate solutions towards XBRL interoperability.

Based on channel theory [23], we define a representational system as follows for our purposes:

1. A representation system, $R S = ( C , L )$ , is made up of a classification, C, and local logic, L. C consists of a set of tokens to be classified, a set of types into which tokens will be classified and binary relations specifying which tokens are classified into which classes. We conceive of L as the set of system (local) specific logics that enable such classification.

2. A communication/information channel in the binary case = (f, g) where f : A ↔ C, g : B ↔ C where A is called the source, B the target. A communication channel specifies a codomain, i.e. C, that enables the mapping of source to target. The local logic of the enclosing representational system, L, operates on the classification, C, by setting the scope of what is possible within the representation system.

3. Tokens of A are representations in RS, and a token, a, is a token of A (source), and b is a token of B (target). Tokens are instances of a type. The token a is simply an instance of A.

4. Types are relevant here, and a set of types $T P _ { A }$ of the source classification, A, indicates the type, $\beta ,$ of the target classification subject to the constraints on the core logic, L. Finally, “[t]he content of a token, a, is the set of all types indicated by its type set. The representation a represents b as being of type $\beta$ if a represents b and $\beta$ is in the content of a” [23].

![](/api/attachments/STJNC9F6/fulltext/images/18de90c61ea0559cc84771c13df5401fcb15419a83b1a43c42121a36e85a5030.jpg)  
Figure 1 – A Representational System [23]

Most illustrations used to depict information flow theory are similar in appearance to figure 1, above. However, instead of L, these depictions typically place C on top of the figure in the binary cases. What is being depicted is a communication/information channel (in our case, f: $\mathbf { A }  C , g : B  C )$ Figure 1 is instead a depiction of a representational system. We place the local logic L at the top of the figure to highlight Barwise & Seligman’s third principle of information flow: “It is by virtue of regularities among connections that information about some components of a distributed system carries information about other components” [23, p. 35]. For our purposes, the local logic represents the regularities among system components that enable the existence of communication/information channels within the system. It is the local logic of financial reporting in the United States that is of interest in our operationalization of channel theory. FinCEM seeks to generate classifications by approximating the local logic of financial reporting in the United States.

## 4.2 Modeling XBRL as a Representational System

A given XBRL filing is an instance of a representation (a source, A, in figure 1) within a representation system. The target, B, is a government-mandated disclosure regarding the financial position and performance of a firm over a specified period and at a moment in time. For each filing there exist “types” which correspond to XBRL elements in a taxonomy. There also exist “tokens” which correspond to instances of those types being used to assert reporting facts in the given filing. With respect to the target, types correspond to financial concepts as recognized in GAAP with tokens being instances where these concepts are used to define a disclosure in a particular financial statement. L, the local logic of this system, is the set of regularities (logical constraints) that permit information flow in the system. In other words, L represents the XBRL framework as understood by both filers and downstream consumers of financial reports and as formalized in UGT. L, therefore, models the manner through which the representation of a financial concept in an XBRL filing can be inferred as equivalent to an actual US GAAP financial reporting concept.

Channel theory leads us to posit that L is stable across all XBRL filings in the same jurisdiction. Were this not the case, no user of XBRL would be able to detect equivalence relationships between XBRL financial concepts and US GAAP financial concepts. In other words, a stable local logic, L, is a necessary condition in many representational systems. It serves as a prerequisite for information flow between a representation and its target, and, as a result, is both a necessary and sufficient condition for the interpretation of a representation. In addition, the target is stable in the short run (assuming that changes to US GAAP are a slow process where all stakeholders are involved). However, while the local logic is stable, the set of types found in each classification (XBRL filing) varies from filing to filing.

Consider Figure 2. Each triangle is a rendition of a representation system corresponding to an XBRL filing. The XBRL filings are the filings of two distinct firms within the same period. A and B are classifications<sup>5</sup> corresponding to the representation, the source, and the realities that are represented, the target, respectively. To illustrate the problem of XBRL interoperability, we demonstrate the special case where both filings represent exactly the same reality, B, using varying sets of types $T K _ { A }$ and $T K _ { A } .$ The local logic, L, is stable between the filings as the same standard is being used for the reporting activities.

![](/api/attachments/STJNC9F6/fulltext/images/b491fdcf10a932375b871d1c9ba131b3940fbe2698ccecb53298de0e751692fe.jpg)  
Figure 2 – XBRL Interoperability in terms of IF-Theory

With insight from channel theory, we see that the regularities in the information system (i.e. XBRL financial reporting) enable the interpretation of heterogeneous representations into the same reality. Put another way, the regularities within the system are the catalyst for information flow between the representation and the targeted reality. This revelation informs our design process with respect to providing a solution to XBRL interoperability: we look at the regularities across XBRL filings (these regularities are intrinsic to the XBRL standard) for semantics both necessary and sufficient to identify and discriminate between financial concepts in XBRL filings.

## 5. Framework for XBRL Interoperability: FinCEM

Figure 3 presents the architecture of our proposed framework, called Financial Concept Element Mapper (FinCEM). Our framework operates in two phases: 1) development and 2) operation with adaptive learning. The first phase is a process that culminates in the generation of an upper level ontology, FinOnt, based on a set of training calculation linkbase ontologies. The second phase ensures that even after deployment, FinOnt will be continuously improved as the framework engages in a constant learning process.

The conversion of a set of XBRL calculation linkbases initiates the development phase of the framework. These calculation linkbase documents are analogous to an unlabeled set of training examples. Calculation linkbase ontologies provide a convenient representation of the calculation relationships between XBRL elements. In the next section, we describe the automated mapping process used to generate these calculation linkbase ontologies. The M Plus method is applied on the set of linkbase $\mathbf { M } ^ { 3 }$

ontologies and a set of financial terms of interest to an investor or a financial analyst. $\mathbf { M } ^ { 3 }$ Plus automatically maps the end user terms to financial elements in XBRL on the basis that a financial element is equivalent to an investor term where the element and term refer to the same financial concept. These mappings are rendered to an ontology, FinOnt, completing the development portion of the framework.

The operation and learning phase of FinCEM is the application of FinOnt on a set of XBRL filings that are of interest to the user of the framework. As FinOnt establishes relationships between the end user’s query terms (“Investor Vocabulary” in Figure 3) and XBRL elements, it is possible to query a set of XBRL filings for the XBRL elements and their values corresponding to the end user’s terms. Where a term cannot be resolved to an XBRL element in a particular document, the development process is reinitiated.

![](/api/attachments/STJNC9F6/fulltext/images/d1dcdab737cfb30f9226c1cc2f3a73183cad0e17a1232c9f4b58bde3865910de.jpg)  
Figure 3 – Architecture of FinCEM

## 5.1 Calculation Linkbase Ontology Generator

Leveraging the structural information expressed within calculation linkbases is essential to the functioning of our approach. We extract this structural information and explicitly represent it in the form of an ontology. We do this automatically as the mapping from linkbase to linkbase ontology is straightforward. The top section of Figure 4 is a rendition of a portion of a calculation linkbase ontology. Calculation linkbase ontologies are represented using the Resource Description Framework (RDF), an XML-based ontology language. The calculation hierarchies expressed in a calculation linkbase are

converted into a series of subsumption relationships (“is-a”). Figure 4 also shows a snippet of XML from a calculation linkbase that corresponds to a subset of the linkbase ontology shown. The labels indicate how this correspondence is established.

Calculation linkbases are a collection of calculationArc elements. A calculationArc expresses a relationship between two XBRL financial elements. Each calculationArc element contains the attributes @xlink:from and @xlink:to. The value of the @xlink:from attribute corresponds to a financial element that is an aggregation, in the summation sense of the word, of the financial element corresponding to the value of the @xlink:to attribute. In the example in Figure 4, AssetsCurrent is a child of Assets. In terms of a calculation hierarchy, AssetsCurrent is a component of Assets such that it is one of the line items that make up Assets.

![](/api/attachments/STJNC9F6/fulltext/images/9cd623a16e16393a2642f85725108c4e3e1ab33839a8b532866bb9830d5d88de.jpg)

## 5.2 Similarity Measurements

In order to leverage the structural information in XBRL calculation linkbases towards improving interoperability, we require an approach that simultaneously quantifies the structure of an XBRL financial concept while providing a measure of similarity between its structure and the structure of another XBRL financial concept.

We approximate the structure of a given XBRL financial concept as shown in formula 1 where $S t r u c t _ { x t }$ represents this approximation for an XBRL financial concept xt. Say $p t _ { x t }$ is a vector of parent concepts, $c t _ { x t }$ is a vector of child concepts and ${ { s t } _ { x t } }$ is a vector of sibling concepts, all with respect to xt. The union of these vectors yields a concept-space that we hypothesize is sufficient to discriminate between XBRL concepts.

## Formula 1: $_ { \cdot x t } = p t _ { x t }$ U $c t _ { x t }$ U stxt

To compute the similarity between two XBRL concepts, we consider the similarity between the concepts themselves, and the similarity between each concept’s concept-space $( S t r u c t _ { x t } )$ as determined from a calculation linkbase ontology. Leveraging the generalized similarity formula given in formula 2, [29], we can compute the similarity between the terms themselves by considering the ratio of terminological overlap to the union of the two terms. We also apply the same formula for concept spaces such that we can compute the similarity between two concept spaces X & Y. In computing the similarity between two concept spaces, it is also possible to weight the individual components of a concept space: $p t _ { x t } , c t _ { x t } ,$ and $s t _ { x t } .$

Formula 2:

$$
\operatorname{Sim} (X, Y) = \frac {X \cap Y}{X \cup Y}
$$

## 5.3 Multi-Ontology Multi-Concept Matrix Plus Learning $( M ^ { 3 } P l u s )$ Method

The ability of FinCEM to improve the interoperability of XBRL filings by resolving semantic heterogeneity is directly provided by the $\mathbf { M } ^ { 3 }$ Plus method. Given a financial concept of interest to an end user and a set of XBRL filings from which the user wishes to extract facts about the financial concept, our approach retrieves values corresponding to the financial concepts for all firms in the set of XBRL filings within a pre-specified context. The M Plus method requires as its input a set of financial terms from the $\mathbf { M } ^ { 3 }$ end user (each term corresponds to a financial concept), a training corpus of XBRL calculation linkbases, and a set of complete 10-K XBRL filings of interest to the end user. M<sup>3</sup> Plus significantly extends the $\mathbf { M } ^ { 3 }$ $\mathbf { M } ^ { 3 }$ approach, presented in [20], where this earlier approach uses only one of the M Plus’s three structural $\mathbf { M } ^ { 3 }$

similarity measurements and is not imbued with any learning capabilities. Full details regarding the operation of $\mathbf { M } ^ { 3 }$ Plus are provided in Table 2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Let F be a financial term of interest to the end user
Let E be the set of all XBRL financial elements asserted as equivalent to F
Let ET$_{n}$ be the n$^{th}$ element in E
Let O be the set of calculation linkbase ontologies in the training corpus
Let CLO$_{j}$ be the j$^{th}$ calculation linkbase ontology in O
Let SFC be a vector of XBRL financial elements likely similar to F
Let FC$_{jk}$ be an element of SFC which is the k$^{th}$ financial concept from the j$^{th}$ calculation linkbase ontology.
Let WL be a weight assigned to lexical similarity
Let WC be a weight assigned to children similarity
Let WP be a weight assigned to parent similarity
Let WS be a weight assigned to sibling similarity
Let T$_{j}$ be a similarity threshold applied for the financial concepts of the j$^{th}$ calculation linkbase ontology
Let TCS$_{jk}$ be the sum of the similarity coefficients for the k$^{th}$ financial concept from the j$^{th}$ calculation linkbase ontology

M$^{3}$ Plus () {
    for each CLO$_{j}$ ∈ O do
    FindCandidateFinancialConcepts (SFC, CLO$_{j}$)
    end for each
    FindMostSimilarFinancialConcepts (SFC, TCS)
    append max$_{FC_{jk} \in SFC}$ TCS$_{jk}$ to E
    for each CLO$_{j}$ ∈ O do, where CLO$_{j}$ doesn't include E
    FindEquivalentToMostSimilarFinancialConcept (SFC, TCS, E)
    append max$_{FC_{jk} \in SFC}$ TCS$_{jk}$ to E
    end for each
    for each ET$_{n}$ ∈ E do
    Create ET$_{n}$ as a subclass of F
    end for each
}

FindCandidateFinancialConcepts (SFC, CLO$_{j}$) {
    for k = 0 to p do, where p is FC$_{jk}$ the number of financial concepts in CLO$_{j}$
    Let FC$_{jk}$ be the k$^{th}$ financial concept from the jth calculation ontology
    for each FC$_{jk}$ ∈ CLO$_{j}$ do
    FC$_{jk,sim}$
    append FC$_{jk}$ to CLJS(FC$_{jk}$,F)
    end for each
    end for
    largestLexSim$_{j}$ ← max$_{FC_{jk} \in SFC}$ CLJS(FC$_{jk}$,F)
    T$_{j}$ ← largestLexSim$_{j}$ - (0.2 * largestLexSim)
    for each FC$_{jk}$ ∈ SFC do
    if CLJS(FC$_{jk}$,F) &lt; T$_{j}$ then // the j$^{th}$ index has to match for CLJS(FC$_{jk}$,F) and T$_{j}$
    add FC$_{jk}$ to SFC
    end if
    end for each
}

FindMostSimilarFinancialConcepts (SFC, TCS) {
    Let Sim(FC$_{jk}$, FC' $_{jk}$) ← (WL * LexicalSim + WC * ChildrenSim + WP * ParentSim + WS * SiblingSim)
    between FC$_{jk}$ and FC' $_{jk}$, where FC$_{jk} \neq FC'_{jk}$
    for each FC$_{jk}$ ∈ SFC do
    Let V$_{jk}$ be a vector of similarity coefficients for the k$^{th}$ financial concept in the j$^{th}$ linkbase ontology
    for each FC' $_{jk}$ ∈ SFC do // FC$_{jk} \neq FC'_{jk}$
    V$_{jk}$ ← Sim(FC$_{jk}$, FC' $_{jk}$)
    end for each
end for each
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Let CEM be the set of all  $V_{jk}$  CEM
for each  $V_{jk} \in CEM$  do
    Let  $TCS_{jk}$  be the sum of all  $\text{Sim}(FC_{jk}, FC'_{jk}) \in V_{jk}$ 
    end for each
}

FindEquivalentToMostSimilarFinancialConcept (SFC, TCS, E) {
    for each  $FC_{jk} \in SFC_{j}$  do
    Let  $V_{jk}$  be a vector of similarity coefficients for the  $k^{th}$  financial concept in the  $j^{th}$  linkbase ontology
    for each  $ET_{n} \in E$  do
    Find Parent, Children, and Sibling of  $FC_{jk}$  and  $ET_{n}$ $\text{Sim}(FC_{jk}, ET_{n}) = (\text{WL} * \text{LexicalSim} + \text{WC} * \text{ChildrenSim} + \text{WP} * \text{ParentSim} + \text{WS} * \text{SiblingSim})$ 
    append  $\text{Sim}(FC_{jk}, ET_{n})$  to  $V_{jk}$ 
    end for each
    end for each

Let CEM be the set of all  $V_{jk}$  //the set of all  $V_{jk}$  constitutes the CEM matrix
for each  $V_{jk} \in CEM$  do

Let  $TCS_{jk}$  be the sum of all  $\text{Sim}(FC_{jk}, ET_{n}) \in V_{jk}$ 
    end for each
end for each
}
</div>

Table 2: Logics of the M<sup>3</sup> Plus Method

Given a set of financial terms of interest to the end user, the $\mathbf { M } ^ { 3 }$ Plus method examines each term in the set. For each term $F ,$ the $\mathbf { M } ^ { 3 }$ Plus method uses the FindCandidateFinancialConcepts method to extract XBRL financial concepts from each of the resultant calculation linkbase ontologies $C L O _ { j }$ . For each of the XBRL financial concepts $F C _ { j k , }$ extracted from the calculation linkbase ontologies, the method examines the Jaccard Similarity [29] with F. We select an $F C _ { j k }$ only if the similarity between F and $F C _ { j k }$ is greater than or equal to 80% of the largest Jaccard similarity between $\mathrm { F }$ and $F C _ { j } .$ This $F C _ { j k }$ is then added to a vector SFC, which represents the set of all XBRL financial concepts in the training set of calculation linkbase ontologies that are potentially equivalent to a given F. For each F given by the end user, there is a corresponding SFC.

Once SFC for F is built from all calculation linkbase ontologies in the training corpus, the $\mathbf { M } ^ { 3 }$ Plus method calls for the FindMostSimilarFinancialConcept method. For an XBRL financial concept $F C _ { j k }$ in SFC, this method performs a similarity computation between $F C _ { j k }$ and $F C _ { j k }$ <sub>’</sub>. In other words, for each $F C _ { j k }$ , a collection of all other XBRL financial concepts in SFC which are not terminologically equivalent to $F C _ { j k }$ is compiled. $F C _ { j k }$ <sub>’</sub> is the $k ^ { t h }$ of these concepts sourced from the $j ^ { t h }$ calculation linkbase ontology.

# ACCEPTED MANUSCRIPT

For each $F C _ { j k }$ a similarity computation is conducted against $F C _ { j k }$ . This similarity computation is the weighted sum of lexical similarity (LS), parent similarity (PS), children similarity (CS), and sibling similarity (SS) (see formula 3). The weights of these components are determined through a series of experiments, which is discussed in Section 6.3. The result is a matrix of our custom similarity coefficients where each coefficient measures the overall structural and lexical similarity between two XBRL financial concepts sourced from the calculation linkbase ontologies in a training corpus. With K XBRL financial concepts represented in the matrix, any $F C _ { j k }$ is represented in $K { - } I = K ^ { \prime }$ similarity coefficients. For each $F C _ { j k }$ a cumulative similarity coefficient, $T C S _ { j k } ,$ , is derived as shown in formula 4, where $T C S _ { j k }$ is equal to the sum of the similarity between a given $F C _ { j k }$ and all $F C _ { j k }$ <sub>’</sub>. In formula 5, we demonstrate the criteria for determining that an XBRL financial concept, $F C _ { j k } ,$ is conceptually equivalent to an end user provided financial term, F. The FindMostSimilarFinancialConcept method returns a vector of TCS for all financial concepts in SFC. Given SFC, the vector of candidate XBRL financial concepts (recall that this vector is generated based on the lexical similarity between F and all XBRL concepts in the training corpus of calculation linkbase ontologies), the $\mathbf { M } ^ { 3 }$ Plus method then selects the $F C _ { j k } ,$ where $F C _ { j k } \in S F C ,$ , that corresponds to the largest $T C S _ { j k }$ as equivalent to F (see formula 5). $F C _ { j k }$ is added to a vector E as a financial concept equivalent to $F .$

For every company in the training corpus that does not use $F C _ { j k }$ (the $k ^ { t h }$ XBRL financial concept from the $j ^ { t h }$ calculation linkbase ontology posited to be equivalent to the user supplied financial concept F), the $\mathbf { M } ^ { 3 }$ Plus method calls for the FindEquivalentToMostSimilarFinancialConcept method. For each financial concept $F C _ { k }$ in the calculation linkbase ontology, the $\mathbf { M } ^ { 3 }$ Plus method computes a Jaccard similarity coefficient between F and $F C _ { k } .$ All $F C _ { k }$ where the similarity figure exceeds the threshold given above are added to a new SFC vector of similar XBRL financial concepts. For each financial concept $F C _ { k } \in S F C$ in the calculation linkbase ontology for the company, the FindEquivalentToMostSimilarFinancialConcept method executes the operation in formula 6, which computes the sum of $( F C _ { j k } , F C _ { k } )$ for all $F C _ { k } \in$ SFC. The method then returns the vector of TCS in which each element is the sum of all $S i m ( F C _ { j k } , F C _ { j k } ^ { , } )$

The $\mathbf { M } ^ { 3 }$ Plus method adds the $F C _ { k }$ that corresponds to the largest $T C S _ { k } , \operatorname* { m a x } _ { F C _ { k } \in S F C } C S _ { k }$ , to the vector E as a financial concept equivalent to F. Each financial concept in the vector E is created as a subclass of F in FinOnt. This process is repeated for every F. When this iterative process is completed, FinOnt specifies relationships of equivalency between terms supplied by an end user and the more formal XBRL financial concepts, thereby becoming our topmost level ontology.

Formula 3: $\begin{array} { r } { { S i m } \big ( F C _ { j k } , F C _ { j k ^ { \prime } } \big ) = { C S } \big ( F C _ { j k } + F C _ { j k ^ { \prime } } \big ) + { S S } \big ( F C _ { j k } + F C _ { j k ^ { \prime } } \big ) + { P S } \big ( F C _ { j k } + F C _ { j k ^ { \prime } } \big ) + { L S } \big ( F C _ { j k } + F C _ { j k ^ { \prime } } \big ) } \end{array}$

Formula 4:

$$
T C S _ {j k} = \sum_ {F C _ {j k} ^ {\prime} \in S F C} \operatorname{Sim} \left(F C _ {j k}, F C _ {j k} ^ {\prime}\right); F C _ {j k} \neq F C _ {j k} ^ {\prime}
$$

Formula 5: $\operatorname* { m a x } _ { F C _ { j k } \in S F C } C S _ { j k }$

Formula 6: $T C S _ { k } = \sum _ { F C _ { k } \in S F C } S i m ( F C _ { i j k } , F C _ { k } ) ; F C _ { i j k } \not = F C _ { k }$

## 5.4 Adaptive Learning

Given the FinOnt representation created by the $\mathbf { M } ^ { 3 }$ Plus method, FinCEM can begin to retrieve XBRL financial concepts and their corresponding values from a set of company filings, XBRL instance documents, that are of interest to the end user. For each company’s filing that is of interest to the end user, the learning process occurs if and only if the filing does not contain an XBRL term that matches the equivalent terms in FinOnt. For the learning process, FinCEM re-executes the $\mathbf { M } ^ { 3 }$ Plus method for a financial concept F<sub>i</sub> given the calculation linkbase ontology for this new errant filing. In developing an instance of FinCEM, we used JAVA and several semantic web technologies. Specifically, the RDF converter uses an RDF-aware utility called TopBraid Composer to convert XML documents into RDF ontologies. To extract the classes and their contextRef in XBRL instance ontologies, we used the JENA framework which is a Java-based framework for building a Semantic Web application. It provides an API for reading, processing, and writing RDF data, as well as a SPARQL query engine [30]. We also used Protégé $5 . 1 ^ { 7 }$ in examining the RDF ontologies.

## 6. Evaluation

## 6.1 Evaluation Metrics

Our evaluation philosophy is grounded in the experimental approach, and we adopt the formal ontology evaluation method developed by Yu, Thom & Tam [31]. The formal ontology evaluation method in [31] defines a derived ontology to be evaluated as $O = \{ O _ { c } , O _ { i } , O _ { r } \}$ , where $O _ { c }$ is the set of concepts, $O _ { i }$ is a set of instances, and $O _ { r }$ is a set of relationships between $O _ { c }$ as well as a set of relationships between $O _ { i } .$ The Frame of Reference is the target ontology and is defined as $F = \{ F _ { c } , F _ { i } , F _ { r } \}$ where $F _ { c }$ is the set of concepts, $F _ { i }$ is a set of instances, and $F _ { r }$ is a set of relationships between $F _ { c }$ as well as a set of relationships between $F _ { i } .$ Adopting [33, 34], we use the precision and recall metrics to evaluate the quality of a derived ontology, O, with respect to the target ontology, F. The precision ratio describes the proportion of all retrieved documents that are relevant [33]. In the context of FinCEM performance, this ratio measures the proportion of XBRL elements correctly retrieved. The recall ratio represents the proportion of relevant documents in the entire relevant document space that are retrieved by an information retrieval approach [33]. In the context of FinCEM performance, this ratio measures the number of XBRL elements asserted to be equivalent to a financial concept as a proportion of all XBRL elements that are relevant to the financial concept. The F-measures is the harmonic mean of precision and recall and is specified as:

$$
F M e a s u r e = 2 \cdot \frac {p r e c i s i o n \cdot r e c a l l}{p r e c i s i o n + r e c a l l}
$$

Using these three scores, we can develop a comprehensive view of the quality of the equivalence relationships represented in FinOnt, which FinCEM automatically generates. The quality of FinOnt directly measures the extent to which FinCEM benefits XBRL interoperability; higher precision and recall of FinOnt indicate better FinCEM performance.

# ACCEPTED MANUSCRIPT

## 6.2 Evaluation Data and Frame of Reference

We use the annual financial reports (10-K) of the 92 firms listed in the S&P 100 for the fiscal years ending in 2011 and 2012; 8 of the S&P 100 firms do not have XBRL filings in 2011 and 2012. The S&P 100 includes a wide variety of industries whose XBRL filings are very different from each other. Of the S&P 100 firms, we used a randomly selected hold-out sampling method. Further, in order to test the generalizability of our proposed solution over multiple years, we chose a training data set only from the XBRL filings in 2011. As a result, our model training set consists of the 2011 XBRL filings of 10 randomly selected firms. The design artifact is trained using XBRL format 10-K annual reports for 10 firms for the fiscal year 2011 (FY 2011). We use XBRL format 10-K annual reports for 82 firms in FY2011 and for all 92 firms in FY 2012 for the FinOnt testing. We analyzed the effect of our hold-out sample size on the performance and found that there was no benefit to a training set greater than 10 firms. Drawing upon the widely used F-Score developed by Piotroski [34] for the analysis of firms’ performance, we identify specific financial concepts necessary for the calculation of F-Score to evaluate the three financial conditions: profitability, financial leverage/liquidity, and operating efficiency. Profitability assesses the ability of a company to generate funds internally and is used in the measurement of Return on Assets, Net Cash Provided by Operating Activities, and Accrual. Financial leverage indicates a snapshot of a company’s capital structure and its ability to meet future debt service obligations. The two indicators of financial leverage are Current Ratio and Common Stock. Operating efficiency is measured by Asset Turnover. The calculation of those ratios necessary for computing the Fscore requires the value of the nine specific financial concepts listed in Table 3. We then develop the frame of reference by manually extracting the XBRL terms used to report those nine financial concepts from the 2011 XBRL filings of 82 firms and the 2012 XBRL filings of 92 firms using the “interactive data” tool available for XBRL filings on SEC’s EDGAR database. Our frame of reference is used to evaluate a number of versions of FinOnt developed using various experimental configurations of the M<sup>3</sup> Plus method.

<table><tr><td colspan="3">Financial Concepts in Frame of Reference</td></tr><tr><td>1.</td><td>Cash Generated By Operating Activities</td><td>6. Total Current Assets</td></tr><tr><td>2.</td><td>Common Stock</td><td>7. Total Current Liabilities</td></tr><tr><td>3.</td><td>Long Term Debt</td><td>8. Total Liabilities</td></tr><tr><td>4.</td><td>Net Income</td><td>9. Total Revenues</td></tr><tr><td>5.</td><td>Total Assets</td><td></td></tr></table>

Table 3 – Specific Financial Concepts (Investors’ Terms) in Frame of Reference

Each XBRL calculation linkbase of the 10 randomly selected firms in the training set corresponds to a single, automatically generated, calculation linkbase ontology (see section 5.1). A given filing has a single calculation linkbase and thus a single calculation linkbase ontology. We briefly discuss some descriptive statistics regarding the calculation linkbase ontologies generated for training $\mathbf { M } ^ { 3 }$ Plus. For the average firm’s calculation linkbase ontology within our training corpus, we observe that the calculation hierarchy is 7 elements in depth with 194 unique financial elements. The average calculation linkbase ontology has just 4 elements that have 2 to 3 parent elements each. In addition, 45 financial elements have children elements with an average of 4 children, ranging from 1 to 21. 175 elements in the average firm’s calculation linkbase ontology have sibling elements with an average of 5 siblings, ranging from 1 to 24.

## 6.3 Comparative Performance Analyses

In this section we rigorously test the effects of our comprehensive measure of structural information, as well as the effects of our learning system, on FinCEM’s performance. Refer to section 6.1 for full details on how we conceptualize FinCEM’s performance. As described earlier, our comprehensive structural similarity measurement is composed of four individual measures: lexical similarity, parent similarity, children similarity, and sibling similarity. We examine various combinations of these measurements in order to demonstrate their granular combinations to FinCEM’s overall performance. In addition, we compare FinCEM with $\mathbf { M } ^ { 3 }$ demonstrating how the inclusion of additional structural information and learning capabilities substantially improve performance. Our analyses establish unequivocally that the structural measurement in concert with learning produce state-of-the-art performance. Tables 4 and 5 summarize the results of our experiments.

# ACCEPTED MANUSCRIPT

## Lexical Similarity (LS) vs. LS + Comprehensive Structural Similarity

We conduct a series of experiments to identify appropriate weights for the various components of our comprehensive structural measure. Our experiments reveal that the structural information encoded within children and sibling classes affects the performance far more than that of parent classes. Consider that we generate ontologies on-the-fly from calculation linkbases. Although a calculation linkbase does not need to be a strict tree [35], a given financial concept within a calculation linkbase will typically only have a single parent, a single grandparent, a single great grandparent, and so on with very few exceptions. The same financial concept, however, can have several children. Each of those children may also have several children, and so on. With respect to siblings, XBRL calculation linkbases naturally form wide hierarchies. As such, for any given element in the hierarchy, several other elements will be asserted at the same depth. It is intuitive to expect (and our experiments corroborate this) that more information is encoded in sibling and children hierarchies than in parent hierarchies. Based on the results of our experiments, we decided to use the weights of 0.2, 0.2, 0.8 and 0.8 for lexical, parents, children, and sibling similarities, respectively. Our future study includes a more thorough analysis of the weight’s impact on the performance.

Using the comprehensive structural similarity measure in combination with the lexical similarity measure, we obtain increased precision over lexical similarity alone on six investor terms: Common Stock, Long Term Debt, Net Income, Total Assets, Total Liabilities, and Total Revenues. In addition, the recall scores increase over the levels reported for lexical similarity only when extracting XBRL elements for the financial concept name Common Stock, Net Income, and Total Assets. As such, we can conclude that an approach using lexical and comprehensive structural similarity measures will be more effective in improving XBRL interoperability than an approach using lexical similarity alone.

## LS vs. LS + Sibling Structure

The inclusion of Sibling Structure results in performance improvements on the investor terms, Net Income, Total Liabilities, Total Revenues for both years. We noted earlier that a given XBRL

element within a calculation linkbase will tend to have a large number of sibling elements. As such we have substantially more information about the element based on its siblings.

## LS + All Structure vs. LS + All Structure + Learning

The LS + All Structure + Learning condition generally results in a moderate recall improvement and no improvement over precision. The LS + All Structure + Learning condition is therefore recall oriented. We do observe some interesting results when comparing this condition with the $\mathrm { L } S + \mathrm { A l l }$ structure condition. In particular, in the case of Total Liabilities, the precision score decreases in the LS + All Structure + Learning condition. A possible explanation of this decrease is that, compared to the other financial concepts, fewer companies report the value of Total Liabilities; 55 out of 82 firms in 2011 and 58 out of 92 firm in 2012. This lack of information compromises the $\mathbf { M } ^ { 3 }$ Plus method’s ability to identify accurate equivalent terms for those companies that do not report their values.

## FinCEM vs. M<sup>3</sup>(LS + Children Similarity)

In order to assess the value added by our proposed solution, we also compare FinCEM with the state of the art in XBRL integration for the US financial reporting jurisdiction: M<sup>3</sup> [20]. $\mathbf { M } ^ { 3 }$ utilizes partial structural similarity information; only children similarity information is considered in concert with lexical similarity. Tables 4 & 5 also summarize the results of our comparative performance analysis. FinCEM outperforms $\mathbf { M } ^ { 3 }$ on the average of recall and precision (F-Measure). In the Total Revenues condition, we observe an improvement in FinCEM using the comprehensive structural similarity treatment over $\mathbf { M } ^ { 3 }$ with respect to both the recall and precision ratios. In the Long Term Debt and Total Liabilities conditions, we also observe an improvement in FinCEM over $\mathbf { M } ^ { 3 }$ with respect to the precision ratio alone. In the Common Stock condition, we note the increase in FinCEM over $\mathbf { M } ^ { 3 }$ with respect to the recall ratio. FinCEM performance improvements are most notable in the form of larger recall ratios. These results clearly show that FinCEM will be more effective in improving interoperability than $\mathbf { M } ^ { 3 }$ thus substantiating our contributions over $\mathbf { M } ^ { 3 }$

<table><tr><td></td><td></td><td>M3</td><td>FinCEM Using M3 Plus</td></tr></table>

<table><tr><td></td><td colspan="3">Lexicon Only (LS)</td><td colspan="3">LS + Children Structure</td><td colspan="3">LS + Sibling Structure</td><td colspan="3">LS + All Structure</td><td colspan="3">LS +All Structure + Learning</td></tr><tr><td>Investor&#x27;s Term</td><td>P</td><td>R</td><td>F</td><td>P</td><td>R</td><td>F</td><td>P</td><td>R</td><td>F</td><td>P</td><td>R</td><td>F</td><td>P</td><td>R</td><td>F</td></tr><tr><td>Cash Generated By Operating Activities</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Common Stock</td><td>0.55</td><td>0.87</td><td>0.67</td><td>1</td><td>0.87</td><td>0.93</td><td>0.55</td><td>0.87</td><td>0.67</td><td>1</td><td>0.98</td><td>0.99</td><td>1</td><td>0.99</td><td>0.99</td></tr><tr><td>Long Term Debt</td><td>0.68</td><td>1</td><td>0.81</td><td>0.68</td><td>1</td><td>0.81</td><td>0.68</td><td>1</td><td>0.81</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Net Income</td><td>0.57</td><td>0.38</td><td>0.46</td><td>1</td><td>0.57</td><td>0.73</td><td>1</td><td>0.57</td><td>0.73</td><td>1</td><td>0.57</td><td>0.73</td><td>1</td><td>0.57</td><td>0.73</td></tr><tr><td>Total Assets</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Total Current Asset</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Total Current Liabilities</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Total Liabilities</td><td>0.81</td><td>1</td><td>0.9</td><td>0.38</td><td>1</td><td>0.55</td><td>0.89</td><td>1</td><td>0.94</td><td>0.89</td><td>1</td><td>0.94</td><td>0.46</td><td>1</td><td>0.63</td></tr><tr><td>Total Revenues</td><td>0.79</td><td>0.78</td><td>0.78</td><td>0.71</td><td>0.56</td><td>0.63</td><td>1</td><td>0.78</td><td>0.88</td><td>1</td><td>0.78</td><td>0.88</td><td>1</td><td>0.89</td><td>0.94</td></tr></table>

P: Precision, R: Recall, F: F-Measure

Table 4 - Results of 2011 Filings: N = 82 Firms

<table><tr><td rowspan="2"></td><td colspan="3"></td><td colspan="3">M3</td><td colspan="9">FinCEM Using M3 Plus</td></tr><tr><td colspan="3">Lexicon Only (LS)</td><td colspan="3">LS + Children Structure</td><td colspan="3">LS + Sibling Structure</td><td colspan="3">LS + All Structure</td><td colspan="3">LS +All Structure + Learning</td></tr><tr><td>Investor&#x27;s Term</td><td>P</td><td>R</td><td>F</td><td>P</td><td>R</td><td>F</td><td>P</td><td>R</td><td>F</td><td>P</td><td>R</td><td>F</td><td>P</td><td>R</td><td>F</td></tr><tr><td>Cash Generated By Operating Activities</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Common Stock</td><td>0.56</td><td>0.88</td><td>0.68</td><td>1</td><td>0.88</td><td>0.94</td><td>0.56</td><td>0.9</td><td>0.69</td><td>1</td><td>0.99</td><td>0.99</td><td>1</td><td>0.99</td><td>0.99</td></tr><tr><td>Long Term Debt</td><td>0.64</td><td>1</td><td>0.78</td><td>0.64</td><td>1</td><td>0.78</td><td>0.64</td><td>1</td><td>0.78</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Net Income</td><td>0.56</td><td>0.39</td><td>0.45</td><td>1</td><td>0.58</td><td>0.73</td><td>1</td><td>0.58</td><td>0.73</td><td>1</td><td>0.58</td><td>0.73</td><td>1</td><td>0.58</td><td>0.73</td></tr><tr><td>Total Assets</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Total Current Assets</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Total Current Liabilities</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Total Liabilities</td><td>0.76</td><td>1</td><td>0.86</td><td>0.37</td><td>1</td><td>0.54</td><td>0.89</td><td>1</td><td>0.94</td><td>0.89</td><td>1</td><td>0.94</td><td>0.45</td><td>1</td><td>0.63</td></tr><tr><td>Total Revenues</td><td>0.79</td><td>0.78</td><td>0.78</td><td>1</td><td>0.78</td><td>0.97</td><td>1</td><td>0.78</td><td>0.88</td><td>1</td><td>0.78</td><td>0.88</td><td>0.99</td><td>0.88</td><td>0.93</td></tr></table>

P: Precision, R: Recall, F: F-Measure

Table 5 - Results of 2012 Filings: N = 92 Firms

## 6.4 Threshold Effect on Learning

During the operation phase, FinCEM may not find the value of a particular financial concept from a firm’s XBRL instance document. This would occur either because the equivalent terms in FinOnt do not match with the XBRL term used in the firm’s filing, or because the firm does not report the value of this particular financial concept; a firm is not obligated to directly report the value of all its financial concepts. As stated earlier, only when FinCEM has found no value for a financial concept does it re-execute the M<sup>3</sup> Plus method to identify the equivalent XBRL term used by the firm. A challenge in the adaptive learning process is that an XBRL term with the largest similarity score may not be the right term, since a firm may not report its value. For this situation, a threshold is used to filter out the XBRL term whose similarity score happens to be the largest among all the terms. In order for the XBRL term with the largest similarity score to be recognized as an equivalent term for the financial concept, its average similarity score must exceed a certain threshold; the mean similarity score is obtained by dividing the cumulative similarity score by the number of candidate finance concepts. A threshold value is an important parameter, which significantly affects the precision and recall ratios of the nine financial concepts. We determined a threshold value after carefully analyzing the effect of varying thresholds on those ratios. Our experiment started at a 0.1 threshold with 0.1 increments, resulting in the ten different FinOnt versions. The precision and recall ratios of each FinOnt version are calculated. The results show that the varying thresholds have no effect on the precision and recall ratios for the four financial concepts: Cash Generated By Operating Activities, Common Stock, Total Assets, and Total Current Liabilities. However, the different thresholds result in significantly different precision and recall ratios for the remaining five financial concepts: Long Term Debt, Net Income, Total Current Asset, Total Liabilities, and Total Revenues. Figures 5 and 6 show the changes in F-measures for those five financial concepts for the 2011 and 2012 filings, respectively. The charts show that the F-measures for those financial concepts, except Net Income, increase and then gradually decrease in the 2011 filings. The results for the 2012 filings are very similar to those for the 2011 filings, but the F-measures of Total Liabilities increase at the threshold of 0.8. Taking account of the F-measures of all financial concept names for those two years, the threshold of 0.5 results in the overall highest F-measure; thus, we chose 0.5 as the threshold for FinCEM.

![](/api/attachments/STJNC9F6/fulltext/images/59e099a9bb9315c2c4b764bebe9e5e41a70b7118a259bcabc740aab595f2d337.jpg)  
Figure 5 - Threshold Effects on Learning assessed by F-measures: 2011 Filings

![](/api/attachments/STJNC9F6/fulltext/images/d211fd0dcb6a2887ec828b4337ff8d0a111054500827d7b64137048dc880f495.jpg)  
Figure 6 - Threshold Effects on Learning assessed by F-measures: 2012 Filings

## 7. Conclusion

The work presented here makes significant strides towards a viable solution to the problem of XBRL interoperability. We define this problem as occurring when, for a given financial concept, two or more XBRL filings are terminologically ambiguous with respect to their representation of the financial concept. We also cite the less than adequate state of the US implementation of XBRL for financial (external) reporting with respect to interoperability. These interoperability problems limit the ability of US implementation of the XBRL standard to meet its primary objective of streamlining, via automation, the consumption of US firm financial statements. Our work presents a pathway to a feasible solution for this problem.

Specifically, our design artifact is a fully automatic method for improving interoperability between XBRL filings in the US jurisdiction. Using insights from channel theory, we posit a unique design wherein we leverage the regularities inherent in XBRL as a representation language. Specifically, we argue and decisively demonstrate that there are semantics encoded within the structure of calculation linkbases that are sufficient to discern financial concepts. The significance of this discovery lies in the idea that calculation hierarchies can discriminate between abstract financial concepts such that these concepts can be resolved to XBRL element names based on a user query. Both the full automaticity of the artifact and our reliance on theory to inform its design are novelties in this area. We demonstrate that our approach is highly accurate in the retrieval of values corresponding to nine financial concepts. Further, we

# ACCEPTED MANUSCRIPT

add an adaptive learning component to our design artifact. This component ensures that our design artifact is robust with respect to idiosyncratic reporting situations which may be encountered in the course of fulfilling a user’s request for data.

Going forward, we identified in the evaluation section that a limitation of our approach is that it assumes that every financial concept is represented in a filing by a single XBRL element and corresponding value. We are currently investigating methods to automatically detect “composite” financial concepts and perform the necessary calculations. The weights play important roles in the comprehensive structural similarity computation. We determine their values based on a series of experiments. A more thorough analysis of the weight’s impact on performance, where the weights are treated as continuous variables, is useful. The experiments we conducted to determine the weights used for the various structural measurements was based on discrete tests with different values attached to the weights. For this work, we concluded our experiments once we identified an intuitive trend viz. the ce. Accordingly, our weights are only quasi-optimal. Another promising area for future development, which we hinted at in the literature review, is the potential of this method to enable the automatic generation of links between XBRL filings and linked open data sets, as well as other diverse upper level ontologies. Were this method amenable to such ends, it would provide a non-trivial contribution to the Linked Open Data community in finance. Finally, we would like to acknowledge the potential of our approach to other semantic integration domains. As an alternative to existing ontology-based semantic integration methods, the applicability of our design artifact goes beyond the XBRL interoperability problem. The efficacy of our approach relies on two core conditions being met. First, that the domain of discourse be very well defined in the to-bemerged data representations . Second, that there exists sufficient richness in the structural representations of the to-be-merged data. When these two conditions are met, we are confident that our technique will offer much promise to the domain.

## Acknowledgement

The authors would like to thank Dr. Richard Redmond in the Department of Information Systems,

School of Business, Virginia Commonwealth University, for his helpful suggestions in describing the M<sup>3</sup>

Plus method.

## References

[1] M. Enachi and I. I. Andone, “The Progress of XBRL in Europe – Projects, Users and Prospects,” Procedia Econ. Financ., vol. 20, no. 15, pp. 185–192, 2015.

[2] R. Debreceny and G. L. Gray, “The production and use of semantically rich accounting reports on the Internet: XML and XBRL,” Int. J. Account. Inf. Syst., vol. 2, no. 1, pp. 47–74, 2001.

[3] R. S. Debreceny, S. M. Farewell, M. Piechocki, C. Felden, A. Gräning, and A. d’Eri, “Flex or Break? Extensions in XBRL Disclosures to the SEC,” Account. Horizons, vol. 25, no. 4, pp. 631– 657, 2011.

[4] N. Müller-wickop, M. Schultz, M. Nüttgens, N. Mueller-wickop, and M. N. De, “XBRL : Impacts , Issues and Future Research Directions,” pp. 1–20, 2012.

[5] H. Zhu and H. Wu, “Assessing the quality of large-scale data standards: A case of XBRL GAAP Taxonomy,” Decis. Support Syst., vol. 59, pp. 351–360, 2014.

[6] H. Carretié, B. Torvisco, R. Garcia, and J. Carlos, “Using semantic web technologies to facilitate XBRL-based financial data comparability,” in International Workshop on Finance and Economics on the Semantic Web, 2012.

[7] M. Spies, “An ontology modelling perspective on business reporting,” Inf. Syst., vol. 35, no. 4, pp. 404–416, 2010.

[8] T. Wunner, P. Buitelaar, and S. O’Riain, “Semantic, terminological and linguistic interpretation of xbrl,” Reuse Adapt. Ontol. Terminol. Work. 17th Int. Conf. Knowl. Eng. Knowl. Manag., 2010.

[9] R. Chowdhuri, V. Y. Yoon, R. T. Redmond, and U. O. Etudo, “Ontology based integration of XBRL filings for financial decision making,” Decis. Support Syst., vol. 68, pp. 64–76, 2014.

[10] A. Gräning, C. Felden, and M. Piechocki, “Status Quo and Potential of XBRL for Business and Information Systems Engineering,” Bus. Inf. Syst. Eng., vol. 3, no. 4, pp. 231–239, 2011.

[11] S. Gregor and D. Jones, “The anatomy of a design theory,” J. Assoc. Inf. Syst., vol. 8, no. 5, pp. 312–335, 2007.

[12] J. F. Nunamaker Jr and M. Chen, “Systems development in information systems research,” in System Sciences, 1990., Proceedings of the Twenty-Third Annual Hawaii International Conference on, 1990, vol. 3, pp. 631–640.

[13] J. Bao, G. Rong, X. Li, and L. Ding, “Representing financial reports on the semantic web,” in Semantic Web Rules, Springer, 2010, pp. 144–152.

[14] M. Radzimski, J. L. Sanchez-Cervantes, A. Garcia-Crespo, and I. Temiño-Aguirre, “Intelligent Architecture for Comparative Analysis of Public Companies Using Semantics and XBRL Data,” Int. J. Softw. Eng. Knowl. Eng., vol. 24, no. 5, pp. 801–823, 2014.

[15] H. H. Zhu and S. Madnick, “Semantic integration approach to efficient business data supply chain: integration approach to inter-operable XBRL,” 2007.

[16] T. Declerck and H.-U. Krieger, “Translating XBRL Into Description Logic. An Approach Using Protege, Sesame & OWL.,” in BIS, 2006, pp. 455–467.

[17] R. Garcia and R. Gil, “Linking XBRL Financial Data,” in Linking Enterprise Data, D. Wood, Ed. Springer Science+Business Media, LLC, 2010, pp. 103–125.

[18] B. Livieri, M. Zappatore, and M. Bochicchio, “Towards an XBRL Ontology Extension for Management Accounting,” Concept. Model. 33rd Int. Conf. ER 2014, Atlanta, GA, USA, Oct. 27- 29, 2014. Proc., pp. 289–296, 2014.

[19] S. O’Riain, E. Curry, and A. Harth, “XBRL and open data for global financial ecosystems: A linked data approach,” Int. J. Account. Inf. Syst., vol. 13, no. 2, pp. 141–162, 2012.

[20] U. Etudo and V. Yoon, “Leveraging XBRL Calculation Linkbases to Overcome Semantic Heterogeneity across XBRL Fillings: The Multi-Ontology Multi-Concept Matrix (M3),” 2015.

[21] T. I. M. Berners-Lee, J. Hendler, and O. R. a Lassila, “The Semantic Web,” Sci. Am., vol. 284, no. 5, pp. 34–43, 2001.

[22] N. F. Noy, “Semantic Integration: A Survey of Ontology-based Approaches,” SIGMOD Rec., vol. 33, no. 4, pp. 65–70, 2004.

[23] J. Barwise and J. Seligman, Information flow: the logic of distributed systems, volume 44 of Cambridge tracts in theoretical computer science, vol. 252. Cambridge University Press Cambridge, 1997.

[24] Y. Kalfoglou and M. Schorlemmer, “IF-Map: An ontology-mapping method based on information-flow theory,” in Journal on data semantics I, Springer, 2003, pp. 98–127.

[25] K. Ramar and G. Gurunathan, “Technical Review on Ontology Mapping Techniques,” Asian J. Inf. Technol., vol. 15, no. 4, pp. 676–688, 2016.

[26] S. Melnik, H. Garcia-Molina, and E. Rahm, “Similarity Flooding: A Versatile Graph Matching Algorithm,” Data Eng., vol. 2002, pp. 117–128, 2002.

[27] N. F. Noy and M. A. Musen, “Anchor-PROMPT: Using Non-Local Context for Semantic Matching,” Framework, vol. 39, no. Figure 1, pp. 63–70, 2001.

[28] M. H. Seddiqui and M. Aono, “Anchor-flood: results for OAEI 2009,” in Proceedings of the 4th International Conference on Ontology Matching-Volume 551, 2009, pp. 127–134.

[29] C. J. van Rijsbergen, Information Retrieval. Butterworth, 1979.

[30] E. Prud’hommeaux and A. Seaborne, “SPARQL Query Language for RDF. W3C Recommendation, January 2008.” 2008.

[31] J. Yu, J. A. Thom, and A. Tam, “Requirements-oriented methodology for evaluating ontologies,” Inf. Syst., vol. 34, no. 8, pp. 766–791, 2009.

[32] N. Guarino, “Formal Ontology and Information Systems,” in Proceedings of the First International Conference on Formal Ontologies in Information Systems, FOIS’98, 1998, pp. 3–15.

[33] E. M. Voorhees, “The philosophy of information retrieval evaluation,” in Evaluation of crosslanguage information retrieval systems, Springer, 2002, pp. 355–370.

[34] J. D. Piotroski, “Value investing: The use of historical financial statement information to separate winners from losers,” J. Account. Res., pp. 1–41, 2000.

[35] H. Fischer, L. Hampton, C. Hoffman, L. Matherne, C. Pryde, Y. Wang, and M. Goodhand, “Extensible Business Reporting Language (XBRL) 2.1,” XBRL International, 2003. [Online]. Available: http://www.xbrl.org/Specification/XBRL-2.1/REC-2003-12-31/XBRL-2.1-REC-2003- 12-31+corrected-errata-2013-02-20.html.

Ugochukwu Etudo is PhD Candidate in the Department of Information Systems at Virginia Commonwealth University. He received his M.S in Information Systems from Virginia Commonwealth University in 2013. His research interests include text mining, decision support systems and sociotechnical systems. His article appears in Decision Support Systems.

Victoria Yoon is Professor in the Department of Information Systems at the Virginia Commonwealth University. She received her M.S. from the University of Pittsburgh and her Ph.D. from the University of Texas at Arlington. Her primary research area has been the application of Artificial Intelligence to business decision-making in organizations and technical and social issues surrounding such applications. She has published articles in such leading journals as MIS Quarterly, Decision Support Systems, Communications of the ACM, and Journal of Management Information Systems.

Dapeng Liu is PhD student in the Department of Information Systems at Virginia Commonwealth University. He received his M.S in Economics from Shandong University in 2014 and his MBA from Missouri State University in 2013. His research interests include business intelligence, social media analytics, big data analytics, and systems theory.

## Highlights

 This study aims to resolve the element heterogeneity issue in XBRL filings.

 Using channel theory, we modeled the problem of XBRL interoperability.

 We used XBRL calculation linkbases to resolve semantic heterogeneity across multiple XBRL filings.

 Our design artifact, called FinCEM, is capable of mapping heterogeneous financial elements used in XBRL filings
