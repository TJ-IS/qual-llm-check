---
otero_id: 25933
otero_key: "DMMW5FPA"
title: "Information retrieval and hypertext: competing technologies or complementary access methods"
authors: "Alan F Smeaton"
year: "1992"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1992.tb00077.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information retrieval and hypertext: competing technologies or complementary access methods

Alan F Smeaton

School of Computer Applications, Dublin City University, Glasnevin, Dublin 9, Ireland

Abstract. Information retrieval typically involves accessing textual information from a database in response to a user's vague information need. Hypertext or hypermedia, on the other hand, involves a user browsing through a database of textual or multimedia information in response to a variety of types of information need. Thus information retrieval can be said to have a searching metaphor while hypertext has a browsing analogy. Initially, these two technologies for information access appear to be very different, almost competitive in nature. In this paper information retrieval systems are briefly reviewed and hypertext systems are also examined. These two techniques for accessing information have been integrated into a prototype system which is described. The system dynamically generates guided tours in response to a user's query and the tour guides the user through the hypertext. Some experiments reporting on the effectiveness of this as an information access strategy are given.

Keywords: hypertext, information access methods, information retrieval, text retrieval.

## INTRODUCTION

Textual information in computer-readable format has become increasingly important and commonplace in organizations today. Currently we have documentation for all kinds of systems: office information such as memos and letters, electronic mail and authored texts such as reports, books, papers etc., all consisting of textual data and all available electronically in some format. However, despite the huge increase in the amount of text on computers there has not been a corresponding increase in interest in developing information systems to access effectively and to manipulate this information.

For many years we have seen the gradual development of information retrieval (IR) as a scientific discipline, originally operating on bibliographic data only and then expanding recently into other areas as more and more textual information becomes available in machine-readable form. In terms of functionality from a user's perspective, an IR system is used by inputting a query representation of a user's information need and examining a set or a list of texts selected by the system in response to the query, until the information need is satisfied. An iterative cycle may be used to refine the original query based on the generated output to 'home in' on relevant information.

The recent emergence of hypertext technology as a method for accessing information, including textual information, has meant that there is now an alternative to conventional information retrieval by computer. Hypertext is computer supported non-linear viewing of information where the reader can choose to view information in one of numerous orders of presentation. A hypertext information space is made up of a number of nodes or chunks of information which each represent independent and autonomous fragments of the overall context of the hypertext. The nodes can contain information in the form of text, audio, graphic, animation or other media. If text is the only media used it is usually referred to as a hypertext system; if other media are used the resulting system is referred to as hypermedia. Each node may be linked to a number of other nodes in the hypertext via specially authored information links. A user reads a hypertext by 'jumping' into the hypertext database wherever he or she likes and then browses from a node or a piece of information to other nodes until the original information need has been satisfied. This user-controlled browsing of an information space is very different from information retrieval functionality where the user actually has very little choice in the order presentation of the material unless he or she wishes to do another search.

These two metaphores for accessing textual information do indeed appear to be poles apart in terms of functionality. This paper gives a brief review of each of the two areas, but the main objective is to present an information model of a computer-based information system which combines the best features of hypertext and information retrieval systems and tries to combine the retrieval functionality of the two areas in some way. The next section of this paper reviews information retrieval and the subsequent section reviews hypertext systems. The assertion from these overviews is that it is necessary to combine the two functionalities and how this has been done elsewhere is the subject of the section on integration of IR and hypertext. The section entitled 'Information retrieval from hypertext in practice' presents an outline of a prototype information system we have developed which integrates hypertext and information retrieval functionalities and reports on some experiments which assess the effectiveness of this system for accessing information. The concluding section will then sum up the potential for future research in this domain.

## OVERVIEW OF INFORMATION RETRIEVAL

Information retrieval is concerned with the means of identifying, retrieving and/or ranking individual texts from a collection of texts which might be relevant to a given user query. This functionality is usually implemented by analysing the textual material (e.g. documents) into an internal representation or text-surrogate within the IR system. The retrieval operation thus involves turning the information need of the user into a query, turning that query into the internal representation form being used, and performing a match between the query and each of the text representations to quantify the degree of match between them.

In order to provide retrieval from texts, information retrieval has been divided into two separate processes: the indexing of text into the internal representation being used, and the subsequent retrieval operation on the text surrogates. There have been a number of different representation formats proposed and used for text and these are inevitably tied to the strategy being used during the ensuing retrieval operation. The indexing process itself can be done using statistical, knowledge-based or natural language processing techniques depending on the vocabulary or representation into which a text is being translated.

Of all the text representation formats available (Salton, 1989) the simplest would be to use the words that occur in the text or query with the stopwords or commonly occurring non-context-bearing words eliminated. A variation would be to use a restricted or a closed vocabulary and to use a mapping of all words into a subset of words: the restricted vocabulary. An enhancement of this approach would be to use word-stemming in indexing which reduces syntactic variants of a word into the common root form of the word. An even more sophisticated representation would be to use phrases or other context-bearing units from the text. Phrases could be normalized to eliminate syntactic variations so computer peripheral would be the normalized representation of texts which include the phrases peripherals from a computer or peripherals which are connected to a computer.

Once a collection of texts has been indexed in some way, the retrieval operation obviously depends on the indexing language used for documents and for queries. The text retrieval process is one which has been subjected to a lot of study over the years and a number of mathematical models have been derived to try and capture the essentials of the operation. These models have used vector spaces (Salton, 1989), probability theory (van Rijsbergen, 1979), and fuzzy set theory. Based on these models, a number of retrieval strategies have been defined.

Traditionally, there have been two approaches to retrieval in the most commonly used information retrieval systems: boolean retrieval and retrieval based on a vector space model. In boolean retrieval, a user specifies a boolean combination of keywords or phrases, linked using the logical AND, OR and NOT operators with perhaps an added word adjacency operator. The system retrieves a set of texts where the set is of indeterminate size a priori and where each text or document in the set exactly matches the specification in the query, and the system then presents the set to the user. In retrieval based on vector space modelling, a user gives a query as a list of terms, possibly derived from a natural language statement of information need, and the system matches the query against its representation for each text and ranks or sorts the texts in the collection based on the closeness of the match between the query representation and the representation for each document.

Besides the two main approaches to text retrieval there has also been work on retrieval using document clustering (Willett, 1988). More recent work in the area of document retrieval has tried to reduce the size of the vocabulary while preserving the document indexing using latent semantic indexing (Furnas et al., 1988) and there has also been interest in combining several distinct retrieval strategies into one single unified strategy using multiple sources of evidence.

These techniques are experimental at present but represent the trend and direction within the information retrieval community.

## OVERVIEW OF HYPERTEXT

In the last few years there has been a surge of interest in hypertext and hypermedia technology. This has covered the development of hypertext authoring and browsing tools, the tackling of problems inherent to hypertext technology like disorientation, the definition of formal models for hypertext information systems, the development of techniques for efficient implementation of systems and the evolution of different authoring strategies for hypertext databases. Hypertext is now maturing into a serious scientific discipline. There have been large international conferences on hypertext in Europe and the US as well as numerous national gatherings in most countries. Publications on hypertext research and practice are appearing in many forums related to information systems, and most importantly, there are now many information systems in use today which could be considered to be using hypertext ideas and technologies.

What hypertext systems provide that other information systems do not support is user-controlled browsing of an information space. This type of search and retrieval has many application areas and one of the most obvious of those application areas is in providing online documentation of a technical nature. Many computer manufacturers like DIGITAL, SUN, Hewlett Packard and Symbolics now ship documentation and manuals for their computer systems in machine readable format and provide hypertext-like browsing software to allow users to read it. Hypertext systems are also being used to provide access to reference material like dictionaries and encyclopaedias like the Oxford English Dictionary (Raymons & Tompa, 1988) which is now available on CD-ROM. Another application area of hypertext is within the field of software engineering. The ISHYS system under development at the University of Southern California (Garg & Scacchi, 1989) provides software hypertext where the nodes contain information related to the development and maintenance of a software system.

An important thing to infer from examples of hypertext applications is that the applications are for diverse classes of users ranging from software engineers to those browsing a reference source. The diversity of users itself is not important but what is important is that hypertext technology is serving a variety of types of information needs for different users. Some users may be seeking specific pieces of information like software engineers maintaining a system while others browsing through the Oxford English Dictionary or even an encyclopaedia in hypertext format may be following a single trail of related information. All these users use the hypertext in different ways because their information needs are different.

It is not surprising to see that one of the issues receiving a lot of attention recently is the question of turning existing machine-readable linear text into hypertext form. This conversion of text into hypertext using structural aspects of the linear text is easily facilitated if the original text is in some special mark-up format like SGML or ODA. Such conversion is supported by systems like IDEX (Ritchie, 1989) and the JUSTUS project at the University of Kent at Canterbury (Wilson, 1990) which is converting legal documents into hypertext using structural links from the original texts. The major problem with converting linear text into hypertext is with the judicious creation of the other semantic information links between nodes that makes hypertext information bases suitable for browsing. Structural links alone do not suffice for hypertext browsing by users and it is the automatic generation of these kinds of links that is posing such problems to researchers and developers. In reality, creating information links in a hypertext is a craft or a skill which at present is best acquired through practice.

Another one of the serious problems of hypertext technology is the overhead of the hypertext authoring process and this is a responsibility which receives little or no support from hypertext authoring tools. Creating a map or overall 'plan' is essential when creating hypertext documents as the overall structure of the hypertext will influence its usability and hence its effectiveness. The major difficulty in authoring hypertexts is not the creation of the contents of the nodes, nor the definition of anchors or link origins, nor the overall planning of the 'topography' of the hypertext and not the actual creation of the links, but the task of trying to do all these things at once! Hypertext authoring tools presently offer no support in the overall authoring proces.

The power of hypertext is that it allows users to browse through an information space until their information need is satisfied. But one of the consequences of allowing users to have such freedom of choice is that they quite often get 'lost in hyperspace' and become disoriented. Specifically, users ask 'Where am I?' and 'How do I get back to a node I know?' Manual linear documents provide orientation clues like thumbtabs, bookmarks, margin notes, etc. These clues have been included in some commercial hypertext systems like the Hypergate system (Bernstein, 1988) among others. More captivating orientation cues are based on the spatial presentation of the hyperspace as a two-dimensional map where the 'position' of nodes on the map is automatically computed by the system and presented on a screen to the users.

One of the more interesting ideas to emerge in recent work on hypertext has been the appearance of the notion of authored guided tours as part of the actual hypertext. Guided tours are being authored as part of the PERSEUS project (Mylonas & Heath, 1990) but the idea of guided tours was really developed by Trigg (1988). The way these tours work is that the author, in creating nodes and links, encodes a recommended path through the hypertext which the author feels a reader should take. Of course, the reader does not have to stick to the tour and can follow his or her own path as desired, returning to the tour whenever the reader desires. Guided tours have been proposed as a solution to the problem of user disorientation in hypertexts but the notion of a guided tour is something that can provide a vehicle for combining hypertext browsing and information retrieval searching.

For readers interested in a more detailed and comprehensive overview of hypertext the most cited paper in the field is probably by Conklin (1987). Nielsen has also published a book (Nielsen, 1990) which gives a gentle but thorough overview of hypertext topics, and this book seems set to become the standard reference in the field.

## INTEGRATION OF INFORMATION RETRIEVAL AND HYPERTEXT

There are few examples of work reported which really integrates information retrieval searching functionality into hypertext systems. In Frisse (1988) there is a description of the implementation of a popular medical handbook in hypertext format and an investigation into the necessity of information retrieval functionality within a hypertext system. Frisse develops a method for computing the 'best' hypertext node from which a user should begin a search based on the closeness of the node's contents to the user's query, plus the connectivity of the node, plus the similarity between the query and the connected nodes. Thus a measure of utility of a node is formulated in terms of the node itself and its immediate 'neighbourhood'. For reasons of computational tractability, this work computes the utility of a node as a function of the immediately linked nodes and no others. This approach does indeed go a long way to addressing the 'jumping into hyperspace' problem, but once the user has jumped in, Frisse's system cannot help any more.

Dunlop & van Rijsbergen (1991) propose a model for access to multi-media hypertexts and using a probabilistic information retrieval approach they generate a ranked list of starting points for a hypermedia browse to commence. However, as with the Frisse approach above, their technique does not help once the user has jumped into the hyperspace.

Coombs (1990) presents a statistical method for searching through hypertext thus providing information retrieval functionality. Coombs uses statistical ranking of the contents of nodes combined with simple linguistic processing, using the overall hypertext structure to limit the scope of the search. Like the work of Frisse, the Coombs approach does not help the user beyond providing start nodes for the browsing. Watters & Shepherd (1990) describe a model of hypertext which attempts to integrate hypertext and information retrieval functionality into one system. They propose the creation of a transient hypergraph on top of an existing hypertext which is created dynamically in response to a user query and lasts only for the duration of that query. Our criticism of this approach is that the links created in the resulting hypergraph are all created by the system and do not use any of the manually authored links of the hypertext in any way. We believe that this is a waste of carefully crafted information, which should be used by the system wherever possible.

Apart from the few examples discussed above, present hypertext systems and present information retrieval systems seem to have very little in common. Both provide access to information which can be of a textual or multimedia nature, in response to direct requests or queries from users. However, there the overlap seems to end. Information retrieval research has addressed issues like the representation of the query and of the text base and the concept of relevance of a document to a query, by using the idea of relevance feedback from users and then building a model of the users' information need. Hypertext research has concerned itself with issues of user disorientation, authoring strategies and converting linear text to hypertext.

Hypertext and information retrieval systems have evolved to satisfy different types of users. Hypertext has a browsing metaphor and its use easily facilitates that kind of searching although current hypertext systems are lacking in their ability to perform searches for specific information. They are also lacking in the way they help a user during their overall browse session. Information retrieval systems help users during a search by allowing them to express their initial information need in natural language, thereby allowing relevant feedback and dynamic query modification during searching. However, this searching metaphor does have the disadvantage that it constrains a user to keep searching for information on one topic until satisfied. If a user needs to search or even browse on a different topic during the first search then this can only be satisfied by allowing a subsequent and totally different search. It is not possible to browse through retrieved material in an information retrieval system as the IR system is too strict and narrow.

To sum up the situation: hypertext needs more searching and information retrieval needs more browsing. Hypertext technology is being used to provide information for a diverse set of users with assorted types of information needs. Every type of information need for every user has some elements of hypertext browsing and some elements of information retrieval searching. Between the two extremes there is a range of types of required information access. To date, information systems could be classified as either hypertext systems or information retrieval systems. Our contention is that if we look at the users' real information needs instead of what the current information systems actually provide, we will see that some combination of both types of information access is needed.

In order to integrate the functionality of a browsing system with the functionality of an information retrieval system, some model or basis for presenting this diversity of functionality as one unified mode of information access must be used. In hypertext we browse through an unordered network of information pieces. In information retrieval the system orders or sorts the required information for us. One approach to allowing a system to impose an ordering upon a hypertext is the idea of a guided tour.

Guided tours (Trigg, 1988) were mentioned earlier as a solution to the disorientation problem in hypertext where the hypertext authors plan a tour which users can follow if they so desire during browse time. However guided tours can also provide a vehicle by which the browsing metaphor of hypertext systems can be integrated with the searching metaphor of information retrieval by allowing the system to compute a guided tour dynamically in response to a user's query. Here a user would follow the tour of nodes, while still retaining, if desired, the flexibility of browsing in hypertext-fashion away from the system-generated tour.

Dynamically created guided tours in response to a user's query performs a search for a user but presents the results — the guided tour — as if it were a browse. This combines the advantages of hypertext browsing with IR searching into one information access mechanism. In order to find out how this idea would work in practice, we implemented a prototype system to create guided tours dynamically on a hypertext system. This system, and the preliminary evaluation of its effectiveness for information access, is described in the next section.

## INFORMATION RETRIEVAL FROM HYPERTEXT IN PRACTICE

The system described here which combines IR and hypertext functionality runs on a SUN4/390 SparcServer with the display appearing on SUN SparcStations or any X-terminal. It is written in C and uses the OPEN WINDOWS Graphical User Interface (SUN, 1990). The information associated with the hypertext needed to compute a tour, such as word frequencies and occurrences, is stored using the ORACLE relational DBMS. The hypertext itself consists of 462 nodes, all containing text information. Each node has an average of 500 words and the total text content is about 234 k characters, about the same as a small textbook. There are 1398 unidirectional information links and these are distributed among the nodes in a skewed fashion such that some nodes have only one link coming from them while others may have up to 10 or 12 (Smeaton, 1991).

The information content of the hypertext covers all the material used by undergraduate students attending a third-year course on databases. It covers the relational and other models of data, SQL, distributed databases, database machines, query optimization, catalogue management and other topics. Students can use the hypertext in addition to presented lectures and recommended textbooks in order to seek specific information (the syntax of the SQL CREATE TABLE statement for example) or to get more general overview information (like how does query optimization work). It is this latter type of information need that the guided tour mechanism specifically caters for.

There are three steps involved in the creation of a guided tour for a user. Users input a natural language statement of their information requirement and, using statistical IR techniques based on the vector space model, the system computes a measure of similarity S, between the user's query and the text of each node. This first step is based on comparing and counting the overlap of word stems in both query and nodes. Step two involves the calculation of a utility measure $U_{i}$ for each node in the hypertext. This utility weight for a node is given as the sum of the similarity weight for the node plus the averaged similarity weight for all nodes to which the node in question has information links. In mathematical terms,

$$
U _ {N o d e} = S _ {N o d e} + \frac {\sum_ {i \in C _ {N o d e}} S _ {i}}{| C _ {N o d e} |}
$$

where $C_{Node}$ is the set of all nodes with links from the node being considered. Thus in Figure 1, node A, which has three links to nodes B, C and D, has a similarity measure of 10 to the user's query, B has a similarity of 5, etc. Thus the utility weight for node A would be 13.

![](/api/attachments/DMMW5FPA/fulltext/images/fe720dcb80301f6f99209a870986cc983c0d82c8476298c578bd2ece3eaeb799.jpg)  
Figure 1. Sample calculation of a utility weight.

The final step in planning a tour is choosing the nodes based on the utility measures. We always begin the tour with the node which has the highest utility measure. To implement the rule for choosing the second and subsequent tour nodes a threshold utility value, T, is computed. After some experimentation it was found that a threshold value of one-third the utility value of the highest scored node in the hypertext performs best although this is something that could be user-controlled. The rule for choosing tour nodes after the first is to move from the current node to the connected or linked node with the highest utility value provided that value is not below T and that node has not already been seen by the user in the current session.

Figure 2 illustrates a small nine-node network or hypertext with nodes A–I and the utility value weights in parentheses. From this we can see that the highest scored node, A, has a utility score of 12, so the threshold value T is 4 and A is the first node on the tour. Node A is connected to nodes B, F and D and as D has the highest utility weight (9) the tour moves there. From D we could move to nodes B or E but both these have scores below T so we chose the next highest scored node in the network, excluding those we have already seen. This takes us to F with a score of 8. From F we go to G, then to H rather than D, then to C and at that point the guided tour ends.

The route-planning algorithm we have evolved is obviously based on local rather than global optimization. This approach is justified as the utility weight for each node is a function of what Frisse (1988) calls the 'intrinsic and extrinsic' properties of a node. This means that the weight for each node indicates the usefulness of that node and its immediate connections, which is important from the point of view of a user browsing through a hypertext. By the judicious design of the underlying DBMS schema favouring the calculations of a guided tour, the prototype system performs all the computations needed to generate a tour for a five-word query in 2 to 3 seconds of elapsed time.

![](/api/attachments/DMMW5FPA/fulltext/images/7dd8310ef31e86938f00c4ec087d1fe74c9c357fbd1d1ec5712ece35d645e48b.jpg)  
Figure 2. Sample hypertext network with utility scores.

In order to reduce the problem of users becoming disoriented in the hypertext, the prototype system includes a GO BACK button to return the user, recursively, to previously seen nodes, a bookmark facility to keep note of a chosen node and return to it at the click of a button, a browser map illustrating the neighbourhood of the currently displayed node, a breadcrumb which is displayed when any node is re-visited, a history list of the titles of all nodes visited during the current session, and a count of the number of guided tour nodes visited so far and the number still to be seen. As with manually constructed guided tours, a user can persist with the tour by pressing the tour icon, or can leave the tour at any stage to follow information links to other nodes and return to the tour at a later stage. Thus a dynamically constructed tour combines the browsing of a hypertext with the searching of an IR system.

To gauge the effectiveness of the tours being generated in terms of the relevance or usefulness of the nodes appearing on the tour, we asked nine users to input natural language queries from which tours were generated. These queries and the lengths of the generated tours are given in Table 1. We then asked each user to make a decision on the relevance or non-relevance of each node presented to them. The results of this evaluation are displayed in Appendix I.

Table 1. Sample queries and lengths of generated tours

<table><tr><td>User query</td><td>Tour length</td></tr><tr><td>Tables in the system catalogue</td><td>20</td></tr><tr><td>How to implement a database machine</td><td>28</td></tr><tr><td>Cursors as used with ESQL</td><td>20</td></tr><tr><td>Views as used in security</td><td>38</td></tr><tr><td>How to use foreign and primary keys</td><td>6</td></tr><tr><td>The network and hierarchical models</td><td>14</td></tr><tr><td>Three-level architecture: internal, external and conceptual levels</td><td>7</td></tr><tr><td>Query optimization</td><td>18</td></tr><tr><td>Security</td><td>16</td></tr></table>

In order to calculate precision and recall figures as used in conventional evaluation of IR systems (Salton, 1989) users would have to examine all nodes in the hypertext for relevance, but that is an option that was not available for this experiment and so these results can only be regarded as preliminary. Despite this they do indicate that a high percentage of the nodes seen are indeed relevant according to the users.

One interesting comment made by some users in the experiment was that when viewing a tour of nodes the relevance or usefulness of a node's information content varied depending on its position in the tour. For example, a node which gives an overview of the topic was found to be useful and hence marked as relevant if it appeared at the start of a tour, while it was less useful if it was in the middle or even at the end. This suggests that there is a natural order of presentation of hypertext information, or at least an order with which users feel comfortable. An extension of the basic hypertext model which is used in some domain-specific hypertext applications like co-operative work (Conklin & Begeman, 1988) and software engineering (Garg & Scacchi, 1989) is to allow the nodes and/or the information links to be typed or categorized. Ideally, any guided tour through a hypertext, constructed manually or automatically, should have introductory nodes and definitions followed by the information-bearing nodes and then followed by some overview or conclusion nodes. This would contribute to an improved overall interaction between the user and the material presented from the hypertext. If this could be done then the application areas for such an 'intelligent tour planner' would be places like computer-based training (CBT) and others where the users have a real information need which is satisfiable by the presentation of a set of nodes, instead of a browsing interest in information. Indeed, one could even go so far as to imagine an intelligent tour planner which also considers a user's profile or model on past searches of the hypertext or on a pre-search dialogue. Tours could also consist of planned multiple paths or cross-roads instead of the more usual one-path configurations.

If a hypertext information space has been built with the links and nodes typed, then that extends the richness of the representation of information in the hypertext and could be used to allow more effective retrieval and browsing. Typed hypertexts would also increase the possibilities for integrating information retrieval and hypertext functionality together by supporting intelligently planned guided tours. Planning such tours would be easier if the hypertext information space consisted of typed links and nodes but the disadvantage of typing links and nodes in a hypertext is the cost in terms of yet more cognitive pressure on hypertext authors. This is an area in which we are currently working.

## CONCLUSIONS

Two different types of existing information systems which can be used to operate on text data have been presented and discussed in this paper. Information retrieval systems rank text documents in response to a user's query based on statistical or other means. The retrieval model is of a user serially processing the output of the system's ranking, perhaps feeding back relevant information in order to allow the system dynamically to re-adjust the remaining ranking as this feedback information becomes available.

Hypertext systems use a network of text information nodes which have been linked together via specifically authored information links. A user poses a simple query to the hypertext system, usually a string to be searched for or a boolean combination of keywords, and the system responds with a set of possible start nodes for the user to begin to browse. The system displays a node and allows the user then to jump to one of a number of other nodes, following the authored information links.

From looking at these two kinds of systems in detail and examining the current trends and developments in the respective areas it is evident that these are two information-access methods serving users with two different types of information needs. There have already been several attempts at using information retrieval functionality within hypertext systems in general, but not in the area of combining the two functionalities together for retrieval or access. While each retrieval model has its merits and virtues, each is also lacking in some element of the functionality of the other. We have described a hybrid information system which not only combines but integrates hypertext browsing and information retrieval ranking and which serves a type of information requirement which is not currently satisfied wholly by either. A prototype system was described which generates a guided tour in response to a user's query and a preliminary evaluation of its effectiveness is given.

There is still much work to be done to exploit the features that a hypertext has fully in terms of typing of links and typing of nodes which could lead to a better overall guided tour. User profiles, relevance feedback on nodes during a browse, branching guided tours, nodes and other media besides text, are all possible areas for further work. Enlarging the hypertext used here in terms of its coverage and its size is obviously an important thing to be done in order more accurately to evaluate the quality of the generated tours. However, as other researchers have discovered, evaluating anything to do with hypertexts and their usage is an extremely difficult thing to do.

## REFERENCES

Bernstein, M. (1988) The Bookmark and the Compass: Orientation Tools for Hypertext Users. ACM SIGOIS Bulletin, 9, 34–45.

Conklin, J. (1987) Hypertext: An Introduction and Survey. IEEE Computer (September 1987), 17–41.

Conklin, J. & Begeman, M. (1988) gIBIS: A Hypertext Tool for Exploratory Policy Discussion. ACM Transactions on Office Information Systems, 6, 303–331.

Coombs, J.H. (1990) Hypertext, Full Text and Automatic Linking. In: Proceedings of the 13th International Conference on Research and Development in Information Retrieval. Vidick, J.-L. (ed.), pp. 83–96. Presses Universitaires de Bruxelles, Brussels, Belgium.

Dunlop, M. & van Rijsbergen, C.J. (1991) Access Methods for Non-Textual Documents. In: Proceedings of the International Conference on Multimedia Information Systems. Christodoulakis, S. and Narasimhalu, D. (eds), pp. 77–81. McGraw-Hill.

Frisse, M. (1988) Searching for Information on a Hypertext Medical Handbook. Communications of the ACM, 31, 881–886.

Furnas, G. W., Deerwester, S., Dumais, S. T., Landaur, T. K., Harshman, R. A., Streeter, L. A. & Lochbaum, K. E. (1988) Information Retrieval Using a Singular Value Decomposition Model of Latent Semantic Structure. In: Proceedings of the 11th International Conference on Research and Development in Information Retrieval. Chiaramella, Y. (ed.), pp. 465–480. Presses Universitaires de Grenoble, Grenoble, France.

Garg, P.K. & Scacchi, W. (1989) ISHYS: Designing an Intelligent Software Hypertext System. IEEE Expert (Autumn 1989), 52–63.

Mylonas, E. & Heath, S. (1990) Hypertext from the Data Point of View: Paths and Links in the Perseus Project. In: Hypertext: Concepts, Systems and Applications. Rizk, A., Streitz, N. & Andre, J. (eds), pp. 324–326. Cambridge University Press, Cambridge.

Nielsen, J. (1990) Hypertext and Hypermedia. Academic Press, London.

Raymonds, D.R. & Tompa, F.W. (1988) Hypertext and the New Oxford English Dictionary. Communications of the ACM, 31, 871–879.

Ritchie, I. (1989) Hypertext: Moving Towards Large Volumes. The Computer Journal, 32, 516–523.

Salton, G. (1989) Automatic Text Processing: The Transformation, Analysis and Retrieval of Information by Computer. Addison-Wesley, Reading, USA.

Smeaton, A.F. (1991) Using Hypertext for Computer Based Learning. Computers & Education, 17, 173–179.

SUN Microsystems, Inc. (1990) OPEN LOOK: Graphical User Interface Application Style Guidelines. Addison-Wesley, Reading, USA.

Trigg, R.H. (1988) Guided Tours and Tabletops: Tools for Communicating in a Hypertext Environment. ACM Transactions on Office Information Systems, 6, 398–414.

van Rijsbergen, C.J. (1979) Information Retrieval, 2nd edn. Butterworths, London.

Watters, C. & Shepherd, M.A. (1990) A Transient Hypergraph-Based Model for Data Access ACM Transactions on Information Systems, 8, 77–102.

Willett, P. (1988) Recent Trends in Hierarchic Document Clustering: A Critical Review. Information Processing and Management, 24, 577–598.

Wilson, E. (1990) Links and Structures in Hypertext Databases for Law. In: Hypertext: Concepts, Systems and Applications. Rizk, A., Streitz, N. & Andre, J. (eds), pp. 194–211. Cambridge University Press, Cambridge.

## Biography

City University where he teaches courses on Databases and Information Systems. He holds the MSc and PhD degrees in Computer Science from University College Dublin. His research interests include the application of natural language processing techniques to improving information retrieval quality, and the retrieval of textual information from hypertexts.

Alan F. Smeaton is a Senior Lecturer in Computing at Dublin

APPENDIX I. Results of the preliminary evaluation. Query 'X' = relevant; '.' = non-relevant.

1 XXXXXX..XXXXXXXX.XXXX

2 XXXXXXXX .... XXX .. XXXXX . XXXX .

3 XXXXXX.XXXXXXXXX..X

4 .... XX .... XXXXXX.... X ....... X ...

5 XXXX.X

6 XXX.XXXXXXXX..

7 XXXXXX

8 XXXXXXXXXX

9 XXXXXXXXX.XX...
