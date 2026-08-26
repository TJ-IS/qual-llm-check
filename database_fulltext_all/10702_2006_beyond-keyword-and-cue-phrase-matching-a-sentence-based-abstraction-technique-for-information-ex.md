---
otero_id: 10702
otero_key: "J5EBUWM9"
title: "Beyond keyword and cue-phrase matching: A sentence-based abstraction technique for information extraction"
authors: "Samuel W.K. Chan"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.11.017"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Beyond keyword and cue-phrase matching: A sentence-based abstraction technique for information extraction

Samuel W.K. Chan

Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong, Hong Kong

Received 1 June 2003; accepted 1 November 2004

Available online 28 June 2005

## Abstract

With the explosion in the quantity of on-line text and multimedia information in recent years, there has been a renewed interest in the automated extraction of knowledge and information in various disciplines. In this paper, we provide a novel quantitative model for the creation of a summary by extracting a set of sentences that represent the most salient content of a text. The model is based on a shallow linguistic extraction technique. What distinguishes it from previous research is that it does not work on the detection of specific keywords or cue-phrases to evaluate the relevance of the sentence concerned. Instead, the attention is focused on the identification of the main factors in the textual continuity. Simulation experiments suggest that this technique is useful because it moves away from a purely keyword-based method of textual information extraction and its associated limitations. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Information extraction; Automatic summary; Shallow text processing; Connectionist model

## 1. Introduction

The explosive growth of the World Wide Web has vastly increased the amount and availability of information. This, in turn, has created an overload of electronic text, which has made it even more difficult to access and identify the information that is required. The abundance of on-line electronic text has opened up opportunities for systems that can understand natural language and automatically extract and organize relevant knowledge in a usable format. The application of text-based abstraction techniques in various disciplines has recently become more widespread. For example, the COBALT and FACILE projects apply text information extraction techniques to the financial domain [7,50]. They extract details of joint business ventures from stock-related newswires. The TREE project, which was proposed by Somers et al., is a foreign language information extraction system for application in the employment domain [54]. It aims to extract a database of employment opportunities from a pool of job advertisements. Weiss et al. propose a lightweight document-matching system for business applications, which is a help desk information retrieval mechanism that is suitable for a wide range of users [61]. The prototype that has been developed, which uses minimal data structures and lightweight algorithms to match new documents with those stored in a database, rapidly focuses on the information that is required. Lam and Ho describe a financial information digest system that can summarize on-line financial news automatically [35]. Their system is able to integrate information from different articles by conducting automatic content-based classification and information item extraction. The SAL-OMON system automatically summarizes criminal court cases to make accessing a large number of existing court cases easier [43]. This system extracts the relevant text units from court decisions to form a case summary. This type of case profile aids the rapid determination of the relevance of previous court decisions to the current case. The Meeting Browser that was developed at Carnegie Mellon University allows users to review and browse the content of meetings based on automatic textual summarization [59]. Salient turns in the meeting conversation are provided as summaries in the Browser. The News on Demand system allows the reconstruction of multimedia news broadcasts [25].

Although the demand for a sophisticated text abstraction technique is pervasive, it is commonly accepted that the latest technology that has developed from current linguistic analysis, which aims to completely simulate the human intellectual understanding, is far from satisfactory. This has given rise to considerable debate about the shallow versus deep approaches to information extraction. Basically, the process that information extraction systems follow can be roughly divided into two main stages. At the syntactic stage, information extraction involves tokenization, parts-of-speech tagging, syntactic parsing, phrasal pattern-matching, and the transformation of each sentence into an intermediate structure using various templates. The early approaches that came out of the Message Understanding Conferences (MUC) have demonstrated their capabilities at this stage of information extraction [18]. However, at the discourse stage, domain knowledge is used to integrate all of the intermediate templates that are generated to produce a large-scale knowledge structure that serves to provide coherent information for extraction. Thus, an extraction system can be shallow or deep, depending on which of these two different stages is used as the basis for the system. At one extreme, some systems may produce a simple knowledge structure that is solely a collection of unordered sample features, and at the other extreme, there are systems that use abductive theorem provers to turn every sentence in the text to a designated logical model [26]. Even though the debate on how shallow a system can be has not been settled, recent research in information extraction has increasingly turned to text analysis, due to the fact that text structures are manifestly necessary in bonding the intermediate templates [40,43].

Text structure has been examined in a variety of disciplines, including information science [16,56], artificial intelligence [28–30,42,44,62], and text retrieval [20,23,47,49]. Text usually has a rich structure, in which sentences are grouped and related to one another in a variety of ways. A text is usually taken to be a group of connected and meaningful sentences, rather than merely a sequence of random text segments. The analysis of text usually involves a process of making connections between the sentences through inter-sentential knowledge. Textual continuity is a key component in all inter-sentential knowledge, because it differentiates a text from a random sequence of sentences. It also explains how coherent text structures can be built [38]. This continuity provides the basic rationale for the creation of text, and represents the connections between sentences.

In this article, a sentence-based abstraction technique for information extraction is presented. It is based on a connectionist model that incorporates affective and rational discourse variables in textual continuity, including cohesion and coherence. A discourse network is explored for the representation of discourse that goes beyond sentence boundaries and treats a text as a whole unit that is composed of interrelated parts, rather than a sequence of isolated sentences. We show how this discourse network can be used to derive a meaningful discourse structure from which the important parts of a text can be identified. The interconnected links in such a network reflect the attributes of textual continuity, and provide a means for ascertaining the saliency of each sentence. Although the connectionist approach to shallow text processing is still in its infancy, we provide preliminary simulations and experiments to demonstrate the potential merit of this approach. The rest of this article is organized as follows. In Section II, we describe our discourse network for the representation of text, and the overview of the system architecture is also explained. We demonstrate how the links in the discourse network summarize the primary attributes of textual continuity, and this leads to Sections III and IV, which demonstrate how these linguistic attributes can be formulated and assigned to the network. Section V explains a sentence-based abstraction technique, which is a strategy that captures the dynamic influences of context and preference using an associative memory model. Section VI describes a prototype system that studies the behavior of the system in different texts, which is followed by a discussion and a conclusion.

## 2. Text representation in a discourse network

In the consideration of how to represent a discourse, one of the fundamental notions that has been suggested is that of discourse segments, which are the smallest units of interaction [33]. A discourse is a sequence of segments $s _ { 1 } , \ s _ { 2 } , \ . . . , \ s _ { n } ,$ such that the semantic interpretation of segments $s _ { i } ( \mathrm { f o r } 2 \leq i \leq n )$ is dependent on the interpretation of the sequences $s _ { 1 } ,$ $\dots , s _ { i - 1 }$ . An adequate representation of a discourse requires some knowledge of the context in which the discourse appears. In our research, we have chosen to model textual continuity as a means of binding segments together, by using a discourse network D. The network represents the inter-sentential relationships that exist among the segments, as is shown in Fig. 1. The discourse segments function as terminal nodes in a discourse network that cover the entire discourse. To demonstrate the inter-relationships within a discourse, we begin by defining a discourse network $D$ as a set of discourse segments, which stand in functional relation to each other and are represented as a graph that is characterized by a quintuple

$$
D = \langle V, C, A, E, W \rangle ,
$$

where

! $V$ is a finite set of discourse segments that comprises the text.

! $C$ is a finite set of content words in each segment.

<sup>!</sup> A is a set of arcs that represents the textual continuity among the discourse segments.

! $E$ is a set of the weights of the arcs, and lies between 1 and 1.

<sup>!</sup> W is a function W: $A { \longrightarrow } E$ that assigns lateral weights to the arcs.

The application of the discourse network D to model text continuity is quite straightforward. We use a set of discourse segments that comprise the discourse in the set V. In the discourse network $D ,$ the lateral weights W between the arcs among the discourse segments are defined by the constraints of textual continuity. Let $\nu _ { i } , ~ \nu _ { j } \in V$ be two discourse segments in the discourse network $D ,$ each representing a different discourse segment. If both of these segments are interrelated, then the connection between them, i.e., $W _ { i j } ,$ is assigned a large positive weight. As a result, high activity in $\nu _ { i }$ would produce high activity in $\nu _ { j } ,$ and vice versa. Modeling textual continuity, from a microscopic point of view, is regarded as a process of assigning lateral weights to the discourse segments. The processing operation that we put forward is not a direct translation of the encountered discourse to the structure, but rather a procedural model that establishes a network of relationships between the segments in the discourse.

To reflect the way in which readers interpret sentences as part of a larger discourse, we have developed a means whereby textual continuity can be formally modeled. Quantitative coefficients are devised to assess the degree of continuity of a discourse by considering two distinct fundamental factors, cohesion and coherence. Segments are cohesive to the extent that the interpretation of some expressions depends on the analysis of the preceding expressions in the discourse. Cohesion, which is the connection between the sentences in the nearby segments, is defined as the formal linguistic realization of semantic and pragmatic relations between clauses and sentences in a text [48]. Several cohesive factors have been identified as contributing to a cohesive discourse, namely lexical cohesion [24], referential cohesion [33], and verb cohesion [22]. Common to all these studies is the notion of repetition, which serves to show the relatedness of sentences in much the same way that a bibliographical reference shows the relatedness of academic papers. In fact, the perception of cohesion is the result of a complex problem-solving process in which the reader infers relations among the

<table><tr><td>Sentences in the story of Judy&#x27;s Birthday</td><td>Discourse Segments</td></tr><tr><td>Judy is going to have a birthday party.</td><td>1. Has(J, BP)</td></tr><tr><td>Since she is ten years old,</td><td>2. Is(She, 10 years_old)</td></tr><tr><td rowspan="2">she wants a hammer and a saw for presents.</td><td>3. Want(She, H &amp; S)</td></tr><tr><td>4. Present(H &amp; S)</td></tr><tr><td rowspan="2">in order to make a coat rack and fix her doll&#x27;s house.</td><td>5. Want(She, Make(Coat Rack))</td></tr><tr><td>6. Want(She, Fix(Doll&#x27;s House))</td></tr><tr><td>She asked her father to get them for her.</td><td>7. Ask(She, Father, Get(them))</td></tr><tr><td>However, her father did not want to get them for her.</td><td>8. Want(Father, Not_have(She, them))</td></tr><tr><td>He did not think girls should play with a hammer and a saw.</td><td>9. Think(Father, Not_play(Girl, H &amp; S))</td></tr><tr><td>But he wanted to get her something.</td><td>10. Want(He, Get(She,Something))</td></tr><tr><td>So he bought her a beautiful new dress.</td><td>11. Buy(He, She, Beautiful(Dress))</td></tr><tr><td>Judy liked the dress</td><td>12. Like(Judy, Dress)</td></tr><tr><td>but she still wanted the hammer and saw.</td><td>13. Want(She, H &amp; S)</td></tr><tr><td>Later she told her grandmother about her wish.</td><td>14. Tell(She, GM, Her wish)</td></tr><tr><td>In fact, her grandmother knew that</td><td>15. Know(GM, Desire(She, H &amp; S))</td></tr><tr><td>Judy really wanted a hammer and a saw.</td><td></td></tr><tr><td rowspan="3">She decide to get them for her because when Judy grows up and becomes a woman.</td><td>16. Decide(She, Get(She, She, Them))</td></tr><tr><td>17. Think(GM, Is(J, Adult))</td></tr><tr><td>18. Think(GM, Is(J, Woman))</td></tr><tr><td rowspan="2">She will have to fix things when they break.</td><td>19. Think(GM, Fix(J, Broken(Things)))</td></tr><tr><td>20. Broken(Things)</td></tr><tr><td rowspan="2">Then her grandmother went out and bought the tools for Judy.</td><td>21. Go(GM, Out)</td></tr><tr><td>22. Buy(GM, Judy, Tools)</td></tr><tr><td>She gave them to Judy.</td><td>23. Give(She, Judy, Them)</td></tr><tr><td>Judy was very happy.</td><td>24. Happy(Judy)</td></tr><tr><td>Now she could build things with her h. &amp; s.</td><td>25. Think(She,Build(She,thing,With(H&amp;S)))</td></tr></table>

![](/api/attachments/J5EBUWM9/fulltext/images/e5a42c8e1c5b4796414abb08ff4fe95c082d8d106bf351ba7afeeecf98042bf7.jpg)  
Fig. 1. Modified version of the Judy’s Birthday text and its corresponding discourse segments. A fragment discourse network D that represents the text is displayed in the lower part. The rectangular boxes represent the discourse segments, and the ellipses are the corresponding context nodes.

lexical items and events that are described in the text [58]. These repetitions also serve as vital links to make the text cohesive. It has been observed that not all sequences of cohesive sentences necessarily make up a text. In a discourse, sentences are perceived as working together to build up a unified whole through coherence. Coherence is the connection that is brought about by world knowledge [1]. It is also the connection between successive segments that are not apparent in the text elements. Although coherence is the umbrella term that is used by most linguists, it is commonly divided into two further categories of local coherence, which refers to short sequences of clauses, and global coherence, which is measured in terms of overarching themes. Causal, spatial, and temporal continuities are the main constituents in the understanding of textual coherence [19].

The schematic diagram of the system is shown in Fig. 2. First, each sentence in the text is analyzed in a sentence analyzer. Texts with different formats are first input and preprocessed in a preliminary processing which intends to extract the statistical distribution of each token. The statistics, such as n-gram and entropy measures, signify a surface and coarse classification of the text. At the same time, the sentences are then segmented, and are subject to parts-of-speech tagging. As most of the meaning in a sentence is expressed in its content words, all of the function words in the segments are removed [10,13]. While the syntactic constraints, though necessary, have little extension in semantic dimensions of the domain of analysis, it is well known that evaluating semantic similarity is crucial in solving many natural language processing tasks. An essential component of the lexical entry of a token is its definition of meaning. In our lexical cohesion analysis, a variety of semantic relationships will be identified based on a type hierarchy. The type hierarchy contains both verbs and noun classes that correspond to world and domain-specific knowledge. The tokens in the type hierarchy are related to each other through (i) equivalence relationship (e.g., synonyms); (ii) hierarchical relationship (e.g., super/sub-ordinate terms); (iii) associative/symmetric relationship (e.g., opposites). The objective of the lexical cohesion analysis is to identify this shallow but pervasive semantic knowledge in the sentences of the text, by making use of the hierarchy and the text information captured from the statistic distribution. The analysis generates a hypothetical set of immediate links on which the connections might be focused by virtue of each adjacent segment.

While we focus on continuous text, rather than on concordance lines, it is ascertained that readers attempt to tie each event that is encountered in the text to some previous text or relevant background knowledge. The logical relations between segments based on linguistic clues in the text will be analyzed. Our coherence analysis will rely on the rhetorical relations which model the intentions that lie behind the utterance of two coherent segments [39]. To model the complete textual continuity in the discourse network D, all the possible links that generate from the lexical cohesion as well as textual coherence are combined as shown in Fig. 3. For expository reasons, only 4 of the 25 segments that are shown in Fig. 1 are involved. The pattern of connection weights between any two nodes is entirely determined by lexical cohesion and textual coherence analysis.

The main idea behind capturing the nonlinearity of the discourse structure during the sentence-based abstraction can be interpreted as the iterative change of the activation level of the discourse segments based on the textual continuity, which is encoded in the connection weights. The activation of each segment, as a node in the network, is modified until the competing coalitions of the units drive the network to a stable equilibrium. The network also reflects the significance of each discourse segment in the discourse within that particular context. It is based on the fact that the contextual significance of the sentence as a whole is determined by the contextual significance of the words or phrases of which it is composed. A detailed discussion on how the activation is spread and the discourse structure formed will be further explained in Section V.

![](/api/attachments/J5EBUWM9/fulltext/images/8a2b0bac5d609dc1d1823f01f34c4bc259d4139043084f457ac87216280d54cf.jpg)  
Fig. 2. System schematic diagram.

![](/api/attachments/J5EBUWM9/fulltext/images/744239c2ecd034c4a66034658803d3e1e746097cccdbe47567b79b5e979b1590.jpg)  
Fig. 3. Connection weight patterns among the discourse segments. The links that are built from the lexical cohesion and textual coherence analysis are represented by the dotted and solid lines, respectively. While the first component of the order pair represents the ID of the discourse segment, the second component shows the activation of the segment at the iteration. The activation of each discourse segment will be propagated by the links in each processing cycle until the asymptotic value is reached during the sentencebased abstraction.

## 3. Modeling lexical relations in text

An aspect of world knowledge that is essential to the construction of a discourse network is the ability to identify when two words in a discourse segment are related. With the exception of conjunctions in the study of cohesion, the commonly shared cohesive ties entail repetition, and this is also true of the category that Halliday and Hasan loosely label lexical cohesion [24]. Under this heading, they detail a variety of semantic relationships that can exist between lexical items, and cluster them into two broad subclasses: reiteration and collocation. Reiteration covers the range of ways in which one lexical item may be understood to conjure up the sense of a preceding item. Several major types of relationships give a text cohesiveness by relating lexical items to one another: (i) identical lexical items (man and man), (ii) synonyms (man and male), (iii) near-synonyms (guy and man), and (iv) superordinates or subordinates (human and man). Collocation is defined as an arbitrary and recurrent word combination [6]. It represents the relationships between lexical items that appear with greater than random probability in a textual context. It is seen as a relationship of associative meaning between regularly co-occurring lexical items in a text.

Cohesion parsing, as shown in Table 1, is achieved within a constraint net, which is formulated as a constraint satisfaction problem over a set of finite elements [60]. The elements in the net represent the discourse segments with their dominant and context nodes. The distinctive property of this cohesion parsing is the involvement of buffers, which are designed to carry each preceding discourse segment that is analyzed over into the current processing cycle, in the hope that these segments will serve as common bridging elements between the segments, as is shown in Fig. 4. Based on the following two principles, the incohesive segments are identified in cohesion parsing.

```txt
Table 1
Algorithm of cohesion parsing

Cohesion Parsing
FOR each discourse segment l DO
BEGIN
    allocate a buffer for each preceding analyzed discourse
    segment in the constant net
    FOR each lexical item i in l DO
    BEGIN
    allocate a node for the item i in the constraint net
    allocate some associated nodes for item i from
    the lexicon
END
assign the initial activation values, U(0) for all the nodes
and the buffers
derive a matrix K, which contains connection strengths
between the nodes
WHILE tolerance ≥ threshold DO
BEGIN
    U(t+1) ← T[U(t) K], where T is a vector normalization
operation
    calculate the new tolerance by comparing U(t+1) with U(t)
END
compute the change of activation in each respective buffer
END
```

Principle of reiteration analysis. A positive link between two linguistic items should be built not only when the items are identical, but also when they are semantically dependent. That is, if the surface components of some items depend upon other items in the buffers, such as synonyms, pronouns, lexical relationships, superordinates or subordinates, it is essential to make use of them to resolve lexical cohesion.

Principle of collocation analysis. The basis for computing a set of collocation links is their respective degrees of relevancy. Greater relevancy  that is, links that introduce more semantic overlapping with the buffers  is preferred, as the semantic overlapping reinforces the interpretation of both elements. That is, if there is a lexical item in the analyzing discourse segment that succeeds in establishing a semantic relation with an element that is already present in the buffers, then it is favored over an item that does not.

These principles give a very simple procedural account of the cohesion resolution and the relation of collocation. The processing strategy that is used to apply these principles is as follows. Each linguistic concept in the discourse segment that is being analyzed is processed separately and effectively in parallel. Links are built across the concepts in the buffers. As the concepts in each of the preceding buffers have been unified, they act as potential cohesive and collocative units. Fig. 4 shows the initial constraint net when the sixth discourse segment (see Fig. 1) is under analysis. Under these principles, the following resolution rules that model the nature of cohesion and collocation can be implemented:

a) Lexical Relationships: items have positive links if they have high similarity measures or superordinate or subordinate relations, for example, make<sup>X</sup> fix, hammer<sup>X</sup> tool.

b) If the lexical items are identical, they will have strong positive links.

c) Pronoun: links will be set to be positive if the items are grammatically dependent, for example, the lexical items Judy and She in Fig. 4.

![](/api/attachments/J5EBUWM9/fulltext/images/9c47fb9a9607696fc3c8f33994431cdf5e1bc76d4a1ae0459bba36cf9a4514fe.jpg)  
Fig. 4. A constraint network with the corresponding discourse segments that act as a buffer when the sixth discourse segment is under analysis by cohesion parsing. The complete set of discourse segments is shown in Fig. 1.

d) Collocation: links between items may be deduced from co-occurrences. For example, the collocations of birthday, 10 years old, and present may give positive links between the three lexical items.

e) A penalty is incurred for each link that arises when items with alternative meanings of a polysemy are constructed.

f) Penalties are incurred by discourse segments that are a greater distance from the segment being analyzed.

g) Other connections may be set to small negatives.

These tie-breaking weak heuristic rules generate loose connections between the current segment and all of the preceding segments. This rough, piecemeal, and approximate representation of the discourse segment is subjected to cohesion parsing [14]. The reason for the parsing is to reduce the dimensionality of the net and to analyze the influence of each discourse segment buffer with respect to the current segment, and, more importantly, to identify the incohesive buffers and remove them from the context.

This parsing is achieved on the basis of the strength of the associations between concepts in the buffers and the current segment. The parsing depends on reactivating the preceding analyzed discourse segments. The lexical items, both in the discourse segment and the buffers, strengthen or inhibit each other until a stable state is reached. Initially, U(0) represents the initial activation values of all of the lexical items both in the buffers and the current analyzed segment. For each of the vectors U(t), the vector U(t + 1) is calculated, which represents the updated activity. This procedure is applied repeatedly, and is an analogy of the spreading activation process through a vector– matrix multiplication [12,13,34]. Continued spreading by repeated vector multiplication leads to equilibration, and is a kind of parallel constraint satisfaction process. The final activation vector shows that strongly related items strengthen each other, whereas irrelevant lexical items that are irrelevant to the current segment have near zero activation values. The activation value of each discourse segment is calculated from the sum of the final asymptotic activation values of its respective context nodes. Clearly, the activation of a discourse segment relies on the number of lexical items that are activated and pursued in the process of cohesion parsing. The activation of the buffers, with little reiteration and collocation, will readily decay to zero. However, the highly cohesive discourse segments have steady activation values throughout the parsing, and as a result, the activation change in each buffer indicates the degree of cohesion of each previous discourse segment with the current segment. Let $\mathrm { L C } = \left( \mathrm { L C } \right) _ { i j }$ be a square matrix that represents the weights that are defined only by the effect of lexical cohesion and the combined effect of the reiteration and collocation.

$$
L C _ {i j} = \exp \big (- \varepsilon | \mu_ {i j} | \big),
$$

where

$$
\mu_ {i j} = \left(\frac {\text { change   of   activation   of   buffer } i \text { in   respect   to   segment } j}{\text { activation   of   buffer } i}\right).\tag{1}
$$

This exponential function defines the distance measure between two discourse segments in terms of lexical cohesion, and regards the collocation links as another form of cohesion. It is devised to transform the degree of lexical cohesion $\mu _ { i j }$ of the discourse segment i with respect to j into a connection strength within the desired range of 0.00 to 1.00. An exponential strength is chosen, according to the minimal information distribution, which is a maximumlikelihood function that is described by Smolensky [53]. The constant e, which is a positive parameter, is estimated based on the average activation change in the buffers. The parameter is set to penalize all of the links with a large activation change, and to give strong preference to lexical cohesion by the creation of stronger connection strengths for the highly cohesive segments.

## 4. Modeling coherence relations in text

Although cohesion and collocation reveal some of the surface and lexical relations between discourse segments, and seem to be the main ingredients for constructing the interpretations and representations of discourses, they are certainly not necessary or sufficient for the understanding of a discourse. A discourse plainly has to be coherent as well as cohesive, in that the concepts and relationships that are expressed should be relevant to each other, thus enabling readers to make plausible inferences about the underlying meaning. For example, the following excerpt, <sup>b</sup>. . .a week has seven days. Every day I feed my cat. It has four legs. It is on the mat, which has three letters. . .<sup>Q</sup> is highly cohesive but is nonetheless incoherent. The analysis of coherence is therefore indispensable in understanding a discourse. Although causality, temporality, and spatiality are the intertwining links in global coherence when behavioral episodes are unfolded in a discourse [63], we limit our scope in this article to the discussion of causal coherence. It is ascertained that readers attempt to tie each event or fact that is encountered in a text to some previous text or relevant background knowledge [17]. Even with this restriction, the concept of causal coherence seems too unrealistic to manipulate into a simple, explicit, and algorithmic definition. Capturing causal coherence requires deep semantic processing with a broad knowledge, and the strategies for generating such connectivity are highly domain dependent [2]. The complexity of knowledge that is involved in causal coherence, and the multifaceted nature of the process that underlies it, strongly point toward the alternative method of coherence analysis that is offered by the surface structure of a discourse.

Rhetorical Structure Theory (RST) determines the logical relations between segments based on linguistic clues in a discourse, and explicitly models the intentions that lie behind the utterance of two coherent segments [39]. In RST, coherence is established by semantic and pragmatic links, such as connective expressions, that exist between two or more segments, and hence allows the identification of argumentative chunks of discourse. Our textual coherence analysis using RST determines the organization of a discourse by mapping the rhetorical and causal relations between the segments onto coherence weights in the discourse network. The segments in the discourse are causally linked so that one idea builds on another. Causal continuities have been found to be particularly important, and are analyzed in any understanding process. Our textual continuity is based on the concept of rhetorical connectivity, which is defined by the following principle.

Principle of rhetorical connectivity. Each of the subsequent discourse segments is interpreted in terms of whether it instantiates some expectation of the preceding discourse segments in the buffers. If there is a discourse segment being analyzed that succeeds in establishing rhetorical connections with the preceding segments, then it is favored over a segment that does not.

This principle takes into account the overall argumentational organization of the text, and derives the important rhetorical relations from the surface realization. Some of the rhetorical relations and the possible surface realization that signifies the relations are shown in Table 2.

The rhetorical structure under the above principle is represented by two layers: intra-sentence and intersentence structures. Based on the minimalist hypothesis that only intra-sentence coherence is normally established during comprehension [41], our intra-sentence structure demonstrates the coherence between the adjacent segments within the sentence. The rank, as is shown in the right-hand column of Table 2, is assigned as the weight between the segments if they all belong to the same intra-sentence chunk. Some heuristic rules are used to represent the local preferences for consecutive rhetorical relations between segments. For example, consider the

P ; however; Q ; and R:

where P, Q, and R are the discourse segments in a sentence.

The rhetorical structure for the sentence above can either be Conjunction(Negative( P, Q), R) or Negative( P,Conjunction ( Q, R)). To resolve this ambiguity, the following heuristic rule is adopted in the assignment of the weight between the segments of a sentence.

Table 2  
Rhetorical relations and their corresponding surface realizations

<table><tr><td>Rhetorical relations</td><td>Surface realization</td><td>Rank (ξ)</td></tr><tr><td>Explanation</td><td>because, since, in order to</td><td>3</td></tr><tr><td>Negative</td><td>however, but, although, nevertheless, nonetheless</td><td>3</td></tr><tr><td>Sequence</td><td>first, second, third, next, later</td><td>3</td></tr><tr><td>Contrast</td><td>on the other hand</td><td>2</td></tr><tr><td>Amplifying</td><td>moreover, that is to say, in particular, in fact</td><td>2</td></tr><tr><td>Conclusion</td><td>hence, accordingly, in conclusion, consequently</td><td>2</td></tr><tr><td>Conjunction</td><td>thus, and, as well, at the same time</td><td>1</td></tr><tr><td>Extending</td><td>further, in addition, this is, so</td><td>1</td></tr><tr><td>Exemplify</td><td>for example</td><td>0</td></tr></table>

## Heuristic Rule

For the intra-sentence rhetorical relations, the adjacent segments that have a higher rank of rhetorical relation will be favored over others.

As the rhetorical relation of the connective however has a higher rank than the connective and, P and Q are considered to be locally close, and the structure Conjunction(Negative( P, Q), R) is more preferable than Negative( P,Conjunction ( Q, R)). In this preliminary quantitative study, the assignment of weights does not need to be very precise or sophisticated; it just has to be powerful enough that the right connections are likely to appear among those that are generated, even though irrelevant or even outright inappropriate connections will also be deduced. However, as the text might exhibit a rhetorical expression between distant segments, the inter-sentence structure, which is different from the intra-sentence structure, represents the expressions that use complete sentences as their units of representation. Certainly, one of the best solutions to identifying the correct inter-sentence rhetorical structures is to understand the meaning of each segment [5,37]. However, due to the complexity that is imposed by any deep semantic analysis, in which the search space for potential explanations in a large-scale natural language processing system is likely to be extremely large, we describe only one main type of inference that is used to enforce the connection among segments and is imposed by inter-sentential relation. Understanding a coherent situation relation requires that a path of inferences be established between the situations (i.e., events or states) that are described in the participating text as a whole. Four such relations are summarized in Table 3. In all four cases, the reader is to infer X from key segment $S _ { 1 }$ , and Y from subordinate segment $S _ { 2 }$ under the constraint that the list of presuppositions is abduced [26].

Table 3  
Types of relations and their corresponding connective expression

<table><tr><td>Relation</td><td>Presuppose</td><td>Possible connective expression</td><td>Rank (δ)</td></tr><tr><td>Consequence</td><td>X→Y</td><td>Therefore</td><td>4</td></tr><tr><td>Support</td><td>Y→X</td><td>Because</td><td>4</td></tr><tr><td>Contrast</td><td>X→~Y</td><td>But</td><td>4</td></tr><tr><td>Denial</td><td>Y→~X</td><td>Even though</td><td>4</td></tr></table>

X and Y are the key and subordinate segments, respectively.

Examples of these relations are given in the segments (S1) a–b.

<table><tr><td>(S1)</td><td>a. Judy has a birthday party. ..... (Therefore)She wants a present. (Consequence)b. Judy wants a present. ..... (Even though)It is not her birthday party. (Denial)</td></tr></table>

Beyond what is asserted by the individual meaning of these two segments, each of the segments requires the supposition that having a birthday party implies getting a present. This inference utilizes the sentencelevel semantics that are required for coherence. The inference of the relations relies on the inter-sentential segments as a whole. Once these coherent connections among the segments have been detected, a corresponding rank is assigned to the connection weight. Let $\mathrm { R C } = ( \mathrm { R C } ) _ { i j }$ be a square matrix that represents the connections that are defined only by the effect of rhetorical coherence relations, which is defined by

$$
\mathrm{RC} _ {i j} = \left\{ \begin{array}{l l} \xi + \delta > 0, & \text { if   units } i, j \text { are   coherently   related } \\ 0, & \text { otherwise } \end{array} \right.\tag{2}
$$

We have shown how a shallow coherent structure that is based on rhetorical relations is constructed. In sum, the discourse coherence in our model is modeled by the process of matching text against a small set of relation types, and then using predefined ranks to organize the instances of the event/state concepts that appear in the text. Previous models of text understanding have relied on an allor-none approach, which denies the partial coding of global coherence. Our textual coherence analysis approach changes the goal of understanding from top-level-pattern instantiation to coherence-oriented satisfaction using heuristic rules, and thus generates partial inter-segment relations. In addition, one issue that we have addressed is how coherence is incrementally derived from a static set of observations. The semantic tagging gives us a computational handle on the text by analyzing it into quasi-structured coherent chunks of event descriptions. As the coherence structure is relatively easier to produce than deep causal representation, more difficult causal interpretations of the text can be easier to establish based on these primary representations.

## 5. Sentence-based abstraction technique

The preceding section demonstrates the way in which textual continuities are defined among the discourse segments in the discourse network. In fact, it is considered that the understanding of a discourse involves a series of specific processes, the final result of which is a complete semantic mental representation [32]. The vast amount of information within a discourse is reduced to the essentials when a reader is asked to recall a discourse [9,15]. Details are selectively ignored to produce a distilled version of the original text. It is further demonstrated that discourse can be represented as a skeleton, or a summary, in which the relationships among the clauses can be grouped together in a way that replicates the semantic structure of the original discourse [21]. In this section, we describe how the nonlinearity of the discourse structure that reflects the skeleton can emerge from the discourse through a focusing heuristic. The skeleton emphasizes the central elements of the discourse, but the peripheral details are neglected.

In the discourse network $D ,$ the connection weights between the segments are represented by a square matrix W. Each entry $W _ { i j }$ in W is a numerical value that shows the degree of textual continuity between the discourse segments $\nu _ { i } , \nu _ { j } \in V .$ These are defined by a combination of each of the effects of the above three principles, as is shown in (3). Positive excitatory links with values $\omega _ { 1 } \mathrm { L C } _ { i j } + \omega _ { 2 } \mathrm { R C } _ { i j }$ occur between all of the linguistically related nodes, and negative inhibitory links g occur among the unrelated nodes. $\omega _ { 1 }$ and $\omega _ { 2 }$ are parameters that specify the relative importance of each effect. They are chosen in such a way that both LC and RC are regarded as equally important without discriminating between them. Obviously, W is not a learnt matrix, as is typically the case in auto-associative networks [4,27]. Furthermore, our model takes the simplest conceivable step of generalization by substituting a pair of oppositely directed links of equal weight. Each of the connections carries the meaning is related to without discriminating between the roles of cause or effect. As a result, W is a symmetric matrix; that is $W _ { i j } { = } W _ { j i }$

$$
W _ {i j} = \left\{ \begin{array}{l l} \omega_ {1} \mathrm{LC} _ {i j} + \omega_ {2} \mathrm{RC} _ {i j} & \text { for   LC } _ {i j} \text {   or   RC } _ {i j} \neq 0 \\ - \eta & \text { or   otherwise } \end{array} \right..\tag{3}
$$

When the matrix W has been constructed, a focusing heuristic is used to derive the text nonlinearity from the discourse network. The focusing heuristic is interpreted as a particular transformation of a given set of discourse segments based on the textual continuity. The heuristic is a modified version of a dynamic associative memory network with M nodes that are highly interconnected and feed back upon themselves. It is proved to be capable of capturing the main properties of the human conceptual system, and has been used in various psychological models [3]. Table 4 summarizes the focusing heuristic.

<table><tr><td colspan="2">Table 4Focusing heuristic</td></tr><tr><td>Step 1:</td><td>Construct the overall weight matrix  $W$  as shown above. Initialize a state vector for the discourse segments,  $A(0)=(\Omega_1(0), \Omega_2(0), \dots, \Omega_M(0))$ , where  $\Omega_i(0)$  is the activation of the discourse segment  $i$  as shown in the cohesive parsing.  $M$  is the number of discourse segments in the discourse.</td></tr><tr><td>Step 2:</td><td>At each discrete time,  $t$  activations spread among the nodes of discourse segments and are updated by the following function: $A(t+1)=\beta A(0)+\gamma A(t)+\alpha WA(t).$  (4)</td></tr><tr><td>Step 3:</td><td>Vector  $A(t+1)$  is normalized according to the saturation and habituation functions. $A(t+1)=[\text{SAT}(A(t+1))] \sigma(t)$ , where  $\sigma(t)$  is a habituation variable and $SAT(x)=\begin{cases}1,&1\( x,&-1\leq x\leq1.\\-1,&x<-1\end{cases}$ </td></tr><tr><td>Step 4:</td><td>The reinforcement of  $W_{ij}$  is given by the modified Hebbian learning, where  $\delta W_{ij}(t)=\varphi\{[a_i(t+1)-a_i(t)]a_j(t)+[a_j(t)(t+1)-a_j(t)]a_i(t)\}$ , where  $\varphi$  is the learning rate.</td></tr><tr><td>Step 5:</td><td>Apply steps 2 to 4 for a number of iterations.</td></tr><tr><td>Step 6:</td><td>The final strength between each pair of node  $i,j$  in the discourse network is  $W_{ij}^{*}=\Psi(W_{ij})$ , where  $\Psi(x)=(1)/(1+\mathrm{e}^{-\lambda(x-\theta\bar{x})})$ , where  $\lambda$  is the gain,  $\theta$  is the linkage constant, and  $\bar{x}$  is the mean of  $x$ .</td></tr></table>

The main idea in the heuristic is to modify the activation values of the discourse segments iteratively according to their relative importance. The system operates by accepting a pattern of activations and then amplifying that pattern through the feedback loop. Competing coalitions of the nodes of the discourse network drive the network into a stable equilibrium. The nonlinear skeleton of the discourse is extracted by the interactive activation and competition mechanisms. The details are described as follows. Each discourse segment has its own initial activation value $\Omega _ { i } ( 0 )$ , which is the sum of the final asymptotic activation values of its respective context nodes that were described in the cohesion parsing. Information in this system is represented by an M-dimensional vector with each segment as its component. In step 2, the system receives a constant input $\beta A ( 0 )$ , in which the initial activation of each discourse segment is constantly present. The second term, $\gamma A ( t )$ , causes the current state to decay slightly. This term has the qualitative effect of causing error to eventually decay to zero as long as $\gamma$ is less than 1. The third term, $\alpha W A ( t )$ , passes the current state through the network, and adds more information that is reconstructed from the cross connections. In step 3, the saturation function SAT(x) is the nonlinearity in the associative memory. This confines the states to the hypercube of $[ - 1 , 1 ] ^ { M }$ . When released from the initial state, the discourse network converges to one of the stable vertices of the hypercube [36,51]. As the autoassociative connections form a positive feedback loop, once all the segments in the first set reach their minimal or maximal activation, the pattern of activity no longer changes. As a result, $W _ { i j }$ will be steady. One solution to this problem is to introduce the habituation variable $\sigma ( t )$ into the system, as is shown in step 3 of the heuristic. This provides a mechanism for getting the state out of the corner in which it is trapped. Once all of the nodes become maximally or minimally activated, this modification temporarily decreases the connection strengths between the pairs of elements that display activities that are positively correlated, and increases the connection strengths between pairs of elements that display activities that are negatively correlated. In other words, once a segment has reached its maximum firing rate, this process becomes effective over a fixed period, and lowers the input sensitivity of the node, thus causing a decrease in the components of the saturated subvector. As a consequence, the saturated segments may leave the corners.

The formation and the reinforcement of the weights are represented in step 4. The changes in the strength of the weights are modified by the Hebbian learning rule. It is apparent that the strongest connections will tend to form between pairs of segments that maintain high levels of activation for a prolonged period. Finally, the function $\psi$ in step 6 serves as a cluster transfer function. It is a sigmoid function that enhances the effects of clusters by the gain k with strength above h, the linkage constant multiplied by the mean $W _ { i j } ,$ and the overall mean of the weights in the network. It controls the amount of clusters that appear in the final discourse skeleton. The final stage of the heuristic is to screen the clusters and reduce background clutter in the emerging discourse network. The function W creates a threshold below which a cluster is unlikely to be included as part of the skeleton. It eliminates the weaker connections that result from the formation of weak textual continuity. Qualitatively speaking, the vector $A ( t )$ in the discourse network is a unit vector in a hypercube. As the heuristic proceeds, $A ( t )$ searches its corner and rests in a stable direction that represents the discourse skeleton that is distilled from the multi-faceted interconnections of the textual continuity.

## 6. Simulation experiment and results

The prototype of the system is developed in C and implemented on a DEC Alpha 2000 5/250 in a UNIX environment. In this section, the simulation experiments are described. First of all, to illustrate the above ideas, it is necessary to specify the kind of discourse that is being examined. We have limited our domain of study to texts that describe a sequence of events that follow one another in an approximately linear temporal sequence. They are based on a relatively small number of formats, and consist of a limited set of event sequences that are connected in common ways. It is further put forward that humans assimilate these sequences to form high level knowledge structures that guide comprehension and control memory retrieval [8,45,46]. However, the ideas that are suggested in this article are not just applicable to this restricted class of sequences.

![](/api/attachments/J5EBUWM9/fulltext/images/a61643269088079582c60475fc957fb945515e247df2c25d7ba477f29a2c8bf7.jpg)  
Fig. 5. Initial discourse network of the text Judy’s Birthday. Initial activation of each discourse segment is shown in square brackets. The corresponding discourse segments are shown in Fig. 1.

In our experiments, four texts by Stein and Glenn [55] are analyzed and studied in a series of simulations, and each of the four texts is individually analyzed and modeled as previously described. The details of the text Judy’s Birthday will be discussed for the purposes of illustration. For the text Judy’s Birthday, which has already been shown in Fig. 1, the first step in the simulation involves the construction of the discourse network. Discourse segments are preprocessed in the system, and the two matrices LC and RC are constructed, as described in Sections III and IV. Fig. 5 illustrates the initial discourse network that is formed with 25 nodes, each of which represents a discourse segment, with the context nodes being suppressed. Equal weights are assigned to $\omega _ { 1 }$ and $\omega _ { 2 } ,$ , as is shown in (3), without discriminating between the two factors. More than 40 LC links and 30 RC links are connected with the segments of the discourse network, even though some of them are rather weak. Only the most significant links are shown in the figure. The dotted lines represent the lexical cohesion links and the solid arrows represent the rhetorical coherence relations among the discourse segments with all the inhibitory links hidden. The strength of each connection is defined in (3), and is then subject to the focusing heuristic. Activations are spread in the discourse network with the initial activation vector A(0), as is shown in Fig. 5.

Competing coalitions of the segments drive the network into a stable equilibration. The re-arranged patterns of activation of the discourse segments are shown in Fig. 6. The re-arranged three-dimensional mesh plot is interpreted by noting that the height of each point in the mesh plot that corresponds to the activation of a discourse segment in the discourse network. All points that lie on the same horizontal line correspond to the same discourse segment (e.g., 6. Want(She, Fix(Doll’s House))) at different points in time. All of the points that lie on the same vertical line correspond to the activations of all of the discourse segments that are associated with a situation at a particular instant in time, where time is ordered from the left-hand side of the graph to the righthand side. In the figure, the activation of the 25 discourse segments in the network is indicated by the height above or below the null activation level.

![](/api/attachments/J5EBUWM9/fulltext/images/d8b59ccc65d3e61da073a948cdd201a54a100f4e98f989d93a2efa6da5a5b893.jpg)  
Fig. 6. Mesh plot of activation change in the text Judy’s Birthday during the focusing heuristic.

It is apparent, after more than 20 iterations, that all of the discourse segments become saturated with activations either at 1 or 1. Fig. 7 shows the resultant discourse skeleton in the simulation. The dotted and solid lines represent the clusters that are formed with final strengths that are equal to 0.8 and 1.0, respectively.

The topology of the resultant discourse skeleton reveals something interesting about the salience of information in the text. The basic rationale behind the approach is that nodes that are connected to many other nodes are likely to carry important information [52]. In other words, the salience of a sentence is proportional to the number of sentences that are semantically related to it. The more salient a sentence, the more likely it is that it will be elicited in the process of textual information extraction. Obviously, in our approach, the likelihood of extracting this skeleton from the text relies on the textual continuity. Although there are a number of sophisticated algorithms that can further reduce the size of the graph by collapsing the vertices and edges [31], we take the simple step of singling out the knowledge-intensive subgraph if the final strength of the edge-weights is greater than 0.8. After the focusing heuristic, the subgraphs are consolidated into a more coherent representation and can be regarded as the chunks of knowledge that are extracted from the text.

![](/api/attachments/J5EBUWM9/fulltext/images/b933fd9d7b07eefb8df37adda4f37f45ecd70afa21703a93e7e000e96246499a.jpg)  
Fig. 7. Final discourse skeleton with dotted lines and solid lines representing the clusters that are formed with final strengths that are equal to 0.8 and 1.0, respectively. The gray clusters are the possible knowledge that is extracted from the text.

The study of the important units in text has a long history, but there is little literature on text details and their inter-sentential connections. Trabasso and his colleagues examine what makes a statement <sup>b</sup>important<sup>Q</sup> in a text [57]. It has been hypothesized that when a person judges the importance of a segment of text, they apprehend the conceptual dependencies that the textual segment has on other parts of the text. It has been suggested that the importance of a segment of text relies heavily on the number and quality of the dependencies that the segments have to other text segments. Two main conceptual dependencies have been studied. The first is the identification of the segments that are linked by successive causes and consequences through the text from its opening to its closing. The second is the measurement of how many direct, operative links a textual segment has to other segments, which is also referred to as structural centrality. In the experiment of Trabasso et al., four texts are manually analyzed to find out how readers use these two conceptual dependencies to link segments. In each text, dependency relations are found judgmentally and intuitively, and are then tested using the logical criteria of necessity and sufficiency. All of the segments are represented in a network with the conceptualizations of the events as nodes and the dependencies as arcs. The causal chain of the text is then found using criteria for opening, continuing, and closing the chain, and, more importantly, segments are variously identified as important if they are in the chain.

Because this is a manual analysis, as a check of reliability, their experiments are performed on two different groups who agreed on an average of 96% of the important segments, and the differences were resolved through discussion. Trabasso et al. also found that the direct causes and consequences of text segments can also predict the amount of immediate and delayed memory recall.

To justify our computational approach in squeezing out the important textual information, we compare our discourse skeleton with the causal chains that were formed in Trabasso’s experiment. The comparisons, including the Spearman rank correlation coefficients for each of the four texts, are shown in Table 5.

The Spearman rank coefficient is an alternative to the usual correlation coefficient. It is based on the ranking of the data, but not on the data itself, and so is resistant to outliers. The null hypothesis that is tested by the Spearman rank correlation coefficient is that two variables are independent of each other, against the alternative hypothesis that the rank of one variable is correlated with the rank of another variable. The value of the statistics ranges from  1, which indicates that the high ranking of one variable occurs with the low ranking of another variable, through 0, which indicates no correlation between the variables, to +1, which indicates that the high ranking of one variable occurs with the high ranking of the another variable. The coefficients are usually taken to be the measures of agreement between the judgments among any two groups of observations. In Table 5, each correlation coefficient compares the relative importance of the nodes in the representation of Trabasso et al. with the ranking of the discourse segments in our discourse skeleton after the focusing heuristic. The Spearman rank correlation coefficients that are given above are all significant at the 0.01 level. In general, Spearman rank coefficients between 0.55 and 0.75 are considered to be positive correlations, and coefficients that are larger than 0.75 are considered to be strong correlations. As can be seen in Table 5, the overall correlation coefficients are significant, ranging from 0.42–0.65, despite the differing nature of our discourse skeleton and the causal links in the model of Trabasso et al.

Comparison of the resultant discourse skeletons with the causal chains

<table><tr><td></td><td>Text 1</td><td>Text 2</td><td>Text 3</td><td>Text 4</td></tr><tr><td>Number of words</td><td>173</td><td>163</td><td>178</td><td>160</td></tr><tr><td>Number of sentences</td><td>17</td><td>13</td><td>10</td><td>13</td></tr><tr><td>Number of segments</td><td>25</td><td>23</td><td>23</td><td>25</td></tr><tr><td>Percentage of discourse skeleton formed*</td><td>0.38</td><td>0.31</td><td>0.34</td><td>0.42</td></tr><tr><td>Spearman rank correlation coeff.*@</td><td>0.56</td><td>0.62</td><td>0.53</td><td>0.57</td></tr><tr><td>Percentage of discourse skeleton formed**</td><td>0.26</td><td>0.20</td><td>0.23</td><td>0.29</td></tr><tr><td>Spearman rank correlation coeff.**@</td><td>0.42</td><td>0.51</td><td>0.65</td><td>0.45</td></tr></table>

Note: @ the comparison of the discourse skeletons with the causal links in the model of Trabasso et al. [57] \* final strength = 0.8; \*\* final strength = 1.0.

## 7. Discussion and conclusion

Traditional information retrieval (IR) is concerned with the storage and retrieval of information, and the almost complete absence of the actual analysis of semantic content in IR poses an arduous and timeconsuming subsequent processing requirement for the retrieved documents. Although some serious largescale research efforts in information extraction (IE) have gradually and systematically increased the complexity of the input texts and tried to understand some narrow topics, one of the major limitations to current IE systems is that the template slots and their associated filling criteria must be anticipated and encoded. Most IE research has focused on the production of templates that encode the structure of relevant topics. Even though the information that is encoded in the templates might be central to many applications, there is still widespread demand for a system that uses semantics and moves beyond word-level processing to an understanding of internal discourse structures and partition text. Our technique provides an extract that is constructed by choosing the most relevant pieces of text. It goes beyond templates and begins to address the meaning of the text itself. We target the comparative assessment of saliency and the connectivity of text fragments by using lexical cohesion and thesaural relations. Such an approach makes it possible to detect the major topics of a text automatically, and to assess how well each text unit represents these topics. Our technique can be viewed as one that compresses or condenses a text by discarding the less relevant material. The usual approach to text classification is to reduce a text to a bag of words, which throws away a lot of the linguistic information that is represented, but the salient sentences that are extracted by this abstraction technique provide an alternative to text classification and indexing.

Question answering (QA) has recently attracted intensive research interest, spurred by the competition-based annual Text Retrieval Conference (trec.- nist.gov). QA is an offshoot of the information extraction task. The task of QA moves beyond simple text classification and indexing into the realm of intelligent knowledge extraction. QA is different from simple web searching, because the fully formed questions encode information about the type of answer that is being looked for, whereas keyword queries in traditional search engines do not. Document processing forms the main core of a QA system. A typical QA system performs a more in-depth analysis of both the question and the answer. For example, the answer candidates may be fed into an answer extraction module that determines the best answer on the grounds of the semantic similarity between the question and the answer candidate. One of the critical steps in QA is to identify the most salient sentences and associated boundaries in the text. Our abstraction technique can be used to detect the boundaries between groups of consecutive sentences that are highly relevant to each other. This will help to prevent the QA system from misidentifying important text in a query as being the less important text of a new topic. This allows the QA system to know which topics should be represented in the answer.

With the increasing availability of digital imaging devices and the number of digital images growing at a considerable rate, multi-media communication has become a part of everyday life, and its applications in information systems are increasing in diversity. Nevertheless, the efficient and effective retrieval and management of these multi-media documents are still very challenging research issues. One of the possible extensions of the system that is devised here is in the area of content-based multi-media document retrieval, with both words and image features to represent the relevant document contents. As is discussed in Section II of this paper, although we have defined a discourse network D as a set of discourse segments with finite content words in each segment, extensions can be made to D with a new V, say VV, being a set of multi-media documents and CV being a finite set of keywords and images that are associated with each multi-media document, $\nu ^ { \prime } \in V ^ { \prime }$ . In other words, each vV and its associated content nodes would be used to represent a multimedia document in a collection. Instead of using cohesion parsing and textual coherence analysis to devise the initial weights of the network, as is shown in (3), the connection weights between the multimedia documents in the collection could be deduced based on their image and lexical similarity, without differentiating the cause and effect that is commonly found in the sequence of events in text. We have already explained thoroughly in Section III how the textual features can be extracted, and image feature similarity measures that are based on color, shape, texture, and edge could be used in constructing the weight function W [11]. These heterogeneous textual and image features not only uniquely characterize multi-media documents, but also provide a means to exploit their similarities and differences in content. Our focusing heuristic provides a mechanism for clustering documents based on their relevance, and only similar documents will be linked up in the final skeleton. This integrated multi-media retrieval design, which enables the simultaneous classification of the image and text content of a document (a feature not that is supported by the existing retrieval systems), is an alternative to overcoming the fundamental problem that plagues existing multi-media retrieval systems. The problem is that users want to retrieve documents on the basis of conceptual content, and individual keywords provide weak, if not unreliable, evidence of the conceptual meaning of multi-media documents.

In sum, as interest has extended from pure keyword and cue-phrase matching to a more sophisticated sentence-based approach in information extraction, the importance of text structures in shallow text processing has been realized. In this article, we have identified both the general thread of a text and the ways in which individual sentences fit together. We have described a discourse network of sentence abstraction based on textual continuity that arises from a connectionist model. The experimental results for our prototype show that the discourse network and its abstraction technique are able to correlate semantically relevant sentences. It is a promising approach to understanding documents at a higher level, and one that better reflects human perception. We have also shown that the integration of textual continuity with both lexical cohesion and textual coherence analysis, together with the discourse network, can represent text content better than the use of keywords or cue-phrases only, which helps to improve retrieval performance significantly. The underlying abstraction technique is powerful in capturing and representing textual features in an effective and efficient way.

## Acknowledgement

The author would like to thank the area editor and the anonymous reviewer for their valuable and constructive comments which have contributed to the improvement in the paper. This research project was supported in part by two Competitive Earmarked Research Grants (CUHK 1221/00E and CUHK 4171/01E) of the Research Grants Council of Hong Kong SAR.

## References

[1] R. Alterman, A dictionary based on concept coherence, Artificial Intelligence 25 (1985) 153 – 186.

[2] R. Alterman, L.A. Bookman, Reasoning about a semantic memory encoding of the connectivity of events, Cognitive Science 16 (1992) 205– 232.

[3] J.A. Anderson, G.L. Murphy, Psychological concepts in a parallel system, Physica D 22 (1986) 318 – 336.

[4] J.A. Anderson, J.W. Silverstein, S.A. Ritz, R.S. Jones, Distinctive features, categorical perception, and probability learning: some applications of a neural model, Psychological Review 84 (5) (1977) 413 – 451.

[5] R. Basili, M.T. Pazienza, P. Velardi, An empirical symbolic approach to natural language processing, Artificial Intelligence 85 (1996) 59–99.

[6] M. Benson, Collocations and general-purpose dictionaries, International Journal of Lexicography 2 (1990) 1– 14.

[7] W.J. Black, F. Ciravegna, L. Gilardoni, A. Lavelli, Flexible text classification for financial applications: the FACILE system, Proceedings of 14th European Conference on Artificial Intelligence, IOS Press, Amsterdam, Netherlands, 2000, pp. 696–700.

[8] L. Bloom, Language Development from Two to Three, Cambridge University, 1993.

[9] C.J. Brainerd, V.F. Reyna, Gist is the grist: fuzzy-trace theory and the new intuitionism, Development Review 10 (1) (1990) 3– 47.

[10] S.W.K. Chan, Integrating linguistic primitives in learning context-dependent representation, IEEE Transactions on Knowledge and Data Engineering: Special Issue on Connectionist Models for Learning in Structured Domains 13 (2) (2001) 157– 175.

[11] S.W.K. Chan, M.W.C. Chong, Unsupervised clustering for non-textual web document classification, Decision Support Systems 37 (3) (2004) 377 – 396.

[12] S.W.K. Chan, J. Franklin, Remembrance of discourse based on textual continuity: a spreading activation network, in: N. Foo, R. Goebel (Eds.), PRICAI’96: Topics in Artificial Intelligence: Lecture Notes in Artificial Intelligence, vol. 1114, Springer-Verlag, 1996, pp. 218 – 228.

[13] S.W.K. Chan, J. Franklin, Symbolic connectionism in natural language disambiguation, IEEE Transactions on Neural Networks: Special Issue on Neural Networks and Hybrid Intelligent Models 9 (5) (1998) 739– 755.

[14] S.W.K. Chan, B.K. T’sou, Analyzing discourse structure using lexical cohesion: a connectionist tool, Proceedings of IEEE World Congress on Computational Intelligence – 1998 International Joint Conference on Neural Networks, Alaska, vol. 1, IEEE, New York, NY, 1998, pp. 657 – 662.

[15] H.C. Ellis, R.R. Hunt, Fundamentals of Human Memory and Cognition, Brown, 1989.

[16] B. Endres-Niggemeyer, E. Neugebauer, Professional summarizing: no cognitive simulation without observation, Journal of the American Society for Information Science 49 (6) (1998) 486– 506.

[17] C.R. Fletcher, J.E. Hummel, C.J. Marsolek, Causality and the allocation of attention during comprehension, Journal of Experimental Psychology. Learning, Meaning, and Cognition 16 (2) (1990) 233 – 240.

[18] R. Gaizauskas, Y. Wilks, Information extraction: beyond document retrieval, Journal of Documentation 54 (1) (1998) 70 – 105.

[19] A.C. Graesser, M. Singer, T. Trabasso, Constructing inferences during narrative text comprehension, Psychological Review 101 (3) (1994) 371 – 395.

[20] S.J. Green, Building hypertext links by computing semantic similarity, IEEE Transactions on Knowledge and Data Engineering 11 (5) (1999) 713 – 730.

[21] B.J. Grosz, A.K. Joshi, S. Weinstein, Centering: a framework for modeling the local coherence of discourse, Computational Linguistics 21 (1995) 203– 225.

[22] K. Haberlandt, G. Bingham, Verbs contribute to the coherence of brief narratives: reading related and unrelated sentence triples, Journal of Verbal Learning and Verbal Behavior 17 (1978) 419– 425.

[23] U. Hahn, Topic parsing: accounting for text marco structures in full-text analysis, Information Processing & Management 26 (1990) 135– 170.

[24] M.A.K. Halliday, R. Hasan, Language, Context, and Text: Aspects of Language in a Social-Semiotic Perspective, Deakin University Press, 1985.

[25] A.G. Hauptmann, M.J. Witbrock, Informedia: news-on-demand multimedia information acquisition and retrieval, in: M. Maybury (Ed.), Intelligent Multimedia Information Retrieval, AAAI/MIT Press, California, 1997, pp. 215 – 240.

[26] J.R. Hobbs, M.E. Stickel, D.E. Appelt, P. Martin, Interpretation as abduction, Artificial Intelligence 63 (1993) 69 – 142.

[27] J.J. Hopfield, Neural networks and physical systems with emergent collective computational abilities, Proceedings of the National Academy of Sciences 79 (1982) 2554 – 2558.

[28] E.H. Hovy, Automated discourse generation using discourse structure relations, Artificial Intelligence 63 (1993) 341 – 385.

[29] L. Iwanska, Recovering nonlinearly distributed knowledge: computing discourse structure in factual reports, Natural Language Engineering 3 (1997) 191 – 213.

[30] P.S. Jacobs, L.F. Rau, Innovations in text interpretation, Artificial Intelligence 63 (1993) 143 – 191.

[31] G. Karypis, V. Kumar, A fast and high quality multilevel scheme for partitioning irregular graphs, SIAM Journal on Scientific Computing (1996) 269–278.

[32] W. Kintsch, A cognitive architecture for comprehension, in: H.L. Pick, P. van den Broek, D.C. Knill (Eds.), Cognition: Conceptual and Methodological Issues, 1992, pp. 143 – 163.

[33] W. Kintsch, T.A. van Dijk, Toward a model of text comprehension and production, Psychological Review 85 (5) (1978) 363 – 394.

[34] B. Kosko, Fuzzy cognitive maps, International Journal of Man–Machine Studies 24 (1986) 65 – 75.

[35] W. Lam, K.S. Ho, FIDS: an intelligent financial web news articles digest system, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 31 (6) (2001) 753–762.

[36] W.E. Lilo, D.C. Miller, S. Hui, S.H. Zak, Synthesis of Brain-State-in-a-Box (BSB) based associative memories, IEEE Transactions on Neural Networks 5 (5) (1994) 730 – 737.

[37] D. Long, R. Garigliano, Reasoning by Analogy and Causality: A Model and Application, Ellis Horwood, 1994.

[38] I. Mani, Automatic Summarization, John Benjamins, Amsterdam, 2001.

[39] W.C. Mann, S.A. Thompson, Rhetorical structure theory: toward a functional theory of text organization, Text 8 (3) (1988) 243 – 281.

[40] D. Marcu, Discourse trees are good indicators of importance in text, in: I. Mani, M.T. Maybury (Eds.), Advances in Automatic Text Summarization, MIT Press, Massachusetts, 1999, pp. 123 – 136.

[41] G. McKoon, R. Ratcliff, Inference during reading, Psychological Review 99 (3) (1992) 440 – 466.

[42] R. Miikkulainen, Subsymbolic Natural Language Processing: An Integrated Model of Scripts, Lexicon, and Memory, MIT Press, 1993.

[43] M.F. Moens, C. Uyttendaele, J. Dumortier, Information extraction from legal texts: the potential of discourse analysis, International Journal of Human-Computer Studies 51 (1999) 1155– 1171.

[44] J. Moore, C. Paris, Planning text for advisory dialogues: capturing intentional and rhetorical information, Computational Linguistics 19 (1993) 651 – 694.

[45] K. Nelson, Remembering and telling: a developmental story, Journal of Narrative and Life History 1 (2&3) (1991) 109– 127.

[46] E. Ochs, C. Taylor, D. Rudolph, R. Smith, Storytelling as a theory-building activity, Discourse Processes 15 (1) (1992) 37 – 72.

[47] C. Paice, Constructing literature abstracts by computer: techniques and prospects, Information Processing & Management 26 (1990) 171 – 186.

[48] R. Quirk, S. Greenbaum, G. Leech, A Comprehensive Grammar of the English Language, Longman, 1985.

[49] D.V. Rama, P. Srinivasan, An investigation of content representation using text grammars, ACM Transactions on Information Systems 11 (1993) 51– 75.

[50] G. Rocca, L. Spampinato, G.P. Zarri, W. Black, P. Celnik, COBALT: construction, augmentation and use of knowledge bases from natural language documents, Proceedings of the Artificial intelligence Conference (1994) 165– 173.

[51] A. Schultz, Collective recall via the Brain-State-in-a-Box network, IEEE Transactions on Neural Networks 4 (4) (1993) 580– 587.

[52] E.F. Skorochod’ko, Adaptive method of automatic abstracting and indexing, in: C.V. Freiman (Ed.), Information Processing 71: Proceedings of the IFIP Congress 71, North Holland, Amsterdam, 1972, pp. 1179– 1182.

[53] P. Smolensky, Connectionist modeling: neural computation/ mental connections, in: L. Nadel, L.A. Cooper, P. Culicover, R.M. Harnish (Eds.), Neural Connections, Mental Computation, MIT Press, Cambridge, Mass., 1989, pp. 49 – 67.

[54] H. Somers, B. Black, J. Nivre, T. Lager, A. Multari, L. Gilardoni, J. Ellman, A. Rogers, Multilingual generation and summarization of job adverts: the TREE project, Proceedings of the 5th Applied natural Language Processing Conference, Association for Computational Linguistics, New Brunswick, NJ, 1997, pp. 269 – 276.

[55] N.L. Stein, C.G. Glenn, An analysis of story comprehension in elementary school children, in: R.O. Freedle (Ed.), New Directions in Discourse Processing, Ablex Pub., Norwood, NJ, 1979, pp. 53 – 120.

[56] T. Tombros, F. Crestani, Users’ perception of relevance of spoken documents, Journal of the American Society for Information Science 51 (10) (2000) 929 – 939.

[57] T. Trabasso, T. Secco, P. van den Broek, Causal cohesion and story coherence, in: H. Mandl, N.L. Stein, T. Trabasso (Eds.), Learning and Comprehension of Text, Lawrence Erlbaum, Hillsdale, NJ, 1984, pp. 83 – 111.

[58] P. van den Broek, C.R. Fletcher, Investigations of inferential processes in reading: a theoretical and methodological integration, Discourse Processes 16 (1993) 169– 180.

[59] A. Waibel, T. Schultz, M. Bett, M. Denecke, R. Malkin, I. Rogina, R. Stiefelhagen, J. Yang, Proceedings of IEEE International Conference on Acoustics, Speech and Signal Processing 4 (2003) 752–755.

[60] D.L. Waltz, J.B. Pollack, Massively parallel parsing: a strongly interactive model of natural language interpretation, Cognitive Science 9 (1985) 51– 74.

[61] S.M. Weiss, B.F. White, C.V. Apte, F.J. Damerau, Lightweight document matching for help-desk applications, IEEE Intelligent Systems 15 (2) (2000) 57– 61.

[62] J. Wiebe, G. Hirst, D. Horton, Language use in context, Communications of the ACM 39 (1996) 102 – 111.

[63] R.A. Zwaan, J.P. Magliano, A.C. Graesser, Dimensions of situation model construction in narrative comprehension, Journal of Experimental Psychology. Learning, Meaning, and Cognition 21 (2) (1995) 386 – 397.

Samuel Chan received the M.Sc. degree from the University of Manchester, U.K., and M.Phil. degree from the Chinese University of Hong Kong, and the Ph.D. degree from the University of New South Wales, Australia, all in Computer Science. Before joining the Chinese University of Hong Kong as an associate professor, he has been working in computational intelligence since 1989. His current research interests are in applying machine learning techniques in text and image, corpus-based natural language processing, information retrieval and extraction, and multimedia information processing with emphasis on text and image. He has published articles in Decision Support Systems, IEEE Transactions on Neural Networks, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man and Cybernetics, Journal of Information Science, Artificial Intelligence in Medicine, Machine Translation, International Journal of Computer Processing of Oriental Languages, Applied Artificial Intelligence, and others.
