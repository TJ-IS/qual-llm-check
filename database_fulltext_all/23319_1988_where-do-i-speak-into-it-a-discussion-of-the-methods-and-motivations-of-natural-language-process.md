---
otero_id: 23319
otero_key: "V2KRWYWB"
title: "“Where Do I Speak Into It?” – A Discussion of the Methods and Motivations of Natural Language Processing"
authors: "Matthew G Johnson"
year: "1988"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1988.37"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Personal View "Where Do I Speak Into It?" – A Discussion of the Methods and Motivations of Natural Language Processing

Matthew G. Johnson, Imperial College of Science and Technology

'Where do I speak into it?' – a perfectly honest question posed by an elderly gentleman when first encountering an IBM PC. We as computer scientists may scoff at his naivete; however, this is often the image given to us by such dependable sources as 'Star Trek' and 'Star Wars'. But why do our computers not understand English? And even if the technology were open to us, why would we want them to? Certainly there are a number of reasons why we should not.

If we wish to give precise information, English is often imprecise and ambiguous. Consider the following:

One teacher takes every pupil in the fifth form.

One woman gives birth in the United States every five minutes. If we could only find her we would have the population problem solved!

and compare the first with similar statements in first order predicate logic.

Here the scope of quantification is precisely specified, whereas in the first case we were left simply to deduce it from the context (more of this later). We could also consider the old favourite:

For sale: Large Alsation, eats anything, likes children.

If it were not for the knowledge that no one would sell a man-eating dog, it would be a valid inference that this Alsatian ate children.

Even if we were able to resolve these problems, either by further querying or by a large knowledge base (not necessarily rule-based), it is likely that such an implementation would require massive amounts of both processing power and memory. Most systems implemented so far have only dealt with small subsections of English, such as questions on one particular database, even then using a much restricted language. Those used on a broader domain, such as automatic translation, have required an expert to 'adjust' the machine output; such 'adjustments' often took longer than the original translation.

But having developed a moderately competent 'natural language' system, what would we do with it? It would be well to remember the public reception of the Austin Maestro, one of the first cars to incorporate a human speech module. Most found its monotone voice so irritating that they had to turn the thing off. Would our system not be equally insufferable, incessantly requiring clarification of what we regarded as obvious? Consider a common piece of PC software such as a spreadsheet. To operate such a thing by means of English would be both slow and prone to error (and very infuriating). Innovations such as icons, pull-down menus, and multiple windows, have done much more for such a package than natural language processing is ever likely to do, and at a much lower price in terms of memory and processing power.

The arguments given above are very powerful, and must be given due credence. However, if we pause to consider the problem in broader context, and think not of present computing technology and the people who use it but about the world in general, we will realize that it is full of people thinking, speaking, and writing in human languages. The first (and for many people the only) language that they know and use is that which they learnt at their father's knee. If we are to neglect this, masses of information and communication will always remain out of the grasp of computers (at least in comprehension).

It might be just to class such a hope as that of the alchemist searching to transmute iron into gold. Such a pursuit would have been highly profitable had it succeeded, but as we now know it was doomed to failure. Many years were spent in this pursuit, perhaps uselessly although it did give rise to the science of chemistry. Are we then to give up all hope? I suggest not, and for one very important reason – that systems dealing with restricted domains are in fact useful. We can thus build such limited applications in the knowledge that it is possible to put them to real use, and in doing so progress towards larger goals. One particularly apt field, surprisingly enough, is that of database query systems, an example of this being the GUS developed at Xerox Palo Alto (described later). The reason for its aptness is that the semantic base is normally covered by the database itself, and that inputs to it are of a restricted vocabulary, normally in the form of one-sentence queries. The advantage of such a system over a conventional one is that although formal languages are very precise they are often cumbersome, especially for long queries, and require a translation by the user of an initial question which, if not written in English, is certainly conceived in it.

If we have decided that we do in fact wish to study the problem of analysing natural language, how do we go about it? As promoted by Chomsky the analysis is normally broken down into two main sections: syntax and semantics. The first is concerned with grammatical structure and the second with meaning. Unfortunately it is often impossible to untangle them when dealing with natural language processing. That is not to say that the division is a false one. When approaching a complex subject such as this one, it is often sensible to divide it up into more manageable parts, and this is no exception. However, I reiterate that treating them as independent processes is likely to lead to failure. Consider the following:

Bob washed the dishes in the sink.

Bob washed the dishes in an apron.

Syntactically it is impossible to decide whether it was the dishes or Bob that were in the sink. The decision that it was the dishes is totally a semantic one. Why then should we bother constructing a syntactic analysis at all? An average person when given the words of the above sentence would reconstruct its meaning easily. However such sentences are small in number, and syntax must often be invoked to resolve ambiguity. Consider the next sentences:

The horse raced passed the pavilion.

The horse raced passed the pavilion jumped over the gate.

Flying planes are dangerous.

Flying planes is dangerous.

In the first example, by adding on four words to the end of the sentence we have totally changed its meaning. The words raced and jumped can both be used as past participles or simple past conjugations, and it is necessary to look at their position in the sentence to determine which of these it is. In the second we have a possible ambiguity between flying planes as a plural compound noun, and as an action. It is only the case of the following verb which resolves the problem.

We have shown that in any non-trivial natural language system, an understanding of both syntax and semantics will be essential to proper analysis. In any real system it is likely that these parts would be highly interlinked; however, for simplicity the two parts have been separated in the following text.

## Syntax

How could we represent a sentence in English? Consider the following sentences:

John lives.

John eats a tomato.

All boys like girls.

The first can be separated into subject and verb, the second into subject, verb and object etc. It would surely be impossible to list all the possible ordering of words explicitly and so instead we may use a system of productions; every sentence consists of a subject and a verb phrase; every verb phrase can be made up of either an intransitive verb, or a transitive verb followed by an object; a subject or object is a noun phrase where . . . or, more succinctly:

<sentence> ::= <noun phrase><verb phrase>

<verb phrase> ::= <intrans verb> | <trans verb> <noun phrase>

<noun phrase> ::= <proper noun>|<determiner><common noun>

(where the vertical bar stands for or)

Such a grammar is called context free, as the productions do not depend on surrounding words (like the subject in the case of <verb phrase>). As we can see from the third sentence, this causes a problem; how do we make the subject and verb agree? One way would be to alter the productions so that we had two options for each sentence (singular and plural) and then two parallel sets of rules for noun and verb phrases. Although this would solve the problem, it is very inelegant and does not really express the concept. Instead, the grammar can be augmented in order to cope with such cases. The most widely used of such methods is Wood's Augmented Transition Network; however, I choose to discuss an alternative approach derived from PROLOG, definite clause grammar (DCG) (see Pereira and Warren, 1980).

Here, in addition to the symbols of the context-free grammar, we allow the non-terminals (e.g. <verb phrase>) to carry parameters and can insert conditions on the use of productions enclosed in braces thus []. Terminals (i.e. words) are enclosed in square brackets thus []. We can now produce a grammar to deal with the three sentences above (in fact, this is a program that could be run by PROLOG):

sentence --> noun phrase(Number),verb phrase(Number).

verb phrase(Number) -->

intrans\_verb(Number);

trans\_verb(Number), noun\_phrase(Any).

noun phrase(Number) --> proper noun,[Number=singular]; determiner(Number),common noun(Number).

intrans\_verb(singular) -->[lives].

intrans\_verb(plural) -->live.

trans\_verb(singular) -->[eats];[likes].

trans-verb(plural) -->[eat];[like].

determiner(singular) -->[a];[the].

determiner(plural) --> [all];[the];[]

proper-noun -->|John|.

common noun(singular) --> [girl]; [boy]; [tomato].

common noun(plural) --> [girls];[boys];[tomatoes].

(here or is represented by a semi-colon)

Another possible way of analysing syntax is to view sets of similar sentences and consider them as modifications or derivations of each other. Starting from a simple assertion such as:

John is eating an apple

we can derive a passive form:

An apple is eaten by John

a past tense:

John ate an apple

a pluperfect:

John had eaten an apple

even a pluperfect passive:

An apple had been eaten by John.

Now instead of writing ‘An apple is eaten by John’ we could say, ‘John eats an apple by passive’, and view these two sentences as equivalent relative to a transformation. There are many examples of such transformations in English – a review of some are given below:

1. Imperatives:
You do your homework ->Do your homework!
You are good. ->Be good!

2. Why not:
Why do you not clean it? ->Why not clean it?

3. Wh . . -fronting:
John bought which coat? ->Which coat did John buy?

4. CCS (conjoined coreferent subject):

Mary hit John then she hit Joe.
->Mary hit John then hit
Joe.

5. Extraposition:

That Mary screamed frightened me.
->It frightened me that
Mary screamed.

Such a ‘transformational’ grammar as proposed by Chomsky is very attractive in that it reduces many of the structures that we have to consider. If we take a basic set of production rules and transformations, and try to manufacture a complete set of productions from them, we are likely to find we have more than the product of the two for our eventual set. What is more, such transformations give a semantic meaning by grouping like sentences, that is sometimes not evident in plain productions.

Having devised a schema for our grammar, we are posed with the problem of fitting it to an arbitrary sentence. Such as operation is called parsing, and there are two main techniques for doing this.

## 1. Top-down

This is essentially a generative procedure. We start with the most basic unit, and start to produce sentences from it while trying to direct this creation toward the sentence at hand. For the DCG this is simple: since order is preserved, we can unfold the left/right most non-terminal until we reach a terminal and then compare it with the left/right most word in the sentence. If it does not match we can backtrack and try some other possibility. With the transformational grammar this is nigh impossible, since there is no sensible way of directing the productions towards the given sentence.

## 2. Bottom-up

Starting with the words of the original sentence, we try to fit rules to them in reverse, so as to work towards the most simple structure. Although this is a perfectly feasible method for DCGs, the top-down method has tended to dominate, probably due to the fact that PROLOG implements it in this way. For transformational grammars, however, this is the only technique available and even then it is not an easy one. The basic hitch lies in the fact that many transformations delete information, and in parsing it is necessary to reconstruct this information. Nevertheless there have been attempts at constructing parsers, such as Petrick's MITRE. After having produced an attempt at a reverse transform, MITRE had to check it by means of applying a forward transform. Many of the attempts thus produced were eliminated at this stage, leading to large inefficiencies.

## Problems

Although there has been some success generated by use of the methods outlined above, there are still a number of basic problems in parsing. Some of these are given below:

1. Co-ordination (i.e. sentences using 'and/or')
Bill and Jane ate the meal.
Bill cooked and Jane ate the meal.
Bill cooked and ate the meal.

It is fairly clear that English allows us to insert an and almost anywhere in the sentence. If we are to deal with this in a DCG, one way is to insert possible co-ordination in every production; however, this is not only inelegant but is also highly inefficient. One way to solve this has been to use categorical grammars, as proposed by Bar-Hillel, which cope far better with this problem.

## 2. Adjuncts

I saw the man along the pier with a telescope

Here the prepositional phrases, along the pier and with the telescope can be attributed in many ways to the subject, object or verb of the sentence. Did the pier have the telescope, or was I looking down it? Was I or the man on the pier when I saw him, or was I simply sighting along it. This problem is simply not soluble from a syntactic approach. However, if faced with such a problem we must consider whether it is worth generating all possible parses before we start on semantic analysis, as many of these could be thrown away immediately.

## Semantics

The problem of a semantic interpretation of language is immense, and can be seen to be as formidable as the problem of a general artificial intelligence. However there have been a number of successful systems dealing with restricted domains. Rather than deal with these immediately, I will first illustrate some of the very basic-level problems involved in the understanding of language.

## Anaphora (or repeated reference to an entity)

We will start with a few simple examples:

Bob ate an apple pie. It was delicious.
Bob ate an apple pie. He was very full.

It is very easy to see what each of the pronouns in the second sentence is referring to. It is simply a matter of a syntactic check: male people are referred to by a he, and objects by it. However, even at this syntactic level, there are some problems. One of these is the use of each or every:

Each student bought some cherries. They were ravenous.

Although the only plural noun in the first sentence is cherries, we realize that they refers to the implicit plural in each student as it is unlikely that cherries could be ravenous.

Another problem is when pronounal references can be made to nouns in the same sentence:

Jake left town after he robbed the bank. He left town after Jake robbed the bank. After Jake robbed the bank, he left town. After he robbed the bank, Jake left town.

Jack likes him.
Jack likes himself.

In the first set we see that the only case in which he cannot refer to Jake is when it both precedes and dominates the clause containing Jake (this rule was devised by Langacker). In the second set, we see that the object of the verb can only refer to the subject, if it is of a reflexive type, i.e. ‘-self’.

However, such syntactic checks are often insufficient to distinguish between the various possibilities. Consider the following:

The city councilmen refused to give the women a permit for a demonstration because they feared violence.

The city councilmen refused to give the women a permit for a demonstration because they advocated violence.

Here, by changing one verb, we radically change our understanding so as to fit in with our domain knowledge. In the second case we even invent a group of people, possibly led by the women, so as give a meaning to the pronoun they. Similarly in the following problem:

The new fighter took off from the Kennedy. It flew beautifully.

Here again, knowledge of the domain is essential.

However, pronouns are by no means the only form of anaphora. Not only may other nouns be used but also they do not even have to refer to the exact object in question:

I invited ten friends to my birthday party. All of the guests were hungry when they arrived.

Peter picked a punnet of peaches. Several were over ripe.

Peter stole a strawberry, and Mary stole one as well.

In the second sentence the several refers to some of the peaches in the punnet, whereas in the third sentence the one refers only to the idea of a strawberry and not to the object itself. Such reference is named 'description' anaphora as opposed to 'entity' anaphora.

## Quantifiers

As we saw at the beginning of this discussion in the example of the fecund American women, the precedence of quantifiers can be vitally important. Although this is also heavily dependent upon the context, there is one rule which can be of use. That is simply the order of the quantifiers in the sentence.

Everyone in the room speaks two languages.

Two languages are spoken by everyone in the room.

In the first sentence we see that two languages are spoken, but that the particular languages may depend upon the person; in the second sentence there is an implication that there are two prescribed languages spoken by everyone. But this interpretation is certainly not concrete and could be altered by an appropriate context.

## Ellipsis

In normal English it is usual to leave out various parts of a sentence when those parts are redundant or could be assumed.

Mary ate a cherry pie, and John – a fairy cake.

You think he'll be here tomorrow. I predict – Friday.

Is John taller than Mark? Is William -?

Reinserting the lost information just requires common-sense – unfortunately this is often lacking in computers!

## Intention

When making a request to someone for some information, we very rarely ask a direct question. In fact it is often considered as very impolite to do so. When we want to know the time, we might ask someone:

Do you know the time?

If the person addressed did in fact possess this information, we would be somewhat rebuffed if we received the answer 'Yes'.

Consider a possible dialogue between a naive train information system and an irate South London commuter:

Could you tell me when the next train to Blackfriars departs?

Very honestly, the system replies:

Yes I am certainly capable of that.

Becoming more frustrated the commuter tries again:

Look! I want to know the time of the next train to Blackfriars.

to which our system replies with compassion:

I understand your desire Sir.

At this stage the commuter picks up his heavy umbrella, and rams it through the screen. So much for hi-tech!

We now examine several practical systems and look at how they have overcome some of the problems mentioned above. The first of these is LIFER (language interface facility with ellipsis and recursion) which was developed at SRI by Hendrix (Hendrix et al., 1978) for producing a natural language interface for database retrieval. The second is a method called Scripts, derived by Schank (Schank and Abelson, 1977) to analyse texts covering stereotypic situations. And lastly GUS (genial understanding system) produced at Xerox, Palo Alto (Bobrow et al., 1977), to play the part of a travel agent giving information and making bookings.

## Lifer

This system uses a semantic grammar to distinguish various interpretations. In this grammar, instead of simply indicating the parts of speech such as noun, adjective etc. we also specify the types; that is, we use terms such as 'ship' and 'attribute' instead of just 'noun' and 'adjective':

<query> --> What is the <attribute> of <ship>?

<query> --> Is <ship> a <class>?

<person> ={Santa Inez, Kennedy}

<attribute> = {length, speed}

<class> ={frigate, destroyer, carrier}

This can help us with both ellipsis and anaphora. Here are some example:

What is the speed of Kennedy?

Is it a destroyer?

What is the length of Santa Inez? Of Kennedy?

In the first example the system is faced with the problem of co-referencing the pronoun it. However, since the grammar stipulates that this part of the sentence must be of type <ship>, we have no problem in linking it to the Kennedy. In the second example we have a case of ellipsis. On failing to parse this query, LIFER assumes that it will be of the same type as before, and tries to superimpose the fragment on to the previous question. It thus constructs a new query which it passes to the database. This technique is limited, however, as many cases of ellipsis do not repeat the structure. Consider the following.

Did John have any chest X-rays?

Yes three.

Any clouding or thickening?

Here the fact we are referring particularly to John's X-rays is omitted. We will have to do more than

slot-filling to infer this.

## Scripts

Consider the following scene from a restaurant:  
The customer gave his order to the waiter. Thirty minutes later he returned with the wrong entree. The man was furious and stomped out of the restaurant.  
We know from the context that he refers to the waiter and the man to the customer, but how do we represent this knowledge so as to allow it to be used by a machine? Scripts are an attempt to do this. The idea is to tabulate the major actors and props and the roles they play in the scene. Schank's system used the primitive actions of his conceptual dependency theory which I have omitted for the sake of clarity.

<table><tr><td colspan="4">Script: RestaurantTrack: Coffee Shop</td></tr><tr><td>Props:</td><td>TablesMenuFoodBillMoney</td><td>Roles:</td><td>Customer (C)Waiter (W)Cashier (M)Owner (O)</td></tr><tr><td>Entry conditions:</td><td>S is hungryS has money</td><td>Result:</td><td>S has less moneyO has more moneyS is hungryS is pleased(optional)</td></tr><tr><td colspan="4">Scene 1: Entering</td></tr><tr><td colspan="4">S goes into restaurant</td></tr><tr><td colspan="4">S looks for empty table</td></tr><tr><td colspan="4">S decides where to sit</td></tr><tr><td colspan="4">S goes to table</td></tr><tr><td colspan="4">S sits at table</td></tr><tr><td colspan="4">Scene 2: Ordering</td></tr><tr><td colspan="2">(menu on table)</td><td colspan="2">(menu not on table)</td></tr><tr><td colspan="2">S takes menu</td><td colspan="2">S calls WS asks for menu</td></tr></table>

## GUS (genial understanding system)

We conclude with a look at a complete system intended to act as a travel agent. GUS is a mixed initiative system, in that both it and the customer may ask questions. GUS will start by asking questions but will accept a question in place of an answer if the customer is in doubt. In addition GUS is frame driven; when it has no outstanding questions to answer GUS checks for the next empty slot in the current frame and tries to fill it. An example of its frames is given below.

Booking frame

<table><tr><td>Slot</td><td>Type of value</td><td>Procedures</td></tr><tr><td>Homeport</td><td>city (default: Palo Alto)</td><td></td></tr><tr><td>Foreignport</td><td>city</td><td></td></tr><tr><td>Outwardleg</td><td>trip leg</td><td>to fill: create trip leg frame</td></tr><tr><td>Inwardleg</td><td>trip leg</td><td>to fill: create trip leg frame</td></tr><tr><td colspan="3">Trip leg-frame</td></tr><tr><td>Slot</td><td>Type of value</td><td>Procedures</td></tr><tr><td>Fromplace</td><td>city</td><td>to fill: find from Homeport</td></tr><tr><td>Toplace</td><td>city</td><td>to fill: Ask client</td></tr><tr><td>Traveldate</td><td>date</td><td>to fill: Ask client</td></tr><tr><td>Departurespec</td><td>timerange</td><td>to fill: Ask client when-filled: propose flight by departure</td></tr><tr><td>Arrivalspec</td><td>timerange</td><td>when-filled: propose flight by arrival</td></tr><tr><td>Propsedflights</td><td>(set of flight)</td><td></td></tr><tr><td>Flightchosen</td><td>flight</td><td>to fill: Ask client</td></tr><tr><td>Traveller</td><td>person</td><td>to fill: Ask client</td></tr></table>

GUS: Hello. My name is GUS. I can help you to plan a simple trip by air. Where do you want to go?

Client: I want to go to San Diego on May 28.

GUS: What time do you want to leave?

Client: I must be in San Diego before 10 am.

GUS: Would you like PSA flight 102 that leaves at 7.50 am and arrives at 9.15 am?

Client: When is the next flight

GUS: Air California flight 310 that leaves at 8.30 am and arrives at 10.00 am.

Client: I'll take the first one.

Although GUS has the basic goal of trying to complete its form, it will accept direct questions and give them immediate priority before returning to its main goal. It thus allows a much more natural dialogue than would otherwise be possible.

## Summary

As already stated, it is clear that both syntax and semantics will be required in any reasonably sized natural language system, and that many of the possible ambiguities will need some form of domain knowledge in order to clarify them. It is not surprising that human language has a totally different form from that of computer languages – the former is organic, and the latter is preordained for a particular purpose. It is inevitable that when something is used frequently it will be substituted by something simpler. When it is possible to distinguish between a number of possibilities from context, we will not strive to make this distinction in words as such effort would be wasted. We have an inherent interest in reducing our workload, because it allows us to communicate at a faster rate, and from a broader perspective it is essential for such an organic entity to be compacted at times if it is not to grow too unwieldy.

Perhaps, though, it is more interesting that unlike other activities associated with the brain, such as image processing and motor co-ordination, natural language processing has been so amenable to the algorithmic techniques presented above. Such conventional techniques and their associated computers have failed largely to compete with the mastery of the human brain on other such apparently simple problems. I venture that maybe this is not as surprising as it seems. If, as some linguistic philosophers would suggest, our power to think depends largely on the power of the language we use, is it so astonishing that some of the fruits of our cognition resemble and hence more easily comprehend that initial source?

## References

Bobrow, D., Kaplen, R., Ray, M., Norman, D., Thompson, T. and Winograd, T. (1977) GUS, a frame driven system. Artificial Intelligence, 8.

Hendrix, G., Sacerdoti, D., Sagalowicz, D. and Slocum, J. (1978) Developing a natural language interface to complex data. ACM TODS, 3, 2.

Pereira, F. and Warren, D. (1980) Definite clause

grammars for language analysis, a survey of the formalism and a comparison with augmented transition networks. Journal of Artificial Intelligence 13.

Schank, R. and Abelson, R. (1977) Scripts, plans goals and understanding. Lawrence Erlbaum Associates., Hillsdale, NJ.

![](/api/attachments/V2KRWYWB/fulltext/images/0030e01b956b5bd7000ddad80f8a48d6c2e6b46d6340975a3f61fc73c7d2d3d5.jpg)

## Biographical notes

Matthew Johnson gained a bachelor's degree with honours in the Mathematical Tripos at Robinson College, Cambridge. He is now studying for a master's degree in Advanced Information Technology at Imperial College, under a grant from the Department of Education for Northern Ireland. His current work is on the use of temporal phrases and tenses in English.

Address for correspondence: Imperial College of Science and Technology, 180 Queen's Gate, London SW7.
