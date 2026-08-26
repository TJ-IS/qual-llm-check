---
otero_id: 17720
otero_key: "WABGGUY5"
title: "Generating suggestions through document structure mapping"
authors: "Zhengxin Chen"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00024-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Generating suggestions through document structure mapping

Zhengxin Chen

Department of Computer Science, University of Nebraska at Omaha, Omaha, NE 68182-0500, USA

Received 19 June 1994; revised 14 February 1995, 22 July 1995

## Abstract

In this article we discuss the role of analogical reasoning for decision making and creativity support. In particular, we investigate the issue of how to apply structure mapping theory of analogical reasoning so that when requested information is not available, a new document can be generated through analogical reasoning using structure mapping. We also describe an implementation using schema-free relational databases, in which document structure mapping is realized as new tuple generation in schema-free relational databases.

Keywords: Creativity support systems; Analogy generation by computer; Database methods for analogy generation; Structure mapping

## 1. Introduction

## 1.1. Analogical reasoning for decision support

Metaphor or analogy plays an important role in human decision making. Metaphor differs from analogy in that it is defined from a rhetoric point of view, thus serving as a linguistic device. As noted by Carbonell and Minton (1983), analogical reasoning requires less cognitive effort than more formal types of reasoning; this fact could explain why analogical reasoning is so prevalent in human thought processes.

Analogy to existing problems gives a heuristic problem solving strategy in which the result or method of the related problem can be carried into the new problem. Analogies are similarities or likenesses between things otherwise different. Things which are similar in some respects tend to be similar in other respects. Therefore, previously remembered experiences are transformed and extended to fit new unfamiliar situations; the old and new situations need not be in the same domain. The two domains, the source domain and the target domain, are entirely different, but similarities between the relationships of objects remain strong, seemingly suggesting a likely consequence of the regularity of nature. For example, consider the well-known Rutherford analogy: "The atom is like the solar system". Here both the solar planetary system and the atom consist of a system of smaller bodies being attracted to and revolving around a more massive nucleus. In this example, the solar system is used as a source analog (or base analog) while the atom is used as a target analog. The flow of liquids in pipes and the flow of electricity in conducting wires provide another example of analogy.

Researchers in artificial intelligence (AI) and cognitive science have studied analogical reasoning and analogical problem solving with great enthusiasm. Various efforts have been made to operationalize the concept of analogy as heuristic inference. The two volumes edited by Michalski et al. (1983, 1986) reported some important progress made in the last decade. A nice summary of computational approaches to analogical reasoning is provided in Hall (1989).

Holsapple and Whinston (1987) predicted that knowledge-based systems in future knowledge-based organizations should be “computer coworkers” with the ability to “recognize needs, stimulate insights and offer advice”. Analogy and metaphor can provide an important role in offering advices. Research work has been conducted to support analogical problem solving or achieve creativity support systems through computerized metaphor generation. For example, in Young (1987, 1988), three levels have been defined for supporting metaphoric thinking: at the secretarial level, the framework-paradigm level, and the generative level. The three support levels are hierarchical and cumulative; thus the generative level includes the prior two levels. A database method was developed for purposes of automatically generating metaphors at the request of the user. In addition, analogy has been incorporated into model management systems using case based reasoning (Liang, 1991, 1993). Metaphor or analogy has been studied from other perspectives related to decision making (Vranes et al., 1992, Marchant et al., 1993, Cole and Stewart, 1993). However, automated support for analogical or metaphorical thinking in decision support systems is still an issue to be further investigated.

In this article, we explore the role of analogical reasoning for generation of suggestions for decision making. The goal of our study is somewhat similar to Young's metaphor engine (Young, 1987, Young, 1988); however, instead of focusing on similarity between pairs of individual terms, we have put our emphasis on the structural similarity between pairs of grouped sentences. We will refer a group of related sentences used to describe some scenario as a cognitive document (or simply document). Since previous successful decisions and other acquired knowledge can be treated as stored documents, if a decision need be made to deal with a new but similar scenario, a suggestion could be generated based on analogy. Our goal is also somewhat similar to the very interesting approach proposed by Liang (1993) which employs analogical reasoning and case-based learning for model management. However, since the problems faced by intelligent decision support systems are inherently unstructured and complex (Shaw, 1993), there is also a need to investigate the use of analogical reasoning on levels other than models, such as cognitive documents which deal with the structures at the syntax level.

## 1.2. Structure mapping theory of analogy

Generating suggestion from available cognitive documents implies a kind of knowledge creation through information retrieval by drawing inferences from what is already known. Analogical reasoning can play an important role in this regard. An influential theory on analogical reasoning called structure mapping theory (Gentner, 1983) is used in our approach as the foundation to perform the intended tasks. The following is based on Leishman's summary (Leishman, 1990) of this theory. A theory of analogy must describe how the meaning of analogy is derived from the meaning of its parts. In the structure mapping theory, the interpretation rules are characterized as implicit rules for mapping knowledge about a base domain into a target domain. An important feature of this theory is that the rules depend only on syntactic properties of the knowledge representation rather the specific content of the domains. There are two important mapping principles: (a) relationships between objects (rather than attributes of objects) are mapped from base to target; and (b) the particular relationships mapped are determined by systematicity, as defined by the existence of higher-order relations. An important notion called the systematicity principle formally captures the intuitive notion that since a structure mapping is supposed to transfer the structure of the source domain to the target domain, the relations that are richly interconnected are more likely to be transferred.

## 1.3. Objectives and organization of the paper

The theme of this paper is to investigate how to approach analog retrieval by extending computerized information retrieval so that suggestions can be generated as an aid for decision making. The structure mapping theory as summarized above is used to guide the generation of such suggestions. We will treat source analog retrieval as the first step of performing analogical reasoning or problem solving, rather than a preparation step for structure generation. Algorithms are described and examples are provided. In order to make this paper self-contained, some background information about our computational model and its implementation will also be briefly summarized.

The paper is organized as follows. In Section 2 we briefly review our computational model, and use an example to illustrate how to realize structure mapping in this model. A more concrete description for the steps of document structure mapping is provided in Section 3. In Section 4 we further discuss how to implement document structure mapping using schema-free relational databases. We conclude our paper in Section 5.

## 2. Structure mapping on cognitive documents

The uniqueness of our work in analogical reasoning lies in the perspective of applying structure mapping on short (cognitive) documents. These short documents are written in restricted English. We start with a sketch on a computational model for information retrieval. We will also provide an introductory example to illustrate how this computational model supports document structure mapping.

## 2.1. A computer model for intelligent information retrieval

Since our approach of document structure mapping is conducted on the computer model we developed for storage and retrieval short scientific documents written in restricted English defined by simple grammar, here we will briefly summarize this model. (More detail of this model can be found in Chen, 1993.)

The model consists of the following components. There is a document base D, which is the conceptual place to store the documents. There is also a knowledge base K consisting of nodes connected by links, which is the actual place to store the knowledge converted from the documents. Each acquired document is assigned a unique sequential identifier, converted to its internal form (called document stem) and then stored in a global knowledge base. We envision that each document stem occupies a certain area in the knowledge base, and each area is bound by its own boundary. A system component called document description list (or keyword list) L identifies the boundaries of the document stems. The system also consists of a conceptual memory which is a hierarchically structured thesaurus used for indexing of documents. Finally, the system has a set of mapping functions M between various system components, including the function f from D to K, which transforms the content of each document into its internal form; the function $f_{c}$ maps from C to K, which specifies the boundary of each document stem in the knowledge base; the function $f_{d}$ connecting D with L, which constructs an item in the document description list for each acquired document; and the function $f_{c}$ connecting C with L, which constructs the index for each document in the conceptual memory. The model is depicted in Fig. 1.

The model handles storage and retrieval in the following manner. The document description list of a document provides keywords which are used to index the document in the conceptual memory for the convenience of retrieval. The document description list also forms the boundary of the internal form (namely, the document stem) of the document. Upon a user's request, by searching through the conceptual memory, relevant documents will be identified, and a text (written in restricted English) will be reconstructed from a single document-stem or constructed from several document stems; in the latter case, the text is referred to as a fact.

In order to illustrate how the documents are stored, including how they are converted into document stems, let us consider the following document:

![](/api/attachments/WABGGUY5/fulltext/images/3c4d2f2b01d3c54e4b4c1264b87a0c2899f328d6da0e176912d03321d2343330.jpg)  
Fig. 1. The computational model for storage and retrieval.

a bat emits a sound.

the sound is inaudible.

an obstacle reflects the sound to the bat.

the obstacle is invisible.

the bat detects the obstacle.

A unique serial identifier is assigned to this document. The document is indexed in the conceptual memory. To facilitate future retrieval, an item corresponding to this document is added to the document description list, which consists of some indexed terms to form the boundary of the document stem (the internal form of the document) in the knowledge base. This document is converted into its internal form consisting of objects and relationships connecting them. The document stem is depicted in Fig. 2, where objects are represented by ellipses and relationships are represented by arcs. Each object and relationship is attached by a location number in the knowledge base.

The model has been implemented using schema-free relational databases; namely, the internal form of each document consists of relational tuples (Motro 1986). Since documents are written in restricted grammar, each sentence in the document consists of one or two relationships. These relationships are converted to one or two relationship tuples; the objects associated by relationships are converted to object tuples. The relationship tuples obtained from various sentences form the relationship list, and the object tuples form the object list. Articles (including the words “a”, “an”, “the”) are ignored.

![](/api/attachments/WABGGUY5/fulltext/images/f9fc266295f46513ad4820d5e23da02300d20750ba3d554a96bc193e7aaca5b7.jpg)  
Fig. 2. A document stem.

The tuples used to represent the bat example are shown in Table 1. Each object in the document written in the restricted English is converted to a tuple, consisting of its internal location in the global knowledge base, attribute values, and locations of relationships which connect it to some other objects. Each (binary) relationship in the document is converted to a tuple, consisting of its internal location in the global knowledge base, along with the attribute values, and the objects it connects to. The order of the two objects involved in a relationship is consistent with the direction of the arc in Fig. 2.

Table 1  
Tuples representing a document (later will be used as source analog)

<table><tr><td colspan="4">Object list is source analog:</td></tr><tr><td>location</td><td>object name</td><td>attribute</td><td>relationship location</td></tr><tr><td>109</td><td>bat</td><td></td><td>110, 114</td></tr><tr><td>111</td><td>sound</td><td>inaudible</td><td>110, 112</td></tr><tr><td>113</td><td>obstacle</td><td>invisible</td><td>112, 114</td></tr><tr><td colspan="4">Relationship list in source analog:</td></tr><tr><td>location</td><td>relationship name</td><td>attribute</td><td>object location</td></tr><tr><td>110</td><td>emits</td><td></td><td>109, 111</td></tr><tr><td>112</td><td>reflects</td><td></td><td>113, 111</td></tr><tr><td>114</td><td>detects</td><td></td><td>109, 113</td></tr></table>

A regular user query consists of a list of keywords provided by the user. The retrieval is handled in the following manner. First, the conceptual memory is searched to determine the relevant documents. If there is at least one document which satisfies all the keywords, from its boundary description (available from the document description list), the relevant tuples in the global knowledge base will be retrieved (using conceptual memory) to reconstruct an answer to the user. On the other hand, if no single document satisfies all the keywords specified by the user, a fact may be constructed by joining (namely, merging) two (or more) relevant document stems. Although each of these document stems can only satisfy several (but not all of the) keywords, together they can satisfy all the keywords specified by the user. As an example, suppose a user query consists of 6 keywords and no single document satisfies all of them. But the result of searching the conceptual memory also indicates that document with identifier 7 satisfies 4 keywords and the document with identifier 20 satisfies the other 2 keywords. In this case, the portion of document 7 which is relevant to the query will be identified, and the relevant portion taken from document 20 will also be identified. If these two portions share at least one object, a join operation can be applied to them so that an answer can be constructed. A more concrete discussion on the join operation is the major topic of Chen (1993).

Our computational model is suitable for structure mapping due to at least the following two reasons. First, the model provides a two-layer structure for handling documents; in other words, the model has kept the identity of each document for convenience of retrieval. Since retrieval of source analogs resembles retrieval of documents, techniques similar to conventional information retrieval can be used. Secondly, since the internal representation of the documents (rather than the original texts of these documents) are stored, the stored internal form of documents reveals some structure of the text, and facilitates structure comparison (as required by the structure mapping theory of analogical reasoning).

## 2.2. Generating suggestion: Basic idea and an example

The overview given in the last section indicates that our computational model provides dual modes to deal with user queries. On the one hand, if information requested by the user is available, a document is reconstructed from its internal form (called the document stem) in the knowledge base and presented it in the text format to the user. This is the regular mode which is already briefly described in the previous section. On the other hand, in case that the requested information is not available, the user may use the analogy mode to ask the system to generate a document using analogical reasoning. This generated document may serve as a suggestion or an advice to the user. One option could be considered here is to map the keywords in the query list submitted by the user to another list. For example, if the user wants to know how people deal with planes dispatched by enemies, he may submit a query “people, enemy, plane”. Suppose no relevant document is found. Since both the document description list and the query description list consist of objects, if a suggestion is to be generated using analogy reasoning, it has to be done by mapping of objects only. However, as we have briefly summarized in an earlier section, at the heart of the structure mapping theory is the mapping of relationships among these objects. Such structure information is not implied in the query consisting of keywords “people, enemy, plane”; it must be explicitly stated. In other words, in order to perform structure mapping, it is not enough for the user to simply enter a few keywords. A reasonable way to deal with this situation is to ask the user to provide some help. Although the user does not have the answer (otherwise he will not consult the system), he can still provide some information concerning the relationship between the objects to be retrieved. For example, he can tell the system what he knows, namely, the enemies have dispatched a plane and the plane is not visible; he should also tell the system what he wants to know, that is, how to detect the planes. The system can acquire such structural information by asking user to enter this query in a form similar to a document, but with some missing information to be filled. By doing so, the user describes the structure of the target analog; the system can then find one or more source analogs (ie., document stems) from which structure mapping can be performed to generate new structure so that the missing information in the target analog can be filled. The target analog, since it takes the form of a regular document, will be referred to as an incomplete document. Just like a regular document, an incomplete document is written in restricted English, but it differs from a regular one in that it contains unknown information to be answered. An incomplete document always has a sentence appearing at the end, started with a word “how” and ended with a question mark (“?”). In our example, the incomplete document takes the following form:

the enemy dispatch a plane.

the plane is invisible.

how people detect the plane?

The last sentence of an incomplete document indicates an unknown part, while the other sentences form the known part of the incomplete document (the known part is similar to a regular document). An incomplete document and its correspondent incomplete document stem will be denoted as $d^{-}$ and $\delta^{-}$ , respectively.

Now let us consider the entire process of suggestion generation. Suppose the user wanted to retrieve a document for detecting enemy's plane. He used the regular retrieval mode by providing several keywords but no relevant document could be retrieved. Then he had to switch to the mode of analogical reasoning. In order to let the system find a structural similar document, the user provided an incomplete document as shown above. To answer this query, the system formed a query description list from this incomplete document. In the simplest case, the query description list could be obtained by taking the first object (noun) of each sentence; in this example, it consists of "enemy, plane, people". What the system would perform is not to retrieve a document (or a fact) consisting the words in the query description list, but rather, a document (or a fact) which consists of words similar to the query description list and contains a portion which has the same structure with the known part of the incomplete document. The retrieved document (or fact) also contains a portion which does not have a counterpart in the incomplete document. The incomplete document can then be filled by mapping this portion into the domain which the incomplete document belongs to. A new document in the target domain is thus generated, which provides a suggestion to the user. If the user is satisfied with it, it can be further stored as a regular document.

Back to our example, assuming that the document concerning the bat is a document acquired by the system earlier, which has the structure similarity with the incomplete document, and can thus be used as a source (base) analog. This document will be retrieved. For convenience of our discussion, the document is repeated below.

a bat emits a sound.

the sound is inaudible.

an obstacle reflects the sound to the bat.

the obstacle is invisible.

the bat detects the obstacle.

The incomplete document itself, on the other hand, becomes part of the target analog. With the help of the conceptual memory, the system determines the similarity between the incomplete document and this existing document. Using a structure mapping algorithm (detail will be provided later), the system will generate the following document as a suggestion to fill the incomplete document originally provided by the user:

the enemy dispatch a plane.

the plane is invisible.

people emits [sound-like].

the [sound-like] is inaudible.

the plane reflects [sound-like] to the people.

people detects plane.

The third, fourth and fifth sentences in the above document are generated by the computer. Here a word in the pair of squared brackets [ ] indicates a new object generated through structure mapping. For example, the object [sound-like] is an object generated from the object “sound”; it means “something similar to the sound”.

As illustrated by this example, document generation using analogical reasoning is the process of filling an incomplete document stem $d^{-}$ (ie., the internal structure of the incomplete document provided by the user). This can be denoted as

$$
\delta = \delta_ {0} \bowtie \psi
$$

where $\delta$ is the completed document by filling $\delta^{-}$ , $\delta_{0}$ is the known part of $\delta^{-}$ and $\psi$ is the generated part through structure mapping, and $\bowtie$ is the join operation (as defined in Chen, 1994) of $\delta_{0}$ and $\psi$ . Since document stems are nodes and links in the knowledge base, both $\delta_{0}$ and $\psi$ can be treated as document stems.

In the previous incomplete document, we have $\delta^{0}$ :

the enemy dispatch a plane.

the plane is invisible.

and the generated part is

ψ:

people emits [sound-like].

the [sound-like] is inaudible.

the plane reflects [sound-like] to the people.

In general, the known part $\delta_{0}$ consists of more sentences, thus having a more complicated structure. This example is made simple so that the structure of the document can easily be visualized (as indicated in figures later in this paper).

Since the last few sentences are generated rather than retrieved, they are not necessarily true knowledge; in other words, they just form a suggestion to the user. In this example, these generated sentences suggest that in order to detect the enemy plane (as submitted as a user request), people may use some thing which is similar to the inaudible sound (as used by a bat) so that the invisible plane will reflect the sound to the people. This is of course a highly simplified reproduction of invention of radar (which is a device to produce inaudible sound for detecting distant objects).

## 2.3. Steps for analogical problem solving

We now describe the steps for performing document structure mapping in our computational model in terms of a general framework as summarized in Burnstein (1988). The framework provides a process theory of analogical reasoning consisting of six stages:

1. Base domain memory retrieval;

2. Comparison of base and target models;

3. Mapping a partial model from the base to the target;

4. Justification and integration of the mapped model;

5. Debugging the target model;

6. Generalization of shared structure.

For our purpose, we will only consider the first three stages. That is, we are satisfied with a suggestion which takes the form of a newly generated document in the target domain. Among these three stages, the first stage is also the most critical one, describing how this can be done in our system is the major purpose of our current paper.

In our system, steps 4 and 5 have been simplified on purpose. We treat a newly generated document (namely, the filled incomplete document) in the target domain as a suggestion or possible solution produced from the system's currently available knowledge, leaving the responsibility of determining the quality of the suggestion to the user. If the suggestion is acceptable, upon the user's request, the system will store it as a regularly acquired document.

According to the structure mapping theory, objects and relationships in the source (or base) domain are mapped into the target domain. In our computational model, we consider the structure mapping from a source analog (consisting one or more stored documents) to a target analog (which is a pseudo-fact). A pseudo-fact (where the term “fact” is used in the sense defined earlier in Subsection 2.1) is a document-like unit containing a portion which is generated through structure mapping.

In our implementation, parsing an incomplete document is similar to parsing a regular document. The internal form of the incomplete document (the document stem) is stored in a temporary area separated from the knowledge base. Each object or relationship is assigned a negative integer as its sequential location number (instead of a positive one, as used in the knowledge base), so that the incomplete document and the generated structure will not be mixed with the actual knowledge base. However, a procedure exists so that upon the user's request, the pseudo-fact can be converted as a regular document and is then stored in the knowledge base.

An overview on the general pseudo-fact generation process in our computational model (as well as in the experimental system) is depicted in Fig. 3.

## 3. Structure mapping for generating suggestions

We now provide some detail on structure mapping for generating suggestions. Since the basic idea of document mapping can be clearly illustrated in the case of source analog consisting of only one document, our discussion will be mainly around the case of using single document. The entire process of suggestion generation is to be performed as two steps: construct a document stem $\Delta$ as the source analog, followed by a mapping and structure generation process $\phi\Delta$ .

![](/api/attachments/WABGGUY5/fulltext/images/7716dc3f669f1ef222ff86e7b8ad11edfdd1c356b2fe9322b8884b68b4a817a4.jpg)  
\* (Solid lines indicate operations related to storage; dashed lines indicate operations related to query)
Fig. 3. Overview for pseudo-fact generation process.

As indicated in the previous section, parsing an incomplete document is similar to parsing a regular document. A little more detail is given below. A description list for this incomplete document (which will be referred to as a query description list), is constructed in the same way as for a document description list. In order not to let our basic idea intertwined with technical difficulties involving natural language processing, we have taken the following simplified treatment. If a sentence is a regular sentence, this list is constructed from the first noun of each sentence. On the other hand, if a sentence is a question, we first change the sentence from the original form into a form consisting an object with unknown name “?” and a relationship with unknown name “?”. The document stem converted from the incomplete document is stored in the temporary area separated from the knowledge base. There will be a sequential location number, but they will be indicated by a negative sign (instead of a positive one, as used in the knowledge base).

## 3.1. Overview and the general algorithm

We now describe the general process of using analogical reasoning to generate suggestions. The basic idea of structure generation in our system can be explained in the case where the structure to be mapped is from a single document. In this case, the pseudo fact is generated by mapping a document to the incomplete document.

The heuristic used in generating new structure is that since the structures as described in two documents are similar in part, it is reasonable to expect that the rest part of their structures should also be similar. Our approach shares some common concern with the Structure Mapping Engine (SME) (Falkenhainer et al., 1989) which works in four stages: local match construction of all pairs of base item and target item, combines the local matches into maximal consistent collections of correspondences, candidate inference construction, and match evaluation. However, our focus is to implement structure mapping theory in the context of intelligent document information retrieval.

The entire process of generating document (which serves as a suggestion) is performed in two phases: find a source analog (which is fact constructed from stored document stems), and then map this source analog to generate a new document. Unlike the retrieval in the regular mode, in the analogy mode what to be retrieved is not precisely specified in the original query; rather, the task is to retrieve a document which is structurally similar to the query.

We use the term object similarity to refer to the similarity between an object in the incomplete document and an object in the source analog. Object similarity is determined by using conceptual memory and attributes similarity. We use the symbol $a \sim b$ to denote object similarity between two objects a and b. We also use the term document similarity between two documents. Object similarity is used in document similarity, but the similarity between relationships in these two documents is of fundamental importance in determining document similarity. This is compatible with Gentner's principle of systematicity of structure mapping theory (Gentner, 1983), as briefly mentioned in Section 1.2. Relationships in the two document stems (will be referred to as relationship pairs) are considered similar if they have exactly the same name or carry same semantic information using auxiliary rules (a topic which will not be addressed in this paper). We use the symbol $d_{1} \simeq d_{2}$ (or $\delta_{1} \simeq \delta_{2}$ ) to denote similarity between two documents $d_{1}$ and $d_{2}$ (or their corresponding document stems $\delta_{1}$ and $\delta_{2}$ ).

Both object similarity and document similarity can be numerically determined and are controlled by a predefined threshold. Since the purpose of this paper is to explain the basic idea of structure mapping, details are omitted here. Some key ideas of a top level algorithm for document structure mapping are summarized below.

1. Convert the incomplete document (whose document stem is $\delta_{0}$ into internal form (in a temporary area). Identify the objects on the query description list. Suppose the query description list is $Q = (q_{1}, q_{2}, \ldots, q_{n})$ .

2. Retrieve (with the assistance of the conceptual memory) a document or a fact which satisfies the following the following two requirements:

1. The document to be retrieved satisfies the query description list $Q' = (q_{r_1}', q_{r_2}', \ldots, q_{r_m}')$ ( $m \leq n$ ), $q_1 \sim q_{r_1}', q_2 \sim q_{r_2}', \ldots, q_m \sim q_{r_m}'$ . This is to construct a list $Q'$ consisting words similar to Q and use $Q'$ instead of Q itself to retrieve relevant documents.

2. The document stem of the retrieved document $\delta'$ satisfies $\delta' \simeq \delta_0$ . This is to retrieve a document which is structurally similar to the incomplete document.

3. Construct structure mapping function $\Phi$ based on similarity between $\delta_0$ and $\delta'$ :

$$
\Phi \colon \delta^ {\prime} \to \delta_ {0},
$$

so that $\delta_0 \subset \Phi(\delta')$ . (Here the notation $\subset$ indicates that $\delta_0$ is contained in $\Phi(\delta')$ .) As stated earlier, $\delta'$ can be considered as consisting of two parts $\delta'_0$ and $\psi'_*$ (each can be considered as a document stem): $\delta' = \delta'_0 \bowtie \psi'_*$ where $\delta'_0$ satisfies $\delta_0 = \Phi(\delta'_0)$ . Here $\bowtie$ denotes the join operation of two document stems (the operations on document stems were defined in Chen, 1994).

4. Perform structure mapping to generate new structure to fill the incomplete document:

$$
\psi_ {*} = \Phi (\psi_ {*}).
$$

Step 2 as shown above is concerned with object similarity and document similarity. The object similarity sim is determined by applying the following rules:

1. If two objects have the same name, then they are treated as the instances of the same object; assign sim = 1.

2. If two objects have the same parent in the hierarchical conceptual memory, assign $sim = W(0 \leq W \leq 1)$ . If in the hierarchical conceptual memory, one object is the parent of the other object, assign $sim = W'(0 \leq W' \leq 1)$ . Both W and $W'$ are some constants indicating certain degrees of similarity; for example, they can be assigned as 0.6 and 0.5, respectively.

3. Compute similarity based on the ratio of attributes shared by both objects. For example, if the object “ship” has attributes “people-mover”, “big” and “in-water”, and the object “car” has attributes “people-mover”, “big” and “in-land”, then two out of three attributes are shared by both objects. Therefore, sim (ship, car) is 2/3 or 0.67. Similar rules have also been developed to deal with two objects which have different number of attributes.

4. If none of the above rules is applicable, then assign $sim = U$ (for unknown). The purpose of assigning U for some pairs is to give a chance to the pairs whose similarity cannot be decided immediately.

In addition, relationships in these two document stems (also called relationship pairs) are considered similar if they have exactly the same name, or if they can be treated as similar by using additional heuristic rules (such as relationships “like” and “love”). Based on the notions of object similarity and relationship similarity, the similarity between two parts of document stems can be determined. In general, the overall similarity between two document stems are the minimum similarity among all the involved object pairs and relationship pairs as stated above.

The search process in the conceptual memory is revised from regular retrieval. Due to space limitation, we will only highlight some key points in this process. The query description list constructed from the incomplete document will be used for searching; for each candidate pair of objects, relationships involving this pair of objects will be compared. Furthermore, compute the overall document similarity after every relationship pair comparison is checked, and the comparison is aborted as soon as the similarity is determined under a certain threshold $\theta$ . Repeat the same process by starting to compare different objects on the boundaries of the two document stems, or choosing some other document stems to compare.

As a concrete example, the experimental system handles the “plane” example in the following manner. First, the boundary can be constructed by determining the first object of the sentence. A query description list is constructed, which con-

sists of “enemy, plane, people”. This list is used to retrieve a document which has similar words with these words. Suppose in the conceptual memory, after a sequential search in the top level of the hierarchy, nothing is found similar to the word “enemy”, two words which are similar to the word “plane”, and two other words which are similar to the word “people”. One word similar to “plane” is the word “train”; they are similar because they share the same parent “transportation tool” in the conceptual memory. The other word found similar to “plane” is the word “obstacle”, due to the shared attribute “invisible”. Suppose the word “plane” is used to index documents with identifiers 14 and 20, while the word “obstacle” is used to index documents with iden-

Incomplete document (query):
enemy dispatch plane. plane is invisible. how people detect plane.

![](/api/attachments/WABGGUY5/fulltext/images/391ed1b857cf39efa2d8f7bd7c6bec3d4367994014749d078c170c73ef716b02.jpg)  
Fig. 4. The construction of structure mapping function.

tifiers 2 and 6. We also assume that the system has determined that there are two words similar to the word “people”: one of them is “bat”, since both the words “people” and “bat” share the same parent “living beings” in the conceptual memory; another word is “student”, because “people” is at the parent node of the word “student” in the conceptual memory. Suppose “bat” is used to index document 2, and “student” is used to index document 15. Since no document is relevant to any word similar to “enemy”, and since document 2 consists of two words similar to “plane” and “people”, document 2 now becomes a candidate of the structure comparison. At this stage, the structure information carried by the incomplete document plays a crucial role. The relationship “detects” associating “plane” and “people” in the incomplete document and the relationship “detects” associating “obstacle” and “bat” in document 2 indicate a perfect match. The candidate analog thus becomes the source analog, and the structure mapping function can be constructed (as to be discussed in the next section). On the other hand, if the structure similarity is not established, another candidate document should be selected; and if no candidate is similar to the incomplete document, then a failure should be reported.

In general, when the structure of the incomplete document and the candidate document is more complicated, there may be more matching items, some of them may only be partially matched. The predetermined threshold $\Theta$ will be used to determine the overall similarity. However, the basic idea of matching remains same.

## 3.2. Construction of structure mapping function

We now further describe the construction of the structure mapping function which is used in our system to perform the needed mapping from the source (base) domain to the target domain. This function is constructed based on the structure similarity between a source analog and the target analog as stated in the incomplete document. We use the notation $\Phi$ to denote the finally constructed mapping function from the source to the target. We also use the notation $\phi$ to denote the mapping from the objects and relationships in the source analog to the objects and relationships in the known part of the incomplete document. The function $\Phi$ is more general than the function $\phi$ in that it involves not only the known part of the incomplete document, but also the newly generated objects and relationships as well. Note that $\phi^{-1}$ is first constructed during the retrieval of a candidate source analog; the inverse of $\phi^{-1}$ , namely, $\phi$ is then extended to $\Phi$ . For example, from the word “people” in the query description list, a similar word “bat” is found; that is, we have established a candidate inverse mapping “ $\phi^{-1}$ (people) = bat”, and consequently we have “ $\phi(\text{bat}) = \text{people}$ ”. Similarly, $\phi^{-1}$ (detects) = detects can be established, so we have “ $\phi(\text{detects}) = \text{detects}$ ”.

![](/api/attachments/WABGGUY5/fulltext/images/daf01ce2d633355a33d4516c0bb204ed05853f801399bf04474b0193927f290e.jpg)  
Fig. 5. Algorithm for pseudo-fact generation.

To avoid unnecessary mathematical detail, instead of presenting the resulting mapping function $\Phi$ in its formal form, here we state the following mapping rules which are derived from the mapping function $\Phi$ :

(1) If an object or a relationship is in the original known part of the incomplete document, the mapping of $\Phi$ should agree with $\phi$ . So we have “ $\Phi(\text{bat}) = \text{people}$ ” and “ $\Phi(\text{detects}) = \text{detects}$ ”.

(2) If x is an object which is in the source analog but not part of the original known part of the incomplete document, generate a new object x-like as the result of mapping. For example, since there was no object in the incomplete document corresponding to the word “sound”, a new object name “sound-like” is generated as the result of mapping the object “sound”. That is, we have “ $\Phi(\text{sound}) = \text{sound-like}$ ”.

![](/api/attachments/WABGGUY5/fulltext/images/ca124f15ddcedc59fa995846a9bcfcd46107abc01879917e51f3d3407d303a5b.jpg)  
Fig. 6. (a) Structure similarity between incomplete document and source analogy, (b) result of structure mapping.

(3) If x is a relationship which is in the source analog but not in the original known part of the incomplete document, map it as it is. For example, both “emits” and “reflects” are mapped into the incomplete document.

The construction of the structure mapping function can be depicted in Fig. 4, while the algorithm for generating pseudo-fact is summarized in Fig. 5.

In summary, the structure mapping function for new text generation in the “plane” example consists the following:

$$
\Phi (\text { detects }) = \phi (\text { detects }) = \text { detect }
$$

$$
\Phi (\text { obstacle }) = \phi (\text { obstacle }) = \text { plane }
$$

$$
\Phi (\text { bat }) = \text { people }
$$

$$
\Phi (\text {   emits   }) = e m i t s
$$

$$
\Phi (\text { reflects }) = \text { reflects }
$$

$$
\Phi (\text { sound }) = \text { sound - like }
$$

The italicized objects and relationships are generalized by mapping. Note that a new relationship name in the target domain is same to the name of the relationship in the source domain from which it is mapped, while a new object name in the target domain will be the original name attached with a postfix “-like”.

![](/api/attachments/WABGGUY5/fulltext/images/4c07a982002e517764a0e3aa85b5db4fbba92ef9e7253455327029841d16df44.jpg)  
Fig. 6 (continued).

The process of mapping from the source analogy in the knowledge base (with positive location numbers) to the temporary area (with negative location numbers) can be depicted in Fig. 6, where each document stem is conceptually bounded by a boundary (which is depicted as a big circle). Usually the knowledge base consists of numerous document stems, while the temporary area consists of only one document stem (the internal form of the incomplete document). Fig. 6a depicts the structure similarity between the incomplete document and the source analog, while Fig. 6b depicts the result of the document structure mapping.

## 3.3. Revised algorithm for source analog constructed from multiple documents

In order to construct the pseudo fact, more than one document may be needed. That is, the source analog is a fact (as defined in our earlier paper, a fact is constructed from several documents) rather than a single document. In the case that a source analog consists of multiple documents, more time complexity is involved. However, the concept of document structure mapping remains same as in the case of single document mapping.

The algorithm summarized in Section 3.1 should be revised when multiple documents are need to form a fact as the source analog. The basic idea described in the previous algorithm can be generalized to handle the case in which no single document is qualified to be a source analog, but a source analog can still be constructed from several documents (in our terminology, this is equivalent to say that the source analog is a fact). In this case, a relevant document stem is only a part of the source analog. Consequently, the task is to find to document $d_{i}, d_{j}$ so that

$$
\phi \left(\delta_ {i} \bowtie \delta_ {j}\right) = \psi ,
$$

where $\phi$ is the structure mapping function, ✗ denotes the join operation defined on document stems, and $\psi$ is the document stem of the pseudo fact. In other words, the task is to retrieve a fact which is similar to the incomplete document provided by the user. The fact can be retrieved in a way similar to what has been described at the end of Section 2.1. After the fact is retrieved, the structure mapping function can be constructed using the rules described in Section 3.2. Furthermore, these considerations can be generalized to handle the case in which more than two documents are involved in forming a fact.

## 4. Implementation using schema-free relational databases

We now give a few remarks on the implementation using schema-free relational databases.

## 4.1. A brief review of schema-free databases

A schema-free (also called loosely-typed) database employs a relational data model but without using any schema (Motro, 1986). In Chen (1994) we summarized an experimental system which uses schema-free relational databases to implement the computational model summarized in Section 2.1. Under this implementation, documents are internally represented by relations consisting of object tuples and relationship tuples. Operations on document stems (such as join operation of two document stems which have some common part) have been defined, and can be realized through operations on schema-free relational databases (for example, join of two document stems can be realized through union of relations defined on the schema-free relational databases).

## 4.2. Generating new tuples of schema-free relations

We now describe, in some detail, how document structure mapping is performed in the schema-free relational databases. As already mentioned earlier, objects and relationships are represented using tuples of schema-free relations. This is also applied to the incomplete document.

After structure mapping, new objects and relationships will be generated. We use a question mark “?” to denote the name of each generated object or relationship. It is referred to as an incomplete object or relationship, and can be further represented as an incomplete object tuple or relationship tuple with its internal representation stored in the temporary area. Each tuple consists of fields indicating the location of the object stored in the knowledge base, the name of the object, the attributes of the object, and the locations of the associated relationships. For instance, the following is an incomplete object:

$$
[ - 4, [? ], [ ], [ - 5 ] ],
$$

which indicates an object stored at temporary location -4 has an unknown name, with no specified attributes (but may be added later), and is associated to a relationship which is stored at temporary location -5. Similarly we can define incomplete relationships. For example, the following is an incomplete relationship:

$$
[ - 7, [? ], [ ], [ - 3, - 6 ] ],
$$

which indicates a relationship is stored at temporary location -7, has an unknown name, and is associated with two objects stored at locations -3 and -6. The question mark as appeared in the incomplete tuples will be replaced by generated object names and relationship names. A text (written in restricted grammar) will then be reconstructed and presented to the user from these tuples.

For convenience of discussion, in the following we will use the table format to represent relations formed from a group of object tuples or relationship tuples. The table corresponding to the incomplete document is shown in Table 2, while the source analogy (namely, the document concerning the bat) is already shown in Table 1. The object tuples from an incomplete document form an object relation. Similarly the relationship tuples from the same incomplete document form a relationship relation. These two relations are shown in Table 2. This table is correspondent to Fig. 6a, and reflects the internal representation of the document on “bat”.

Internal representation of incomplete document in temporary area

<table><tr><td colspan="4">Object list in incomplete document:</td></tr><tr><td>location</td><td>object name</td><td>attribute</td><td>relationship location</td></tr><tr><td>-1</td><td>enemies</td><td></td><td>-2</td></tr><tr><td>-3</td><td>plane</td><td>invisible</td><td>-2</td></tr><tr><td>-101</td><td>people</td><td></td><td>-102</td></tr><tr><td colspan="4">Relationship list in incomplete document:</td></tr><tr><td>location</td><td>relationship name</td><td>attribute</td><td>object location</td></tr><tr><td>-2</td><td>dispatch</td><td></td><td>-1, -3</td></tr><tr><td>-102</td><td>detect</td><td></td><td>-101, -3</td></tr></table>

The mapping from the document to this internal representation can be briefly summarized as follows. A blank row in Table 2 is used to separate the known part and the “how” question. Note that in order to reserve places for the objects and relationships which may be generated later, the locations of the objects and relationships in the incomplete document in the “how” part is temporary assigned a separate location number (-101 is used as the starting number in the implementation), and will be replaced by an actual number later. For instance, the object “people” and the relationship “detect” in the “how” part have original location numbers -101 and -102, respectively (as shown in Table 2), and these two numbers are replaced later by -4 and -8, respectively (as shown in Table 4). Source analog forms another relation, consisting of tuples as shown in Table 2. Table 3 shows the tuple generation after structure mapping, with newly generated incomplete objects and incomplete relationships. Finally, Table 4 shows the final result after relationships and objects are mapped according to the mapping function defined before.

Tuple generation after structure mapping (with incomplete objects and incomplete relationships)

<table><tr><td colspan="4">Object list in pseudo-fact:</td></tr><tr><td>location</td><td>object name</td><td>attribute</td><td>relationship location</td></tr><tr><td>-1</td><td>enemy</td><td></td><td>-2</td></tr><tr><td>-3</td><td>plane</td><td>invisible</td><td>-2, -7, -8</td></tr><tr><td>-6</td><td>?</td><td>inaudible</td><td>-5, -7</td></tr><tr><td>-4</td><td>people</td><td></td><td>-5, -8</td></tr><tr><td colspan="4">Relationship list in pseudo-fact:</td></tr><tr><td>location</td><td>relationship name</td><td>attribute</td><td>object location</td></tr><tr><td>-2</td><td>dispatch</td><td></td><td>-1, -3</td></tr><tr><td>-5</td><td>?</td><td></td><td>-4, -6</td></tr><tr><td>-7</td><td>?</td><td></td><td>-3, -6</td></tr><tr><td>-8</td><td>detect</td><td></td><td>-4, -3</td></tr></table>

Table 4  
Final result of pseudo-fact

<table><tr><td colspan="4">Object list in pseudo-fact:</td></tr><tr><td>location</td><td>object name</td><td>attribute</td><td>relationship location</td></tr><tr><td>-1</td><td>enemy</td><td></td><td>-2</td></tr><tr><td>-3</td><td>plane</td><td>invisible</td><td>-2, -7, -8</td></tr><tr><td>-6</td><td>sound - like</td><td>inaudible</td><td>-5, -7</td></tr><tr><td>-4</td><td>people</td><td></td><td>-5, -8</td></tr><tr><td colspan="4">Relationship list in pseudo-fact:</td></tr><tr><td>location</td><td>relationship name</td><td>attribute</td><td>object location</td></tr><tr><td>-2</td><td>dispatch</td><td></td><td>-1, -3</td></tr><tr><td>-5</td><td>emits</td><td></td><td>-4, -6</td></tr><tr><td>-7</td><td>reflects</td><td></td><td>-3, -6</td></tr><tr><td>-8</td><td>detect</td><td></td><td>-4, -3</td></tr></table>

Table 2 is the correspondence of Fig. 6a, both indicate the original incomplete document submitted as a user query; while Table 4 is the correspondence of Fig. 6b, both indicate the final pseudo-fact constructed. The generated part is indicated using italics. Although the known part of the incomplete document in this example consists of only three objects, in general, the structure may be much more complicated.

## 5. Conclusions

Rich literature exists for computational approaches to analogical reasoning and analogical problem solving. In this paper, we have examined the issue of generating suggestions through document structure mapping. The generated suggestions can be used by the decision maker directly, or to be forwarded to some other computer software for further processing. Either way, the generated suggestions may contribute to intelligent decision support.

Although pseudo-facts take the format of documents or facts, it is important to keep in mind that pseudo-facts generated through analogical reasoning are not necessarily true knowledge. Thus, we should be cautious when we are trying to use “information” retrieved in this way. On the other hand, suggestions provided by pseudo-facts may lead to interesting advices or even “discoveries”.

Due to the complexity involved, the implemented system has only demonstrated the most important idea behind our approach using simple documents. In order to deal with real documents, a powerful special purpose parser should be constructed so that structure mapping should be authentic mapping of semantics. An ideal parser, assisted by a knowledge-rich conceptual memory, should be constructed in such a way so that it supports easy identification of the boundaries of relevant similar document stems.

Another potential problem is that the generation of suggestions could be either too easy or too hard. If it is too hard to generate suggestions, then the system will be of little use. On the other hand, if the threshold set up to determine the similarity is too low, then it may be an overabundance of generated suggestions, some of them may be ridiculous. The user is responsible to determine whether the automatically generated suggestion is acceptable or not. As a future direction of work, a better way of controlling the quality of the suggestions is needed, including the possible incorporation of various techniques in dealing with uncertainty reasoning.

## Acknowledgements

The author thanks an anonymous reviewer for his/her critical comments and useful suggestions on earlier versions of this manuscript.

## References

M.H. Burnstein, Combining Analogies in Mental Models, in: D.H. Helman (ed.), Analogical Reasoning (Kluwer, Dordrecht, 1988).

J.G. Carbonell and S. Minton, Metaphor and Commonsense Reasoning, in: J.R. Hobbs and R.C. Moore (eds.), Formal Theories of the Commonsense World (Ablex, 1983).

Z. Chen, Let Documents Talk to Each Other, J. Documentation 49, No. 1 (1993) 44–54.

Z. Chen, Enhancing Database Management to Knowledge Base Management, Information Processing and Management 30, No. 3 (1994) 419–435.

W.G. Cole and J.G. Stewart, Metaphor Graphics to Support Integrated Decision Making with Respiratory Data, Int. J. Clinical Monitoring and Computing 10, No. 2 (May 1993) 91–100.

B. Falkenhainer, K. Forbus and D. Gentner, The Structure-Mapping Engine: Algorithm and Examples, Artificial Intelligence 41, No. 1 (1989) 1–63.

D. Gentner, Structure Mapping: A Theoretical Framework for Analogy, Cognitive Science 7 (1983) 155–170.

R.P. Hall, Computational Approaches to Analogical Reasoning: A Comparative Analysis, Artificial Intelligence 39 (1989) 29–120.

C.W. Holsapple and A.B. Whinston, Knowledge-based Organizations, Information Society 5 (1987) 77–90.

D. Leishman, An Annotated Bibliography of Works on Analogy, Int. J. of Intelligent Systems 5 (1990) 43–81.

T.-P. Liang, Modeling by Analogy: A Case-Based Approach to Linear Program Formulation, Proc. 24th Annual Hawaii International Conference on Systems Sciences, III: Decision Support and Knowledge Based Systems Track (January 1991) pp. 276–283.

T.-P. Liang, Modeling by Analogy and Case-Based Learning in Model Management Systems, Decision Support Systems 10 (1993) 137–160.

G. Marchant, J. Robinson and U. Anderson, The Use of Analogy in Legal Argument: Problem Similarity, Precedent, and Expertise, Organizational Behavior and Human Decision Processes 55, No. 1 (June 1993) 95–119.

R.K. Michalski et al. (eds.), Machine Learning: An Artificial Intelligence Approach, Vol. I and Vol. II (Morgan Kaufmann, San Mateo, CA, 1983).

A. Motro, Assuring Retrievability from Unstructured Databases by Contexts, Proc. Int. Conf. on Data Engineering (Chicago, 1986) 426–433.

M. Shaw, Machine Learning Methods for Intelligent Decision Support: An Introduction, Decision Support Systems 10 (1993) 79–83.

S. Vranes, M. Lucin and M. Stanojevic, Blackboard Metaphor in Practical Decision Making, Eur. J. Operations Research 61, Nos. 1/2 (1992) 86–97.

L.F. Young, The Metaphor Machine: A Database Method for Creativity Support, Decision Support Systems 3 (1987) 309–317.

L.F. Young, Decision Support and Idea Processing Systems (Wm. C. Brown, Debuque, 1988).

![](/api/attachments/WABGGUY5/fulltext/images/e71078d6fcea376c65fedd36ec316895fd86b9a3ca4567218f73b865572eb5cf.jpg)  
Zhengxin Chen holds MS and PhD degrees from Louisiana State University. He is now associate professor of Department of Computer Science, University of Nebraska at Omaha. He is interested in various issues related to building intelligent information systems, and has publications in several refereed journals.
