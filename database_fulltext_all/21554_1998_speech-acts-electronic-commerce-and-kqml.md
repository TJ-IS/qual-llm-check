---
otero_id: 21554
otero_key: "CWXHCUYY"
title: "Speech acts, electronic commerce, and KQML"
authors: "Michael A Covington"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00059-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Speech acts, electronic commerce, and KQML <sup>1</sup>

Michael A. Covington )

Artificial Intelligence Center, The UniÕersity of Georgia, Athens, GA 30602-7415, USA

## Abstract

Speech act theory the study of how utterances function as statements, questions, commands, etc. is increasingly Ž . applicable to software design. KQML, a knowledge interchange language developed with ARPA funding, is based on speech act theory. It differs in significant ways from human speech and conventional EDI, and it can be improved in a number of ways. Although speech act theory is highly relevant to electronic communication, the needs of computers are different from those of humans. Computers need to perform concisely speech acts that are clumsy in human speech, such as arranging communication paths. They also need to recognize speech act types as immediately as possible, whereas human language gets along with clumsy encodings of speech acts into grammar. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Speech act theory; Pragmatics; Natural language; KQML; EDI; Electronic data interchange; Knowledge interchange; Electronic commerce

## 1. Speech acts in electronic communication

Speech act theory—the study of how utterances function as statements, questions, commands, and so on—is no longer just an area of theoretical linguistics; it is finding increasing applications in software engineering. Several groups of researchers are experimenting with knowledge interchange languages based explicitly on speech act theory 7,8,17,12 . <sup>w</sup> <sup>x</sup> Further, Moore 18 has opened an important line of <sup>w</sup> <sup>x</sup> investigation by comparing the repertoire of speech acts used in electronic communications with those used in human speech.

Moore analyzed the illocutionary force of EDI-FACT EDI transactions, S.W.I.F.T. securities transactions, and Apple Events in the Macintosh operating system. He found, perhaps surprisingly, that all of these electronic messages display much the same variety of speech act types as human speech. There are a few gaps; for example, computers do not normally express condolences to each other. But the applicability of human-language speech act theory to electronic messaging, even the internal messages used within an operating system, is impressive.

Nonetheless, electronic communication is not human speech. It is time to look more deeply at speech act theory from the viewpoint of software engineering as well as linguistic description. In this paper, I will raise some methodological points, then examine the usage of speech acts in KQML, a new speechact-based knowledge interchange language, and briefly contrast KQML with conventional EDI.

Table 1

## 2. The central claim of speech act theory

## 2.1. The ‘Vulcan mind meld’ theory of communication

Perhaps the best way to introduce speech act theory is to compare it to a naive view of communication that does not recognize speech acts. On that naive view—known to Star Trek fans as the ‘Vulcan mind meld’—communication is simply the transmission of thoughts or knowledge from one mind to another. When you connect your brain to mine, you know what I know.

That is indeed how computer-to-computer communication has often been approached. Networks allow one machine to mount another machine’s disk drives; EDI forms such as ANSI X.12 9 allow one <sup>w</sup> <sup>x</sup> program to stuff data into variables in another program. Distributed databases enable computers to share non-trivial knowledge structures.

But Vulcan mind melds do not occur in human experience, and they are a poor model of how humans actually communicate, for at least three reasons. First, my thoughts are not your thoughts; they are of no use to you unless I express them in a common language, making appropriate assumptions about background knowledge. This, indeed, is the problem that standard EDI formats and knowledge representations address.

Second, the Vulcan mind meld theory ignores the voluntary nature of communicative acts. I can’t give you all my thoughts; I have to select particular things to say at particular times. Thus, alongside syntax and semantics, every language needs rules of pragmatics, the knowledge of what to say when.

Third, and perhaps most importantly, I can’t just deliver my thoughts to you; I have to tell you what I want you to do with the propositions that I express. If you can’t distinguish statements from conjectures or questions, my utterances will be of no use to you. That is where speech acts come in: effective communication requires accurate recognition of speech acts.

## 2.2. The F P hypothesis ( )

The central claim of speech act theory is that people do not just utter propositions; they perform illocutionary acts such as stating, requesting, commanding, and so forth. Every speech act consists of an illocutionary force F applied to a proposition P. This is known as the F PŽ . hypothesis. The importance of illocutionary force was first made explicit by Austin 2 but was foreshadowed by the semantic<sup>w</sup> <sup>x</sup> theories of the ancient Stoics. Diogenes Laertius, inŽ LiÕes of the Philosophers VII. 65–68, divides utterances into statements, yes<sup>r</sup>no questions, questions seeking information, commands, oaths, acclamations, and exclamations..

Various illocutionary acts with the same or nearly the same propositional content

<table><tr><td>Illocution</td><td>English sentence</td></tr><tr><td>Statement</td><td>The cat is on the mat.</td></tr><tr><td>Question</td><td>Is the cat on the mat?</td></tr><tr><td>Command</td><td>Put the cat on the mat.</td></tr><tr><td>Polite request</td><td>Could you put the cat on the mat, please?</td></tr><tr><td>Promise</td><td>I promise that the cat will be on the mat.</td></tr><tr><td>Guarantee</td><td>I certify that the cat is on the mat.</td></tr><tr><td>Offer</td><td>I&#x27;ll put the cat on the mat if you&#x27;d like.</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td></tr></table>

Moore summarizes the F PŽ . hypothesis as claiming that ‘the outermost logical operator of <sup>w</sup> <sup>x</sup> eÕery utterance everything we could possibly say is notŽ . Boolean, not temporal, not even defeasible—it is an illocutionary force’ 18 . Further, this outermost op- <sup>w</sup> <sup>x</sup> erator is never vacuous; that is, F PŽ . <sup>/</sup> P. Even when stating a fact, you are making a statement, not just voicing a fact.

Table 1 shows several different illocutionary forces applied to the proposition ‘The cat is on the mat.’ Many more illocutions are possible, many of them restricted in various ways; to take an extremely specialized example, christening a ship—which is a speech act—is possible only in a very specific setting.

## 2.3. Some distinctions

Illocutionary force is distinct from grammar, meaning, and perlocutionary effect. Taking the last of these first, the perlocution of an utterance is what it actually accomplishes, such as informing, persuading, dissuading, and the like. Illocutions and perlocutions are closely related, but discrepancies can easily arise. For example, by inviting you to do something in a particular way, I may end up actually dissuading you from doing it. The speaker controls the illocution but only attempts to control the perlocution.

Illocution is also distinct from meaning. Questions about the weather are no different, as far as illocution are concerned, from questions about dogs and cats; the only difference is in the propositional content. Whenever a classification of speech acts becomes excessively fine-grained, one suspects that the classification is picking up distinctions of meaning as well as illocution.

Bierwisch 5 points out that this mistake is espe-<sup>w</sup> <sup>x</sup> cially easy to make when the information content of the utterance refers to a speech act—that is, when P contains another F. Some speech acts refer to others; for example, ‘Please tell me your name’ is a request for a statement. Nonetheless, the utterance itself is one speech act, not a combination of them—it is a request referring to a statement, not a request combined with a statement. Logically, it is request tell nameŽ Ž .., not <sup>w</sup> <sup>x</sup> request <sup>q</sup> tell nameŽ ..

Finally, the encoding of illocution into grammar in English is notoriously non-uniform. Some speech acts are encoded by particular syntactic structures Ž . statements, questions, exclamations ; others are encoded by particular verbs promise, accept, nomi-Ž nate ; and still others, the most specialized, are per-. formed by asserting that one is performing them, such as ‘I hereby dub thee knight.

The requisite distinctions can be subtle. ‘I will go to New York next week’ can be a statement, an offer, a promise, or even a threat, depending on the context. Human language requires elaborate inference in order for the hearer to identify speech acts. In electronic communication, we want to keep the necessary inference as simple as possible.

## 3. Classifying speech acts

The study of speech acts begins with classifying them, and many rival classifications have been proposed 1,4,21,20 . See Ref. 21 for a particularly <sup>w</sup> <sup>x</sup> Ž <sup>w</sup> <sup>x</sup> good overview up to 1983. In his study, Moore used . the classification system of Bach and Harnish 3 ,<sup>w</sup> <sup>x</sup> summarized in Fig. 1.

For Moore’s purposes, this classification is ideal because it makes as many distinctions as possible,

Communicative speech acts Constatives (statements of fact) Assertives, predictives, retrodictives, responsives, suggestives. . . Directives Requestives, questions, requirements, prohibitives, permissives, advisories Commissives Promises, offers Acknowledgments Apologize, condole, congratulate, greet, thank, bid, accept, reject

Conventional speech acts (declarations) Effectives Appoint, nominate, suspend, demote, resign, abdicate, arrest. . . Verdictives Acquit, certify, disqualify, clear, rule, adjudicate... Fig. 1. Speech acts as classified by Bach and Harnish.

thereby enumerating the whole range of human speech acts. But the Bach–Harnish classification is less than ideal for shedding light on how speech acts actually work. In some respects, it is more a collection of data than a theory. Notice the large number of verbs that are in classes by themselves.

A more insightful classification will take into account the fact that speech acts differ along more than one dimension 1,19 . For example, the differ-<sup>w</sup> <sup>x</sup> ence between a command and a polite request, or between a confident assertion and a cautious suggestion, is not a logical difference; it is a difference of strength. Similarly, the difference between a promise and a threat is whether the affected person wants the thing to happen. Indeed, one important dimension is whether the speech act pertains primarily to the state of the speaker, the state of the hearer, or both.

Accordingly, not every distinction calls for another leaf in the Bach–Harnish classificatory tree. An alternative approach is to distinguish a smaller number of basic speech act types and equip each speech act with parameters to describe further aspects of its illocutionary force. One then ends up with a matrix rather than a tree.

What does all this imply for engineering? Three things. First, it is reasonable to want the encoding of speech acts in an artificial language to be syntactically uniform. An utterance should wear its illocutionary force on its sleeve, so to speak, for the convenience of the routines that process it. Second, the set of speech act types should not be too large; instead, parameters should encode subtle variations on basic types. Third, the inference required on the receiving end should be held to a minimum. Entertaining though misunderstandings or ‘comedies of manners’ may be, we do not want them to become a regular part of electronic knowledge interchange.

## 4. Speech acts in KQML

## 4.1. The KQML language

KQML Knowledge Query and ManipulationŽ Language is a Lisp-based language that was devel- . oped as part of the ARPA Knowledge Sharing Effort <sup>w</sup> <sup>x</sup> 10,11,14,16 and has been implemented by several different working groups. I will discuss first the 1993 version 10,11 and then the proposed 1997 revision<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 15 . I shall call these KQML 1993 and KQML 1997, respectively.

The main focus of KQML research so far has been the use of intelligent agents to arrange transport and handling of messages. Accordingly, the knowledge content of a KQML message need not be written in KQML; it can be expressed in Prolog or some other language. The KQML wrapper indicates the kind of message, the intended recipient, the language, the ‘ontology’ knowledge base , and other Ž . parameters. Fig. 2 shows examples from Ref. 11 .

```txt
(ask-one
: content (PRICE IBM ?price)
: receiver stock-server
: language LPROLOG
: ontology NYSE-TICKS)

(ask-all
: content "price(IBM, [?price, ?time])"
: receiver stock-server
: language standard_prolog
: ontology NYSE-TICKS)

Fig. 2. Examples of KQML messages.
```

## 4.2. The KQML performatiÕe set

KQML is based on speech act theory, and message types are indicated by performatives. In natural language, a performative is a verb that you use to perform a speech act by saying you are doing so, as in ‘I hereby promise . . . ’ the concept goes back to Ž . Ž Austin 2 . In KQML, a performative is an operator <sup>w</sup> <sup>x</sup>. whose arguments include the contents of the message. The basic performative set is shown in Figs. 3 and 4.

The first thing one notices is that there is some doubling up of basic performatives: ask-one<sup>r</sup>ask-all, delete-one<sup>r</sup>delete-all, and so on. I shall return to this point.

Some of the KQML performatives correspond closely to basic speech acts in human language, such as tell, ask-if, ask-all, eÕaluate, and achieÕe Žthe last of these requests a change in the physical world, as opposed to requesting a reply or a change in a knowledge base . The distinction between requests. and assertions is blurred; insert, for example, means ‘Put this information in your knowledge base,’ which is close, but not identical, to what we normally achieve by telling someone a fact.

Other performatives are negative, serving to undo other performatives. For example, after telling someone something you can untell it and thereby retract your statement. Similarly, unachieÕe cancels a request for a physical act, and deny cancels any speech act whatsoever. This solves a problem noted by Moore 17 , which is that in a conventional EDI system, it is often impossible to tell someone to disregard an earlier message.

Note that untell is a nested combination of deny with tell, and unachieÕe equals deny achieÕe. I do not think the designers of KQML have fallen into the confusion that Bierwisch warned us about; rather, they are making their vocabulary efficient. Some nested combinations occur so regularly that they deserve their own lexical encodings.

Database technology looms large in KQML, and many of the performatives resemble the user interface of Prolog. KQML provides insert, delete, and numerous tactics for obtaining multiple responses to a query—in a list, in a stream of messages, or even by standing ready to deliver additional answers when asked Ž . standby . Mechanisms for delivering the answers include the ready, eos Ž . ‘end-of-stream’ , and sorry performatives.

<table><tr><td>Basic informatives (constatives)</td></tr><tr><td>tell (share a piece of knowledge)</td></tr><tr><td>deny (retract or negate a speech act)</td></tr><tr><td>untell (retract a statement; equals deny tell)</td></tr><tr><td>Database performatives</td></tr><tr><td>insert (ask recipient to add something to his KB)</td></tr><tr><td>delete (ask recipient to delete a fact from his KB)</td></tr><tr><td>delete-one (ask recipient to delete one of the facts that match X)</td></tr><tr><td>delete-all (ask recipient to delete all facts that match X)</td></tr><tr><td>Responses from recipient</td></tr><tr><td>error (what you said doesn&#x27;t make sense)</td></tr><tr><td>sorry (I can&#x27;t do what you requested)</td></tr><tr><td>(also means “no (more) answers” as in Prolog)</td></tr><tr><td>Query performatives</td></tr><tr><td>evaluate (evaluate an expression; details depend on language)</td></tr><tr><td>reply (I am sending you data to answer your query)</td></tr><tr><td>ask-if (yes-no question)</td></tr><tr><td>ask-about (tell me what you know about X; reply with 1 list)</td></tr><tr><td>ask-one (send me one response that matches my query)</td></tr><tr><td>ask-all (send me all responses that match my query)</td></tr><tr><td>Multi-response query performatives</td></tr><tr><td>stream-about (like ask-about, but reply with a series of messages)</td></tr><tr><td>stream-all (like ask-all, but reply with a series of messages)</td></tr><tr><td>eos (“end of stream,” marks end of series of messages)</td></tr><tr><td>Effector performatives</td></tr><tr><td>achieve (change things to make X true)</td></tr><tr><td>unachieve (you need not make X true)</td></tr><tr><td>Fig. 3. Predefined performatives of KOML 1993.</td></tr></table>

Fig. 3. Predefined performatives of KQML 1993.

Here sorry either means ‘No more answers’, Ž . like Prolog failure, or means ‘I can’t respond to what you said; it’s beyond my computational power.’ It is surprising that the designers tolerated this ambiguity, since there are situations in which it could cause problems. Technically, a server that responds Ž sorry to all communications is KQML-compliant, although the amount of KQML that it implements is essentially zero; a wag has observed that ‘KQML means always being able to say you’re sorry.’.

Still other performatives have to do with establishing communication paths and finding suitable agents to handle a message. Here, perhaps, is where KQML shows the greatest originality. An agent can advertise its own capabilities and ask other agents who can process a particular kind of message, either through ‘brokering’ you send it somewhere for me Ž and send me the result that you get or ‘recruiting . Ž . you tell me whom to send it to . These are activities that require complicated utterances in human language, but the designers of KQML felt, probably correctly, that they are going to be so common in electronic communication that they should be treated as basic.

The KQML performative set is, of course, a classification of speech acts, although it is quite different from that used by Bach and Harnish. The KQML performatives do fit into the Bach–Harnish classification, albeit with some risk of triviality, since many of them are requests. What we see in

![](/api/attachments/CWXHCUYY/fulltext/images/d56670d3e38b75de334a0864597b0339cda9f3f9e18bf82be826d8c9d2a9036e.jpg)  
Fig. 4. Predefined performatives of KQML 1993 continued .Ž .

KQML is a classification developed for a completely different purpose, not for studying human language but for conveying electronic communications concisely.

## 4.3. Parameters in KQML

Each KQML performative is accompanied by parameters that given additional information Fig. 5 .Ž . Parameters identify the sender and recipient, provide tags for pairing up messages with their replies, and identify the language and ontology being used.

More significantly as far as illocution types are concerned, one parameter, force, can be used to mark a speech act as irrevocable. Other parameters could be defined to encode further distinctions in illocutionary force.

## 4.4. KQML 1997

In 1997, Labrou and Finin 15 proposed a revised<sup>w</sup> <sup>x</sup> specification for KQML. The main changes are the following:

<sup>Ø</sup> the semantics is cleaner and more Prolog-like, though still not rigorous; it is based on the concept of ‘virtual knowledge base’, i.e., all the knowledge that an agent has or can infer;

<sup>Ø</sup> ask-about and stream-about are gone, presumably because they do not represent feasible Prolog-like queries;

<sup>Ø</sup> deny no longer means ‘retract a speech act’; instead, it means ‘assert that P is false’, and untell means ‘assert that P is not known to be true’;

<sup>Ø</sup> a number of speech acts have counterparts begin-

:sender symbol identifying the sender

:receiver symbol identifying the recipient

:reply-with identifier that must appear in the reply

:in-reply-to symbol from reply-with field of

:content the content of the message, i.e., P in F(P)

:language language in which content is expressed

:ontology ontology (knowledge base) used by content

:force true if the sender will never retract (deny) this message

Some performatives take additional parameters.

There are defaults for parameters that are omitted.

Fig. 5. Basic set of KQML performative parameters 1993 draft .Ž .

ning with un-, for retracting them; thus delete has been renamed uninsert and unadÕertise has been provided to cancel adÕertise;

<sup>Ø</sup> reply, generator, and monitor have been subsumed into tell, standby, and subscribe, respectively;

<sup>Ø</sup> pipe and break are absent, presumably because they are too low-level, and transport-address is redefined to link it more closely to the activities of agents;

<sup>Ø</sup> the : force parameter is no longer supported, but : from and :to have been added as parameters for forwarded messages.

## 4.5. Critique of KQML

Any evaluation of KQML must take into account the fact that KQML is not a theory of illocution, nor an account of the pragmatics of human speech; it is a tool for prototyping agent-based software. Thus, although it should have a solid theoretical basis, theoretical elegance is not its main goal.

Cohen and Levesque 6 point out three weak-<sup>w</sup> <sup>x</sup> nesses in KQML 1993 version . First, the semanticsŽ . is not formalized and is in some cases seriously unclear. For example, in KQML 1993, it was not clear whether deny tell meant to retract a statement or to assert a negative one. This has been fixed in KQML 1997 by redefining deny; unfortunately, there is no longer a general way to cancel speech acts.

Second, some KQML ‘performatives’ seem to be perlocutions rather than illocutions, or at least have misleading names. For example, achieÕe, broker, and stream-all have names denoting the intended effect rather than the speech act itself. This is not a fatal flaw, but it does represent a path which, if followed further, could lead to serious confusion.

Third, and more seriously, KQML provides no way to express commissives promises , the stuff ofŽ . which commerce is made. This is especially the Ž case now that : force has been deleted from KQML 1997. Cohen and Levesque demonstrate that future . tense statements are no substitute for promises; e.g., in 1979, I could have told you whom I was almostŽ certainly going to marry, but at the time I had not. yet promised to do so.

To this I can add another point: the performative set is too large and lacks orthogonality, encoding in the performatives some distinctions that should have been parameters.

This problem manifests itself in two places. First, instead of the pairs of performatives ask-one and ask-all, broker-one and broker-all, recruit-one and recruit-all, recommend-one and recommend-all, there should be a parameter indicating whether the recipient wants all possible answers or just the first one. One could go further and give this parameter four values: ‘give me only a boolean yesŽ . <sup>r</sup>no answer’, ‘give me one piece of data as an answer’, ‘give me all answers in succession’, ‘give me all answers in a list’. In that case, the four varieties of ask could be combined into one, although there would be some combinations that are not normally used, such as stream asking for a single answer.

Second, as noted, there are a number of pairs of the form X:un-X, but, in KQML 1997, no general mechanism to cancel speech acts. The 1993 sense of deny needs to be reinstated, and the performatives that begin with un- removed unless clearly needed for conciseness.

## 5. Speech acts in ANSI X12

Now consider ANSI X12 9 , a set of standard<sup>w</sup> <sup>x</sup> forms for electronic data interchange already critiqued by others 7,13,17 .<sup>w</sup> <sup>x</sup>

The X12 standard is a set of encodings of hundreds of business forms, such as purchase orders, invoices, bills of lading, educational transcripts, insurance claims, and so forth. Notoriously, X12 fails to make generalizations about the knowledge in these forms. Each form is entirely sui generis, with a separate form number and a separate syntax. Even basic semantic units such as ‘number’ are not defined; instead, there’s a three-digit numeric field here, a five-digit field there, and so on.

Moore 18 showed that EDI messages can per-<sup>w</sup> <sup>x</sup> form a wide variety of speech act types. He studiedŽ EDIFACT, but X12 messages have essentially the same expressive power. However, nothing like the. Bach–Harnish classification is built into X12. Instead, the encoding of speech acts into X12 either misses the point totally, or is brilliantly simple, depending on your point of view. Very simply, each form is a different kind of speech act. The form numbers stand for illocutionary forces together with schemata for the information content. A purchase order is a request, a bill of lading is a constative, and so forth.

The overwhelming advantage of this system—one that should be preserved as far as possible in more sophisticated system—is that any computer can tell at a glance whether a particular X12 message is one that it can process. Apart from that, of course, X12 is quite unsystematic and ripe for replacement with a true knowledge representation language.

## 6. Toward an applicable speech act theory

What can we conclude from all of this? Several things. First, speech act theory provides considerable insight into the workings of electronic communication. More specifically, speech act theory provides an appropriate way to label utterances so the recipient will know, at least roughly, what to do upon receiving a message. The efficiency of X12 comes from a simple, if uninsightful, encoding of speech acts.

Second, although Moore is quite right in pointing out similarities between human and electronic speech acts, the needs of electronic communication are different from those of human speech. Two differences are brought out by the design of KQML. Computers often need to do concisely things that are clumsy and require many steps in human language, such as arranging communication paths to other agents. Further, computer communications are influenced by the nature of databases and knowledge bases, which is why so much of KQML resembles the Prolog user interface.

Third, although it is speech-act-based, KQML does not exploit speech act theory as fully and elegantly as it might. I noted that the set of basic performatives could be made smaller by treating the handling of multiple answers as a parameter rather than a difference of basic performative type. A similar point could be made about some of the performatives that deal with communication; they make unduly fine-grained distinctions at the top level of classification.

Nonetheless, KQML is a good start, and together with other proposed speech-act-based languages, it demonstrates the applicability of speech act theory to electronic communication.

## References

<sup>w</sup> <sup>x</sup> 1 K. Allan, Speech act classification and definition, in: R.E. Asher Ed. , The Encyclopedia of Language and Linguistics, Ž . Vol. 8, Pergamon, Oxford, 1994, pp. 4124–4127.

<sup>w</sup> <sup>x</sup> 2 J.L. Austin, How to Do Things With Words, Oxford Univ. Press, Oxford, 1962.

<sup>w</sup> <sup>x</sup> 3 K. Bach, R.M. Harnish, Linguistic Communication and Speech Acts, MIT Press, Cambridge, MA, 1979.

<sup>w</sup> <sup>x</sup> 4 T. Ballmer, W. Brennenstuhl, Speech Act Classification: A Study in the Lexical Analysis of English Speech Activity Verbs, Springer, Berlin, 1981.

<sup>w</sup> <sup>x</sup> 5 M. Bierwisch, Semantic structure and illocutionary force, in: J.R. Searle, F. Kiefer, M. Bierwisch Eds. , Speech ActŽ . Theory and Pragmatics, Reidel, Dordrecht, pp. 1–35.

<sup>w</sup> <sup>x</sup> 6 P.R. Cohen, H.J. Levesque, Communicative actions for artificial agents, Proceedings of the International Conference on Multi-Agent Systems 1995 , Copy obtained from Ž . http:<sup>rr</sup>www.cs.umbc.edu.

<sup>w</sup> <sup>x</sup> 7 M.A. Covington, Toward a new type of language for electronic commerce. Proceedings of the 29th Annual Hawaii International Conference on System Sciences, Vol. 4, 1996, 329–336.

<sup>w</sup> <sup>x</sup> 8 S.K. Dewitz, R.M. Lee, Legal procedures as formal conversations: contracting on a performative network. Proceedings, Tenth International Conference on Information Systems, 1989, 53–65.

<sup>w</sup> <sup>x</sup> 9 Electronic Data Interchange X12 Standards, draft version 3, release 4, New York: American National Standards Institute, 1993.

<sup>w</sup> <sup>x</sup> 10 T. Finin, J. Weber, et al., Draft specification of the KQML agent-communication language plus example agent policies and architectures, 1993, Manuscript obtained from http:<sup>rr</sup>www.cs.umbc.edu.

<sup>w</sup> <sup>x</sup> 11 T. Finin, R. Fritzson, D. McKay, R. McEntire, KQML as an agent communication language, Proceedings of the Third International Conference on Information and Knowledge Management CIKM ’94 , Copy obtained from Ž . http:<sup>rr</sup>www.cs.umbc.edu.

<sup>w</sup> <sup>x</sup> 12 S.O. Kimbrough, R.M. Lee, On illocutionary logic as a telecommunications language. Proceedings, Seventh International Conference on Information Systems, 1986, 15–26.

<sup>w</sup> <sup>x</sup> 13 S.O. Kimbrough, S.A. Moore, On automated message processing in electronic commerce and work support systems: speech act theory and expressive felicity, ACM Transactions on Information Systems, to appear.

<sup>w</sup> <sup>x</sup> 14 Y. Labrou, T. Finin, A semantics approach for KQML—a

general purpose communication language for software agents, Manuscript obtained from http:<sup>rr</sup>www.cs.umbc.edu.

<sup>w</sup> <sup>x</sup> 15 Y. Labrou, T. Finin, A proposal for a new KQML specification, Technical Report CS-97-03, Computer Science and Electrical Engineering Department, University of Maryland, Baltimore County, 1997.

16 J. Mayfield, Y. Labrou, T. Finin, Evaluation of KQML as an agent communication language, Manuscript obtained from http:<sup>rr</sup>www.cs.umbc.edu.

<sup>w</sup> <sup>x</sup> 17 S.A. Moore, Saying and doing: uses of a formal language in the conduct of business, Dissertation, PhD, University of Pennsylvania, 1993.

<sup>w</sup> <sup>x</sup> 18 S.A. Moore, Categorizing automated messages, Decision Support Systems, this issue.

<sup>w</sup> <sup>x</sup> 19 J.R. Searle, Expression and Meaning: Studies in the Theory of Speech Acts, Cambridge Univ. Press, Cambridge, 1979.

<sup>w</sup> <sup>x</sup> 20 M. Ulkan, Zur Klassifikation von Sprechakten: eine grundlagentheoretische Fallstudie, Tubingen, Niemeyer, 1992.¨

<sup>w</sup> <sup>x</sup> 21 J. Verschueren, Review article: speech act classification, Language 59 1983 166–175.Ž .

![](/api/attachments/CWXHCUYY/fulltext/images/a4a9a2566ad7018534c34a0bc7d021f2aeacb1a1bc95d1c0a3da53dc57a35b7b.jpg)  
Michael A. Covington is associate director of the Artificial Intelligence Center of the University of Georgia, where he does research on computational linguistics and logic programming. He is the author of Natural Language Processing for Prolog Programmers ŽPrentice-Hall, 1994 ..
