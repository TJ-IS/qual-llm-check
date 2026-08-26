---
otero_id: 25210
otero_key: "FMHYZZVT"
title: "Operational Knowledge Representation for Practical Decision-Making"
authors: "Jean-Charles Pomerol; Patrick Brézillon; Laurent Pasquier"
year: "2002"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2002.11045698"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Operational Knowledge Representation for Practical Decision-Making

Jean-Charles Pomerol, Patrick Brézillon, Laurent Pasquier

To cite this article: Jean-Charles Pomerol, Patrick Brézillon, Laurent Pasquier (2002) Operational Knowledge Representation for Practical Decision-Making, Journal of Management Information Systems, 18:4, 101-115, DOI: 10.1080/07421222.2002.11045698

To link to this article: http://dx.doi.org/10.1080/07421222.2002.11045698

![](/api/attachments/FMHYZZVT/fulltext/images/54b6b08a22448c8ee3a7b01357568111f70e11023b12bd154b9ff3a01c8471bb.jpg)

Published online: 23 Dec 2014.

![](/api/attachments/FMHYZZVT/fulltext/images/df512dc2d4498fb50259eeb8759448141464a25769600bc34f3d11a44c379adf.jpg)

Submit your article to this journal

![](/api/attachments/FMHYZZVT/fulltext/images/a47ae01470be81fef6b5278f957090d3cd1438fe0fbc478a6934d2b0012929ee.jpg)

Article views: 19

![](/api/attachments/FMHYZZVT/fulltext/images/45968d5ca8baa80635edd5c75d3a65f8921580ca0a73ae0a2feaa9c0035d6701.jpg)

View related articles

![](/api/attachments/FMHYZZVT/fulltext/images/8347ca015d7b50fa70c409990285d91e2e4fabe6b7f858f7a8fa9ac0f072a8f8.jpg)

Citing articles: 7 View citing articles

# Operational Knowledge Representation for Practical Decision-Making

JEAN-CHARLES POMEROL, PATRICK BRÉZILLON, AND LAURENT PASQUIER

JEAN-CHARLES POMEROL is Professor of Computer Science and one of the Vice Chairpersons for Research of the University Pierre and Marie Curie in Paris (UPMC). He was formerly the head of the common UPMC-CNRS Artificial Intelligence Laboratory of Paris, now a part of the Computer Science laboratory of the UPMC (LIP6). Jean-Charles Pomerol defended his “Thèse d’état” in convex analysis in 1980. He then turned to research in the areas of decision theory and decision support systems. His current interests revolve around the design and development of “intelligent” decision support systems. He is the author or coauthor of many papers and four books concerning expert systems, decision support systems, and, recently, practical multicriterion decision-making (Kluwer Publishers, 2000). He is also the chief editor of the Journal of Decision Systems and the Revue Française d’Intelligence Artificielle (Hermes-Science Publishers).

PATRICK BRÉZILLON is a research fellow at the National Center for Scientific Research in France (CNRS). In 1983, he received his “Thèse d’état” in natural sciences at the University Pierre and Marie Curie. His thesis is devoted to the mathematica modeling of the calcium metabolism as a self-oscillating nonlinear model. He aims at merging mathematical modeling with artificial intelligence, and is interested in such topics as cooperation, context, explanation, and incremental knowledge acquisition in the framework of intelligent assistant systems. He has contributed to the founding and is one of the leaders of the worldwide research community working on contex representation and its use in real-world applications.

LAURENT PASQUIER is an engineer in automatics and operational research. He is completing a Ph.D. thesis, “Modeling of context-based reasoning, and application to incident management on subway lines,” under the direction of Patrick Brézillon, at the RATP (Parisian public transportation company) and LIP6. He is interested in knowledge representation and decision support systems.

ABSTRACT: For the design of an “intelligent” assistant system aimed at supporting operators’ decision in subway control, we modeled operators’ activity and knowhow. As a result, we introduce the notion of a contextual graph, which appears as a simple solution to describe and manage operational decision-making.

KEY WORDS AND PHRASES: context representation, contextual graphs, decision tree, knowledge representation, operational knowledge.

IN HIGHLY TECHNICAL AND HEAVILY DYNAMICAL regulation processes, operators who are responsible for the process control must rapidly react. If an incident occurs, they have only a few minutes to forge a representation of the issue, gather information on the situation, analyze the incident, and undertake corrective actions. To ease their job, many companies have established fixed procedures. Initially, general procedures have been designed to provide operators with a secure reference for process control. However, these general procedures overlook the contextual dimension of the situation at hand. Nowadays, companies are diversifying these procedures by increasingly introducing contextual considerations. This raises the question of representing and managing these very numerous, contextual-dependent procedures.

In this paper we present a new framework inspired from decision trees to represent and use contextual information in operational decision-making. This representation, named contextual graph, relies heavily on our previous works on the representation of context (such as [31]).

## Operational Knowledge Representation and Context

OPERATIONAL PRACTICES ARE DIFFICULT TO MODEL: first, they are numerous; second they are often implicit within a community of practice [6] and strongly linked one to another; and third, the main distinction among them is the context in which these practices apply. Moreover, these practices are often dynamically constrained in sequences of actions. To gather and study operational practices, we worked on the control of a subway line [4, 5, 25, 26]. In this framework, we recorded the incidents handled by the operators as a set of characteristics (precondition), including context description and the subsequent corrective action. Using production rules vocabulary, we could say that we collected the precondition of the actions, together with their conclusion. With this feedstock, we constructed an adapted representation to record and model this type of knowledge for reuse purposes. Before going forward with the descrip tion of the representation by contextual graphs let us discuss some facts about context.

## Importance of the Contextual Dimension and

## Dynamics of Context

From an engineering point of view we can start from the definition of context as a collection of relevant conditions and surrounding influences that make a situation unique and comprehensible [1, 14]. The difficulty with this definition is that there are “numerous interacting factors that people do not even pay attention to on a conscious level, and many of which are outside the ability of machine input devices to capture” [12].

Let us take an example: in the control of a subway line [4, 5], where a large amount of knowledge about trains, electricity, peoples reactions, and so on, contributes to make the situation unique, whereas some more particular conditions about the time, the day, the weather, and so on, specifically influence many decisions. In other words, there is a common background context that is then specified by some conjecture and contingent influences. For example, the general context is subway control, which differs from train or bicycle control, although they share some mechanical laws and the particular context is specific to a line, a day, an hour, and so on. These considerations explain why Tiberghien [37] defines context as the whole set of secondary characteristics of a situation or secondary properties of a cognitive or motivational state of an individual, which may modify the effect of an effective stimulation (stimu lus) or an oriented activity.

![](/api/attachments/FMHYZZVT/fulltext/images/50d96dd8e644dd8f57c61a0921e9fb0ecf01f67cc70b3b99f6f117f5bc6a0e84.jpg)  
Figure 1. Three Types of Contexts

Thus, it would probably be wise to talk of primary and secondary context to distinguish between the general, relatively fixed primary characteristics of a situation, and the secondary characteristics, which are more mobile. If we think about primary context, we must confess that it is difficult to avoid the word knowledge about this general background used by the operators to carry out their task. This is the reason we have proposed [3] to call “contextual knowledge” the primary or back-stage context.

Therefore, at a given step of a decision process or task-performing, we distinguish between the part of the context that is relevant at this step of decision-making or taskperforming, and the part that is not relevant. The latter part is called external knowledge. The former part is called contextual knowledge, and obviously depends on the agent and on the decision at hand. At a given step of decision-making, a part of the contextual knowledge is proceduralized. We call it the proceduralized context (Figure 1). The proceduralized context is a part of the contextual knowledge, which is invoked, structured, and situated according to a given focus.

The contextual knowledge is a backstage knowledge, whereas proceduralized context is immediately useful for the task at hand. In our representation of context, the contextual knowledge is largely tacit, mainly because it is the context that everybody knows without expressing it. In a distinction reminiscent to cognitive ergonomics [21], we could say that the contextual knowledge is useful to identify an activity whereas the proceduralized context is relevant to characterize a task.

An important issue is the passage from contextual knowledge to proceduralized context. This proceduralization results from the focus on a task. Thus, the proceduralization process is task-oriented just as knowing how; it is often triggered by an event or primed by the recognition of a pattern. Another aspect of procedural ization is that the operators transform contextual knowledge into some functiona knowledge or causal and consequential reasoning in order to anticipate the result of their own action (see also [11], for a similar observation). Thus, the functionalization is a part of the proceduralization process, and this is the reason why we have chosen the term proceduralization.This functionalization, or proceduralization,obeys to the necessity of having a consistent explicative framework to anticipate the results of a decision or an action. This consistency is obtained by reasoning about causes and consequences in a given situation. Thus, we can separate the reasoning between diagnosing the real context and anticipating the follow-up [28]. The second step needs a conscious reasoning about causes and consequences. This explicit reasoning in the mind of the subject has also been recognized by Levesque [22], about beliefs that are very close to our view.

A second proceduralization aspect is a kind of instantiation (see also [13]). This means that the contextual knowledge or background context needs some further speci fications to perfectly fit the task at hand. These precisions and speciation brought to the contextual knowledge is also a part of the proceduralization process. We gave elsewhere [26] some insights about the construction of the proceduralized context by the interaction between agents.

## Representing Context

Artificial intelligence was developed, for several years, representing operational knowledge languages. Here we present some approaches. Let us start with production rules since, as we said, at a first glance, operational decision-making can be interpreted as rule application. These rules are pieces of knowledge of the form “if preconditions, then conclusions.” They are recorded in large rule bases difficult to update. The rules are structured chunks of knowledge, which are easily understood by the domain ex perts. However, the lack of structure of the rule-base impedes the comprehension (even for the experts of the domain) and the maintenance of the knowledge.

Some works have been done on rule-bases structuring, namely on the splitting of the rule bases into several rule packets, each containing a subset of rules applied to solve a specific subproblem [2]. Clancey [9] proposed to add screening clauses to the precondition part of the rules so that they are activated only in some kind of context, this amounted to adding some clauses constraining the triggering to a certain contex in the preconditions of the rules. This is burdensome because the designers must anticipate all the possible contexts to define the preconditions of the rules. Moreover, each rule describes a part or a whole context without any reference to the dynamics of the situation that is fundamental to understand the situation.

The decision tree approach [32] tries to represent the decision step-by-step. This i obtained by the presence of two types of nodes: the event nodes and the decision nodes. At an event node, paths are separated according to all the possible realizations of an event on which the decision-maker has no influence. At a decision node, the person makes a choice. Thus, we obtain a tree of scenarios, each depending on the events. The main problem with this structure is the combinatorial explosion (see [30]). The number of leaves is an exponential function of the depth of the tree. The addition of a contextual element may easily double the size of the tree.

Belief networks [27] and influence diagrams (for example, see [23]) have also been used for decision-making. In these nets, the nodes represent propositions, whereas the arcs make explicit direct dependency between the linked propositions. Thus, the combinatorial explosion is avoided, but the propositions are random variables and the complexity is reintroduced via the conditional probabilities that must be propagated along the links. The belief networks and influence diagrams are particularly used for diagnosis. Indeed, they face the same difficulty as decision trees when the number of events or random variables increases. They are very information-intensive in terms of probabilities. Another difficulty is that influence diagrams bring a simplification of the decision tree only when many variables are independent [15, 27]; this depends on the case at hand and is generally not true in troubleshooting.

Another interesting approach is case-based reasoning (CBR), which is a kind of analogy reasoning [18]. To solve a current issue, one selects the most similar problem in a problem base and adapts the solution to the problem at hand. Note that instead of adapting prior solutions, Leake [19] proposes as an interesting alternative to store and reuse traces of how those solutions were derived. The main advantage of this reasoning is its great power of generalization and its maintenance facility. However, it fails to provide explanations on the obtained solution.

## Contextual Graphs

## Representing Contextual Information

NONE OF THE ABOVE REPRESENTATIONS gave us satisfaction and stuck to the operators’ reasoning, which is more or less a mixture of rules, decision trees, and CBR. This is the reason we started to thoroughly study the operators’ practice in the case of incident troubleshooting in the Paris subway. This study proved that the operators are very sensitive to the context of their action. They try to diagnose, as soon as possible, the real state of the system by recognizing and anticipating sequences of events. As such, it is reminiscent of scenario thinking. For this reason we started from the notion of a decision tree.

However, there is a big difference with scenario thinking. In a decision tree, each event at an event node carries on a part of the uncertainty of the situation. There are two ways to manage this uncertainty, either assess some probabilities for each event, which is the usual view in decision theory, or consider that the two events are possible, anyway, depending on the circumstances. Our representation must provide an answer for any possible circumstances, whatever the probability is. The problem of an operator is to get an adapted answer as soon as he knows what the situation is.

Thus, the main problem is to diagnose the exact situation according to the contextual information reaching the operators. For this reason we considered that each branch actually describes a contextual knowledge, which becomes more and more accurate as long as the branch is followed. The question is not to guess the true future event, because all the situations that may happen have to be represented whatever their probabilities are. Thus, we are no longer interested by the probability of a branch, but by the possibility to determine, as soon as possible, on what path the operator is, to determine what is the next action to undertake. In other words, we come back to the original idea of Savage [33], namely that each state of nature (a sequence of events is a state of nature) describes a state of the world, or using our words, a context for action. We must also stress that the operator has no choice of the path and therefore no optimal choice, because the path is dictated by the context of the incident.

At this step there are no probabilities on the events, the main purpose is to describe, with the maximum of parsimony, all the possible contexts in which the decision has to be made. For example, in Figure 2 the branch with $\{ C _ { 1 2 } , C _ { 2 1 } , C _ { 3 2 } \}$ describes a context in which there is no immediate repair possible but still enough power and a steep incline in view (see the Appendix for the significance of the nodes). For this reason we will talk hereafter of context nodes instead of event nodes and of contexts instead of states of nature. Let us repeat that we are not interested in the probability of say, $C _ { 1 2 }$ versus $C _ { 1 1 }$ , because our representation intends to be used for any incident, whatever the probabilities are. In this sense, the $C _ { i }$ are not random variables unlikely in influence diagrams [23]. At a first glance, influence diagrams are acyclic graphs bringing a simplification to decision trees when the random variables are only moderately dependent on each other. In operation, the difference is that we are less interested in the possible causes of the problems than in its resolution. When an incident occurs, the probability of occurrence no longer matters, what matters is the chaining of troubleshooting actions.

The action postponement to the leaves observed in Figure 2 amounts to relating each decision to a state of nature, here the context described in the branch. Thus, our representation tends to stick to operators’ behavior. In some cases, especially at the beginning of the tree, decision-making under uncertainty would probably, if possible, be interesting, but by trying to gather as much relevant information as possible before action, the operators endeavor to make their decision under certainty. This means that when undertaking an action in the tree they consider that, due to the contextual information they got, the state of nature between the root and the action un dertaken is the true state of nature.

Thus, we adopted a tree representation, made of two types of elements: the actions and the contextual nodes, which select a branch depending on the knowledge abou the current context. Figure 2 shows the decision tree representation of the procedure for “train lack of power” solving (the meaning of the boxes is not important here, but can be found in the Appendix and in [24]), it suffices to say that the rectangular boxes are actions and the circles, contextual nodes.

In summary, our representation is inspired by decision trees, but mainly differs on two points. First, our trees have no chance nodes, but contextual nodes. Second, there are no probabilities. This representation shows several important characteristics that have some consequences on the size and structure of our tree:

<sub>d</sub> <sub>by</sub> <sub>[University</sub> <sub>of</sub> R<sup>ochester]</sup> <sup>at</sup> <sup>03:14</sup> <sup>11</sup> <sup>A</sup>  
![](/api/attachments/FMHYZZVT/fulltext/images/d31581fb8f432ef3a7c750468ea6c541b3be4e33293f05560eff3b306210cb47.jpg)  
<sub>nTreeRepresen</sub>t<sup>ingtheOficialProcedurefor“LackofTrainP</sup>

1. As said in the subsection “Representing Context,” operators use many contextual elements to perform their choice. This leads to a large number of practica strategies, even for the same incident. This multiplies the number of branches and the tree grows rapidly.

2. The operators prefer to gather a maximum of information before making their decision. This behavior postpones most of the actions to the end of the branches of the tree [2, 30]. This observation is very close to the observation of Watson and Perera [39], who consider a hierarchical case representation that holds more general contextual features at its top and specific building elements at its leaves.

3. The operators preferentially choose actions allowing them to reach common intermediary situations. Thus, they can reuse common strategies to clear the incident. Graphically, the tip sequence of actions is often repeated from one branch to another.

4. Several action sequences are executed in the same order in different situations (paths).

5. Some actions could be done in a different order, but must precede a given one. For example, before linking two trains, both have to be emptied, but the order in which they are emptied does not matter (partial order on the actions).

It is not easy to represent highly contextual decision-making in a tree structure. In the next section, we explain the modification we have done, based on the characteristics discussed above, to obtain a manageable structure for representing operationa knowledge about incident solving on subway lines.

## From Contextual Trees to Contextual Graphs

First, we can reduce the number of objects in the structure by replacing repeated subsequences of actions (characteristics 3 and 4 above) by a single object called macroaction. The choice made for defining the different macro-actions is based on common sub-procedures known by the operators, such as “linking trains” and “return to end-station without travelers.” The principle of replacing is explained in Figure 3.

This replacement simplifies the lecture of the tree, but does not reduce the structural expansion of the tree. Second, relying on the previous observation 3, we can merge the branches of the tree as soon as the sequence leading to the end of the incident are similar, as shown in Figure 4.

Cognitively speaking, this amounts to using a scarcity principle, which leads the operators to try to reuse well-known procedures as soon as possible. This operation has several consequences on the structure of the representation and on the meaning of the model.

1. We no longer face a tree but a graph. This graph is oriented and has no cycles, with exactly one root and one goal because the operators have only one goal (clear the incident and go back to normal exploitation) and the branches express only different strategies, depending on the context, to achieve this goal. The graph structure moreover allows extending of the representation.

![](/api/attachments/FMHYZZVT/fulltext/images/ec255e31c4ea123cf54211a4bee5f4a88c294287191399f5cc466c34df843569.jpg)  
Figure 3. From a Sequence of Actions to a Macro-Action

![](/api/attachments/FMHYZZVT/fulltext/images/9e76a00a7d7550e9b8501ea3adee559af75c3212ffe5379f76b93766afa32142.jpg)  
Figure 4. From Tree to Graph

2. The size of the structure is now under control and the consideration of a new contextual element will add some elements in the graph, but not drastically increase its size.

3. The change of the structure introduces a dynamic comparable to the dynamics of the change between proceduralized and contextual knowledge. Indeed, when two branches are merged, it means that the undertaken actions led to a common situation from different contexts. The contextual elements attached to the different branches are proceduralized at the diverging node. They stay in this state for the different action sequences because they intervene in the branch decisions. Finally, they are de-proceduralized when the branches are merged. By doing this, we explicitly express the duration of the contextual elements (Figure 5).

Even in a part of a subgraph it may happen that the actions are only partially ordered. (See the above example of two trains on the same line, which have to be cleared of the travelers whatever the order of the operations is.)

We need to represent this issue; this is why we introduced the temporal branching symbols to represent action sequences that can be done in different order (characteristic 5). This symbol is made of two parts: a divergent branching and a convergent branching; the parallel branches wear the temporally independent decision blocks. Finally, we obtain the structure represented in Figure 6, that we called contextual graph.

In the contextual graphs that we have built for several incident types, we note that some parts of the different graphs are identical. Analyzing these subgraphs, we exhibit that they complete a common subgoal (for example, when a train lacks power and cannot restart alone, or when a train has no more brake, either train needs to be helped by another train). Such a representation by contextual graphs/subgraphs (Figure 7) is very similar to the generic tasks proposed by Chandrasekaran [8]. The difference is that our tasks are not generic in the sense that they cannot be combined to lead to more integrated tasks as Chandrasekaran’s ones; they are rather elementary tasks that can only be linked or followed by each other in any order.

![](/api/attachments/FMHYZZVT/fulltext/images/0090a48e1afd8ce2504897e2b671729f2f0cd4a3ae2e140b27ee305b9b7883eb.jpg)  
Figure 5. Proceduralization and De-proceduralization

![](/api/attachments/FMHYZZVT/fulltext/images/5fb2dbd7bd7c1eda6e512554af24192407aebde11c864b290cb549471e17558d.jpg)  
Figure 6. Contextual Graph Representing the Official Procedure for “Lack of Train Power” Incident Represented in Figure 2

## Contextual Graphs in Action

MOST OF THE EXAMPLES IN THIS STUDY are drawn from a system (SART) that we are developing by using contextual graphs for the Paris subway organization (RATP). The SART project [5, 24] aims at the design and development of a decision support system for the operators in charge of the control of a subway line. This project is based on the interaction between the operator and the system and will ease their mutual comprehension. For this purpose, we tried to mimic the system reasoning on the operators’ one. Thus, we needed to analyze the operational knowledge used by operators and to record it in an adapted structure that can be easily understood by the operators and efficiently used by the computer. For an extensive description of the context of the case, see [5] and [24]. The system is not yet in operation, but a part of the knowledge is already represented by contextual graphs and submitted to operators’ validation [40].

![](/api/attachments/FMHYZZVT/fulltext/images/4e46f7323884aa36fa48ff3d4271fe90c16dcdfb6d2b514ec2e4c6d771787df4.jpg)  
Figure 7. Set of Contextual Graphs Used While “Lack of Train Power” Incident Resolution

Our representation by contextual graphs comes from this experience. This repre sentation is more compact than trees, and is well accepted by the operators [40], it simply represents the succession of actions to carry out in order to solve an incident; the different possible paths express the possible strategies according to the context.

The idea to use the dynamics of scenarios for modeling practices is somehow remi niscent of various scenario-based analyses, in particular, in strategic planning [20, 38], design [7], software engineering, and especially in requirements engineering (such as [16, 29, 36]). For instance, the manual V1.3 of the Unified Modeling Language (UML) describes how activity graphs are used to model operations (action state). When an activity is modeled, it is equipped with some internal procedures to execute and some actions that trigger other activities. UML let the possibility to execute actions, either linearly or in parallel. This last possibility is quite similar to temporal branching in our contextual graphs.

Design also uses a notion of scenario, but in a slightly different sense than in software engineering. The defining property of a scenario is that it projects a concrete description of the activity that the user engages in when performing a specific task, a description sufficiently detailed so that design implications can be inferred and specified [7]. Central to most scenario-based design is a textual description or a narrative episode of use. A scenario is a narrative that describes someone trying to do something in some environment [17]. As such, it is a description of a context, which contains information about users, tasks, and environment. Scenarios are viewed by the user and may include social background, resource (such as, disk space, time) constraints, and background information. Scenarios seek to be concrete; they focus on describing particular instances of use, and according a user’s view, they describe what happens, how it happens, and why [7]. By using a narrative it is possible to capture information about the user’s goals, and the context the user is operating in. Scenarios help to express the complexity of the working context to design, and reveal some of the organizational trade-offs implicit in developing new automation [10]. In some sense, contextual graphs offer an adequate representation for the capture of all these kinds of scenarios. What is striking is that, in all these frameworks, as in our case, what is important is not the probability, but the exhaustibility; all the possible paths must have been envisioned.

Each isolated subgraph is named (operators know the corresponding procedures and agree on a name), and as such, isolated and identified, it is more or less reminiscent of a script [34, 35], or a scheme of action, but moreover, it includes the dynamics of proceduralization. These structures can be reused and adapted for other actions. For example, in Figure 7 the sub-procedure “helping train clearing” is derived from the sub-procedure “damaged train clearing” and adapted by the introduction of the fact that an available train may run to the next station, if this station is free, to evacuate its travelers in better conditions. In our system the subgraphs are the elementary chunks of reasoning stored and reminded to the operators in case of incident. The adaptation to the context is made by the choice of the path. Some flexibility is left to the operators by the adaptation of the elementary actions contained in the graph, because the actions are generally defined by their result rather than by a detailed modus operandi.

## Conclusion

OUR REPRESENTATION BY CONTEXTUAL GRAPHS is inspired from practice. We observed that contextual information matters more than probabilities to make a decision in an operational setting. Thus, we adapted the notion of a decision tree to take into account contextual representation and its dynamics. We simplified the tree representation, thanks to two notions, namely macro-action and temporal branching. Going one step beyond the computer representation of the reasoning, relying on context and contextual graphs, we have pointed out that some subgraphs represent usual procedures or schemes of action. These subgraphs, beyond the fact that they give a simple computer representation of reasoning, have a deep meaning for operators and are significant, even drawn out of the context of a given incident. We are thus able to propose a set of interrelated contextual graphs that incorporate the notion of context in any problem solving (such as, an incident solving) and represent the dynamics of the proceduralization de-proceduralization process.

Acknowledgments: RATP and COFECUB in France and CAPES in Brazil provided grants. The authors thank J.-M. Sieur at RATP and all of the other members working on the SART project.

## REFERENCES

1. Anderson J.R. Rules of the Mind. Hillsdale, NJ: Lawrence Erlbaum, 1995.

2. Brézillon, P., and Pomerol, J.-C. Using contextual information in decision making. In D. Berkeley, G. Widmeyer, P. Brézillon, and V. Rajkovic (eds.), Context Sensitive Decision Sup port Systems. London: Chapman and Hall, 1998, pp. 158–173.

3. Brézillon, P., and Pomerol, J.-C. Contextual knowledge sharing and cooperation in intel ligent assistant systems. Le Travail Humain, 62, 3 (1999), 223–246.

4. Brézillon, P.; Pomerol, J.-C.; and Saker, I. Contextual and contextualized knowledge: An application in subway control. Special Issue on Using Context in Application, Internationa Journal on Human-Computer Studies, 48, 3 (1998), 357–373.

5. Brézillon, P.; Gentile, C.; Saker, I.; and Secron, M. SART: A system for supporting operators with contextual knowledge. In M. Cavalcanti and P. Brézillon (eds.), First Interna tional and Interdisciplinary Conference on Modelling and Using Context (CONTEXT’97). Rio de Janeiro: Federal University of Rio de Janiero, 1997, pp. 209–222, available at www.poleia.lip6.fr/\~brezil/Pages2/CONTEXT-97/index.html.

6. Brown, J.S., and Duguid, P. Organizational learning and communities of practice: Towards a unified view of working, learning and organization. Organization Science, 2, 1 (1991), 40–57.

7. Carroll, J.M. (ed.). Scenario-Based Design. New York: Wiley, 1995.

8. Chandrasekaran, B.; Johnson, T.R.; and Smith, J.W. Task-structure analysis for knowl edge modeling. Communications of the ACM, 35, 9 (1992), 124–137.

9. Clancey, W.J. Tutoring rules for guiding a case method dialogue. International Journal of Man-Machine Studies, 11, 1 (1983), 25–49.

10. Dearden, A.; Harrisson, M.; and Wright, P. Allocation of function: Scenarios, context, and the economics of efforts. International Journal of Human-Computer Studies, 52, 2 (2000), 289–318.

11. Decortis, F.; Noirfalise, S.; and Saudelli, B. Activity theory, cognitive ergonomics and distributed cognition: Three views of a transport company. International Journal of Human-Computer Studies, 53, 1 (2000), 5–33.

12. Degler, D., and Battle, L. Knowledge management in pursuit of performance: The chal lenge of context. Performance Improvement Journal, 39, 6 (2000), 25–31.

13. Grimshaw, D.J.; Mott, P.L.; and Roberts, S.A. The role of context in decision making: Some implications for database design. European Journal of Information Systems, 6, 2 (1997), 122–128.

14. Hasher, L., and Zacks, R.T. Automatic processing of fundamental information: The case of frequency of occurrence. American Psychologist, 39, 11 (1984), 1372–1388.

15. Howard, R.A. From influence to relevance to knowledge. In R. Oliver and J. Smith (eds.), Influence Diagrams, Belief Nets, and Decision Analysis. New York: John Wiley & Sons, 1990, pp. 3–23.

16. Jarke, M.; Rolland, C.; Sutcliffe, A.; and Dömges, R. (eds.). The Nature of Requirements Engineering.Aachen, Germany: Shaker Verlag, 1999.

17. Karat, J. Scenario use in the design of a speech recognition system. In J.M. Carroll (ed.), Scenario-Based Design: Envisioning Work and Technology in System Development.New York: John Wiley & Sons, 1995, pp. 109–133.

18. Kolodner, J. Case-Based Reasoning. San Francisco: Morgan Kaufmann, 1993.

19. Leake, D.B. Case-based reasoning: Experiences, lessons, and future directions. In D.B. Leake, CBR in Context: The Present and Future. Menlo Park, CA: AAAI Press, 1996, pp. 111–124.

20. Leemhuis, J.P. Using scenarios to develop strategies. Long Range Planning, 18, 2 (1985), 30–37.

21. Leplat, J., and Hoc, J.M. Tâche et activité dans l’analyse psychologique des situation [Task and activity in psychological analysis of interactions]. Cahiers de Psychologie Cogni tive, 3, 1 (1983), 49–63.

22. Levesque, H.J. A logic of implicit and explicit belief. In Proceedings of the Fourth National Conference on Artificial Intelligence (AAAI-84). Menlo Park, CA: AAAI Press, 1984, pp. 198–202.

23. Oliver, R., and Smith, J. (eds.). Influence Diagrams, Belief Nets and Decision Analysis. New York: John Wiley & Sons, 1990.

24. Pasquier, L. Modélisation de raisonnements tenus en contexte et application aux agents d’aide à la gestion d’incidents de SART [Modeling context-based reasoning with application to the management of incidents in SART]. LIP6 Research Report N.2000-010. LIP6, Paris, 2000.

25. Pasquier, L.; Brézillon, P.; and Pomerol, J.-C. Context and decision graphs in incident management on a subway line. In P. Bouquet, L. Serafini, P. Brézillon, M. Beneracatti, and F. Castellani (eds.), Modeling and Using Context (CONTEXT-99), Lecture Notes in Artificia Intelligence, no. 1688. Berlin: Springer Verlag, 1999, pp. 499–502.

26. Pasquier, L.; Brézillon, P.; and Pomerol, J.-C. From representation of operational knowl edge to practical decision making in operations. In S. Carlsson, P. Brézillon, P. Humphreys,

B.G. Lundberg, A. McCosh, and V. Rajkovic (eds.), Decision Support Through Knowledge Management. Edsbruk, Sweden: Akademitryck AB, 2000, pp. 301–320.

27. Pearl, J. Probabilistic Reasoning in Intelligent Systems. San Francisco: Morgan Kaufmann, 1988.

28. Pomerol, J.-C. Artificial intelligence and human decision making. European Journal of Operational Research, 99, 1 (1997), 3–25.

29. Pomerol, J.-C. Scenario development and practical decision making under uncertainty: Application to requirements engineering. Requirements Engineering, 3, 1 (1998), 174–181.

30. Pomerol, J.-C. Scenario development and practical decision making under uncertainty Decision Support Systems, 31, 2 (2001), 197–204.

31. Pomerol, J.-C., and Brézillon, P. Dynamics between contextual knowledge and proceduralized context. In P. Bouquet, L. Serafini, P. Brézillon, M. Beneracatti, and F. Castellan (eds.), Modeling and Using Context (CONTEXT-99), Lecture Notes in Artificial Intelligence, no. 1688. Berlin: Springer Verlag, 1999, pp. 284–295.

32. Raïffa, H. Decision Analysis. New York: McGraw-Hill, 1968.

33. Savage, L.J. The Foundations of Statistics. New York: John Wiley & Sons, 1954.

34. Schank, R.C. Dynamic Memory, A Theory of Learning in Computers and People. Cambridge: Cambridge University Press, 1982.

35. Schank, R.C., and Alberson, R.P. Scripts, Plans, Goals and Understanding: An Inquiry into Human Knowledge Structures. Hillsdale, NJ: Lawrence Erlbaum, 1977.

36. Sutcliffe, A. Scenario-based requirement analysis. Requirements Engineering, 3, 1 (1998), 48–65.

37. Tiberghien, G. Context and cognition: introduction. Cahier de Psychologie Cognitive, 6 2 (1986), 105–119.

38. Wack, P. Scenarios: Uncharted waters ahead. Harvard Business Review, 63, 5 (1985), 72–89.

39. Watson, I., and Perera, S. A hierarchical case representation using context guided retrieval. Knowledge Based Systems Journal, 11, 5–6 (2000), 285–292.

40. Zanarelli, C.; Saker, I.; and Pasquier, L. Un projet de coopération ergonomes/concepteurs autour de la conception d’un outil d’aide à la régulation du trafic du métro [An ergonomist– designer co-operation about the design of a subway control system]. In Ingénierie des Connaissances (IC’99). Palaiseau, France: Association Française pour l’Intelligence Artificielle, 1999, pp. 161–170.

<table><tr><td colspan="2">Actions</td><td colspan="2">Contexts</td></tr><tr><td>1</td><td>Residual traffic regulation</td><td>C11</td><td>Immediate repair possible</td></tr><tr><td>2</td><td>Damaged train continues with travelers</td><td>C12</td><td>Immediate repair impossible</td></tr><tr><td>3</td><td>Damaged train continues with travelers until a steep incline</td><td>C21</td><td>Enough motor coaches available</td></tr><tr><td>4</td><td>Damaged train restarts without travelers</td><td>C22</td><td>Not enough motor coaches available</td></tr><tr><td>5</td><td>Stable damaged train at end station</td><td>C31</td><td>No steep incline between damaged train and end station</td></tr><tr><td>6</td><td>Repair damage</td><td>C32</td><td>Presence of steep incline until end station</td></tr><tr><td>7</td><td>Exit of the travelers out of the damaged train</td><td></td><td></td></tr><tr><td>8</td><td>Exit of the travelers out of next train</td><td>C41</td><td>Damaged train at station</td></tr><tr><td>9</td><td>Exit of the travelers out of damaged train via available cars</td><td>C42</td><td>Damaged train under tunnel</td></tr><tr><td>10</td><td>Exit of the travelers out of next train via available cars</td><td>C43</td><td>Damaged train partially at station</td></tr><tr><td>11</td><td>Exit of the travelers out of damaged train via track</td><td></td><td></td></tr><tr><td>12</td><td>Exit of the travelers out of next train via track</td><td>C51</td><td>Next train at station</td></tr><tr><td>13</td><td>Next train joins damaged train</td><td>C52</td><td>Next train under tunnel</td></tr><tr><td>14</td><td>Link both trains</td><td>C53</td><td>Next train partially at station</td></tr><tr><td>15</td><td>Convoy return to end station</td><td></td><td></td></tr><tr><td>16</td><td>Disassemble convoy</td><td>C61</td><td>Presence of a station between damaged train and next train</td></tr><tr><td>17</td><td>Next train goes to next station</td><td>C62</td><td>No station between both trains</td></tr><tr><td colspan="2">Macro-actions</td><td colspan="2">Actions lists</td></tr><tr><td>MA 1</td><td>Damaged train continues service</td><td colspan="2">Actions 2 and 5</td></tr><tr><td>MA 2</td><td>Damaged train stops service</td><td colspan="2">Actions 7, 4, and 5</td></tr><tr><td>MA 3</td><td>Make a convoy with damaged train and next train</td><td colspan="2">Actions 13, 14, 15, 5, and 16</td></tr><tr><td>MA 4</td><td>Empty next train at a station</td><td colspan="2">Actions 17 and 8</td></tr></table>
