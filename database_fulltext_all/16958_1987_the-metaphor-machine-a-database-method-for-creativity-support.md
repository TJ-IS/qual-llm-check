---
otero_id: 16958
otero_key: "WRYNNP5W"
title: "The metaphor machine: A database method for creativity support"
authors: "Lawrence F Young"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90102-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Metaphor Machine: A Database Method for Creativity Support

Lawrence F. YOUNG

University of Cincinnati, Cincinnati, OH 4522 $^{1}$ , USA

This paper shows how a data base method can be applied to the automatic generation of metaphors. The utility of automatic metaphor generation is based on providing interactive support to creative human thinking processes. Such interactive support systems have been called Idea Processing systems, and are seen as special qualitative types of Decision Support Systems (DSS). They include functions to support metaphorical thinking as well as other modes of creative idea development. The paper presents brief backgrounds references on creativity and the relevance of metaphors, as well as to previous work in Idea Processing. It then presents a relational data base method for automatic metaphor generation. The method is described and illustrated, as well as shown in relational algebra and relational calculus notation. In conclusion, the paper indicates how the relational data base method presented can be operationalized through using existing data base software or by integration with a specialized interface for the particular application of metaphor generation.

Keywords: Creativity Support Systems, Methaphor Generation by Computer, Database Methods for Metaphor Generation, Idea Processing Support, Computer Support of Metaphorical Thinking, Support of Creative Thinking, Qualitative Support Systems, A Relational Calculus for Metaphor Generation, Relational Database Methods for Metaphor Generation, Interactive Support Systems for Creativity, Right-Brained Support Systems, Relational Algebra for Metaphor Generation, Database Structures for Metaphor Generation, Computer Support of Divergent Thinking.

![](/api/attachments/WRYNNP5W/fulltext/images/ac23137ec9af09a384e23cf0494108732536ffc1f8e0268c06c94a76703668fa.jpg)

Lawrence F. Young is Director of Information Systems Programs at the College of Business Administration, University of Cincinnati. He previously planned and served as Advisor for MIS programs at Drexel University and at the Technion, Israel Institute of Technology. Dr. Young was vice president for management sciences at the Interpublic Group of Companies, where he pioneered in the development of marketing/advertising support systems, and has held professional positions with the Du Pont Company, IBM, and Western Electric. He was Editor of Information Systems Management and is advisory board member and reviewer for several journals. Dr. Young has consulted for AID, U.S. State Department, NAVSSES, and business organizations in the U.S., Europe, Israel, and China.

## 1. Scope and Objectives

The main purpose of this paper is to show how existing data base methods can be applied to the automatic generation of metaphors. The utility of automatic metaphor generation is based on providing interactive support to creative human thinking processes. Such interactive support systems have been called Idea Processing systems, and are seen as special qualitative types of Decision Support Systems (DSS). They include functions to support metaphorical thinking as well as other modes of creative idea development. Brief background and references regarding creativity and the relevance of metaphors are given, as well as to previous work in Idea Processing, before presenting relational data base methods for automatic metaphor generation. The paper concludes by indicating how the relational data base methods presented can be used in practice either through existing data base software or by integration within a specialized interface for the particular application of metaphor generation.

## 2. Human Creativity and Idea Processing Support Systems

As noted above, the formulation and development of new forms of computer support systems, called Idea Processing systems, are aimed at facilitating the human creative processes of finding and developing new ideas. Only very general models of the human creative process are available as references for this work, most notably, the Wallas model (1925). The Wallas model merely describes a four stage process of Preparation, Incubation, Illumination, and Verification. However, several other observers have added to our understanding of creative thinking by describing certain commonly recurring themes. One such theme is that which claims and cites evidence that divergent thinking processes, as opposed to convergent thinking, are relevant to creativity [Guilford (1967)]. Divergent thinking involves a broad search for alternatives, usually in an ‘open problem’, that is, a problem for which there is no unique answer. Tasks involving divergent thinking were examined by Fulgosi and Guilford (1968) with respect to short-term incubation (unconscious divergent thinking, as in Wallas’ idea incubation stage). In divergent processes, the generation of alternatives involves finding many combinations of elements that may provide possible answers. Fluency of thinking and originality characterize a divergent search for alternatives, rather than rigorous adherence to prescribed steps and criteria for finding some uniquely ‘correct’ result. In a convergent search, the opposite is true; that is, there is a unique solution to meet prescribed criteria that is sought. As Guilford points out (1975), however, these two modes are not necessarily used in isolation and can be intermixed in that a ‘guessing’ or divergent approach can be used ‘on the way’ to a convergent solution. The degree to which the entire process can be characterized as divergent or convergent is relative rather than absolute and depends on the degree of limitations imposed on the answer.

Although the research base is sparse, another recurring theme is the relevance of creativity to problem discovery and formulation as opposed to finding problem solutions. Taylor (1972) observed that those high in creativity tended to gravitate toward more generic problems in an attempt to understand underlying general relationships as opposed to the more direct approach of solving more well-defined and specific problem manifestations. Other investigators [Csikszentmihalyi and Getzels (1971)] also found that originality in artists was highly related to the problem discovery orientation.

These themes and others, such as the use of metaphors in creative thinking (discussed below), have been used to foster creativity through special (non-computerized) procedures such as Brains-torming [Osborn (1963)]. Synectics [Gordon (1961)], and several other noncomputer-based methods described by Rickards (1974). Based on these processes and the descriptive observations of creativity, Young (1983) formulated a set of computer-based functions to support human creativity. In the book ‘Decision Support and Idea Processing Systems’, Young (scheduled publication, Jan. 1988) has revised these functions and extended them into a more fully formulated interactive support system to enhance individual user's ability to think creatively. An Idea Processing support system would include several functions to aid divergent thinking and to help organize and reorganize ideas. These include, among others, such functions as the ability to generate new combinations of ideas, to help users to develop their ideas through organizing aids such as hierarchical outlining and successive generalization structures, aids to assist in developing qualitative scenarios, and aids for metaphorical thinking.

## 3. The Role of Metaphors in Creative Thinking

A pervasive theme in describing creative thought processes is the role of metaphorical thinking. Metaphors are figures of speech in which one kind of object or idea is used in place of another to suggest some kind of likeness between them. They serve in making connections between things which are not usually seen as connected in any literal way. Through such non-literal connections we are able to see things in a new way. Poetic uses of metaphor, such as 'My love is a red rose' or 'My soul is an enchanted boat' evoke feelings and associations that help to convey the non-literal emotions and thoughts of the author's mind to the mind of the reader. In the world of politics and business, metaphors are also commonly used to emphasize, familiarize, and to explain. For example, computer science instructors often explain the function of the Control Unit in a computer's Central Processing Unit by saying it is 'the traffic policeman of the computer'. The general use of the term 'memory' to denote computer storage is metaphoric. Metaphors are instruments of divergent processes because they synthesize disparate ideas. They include and integrate possibilities that would be excluded by referring only to literal standard categories. For this reason metaphors are useful in extending the search for discovering and understanding new problems and in identifying potential new solutions.

Metaphors have been observed to be used spontaneously by creative thinkers. Based on the assumption that metaphors can also be used intentionally to foster creativity, the generation of metaphors are a key device in Gordon's (1961) 'synectics' process for developing creativity (see exhibit 1). Gordon uses metaphorical aids to first ‘make the familiar strange’ so that the usual constraints of literal logic and fixed perceptions of the familiar can be broken through. In another phase of the synectics process, metaphors are further used to ‘make the strange familiar’; as a means of seeing new relevance in the unfamiliar to the problem at hand.

<table><tr><td>Exhibit 1Synectics and the Use of Metaphor.</td></tr><tr><td>The Synectics Process follows the following general phases:</td></tr><tr><td>Phase 1Problem As Given (developing or identifying the original understanding of the problem or general concern).Example: ‘Stop the decline in sales of powdered milk. Large families with low incomes are our main customers and they are demographically declining’.</td></tr><tr><td>Phase 2Making the Strange Familiar (uncovering and revealing hidden or contrary elements not previously identified).Example: ‘Powdered milk customers are disappearing – what else is shrinking in size?’ ‘When can less become more?’</td></tr><tr><td>Phase 3Problem as Understood (analysis and digestion of the initial problem in order to redefine the problem in a more appropriate new way).Example: ‘How can we increase profits from the sale of our product even if our traditional customer base is decreasing?’</td></tr><tr><td>Phase 4Operational Mechanisms (metaphors are developed which are relevant to the problem as understood. The purpose is to open up the problem and escape from rigid, overly constrained thinking).Example: ‘What is a book title that captures the contradiction here?’ ‘Smaller is bigger!’ ‘David Beats Goliath!’ ‘what is a metaphor for a ‘David’ from the World of Sports?’ ‘How about a horse racing jockey? – The smaller they are, the better they are at winning races because they are lighter!’</td></tr><tr><td>Phase 5The Familiar Made Strange (uses the metaphors to see the problem in a strange new way).Example: ‘How could our product be likened to the jockey?’‘We want less of our product to mean more when it’s used</td></tr><tr><td>Phase 6Psychological States (creates the psychological atmosphere, including involvement and detachment, most conducive to creativity according to synectics theory).‘Let’s not get too literal yet. Is there another way to describe our situation as a book or movie title that expresses a paradox?’ ‘How about: The Customer Takes A Powder.’</td></tr><tr><td>Phase 7States Integrated With Problem (the most pertinent analogy is conceptually compared with the problem and used to liberate the problem form its old form).Example: ‘We need to make the product more like a jockey so that smaller portions will return more and we need to stop chasing the same customers but instead put the product into a different race.’</td></tr><tr><td>Phase 8Viewpoint (stating a technical insight obtained through the prior steps).Example: ‘We need to package the product in smaller units and sell it to a different group of users who will pay more for its convenience and value-in-use rather than for its quantity. For example – use it in a prepared cooking mix for busy working couples; or use it in small packets as a coffee additive in offices, or position it as low fat alternative to whole milk for the health conscious’.</td></tr><tr><td>Phase 9Solution or Research Target (the viewpoint is made operational by testing the underlying principle or defining the necessary further research).Example: ‘We need a consumer market test for each of these product-market segments.’</td></tr></table>

## 4. Levels of Support For Metaphoric Thinking

Young (1988) defines three levels of support for Idea Processing systems:

(a) The Secretarial Level - at which the computer is used essentially as a dynamic electronic blackboard, that is, as a device for capturing, storing, and mirroring back the user's thoughts in order to facilitate their modification and further development through human thinking processes.

(b) The Framework-Paradigm Level – at which the computer system adds to its secretarial capabilities by also providing the user with selected frameworks appropriate to the organization of the user's thoughts, with frameworks consisting of both organized, labeled structures, as well as completed examples or sample entries to serve as both thought stimuli and guides to the user.

(c) The Generative Level - at which the computer adds to the prior two types of capabilities the ability to automatically synthesize and display new ideas based on associating elements previously stored in some data base structure or currently entered by the user.

This paper refers to a data base method which would enable the third level of support to be operationalized for purposes of automatically generating metaphors at the request of the user. As indicated in the above descriptions, the three support levels are intended to be hierarchical and cumulative, implying that support for metaphoric thinking at The Generative Level includes the prior two levels as well as the ability to automatically generate metaphors. However, the lower levels of support will not be explicitly treated in this paper. [See Young (1988) for examples and interface design specifics at all three levels.]

## 5. Data Base Methods for Metaphor Generation

## 5.1. The Basic Processing Logic

The logic of the mental association between any input entity and an output metaphor depends on finding one or more physical, functional, or situational similarities between them. The nature of the similarity, its degree (or strength), can vary over a wide range, the extent of which depends on the thinker's scope of experience and ability to perceive and recall associations. A guiding model of metaphoric association that can serve as the basis for formulating computer support functions is presented in exhibit 2. The key to this model is the observation that any entity can be metaphorically associated with another entity through a four-step logical process.

(a) place the initial entity within an applicable predicate (in other words, make a statement about what the entity is or does or its condition (state) of being); in the example, the initial entity is ‘chairperson’ and the first applicable predicate chosen is ‘chairpersons expedite’.

(b) identify a synonym for the verb component of the predicate; in the example a synonym list for ‘expedite’ is referenced and in the first iteration, the synonym ‘cut through’ is selected, and the synonym ‘dispatch’ is also subsequently selected.

(c) find another (different) predicate using the verb synonym just found; in this example, the same verb phrase 'cut through' is found among the predicates in the list called 'World of Tools', and 'dispatch' is found in the predicate list called 'World of Entertainment'.

(d) extract the object noun from this new predicate as a metaphor for the initial entity. (In this step, a predicate containing the identical entity to the initial entity is rejected and step (c) is repeated to find a different predicate.) In the example, ‘Knives’ is obtained from ‘Knives cut through’ in the ‘World of Tools’, and ‘Masters-of-Ceremonies’ is obtained from

'Masters-of-Ceremonies dispatch' in the 'World of Entertainment'. Thus knives (or knife) and Master-of-Ceremony are each metaphors for a chairperson.

(e) To find additional metaphors, the process can loop back to step(b) to find another synonym for the same verb, or can loop back to step(a) to find a new predicate statement about the same initial entity

Using this process of finding metaphors repeatedly, the number of metaphors that can be found for a single initial entity depends on the number of predicate statements one can make about that entity and on the number of synonyms that are examined for the verb component of each predicate.

A synonym is a word which has the same, or a similar meaning to another word. The quality of being synonymous is not exactly the same as two terms being mathematically equal or logically identical. Words are seldom exactly interchangeable, but can grouped in a continuum of connectedness through varying degrees of similarity according to varying dimensions or associations. This is essentially what a good thesaurus does and often explains in its foreword (see the Foreword of Roget's International Thesaurus (1977) for example). Thus, varying degrees of similarity between verbs can be used as the mechanisms for uncovering varying kinds of similarity between entities to which those verbs can be applied. This method, like any mode of metaphoric thinking, is not a content-free logical algorithm but requires prior experience and general knowledge about the world before one is capable of identifying metaphors.

The manner in which the human mind actually operates may or may not be anything like the logical processing method described above. But the logic of this process works in the sense that it provides an output metaphor for an input entity, given a large enough stored set of predicates and synonyms. Whether or not one or more of the metaphors thus generated are useful for the purpose at hand depends on the associations they may evoke in the user's mind. It is likely that most metaphors generated by this kind of automated process will be trivial, will not stimulate useful associations, and will therefore be passed over by the user. Therefore the process will usually have to be repeated many times to generate lists of metaphors for the user to scan until one may strike the user by stimulating an interesting new association providing a new insight. In this respect, this process, here involving a single user working with an automated procedure, is not unlike the group protocols of synectics or brainstorming, in which the generating mechanism is the collective minds of the people in the group. In the group process also, many if not most of the metaphors and ideas generated can be expected to be passed by until a strikingly useful one is presented.

As described below, his logical process for generating metaphors can be computer automated by organizing stored lists of predicates into ‘Worlds’ represented by relational databases. organizing and storing a large set of synonym-pair relational databases (possibly including the full contents of a standard thesaurus), using a sequence of database join operations, and suitably arranging and displaying the results.

A 'World', in the sense used here (and illustrated in much scaled-down form in exhibit 2) consists of a large set of predicates which are statements about what occurs or exists with respect to the entities in a particular area of related activities (e.g., in the 'World of entertainment' 'singers sing', 'comedians tell jokes', etc., while in the 'World of Education', 'students read', 'teachers lecture', etc.). The statements that comprise each World can be represented as database relations, each relation representing a different world.

In applying such an automated process, the user can repeatedly interact with the system in a manner similar to the manner in which the user might interact with one or more persons, by in effect asking: 'Can you give me a metaphor for (entity X)?'

The system then responds with a list of metaphors, displayed for the assessment of the user.

## 5.2. Relational Data Base Organization and Relational Algebra

The basic relational data base form of representing ‘Worlds’ containing predicates and synonym pairs is illustrated in exhibit 3. In the following discussion, relational notation consistent with that defined by Martin (1975) is used.

![](/api/attachments/WRYNNP5W/fulltext/images/48e2856b8f2d77e66fc7d5c81b028b0a233f37d21d93f7f17c41ccb127510b67.jpg)  
Exhibit 2. A Model of Metaphoric Association.

## Assume the given relations

$W_{1}(N, V)$ , where $W_{1}$ is a given World (World 1) consisting of 2-tuples N, V in which N is a column of nouns (entity names) and V is a column of corresponding verbs (actions or states of being),

$W_{2}(N, V)$ , where $W_{2}$ is another World (World 2) consisting of tuples N, V, in a similar manner to that of $W_{1}$ . Any number of relations can be created to represent up to N such Worlds, with the last World represented by the relation $W_{N}$ .

$S(V, V')$ , where $S(V, V')$ is a relation consisting of pairs of synonymous verbs, V and $V'$ .

$M(N, N')$ , where M is a new relation to be generated and consisting of 2-tuples N and $N'$ , in which the values of N are respectively metaphors for the corresponding values of the entity $N'$ .

## 5.3. Relational Algebra for Generating First Order Metaphors

A basic relational algebra to produce metaphors consists of the following

$$
J O I N 1 = W _ {1} * S \left(N ^ {\prime}, V ^ {\prime}\right),
$$

in which $W_{1}$ and S are joined on their common column V and $N'$ is the new designation for the N column of $W_{1}$ ,

$$
M = W _ {2} * J O I N 1 (N, N ^ {\prime}),
$$

in which $W_{2}$ and JOIN1 are now joined on their common column V, assuming $V'$ is defined as an alias for V for this purpose.

The new relation M now contains the desired output of tuples in which each N value is a metaphor for each $N'$ . It should be emphasized that this relational algebra will result in producing a complete relation with as many metaphorically paired entities as may result from applying the relational operators to the given relations. In practice a user is likely to want to see metaphors for only a single given initial entity at a time. This can be accomplished by initially making a selection from a particular World relation in which the user entered entity resides and treating that selection as a new initial relation before proceeding. In other words, the steps in the algebra could be modified as follows.

$U_{1} =$ selection from $W_{1}$ for $N =$ (entity name), (1)

Relation W1 WORLD OF SPORTS (Predicates)  
![](/api/attachments/WRYNNP5W/fulltext/images/85c48f9a39bfdf8b37a6d1b151f866fe66d9475ad76198f57177fccb5a8655f4.jpg)

Relation S Synonyms  
![](/api/attachments/WRYNNP5W/fulltext/images/260c7e2898d6fc5cbebb69df36a494b1a8f368f6ce297a8b90553f8796306d7e.jpg)  
Exhibit 3. Relational Data Base Organization.

where (entity name) would be a particular value (that is, a text name of some particular entity) specified by the user.

$$
J O I N 1 = U _ {1} * S \left(N ^ {\prime}, V ^ {\prime}\right).\tag{2}
$$

The last step (now step 3), would be as before

$$
M = W _ {2} * J O I N 1 (N, N ^ {\prime}).\tag{3}
$$

An alternative to the above procedure would be to generate all metaphor pairs as in the initially presented two-step algebra, and then to select tuples for display from the complete output relation according to user supplied entity names.

It may also be desirable to display not only the original entities and their metaphors, but the full original and matched predicates. This can be done by creating an expanded new relation M that contains N, V, $N'$ , and $V'$ . The above steps would then be modified as follows:

$$
J O I N 1 = W _ {1} * S \left(N ^ {\prime}, V, V ^ {\prime}\right),\tag{1}
$$

in which $W_{1}$ and S are joined on their common column V and $N'$ n is the new designation for the n column of $W_{1}$ .

$$
M = W _ {2} * J O I N 1 (N, V, N ^ {\prime}, V ^ {\prime}),\tag{2}
$$

in which $V'$ is now used as the designation for the column originally called V of $W_{2}$ for purposes of this join with relation JOIN1 based on its column $V'$ .

Ignoring these latter variations that may be desired for the convenience of the user (or for the sake of processing efficiency) but not affecting the basic logic of finding metaphoric linkages, the relational algebra presented above operationalizes the equivalent logical process described at the beginning of this section. However, using the same defined relations, metaphor generation can be accomplished in other less direct ways. The fundamental procedure described finds a fairly direct linkage between two entities based on an equivalence between a verb tied to entity number 2 and a synonymous verb tied to entity number 1. Metaphors generated through this kind of linkage can be designated first order metaphors. Another approach is described in the next section.

## 5.4. Second Order Metaphor Generating Relational Algebra

Instead of the type of linkage obtained through the previously described procedure, two different entities can be metaphorically linked based on an equivalence between a synonym of a verb tied to entity number 2 and a synonym of a verb tied to entity number 1. Metaphors generated through this kind of linkage can be designated second order metaphors. (See exhibit 4.)

Referring to the same relations previously defined, the basic relational algebra for generating second order metaphors is given as follows.

$$
J O I N 1 = W _ {1} * S (N 1, V ^ {\prime}),\tag{1}
$$

in which $W_{1}$ and S are joined on their common column V, N1 is the designation for the N column of $W_{1}$ now placed in the relation JOIN1, and $V'$ is taken from relation S.

$$
J O I N 2 = W _ {1} * S (N 2, V ^ {\prime \prime}),\tag{2}
$$

in which $W_{2}$ and S are joined on their common column V, N2 is now the N column of $W_{2}$ placed in relation JOIN2, and $V''$ is the $V'$ column from relation S now placed into relation JOIN2.

$$
M = J O I N 1 * J O I N 2 (N 1, N 2),\tag{3}
$$

in which the relations JOIN1 and JOIN2 are now joined based on considering $V'$ and $V''$ to be mutual aliases. N1 and N2 tuples now consist of second order metaphors.

It can be noted that it is possible that this procedure would yield some second order metaphors that would also be generated as first order metaphors. This could come about if tuples are found in S in which the value of V for a given tuple in S is also found as the value of $V'$ for another tuple in S.

![](/api/attachments/WRYNNP5W/fulltext/images/7e12fca7cc878129ce328404fe119de1f15497cdeec439e6e5f403222b3048bf.jpg)  
Exhibit 4. Generating Second Order Metaphors.

## 5.5. Relational Calculus Expression for Metaphor Generation

A relational calculus expression defines the desired relation with respect to other given relations without specifying the step by step process required to produce the desired relation. In this respect it differs from a relational algebra, which does specify a sequential process. A relational calculus expression may be useful to compactly convey logical linkage in a manner that is independent of a particular system of operations. Referring to relations $W_{1}$ , $W_{2}$ , S, and M, defined previously, a relational calculus expression for first order metaphors is as follows:

$$
\begin{array}{r l} M (W _ {1} \cdot N ^ {\prime}, W _ {2} \cdot N): W _ {1} \cdot V & \\ = S \cdot V ^ {\wedge} S \cdot V ^ {\prime} = W _ {2} \cdot V, \end{array}\tag{1}
$$

where $\hat{}$ denotes ‘and’, : denotes ‘such that’, R. X denotes a set of values of data items in domain X in relation R and $Q(R \cdot X, T \cdot Y)$ denotes a relation Q consisting of domains X from relation R and Y from relation T.

Similarly, a relational calculus expression for second order metaphors (as previously defined) is

as follows:

$$
M \left(W _ {1} \cdot N ^ {\prime}, W _ {2} \cdot N\right): S \cdot V ^ {\prime} = S \cdot V ^ {\prime \prime} \dot {A}\tag{2}
$$

$$
W _ {1} \cdot V = S \cdot V ^ {\wedge} W _ {2} \cdot V = S \cdot V,
$$

where À denotes 'for all'.

## 6. Metaphor Generation in Practice

Almost any database software package, whether it runs on a mainframe system or on a microcomputer, can be used to carry out the select, join, and display operations for the procedures described in this paper. The author ran some practice examples using the 1st Base Relational Database System for the MacIntosh to test out the logic presented here. While any similar system that can perform basic join operations can be used, it would be desirable to create a specialized interface that would be easier to use for this special application. Such an interface could not only prompt the user for the initial object for which metaphors are desired, but could also format the output list of metaphors for convenient user scanning. Moreover, the special interface could include a macro-operation for metaphor generation by automatically carrying out the sequence of join operations without requiring the user to know how to do this or to take the trouble to do it step by step. In addition, special operations that could be provided and would seem to be desirable would include enabling the user to select, rearrange, and save certain metaphors in an output display list for subsequent printing or assessment or 'pasting' into a separate text document.

It may also be useful to provide interface features and telecommunications to enable a user to converse with other users and trade metaphors and other comments within an on-line group protocol such as the synectics process or brainstorming. This would convert an individual creativity support system into a group support system.

Early experimental use of the procedure makes it clear that the utility of such a system depends largely on the scope and content of the databases for describing Worlds as well as that of the synonym database. Interesting or surprising metaphors are unlikely to be generated and were not generated from the small worlds or short list of synonyms needed only for testing the logic of processing. In practice, an extensive synonym verb database is needed and could be segmented and searched in a variety of ways that would make for more efficient processing than would a random or sequential search of a table of verbs. Such search procedures are well-known in computer science and need not be described here.

The entire contents of an extensive thesaurus need not be included in the relational synonym database. Only verbs are called for by the method described here. A rough estimate of the total number of characters required for such a database based on the verb contents of Roget's International Thesaurus (1977) is between 300,000 to 400,000 characters. Of course, the World databases would also require considerable storage. It would seem to be useful to conduct some experiments with varying numbers and sizes of worlds, in conjunction with a complete database of verb synonyms, in order to approximate the size and scope of Worlds needed for a useful system.

## Conclusion

This paper has presented an Artificial Intelligence method based on standard database operations for a process normally associated with human memory and creativity. The purpose, however, is not to displace human creativity with some artificial imitation, or to merely perform a computer ‘trick’, but to instead provide a basis for the potential support of an essentially human creative process. While a group of interacting people can be quite effective in generating metaphors for the purpose of stimulating new ways of looking at the familiar, the use of groups is not always feasible because of time availability or for other reasons. When a small group is available, the computer can, in effect, join the group and enhance it by serving as an extended memory device.

Computer generation of metaphors is one of several functions previously identified as appropriate for an Idea Processing support system in which the computer acts as an interactive secretary and partner. Unlike metaphor generation, the other identified functions of Idea Processing did not require Artificial Intelligence or currently unknown processing algorithms. By identifying a method of metaphor generation, this paper attempts to advance the development of more generalized and integrated Idea Processing Systems.

A method such as that described here can also be useful as an educational device and stimulus to develop an individual's imagination in courses and training programs on creativity. (Several universities have such courses. At the author's university, for example, there is a course called ‘Metaphorical Thinking’.)

Continuing research, development, and demonstration systems seem to be needed not only to advance the technology of Idea Processing, but also to break down existing mind sets on the limits of how the computer can serve us. The Decision Support Systems movement has gone a long way in widening the scope of our thinking in this regard. The extension of our notion of support systems into new realms of creative human thinking would seem to also be worthy of further exploration.

## References

Anderson, J. and G. Bower, Human Associative Memory (Winston, Washington, DC, 1973).

Csikszentmihalyi, M. and J.W. Getzels, Discovery Oriented Behavior and the Originality of Creative products: A Study with Artists, Journal of Personality and Social Psychology 19 (1971) 47–51.

Fulgosi, A., and J.P. Guilford, Short Term Incubation in Divergent Production, American Journal of Psychology 81 (1968) 241–246.

Gordon, W., Synectics: The Development of Creative Capacity (Harper and Row, New York, 1961).

Guilford, J.P., The Nature of Human Intelligence (McGraw-Hill, New York, 1967).

Guilford, J.P., Creativity: A Quarter Century of Progress, in I.A. Taylor and J.W. Getzels, eds., Perspectives in Creativity, (Aldine, Chicago, IL, 1975).

Martin, J., Computer Data Base Organization, 2nd ed. (Prentice-Hall, Englewood Cliffs, NJ, 1977).

Mintzberg, H., Planning On the Left Side and Managing On the Right, Harvard Business Review (July–Aug., 1976).

Osborn, A., Applied Imagination: Principles and Procedures of Creative Thinking (Scribner's, New York, 1963).

Parnes, S., Creative Behavior Guidebook (Scribner's, New York, 1967).

Rickards, T., Problem Solving Through Creative Analysis (Wiley, New York, 1974).

Roget's International Thesaurus, 4th ed. (Harper and Row, New York, 1977).

Sackman, Harold and Ronald L. Citrenbaum, Online Planning – Towards Creative Problem-solving (Prentice-Hall, Englewood cliffs, NJ, 1972).

Simmons, R.F., Semantic Networks: Their computation and use for understanding English sentences, in: R.C. Schank and K.M. Colby, eds., Computer Models of Thought and Language (Freeman, San Francisco, CA, 1973).

Taggart, W. and D. Robey, Minds and Managers: On the Duel Nature of Human Information Processing and Management, Academy of Management Review 6, Nr. 2 (1981) 187–195.

Taggart, W., and D. Robey, Human Information Processing in Information and Decision Support Systems, MIS Quarterly 6, Nr. 2 (June, 1982) 61–73.

Taylor, I.A., A Theory of Creative Transactualization: A Systematic Approach to Creativity with Implications for Creative Leadership, Occasional Paper 8 (Creative Education Foundation, Buffalo, NY, 1972).

Wallas, Graham, Art of Thought (Harcourt Brace, New York, 1925).

Young, L.F. Computer Support for Creative Decision-Making: Right-Brained DSS, in: H.G. Sol, ed., Processes and Tools for Decision Support (North-Holland, Amsterdam and New York, 1983).

Young, L.F., Right-Brained Decision Support Systems, Data Base, 14, Nr. 1 (1983) 28–38.

Young, L.F., Decision Support and Idea Processing Systems (Wm. C. Brown, Dubuque, Scheduled publication, Jan., 1988).

Zaidel, E., quoted in Scmeck, H.M., Jr., Two Brains of Man: Complex Teamwork, New York Times, pp. C1–C3, Jan. 8 (1980).
