---
otero_id: 16980
otero_key: "WXDJH3SP"
title: "The AI potential of model management and its central role in decision support"
authors: "M. Jarke; F.J. Radermacher"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90002-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The AI Potential of Model Management and Its Central Role in Decision Support $^{1}$

M. JARKE \* and F.J. RADERMACHER \*\*

\* Fakultaet fuer Mathematik und Informatik, Universitaet Passau, 8390 Passau, FRG

\*\* FAW (Artificial Intelligence Laboratory), 7900 Ulm, FRG

The paper stresses the general idea that ‘intelligence’ may be viewed to a great extent as the ability to model relevant parts of reality and to draw relevant conclusions from such models. Consequently, future software systems should be able to adequately handle a significant body of models for specific domains together with associated algorithmic tools. With respect to decision making and decision support, which require a high degree of cognitive sophistication, this leads to the quest for integrating into DSS results from model-oriented research in fields such as stochastics, statistics, decision theory, operations research and business applications. Based on such modelling capabilities, a DSS should be able to take a more active, normatively based role in aiding a decision maker. This kind of support requires strong interactive capabilities, driven by online computational results and based on parallel problem exploration with partial models, incomplete information and robust solution methods. Additionally, such multi-level simultaneous use of a great number of interdependent models and associated algorithmic tools requires in itself an increased sophistication in model management. This should include a dynamic, performance-driven and adaptive use of the available algorithmic tools which actively addresses issues possibly overlooked by the user. In establishing this kind of sophistication, extensive use of available AI techniques will be in order. The paper tries to establish some guidelines for advanced system designs aiming at such sophisticated, highly integrative solutions.

Keywords: Artificial Intelligence, Knowledge-based Systems, Decision Support Systems, Deep Modelling, Distributed Systems, Genetic Algorithms, Modelling, Model Management Systems, Normative Decision Support, Statistical Adaption, Stochastic Bounding Techniques.

## 1. Introduction

The use of sophisticated modelling techniques and algorithmic tools from many classical disciplines has recently seen a comeback in popularity among DSS researchers. A workshop on model management at the University of Texas at Austin resulted in a special issue of the DSS journal (Decision Support System 2, 1 (1986)). In the IFIP Working Conference, 'Decision Support Systems: A Decade in Perspective' (see [47]), Peter Keen criticized existing DSS as providing only passive support, i.e. they do not exploit the results of other disciplines such as Mathematics, Economics, Management Science, Business Administration and Cognitive Psychology to the extent that they

![](/api/attachments/WXDJH3SP/fulltext/images/77b63bb60bb6b0c60c4cc64247e920d912e821d5874299f517c5e0b948567b7d.jpg)

Franz Josef Radermacher is the scientific director of the FAW (Artificial Intelligence Laboratory) Ulm and also has a faculty position for Data Bases/Artificial Intelligence at the University of Ulm which presently builds up a new Computer Science curriculum. Before, he was Professor of Computer Science and Operations Research at the University of Passau and took part in building-up a new Computer Science curriculum in this place. In 1980/81 he stayed at the University of

California/Berkeley as a visiting researcher. Prof. Radermacher holds Doctoral degrees in Mathematics from the Technical University in Aachen and in Economics from the University (TH) in Karlsruhe; his habilitation in mathematics was effected at the TH Aachen. Presently, he is also President of the Society for Mathematics, Economics and Operations Research (GMÖOR).

Matthias Jarke received the Diploma degrees in business administration and computer science in 1977 and 1979, respectively, and the Ph.D. degree in economical sciences in 1980, all from Hamburg University West Germany. He is now a Professor of Computer Science at the University of Passau, West Germany. Formerly, he held faculty positions at New York University and Johann Wolfgang Goethe University, West Germany. His research interests include the design, evaluation, and optimization of high-level database interfaces to end users, decision support systems, and expert systems, both from a systems programming and from a user perspective. He is currently leading ESPRIT project DAIDA which investigates knowledge base management systems for database software development and maintenance. He is the author of a number of articles and book chapters on computer science and business subjects, and of four books in these areas. Dr. Jarke is a member of the Association for Computing Machinery, the American Association for Artificial Intelligence, and the IEEE Computer Society.

give active advice to decision makers. Researchers in these different fields have continually come up with new sophisticated methods and models, but only specialists can build, integrate and use them.

There is some hope that artificial intelligence methods for knowledge representation and planning – when adequately integrated with the results from more classical fields – can go a long way towards the kind of normative support or even extended support (which would include problem identification) desired for the next generation of DSS.

However, how can the problems of knowledge acquisition and merging in the presence of narrow specialization of experts be overcome? How can the complex issues of uncertainty and preference modelling be dealt with in a sufficiently general and normatively correct fashion? State-of-the-art systems (cf. [29]) provide a lot of general tools, but only a limited normative basis and assistance in applying them correctly and consistently.

Given this situation, the present paper aims at giving at least partial answers to some of the questions posed. This is done in the context of a more general discussion of the nature of the basic problems involved, building on contributions of many scientists and on the authors' personal experience with these questions. The organization of the text is as follows: We regard consistent decision making in a changing and uncertain environment as one of the dominating, everywhere present and most sophisticated human cognitive abilities. Therefore, section 2 starts with a general discussion on our understanding of the nature of intelligence. We identify modelling, model management and inference in models – properly understood – as key elements of intelligent behaviour (cf. also [36], [40]). Various types of models are involved here, ranging from knowledge bases in artificial intelligence, to frameworks for genetic strategies and to all kinds of 'deep' models from e.g. statistics, stochastics, operations research, decision theory and applied mathematics.

In section 3, we argue for a type of advanced, normative decision support, obtainable by appropriately integrating modelling tools from various disciplines, with particular emphasis being given to decision theory. Such normatively-based tools are far beyond the scope of present day solutions. In this respect, we add some remarks on the history and the current status of model management in decision support in section 4; we also sketch a three-layered architecture for a normatively-based model management system, that is presently being realized by the authors of this paper. Finally, section 5 closes with a summary and some general conclusions drawn from the previous considerations.

## 2. Modelling and Artificial Intelligence

Making adequate decisions over long time periods in a changing environment and subject to incomplete information, misinformation, uncertainty and changing preferences is one of the central and most sophisticated cognitive abilities of man [58]. Understanding the determinants of good decision making resembles the understanding of intelligent behaviour. Of course, the question for the nature of intelligence – and similarly for the potential of artificial intelligence – is an old one that finds many answers, but will hardly be fully settled [13], [26], [27], [76].

We argue in this paper, in line with many other scientists [68], that the essence of intelligence may be – properly understood – the ability to model relevant parts of reality in a meaningful way and to draw relevant conclusions (inferences) from such models as a basis for further actions. Here, notions like ‘meaningful’ are all ultimately to be traced back to the evolutionary principle of ‘relative fitness’ or ‘survival’ as the last interpretation of ‘successful behaviour’ (see also [43], who applies evolutionary principles to the progress of science).

Of course, reality may shrink to sub-worlds, if we restrict attention and performance requirements to very specific domains. Extreme specializations of this type are 'toy worlds' such as the block worlds in special robotics applications or man-made 'artificial worlds', if we deal with e.g. simple games or specific mathematical theories. The more, however, we deal with real-life applications – and decision problems are usually of this type—the more we have to deal with phenomena that man himself understands only to a certain extent. I.e. we deal with a reality for which we do not possess more than (maybe quite elaborate) models which are open to falsification in the course of progress of science [57]. Certainly, when designing advanced systems for decision support, we have to take this central role of modelling into account, however, with a broad enough perspective and understanding of the nature of models.

In the following, we will give short indications to four different – though related – modelling frameworks that will all contribute to system architectures as discussed in section 3. These frameworks are knowledge bases, evolutionary principles, normative theories for handling preferences and uncertainty and, finally, certain ‘deep’ mathematical models of specific problem domains.

## 2.1. Knowledge Bases

Central to understanding, to modelling, even to 'survival' are notions for relevant entities in the respective part of the world (problem domain) together with certain relations or interaction patterns between such notions. As an example, we just mention the ability of man to distinguish units like trees, animals, hills, rivers and so on in his environment as well as his natural ability to apply e.g. an operator such as 'modus ponens' or to make use of simple monotonicity properties which reflect the appropriate frameworks for simple cause-effect relationships and eventual fine-tuning of actions taken in real life.

Such abilities are – on a very basic level – to be understood as a result of evolutionary processes, maybe involving activities of neural-net type or deterministically encoded behavioural patterns. They are abound in all kinds of higher developed animals and not usually associated with the highest cognitive abilities. Still, such abilities form the essential basis for all higher functionalities, i.e. they are the atomic parts from which models may be built and high performance may eventually be drawn. From an evolutionary perspective, this kind of basic structuring of reality comes naturally in taxonomies, i.e. in a hierarchical organization.

This is basically due to the evolutionary process character of gaining increased knowledge over time that to a great extent may be viewed as an ever finer modelling process, driven by a kind of statistical learning, leading to always more detailed sub-entities to be considered explicitly (though, simultaneously, also sometimes structured in new ways by adequate kinds of generalizations). From a certain point in evolution on, the diversity of entities to be handled required a kind of symbolic representation for adequate model manipulation, maybe organized around collections of images.

Human verbalization of such collections led to an extreme degree of freedom in symbolic manipulation, and the human language – properly understood – is about the most mighty modelling tool we know. It allows not only to address extremely narrow basic entities, but also subtle – and maybe not completely understood – interactions and dependences between these basic units to be communicated. Herein, implicit references are often made to bundles of pictures of past personal experiences, maybe even not yet completely symbolically agreed upon inter-personally, and these difficult references certainly add to the apparent problems of machine-understanding of natural language. Certainly, though, the world modelling perspective, underlying present-day research in this field, seems to be the direction in which to go.

Summarizing these few remarks and transforming them to system design, the basic entities involved in a system architecture (such as e.g. which types of system users to distinguish, or which routes to allow for a robot, or which transactions to consider in an office automation, or which patterns of on-line signals to consider in system diagnosis), determine the frame from which a system's competence may ultimately derive. There is, however, one addition to that, viz. meta levels for the modification of basic entities or relations. The partially explicit understanding and use of such modifications is an ability obtained by man very late and the very basis of e.g. modern scientific progress. Its automatization, which includes automatic learning, is particularly hard and progresses slowly. Again, the simpler versions, reflecting partially the nature of the evolutionary process, may be coped with. We just mention things like the splitting of cases into sub-cases (based on other observed entities) or combining different sub-cases to new super-cases. Much harder are processes like 'analogy', 'identification of hidden variables' and so forth. Lenat's AM system [45] and his present work on world modelling [46] deserves credit for demonstrating how far automation of such tasks may presently go.

Combined with additional randomization elements, such approaches may eventually yield a high degree of sophistication and cause ‘surprising’ behaviour with respect to the basic notions and operators involved in systems. However, difficulties along the route are substantial.

We have called this part ‘knowledge bases’. The reason is our belief that the recent essential contribution of artificial intelligence, particularly the field of expert systems, to the problems discussed here has been the establishment of design and programming methodologies and development environments (e.g. object-oriented programming languages, frames, production systems, triggers, elementary logical operators, and so on) that – when properly integrated with contributions from data base theory – allow the automated handling of larger sets of basic entities, case distinctions, elementary relations and so forth in a quite effective way. As mentioned above, this corresponds not necessarily to the most brilliant parts of what we usually call cognitive competence. Still, these more elementary handling processes (mastered to a certain extent by all higher animals) are the very basis for all higher cognitive levels. Such more involved levels are discussed below.

## 2.2. Evolutional Processes

Evolution is the meta-principle that naturally comes along with every process of reproduction, including the building of good support systems. It allows us to understand how higher levels of life eventually carried models of their environment, and even, at a very high level, models of themselves (consciousness). Models are very coarse in the beginning, reducing the whole world to maybe two states (good environment: action ‘stay’, bad environment: action ‘move’). They become more involved over time in this evolutionary process driven by the ultimate criteria of survival.

Basic to survival is often a higher degree of granularity in modelling, e.g. splitting the good state in the above example into two sub-cases of good and very good (depending e.g. on the presence of a certain chemical substance), or, in present days, to classify e.g. sub-cases of a certain cancer in a way that yields significant information about the survival rate.

The principles involved here can be characterized by processes of recombinations and randomization. We note that recombination is a quite safe way to produce new (working) solutions in an (implicitly given) solution space. Randomization is – on the action level – a smoothing device; on the reproduction level it is a cautious way of extending the borderline of the solution space.

Driving this process is again the survival criterion that statistically gives a higher degree of influence on shaping the next generation to those individuals that 'behave' better. With sexual reproduction and group coherence, more weight is put on carrying latent information, spreading of information over group members or even carrying mutually beneficial abilities over various cooperating group members. It is apparent that copying the evolutionary process is our best hope for real 'smart' systems which eventually should show really surprising and impressive behaviour. There is a long scientific tradition in this respect, known as 'evolution strategy' or 'genetic algorithms' [18], [60], [65].

In system design it leads (as an extreme version) to the idea of highly modularized systems that come along in populations. New systems are designed by intermixing blocks from different systems, combined with some further random changes. In doing so, modules are favoured in the mixture if they have been termed ‘good’ or ‘successful’ before, e.g. by the user (without any deeper insight, what really caused this good behaviour). Recent object-oriented approaches to software reusability appear to be moving in this direction. Somewhat weaker versions of evaluationary strategies are statistical adaption, simulated annealing [18], [24] and related approaches [23].

Statistical adaption in its easiest form means that one favours actions successful in earlier stages relative to other available actions by decreasing accordingly the probability of activating unsuccessful actions. Note that this is a way of accumulating knowledge and system-experience over time. We will argue for this type of adaption in section 3, e.g. with respect to learning which algorithmic tool to use in which situation. Of course, this approach should be combined with the possible modification of the notion of ‘situation’ as discussed above, e.g. if we notice that success often comes along with another observed entity, this should indicate a new class notion.

Unfortunately, in most solution spaces such local optimization alone may lead to locally optimal solutions or notions only. The annealing principle therefore to a certain extent prefers worse solutions to better solutions in order to avoid local optimality traps. For stability reasons, the probability of accepting bad steps decreases over time, following basic properties of thermodynamic processes. Note again, that all these 'blind' adaptation processes are only recommendable if deeper (human) insight is missing.

Also, the more vague and unintentional these 'learning' or 'adaption' processes become, the slower they work. There is often no way of using old collected data for training and acceleration of such an adaption process, as the interaction of the constantly modified system with this old data (i.e. the system-user interaction) would be missing. Thus, adaption is slow; it is comparable to the adaption of living beings, thus limiting exaggerated expectations when seen for applications in typical sophisticated applications involving constant man-machine interaction.

## 2.3. Normative Theories for Handling Preferences and Insecurity

We did already argue for decision-making as one of the most involved cognitive tasks that man is confronted with. In real life applications, decision-making is often closely related to questions of success or survival.

As we deal with processes in time and have to consider situations with only partial information and a high degree of uncertainty, we are generally confronted with the risk of a 'bad' decision (seen ex post), whatever we decide ex ante. Good decisions can in general at best increase the probability for a good outcome, but cannot guarantee it. What constitutes a good outcome is in general a subjective evaluation of effects and will usually mean to judge a number of conflicting aspects of a result in comparison with the same set of conflicting aspects of another obtainable alternative. Often one outcome will be preferred in some aspects, while another will be in other aspects. Moreover, preferences may change over time; even if a decision yields the originally preferred solution, it may no longer be wanted when realized. Luckily, it may also be the other way round.

The very involved nature of these different intermixed aspects of preferences and uncertainty have somewhat limited the degree to which humans have a systematic and uniform ability to cope with difficult decision situations in a satisfactory way. We know from cognitive psychology that there is a quite stable human reaction pattern only in relative simple decision situations.

In more complicated situations, however, reactions may become instable, may possibly be revised after a thorough examination, and may often also contradict certain logical principles that the same person wants to follow. Research on such so-called Bias phenomena [16], [25], [28], [37], [54], [64] in behavioural sciences constitutes an important help in the design of user interfaces when trying to translate ‘naive’ user models into normative (mathematical) models employed by the system.

The main underlying ideas in this area date back to the basic work and central representation theorem by von Neumann and Morgenstern [73] that identifies good decision making as maximizing the expected utility over an action space with regard to (subjective) probabilities for world-states involved and with regard to a (multi-attribute) utility function for the evaluation of (vectors of) results.

This utility-theoretic framework is by now very rich, due to contributions such as [17], [39]. Its use in decisions of great importance (e.g. placement of energy plants, of atomic waste sites, of airports etc.) has been very successful [38]. There exist by now also a number of software tools, e.g. for finding single or multi-attribute utility functions or for doing decomposition in this context (see e.g. [74], [75]). Available are also quite general decision-theoretical framing systems, e.g. PREFCALC [31] or MAUD [30]. MAUD even has a component that uses statistical factorial analysis to obtain indications to missing utility dimensions in particular decision situations. It is significant to note that in spite of all this solid normative basis and quite involved methodological background, the use of decision-theoretical models in decision support and expert systems is not common.

Similarly, explicit modelling of user preferences as part of man-machine interface design and user modelling has hardly been exploited. Also, choices available on all levels of system operation are often not made explicit. The dominating, quite simple approach is instead having the user translate dissatisfaction with certain solutions into additional constraints. This means in effect a steady shrinking of the solution domain instead of the adaption of the goal function over the whole domain. Eventually, the ‘best’ solutions (or even the existence of a solution) might be lost in this way. To cope for that with methods of e.g. truth maintenance (which in this context means a possible later elimination of constraints introduced before) is quite involved and inefficient.

As an alternative we argue here for the use of a general multi-attributive decision generator mechanism for choice control on all levels of system behaviour. In this, attributes employed should be based on value dimensions and proper measures should be taken to avoid cognitive biases (cf. the papers of R.L. Keeney and D. von Winterfeldt in this volume). In particular, a means to obtain and represent preferences in a declarative way has to be offered to users.

Besides preference modelling, probability theory is the other basic normative ingredient to general model building in decision support. Contributions from this field to the treatment of applications are so abundant that they need not be discussed here. We just mention general principles like ergodicity, limit theorems, best statistical tests or, more recently, stochastic bounds (in the sense of stochastic dominance [41], [42], [49], [67], [71]). With these general results and principles, probability theory partly overcomes the data acquisition problems that it seems to cause in the first place, and this is done in a normatively correct fashion.

Note that such general theories and theorems, as present in the context of e.g. decision theory, probability theory or statistics, form about the strongest inference mechanisms available. For reasons of efficiency and consistency, their use is recommended over other forms of knowledge-processing, whenever they might be employed. In many applications, e.g. queueing type problems, reliability applications, quality control or scheduling problems, the stochastic aspects may be the dominating elements of modelling.

In such situations, really advanced systems have to be able to do automatic stochastication and sensitivity analysis for the treated problems (even in cases where users do not know what probability is), in order to internally validate the stability of solutions and, if needed, communicate certain risks to the user.

There is a lot of recent literature on 'fuzziness' and different approaches of handling such phenomena. Certainly, much of what we just discussed belongs to this wide paradigm of fuzziness. But not only does it belong to this field, instead, it seems that the classical frameworks constitute to a great extent the scientific answer to such problems. This answer is based on many decades of thorough scientific work and corresponding bodies of theories and hard theorems. Consequently, it is not only the authors' position that most fuzzy phenomena can be handled with the classical tools from utility theory and probability theory, when used in a sufficiently broad context, i.e. valuation functions and extended models of uncertainty. For the latter aspect, the Shafer-Dempster theory of evidence [66], with its relations to classical probability spaces as well as to uncertainty values in expert systems, should particularly be mentioned here. The paper of T. Kaempke in this volume gives some remarks on this more general framework and reports some of the arising difficulties with such generalizations.

## 2.4. Deep Modelling

A recent trend in the field of expert systems distinguishes second generation expert systems from earlier systems by the use of “deep models” as a background for ‘flat’ knowledge alone (flat knowledge being of the type addressed above as knowledge bases). While flat knowledge in typical expert system applications tries to catch the behavioural patterns of competent application specialists, the idea of deep knowledge processing is to use, in addition, general scientific insight into particular domains, usually available in the form of theories, basic or first principles, analytical models and so forth.

Advanced decision support systems, as intended here, will even have to go a step further, integrating knowledge on a number of deep models, on the algorithmic handling of operations in such models, on addressing the right type of data sources for certain computations and so forth, i.e. they should behave like support teams, composed of experienced practitioners, scientific staff, computational experts and so forth. Deep modelling, as a general topic, is almost as broad as formalized sciences in general.

Therefore, it cannot be addressed here in any detail; and maybe, it presently isn't a particular issue for AI research at all. We just mention the use of contributions of game theory (e.g., Nash solutions) as a tool for organizing automated mediator components in group decision support systems as a simple example of what we are thinking about in this context (for mediator systems cf. [32], [33]). Given the diversity of issues in deep modelling, there seem to be a few general topics, though, that might be of particular interest in decision support systems with emphasis on applications in economics. Central is certainly the general decision-theoretical and probabilistic background discussed separately above.

Furthermore, descriptions of mechanical phenomena via systems of differential equations should be mentioned. Typical for design and planning tasks are the usual models from operations research, optimization theory and applied mathematics. Associated with such models are strong inference operators such as fix points, limits, confidence intervals, optimal values and so forth. Finding such strong solutions is generally a very involved task. We mention here particularly problems with the numerical stability of solutions, a central topic in the use of supercomputers, particularly when dealing with huge systems of differential equations or involved integration processes.

The phenomenon of NP-completeness [20] of many discrete or combinatorial optimization problems is a severe one (and often not taken seriously enough). One answer to these computational difficulties is a fine granularity which classifies special problem instances according to their algorithmic behaviour, and further to employ all kinds of heuristic approaches in a skillful way as best choice if principal algorithmic difficulties cannot be overcome. In a field like scheduling ([2], [51], [52], [53]), one distinguishes hundreds of sub-cases and a rich body of algorithms [44], [61], whose proper use and control by now constitutes an involved problem in itself.

Integration into an automatized system does not only mean increased algorithmic efficiency, but also an adequate modern form of scientific knowledge transfer that is furthermore open to automatic performance improvement in tool application via statistical adaption. Tool use will aim at exploiting distributed processor environments and this should be done in a way that hides the details from the user. All of the knowledge-based constructions, genetic principles and normative requirements discussed above apply to the organization of these computational tasks as well. This includes e.g. the use of hierarchies of models (cf. e.g. the contributions to decompositions in discrete structures presented in [50]) together with general operators such as 'simplify', 'generalize', 'stochastify'. Even more one will have to organize all such tools towards the general aim of approaching reasonable solutions for problems. Determining successively improved upper and lower bounds is one of the most successful general guidelines in this respect.

## 2.5. Summary of Section 2

To summarize section 2, we stress the idea of an integrative use of many different modelling tools in advanced decision support systems. The recent contributions from artificial intelligence open the door to completely new solutions, while decision and probability theory form the classical modelling framework, that is: the hard normative basis for an extended type of support, particularly for application in economics.

Certainly, systems as intended here are of an interdisciplinary and very involved nature. Consequently, there is hardly a chance of having knowledge engineers doing this work by themselves. Instead, a broad cooperation of active scientists from related subject areas is required here. In such a cooperation, all subjects covered are so crucial that each of them possesses a kind of bottleneck property. This is certainly the reason why many system developments behave so poorly outside an extremely narrow problem area, and when confronted with slight problem modifications. Consequently, the right kind of scientific cooperation has to be organized. If models can be developed and organized effectively by such a cooperation, there could be wide-ranging effects, from the use of model bases in education to a much increased speed of knowledge transfer from science to practice.

We know of a number of places where this is being attempted, among them a number of Dutch universities, the University of Passau/FRG and the FAW (Artificial Intelligence Laboratory) in Ulm/FRG. Characteristic aspects of ongoing research activities at the places mentioned are reported in the next section.

## 3. Design Aspects of Advanced Decision Support Systems

As discussed in the introduction, there is recently a strong emphasis on a research agenda that aims at a new generation of normatively based decision support systems. Such systems have to be of an integrative nature, combining contributions from a number of scientific fields, ranging from artificial intelligence to e.g. decision theory, operations research and applied mathematics.

In section 2 we have argued that a multitude of modelling tools, ranging from knowledge bases to evolutionary principles and deep mathematical models and theories, has to be incorporated in order to allow systems to show a convincing behaviour. One of the problems faced in such developments is the impossibility of keeping a real narrow focus; when aiming at solutions of the degree of cognitive sophistication described, the internal requirements become so overwhelming that necessarily not only an application system will be built.

In effect, with little additional effort one will realize simultaneously at least also a support tool for producing course material, a computer-aided instruction tool, a modern scientific documentation and knowledge transfer instrument, an on-line test and installation environment for new algorithmic tools in the respective fields and, finally, a device for automatic knowledge acquisition concerning the use of particular algorithms in particular problem instances.

This richness of potential system performance stems from the fact that in addition to the detailed MODELLING of the APPLICATION DOMAIN, at least three other modelling processes have to be performed in sufficient depth. These quite general, only partially application-dependent modelling tasks concern USER MODELS, MODELS OF THE DIALOGUE PROCESS and EIGEN-MODELS OF SYSTEMS. All these constitute separate general research issues actively addressed by scientists all over the world. We just mention a few topics that we would like to see to be actively treated.

In user models, we regard the integration of an explicit representation of user preferences and user estimates of randomness (in an appropriate degree of precision) as essential. Concerning the dialogue process, systems should continuously draw on all kind of available explicit or implicit knowledge in order to focus the dialogue to essential aspects. Finally, Eigen-models are the very basis for any advanced integration of concepts from the field of genetic algorithms into system design. Systems might eventually enrich their Eigen-models by analyzing their own reactions to certain inputs. Good system design would mean that this enrichment really goes into the direction of the true system design. Needless to say that a system should supply a certain amount of processor capacity just for these internal learning and adaption processes. In the following, we shortly give six guidelines for system design (cf. [34]), as intended in this context.

## 3.1. Support the Modelling Process

Given a particular application domain, user inputs are interpreted as aspects of his internal problem model that have to be translated consistently into the formalized internal model used by the system. Usually, imprecision or incompleteness on the side of the user will lead to classes of internal system models, resulting from parameter variations. Graphical tools, direct manipulation, incremental design and maybe even natural language constructs may gradually be accepted as user input into this transformation process.

Insight from cognitive psychology will be required for debiasing in this context. Internally, the system will use bounding techniques, hierarchical structuring and so forth to cope with the imprecision or incompletion of the user's input. A great help for system design lies in the clear separation between the formalized internal model used by the system and the user's maybe 'naive' personal modelling; however, the knowledge representation should also offer 'escapes' (exceptions) for stating information that cannot be translated into the system's model.

Inevitably, the modelling process will reveal new problems and inconsistencies in the user's initial ideas. Another, equally important aspect is therefore the representation of the modelling process itself in the knowledge base [55]. This allows methods such as reason maintenance to restrict the re-modelling that has to be done to resolve such problems, similar to sensitivity analysis methods in OR [11].

3.2. Normatively-Based Forms of Generating Solutions

Besides help in the finding and definition of problems or opportunities, what users ultimately expect from decision support or expert systems are solution proposals for the given problem instance. The better the proposals, the better the system, i.e. proposing good solutions is what users primarily and essentially expect from a system. Whatever it does additionally, e.g. user modelling, self-analysis and so forth, is intended to ultimately improve the generation of good solutions.

In spite of this central importance of solution generation, many available systems aim at just one solution and have the user to decide whether to keep it or to ask for another alternative. This is a very poor form of support. First of all, there are often large (exponentially large) solution spaces. Users can explicitly consider only a very small fraction of these solutions via proposals by the system. There is then generally no information available on whether there are much better solutions (with view to the user's preference) still hidden in the solution space. Secondly, in a number of applications, finding any or the best solution are algorithmically both already NP-complete problems. Therefore, we argue in this paper for a normatively-based decision support.

This requires the best possible user-specific decision-theoretic modelling of the problem and the most competent use of available algorithmic tools to produce as good as possible a solution proposal. If this solution is rejected, additional information becomes available to adapt the present model to come closer to the fitting model for the user's problem. This normatively-based approach to the generation of solutions is usually continued until the user accepts a proposed solution.

In accepting such a solution, he has a kind of guarantee that, at least with regard to the available modelling framework and algorithmic tools, this is the best solution concerning his own preference structure that scientific support can offer him under the particular circumstances.

## 3.3. Usage of Implicit Information

The translation process from a user's private model into (classes of) internal models of a system can be viewed as an incremental process of narrowing the focus. The more hierarchical structuring and bounding techniques are used, the earlier partial information on potential (classes of) solutions become available internally to the system.

As user's time and patience are very scarce resources and complete problem modelling is often impossible, such implicit pre-information has to be used excessively to focus the dialogue. This is so basic that going from rough to fine models and starting from estimates and bounds towards exact solutions should be tried under almost all circumstances.

When reasonably organized, early vague results will help to reduce unnecessary questions, while the user's inputs as well as the results from early coarse models will ease the algorithmic difficulties in finding good solutions on the more detailed level. In fact, this seems also to be a way to ease the algorithmic difficulties with e.g. NP-complete problems.

## 3.4. Reasonable Use of Available Algorithmic Tools

As argued above, normatively-based decision support system will try to produce the best solution proposal, given a certain state of modelling and certain algorithmic tools. Such tools concern the determination of e.g. fix points, optimal values and so forth with regard to often very nasty problem formulations.

This is done with the aim of a true modelling of user intentions rather than forcing the user into particular modelling frameworks just because these can nicely be handled. Consequently, finding good solutions will often be a very involved task for which no easy or standard or generally successful algorithmic method is available. Available are instead complicated distinctions of special cases together with all kinds of hierarchical and bounding approaches. Together with various heuristic methods they will have to be employed simultaneously in an integrative way, possibly using distributed processor environments. The reasonable approach here seems to be a knowledge-based translation of the algorithmic task to be performed into particular given processor environments. The individual algorithms in such an environment should be designed so that they have certain monotonicity properties with respect to solution quality over time, especially in a real-time environments with hard time bounds.

In doing so, processor time should generally be attributed in a randomized (thus smoothly adaptable) fashion, favouring with higher probability those tasks that are particularly promising in a special problem instance. The general knowledge-based separation of this distribution task from the inner system architecture favours asynchronous forms of concrete system development. Note that this knowledge-based distribution process of algorithmic tasks is a very nice example for combining all kinds of statistical or genetic adaption tools, as argued above. In this example, a system may accumulate over time experience on which tool to use in what situation. This information becomes available to the expert user as a useful additional spin-off.

## 3.5. Explanation Facilities

One of the most successful and user-friendly properties of present-day expert systems is their ability to give explanations for proposals made. Even if such explanations are often essentially just chains of successful implications or term replacements, they can be extremely useful to the user. If the chain of arguments is convincing to him, he can gain full confidence in a solution by just checking the steps, but without having to find a successful deduction path by himself and without having to master by himself facts and rules involved.

It is clear that similar facilities have to be offered by advanced decision support systems. In a number of aspects, such explanation facilities will have to go beyond the presently available solutions. In particular, explanations should be given from the viewpoint of goals and constraints to be satisfied. Depending e.g. on the degree of deep modelling involved, explanations have also to be tailored towards the user's abilities. For expert users they might in special cases even contain references to the literature, demonstration examples of particular algorithms, presentation of bounds for e.g. NP-complete problem instances (where at least the bounds may be verified fast by the user), explanations for the use of particular algorithms in certain situations (including perhaps a tracing of involved realizations of randomization steps) and so forth.

On top of that, references to coarse model variants, to stochastic perturbations of the models used or e.g. to the results of various types of sensitivity analysis undertaken (e.g. concerning preference change), may be needed. Certainly, the system's Eigen-model will provide an important ingredient for the realization of a well-founded explanation facility for future advanced systems.

## 3.6. Comfortable Development Environments

Designing systems of the intended type involves the collaboration of many researchers over long periods of time as well as experimentation with variants of systems. With regard to applying forms of genetic adaption, we even have to think about ‘populations’ of systems and their adjustment over time.

Comfortable development tools must include the control of system variants, statistical evaluation of different versions, and so on. The requirements towards integrated development support systems, allowing the simultaneous handling of data, methods, models and system versions via expert system-like manipulation and control devices, can only be satisfied with substantial contributions from the respective disciplines in computer science. We mention here in particular object-oriented data base systems and hypertext manipulation systems [3], [4], [10], [35]. Some considerations in this respect are given in the next section of this paper.

## 3.7. Summary of Section 3

If we see the modelling necessities reported in this section in context with the six guidelines for advanced system design (just discussed), it becomes apparent that we deal here with a research agenda that requires a certain time horizon for full realization. And in spite of the application-oriented nature of the problems posed, competent solutions necessitate quite a number of research contributions of a very basic nature.

The broad scope of problems that have to be addressed makes international cooperation a necessity. Presently, the authors are working on a number of projects that address at least parts of the question posed in this paper, in the context of the ESPRIT-DAIDA project [35] and by a system development in the field of scheduling, described more detailed in [2]. At a rather basic level, there are also in preparation internal projects at the

FAW in Ulm that address the design of some general tools with the idea to use them in the majority of applied system developments in the areas of CIM, office automation, environment information systems and advanced automated cars that are going on in this institute. Such general components are:

## - A General Decision-Theoretical Framing System:

This system aims to support the declarative formulation of relevant attributes for the evaluation of results as well as to support the determination of the associated utility functions. Similar, it aims at obtaining (subjective) probability distributions involved. Decomposition methods and approximation techniques will be used together with a consequent object orientation. Furthermore, some debiasing tools will be incorporated. The framing system shall be usable in all kinds of explicit choice making.
- Generating Robust Stochastic Bounds in Systems with Monotonic Behaviour:

As reported in [2], robust stochastic bounds form a contribution from applied stochastics that can help in overcoming some of the data deficiency and computational problems in stochastic models, particularly as far as special distributions and stochastic dependences are concerned. This theory [41], [49], [71] allows a computationally efficient way of determining a bound to the distribution functions of arbitrary monotonic system characteristics (such as maximal flow or shortest project duration in networks). The bounding property holds with regard to all distributions whose marginal distributions have certain properties, with arbitrary stochastic dependencies allowed. Where this tool can be applied, it constitutes a very strong inference mechanism that allows a number of pre-decisions to be taken on a few highly aggregated and incomplete data and thus at a very early stage of analysis.

## - A General Framework System for Genetic and Statistical Adaption:

This system is intended as a tool for all kinds of system modules to be embedded in an individual control environment that allows the statistical update of parameter values, the eventual self-adaptive modification of basic notions and classification schemes via standard logical operators and, in principle and in a longer perspective, also the controlled recombination and stochastic perturbation as required for system reconfiguration, orientated on basic evolutionary principles.

\- A Blackboard Architecture for the Knowledge-Based Distribution of Algorithmic Tasks:

This is again a very general tool that builds on previous work concerning the design of a DSS for scheduling applications [2], [15]. The distribution of tasks will be done in a randomized fashion, oriented as much on the estimated performance chance of certain algorithmic tools as on the availability of different types of computational resources. Integrated into the estimation functions is a classification of meaningful sub-cases. The design will be object-oriented in such a way that it fits into the general framework system for genetic and statistical adaptation.

## 4. Model Management Systems

While the two previous sections were concerned with more general considerations, the remaining section gives some remarks on more specific system realizations, aiming at the kind of model management abilities that will be a necessary base for the advanced systems we propose.

## 4.1. The Task of Model Management

In the history of DSS, two parallel developments can be observed. A large number of DSS and expert system software packages have emerged that combine sophisticated user interfaces and model-building technology with relatively shallow model representations. In parallel, operations researchers and others have developed more and more sophisticated models; environments for creating and maintaining such models have also been introduced, but they are intended for specialist usage only and the model development process closely resembles complex information system development [1], [48].

Since the development of the model management idea in the mid-1970's it has been hoped that integrated data and model management systems, possibly using AI methodologies, can bridge this gap, thus also transferring theoretical advances faster to practical applications. As data base management systems factor out common data management tasks from application programs, model management systems are intended to provide generalized support for the construction, usage and analysis of a large class of models in an organization. The major tasks of a model management system can be arrived from either an individual or an organizational perspective.

From an individual perspective, MMS aspects are:

\- structuring a decision problem in terms of one or more available analytic tools;

\- facilitating the use of tools [14];

\- analyzing and explaining the results of tool use [9].

From an organizational perspective, MMS are intended to avoid double work, inconsistencies, modelling errors by individuals and security problems by managing the base of models as a centralized organizational resource. A model base can also be viewed as a knowledge exchange medium among different specialists and decision makers. By preserving modelling experiences in a knowledge base, one can also accumulate a kind of corporate memory for reuse in analogous situations.

Model management involves knowledge about a number of concepts and tasks related to the construction, validation, usage and analysis of models. Elam et al. [14] distinguish four kinds of such knowledge: method knowledge, application background knowledge, language knowledge and model documentation. In a general sense, all of these aspects require a number of theories that must be incorporated into a model management system:

\- There must be an abstract representation of models. Such a representation is intended to facilitate MMS capabilities such as the combination of models, the explanation of their capabilities and the definition of their interfaces to data sources and result reports. Good examples of such representations include the relational theory of model management [6], the structured modelling approach [22], and frame structures [12]. From a programming language viewpoint, all of these are closely related to concepts of abstract data types in which a model is represented by its interfaces, and a formal definition of its preconditions and input/output relationships.

\- There must be one or more modelling paradigms. These mimic basic strategies used by system analysts to structure a problem in terms of a given set of analytic tools; obviously, such strategies depend on the kinds of available tools and (possibly) the application area. One such paradigm could be the cost-based search for a solution strategy in the space defined by feasible compositions of a large set of existing methods [69]. Another well-known paradigm is recursive problem decomposition, combined with a classification of sub-models as standard model types [56]. Moreover, the existence of application domain-specific knowledge may provide structure to the modelling process [5]. It should be noted, however, that any such paradigm necessarily narrows the view of the person who uses it. Therefore, the knowledge representation language should offer extensibility and multiple viewpoints to look at a problem.

\- Finally, the modelling process should be documented in order to understand the structural decisions underlying a mathematical representation. Such process knowledge can facilitate the sensitivity analysis of models with respect to major qualitative changes [11]. Additionally, process knowledge also enables an interactive modelling process to be interrupted without loss of information and a parallel execution of multiple models simultaneously by one or more users.

As mentioned, some results have been obtained in all of these areas. However, the existing concepts are not rich enough to support advanced modelling and solution control procedures as proposed in the previous sections, and the research on the integration of method and application domain knowledge is very limited. Simple solutions, such as replacing advanced mathematical models by rule bases, only work in special cases. For example, relational model management only considers input/output relationships, and it would be difficult to express within this framework the fact that one model is a simplification (or a stochastication) of another one. As argued above, such relationships might e.g. be needed to compute lower and upper bounds on the solution of other models, or to explain its results to a (naive) user [21].

## 4.2. A Research Program

Given such limitations, an interdisciplinary group of researchers at the University of Passau and other places, including programming language and data base system specialists, mathematicians and various business specialists some years ago began the creation of a scientific environment and a hardware/software basis that would enable advances towards normative DSS with a long-term perspective.

The conceptual approach taken is based on experiences with the expert system approach in AI, with the construction and use of sophisticated, computer-based operations research models and with some tailored DSS for various application areas. These experiences indicate that a powerful, normatively-oriented DSS must convey a fair amount of application-specific knowledge in addition to expertise on how to use a (possibly large) set of potentially applicable models and associated algorithmic tools.

After reviewing a number of architectural proposals for DSS (e.g. those by [7], [8], [70] and [72]) and after organizing several working conferences, e.g. [40], [59], they came up with the following concept:

\- There should be an application-independent kernel DSS. In this kernel, a knowledge-based model management system supervises the utilization of an integrated base of data, algorithms and models, using a multi-attribute decision generator mechanism for control.

\- The kernel system will also provide 'hooks' for installing various application-specific knowledge bases and environments, thus leading to application-oriented DSS generators. These should be built directly by university experts, thus circumventing some of the usual knowledge engineering problems and combining the kernel system with state-of-the-art expertise in business applications.

\- Although system builders and system users will need different kinds of user interfaces, it seems to be very important to provide at least a common base of formal semantics in the interaction languages. The design of this formal kernel was therefore separated from user interface technology and tools of a design and usage environment.

These considerations lead to a general research agenda, consisting of three methodological levels, viz.

(1) environment and interfaces

(2) a decision-theoretical kernel system

(3) specific end-user DSS

Work at level one (environment and interfaces) should aim at the establishment of a rich, tailored development environment based on specific language constructs for DSS. In particular, the aim is for a common semantic basis for imperative, logic, functional and object-oriented language styles leading to language support for at least three types of user interfaces, viz. the professional computer scientist interface, the configuration interface for application-oriented system builders and, finally, the interface for the decision maker.

Given the intended degree of system sophistication, the latter interface asks for special care. For it is here, that conceptually demanding data, such as joint distributions and multi-attribute utility functions, are required from users which might not even be familiar with the concepts involved. As mentioned in the previous sections, methods for debiasing (seen from the background of cognitive psychology) as well as aggregation techniques and dialogue management, based on results gained from robust solution methods, are major features for addressing these difficulties.

At the second level (a decision-theoretical kernel system), a general solution framework for specific on-line decision-making tasks is asked for. This should include the building of a generalized decision generator which essentially produces strategy proposals of high subjective utility, given a set of (possibly incomplete) data and a set of available algorithmic tools. From a representational point of view, adequate forms of model based reasoning will be required in this context. The tools used may be of a general or of a problem-specific nature. Contributions from the areas of applied probability, statistics, numerical mathematics and optimization theory are charged with augmenting the general algorithmic base and taking care of the proper use of these methods by providing suitable interfaces and test-routines for algorithms.

The special systems on the third level will, of course, have to provide specific algorithms with their own system developments. Actually, in a realized system there will be hundreds of algorithms for internal use that take care of model changes and data changes in steps like automatic stochastification, model perturbation and monotonic model variation. All these steps aim at improving the sensitivity analysis of problems which in turn may trigger other computations or the need for further information elicitation from the user.

Finally, on the third level (specific end-user systems), application domain-specific topics have to be addressed. Domains attacked should be such that detailed competence concerning modelling and algorithmic treatment is available in the research group. Senior scientists from these fields should take over the responsibility for the domain-specific aspects of the particular end-user systems. Contrary to many recent developments of expert systems, the steady inflow of expert knowledge and expert interest can be guaranteed in this way, as is the personal basis for field studies of system performance in contact with potential users.

The aims of these systems, as discussed in the previous sections, are:

\- to find normatively good solutions based on a detailed analysis of the user's multi-dimensional preference structures (this is in contrast to single 'what if' analysis as well as in contrast to naive single-objective optimization),

\- to use a tailored dialogue with the user that concentrates on essential information needs,

\- to control search in a large problem space and

\- to take into account automatically certain aspects that tend to be overlooked by model builders, in particular uncertainty issues.

## 4.3 An Architecture for Normative Model Management

It is one of the driving expectations of this research perspective that in spite of the differences between various fields of applications a large set of common aspects concerning the design of normative DSS can be isolated. This subsection proposes an architecture for advanced, normative model management systems that can hopefully form a common basis for many developments in the field, as they will be undertaken e.g. at the FAW (Artificial Intelligence Laboratory) in Ulm.

When building such a system, there are problems of size in the model base as well as in the number of concurrent processes, and there is a large number of dedicated control strategies for integrated model construction, solution, data access and result management. It is difficult to imagine that this broad variety of tasks, ranging from purely administrative to high-level expertise can be accommodated by a single kind of system. We are therefore developing a layered architecture of three loosely coupled levels:

\- object-oriented DBMS kernel system,

\- integrated data, algorithm and model administration system,

\- knowledge-based system for manipulation of model bases.

Level 1 is an extensible data base programming kernel system based on the representation of complex objects, a predicative style of querying and integrity management, and a modular software organization. This is a very active research area; examples of systems under development in Europe include DASDBS [62], DBPL [63] and GEODE [19]; cf. also [3].

Level 2 adds to this general kernel system some DSS-specific features:

\- the representation of data structures, algorithms and models as persistent abstract data types. Abstract data types allow the formal specification of model interfaces (e.g. time series, sparse matrix representation) that will be provided to store model inputs and intermediate results efficiently.

\- the representation of relationships among the above mentioned objects as data base objects. A classification scheme of such relationships is being defined based on the analysis of complex examples as, e.g. the scheduling system development and the DAIDA project. Aspects include: the input/output relationship between model and data; the fact that the use of one method is a precondition of using another one; generalization hierarchies of objects and models, etc.

\- transaction concepts for (group) decision support. The process by which a user constructs and solves models for a particular problem can be considered as a long interactive database transaction, similar to those in design databases [4]. Such a transaction can involve a large number of sub-transactions, sometimes performed by a group rather than an individual designer.

Concepts such as subcontracting and integration of views are being investigated here. An additional complication is that one decision maker can invoke multiple methods, models and data sources for the same problem simultaneously (optically represented e.g. by multiple windows on a screen), and that these models may exchange intermediate results.

In summary, the levels one and two are responsible for the representational and administrative aspects of the model management system. Our analysis and case studies so far as well as current results of research in design databases indicate that this part of the system can be developed fairly independently of any particular application area or mathematical method. In contrast, the level 3 component is specifically dedicated to bring in higher levels of modelling expertise as a basis for a type of model based reasoning. Some of the expertise involved will necessarily be determined by the nature of the application problems considered and by the analytic tools used. Therefore, this component will provide two kinds of tools. The first one is an application-independent model management expert system for:

\- rule-guided combination of building blocks to solution strategies,

\- interactive introduction of preferences including the aggregation and negotiation of preferences in a group,

\- model changes by simplification, stochastication, use of heuristics and bound estimates (different levels of aggregation),

\- control strategies for the optimal use of cpu time by controlled competition of multiple parallel and communicating algorithms,

\- data access and scenario generation.

The second one is an object-oriented and extensible knowledge representation for the introduction of domain-dependent knowledge and inference/control strategies based on application expertise. These internal tools will be combined with related interface concepts such as explanation generation, 'debiased' acquisition of factual and preferential information and result display.

A large portion of the level 3 knowledge bases can be organized in the form of rules or using some suitable expert system shell. Note, however, that these rules or other forms of representation support (and make palatable to naive users), rather than replace, the use of mathematical techniques in model building and application. In fact, meta-knowledge concerning model building and the use of mathematical techniques is what is mainly represented and processed via rules in this context as a form of model based reasoning.

## 5. Conclusions

In this paper, we first argued for the central role of modelling in human intelligence, and – consequently – for the importance of modelling environments and management systems in decision support. In particular, we stressed:

\- the role of knowledge bases to maintain model information with complex structure;

\- the role of evolutionary processes as robust knowledge accumulation strategy;

\- the normative role of decision and probability theory together with a large body of mathematical results for dealing with preferences and uncertainty;

\- the need for exploiting scientific results from many disciplines in the form of 'deep models'.

Based on this analysis, the aim of this research is to strengthen the normative aspects of decision support systems by providing model management environments with the following capabilities:

\- support of the modelling process by specific data structures, language constructs, methodologies and tools;

\- normatively correct and robust methods for generating solutions:

\- exploitation of implicitly available information to reduce the information acquisition requirements on the user;

\- sensible allocation of available computational resources in a parallel-processing environment by defining and automatically adapting cost estimates of various methods;

\- assistance in explaining complex strategies and results to the user; and

\- a two-level DSS knowledge base that permits the easy addition of application-specific knowledge to a standard methodological kernel.

It is obvious that a full realization of such capabilities requires substantial progress in a number of areas, and in particular organizational forms that allow the integration of expertise in many diverse fields. Real progress in this field must therefore be viewed as a long-term basic research effort in which it is hoped that the close cooperation of methodological and application experts will overcome some of the above-mentioned barriers and lead to some badly needed conceptual foundations in the DSS field.

As we argued in chapters 2 and 3 of this paper, this will simultaneously mean a significant contribution to basic research aspects in artificial intelligence, particularly, as far as the cognitive competence of consistent decision making is concerned. In this respect but also from a general point of view, the paper stresses the basic importance of modelling and model management for any higher level of cognitive competence in systems.

## References

[1] Applegate, L.M., Konsynski, B.R., Nunamaker, J.F., Model Management Systems, Design for Decision Support, in: Decision Support Systems 2 (1986) 1, p. 81–91.

[2] Bartusch, M., Moehring, R.H., Radermacher, F.J., Design Aspects of an Advanced Model-oriented DSS for Scheduling Problems in Civil Engineering, to appear in DSS 1989.

[3] Baucilhon, F. (1988), Object-oriented database systems. in: ACM Symposium on Principles of Database Systems, New York; ACM Press, p. 152–162.

[4] Baucilhon, F., Kim, W., Korth, H.F., A Model of CAD Transactions, in: Proc. 11th VLDB Conf., Stockholm 1985, p. 25–33.

[5] Binbasioglu, M., Jarke, M., Domain-Specific DSS Tools for Knowledge-Based Model Building, Decision Support Systems 2, 3 (1986).

[6] Blanning, R.W., A Relational Framework for Model Bank Organization, Proc. IEEE Workshop on Languages for Automation, New Orleans 1984, p. 148–154.

[7] Bonczek, R.H., Holsapple, C.W., Whinston, A.B., Foundations of Decision Support Systems, Academic Press, New York 1981.

[8] Bonczek, R.H., Holsapple, C.W., Whinston, A.B., The Evaluation of MIS to DSS, Extension from Data Management to Model Management, in, Ginzberg, N., Reitman, W., Stohr, E.A. (eds.), Decision Support Systems, North Holland, 1987.

[9] Brennan, J.J., Elam, J., Understanding and Validating Results in Model-Based Decision Support Systems, Decision Support Systems (1986) 2, p. 49–54.

[10] Conklin, F. (1987), Hypertext, An Introduction and Survey, IEEE Computer 20, 9, p. 17–41.

[11] Dhar, V., PLANET - An Intelligent Decision Support System for the Formulation and Investigation of Formal

Planning Models; Ph.D. Thesis, University of Pittsburg 1984.

[12] Dolk, D.R., Konsysnki, B.R., Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering SE-10 (1984) 6, p. 609–628.

[13] Dreyfuss, H.L., Die Grenzen Künstlicher Intelligenz, Athenäum, Königstein 1985.

[14] Elam, J.J., Henderson, J.C., Miller, L.W., Model Management Systems, An Approach for Decision Support in Complex Organisations, Proc. First Intl. Conf. Information Systems 1980, p. 98–109.

[15] Felter, R., Conceptual Outline of a Decision Support Assistant (DSA), in: Proc. 12th SOR – Passau 1987, Athenäum, München, 1988.

[16] Fischhoff, B., Slovic, P., Lichtenstein, S., Knowing What You Want: Measuring Labile Values, in: Wallstein, T. (ed.), Cognitive Processes in Choice and Decision Behaviour, Erlbaum, Hillsdales, N.J., 1980.

[17] Fishburn, P.C., Utility Theory for Decision Making, Wiley, New York, 1977.

[18] Fogel, L.J., Owens, A.J., Walsh, M.J., Artificial Intelligence through simulated evolution, John Wiley, New York, 1966.

[19] Gardarin, G., Pucheral, P., Thevenin, J.M., Overall Architecture of the GEODE Extensible DBMS Kernel, in: Proc. of the 5th Annual ESPRIT Conference, North Holland, Amsterdam, 1988, p. 863–876.

[20] Garey, H.R., Johnson, D.S., Computers and Intractability, A Guide to the Theory of NP-completeness, Freeman, San Francisco, 1979.

[21] Geoffrion, A., The Purpose of Mathematical Programming is Insight, Interfaces (1976) 7.

[22] Geoffrion, A., Structured Modelling, UCLA Graduate School of Management, Los Angeles 1988.

[23] Glover, F., Tabu Search, CAAI Report 88-3, Center for Applied Artificial Intelligence, University of Colorado, Boulder, 1988.

[24] Grefenstette, J.J. (ed), Proc. Intern. Conf. on Genetic Algorithms and their Application, The Robotics Institute, Carnegie-Mellon University, 1985.

[25] Hersey, P., Kunreuther, H., Schoemaker, P.J., Bias in Assessment Procedures for Utility Functions, Management Science (1982) 28, p. 936–954.

[26] Hofstadter, D.R., Gödel, Escher, Bach, Klett-Cotta, Stuttgart 1985.

[27] Hofstadter, D.R., Dennett, D.C., The mind's I. Bantam Books, London 1982.

[28] Hogarth, R.M. (ed.), Question Framing and Response Choice, Jossey-Bass Inc., San Francisco 1982.

[29] Holsapple, C., Whinston, A.B., Building Business Expert Systems with GURU, Addison-Wesley, 1987.

[30] Humphreys, P.C. et al., A brief description of MAUD, Technical Report, Decision analysis unit, London School of economics and political sciences (1986).

[31] Jacquet-Lagréze, E., Siskas, J., Assessing a Set of Additive Utility Functions for Multicriteria Decision Making, The UTA Method, Europ. Journal of Operations Research 10 (1982), p. 151–164.

[32] Jarke, M., Group Decision Support Through Office Systems, Developments in Distributed DSS Technology, in: McLean, E., Sol, H.G., Decision Support Systems, A Decade in Perspective, North Holland, Amsterdam 1986.

[33] Jarke, M., Jelassi, M.T., Shakun, M.F., MEDIATOR, Towards a Negotiation Support System, In: Europ. Journal of Operations Research 31 (1987), p. 314–334.

[34] Jarke, M., Radermacher, F.J., Model Management for Decision Support, A Proposal, Preprint, Universitaet Passau 1986.

[35] Jarke, M., DAIDA Team (1988), The DAIDA Environment for Knowledge-based Information Systems Development. In: Proc. of the 5th Annual ESPRIT Conference, North Holland, Amsterdam, 1988.

[36] Jereslov, R.G. (ed), Approaches to Intelligent Decision Support, Annals of OR 12 (1988).

[37] Kahnemann, D., Slovic, P., Tversky, A. (ed.), Judgement Under Uncertainty, Heuristics and Biases, Cambridge University Press, 1982.

[38] Keeney, R.L., Siting Energy Facilities, Academic Press, New York, 1980.

[39] Keeney, R.L., Raiffa, H., Decisions with Multiple Objectives, John Wiley, New York, 1976.

[40] Keeney, R.L., Moehring, R.H., Otway, H., Radermacher, F.J., Richter, M.M., Multi-Attribute Decision-Making via O.R.-Based Expert Systems. Special Issue of Annals of Operations Research 1988.

[41] Klein-Haneveld, W.K., Robustness Against Dependence in PERT, An Application of Duality and Distributions of Known Marginals, in: Mathematical Programming Studies (1986) 27, p. 153–182.

[42] Klein-Haneveld, W.K., Duality in Stochastic Linear and Dynamic Programming, Springer Lecture Notes in Economics and Mathematical Systems, Heidelberg (1986) p. 274.

[43] Kuhn, T.S. (1970), The Structure of Scientific Revolutions. Chicago University Press, 2 edn.

[44] Lawler, E.L., Lenstra, J.K., Rinnooy Kan, A.H.G., Recent Developments in Deterministic Sequencing and Scheduling, A Survey, in: Dempster M.A.H. et al. (ed.), Deterministic and Stochastic Scheduling, Reidel, Dordrecht, 1982.

[45] Lenat, D.B., On Automated Scientific Theory Foundation, A Case Study Using the AM Program, in: Hayes, J.E., Michie, D., Mikulich, L.I. (eds), Machine and Intelligence 9, Halsted Press, New York, 1977.

[46] Lenat, D.B., Guha, R.V., The World According to CYC, MCC Technical Report No. ACA-AI-300-88, 1988.

[47] McLean, E., Sol, H.G., Decision Support Systems, A Decade in Perspective, North Holland, Amsterdam, 1986.

[48] Meador, C.L., Guyote, M.J., Rosenfeld, W.L., Decision Support Planning and Analysis, The Problem of Getting Large-Scale DSS Started, MIS Quarterly 10 (1986) 2, p. 159–177.

[49] Meilijson, I., Nadas, A., Convex Majorization with an Application to the Length of Critical Paths, in: J. Appl. Prob. (1979) 16, p. 671–677.

[50] Moehring, R.H., Radermacher, F.J., Substitution Decomposition of Discrete Structures and Connections with Combinatorial Optimization, in: Ann. Discrete Math. (1984) 19, p. 257–356.

[51] Moehring, R.H., Radermacher, F.J., Introduction to Stochastic Scheduling Problems, in: Neumann, K., Pallaschke, D. (eds.): Contributions to Operations Research, Springer Verlag (1985), p. 72–130.

[52] Moehring, R.H., Radermacher, F.J., Weiss, G., Stochastic

Scheduling Problems I, General Strategies, in: ZOR (1984) 28, p. 193–260.

[53] Moehring, R.H., Radermacher, F.J., Weiss, G., Stochastic Scheduling Problems II, Set Strategies, in: ZOR (1985) 19, p. 65–104.

[54] Moskowitz, S., Sarin, M.L., Improving the Consistency of Conditional Probability Assessments for Forecasting and Decision-Making, Management Science (1983) 29, p. 735–749.

[55] Mostow, J. (1985), Towards better models of the design process, AI Magazine 6, 1, p. 44–57.

[56] Murphy, F.H., Stohr, E.A., An Intelligent System for Formulating Linear Programs, Decision Support Systems (1986) 2, p. 39–48.

[57] Popper, K.R., Objektive Erkenntnis. Ein evolutionärer Entwurf, Hoffmann & Campe, Hamburg, 1974.

[58] Radermacher, F.J., Entwicklungsperspektiven rechnergestützter Entscheidungsfindung, in: Wolff, J. (ed.), Proceedings des IBM-Symposiums 'Entscheidungsunterstützende Systeme', Oldenbourg Verlag, München, 1988.

[59] Radermacher, F.J., Ritter, G., Ross, S.M., Stochastic Dynamic Optimization and Connections with Scheduling and Related Areas, Conference Report, University of Passau 1985.

[60] Rechenberg, I., Evolutionsstrategie, frommann-holzboog, Stuttgart, 1973.

[61] Rinnocy Kan, A.H.G., Machine Scheduling Problems, Classification, Complexity and Computations, Nijhoff, The Hague 1976.

[62] Scheck, H.J., Paul, H.B., Scholl, M.H. Weikum, G., Deppisch, U., Architecture and Implementation of the Darmstadt Database Kernel System, in: Proc. of the 14th ACM SIGMOD annual conference, 1987, p. 196–207.

[63] Schmidt, J.W., Database Programming, Language Constructs and Execution Models, in: Ammann, U. (ed.), Programmiersprachen und Programmentwicklung, Springer-Verlag 1984, p. 1–25.

[64] Schuett, K.P., Wahrscheinlichkeitsabschaetzungen im Computer-Dialog, Poeschel-Verlag, Stuttgart, 1981.

[65] Schwefel, H.P., Numerische Optimierung von Computermodellen mittels der Evolutionsstrategie, Birkhäuser, Basel/Stuttgart, 1987.

[66] Shafer, G., A Mathematical Theory of Evidence, Princeton University Press, Princeton, 1976.

[67] Shogan, A.W., Bounding Distributions for Stochastic PERT Networks, Networks 7 (1977), p. 359–381.

[68] Simon, H.A., The Sciences of the Artificial, MIT Press, Cambridge, 1981 (2nd ed.).

[69] Sivasankaran, T.R., Jarke, M., Logic-Based Formula Management Strategies in Actuarial Consulting Systems, Decision Support Systems 1 (1985) 3, p. 251–262.

[70] Sprague, R.H., Carlson, E.D., Building Effective Decision Support Systems, Prentice Hall, Englewood Cliffs, N.J., 1982.

[71] Stoyan, D., Comparison Methods for Queues and Other Stochastic Models, John Wiley, Chichester 1983.

[72] Turban, E., Watkins, P.R., Integrating Expert Systems and Decision Support Systems, MIS Quarterly 10 (1986) 2, p. 121–136.

[73] von Neumann, J., Morgenstern, O., Theory of Games and Economic Behaviour, University Press, Princeton, 1963.

[74] von Stengel, B., Decomposition of Multi-Attribute Expected Utility Functions, in: Keeney, R.L., Moehring, R.H., Otway, H., Radermacher, F.J., Richter, M. (eds), Multi-Attribute Decision-Making via O.R.-Based Expert Systems, Special Issue of Annals of Operations Research 1988.

[75] Weber, M., Entscheidung bei Mehrfachzielen und unvollständiger Information, ZfbF (1985) 35, p. 311–331.

[76] Winograd, T., Flores, F., Understanding Computers and Cognition, A New Foundation for Design, Ablex Publ. Co., Norwood, N.J., 1986.
