---
otero_id: 17611
otero_key: "YQHCEZFV"
title: "A cognitivist model for decision support: COGITA project, a problem formulation assistant"
authors: "Bernard Espinasse"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90046-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A cognitivist model for decision support: COGITA project, a problem formulation assistant

Bernard Espinasse

Université Aix-Marseille III, Aix-en-Provence, France

The formulation of a problem may be defined as a process of acquisition and organization of knowledge related to a given situation, on which a decision maker projects some action. The assistance in the problem formulation that we may expect within decision support systems is difficult to design and to implement. This is mainly due to the frequent lack of attention to a sufficiently formalized conceptual framework which would consider the decision with a more cognition sciences oriented approach. In the first part, we will present an instrumental model for the study of decision processes as an attempt to simulate the cognitive process of knowledge acquisition and organization carried out by a decision maker facing a problematic situation. Considering its epistemological foundations, this model can be named “cognitivist model”. Within this model, the decision is defined as a cognitive construction which we call “decisional construct”. It consists of the elaboration of one or several abstract representations of the problematic situation (formulation phase), and the design of operational models (solving phase). In the second part, we will present the COGITA project, which consists of the design and realization of an environment for the development of problem formulation assistance systems. The modelization and simulation of cognitive processes call for relevant techniques originating either in artificial intelligence or in connectionism. We will show which are the main characteristics, potentials, limits and complementarity of these techniques and why their integration is fundamental and necessary to the simulation of the cognitive process associated with the formulation. COGITA is a hybrid system currently under development which tends to integrate symbolic artificial intelligence techniques and connectionist models in a cooperative hybridization the general architecture of which is presented.

Keywords: Problem formulation; Problem resolution; Decision support systems; Decision process; Artificial intelligence; Connectionism; Cognitive process

## 1. Introduction

The assistance in problem identification and formulation that we may expect within Decision Support Systems [21], [10] is difficult to design and to implement. This is mainly due to the absence of a sufficiently formalized conceptual framework which would approach the decision process with a more cognition sciences oriented approach.

In fact, the traditional paradigms for the study of decision processes are principally based on rationality in any form [9]. They do not permit an approach to the decision process as a cognitive process of knowledge acquisition and organization.

An original alternative to rationality proposed by P. Huard [20], seems to be very interesting and capable of building a new, more “cognitive” paradigm of decision. This alternative can be resumed by the following new postulates:

\- Opposed to the explicit, voluntary and positive

![](/api/attachments/YQHCEZFV/fulltext/images/ed8c7be797e3cad3c9267a688b19774db3d5c6820267dfdae3a7ad8b1570e513.jpg)

Bernard Espinasse received a Doctorate in Information Systems from Aix-Marseille III University (France), after an Engineering diploma from the Ecole Nationale Supérieure d'Arts et Metiers (Paris) and a Business Management Certificate (IAE Aix-en-Provence). As an Associate Professor, he has taught Information Systems Engineering at MBA level at Laval University (Québec, Canada) for three years. Currently, Bernard Espinasse is an Assistant Professor of

Information Systems at Aix-Marseille III University and researcher at GRASCE/CNRS laboratory. He also is the Scientific Director of Systemia Institute (Aix-en-Provence) which is specialized in Information Systems Education for Post-Graduates. Dr. Espinasse is co-author of a book about Information Systems Engineering and has published various conference articles in the areas of Decision Support Systems, Artificial Intelligence, Information Systems Design and Database.

character of a decision, are largely unconscious automatisms.

\- Progress, the justification and orientation of rationality, can be replaced by a unification movement, searching for coherence of the existing situation (coherence principle).

These hypothesis lead more particularly to the possibility of replacing the perfectly discriminant rationality procedures with procedures of imitation, repetition of experiences already lived, of assimilation of the new to the old (mimetic behaviour). These procedures are more apt for a cognitive approach to the decision process. In fact, the coherence principle should be seen as closely linked to the equilibration process in J. Piaget's intelligence organization model. Within this model, the intellectual adaptation is a permanent equilibration between an assimilating mechanism and a complementary accommodation of knowledge structures; the individual tends to establish an equilibrium of the relations between its different cognitive elements. This equilibrium assures a coherence with the retained knowledge. This principle results in a certain resistance against any important restructuration of cognitive elements. Applied to the study of decision processes, it leads the decision maker to search for a simplification (of the complexity of the problematic situation he is facing) different from the one postulated by the rationalist models. Thus, the decision maker will tend to:

\- perceive independent problems,

\- in the case of uncertainty impose a clear signifi-cation to the events, a global explanation, rather than making probability calculations,

\- formulate and resolve the problem with the help of beliefs, procedures and solutions he already owes, taking into account their age and their frequency of utilization.

In order to preserve this coherence, certain processes of learning and reinforcement are applied. For instance, the reinforcement of the beliefs will be facilitated by associating with them acquired images and analogies drawn from previous situations. In the case of new informations which contradicts the existing cognitive organization, the decision maker will be able to either affirm that, in fact, within a larger time scale, the coherence is maintained (case of exception), or to reject other choices he considers impossible or having catastrophic consequences.

## 2. A cognitivist model for the study of decision processes

The cognitive decision paradigm mentioned in the introduction, Piaget's work on the formation of human intelligence and Simon's work on the management decision, lead us to proposing a model for the study of decision processes as cognitive processes of knowledge acquisition and organization. Given its Piagetian and Simonian epistemologic foundations, we have qualified this model as "cognitivist".

## 2.1. The decision construct

In the comprehension of decision processes, various scientifics have been inspired by J. Piaget's work on intelligence organization [7], [8], [32]. The genetic perspective of constructivism developed by J. Piaget stresses the interaction between the organization and its operation, or between the structure and its structuration (genetic perspective or constructivism): no more genesis without structure nor structure without genesis. This genetic perspective leads to the progressive construction of knowledge [31]. This is also the constructivist, dialectic interaction between the subject and the object: "...to consider knowledge as linked to an action (by the subject) modifying the object and reaching it only through the transformation introduced by this action...". [translation by the author, Piaget [30], page 1244].

In this model, the decision is defined as a cognitive construction which we will call “decision construct” and which precedes any “decision act”. This decision construct (see Figure 1), a cognitive process of the decision maker, consists first of all of the elaboration of one or more abstract representations of the problematic situation which will be assimilated to a problem formulation phase, followed by the conception of operational models permitting the generation of solutions, which will be assimilated to a problem solving phase.

![](/api/attachments/YQHCEZFV/fulltext/images/0ade913af4b600d4f15e3ba5b788c95998244e1fed3d42a53d83485b0644a666.jpg)  
Fig. 1. The decision construct

## 2.2. The problem formulation phase: Elaboration of abstract representations

In his study of intelligence formation with the human being, J. Piaget [29] has emphasized a process of equilibration of the representations formed by the human being (which he calls schemes). During this equilibration process, newly observed events or consequences of actions are either assimilated in the representation, or lead to an accommodation of the representation, e.g. an adjustment of the latter, permitting to take into account the novelty.

In the comprehension of decision processes, the formulation phase will be assimilated to a process of elaboration of abstract representations of the problematic situation. After observation and perception of the problematic situation, the decision maker will try to understand it. This comprehension is established by the progressive elaboration of an abstract representation of the situation, until its stabilization is achieved (equilibration process). This equilibration is based on two adaptation mechanisms: the assimilation where the observation of the problematic situation leads to a reinforcement of the representation, and the accomodation where the observation leads to a profound modification of the representation. The abstract representations of a problematic situation which the decision maker elaborates can thus:

\- become more precise: fine-tuning of the representation taking into account more details (precision process),

![](/api/attachments/YQHCEZFV/fulltext/images/7ff1639f2625372ef56cacaece7ef9b4c6671102208a70a996939fa6683c0965.jpg)  
Fig. 2. Transformations on abstract representations

\- become more general: in order to incorporate these new facts, the representation is rebuilt without any profound perturbation (accommodation of the representation, generalization process),

\- become more complex: the representation is rebuilt and profound modifications are possible, for example new facts, new variables, new relations (complexification process, as already proposed by J.C. Courbon [7]). This process can be associated to Piaget's “mechanism of reflective abstraction”,

\- stabilize: a stable representation is reached (closure of the formulation, stabilization).

This can be represented in Figure 2 (inspired by J.C. Courbon).

When the comprehension of the problematic situation has become stable (coherence principle), the formulation is closed and leads to a statement of the problem (closure of the formulation).

However, the formulation of very badly structured problems is done according to rules which cannot immediately be formulated in logicomathematic terms. This formulation frequently takes place on the argument level [37]. In this case it is difficult to use the experimental proof or the formal logic to demonstrate and argue facts, deliberations, discussions and organizational decisions [G. Busino in [18]]. Research work on the “natural logics” [18] for the understanding of speeches are an attempt to formalize this argument [6].

## 2.3. The problem solving phase: Design of operational models

The formalization being closed, an operational model will have to be constructed from the statement of the problem which will permit to deduct, to envisage possible solutions to the problem. We will assimilate this construction of operational models to a problem solving phase (similar to H.A. Simon's conception phase).

This conception of operational models may be associated to the development of logico-mathematic structures defined by J. Piaget. We recall that a logico-mathematic structure (LMS) is a knowledge and may be an instrument of knowledge, permitting the elaboration of new knowledges of logicomathematic or empiric type. The LMS may be simple, for example a simple cause/ effect model, several rules of the IF...THEN... type, or they may be complexe, for example an elaborated theory [5].

![](/api/attachments/YQHCEZFV/fulltext/images/ed6c7ad84c7953dcd1454b7a55af43f010e9bbbee97d6415e0c4c205bcb61454.jpg)  
Fig. 3. From formulation to resolution

The development of logico-mathematic structures or models is carried out with the help of other LMS and also through the interaction between the model, which the decision maker is in the process of elaborating and the comprehension of the problematic situation he has built via an abstract representation. The deductions from the model are thus confronted with the abstract representation: this can be called application of the model. In the case of a conflict (incoherence, dissonance) between the deductions of the model and the representation of the phenomenon or the situation, the formulation phase is re-activated in order to modify the representation. New LMS may be used which permit the acquisition of new knowledge regarding the representation and its enlargement by either reinforcement, precision, generalization or complexification. (See Figure 3).

As the model is being designed, the abstract representation gets richer and more and more complete and thus leads to either a destructuration of the associated models, or, if the representations reinforce and affine themselves, to a structuration of the associated models. We observe a dynamic process of structuration/restructuration of models, an adjustment necessary for a good comprehension of the problematic situation. This cycle is repeated several times and makes the model more and more “abstract” from the observed situation. When the abstract representation is in perfect agreement with the deductions of the model, then the model is attributed to the situation, process which may be called attribution of the model.

## 3. COGITA project: An assistant in problem formulation

The role of a decision maker is not restricted to making a choice, but consists of observing and constructing a certain comprehension of a phenomenon, a situation, an environment [11]. Thus, a support in the identification, formulation and structuration of a problematic situation is fundamental. If a correct formulation has been carried out, then the solution frequently turns out trivial. The COGITA project consists of the conception and realization of an environment for the development of problem formulation support systems. Before describing this environment under development, it is necessary to precise what we understand by problem formulation support.

## 3.1. Problem formulation support

The instrumental model that we have previously proposed, helps to distinguish various levels of assistance to the formulation of a problem. We will define them in the order of their growing complexity and indicate how they are or may be treated.

Assistance in the formulation of a formal statement: In this area, artificial intelligence already gives a certain number of solutions [5] with the help of very high level languages permitting the formulation of statements in a declarative manner. We find “problem solvers” allowing to specify and re-specify a statement in a specific language, accepting multiple possible variants of this statement. Examples are the systems ALICE [22], PROMAT [4], conceived for declaring statements of operational research problems. Object oriented languages are also very useful for specifying and re-specifying a statement [12][13].

Passage from the statement to a resolution model: The formal statement being set (closure of the formulation phase), a resolution model has to be defined. In certain problem solvers (ALICE, PROMAT,...), the elaboration of a resolution model from a formal statement is automatic. Depending on the deductions of this model (model application), a new formulation of the statement may be necessary. The to and fro movement between formulation and solution continues until a fixed point is achieved (model attribution), which is a mark of a “satisficing” [35]. At any moment, the initiative of a reformulation stays with the user; and the to and fro movement may very well amplify the human reasoning. Many stock management, production or distribution problems can be treated in this way.

Assistance in the elaboration of abstract representations: This kind of assistance is the most delicate concerning its design and realization. However, it is vital in the case of very badly structured problems. Practically no appropriate tool exists. One may imagine systems allowing to elaborate abstract representations which dispose of a certain number of transformation operators working in a quasi-automatic manner until the achievement of a certain coherence, a stability, a balance. These transformation operators should be capable of constructing and organizing new knowledge about the problem, but maybe also a certain knowledge about the decision maker's behaviour.

## 3.2. Symbolic and associative character of cognitive processes in formulation

The formulation of a problem can be defined as a set of cognitive processes in which the decision maker acquires and organizes a certain knowledge. An assistance in the formulation requires a better comprehension of the employed cognitive processes. Human cognition seems to present a double working mode: the associative mode and the symbolic mode. The associative mode characterizes associative and global treatments directly associated with given perceptive data or mental states. These associative treatments interface via the process of control or concurrence with logic treatments which constitute the logic or symbolic mode. Our symbolic cognitive processes are thus rooted in the perceptive and are in constant interaction with it.

In a general way, responding to a complex question, establishing a diagnosis or analyzing a situation in order to come to conclusions, provokes cognitive action either on the associative level (perceptive, intuitive), or on the symbolic level (logic, reasoning):

The symbolic level is the level privileged by verbalization, explicitation, explanation. It is associated with symbolic representations and treatments, the principal areas in which artificial intelligence has worked. In artificial intelligence, a cognitive process is modelized by a manipulation of symbolical representations structured according to a certain number of formal rules.

The associative level is not necessarily associated to the symbolical representation. A cognitive process of association will rather be associated to the adaptation of a system of representations by accumulation of associations. The association of an interpretation to a situation (formulation) or a solution to a problem (resolution), may be perceived as the result of an equilibration mechanism between knowledge, and cognitive structures which the decision maker disposes of. This equilibration mechanism is a process of constraints satisfaction. An association is not necessarily the result of a logical reasoning, but may be seen as a macro-correlation resulting from a microcorrelation between and within related patterns of representation (equilibration, propagation of multiple constraints) [1]. At least part of these cognitive processes can be modelized with the help of connectionist networks.

The associative level very frequently precedes the symbolic level. The associative level will be prevalent in the formulation phase whereas the symbolic level will be prevalent in the resolution phase. An illustration of this may be the mathematician who finds a theorem and then constructs an elegant proof later on: the formulation takes place on the intuitive, associative level and the resolution on the symbolical, logical level.

## 3.3. Simulation of cognitive processes in formulation

The modelization of cognitive processes requires relevant artificial intelligence or connectionism techniques. Based on D. Memmi's excellent study [25] [26], we shall see which are the main characteristics, potentials and limits of these techniques.

## 3.3.1. Artificial intelligence and cognitive processes

We will look at representations used in artificial intelligence and at their possible treatments. These representations proposed by artificial intelligence are called symbolic due to the fact that they have a meaning, but not because there may be a resemblance between a symbol and its signification. They are characterized by a great clearness. The concepts, the formalisms they utilize, are in fact very close to the natural language (for example the notion of frame), which also leads to relatively easily understandable explanations. Another fundamental characteristic of these symbolic representations is their declarativity. It makes the representations seem to possede a signification for the human spectator which is independent of their usage by the system. This may be dangerous: the psychological signification may be completely different from the representation's signification within the system. Finally, these symbolic representations are described in a quasi-verbal description mode in any possible application area: in the areas of reasoning as for example problem solving (areas where conscious processes may be more or less verbalized), as well as in areas like perception or natural language where mental processes are largely inconscious and very hard to verbalize.

Artificial intelligence carries out a purely formal treatment of the representations. The signification of symbolical expressions is not required for their treatment by the system whereas it is intuitively evident for the human user. The treatment may be largely reduced to formal systems of mathematic logic with its purely syntactic derivation. It is thus possible to realize a manipulation of symbols in terms of mechanisms permitting an computerized simulation. Unfortunately, this is carried out under complete separation of syntaxis and semantics and exclusion of any signification of the process $[25]$ . The structured symbolic representations are then manipulated by processes adapted to these structures (sensitive structures). Artificial Intelligence structures are explicit and manipulated as structures (Pattern Matching). Structures are not only a way of constructing complex expressions, but they also play an important causal role in the very treatment of their representations. This treatment is mainly sequential. In the treatment of knowledge in symbolic artificial intelligence, the parallelism is difficult to implement and often little productive for procedures which are not originally designed for. Finally, the control of the treatment is principally extern and centralized. It can be formalized in an explicit and declarative way, for instance by the usage of meta-knowledge (meta-rules) allowing for the system to reason about the way it operates.

These principal characteristics of artificial intelligence are already widely used for the simulation of cognitive processes of a symbolic nature. A great number of realizations in terms of expert systems, problem solving systems, are the proof. But artificial intelligence has its limits, principally related to its hypothesis that cognitive processes can be reduced to a clear formal language close to the natural language in terms of semantic contents. This hypothesis partially explains the lack of importance granted to learning: the way representations may have been learned is not relevant enough for being added to their contents, structure and usage. Learning in artificial intelligence is often reduced to a recombination of existing symbols. For Memmi, this conception of cognition is a modern form of rationalism, a clear conception but too good to be true [26].

## 3.3.2. Connectionism and cognitive processes

Both connectionism and artificial intelligence can be generally defined as a cognitive computer simulation, each related to a particular conception of human cognition. They issue from the same bases: the computation theory, computer sciences, cybernetics and cognitive simulation $[16]$ . They have progressively differed from each other and finally become competitors. After several precocious successes (the perceptron), the research on neuro-mimetic networks has declined facing conceptual as well as technical difficulties. At the same time, research in the symbolic direction has prospered and led to the success of expert systems. However, during the last years, an important amount of research work has been done $[33]$ , sometimes leading to spectacular realizations, and giving a new vitality to a stream called connectionism (or neo-connectionism). Connectionism seems to emerge as a new autonomous area of research.

Connectionism uses representations which differ from the ones used in artificial intelligence by their principally distributed nature. These distributed representations are more flexible given the repartition of the descriptions on numerous cells representing descriptive micro-features (via activation states, connection valuations). The number of possible representations becomes important. Connectionism thus permits to represent and recognize approximative descriptions, which is difficult in artificial intelligence. Another fundamental characteristic of connectionism is the importance it gives to learning. A great number of distributed models use a learning procedure to adjust their connection weights in order to acquire regularities. Connectionism thus considers that learning is pertinent to explain the structure of representations. Connectionist treatments on representations are mainly of a parallel nature, even if the simulation is carried out with a central, non-parallel processor. Even if the network's cells are sequentially updated, each cell's activity depends on the whole of its neighbour cells. The treatment is thus spread over a number of cells, partially in a redundant way and the network wins in flexibility and robustness.

These main characteristics of connectionism are promising for the simulation of cognitive processes of a more associative nature. In fact, connectionism offers a new type of representation, interesting treatment types, and the possibility to effectively take into account learning mechanisms. But the limits of connectionist techniques lie within the difficulties of managing the treatments (the parallelism, the sequential, …), and in interpretation and exploitation of explicit structures by the distributed representations. The conception of cognition proposed by connectionism is of a certain interest but can in no case be self-sufficient.

## 3.4. General architecture of COGITA; A symbolico-connectionist hybridation

Artificial intelligence offers interesting perspectives in problem formulation support concerning both the formulation of a formal statement and the derivation of an operational model from the latter, as well as in the elaboration and the application of heuristics and resolution strategies. Connectionism should find its main interest in formulation support, and more particularly in the elaboration of abstract representations (not necessarily of a symbolic nature), leading to a formal statement. The elaboration of these representations takes frequently place in the “sub-cognitive”, located below 100 micro-seconds and concerns the link between perception and cognition.

Artificial intelligence techniques aver to be limited concerning modelization and simulation of cognitive processes of a more associative nature (perception, learning). Likewise, connectionist techniques are limited in that which concerns the realization of cognitive tasks demanding at the same time for capacities of “low-level” perception and capacities of “high-level” symbolic reasoning. But the treatment of many problems requires the combined usage of these two resolution modes, the symbolic and the associative. Let's cite the following problems:

\- Plannification problems: when it is necessary to perceive the strategies of other agents before elaborating reasonably and intelligently a response strategy (neutralization, reinforcement,...)

\- Control and test of the process: when it is necessary to link control expert systems with perception or form recognition systems.

The development of artificial systems for the resolution of such problems leads to design systems called “hybrid”. In order to wisely combine the advantages of both approaches, these systems using on the one hand connectionist modules (neural networks techniques) in order to treat “associative” tasks which require flexibility and progressive adjustment, and, on the other hand, symbolic modules (artificial intelligence techniques) for “symbolic” tasks leading to logic reasons.

We can distinguish three major possible types of hybridations depending on their principal objective. An objective for a hybridation may be to enrich an associative process using connectionist models, by using symbolic techniques (connectionist hybridation), as presented in [15]. Another objective may be to enrich a symbolic process using artificial intelligence techniques using connectionist models (symbolic hybridation), as proposed in [14]. A last objective would be to assure a complete cooperation between symbolic and associative processes (cooperative hybridation), as developed by J. Hendler in [19]. The latter objective is the one retained for the COGITA project.

The cooperative hybridation retained for COGITA consists of a strong linkage between symbolic and connectionist modules in order to assure their cooperation in the realization of a common task. As a first application of this hybridation we have fixed the recognition of perception similarities. Neural networks will allow to develop, by learning from a data base of examples, internal representations roughly corresponding to a set of “micro-features”, not identifiable by a symbolic treatment, which can be used for the determination of similarities of a set of entries, then used for a symbolic module. The gen-

![](/api/attachments/YQHCEZFV/fulltext/images/af0562aeba4a406ff25c65e060eba162dfb96a9e21c68527636dcfc4f38049bb.jpg)  
1 - The environment delivers a set of observable facts out of which the connectionist module extracts classifications and correlations.

2 - The connectionist module transmits the correlations and sequences modifying the symbolic representations or treatments to the symbolic module.

3 - The symbolic module influences the connectionist module in matters of, for example, the architecture of the neural network, the learning control, the mechanisms of correlations reinforcement, ...

4 - The environment delivers to the symbolic module a set of observable facts on which a logic reasoning will be based.

Fig. 4. General architecture of COGITA

eral architecture of COGITA is as follows (see Figure 4);

Connectionist module The objective of this module is to allow the elaboration and the manipulation of distributed representations which cause the emergence of micro-features within the neural networks. This module consists of various connectionist models. As a first step, we will exclusively treat multilayer learning networks by back-propagation [33]. Inputs for such a network are coded from a set of observable facts of the environment (1). The aim is to constitute classifiers on coded inputs. Outputs of the network are linked to interface nodes of the symbolic module's semantic network.

Symbolic module The objective of this module is to permit the elaboration and the manipulation of symbolic representation through a semantic network. This module is carried out in Snarx, a language of representation and interpretation of knowledge [17]. The representation of knowledge is of the semantic networks type (triples: object, relation, value), the interpretation is presently done using production rules with variables, used in forward chaining and disposing among others of primitive actions specific to creation, control and exploitation of the connectionist's neural networks.

![](/api/attachments/YQHCEZFV/fulltext/images/d0ab7e89f057507ac018933060fb4b2d25dc65ddd6941dfeacb0e828a65d5cfc.jpg)  
Fig. 5. Dynamic of cooperative hybridation

Dynamic of the hybridation In this hybridation we have a cooperation in order to realize a common task at two different levels; the semantic network at a symbolic level of explanation, and the connectionis network at an associative level of perception. The operation of this hybridation is inspired by the one proposed by Hendler [19] using the algorithm of “marker-passing”. COGITA’s first objective will be to fill a lack of information on the symbolic level by a propagation of activity from the semantic network to the connectionist network and vice-versa. (See Figure 5).

As a first step, by learning the weights of the network connections based on a set of observable facts of the environment (1), the network constructs a distributed representation from which emerge micro-features. The weights leading to the output cells of the neural network can be used for the realization of a similarity based reasoning. These micro-features are taken into account at the interface nodes of the symbolic module's semantic network (2) and propagated within it (symbolic activation, energy delivered by the connectionist network to the semantic network). Referring to the model presented in part 2, this corresponds to a transfer from an abstract representation to an operational model.

As a second step, facts of the environment observed on the symbolic level (4) or inferences carried out in the symbolic module's semantic network, will deliver through the interface nodes of the semantic network, an activation energy (numeric activation) to the connectionist network (3). The symbolic concepts, now more closely linked to each other by inferences, increase the energy of the connectionist network's specific cells. These cells can propage more adapted micro-features to the semantic network by symbolic activation. Referring to the model presented in part 2, this corresponds to an interaction of an operational model towards an abstract representation.

## 4. Conclusion

To abord the assistance of Decision Support Systems in problem identification and formulation, we have proposed a conceptual model for the study of decision processes as cognitive processes of acquisition and organization of knowledge. In this model, Artificial Intelligence offers interesting perspectives in problem formulation support concerning both the formulation of a formal statement and the derivation of an operational model from this statement, as well as in the elaboration and the application of heuristics and resolution strategies. The main interest of Connectionism within this model lies in a formulation support more particularly concerning the elaboration of abstract representations, not necessarily of a symbolic nature, leading to a formal statement. The elaboration of these representations is more related to the “sub-cognitive”, located below 100 micro-seconds, and concerns the link between perception and cognition. COGITA, a project currently under development, proposes a new way of conception and implementation of formulation support systems based on a cooperative symbolico-connectionist hybridation. This hybridation permits the performance of tasks on two different levels: a symbolic level of explanation (with a semantic network), and an associative level of perception (with a connectionist network).

## References

[1] Amy, B., Giacometti, A. and Gut. A. (1990), Modèles connexionnistes de l'expertise, Proc. Neuro-Nimes 90, Pub. EC2, Paris.

[2] Bochereau, L. and Bourgine, P. (1989), Implementation et extraction de traits sémantiques sur un réseau neuromimétique: exemple de la première annonce au bridge, Proc. Neuro-Nimes 89, Publication EC2, Paris.

[3] Borel, M.J., Grize, J.B. and Mieville, D. (1983), Essai de logique naturelle, Peter Lang, Berne, Francfort, New York.

[4] Bourgine, P. (1989), Le langage PROMAT et sa machine virtuelle, Proc. 7 $^{0}$ Congrès Reconnaissance de Formes et Intelligence Artificielle, Publication AFCET, pp. 1011.

[5] Bourgine, P. and Espinasse, B. (1987), Aide à la décision: une approche constructiviste, in Aide à la décision dans l'organisation, publication AFCET, 1987, pp. 47–55.

[6] Borillo, M. et All, (1982), Approches formelles de la sémantique naturelle, Laboratoire de Langages et Systèmes Informatiques, Toulouse, C.N.R.S.

[7] Courbon, J.C. (1984), Transparency of Data Information and Models in Decision Support Systems. Proc. IFORS, Washington.

[8] Courbon, J.C. (1982), Processus de décision et aide à la décision, in Economies et Sociétés, Séries Sciences de gestion, n°3, tome XVI, n°12.

[9] De Bruye, P. (1981), Modèles de décision; les rationalités de l'action, Centre d'Etudes Praxéologiques, Louvain-la-Neuve.

[10] Espinasse, B. and Pascot, D. (1987), Decision Support Systems: A Knowledge Oriented Approach in Economics and Artificial intelligence, Pergamon Press.

[11] Feldman, M.S. and March, J.G. (1981), Information in Organization as Signal and Symbol, Administrative Science Quarterly, n°26, pp. 171–186.

[12] Fox, M.S. (1983), ISIS: A Constraint-Directed Reasoning Approach to Job Shop Scheduling, Proceeding of IEEE Conference on Trends and Applications 83, National Bureau of Standards, Gaithersburg, Maryland.

[13] Fox, M.S. (1985), Knowledge Representation for Decision Support Systems, in Knowledge Representation for Decision Support Systems, edited by L.B. Methlie and R.M. Sprague, North Holland.

[14] Giambiasi, N., Lbath, R. and Touzet, C. (1989), Une approche connexionniste pour l'implication floue, Proc. Neuro-Nimes 90, Pub. EC2, Paris, pp 143–158.

[15] Gallant, S.I. (1988), Connectionist Expert Systems, Communication of the ACM, february 88, volume 31, Number 2.

[16] Gardner, H. (1985), The Mind's New Science: a History of Cognitive Révolution, Basic Books, New York.

[17] Granier, J. and Espinasse, B.(1989), SNARX, un langage de représentation et d'interprétation des connaissances, Note de recherche N° 89-03, GRASCE/CNRS, Université Aix-Marseille III, Aix-en-Provence.

[18] Grize, J.B. (1982), De la logique à l'argumentation, Librairie Droz, Genève.

[19] Hendler, J.A. (1989), Problem Solving and Reaseaning: A Connectionist Perspective, in Connectionism in Perspective, R. Peifer, Z. Schreter, F. Fogelman-Soulier, L. Steels Editors, Elsevier Science Publisher, B.V., North Holland.

[20] Huard, P. (1980), Rationalité et Identité: vers une alternative à la théorie de la décision dans les organisations, Revue économique, vol. 31, n°3, 1980, Paris, pp. 540–572.

[21] Landry, M., Pascot, D., Briolat, D. (1985), Can DSS Envolve without Changing Our View of the Concept of Problem, North Holland, Decision Support Systems 1, pp. 25–36.

[22] Lauriere, J.L. (1976), Un langage et un programme pour énoncer et résoudre des problèmes combinatoires, Thèse de Doctorat d'état, Université Paris VI.

[23] Le Moigne, J.L. (1987), Intelligence des mécanismes et mécanismes de l'intelligence, in Nouvelle encyclopédie des Sciences et des Techniques, Fayard Paris.

[24] March, J.G. (1978), Bounded Rationality, Ambiguity, and the engineering of choice, The Bell Journal of Economics, vol. 9, n°2, fall 1978, pp. 587–608.

[25] Memmi, D. (1989), Connexionism and Artificial Intelligence as Cognitive Models, Notes et Document du LIMSI-CNRS, juin 89.

[26] Memmi, D. (1990), Connexionnisme, intelligence artificielle et modélisation cognitive, in Modèles connexionnistes, Intellectica n°9-10, pp. 41–79.

[27] Newell, A. (1969), Heuristic Programming Ill-Structured Problems, in Progress in Operations Research, Volume III, J.S. Aronofsky (ed.), John Wiley and Sons, 1969.

[28] Newell, A. and Simon, H.A. (1972), Humain Problem Solving, Englewood Cliffs, NJ, Prentice-Hall.

[29] Piaget, J. (1975), L'équilibration des structures cognitives, Presses Universitaires de France, Paris.

[30] Piaget, J. (1976), Logique et connaissance scientifique, Encyclopédie de la Pleiade, Paris.

[31] Piaget, J. (1979), L'épistémologie génétique, Presses Universitaires de France, 3 $^{0}$ édition, Paris.

[32] Ramaprasad, A. and Mitroff, I. (1984), On Formulating Strategic Problems, Academy of Management Review, No. 4, pp. 597–605.

[33] Rumelhart, D.E. and McClelland, J.L. éds. (1986), Parallel Distributed Processing, Volume I and II, Cambridge, Ma., MIT Press.

[34] Simon, H.A. (1960), The new Science of Management Decision, New York and Evanston, Harper and Row Publishers.

[35] Simon, H.A. (1979), Rational Decision Making in Business Organisations, American economic Review, in Models of Bounded Rationality, Vol. II, MIT Press, Cambridge, Mass.

[36] Simon, H.A. (1983), Search and Reasoning in Problem Solving, Artificial intelligence $n^{0}21$ , pp. 7.

[37] Toulmin, S. (1958), The uses of the Argument, University Press, Cambridge.
