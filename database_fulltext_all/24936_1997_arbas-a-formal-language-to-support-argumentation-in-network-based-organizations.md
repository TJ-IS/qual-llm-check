---
otero_id: 24936
otero_key: "YPG6S7B4"
title: "ARBAS: A Formal Language to Support Argumentation in Network-Based Organizations"
authors: "Tung X. Bui; François Bodart; Pai-Chun Ma"
year: "1997"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1997.11518181"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# ARBAS: A Formal Language to Support Argumentation in Network-Based Organizations

Tung X. Bui, François Bodart & Pai-Chun Ma

To cite this article: Tung X. Bui, François Bodart & Pai-Chun Ma (1997) ARBAS: A Formal Language to Support Argumentation in Network-Based Organizations, Journal of Management Information Systems, 14:3, 223-237, DOI: 10.1080/07421222.1997.11518181

To link to this article: http://dx.doi.org/10.1080/07421222.1997.11518181

![](/api/attachments/YPG6S7B4/fulltext/images/498a1416bfc742807eaa94cb1980697d3f0e7e08d90a814e020973547a49ec91.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/YPG6S7B4/fulltext/images/2fe944e76c37b7638b1bd393575eb30d9b107785b077fa9253fefef6721ceff1.jpg)

Submit your article to this journal ↗

![](/api/attachments/YPG6S7B4/fulltext/images/064e25fb359adfa5fd5c6ae34ca75801f6ead2f5832cf623d4404158dac79d33.jpg)

View related articles ↗

![](/api/attachments/YPG6S7B4/fulltext/images/16341ee738ee9522dbda61903d32a4a71ae24defc4953800d7bcd02f11dcc7da.jpg)

Citing articles: 5 View citing articles ↗

# ARBAS: A Formal Language to Support Argumentation in Network-Based Organizations

TUNG X. BUI, FRANÇOIS BODART, AND PAI-CHUN MA

TUNG X. BUI is currently Matson Navigation Co. Professor of Global Business and Decision Sciences at the University of Hawaii at Manoa, Honolulu. He holds a Ph.D. in information systems from New York University and a doctorate in managerial economics from the University of Fribourg, Switzerland. Dr. Bui was on the faculty at New York University, the Universities of Fribourg and Lausanne, Switzerland, the University of Quebec, Montreal, Canada, and the Hong Kong University of Science and Technology. His current research focuses on electronic commerce, effective implementation of information systems in large organizations, and in collaborative technology, including group decision and negotiation support systems.

FRANÇOIS BODART is Professor of Computer Science and department head of the computer and information systems curriculum at the Facultés Universitaires Notre-Dame de la Paix, Namur, Belgium. Dr. Bodart currently serves as a ministerial advisor on information technology. His research interests focus on database applications and on effective implementation of information systems in organizations.

PAI-CHUN MA is an Associate Professor at Baruch College, City University of New York. Prior to joining Baruch College, he was on the faculty at the University of Delaware, Newark, and the Hong Kong University of Science and Technology. Dr. Ma earned his doctorate in information systems from New York University. His research interests include model management systems for mathematical programs, concept-based information retrieval of financial databases, negotiation support, and metagraph applications.

ABSTRACT: This paper proposes a formal language to support and document argumentation, claims, decision and negotiation, and coordination in network-based organizations. The purpose of the language, once implemented in the organization's Intranet, is to promote communication using structured arguments, claims and justified decisions and to preserve this information as corporate memory. We contend that organization effectiveness can be achieved by continuous exchange of information, arguments, and joint agreements on actions with appropriate knowledge of the organizational decision-making context. As a mechanism for group decision and negotiation support and as an organizational repository, the proposed language is constructed based on supporting discussions that focus on the relationship between actions and the resources required to implement these actions.

Acknowledgment: This research was partially funded by the 1996 RGC Earmarked Grant, HKUST, Hong Kong, and by the University Faculties of Notre-Dame, Namur, Belgium.

KEY WORDS AND PHRASES: argumentation theory, group decision and negotiation support, organizational memory.

COMMUNICATION AMONG TEAM MEMBERS HAS BEEN WIDELY RECOGNIZED as a critical ingredient for effective organizational decision making and as a way to alleviate coordination problems. Teamwork can be viewed as the conveyance of commitments between members to perform a task $[13, 24]$ . Organizational members generate and exchange ideas, examine their validity and feasibility, assess their consequences, agree on a final action to take, and coordinate activities to implement the action. However, effective communication is difficult to achieve, while poor communication can obstruct team performance $[15]$ . Another difficulty inherent in effective teamwork and communication is the lack of corporate knowledge that is crucial to support problem definition, problem analysis, argumentation, and claims. In particular, when teamwork is driven by highly dynamic and often emotional negotiation, arguments are often convoluted, vague, or incomplete, leading to less than optimal action outcomes.

This paper proposes a formal language to support argumentation and decision making and to preserve the argumentation process as organizational memory. We first present argumentation as a basis for organizational decision making and then formally present the rationale and principles of an action-resource based argumentation language. We next describe ARBAS formalism and its computerized version. The use of the language is demonstrated with a case study and at the end of the paper we place the contributions of our work in the context of related research.

## Argumentation as a Basis for Organizational Decision Making

THE LITERATURE ON ORGANIZATIONAL DECISION MAKING IS UNANIMOUS in recognizing that a successful meeting is one that encourages divergence and radical thinking to ensure that all the possible alternatives are explored to enhance the chance of converging to the best solution. This search for a common solution is often the result of a continuous exchange of arguments and counterarguments among participants [1, 19, 35]. According to Flores et al. (for example, see [10, 25]), communication can be broken down into four primitive acts: opening (i.e., suggesting an action items), negotiating, performing, and assessing. This approach has been illustrated in a general business context by Scherr [33] to supplement tradition workflow analysis with accountabilities of involved parties. To help promote the exploration and discussion of ideas, Toulmin et al. [37, 38] suggest the use of an argumentation language as a structured means to convey arguments, reasons, evidence, or assumptions. Perhaps the best-known form of information exchange and reasoning is Hegel's [18] dialectical language in which the thesis is challenged by the antithesis until a synthesis is found. This synthesis would capture and integrate all the critical actions that emanate during discussion. The term "argumentation" refers to the act of making claims, backing them up with supporting evidence or reasoning, and criticizing or challenging those reasons [2]. Ramesh and Whinston [31] provide a comprehensive survey on work subsequent to Toulmin.

For the purposes of this research, an argument is typically composed of assumptions supported by fact(s) or reasoning from which conclusions are derived. Assumptions and reasoning are backed by established experience or underlying knowledge. In a highly dynamic and often emotional decision-making situation, arguments are often convoluted, vague, or incomplete. When an argument or a decision is vague, significant costs could be incurred by the additional effort required to ascertain the true meanings of the language or to reduce the risks of misinterpreting that language $[17]$ . Therefore, a concise and structured language might be desirable to promote reasoning, while controlling emotions $[2, 7, 36]$ .

Furthermore, a structured language supporting argumentation is expected to force parties to explicitly reveal underlying differences in opinions. An example of a simple argument structure is proposed by Toulmin [37]. The argument structure consists of three elements: a claim that is used to express an opinion or assumption; data that support the claim; and a warrant that justifies the logical relation between the claim and its supporting data. Binbasioglu and Jarke [5] use the construct opinion. According to Webster's dictionary, however, the word "opinion" connotes a loosely reasoned, ill-structured conclusion thought out yet open to dispute. Chang and Woo [10] propose another example of argument structure. In their protocol, a sentence is composed of two components: a function, which is a category of speech act; and a content, which represents the domain knowledge used for the argument. According to Ramesh and Whinston [31], argumentation centers on positions, and a challenged argument requires appropriate defense and response from the individuals asserting the position.

Finally, the argumentation language should also be able to apprehend the evolution of problem representations over time, where the actions and the accompanying justifications of the stakeholders are to be explicitly represented; hidden agendas can interfere with reaching consensus.

## An Operational View of Modeling Argumentation

## An Action-Resource Approach to Problem Representation and Problem Solving

A DECISION PROBLEM CAN BE SEEN AS ONE that requires the decision maker to identify what actions to take and what resources are affected by these actions, given the restrictions (constraints) of the problem at hand. Actions necessary for solving a defined problem and the resources involved relate to each other as follows: Resources are generated or consumed as a result of actions taken, or conversely, actions require input resources and/or generate output resources.

We define the action and the resources that are input to the action and/or resources generated as output of the action as a unit and refer to that unit as an activity. In general, the activity is composed of an action that may take many resources as input and/or may generate many output resources. For representation purposes, the activity described by an activity triplet consists of:

## input resources | action | output resources.

The activity triplet can be viewed as a “primitive” process component. An activity triplet can represent a portfolio of more than one primitive action. It is important to relate resources to actions under argumentation, on which positions are taken. Although there are quite a variety of possible ways to link resources to actions, probing the impacts of a proposed action on resources increases decision makers’ awareness of the relevance of that action. More important, the irrelevance of certain alternate actions, the idea of which appears appealing, may yet turn out to be infeasible $[8]$ .

## Decision-Making Dynamics, Problem Evolution, and Traceability

An activity can lead to another activity, thus supporting complex problem definitions and redefinitions [8]. Borchardt [6] suggests that new alternatives can be generated to analyze challenged propositions in terms of benefits and burdens, issues and interests: Who is to be benefited or burdened? What are to be the benefits or burdens? When are they to begin and terminate? Where are they to be in effect? How—organizationally and procedurally—are they to be effected? Why is enactment of the proposal in the organization’s interest? Sebenius [34] argues that evaluating current alternatives in the search for new ones helps set the limits of negotiation. Any new proposed action should not be convoluted but, rather, should be convincing enough to gain acceptance from others. In this detailed search for alternate solutions with its strong focus on evaluation, chances for concession/convergence are increased [40].

The action-resource representation supports evolution of problem representation by chaining the activity triplets over time. The chained representation documents the dynamics of activities (or decision processes) during the course of negotiation. As the problem evolves, new (proposed) activities emerge to replace the old ones, and exchanged views on the activities give rise to new ones. In other words, the outcome of an activity can lead to another one, or a new activity can be introduced by the negotiators to reflect their (new) objectives and constraints.

Thus, the dynamics of decision making can be traced by navigating through the chain of activities that occurred during the project development process. Involved parties could navigate along the action chain and search for new solutions, until an action-resource triplet satisfies all parties.

## Toward a Formal and Operable Language for Dialectic and Evolutive Argumentation

We use the word “argumentation” in a broad context as a means for communication, discussion, evaluation, proposition, and decision. Keough and Lake [22] note that arguments, as a discourse for negotiation, serve a distinctive instrumental function in that they are used for persuasion, information exchange, issue definition, and consensus seeking. The structuring of such a discourse can be represented as a “view” to support argumentation. We advocate the use of the word “view” as a general frame to include opinion, sentiment, belief, conviction, and persuasion, where individuals are able to substantiate their views by relating them to the relevant action. We adopt the theoretical framework proposed by Jackson and Jacobs [20], who posit the use of arguments as a conversational mode to support collaborative activities. An argument is not just a monologic process in which the “speaker” merely provides some reasons for his or her claims. Rather, it emerges when a proposed action is regarded as undesirable and further conversations and propositions are required.

Syntactically, a view can take the form of opposition, agreement, or no-opinion (neutrality). Justification can be supportive or contradictory and would relate the view to goals, constraints, facts, or assumptions. Conversely, an assumption has the potential to be factual, but there is a certain amount of doubt (i.e., problematic fact). There is always a chance of switching back and forth between the class of assumptions and that of facts. When a challenged assumption cannot be defended, the problem components based on that assumption also lose support, and the problem structure must be modified accordingly [29].

## ARBAS—A Language for Supporting Action-Resource-Based Argumentation

WE DEFINE A LANGUAGE TO SUPPORT ARGUMENTATION with the following grammatical specifications: The lexicon seeks to provide a vocabulary for the argumentation discourse. Based on the lexicon specified, a syntax must be defined to derive a compound morphology of the argument. This refers to the grammar that deals with combinations of simple words. While the grammar looks at the correctness of the sentences, semantic constraints are used to impose a decision-making structure on the argumentation process. The following describes ARBAS formalism.

\- Lexicography: An argument can be composed of a small lexicon uniquely composed of words that are necessary for an activity-resource-based discussion. We adopt a limited set of vocabulary to avoid convoluted arguments that seeks to represent the negotiators' ultimate position.

Given an action to be jointly accomplished (Action\_Name) and resources to be used in accomplishing it (Resource\_Name), each of the team members (View\_Owner) expresses his or her position (View\_Position) with personal inflection (View\_Intonation). The position is justified by a discourse (View\_Justification) with arguments on the possible impacts of the action being discussed on the resources (Resource\_Name; Resource\_Type). Discussion on the driven resources is implicitly related to the objectives of the task at hand, and explicitly on the amount of resources required for the tasks (Resource\_Quantity, Resource-Limit).

The lexicon notation is given as follows:

View\_Owner: $Z = \{z \mid z \text{ is a name of the team member}\}$

$$
\text { Activity\_Triplet: } A = \{R N, R T | X | R N ^ {\prime}, R T ^ {\prime} \}
$$

Action\_Object: $O = \{o \mid o \text{ is an object used to describe the action}\}$

Action\_Name: $X = \{x(o) \mid x$ is a name of the action}

Resource\_Name: $RN = \{rn \mid rn \text{ is a resource name}\}$

Resource\_Type: $RT = \{\text{Input},\text{Output}\}$

Resource\_Limit: $RL = \{r, l \mid r \geq 0; l \text{ is a resource limit } \{\text{upper, lower}\} \}$

View\_Intonation: $I = \{\text{Sentiment, Opinion, Belief, Conviction, Persuasion}\}$

View\_Position: $P = \{\text{Support, Oppose, Don't Care}\}$

View\_Justification: $J = \{ n \mid n \text{ is a free\_format\_argumentation based on goals, constraints, facts or assumptions}\}$

Proposed\_Move: $M = \{\text{Drop, Implement, Modify, Other}\}$

Time\_Stamp: $T = \{t \mid t \text{ is a time stamp that covers all activities that occur between the start and the end of the process}\}$

\- Syntax: An argument can be composed by following a simple set of rules:

By combining words, a "view" can be derived.

When “a decision maker expresses his/her view on the resource(s) related to the task at hand,” a “View\_On\_Resource” can be defined as follows:

$$
V _ {\text { On - Resource }} (Z, R N, R T, R L)
$$

In the same manner, a "View\_On\_Action" can be composed to describe the situation in which "an owner, with his/her resource in mind, propose an action at time $t$ ":

$$
V _ {\text { On - Action }} (V _ {\text { On - Resource }}, A, T)
$$

The position on the view and its intonation (i.e., inflectional morphology) can be interpreted using the words I and P:

$$
V _ {\text { Position }} (V _ {\text { On - Action }}, I, P)
$$

A recommended action ("What\_move") can be specified using the constructs M and J which suggests an appropriate activity:

$$
V _ {\text {What - move}} (V _ {\text {Position}}, M, J)
$$

\- Semantic constraints: Constraints can be formulated to provide a minimum of semantic correctness to the argumentation language:

—Argumentation logic: This constraint implies that a position, P, should be followed by a logical move, M:

$$
\begin{array}{r l} S = \{(p, m) | (\text { Support,Implement }), (\text { Support,Modify }), & \\ (\text { Oppose,Drop }), (\text { Oppose,Modify }), (\text { Oppose,Other }), & \\ (\text { Don't   Care }, m ^ {*}) \} \end{array}
$$

where S is a constraint to validate the logic of argumentation, and $S \in (P \otimes M)$ ; $m^{*}$ is a wild card. This logic also represents a transition for creating a new action when $m = \{Modify, Other\}$ .

—Operative constraints: A simple transition rule can be defined to assure argumentation continuity. A new action, x, at time $t+1$ will be proposed when, at time $t, s_{t} \in S^{v}$ :

$$
\begin{array}{r l} \exists x _ {t + 1}, \in X, s _ {t} \in S ^ {\prime} = & \{(p, m) | (\text { Support }, \text { Modify }), \\ & (\text { Oppose }, \text { Modify }), (\text { Oppose }, \text { Other }) \} \end{array}
$$

Argumentation and generation of a new action x triggered by a move, m, could theoretically perpetuate with no convergence in sight. An operative constraint can be imposed by setting a time limit to terminate argumentation:

$$
\exists V (t), t \leq t ^ {\prime},
$$

where $t' \in T$ , $t'$ is a time threshold.

Another termination can be set based on the maximum number of actions:

$$
\exists X, \delta (X) \leq c ^ {\prime},
$$

where $\delta$ is a cardinality function about a set, and $c'$ is an action threshold expressed as a positive integer.

The third type of termination, and indeed, the most desirable operative constraint, is defined by a consensus threshold. The threshold, $s'$ , is a value with which members feel satisfied.

$$
\exists x ^ {\prime} \in X, V (z, x ^ {\prime}, p, i),
$$

when $\Sigma(p, i)_z \geq s'$ is met for $\supset z \in Z$ .

The constraints described above are only illustrations of the use of the language for the organization to develop a context-sensitive argumentative reasoning and problem-solving formalism. New constraints can be formulated to satisfy the argumentation process and problem-solving needs of a particular organizational situation.

## A Computerized Version of ARBAS

ARBAS, AS A FORMAL LANGUAGE, HAS BEEN IMPLEMENTED to support on-line argumentation in a networked environment. The model presented below is an improved and networked version of an earlier work [4].

## The ARBAS Entity-Relationship Model

From a data modeling perspective, ARBAS can be represented by an entity-relationship model. As shown in figure 1, we emphasize four argumentation entities:

\- PROBLEM symbolizes the argumentation process to solve,

\- ACTOR is a person or an organization engaged in the process,

\- PROPOSITION is an action suggested by an actor for problem solving, and

\- ARGUMENT is a support, an attack, or a neutral idea submitted to reinforce, destroy, or maintain the validity of an argument or a proposition.

The first two argumentation entities are supplemented by organizational entities (shown in figure 1 by rectangles with rounded corners). The argumentation-organization relationships are defined as follows:

• PROBLEM-[EVENT, PROTOCOL, AGREEMENT, FEEDBACK]

\- ACTOR-[ORGANIZATIONAL OBJECTIVE, GOAL, CRITERIA, DEPARTEMENT]

The relations between entities are shown in figure 1. All the entities and relations are defined by a set of attributes (see [30] for more details). For illustration purposes, the attributes of ARGUMENT, PROPOSITION, and ORGANIZATIONAL OBJECTIVE are reproduced below:

ARGUMENT (argument\_title, argument\_description, creation\_date, deletion\_date, intonation, argument\_reference).

PROPOSITION (proposition\_title, proposition\_description, creation\_date, deletion\_date, intonation, proposition\_reference)

ORGANIZATIONAL OBJECTIVE (objective\_name, objective\_description, creation\_date).

## ARBAS Systems Functions

ARBAS provides a distributed platform that allows team workers to participate in a problem-solving setting without having to be physically present at a conference table. Temporal integration is assured with interactive queries searching for information about past negotiations. Involved members can navigate seamlessly through argumentation states and time-stamped propositions. ARBAS also provides pattern maintenance for its users. As an organizational repository, it provides historical information regarding the members of the organization. The ability to search past history helps the negotiators better understand the culture of the organization(s) with which they are dealing.

![](/api/attachments/YPG6S7B4/fulltext/images/19841bcadd7809d81a09302a8c27a7f45e2062e4a1693ab133ad24e183df60f7.jpg)  
Figure 1. An Entity-Relationship Model for the ARBAS Language

At any phase of an argumentation process, users can align their actions with the objectives and goals of the organization they represent. Organizational learning and adaptation are supported by temporal visualization of sequential problem representation. Members can study the evolution of problems and perform comparative analysis across antagonists.

## Implementation

A prototype of ARBAS has been implemented on a Microsoft Windows NT server using an object-oriented language (Delphi version 2.0). At any point in time, participants to an argumentation session can announce a new problem, generate propositions, specify their preferences, formulate arguments, and interact with others. Negotiation protocols can be outlined and set to the system to dictate how a session must be conducted. A process ends when one of the following conditions is met:

\- Consensus is found.

• Agreement is reached by vote.

\- Allowed time has elapsed.

## An Example: The U.S.—Canada Softwood Lumber Dispute

WE USE A WELL-DOCUMENTED CASE STUDY DESCRIBED in Fang et al. [14] and show how ARBAS could have been used to support and represent the dispute and its resolution. For the sake of clarity, the case study is briefly reproduced below.

The U.S.-Canada dispute over the import of softwood to the United States started in May 1986 and ended December 30, 1986. In 1986, the U.S. lumber industry suffered a significant decline in the softwood lumber market. Meanwhile, Canadian wood cutters had been able to export US\$2 billion/year of softwood lumber to the United States. The U.S. wood cutters argued that the reason that Canada enjoyed 30 percent of their market was because the Canadian lumber industry benefited from low stumpage fees. In May 19, 1986, they formed the American Coalition for Fair Trade (CFT) and formally petitioned the U.S. Department of Commerce and the U.S. International Trade Commission (ITC) to rule on a charge of injury against alleged subsidized softwood lumber imports. CFT requested a duty of 27 percent on Canadian imports to offset the effect of alleged unfair trade.

Based on its own investigation, ITC concluded on June 26, 1986 that softwood lumber imports from Canada were harming the American lumber industry. Subsequently, the U.S. Department of Commerce decided to impose a 15 percent import duty effective January 1, 1987. A few days after the U.S. import duty decision, the Canada coalition, composed of various federal agencies, provincial officials, and lumber firms reunited to counter the U.S. decision. A number of actions were considered, including: campaign to protest the U.S. ruling, voluntary restrictions on softwood export to the United States, or increase stumpage fees to invalidate the CFT's petition. As a result of protracted argumentation between various Canadian stakeholders, Canada decided on December 30, 1986 to raise the stumpage fee. The decision was justified by the fact that (i) there was no way to challenge the ITC decisions, and (ii) if the price of Canadian softwood lumber has to be raised by tax, it is in Canada's interest to raise its own tax. This Canadian decision, just a day before the U.S. tax would take effect, caused the CFT to withdraw its petition.

The problem is entered in ARBAS by defining a new problem (involved actors: CFT, DOC, ITC, Canada; triggering events; initial positions of the declaring parties: propositions and arguments; information regarding organizational profile). Reaction from other parties can be regarded and traced on the problem-state transition window. Figure 2 shows a reaction from the Department of Commerce that counters CFT's proposition with a 15 percent tax imposition. The plus sign in the transition arrow indicates that DOC agrees with CFT's proposition. DOC, however, does have a new proposition. A transition arrow with a minus sign indicates that the current party does not agree with the proposition enumerated previously.

Figure 3 illustrates how ARBAS could be used as a tool for organizational memory. The query searches for all the problems in which either Canada or CFT has been involved so far. As seen on the folders of the query window, search can be performed using the following search keys: organizational objectives, subject or problem description, actors or involved parties, triggering events, actors' evaluation and feedback, termination or negotiation protocols, and time intervals.

Figure 4 shows a typical problem-proposition-argument hierarchy. The proposition window provides detailed information on a selected proposition. Each proposition is explicitly supported (represented in the argument window by rectangles) or criticized (represented in the argument window by circles) from different actors.

![](/api/attachments/YPG6S7B4/fulltext/images/c23e0b5430d3e9ef108c94b3be647e3d597d0fe9ca3f7349121d617ad47efea7.jpg)  
Figure 2. Problem-State Transition

## ARBAS: Related Work and Contributions

TOULMIN'S ARGUMENTATION STRUCTURING APPROACH HAS BEEN the inspiration for many recent formal systems that attempt to promote opinion exchange and joint decision making [9, 11, 12, 16, 21, 23, 25, 26, 27, 31, 35, 39].

Similar to our design objective, the systems cited above assume that agents have individual and common goals. Decision makers are encouraged to interact according to well-defined communication protocols. Opinions and ideas are solicited, consolidated, and supported by facts and arguments, so that counterproductive, rhetorical, or circular arguments are progressively eliminated, and a central and collectively agreeable issue eventually emerges. Conversely, ARBAS as a formal language is context-independent. Also, the representation languages of the cited systems are not powerful and flexible enough to capture the dynamics of negotiation. The dialogue management is not sufficient to guide participants to take actions (either pro-actively or reactively) and does not provide a framework for stakeholders to quickly estimate the impacts of proposed activities.

Most existing systems act as a representation or snapshot of the situation, thus lacking the ability to time the sequences of activities. Our representation language allows involved parties to trace various routes back and forth, thus allowing simulation, search for new alternatives, and backtracking.

![](/api/attachments/YPG6S7B4/fulltext/images/d158e79eca27d9e649af211869d1724ed6cb90fcc850eb2439fc6e3b8d76e903.jpg)  
Figure 3. Queries to Support Context Search

From an operational viewpoint, ARBAS provides a number of unique contributions:

\- Negotiation support: Negotiation can be costly and counterproductive if poorly handled. Organizational effectiveness can be seriously compromised if teamworkers hide their disagreement and avoid confrontation. Supporting explicit negotiation tasks with a very simple yet powerful language to express user opinion effectively addresses this issue. ARBAS provides an innovative way of negotiating. Parties negotiate by taking into account the most essential viewpoint: the input and output resources that are linked to the proposed action.

\- Coordination: Since ARBAS is task-oriented, it facilitates coordination among coworkers. An opinion expressed by a member on a given action is a commitment, as the member is fully aware of the implications of his or her commitment for his or her resources.

\- Support for asynchronous working mode: Problems related to the availability of people for face-to-face meetings are well documented. ARBAS lets people organize their professional interaction at their own convenience. Operative constraints supply a means for imposing possible delays. For example, a member fails to return his input by the deadline at the end of the delay, other participants could assume that he or she does not care. ARBAS works as a way to synchronize the entire project without increasing project management workload.

\- Documentation as a means to preserve corporate memory: Documenting all activities of an organization during its lifetime is indeed a costly and tedious task. To allow the decision maker to focus on solving a task at hand, a secretary is usually assigned to take notes manually and to produce minutes of the meetings. The quality of the documentation (e.g., minutes of meetings) depends on the skills of the note taker. ARBAS provides an automated and structured means to record the discussion. The information can be retrieved by using Action to trace the past decisions and their rationale.

![](/api/attachments/YPG6S7B4/fulltext/images/5f1ceaa9afad345a6dd12ed2daf2284002dad453b375499a9fd4c9374e1d6dd5.jpg)  
Figure 4. Display of Problem-State Transitions, Propositions, and Arguments

## Conclusion

WE HAVE PROPOSED AN ARGUMENTATION LANGUAGE as a conversational medium for members of a networked organization. The language is designed as a formal means that can be used to promote communication and organizational decision making, and can be used as a computerized organizational repository. The decision-making process can be viewed as the identification of appropriate actions and resources, deliberation of organizational goals, and acknowledgment of constraints that might impede the consideration of certain actions.

A decision problem can be seen as one that requires the team members to decide what action to take and to identify what resources are affected by this action. From a communication angle, we view decision makers' interaction as a series of propositions and counterpropositions of different tasks related to the software development project. Proposals and counterproposals represent binding actions in which members are aware of the consequences of the proposed actions in terms of effort required to achieve the tasks and the benefits. We further regard team interaction as an iterative problem-solving process in which the task at hand is continuously defined and redefined until a satisfactory solution is found. When an activity is planned, agents can question or oppose its existence, support its implementation, request modification, or suggest alternative activities. Satisfaction among members implies that expected results (goals) as well as resources required to achieve the task are agreeable to all. In this context, we use the word “argumentation” to denote communication, discussion, evaluation, proposition, and decision.

We propose ARBAS as a structuring language that incorporates an argumentation scheme to present ideas that would likely stimulate focused discussions among the decision makers. We argue that using an action-resource approach, workers are forced to defend their interests and take actions, by making clear their views regarding a (binding) action or move. The explicit representation of the relationships among the problem components also makes it possible to identify situations of likely conflicts when more than one party wants to share the same resources or wants to set their desired levels. As such, the proposed approach could be used as an effective means for promoting collaborative work. Since the proposed approach imposes structure on the discourse of views, it can also be employed when consolidating individual views into a group's view (using a brainstorming technique, for example).

## REFERENCES

1. Axelrod, R. Argumentation in foreign policy settings: Britain in 1918, Munich in 1938, and Japan 1970. In Zartman (ed.), The Negotiation Process. Beverly Hills, CA: Sage, 1977.

2. Ballmer, T., and Brennenstuhl, W. Speech act classification: a study in the lexical analysis of English speech activity verbs. Berlin: Springer-Verlag, 1981.

3. Bazerman, M.H., and Carroll, J.S. Negotiator cognition. In Staw and Cummings (eds.), Research in Organizational Behavior. Greenwich, CT: JAI Press, 1987.

4. Binbasioglu, M.; Bui, T.; and Ma, P.-C. An action-resource language for negotiation support. Journal of Computer Information Systems (Summer 1997), 89–96.

5. Binbasioglu, M., and Jarke, M. Process based reconstructive approach to model building. Decision Support Systems (1986), 97–113.

6. Borchardt, K. Towards a theory of legislative compromise. PB-257-478, May 1976, Harvard University.

7. Bui, T. Evaluating negotiation support systems: a conceptualization. Proceedings of the 27th Hawaii International Conference on System Science, Maui, January 1994.

8. Bui, T., and Shakun, M.F. Negotiation processes, evolutionary systems design and NEGOTIATOR. Group Decision and Negotiation (1997).

9. Chang, A.-M., and Han, T.-D. Design of an argumentation-based negotiation support system. Proceedings of the 28th Hawaii International Conference on System Science, Maui, January 1995.

10. Chang, M.-K., and Woo, C. A speech-act-based negotiation protocol: design, implementation, and test use. ACM Transactions on Information Systems, 12, 4 (1994), 360–382.

11. Conklin, J., and Begeman, M.L. gIBIS: a hypertext tool for exploratory policy discussion. ACM Transactions on Office Information Systems, 6, 4 (1988), 303–331.

12. Cook, P., et al. Project Nick: meetings augmentation and analysis. ACM Transactions on Office Information Systems, 5, 2 (1987), 132–146.

13. Davis, R., and Smith R.G. Negotiation as a metaphor for distributed problem solving. Artificial Intelligence, 20, 1 (1983), 229–243.

14. Fang, L., Hipel, and Kilgour, M. Interactive Decision Making, The Graph Model for

26. Lotus Development Corp. Lotus Notes; Release 3.0 c, 2. December 1993.

Conflict Resolution. New York: Wiley, 1993.

15. Hackman and Morris. Group tasks, group interaction process, and group performance effectiveness: a review and proposed integration, In L. Berkowitz (ed.), Advances in Experimental Social Psychology, vol. 8. New York: Academic Press, 1975.

16. Hahn, U., and Jarke, M. Teamwork support in a knowledge-based information systems environment. IEEE Transactions on Software Engineering, 17, 5 (1991), 467–482.

17. Haramundanis, K. The Art of Technical Documentation. Maynard, MA: Digital Press, 1992.

18. Hegel, G.W.F. The Phenomenology of Mind, 2d ed., trans. by J.B. Baillie. London: George Allen and Unwin, 1964.

19. Hiltz, S.R., and Turoff, M. The Network Nation: Human Communication via Computer. New York: Addison-Wesley, 1978.

20. Jackson, S., and Jacobs, S. Structure of conversational argument: pragmatic bases for the enthymeme. Quarterly Journal of Speech, 66 (1980), 251–265.

21. Johnson, P., and Tjahjono, D. Improving software quality through computer supported collaborative review. Proceedings of the Third European Conference on Computer-Supported Cooperative Work, Milan, September 1993, pp. 13–17.

22. Keough, C.M., and Lake, R.A. Value as structuring properties of contract negotiations. In Conrad (ed.), Values, Communications, and Organizational Decisions. Norwood, NJ: Ablex, 1991.

23. Kersten, G. Simulation and analysis of negotiation processes: the case of softwood lumber negotiations. Proceedings of the 28th Hawaii International Conference on System Science, Maui, 1995.

24. Koo, C.C. Offices are open systems. ACM Transactions on Office Information Systems, 4, 3 (1988), 271–287.

25. Lee, J. SIBYL: a tool for managing group decision rationales. Proceeding of Conference on Computer-Supported Cooperative Work. Los Angeles: ACM Press, October 1990, pp. 79–92.

27. Lowe, D. Cooperative structuring of information: the representation of reasoning and debate. International Journal of Man-Machine Studies, 23 (1985), 97–111.

28. Mason, R.O. A dialectical approach to strategic planning. Management Science, 15, 8 (April 1969), B-403-B-414.

29. McAllester, D. Reasoning utility package user's manual, artificial intelligence laboratory. AI Memo, 667 (1982), Cambridge, MA: MIT.

30. Melard, P., and Vanreusel, J.F. Memoire organisationelle et systeme d'aide à la decision: ARBAS'96. Mémoire de diplôme (1996), Facultés Universitaires Notre-Dame de la Paix, Namur, Belgium.

31. Ramesh, R., and Whinston, A.B. Claims, arguments, and decisions: formalisms for representation, gaming, and coordination. Information Systems Research (September 1994), 294–325.

32. Sawyer, J., and Guetzkow, H. Bargaining and negotiation in international relations. International Behavior: A Social-Psychological Analysis. New York: Holt, Rinehart and Winston, 1965.

33. Scherr, A.L. A new approach to business processes. IBM Systems Journal, 32, 1 (1993).

34. Sebenius, J.K. Negotiation analysis: a characterization and review. Management Science, 38, 1 (1992).

35. Smith, R.G., and Davis, R. Framework of cooperation in distributed problem solving. IEEE Transactions on Systems, Man and Cybernetics, 11, 1 (1981).

36. Thomas, K.W. Conflict and negotiation processes in organizations. In M.D. Dunnette (ed.), Handbook of Industrial and Organizational Psychology, 2d ed., vol. 3. Palo Alto, CA: Consulting Psychologists Press, 1992.

37. Toulmin, S.E. The Use of Arguments. Cambridge: Cambridge University Press, 1958.

38. Toulmin, S.E.; Rieke, R.; and Janik, A. An Introduction to Reasoning. New York: Macmillan, 1979.

39. Winograd, T.A. Language/action perspective in the design of cooperative work. Proceedings of the Conference on CSCW. Austin, TX: ACM Press, 1986.

40. Zartman, I.W., and Berman, M. The Practical Negotiator. New Haven, CT: Yale University Press, 1982.
