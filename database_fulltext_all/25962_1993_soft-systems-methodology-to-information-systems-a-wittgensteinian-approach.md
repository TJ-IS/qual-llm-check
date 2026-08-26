---
otero_id: 25962
otero_key: "ZBMEDBUD"
title: "Soft systems methodology to information systems: a Wittgensteinian approach"
authors: "F. H. Gregory"
year: "1993"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1993.tb00122.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Soft systems methodology to information systems: a Wittgensteinian approach

F. H. Gregory

Warwick Business School, University of Warwick, Coventry CV4 7AL, UK

Abstract. A logical foundation for information system design requires a theory of meaning. Ideational theories attach meaning to the ideas in the private world of a conscious subject. By contrast Wittgenstein held that language and meaning were primarily public and that a private, purely subjective, language was impossible. The iterative debate among stake-holders that takes place in the practice of soft systems methodology (SSM) can be understood as a Wittgensteinian language game in which meaning is created not just discovered. The conceptual models used in SSM can be developed into logico-linguistic models which express stipulative definitions. These definitions can be taken as a logical basis for information system design.

Keywords: axiomatic system, conceptual model, information system design, language game, logico-linguistic model, meaning, private language, soft systems methodology.

## 1 INTRODUCTION

## 1.1 Objectives

The main thrust of this paper is an attempt to provide a sound logical foundation for the use of soft systems methodology (SSM) in information systems (IS) design. It is written in the belief that the major methodologies in current use, such as structured methods and information engineering, do not meet current demands and that information system design based on SSM can provide a viable alternative. It will be argued that attempts to use SSM for information system design (Wilson, 1990; Avison & Wood-Harper, 1990) are inhibited by the limited power of the logical connectives in the SSM conceptual models. This could be overcome by increasing the stake-holder input and producing logico-linguistic models. These models will have the logical power to form the basis for the derivation of an information system design.

The paper will be concerned with philosophical logic, that is questions about how logic relates to language and how language relates to the real world. It will not be part of the scope of this work to discuss the foundations of logic itself. Metalogical questions about the consistency and completeness of systems of logic will not be discussed. It can be taken as a premise of the argument that generally accepted logics, such as the propositional calculus, can be consistent. No claims are made as far as completeness is concerned, indeed it is arguable whether completeness is desirable in an information system.

## 1.2 Approaches to SSM and IS design

In the overview of the UKSS SSM and IS seminar (Mingers, 1992) logico-linguistic modelling was classified as one of the putative methods for front-ending SSM onto structured design methods. While this possibility is not discounted, preliminary work conducted since the seminar indicates that logico-linguistic models, when suitably developed, can act as a substitute for, rather than a step towards, data-flow diagramming and entity relationship modelling. Logico-linguistic models can be expressed in the predicate calculus (Gregory, 1993b). As the predicate calculus forms the basis of programming languages such as PROLOG and forms a theoretical basis for relational data bases, it seems plausible that an IS design, and software specifications, can be obtained directly from a logico-linguistic model.

Mingers describes another approach which consists of embedding structured methods into SSM. With this approach SSM guides the whole project, which may contain hard elements. This idea of embedding is not incompatible with logico-linguistic modelling if a hierarchy of models is understood. For example in the ILSD project Checkland (1989, Fig. 4) gives a model of a system to set up and run an information system. This is not a model of the information system itself (unless, of course, the stake-holders are building an information system to build an information system). A model of what would actually run in computer terms would be at a lower level. This lower level model could be built within the context of the wider model.

## 1.3 Meaning and IS design

The foundation of any applied logic is inexorably tied up with meaning. The literature of logic and, to a certain extent, artificial intelligence abound with elaborate formalisms which have only a tenuous relation to practical problems. An account of meaning will provide the grounding for logic and information system design. It will be argued that the SSM conceptual model building process is a type of Wittgensteinian language game in which a new language is created to describe the problem situation. Given this, the model building will express meaning that can be used as the basis for the logic needed for an IS design.

Connecting Wittgenstein with IS design is not new but other writers have tended to emphasize Wittgenstein's work on the contextual aspect of language (see Hanseth, 1991). Wittgenstein's emphasis on the study of language as it is used largely gave rise to speech act theory. Speech act theory is now employed in modelling for IS design (Auramäki et al., 1988). Here language game theory is employed to help the analyst understand the meaning of terms used in the context of ongoing activities. In this paper a different role will be considered, that of a language game as preliminary to new activities in an existing situation or new activities in a new situation.

It was a fundamental principle of Wittgenstein's later philosophy that the creation of meaning was a public event. This is the aspect of his theory that is relevant to SSM. The iterative debate in which the conceptual models are built is a public event that creates meaning.

Contrary to the later Wittgenstein, subjectivist theories of meaning assert that the determination of meaning is essentially private. This needs to be qualified as the word 'subjective' in information systems literature is apt to do more to confuse than to clarify. We find that 'subjective' is sometimes used to stand for 'private' and sometimes used to stand for 'individual'. That meaning is subjective in the sense of 'individual' is hardly in dispute. It is obvious that different individuals mean different things by the same utterance and that to say that a term is meaningful is to imply the existence of at least some individual people.

The contention that meaning is subjective in the sense of 'private' is called 'the ideational theory' by Grayling (1990). He describes it as:

'The theory . . . that language is an instrument for reporting thought, and thought consists of successions of ideas in consciousness. Ideas are private; only I have access to my own thoughts. Therefore to communicate our ideas to each other we need a system of intersubjectively available sounds and marks, so connected to ideas that the proper use of them by one person will arouse the appropriate ideas in the other person's mind. Accordingly, what a word means is the idea with which it is regularly connected.'

Ideational theories reached their most rigorous exposition in the theories of logical atomism and logical positivism which were propounded in the 1920s and 1930s. Wittgenstein's early work (Tractatus Logico-Philosophicus, 1922) was very close to these movements. However, in the 1940s Wittgenstein changed his position and attacked the ideational theory. The main instrument of this attack was the private language argument. In Anglo-American analytical philosophy this argument is generally regarded as having shown that ideational theories are false. However, they now seem to be appearing in writing relating to IS design.

## 1.4 Plan of the paper

The first part of the paper expresses a concern that ideational theories are beginning to appear in work on the connection between meaning and IS design. The work of Stamper is briefly discussed because despite a good deal of similarity between Stamper and Wittgenstein they differ in important particulars. The contrast between the ideational theory and Wittgenstein's is described. Wittgenstein's argument against the ideational theory is an old one but quite complex. For those readers who are not familiar with the private language argument a summary set in its historical context is given in the appendix. A consideration of Wittgeinstein's theory of truth shows that even formal systems can be regarded as language games. The first three sections of part 1 seek to establish that it is the language game theory of meaning, and not the ideational theory, that is correct.

Part 1 continues with an argument for a Wittgensteinian account of SSM model building. It is argued that one of the products of the SSM iterative debate is an agreement about how the problem situation should be described. Understood as a language game the debate is not merely a mechanism for the analyst to learn what the clients think but creates an agreed framework of stipulative definitions. The last two sections of part 1 seek to establish that Checkland's descriptions of the logical status of SSM models and the actual process of building the models are both compatible with the language game theory but not with the ideational theory.

Part 2 is concerned with expressing SSM conceptual models in a formal language. As computer software requires a logical language, the formal expression of SSM models is a first step towards computerized information system design. The section begins by considering some logical problems in the structure of the models. It is argued that these can be overcome by adding more logical connectives. A more powerful model, a logico-linguistic model, can be built using the SSM iterative debate. The logico-linguistic model can be formally expressed in the proposal calculus. A practical procedure for converting a conceptual model into a logico-linguistic model is described. Part 2 seeks to establish that SSM conceptual models can be developed in such a way that their logical structure will be compatible with the language game theory of meaning.

Part 3 considers how the work in the previous sections can be developed towards a system for information system design. The shortcomings of the propositional calculus are described. The need to establish a system that will deal with the problem of mapping conceptual models on to the real world is pointed out.

## 2 PART 1: THEORIES OF MEANING

## 2.1 Connotation and denotation

The word 'meaning' has a wide range of usage in the English language and only part of that range will be relevant to the arguments in this paper. We will be concerned with meaning only in so far as it is about understanding of the elements in a language. These are, for example, words, terms, sentences and statements. We shall not be concerned with the following types of usage: meaningful relations between lovers, a meaningful action, what a red sky at night means.

Meaning can be broken down into sense and reference. Frege made this distinction with the terms 'sinn' and 'bedeutung' (1892), J. S. Mill with the terms 'connotation' and 'denotation' (1943) and the terms 'intension' and 'extension' are also used to make the same distinction. This distinction is now part of standard logic textbooks. Proper names have denotation but no connotation, but general terms have both. 'A general or class term denotes the objects to which it may correctly be applied . . . The properties possessed by all of the objects in a term's extension are called the intension or connotation of that term' (Copi, 1968). A simpler way of putting this is that sense and connotation are concerned with the relation of terms to other terms, while reference and denotation are concerned with the relation between terms and objects or events.

## 2.2 The ideational theory revived

The ideational theory has an intuitive plausibility for modern Western people, but as Grayling points out 'The word "idea" entered into ordinary English usage only a few centuries ago, until which time it had been strictly a philosophical term of art'. It is not until the theory is worked through that its initial plausibility is seen to be chimerical. One would expect the ideational theory to appeal to a computer scientist who is just beginning to come to grips with the wider aspects of information system design. When the word 'subjective' appears in the context of meaning in the information systems literature the author is often taken a tacit ideational stance.

Nevertheless, a tendency towards the ideational position is not confined to writers unfamiliar with the theory of meaning. For example, a fairly recent paper on semiotics by Ronald Stamper (1987) seems, at first glance, very close to Wittgenstein. Stamper emphasizes agreement and context as essential to the understanding of meaning. He also explicitly disavows the ideational theory (the position he calls 'psychologism'). However, a close attention to the paper indicates a tacit ideationalism. This is evident when we consider what he has to say about Tarski's theory of truth. This theory can be expressed very crudely as the theory that a statement is true if and only if it refers to an actual state of affairs. Thus:

'Snow is white' is true if and only if snow is white.

Stamper attacks this theory because he thinks it makes two big assumptions:

'There is a definite, independently existing world (for without it we cannot resolve semantic questions this way). There clearly is, or equally clearly is not, a correspondence between a sentence and any world of which it might be stated. The first is again the naive belief in one objective reality . . .' (Stamper, 1987).

The first point to notice about this is that Stamper is overstating the theory when he says that the correspondence must be clear if he means that all claims to a correspondence are incorrigible. The theory makes no such assumptions. For example, if all the swans I have encountered are white I will be justified in believing that 'swans are white' and if I do this I will hold that 'swans are white' is true. Later, if I encounter a black swan, I will realize that my earlier belief, although justified at that time, was in fact false. The main object of the correspondence theory is to show that justified belief and truth are not always the same thing.

Be this as it may, the main point is that it is difficult to see how Stamper can avoid an ideational stance if he rejects the notion of an independently existing world. This is because we are forced to ask what 'swans are white' refers to if there is no independently existing world. If there is no 'independent' world then, presumably, there must be some sort of dependent world, and what sort of world is this? A passage at the beginning of the paper might help to clarify Stamper's position:

'Meanings express personal views of reality. When there is a firmly established consensus, and only then, we can pretend that meanings are independent of people.' (Stamper, 1987).

What Stamper seems to be implying here is that the subject alone determine meaning—that public languages are a sort of Esperanto built up out of private languages. From this it follows that essentially 'swans are white' refers to something subjective—one of numerous personal realities. This is certainly ideational. If we agree with Wittgenstein then it is clear that Stamper has the boot on the wrong foot. Language is public and refers primarily to public events. References to subjective sensations are derived from a public language. I don't make up my own word for my pains and then translate it into English. I learn the use of the English word 'pain' by observing public events and then apply the word to my own pains. This does not prevent people from giving different meanings to the same utterance or symbol; this is because the same utterance or symbol is used in different language games. There can be symbols that mean a certain thing in computer jargon but mean something completely different in prison slang. This is because computer scientists and prisoners play different language games. Which language game is being played at a particular time will depend on the history of the players and the context in which it is being played.

Stamper appears to assume that meaning must be entirely objective or entirely subjective. He reasons that meaning cannot be entirely objective because words do not have meanings in themselves, and, therefore, meaning must be entirely subjective. But his assumption is wrong. Meaning is public and as such it is dependent upon the existence of at least two knowing individuals and dependent upon the existence of independent and observable objects and events.

## 2.3 Truth and rules

In the preceding section a discussion of the correspondence theory of truth was used to draw out Stamper's tacit ideational position. A complication must now be added because Wittgenstein did not accept correspondence theories of truth either. However, his reasons were quite different from Stamper's. The later Wittgenstein subscribed to the redundancy theory of truth. This is the theory that saying that 'All swans are white is true' or saying that 'It is a fact that all swans are white' is the same as saying 'All swans are white'.

An objection to the redundancy theory of truth is that without a correspondence to facts sentences cannot form truth-functional compounds. Kripke gives Wittgenstein's answer as 'We call something a proposition, and hence true or false, when in our language we apply the calculus of truth functions to it. That is, it is just a primitive part of our language game . . .' (Kripke, 1982). This reveals an important part of Wittgenstein's thought. For Wittgenstein formal systems such as mathematics and logic are language games. For Wittgenstein reference was not possible outside a rule-based language game. A new game can be devised and played by a group of people agreeing to a set of rules. In the same way a language game will produce rules and these rules can be formalized. In the following sections it is argued that the SSM conceptual model building process is, in part, a language game. As such it offers a viable alternative to attempts to design information systems on the basis of an ideational theory of meaning.

Before proceeding I shall summarize the difference between Stamper and Wittgenstein. Stamper objects to the correspondence theory because he thinks there is no independently existing world. For Wittgenstein there must be an independently existing world because language cannot refer to a logically private world. Wittgenstein's objection to the correspondence theory is that it is part of a language game, not something that stands over and above all language games. However, whether Wittgenstein's objection fires or not depends on how we take the correspondence theory. If we do not take it as a supreme principle, but take it as something to distinguish between justified belief and knowledge within a certain system of definitions, then I do not think Wittgenstein would object to it.

## 2.4 SSM and subjectivity

It seems that in information systems circles the term 'interpretivist' is now being used to denote methods that imply that a social situation is open to more than one interpretation, while the term 'positivist' is used to denote methods that imply that there is only one valid account for a social situation. In this sense SSM is interpretivist, as opposed to positivist, in its account of social events. This might lead one to believe that it must be ideational in its account of meaning, but this does not follow. An ideational account of meaning entails an interpretivist account of social events and this is why they tend to be found together. However, a rejection of the ideational account of meaning does not entail that there is only one valid account of a social event. The language game theory of meaning is compatible with that idea that there are a number of equally valid ways of describing a social event.

## 2.5 SSM as a language game

Checkland has always been adamant that SSM conceptual models are neither true nor false, nor are they correct or incorrect. They are not intended to be a representation of a real world state of affairs. However, if they are neither true nor false they cannot be representations of anything. They cannot, for example, be a representation of the stake-holders' ideas. Nor can they be a representation of what the stake-holders mean by something.

It is this fact that suggests that conceptual model building can be explained, at least partially, as a type of Wittgensteinian language game. If we take it that the stake-holders and the facilitator are playing a game in which a new language is created to describe the problem situation, then the validity of the model does not require that it has a truth value. Taken as a language game the building of a conceptual model is a public event in which the stake-holders come to an agreement about the terms that can be used to describe the problem. The model, therefore, has the logical status of an agreement and agreements are neither true nor false. A more formal explanation is that the finalized conceptual model (the one that marks the end-point of the iterative debate) is a definition of a desirable state of affairs. Here the definition is a stipulative definition, and once again, stipulative definitions are neither true nor false (Robinson, 1954).

This mode of explanation is not open to ideationalists because for them meaning ultimately resides with ideas in the subject's consciousness. From this it would follow that a conceptual model would only be meaningful in so far as it represented ideas in a subjective consciousness. If this were the case it would be true to say that the model was meaningful if it did in fact represent the subject's ideas and it would be false to say it was meaningful if it did not. Thus for ideationalists a putatively meaningful conceptual model would be representational and, therefore, true or false.

Although they cannot be true or false putative conceptual models can be valid or invalid. Validity is concerned with consistency within a set of rules rather than with representation. We can talk of a valid agreement and by this we mean that the agreement conforms to certain rules and regulations for making agreements. A valid agreement in British law is one that conforms to British law on agreements. With conceptual models validity will consist of conformity to the rules of conceptual model building. For example, a rule for SSM conceptual model building is that every bubble must have an arrow going into it or an arrow coming out of it.

The rules of SSM model building are a higher order language game. Before the stake-holders can start building an SSM model relevant to the problem situation they must accept the rules of SSM model building. If they do not want to accept these rules, that is fine—they can do something else; but they cannot build an SSM model and refused to accept the rules.

SSM rules are part of another language game and subject to a yet higher set of rules. These rules include the basic laws of logic such as the law of non-self-contradiction. Once again it is up to the stake-holders whether they want to play this game. If they do not, and they are happy with self-contradiction, that is fine. But in this case they are hardly likely to want a computerized information system.

## 3 PART 2: BUILDING THE LOGICO-LINGUISTIC MODEL

## 3.1 The development of logico-linguistic models

Logico-linguistic models have been developed in a number of theoretical papers (Gregory, 1993, 1993a, b) in an attempt to resolve a number of logical difficulties found in SSM conceptual models. The analysis is confined to the central elements in SSM conceptual models; it will not apply to the measures of performance that should be part of all SSM models. The measures of performance are not entirely definitional but are partially the outcome of the human values that the stake-holders subscribe to. A discussion of the logical status of human values is beyond the scope of the present paper. The logical distinction between value statements, definitions and inductive hypotheses is made elsewhere (Gregory, 1993b). Another limitation is that although it was said in the previous section that definitions are neither true nor false, they will be treated as true in this section. This is because the propositional calculus requires that all statements have a truth value.

The SSM conceptual models, such as the hypothetical one shown in Fig. 1, consist of commands linked by arrows. The arrows are intended to represent logical contingency (Checkland & Scholes, 1990, p. 36). In Fig. 1, activity 5 is logically contingent on activity 4. A logically equivalent way of expressing this is to say that 4 is a necessary condition of 5.

![](/api/attachments/ZBMEDBUD/fulltext/images/c3b0d13c4b1ac1d3e69baf7d8e21ad54f8a000f6baaeb9b38d6201d475153afa.jpg)  
Figure 1. The hypothetical soft systems methodology conceptual model.

Gregory (1991) made the point that necessary conditions are not enough to describe a causal sequence. Conceptual models, therefore, lack the power to fully describe physical transformations and cannot form an adequate basis for an information system design intended to support physical transformations. A description of a causal sequence requires sufficient conditions. A sufficient condition can be made up of a number of necessary conditions to form a necessary and sufficient condition (an N&S condition). Thus if P is necessary for R, Q is necessary for R, R is necessary for P and R is necessary for Q then 'P and Q' will be an N&S condition of R and R will be an N&S condition of 'P and Q'. A second paper (Gregory, 1993a) pointed out that some causal relations are sufficient without being necessary. These sufficient but unnecessary conditions (SUN conditions) also need to be represented.

The second level of difficulty concerns the phrase 'logically contingent'. This is because, strictly speaking, logical connections are between declarative statements, or elements of declarative statements, not between activities or other real world events. Normal logics cannot operate on SSM conceptual models because the elements are expressed as commands rather than as declaratives. This leads some to the conclusion that SSM models are not 'logical' but some sort of representation of a causal sequence (see Probert, 1991).

The first stage of the solution is to convert the commands into propositional form. The next stage is to convert statements of causal relations into logical relations. If we say that event P is necessary for Q then what we are saying is that if Q has occurred P must have occurred. Let us take 'p' to be the statement 'P has occurred' and 'q' to be the statement 'Q has occurred'. Given this the statement 'P is necessary for Q' will be equivalent to 'q cannot be true unless p is true' or simply 'q implies p'. This is expressed in the propositional calculus as 'q→p'. If P is a SUN condition of Q this will be expressed as 'p→q'.

Taking 'r' to be the statement 'R has occurred' we can now express an N&S condition. Pand Q being necessary for R will be expressed as 'r→(p & q)' and P and Q being sufficient for R can be expressed as $(p \& q) \to r'$ . A statement of affairs where $r \to (p \& q)'$ is true and $(p \& q) \to r'$ is true is known as mutual implication and is expressed as $r \leftrightarrow (p \& q)'$ . The symbol $\leftrightarrow$ is known as the biconditional.

In the early days of the propositional calculus mutual implication was indicated by a symbol consisting of three parallel lines. This was sometimes known as 'logical equivalence' or 'identity'. The term 'logical equivalence' is justified by the fact that the formulae on either side of the biconditional will have the same truth value. Equating the biconditional with 'identity' is much more contentious and few present-day logicians would be inclined to do so. Identity is considered to be a stronger relation than mutual implication. Any case in which identity holds will be a case in which mutual implication will hold, but the reverse is not true, not every case of mutual implication will be a case of identity. Modal logics extend this distinction to implication, they distinguish between 'material implication' denoted by $\rightarrow$ and 'entailment'. Entailment is the stronger relation that includes, but is not included in, material implication.

This brings us back to Probert. If the conceptual models are essentially causal in nature then material implication and mutual implication are the strongest relations we can use. If conceptual models are essentially definitional, as is contended in this paper, then the stronger relations of entailment and identity can be used.

In the model given as an example in the next section implication and the biconditional will be used to stand for the strong relations of entailment and identity. However, the notation used will be that of a simple propositional calculus which does not reveal the distinction. A modal logic can be used but such logics must be treated with caution because there are many systems of modal logic. The explanation of a suitable modal system is beyond the scope of the present paper.

The model looks like a cause and effect diagram and there is nothing in its logical expression that indicates that it is not. However, the manner of its construction shows that it is not a representation of a process of cause and effect but that it is a process definition. Most things are defined by their qualities. A chair can be defined as an object with a seat, a back support and more than two legs. Other things are defined by the process of their production. Whisky is a spirit distilled from fermented malted grain. This means that if you take some grain, malt it, ferment it and then distil it you end up with whisky—no matter what it tastes like. By the same token something that has the same taste, alcohol content and colour as whisky is not a whisky unless it is produced by the defining process. For example, in Thailand there is a popular liquor called 'Mehkong' which is made as a substitute for Scotch. Originally Mehkong was made from rice, which is a grain, and Mehkong was, correctly, called a whisky. These days it is made from molasses, which is not a grain, and so Mehkong is now described as a 'liqueur' despite the fact that is has the same alcoholic content and looks and tastes the same as it always did.

## Stake-holder construction

A logico-linguistic model is an expanded version of a traditional SSM conceptual model and it is intended that it should be developed in the same way as a conceptual model. That is, the analyst/facilitator determines the logical form of the model and makes suggestions as to the content. The content is then debated and amended by the stake-holders until agreement is reached through the iterative process.

The example given here is a model produced as a case study for a seminar held by the United Kingdom Systems Society at the University of Warwick (see Systemist, Vol. 14, No. 4, 1992). It is a model for an information system to support the activities of a programme committee involved in arranging a working conference. It must be stressed that conceptual models and logico-linguistic models are intended to be built by stake-holders in the client organization not by analysts. As there was no client organization for the case study the model must be regarded as hypothetical. It is intended to show what the logico-linguistic model might have looked like if there had been stake-holders available to build it.

Figure 1 gives an example of a conceptual model that could have been built by traditional SSM methods. An imaginary logico-linguistic model, which could have been built out of Fig. 1, is shown in Fig. 2. The development has followed a number of rules, these are briefly as follows:

## 3.3 Rules of conversion and expansion

## Rule 1. Convert commands into statements

Figure 1 is expressed in the language of commands. In order to use traditional logics, such as the propositional calculus, we require statements. A command such as 'make a call for papers' can be expressed as a parallel statement as follows: 'the command make a call for papers is, was or will be, obeyed'. For the sake of brevity and elegance this is rendered as 'a call for papers is made' in Fig. 2.

## Rule 2. Include conditions that are sufficient but not necessary (SUN conditions)

The arrows in SSM conceptual models indicate necessary conditions. So, in Fig. 1, we find that 5 is a necessary condition of 6, and 4 is a necessary condition of 5. In causal terms this would mean that 6 cannot happen unless 5 happens and 5 cannot happen unless 4 happens. However, if we take the relations to be definitional then we will say that the truth of 6 entails (logically implies) the true of 5, and that the truth of 5 entails the truth of 4. To these relations of necessity we can add relations of sufficiency. These are indicated by broken lines in Fig. 2. Here 10 is sufficient for 1, which, in causal terms, means that if 10 happens 1 must happen. However, 10 is not necessary for 1 because 1 can happen without 10 happening; in the case in point this would be when 11 (which is also sufficient for 1) happens. Therefore, 11 and 10 are individually sufficient but unnecessary for 1, i.e. they are SUN conditions. SUN conditions are not mutually exclusive, that is both 10 and 11 can happen. In the language of causation we would say that 1 can be caused by 10 or 11 or both. Taking the relations to be definitional we can say that the truth of 10 entails the truth of 1, and that the truth of 11 also entails the truth of 1.

## Rule 3. Make sure that all possible SUN conditions are included

There are two ways of defining a class: extensive definition and intensive definition. An extension

## Rule 3. Make sure that all possible SUN conditions are included

There are two ways of defining a class: extensive definition and intensive definition. An extension definition specifies all the members of the class while an intensive definition gives the criteria for class inclusion. If we think of 1 as a class, the class of calls for papers, 10 and 11 can be regarded as members of that class. If they are the only logically possible members of the class, then they will constitute an extensive definition. This can be expressed in the propositional calculus as follows:

$$
1 \leftrightarrow (1 0 v 1 1)
$$

Taking the biconditional here in the strong sense of 'identity' this formula states that 1 is the logical equivalent of 10 or 11 (or 10 and 11). In other words they are the same thing. In terms of the development of the model what has happened is that the stake-holders have defined 1 as being 10 or 11 (or 10 and 11). Put another way, what 'a call for papers is made' means is that 'a call for papers is published in a periodical or experts are individually requested to produce papers or both'.

It must be noted that if all the logically possible SUN conditions cannot be specified then we cannot have an extensive definition. If it is possible for there to be SUN conditions that we do not know about then the class must be defined intensively.

## Rule 4. Make sure that the set of necessary conditions is sufficient

Figure 2 shows that 2 is a necessary condition of 3. But it is not sufficient for 3; it is possible for 2 to happen without 3 happening. To make sure that 3 happens we must add more necessary conditions (Gregory, 1991), namely 25 and 22. Now the set comprising 2, 25, 22 is sufficient for 3. As 2, 25 and 22 are each also necessary for 3, we can say that the set comprising 2, 25 and 22 is a necessary and sufficient (N&S) condition of 3. In symbols:

$$
3 \leftrightarrow (2 \& 2 5 \& 2 2)
$$

Again taking the biconditional here in the strong sense of 'identity' this formula is a complete intensive definition of 3. It states that if anything is to count as a paper distributed to referees then that paper must have been received, it must have had competent referees selected for it and it must have been distributed to the referees. Any paper that does not meet these three criteria cannot, by definition, count as a paper distributed to referees.

## 3.4 Establishing what is definitional

The words used to express definitions do not always, or even usually, indicate that what is being expressed is in fact a definition. Looking at a defining statement in isolation we will find that it could just as easily be a statement of fact, i.e. an inductive hypothesis or a statement based on an inductive hypotheses. For example, 'Manx cats do not have tails' could be part of

![](/api/attachments/ZBMEDBUD/fulltext/images/8f775253a4141bfbf3c4b7e94a82405d7f56da52cc78cc0c37d3364caaeba8e9.jpg)  
Figure 2. An imaginary logico-linguistic model.

The problem is compounded by using process definitions and extensive definition. People tend to think that a statement about a process is always a statement of contingent fact. Likewise statements that specify all the members of a class are usually factual rather than definitional. People are, therefore, likely to think that they are never definitional. They are apt to find unconvincing the definition of 'a call for papers' as 'something published in a periodical or

## 162 FH Gregory

individual requests to experts'. However, we easily imagine a case where the stake-holders would give the term 'a call for papers' this usually narrow meaning. For example, it might be that this is specified in the constitution of the organization concerned. One of the main tasks of the facilitator in the construction of a logico-linguistic model will be to distinguish definitions from contingent statements of fact.

## 3.5 Logical expression

Figure 2 can be expressed in the propositional calculus as follows:

```txt
Formula 1
6↔((29 & 5 & 28) & (5↔(4 & 27)) & (4↔(26 & 3) & (3↔(2 & 25 & 22)) & (22↔(24 & 23)) & (2↔(19 & 21)) & (19↔(9 & 15 & (17 v 18 v 20))) & (15↔(13 & (14 v 16))) & (13↔(12 & 1) & (1↔(10 v 11)))
```

This enables us to make a number of inferences. We can derive the following:

```txt
Formula 2
6↔(29 & 28 & 27 & 26 & 23 & 24 & 25 & 21 & 9 & 12 & (10 v 11) & (14 v 16) & (17 v 18 v 20))
```

Formula 2 states that if all the necessary conditions and one from each of the three sets of SUN conditions from Fig. 2 are fulfilled we will have a state of affairs in which papers are grouped into sessions and chairmen for each session are selected.

These types of formula can have direct practical application. They can be used as the basis for system control algorithms (Gregory, 1991) and a logical account of system efficiency can be expressed as the choice between SUN conditions (Gregory, 1993a). However, the most important application is likely to be in information system design.

## 4 PART 3: TOWARDS INFORMATION SYSTEM DESIGN

## 4.1 Limitations of the proposal calculus

In the preceding section the propositional calculus was used to show how conceptual models, understood as language games, could be formally expressed. The propositional calculus has the advantage of being easily understood and it has been convenient to use it as a first step. However, it is not powerful enough to take an SSM model through to information system design. Shortcomings were evident at the outset when it was said that definitions needed to be 'treated' as true. The best way to avoid this bodge is to use modal logic. Modal logic distinguishes different types of truth; it can be used to distinguish logical from factual truth. In a modal logic we could say that stipulative definitions were logically true but factually neither true nor false. A second shortcoming is that propositional logic does not distinguish between universal statements and particular statements. This needs to be done, tacitly or otherwise, in every information system. For this the predicate calculus is required.

## 4.2 Universals and particulars

The elements in the logico-linguistic model are universal terms. The expansion of the model using universal terms and the rules given above can only go so far. Eventually, general statements will have to be broken down into particulars. For example, a break down of 'Experts exist' would have to be statements of the form 'Adrian Adams is an expert' or 'Betty Brown is an expert' which have reference to particular states of affairs and are true or false depending upon whether that state of affairs obtains or not. This marks a profound change in status with regard to meaning, logic and epistemology. Hitherto, the truth of the statements in the model could be established by deduction and definition. This is no longer possible, and the truth of the particular statements must be established empirically.

Also the universal statements in the model, those expressed in formulas 1 and 2, are necessarily true (because the stake-holders have set it up that way) while the particular statements are contingent. This is evident if we consider time. The model comprising formulas 1 and 2 will be true for all time but the particular fact that Adrian Adams is an expert will indubitably become false at some time in the future. The definitional universal statements which the model expressed could be taken as the axioms of a formal system while the particular statements could be taken as instantiations of the system.

Parallels to computerized information systems can now be drawn. A correspondence can be seen between universal statements with their logical connections and the structure and processes of a computerized information system. Particular statements have a correspondence to data items. This is most evident in declarative language programs such as PROLOG. The logico-linguistic model can be expressed in the predicate calculus and in this form the universal statements have the same structure as PROLOG rules while particular statements have the same form as PROLOG facts (Gregory, 1993b). In data base design particular statements correspond to records while fields correspond to the subject predicate structure of the particulars.

## 4.3 Similarities to 'holons'

Checkland & Scholes (1990) use the term 'holon' to denote a system of thought. As such a holon can be distinguished from a system in the real world. A similar distinction can be drawn with regard to logico-linguistic models. A logico-linguistic model is an extended definition and as such need not have any correspondence with the real world; the model could just as easily be that of the family tree of a Greek God as anything in the real world. A second important point about the notion of a 'holon' is that there is no single holon that is correct in regard to a given situation. There can be a number of equally valid holons relating to the same situation. The same is true of logico-linguistic models; the same situation could be described using a different set of definitions.

There is also a similarity with axiomatic systems here. The mere fact that an axiomatic system has been formulated is no guarantee that it has any correspondence with the real world. We also find that the same system, such as the propositional calculus, can be formulated using different sets of axioms.

Expanded into logico-linguistic models the SSM conceptual modelling method can be a way of producing axiomatic systems. This stands to be very useful because one of the problems with axiomatic systems is that there is no logical reason for anyone to accept them. If there are reasons for accepting a statement then that statement must be some form of inference not an axiom. Generally, it is said that axioms are self-evident, but this is just another way of saying that they are accepted without reason. Admittedly, some axiomatic systems, such as arithmetic, seem to be very useful, whereas others do not. Nevertheless, before an axiomatic system can be shown to be useful it must be accepted, if only tentatively, and there is no reason to do this. SSM solves this problem pragmatically; as the stake-holders make up their own axioms the question of their acceptability does not arise. However, the question of their usefulness does arise.

## 4.4 The problem of reference

This paper has been concerned with meaning qua sense (connotation, intension), with the meaning of terms in the context of other terms. It has not dealt with the question of how we can establish that a term refers to an existing state of affairs. This is a fundamental issue that is formulated in different ways. In the language of SSM the question is: how can we tell when a conceptual model maps on to the real world? In the theory of truth it is: how do we establish that a statement corresponds to a fact? In Wittgenstein's philosophy it would be: how do we know when a language game is useful? For Hofstadter (1980) it would be: how can we establish that an axiomatic system is isomorphic? Essentially, all these questions are asking: how can something that has been made up help us to understand and describe something that has not been made up?

The answer is not simple and is beyond the scope of the present paper. However, having determined how to establish sense it will make the work of establishing reference easier. This paper is written in the belief that, in information system design, sense should be established before reference. Although sense and reference are closely bound together there is reason to believe that sense is logically prior to reference. The early Wittgenstein gave logical priority to reference; the later Wittgenstein can be understood as giving logical priority to sense.

In more practical terms there is good reason to think that logico-linguistic models will be able to establish reference if they are expanded to include inductive hypotheses as well as definitions (Gregory, 1993c). However, preliminary research indicates that the solution is not simple and may require the use of non-monotonic logic as well as modal logic.

## 5 CONCLUSIONS

Logical atomism and logical positivism are the most forceful attempts at an ideational account of meaning. The leaders of these movements all abandoned this position in their later writing. The ideational account of meaning takes us back to the beginnings of logical atomism. There is, therefore, a danger that the information systems literature will start a rerun of futile debate that began in the 1920s and finished in the 1960s. This will not be necessary if due attention is given to the legacy of Wittgenstein.

Understood as a language game the SSM iterative debate provides both a firm theoretical foundation and a powerful practical tool for the development of information systems. Computer systems are rule bound and formal. It has been argued above that there are rules implicit in SSM conceptual models, these rules can be developed and formalized in logico-linguistic models. This opens the way for the rigorous development of computerized information systems that will be meaningful not only to professional analysts and designers but also to the people who use and interact with the system.

## 6 ACKNOWLEDGEMENTS

The findings in this paper were the result of research funded by the Science and Engineering Research Council (SERC).

## 8 APPENDIX - THE HISTORY OF PRIVATE LANGUAGES

## 8.1 Logical atomism

To find an irrefutable foundation for human understanding has been the ambition of countless philosophers throughout history. Bertrand Russell was no exception. In the early part of this century he began developing a set of ideas that became known as 'Logical Atomism' (Russell, 1918, 1924).

Russell began with the standard empiricist idea that all knowledge comes through the senses. His next move was to say that the only thing we can be certain of is sense experience. Knowledge is, he argued, built up entirely out of atomic units of sense experience. These units he called 'sense data'. The standard analysis of knowledge, which some attribute to Plato (Gettier, 1967), is that it is true, justified belief. Russell was saying that only sense data justify belief and thereby turn it into knowledge. This was nothing particularly new, the sense datum theory can be traced back at least as far as John Stuart Mill.

Russell's next move was rather unusual. He went on to say that not only was knowledge built up out of sense data but that meaning was also built up out of sense data. This was quite profound because if sense data are required for meaning they are also required for the formulation of belief. For Russell it was not possible even to believe anything that was not based on sense data. This, therefore, was a unified theory of knowledge and meaning.

In the 1905 paper 'On Denoting' Russell developed his theory of descriptions. This claimed that most names are in fact disguised descriptions. Names apparently refer to individuals but 'On Denoting' hoped to show that names can be unpacked into logically equivalent descriptions which have sense but no individual reference. Russell (1918) went on to say that only 'logically proper names' have individual reference and these only refer to sense data.

The elegance of this theory was very appealing. Wittgenstein's Tractatus (1922) with its 'picture theory of meaning' is firmly in this tradition. Rudolf Carnap and the Vienna Circle were working on similar ideas which were popularized in Britain by A. J. Ayer (1936) in his best-selling book Language, Truth and Logic. More than any other text this book represents the views that people began to call 'Logical Positivism'.

## 8.2 Empiricism, phenomenalism and phenomenology

Taken independently of the theory of meaning, the sense datum theory is just one species of the philosophical position known as 'phenomenalism'. This comes from J. S. Mill, who held that objects were just 'permanent possibilities of sensation' (Ayer, 1969, pp. 224–5). The empiricist says that all knowledge comes from what we have experience of. The phenomenalist takes this further and says all knowledge is made up of experiences; for the phenomenologist what these experiences are experiences of is something we cannot know.

The position known as 'phenomenology' ends up being similar to phenomenalism in its account of the external world. However, phenomenologists, such as Edmund Husserl, get there by a different route. This is the route of rationalism which claims that knowledge is a priori, a result of thought rather than a result of experience.

The trouble with phenomenalists and phenomenologists is that they board up the window to the outside world, leaving the subject completely alone.

## 8.3 Language games

By the 1940s Wittgenstein had changed his mind completely about the nature of language. In the Philosophical Investigations, which was not published until 1953, he produced an argument that was fatal to logical atomism, logical positivism and many of the ideas of his own Tractatus. This became known as 'the private language argument'. The private language argument shows that it is not possible for a language to refer to objects that only one person can, as a matter of logic, know about. Sense data are logically private because only one person can know his or her own sense data.

The private language argument is a complex one and the exposition here will be limited to an outline. Kenny (1973) considers that the crux of the argument is that the terms of a private language could not be defined. He identifies three prongs to the attack. First, it contends that a private object, a sense datum such as a pain, cannot be ostensibly defined. That is, a person cannot merely fix his attention on a sensation and name it 'so and so'.

... what does it mean to say that he has named his pain?—How has he done this naming of pain?! And whatever he did, what was its purpose—When one says "He gave a name to his sensation" one forgets that a great deal of stage-setting in the language is presupposed if the mere act of naming is to make sense." (Investigations, p. 257)

Secondly, a private sensation cannot be defined in terms of a previous sensation.

We are supposing that I wish to justify my calling a private sensation "S" by appealing to a mental table in which memory-samples of private objects of various kinds are listed in correlation with symbols ... To make use of such a table one must call up the right memory-sample: e.g. I must make sure to call up the memory-sample that belongs alongside "S" and not the one that belongs alongside "T". But as this table exists only in the imagination, there can be no real looking up to see which sample goes with "S", i.e. remembering what "S" means. But this is precisely what the table was meant to confirm. In other words the memory of the meaning of "S" is being used to confirm itself.' (Kenny, pp. 192–3)

Thirdly, a private sensation cannot be defined in terms of public events.

"Let us now imagine a use for the entry of the sign "S" in my diary. I discover that whenever I have a particular sensation a monometer shows that my blood-pressure rises. So I shall be able to say that my blood-pressure is rising without using any apparatus. This is a useful result. And now it seems quite indifferent whether I have recognized the sensation right or not. Let us suppose that I regularly identify it wrong, it does not matter in the least. And that alone shows that the hypothesis that I make a mistake is a mere show. (We as it were turned a knob which looked as if it could be used to turn on some part of the machine; but it was a mere ornament, not connected with the mechanism at all.)." (Investigations, p. 270)

To replace the idea of language as something based on reference to logically private objects and events, Wittgenstein developed the idea of language as consisting essentially of rules. In the Investigations the notion of a language game is developed. A language is like a game. You cannot play the game if you do not obey the rules but the rules are no more than an agreement among the putative players about how to play the game. There are many games that you can play and new ones are being made up all the time. For the later Wittgenstein language is public, and the references in any language are learned from publicly observable objects and events.

## 9 LOGICAL NOTATION

-p means not p (negation). It is true when p is false.

$p \& q$ (conjunction). $p \& q$ is true only if $p$ and $q$ are true.

p v q means p or q or both (alternation). p v q is true if p is true or if q is true or if p and q are true.

$p \to q$ means if $p$ then $q$ (the conditional). $p \to q$ is only false when $p$ is true and $q$ is false, otherwise it is true. Sometimes known as implication.

$p \leftrightarrow q$ means p if and only if q (the biconditional, sometimes known as logical equivalence or identity). $p \leftrightarrow q$ is true if p and q are both true or if p and q are both false, otherwise it is false.

## REFERENCES

Auramäki, E., Lehtinen, E. & Lyytinen, K. (1988) A speech-act-based office modeling approach. ACM Transactions on Office Information Systems 6.

Avison, D. E. & Wood-Harper, A.T. (1990) Multiview: An Exploration in Information Systems Development. Blackwell Scientific Publications, Oxford.

Ayer, A.J. (1936) Language, Truth and Logic. Victor Gollancz, London.

Ayer, A.J. (1969) The Foundations of Empirical Knowledge. Macmillan, London.

Checkland, P.B. (1989) An application of soft systems methodology. In: Rational Analysis for a Problematic World. Rosenhead, J. (ed). John Wiley & Sons, Chichester.

Checkland, P. & Scholes, J. (1990) Soft Systems Methodology in Action. Wiley, Chichester.

Copi, I. (1968) Introduction to Logic, 3rd edn. Macmillan, New York.

Frege, G. (1892) Uber Sinn und Bedeutung. Zeitschrift für Philosophie und philosophische Kritik, 100.

Gettier, E.L. (1967) Is justified true belief knowledge? In: Knowledge and Belief, Phillips Griffiths, A. (ed.). Oxford University Press, Oxford.

Grayling, A.C. (1990) An Introduction to Philosophical Logic. Duckworth, London.

Gregory, F.H. (1991) Causation and Soft Systems Models. Systemist, 13, 105–12.

Gregory, F.H. (1993a) Cause, effect, efficiency and soft systems models. Journal of the Operational Research Society 44, 333–44.

Gregory, F.H. (1993b) Logic and meaning in conceptual models: implications for information system design. Systemist, 15, 28–43.

Gregory, F.H. (1993c) Mapping conceptual models on to the real world. In: Systems Science: Addressing Global Issues—Proceedings of the 3rd International Conference of the United Kingdom Systems Society (in press).

Hanseth, O. (1991) Integrating information systems: the importance of contexts. In: Collaborative Work, Social Communications and Information Systems, Stamper, R. et al. (ed.). North-Holland, Elsevier Science Publishers.

Hofstadter D.R. (1980) Gödel, Escher, Bach: an Eternal Golden Braid. Penguin Books, Harmondsworth.

Kenny, A. (1973) Wittgenstein. Penguin Books, Harmondsworth.

Kripke, S.A. (1982) Witgenstein on Rules and Private Languages. Basil Blackwell, Oxford.

Mill, J.S. (1843) A System of Logic. London.

Mingers, J. (1992) SSM and information systems: an overview. Systemist, 14, 79–98.

Probert, S.K. (1991) A critical study of the National Computing Centre's systems analysis and design methodology, and soft systems methodology. MPhil thesis, Newcastle upon Tyne Polytechnic.

Robinson, R. (1954) Definition. Clarendon Press, Oxford.

Russell, B. (1905) On Denoting. In: Russell (1956).

Russell, B. (1918) The Philosophy of Logical Atomism. In: Russell (1956).

Russell, B. (1924) Logical Atomism. In: Russell (1956).

Russell, B. (1956) Logic and Knowledge, Marsh, R. (ed.). Allen & Unwin, London.

Stamper, R. (1987) Semantics. In: Critical Issues in Information System Systems Research, Boland, R.J. and Hirschheim, R.A. (eds). Wiley, Chichester.

Wilson, B. (1990) Systems: Concepts, Methodologies and Applications. 2nd edn. John Wiley, Chichester.

Wittgeinstein, L. (1922) Tractatus Logico-Philosophicus. Ogden & Richards translation. Routledge & Kegan Paul, London.

Wittgenstein, L. (1953) Philosophical Investigations. Blackwell, Oxford.

## Biography

Frank Gregory obtained a BA in philosophy from York and an MSc in information management from Lancaster. He is currently in the final year of a full time PhD funded by SERC and Warwick Business School. His thesis uses the tools of analytical philosophy to construct a logical framework for the development of soft system models for information system design. He has published a number of papers on this subject.

His working career has largely been based in Bangkok where he worked for 11 years initially as a business journalist and later as a consultant specializing in the design and management of industrial market research projects.
