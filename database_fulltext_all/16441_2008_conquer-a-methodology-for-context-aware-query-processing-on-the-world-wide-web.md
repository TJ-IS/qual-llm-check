---
otero_id: 16441
otero_key: "38MWGZD7"
title: "CONQUER: A Methodology for Context-Aware Query Processing on the World Wide Web"
authors: "Veda C. Storey; Andrew Burton-Jones; Vijayan Sugumaran; Sandeep Purao"
year: "2008"
journal: "Information Systems Research"
doi: "10.1287/isre.1070.0140"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# CONQUER: A methodology for context-aware query processing on the World Wide Web

Article  in  Information Systems Research · March 2008

DOI: 10.1287/isre.1070.0140 · Source: DBL

CITATIONS 48

READS 404

4 authors:

![](/api/attachments/38MWGZD7/fulltext/images/fb04d4c69b215ddf2ec6b0394cce0abbb5d8dc7c407b333af5ffb6b3be24341d.jpg)

SEE PROFILE

Some of the authors of this publication are also working on these related projects:

![](/api/attachments/38MWGZD7/fulltext/images/225fcf1c73f7fd43d318186f17db5e3c3289b99f17ea59e18defdc802e2c35c3.jpg)

ADR practises View project

![](/api/attachments/38MWGZD7/fulltext/images/71ef78b218c42fd2e125a51ed1fe43268965894984e32b5b4f0d1fc73d1d1f3f.jpg)

Project

Sentiment Analysis View project

# CONQUER: A Methodology for Context-Aware Query Processing on the World Wide Web

Veda C. Storey

Computer Information Systems Department, J. Mack Robinson College of Business, Georgia State University, Atlanta, Georgia 30302-4015, vstorey@cis.gsu.edu

Andrew Burton-Jones

Management Information Systems Division, Sauder School of Business, University of British Columbia, 2053 Main Mall, Vancouver, British Columbia V6T 1Z2, Canada, andrew.burton-jones@sauder.ubc.ca

Vijayan Sugumaran Vijayan Sugumaran

Department of Decision and Information Sciences, School of Business Administration, Oakland University, Rochester, Michigan 48309, sugumara@oakland.edu

Sandeep Purao College of Information Sciences and Technology, Pennsylvania State University, University Park, State College, Pennsylvania 16802, spurao@ist.psu.edu

major impediment to accurate information retrieval from the World Wide Web is the inability of search engines to incorporate semantics in the search process. This research presents a methodology, CONQUER (CONtext-aware QUERy processing), that enhances the semantic content of Web queries using two complementary knowledge sources: lexicons and ontologies. The methodology constructs a semantic net using the original query as a seed, and refines the net with terms from the two knowledge sources. The enhanced query, represented by the refined semantic net, can be executed by search engines. This paper describes the methodology and its implementation in a prototype. An empirical evaluation shows that queries suggested by the prototype produce more relevant results than those obtained by the original queries. The research, thus, provides a successful demonstration of the use of existing knowledge sources to enhance the semantic content of Web queries. The paper concludes by identifying potential uses of such enhancements of search technology in organizational contexts.

Key words: query augmentation; semantic retrieval; ontology; lexicon; context; query; semantic web; semantic retrieval system

History: Sumit Sarkar, Senior Editor; H. Raghav Rao, Associate Editor. This paper was received on May 18, 2005, and was with the authors 10 <sup>1</sup> months for 3 revisions.

## 1. Introduction

The World Wide Web is the world’s most valuable information resource (Spink and Ozmutlu 2002). To search the Web, users submit queries with constraints such as AND and OR to search engines that process queries using a variety of algorithms, such as text matches, links, or domain information (Ozmutlu et al. 2003, Pokorny 2004). This process is difficult because query terms can be ambiguous and imprecise. Search engines are generally not equipped to automatically resolve the meaning of imprecise and ambiguous terms (Ide and Veronis 1998), often producing irrelevant results (Spink and Ozmutlu 2002).

The ambiguity of language is typically not a problem for human beings who can infer the appropriate word sense or meaning based on context (Miller 1996), but computer systems such as search engines can usually only overcome these limitations in constrained domains (Stevenson 2003). Thus, the issue of semantics has become the grand challenge for the next-generation World Wide Web (Embley 2004).

There are two approaches to addressing this challenge. The first requires designing a “Semantic” Web by enhancing Web content with metainformation such as tags (Berners-Lee et al. 2001). This approach assumes that the prevalent Web infrastructure and existing Web content can be changed, and aims to develop techniques to incorporate semantics into Web page design, e.g., “marking up” terms in Web pages with clearly specified meanings (Corby et al. 2006, Oberle et al. 2005, Lee et al. 2005). Retrofitting the enormous content on the Web is a significant challenge that is being addressed by approaches such as automatic ontology generation (van Harmelen 2004, Sure et al. 2005, Embley 2005, Veres 2006).

The second approach suggests enhancing the search process by incorporating semantics into queries. This approach concedes that the prevalent Web infrastructure and existing Web content will be difficult to change. Instead, it suggests that semantics may be incorporated into the process of query formulation and execution. Theoretical precursors for this approach include the use of term co-occurrence (van Rijsbergen 1977) and word sense disambiguation (Ide and Veronis 1998, Snasel et al. 2005) to improve query relevance. For example, a user is more likely to find a result relevant if it contains the original query term (e.g., chair) and terms that are related to the desired sense of the query term (e.g., professor) and excludes terms related to unwanted senses (e.g., furniture). Although the addition and exclusion of these terms should be expected to improve a query, these theories are difficult to operationalize because it is hard to identify the desired sense of a user’s query and expand the query with the correct terms and constraints (Peat and Willett 1991, Sanderson 2000, Stevenson 2003).

The research reported in this paper adopts the second approach. The objective of this research is to develop a methodology to enhance user queries on the World Wide Web by incorporating semantics. This constitutes design science research (Hevner et al. 2004) because it designs, creates, and evaluates an artifact that is informed by prior theories (van Rijsbergen 1977, Ide and Veronis 1998, Snasel et al. 2005). Prior research using the above theories has had mixed results (Stevenson 2003). We use the core postulates of these theories with a semantic net representation that includes the original user query as a seed, refined by two knowledge sources (ontologies and lexicons). We, thus, operationalize and extend prior research by using two knowledge sources and a semantic net formalism to disambiguate and improve the precision of the user’s query. To ensure that the work complements existing search technology, the methodology produces an enhanced query with the help of operators such as “and,” “or,” or “not” that can be executed with established search engines. An appropriate evaluation metric for the research is improved relevance of the results.

The contribution of this research is a methodology to incorporate context into Web query processing that directly addresses part of the grand challenge of semantics for the Semantic Web. Specifically, the research provides: (1) a methodology for processing queries on the Web that incorporates semantics from existing lexical and ontological knowledge sources; (2) a design science artifact, the CONQUER (CONtext-aware QUERy processing) prototype, to improve query processing; and (3) an evaluation of the methodology to identify improvements to query results and opportunities for future research.

This paper has six sections. Section 2 reviews prior research. Sections 3 and 4 present the proposed queryprocessing methodology and describe its implementation. Section 5 presents the results of an empirical test of the methodology. Section 6 concludes the paper.

## 2. Related Research

## 2.1. Querying on the World Wide Web

Technologies for query processing and information retrieval from the Web include: (a) crawlers that locate and read Web pages, (b) indexers that index pages based on their content, and (c) query processors that accept user queries and return results (Pokorny 2004). Query processors use two types of algorithms (Pokorny 2004). The first is query dependent and matches query terms with the terms on Web pages (e.g., matching query term “chair” with term “chair” appearing on a Web page). The second is query independent and relies on the topological structure of the Web, inferring the relevance of a page from the network of links amongst pages (e.g., considering a page that many point to for the term “tango” as an authoritative source about that term). Our research aims to improve query-dependent algorithms, focusing on query formulation.

The main challenge faced by query-dependent algorithms is dealing with the semantics of terms. HTML does not facilitate the definition of the meanings of terms on Web pages. As a result, the meanings of terms on Web pages cannot be matched against the meaning of query terms. Schemas defined with XML can overcome this problem by providing tags for developers that specify the meaning of terms (xml.coverpages.org/xmlApplications.html). They are part of the vision for the Semantic Web, where terms in Web pages are marked up by referencing online ontologies that serve as surrogates for the meaning of terms (Hendler 2001). It is unlikely that this vision of the Semantic Web will be realized in the near future because developers may define terms on Web pages using ontologies of varying quality and users may define their query terms with different ontologies again of varying quality. Therefore, semantically matching the intended sense of query terms against those in Web pages will remain problematic.

Researchers have attempted to improve techniques for query processing on the Web by drawing on information retrieval (IR) research (Pokorny 2004), where a central approach to overcoming problems of semantically matching terms is word sense disambiguation (Ide and Veronis 1998, Snasel et al. 2005). The intuition behind word sense disambiguation is that the meaning of a term can be clarified by specifying its relationship with other terms (e.g., the meaning of “chair” is clearer if we say that a chair is a professor). Word sense disambiguation relies on the theory of term co-occurrence: a page will more likely be relevant to a user if it contains the query term plus other related terms (van Rijsbergen 1977).

Word sense disambiguation requires: (1) identifying the intended meaning of query terms, and (2) altering the query so it returns more useful results. The first step is usually achieved by deducing a term’s meaning from other terms in the query (Allan and Raghavan 2002). Unfortunately, this is not feasible for Web queries because most contain only two words (Spink et al. 2001, Spink and Ozmutlu 2002), making them too short to identify context (Voorhees 1994, de Lima and Pedersen 1999). Therefore, some user interaction is inevitable to accurately identify the intended sense of terms in Web queries (Allan and Raghavan 2002). The second step is generally achieved through a combination of:

• Query constraints, such as Boolean operators that require pages to include all or a subset of query terms (Hearst 1996, Mitra et al. 1998, Eastman and Jansen 2003);

• Query expansion with local context, where terms are added to the query based on a subset of documents the user identifies as relevant to his or her query (Salton and Buckley 1990, Mitra et al. 1998, Xu and Croft 1998); and/or

• Query expansion with global context, where terms are added to the query from other knowledge sources, document collections or past queries (Qiu and Frei 1993, Voorhees 1994, de Lima and Pedersen 1999, Greenberg 2001).

Of these three, query constraints are known to improve Web search, but only if used wisely (Moldovan and Mihalcea 2000, Eastman and Jansen 2003). Query expansion with local context is generally ineffective for Web search because users rarely provide relevance feedback (Spink et al. 2001, Cui et al. 2002). The third alternative, query expansion with global context holds significant promise for improving query processing on the Web. Although one might argue that it would be unnecessary on the Semantic Web (because content will be marked up and linked to online ontologies that explain each term’s meaning), that vision remains a distant possibility and may still use different, and possibly incompatible ontologies, requiring disambiguation of query terms (Hendler 2001, Burton-Jones et al. 2005).<sup>1</sup> The methodology we develop, therefore, uses the approaches suggested by query constraints coupled with query expansion with global context.

## 2.2. Query Constraints and Sources of Global Context

To choose query constraints and global context, both theoretical and practical issues must be considered. Most search engines allow Boolean operators (and, or, and not) and phrase indicators (e.g. “quotes around words”) for query constraints. Researchers have investigated the extent to which these constraints help users query the Web. In theory, other constraints are also possible, e.g. “near,” which allows users to find pages that contain specified terms in proximity to one another (Hearst 1996). However, this constraint has been studied less than others, probably because few search engines offer the capability (e.g., AltaVista does; Google and AlltheWeb do not). Constraints improve results, but only if applied wisely (Moldovan and Mihalcea 2000, Eastman and Jansen 2003). However, it is difficult to know how to use constraints. If a user searches for a chaired professor, he or she might use “chaired professor.” This phase will likely harm the query because it will rarely be used on the personal Web pages of chaired professors. Yet, in other contexts, a phrase may help a query. Because of this difficulty, there is no consensus regarding the best automated way to use constraints in queries (Moldovan and Mihalcea 2000). An approach for doing so would be useful because users often make errors when adding constraints (Spink et al. 2001).

In query expansion with global context, terms are added to base queries from a source, prior to executing the queries. One difficulty with doing so is finding appropriate sources. For example, adding terms employed in users’ past queries (Cui et al. 2002) or in users’ personal profiles (Storey et al. 2004) can be useful. However, such approaches assume that query logs and/or personal profiles exist, are relevant, and can be accessed. The approach that requires the least assumptions is to add terms to queries from online knowledge bases (Stevenson 2003, Voorhees 1994). This approach is feasible because publicly available knowledge bases already exist on the Web (Stevenson 2003). The difficulty then lies in choosing which knowledge bases to use and what knowledge to obtain from them. Prior research shows that two knowledge bases should be used, ideally in combination (Mandala et al. 1999, Moldovan and Mihalcea 2000): (1) knowledge bases that provide general knowledge such as the synonyms found in a general thesaurus, and (2) knowledge bases that provide domain-specific knowledge such as terms that are relatively unique to a specific domain.

In this research, we propose that such information is best acquired from two types of sources, lexicons and ontologies. The knowledge sources available in practice may be best understood as a continuum of choices that are marked at the two extremes by informal lexicons and fully formalized ontologies.

Figure 1 Sources of Global Context Knowledge: Ontologies and Lexicons  
![](/api/attachments/38MWGZD7/fulltext/images/075741035e2de4f2300db5238bf53b65d0d89e68ec7b2ab543d64c3b552acc26.jpg)

Although a number of dimensions may differentiate these sources (e.g., formalization or structure, Gomez-Perez et al. 2004), we suggest domain specificity because it allows us to focus on the applicability of the knowledge to different queries. Figure 1 places ontologies and lexicons along this dimension. This continuum of possibilities represented does not, however, dictate how different proponents may name different knowledge sources.<sup>2</sup>

2.2.1. Lexicons. A lexicon describes the generally accepted meanings of words in a language (Stevenson 2003). The two main types of lexicons are dictionaries and thesauri, with the most common ones used for word sense disambiguation being the LDOCE dictionary, Roget’s thesaurus, and WordNet (http://www.cogsci.princeton.edu/<sub>∼</sub>wn). WordNet is a combination of a dictionary and thesaurus, but more comprehensive than the other two (Stevenson 2003). WordNet stores, categorizes, and relates English nouns, verbs, adjectives, and adverbs, organizing them into sets of synonyms (or “synsets”) that share the same underlying word senses (Miller et al. 1990). For example, WordNet describes four word senses for the term “chair” as a noun (seat, professor, chairperson, and electric chair) and two for it as a verb (preside and moderate), as well as superclasses (e.g., furniture) and subclasses (e.g., armchair). Although lexicons can define any term, most focus on generally accepted terms in a language. For example, WordNet could define “use case,” a term used in systems development, but does not. Some domains, such as medicine, have domainspecific dictionaries (e.g., http://www.nlm.nih.gov/ medlineplus/mplusdictionary.html), but it would be extremely difficult to create and identify domainspecific online lexicons for all domains (Greenberg

2001). Lexicons such as WordNet can assist Web queries, but there is no consensus regarding their benefit, the best way to use them, or if they should be used at all (Voorhees 1994, Moldovan and Mihalcea 2000, Stevenson 2003).

2.2.2. Ontologies. Ontologies describe the traits of one’s world (Weber 1997). There are two main types: (1) formal/top-level ontologies that describe reality in general (e.g., the world consists of things and properties), and (2) material/domain ontologies that describe reality in one or more domains (e.g., the auction domain consists of products and bids) (Weber 2002). Both types consist of terms, their definitions, and axioms relating them (Bunge 1977, Gruber 1993). The artificial intelligence community promotes the use of ontologies to help computer programs reason about domains. Thus, much effort has gone into creating ontologies (Chan 2004), ontology development languages (McGuinness et al. 2002), ontology development environments (such as Protégé and Text-to-Onto) (Kishore et al. 2004), and ontology libraries (Ding and Fensel 2001, Staab et al. 2004). Most ontologies are domain specific, although it is possible to specify general features of the real world as CYC<sup>3</sup> does (Lenat 1995). However, there has been little research carried out on retrieving information using either type. The most well known ontology library is the DAML (DARPA Agent Markup Language) library containing 282 ontologies and approximately 68,000 classes and 11,000 properties (http://www.daml.org/ontologies/, accessed 15 February 2008.

2.2.3. Utilizing Lexical and Ontological Sources in Combination. There are two main advantages to using ontologies and lexicons in combination. First, a user should be able to obtain a broader range of knowledge because lexicons and ontologies provide different degrees of domain specificity. This can benefit the user by: (a) providing knowledge for more terms, and (b) providing more knowledge for any given term.<sup>4</sup>

Second, a user should be able to access a broader range of knowledge forms. The forms of knowledge offered in lexicons such as WordNet typically include synonyms, hypernyms (superclasses), hyponyms (subclasses), meronyms (parts), and holonyms (wholes). Ontologies, such as those in the DAML library, typically provide hypernyms, hyponyms, meronyms, and holonyms. Other ontologies include properties, axioms, and inference capabilities, but do not provide synonyms. Having access to more forms of knowledge might help a user expand a Web query, but this has not been studied in depth. Researchers have often examined the applicability of synonyms, hyponyms, and hypernyms for word sense disambiguation, but have rarely examined meronyms or holonyms (Stevenson 2003). Nor have researchers examined whether properties or axioms can help in Web searches, probably because they are not often available in ontology libraries (Burton-Jones et al. 2005). Thus, the extent to which having a broader range of knowledge forms is useful for Web searching is not yet known.

We propose a methodology to address the first advantage, i.e., accessing a broader range of knowledge. As in past word sense disambiguation research, we use synonyms, hyponyms, and hypernyms for global context rather than meronyms, holonyms, axioms, and properties. Thus, we do not address the full potential for complementarity between the two knowledge sources. Instead, we partially address this complementarity by creating a methodology that leverages the benefits from lexicons and ontologies having different levels of domain-specificity. We use the most well-known instance of each source: lexical knowledge from the WordNet lexicon (Miller et al.

1990) and ontological knowledge from the DAML ontology library (Ding and Fensel 2001).<sup>5</sup>

There are two concerns with using lexicons and ontologies in combination. First, they might overlap (Figure 1) requiring conflict resolution. Second, publicly available ontologies may be of varying quality (Burton-Jones et al. 2005). Fortunately, ontology libraries can provide useful domain-specific knowledge even if individual ontologies are incomplete or inaccurate (Stephens and Huhns 2001). Thus, neither concern should negate the usefulness of using ontological and lexical knowledge in combination for Web querying.

## 3. CONQUER: A Methodology for Context-Aware Query Processing

This section presents CONQUER, a methodology to improve the relevance of information retrieved by identifying the intended sense of query terms. The methodology builds on and refines van Rijsbergen’s (1977) ideas on term co-occurrence with an attempt to achieve word sense disambiguation (Stevenson 2003). The methodology is expected to be applicable to search scenarios where: (a) a user’s query terms have multiple interpretations, (b) the number of query terms is small, and (c) a user is willing to clarify the intended meaning when a context is missing. An example is when a user searching for “chair” is interested in the “academic,” as opposed to the “furniture,” sense. There are scenarios where our methodology may not be applicable. For example, the methodology would not help if a user has extensive knowledge of the domain searched and knows the exact terms and syntax to use. The methodology would also not help if the user is searching for instance information (e.g., locating a flight with a proper noun phrase such as “Delta Airlines,” obtained by locating the flight status sub-window or page within an airline’s website). In short, CONQUER is intended for anyone who may encounter a bewildering array of word senses for a query term when searching. This situation occurs frequently because users tend to use only nouns (Stevenson 2003), very short query phrases, no more than two words (Spink et al. 2001, Spink and Ozmutlu 2002), and the simple matching techniques used by search engines (Pokorny 2004). The methodology requires user interaction, so it is most applicable for users when their searches are important (Leavitt 2006) and the users are willing to expend the effort required to achieve accuracy (as with expert systems (Todd and Benbasat 1999)). The second intended audience is the designers of search engines who could extend their systems with CONQUER. We describe how CONQUER can interface with existing Web search engines, its extensibility, and evidence that combining a search engine with CONQUER improves the relevance of query results.

The CONQUER methodology shares goals of prior research on word sense disambiguation and query processing (Ide and Veronis 1998). It improves prior efforts by using two sources of global knowledge (WordNet and DAML ontologies) with a coordinated set of query constraints to construct the context. The methodology clarifies the intended sense of the query with knowledge from these sources, and reformulates the query to reflect this context. Figure 2 summarizes the methodology, which has three phases: Identifying the Query Context, Refining the Query Context, and Executing the Query.

CONQUER uses the following forms and sources of global knowledge: synonyms, hypernyms, and hyponyms from WordNet, and hypernyms and hyponyms from the DAML ontologies. The methodology uses this knowledge in conjunction with the original query to construct a semantic net that represents the context of the intended sense of the query. A semantic net represents the original query terms with associated terms (Chen and Dhar 1990) that can be used to reformulate the query with additional constraints that search engines can recognize and execute.

In summary, CONQUER focuses on: (a) noun phrases for search terms (Eastman and Jansen 2003, Xu and Croft 1998, Jansen and Pooch 2001), (b) synonyms, hypernyms, and hyponyms from WordNet and the DAML ontologies, (c) representation of the context of a user’s query in the form of a semantic net, and (d) reformulation of the user’s query into an enhanced query, based on this context. CONQUER thus, does not require changes to users’ patterns of formulating queries as short noun phrases, leverages existing global knowledge sources, and utilizes existing search engine technology to achieve the goal of retrieving information from the Web that has greater relevance to the user.<sup>6</sup>

Figure 2 Overview of the CONQUER Methodology  
![](/api/attachments/38MWGZD7/fulltext/images/8346b2cc451a0bc879a7c38683aa0497592c0194775c5fe811bf74b2ac43a511.jpg)

Figure 3 Logical Architecture Supporting CONQUER  
![](/api/attachments/38MWGZD7/fulltext/images/a468f3785ac932ffd9e55f8d0309a19362310647187fe792f2e0c90cb9531baa.jpg)

## 3.1. Architecture

CONQUER is supported by the architecture shown in Figure 3 and contains internal components that we developed and external components from the Web.

The internal components include an interface, an inference engine that uses a local knowledge base, and a query constructor. The “interface” captures the user’s query in natural language, transforms it for processing, and presents the results to the user. The “local knowledge base,” conceived as a semantic net, similar to prior retrieval systems (Chen and Dhar 1990, Lee and Baik 1999), allows representation of the query as terms (nodes) and semantic relationships between terms (arcs) (Figure 4). It offers five types of relationships that serve as a semantic basis for constructing context aware queries: synonym (x is equivalent to y), hypernym/hyponym (x is a superclass/subclass of y), negation (x is not y), and candidate (x is related to y). The “inference engine” grows the semantic net by adding terms from the remote lexical and ontological knowledge sources and shrinks the network by pruning knowledge that is not related to the intended sense of the query terms. The “query constructor” uses the local knowledge base to construct context-aware Web queries using the syntax and Boolean constraints required by a given search engine. The external components include “remote knowledge sources” for lexical knowledge (WordNet) and ontological knowledge (DAML ontology library), and “search engines” (such as Google, AlltheWeb and AltaVista) that are invoked to execute the enhanced query.

The architecture and representation mechanism allow us to develop algorithms to operationalize the methodology. The algorithms make minimal assumptions: (a) a search is restricted to query terms and content in English (this assumption may be relaxed with the use of different external knowledge sources<sup>7</sup>), and (b) search engines allow Boolean operators, following the de facto standard of query construction on the Web.<sup>8</sup> Using minimal assumptions overcomes limitations in prior work, which has relied on strong assumptions such the document collection being augmented with data to support disambiguation or tailoring search algorithms to utilize data added to the document collection or expertise from the user (Hearst 1996, Sanderson 2000).

Figure 4 Semantic Net as the Core Representation Mechanism (an Example)  
![](/api/attachments/38MWGZD7/fulltext/images/67cb35665afacd288ae2993f1a8e130a71e291fa73a4ef834b6ace349d95b090.jpg)  
Note. Shaded nodes: original terms from query; Unshaded nodes: new knowledge from lexical and ontological sources.

## 3.2. Algorithms

We illustrate CONQUER with the query posited by Berners-Lee et al. (2001), that is, find Mom a specialist who can provide a series of bi-weekly physical therapy sessions, shortened to more closely approximate Web queries (Spink and Ozmutlu 2002, Spink et al. 2001), find doctors providing physical therapy. Our intended sense is the following, find a doctor’s office that has the staff to provide the needed physical therapy. The algorithms are described below following the three phases in Figure 2. The appendix presents the formal representation.

3.2.1. Phase 1: Identify Query Context. The first phase consists of three tasks (Table 1) that incrementally build the context after parsing the query terms from the users.

Task 1 Identify noun phrases: The query is parsed to identify nouns or noun-phrases that may be matched by words or word pairs in WordNet. For our example, this task would find one noun (“doctor”) and one noun phrase (“physical therapy”). These form the seed for constructing the semantic net (see Figure 5). The terms are linked by a “candidate” relationship based on their proximity in the query. The candidate relationship indicates that these terms are related but that the lexical or domain-specific nature of this relationship has not yet been identified.

Task 2 Build synonym sets: To identify the user’s intended sense of the term, each noun or noun phrase in the query is used to extract synsets from Word-Net. For example, the senses found in WordNet for the noun “doctor” include medical practitioner, theologian, and academic. Each synset comprises one to many synonyms. The synsets for each query term are added to the knowledge base, expanding the network for each term.

Task 3 Decide intended word sense: If a query does not contain enough terms to deduce the user’s intended word sense, user interaction is required (Voorhees 1994, Allan and Raghavan 2002). The user is presented with the synsets for each term in the query that has multiple senses (e.g., “doctor,” “physical therapy”) from which the user selects the intended sense. For example, the user may select “medical practitioner” instead of “theologian” for the term “doctor.”

Table 1 Tasks in Phase 1 of CONQUER

<table><tr><td>Task</td><td>Assumption</td><td>Assessment</td></tr><tr><td>1. Identify noun phrases by querying successive query terms in WordNet.</td><td>WordNet contains most common noun phrases.</td><td rowspan="2">Good support: WordNet is the highest-quality publicly available lexicon. It contains common synsets for most noun phrases (Ide and Veronis 1998).</td></tr><tr><td>2. Find relevant synsets for query terms in WordNet.</td><td>For each noun phrase, WordNet contains most common synsets.</td></tr><tr><td>3. Decide intended word sense: Select one synset for each noun phrase.</td><td>One synset reflects the desired word sense.</td><td>Moderate support: Quality of WordNet but inherent ambiguity of language (Fellbaum 1998).</td></tr></table>

Figure 5 Semantic Net After Completing Task 1  
![](/api/attachments/38MWGZD7/fulltext/images/9427b98865e8360bb0c302a6314797b97f3dbdb3140e2fc3db24a7cd7acb4da4.jpg)

3.2.2. Phase 2: Refine Query Context. The second phase (Table 2) refines the context by excluding terms that suggest unwanted word senses, and adding those that establish the intended context.

Task 4 Exclude unintended word senses: This task filters out pages that contain unintended senses of each term. Traditional and Web-based query expansion techniques augment queries with additional mandatory or weighted-terms but rarely filter out terms of an incorrect sense (Efthimiadis 2000, Greenberg 2001, Jansen 2000). An initial test of a CONQUER prototype (Burton-Jones et al. 2003) confirmed that such exclusion is crucial because of the vast number of results that can be returned on the Web. The difficulty is determining which senses to exclude without increasing user-interaction. CONQUER achieves this by inferring the unwanted senses as distinct from the user’s selected word sense. For example, if a user selects the “medical practitioner” sense for the query term “Doctor,” then the methodology infers that the user does not want pages associated with other senses such as theologian, children’s game, or scholar. Because WordNet orders its synsets by estimated frequency of usage, the methodology excludes the highest ranked sense of the term that is not selected by the user. For our example, this results in exclusion of the sense “doctor of the church” by including in the semantic net another node that is associated with a “negation” link to “Doctor” (Figure 6).

Task 5: Including hypernyms and hyponyms: The user can select hypernyms and/or hyponyms from WordNet and the DAML library. User interaction is required when selecting hyponyms from Word-Net and the DAML library because there is no way to automatically infer a user’s desired subclass from a given query. User interaction is also required when selecting hypernyms from the DAML library because the word senses of ontological terms are not listed. Prior research expanded queries with hypernyms and hyponyms to boost recall. However, in those studies, added query terms are typically optional, so the system returns results that match the original query term (e.g., doctor) or its superclass (medical practitioner) or subclass (general practitioner) (Voorhees 1994, Greenberg 2001). However, optional inclusion enhances recall but can reduce precision (Greenberg 2001), in contrast to requirements for Web-based queries, which prefer precision over recall (Hearst 1996, de Lima and Pederson 1999). Thus, our methodology includes hypernyms and hyponyms from WordNet and DAML for the user’s chosen synset as mandatory. For example, if the user selected the first sense of doctor in Table 3, Row 1, he or she could add a hypernym such as “medical practitioner” and/or a hyponym such as “specialist” to the semantic net, linked by a connection to the synonym “Doc.” Such terms are added in a mandatory fashion because each term on its own is polysemous (e.g., “doctor” has four senses in WordNet, while “specialist” has two senses), thus the inclusion of both can help clarify the intended word sense. Table 3 shows this may result in adding the hypernym “medical practitioner” to the semantic net, linked by the hypernym connection to “Doc.” Hyponyms (e.g., specialist) may also be added with the expectation that the original term would clarify the intended sense of the hyponyms. This is because the narrower term may also be polysemous (e.g., “specialist” has two senses in Word-Net). Table 3 shows hypernyms and hyponyms from the two sources. Figure 6 shows part of the extended semantic net for the refined query.

Table 2 Tasks in Phase 2 of CONQUER

<table><tr><td>Task</td><td>Assumption</td><td>Assessment</td></tr><tr><td>4. Mark exclusion of a word sense by excluding the first synonym from the highest-ordered synset not selected by the user.</td><td>It is sufficient to exclude just one term, rather than all irrelevant senses.</td><td>Moderate support: Quality of WordNet but inherent ambiguity of language (Fellbaum 1998).</td></tr><tr><td>5. Refine the context by including hypernyms and hyponyms from WordNet and DAML.</td><td>WordNet and DAML contain a sufficient number of hypernyms and hyponyms.</td><td>Good support: Size of WordNet (Fellbaum 1998) &amp; DAML(Ding and Fensel 2001).</td></tr><tr><td>6. Resolve inconsistencies by checking if the DAML terms to be added exist among the terms in the unwanted WordNet synsets.</td><td>WordNet synsets provide a sufficient number of synonyms to enable a match if it exists.</td><td>Good support: Size of WordNet and availability of synsets (Fellbaum 1998).</td></tr></table>

Table 3 Word Senses, Hypernyms and Hyponyms Obtained in Tasks 2–5

<table><tr><td>Term</td><td>Word sense (defined by synset)</td><td>Hypernym (superclass)</td><td>Hyponym (subclass)</td><td>Source</td></tr><tr><td rowspan="4">Doctor</td><td>Doc, Physician, MD, Dr</td><td>Medical practitioner, medical man</td><td>GP, specialist, surgeon, intern, extern, allergist, veterinarian</td><td>Lexicon (WordNet)</td></tr><tr><td>Doctor of the Church</td><td>Theologian, Roman Catholic</td><td>No hyponym listed</td><td>Lexicon (WordNet)</td></tr><tr><td>Doctor</td><td>Play, child&#x27;s play</td><td>No hyponym listed</td><td>Lexicon (WordNet)</td></tr><tr><td>Dr</td><td>Scholar, scholarly person, student</td><td>No hyponym listed</td><td>Lexicon (WordNet)</td></tr><tr><td>Physical therapy</td><td>Physiotherapy, physiatrics</td><td>Therapy</td><td>No hyponym listed</td><td>Lexicon (WordNet)</td></tr><tr><td>Doctor</td><td>Not specified in the DAML library</td><td>Qualification, Medical care professional, Health professional</td><td>PhD</td><td>Ontology (DAML)</td></tr><tr><td>Physical therapy</td><td>Not specified in the DAML library</td><td>Rehabilitation, Medical practice</td><td>No hyponym listed</td><td>Ontology (DAML)</td></tr></table>

Task 6 Resolve inconsistencies: This task ensures that the semantic net being constructed does not contain inconsistent assertions. Such inconsistencies arise because: (a) the synonym sets in WordNet are not necessarily orthogonal so a partially relevant word sense may be excluded in Task 4, (b) the DAML ontologies are of mixed quality (Hendler 2001), and (c) WordNet and the DAML ontologies may have differing views of a domain. To identify inconsistencies, the hyponyms and hypernyms of the query terms selected from DAML are checked against the synonyms of query term (in WordNet) that the user did not select as the desired word sense. For example, if a user selects the medical sense of “doctor” from the synsets returned from WordNet, but then selects “theologian” or “scholar” as his or her preferred DAML hypernym; this inconsistency requires user input for resolution. The semantic net is adjusted accordingly.

3.2.3. Phase 3: Execute Query. The final phase (Table 4) executes the query using publicly available search engines.

Task 7 Construct Boolean query: The semantic net is transformed into a query that follows the syntax required by search engines. This task automates query construction with Boolean operators to compensate for the possible lack of expertise of the users (Eastman and Jansen 2003). The Boolean constraints depend on the type of term, the connection to the node in the semantic net, and the rationale provided in the earlier tasks. For instance, the first synonym from the intended synset is added with the OR operator such as: query term OR synonym; the hypernyms or hyponyms are added with the AND operator such as: query term AND WordNet hypernym OR DAML hypernym AND WordNet hyponym OR DAML hyponym; and the first synonym from an unintended synset is added with the negation operator such as: query term AND NOT synonym. This transformation attempts to improve query precision, i.e., adding synonyms in combination with a hypernym or hyponym increases precision (unlike adding synonyms only, which increase recall at the cost of precision). Applying these transformations to our example and assuming the user chooses the “specialist” hyponym for “doctor” and the “medical practice” and “therapy” hypernyms for “physical therapy,” the query constructed is:

Figure 6 Extended Semantic Net Constructed after Tasks 2–5  
![](/api/attachments/38MWGZD7/fulltext/images/2d5607b7d2f61d38d3e789ebd50958158a541bd3f19a517958021b2c873bd737.jpg)  
Note. He: hypernym (superclass); ho: hyponym (subclass); n: negation; c: candidate; s: synonym; shaded ellipse: original terms from query; unshaded ellipse: new knowledge from lexical and ontological sources; dashed line: additional knowledge in Table 2 not shown to conserve space; arrow: inheritance.

Table 4 Tasks in Phase 3 of CONQUER

<table><tr><td>Task</td><td>Assumption</td><td>Assessment</td></tr><tr><td>7. Construct the query by transforming the semantic net into appropriate constraints using Boolean operators.8. Execute query on a publicly available search engine9. Present results to the user</td><td>Using Boolean operators to ensure term co-occurrence is a reliable basis for accepting pages.Web search engines do not conflict with or override the methodology.—</td><td>Good support:Usefulness of term co-occurrence if Boolean operators are used properly (Mandala et al. 1999).Good support:Web search engines (e.g., Google) do not use explicit query expansion. Thus, the methodology appears to add to, rather than conflict with, existing Web search engines.—</td></tr></table>

Doctor OR Doc AND “Specialist” AND NOT “Doctor of the church” AND “Physical therapy” OR physiotherapy AND (therapy OR “medical practice”).

Task 8 Execute query on search engine: The query construction in Task 7 uses common Boolean operators to ensure that the resulting query is not dependent on particular search engines. For example, an operator such as NEAR is not part of the query construction because some search engines allow it; others do not. Likewise, query expansion techniques in traditional information retrieval systems such as in TREC (Text Retrieval Conference (Harman 1993)) can add up to 800 terms to the query with varying weights (Qiu and Frei 1993). In contrast, Web search engines place limits on query length (e.g., Google only processes queries with 10 or fewer terms). Consequently, we limit the query to a small set of terms that are expressed with appropriate Boolean constraints. The query, expanded, transformed and constructed with appropriate Boolean operators is then used to invoke publicly available search engines.

Task 9 Retrieve and present results: Results from the search engine (URLs and “snippets” provided from the Web pages) are retrieved and presented to the user. The intended outcome of the CONQUER methodology is the execution of a context-aware query that results in higher precision (more relevant) results. This is a key evaluation metric for our research.

## 4. Implementation

The methodology was implemented via J2EE technologies in a prototype (CONQUER) that interfaces with existing search engines. The implementation follows the formalisms in the appendix and the architecture in Figure 3. The prototype has three key components: (a) Interface and Parser Module, (b) Local Knowledge-Base and Inference Engine, and (c) Query Constructor. The “interface & parser module” parses a user’s query for nouns and noun phrases using QTAG (http://www.english.bham.ac.uk/staff/omason/software/ qtag/html). The “local knowledge base & inference engine” interfaces with WordNet via JWordNet (http://sourceforge.net/projects/jwn/) and the DAML library via Teknowledge’s DAML Semantic Search (http://www.daml.org/search), to execute tasks in Phases 1 and 2 and constructs the semantic net. To reduce user interaction, the module automatically selects the first hypernym suggested by WordNet for the user’s selected synset. To ensure that the eventual query is not unduly large, it restricts user input regarding hypernyms to one from WordNet and the DAML ontology library for each query term. The “query constructor” transforms the semantic net into a query following standard search syntax. It requests

Figure 7 Parsing the Original Query and Word Sense Selection  
![](/api/attachments/38MWGZD7/fulltext/images/d99124eb8cf109b13ea7ca3912d21b10fb901be2f5b005e8422df8e4dfe0a69e.jpg)  
the first 20 pages from both search engines, returning the title of the page, the snippet, and the URL for each page for presentation to the user.

## 4.1. Illustrative Scenario

The user interface is shown in Figure 7 for the query: “Find a department chair in Atlanta.” The interface and parser module extracts the user’s input and parses it. The noun phrases are displayed (Figure 7) and the user can eliminate those that are not relevant or appropriate. The selected terms form the initial query.

The prototype retrieves word senses for each query term and displays them to the user who selects the appropriate sense. If none are selected, the module uses the user’s original query term. In Figure 7, “chair” has four senses. After selecting the appropriate one, the user initiates the query refinement process. The module gathers the user selections and executes additional tasks (4 through 7) to expand the underlying semantic net. For example, a synonym could be identified and added to the semantic net; i.e., “chair” is expanded with the first term in the user’s selected synset (i.e., chair OR professorship). A synonym of chair is also added as negative knowledge from the next highest synset that has a synonym to exclude unrelated hits (i.e., chair AND NOT president). For each term, the hypernyms and hyponyms (superclass and subclass) corresponding to the selected word sense are retrieved from WordNet and the DAML ontology and displayed (Figure 8). The user-selected hypernyms and hyponyms are added to the semantic net, which is transformed and submitted to Google (Figure 9).

Figure 8 Selecting Hypernyms and Hyponyms from WordNet and DAML  
![](/api/attachments/38MWGZD7/fulltext/images/65a5c8c29667a64995c11d71e5d197e9227a3f7a622b4d430be186defc8e6330.jpg)

## 5. Empirical Evaluation

To assess the methodology’s effectiveness, a laboratory study was carried out. The study compared results obtained by a control group (without CONQUER) against those obtained by an experimental group (with CONQUER) using the same search engine. The key evaluation metric was the relevance of Web pages retrieved.

## 5.1. Treatment and Dependent Variables

The hypothesis posited for the experiment was that users would judge query results returned by CONQUER as more relevant than results obtained from a search engine alone (Figure 10). Because users do not view many Web page results (Buckley and Voorhees 2000, Spink et al. 2001), the dependent variable was the number of relevant pages in the first 10 pages returned (R1[10]). Several variations of this variable were created for sensitivity analysis. First, data was collected on the number of relevant pages in the first 10 and first 20 pages (R[10] and R[20]) (Buckley and Voorhees 2000). Second, each subject reviewed the title and snippet of each page returned to indicate whether the page was relevant, partially relevant, or not relevant for his or her query (Efthimiadis 2000). This provided two additional measures of relevance: R1 (the number of relevant pages) and R2 (the number of relevant or partially relevant pages), i.e., one primary dependent variable, R1[10], and three variations for sensitivity analysis: R2[10], R1[20], and R2[20]. Recall was not tested because it was not considered important for the study, and it is not strictly measurable on the Web (Efthimiadis 2000).

To increase generalizability, the experiment tested two control variables: (a) query term ambiguity and (b) search engines (Figure 10). Query term ambiguity refers to the extent to which query terms are clear. Although we posited no specific hypotheses regarding this variable, we anticipated that query term ambiguity would negatively impact results precision, operationalized as the relevance of pages retrieved. Because CONQUER was aimed at improving query term clarity, it was possible that it could have a greater benefit when search terms were more ambiguous, i.e., an interaction effect (Figure 10). The second control variable, search engines, tested whether the benefits of CONQUER would be independent of search engines. Two search engines were selected: Google and AlltheWeb. Google was selected because of its dominance in the search engine market and its success in using link-based indices and page rankings to provide accurate results. Any improvements over the commercial technology implemented by Google would be powerful indicators of the potential of CONQUER. AlltheWeb was selected because it uses the second highest rated search engine technology, indexing provided by Yahoo!, but focuses only on search (whereas Yahoo! focuses on other services as well). Including AlltheWeb also ensured that the results were not peculiar to any possible interactions between the page ranking technology employed by Google and the heuristics contained in CONQUER.

Figure 9 Presentation of Results to User  
![](/api/attachments/38MWGZD7/fulltext/images/cd7e6cd42edbc7ed676bbfb4cce2093f3f16d5e66541f7a6bba316221866f0bb.jpg)

## 5.2. Query Sample

Construction of the query sample was dictated by the following considerations. First, a large body of diverse queries had to be tested (per Buckley and Voorhees 2000). Second, to evaluate the benefits of CONQUER, a query had to contain terms that exist in WordNet or DAML. In relation to this second point, we recognized that users in practice may use query terms that do not yet exist in WordNet or DAML (e.g., brand names of some products). Thus, the query sample was created as follows.

Figure 10 Empirical Evaluation  
![](/api/attachments/38MWGZD7/fulltext/images/2996450015013a3b91487904c61984094dfc21019428564c2d7e1dd181f5269c.jpg)

First, all single-word classes from the DAML library were extracted. These were then pruned by excluding terms that either (a) had no superclasses in the DAML library, or (b) would be unfamiliar to subjects (e.g., highly specialized terms). This resulted in 280 terms, which were divided into two groups based on their number of word senses in WordNet. The clear group (139 terms) had zero–two word senses, where zero represented a domain-specific term not in Word-Net. The ambiguous group (141 terms) had three or more word senses. Each subject was provided a randomly generated list of 26 terms that were derived from either the clear or the ambiguous group. (A pilot test found that 26 terms was an appropriate number.) The result of the random assignment was that 38 subjects received a list of clear terms, and 33 received a list of ambiguous terms. Subjects were then asked to construct four queries: two containing terms from the list provided to them, and two without any constraints. This enabled us to include “query term ambiguity” as a between-groups factor in the experiment.<sup>9</sup> The queries were formulated in natural language and, consistent with Web queries in practice, were required to be short, including approximately two nouns each (Spink et al. 2001, Spink and Ozmultu 2002). Examples include: “Find a school in Georgia;” “Find soul food recipes;” and “Find wood furniture for office.”

Figure 11 Experimental Design

<table><tr><td rowspan="4">Search engine Google Allthe-Web</td><td colspan="2">Clear terms</td><td colspan="2">Ambiguous terms</td><td rowspan="2">With CONQUER</td><td rowspan="2">Without CONQUER</td></tr><tr><td>With CONQUER</td><td>Without CONQUER</td><td>With CONQUER</td><td>Without CONQUER</td></tr><tr><td colspan="2">Clear terms</td><td colspan="2">Ambiguous terms</td><td rowspan="2">With CONQUER</td><td rowspan="2">Without CONQUER</td></tr><tr><td>With CONQUER</td><td>Without CONQUER</td><td>With CONQUER</td><td>Without CONQUER</td></tr></table>

## 5.3. Experimental Design and Procedure

Seventy-one students from two universities participated voluntarily. They were experienced search engine users, recording a mean of 6 on a 7-point Likert-scale that asked whether the subjects frequently used search engines. The subjects were required to build their own queries in the manner described in the previous section. Each subject contributed four queries. They also evaluated the results because an assessment of whether a result is relevant to a user is one that cannot objectively be made by the researchers (Gordon and Pathak 1999). Figure 11 summarizes the experimental design. Each subject performed each query with and without CONQUER, and used two search engines. Thus, CONQUER and “Search Engine” were within-groups factors and “query-term ambiguity” was the between groups factor.

Each subject received materials explaining how CONQUER operates, how to construct queries, and how to grade the relevance of the results. Each subject’s materials stipulated the order of queries he or she was required to run, and the 26 randomly selected terms based upon the group to which the subject had been assigned (clear or ambiguous). The subjects were given a 10-minute training exercise to introduce them to CONQUER, and to practice developing a query and ranking results. Next, each participant developed his or her queries. Queries 1 and 3 required the user to use the list of terms provided. Queries 2 and 4 allowed the user to use any terms he or she wished. Because the “AlltheWeb” search engine was expected to be less familiar to subjects, the training session and first two queries used AlltheWeb; Queries 3 and 4 used Google. Figure 12 summarizes the procedure with the cells in the figure corresponding to the design in Figure 11.

The experiment took approximately 45 minutes. Subjects were given three minutes to execute each query and four minutes to rank the relevance of the first 20 pages returned from each system (two minutes to rank the 20 pages from CONQUER, and two minutes to rank the 20 pages from the search engine alone). The subjects were given a short time (approximately 6 seconds per page) to assess the relevance of pages because this was considered typical of Webuser behavior (Spink et al. 2001). A pre-test and a pilot test with 49 students indicated that these times were sufficient without burdening the subjects. Of the total number (284) of possible cases, some (23) had to be discarded due to missing values. Thus, the results are based on 261 cases.<sup>10</sup>

Figure 12 Experimental Procedure (N <sub>=</sub> No. Respondents).

<table><tr><td rowspan="5">Search engine Google Allthe-Web</td><td colspan="3">Terms</td></tr><tr><td>Constrained</td><td>Unconstrained</td><td></td></tr><tr><td>Query 1Clear or ambiguous terms performed with and without CONQUER</td><td>Query 2Ambiguity of terms unknown performed with and without CONQUER</td><td>N = 142</td></tr><tr><td>Query 3Clear or ambiguous terms performed with and without CONQUER</td><td>Query 4Ambiguity of terms unknown performed with and without CONQUER</td><td>N = 142</td></tr><tr><td>N = 142N (clear) = 76, N (ambiguous) = 66</td><td>N = 142</td><td>N = 284</td></tr></table>

## 5.4. Results

Table 5 presents the results, which show that the hypotheses were supported. On average, users received 1.5 additional relevant pages (5.38–3.83) in their first 10 pages when using CONQUER (a 15% increase). Table 5 shows consistent support in each sub-sample.<sup>11</sup> A final test was performed for each sub-sample across all four measures of the dependent variable: R1[10], R2[10], R1[20], and R2[20] (not shown to conserve space), each of which supported the hypothesis.

Table 6 summarizes the testing of the main effects and interaction effects for each control variable. Both control variables had a significant main effect on relevance. The results were more relevant when the queries were clear and/or when Google was used. The table also shows that the benefit of CON-QUER does not appear to be moderated by the ambiguity of query terms (i.e., the interaction term for CONQUER  Term Ambiguity is insignificant).

Overall, it appears that queries do not have to be highly ambiguous for CONQUER to be useful; even marginally ambiguous queries can benefit. The results also show that the benefit of using CONQUER was significantly greater when used with Google. This was unexpected and may reflect the ability of some search engines to more effectively utilize the expanded query constructed by CONQUER.

Overall, the results in Tables 5 and 6 consistently support the study’s hypothesis. The effect sizes, although statisically significant, are not large. Averaging across all sub-samples, CONQUER increased the number of relevant pages from approximately 4.5 out of 10 to 6 out of 10. The benefit ranged from two additional relevant pages (out of 10) when query terms were ambiguous or when Google was used, to approximately one additional relevant page (out of 10) when query terms were clear or when AlltheWeb was used. This may not be a substantial increase for only one search. However, with numerous searches every day, the aggregate impact over time can be considerable (Jansen and Molina 2006). Moreover, these results suggest that CONQUER will be especially helpful in situations, when (a) the results of the search are extremely important (every additionally relevant page is crucial), or (b) the results of the search represent fragments, where every additionally relevant page provides another vital part of the overall solution.

An exploratory analysis was performed to assess the contribution of different knowledge sources (lexical or ontological) on the outcomes. We examined queries with constrained terms (72 with clear terms and 62 with ambiguous terms (Table 5)) to ascertain how the results were affected by knowledge source. Subjects added terms to 122 of these 134 queries. For each query, we coded the source of each term added by the subject as lexical (WordNet) or ontological (the DAML library). Of these queries, 100% included terms from WordNet; whereas only 30% included terms from DAML. Thus, subjects chose not to add ontological terms for 70% of the queries. However, in the 30% of cases where subjects added terms from the DAML library, these terms assisted the query (t 63, p 000). Table 7 summarizes these results.<sup>12</sup>

Table 5 Test of Differences in Relevance Due to CONQUER

<table><tr><td rowspan="2">Sample</td><td colspan="2">Mean</td><td rowspan="2">Std. error for diff.</td><td rowspan="2">t-statistic</td><td rowspan="2">Significant 1-tailed</td><td rowspan="2">Result expected?</td></tr><tr><td>With CONQUER</td><td>Without CONQUER</td></tr><tr><td>Full sample (N=261)</td><td>5.38</td><td>3.83</td><td>0.252</td><td>6.13</td><td>0.000</td><td>Yes</td></tr><tr><td>Unconstrained terms (N=127)</td><td>5.5</td><td>4.4</td><td>0.39</td><td>2.66</td><td>0.005**</td><td>Yes</td></tr><tr><td>Constrained terms, clear (N=72)</td><td>5.4</td><td>3.5</td><td>0.42</td><td>4.34</td><td>0.000**</td><td>Yes</td></tr><tr><td>Constrained terms, ambiguous (N=62)</td><td>5.2</td><td>3.0</td><td>0.47</td><td>4.70</td><td>0.000**</td><td>Yes</td></tr><tr><td>AlltheWeb (N=135)</td><td>4.4</td><td>3.7</td><td>0.36</td><td>2.09</td><td>0.020*</td><td>Yes</td></tr><tr><td>Google (N=126)</td><td>6.3</td><td>4.0</td><td>0.33</td><td>7.13</td><td>0.000**</td><td>Yes</td></tr></table>

Notes. Dependent variable: R[10]: Number of relevant pages in the first 10 pages returned.  
<sup>†</sup>N Number respondents. It is less than the maximum due to missing values.  
∗Significant at  < 005 1-tailed, ∗∗at  < 005 1-tailed (Bonferroni adjusted). The adjusted alpha 005/5 001.

Further tests showed that the results in Table 7 were not affected by the ambiguity of query terms. In the “ambiguous” group, subjects chose ontological terms in 28% of the queries, and in the “clear” group, subjects chose ontological terms in 31% of the queries. Likewise, term ambiguity did not moderate the benefit of CONQUER in either the lexical subsample (F <sub>=</sub> 14, df <sub>=</sub> 241, p <sub>=</sub> 024) or the ontological and lexical subsample (F  16, df  75, p  020).

A final analysis was performed to evaluate whether users perceived the benefits of CONQUER to be worth the effort. At the end of the experiment, subjects completed a questionnaire regarding their perception of the usefulness of using CONQUER to that of using a search engine (Google) alone. The questionnaire used a 7-point Likert scale, was reliable (Cronbach’s alpha  092), and contained four items, asking the users to evaluate if CONQUER, “Compared to Google alone”: (1) enables me to find good information faster, (2) is useful for searching information on the Web, (3) improves my performance in Web querying, and (4) increases my productivity in searching the Web.” The mean response for the scale was 4.83 out of 7. The difference between subjects’ responses and a baseline score of 4.0 (the expected score if the system were no more useful than Google) was statistically significant (t 62, df 67, p 000). This indicates that subjects rated CONQUER somewhat more useful than Google, in spite of the additional interaction it required. The baseline provided by Google, as the dominant search engine (Sullivan 2005), makes this a strong outcome. Consistent with the results in Table $6 ,$ subjects’ perception of the usefulness of CONQUER

Table 6 Effects of Control Variables

<table><tr><td>MANOVA $^{\dagger}$ </td><td>Factor</td><td>F-statistic</td><td>Significance (2-tailed)</td><td>Effect size (eta squared) $^{\ddagger}$ </td></tr><tr><td rowspan="3">Main effects</td><td>CONQUER</td><td>12.47</td><td>0.000***</td><td>0.09</td></tr><tr><td>Search term ambiguity</td><td>2.81</td><td>0.004***</td><td>0.02</td></tr><tr><td>Search engine</td><td>7.48</td><td>0.000***</td><td>0.06</td></tr><tr><td rowspan="2">Interaction effects</td><td>CONQUER × Term ambiguity</td><td>1.47</td><td>0.166</td><td>0.01</td></tr><tr><td>CONQUER × Search engine</td><td>2.18</td><td>0.070*</td><td>0.02</td></tr></table>

Key: <sup>†</sup>MANOVA statistics calculated using Pillai’s trace including all DVs (i.e., R1[10], R2[10], R1[20], R2[20]).

Table 7 Exploratory Results of Contribution of Different Sources

<table><tr><td>Test</td><td>Subsample (queries by source of terms)</td><td>N</td><td>Mean with CONQUER</td><td>Mean without CONQUER</td><td>Std. error for diff.</td><td>t-statistic</td><td>Significant 1-tailed</td><td>Result as expected?</td></tr><tr><td rowspan="2">Knowledge sources</td><td>Lexical</td><td>122</td><td>5.48</td><td>3.25</td><td>0.322</td><td>6.92</td><td>0.000**</td><td>Yes</td></tr><tr><td>Ontological and lexical</td><td>36</td><td>5.72</td><td>2.53</td><td>0.504</td><td>6.34</td><td>0.000**</td><td>Yes</td></tr></table>

Notes. Dependent variable: R[10]: Number of relevant pages in the first 10 pages returned.  
∗Significant at  < 005 1-tailed, ∗∗at  < 005 1-tailed (Bonferroni adjusted; 005/6 <sub>=</sub> 0008).

compared to Google was consistent across queries and did not depend upon the ambiguity of query terms $( F = 0 . 2 0 , d f = 6 7 , p = 0 . 6 6 )$ . Overall, the results indicate that, first, the benefit of CONQUER does not come from one particular knowledge source. Rather, both sources are useful, by enabling users to choose an appropriate piece of knowledge for a given query. Second, users value CONQUER despite the additional effort required to operate it.

## 5.5. Implications of the Research Approach

A clear and verifiable contribution of the research is a design artifact and a design methodology, satisfying the design science research requirements (Hevner et al. 2004), as summarized in Table 8.

The work contributes to the Web search literature, which includes diverse approaches ranging from traditional search to the question-answer approach<sup>13</sup> (Cao et al. 2005, Roussinov and Robles 2004) among others, and responds to the grand challenge of dealing with semantics on the World Wide Web. In doing so, we satisfy the problem relevance guideline for design research (Hevner et al. 2004). The semantic net representation of CONQUER is consistent with recent research that has examined human communication using network models of text (e.g., McPhee et al. 2002, Corman et al. 2002). Using such as accepted representation scheme helped improve research rigor. Underlying the CONQUER methodology is a set of formalisms shown in the appendix. These formalisms represent the discovery of a solution that satisfies the design as a search process guideline. The two knowledge sources, ontologies and lexicons, are complementary and provide a broad coverage of relevant knowledge.<sup>14</sup> The development of the CONQUER methodology and its implementation meets the design as an artifact guideline.

An important metric for evaluation of the methodology is the precision of the search results. The empirical study shows that the CONQUER methodology yields results that represent an improvement over those provided by a search engine alone. The laboratory experiment and results rigorously demonstrate the utility, quality, and efficacy of the design artifact via well-executed evaluation methods, satisfying the design evaluation guideline. The organizational implications of the methodology complement a knowledge management perspective (Edgington 2004), where explicit knowledge may be available on the intranet. The communication of this research is through the detailed description of the methodology and the articulation of its application.

The study has several limitations. First, more extensive testing is needed to assess the relative contributions of the knowledge sources. Specifically, it would be useful to devise experimental designs that can rule out potential demand effects and order effects that we could not completely rule out, consider the use of multiple lexicons and ontology libraries, and investigate users’ intent to use the system in practice. Second, the CONQUER methodology should be expanded in terms of its flexibility, scalability, extensibility, and applicability to different settings. These extensions could be done by developing organizationspecific or industry-specific versions of CONQUER, and accommodating new approaches to representing semantics as research in conceptual modeling, linguistics, and computer science evolves.

Table 8 Mapping Against Design Science Guidelines

<table><tr><td>Guideline (Hevner et al. 2004)</td><td>Contribution</td></tr><tr><td>Design as an artifact</td><td>The research outcomes (1. CONQUER methodology, 2. extension and operationalization of constructs such as term-occurrence, 3. underlying mechanisms, and 4. prototype implementation) can be mapped against methods, constructs, models, and instantiation.</td></tr><tr><td>Problem relevance</td><td>Research problem responds to the grand challenge of incorporating semantics into the search process.</td></tr><tr><td>Design evaluation</td><td>Utility and efficacy of design outcome demonstrated by experimental study.</td></tr><tr><td>Research contributions</td><td>Design artifact and design construction knowledge that extend and improve the knowledge embedded in search engines.</td></tr><tr><td>Research rigor</td><td>Use of semantic net formalism for query construction and design evaluation.</td></tr><tr><td>Design as a search process</td><td>Discovery of an effective solution in the form of CONQUER; use of clear versus ambiguous terms and multiple search engines to characterize appropriate environments.</td></tr><tr><td>Communication of the research</td><td>Formalisms of technical details for technology-oriented audiences; implications and opportunities for management-oriented audiences.</td></tr></table>

## 6. Conclusion

This research presents a methodology for contextaware query processing on the Web by using existing ontological and lexical sources. The methodology adapts the theory of term co-occurrence (van Rijsbergen 1977) and uses word sense disambiguation to add context to queries. These ideas have been notoriously difficult to operationalize (Sanderson 2000, Stevenson 2003).

There are three main results of this work. First, this research demonstrates that it is possible to leverage existing knowledge sources (i.e., WordNet and DAML ontologies) to improve the processing of queries on the Web. Specifically, it highlights the need to improve the accuracy and completeness of these publicly available sources. Although the underlying theoretical bases (term co-occurrence and word sense disambiguation) have been articulated, effective query augmentation and refinement methodologies do not exist. This research could be extended to support search problems in other domains such as Semantic Web services in which users search for services in a registry (McIlraith et al. 2001).

Second, our work represents an effort to understand the obscure, often protected, algorithms that commercially available search engines use to improve search results (Stevenson 2003). Increasingly, these search engines encourage users to personalize their search pages (e.g., my.yahoo.com and Google personalization tools), presumably to improve search results.<sup>15</sup> The CONQUER methodology is an alternative to such personalization, allowing the users to retain greater control over their personal details.

Third, the CONQUER methodology has clear applications for searching within organizations. Many organizations allow users (internal and external) to search the content hosted on their Web site (on the intranet as well as on the public pages). For example, a customer may search IBM.com for information regarding software drivers for a product, or an employee at Accenture may search for information on a particular methodology on its intranet. These searches are currently dominated by adaptations of public search engines such as Google or A9 (e.g., amazon.com). The CONQUER methodology could enhance these searches by adding context from organization-specific knowledge sources.

Further research is needed to improve the CON-QUER methodology to make it more scalable and applicable in different settings. Additional empirical analysis is needed to investigate the use of multiple lexicons and ontology libraries. Finally, CONQUER could be employed as a front-end to organizational knowledge repositories.

## Acknowledgments

This research was supported by Georgia State University and Oakland University. Earlier versions of this research were presented at the Twenty-Third International Conference on Information Systems, the Twenty-Second International Conference on Conceptual Modeling and research seminars at Emory University and the University of Houston. The authors thank Cecil Chua, Punit Ahluwalia, and Yi Ding for their help during various phases of the research. They also thank the Senior Editor, Associate Editor, and three anonymous reviewers for Information Systems Research for their helpful comments throughout the review process.

## Appendix A. Formal Expressions of Mechanisms in CONQUER

## Figure A.1 Identifying Noun Phrases (Phase 1, Task 1)

$$
\mathrm{QT} = \left\{\mathrm{T} _ {1}, \mathrm{T} _ {2}, \mathrm{T} _ {3}, \dots , \mathrm{T} _ {\mathrm{n}} \right\}
$$

$$
\mathrm{QT}
$$

$$
\mathrm{NP} _ {\mathrm{i}} = \mathrm{T} _ {\mathrm{i}} + \mathrm{T} _ {\mathrm{i+1}}
$$

$$
\mathrm{NP} _ {\mathrm{i}} \in \left\{ \begin{array}{l} \text { NP } _ {\mathrm{i}} \in \left\{ \begin{array}{l} \text { NP } _ {\mathrm{i}} \in \left\{ \begin{array}{l} \text { NP } _ {\mathrm{i}} \in \left\{ \begin{array}{l} \text { NP } _ {\mathrm{i}} \in \left\{ \begin{array}{l} \text { NP } _ {\mathrm{i}} \in (\text { NP }) \\ \text { NP } _ {\mathrm{i}} \in (\text { NP }) \end{array} \right. \end{array} \right. \end{array} \right. \end{array} \right. \end{array} \right.
$$

$$
\mathrm {T_ {i + 1}}
$$

$$
\mathrm{NP} _ {\mathrm{i}}
$$

## Figure A.2 Constructing an Initial Semantic Net (Phase 1, Task 2)

$$
\mathrm {TN_ {i}}
$$

$$
\mathrm{TN} _ {\mathrm{i+1}}
$$

## Figure A.3 Adding Word Senses to the Semantic Net (Phase 1, Task 3)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
// For each term, get the word senses from WordNet and create Syn nodes
let WS be a word senses set,  $WS = \{WS_{1}, WS_{2}, ..WS_{n}\}$ 
let each word sense set  $WS_{i}$  contain one or more synonyms,  $WS_{i} = \{Syn_{1}, Syn_{2}, \ldots, Syn_{n}\}$ 
for each term node  $TN_{i}$ 
    Get the word senses from WordNet,  $WS_{TN_{i}} = \{WS_{1}, WS_{2}, ..WS_{n}\}$ 
    for each word sense  $WS_{k}$  for the term  $TN_{i}$ 
    Create a synonym node,  $SynN_{k}$ 
    Create the edge connecting the nodes  $TN_{i}$  and  $SynN_{k}$  for the “synonym” relationship
end for
</div>

## Figure A.4 Shrink Semantic Net by Excluding Undesired Word Senses (Phase 2, Task 4)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
// Add negative knowledge node and delete irrelevant sense nodes
let WS$_{j}$ be the selected word sense based on user feed back/reasoning
let syn_added be false
let neg_added be false
for each word sense WS$_{k}$ for the term TN$_{i}$
    if WS$_{k}$ == WS$_{j}$ and not syn_added // from the selected wordsense, add the synonym
    WS$_{k}$ = {Syn$_{1}$, Syn$_{2}$, ..., Syn$_{n}$}
    if TN$_{i}$ ≠ Syn$_{m}$
    SynN$_{k}$ = Syn$_{m}$
    syn_added is set to true
    end if
    else
    if not neg_added // highest sysnset negative knowledge node added
    WS$_{k}$ = {Syn$_{1}$, Syn$_{2}$, ..., Syn$_{n}$}
    if TN$_{i}$ ≠ Syn$_{m}$
    Change the SynN$_{k}$ node to negative knowledge node, NegN$_{k}$
    NegN$_{k}$ = Syn$_{m}$
    Rename the edge to “negative” relationship
    neg_added is set to true
    end if
    else
    delete the SynN$_{k}$ node // once negative node added, remove other nodes
    delete the edge between SynN$_{k}$ and TN$_{i}$
    end if
    end for
end for
</div>

## Figure A.5 Grow Semantic Net by Adding Hypernyms and Hyponyms (Phase 2, Task 5)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
// Add Nodes for Hypernyms and Hyponyms
for each term node TN$_{i}$
    Get the hypernyms from WordNet, WNHe
    Create a WordNet Hypernym node, WNHeN$_{p}$  // Add WordNet hypernym nodes
    Create the edge connecting the nodes TN$_{i}$ and WNHeN$_{p}$ for the WordNet “hypernym” relationship
    Get the hypernyms from DAML ontology library, DMHe
    Create a DAML Hypernym node, DMHeN$_{q}$  // Add DAML hypernym nodes
    Create the edge connecting the nodes TN$_{i}$ and DMHeN$_{q}$ for the DAML “hypernym” relationship
end for
for each term node TN$_{i}$
    Get the hyponyms from WordNet, WNHo
    Create a WordNet Hyponym node, WNHoN$_{r}$  // Add WordNet hyponym nodes
    Create the edge connecting the nodes TN$_{i}$ and WNHoN$_{r}$ for the WordNet “hyponym” relationship
    Get the hyponyms from DAML ontology library, DMHo
    Create a DAML Hyponym node, DMHoN$_{s}$  // Add DAML hypernym nodes
    Create the edge connecting the nodes TN$_{i}$ and DMHoN$_{s}$ for the DAML “hyponym” relationship
end for
</div>

## Figure A.6 Resolving Inconsistencies (Phase 2, Task 6)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
// Present hypernyms and hyponyms to user and get feedback, resolve inconsistencies
for each term node TN$_{i}$
    let WS$_{j}$ be the selected word sense for term TN$_{i}$
    let WNHeN$_{a}$ and DMHeN$_{b}$ represent the selected hypernyms based on user feed back/reasoning
    let WNHoN$_{c}$ and DMHoN$_{d}$ represent the selected hyponyms based on user feed back/reasoning
    let cons_vilotation be false
    for each word sense WS$_{k}$ for the term TN$_{i}$ // check if selected DAML hypernym or hyponym
    if WS$_{k} \neq$WS$_{j}$ // conflicts with unselected wordsense
    WS$_{k}$ = {Syn$_{1}$, Syn$_{2}$, ..., Syn$_{n}$}
    if ((DMHeN$_{b}$ == Syn$_{m}$) OR (DMHoN$_{d}$ == Syn$_{m}$)
    cons_violation is set to true
    Get the user to select another DAML hypernym or hyponym
    end if
    end if
    if not cons_viloation
    for each hypernym or hyponym node of TN$_{i}$
    if WNHeN$_{i} \neq$WNHeN$_{a}$
    delete the WNHeN$_{i}$ node // delete unselected WordNet hypernym nodes
    delete the WordNet hypernym edge between the nodes WNHeN$_{i}$ and TN$_{i}$
    end if
    if DMHeN$_{i} \neq$DMHeN$_{b}$
    delete the DMHeN$_{i}$ node // delete unselected DAML hypernym nodes
    delete the DAML hypernym edge between the nodes DMHeN$_{i}$ and TN$_{i}$
    end if
    if WNHoN$_{i} \neq$WNHoN$_{c}$
    delete the WNHoN$_{i}$ node // delete unselected WordNet hypernym nodes
    delete the WordNet hypernym edge between the nodes WNHoN$_{i}$ and TN$_{i}$
    end if
    if DMHoN$_{i} \neq$DMHeN$_{d}$
    delete the DMHoN$_{i}$ node // delete unselected DAML hypernym nodes
    delete the DAML hypernym edge between the nodes DMHoN$_{i}$ and TN$_{i}$
    end if
    end for
    end if
end for
</div>

## References

Allan, J., H. Raghavan. 2002. Using part-of-speech patterns to reduce query ambiguity. Proc. 25th Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval. ACM Press, New York, 307–314.

Berners-Lee, T., J. Hendler, O. Lassila. 2001. The semantic web. Sci. Amer. (May) 1–19.

Buckley, C., E. M. Voorhees. 2000. Evaluating evaluation measure stability. Proc. 23rd Annual Internat. ACM SIGIR, Conf. Res. Development Inform. Retrieval., ACM Press, New York, 33–40.

Bunge, M. 1977. Treatise on Basic Philosophy: Volume 3: Ontology I: The Furniture of the World. Reidel, Boston.

Burton-Jones, A., V. C. Storey, V. Sugumaran, P. Ahluwalia. 2005. A semiotic metrics suite for assessing the quality of ontologies. Data & Knowledge Engrg. 55(1) 84–102.

Burton-Jones, A., V. C. Storey, V. Sugumaran, S. Purao. 2003. A heuristic-based methodology for semantic augmentation of user queries on the web. Conceptual Modeling-ER. I.-Y. Song, S. W. Liddle, T. W. Ling, P. Scheurmann, eds. Proc. 22nd Internat. Conf. on Conceptual Modeling, Springer, Berlin/Heidelberg, 476–489.

Cao, J., D. Roussinov, J. Robles, J. Nunamaker. 2005. Automated question answering from videos: NLP vs. pattern matching. Hawaii Internat. Conf. System Sci. IEEE Computer Society, Washington, D.C.

Chan, C. W. 2004. From knowledge modeling to ontology construction. Internat. J. Software Engrg. Knowledge Engrg. 14(6) 603–624.

Chen, H., V. Dhar. 1990. A knowledge-based approach to the design of document-based retrieval systems. ACM SIGOIS Bull. 11(2–3) 281–290.

Corby, O., R. Dieng-Kuntz, C. Faron-Zucker. 2006. Searching the semantic web: Approximate query processing based on ontologies. IEEE Intelligent Systems 21(1) 20–27.

Corman, S., T. Kuhn, R. McPhee, K. Dooley. 2002. Studying complex discursive systems: Centering resonance analysis of organizational communication. Human Comm. Res. 28(2) 157–206.

Cui, H., J.-R. Wen, J.-Y. Nie, W.-Y. Ma. 2002. Probabilistic query expansion using query logs. Proc. 11th World Wide Web Conf. ACM Press, New York, 325–332.

de Lima, E. F., J. O. Pedersen. 1999. Phrase recognition and expansion for short, precision-biased queries based on a query log. 22nd Annual Internat. ACM SIGIR Conf. Res. Development in Inform. Retrieval. ACM Press, New York, 145–152.

Deen, S. M., K. Ponnamperuma. 2006. Dynamic ontology integration in a multi-agent environment. 20th Internat. Conf. Advanced Inform. Networking Appl. IEEE Computer Society, Washington, D.C., 373–378.

Ding, Y., D. Fensel. 2001. Ontology library systems: The key to successful ontology re-use. Proc. 1st Internat. Semantic Web Working Sympos. Semantic Web Science Association, Karlsruhe, Germany, 93–112.

Eastman, C. M., B. J. Jansen. 2003. Coverage, relevance, and rank ing: The impact of query operators on web search engine results. ACM Trans. Inform. Systems 21(4) 383–411.

Edgington, T. et al. 2004. Adopting ontology to facilitate knowledge sharing. Comm. ACM 47(11) 85–90.

Efthimiadis, E. N. 2000. Interactive query expansion: A user-based evaluation in a relevance feedback environment. J. Amer. Soc. Inform. Sci. 51(11) 989–1003.

Embley, D. W. 2004. Toward semantic understanding—An approach based on information extraction ontologies. 15th Australasian Database Conf. Australian Computer Society, Inc., Darlinghurst, Australia, 18–22, 3–12.

Fellbaum, C., ed. 1998. WordNet: An Electronic Lexical Database. MIT Press, Cambridge, MA.

Gomez-Perez, A., M. Fernandez-Lopez, O. Corcho. 2004. Ontological Engineering. Springer-Verlag, London.

Gordon, M., P. Pathak. 1999. Finding information on the world wide web: The retrieval effectiveness of search engines. Inform. Processing and Management 35 141–180.

Greenberg, J. 2001. Automatic query expansion via lexical-semantic relationships. J. Amer. Soc. Inform. Sci. 52(5) 402–415.

Gruber, T. R. 1993. A translation approach to portable ontology specifications. Knowledge Acquisition 5 199–220.

Harman, D. 1993. Overview of the first TREC conference. Proc. 16th Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval. ACM Press, New York, 36–47.

Hearst, M. A. 1996. Improving full-text precision on short queries using simple constraints. Proc. Sympos. Doc. Anal. Inform. Retrieval, Information Science Research Institute, Las Vegas, NV, 1–16.

Hendler, J. 2001. Agents and the semantic web. IEEE Intelligent Systems 16(2) 30–37.

Hevner, A., S. March, J. Park, S. Ram. 2004. Design science in information systems research. MIS Quart. 28(1) 75–105.

Ide, N., J. Veronis. 1998. Introduction to the special issue on word sense disambiguation: The state of the art. Computational Linguistics 24(1) 1–40.

Jansen, B. J. 2000. An investigation into the use of simple queries on web IR systems. Inform. Res.: An Electronic J. 6(1) 1–13.

Jansen, B., P. Molina. 2006. The effectiveness of web search engines for retrieving relevant ecommerce links. Inform. Processing & Management 42(4) 1075–1098.

Jansen, B., U. Pooch. 2001. A review of web searching studies and a framework for future research. J. Amer. Soc. Info Sci. Tech. 52(3) 235–246.

Kishore, R., H. Zhang, R. Ramesh. 2004. A helix-spindle model for ontological engineering. Comm. ACM 47(2) 69–75.

Leavitt, N. 2006. Recommendation technology: Will it boost E-Commerce. IEEE Comput. 13–16.

Lee, J.-O., D.-K. Baik. 1999. SemQL: A semantic query language for multidatabase systems. Proc. 8th Internat. Conf. Inform. Knowledge Management. ACM Press, New York, 259–266.

Lee, J. K., S. J. Upadhyaya, H. R. Rao, R. Sharman. 2005. Secure knowledge management and the semantic web. Comm. ACM 48(12) 48–55.

Lenat, D. B. 1995. CYC: A large-scale investment in knowledge infrastructure. Comm. ACM 38(11) 33–41.

Mandala, R., T. Tokunaga, H. Tanaka. 1999. Combining multiple evidence from different types of thesaurus for query expansion. Proc. 22nd Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval. ACM Press, New York, 191–197.

McGuinness, D. L., R. Fikes, J. Hendler, L. A. Stein. 2002. DAML<sub>+</sub>OIL: An ontology language for the semantic web. IEEE Intelligent Systems 17(5) 72–80.

McIlraith, S. A., T. C. Son, H. Zeng. 2001. Semantic web services. IEEE Intelligent Systems (March/April) 46–53.

McPhee, R., S. Corman, K. Dooley. 2002. Organizational knowledge expression and management: Centering resonance analysis of organizational discourse. Management Comm. Quart. 16(2) 130–136.

Miller, G. A. 1996. Contextuality. J. Oakhill, A. Garnham, eds. Mental Models in Cognitive Science. Psychology Press, Hove, East Sussex, UK, 1–18.

Miller, G. A., R. Beckwith, C. Fellbaum, D. Gross, K. J. Miller. 1990. Introduction to WordNet: An on-line lexical database. Intl J. Lexicography 3(4) 235–244.

Mitra, M., A. Singhal, C. Buckley. 1998. Improving automated query expansion. Proc. 21st Annual Internat. Conf. Res. Development on Inform. Retrieval. ACM Press, New York, 1–15.

Moldovan, D. L., R. Mihalcea. 2000. Improving the search on the Internet by using WordNet and lexical operators. IEEE Internet Comput. 4(1) 34–43.

Oberle, D., S. Staab, R. Studer, R. Volz. 2005. Supporting application development in the semantic web. ACM Trans. Internet Tech. TOIT 5(2) 328–358.

Ozmutlu, S., H. C. Ozmutlu, A. Spink. 2003. Are people asking questions of general web search engines? Online Inform. Rev. 27(6) 396–406.

Peat, H. J., P. Willett. 1991. The limitations of term co-occurrence data for query expansion in document retrieval systems. J. Amer. Soc. Info Sci. 50(1) 49–64.

Pokorny, J. 2004. Web searching and information retrieval. Comput. Sci. Engrg. (Jan/Feb) 43–48.

Qiu, Y., H.-P. Frei. 1993. Concept based query expansion. Proc. 16th Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval. ACM Press, New York, 160–169.

Roussinov, D., J. Robles. 2004. Web question answering through automatically learned patterns. Proc. 4th Annual ACM/IEEE-CS Joint Conf. Digital Libraries. ACM Press, New York, 347–348.

Salton, G., C. Buckley. 1990. Improving retrieval performance by relevance feedback. J. Amer. Soc. Inform. Sci. 41(4) 288–297.

Sanderson, M. 2000. Retrieving with good sense. Inform. Retrieval 2(1) 49–69.

Snasel, V., P. Moravec, J. Pokorny. 2005. WordNet ontology based model for web retrieval. Proc. Internat. Workshop on Challenges in Web Inform. Retrieval and Integration. IEEE Computer Society, Washington, D.C., 220–225.

Sowa, J. F. 2000. Knowledge Representation: Logical, Philosophical, and Computational Foundations. Brooks Cole Publishing Co., Pacific Grove, CA.

Spink, A., H. C. Ozmutlu. 2002. Characteristics of question format web queries: An exploratory study. Inform. Processing Management 38(4) 453–471.

Spink, A., D. Wolfram, M. B. J. Jansen, T. Saracevic. 2001. Searching the web: The public and their queries. J. Amer. Soc. Inform. Sci. 52(3) 226–234.

Staab, S., A. Gomez-Perez, W. Daelemana, M.-L. Reinberger, N. F. Noy. 2004. Why evaluate ontology technologies? Because it works! IEEE Intelligent Systems 19(4) 74–81.

Stephens, L. M., M. N. Huhns. 2001. Consensus ontologies: Reconciling the semantics of web pages and agents. IEEE Internet Comput. 5(5) 92–95.

Stevenson, M. 2003. Word sense disambiguation: The case for combinations of knowledge sources. A. Copestake. ed. Studies in Computational Linguistics. CSLI Publications, Stanford, CA.

Storey, V. C., V. Sugumaran, A. Burton-Jones. 2004. The role of user profiles in context-aware query processing for the semantic web. Proc. 9th Internat. Conf. Appl. Natural Language to Inform. Systems, Springer, Berlin-Heidelberg, 51–63.

Sullivan, D. 2006. Nielsen NetRatings: Search engine ratings. Search engine watch, published August 22, 2006, online: http:// searchenginewatch.com/showPage.htm?.page=2156451, retrieved February 15, 2008.

Sure, Y., P. Hitzler, A. Eberhart, R. Studer. 2005. The semantic web in one day. IEEE Intelligent Systems 20(3) 85–87.

Tijerino, Y. A., D. W. Embley, D. W. Lonsdale, Y. Ding, G. Nagy. 2005. Toward ontology generation from tables. World Wide Web. 8(3) 261–285.

Todd, P., I. Benbasat. 1999. Evaluating the impact of DSS, cognitive effort, and incentives on strategy selection. Inform. Systems Res. 10(4, December) 356–374.

van Harmelen, F. 2004. The semantic web: What, why, how, and when. IEEE Distributed Systems Online 5(3) 1–4.

van Rijsbergen, C. J. 1977. A theoretical basis for the use of cooccurrence data in information retrieval. J. Documentation 33 106–119.

Veres, C. 2006. The language of folksonomies: What tags reveal about user classification. C. Kop, G. Fliedl, H. C. Mayr, E. Metais, eds. Proc. 11th Internat. Conf. Appl. Natural Language to Inform. Systems, NLDB, Springer, Berlin/Heidelberg, 58–69.

Voorhees, E. M. 1994. Query expansion using lexical-semantic relations. Proc. 17th Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval. Springer-Verlag, New York, 61–69.

Weber, R. 1997. Ontological Foundations of Information Systems. Coopers & Lybrand and Accounting Association of Australia and New Zealand, Melbourne, Australia.

Weber, R. 2002. Ontological issues in accounting information systems. S. Sutton, V. Arnold, eds. Researching Accounting as an Information Systems Discipline. American Accounting Association, Sarasota, FL, 13–33.

Xu, J., W. B. Croft. 1998. Corpus-based stemming using cooccurrence of word variants. ACM Trans. Inform. Systems 16(1) 61–81.
