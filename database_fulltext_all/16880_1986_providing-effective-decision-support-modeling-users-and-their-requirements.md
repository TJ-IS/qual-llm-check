---
otero_id: 16880
otero_key: "7ACC93WW"
title: "Providing effective decision support: Modeling users and their requirements"
authors: "Suranjan De"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90002-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Providing Effective Decision Support: Modeling Users and Their Requirements

Suranjan DE

Department of Management Sciences, University of Iowa, Iowa City, IA 52242, USA

The major premise of this paper is that in order for a DSS to be effective in a given problem domain, it is important to model the decision-making behavior of the user over and above traditional problem solving concerns. This is achieved by extending the traditional planning framework based on first-order logic to include modal logic. This extended framework is then used to represent beliefs and desires of the user, communicative actions performed by the user and the system, as well as the usual goals, task-related actions etc. The essence of this approach, then, is to view natural language utterances of the user of a DSS as speech acts which can be modeled using the extended framework; this view can, in turn, be used to interpret natural language utterances of the user.

Keywords: Decision Support Systems, Modal Logic, Speech act, Natural Language Processing.

![](/api/attachments/7ACC93WW/fulltext/images/8026db187ee0c691fcd1389eecfe58d4d6046f62e928233d423f5015bdf749f9.jpg)

Suranjan De is an Assistant Professor of Management Information Systems in the Department of Management Sciences at the University of Iowa. He received his Ph.D. from the Krannert Graduate School of Management at Purdue University. His current research interests include decision support systems and the application of artificial intelligence to the solution of manufacturing problems. He is a member of TIMS, ORSA, ACM and the IEEE Computer Society.

## 1. Introduction

In order that a decision support system (DSS) be effective as a decision-making aid, it is important that it not only solve a problem but solve it in terms specific to the user. This implies that the DSS examine a problem in the particular context of the user; that entails knowing or inferring the user's goals and needs, what specific ramifications each alternative may have for the user, how a particular decision may affect the user's employees, owner, competitors, customers and suppliers and what priorities the user places on these possible effects. In other words, the DSS should have the ability to infer the goals of the user, the ability to handle a wide variety of user goals and to adapt its advice to the disparate needs of the user.

It is our contention that building an effective DSS requires that we be able to model decision-making behavior over and above traditional problem solving concerns. In an earlier paper [2], a theoretical basis was developed for understanding the decision process and exploiting the understanding to improve the relevance of available problem solving techniques in a particular functional area. The functional area of interest there was manufacturing. The major emphasis of this paper is to examine specifically the role of language in enhancing the user's decision-making process in the manufacturing context within the framework described in [2]. Some of our earlier papers [3,4] have examined the issue of natural language processing in a DSS environment. However, none of them have explicitly considered representing users and their requirements and taking advantage of that representation in enhancing the language understanding process.

## 2. What's involved in providing decision support?

Instead of viewing decision-making as a process of information grinding, one may view it as a process of tentative, arduous deliberation. In this view, the making of decisions itself is treated as a complex task. The difficulty with complex problems is that it is virtually impossible to decide on circumstances, goals and means and then determine the appropriate solution, all at the same time. One simply does not have the information or the computing competence to do so.

How can a DSS help in such a situation? Generally speaking, the DSS could break complex tasks into simpler tasks, combine smaller decisions (made regarding the simpler subproblems) into bigger ones and, in doing so, also reassess our decisions and the process by which we arrived at them [2]. The emphasis on being able to review and revise tentative solutions or decisions adds to the effectiveness of the decision-making process. The mechanism for doing so will be discussed later in the paper. The importance of the above approach, however, lies not so much in the adoption of a hierarchical planning approach where the revision of tentative solutions are also considered, but in the role that the language component plays in bringing additional flexibility to the deliberative process. Therefore, the traditional interaction mode, whereby the user can only ask questions of the system and the system may only answer them, is clearly inadequate. What we need is a language component that would allow the DSS to become intelligent and helpful to the user, thereby aiding in his/her decision-making process. This sort of capability can be achieved by incorporating in the system the ability to ‘understand’ rather than merely decode utterances of the user. (Here we assume that the user will be interacting with the system through a natural language interface.) Over and above syntactic and semantic analysis, natural language ‘understanding’ requires reasoning about other agents, what they might do and what they believe. By reasoning about the knowledge and wants of other agents, the system ought to determine what courses of action other agents can be expected to take in the future and incorporate those actions into its own plans.

The importance of these considerations can hardly be overstated. In a decision-making context, users, when asking questions of the systems, expect their intentions to be recognized and responded to. They expect assistance from the system in order to interpret their answers, correct their misconceptions and choose an alternative means to fulfilling their goals when a dead end is reached. Besides, users do more than just ask questions; they give commands, make comments, seek clarifications and provide descriptions of their desires. In a traditional system, solving a complex task would involve the systematic specification of all the details that are typically left unspecified when the manager instructs another person to carry out the same task. In our case, the system ought to know enough about the goals and intentions so that it can fill in details in reasonable ways, asking the user for clarification when necessary. The language component of the DSS, in essence, should model a speaker-hearer system (despite the name, the interest lies in typed input rather than voice input) where the effectiveness is enhanced as a result of the DSS sharing with the user knowledge of the domain of discourse, knowledge of some of the user's intentions and goals as well as what the user thinks the system can do. Misspecification of the belief knowledge may cause an otherwise effectively developed system to appear as unresponsive to the user's needs. The statement that the effectiveness of the speaker-hearer system is enhanced by the systems's knowledge of the domain of discourse implies that each such system should focus on any one domain of discourse exclusively. The domain of discourse in our case is manufacturing.

## 3. A planning framework for language understanding

Central to adopting the planning framework is the notion that language understanding is an instance of goal-directed reasoning performed by the DSS. The system must engage in a process of reasoning about how an utterance is being used (i.e., what are the user's intentions), what communication actions it should perform, and how they should be performed. The system should be capable of inferring what the user wants to achieve as well as performing actions that lead to the desired goal. In a sense, the system carries out the process of understanding utterances of the user and the tasks that are implied by the user's queries in an integrated fashion.

The system has three functional components, each of which performs some form of goal-directed reasoning: linguistic level reasoner, communicative level reasoner and task level reasoner.

Conceptually, the functioning of the system can be summarized as follows. First, the system receives as input an utterance from the user (or the managerial decision-maker) through the natural language interface which it translates into an internal form which the system can process. The system then examines the utterance in internal form and based on the mood of the sentence attributes the effect of the (communicative) act to be a goal of the user. The next task is to infer, if possible, using intended plan recognition and shared beliefs, how the actions of the user fit into a plan the user is expected to have. If a plan cannot be uniquely specified, a system goal to discover the user's goal is created. Then more detailed system goals need to be created to achieve the intended goals of the user. Given these detailed system goals, the system can use its own beliefs about the problem domain to determine conflicts or obstacles at which the user's plans might fail, or that the user might need help. Then the system can adopt the negation of these obstacles as goals for the system. The system can now construct a plan that achieves the system's goals, especially goals to overcome the user's obstacles. Depending on this goal, this plan may include communicative actions, such as response to the user's query or utterance, or perhaps questions to clarify the user's goals. Now the resulting sequence of actions could be executed. A schematic diagram of the system as we have described it is given in fig. 1. For a more detailed description of the overall framework, see [2].

The broad framework that we have just outlined is based on what is referred to as planning in the Artificial Intelligence (A.I.) parlance. Early research on planning has dealt for the most part with single agents in simple worlds performing only task related actions [7]. However, in our case where we also need the system to interpret and perform communicative actions, the issue involves the use of planning models in addressing problems of discourse as well. Specifically, we need to use planning models to determine goals and plans of agents engaging in a dialogue as well as to model single or multiple speech acts.

The planning mechanism we propose to model both communicative and task-related actions (although in this paper the focus is only on the communicative actions) consists of the following:

(i) a formal language, which in our case is based on model logic, with a semantics that allows states in the world to be expressed in the language,

(ii) a goal or a set of goals, (iii) a set of actions; actions could be task-related or communicative actions as in a dialogue,

![](/api/attachments/7ACC93WW/fulltext/images/10a9bdf9e720804f23657c0c9a28334f21adc4163da023772898df41d6ce7efa.jpg)  
Fig. 1. Integrated Understanding System.

<table><tr><td>40</td><td>Red 17&quot; basic bicycles</td></tr><tr><td>80</td><td>Yellow 17&quot; basic bicycles</td></tr><tr><td>80</td><td>Black 17&quot; basic bicycles</td></tr><tr><td>60</td><td>Rear view mirrors</td></tr><tr><td>120</td><td>Standard seats</td></tr><tr><td>80</td><td>Racing seats</td></tr><tr><td>60</td><td>Standard handlebars</td></tr><tr><td>140</td><td>Racing handlebars</td></tr></table>

(iv) a set of beliefs about the world and about itself, expressed as axioms in the formal language,

(v) a planning process, which is nondeterministic in general.

One point that needs to be noted here is that the description of a dialogue in a natural language in terms of a planning mechanism is construed to be only a formal description of observable behavior. The actions, plans and goals are only formal constructs and there is no claim of psychological reality.

## 4. Importance of language considerations in manufacturing problems

It is not the purpose of this section to discuss solving complex manufacturing problems within the DSS framework. The importance of a DSS as a powerful mechanism to solve manufacturing problems has long been recognized. Here we shall illustrate with an example how language understanding can be effective in aiding the solution of the more fundamental problems, in this case from the manufacturing domain.

Consider the case of a user who is involved in the resource requirements planning (RRP) for manufacturing. RRP is a rough cut examination of manufacturing resource requirements. It is based on the same general logic as materials requirements planning (MRP) but uses more averaged data for material and labor or other resource planning. The aim of RRP is to provide approximate answers to such manufacturing questions about the next five years (or so) as to the availability of enough floor space for inventory or manufacturing equipment, enough machine capacity, enough manpower in the right crafts and at the needed skill levels, etc. RRP is intended to be a quick and simple process that answers 'what if' scenario questions. At this macro level, it is sufficient to have a planning bill of materials or a planning bill of labor for a product group as opposed to a single product or subassemblies that go into a product. Suppose the user is interested in knowing the RRP for an additional 200 units of 17" MX bicycles before deciding whether to manufacture the items or not. Let us say the planning bill of materials for the product group is given by fig. 2. Hence the planning bill of materials explosion would result in rough cut material (or part) requirements of

Note that RRP is performed without regard to the present work load or materials in the factory, since the time period involved is far greater than the time necessary to finish manufacturing the current work in process.

Now consider the following query posed by the user. 'Can you tell me what raw materials we need for 200 17" MX bicycles?' The first thing to point out is that a mere literal interpretation of the utterance is not enough. The system ought to realize that this is not a question that demands only a yes/no answer; rather, it is an indirect request for the planning bill of materials (or an indirect speech act). Hence one task of the integrated understanding system is to take utterances of the user literally and identify the linguistic action performed by the user using syntactic and semantic analysis; however, the system ought to go a step further (pragmatic analysis) and infer what the user meant rather than what he/she actually uttered. In order to do so, however, the system must recognize the plans and goals of the user by finding an inference path connecting what was said to an expected goal in the context. In the case of this query, the system may (or, probably ought to) realize that the user is trying to determine the RRP for 200 additional bicycles before deciding whether to order the manufacturing of those items. A simple outline of the plan is given in fig. 3. A possible goal of the user as assumed by the system is to determine the feasibility of manufacturing the additional items. Reading the plan from the bottom to the top, we see the following connections. An effect of the user's request is that the system carries out computations to determine the material requirements and then informs the user of the same. This knowledge is necessary for the user to achieve the goal of determining the RRP. But the system also determines that there are other components to achieving the goal of the RRP. The user needs to know about the availability of machine capacity as well as the availability of labor.

<table><tr><td colspan="3">Basic 17&quot; Bicycle</td><td>Rear View</td><td colspan="2">Seat</td><td colspan="2">Handlebars</td></tr><tr><td>Red</td><td>Yellow</td><td>Black</td><td>Mirror</td><td>Standard</td><td>Racing</td><td>Standard</td><td>Racing</td></tr><tr><td>20%</td><td>40%</td><td>40%</td><td>30%</td><td>60%</td><td>40%</td><td>30%</td><td>70%</td></tr></table>

Fig. 2. A Planning Bill of Materials For The 17" MX Bicycle Group.

The system then examines the user's intended plan (fig. 3) and finds three obstacles. The first was directly on the path outlined above: the user needs to know the bill of materials. The other two follow from the general knowledge about the structure of plans: the user also needs to know the machine capacity and the labor available for the task. The systems's response, therefore, could include not only the information about the bill of materials, but also the available machine capacity and labor. Suppose that in this case there was enough machine capacity but not enough manpower to produce the additional items. In that case, the system's response would include the bill of materials for 200 bicycles as well as a reminder that additional manpower would be needed if the task were to be carried out. In an integrated understanding systems, this is how a helpful response can be generated. The most important point here is that the user's intended plan is recognized starting from the literal interpretation of the user's query. Another important point to note is that the problem solving process (computation of material requirements, machine capacity, etc.) is also carried out simultaneously without explicitly being requested by the user.

The example we have cited involves only a single utterance. In order to be effective, the system also ought to understand multiple sentences or dialogue. Consider, for example, the query 'Can you tell me what raw materials we need for 200 17" MX bicycles? And what machine capacity?' The first of these utterances was analyzed earlier. What is the user's goal in the second utterance? From one viewpoint, it is to get additional information to determine the RRP of the task implied in the first utterance. From another viewpoint, however, the important goal is to recognize that this sentence is intended to be an extension on the previous request. The goals at this level of analysis are only indirectly related to the goal of determining the bill of materials or the overall RRP. Thus there are at best two levels of analysis that must be considered. One is the task level, which includes goals such as determining bill of materials, available machine capacity, etc. The other is the communication level, which includes such goals as introducing a topic, clarifying or elaborating on a previous request, modifying the current topic, etc. In our case, the topics generally concern some task in the manufacturing domain that the user needs assistance in performing. Some of the interesting aspects of the system from a language point of view include the generation of responses that provide more information than required (as in the case of the query referred to in fig. 3) but not something that is not useful to the user, the generation of responses to sentence fragments (as in the case of the second part of the previous query) and, of course, the analysis of indirect speech acts.

![](/api/attachments/7ACC93WW/fulltext/images/5be2a84a1ee9123a700a5ff699bd5853c4269a8d1eb2951a00a41772074625a7.jpg)  
Fig. 3. A Simple Plan Recognized From The Query.

## 5. Representation of belief, knowledge and wants

Logic-based systems have been proposed [3,6,8] to deal with natural language processing problems. The usefulness of each of these systems is limited to a great extent because there is no mechanism here by which one can represent the personal idiosyncracies, knowledge and desires of the user. Representation of beliefs, knowledge, etc. in the framework of modal logic have been proposed by Hintikka [5] and have been used in language processing by Perrault and others [1,9].

There is a fundamental difference between systems based on modal logic and those based on classical first-order logic. In classical logic, the focus is on truth whereas in belief systems, the focus is on acceptability. In other words, they reflect different analyses of understanding. On one analysis, to understand a sentence is to know what makes it true. On the other, it is to know what would make it acceptable. In a belief system it is not necessary to believe that the sentences involved are objectively true or false; instead of being concerned with what is true or false, the belief system should describe language in terms of a person's beliefs about the world. Acceptability is, therefore, viewed as a more primitive notion than truth.

The representation scheme for beliefs etc. is based on the earlier work of Hintikka [5] and Perrault [1,9]. Belief is represented as a model operator $B_{A}(P)$ , where P is the proposition believed and A is the believing agent. The model operator B is supposed to satisfy the following axioms:

(i) $B_{A}$ (all theorems of first-order predicate calculus),

(ii) $B_{A}(\mathbb{P})\to B_{A}(B_{A}(P)),$

(iii) $B_A(P)\vee B_A(Q)\to B_A(P\vee Q),$

(iv) $B_A(P) \wedge B_A(Q) \to B_A(P \wedge Q)$ ,

(v) $B_{A}(\sim P)\to \sim B_{A}(P),$

(vi) $(B_A(P\to Q))\wedge B_A(P)\to B_A(Q),$

(vii) $(\exists X)B_{A}(P(X))\to B_{A}(\exists XP(X)).$

Similarly, want is also represented as a model operator $W_{A}(P)$ (which denotes that agent A wants P) or as $W_{A}(\mathrm{ACT}(B))$ (which denotes that agent A wants B to do ACT). The model operator W is supposed to satisfy the following axioms:

$$
\begin{array}{l} \text {(i)} \mathrm {W_ {A} (P) \equiv B_ {A} W_ {A} (P)} \\ \text {(ii)} \mathrm {W_ {A} (P\land Q) \equiv W_ {A} (P)\land W_ {A} (Q)} \end{array}
$$

Finally, following Perrault and Allen [10], we use the work ‘knowing’ in three different senses:

(i) knowing that a proposition $P$ is true

$$
K _ {A} (P) \equiv P \wedge B _ {A} (P),
$$

however, the statement 'A does not know P' is represented as

$$
\sim K _ {A} (P) \equiv P \wedge \sim B _ {A} (P),
$$

(ii) knowing whether a proposition $P$ is true $KW_{A}(P) \equiv K_{A}(P) \vee K_{A}(\sim P)$ ,

(iii) knowing what the referent of a description is $KR_{A}(P(X)) \equiv (\exists X)((\forall Z)P(Z) \equiv Y = Z) \land B_{A}((\forall Z)P(Z) \equiv Y = Z),$ e.g., agent A knows the cost of an ITEM (i.e., $KR_{A}(\text{COST(ITEM)})$ if ITEM has a unique cost Y, and if agent A believes Y to be the
unique cost of ITEM.

An important point to note here is that unlike in classical logic, some operators in belief systems are intensional rather than extensional. For example, the operator 'V' is extensional because the truth of $A \vee B$ depends only on the truth of $A$ or the truth of $B$ . No other properties matter. On the other hand, $B_A(P)$ is intensional because its truth value depends on the meaning of $P$ , not just its truth value.

The important issue that remains is the use of this representation scheme in enhancing the language understanding process. There are two important aspects from a planning point of view that we shall discuss here. As indicated in fig. 1, the task of the natural language parser is to take as input a natural language sentence and, using syntactic and semantic information, produce a literal interpretation of the output – an observed linguistic act or speech act. The first aspect deals with the modeling and analysis of speech acts that form the output of the natural language parser. The second aspect deals with the plan recognition problem, i.e., given a sequence of actions (communicative actions in this case) performed by the actor, the task is to infer the goal pursued by the actor and also to organize the action sequence in terms of a plan structure. These two aspects are briefly discussed in sections 6 and 7 respectively.

## 6. Modeling speech acts in a belief system

A speech act is an intentional action that has as parameters a speaker, a hearer, and a propositional content, and whose execution leads to the production of an utterance. As is common in planning mechanisms, actions can be grouped into families represented by action schemas. An action schema consists of a name, a set of parameters and sets of formulas in the following classes:

Preconditions: Conditions that should be true before the action can be executed.

Effects: Conditions that become true as a result of the execution of the action.

Body: A specification of the action at a more detailed level; the specification may involve a sequence of actions to be performed, or a set of new goals that must be achieved.

Our treatment of speech acts is based on the earlier work of Cohen and Perrault [1] and Perrault and Allen [9]. Although we are developing a large number of operators corresponding to linguistic actions performed in the manufacturing domain, for the purposes of discussion we shall present only a few in this paper. Some of the operators are given in fig. 4.

Consider, for example, the operator 'INFORM(S, H, P)' where the speaker informs the hearer of the proposition $P$ . The precondition of the operator is that the speaker $S$ himself/herself 'know' the proposition $P$ (i.e., $K_{S}(P)$ ) and the effect of the operator is that the hearer then 'knows' the proposition $P$ (i.e., $K_{H}(P)$ ). In order to achieve this desired effect, however, one needs to achieve the body (i.e., $B_{H}W_{S}(K_{H}(P))$ ) which states that the hearer believes that the speaker $S$ wants the hearer H to ‘know’ the proposition P. It may be interesting that the body can be achieved by applying the operator ‘DECIDE-TO-BELIEVE(AGT 1, AGT 2, P)’. Thus the task of an agent A informing the system S of a proposition P can be accomplished in the planning framework by the operators ‘INFORM(A, S, P)’ and ‘DECIDE-TO-BELIEVE(S, A, P)’. Similarly, the task of an agent A requesting the system S to perform a certain ACT can be accomplished by the operators ‘REQUEST(A, S, ACT)’ and ‘CAUSE-TO-WANTS(S, A, ACT)’.

<table><tr><td>INFORM (S, H, P)</td><td>DECIDE TO BELIEVE (AGT1, AGT 2, P)</td></tr><tr><td>PRE:  $K_S(P)$ </td><td>PRE:  $B_{\text{AGT1}} W_{\text{AGT2}} (K_{\text{AGT1}}(P))$ </td></tr><tr><td>EFFECT:  $K_H(P)$ </td><td>EFFECT:  $K_{\text{AGT1}}(P)$ </td></tr><tr><td>BODY:  $B_H W_S (K_H(P))$ </td><td></td></tr><tr><td>INFORMIF (S, H, P)</td><td> $\bar{I}NFORMREF (S, H, D(X))$ </td></tr><tr><td>PRF· $KW_S(P)$ </td><td>PRE:  $KR_S(D(X))$ </td></tr><tr><td>EFFECT:  $KW_H(P)$ </td><td>EFFECT:  $KR_H(D(X))$ </td></tr><tr><td>BODY:  $B_H W_S (KW_H(P))$ </td><td>BODY:  $B_H W_S (KR_H(_(X)))$ </td></tr><tr><td>REQUEST (S, H, ACT)</td><td>CAUSE TO WANT (AGT 1, AGT 2, P)</td></tr><tr><td>PRE:  $W_S (ACT(H))$ </td><td>PRE:  $B_{\text{AGT2}} B_{\text{AGT1}} W_{\text{AGT1}}(P)$ </td></tr><tr><td>EFFECT:  $W_H (ACT(H))$ </td><td>EFFECT:  $W_{\text{AGT2}}(P)$ </td></tr><tr><td>BODY:  $B_H W_S (ACT(H))$ </td><td></td></tr><tr><td>S. INFORM (S, H, F)</td><td>S. REQUEST (S, H, ACT)</td></tr><tr><td>EFFECT:  $B_H W_S (K_H(P))$ </td><td>EFFECT:  $B_H W_S (ACT(H))$ </td></tr></table>

Fig. 4. Some Speech Act Operators.

'INFORMIF(S, H, P)' is also an act of informing where the information for the propositional content is not known at the time of planning; however, it is assumed that P or its negation will become true. 'INFORMREF(S, H, D(X))' is an act of informing where the speaker S informs the hearer H of the description D(X) of X, e.g., price of an item given by PRICE(ITEM).

The speech acts that we have discussed so far are defined by the intentions of the speaker and are carried out by executing some surface act. An essential condition for the performance of such acts is that the hearer recognize that the speaker intended to perform that act. However, in many cases, it may be ambiguous as to whether the speech act was a direct one or an indirect one. For example, the speech act in the question 'Do you know the departure time of flight #203?' can be viewed as an indirect one where the response expected by the speaker was not a yes or a no but rather the act of informing by the hearer as to the departure time of the flight in question. On the other hand, it is possible to view the same question as a direct speech act with a yes or a no response; a plausible context where that could be true would be the situation where the speaker was hoping that the hearer knew the departure time so that he/she (i.e., the hearer) could be at the airport on time. To avoid such ambiguities, we use surface speech acts that correspond directly to the form of the utterance. Hence, as shown in the remaining operators in fig. 4, an imperative mood sentence is always a surface request act S.RE-QUEST (S, H, ACT) whether it is interpreted directly or not whereas an indicative mood sentence is always a surface inform act S.IN-FORM (S, H, P).

Merely having a repertoire of speech act operators is not enough to interpret natural language utterances. What we also need is an inferencing mechanism whereby the system can consider a sequence of speech acts performed by the user and infer the goal or goals implicitly pursued by the user. In this section, we intend to illustrate how inference rules can be used to make plausible inferences from individual speech acts. Instead of presenting the entire set of inference rules, we will only state a few for the purpose of illustration. The inference rules are of the form

$$
B _ {S} W _ {A} (P) \stackrel {I} {\rightarrow} B _ {S} W _ {A} (Q),
$$

which states that if the system S believes that agent A's plan contains P, then S may infer that A's plan also contains Q. A few such rules are given in fig. 5. For example, the action-effect rule states that if E is an effect of ACT, then if the system S believes that agent A want ACT to be performed, the system S may infer that the agent A wants E to be true. In the remainder of this section, we give a few examples to illustrate how the speech act operators could be used in conjunction with the plan inference rules to interpret natural language utterances. The examples are given in fig. 6, fig. 7 and fig. 8.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
PRECONDITION-ACTION RULE (PA)
 $B_{S}W_{A}(P) \stackrel{I}{\Rightarrow} B_{S}W_{A}(ACT)$ 
if P is a precondition of ACT
ACTION-EFFECT RULE (AE)
 $B_{S}W_{A}(ACT) \stackrel{I}{\Rightarrow} B_{S}W_{A}(E)$ 
if E is an effect of ACT
BODY-ACTION RULE (BA)
 $B_{S}W_{A}(B) \stackrel{I}{\Rightarrow} B_{S}W_{A}(ACT)$ 
if B is part of the body of ACT
WANT-ACTION RULE (WA)
 $B_{S}W_{A}(W_{N}(ACT)) \stackrel{I}{\Rightarrow} B_{S}W_{A}(ACT)$ 
if N is the agent of ACT
KNOW-POSITIVE RULE (KP)
 $B_{S}W_{A}(KW_{A}(P)) \stackrel{I}{\Rightarrow} B_{S}W_{A}(P)$
</div>

Fig. 5. Some Plan Inference Rules.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
QUERY:
TELL ME THE PRICE OF A WIDGET
S. REQUEST (A, S, INFORMREF (S, A, PRICE (WIDGET)))
↓AE
$B_{S}W_{A}$ (INFORMREF (S, A, PRICE (WIDGET)))
↓BA
REQUEST (A, S, INFORMREF (S, A, PRICE (WIDGET)))
↓AE
$W_{S}$ (INFORMREF (S, A, PRICE (WIDGET)))
↓WA
INFORMREF (S, A, PRICE (WIDGET))
↓AE
$KR_{A}$ PRICE (WIDGET))
</div>

Fig. 6. Interpretation of Query #1.

Consider, for example, the query in fig. 6: 'Tell me the price of a widget'. To begin with, the utterance is viewed as a surface request act by the agent A of the system S to inform the agent A the price of a widget. Then, by applying the action-effect rule, it can be inferred that the system S believes that the agent A wants the system S to inform the price of the widget. Next, by applying the body-action rule, it can be inferred that the speech act is a request by agent A of the system S to perform the act of informing the agent A the price of a widget. As shown in fig. 6, other inference rules can be applied until the agent A 'knows' the price of the widget (i.e., until the assertion $KR_{A}$ (PRICE(WIDGET)) is true). Variations of the above query can be handled similarly as shown in fig. 7 and fig. 8. It is important to note that the latter two queries are examples of indirect speech acts (unlike the one in fig. 6) which results eventually in the same outcome, namely, $KR_A$ (PRICE(WIDGET)).

Fig. 8. Interpretation of Query #3.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
QUERY:
DO YOU KNOW THE PRICE OF A WIDGET?
S. REQUEST (A, S, INFORMIF (S, A,  $KR_{S}$  (PRICE (WIDGET))
↓AE
 $B_{S}W_{A}$  (INFORMIF (S, A,  $KR_{S}$  (PRICE (WIDGET))))
 $B_{S}W_{A}$  ( $KW_{A}$  ( $KR_{S}$  (PRICE (WIDGET))))
↓KP
 $B_{S}W_{A}$  ( $KR_{S}$  (PRICE (WIDGET))))
↓PA
 $B_{S}W_{A}$  (INFORMREF (S, A, PRICE (WIDGET)))
↓BA
REQUEST (A, S, INFORMREF (S, A, PRICE (WIDGET)))
↓AE
 $W_{S}$  (INFORMREF (S, A, PRICE (WIDGET)))
↓WA
INFORMREF (S, A, PRICE (WIDGET))
↓AE
 $KR_{A}$  (PRICE (WIDGET))
</div>

Fig. 7. Interpretation of Query #2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
QUERY:
CAN YOU TELL ME THE PRICE OF A WIDGET?
S. REQUEST (A, S, INFORMIF (S, A, CANDO (S, INFORMREF (S, A, PRICE) (WIDGET)))) ↓AE
B$_{S}$W$_{A}$ (INFORMIF (S, A, CANDO (S, INFORMREF (S, A, PRICE (WIDGET)))) ↓AE
B$_{S}$W$_{A}$ (KW$_{A}$ (CANDO (S, INFORMREF (S, A, PRICE (WIDGET)))) ↓KP
B$_{S}$W$_{A}$ (CANDO (S, INFORMREF (S, A, PRICE (WIDGET)))) ↓PA
B$_{S}$W$_{A}$ (INFORMREF (S, A, PRICE (WIDGET))) ↓BA
REQUEST (A, S, INFORMREF (S, A, PRICE (WIDGET))) ↓AE
W$_{S}$ (INFORMREF (S, A, PRICE (WIDGET))) ↓WA
INFORMREF (S, A, PRICE (WIDGET)) ↓AE
KR$_{A}$ (PRICE WIDGET))
</div>

In any language understanding system of the type being discussed here, there will typically be a large number of plan inference rules and, more often than not, more than one rule will be applicable in any given situation. We are currently developing heuristics that will help guide the search for appropriate rules applicable in any stage of the interpretation process. However, we shall not discuss the issue any further in this paper.

## 7. Other research issues

So far we have discussed the issue of representing beliefs and wants of agents, and using them to model speech act operators which in turn can be used to interpret natural language utterances. However, as is apparent from fig. 1, the language component of a DSS contains many other features that have been discussed so far. An important aspect that we are currently dealing with is the plan recognition problem. A complete discussion of the issue is beyond the scope of the paper and therefore we shall only provide a brief overview of the research questions that must be addresses.

The problem of plan recognition is to take as input a sequence of actions performed by an actor and to infer the goal pursued by the actor and also to organize the action sequence in terms of a plan structure. In dealing with language, the input sequence of actions results from the natural language parse in the form of ‘observed linguistic acts’ (see fig. 1). The features crucial to the plan recognition process include the ability to form hypotheses about the possible intent behind the user’s questions based upon an initial segment of the input sentence as well as background information about the user, the ability to maintain a description of the state of the world and the user’s beliefs, the ability to recognize the next observed speech act as one of the expected actions and, most importantly, the ability to revise and reformulate the hypotheses when the observed action deviates from expectations.

![](/api/attachments/7ACC93WW/fulltext/images/44abc64c726c3a4e3af263826865676f1dbc0537098527277b78683d0077315f.jpg)  
Fig. 9. Knowledge Representation in the Plan Recognition Process.

Central to the plan recognition process is an effective knowledge representation scheme. The scheme we propose is given in fig. 9. The world model consists of the assertions that the system believes to be true about the current physical situation. The user model represents the system's model of the user's beliefs and wants. The plan model consists of those plan structures that are active hypotheses for the actions being modeled in the user model and the world model. In terms of our earlier notations, the assertions in the world model are of the form of a proposition P; the assertions in the user model could be stated as any of the following: $P, B_{A}(P), K_{A}(P), KW_{A}(P), KR_{A}(D(X))$ . The world domain, the user domain and the plan domain define the set of notions that may be used to represent the input sentence as a set of actions as well as represent the various states of the hypothesis about the intentions behind the user's utterances.

To summarize, the essence of the plan recognition problem is to develop a plan structure (described as expectation structure in fig. 9) to achieve a specified goal that may be attributed to the user. The hypothesized plan structure will be used by the system to guide the interpretation of the input speech acts. The effectiveness of this problem will depend on how well the system can revise the expectation structure when the expectations are not matched by the observations.

## 8. Conclusion

In this paper, we have examined the importance of representing belief, knowledge, and wants in decision support systems. We have also examined how classical first order logic can be extended to incorporate notions of belief, knowledge and wants of users and the knowledge about the problem domain. Implications of this extended logic (modal logic) include: (i) it is possible to specify sentences (that could use notions of belief, knowledge etc.) that describe possible worlds, (ii) consistency and defensibility of the set of sentences that include the notion of belief, (iii) consistency and defensibility of the set of sentences that include the notion of knowledge, (iv) consistency and defensibility of the set of sentences that include both the notions of belief and knowledge. This extended logic is then used to develop a planning framework to model the (communicative) actions of the speaker-hearer system. Finally, this planning framework is then used to interpret natural language sentences.

## References

[1] Cohen, Philip R. and C. Rayond Perrault, Elements of a Plan-Based Theory of Speech Acts Cognitive Science 3 (1979) 177–212.

[2] De, Suranjan and Andrew B. Whinston, A Framework for Integrated Problem Solving in Manufacturing, IIE Transactions 18, no. 3 (1986) 286–297.

[3] De, Suranjan and Andrew B. Whinston, Natural Language Query Processing in a Temporal Database, Data and Knowledge Engineering 1 (1985) 3–15.

[4] De, Suranjan, Shuh-Shen Pan and Andrew B. Whinston, Temporal Semantics and Natural Language Processing in a Decision Support System, forthcoming in: Information Systems 12, No. 1 (1987).

[5] Hintikka, Jaakko, Knowledge and Belief: An Introduction to the Logic of the Two Notions (Cornell University Press, Ithaca, New York, 1962).

[6] McCord, Michael C., Using Slots and Modifiers in Logic Grammars for Natural Language, Artificial Intelligence 18 (1982) 327–367.

[7] Nilsson, Nils J., Principles of Artificial Intelligence (Tioga Publishing Company, 1980).

[8] Pereira, Fernanco C.N. and David H.D. Warren, Definite Clause Grammar for Language Analysis - A Survey of the Formalism and a Comparison With Augmented Transition Networks, Artificial Intelligence 13 (1980) 231–278.

[9] Perrault, C. Raymond and James F. Allen, A Plan-Based Analysis of Indirect Speech Acts, American Journal of Computational Linguistic 6, No. 3–4, July–Dec. (1980) 167–182.

[10] Samuel, A.L., Some Studies in Machine Learning Using the Game of Checkers, in: E.A. Feigenbaum and J. Feldman, eds., Computers and Thought (McGraw-Hill, New York, 1963).

[11] Shortliffe, E.H., Computer-based Medical Consultations: MYCIN (American Elsevier, New York, 1976).
