---
otero_id: 23330
otero_key: "A3VSJ45U"
title: "What Good are Neural Nets?"
authors: "Ian M Donaldson"
year: "1988"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1988.46"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Personal View What Good are Neural Nets?

Ian M Donaldson

Artificial intelligence has come a long way since the pioneering Dartmouth Conference which fixed upon the name. It has been a long road to the place at which the science now finds itself, but it may be an even longer road to its stated aim of producing a machine which can think. This is why the new paradigm of neural computing, or connectionism, seems so tempting: connectionism copies the way in which a realized thinking machine, the brain, works, in a 'nice' way; it has produced some extremely impressive results in a relatively short period of widespread study and, for the moment at least, it seems to take a step back from the superficially contrived and convoluted methods of representing knowledge and reasoning that traditional rule-based methods use.

Nevertheless, we shouldn't be like the man in the cartoon, who doodles while his colleagues get on with hard programming, because he is, 'waiting for neural nets.' It is precisely because neural computing looks so enticing that we should stop and consider whether a connectionist approach is likely to help in achieving the goals of artificial intelligence; to do that, we need firstly to clarify those goals and satisfy ourselves that they are, in principle, attainable.

The term ‘artificial intelligence’ can be, and is, used in two very distinct senses. It is still used in its original sense of ‘the science and engineering of manufactured systems which can be made consistently to behave in all the ways which we associate with thought, when exhibited by a human being.’ This definition skirts round the philosophical problem of ‘other minds’; we would prefer to say, if we could, that we were in the business of manufacturing systems which could, simply, think.

The words ‘artificial intelligence’ however, have come to be applied to the whole field of research which has arisen in pursuit of this goal. Many commercially available systems which have arisen out of this research are now labelled ‘artificially intelligent’ despite the fact that they don’t claim to satisfy any definition of the term. Moreover, much work in the field now is not in direct pursuit of the goal but rather seeks to make researchers' achievements so far useful and commercially viable. This field of research can be seen as working towards systems which behave in some of the ways which we associate with thought, and have other features which make them particularly useful in practical applications. The 'dream' which started the whole thing off is recognized to be just that – a dream, which may one day be fulfilled, but which shouldn't stop profitable work being done in the meantime.

We can see that, in considering the potential of a new paradigm for ‘artificial intelligence’ (AI), we must be careful to specify exactly which brand of AI we are wanting to talk about.

We shall consider first the possibility, from a philosophical standpoint, of ‘true’ artificial intelligence. When Alan Turing first wrote about this, he enumerated many arguments which purported to show that artificial intelligence was impossible in principle. $^{1}$ This paper will consider particularly those discussions on which the essential differences between symbolic and neural artificial intelligence have some bearing.

The argument that Turing called ‘various disabilities’ listed various human features which, the contention was, a machine could never share. These features included creativity. Lord Byron’s daughter, Ada Lovelace, believed that Babbage’s ‘. . . analytical engine has no pretensions whatever to originate anything.’ $^{2}$ There are two general points which should be made in response. The first is that there is no particular reason to suppose that, from a behavioural point of view, humans do anything other than they are programmed to do. To be sure, a human’s programmer is its entire environment; nevertheless, we don’t have to look any further than that programming to account for human creativity. Secondly, there is no need to define creativity in terms of the ability to depart from programmed behaviour. Newell, Shaw and

Simon, for example, put forward the view that ‘. . . creative activity appears simply to be a special class of problem-solving activity characterized by novelty, unconventionality, persistence and difficulty in problem formulation.’

Once the problem of creativity is untied from the problems of free will and consciousness in this way, there seems to be little to choose between the neural and the symbolic approaches to modelling it. In rereading Newell, Shaw and Simon's definition of creativity, however, the crucial word seems to be 'novelty'; if a problem isn't new in any sense, it can be tackled in just the same way that all previous problems have been. But do humans themselves ever have truly new concepts or new knowledge, given that new things can almost always be explained in terms of old ones? The answer seems to be that the only really new concepts we, or any machine, can have, are those which can only be experienced directly through the senses. In this respect, the neural paradigm seems to have a big lead over its symbolic counterpart: abstraction and concept formation are properties which seem to arise very naturally from many neural theories of perception and learning. Jones and Hoskins, for example, have found that 'it is often the case that hidden units, through the actions of back-propagation, will come to represent useful abstractions of the outside world' $^{3}$ , while in Smolensky's harmony theory 'the nodes...support representation of the environment at all levels of abstractness.' $^{4}$ The contrast between the relative ease with which these properties arise and the effort needed to represent even completely concrete new concepts in symbolic processing, never mind the same concept 'at all levels of abstractness', is striking. Although creativity is a philosophical possibility for both connectionist and symbol-processing machines, on a first examination, it seems that creativity could much more easily be demonstrated by a neural computer than by a traditional one.

Another ‘disability’ which Turing attempted to tackle, and which has arisen again in connection with John Searle’s ‘Chinese Room’ argument $^{5}$ , is that of consciousness. Searle feels that, no matter how it behaves, a program which blindly follows rules and which works with symbols and syntax, rather than meaning, cannot be said to be consciously thinking.

In a sense, we made a decision to ignore the whole question of consciousness when we took a behavioural approach to the definition of artificial intelligence. Many of those working in the field, however, are cognitive psychologists or philosophers, rather than computer scientists. For some of them, consciousness is crucial to thought, and for all of them an explanation of consciousness is a most important goal. Are neural nets more likely, then, to provide a bottom-up explanation for consciousness than traditional symbolic approaches?

In my own view, the answer is yes. This is a statement, though, about the relative chances of success of the two paradigms: at the moment, no argument similar to the Chinese Room has been produced which purports to show that neural nets cannot be conscious, though Searle believes that the Chinese Room argument applies equally to connectionist systems. Moreover, connectionism models the brain; if consciousness did not have a connectionist explanation, we would be forced into believing that organic chemicals contained some magical consciousness-endowing ingredient that could not be modelled.

But in fact, we made a behavioural definition of artificial intelligence in the first place precisely because AI will have nothing to say about consciousness until a test for consciousness has been devised. Even if a conscious machine was built, we would have no way of knowing that we had succeeded. Searle goes so far as to say that, because consciousness is completely subjective, it will never admit any objective detection or explanation $^{6}$ . But in any event, no progress can be made in simulating consciousness until we have some way of detecting it. At the moment, as far as artificial intelligence is concerned, consciousness is a non-problem.

It can be shown that neural networks are formally equivalent to Turing machines. Most of the other main objections in principle to ‘original’ artificial intelligence, such as the argument from Gödel’s theorem, thus apply equally to connectionist and symbolic theories. Our examination of objections to the possibility of artificial intelligence has suggested that neural networks offer no real philosophical advantages over symbol processing machines.

Schank $^{7}$ has proposed a list of issues which he feels must be tackled before artificial intelligence can become a reality. These include creativity, representation, decoding, inference, control of combinatorial explosion, indexing, prediction and recovery, dynamic modification and generalization.

## Representation

In neural nets the crucial choice is between local and distributed representations of knowledge. However, once an approach to representing indivisible concepts has been chosen, composite notions are developed and represented in a very natural, almost automatic, way. Moreover, the particular tasks which the net is made to perform in part determine the new higher-order representations.

Rumelhart and McClelland, $^{4}$ in discussing the strengths and weaknesses of local and distributed representations for the creation of new concepts, argue that: 'One of the central problems ... is specifying the exact procedures by which distributed representations are to be learned. Not all the problems have been solved, but significant progress is being made ...'

By contrast, in programming symbolic machines, we are forced to fix, even if only implicitly, the structure of every symbol the machine will use. Worst of all, our choice of symbols will reflect the use which we expect to be made of the knowledge, rather than the machine's experience of the uses to which it is actually put.

## Decoding

There must be ways of translating items of knowledge between a representation and a form which can readily be understood by the users of a machine — otherwise our knowledge representation scheme, however efficient, will be useless. Here, symbolic approaches have the edge. A symbol designed by a human programmer can by definition be translated into human terms. The problem of translating a pattern of activation over a group of neurons into the same human terms, on the other hand, is particularly complicated, as a result of the self-organizing ability of networks. Although the net itself should work as a reliable ‘translation’ device, all programs — and machines — need to be debugged, and the ability independently to monitor the interaction of symbols during a computation in a neural net will prove to be indispensable.

## Inference

Humans are very good at communicating implicit information. Analogy, hinting and sarcasm are only the most obvious examples of techniques of language which require both the speaker and the listener to infer a great deal of what is meant. This ability is knowledge-intensive and works because we share broadly the same world model and basic experiences. The paradigm which will support inference more easily and efficiently is likely to be the one which can cope better with large databases of world knowledge. We have already noted that neural networks have useful properties as far as knowledge representation is concerned. Abu-Mostafa $^{8}$ shows that ‘the capacity of the network grows faster than the number of neurons . . . artificial intelligence problems requiring huge databases . . . make the most use of neural networks.’

## Controlling combinatorial explosion

In symbolic machines, huge knowledge bases force us to use powerful heuristics in order to limit search spaces. This, in turn, requires specialized study by the programmer of every context in which a program or machine will be required to work. This feels rather like doing the work ourselves for which we are writing the program. If we wish to avoid it, we must develop heuristics which can be applied more generally. One other possibility is not to limit the size of the search but simply, by parallelism or improvements in processor technology, to execute the search more quickly.

Parallelism, of course, is an inherent part of connectionist models. But the absence of explicit rules from neural nets means that searches through large search spaces do not really occur in using them. Even when options are considered, the computation takes the form of the construction of a solution which is most compatible with our goal, rather than separate consideration of the merits of each option before a final choice of that option which seems to take us closest to the goal.

## Indexing

This question is really the search problem viewed from a passive rather than an active standpoint: how can we construct the search space so that it makes searching easy? Symbolic machines suffer from the problem that without any heuristics to help them, searches through their knowledge bases are totally uninformed. They will rely on the language in which they are written, rather than the problem they are trying to solve, for the order in which solutions are considered. Moreover, efficient indexing schemes are crucial to the power of heuristics: 'Sophisticated control ideas are dangerous because they can deflect people away from fundamental questions about representation and constraint.' Beyond these points, little is known about knowledge organization in general. Schank' believes that will soon have to change: 'AI programs are usually not large enough to make their answers to the indexing question meaningful, but the construction of programs of the appropriate size should become more important in the years ahead.'

Because of the inherently associative nature of connectionist models of memory, which links items together very much like a semantic net, indexing is much less of an issue in neural networks than it is in symbolic machines, which must have some organization artificially imposed on them. Search in a neural memory will be inherently directed by the relaxation process — the tendency of the net to reduce its ‘computational energy’ as far as possible. Is indexing even possible in a machine which creates its own knowledge representations?

## Prediction and recovery

One of the most important tasks of artificially intelligent programs is/will be to predict: we will want our machines to advise us on stock market movements, for example; machines will need to be able to predict the structure of the second half of a sentence having been given the first half. On top of this, a machine must be able to cope with, and learn from, mistakes in its expectations.

Prediction can be viewed as a kind of pattern completion exercise. This is the sort of problem for which connectionist computing is particularly suited because of the dynamics of patterns of activation. However, connectionist pattern completion research has concentrated up to this point on very simple patterns: single words or sentences at the most. It remains to be seen whether tasks which are computationally much more intensive and which (for once) defy even human intelligence, such as weather forecasting, can be embedded in pattern completion terms as easily. Nevertheless, there is no doubt that neural nets score points on the ‘recovery’ aspect: one of connectionism’s most publicized strengths has been resilience. Since learning is the central mechanism by which neural networks operate, there seems little doubt that networks could both cope with and learn from, their mistakes; in fact, networks can learn from every computation they make, whether successful or not.

It is perhaps significant that when humans attempt tasks like weather forecasting, they often end up following simple rules of thumb such as 'red sky at night . . .' A rule-based approach seems to be the next best thing to the computationally intractable (for the brain) problem of solving simultaneous differential equations. But in fact, there are special-purpose computers in existence which can make very accurate predictions within narrow contexts and it is possible that, with improvements in technology, these computational abilities will be available in artificial intelligence applications.

'Recovery' is a harder issue for symbolic machines to deal with. A frequently raised problem in software engineering is that of brittleness. As programs become too complex to be understood clearly by any one person, they become more and more susceptible to 'dumb' input and other aspects of environments which do not fit with their expectations and, far from learning from incorrect predictions, may even fail altogether on discovering their mistake.

Brittleness is not a problem which will easily be solved.

## Dynamic modification

Schank $^{7}$ believes that learning is the fundamental issue in artificial intelligence: ‘AI is the science of endowing programs with the ability to change themselves for the better as a result of their own experiences. . .No matter how sophisticated a story understander might seem, it loses all credibility as an intelligent system when it reads the same story three times in a row and fails to get mad or bored or even notice.’

A neural network at Imperial College, London, recently demonstrated very publicly its ‘credibility as an intelligent system,’ when it succeeded in getting bored.. The machine was being used to simulate the way a baby learns to associate words with concepts and objects and it was found that if the associations it was asked to perform were not sufficiently varied and challenging, it simply decided it didn’t like this game and stopped cooperating. $^{10}$

Learning isn't just what neural nets do best; it is simply what they do. During the training phase of a network's use, many example inputs are presented to the machine. After the net has computed a 'solution' to the problem, that solution is either reinforced or weakened by modifying the interconnections within the network itself. As was noted above, a network can learn from every computation it makes. The fundamental nature of this continuous self-modification as a result of experience is one of the most promising, in terms of potential for artificial intelligence, features of neural networks.

In symbolic machines, knowledge representation turns out to be crucial to the issue of learning. The question of when to abandon old representation structures and build new ones is clearly not one which can be answered without specific structures about which we can talk, even if they are only implicitly defined in self-adapting code. As a result, widespread work on learning is really beginning only now that progress seems to be being made in knowledge representation. It seems extremely unlikely, though, that approaches to learning could turn out to be any simpler or more elegant on symbol processing machines than on neural networks.

## Generalization

Rumelhart and McClelland see generalization in neural nets as 'spontaneous', and emerging particularly from the use of distributed representations.

If different instances of objects in a particular class are encoded in a network, a statement about any one of them will have a tendency to be interpreted as a statement about every member of the class.

In symbol-processing machines, we run up against the problem of having to define precisely what we mean by ‘generalization’, before we can start to build programs which demonstrate it. In particular, rule-based approaches must develop explicit new rules to express generalizations. This will involve generating hypotheses and examining the particular cases in which they break down. The quality and order of examples from which the machine wishes to generalize will also have to be taken into account. This process doesn’t claim to be ‘spontaneous.’

Having examined these issues, all central to artificial intelligence, it might seem that there is no contest between neural nets and the more established symbol processing machines: connectionism seems to be a panacea for all of artificial intelligence's ills. Indeed, in pursuing the original goal of AI, the dream of a truly intelligent machine, indistinguishable, as Turing stipulated, from a human being, it is possible that neural networks will turn out to be invaluable.

Human beings, however, have many undesirable features. They forget things, they arrive at decisions without being able to explain how they got there, they suffer from unpredictable mood swings and they aren't very good at mental arithmetic. The features of neural nets which make them useful for simulating human beings seem to be too closely allied to those which we would like to avoid, in constructing reliable and utilitarian programs, for comfort.

Moreover, the ease with which recognizable 'human' traits emerge in the behaviour of neural nets has a darker side. Whereas in symbolic machines, every step must be agonized over and cannot be implemented until it is fully understood, in neural nets we rely much more on intrinsic and ill-understood characteristics of the net itself.

Some researchers believe that even rule-based approaches are already too non-deterministic, from an extensional point of view, for some applications: '... computers are already in large measure inscrutable to us even when they are functioning correctly. Artificial intelligence systems go far beyond anything that can make digital computers seem predictable and comprehensible to us and they each have characteristic flaws that could make them highly dangerous.' $^{11}$ We touched on this point in our discussion of the decoding of knowledge representations: without uncovering every hidden unit and following every single step in a neural network's computation, we can have very little idea of what it is doing apart from what it deigns to tell us itself. The perceived inpenetrability of rule-based systems will be nothing compared to that of neural networks. As Adrian Redgers recently warned the British public $^{10}$ : 'We don't know enough about them to put them in charge of, say, a nuclear reactor.' No indeed.

## References

1. George, F.H. (1979) Philosophical Foundations of Cybernetics, Abacus Press.

2. McCorduck, P. (1979) Machines Who Think, W.H. Freeman.

3. Jones, W.P. and Hoskins, J. (1987) Back propagation: a generalized delta learning rule. Byte, October.

4. Rumelhart, D.E., McClelland, J.L. and The P.D.P. Research Group (1986) Parallel Distributed Processing: Explorations in the Microstructure of Cognition. Volume 1: Foundations, The M.I.T. Press.

5. Searle, J.R. (1980) Minds, brains and programs. Behavioural and Brain Sciences, 3 (3).

6. Searle, J.R. on Voices, Channel 4, British television, 12th April, 1988.

7. Schank, R.C. (1987) What is AI anyway? AI Magazine, Winter.

8. Abu-Mostafa, Y.S. (1986) Neural networks for computing? In Denker, J.S. (ed.), Neural Networks for Computing, A.I.P. Conference Proceedings, No. 151, American Institute of Physics.

9. Winston, P.H. (1984) Artificial Intelligence, Addison-Wesley.

10. Matthews, R. (1987) Computer in a tantrum holds up 'baby' project. The Times, 14th April, 1988.

11. Pullum, G.K. (1987) Natural language interfaces and strategic computing. AI and Society, 1, 47–58.

## Biographical notes

Ian M. Donaldson was born in Lancaster, England, in 1966. He spend his childhood there and in Glasgow, Scotland. He left Hutchesons' Grammar School, Glasgow, in 1983 and graduated from the University of Glasgow in 1987 with a B.Sc. (Hons.) in Mathematics. His first contact with artificial neural networks was during 1988 on an MSc course in the Foundations of Advanced Information Technology in the Department of Computing at Imperial College, London. It was during this course that this article was written. He can now be contacted through Professor I. Aleksander, Department of Electrical Engineering, Imperial College, Exhibition Road, London, SW7.
