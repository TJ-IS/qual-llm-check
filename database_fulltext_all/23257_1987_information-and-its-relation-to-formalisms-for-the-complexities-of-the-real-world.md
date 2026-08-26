---
otero_id: 23257
otero_key: "QFEM3QN6"
title: "Information and its Relation to Formalisms for the Complexities of the Real World"
authors: "John Shawe-Taylor"
year: "1987"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1987.27"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
PERSONAL VIEW

# Information and its Relation to Formalisms for the Complexities of the Real World

John Shawe-Taylor,

Department of Computing Science, Royal Holloway and Bedford New College, University of London

The idea of information is closely related to the abstract idea of knowledge, yet seems to imply knowledge in a form that can be communicated or at least interpreted. It is natural therefore in investigating this question to examine the ideas of Chomsky, Winograd, Schank and Abelson concerning natural language and also the ideas of Shannon concerning the transmission of information. In examining the ideas of these researchers we will also concern ourselves with the problem of finding formalisms to deal with the complexities of language and indirectly of the real world. It is often the limitations of these formalisms that also provide the greatest obstacle to our understanding the nature of information. The most basic method of communicating information available to humans is language. What are the ingredients of language that enable it to act in this way? One of the first researchers to seriously investigate this question was Chomsky (1957).

His initial attempt to understand language led him to generative grammar. This seeks to outline a system of rules which are capable of generating all the grammatical utterances of a language and no ungrammatical ones. A central notion is that sentences are hierarchically organized and each level can be obtained from the one above by rewrite rules. Thus a sentence (S) might be specified as follows:

$$
\mathbf {S} \rightarrow \mathbf {N P} + \mathbf {V P}
$$

where NP stands for a noun phrase and VP for a verb phrase. (This and subsequent examples of Chomsky's theory are taken from Taylor, 1982.) At the next level the noun phrase (NP) would be specified further: for example it must contain a noun (or pronoun in which case the following options are excluded); it may start with an article; it may include an adjective governing the noun, in which case the adjective must immediately precede the noun. We might represent this rule as follows:

$$
\mathrm{NP} \longrightarrow (\mathrm{Art}) + (\mathrm{Adj}) + N
$$

where the brackets indicate that the element is optional and N stands for the noun. Similarly the verb phrase (VP) might be developed as follows:

$$
\mathrm{VP} \longrightarrow \left\{ \begin{array}{l} \mathrm{Vtr} + \mathrm{NP} \\ \text { Vintr } \\ \mathrm{Vcop} + \text { Adj } \end{array} \right.
$$

where Vtr stands for a transitive verb, Vintr an intransitive verb and Vcop for a copular verb (such as to be). By further developing the elements at each level we eventually generate real sentences. It is possible in this way to analyse most simple English sentences by generating their phrase structure. But how far does this method contribute to our understanding of how language communicates information? Consider, for example, the following two sentences:

The Apache are eager to kill.

The Apache are easy to kill.

Although they have identical phrase structure and in fact just one adjective is differently instantiated, the kind of information is entirely different.

This problem is our first illustration of the limitations of formalisms with respect to the complexities of the real world. What at first sight seemed a good way of 'understanding' sentences is found to be incapable of significantly distinguishing two simple statements which have almost complementary meanings.

Such differences are difficult, if not impossible, to understand in terms of superficial structure, even if hierarchically analysed. To deal with such problems Chomsky proposed that sentences possess not only surface structure but also deep structure, which specifies the logical relations of their constituents, and their relation to other sentences much more directly than does their surface structure. Chomsky argues, therefore, that in order to give a complete account of sentence structure one must outline first the base rules which define the deep structure of sentences, and second the transformational rules which mediate the translation of deep structure into surface structure. What is aimed at in the base rules is a complete description of the elements involved in the sentence and their relationships. It is then simply a matter of applying the transformational rules to produce the sentence. The problem with this approach is how to specify all this information in a manner that could reasonably be accessible in human processing on the one hand, and be programmed into a computer on the other.

One method of overcoming the problem is to put very strong constraints on the 'outside world', and so make it reasonably easy to completely specify the logical relations of the agents involved. Perhaps in such a situation it would be possible to make sentences interpretable by a machine, and so indirectly for us to gain some understanding of how language conveys information; for as Winograd (1972) says:

If I have a complete blueprint for a complex mechanical device, it is not a 'theory' of how that device works. But it would be foolish not to see a blueprint as a valuable part of an 'explanation' of that device. Similarly, a program which completely duplicated the processes of human language use would still not be a theory. But any program which is built can be viewed as an hypothesised partial blueprint and can be a step towards understanding.

It is therefore to Winograd's attempts in this direction that we now turn. The particular simple world that Winograd uses is a scene in which various geometrical shapes are placed. He has developed a computer program which, with this scene stored in its memory, can interpret sentences about the objects in the scene and then manipulate the objects as requested. The manipulations are actually performed in memory and the program then remembers what it has done and why. Thus, for instance, here is part of a dialogue with the system quoted by Winograd (1972) (bold face are human input, capitals are program output):

... (after a sequence of requests have been performed on a scene)

had you touched any pyramid before you put the green one on the little cube?

YES, THE GREEN ONE.

when did you pick it up?

WHILE I WAS STACKING UP THE RED CUBE, A LARGE RED BLOCK AND A LARGE GREEN CUBE.

why?

TO GET RID OF IT.

why did you do that?

TO CLEAR OFF THE RED CUBE.

why did you clear off that cube?

TO PUT IT ON A LARGE GREEN CUBE.

why did you do that?

TO STACK UP THE RED CUBE, A LARGE REL BLOCK AND A LARGE GREEN CUBE.

why did you do that?

BECAUSE YOU ASKED ME TO.

how did you do it?

BY PUTTING A LARGE RED BLOCK ON THE TABLE; THEN LETTING GO OF IT; THEN PUTTING A LARGE GREEN CUBE ON IT; THEN LETTING GO OF THAT CUBE; THEN PUTTING THE RED CUBE ON THAT CUBE; THEN LETTING GO OF THAT CUBE.

The ability of the system to 'understand' complex sentence structure, tenses, implicit references etc. is, I feel, very remarkable. It illustrates what can be achieved when the formalism is limited to a simple predefined situation, in which the computer is effectively omniscient (the situation is exactly what is in its memory — no more, no less). The program is of course quite out of its depth as soon as any new dimension is added to the problem, for example another agent who can also move blocks or fluid which can be poured from one block to another. However, I think this example demonstrates one very important point; namely that perhaps our preoccupation with the grammar and syntax of language is misplaced, for in at least one situation where we know more about the semantics these problems can be dealt with very effectively. It seems that we are required to find a formalism which is capable of dealing with the complexities of the real world, if we are to make significant progress in understanding how natural language conveys information.

It was this challenge that led Schank (1983) to develop his Conceptual Dependency Theory. This was an attempt to find a universal shorthand of 'meaning propositions' for expressing the meaning of sentences. Its basic axiom is:

A. For any two sentences that are identical in meaning, regardless of language, there should be only one representation.

The initial framework he developed was as follows:

B. The meaning propositions underlying language are called ‘conceptualizations’ A conceptualization can be active or stative.

C. An active conceptualization has the form: Actor Action Object Direction (Instrument)

D. A stative conceptualization has the form: Object (is in) State (with Value)

This form for conceptualizations led Schank to the principle of primitive actions, for if a conceptualization is defined as an actor doing something to an object in a direction, then just what an actor can do has to be determined. The best representation of a given verb was found to be the primitive element it shares with other verbs of similar meaning plus explicitly stated the concepts that make it unique. To give a feel for this conceptualization we will describe a few primitive actions and how some verbs are interpreted using them.

ATRANS: the transfer of an abstract relationship such as possession, ownership or control. Thus, one sense of 'give' is: ATRANS something to someone else. 'Buy' is made up of two conceptualizations that cause each other, one an ATRANS of money, the other an ATRANS of the object being bought.

PROPEL: the application of a physical force to an object. PROPEL is used whenever any force is applied regardless of whether a movement took place. In English, 'push', 'pull', 'throw' and 'kick' have PROPEL as part of them.

Schank proposed 11 primitive acts in all, though he is by no means dogmatic about the choice or number. He notes that the use of such primitives (and in particular the surprisingly small number apparently needed) severely reduces the inference problem, since inference rules need only be written once for a primitive action rather than for each verb that references that action.

Conceptual Dependency Theory, however, requires more than primitive actions. Schank next introduces a relatively larger number of scales measuring various states such as HEALTH, MENTAL STATE etc. These are rated by points between -10 and 10 indicating where a particular entity lies on this scale (e.g. HEALTH(-10) is dead, while MENTAL STATE(10) is ecstatic). Finally an arrow symbol was introduced for connecting conceptualizations, indicating a causal relationship. For example the sentence 'John killed Mary' would be represented by two conceptualizations connected by a causal arrow:

## John DO $\leftarrow$ Mary HEALTH(-10)

Note that the direction of the arrow is the opposite to what a logician would expect!

It might be of interest to logicians and the possible limitations of their formalisms that Schank and Abelson (1977) in developing their theories to equip programs to deal with real life stories found it necessary to introduce not just the one notion of causality used above but, in all, six different causal links. These differ according to whether an action causes a state, a state enables an action, a state or action initiates a mental state, a mental action causes a physical action or a state disables an action.

With this apparently formidable formalism, Schank and Abelson tackle the problem of developing a system which is capable of 'understanding' human language. One of their crucial observations is illustrated by the following pair of sentences:

MacEnroe, in a fit of anger shook the high chair. Baby John, in a fit of anger shook the high chair.

Clearly these two sentences have exactly the same structure, but to an average reader entirely different meanings. What is it that causes us to see the high chair in the first sentence as an umpire's, while in the second it is a baby's? Clearly in the first sentence the name MacEnroe triggers our memory banks and conjures up a tennis match, while the reference to baby John in the second sentence has a different effect – the rest of the sentence is then interpreted in the framework that has arisen in our minds.

Schank and Abelson's first attempt at equipping a system with this kind of background knowledge is perhaps the next step beyond Winograd's simple scenes. They suggest that situations which we encounter very often, and which generally unfold according to a standard pattern, can be 'understood' if we interpret them as instantiations of a general 'script'. For example the following story is readily understood by most people:

John went to a restaurant. He asked the waitress for coq au vin. He paid the bill and left.

The reference to a restaurant allows us to understand immediately the role of the waitress and the strange 'coq au vin'. The computer system that Schank and Abelson developed can 'understand' stories involving several scripts (about which it has been informed) and can further answer questions about what took place and why. In one example the following dialogue took place after a story had been related about John taking a trip to New York, having his money stolen on the subway only to discover the fact when attempting to pay his bill in a restaurant called Leone's:

why did John go to New York?

BECAUSE JOHN WANTED TO GO TO LEONE'S.

how did John get to Leone's?

JOHN TOOK A BUS TO NEW YORK AND THEN HE TOOK THE SUBWAY TO LEONE'S.

did anything unusual happen on the bus?
I DON'T REMEMBER ANYTHING.

did anything unusual happen on the subway?

A THIEF PICKED JOHN'S POCKET.

did anything unusual happen at the restaurant?

JOHN DISCOVERED THAT HE COULDN'T PAY THE BILL AND SO HE HAD TO WASH DISHES.

how was John able to take the bus back to New Haven?

## PROBABLY JOHN HAD A TICKET.

Incidentally the system was able to translate the substance of the story into Chinese by simply designing a Chinese interpreter for Conceptual Dependency Theory.

As with Winograd's system we are struck by its ability to 'understand' natural language provided the topic of conversation is well defined beforehand. But how far does this formalism go? Clearly life situations are not just a selection of different scripts all of which have been met on many occasions. At the very least there must have been a first time we met any given situation and clearly in everyday life we are continually meeting novel situations. For example it would be hard to justify a 'what to do when a policeman pulls you over for speeding' script!

Schank and Abelson meet this difficulty with an important idea. They propose that the mechanism which gives rise to scripts is 'plans'. They are also explanations of actions that are intended to achieve a goal. The difference between scripts and plans is that scripts are specific while plans are general.

As with scripts various plans are proposed which have virtually universal application; for example the plan for going to an intended location or more generally changing the state of proximity (to something). These goals are called 'delta goals' or D-goals. Not all goals are D-goals. Many goals are specific to some process as for example in instrumental scripts for preparing food. These goals are referred to as I-goals.

The process of understanding plan-based stories is as follows:

a. Determine the active goal.

b. Determine the D-goals that will satisfy that goal.
c. Analyse input conceptualizations for their potential realization of one of the D-goals.

As an example, consider the story:

John was lost. He pulled his car up to a farmer who was standing by the road.

The first sentence clearly suggests a main goal of finding position. The second sentence is readily interpreted as forming a precondition necessary for John to make an enquiry — clearly one of the possible D-goals which will satisfy the main goal. This kind of analysis has led Schank and Abelson to draw 'goal fate graphs' for stories. These diagrams indicate the sequential appearance, substitution, interruption, failure or successful completion of all the goals mentioned or implied by the story. It seems that 'goal semantics', if we might so call this kind of approach, provides a very good model for much understanding, especially of human behaviour. We feel there is great potential for this formalism, though it will of course have its limitations — consider trying to understand mathematics in terms of goals. Schank and Abelson have even gone a step further in their attempts to understand human behaviour and considered how goals tend to group together into what might be called belief systems — but this goes beyond the scope of our subject.

We have examined how Chomsky, Winograd, and finally Schank and Abelson have taken successive steps in designing a formalism which would provide a framework for using natural language to communicate information. Each formalism proposed has been more complete but has been found to have its limitations.

One observation that we have been able to make through looking at these formalisms is how surprisingly underspecified natural language is — in contrast to the more superficial observation that it is verbally somewhat redundant. This observation highlights how the meaning of language as it is usually understood lies in its relation to a very complex knowledge base which the receiver is assumed to possess. In this context it becomes very difficult to talk about information without specifying 'for whom'.

It is interesting to observe in this context that things we say most often, though sometimes very complex in meaning, can be expressed very succinctly — for example, 'yes', 'I should think so', etc. This fact appears to be an example of applying Huffman's minimum code algorithm, which given a finite number of possible messages, $m_1, \ldots, m_n$ , with probabilities of use $w_1, \ldots, w_n$ respectively, finds a binary code word for each message such that their lengths $l_1, \ldots, l_n$ satisfy $\sum_{i=1}^{n} w_i l_i$ is minimum, implying that communication is most efficient on average. The point about this algorithm is that messages which are more probable are assigned shorter code words, as intuition would predict.

These considerations have revealed a paradox between the understanding of information we have gained so far (as meaning conveyed by language) and the definition proposed by Shannon (1949).

Shannon was studying band widths of communication channels, with a view to maximizing the amount of 'information' that can be transmitted. He was led to conclude that the more expected a transmitted symbol is, the less information it conveys. Thus in a security check transmission it is the indication that some part is out of order which is of importance. Hence for Shannon it is precisely those commonplace phrases in natural language that carry little information. The first point to note is that the Huffman algorithm is working to increase 'Shannon information', for if we expressed a common phrase in a longer form the individual words would convey even less information. But beyond this Shannon's does seem to be a fundamentally different viewpoint, which does not relate so readily to the problem of understanding the meanings conveyed but rather to how economically they can be transmitted. There is no part of Shannon's theory which rules out the possibility that an algorithm capable of 'understanding' the message might need several hours for processing one message, but just a few minutes for a second message of the same length. The answer to the question 'Did I get the job?' might be an example in the human context.

Finally we return to the limitations of formalisms and ask whether it is theoretically feasible to build a system capable of interpreting the complexities of the real world. One way of expressing Gödel's incompleteness theorem is that any finitely defined formal system must be incomplete (while for the real world we assume completeness as in every model!). Hence some properties cannot be recognized by the formalism. In practice the problem is worse, as what usually happens is that a particular formalism is valid only within a particular framework, as in the examples we have considered above. This, however, implies that if we treat the formalism as universal it is not just incomplete, but incorrect. The problem of delineating when it does in fact hold is apparently as intractable as finding a universal formalism.

It is very interesting in this connection that some of Schank's more recent work is concerned with what he calls 'Dynamic Memory', which refers to the significance for human understanding and memory of events which fail to fulfil our expectations, i.e. break the limitations of our present formalism. These events appear to have special significance for humans as they necessarily lead to an adaptation of our understanding. It is this ability of humans to evolve their understanding of the world which is the most elusive and difficult to mimic. It is also a question which has received very little theoretical treatment and yet one which is central to our understanding of information processing and the limitations of formalisms.

## References

Chomsky, N. (1957) Syntactic Structures. Mouton, The Hague.

Schank, R.C. and Abelson, R.P. (1977) Scripts, Plans, Goals and Understanding. Lawrence Erlbaum, New Jersey.

Schank, R.C. (1983) Dynamic Memory. Cambridge University Press.

Shannon, C.E. and Weaver, W. (1949) The Mathematical Theory of Communication. University of Illinois Press.

Taylor, Ann (1982) Language. In Taylor, Ann et al., Introducing Psychology. Penguin Books Ltd.

Winograd, T. (1972) Understanding Natural Language. Edinburgh University Press.

![](/api/attachments/QFEM3QN6/fulltext/images/1f6ec1480f7fe24ca93b33c1564f6d51d8eb9b9856f2d88c41ca55fa2743ac0f.jpg)  
Dr J.S. Shawe-Taylor is currently a Lecturer in Computer Science at Royal Holloway and Bedford New College. He has a degree in Mathematics with Computer Science and a postgraduate degree in Algebraic Graph Theory. He is currently taking an MSc in The Foundations of Advanced Information Technology at Imperial College. His main research areas have been in graph theory and cryptography, and at present are in the semantic theory of programming languages.

Address for correspondence: Royal Holloway and Bedford New College, Department of Statistics and Computer Science, Egham Hill, Egham, Surrey TW20 0EX.
