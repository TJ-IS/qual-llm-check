---
otero_id: 14528
otero_key: "G63CS3P6"
title: "Dynamic faceted navigation in decision making using Semantic Web technology"
authors: "Hak-Jin Kim; Yongjun Zhu; Wooju Kim; Taimao Sun"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.01.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dynamic faceted navigation in decision making using Semantic Web technology

Hak-Jin Kim <sup>a</sup>, Yongjun Zhu <sup>b</sup>, Wooju Kim <sup>c,</sup>⁎, Taimao Sun <sup>c</sup>

<sup>a</sup> School of Business, Yonsei University, 50 Yonsei-ro, Seodaemun-gu, Seoul 120-749, Republic of Korea

<sup>b</sup> College of Computing and Informatics, Drexel University, 3141 Chestnut Street, PA 19104, USA

<sup>c</sup> Dept. of Information and Industrial Engineering, Yonsei University, 50 Yonsei-ro, Seodaemun-gu, Seoul 120-749, Republic of Korea

## a r t i c l e i n f o

Article history: Received 16 July 2013 Received in revised form 31 December 2013 Accepted 17 January 2014 Available online 25 January 2014

Keywords: Facet navigation Semantic search Information gain Decision making

## a b s t r a c t

Categorization in the decision making classi<sup>fi</sup>es decision makers' experiences about the world and provides a guide to reach a goal. This implies that dynamically providing categories re<sup>fl</sup>ecting the given decision context gives a great enhancement in decision quality. This study discusses the dynamic category selection under the Semantic Web environment, focusing on an implementation of a decision support system, the dynamic facet navigation system working with an ontology. Prede<sup>fi</sup>ned <sup>fi</sup>xed categories are provided to re<sup>fi</sup>ne search results to evade use of complex queries and tedious review of search results, but they often output insensible information because of never re<sup>fl</sup>ecting the difference in search results. This paper proposes a dynamic category selection mechanism by using the total gain ratio under a given ontology, and a reordering scheme for resulted categories. It proves the validity of the proposed approach with a statistical analysis lastly.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Consumers face decision making in their everyday lives to <sup>fi</sup>nd their products of interest such as when shopping in the supermarket and choosing their magazines from a variety of periodicals. Nowadays their decision making has gotten more dif<sup>fi</sup>cult because of the product speci<sup>fi</sup>city and the consumer preference variation from mass customization in modern production. This burden of comparing the vast number of different products to <sup>fi</sup>nd the proper demands to decision makers requires good strategies that ease the dif<sup>fi</sup>culty in their decision process. Since decision making commands gathering data and developing alternatives together with conceptual grouping, categorization is one of the fundamental and important approaches in decision process—as in cognitive processes such as language acquisition, learning, prediction, production, and inductive reasoning [1]. Amos Tversky's decision making process, elimination by aspects [2], says that decision making compares all alternatives by aspects; it chooses an aspect; any alternatives without that aspect are eliminated; it repeats this process with as many aspects as needed until there remains only one alternative. With the interpretation of Tversky's decision process, decision makers group alternatives as categories—also called facets—and scope down to the alternatives in the relevant categories in their decision process. Categories, as the abstraction of decision maker's experience in the world, hence have two roles: a category integrates alternatives into a general description toward a decisionmaking goal, and provides an instructional manual for inferences to guide for the goal [3]. The conceptual system of decision making therefore depends on construction of categories and their selection.

This paper focuses on a dynamic categorization—called faceted navigation in literature. The topic of the paper is, in particular, facet selection/ordering using the total gain ratio, applied to a movie search engine working with an ontology. Based on our initial work [4], this study focuses on implementing a dynamic faceted navigation system, as a decision support system, which groups results based on search context using the Semantic Web technology. The current state of search systems requires users to review long lists of items from search results laboriously. A conventional solution to its alleviation is the provision of re<sup>fi</sup>ning <sup>fi</sup>xed categories. Search engines provide categories that classify items in a search result into several groups, and users may re<sup>fi</sup>ne their searches by selecting a category value more relevant to what they want to <sup>fi</sup>nd. A fundamental problem residing in this approach is that re<sup>fi</sup>ning categories are prede<sup>fi</sup>ned and <sup>fi</sup>xed regardless of the difference in search results. Considering human decision making, faceted navigation should dynamically evolve and provide relevant information by contextual grouping, but due to lack of contextual knowledge, <sup>fi</sup>xed category systems do not <sup>fi</sup>t on the condition. Fixed categories may provide insensible information. For example, IMDB<sup>1</sup>, an online database on <sup>fi</sup>lms, has <sup>fi</sup>xed categories in the <sup>fi</sup>xed order such as “Re<sup>fi</sup>ne By Type”, “Re<sup>fi</sup>ne By Provider”, “Re<sup>fi</sup>ne By Top Titles”, “Re<sup>fi</sup>ne By Top Names”, “Re<sup>fi</sup>ne By Genre” and “Re<sup>fi</sup>ne By Payment Model” (Fig. 1). Querying “CBS videos” to its search engine produces all videos provided by “CBS”, but in this case the category “Re<sup>fi</sup>ne By Providers” becomes super<sup>fl</sup>uous

![](/api/attachments/G63CS3P6/fulltext/images/781f8125a69f18d20cf39310d536142dd3211b35b15b5798f104b22ec262dc7c.jpg)

Refine By Type Full Movie (19600) Full Episode (19) Trailer (5132) Film Chort (0) Clip (1054) Music Video (13) Interview (92) Promo (15) Featurette (151) News (254) Videa (3) Derro Reel (430)

## Refine By Provider

WithoutABox (19126) MoveMaze.de (3606) Internet Archive (977) CBS (655) IMDb (646) YouTube (617) Vimeo (218) SnagFilms (167) CineMagla.ro (68) MovesTrailer (42) Moveplayer.it (41) AZMovies (37) MyMovies.Net (37) ZuGuide.com (32)

Refine By Top Titles GameSpot TV (318) The Early Show (74) Entertainment Tonight (51) 60 Minutes (29) The Muppets (28) Rio (27) CBS Evening News with Bob Schieffer (25) CBS News Sunday Morning (22) Naked Horror: The Movie (22) Ncw Moon (17) Mamma Mia! (15) CBS Evening News with Katie Couri: (15) Late Show with David Letterman (13) Bruno (13) The Adventures of Smilin' Jack (12) Up (12) The Insider (11) Låt den rätte komma in (11) The Return of Chandu (10)

##

Harry Strang (54) George Morrell (48) Edward Peil Sr, (17) Horace B. Carpenter (45) Edward Hearn (42) Charles Chaplin (41) Herman Hack (41) Jack O'Shea (41) Jesse Eisenberg (40) Lynton Brent (39) Kristen Stewart (39) Stanley Blystone (33) Charles King (38) J. Farrell MacDonald (38)

Refine By Genre Drama (5810) Comedy (4977) Thriller (1865) Documentary (1787) Rumance (1763) Action (1393) Horror (1294) Fantasy (1096) Crime (1084) Adventure (1071) Animation (1023) Family (956) Mystery (917) Science Fiction (865)

Refine By Payment Model Free—All (26764) cludes ad-supported and offsite videos. Free-Without Leaving IMDb (20884) Includes ad-supported videos

Fig. 1. Fixed categories in IMDB.

and insensible. The combination of free queries and facet selection asks for dynamic generation of facets.

The dynamic category selection is conceivable because the system is based on an ontology which makes meanings of instances and their properties understood by the system. Using the information from the ontology, the selection is attained by the measurement of the relevancy of the properties. Items resulted in a query search hence are structured with their associated properties. For example, if a search result has a book “The Old Man and the Sea”, it has properties in a book ontology such as “Author”, “Publication Date” and “Publisher” (Fig. 2).

![](/api/attachments/G63CS3P6/fulltext/images/b92bc624e52c513760f11c1c8f9bd71e1a07fea834621653e54fae8d9c0b62c4.jpg)  
Fig. 2. Properties of a book.

The properties for a given book item have their own values that describe the characteristics of the item. Importantly, properties may be used for classifying book items as well as for describing them. In this research, categories are properties whose values classify items in search results; items with the same property value go into the same group. The dynamic selection of categories hence can be rephrased as selecting properties that classify items depending on search results; different search results induce different selections. It needs to de<sup>fi</sup>ne a criterion used in the selection process—that is proposed in this research. The ordering in categories is another issue because a category beyond the selection range of order cannot be displayed. The ordering in categories may partially affect on the quality of classi<sup>fi</sup>cation. This research therefore suggests a dynamic category system by developing a measure for a criterion in the category selection and an algorithm for the category ordering.

The presentation is organized after this section as follows. Section 2 provides some background knowledge and information in related works about the dynamic faceted navigation. Section 3 presents the overview of the dynamic category system, the dynamic category selection measure, and the selection procedure. Section 4 proposes a reordering scheme for selected categories and its algorithm. Section 5 demonstrates an example on the calculation of the proposed measure and the reordering scheme. Section 6 evaluates the performance of the system in comparison with the <sup>fi</sup>xed category system. The section of conclusion comes last.

## 2. Related works

This research assumes that a search system is based on ontology. While the term ontology is used in many different disciplines such as philosophy, metaphysics, and information science, this study uses the meaning of ontology de<sup>fi</sup>ned in the Semantic Web technology formed with the Resource Description Framework (RDF), RDF schema, the Ontology Web Language (OWL) [5–8]. Ontology is a speci<sup>fi</sup>cation of a representational vocabulary for a shared domain of discourse (de<sup>fi</sup>nitions of classes, relations, and functions with other objects) [9]. Its expressiveness of resources and their relationships facilitate many information systems adopting it as their structural framework for organizing information and data, mainly due to its availability of information search.

In literature, categories are also called facets and the search using categories faceted search. The faceted search is known to be a good alternative in search for complex search queries, because the mean query length is about 2.4 words and most users do not use advanced search functionality according to [10]. Literature about faceted search or navigation mainly focuses on facet construction, user interface, and facet selection. For facet construction, how to map documents to facet hierarchy is a key issue. Many authors used varied ways: algorithms based on lexical subsumption in [11,12], synsets and hypernym relations in [13], the RawSugar social tagging system in [14], and personalized PageRank values in [15]. For user interface, authors are interested in how to enable intuitive discovery-oriented navigation with easy presentation of a complex information space. A design recommendation in user interface is provided in [16], a visualization scheme in [17], and two-dimensional tables with axes of hierarchical categories and correlating pairs of facets in [18,19], respectively. Facet selection is important in the drill down operation. Ref. [20] selects facets in the perspective of <sup>fi</sup>nding the “surprising” aspects of the data, Ref. [17] uses the combination of each facet's a-priori, query independent usefulness and a dynamic, entropybased measure in selection. Ref. [21] maximizes the utility of the selected facets to each individual searcher, and Ref. [22] sets up and solves the facet selection problem with approximation algorithms. Refs. [23,24] applied the faceted search to product search on the Web.

In generating categories dynamically, a measure needs to be used in selecting one property against another. A fundamental concept that is necessary in order to construct such a measure is Shannon's entropy.

In information theory, entropy is a measure of the average information amount of a given content when it is considered as the value of a random variable [25,26]. Consider the situation of using compression by variable-length codes, where different words are encoded in bit strings of different length. Frequent words are encoded with shorter codes and rare words with longer codes. Entropy is a precise lower bound of the expected number of bits required to encode an instance, denoted by a random variable X and sampled with a probability distribution $p \ [ 2 7 ] .$ It is also considered as a measure of unpredictability; high entropy states that the outcome is unpredictable and zero entropy states that the outcome value is constant. Shannon [25] de<sup>fi</sup>ned the entropy H of a discrete random variable X with the <sup>fi</sup>nite number of values x as

$$
H (X) = E \left[ \log \frac {1}{p (X)} \right] = - \sum_ {x} p (x) \log p (x)\tag{1}
$$

where $p ( x )$ is the probability mass function of an outcome x. When two random variables involved, the joint entropy is de<sup>fi</sup>ned as

$$
H (X, Y) = E \left[ \log \frac {1}{p (X , Y)} \right] = - \sum_ {x, y} p (x, y) \log p (x, y).\tag{2}
$$

To de<sup>fi</sup>ne the measure for faceted navigation, another conceptual measure information gain is needed. In Shannon's theory, a receiver receives a corrupted message with noise. The situation may be represented with two random variables X and Y, where X denotes the original source of the message and Y noise [28]. The amount of information of a random variable X contained in another Y is called information gain IG(X; Y) or mutual information I(X; Y), which is usually de<sup>fi</sup>ned with conditional entropy. Conditional entropy of two random variables X and Y is the amount of information that is newly obtained by X beyond the information about X contained in Y; that is, the additional cost of encoding X given the encoding of Y. It is de<sup>fi</sup>ned by the conditional probability

$$
H (X | Y) = H (X, Y) - H (Y) = - \sum_ {x, y} p (x, y) \log \frac {p (x , y)}{p (y)}\tag{3}
$$

where $p ( x , y )$ is the probability that $X = x$ and $Y = y .$ . Using the conditional entropy, the information gain is de<sup>fi</sup>ned as

$$
I G (X; Y) = H (X) - H (X | Y).\tag{4}
$$

According to [29], it is an asymmetric measure of the difference between two probability distributions, and also the change in information entropy from a prior state to a state that takes some additional information. This means that the entropy of X is obtained by adding some extra information described with the conditional entropy H(X|Y) to the information IG(X; Y) in X presented by Y.

The generation of dynamic categories has not been studied well, and it is hard to <sup>fi</sup>nd an article on it in the literature. Park et al. [30], one of the rare studies, proposed an e-mail classi<sup>fi</sup>cation agent using a category generation method. Their agent generates categories dynamically, based on the information of titles and contents in e-mail messages. Since titles and contents in e-mail messages contain unstructured information that is hard to classify, categories cannot be prebuilt before search and selected from the prebuilt. Thus, they are generated on the spot, and because of that, users cannot anticipate what categories will be generated. This implies that it is very hard to avoid meeting odd and unintuitive categories that are not easily understandable. Users tend to dislike such categories because classifying e-mail messages according to such might be very awkward and make later references not easy. Search results considered in this research, however, are structured because search is based on structured ontology databases; ontologies have prede<sup>fi</sup>ned properties which can be used as categories that classify search results. That structuredness also enables precise analysis in search results and may generate more intuitive and understandable categories. Khoshnevisan [31] proposed a method that identi<sup>fi</sup>es a set of search categories based on category preference obtained from search results. Items in a search result are ranked according to the relevancy to query and each has category preference information. The preference of a category is determined by the order of items found from that category. On the other hand, all items of search results in this paper become correct answers to the given query because ontology search is used; items in a search result cannot be ranked because they have no concept of priority and have the same relevancy to query. All items in an ontology search result are evaluated together, rather than dealt separately, in generating categories. Also, the generated categories may provide more appropriate classi<sup>fi</sup>cation than the method proposed by Khoshnevisan because this research uses an ontology-based complete search while the Khoshnevisan's uses the conventional text-based search.

## 3. The dynamic category selection

## 3.1. The overview of the dynamic category system

The goal of this research is to propose a dynamic category system where categories on search results dynamically change. Fig. 3 shows the overview of the system. All instances are stored in the ontology. When a user asks a search query to the ontology, it returns its result as resources. The system calculates values of measures for categories to be proposed next using the knowledge stored in the ontology. The given number of categories is selected based on the values according to a certain criterion. The selected categories are displayed to the user with the resources. Then the user checks if the displayed resources have an item she or he wants. If it is found, the system stops. Otherwise the user selects a category, which makes the system <sup>fi</sup>nd the corresponding property and identify the property's values from the ontology. The system expands the values to the user, and the user chooses a value. Using the chosen category and value, the system updates the collection of resources to the reduced version of resources that collects all items whose property is the chosen category and whose property value is the chosen value. Based on the updated resources, category measures are recalculated, and the given number of categories is selected and displayed again. This gives the user another chance to check her or his item. If one is not found, it goes to the step of the selection. This process continues until the user <sup>fi</sup>nds an item.

![](/api/attachments/G63CS3P6/fulltext/images/638ce32018f41a735b7f0b6b110acdc77b00e31e9006afe0be0b92dd7820d17c.jpg)  
Fig. 3. Overview of the dynamic category system.

## 3.2. A measure for the category selection

An ontology and resources as a search result under the ontology become inputs to the process. The process analyzes the resources with the knowledge of the structure of the ontology, and outputs a classi<sup>fi</sup>cation of categories, also called properties, according to the resources. The dynamic category generation in ontology search compels selections of appropriate properties prede<sup>fi</sup>ned in a given ontology. A natural arising question is then in what criterion to select properties. A notion is introduced to answer that question. Property A explains Property B well if the category made by Property A contains items homogeneous in the value of Property B. Table 1 lists ten movie titles with three relevant properties: “Director”, “Genre” and “Country”. If the “Genre” of a movie is known to be “Action”, it is easily deduced from Table 1 that the movie was released in “Korea” and directed by “Gyeongtaek Kwak”. If a movie is known to be directed by “Changdong Lee”, its “Genre” is “Drama” and it is a Korean movie. This deduction is not always available because the knowledge of “Korea” gives no hints on properties of “Genre” and “Director”. The main reason for this unavailability is that movies with the value “Korea” of the property “Country” have many different values in the other properties.

When movies in Table 1 are classi<sup>fi</sup>ed in the property “Country”, eight movies belong to one category of value “Korea”, but their similarity within the category is very small because they have different values in properties “Director” and “Genre”. This is the same on the items in the category of value “USA”. They have almost no similarity except that they are released in the same countries. When the movies are classi<sup>fi</sup>ed in the property “Genre”, the extent of similarity increases. Movies in “Action” and “Thriller” categories are all directed by “Gyeongtaek Kwak” and “Junho Bong”, respectively. Even though the “Drama” category still has different values in the property “Director”, the others have the same value. The classi<sup>fi</sup>cation with the property “Director” also increases similarity in comparison with that with the property “Country”. When several classi<sup>fi</sup>ers are available in faceted navigation of objects, a question arises: which classi<sup>fi</sup>er is the best for faceted navigation? It is conventionally stated that a good classi<sup>fi</sup>er classi<sup>fi</sup>es objects similar in values of other properties or features into the same category, and different objects into different categories [32]. This question naturally leads to the requirement of a measure of similarity within each category, made by a given classi<sup>fi</sup>er. If one property explains the others better than any other does in such a measurement, the property should become the best classi<sup>fi</sup>er. In the example of Table 1, the measures of the properties, “Director”, “Genre” and “Country”, represent their abilities to explain “Genre” and “Country”, “Director” and “Country”, and “Director” and “Genre”, respectively.

The total gain ratio (TGR) is used in this paper for the measurement of the extent to which a property explains the others. Every property has a TGR value; if the value is bigger, it explains the other properties better. TGR for a property p in a set of properties is formally de<sup>fi</sup>ned by <sup>P</sup>the sum of values of a subordinate measure, the gain ratio (GR).

Movies with three properties.

<table><tr><td>Movie</td><td>Director</td><td>Genre</td><td>Country</td></tr><tr><td>Friend</td><td>Gyeongtaek Kwak</td><td>Action</td><td>Korea</td></tr><tr><td>Typhoon</td><td>Gyeongtaek Kwak</td><td>Action</td><td>Korea</td></tr><tr><td>The Host</td><td>Junho Bong</td><td>Thriller</td><td>Korea</td></tr><tr><td>Mother</td><td>Junho Bong</td><td>Thriller</td><td>Korea</td></tr><tr><td>Tokyo!</td><td>Junho Bong</td><td>Drama</td><td>Korea</td></tr><tr><td>SILENCED</td><td>Donghyeok Hwang</td><td>Drama</td><td>Korea</td></tr><tr><td>Secret Sunshine</td><td>Changdong Lee</td><td>Drama</td><td>Korea</td></tr><tr><td>Poetry</td><td>Changdong Lee</td><td>Drama</td><td>Korea</td></tr><tr><td>The Beaver</td><td>Jodie Foster</td><td>Comedy</td><td>USA</td></tr><tr><td>Battleship</td><td>Peter Berg</td><td>War</td><td>USA</td></tr></table>

$$
T G R (p) = \sum_ {\hat {p} \in \mathcal {P} \backslash \{p \}} G R (\hat {p}; p)\tag{5}
$$

For a property p, gain ratio values of any other properties $\hat { p }$ about $p$ are calculated and summed to obtain its TGR value. After calculation of TGR values for all properties in , those properties are ordered and considered as categories.

The calculation of the total gain ratio is sequentially built on top of the average information amounts, entropies, of the properties in $\mathcal { P } .$ Before describing the details of the calculation, we de<sup>fi</sup>ne some notations. First let be the ontology that de<sup>fi</sup>nes the domain of the search, <sup>O</sup>and be the set of resources obtained as a search result. Each element <sup>R</sup>in is an instance of the type of , a subject s of a triple $( s , p , o )$ for some <sup>R R</sup>property p and object o in the triple store $\boldsymbol { \mathcal { T } } ( \boldsymbol { \mathcal { O } } )$ representing O. Let be the set of properties whose domains are of the type of ; that is, the set <sup>R</sup>of properties such that triples containing them have the subjects in $\mathcal { R } .$ For example, if a search result contains books such as “The Old Man and the $S e a "$ <sup>R</sup>, “Pride and Prejudice”, and “Oliver Twist”, the type of may be “Book”, and its properties “title” and “author” belong to $\mathcal { P } .$ Now let $\tau$ <sup>P</sup>be the set of triples such that their subjects are search result <sup>T</sup>items in and their properties are in with some objects; that is,

$$
\mathcal {T} = \{(s, p, o) \in \mathcal {T} (\mathcal {O}) | s \in \mathcal {R}, p \in \mathcal {P} \}.
$$

If “The Old Man and the $S e a "$ has the value of property “Author”, “Hemingway”, then a triple

“The Old Man and the Sea”; “Author”; “Hemingway $\ " ) \in \tau$

exists. Let $( \cdot , p , \cdot )$ be a set of all triples with the speci<sup>fi</sup>c property $p$ for some subject and object,

$$
(\cdot , p, \cdot) = \{(s, p, o) | \exists s, o: (s, p, o) \in \mathcal {T} \}
$$

If either the subject or the object of triples is speci<sup>fi</sup>ed, we have more restricted notations such as $( \cdot , p , b )$ ; that is,

$$
(\cdot , p, b) = \{(s, p, b) | \exists s: (s, p, b) \in \mathcal {T} \}
$$

Also given the speci<sup>fi</sup>cation of a property $p _ { j }$ and its object $^ { \cdot } b ,$ the triple set with property $p _ { i } \left( p _ { i } \neq p _ { j } \right)$ and the same subject as the speci<sup>fi</sup>cation is de<sup>fi</sup>ned by,

$$
(*, p _ {i}, \cdot | *, p _ {i}, b) = \left\{(s, p _ {i}, o) | \exists s, o: (s, p _ {i}, o), (s, p _ {j}, b) \in \mathcal {T} \right\}
$$

With more speci<sup>fi</sup>cation about the value of a property, the following is de<sup>fi</sup>ned similarly

$$
\left(*, p _ {i}, a | *, p _ {j}, b\right) = \left\{(s, p _ {i}, a) | \exists s: (s, p _ {i}, a), (s, p _ {j}, b) \in \mathcal {T} \right\}
$$

$N ( S )$ is used to denote the size of a set S. For example, $N ( \cdot , p ; )$ denotes the size of $( \cdot , p , \cdot )$ , the number of triples in with a property p. $N ( \cdot , p , b )$ $N ( * , p _ { i } , \cdot \mid * , p _ { j } , b )$ and $N ( * , p i , a | * , p _ { j } , b )$ <sup>T</sup>are similarly de<sup>fi</sup>ned. $V _ { \mathcal { R } } ( \boldsymbol { p } _ { i } )$ denotes the set of all values that are of range of ${ \dot { p } } _ { i }$ in $\tau ;$ i.e. $V _ { \mathcal { R } } ( p _ { i } ) =$ $\{ o | \exists s , o : ( s , p _ { i } , o ) \in T \}$ <sup>T Rð Þ ¼</sup>. In the similar fashion, given the speci<sup>fi</sup>cation <sup>jf ð</sup>of a property $p _ { j }$ <sup>gÞ T</sup>and its object b, the following set is de<sup>fi</sup>ned

$$
V _ {\mathcal {R}} \left(p _ {i} | \cdot , p _ {j}, b\right) = \left\{o | \exists s, o: (s, p _ {i}, o), (s, p _ {j}, b) \in \mathcal {T} \right\}
$$

Under the notations de<sup>fi</sup>ned above, all subordinate measures to evaluate TGR can be constructed. The entropy $H ( p )$ for each property $p \in \mathcal { P }$ is calculated by:

$$
H (p) = - \sum_ {a \in V _ {\mathcal {R}} (p)} \frac {N (\cdot , p , a)}{N (\cdot , p , \cdot)} \log_ {2} \frac {N (\cdot , p , a)}{N (\cdot , p , \cdot)}\tag{6}
$$

The conditional entropy of $p _ { i }$ given a speci<sup>fi</sup>c value b of a property p<sub>j</sub> is next evaluated, for every pair of properties $p _ { i } , p _ { j } { \in } { \mathcal { P } }$ with $p _ { i } \neq p _ { j } ,$

$$
H \left(p _ {i} | \cdot , p _ {j}, b\right) = - \sum_ {a \in V _ {\mathcal {R}} \left(p _ {i} | \cdot , p _ {j}, b\right)} \frac {N \left(* , p _ {i} , a | * , p _ {j} , b\right)}{N \left(* , p _ {i} , \cdot | * , p _ {j} , b\right)} \log_ {2} \frac {N \left(* , p _ {i} , a | * , p _ {j} , b\right)}{N \left(* , p _ {i} , \cdot | * , p _ {j} , b\right)}\tag{7}
$$

Then the conditional entropy of ${ \dot { p } } _ { i }$ given $p _ { j }$ is de<sup>fi</sup>ned as the average of those conditional entropy values of p for the values of $p _ { j } ,$

$$
H \left(p _ {i} \mid p _ {j}\right) = \sum_ {b \in V _ {\mathcal {R}} \left(p _ {j}\right)} \frac {N \left(* , p _ {i} , \cdot \mid * , p _ {j} , b\right)}{\sum_ {c \in V _ {R} \left(p _ {j}\right)} N \left(* , p _ {i} , \cdot \mid * , p _ {j} , c\right)} H \left(p _ {i} \mid \cdot , p _ {j}, b\right)\tag{8}
$$

The information gain of a property p about a property $p _ { j }$ with $p _ { i } \neq p _ { j }$ is obtained from the difference of the entropy of ${ \dot { p } } _ { i }$ and the conditional entropy of p<sub>i</sub> given p<sub>j</sub>:

$$
I G \left(p _ {i}; p _ {j}\right) = H (p _ {i}) - H \left(p _ {i} | p _ {j}\right)\tag{9}
$$

As mentioned earlier, the information gain provides the amount of information on $p _ { i }$ explained by the information on $p _ { j } .$ In other words, the value of the information gain gives us how much the property $p _ { i }$ is explained by the property $p _ { j } .$ . Since the value of the information gain depends on the number of values of $p _ { j }$ and the total number of triples, it needs to be normalized, and the classification information is used for that purpose. The classi<sup>fi</sup>cation information of ${ \bf \dot { \rho } } _ { p _ { i } }$ and $p _ { j }$ with $p _ { i } \neq p _ { j }$ is calculated as follows:

$$
C I \left(p _ {i}; p _ {j}\right) = \frac {\left| V _ {\mathcal {R}} \left(p _ {j}\right) \right|}{\sum_ {c \in V _ {\mathcal {R}} \left(p _ {j}\right)} N \left(* , p _ {i} , \cdot | * , p _ {j} , c\right)}\tag{10}
$$

The denominator of the classi<sup>fi</sup>cation information is the total number of triples about $p _ { i }$ in all categories over $p _ { j } .$ . The score then represents how many categories of $p _ { j }$ each triple on $p _ { i }$ belongs to on average. The gain ratio of $p _ { i }$ about $p _ { j }$ is obtained by dividing the information gain with the classi<sup>fi</sup>cation information,

$$
G R \left(p _ {i}; p _ {j}\right) = \frac {I G \left(p _ {i} ; p _ {j}\right)}{C I \left(p _ {i} ; p _ {j}\right)}\tag{11}
$$

Thus, the gain ratio is the normalized version of the extent of the explanation of $p _ { i }$ by $p _ { j } .$ . When p has a lot of values and the category of each value has fewer triples, the classi<sup>fi</sup>cation information is big, and consequently the gain ratio gets smaller, which is not an ideal case. The total gain ratio of a property $p$ measures the extent of explanation of all the other properties in by selecting p in (5).

<sup>P</sup>When the ontology and the resources are given, the following <sup>O R</sup>summarizes the procedure of the calculation of the total gain ratio brie<sup>fl</sup>y:

1. Identify the type of to <sup>fi</sup>nd the set $\mathcal { P }$ of properties whose domains <sup>R</sup>are of the type of by referring to .

2. Construct a set of all triples that describe properties in and their values for items in $\mathcal { R } .$

<sup>R</sup>3. Calculate an entropy $H ( p )$ for each property p in .

4. For each pair of propertiesp ; $p _ { j } { \in } { \mathcal { P } } { \mathrm { w i t h } } p _ { i } { \neq } p _ { j } ,$ calculate a conditional entropy $H ( p _ { i } | \cdot , p _ { j } , b )$ for each $\overset { \cdot } { b } \in \overset { } { V } _ { \mathcal { R } } ( p _ { j } )$ , and $H ( p _ { i } | p _ { j } )$ by averaging $H ( p _ { i } | \cdot , p _ { j } , b ) .$

5. For each pair of $p _ { i }$ and $p _ { j }$ with $p _ { i } \neq p _ { j } ,$ calculate the information gain $I G ( p _ { i } ; p _ { j } )$ , the classi<sup>fi</sup>cation information $C I ( p _ { i } ; p _ { j } )$ and the gain ratio GR(p<sub>i</sub>; p<sub>j</sub>) of $p _ { i }$ about $p _ { j } .$

6. Calculate the total gain ratio $T G R ( p )$ for each property p in $\mathcal { P } .$

<sup>P</sup>7. Order the properties in according to the decreasing order of their TGR scores. A property with a higher score is a better classi<sup>fi</sup>er.

## 3.3. A replacement procedure in the category selection

From Section 3.2, properties whose domain consists of resources are arranged as categories by the TGR score values. This may be improved by looking down in the tree spanned out of the type of resources on the ontology further. Consider the situation when a candidate property in has its range type which has also subsequent properties. In Fig. $^ { 4 , }$ <sup>P</sup>the class “Film” has many properties that link many classes as their ranges. The class $" \mathrm { A c t o r } "$ is one of them that is linked by a property, say $p _ { f } , 0 \mathrm { f ^ { * } F i l m ^ { * } }$ , and has also other properties $( \mathsf { e } . \mathsf { g } . \mathsf { p } _ { \mathrm { g } } )$ as their domain to link other classes such as “Education”, “Country”, “Height” and so on. If a property $p _ { g }$ of “Actor” gives more amount of information than $p _ { f }$ in terms of the TGR score values, then it is better that $p _ { g }$ replaces $p _ { f }$ for categories. This replacement process may go down through the tree on the ontology to <sup>fi</sup>nd a better category. This procedure is given as follows:

1. According to the decreasing order of scores of the TGR, order properties in for resources .

<sup>P R</sup>2. If the range of a property $p { \in } { \mathcal { P } }$ has no properties that have it as their <sup>P</sup>domain, p is ranked to its original order.

3. If the range of a property $p _ { i } { \in } { \mathcal { P } }$ has properties that have it as their <sup>P</sup>domain—denote the set of the properties by $\mathcal { P } ( \mathfrak { p } _ { i } )$ , then replace $p _ { i }$ for $p _ { j } { \in } \mathcal { P } ( p _ { i } )$ and calculate the TGR score for $p _ { j } .$ <sup>Pð Þ</sup>For the replacement, <sup>Pð Þ</sup>consider the sequence of triples of $( s , p _ { i } , o _ { i } ) , ( s _ { j } , p _ { j } , o _ { j } )$ where $o _ { i } = s _ { j } ,$ as one triple $( s , \widetilde { p } , o _ { j } )$ by introducing $\widetilde { \boldsymbol { p } } = \boldsymbol { p } _ { i } \boldsymbol { p } _ { j }$ . Then replace $( s , p _ { i } , o _ { j } )$ for $( s , \widetilde { p } , o _ { j } )$ and calculate the TGR for $p _ { j }$

4. Choose $p _ { j } { \in } \mathcal { P } ( p _ { i } )$ that has the highest TGR score and compare it with that of $p _ { i \cdot }$

5. If the TGR score of p is greater than that of ${ \dot { p } } _ { j } , p _ { i }$ remains in its original position of the property ordering of .

<sup>P</sup>6. If the TGR score of p is greater than that of p , p o p replaces p in the property ordering of .

By considering all the properties branched out of resources, it is possible to generate the best properties that explain the resources well.

![](/api/attachments/G63CS3P6/fulltext/images/16f3f1c3021986510d3123263173dab9c97a1094a083003dce385a80240f7743.jpg)  
Fig. 4. The structure of a sample ontology.

## 4. Reordering by Similarity

## Algorithm 1. Property reordering

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1 $L = \emptyset; U = \mathcal{P}$;  
2 pick $p \in U$;  
3 $L \leftarrow L \cup \{p\}; U \leftarrow U - \{p\}$;  
4 while $U \neq \emptyset$ do  
5 forall $p_u \in U$ do  
6 $\text{sim}_L(p_u) = \sum_{p_s \in L} \text{sim}(p_u, p_s)$;  
7 end  
8 $p^* \leftarrow \arg \min_{p_u \in U} \text{sim}_L(p_u)$;  
9 $L \leftarrow L \cup \{p^*\}; U \leftarrow U - \{p^*\}$;  
10 end
</div>

This section discusses a method to reorder categories resulted from the last section by using a similarity measurement. In the category selection, the TGR score re<sup>fl</sup>ects the amount of knowledge about the other properties and as a property contains the most amount of knowledge about the others, it is selected <sup>fi</sup>rst. Hence the selection chooses properties in the order of the amount of knowledge about the others. When the similarity of a pair of properties is de<sup>fi</sup>ned as the extent to which they share their domain instances in triples, choosing a property that has the lowest similarity from the already chosen may give a better classi<sup>fi</sup>er because it induces more different items. Using this idea, the categories may be reordered and may provide a better choice to users. Algorithm 4 describes this rearrangement procedure.

L and U are a pair of ordered and unordered sets of properties, respectively, with $L \cup U = { \mathcal { P } }$ and $L \cap U = \emptyset$ . The algorithm starts from the empty L with for U. Initially it selects an arbitrary p for L from $U ,$ <sup>P</sup>and for each step selects a property p<sup>∗</sup> from U that has the minimum similarity with L. The similarity of a property to the set L is the sum of the similarity values to properties in L.

## Algorithm 2. Similarity calculation

```txt
1 sim(p, q)
2 R ← V_R(p);
3 C ← V_R(q);
4 total ← 0;
5 foreach v ∈ R do
6 val_v ← min_{w∈C} x_p(v) · x_q(w);
7 w* ← arg min_{w∈C} x_p(v) · x_q(w);
8 R ← R - {v};
9 C ← C - {w*};
10 total ← val_v + total;
11 end
12 return total;
13 end
```

Algorithm 2 shows the calculation of the similarity between two properties, which is used in Algorithm 1. Let p and q be two properties in . For each property p, the resource set are partitioned into several <sup>P R</sup>groups according to its range values; equivalently, $\mathcal { T } = \cup _ { \nu \in V _ { \mathcal { R } } ( p ) } ( \cdot , p , \nu )$ for $p \in \mathcal { P }$ . Then each partite $( \cdot , p , \nu )$ <sup>T ¼ Rð Þð Þ-</sup>is represented with the 0–1 vector $\vec { x } _ { p } ( v ) = ( a _ { r } ) _ { r \in \mathcal { R } }$ such that $a _ { r } \mathrm { i } s 1 \mathrm { i } \mathrm { f } ( r , p , v ) { \in } T ;$ ; otherwise, 0. For a pair of <sup>ð Þ ¼ ð Þ R</sup>properties p and q, a matrix $M ( p , q )$ <sup>Þ T</sup>is de<sup>fi</sup>ned by the product of two representative vectors for partites of p and $q ;$ i.e. $\left( \vec { x } _ { p } ( v ) \cdot \vec { x } _ { q } ( w ) \right) _ { v . w }$ where $\nu \in V _ { \mathcal { R } } ( p ) , w \in V _ { \mathcal { R } } ( q )$ <sup>ð Þ - ð Þ</sup>. This implies that each entry of the matrix <sup>Rð Þ Rð Þ</sup>is the number of common subjects s such that $( s , p , \nu )$ and $( s , q , w )$ belongs to . The similarity value of p and q is calculated on $M ( p , q )$

recursively. For $\nu \in V _ { \mathcal { R } } ( p )$ , select $w ^ { * } = a r g m i n _ { w } [ M ( p , q ) ] _ { \nu , w }$ with its minimum value $\nu a l _ { \nu } .$ <sup>Rð Þ</sup> Then the submatrix is obtained by removing the row and column corresponding to v and w<sup>∗</sup>. The <sup>fi</sup>nal similarity value is obtained by adding val and the similarity value from the submatrix.

## 5. An example

This section uses the example of Table 2 to explain better the process of the dynamic category selection described in the last sections. In Table 2, the search result consists of <sup>fi</sup>ve movies whose type is “Movie” with three properties: “Genre”, “Country” and “Director”. To arrange the properties in order of the TGR, their entropy values <sup>fi</sup>rst should be calculated. Since “Genre” has eight triples with <sup>fi</sup>ve different values, its entropy is 2.16 from (6). In the same fashion, “Country” and “Director” has 1.46 and 2.58, respectively. The highest entropy value for “Director” implies that the property value is the most unpredictable. To calculate the gain ratio, the resources of the result is classi<sup>fi</sup>ed according to the values of “Genre”. It is shown in Table 3 when targets are set to “Country” and “Director”. The conditional entropy of “Country” given the values of “Genre” are $\mathrm { ~ 0 ~ } ( = - \mathrm { ~ 1 } l o g _ { 2 } { 1 } )$ for “Comedy”, $1 . 5 ~ ( = ~ - ~ 2 / 4 l o g _ { 2 } 2 / 4 ~ -$ $1 / 4 l o g _ { 2 } 1 / 4 - 1 / 4 l o g _ { 2 } 1 / 4 )$ for “Action”, 1.58 $( = - 1 / 3 ( l o g _ { 2 } 1 / 3 + l o g _ { 2 } 1 /$ $3 + l o g _ { 2 } 1 / 3 ) )$ for “Thriller” $~ 0 ~ ( = - ~ 1 l o g _ { 2 } { 1 } )$ for “Adventure”, and 0 (= − 1log 1) for “Drama”.

The conditional entropy of “Country” given “Genre” can be obtained from averaging these values. Its value is $1 . 0 7 \ : ( = 4 / 1 0 \times 1 . 5 + 3 / 1 0 \times$ 1.58). The corresponding information gain has the value $0 . 3 9 \ : ( = 1 . 4 6 \mathrm { ~ - ~ }$ 1.07) from the difference between the entropy and the conditional entropy. The classi<sup>fi</sup>cation information is $0 . 5 \ : ( = 5 / 1 0 )$ since the number of range values of “Country” is <sup>fi</sup>ve and the number of triples whose range type is “Country” ten. The gain ratio is calculated to be $0 . 7 8 \ : ( = 0 . 3 9 / 0 . 5 )$ . In the same way, the gain ratio of “Director” about “Genre” is 2.88 by setting “Director” as the target. Then the total gain ratio of “Genre” is 3.66 (= 0.78 + 2.88) by adding the gain ratio values of “Country” and “Director” about “Genre”. The total gain ratio scores of all properties are given in Table 4. The properties are arranged in the order of “Country”, “Genre” and “Director” according to the TGR scores.

Alternatively, another arrangement may be obtained by using the measure of similarity. For binary representative vectors, the vector indexes correspond to the movies shown in Table 2. Since <sup>fi</sup>ve resources in the table, vectors are <sup>fi</sup>ve dimensional. Consider the calculation of the similarity between “Country” and “Genre”. Since

$$
\begin{array}{l} V _ {\mathcal {R}} (\{\text {Country} \}) = \{\{\text {Korea} \}, \{\text {USA} \}, \{\text {Australia} \} \} \\ V _ {\mathcal {R}} (\{\text {Genre} \}) = \{\{\text {Comedy} \}, \{\text {Action} \}, \{\text {Thriller} \}, \{\text {Adventure} \}, \{\text {Drama} \} \} \end{array}
$$

the subjects s satisfying s; }Country}; }Korea} ∈ are “Highway <sup>ð Þ T</sup>Star”, “War of the Arrows”, and “SILENCED”, and its corresponding representative vector is (1, 0, 1, 0, 1). In the same way, the vector for the range values “USA” and “Australia” are (0, 1, 0, 1, 0) and (0, 1, 0, 0, 0), respectively. The property “Genre” has representative vectors (1, 0, 0, 0, 0) for “Comedy”, (0, 1, 1, 1, 0) for “Action”, (0, 1, 0, 0, 1) for “Thriller”, (0, 0, 1, 0, 0) for “Adventure”, and (0, 0, 0, 0, 1) for “Drama”. Also, the property “Director” has (1, 0, 0, 0, 0) for “Sangchan”, (1, 0, 0, 0, 0) for “Hyeonsu”, $( 0 , 1 , 0 , 0 , 0 )$ for $^ { \ast } \mathrm { G a r y } ^ { \ast } , ( 0 , 0 , 1 , 0 , 0 )$ for “Hanmin”, (0, 0, 0, 1, 0) for “Len”, and $( 0 , 0 , 0 , 0 , 1 )$ for “Donghyuck”. The products of the vectors for “Country” and “Genre” and for “Country” and “Director” make two matrices in Table 5.

An example for the dynamic category selection.

<table><tr><td>Movie</td><td>Genre</td><td>Country</td><td>Director</td></tr><tr><td>Highway Star</td><td>Comedy</td><td>Korea</td><td>Sangchan Kim, Hyeonsu Kim</td></tr><tr><td>The Killer Elite</td><td>Action Thriller</td><td>USA Australia</td><td>Gary McKendry</td></tr><tr><td>War of the Arrows</td><td>Action Adventure</td><td>Korea</td><td>Hanmin Kim</td></tr><tr><td>Live Free or Die Hard SILENCED</td><td>Action Drama Thriller</td><td>USA Korea</td><td>Len Wiseman Donghyeok Hwang</td></tr></table>

Table 3 Movies classi<sup>fi</sup>ed by “Genre”.

<table><tr><td></td><td>Target: country</td><td>Target: director</td></tr><tr><td>Comedy</td><td>Highway Star: Korea</td><td>Highway Star: Sangchan Highway Star: Hyeonsu</td></tr><tr><td>Action</td><td>The Killer Elite: USA The Killer Elite: Australia War of the Arrows: Korea</td><td>The Killer Elite: Gary War of the Arrows: Hanmin Live Free or Die Hard: Len</td></tr><tr><td>Thriller</td><td>The Killer Elite: USA The Killer Elite: Australia SILENCED: Korea</td><td>The Killer Elite: Gary SILENCED: Donghyeok</td></tr><tr><td>Adventure Drama</td><td>War of the Arrows: Korea SILENCED: Korea</td><td>War of the Arrows: Hanmin SILENCED: Donghyeok</td></tr></table>

$u _ { 1 } , . . . , u _ { 3 }$ stand for the values of $V _ { \mathcal { R } } ( " \mathrm { C o u n t r y " } ) , \nu _ { 1 } , . . . , \nu _ { 5 }$ for those of $V _ { \mathcal { R } } \left( \mathrm { " G e n r e " } \right)$ , and $w _ { 1 } , . . . , w _ { 6 }$ <sup>R</sup>for those of $V _ { \mathcal { R } } \left( " \mathrm { D i r e c t o r s " } \right)$ . In the <sup>R R</sup>matrices, selections of entries are denoted by bold-faced numbers. Each entry is the product of two representative vectors. If the value is higher, the two corresponding groups share more items and have higher similarity. For each value of one property, the smallest value of the other is selected in the calculation of the similarity. In the <sup>fi</sup>rst matrix, $\nu _ { 1 }$ is selected for $u _ { 1 } ;$ after removing those row and column, v for $u _ { 2 } ;$ after removing $u _ { 2 }$ and $\nu _ { 4 } , \nu _ { 5 }$ for $u _ { 3 } .$ . The similarity value of “Country” and “Genre” is the sum of the chosen values, $1 + 0 + 0 = 1 .$ In the same fashion, the similarity of “Country” and “Director” is obtained with its value 0. Since the similarity value between “Country” and “Director” is smaller than that between “Country” and “Genre”, we can switch “Genre” and “Director” in their positions. We have a new arrangement: “Country”, “Director” and “Genre”.

## 6. Evaluation

This section proves the performance of the proposed scheme by experimentation. Since this study assumes the Semantic Web environment, the usual unstructured Web data whose search method is textbased is not good for the purpose; it requires that data be organized under an ontology and available to ontology-based search systems. A <sup>fi</sup>lm ontology was constructed after that of FreeBase.<sup>2</sup> In Fig. 5, Class Film has <sup>fi</sup>fteen properties; the classes of type Person, such as Director, Actor, Producer and so forth, have <sup>fi</sup>ve properties; Class Country has two properties. All individual data were collected from the Web site of DAUM Movies <sup>3</sup> by using a parser. The class instance data were excerpted as many as possible, and property information, about such as directors, actors and so on, was also collected from the site. The ontology store thereby contains more than one thousand movie instances and nine thousand person instances.

This experimentation assumes the situation of browsing—to see what is available for certain combinations of facets. It compared the performances for the conventional <sup>fi</sup>xed faceted navigation and four variant methods of the proposed scheme with TGR and the similarity measure in Table 6. For each method, a navigation system was implemented to help users search. Twenty four users were asked to use these systems representing the given methods to search their target items with help of their hinting category values about the targets. Table 7 displays all search items that users searched. Each user was assumed not to know exactly the target item he or she wants to <sup>fi</sup>nd but to know three hinting categories and their values for the unknown target item. A user started with a search result and the categories generated from the initial query by each system. Then he or she chose a category and selected the corresponding value according to the hinting category-value pairs of the target item; it is said to be a step in a navigation process. A system generates the reduced search result with the selection of a category and its value as its input and moves to the next step of the process. Since a selection of category and its value strengthens the search condition, the result narrows down to the smaller number of search items.

Table 4  
The TGR scores calculated from IG, CI, and GR.

<table><tr><td rowspan="2">Target property</td><td colspan="3">Genre</td><td colspan="3">Country</td><td colspan="3">Director</td></tr><tr><td>IG</td><td>CI</td><td>GR</td><td>IG</td><td>CI</td><td>GR</td><td>IG</td><td>CI</td><td>GR</td></tr><tr><td>Genre</td><td></td><td></td><td></td><td>0.52</td><td>0.3</td><td>1.73</td><td>1.49</td><td>0.07</td><td>2.22</td></tr><tr><td>Country</td><td>0.39</td><td>0.5</td><td>0.78</td><td></td><td></td><td></td><td>1.17</td><td>0.86</td><td>1.36</td></tr><tr><td>Director</td><td>1.61</td><td>0.56</td><td>2.88</td><td>1.15</td><td>0.43</td><td>2.67</td><td></td><td></td><td></td></tr><tr><td>TGR</td><td></td><td></td><td>3.66</td><td></td><td></td><td>4.4</td><td></td><td></td><td>3.58</td></tr></table>

Table 5  
Matrices of the products of representative vectors. The signi<sup>fi</sup>cance of bold emphasis are <sup>fi</sup>nally chosen values for similarity value calculation.

<table><tr><td></td><td> $v_1$ </td><td> $v_2$ </td><td> $v_3$ </td><td> $v_4$ </td><td> $v_5$ </td><td> $w_1$ </td><td> $w_2$ </td><td> $w_3$ </td><td> $w_4$ </td><td> $w_5$ </td><td> $w_6$ </td></tr><tr><td> $u_1$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td> $u_2$ </td><td>0</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $u_3$ </td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 6 Search methods.

<table><tr><td>No.</td><td>Methods</td></tr><tr><td>1</td><td>Fixed faceted navigation (F)</td></tr><tr><td>2</td><td>TGR faceted navigation without update (T)</td></tr><tr><td>3</td><td>TGR faceted navigation with update (T-update)</td></tr><tr><td>4</td><td>TGR-similarity faceted navigation without update (T-S)</td></tr><tr><td>5</td><td>TGR-similarity faceted navigation with update (T-S-update)</td></tr></table>

The <sup>fi</sup>xed faceted navigation (F) always provides a <sup>fi</sup>xed set of categories displayed for whatever the search query and the chosen value are. This is the conventional faceted navigation. The second (T) calculates TGR scores when the system generates the search result from the initial query statement. All categories are ordered according to the TGR scores and their respective <sup>fi</sup>xed numbers are displayed to users. In this search process, TGR scores are never updated. If one category is selected and removed in the next step, the category not displayed with the highest TGR score is added to the display to show the same number of categories in display. The third (T-update) is the same as the method T but updating TGR scores according to the search result at every step. The fourth (T-S) uses the similarity measure in reordering categories without update. As in method T, it orders all categories by TGR scores with respect to the initial search result and reorders them by the similarity. It never updates the order in the following steps. The last (T-S-update) updates TGR and similarity measures at every step.

Each navigation process proceeds step by step according to the selections of categories and values until the number of items in results

![](/api/attachments/G63CS3P6/fulltext/images/6b99ecaf5bfd105f4f238c69d0aeeccfc92bc6a421cc825299152ebb8a913a63.jpg)  
Fig. 5. Structure of <sup>fi</sup>lm ontology.

Table 7 Search samples

<table><tr><td>Target Item</td><td colspan="3">Hinting categories/values</td></tr><tr><td rowspan="2">The Scent of Love</td><td>Producer</td><td>Art director</td><td>Story writer</td></tr><tr><td>Taewon Jung</td><td>Sangho Ha</td><td>Hain Kim</td></tr><tr><td rowspan="2">The Scam</td><td>Writer</td><td>Music director</td><td>Distribution co.</td></tr><tr><td>Hojae Lee</td><td>Youngjin Mok</td><td>Showbox</td></tr><tr><td rowspan="2">Skills</td><td>Cinematographer</td><td>Editor</td><td>Costume designer</td></tr><tr><td>Ola Magnestam</td><td>Johannes Runeborg</td><td>Karolina Nilsson</td></tr><tr><td rowspan="2">To Catch a Virgin Ghost</td><td>Writer</td><td>Cinematographer</td><td>Art director</td></tr><tr><td>Jungwon Shin</td><td>Hyunjae Oh</td><td>Sangman Oh</td></tr><tr><td rowspan="2">The Sorcerer&#x27;s Apprentice</td><td>Story writer</td><td>Production Co.</td><td>Music director</td></tr><tr><td>J. W. von Goethe</td><td>Jerry Bruckheimer</td><td>Trevor Rabin</td></tr><tr><td rowspan="2">Barking Dogs Never Bite</td><td>Editor</td><td>Writer</td><td>Music director</td></tr><tr><td>Ensoo Lee</td><td>T. Sohn, J. Bong</td><td>Sungwoo Jo</td></tr><tr><td rowspan="2">Source Code</td><td rowspan="2">Distribution co. Synergy</td><td>Art director</td><td>Costume designer</td></tr><tr><td>Pierre Perrault</td><td>Renée April</td></tr><tr><td rowspan="2">Aegis</td><td>Music director</td><td>Story writer</td><td>Editor</td></tr><tr><td>Trevor Jones</td><td>Harutoshi Fukui</td><td>William M. Anderson</td></tr><tr><td rowspan="2">Antarctic Journal</td><td>Initial release date</td><td>Music director</td><td>Writer</td></tr><tr><td>2005-05-09</td><td>Kenji Kawai</td><td>J. Bong, P. Yim</td></tr><tr><td rowspan="2">Dororo</td><td>Story writer</td><td>Writer</td><td>Initial release date</td></tr><tr><td>Osamu Tezuka</td><td>Masa Nakamura</td><td>2007-10-25</td></tr><tr><td rowspan="2">A Million</td><td>Initial release date</td><td>Story writer</td><td>Cinematographer</td></tr><tr><td>2009-08-06</td><td>Sungkyu Jo</td><td>Jaehoon Lyu</td></tr><tr><td rowspan="2">Jealousy Is My Middle Name</td><td>Writer</td><td>Editor</td><td>Producer</td></tr><tr><td>Chanok Park</td><td>Chanok Park</td><td>Jokwangsoo Kim</td></tr><tr><td rowspan="2">The City of Violence</td><td>Music director</td><td>Art director</td><td>Writer</td></tr><tr><td>Joonsuk Bang</td><td>Hwasung Jo</td><td>Wonjae Lee</td></tr><tr><td rowspan="2">My Love</td><td>Director</td><td>Costume designer</td><td>Production co.</td></tr><tr><td>Han Lee</td><td>Heejoon Ahn</td><td>Ozone Film</td></tr><tr><td rowspan="2">Over the Rainbow</td><td>Director</td><td>Music director</td><td>Initial release date</td></tr><tr><td>Jinwoo Ahn</td><td>Hojoon Park</td><td>2002-05-17</td></tr><tr><td rowspan="2">The International</td><td>Cinematographer</td><td>Producer</td><td>Initial release date</td></tr><tr><td>Frank Griebe</td><td>Lloyd Phillips</td><td>2009-02-26</td></tr><tr><td rowspan="2">The Ring Virus</td><td>Writer</td><td>Music director</td><td>Art director</td></tr><tr><td>Dongbin Kim</td><td>Il Won</td><td>Bongoh Kim</td></tr><tr><td rowspan="2">The Last Legion</td><td>Writer</td><td>Music director</td><td>Art director</td></tr><tr><td>Valerio Manfredi</td><td>Patrick Doyle</td><td>Roberto Caruso</td></tr><tr><td rowspan="2">The Girl Is Bad Ass</td><td>Initial release date</td><td>Producer</td><td>Distribution Co.</td></tr><tr><td>2010-03-25</td><td>Prachya Pinkaew</td><td>DigitalKIN</td></tr><tr><td rowspan="2">Stormbreaker</td><td>Story Writer</td><td>Writer</td><td>Editor</td></tr><tr><td>Anthony Horowitz</td><td>Anthony Horowitz</td><td>Andrew MacRitchie</td></tr><tr><td rowspan="2">Soo</td><td>Distribution co.</td><td>Story writer</td><td>Music director</td></tr><tr><td>Cinema Service</td><td>Youngwoo Shin</td><td>Byungwoo Lee</td></tr><tr><td rowspan="2">HAHAHA</td><td>Music director</td><td>Cinematographer</td><td>Production co.</td></tr><tr><td>Youngjin Jung</td><td>Hongel Park</td><td>Jeonwonsa</td></tr><tr><td rowspan="2">Running Turtle</td><td>Art director</td><td>Initial release date</td><td>Writer</td></tr><tr><td>Sungjoo Nam</td><td>2009-06-11</td><td>Yeonwoo Lee</td></tr><tr><td rowspan="2">Countdown</td><td>Music director</td><td>Cinematographer</td><td>Art director</td></tr><tr><td>Youngkyu Jang</td><td>Taekyung Kim</td><td>Hongsam Yang</td></tr></table>

becomes at most <sup>fi</sup>fteen. When the <sup>fi</sup>nal result contains the target item, the process is considered as a success. The process should never go on in<sup>fi</sup>nitely because a user never keeps selecting categories in reality. This experimentation gave <sup>fi</sup>ve steps as the maximum. The number of steps, corresponding to the number of clicks to users, is counted until the search <sup>fi</sup>nds its target item successfully. If the process passes the <sup>fi</sup>fth step with neither the reduction of the result up to at most <sup>fi</sup>fteen items nor the containment of the target item, the process is considered to go forever and marked as a failure; this case is scored 10. All methods display <sup>fi</sup>ve categories to users.

Table 8 shows the mean number of steps each system took to <sup>fi</sup>nd target items with the given samples. Method T is almost the same as the <sup>fi</sup>xed faceted navigation in performance, which is reasonable because it is fundamentally the same as Method F. Method T is different only in the initial display while both keep the <sup>fi</sup>xed set of categories. For the different scores, signi<sup>fi</sup>cance tests were performed by the nonparametric studentized bootstrapping method [33,34] to see whether the differences are statistically signi<sup>fi</sup>cant. An open source statistical language, Language R, with a package “bootstrap” was used for implementation. The methods were pairwise compared with mean comparison hypotheses. R = 999 bootstrap samples were replicated out of values for the items in Table 7. Each bootstrap sample is then used to evaluate student- t statistics t<sup>∗</sup>. The resulted p value is calculated as follows:

Mean values for the number of steps.

<table><tr><td>F</td><td>T</td><td>T-S-update</td><td>T-S</td><td>T-update</td></tr><tr><td>5.8333</td><td>5.8333</td><td>5.6667</td><td>4.8750</td><td>3.6250</td></tr></table>

$$
p = \frac {1 + \# \{t _ {r} ^ {*} \geq t \}}{R + 1}
$$

where t is the student- t statistic value for the original sample and #{A} is the number of elements satisfying a statement A. The results of this signi<sup>fi</sup>cance test are given in Table 9. In the table, the value of each cell is the p-value for the alternative hypothesis that the mean for the corresponding row method is greater than that for the corresponding column method. Under the 5% signi<sup>fi</sup>cance level, method T-update improves the performance when compared with any other methods except method T-S. Since the method accompanies update of TGR value at every step, it is a complete dynamic faceted navigation scheme, and is clearly better than the <sup>fi</sup>xed schemes of methods F and T. While the mean step number for T-update is smaller than that of T-S, their difference is insigni<sup>fi</sup>- cant. From the comparison of methods F and T, it seems that how to determine the <sup>fi</sup>xed set of categories does not give an impact in performance. Unfortunately, the result of the table shows that the use of the similarity measure in reordering has unclear results on the performance improvement. Using the similarity at every step (T-S-update) resulted in aggravated score in Table 8 in comparison with the mean step value of the method T-S, even though they are not signi<sup>fi</sup>cantly different. If TGR and the similarity measure is used only at the initial step without update (T-S), there is a little improvement but it is not signi<sup>fi</sup>cantly different. Since the reordering with the similarity is based on how much a category does not share values with the top TGR category, it seems not to measure its natural information containment but the relative extent far off from the top category. The similarity does not seem to be a good measure in faceted navigation. It is supposed to give just a disruptive effect on the faceted navigation using TGR.

In this experimentation, a simple query statement “<sup>fi</sup>lm” is used to obtain the initial search result. Using other or complex queries has no problem in the current experimentation scheme while complex query statements require the collection of the vast amount of data. Considering the requirement of the construction of structured data under the Semantic Web technology, it is very hard to construct a system for experimentation that is very close to the real situation. The implication obtained in this section, however, can be easily extended to the cases of complex queries as well as other simple queries. The reason is that the search process depends only on the information contained in the initial search result—the extent to which the result is explained by other related categories, but not on the form of queries. In particular, asking a complex query about <sup>fi</sup>lm may put out resulted items of narrower scope because of the stronger condition, but they are still related to the same kinds of properties as in the simple query “<sup>fi</sup>lm”; this suggests that the search step for the complex query meets the same state as in the simple query, and the search process proceeds in the same fashion. The improvement of search by the dynamic faceted navigation is therefore useful even when using complex queries.

## Table 9

p-Values in signi<sup>fi</sup>cance tests for comparisons of mean values.

<table><tr><td></td><td>F</td><td>T</td><td>T-S-update</td><td>T-S</td><td>T-update</td></tr><tr><td>F</td><td>-</td><td>0.481</td><td>0.511</td><td>0.439</td><td>0.025*</td></tr><tr><td>T</td><td>-</td><td>-</td><td>0.521</td><td>0.820</td><td>0.023*</td></tr><tr><td>T-S-update</td><td>-</td><td>-</td><td>-</td><td>0.796</td><td>0.023*</td></tr><tr><td>T-S</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.120</td></tr></table>

## 7. Conclusion

This paper proposes a dynamic faceted navigation under the Semantic Web environment through a dynamic category system in the context of the ontology-based search. Selecting categories dynamically has advantages in that it provides different categories for users according to their search contexts. If users query with different key words, they might assume different contexts and naturally categories provided with the results should be adapted to their situations. The proposed approach evaluates search results with a measure and shows different categories according to the results. This is signi<sup>fi</sup>cant because this faceted navigation leads to different paths of search experience that suit for users' search contexts, and users eventually reach the items with ease that they want to search for. It can save much time for users and improve the ef<sup>fi</sup>ciency in search. While this study focuses on the ontologybased search in the Internet, the proposed dynamic faceted navigation can be extended to any category systems based on structured data. Together with the proposed measure, which analyzes information of search results to select categories, this paper also suggests a replacement procedure to improve the categories obtained from the measure, and an reordering algorithm based on a measure of similarity. The experimentation for performance evaluation shows that the outcome from the dynamic faceted navigation is more ef<sup>fi</sup>cient than the <sup>fi</sup>xed counterpart while using the similarity for reordering gives no effect. One possible future research direction is to re-validate the effect of the similarity for reordering because this paper considers only search steps as a unique performance measure. Since using similarity requires more computational work at each step, a computational study might be needed to measure the true effect of this approach.

## References

[1] Formal approaches in categorization, in: E.M. Pothos, A.J. Wills (Eds.), Cambridge University Press, 2011.

[2] R. Batley, A. Daly, On the equivalence between elimination-by-aspects and generalized extreme value models of choice behavior, Journal of Mathematical Psychology 50 (5) (2006) 456–467.

[3] Handbook of categorization in cognitive science, in: H. Cohen, C. Lefebvre (Eds.), Elsevier Science 2005.

[4] Y. Zhu, D. Jeon, W. Kim, J.S. Hong, M. Lee, Z. Wen, Y. Cai, The dynamic generation of refining categories in ontology-based search, Semantic Technology, Springer, 2013. pp. 146–158.

[5] D. Brickley, R.V. Guha, RDF vocabulary description language 1.0: RDF Schema, W3C recommendation, February 2004.

[6] G. Klyne, J.J. Carroll, B. McBride, Resource Description Framework (RDF) concepts and abstract syntax, W3C recommendation, February 2004.

[7] Semantic Web Workshop (WWW), Jena: implementing the RDF model and syntax speci<sup>fi</sup>cation.

[8] E. Prud'hommeaux, A. Seaborne, SPARQL query language for RDF, W3C candidate recommendation, June 2007.

[9] T.R. Gruber, A translation approach to portable ontology speci<sup>fi</sup>cations, Knowledge Acquisition 5 (2) (1993) 199–200.

[10] H. Inan, Search analytics: a guide to analyzing and optimizing website search engines, Hurol Inan, 2006.

[11] W. Dakka, P.G. Ipeirotis, K.R. Wood, Automatic construction of multifaceted browsing interfaces, Proceedings of the 14th ACM International Conference on Information and Knowledge Management, ACM, 2005, pp. 768–775.

[12] W. Dakka, R. Dayal, P. Ipeirotis, Automatic discovery of useful facet terms, SIGIR Faceted Search Workshop, 2006, pp. 18–22.

[13] E. Stoica, M.A. Hearst, M. Richardson, Automating creation of hierarchical faceted metadata structures, HLT-NAACL, 2007, pp. 244–251.

[14] D. Feinstein, F. Smadja, Hierarchical tags and faceted search. The RawSugar approach, Proc. SIGIR 2006 Workshop on Faceted Search, 2006, pp. 23–25.

[15] C. Kohlschütter, P.-A. Chirita, W. Nejdl, Using link analysis to identify aspects in faceted web search, SIGIR'2006 Faceted Search Workshop, 2006, pp. 55–59.

[16] M. Hearst, Design recommendations for hierarchical faceted search interfaces, ACM SIGIR workshop on faceted search, 2006, pp. 1–5.

[17] W.A. Arentz, A. Øhrn, Multidimensional visualization and navigation in search results, Knowledge-Based Intelligent Information and Engineering Systems, Springer, 2004, pp. 620–629.

[18] B. Shneiderman, D. Feldman, A. Rose, X.F. Grau, Visualizing digital library search results with categorical and hierarchical axes, Proceedings of the <sup>fi</sup>fth ACM conference on Digital libraries, ACM, 2000, pp. 57–66.

[19] D.N. Meredith, J.H. Pieper, Beta: better extraction through aggregation, SIGIR2006 Workshop on Faceted Search, 2006, pp. 8–12.

[20] D. Dash, J. Rao, N. Megiddo, A. Ailamaki, G. Lohman, Dynamic faceted search for discovery-driven analysis, Proceedings of the 17th ACM Conference on Information and Knowledge Management, ACM, 2008, pp. 3–12.

[21] J. Koren, Y. Zhang, X. Liu, Personalized interactive faceted search, Proceedings of the 17th International Conference on World Wide Web, ACM, 2008, pp. 477–486.

[22] S. Liberman, R. Lempel, Approximately optimal facet selection, Proceedings of the 27th Annual ACM Symposium on Applied Computing, ACM. 2012, pp. 702–708

[23] D. Vandic, J.-W. Van Dam, F. Frasincar, Faceted product search powered by the semantic web, Decision Support Systems 53 (3) (2012) 425–437.

[24] D. Vandic, F. Frasincar, U. Kaymak, Facet selection algorithms for web product search, Proceedings of the 22nd ACM International Conference on Conference on Information & Knowledge Management, ACM, 2013, pp. 2327–2332

[25] C.E. Shannon, A mathematical theory of communication, ACM SIGMOBILE Mobile Computing and Communications Review 5 (1) (2001) 3–55.

[26] T. Cover, J. Thomas, Elements of information theory, John Wiley & Sons, 1991.

[27] D. Koller, N. Friedman, Probabilistic graphical models: principles and techniques, The MIT Press, 2009.

[28] R.M. Gray, Entropy and information theory, Springer, 2011.

[29] S. Kullback, R.A. Leibler, On information and suf<sup>fi</sup>ciency, Annals of Mathematical Statistics 22 (1) (1951) 76–86.

[30] S. Park, S.-H. Park, J.-H. Lee, J.-S. Lee, E-mail classi<sup>fi</sup>cation agent using category generation and dynamic category hierarchy, AIS'04 Proceedings of the 13th International Conference on AI: Simulation, and Planning in High Autonomy Systems, 2004, pp. 207–214.

[31] C. Khoshnevisan, Dynamic selection and ordering of search categories based on relevancy information, Tech. Rep. US 7,698,261 B1, U.S. Patent (April 2010).

[32] R.O. Duda, P.E. Hart, D.G. Stork, Pattern classi<sup>fi</sup>cation, John Weilery & Sons, 2001.

[33] B. Efron, R.J. Tibshirani, An introduction to the bootstrap, Chapman and Hall/CRC, 1994.

[34] A.C. Davison, D.V. Hinkley, Bootstrap methods and their application, Cambridge University Press. 1997

Hak-Jin Kim is an associate professor of Operations Research in the School of Business at Yonsei University, Seoul, Korea. He holds a Ph.D. in Operations Research from Tepper School of Business in Carnegie Mellon University, an MS in Mathematics from University of Illinois at Urbana-Champaign, and a BBA from Yonsei University. He is currently interested in the integer programming, constraint programming, logic-based optimization, Semantic Web and sensor networks. He has published in Decision Support Systems Annals of Operations Research, Knowledge Engineering Review, Telematics and Informatics and other journals.

Yongiun Zhu received his B.S. degree in International Economics and Trade with a double major in Computer Science from Yanbian University of Science and Technology, China in 2009. He is currently working toward the M.S. degree in Information and Industrial Engineering as a member of the Intelligent Web Business Lab at Yonsei University, Korea. His research interests include Ontology, Semantic Web, and Information Retrieval.

Wooju Kim is a professor of Information and Industrial Engineering at Yonsei University, Seoul, Korea. He received a BBA degree from Yonsei University in 1987, and a Ph.D. in Management Science from KAIST in 1994. He has published many papers related to the issues including Semantic Web, Web Services, e-Business, Expert Systems, S/W Engineering and Managerial Forecasting. His current research areas are decision support systems on the Semantic Web environment, Semantic Web mining, knowledge management and intelligent web services.

Taimao Sun received his B.S. Degree in Management Information System from Yanbian University of Science of Technology (YUST), China in 2010. He is currently working toward the M.S Degree in Information and Industrial Engineering as a member of the Intelligent Web Business Lab at Yonsei University, Seoul, Korea. His research interests include Ontology, Semantic Web, Linked Data, and Semantic Web mining.
