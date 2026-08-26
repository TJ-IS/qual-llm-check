---
otero_id: 23270
otero_key: "EJA47FCZ"
title: "Towards a Concept of Pure Information"
authors: "David Henley"
year: "1987"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1987.36"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards a Concept of Pure Information

David Henley

## Introduction

The information content of a database is normally identified in some way with the meaning of the data that can be retrieved from it. It is therefore specific to the given application area, and accordingly is referred to in this paper as applied information. But what is it that makes such information retrieval possible? Only certain sorts of data structure are complex enough to store a given quota of applied information. I call this complexity the pure information content of the relevant data model. The use of the term 'data model' here is slightly unorthodox and refers not to a schema such as in Figure 1 describing a database logically, but to the entire logical database itself, as shown in Figure 2. These remarks apply, of course, to other data models such as network or relational, as well as to the hierarchic example presented. In the course of the paper the discussion is generalized to arbitrary data structures.

## Applied information and pure information

Generally speaking, a database does not give information about its own structure but only about the things and events modelled. This could be more accurately expressed by saying that the database provides information only about its data values and not about how they are linked physically or where they are stored. As long as two databases compute the same associations of data, they will be viewed as holding the same information. Thus in defining the information in a database we are very much concerned with particular values of data and very little concerned with the navigation necessary to find them. When accessing an implementation, only a limited subset of the full range of possible processing is required, in order to generate the necessary logical associations. For example, consider this minuscule data model:

![](/api/attachments/EJA47FCZ/fulltext/images/2caadeb2424e000d9804089ab6ab206f1b156c7b5d0c8fccc88c1834f04ca288.jpg)

As nodes the two children cannot be distinguished — but we are only interested in their data. This data model might actually be stored using the following 'implementation':

![](/api/attachments/EJA47FCZ/fulltext/images/0a7607ec74f7ec5a97de683519db724e0f26099a2ec06f5e0e0afd933ce757a4.jpg)

Because of the data model, this structure is only ever processed in such a way as to ignore the sequence of the two children: the fact that one child comes before the other is regarded as an 'implementation detail'. Although this sequence does distinguish the two child nodes individually, the difference cannot be used to distinguish the two children themselves, because that would presuppose a different data model (that is, one describing a different situation, e.g. a bus queue). We see that the meaning of the implementation is determined by the limited kind of processing permitted by the data model.

The above example may be made more realistic by extending it to the whole database of Figure 2. A sequential implementation corresponding to the hierarchic data model is shown in Figure 3: here each new 'application' is prefixed by the special header 'A' and each child sub-record is prefixed by the special symbol 'C'. These two symbols (A and C) may be regarded as special kinds of data values used by the system and not retrieved by the user. I call such values parametric data or just parameters; parametric data do not constitute part of the information in the database but, like the links and nodes themselves, contribute only to its structure.

So the information in any database is given by the processing defined on its data model. We can see that there is a tendency for 'random' accessing in the model to give rise to sequential processing in the implementation. Now the same data model can be implemented in many different ways, for example the hierarchic model leads to both a sequential implementation and to a master file, or less directly to a relational database or a network database. In each case we can say that the meaning of the implementation is given by the data model. Each implementation, by means of a restricted range of processing, generates all the information defined by its data model. This information is, of course, precisely the information contained in the database.

![](/api/attachments/EJA47FCZ/fulltext/images/a5d19c0b60ad89cc3aa4b8ab34dcef54e28e790d5630bb80c98201668a9cf527.jpg)  
Figure 1. A hierarchic schema

![](/api/attachments/EJA47FCZ/fulltext/images/a46433a1285b94e1f3753d9f5a43831a52ddff28991254c3cc2d9e0bf5a0087a.jpg)  
Figure 2. A hierarchic data model\*

![](/api/attachments/EJA47FCZ/fulltext/images/c5c6fb576c27c6e381341253be931a2a374097fc5dff0df31ef44930d202f63f.jpg)  
Figure 3. A sequential implementation of the database

For a given physical database one can ask whether it has been implemented correctly (i.e. whether it is an adequate encoding of the intended data model). Faulty parameters may have been entered at DBMS initiation, or there may be an error in the DBMS software itself; in either of these cases we would not have a valid implementation. But there is a more fundamental question — whether it was even possible for the data model to be implemented in that way. What is in common between all possible implementations? What is the definition of an implementation? A hierarchic data model can be implemented sequentially, but what happens if we reverse the roles of data model and implementation? Considering the sequential data structure of Figure 3 as a data model we see that the hierarchic structure of Figure 2 could not possibly be viewed as an implementation of it — there would be a loss of information. For example, no clue is given in Figure 2 as to the strict sequence of the different households, nor of the fact that information about James comes before information about Mary. We would say that Figure 3 contains more information than Figure 2; that is why the former can be an implementation of the latter but not vice versa.

We are now using ‘information’ in a completely different way, for certainly there is exactly the same information about the various welfare applications in both the data model and the implementation. What we are discussing now is not information about parents and children, but information about the database itself; not the meaning of the data, but its structure. And one inference we seem to have drawn is that where one data structure contains a sequence that is not present in the other, then this indicates that the second structure contains less information, in our new sense, than the first. Let us distinguish between these two kinds of information as follows. We refer to the external meaning of the data as the applied information in the database — this is what one usually understands by information. But then the structural information, because it tells us nothing about the application, can be referred to as the pure information content of the database.

We have already seen that the applied information in a database tells us little about its structure, since this was not its intention. Similarly the pure information in a data structure tells us little about its intended meaning. However, there is one connection we can establish, and that is that the pure information in an implementation must have the capacity to support the desired meaning. If the implementation were too simplistic the necessary application processing would not be possible. If, for instance, one of the hierarchic trees in Figure 2 were 'implemented' by a structure in which all nodes radiated from a common central node, one would not be able to identify which age belonged to which child or which salary belonged to which parent. Thus the applied information presupposes a minimum level of structural richness or complexity, i.e. a certain minimum of pure information — not that such information can be measured numerically, but it does seem to correspond with some absolute criterion of simplicity and complexity.

So the pure information is basic to a database in this sense: that it determines the possibility of the database conveying its applied information, of conveying the desired meaning. Not every data structure containing pure information also contains applied information (i.e. not every data structure is a database). If, for example, the input parameters to a complex program are structured for ease of processing, then this parametric data is not a database, nor indeed is the program itself. These are not databases because we do not search for parameters satisfying a certain criterion and we do not generally search for individual characters in a program listing. In any case these parameters and characters may not denote observed values of any kind - i.e. they are not 'applied' data. Nevertheless each of these data structures contains pure information because each has the possibility of being implemented in different ways: for example, a nested character-string might be held as a binary tree. In each case the representation would have at least as much pure information as the original structure.

I should now like to consider an example which might be thought of as a hybrid between the two extremes of a database on the one hand, and a parameter structure on the other. A matrix of numbers and letters conveying a coded message can be converted into an ordinary sentence by suitable manipulations. Does the matrix contain applied information? Not explicitly; it masks a natural sentence which has an informal applied meaning, but it cannot be regarded as a database. As a matrix of characters, however, it possesses pure information in perfectly explicit terms. In keeping with our terminology, therefore, we should have to say that the characters in the matrix constitute parametric data, rather than applied data. Of course parametric structures arise all the time in computational processes, namely at the many intermediate stages on the route between input and output (inside the computer).

So in the case of coded messages we do not have a database of characters; rather it is the whole structure that provides the meaning ('the medium is the message') by its facility to be converted into another form - i.e. by means of its pure, rather than its applied, information. Consider a data structure containing both parametric and applied data, such as in Figure 3. In a structure such as this we can usefully distinguish the properties of the pure, as opposed to the applied, information. From the point of view of the applied information the sequential order of children of the same parent is not relevant, nor are the parameters A, C and their relative positions. All that matters are the computable sets of applied data.

From the viewpoint of pure information, however, it is the applied data which are irrelevant, because none of these affect the ways in which the structure can be converted into other structures. If Figure 3 were converted into the hierarchic data model of Figure 2, as it easily could be (albeit with an accompanying loss of pure information), then this process would be undertaken by completely ignoring all the individual data values. There would be some data which would not be ignored, however, and those are the parametric values A and C, for these are vital in determining where a sub-tree starts and ends. Implementations, and file conversions generally, do not attend to specific data values in particular records but employ a perfectly general program which treats all records equally. Thus, another way of expressing the above contrast would be to say that the information in a database from the point of view of implementation is a very different thing from its information as regards interrogation.

It can be seen, therefore, that although it is the pure information that makes a given level of applied information possible, nevertheless these two concepts are defined quite independently. The pure information in a database would be the same whatever data was held in the particular fields, just as long as the fields remained the same. To investigate the former a database might just as well be regarded as completely empty of data, except for the parametric values which define the structure. Just as we think of the applied information as independent of local structure, so we might think of the pure information as data independent.

It is a peculiar thing to think of the information in a database as independent of its data, no matter what the level of analysis, and yet we see that it is so, because the graph structure of a database is linked only incidentally to the particular data which gave rise to it. Nevertheless, without that structure no data access could take place and there could be no applied information. And with a degraded structure there would be correspondingly degraded applied information – logical associations between data can only be maintained if physical associations are maintained. Thus the applied (structure independent) information content presupposes the pure (data independent) information content.

As a case in point, the sequence of children for a given parent implements the logical associations (with no sequence) because the former has more pure information than the latter. But if there were no physical connections between the parent and his children at all, then there would be no logical associations either – this is because there is now less pure information. Thus the data model itself must have a certain minimum of structure in order to support its own ‘structure-free’ operations. We have seen that these operations represent a somewhat limited range, among all the processing that is possible. Let us surmise, for the time being, that it is the full range of processing that defines, after all, the pure information. This, then, justifies our assertion that pure information is a prerequisite for applied information – because the former is defined by a programming language of which the latter conforms to only one part.

In considering the nature of pure information the various structures will be for the most part empty of data, with the exception of structural parameters.

## The concept of pure information

This notion that we have touched upon – that there is a structural concept of information independent of any particular meaning, but representing the capacity to express all meaning – is one that is extremely subtle. It leads to deep and probing questions, with unexpected consequences. However, in this paper we shall consider only the very simplest of its manifestations. From now on the word ‘information’ should be taken to mean pure information.

If a television picture is given by a stream of colour data (R = red, G = green, Y = yellow)

$$
\texttt {R G G Y R R Y G R R R}\tag{1}
$$

then mapping green and red to black (B) and yellow to white (W) implies a loss of information:

## B B B W B B W B B B B

(2)

There is now reduced information about the scene being transmitted (we do not know what colour it is) - i.e. a loss of applied information. However, this data stream is not so much a database as a coded message, and we may therefore view the data as constitutive of the structure, i.e as parametric (this means we cannot ignore the values of the data). Consequently this is really a structural loss; there is a loss of pure information. It is easy to see why - a computer program attempting to build the former string (1) from the latter string (2) would have an impossible task, without importing the additional information as to which Bs mean R and which Bs mean G, from outside. If that were to happen then the data stream (2) would no longer be explicit: it would no longer claim to tell the whole story and would have to be viewed as only part of some larger signal. Leaving this possibility aside and treating (2) as the whole signal, we see that the process is one-directional: we can go from (1) to (2) but not from (2) to (1). Any computer program effecting such a transformation must surely only be of a certain limited type, for it certainly cannot be the type of program that contains within itself some arbitrary decisions as to which Bs are R and which Bs are G, either by means of its own structure or by a stored table.

Information is lost in exactly this manner when a colour TV picture is converted to black and white – there is no machine that can possibly be built which will re-obtain the colour picture. The most that can be done is to produce a simulated effect: i.e. to 'guess' what the original colours were. But this is a remarkable assertion because what we have done is made a law about all machines – those which exist and those yet to come – to the effect that they cannot create information out of nothing.

Similarly, if (1) did represent a logical database or data model, then (2) could not be an implementation of it because it is unable to make all the necessary distinctions: (1) is a structure altogether too 'rich' to be summed up by the simplicity of (2). When we say that (2) cannot make the distinctions necessary to (1) we are making a statement about all possible algorithms - we are saying that no algorithm can be devised which will transform (2) into (1): this really tells us something about what we mean by an 'algorithm'.

It thus appears that data structures have, locked within them, some sort of algorithmic potential, i.e. the potential to represent other structures by means of an algorithm. I have hinted that not every possible algorithm is relevant here; those which contribute information of their own, or from other structures, should be excluded. It is for this reason that I use the word (semantic) 'rule' to describe the kind of transformation that allows one data structure to be converted into another data structure without adding any information from outside. These concepts are all correlative and, at this stage, the above remarks may all seem hopelessly vague; however I promise greater clarity will emerge as the development proceeds.

The ‘algorithmic potential’ of a data structure is, of course, its pure information content; where a rule exists to generate structure $D_{2}$ from structure $D_{1}$ but not vice versa, we say that $D_{2}$ contains less information than $D_{1}$ or that there has been a loss of information in making the transformation. This is a situation that occurs all the time in data processing; indeed it is inconceivable to imagine a data processing industry without it. For whenever a computer program takes a given input and generates a corresponding output there is a tendency towards information reduction. If, for example, the program selects information from a database and prints it out as a listing, then there will generally be considerably less information in the output than in the input. Needless to say, the process is irreversible; the database could not be generated from the printout. If the processing was the result of a user query it would be a mistake to identify the input with the query; we must include all data accessed by the program — and that embraces the entire database.

However, this analysis is quite superficial for we have yet to say what kind of processing is admissible; we will need eventually to define the kind of program that does not artificially contribute information of its own, and that will require a precise definition of a 'rule'. It is only then that we can adequately define what we mean by pure information. If we call two data structures equivalent if they contain the same information, this means that each structure is capable of generating the other by means of a rule. This then gives us the definition of the pure information contained in a structure D; it is that which is in common between all data structures equivalent to D. Once we have a precise definition of 'rule' we will also have a precise definition of information. This will involve, among other things, specifying the semantics of a programming language in which all possible rules can be written. Thus, the 'algorithmic potential' of a data structure is a linguistic potential; it is a measure of its ability to be acted upon by a programming language. This is the basic connection between language and pure information.

However, it is perhaps possible to indicate what I mean by a rule, in a preliminary fashion. Figure 4 illustrates a 'pyramid' data structure which is mapped into a sequential vector in two different ways. In (a) the nodes are mapped systematically on to the vector by starting at the apex and filtering down the pyramid one row at a time, moving from left to right along the vector. This narrative description gives the basis of a formal program which would do the same thing. In the case of (b) no such narrative exists and the only way to define the mapping is to set up a list of random associations such as:

![](/api/attachments/EJA47FCZ/fulltext/images/4cd5bcdf9fe40212e2417998060d0198d369b3be6475209b50ca1eb1c80e7f53.jpg)  
Figure 4. Random and general rule mappings

'map P1 to V2'

I call such a mapping a 'random mapping'. It is important to realize that although this concept will be defined by a particular language, it is not really confined to any particular syntax. The difference is one of referring to individual nodes directly, as opposed to referring to them indirectly and never mentioning them by name. The latter has the all-important asset of generality, while the former does not; it is generality which is the hallmark of a rule.

We can see that a rule is general because in a well-defined sense we can treat every node alike, without picking and choosing between different nodes for no apparent reason, and what this means, simply, is that we can execute the same program code at each and every node. What makes the mapping rule-governed rather than random, is the fact that there is a suitable language in which such program code exists. The language in which such programs are written, which defines this characteristic called 'generality', cannot be unique in any trivial sense, for it will be observed that this characteristic was retained too, when the mappings were defined in natural language. And it is this language characteristic, also, that will ultimately provide a definition of information.

Returning now to the data stream for the television picture; since there were 11 nodes, the empty storage structure will be called the vector $V_{11}$ . We have seen essentially that a rule which merges different data values while leaving the structure intact produces an information loss. Is the same true if we alter the structure but keep the data the same? Imagine the string (2), but with the last node missing,

## B B B W B B W B B B

(3)

then how are we to know what the last node should have been? How are we to reconstruct (2)? Again we have a loss of information; the string is identical in all other respects except for being a $V_{10}$ instead of a $V_{11}$ . Likewise, if we attach an extra node to (2) somewhere in the middle:

## B B B W B B W B B B B |  B

(4)

then there is nothing in the structure of (2) to indicate where this might take place, so no perfectly general program could construct (4) from (2) and so (4) could not be the meaning of (2) under any language system. Normally, programs do not preserve information; the usual situation is information loss. Exceptions are simple reformatting on the one hand, and large file conversion routines on the other hand. When information has been maintained we generally say that one of the structures is just an encoding of the other. Just as each of the structures may be considered the output from the other as input, or both may be seen as expressing the same applied meaning, so one structure may be considered the secret message encoded by the other.

Thus, in Figure 4 any data stored in the pyramid could be encoded in the vector by mapping (a), but not by mapping (b). The latter would irretrievably scramble the message and no amount of ingenuity could decipher it. And in the examples just examined, the message (1) could not possibly be encoded in the signal (2) — unless by random means, in which case it would be impossible to decipher. The random 'key' or code book would constitute additional information not contained in the message itself (just like the stored table envisaged earlier) which the receiver would need to be aware of. By the same token (3) could not encode (2), but (2)

could encode (3) as its meaning – this would just be a code in which the last symbol, like a full stop, was not part of the message and could be safely ignored. In this context the word 'code' plays the same part as semantic 'rule' or 'computer program'. We might say that equivalent structures can convey the same applied meaning.

The original question over the alternative implementations of a given data model may now be rephrased somewhat differently. In more general form, for any pair of data structures $D_{1}$ , $D_{2}$ the question becomes whether it is always possible to find a mode of representation (a rule) so that the meaning expressed by $D_{1}$ can also be expressed by $D_{2}$ . The answer, from the examples we have considered, is clearly 'no' — if we understand the relationship of meaning to emanate entirely from the structures themselves and not something arbitrarily designated from outside the two structures (i.e. $D_{1}$ , $D_{2}$ are both explicit). For, in certain cases, there is simply not enough information in the sign for it to convey the requisite meaning; for it to encode the desired message. And the concept of encoding I have suggested consists of rules taking a certain form. This, and the notion of information itself, will be analysed and refined in what follows. We shall be concerned not with whether one structure means another structure under a given scheme of interpretation, but whether it is even possible for an interpretation to exist whereby one structure can express the meaning of the other structure.

Before proceeding further, however, this is perhaps the right moment to give formal definitions of what I mean by 'data structure'.

## Definitions

The following definitions will be used at various points throughout:

## Definition 1

A storage structure is any finite set of storage cells (henceforward referred to as nodes), together with a set of links allowing access from one node to another. The links are classified into various types denoting the different kinds of access which are possible. Only one link of a given type can point from one node to another. In this paper, nodes are always drawn as circles, and links as labelled arrows between them. This then forms a sort of canonical notation or archetypal formula on paper, for storage structures, regarded as syntactic objects. In short, a storage structure is a directed graph with labelled links but unlabelled nodes. We may define storage structures in terms of sets and relations as follows:

Let N be the set of nodes. Then the cartesian product N x N is the set of all possible ordered pairs of these nodes. A set of arrows bearing label R is a binary relation on N - i.e. any subset R ⊆ N x N. Let Γ be any set of such relations. Then a storage structure may be defined by the pair <N, Γ>.

If we also stipulate that for every pair of nodes in N there is a path of links $R_{i} \in \Gamma$ holding between them, then we ensure that the storage structure is strongly connected (unlike a data model).

Next we can define a data structure as an equivalence relation over a storage structure. First of all, an equivalence relation can be defined as a binary relation E having all the following properties:

1. E is reflexive, i.e. $\mathbf{E}(x,x)$ for every x.

2. E is symmetric, i.e. $\mathrm{E}(x,y)$ implies $\mathrm{E}(y,x)$ .

3. E is transitive, i.e. $\mathrm{E}(x,y)$ and $\mathrm{E}(y,z)$ implies $\mathrm{E}(x,z)$ .

Any such relation defined on a set N divides the set into non-intersecting classes. This is exactly what we need to define data structures because each data value can be identified with one of these classes.

## Definition 2

(a) A data structure is a triple $<\mathrm{N}, \Gamma, \mathrm{E}>$ where $<\mathrm{N}, \Gamma>$ is a storage structure, and E is any equivalence relation over N; alternatively,

(b) A data structure is a quadruple $<\mathbf{N}, \Gamma, \mathbf{D}, \phi>$ where, if the number of nodes in $\mathbf{N}$ is $\mathbf{n}$ , then $\mathbf{D}$ is a set containing $\leqslant n$ data values and $\mathbf{C}$ is a content-function $\mathbf{C}: \mathbf{N} \longrightarrow \mathbf{D}$ mapping each node to a unique data value.

What does isomorphism mean with regard to data structures? No abstraction is necessary to define the property to be preserved; the symbol is abstract already and defines its own structure.

## Definition 3

Two data structures

$$
\mathbf {D} = <   \mathbf {N}, \Gamma , \mathbf {E} >
$$

$$
\mathbf {D} ^ {\prime} = <   \mathbf {N} ^ {\prime}, \dot {\boldsymbol {\Gamma}} ^ {\prime}, \mathbf {E} ^ {\prime} >
$$

are said to be isomorphic if mappings $\phi_{N}$ , $\phi_{\Gamma}$ exist such that:

(a) $\phi_N: \mathbf{N} \longrightarrow \mathbf{N}'$ is a one/one correspondence

(b) $\phi_{\Gamma}:\Gamma \longrightarrow \Gamma^{\prime}$ such that for every $\mathbb{R}\in \Gamma$

$$
(x, y) \in \mathrm{R} \Leftrightarrow (\phi_ {N} (x), \phi_ {N} (y)) \in \phi_ {\Gamma} (\mathrm{R})
$$

(c) $(x, y) \in \mathrm{E} \Leftrightarrow (\phi_{N}(x), \phi_{N}(y)) \in \mathrm{E}^{r}$

Thus, D, D' are essentially the same data structure but with different names. The definition says that to every label of link in D there is a corresponding label of link in D', which connects corresponding nodes.

To illustrate that the definition is not entirely trivial, the example in Figure 5 shows two different structures on the same set of nodes $\{1,2,3,4,5\}$ .

(a) $\phi_N$ is defined by

<table><tr><td>x</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td> $\phi_{N}(x)$ </td><td>1</td><td>4</td><td>5</td><td>2</td><td>3</td></tr></table>

(b)

(a)

<table><tr><td>R</td><td>f</td><td>g</td></tr><tr><td> $\phi_{\Gamma}(R)$ </td><td>g</td><td>f</td></tr></table>

where f, g are defined by the diagram.

(c) There is no data so $E' = E = N \times N$ .

To see this in an isomorphism check any of the links, e.g.

$$
\begin{array}{l} \text {In (a) (2, 3)} \epsilon g \Rightarrow (\phi_ {N} (2), \phi_ {N} (3)) \epsilon \phi_ {\Gamma} (g) \\ \text {because (4, 5)} \epsilon f \text {in (b)} \\ \text {In (a) (1, 4)} \epsilon f \Rightarrow (\phi_ {N} (1), \phi_ {N} (4)) \epsilon \phi_ {\Gamma} (f) \\ \text {because (1, 2)} \epsilon g \text {in (b)} \end{array}
$$

(b)

Of course more abstract properties may be preserved, and so there can be more abstract forms of isomorphism.

How do these technical definitions relate to questions of information? In the first instance we shall see that isomorphism is far too strict a requirement for information equivalence.

## Equivalent structures

Data structures which contain the same pure information can look bewilderingly different; there is a great variety and range of ways in which, say, the results of a questionnaire could be held in a computer. And yet, while these alternatives would contain the same applied information, they would not necessarily have the same pure information. Various database implementations are unlikely to be equivalent in this sense, although they may be. Of course this would not be the point at issue when undertaking the conversion of, for example, a relational database into a network database – the only question here is whether the applied information is preserved. The structural or pure information would demand that every pointer and every sequence was rigorously translated into an analogous form, a far more exacting requirement.

A practical situation in which pure information is of importance, however, is when a compiler translates a source program into an object program. Here every structural aspect of the object code (such as the nesting of loops) must have resulted from a corresponding feature of the source program. Superficially, however, the two structures will look wildly different — in fact it is highly improbable that there will be any structural attribute in common between the two, apart from the fact that one could be obtained from the other by means of a complex rule. The representation is an indirect one; the source program indirectly represents the object program because there is no isomorphism, however abstract, which is capable of defining the relationship between them. Of course, the object program does not represent the source program without ambiguity, as several source programs may compile down into the same object code; it is a many/one relationship. For this reason the two structures are not equivalent and the compiler loses information; the vital program logic is not lost, of course, just the decorative syntax of the source code. However, from a technical viewpoint this still counts as an information loss.

![](/api/attachments/EJA47FCZ/fulltext/images/53fa2022aedf3f152ca9b00f2a8dfe39a2fca1effafb6c173aff5aee659bdaf6.jpg)  
Figure 5. Isomorphic structures

But could there not be a sense we might attach to saying there is, after all, a similarity between the two structures? As we look at the uncompiled listing and the compiled listing, can we gain no inkling of a connection between them? Certainly if it was within our mental powers to imitate the action of a compiler we could verify the compilation by computation; but could we not, simply by casting our eye over the two listings, perceive any similarities? Certainly anything we observe cannot be inherent in the listings alone, as we have just noted that no isomorphism exists; the only connection between the structures is the existence of a rule to convert one into the other. How is this compatible with observing a similarity? Is it not possible that we have an ability to observe rules, without knowing them explicitly but in some sense seeing the symptoms, the tell-tale marks, of a rule? If this were true then we could observe a similarity between two data structures where, so to speak, none exists. Rules are formulated in a language, and language is something we all possess, so what we would be seeing are the manifestations, the distinctive marks, of language.

In this way we might be said to perceive the pure information in data structures, just as we perceive applied information. Indeed if we were not supplied with an application then that is all we could see. For two equivalent structures it might, in this way, be possible to perceive in the data graph of each structure the potentiality for representing the other, without the actuality of a representation.

Obviously compilation listings are colossal data structures to analyse; to examine these suggestions systematically it will be more helpful initially to consider only the very simplest of data structures. And naturally enough, in order to explore the above hypothesis, we shall not be comparing data structures by executing detailed programs on them; we shall be comparing them intuitively, but noting what reveals itself to careful inspection.

## Notation

Data structure diagrams will from now on be shown in various abbreviated forms, not out of laziness on my part but for the sake of greater clarity. For example, when two nodes are linked by an undirected line, this is a shorthand for a pair of links $f, f^{-1}$ one pointing forward, the other pointing backward, i.e.

![](/api/attachments/EJA47FCZ/fulltext/images/55832eddbd12d83cdf50b78ceafa9131afb75d5fe0c5943ec887a8aa682a216f.jpg)

or

![](/api/attachments/EJA47FCZ/fulltext/images/0f2bf20a74ead7161d5162cfee1f467b114c2519187fbaaff195f01c7d2ecbb1.jpg)

Moreover, when all the directed links in a structure are unlabelled, this is taken to mean they all have the same label, say f. Thus, for example,

![](/api/attachments/EJA47FCZ/fulltext/images/a0f8438200fbd3bf5a910cab94ac4a27bb8c4984460f27d739d9d56441df1ea2.jpg)

![](/api/attachments/EJA47FCZ/fulltext/images/07acf6475aab63dfb02c136335290079a35d20416f2c4da21adf9b6fd165aed5.jpg)

Just as when all the nodes are empty this is equivalent to a structure in which they all contain the same data value, for example:

![](/api/attachments/EJA47FCZ/fulltext/images/31d3b1ad52b28e15ba4ec705eb20e94a808433d69798f39a3273bb5765280580.jpg)

If only one of the nodes is marked with a value, it is assumed that all the other nodes are the same as each other, thus:

![](/api/attachments/EJA47FCZ/fulltext/images/15e041d9fb017cc7b795d5fcc5216fa24083f6667b7bb975b443dd7a349b5f5b.jpg)

Of course, unlabelled links are subject to no such generalization because while one can have two or more labelled links between the same two nodes:

![](/api/attachments/EJA47FCZ/fulltext/images/420a3511066feaf9912a1fe46200eb68ff655cc267966c7f718edb82faa7ddef.jpg)

if they were unlabelled, no distinction could be drawn between them. If a structure contains only undirected links which are unlabelled, thus:

![](/api/attachments/EJA47FCZ/fulltext/images/f12b9936331db41267d9e77fd88884ec685874e56d0b6f6d7e70bfd251c18b5f.jpg)

then this is taken to mean that there are two chains of links $f, f^{-1}$ and that either the labelling of these chains can be inferred from context

![](/api/attachments/EJA47FCZ/fulltext/images/b10e2daee1c04def0242799fcaa70c9cb148306bcae8ba237113ffa2c5bfdc22.jpg)

or that the labelling is irrelevant to the example being given and the statements being made.

Sometimes a tabulation is used, such as:

<table><tr><td>X</td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Y</td><td></td><td>A</td><td>B</td><td>A</td><td>C</td><td>B</td></tr></table>

and this is meant to be interpreted as the pure structure:

![](/api/attachments/EJA47FCZ/fulltext/images/a9fa9155c7d2d6c43591cc30be6b8eedcfea3b49e558896d0a8663bdb11ae84a.jpg)

for it is frequently the case, in data processing, that data is assembled into rectangular tables and it saves essential duplication if the above transition can be taken as understood rather than made explicit each time. Moreover a simple vector like:

![](/api/attachments/EJA47FCZ/fulltext/images/5c8f25ff711de5bfc102f8246b6f035d462883fd2bddcbbac740750bfd52245f.jpg)

may often be written simply as:

## A B B A B

both of which really mean:

$$
ⓐ \xrightarrow [ f ^ {- 1} ]{f} Ⓑ \xleftarrow [ f ^ {- 1} ]{f} Ⓑ \xleftarrow [ f ^ {- 1} ]{f} Ⓐ A \xleftarrow [ f ^ {- 1} ]{f}
$$

For structures A, B when B contains at least as much information as A we write:

$$
\mathrm{B} \geqslant \mathrm{A}
$$

When A, B are equivalent we write:

$$
\mathrm{A} \equiv \mathrm{B}
$$

Thus $\mathrm{A} \equiv \mathrm{B}$ if and only if $\mathrm{A} \leqslant \mathrm{B}$ and $\mathrm{B} \leqslant \mathrm{A}$ .

If B has more information than A but A, B are inequivalent we write:

$$
\mathrm{B} > \mathrm{A}
$$

If A, B are inequivalent we write:

$$
\mathrm{A} \not \equiv \mathrm{B}
$$

Thus A ≠ B if A > B or B > A,

but also if A, B are independent.

We write IND(A, B) if A, B are independent, i.e. IND(A, B) if and only if

$$
\mathrm{A} \geqslant \mathrm{B} \text {   and   } \mathrm{B} \geqslant \mathrm{A}.
$$

Notice that A > B means that A can represent B but B cannot represent A. IND(A, B) means neither can represent the other but with A ≠ B it is possible that one could represent the other.

Notice that if IND(A, B) then we would expect for any other representation A', B' of A, B respectively, that these also would be independent, i.e. IND(A', B') more formally:

$$
\operatorname{IND} (\mathrm{A}, \mathrm{B}) \& \mathrm{A} \equiv \mathrm{A} ^ {\prime} \& \mathrm{B} \equiv \mathrm{B} ^ {\prime} \Rightarrow \operatorname{IND} (\mathrm{A} ^ {\prime}, \mathrm{B} ^ {\prime}).
$$

## Intuitive examples

There are certain standard methods by which any structure may be represented; yet although these are standard encodings there is not the slightest resemblance between the structure and its coded form.

First a slightly artificial example, but one which is of historical relevance to relational databases. In 1900, Bertrand Russell published a paper entitled 'The Logic of Relations' which was to lead on (with A.N. Whitehead) to 'Principia Mathematica' and the development of predicate logic. From our point of view, every data structure can be described as a collection of relations (a binary relation for each type of link) and so can be viewed in tabular form — as a relational database, in fact.

Referring to Figure 6, we see that the original structure (a) could be stored as a series of 'records' as shown in (b). Here the data values are names of the actual nodes in (a) and each row or record says that the node on the left is linked to the node on the right. This is the typical form of representation envisaged by logic — the table would be described as a relation (i.e. a set of 'ordered pairs' of data values). However, as we have seen, relations are just one form of representation among many.

They do, however, possess an interesting feature that was at one time considered philosophically fundamental, namely that all the data values in one data structure stand for nodes in the other data structure. It was felt by Russell, Wittgenstein (although not in his later work), and others that the act of naming was basic to all forms of representation; if it has not become evident already we shall soon show that this is by no means the case. Notice here that the data (the 'names') are all parametric, i.e. part of the structure.

The table in Figure 6(b) is not in the notation we have adopted for data structures and might be more explicitly presented as at (c). Notice the link $f$ here corresponds exactly to the $f$ in (a). Now the question is, does the structure in (c) contain the same information as (a) - are they equivalent? The answer is 'no'. Certainly the information as to the structure of (a) is all available inside (c) and from it (a) may easily be reconstituted. (Russell might have said that (c) is simply a description of (a) just like the formula $f(1,2) \& f(3,4) \& \ldots$ ) But the fact is that (c) contains more information than (a) because the ordering of the pairs (1, 2), (3, 4) etc in a series is nowhere given in the structure (a). I have listed the pairs in an arbitrary order and there is nothing in (a) to determine this. The pairs could have been listed in a different order and have represented (a) equally well (just as the components in the conjunction $f(1,2) \& f(3,4) \& \ldots \& f(5,3)$ could have been rearranged and still provided an equally true description).

Thus we can see that although (c) can represent (a), there is not sufficient information in (a) for it to represent (c). This means that there is no rule which can be applied to (a) to generate (c); (a) cannot be viewed as containing the coded message (c) — not just under one particular encoding but in all coding schemes whatsoever.

All that is necessary to represent (a) is a set of ordered pairs, but the astute reader will probably have noticed that a set of ordered pairs is not, properly speaking, a data structure at all. The whole notion of a 'set' is an abstraction which presupposes no particular ordering for its elements. Since, in many cases of practical information retrieval, the precise ordering of the records in a file is immaterial, the idea of a set has sometimes been found to be a useful one for database design. However, the fact remains that every file is stored in some particular order, and to say that we have abstracted from this does not lessen that fact. It is the particular order in which the data is stored which, from our point of view, defines the data structure for such a file.

(a)  
(b)  
![](/api/attachments/EJA47FCZ/fulltext/images/080c1b6480a1f0eca4b116cc4c9423ec15ef4958e2c1dbc5c00cccdcfa3e3515.jpg)  
(d)  
Figure 6: Storing a structure as a relation

Reverting to Figure 6, we can say that in order to do justice to the information content of (a) we need a rendering of table (b) which does not commit us to any particular sequence of the ordered pairs. Only in this way could we be said to be implementing a data structure equivalent to the idea of an unordered set. Such a data structure is provided at (d). The way this may be understood is as follows: the centre of the 'star' may be thought of as the set itself and the radiating lines may be thought of as the ordered pairs t (for '2-tuple'). The values in each pair are given by the data, linked by f as before. To progress from one pair to the next, one always returns to the centre so there is no implied ordering between them. It will be apparent how very different this structure (d) looks from the original structure (a); and yet these two structures are equivalent — each is just a coded version of, a method of storing, the other.

A statement of equivalence is of course an existential statement, a statement to the effect that a semantic rule exists that will transform either structure into the other, whereas a statement of inequivalence is a universal statement — a statement to the effect that no such rule is possible. With regard to Figure 6, finally it should be clear that (c) and (d) are inequivalent; there has been a loss of information in passing from (c) to (d) because although the individual 2-tuples are faithfully represented in (d), no guidance is given as to what order they occurred in; moreover, no method could salvage this information from (d). Notice that although in the particular illustration (1, 2) occurs between (3, 4) and (5, 3) in (d), this is for graphic purposes only on the page; topologically there are no internal links to establish this.

Every data structure can be written as a relation (even tables for relations can be expressed as further relations). There is also another standard technique for reformatting data structures and that is the use of a transition matrix. In its basic form this really applies only to structures containing just one type of link - just as indeed the relational representation is a representation of only one type of link. (If Figure 6(a) had contained another link g, then another table in (b) would have been necessary.) If we consider the same structure - Figure 7(a) - we find we can also represent it as a collection of bits in a table. The nodes are listed along the sides and if a 1 appears in an entry then that means there is an f-link from the node for that row to the node for that column - as in (b).

The full table shows all the possible connections that can be made between the nodes $(5^{2}=25)$ of which the stored bits show which connections have actually been made. Of course the numbers 1 to 5 along the sides are purely incidental; in order to recreate (a) the rule only has to ensure that the node corresponding to the second row is the same as the node corresponding to the second column, etc. In fact even this is not necessary in general, and there only has to be a one-one correspondence between rows and columns which the rule can then make use of. Thus the information necessary to generate (a) is all contained in (c) provided it is correctly interpreted. Like the relation, this matrix again contains a sequence not present in the original structure (i.e. the ordering of the nodes 1, 2, 3...), and so (b) and (c) both contain more information than (a).

A practical example of structures which are truly equivalent may be given by two alternative implementations of a questionnaire. Consider a questionnaire in which all the questions can be answered 'Yes' or 'No'; the page is ruled into two columns and for each question the response is recorded by placing a tick (√) in the appropriate column, opposite the question. The arrangement is shown below:

<table><tr><td>Questions</td><td>Yes</td><td>No</td></tr><tr><td>Q1</td><td></td><td></td></tr><tr><td>Q2</td><td></td><td></td></tr></table>

Omitting the questions, this gives us the data structure of Figure 8(a). Equivalently, this same information could be held by using only one column and writing Y for 'Yes' and N for 'No' in it, giving a structure such as Figure 8(b).

The interesting thing about this structure is that while we have halved the number of nodes in passing from (a) to (b), we have compensated for this by doubling the number of values of data. Because there are twice as many nodes, there is no sense in which this could be an isomorphism, since the most elementary prerequisite for isomorphism is one-one correspondence. Admittedly the structures are not so wildly different as in Figures 6 or 7 but the 'similarity' between them is not definable by isomorphism.

![](/api/attachments/EJA47FCZ/fulltext/images/f711a7e515f4d82029b49136d7f2078f7b95a07d828672eebd1b9c424f15ecc3.jpg)

Figure 7. Storing a structure as a transition matrix  
(a)  
(b)  
![](/api/attachments/EJA47FCZ/fulltext/images/e16edc56a4f2e689f1942266c44ccbd6bdb10d6bc201290814f48fbacb29fde4.jpg)  
Figure 8. Two data structures for a questionnaire

We can define it, of course, but only in terms of a rule for converting one structure into the other—not in terms of any characteristic common to the two structures. If we observe anything common to them both, what we must be seeing is the rule. Perhaps the best way of putting the matter is to say that there is no descriptive rule (set of axioms) satisfied by both structures and sufficient to make them equivalent. There is only a pair of procedural rules (programs), for converting each structure into the other.

So structures, while being superficially very different, may still be capable of fully representing each other. The exact method by which such representations are verified (that is, what is and is not to count as a semantic rule) will be developed in a future paper. However, at this stage it is interesting to note that merely by inspecting a pair of structures it is possible to see how one may be transformed into the other and to arrive at a decision regarding their mutual information content. How do we do this? Perhaps descriptively, by seeing what elements or groups of elements in one data structure correspond to elements in the other; or perhaps procedurally, by imagining some algorithm which will convert one structure into the other. An example of the first was when we saw that the data values in Figure 6(c) stood for the nodes in Figure 6(a); an example of the second kind was the imagined procedure by which the transition matrix, Figure 7(b), could be converted into its structure, Figure 7(a).

When two structures are equivalent it is likely that if any links or nodes are added on to one of the structures gratuitously (that is, not via a rule), it will then contain strictly more information than the other structure insofar as the other structure contains no inkling of this alteration. Thus the equivalence is usually lost and the structures become inequivalent. For example, suppose one more question were added to the questionnaire and that Figure 8(a) is appropriately updated with two extra nodes but its abbreviated form, Figure 8(b), is not. Then (b) is no longer the abbreviated form of the revised structure and, moreover, we may deduce that (b) is incapable of representing (a) by any more exotic encoding by the following argument: the original (a) is equivalent to (b), but when we add new nodes to (a) we obtain a structure which cannot be constructed from the old (a) under any circumstances — there is simply nothing in the old (a) to say what the new data will be. If that is the case then equally there is nothing in (b) to say what its new data should be since (b) is equivalent to (a). Therefore the new (a) cannot under any circumstances be built from the old (b).

Thus it is a good starting point, in investigating how information is gained and lost, to begin with equivalent structures and see which kinds of alterations do and do not render them inequivalent. It is worth pointing out, however, that not every alteration to a structure changes its information content — it depends how it is done. For example, in Figure 9 while there is an evident increase of information by arbitrarily adding the node to (a) to give (b), this is not the case with (c). Although (c) appears more complex than either of the other structures it is in fact simpler than (b). Examining (c) we find that an extra node has been linked by g to every node of (a) — so whereas in (b) one node was singled out in this regard, now every node has received the same treatment so there is nothing special about any of the nodes; equilibrium has been restored. Thus (c) contains the same information as (a) — i.e. less than (b); in fact whenever one wishes to process structure (c) one can always ignore the g-links as redundant — that is, one can treat all pairs of nodes such as this:

![](/api/attachments/EJA47FCZ/fulltext/images/f445071236cc3c9bb018398fc6cf3eccc84f06fb270d98d0b551998845d0efad.jpg)

as single units and, in so doing, one would be processing the structure exactly as if it were (a).

All these ideas, which we have been expressing loosely, are formidably difficult to make precise. However, Figure 9 serves to illustrate that merely by adding nodes to a structure one does not automatically increase its information content – although if one does so selectively, one frequently can. The one golden rule in these matters would seem to be that generalizations should not be made – each case must be judged individually.

I have tended to use information content as a measure of complexity insofar as a structure containing more information has been said to be more complex than one containing less information. In other words if A can construct B but B cannot construct A, then A is more complex than B and B is simpler than A.

Our usage is also in accord, I believe, with Ludwig Wittgenstein's tantalising expression 'mathematical multiplicity' (see, for example, Tractatus Logico-Philosophicus at 4.0411). This is a term which he never defined. He was wont to say, when commenting on the grammar of a particular propositional sign, that it lacked the requisite mathematical multiplicity to express the desired meaning. We can understand this to refer to the information content or complexity of the sign.

Complexity is not a numerical measure, as some have tried to maintain. The latter who have devised ‘complexity metrics’ are notably people adopting a concept of information based on entropy. This is an analysis which we totally reject in this work since entropy is based on probability, i.e. the analysis of chance events. Rather than take this negative course of defining information as absence of randomness, we define it more positively as the source and origin of meaning.

(a)  
(b)  
![](/api/attachments/EJA47FCZ/fulltext/images/4de7f65bf63bbc28807152f1f5032df3ace94b036a33c42fc41fb06a3b6fc0e3.jpg)

(c)  
![](/api/attachments/EJA47FCZ/fulltext/images/85fcfc887b2577bed3faf39cbc5423e087b664f46c3da7be9e8fd9671cc16990.jpg)  
Figure 9. Altering the information content of a structure by adding extra nodes

![](/api/attachments/EJA47FCZ/fulltext/images/cd4a0b690859cbe9e66a8ee531aeb65fdbeef3a52ef3deadd0dfede5b1f517f7.jpg)  
Figure 10. Two independent structures

Complexity, then, is not numerical but it does set up an ordering between structures — it is what mathematicians call a partial ordering insofar as whenever one structure represents another we can always decide which contains the more information, but it is not always possible to compare an arbitrary pair of structures from this point of view — they may be completely independent. Two structures are said to be independent if it is impossible for the first structure adequately to represent the second but it is also impossible for the second structure adequately to represent the first (see the section on Notation).

A simple example is sufficient to illustrate the concept of independence: in Figure 10 two ways of structuring four nodes are shown — the star $S_{4}$ and the circuit $C_{4}$ . However, neither of these structures may be converted into the other: starting with $S_{4}$ , between which pair of nodes are we to place the centre node when creating $C_{4}$ ? Indeed, in what order are any of the outer nodes to be arranged so as to produce $C_{4}$ —which pair of nodes should be adjacent, for example? The information is simply not provided. When we say the information is not provided, we do not mean by one particular rule, we mean that whatever rule we care to choose there are not sufficient structural elements within $S_{4}$ upon which such decisions could be based. It is an intrinsic poverty about the structure of $S_{4}$ . Because of this one might be inclined to think that $C_{4}$ is a richer structure, that from $C_{4}$ , $S_{4}$ could be built. But this is not the case either; for on what basis would we choose one of the nodes in $C_{4}$ to be the central node in $S_{4}$ ? All the nodes in $C_{4}$ are indistinguishable; there is not sufficient reason to single one out and, again, there is nothing structural upon which such a decision could be based. Therefore $C_{4}$ cannot generate $S_{4}$ either. Gazing at the two simple structures $S_{4}$ and $C_{4}$ it is perhaps somewhat of a surprise that neither could ever contain the other as a coded message.

In what kind of thought process have we just been engaged? We were not checking corresponding elements against a common description because there was no description and there was no correspondence. Nor were we validating any particular procedures to convert one structure to the other because there were no such procedures — these structures were independent. It seems that we were thinking at a more abstract level altogether; we noted that in $S_{4}$ one node was different from all the rest — an ‘odd man out’ — whereas in $C_{4}$ all the nodes were the same or ‘indiscernible’. The precise nature of this oddity did not concern us. We were not concerned in $S_{4}$ that there was a unique node which pointed to all the others. Had we done so, there would have been a specific description that we were checking. But there was no such description — the uniqueness itself seems to have been what we were checking, in the sense that had we found a similar uniqueness in $C_{4}$ we might have had cause to assume the existence of a rule taking one structure to the other. Indeed, it does seem that it was not so much rules that we were examining (for there were none), as the possibility of rules. And this possibility will of course gain expression ultimately in terms of the syntax and semantics of a certain programming language. In this example, as it turned out, there was no such possibility and we concluded that no rules exist, the structures being independent.

I am not suggesting that every comparison between structures will follow the above lines; merely that the nature of such a comparison is not as obvious as it seems and that if, as I have claimed, it is always rules that we are looking for, then it would appear that there are a number of visual cues that can lead us to the existence of rules, without our being in full possession of the detailed rule itself.

## Biographical notes

![](/api/attachments/EJA47FCZ/fulltext/images/78caffbed6d78413b2699f707dd62eeac022f26896ebbfbf5a1509060d390bc2.jpg)  
David Henley is a data analyst whose principal interest has always been the philosophical and psychological implications of computing. He holds a BA degree in mathematics and philosophy and an MSc in business systems analysis. In 1973, after joining the Research and Advanced Development Centre at ICL, he worked for seven years on the early theory and practice of relational databases. Special interests were data modelling of the external world and relational interfaces with natural

language. In 1983, after a short spell in teaching, he joined a software house where he worked as a systems analyst, mainly for clients in the public sector. For many years he has also been engaged in a sustained programme of unpublished research into the nature of information, much of which is currently being consolidated into book form, and as a result he is now working full-time as an author.

Address for correspondence: 21a Vincent Gardens, Neasden, London NW2 7RJ.
