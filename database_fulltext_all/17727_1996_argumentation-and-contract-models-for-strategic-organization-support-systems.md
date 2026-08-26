---
otero_id: 17727
otero_key: "XU9X9JBM"
title: "Argumentation and contract models for strategic organization support systems"
authors: "John A.A. Sillince"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00027-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Argumentation and contract models for strategic organization support systems

John A.A. Sillince \*

Management School, University of Sheffield, 9 Mappin Street, Sheffield SI 4DT, UK

## Abstract

Strategic organizational support systems enable and support unstructured reasoning and communication within organizations. Such argumentation-based unstructured transactions can be used to continuously maintain a cognitive model of the organization. The model can be subjected to a prescriptive theory, in order to diagnose good and bad patterns in organizational cognition. Because semi-autonomous groups need to form and then dissolve when tasks have been completed, the relationship between group members (who may be inside or outside the organization) can be formalized by means of contracts. Such contracts initiate changes to the organization's business model. Contracts are monitored in order to enable adequate supervision and control to be exercised. A business model enables users to seek the organization's goals via a number of functions, such as policy making and plan making. An organizational interface controls when collaboration takes place (via argumentation, contracting, or other communicative acts). Senior managers spend most of their time collaborating on a large number of unscheduled tasks, and so a collaboration context model provides graceful engagement and disengagement using information about sender, receiver, message and task.

Keywords: Argumentation; Contract; Organization support; Collaboration; Cooperation; Cognitive model; Organizational goal; Qualitative; Soft information; Task force

## 1. Introduction

Despite the existence for a number of years of management information systems, evidence suggests that such systems do not fit into managers' work methods or organizational environment [4]. Firstly, managers prefer to gather soft information (anecdotes, rumours, opinions) in unscheduled meetings for their greater timeliness and relevance over computerised information or formal reports [12]. This suggests that one important dimension of group decision support systems is simulating the face to face nature of managerial work. Secondly, current systems over-emphasise the quantitative aspects of decisions (voting, scoring attributes, decision theory notions) rather than the qualitative nature of decisions. This involves discontinuous conflict resolution via position-taking and persuasion via argumentation rather than a continuous, summative consensus process. Thirdly, organizations are increasingly devolving responsibility onto lower levels, closer to where decision impacts are felt, by means of creating temporary task forces, delayering, and by means of resource access on a need-to-use basis, and information access on a need-to-know basis. This suggests that decision making is becoming more pluralistic and less hierarchical, determined not so much by position in the corporate hierarchy and more by the argumentative and evidential value of what one has to say. Such ephemeral statuses can only be captured by systems which mediate and transcribe argumentation and the shifting contracts which are continually being created as work tasks progress and vary through time. Fourthly, as such qualitative processes come to the fore, there is an increased need to evaluate and increase their quality. This means that such systems must have the ability to structure (arguments are broken down into evidence, warrants, and claims), externalise (via screen diagrams and hypertext links) and remember (avoiding old arguments and using existing knowledge). Structuring, externalising, and remembering are potential aids to increased rationality of decision making.

Consider the example of a company which has chosen a strategy of acquisition in order to gain market presence. This process can be mediated and supported by a Strategic Organizational Support System (SOSS) (Fig. 1) which has a number of components:

\- Argumentation is used, for example, to justify choosing particular acquisition candidates. Different acquisition candidates are put forward and the arguments supporting or attacking them are discussed and evaluated.

\- A business model is used to allocate resources for particular acquisition actions, or for generalising from past to future acquisition actions.

\- A contract support system enables agreements between parties within or between organizations to be formalized and remembered. For example, “Buyer gets majority control and acquisition candidate gets cash injection to fund its investment plans”.

\- A contract control theory lays down guidelines for controlling contracts. Before a contract for acquisition is established “Buyer needs to know Seller’s lowest price, and Buyer needs to have the authorization to use funds for acquisition”.

\- An organizational cognitive model represents the shared organizational cognitions (contained in argumentation and contract transcripts) in mathematical terms as a multi-dimensional space. For example, “The lower your raw material costs, the lower your finished goods prices” suggests that two parallel (synonymous) constructs exist. These are cheap-expensive raw materials, and high-low price. On the other hand, the argument “Raw material costs do not significantly affect information-intensive industries” means that the constructs cheap-expensive raw materials and high-low information content are perpendicular (unrelated) to each other.

![](/api/attachments/XU9X9JBM/fulltext/images/339a15e5f14e7083dc862277d0e53769062d65428006629bea1eb1706cf01473.jpg)  
Fig. 1. Strategic organisational support system components.

\- A cognitive control theory can distinguish between different structures of the multi-dimensional construct space. In particular, it can distinguish between monolithic structures (most constructs are seen as related so that change is difficult and painful), segmented structures (most constructs are seen as unrelated so the meaning of change in one part on another part is unpredictable) and articulated structures (constructs are organized into related subsystems which are robust during change). The theory enables diagnosis of healthy or pathological organizational cognitions.

\- A collaboration interface enables users of the system to switch relatively effortlessly between argumentation “ABC should be acquired” to contract “Buyer acquires ABC for \$100 million and agrees to invest a further \$100 million in ABC”, and back to argumentation “But this contract should not be seen as a precedent”.

\- The collaboration context model provides a map of activities and dialogues near to the user's own, in order to recommend, together with message and sender attributes, how acceptable and of how long a duration any interruptions should be. It also provides a map of default tasks, roles and user identities for subsequent recovery after interruption. The model identifies relationships which the system monitors and makes recommendations about. For example “Anonymous messages on this topic have caused conflict in the past — sender should identify himself” or “Messages on this asynchronous meeting have discussed agenda items one and five only — meeting should be reconvened with new agenda”.

## 2. Argumentation

Our example debate centres around an acquisition candidate, ABC Inc. The main claim “We should acquire ABC" is supported by the claim "Acquiring ABC is a very good idea although ABC is not the best candidate". Fig. 2 shows the main elements of the argumentation.

Arguing successfully requires relating aspects of one's own position for or against a main claim to current circumstances. This is done by the use of warrants, or general rules with place slots for variables. Warrants are “if–then” rules which relate premises to claims. These warrants may be very domain-specific (see Fig. 2) or they can include rhetorical arguments such as fairness, reciprocity and deterrence and logical arguments such as deduction, induction, abduction and or-introduction. A claim is made when warrants are instantiated with premises (pieces of evidence which act as acceptable values for variables). Table 1 shows that premises and claims can be represented as nodes and warrants as relations in a graph G which is directed (something supports or attacks something else), weighted (arguments have strengths), and recursive (arguments can be about arguments).

The argumentation domain is a 4-tuple $D = [M, S, AG, W]$ such that

\- $M$ is a set of rules governing moves in the debate. The graph in Fig. 2 shows the effect of several debate moves. Each participant has a turn. For example, Jones argues “We can afford ABC because current gearing is low”, and Smith argues “Good idea to acquire ABC because we want to expand into Europe”.

\- Both Smith and Jones in Fig. 2 have claims which are equally distant from the main claim, and so on this “relevance” dimension of argument strength have made equally strong claims. The strength of argument is represented by a set of argument strength criteria contained in the domain structure S, which comprises the graph G (see Fig. 2), the main claim $C_{m}$ (such as “We should acquire ABC”) and the current claim $C_{c}$ (both of which are in G), the list $P = [p0, p1, p2, \ldots, p_{n}]$ of plans derivable from G which lead from $C_{c}$ to $C_{m}$ and a 3-tuple argument $A = [T, I, E]$ , where T is a set of warrants, and I and E are internal (already referred to) and external information. If current claim is “Current gearing low” and if main claim is “Acquiring ABC a very good idea”, then there is only one plan, comprising the two intermediate claims “We can afford ABC” and “Good idea acquiring ABC”.

Argumentation grammar [22]  
```csv
similar(X,Y) ∧
obliger(X) ∧
receiver(Y)
reciprocity
→
should_oblige(Y) ∧
should_be_receiver(X)
```

Table 1

<table><tr><td colspan="2">Argumentation grammar [22]</td></tr><tr><td>Graph</td><td>= SetofEdges × SetofVertices</td></tr><tr><td>SetofEdges</td><td>= Edge *</td></tr><tr><td>SetofVertices</td><td>= Vertex *</td></tr><tr><td>Edge</td><td>= Relation × Vertex × Vertex × Attributes</td></tr><tr><td>Vertex</td><td>= Node × Attributes</td></tr><tr><td>Node</td><td>= Term | Graph</td></tr><tr><td>Term</td><td>= Text</td></tr><tr><td>Attributes</td><td>= Opinion × Opinion × Timestamp</td></tr><tr><td>Opinion</td><td>= DegreeOfBelief × DegreeOf Importance</td></tr><tr><td>DegreeOfBelief</td><td>= [ -10.. + 10 ]</td></tr><tr><td>DegreeOfImportance</td><td>= [0..10]</td></tr><tr><td>Timestamp</td><td>= CardinalNumber</td></tr><tr><td>Relation</td><td>= attacks|supports</td></tr></table>

\- $AG$ is a set of agent models containing $V$ , the partially ordered set of agent value hierarchies. For example, the strategists who are pursuing an acquisition policy highly value the future, so that Smith's argument “We want to expand into Europe” strikes a chord with this future orientation and is consequently a stronger argument because of it.

\- $W$ is the debate domain, containing domain information such as facts and assumptions represented as rules or semantic nets. For example, an assumption used by Smith is that “ABC owns European outlets”.

An argument a:A is a mapping from premises to claims. A premise is some evidence upon which the argument may be based. It may be a fact, an assumption or an earlier claim. A claim is a statement which can be said to be either true or false. A warrant is a rule which leads from a premise to a claim. An argument is either (a) a mapping from a premise to a claim using a warrant or (b) a construct used together with a set of elements, or (c) a relationship between two or more arguments or (d) a relationship between two or more constructs. In Fig. 2, a premise is “Current gearing is low”, a warrant is “If current gearing is low, or if cash flow very good or if reorganization possible, then support claim that can afford to acquire", and a claim is "We can afford ABC". Several premises and claims can be grouped together to form a new premise. Thus, premise-claim pairs can be chained together in plans. An example of a plan in Fig. 2 leads from "Current gearing is low" to "We should acquire ABC" using warrants W1, W3, and W5.

Warrants either attack or support a claim. They can be represented using logic [14] An example of a rhetorical warrant is reciprocity. For example, it could be argued that “Our main competitor has decided to threaten us with an acquisition strategy, so we should do the same to him”. In reciprocity arguments the two individuals or groups X and Y must be similar in some relevant way, thus enabling the service performed by the obliger X to be relevant to Y, but also where the obliger X must have done something not done by Y (an asymmetric relation):

Another example is deterrence. For example, "The French company could come into our market but it knows that if it did, we would go into theirs". The logic representation is:

$$
\begin{array}{l}\text {wants} (X, Y) \wedge\\\text {can\_do} (X, Y) \wedge\\\neg \text {wants} (Z, Y) \wedge\\\text {can\_hurt} (Z, X) \wedge\\\left(\text {knows} (X, \text {does} (X, Y) \rightarrow \text {hurts} (Z, X))\right)\\\rightarrow \neg \text {does} (X, Y)\\\underset {\rightarrow} {\text {deterrence}}\\\text {should\_ensure} (Z, \text {knows} (X, \text {does} (X, Y)\\\rightarrow \text {hurts} (Z, X)))\end{array}
$$

The approach taken below does not assume truth propagation or consistency maintenance. Instead inconsistency is acceptable unless it is attacked by an opponent. This avoids the need for an ATMS-based system (e.g., [7]) or some other method for separating incompatible predi-

![](/api/attachments/XU9X9JBM/fulltext/images/d33ae14a8b1d11a7f5d235707724bdecc76f6704f8c92530b0a7a1cc67817b74.jpg)

warrant W1: If current gearing is low or if cash flow very good or if reorganization possible then support claim that can afford to acquire.

warrant W2: If a company owns outlets in a region and if we want to expand in that region then support claim that good idea to acquire that company.

warrant W3: If an action is a good idea and if we can afford that action then support claim that the action is a very good idea.

warrant W4: If a candidate for an action exists and if that candidate is not the best candidate then attack that candidate.

warrant W5: If a candidate for an action is attacked and if that attacking claim is itself attacked and if no other attack exists then support that action.

warrant W6: If a claim includes a difficult to define term then attack that claim.

Fig. 2. Argumentation that “We should acquire Company ABC”.

cates. More significantly, it avoids the need to deal with non-monotonicity, a problem which has as yet not been solved for practical implementation purposes. A recent literature review is given in [24].

A multi-dimensional evaluation function f ascribes argument strength values to nodes and edges. It has the dimensions shown in Table 2.

When a node or edge is abandoned, the user with the highest score “wins” that node or edge. The users’ overall scores for the debate are the sum of values for nodes and edges won, plus the sum of values for supporting nodes and edges, minus the values for attacking nodes and edges. An evaluation function also exists for calculating which of several possible plans (routes from current claim to main claim by means of warrant-premise combinations of support) is the best one. It is the average claim strength weighted by the plan length (shorter plans get higher evaluations).

A user shifts to a new focus by one of two means:

(i) A relevant move. There is a short inter-claim distance from the proposed new claim to the current claim. In natural dialogue such shifts are marked by “frame words”. To justify a shift explicitly requires a focus shift warrant. There are four types of focus shift warrant [23]:

1. Forward. If the old focus $\phi_{t}$ makes a claim $C$ more believable then move to a new focus $\phi_{t+1}$ which is the old focus $\phi_{t}$ supporting claim $C$ . For example, in Fig. 2, $\phi_{t} =$ "Acquiring ABC a very good idea" and $C =$ "We should acquire ABC".

2. Backward. If a new focus $\phi_{t+1}$ comprising the original focus $\phi_{0}$ plus a supported claim C is more believable than the old focus $\phi_{t}$ , then move to the new focus. For example, in Fig. 2 $\phi_{t}=$ “Acquiring ABC a very good idea”, whereas the original focus $\phi_{0}=$ “ABC is not best candidate” supports claim C=“We should wait for better candidate”.

3. Attack. If a claim C contradicts the current focus $\phi_{t}$ then move to a new focus $\phi_{t+1}$ which

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
initially agents P$_{i}$ not finished; calculate current focus definition; set focus goal (SA 1):
while not finished
for i = 1 to Number_of_agents do
    set move(i) = not completed; do steps 1 to 12 (SA 21); agent P$_{i}$ invokes SAs 3-15, 17, 19, 20, 24, 25.;
    P$_{i}$ inputs warrant w1, premise d, claim c;
    check that inputs are well-formed and if not well-formed then request new ones:
    if c = an existing in_scope premise or claim then set c in_scope:
    if c in_scope then
    compare c with current focus definition and if c fits def. then set c in_focus;
    if c in_focus then
    add w1,d,c to graph;
    calculate anew all scores;
    else {c not in_focus}
    request new focus definition from P$_{i}$;
    if P$_{i}$ inputs new focus definition and other P$_{j}$ agree then
    redefine current focus definition;
    add w1, d, c to graph;
    calculate anew all scores;
    else if P$_{i}$ inputs new focus definition and no agreement from other P$_{j}$ then
    calculate anew all scores;
    compare effect of this move on score with previous move;
    if this move has higher scoring effect then
    redefine current focus;
    add w1, d, c to graph;
    else {not higher scoring effect}
    set c out_of_focus;
    add w1, d, c to graph;
    calculate anew all scores;
    endif; {higher scoring effect}
    else {no new def}
    set c out_of_focus;
    add w1, d, c to graph;
    calculate anew all scores;
    endif: {new focus def and agreement}
    endif; {c in_focus}
else {not in_scope}
request to input warrant w2 justifying relevance of c to main claim;
if w2 well-formed and P$_{j}$ agree with w2 then
    redefine scope:
    set c in_scope:
    add w2, d, c to graph;
    calculate anew all scores;
    else output rejection message 'no claim entered because not relevant';
endif; {w2 well-formed and agreement on w2}
endif; {c in_scope}
request P$_{i}$ to say whether finished:
endfor; {i to Number_of_agents}
P$_{i}$ ceases to invoke SAs 3-15, 17, 19, 20, 24, 25.;
set move(i)=completed;
if closure(i) (SA 16) and if P$_{i}$ inputs new focus definition and if other P$_{j}$ agree then
    redefine current focus definition;
endif; {closure and P$_{i}$ inputs and P$_{j}$ agree}
do step 13 (SA 21);
endwhile; {not finished}
</div>

Fig. 3. Dialogue algorithm.

## Table 3

## Software agents

## 1. Focus goals.

If focus goal is assertion then support or attack assertion. If focus goal is explanation then support or attack explanation. Classify the type of focus goal (descriptive, predictive, prescriptive) using pragmatic markers and clue words of expectations experienced by the hearer, in order to discover a suitable warrant. For example, “should”-predicates are prescriptive, “will”-predicates are predictive, etc.

## 2. Classify focus topic.

When current focus definition is calculated, classify the topic in order to discover a suitable warrant. For example, “implies” and “equivalent” suggest logic, whereas “take advantage” suggests fairness. For each topic, build a semantic net of objects and relations. In any search for “similar” objects or relations, those adjacent in the semantic net are generated and tested first. Also use the semantic net information to construct recognition functions and non-overlapping sets useful in similarity detection $[10]$ .

## 3. Warrant matching.

Given any two of warrant, claim, or premise, find the other matching element.

## 4. Choice of claim to support or attack.

Attack opponent's critical weaknesses and support one's own critical strengths. Support those claims which the opponent is more likely to accept (i.e. make use of common ground).

## 5. Argument strength.

Calculate argument strength based on constructiveness, relevance, simplicity, emphasis on ends, matching hearer's emotional expectations, upbeatness, consistency, matching hearer's change orientation, matching hearer's time orientation, and matching hearer's rationality orientation. Choose the strongest argument.

## 6. Destructiveness.

Aim for a balance of supporting and attacking claims rather than a completely destructive argument. Although this is one of the argument strength dimensions (and therefore relevant whenever the dynamic updating of the argument graph is done), it also operates strategically, i.e. used to help decide which claim to attack or support next.

## 7. Strategy.

7.1 Argument by stages. If the opponent would disagree with an argument, and if the argument can be broken down into smaller sub-arguments, and if those sub-arguments are less likely to be disagreed with by the opponent, then do this.

7.2 Comparison Strategy. If a goal is to get the opponent to reveal his best arguments in advance, (because the opponent model is empty) place a weak argument before a strong one.

7.3 Straw Man Strategy. If the opponent's claim C can be extended to form C', which can be more easily attacked, then do this.
7.4 Implying "all" when only "some" is true. If a specialised premise is used with a generalised claim, then find counter examples or suggest a more specialised claim. (Generalisation defined as dropping a condition, or adding disjuncts, or turning constraints into variables, or extending the domain, or climbing the generality tree, or suppressing the antecedents of implications; the definition assumes generality taxonomies are available).

7.5 Circular argument. If the opponent's argument is of the form if A implies B, and B implies C, and C implies A then A,B,C are true, then label that argument "circular". Some labels such as circularity have perdetermined claim strengths (low in this case).
8. Reaction to opponent.

If the opponent has used a category-based (or exception-based) warrant, then defend with an exception-based (a category-based) warrant; (e.g. category-based “X and Y are parts of Z” can be attacked by exception-based “X and Y are different because of W”).

## 9. Premise-led warrant choice.

Given a set of premises, search for a matching warrant.

Step 1. Get a clue word from a database of commonsense and known facts. For example, goal is “predict weather” and database contains only one “weather” fact, “Red sky at night”.

Step 2. Search taxonomies for clue word to get a possible warrant. For example, the category of predictive warrants contains induction, deduction, implication\_elimination, or\_introduction, part\_in\_whole, whole\_in\_part, probability, causation.

Step 3. Use the warrant and premise to generate claim. Match claim to see if it is in goal set each agent maintains of claims considered ready-to-use for attack or support.

## 10. Claims-led warrant choice.

Given a set of claims in the goal set, search for a matching warrant for at least one of them. Some preprogramming or rule making is possible — e.g. “use in argument with Y, fairness in favour of X, if Y is in a better position to X”. However, much rule making must be inductive, of the form “if warrant w worked in situation s then use generalisation of it in the next (generalised) situation s”, or “if warrant w failed in situation s then use a specialisation of it in the next (specialised) situation s”. Warrants are also included in the semantic net. Warrants may tend to co-occur near each other in the argument graph and so “relevance” here is indicated by short inter-claim distance. A different approach is to use pragmatic markers and clue words.

## Table 3 (continued)

## 11. Categorisation.

The semantic net is used to define categories. Some definitions are preprogrammed. Such rules are falsifiable, and users keep a record of their susceptibility to attack. Others are suggested by users as debate proceeds and must be agreed by the other users and adhered to. Categories have their own updateable score of ratio of strong to weak arguments generated by premises they contain. This guides search for premises. What follows about the use of categories therefore depends on categories existing or being created by users as necessary.

(1) If it is claimed that $\mathbf{X}$ is a Y and $\mathbf{X}$ does not resemble category Y then attack the claim that $\mathbf{X}$ is a Y.

(2) If X not related to Y then attack the claim that X is a Y. (3). If there is more advantage by splitting category X into two or more parts, (plans have higher strength evaluations with a split category than without) then do this. (4). If the opponent argues that X implies Y, and the user's goal is not-Y, then split (using dissociation) X into X1 and X2 where X1 implies Y and X2 does not imply Y. (5). Where a category has a good label and an exception has a bad label then make an exception seem to be a category (i.e. makethe exceptional and unacceptable seem usual and acceptable) and vice versa. (6). If two categories A and B are used in the user's claim, and another claim exists in which A and B are incompatible, then search relations between A and B, and parts of A and B, for incompatibilities. (7). If they exist, then attack the claim that A and B are related using incompatibility.

## 12. Generalisation and specialisation.

If X is a Y and a premise or claim Z includes X, then a generalisation is Z with Y substituted for X. If X is a Y and a premise or claim includes Y, then a specialisation is Z with X substituted for Y. If a premise includes X and a candidate claim includes Y then generalise. If a premise includes Y and a candidate claim includes X then specialise.

## 13. Choice of premise.

The important elements are (1) the argument elements (premises, warrants, claims, arguments) used so far, accepted facts, and rules for deducing possible premises from these arguments and facts, and (2) target claims that one would wish to reach. The list (2) is determined by a strategic view of the argument graph and the location on it of the current claim and the main claim and the need to form an unbroken line of supports from the former to the latter. Given a claim derived from (2), find a matching warrant and deducethe necessary premise, checking whether this premise exists in (1).

## 14. Common ground-led claim choice.

If a claim is part of one's own position, and if the opponent is likely to agree with that claim, then find if the opponent does agree with it, possibly using a disclaimer or a common ground-assent-claim structure, and if this is so, then use an argument which supports it. A disclaimer offers a claim as not necessarily one's own ("Some people think that.") and waits for a reaction. A common ground-assent-claim structure consists of search for common ground, followed by opponent's acknowledgement, followed by a claim, all in the same move.

## 15. Encapsulation.

If a number of previously used argumentation elements (premises, warrants, claims, arguments) are relevant to an argument in some way (where elements can be labelled “circular” or “sour grapes” or “weak due to lack of evidence” or “thin end of the wedge”, etc.), then draw an encapsulation, around those argumentation elements and label the encapsulation. Define the encapsulation as a node and its label as text.

## 16. Closure.

If it is necessary to fix the belief value of a set of argumentation elements (e.g. to argue “You remember we decided that X...”) then get the assent of others to put an envelope around a particular claim or collection of claims. That envelope can always be revisited.

## 17. Goals.

A user either supports or attacks a main claim. That claim is either an explanation or an assertion. He adds the attacking or supporting of claims to his goal set if they are part of premise-claim chains leading to the main claim. A user only proposes claims which are in his goal set. Members of the ready\_to\_use attack list and ready\_to\_use support list are members of this goal set.

## 18. Focus shift.

If a user has just carried out closure, or if he uses a warrant to justify a focus shift or if the new focus is the claim of a warrant which uses the old focus as a premise, then shift focus. A focus shift establishes a new focus goal. A focus goal which invites an explanation requires an explanation to follow, and one which invites an assertion must be followed by an assertion.

## 19. Supporting a relation.

If the opponent attacks a claim X related\_to Y then use a category-based warrant, or support the category containing X and Y. 20. Planning.

A claim can be used as a premise to a further claim, and so on in a chain, enabling users to plan. If the claim to be attacked or supported is X, and if a premise-claim chain leads from Y to X, then include Y in the ready to use attack list of claims worth attacking, or the ready to use support list (worth supporting).

## Table 3 (continued)

## 21. Move sequencing.

Steps 1 to 12 are parts of one turn (potentially several moves by J against at least one of agents I,K, and others. Steps 2 to 12 have mutually exclusive “expectation” conditions.

Step 1. I takes turn; while J can find consecutive, i.e., chaining claim-warrant-premise sets do steps 1 to 12

Step 2. A user (J) proposes a claim-warrant-premise set. Invoke SAs 3–15, 17, 19, 20, 24, 25. This move constitutes ignoring I's turn, agreement, disagreement, a challenge to I, a supporting continuation, seeking justification from I, a chaining from J's own earlier move, an indeterminate continuation, or an initial move after focus definition. If I's claim has a small effect on the debate compared with another claim which J wishes to propose then J ignores I's claim. If I's claim is in J's goal set or if the previous move used a common ground-assent-claim warrant then J agrees with I's claim. If I's claim matches a warrant which attacks a claim in J's set of won claims or in J's goal set, and if there exists a warrant which with I's premise gives a claim attacking I's claim, or if there exists a premise which with I's warrant gives a claim attacking I's claim, then J disagrees with I's claim. If I's claim matches a warrant which attacks a claim in J's set of won claims or in J's goal set, and if there exists a premise and warrant which lead to a new claim which attacks I's claim, then J challenges I's claim. If J can see common ground in I's claim then he continues I's claim. If I's claim is based upon a weak premise or warrant then J seeks justification for the premise or warrant from I. If there exist additional premises or warrants which support the currently proposed claim, then use them to bolster the argument. If J can introduce another premise-warrant-claim set related to what J has already (in this turn) introduced, then use this set as a chain from J's own earlier move. If J can introduce another premise-warrant-claim set related to what I has previously (in a previous turn) introduced, then use this set as an indeterminate continuation (indeterminate in the sense that I's material is being used, but it is as yet unclear its effect). If I's turn was to define or shift focus, and this is the first of J's moves in this turn, then J's move is unconstrained and is an initial move.

Step 3. If J ignores or agrees then

Step 3.1. credit I with having "won" that particular claim,

Step 3.2. J may optionally shift focus,

Step 3.3. J decides which claim to attack or support

Step 4. If J disagrees, J gives a new warrant which with I's premise gives a claim attacking I's claim, or J gives a new premise which with I's warrant gives a claim attacking I's claim.

Step 5. If J challenges then J provides a premise and warrant which lead to a new claim which attacks I's claim.

Step 6. If J follows up then J provides a warrant such that this warrant together with I's claim (used as a premise) generates an untenable claim.

Step 7. If J continues I's claim then he repeats I's claim or he uses I's claim as a premise to produce a claim which both J and I are likely to agree with.

Step 8. If J seeks justification then he must pick a premise or a warrant which he wants justified.

Step 9. If J has already ignored, agreed, disagreed, challenged, continued, or sought justification and if there are other premises and warrants which support J's action, then bolster J's action.

Step 10. If J can introduce another premise-warrant-claim set related to what J has already (in this turn) introduced, then use this set as a chain from J's own earlier move.

Step 11. If J can introduce another premise-warrant-claim set related to what I has previously (in a previous turn) introduced, then use this set as an indeterminate continuation (indeterminate in the sense that I's material is being used, but it is as yet unclear its effect).

Step 12. If I's turn was to define or shift focus, and this is the first of J's moves in this turn, then J's move is unconstrained and is an initial move.

endwhile.

Step 13. Turn given to agent K and go to Step 1.

## 22. Coordination.

This coordinates SAs 3–15, 17, 19, 20, 24, 25. (The other SAs belong within the stricter constraints of the algorithm in Fig. 3, or their firing conditions have been clearly described.) It determines the precedence of {warrant, claim, premise} sets discovered by these SAs and assigned by them to ready to use attack or support lists. This rule is always active.

## 23. Interruption.

Any step in a move sequence can be interrupted. The 11 strength dimensions are always actively evaluated for all agents and when an agent gets a claim-warrant-premise set which exceeds a certain score then that agent interrupts. After interruption users return to the interrupted step. This rule is always active.

24. Simplification.

If there is more than one premise-claim chain of one's own (or another agent's) leading to a main claim, then choose to support (or attack) a claim in the one with the highest average claim strength weighted towards the shortest plan.

25. Reuse of warrant.

If two premises are similar, and if one premise was used in a warrant before, generate a new claim from the other premise.

is an earlier focus $\phi_{t-n}$ ( $n$ as recent as possible) which is not contradicted by claim $C$ . For example, if $C=$ "ABC is not best candidate" contradicts the current focus $\phi_t=$ "Acquiring ABC a very good idea" then move to earlier focus $\phi_{t-1}=$ "Good idea acquiring ABC".

4. Defence. If a claim C makes an old focus $\phi_{t}$ more believable then move to a new focus $\phi_{t+1}$ which is the old focus $\phi_{t}$ supported by claim C. For example, if the old focus $\phi_{t}$ = “Acquiring ABC a very good idea although ABC not best candidate” then a new focus $\phi_{t+1}$ should be this old focus supported by the claim C = “Best candidate difficult to define”.

(ii) Escaping from an unfavourable claim. If a user escapes from a claim in this way without warrant then the other user can stay at the original claim, or the escaper concedes the focal claim he has just vacated. Therefore, unjustified focus move is short-lived or unprofitable if no focus shift warrant is offered.

In the case where a scope shift has occurred, it should be possible for a “sketchy” bridging warrant to be created between current claim and main claim. Such a bridging warrant ought always to be able to be requested (in the manner of “what is the relevance of that claim?”) Such a request ought to state the end-claim to which the current claim must be relevant. This end claim does not need to be the main claim: it may be a more local claim. A relevance warrant is a plan (a premise-conclusion chain leading from current claim to the requested end-claim). Because only “sketchy” justification is appropriate matching conditions are not as strong as for making a single claim using a premise and a warrant.

A set of software agents (SAs) which are autonomous and concurrent processes, provides the top-level control algorithm shown below in Table 3 and Fig. 3. The design comprises several modules, shown in Fig. 4.

The main modules are:

The Dialogue Manager. This module defines the current focus, current scope, and current node or edge, adjudicates when there are requests for new focus or new scope, and manages turn-taking. Specialised tasks are distributed among 26 software agents (SAs) autonomous and concurrent processes whose duration of activity is defined in Table 3 and Fig. 3.

The Control Module, which utilises the Coordination SA (SA 22) to establish precedence relations between the SAs (3–16, 18, 20–21, 25–26) which do not appear in the algorithm in Fig. 3. This SA is always active. Where there is conflict between SAs, several precedence rules are possible: to take the first one which yields above a “satisfactory” strength score, to take the best of a set generated within a certain time, or the best of the first N claims.

![](/api/attachments/XU9X9JBM/fulltext/images/9f0dcb6a6987986f2e6fb06a507257567c937635e0766f53545406570d01ac09.jpg)  
Fig. 4. Argumentation architecture.

The Graph Manager. This performs matches of premises, claims and warrants, uses the matches to decide on premise-claim chains (plans), decides on strategy of argument presentation, finds strong and weak points in the argument graph, sorts these elements into ready-to-use lists, interacts with the Dialogue manager to decide on focus change, and interacts with the Opponent Model to estimate common ground.

The Warrants Module. This comprises a list of rules which establish whether descriptions and prescriptions are acceptable.

## 3. Business model

The model uses the five meta-goals derived from the pentagon model [13] of organizational forces (Direction, Efficiency, Concentration, Proficiency, and Learning). Each meta-goal is associated with a number of decision functions (e.g., Fig. 5). The crucial relation between argumentation and decisions [19] is grounded in the rule that argumentation gains strength if it clearly relates to meta-goals and decision functions. For example, “We want to expand into Europe” is supplied as a generic “expansion” claim from a library using function “Identify target position”. “We can afford ABC” is supplied as a generic “can afford” claim from a library using the function “Identify current position”. To see how to get from current claim “We can afford ABC” to the main claim “We should acquire ABC” we use the function “Make plan”. “ABC owns European outlets” is supplied as generic “ownership” and “ownership creates opportunities” claims from a library using the function “Identify threats/opportunities”.

![](/api/attachments/XU9X9JBM/fulltext/images/76f9ce3d77308bc0688afbb62c9f79e23b4449af94463bbb2d63e80ec91fcbc0.jpg)  
Fig. 5. Business model.

Some of the functions are represented as templates [27]. Templates are frames of reference used for evaluating an issue domain. They comprise an ordered list of place slots (empty holders in which information can be instantiated) for several variables. Some of the possible slots for “Make model” in Fig. 5 for example, are model type = “means-end”, variable of means = “acquisition”, variable of end = “new market”, method of end achievement = “goodwill maintained”, precondition for means = “can afford”, precondition for end = “local market outlets”.

Other functions in the Business Model will be controlled by trigger-recognizers. A trigger is a stimulus which causes changes in template information. An example would be “If ABC is bought by a foreign company then trade union reaction would reduce goodwill”.

Means-end template modifications are triggered by gap recognizers. These compare current policy milestones such as goals, commitments, deadlines, and promises with previously reached milestones, to see how feasible such milestones are. The goal might be “Expand into Europe”, and the deadline might be “New acquisition within 6 months”. The gap recognizer would compare with similar situations such as where the goal is “Expand into S.E. Asia”, and the deadline is “New acquisition within 2 years”, and would identify a time gap in the deadlines. This gap is related to a causal model such as “New acquisition period = market analysis period plus negotiation period”, or else a means-end template modification is triggered. Such gaps could also be identified on a speculative, “what would happen if” basis [20]. Causal models are cause and effect models of part or all of the organization or its environment. Although organizational models exist based upon mathematical feedback and control theory such models use inappropriately high levels of quantification. However, it is possible to create feedback models of a less quantitative kind. Most causal models of organizations do not use structured techniques. Rather, they are intuitive, flexible heuristics developed from experience and useable as hypotheses. Examples of such qualitative causal models might include one relating an ageing population to demand for more health products, and one relating more working women to demand for more convenience foods. Such modifications to templates caused by triggers have been termed twitches [27].

## 4. Contract support system

When goal consensus exists or where people have things to exchange, people enter into contracts [7] with each other. These contracts can be simple, semi-structured, or unstructured. An example of a simple contract is a market price system such as bidding arrangement to encourage information sharing. Semi-structured and unstructured contracts are negotiated within a system in which exist users, termed agents [3] (such as “market analyst” and “negotiator”), who belong to organizations (such as ABC, and Buyer) and who have tasks (such as “Find best acquisition candidate” and “Get lowest price”). Users and organizations share relationships [3] agreed under contracts or established as the result of argumentation (see below). Relationships between users form nets. Such contract transactions might be used in constructing and monitoring knowledge bases for individual members of organizations [8]. This information triggers a conversation [3] between them about whether or not a contract of some kind (such as “Market analysis”, or “Negotiation” or “Acquisition”) can be advantageous. The process follows a contract net protocol, [5] with a task announcement stating what is wanted (such as “ABC wants highest price” or “ABC wants minority board representation”) or able to be given (such as “ABC gives European outlets”) by each party, and then by a trigger to determine an awarded contract. In order to create some form of global coherency, users obtain priorities based on a preference ordering $V,\geq$ from their organization over goals V dependent upon the match between their own and the organization’s goals and upon instructions from superiors to subordinates. The following types of message are involved [7]:

Task abstraction is the description of the goal (a problem to be solved) such as “ABC wants more investment secured by means of partnership". User $i$ says he has a $j$ th goal $V_{ij}$ where $V_{ij} \in V$ , the set of organizational goals. This gives potential contractor $k$ the chance to compare $V_{ij}$ with his preferences $(V, \geq)$ .

Node abstraction is the bid information given by the potential contractor k to user I. For example, “Buyer suggests acquisition rather than partnership”.

Eligibility specification is a list of conditions $\nu_{h}\in V_{ij}, h=l,\ldots,n$ which must be satisfied before potential contractor k can be considered a suitable bidder. Thus $\forall h\cdot\nu_{h}\cap k\neq\{\}$ . For example, “Partner must be large, profitable, have credible goals, and be cash rich”.

Bid specification is a description of required bid variables such as “Number of shares”, “Price of shares”, and “New board composition”. This is a list of bid attributes $b \in V_{ij} \cup \{\nu_h\}$ which enable rival bids to be easily compared.

Expiration time by which bids must be submitted.

The process results in a maximum intersection $max V_{i} \cap V_{k}$ of the preference sets of the contract tenderer (user i) and the potential contractor or bidder (user k). For example, ABC gets new investment cash but loses control, and Buyer gets European outlets but not the best candidate.

## 5. Contract control theory

The Contract Control Theory lays down operating principles with which the contracting process must comply. Table 4 suggests some elements of such a theory. A necessary component of any Contract Control Theory is the identification of desirable organizational behaviour. Rewards can then be directed towards selectively reinforcing behaviours approaching the organization's goals, a process known as shaping [17] and towards the question of how reinforcement is administered, a process known as schedules of reinforcement [11].

Goals are at least partly set by the contractor. But contractors differ widely in the extent to which they believe they can affect outcomes significantly. One expression of this, locus of control, [21] is the extent to which individual users believe outcomes are due to their own actions (“internals”) or the actions of others (“externals”). In order to more objectively establish the link between individual and organizational goals, one needs to attribute reasons why a particular individual acts as he does. For example, is he acting in this way because of organizational goals or for other reasons? Such judgements are subject to attribution errors [15] and thus some degree of control is required. This problem of attribution becomes less important if the task announcement is narrowly defined, since the higher the task-specificity, the more easy it is to monitor and evaluate it, and the more responsive is the contractor’s performance to schedules of reinforcement [1]. Research has found that performance improves with goal setting and feedback [6]. However, perhaps to avoid such a critical spotlight, contractors may define tasks in deliberately ambiguous ways.

Components of contract control theory

<table><tr><td>Operating principle</td><td>Test criterion</td></tr><tr><td>Goal-contract conformity</td><td>Do the contractor&#x27;s goals conform with the terms of the contract?</td></tr><tr><td>Appropriate authority</td><td>Is the authority claimed by the contractor too great or too small for the responsibility or task?</td></tr><tr><td>Appropriate resources</td><td>Have contractors got appropriate resources for the contracted tasks and responsibilities?</td></tr><tr><td>Contract honoured</td><td>Have contractors given what they contracted to give?</td></tr><tr><td>Appropriate goals</td><td>Are contractor&#x27;s goals and priorities appropriate to his organization?</td></tr><tr><td>Locus of control</td><td>Does contractor have an over- or under-valuation of the effect of the contract on the organization&#x27;s goals?</td></tr><tr><td>Contract advantage</td><td>Are the contractor&#x27;s actions in the best interests of his organization?</td></tr><tr><td>Attribution</td><td>Is the contractor doing tasks because of organizational goals or for other reasons?</td></tr><tr><td>Appropriate task announcement</td><td>Is there a match between an contractor&#x27;s tasks, responsibilities, and goals and the task announcement he has made?</td></tr><tr><td>Task performance</td><td>Is goal setting having a good effect on performance?</td></tr><tr><td>Inter-role conflict</td><td>Are the many tasks being performed by one contractor in conflict with one another?</td></tr><tr><td>Intra-role conflict</td><td>Has any contractor got contracts with two others whose goals conflict?</td></tr><tr><td>Evaluation</td><td>Is policy being implemented?</td></tr><tr><td>Mediation</td><td>Does failure to agree a contract require the intervention of a third party?</td></tr><tr><td>Social loafing</td><td>Do some contractors always initiate, and some always passively accept contracts?</td></tr><tr><td>Contractor performance</td><td>How many contracts is an contractor involved in? Is this too few or too many?How is this related to task performance, goal setting, and rewards?</td></tr><tr><td>Keeping to contract</td><td>Are an contractor&#x27;s goals, tasks, responsibilities, resources, those which he contracted for?</td></tr></table>

One possible solution to such problems is the concept of perspectives [22]. A contractor's goals may conform to the terms of the contract looked at from the point of view of an ability perspective (e.g. ability to acquire ABC) but not from that of a competitive advantage perspective (e.g. the effect of owning European outlets). Perspectives are also useful for controlling the problem of goal conflict, both when one contractor is performing several tasks which in some ways conflict with one another, inter-role conflict, and when one contractor is caught between two others whose goals conflict, intra-role conflict [18]. Such contradictory goals and expectations are numerous in an organizational environment. [22] has provided detailed examples of control indicators for each of several perspectives.

Some of the questions asked by Table 4 are: Do the contractor's goals conform with the terms of the contract? ("Is the negotiator proceeding on the basis of acquisition of ABC rather than partnership?"); Is there the appropriate authority? ("Does the seller have the authority from ABC to sell shares, to fix prices, to determine board composition?"); and Do contractors have the appropriate resources? ("Does the Buyer's negotiator know the maximum price the Buyer is prepared to pay for ABC?").

## 6. Organizational cognitive model

The Organizational Cognitive Model comprises a simplified view of how the organization construes itself, the environment, and its tasks and goals. In specifying the model, several assumptions have been made of a theoretical and methodological nature. These assumptions are that (a) strategic decisions arise from shared cognitions within organizations, (b) the main strategic discourse is provided by the main decision makers, (c) discourse manifests itself in argumentation, (d) argumentation can be used to characterise social and organizational cognition, (e) individual level cognitive theories can be generalised up to the level of the organization, (f) argumentation can be used to represent a shared construct system, and (g) it is possible to make prescriptions about organizational cognitions. These assumptions are widely shared within the organization studies literature [25]. The model makes use of Personal Construct Theory [9], and applies it to organizational contexts.

Argumentation can be represented in construct system form [25]. So argumentation provides the data for knowledge about organizational construct systems. Argumentation is parsed and reassembled in the form [Premise, Implication, Claim]. Three types of argumentation are distinguished: descriptive (e.g. The company is small so it cannot buy cheaply), predictive (e.g. The company is small and growing and so it will be large) and prescriptive (e.g. The company is small so it cannot buy cheaply. It wants to buy cheaply. Therefore the company should be large). Events or elements (e.g the company now, the company in future) are assigned to bi-polar dimensions or constructs (e.g. x small, y must buy dearly, z growing). So for E:Elements,x,y,z:Constructs the three forms are:

descriptive: $E_{t} \in x \xrightarrow{\text{implication}} E_{t} \in y$ .

predictive: $E_{t} \in x \land E_{t} \in z \stackrel{\text{prediction}}{\rightarrow} E_{t+1} \in \neg x$ .

prescriptive: $(E_{t}\in x\land E_{t}\in y\land E_{t + 1}\in \neg x)$

$$
\stackrel {\text { warrant }} {\rightarrow} E _ {t + 1} \in \neg y
$$

where the general form of a descriptive argument, with $p:Premise$ and $c:Claim$ , is $a \equiv (p_t \overset{\text{implication}}{\to} c_t)$ , for a predictive argument is $a' \equiv (p_t \overset{\text{prediction}}{\to} c_{t+1})$ and for a prescriptive argument is $a'' \equiv a \wedge ((p_t \wedge p_{t+1}) \overset{\text{warrant}}{\to} c_{t+1})$ , where warrant denotes one of a number of rhetorical or logical rules. Construct systems can be represented mathematically as a multi-dimensional space, where the mathematical form enables generalisation beyond the usual three-dimensional representation of coordinate systems to an arbitrary number of coordinates [27]. Logical expressions can be represented in coordinate space in the following way. All statements of the form $x_1 \to x_2, x_1, x_2 \in Constructs$ are represented as two parallel axes with $\{x_1, x_2\}$ both at the same pole. (Here the unlabelled arrow denotes merely association rather than specifically any of description, prescription or prediction). All statements of the form $x_1 \to \neg x_2$ are represented as two parallel axes with $x_1$ and $x_2$ at opposite poles. All $x_i$ not related by an argument mapping symbol $\to$ are orthogonal (unrelated and perpendicular to each other in multi-dimensional space). All $E_i \in Elements$ are allocated to those construct poles $x_i$ which contain them.

Consider the following argument: “The lower your raw material costs, the lower your finished goods prices”, The argument means that the two constructs cheap-expensive raw materials and low-high price are synonymous with (parallel to) each other. Cheap is the same as low price, and expensive is the same as high price. However, the argument “Raw material costs do not significantly affect information-intensive industries” means that the two constructs cheap-expensive raw materials and low-high price information products are orthogonal to (perpendicular or unrelated to) each other.

## 7. A cognitive control theory

When the organization's shared cognitions become pathological in some way, threatening its survival, a Cognitive Control Theory (Table 5) develops a considered response to the threat, by means of modifications to the Business Model. PCT leads to prescriptions for individuals [2] as well as for organizations [25]. The structure of the organizational construct system signals the quality of the organization's cognitions and decision making processes [25]. Organizations with segmented construct systems see everything as different and find it difficult to relate together things which should be related. A segmented construct system is characterised by an argument graph G comprising several isolated clusters of arguments without any linking arguments. Organizations with monolithic construct systems see everything as related. Organizations with articulated construct systems, on the other hand, see some things as similar and some things as different, and are able to maintain a more adaptive and robust construct system. An articulated construct system structure is defined by the existence of many connections between arguments and the absence of any isolated clusters of arguments.

Consider the following arguments: (1) “The lower your raw material costs, the lower your finished goods prices”, (2) “The more raw materials you buy, you can negotiate a lower price”, and (3) “An acquisitions policy means that you buy larger amounts of raw materials”. Argument (1) means that the two constructs cheap-expensive raw materials and low-high price are synonymous with (parallel to) each other. Cheap is the same as low price, and expensive is the same as high price. Argument (2) means that buy more-less and cheap-expensive raw materials are seen as parallel to each other. Argument (3) means that Acquisition policy-no policy is seen as parallel to buy more-less. It is clear there are four constructs, all parallel. If any one of them were to be questioned (say there was evidence that there are several ways of getting low raw material prices, or that raw material costs are not a significant part of total costs) then they are all questioned, because they all depend on each other. This is a monolithic construct system.

If all that existed was arguments (1) and (3), then cheap and low price would be related and also acquisition policy would be related to buy

more. But there would be no link between these two parts of the construct system. This would be a segmented system: two unrelated subsystems (arguments (1) and (3)) — what we learned about cheap raw materials would tell us nothing about whether to have an acquisition policy.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 5
A cognitive control theory
Single pole. An argument uses both poles of a construct if both poles are implicitly or explicitly used, and if elements related to those poles are related in equal numbers or if related elements on each pole have similar evaluations (either both good or both bad). Putting elements exclusively on one construct pole reduces that construct's anticipatory power because everything is seen as more or less the same. A single pole construct c exists iff
 $\forall i,i=l,...,n,\exists c$  such that  $e_{i}\in c\quad e_{i}\notin\neg c$ 
Grades of meaning. An argument defines a graded construct if it rejects both poles as relevant for the element under discussion and still uses the construct. Optionally it may redefine an intermediate position on the construct as being most relevant for the element under discussion. Constructs which have grades of meaning between poles are more useful than constructs which are merely bipolar. A construct c has grades of meaning iff
 $\exists e_{i}$  such that  $e_{i}\notin c\land e_{i}\notin\neg c\land e_{i}\cap c\neq\{\}$ 
Slot change. An argument defines slot change along a construct if the element under discussion is shifted along from one to the other construct pole as a result of the argument. Ability to change the organization's preferred pole enables the construct to more easily adapt to change. Currently an element such as "Our preferred position" is at pole c, and in future it will be at pole  $\neg c$ , so that this change occurs. That is, slot change occurs iff
 $((e_{i}\in c)\in E_{t}\wedge(e_{i}\in\neg c)\in E_{t+1}\Rightarrow(e_{i}\in\neg c)$ 
New constructs. An argument which subdivides existing categories or defines a construct pole in terms of a bipolar construct creates a new construct. Creating smaller, new categories out of larger, old ones is a useful means of effecting organizational cognitive change. When construct specificity is too low, create a new more specific construct related to the old construct. For example, the construct  $c_{k,t}$  "cheap-expensive raw materials" does not discriminate between occasions  $\{e_{i},e_{j}\}$  when high quality, expensive raw materials are or are not needed and so we create a new construct  $c_{k,t+1}$  "high-low quality". So:
 $(\{e_{i}\cup e_{j}\}\in c_{k,t}\wedge e_{i}\setminus e_{j}=\{\})^{\text{warrant}}\Rightarrow\{e_{i}\cup e_{j}\}\in c_{k,t+1}\wedge e_{i}\setminus e_{j}\neq\{\}$ 
When construct specificity is too high, create a new, more general construct related to the old construct. For example, the construct  $c_{p}$  "cheap-expensive raw materials" does not apply to  $c_{q}$  "high-low pay", and so create a newconstruct  $c_{r}$  "cheap-expensive factors of production". So:
 $(c_{p,t}\cap c_{q,t}=\{\})^{\text{warrant}}\Rightarrow c_{p,t+1}\in c_{r}\wedge c_{q,t+1}\in c_{r}\wedge c_{p,t+1}\cap c_{q,t+1}\neq\{\}$ 
Monolithic construct systems. Organizational construct systems are monolithic when a large proportion of constructs are closely related together, so that the world is seen in a very simple way, with different constructs predicting similar information about events. They lead to obsessive or rigid-dogmatic organizational cognitions. Count k instances where
 $e\in c_{i}\Rightarrow e\in c_{j}\wedge i\neq j$ 
A system is monolithic iff k&gt;N.
Segmented construct systems. Organizational construct systems are segmented when several construct clusters exist with few linkage constructs. They lead to unpredictable and inconsistent organizational cognitions. Count k instances where
 $e\in c_{i}\Rightarrow e\in c_{j}\wedge i\neq j$ 
A system is segmented iff k&lt;M.
Articulated construct systems. Organizational construct systems are articulated when several construct clusters exist with many linkage constructs between them. They lead to robust and adaptive organizational cognitions. Count h instances where  $e\in c_{i}\Rightarrow e\in c_{j}\wedge i\neq j$  and count k instances where  $e\in c_{i}\Rightarrow e\notin c_{j}\wedge i\neq j$ . Then a system is articulated iff M&lt;h∧N&gt;k.
Hierarchical structure. An argument which mentions evaluation or prescription defines hierarchical importance. Such arguments make construct systems become more hierarchically organized. Organizational construct systems require a hierarchical structure to ensure that a well-developed partial order of priorities exists. A system is hierarchical, where a preference ordering (V,≥) exists, iff for all  $c_{i}$  it is possible to arrange them  $c_{1}\geq c_{2}\geq\ldots\geq c_{n}$ .
</div>

However, if we add another argument: (4) “An acquisition policy means that you have the flexibility of a wider range of choices of products to push”. Then even if, say, argument (2) is attacked (buying larger amounts of raw materials does not necessarily reduce their price — higher demand may push the price up) the acquisition policy would not necessarily also come under attack — i.e. the construct system is now more robust. Now the construct acquisition policy is related to two subsystems — the cheap-low price-buy more subsystem and the flexibility subsystem, so that even if the first subsystem is disconfirmed, the second subsystem is still left intact. This system of related subsystems is an articulated structure.

## 8. Collaboration interface

The more senior that managers are, the more time they spend collaborating, and the less time they spend on each individual activity [12]. Rapid movement from topic to topic occurs in an unscheduled way. Information is usually filtered and "soft" rather than in document form. Fig. 6 shows a transition network of the actions of an interface for managing this rapid, unscheduled series of activities. Each circle is a node (where interruption can occur). Each arrow is a type of action. An action bid is realized by a request, ("Can we discuss closer contact between our company and ABC?"), which if refused involves a renegotiation of validity conditions [16] (“ABC sees closer contact as meaning a partnership”). If the bid is accepted as valid it may still be refused, (“Good, we would like that, but first we need to discuss your motives”) or a promise made that it will be complied with later, or resort may be made to argumentation, (“ABC has cash flow problems and a deal needs to be struck within days”) or (the favourable outcome) it can be made into a contract (“We buy half the stock and you give us four seats on the board”).

![](/api/attachments/XU9X9JBM/fulltext/images/381add3d53959a9695f3fdf580a143603f75fe0143aa4fee7ef9c1f18a7a1ef3.jpg)  
Fig. 6. Collaboration interface.

## 9. Collaboration context model

When interruptions occur the task and user context must be saved, and a map provided of “neighbouring” tasks and users. Also, interruption itself must be collaboratively negotiated. These contextual aspects are provided in a Collaboration Context Model. Interruption itself may be on a number of different levels, with varying degrees of copresence shared by two users. Recipient (or interruptee) and sender (or interruptor) users have statuses, responsibilities, accessibilities, commitments, pressures, social spaces, privacies, and social distances, and messages have urgencies and relevancies, and these influence the acceptability and duration of interruption $[26]$ . Besides sender, receiver and message attributes, interruptibility is also influenced by task attributes. The nearer a task is to another task (according to role, decision stage, and group formation stage, see Fig. 6) the easier to justify interruption. Identify issues and Explore dissonance (Fig. 6) are more similar and hence on average closer in time than Make commitment. The activity “map” can be used to justify interruption, task reordering, deadlines, to-do lists or new topics. Such maps may have different configurations for different individuals or for different task processes and so would be subject to rapid reconfiguration.

Collaboration is also affected by network characteristics such as who can talk to whom (and how easily). At one extreme, a user might be unsupervised, or anonymous, or one of the mere spokes of a “wheel”. At this extreme group polarisation may occur, conflict develops (this may be functional during conflict or “storming”), and deindividuation (loss of sense of identity) and resentment are a problem. At the other extreme, a user may be strongly supervised, or identifiable, or connected to all other users. At this extreme, there are problems of availability bias (judgements being based only on easily available evidence), representativeness bias (stereotyping), escalation of commitment (continued commitment despite warning signs), conformity to group norms (“groupthink” and “tunnel vision”), and status or dominance bias (being over-deferential to status or personality). The optimum position on these related dimensions is influenced by decision and group stages (e.g. non-anonymity is helpful for finding common ground during “norming”) and by activity (e.g. information role activities are inhibited by over-supervision). The interface should monitor these cognitive variables, and provide meaningful feedback related to user choices.

The three components of Collaboration Interface, Argumentation, and Contract are the most "visible" to the user, and hence are shown in heavy lines in Fig. 7. Interactions between components require justified actions. For example, arguing about contracts involves negotiating terms.

## 10. Conclusion

Software technology enables artificial intelligence to be applied at an organizational scale, in the distributed, agent-oriented way described above. Organizational form is becoming less hierarchical, less layered, more flexible and fluid depending on external environmental conditions. Contracts are an example, because they are agent-centred, and involve the creation of perhaps temporary relationships contingent on changing task characteristics, expertise and access to resources. Argumentation is another example, because types of organizational form are emerging which involve the giving of information on a need-to-know basis and power and authority according to reasoned argument (one's relatedness to the problem, how informed one is, relevant personal experience) rather than hierarchical position.

![](/api/attachments/XU9X9JBM/fulltext/images/6d123e2fa38f2a9ad2f858cfeb0ef233bc6548088b6ecc531af1902daa2aa378.jpg)  
Fig. 7. Collaboration context model.

## Acknowledgements

The author would like to thank the two anonymous reviewers for their many constructive comments.

## References

[1] S.C. Ainlay, G. Becker and L. Coleman (eds.), The Dilemma of Difference (Plenum, New York, 1986).

[2] D. Bannister and J.M.M. Mair, The Evaluation of Personal Constructs (Academic Press, London, 1968).

[3] A. Blyth, ORDIT: Using Agency to Model and Comprehend Organizational Problems in Software Engineering, Proceedings of the Third Belief Representation and Agent Architectures Workshop, (BRAA'92), School of Engineering and Computer Science, University of Durham, 1992.

[4] R.L. Daft, R.H. Lengel and L.K. Trevino, Message equivocality, media selection, and manager performance: implications for information systems, MIS Quarterly (1987) 355–366.

[5] R. Davis and S.G. Smith, Negotiation as a metaphor for distributed problem solving, Artificial Intelligence 20 (1983) 63–109.

[6] C. Fombrun and M. Shanley, What's in a name? Reputation building and corporate strategy, Academy of Management Journal 33 (1990) 233–258.

[7] U. Hahn and M. Jarke, A multi-agent reasoning model for negotiation support, in: R.M. Lee, A.M. McCosh and P. Migliarese (eds.), Organisational Decision Support Systems (Elsevier Science, Amsterdam, 1988) pp. 101–115.

[8] V.S. Jacob and H. Pirkul, Organizational Decision Support Systems, International Journal of Man-Machine Studies 36 (1992) 817–832.

[9] G.A. Kelly, The Psychology of Personal Constructs, Vols. 1 and 2 (Norton, New York, 1955).

[10] Y. Kodratoff, Introduction to machine learning (Pitman, London, 1988).

[11] F. Luthans and R. Kreitner, Organizational Behaviour Modification and Beyond (Scott Foresman, Glenview, Il, 1985).

[12] H. Mintzberg, The Nature of Managerial Work (Harper and Row, New York, 1973).

[13] H. Mintzberg, Mintzberg on Management: Inside our Strange World of Organizations (New York, Free Press, 1989).

[14] I.A. Mitroff, R.O. Mason and V.P. Barabba, Policy as Argument — A Logic for Ill-structured Decision Problems, Management Science 28, No. 12 (1982) 1391–1404.

[15] B. Mullen and C.A. Riordan, Self-serving Attributions for Performance in Naturalistic Settings: A Meta-analytical Review, Journal of Applied Social Psychology 18 (1988) 3–22.

[16] D.E. Murray, Requests at Work: Negotiating the Conditions for Conversation, Management Communication Quarterly 1, No. 1 (1987) 58–83.

[17] K. O'Hara, C.M. Johnson and T.A. Beehr, Organizational Behaviour Management in the Private Sector: A Review of Empirical Research and Recommendations for Further Investigation, Academy of Management Review 10 (1985) 848–864.

[18] J.L. Pearce, Bringing Some Clarity to Role Ambiguity Research, Academy of Management Review 6 (1981) 665–674.

[19] R. Ramesh and A.B. Whinston, Claims, Arguments and Decisions — Formalisms for Representing Gaming and Coordination, Information Systems Research 5, No. 3 (1994) 294–325.

[20] U. Rosenthal and B. Pijnenburg, Simulation-based Scenarios, Contemporary Crises 14 (1990) 277–283.

[21] J.B. Rotter, The Development and Applications of Social Learning Theory: Selected Papers (Praeger, New York, 1982).

[22] G. Schafer, Functional Analysis of Office Requirements: A Multifunctional Approach (Wiley, New York, 1988).

[23] J.A.A. Sillince and R.H. Minors, Argumentation, Self-consistency and Multi-dimensional Argument Strength, Communication and Cognition 25, No. 4 (1992) 325–338.

[24] J.A.A. Sillince, Multi-agent Conflict Resolution: A Computational Framework for an Intelligent Argumentation System, Knowledge-Based Systems 7, No. 5 (1994) 75–90.

[25] J.A.A. Sillince, Extending the Cognitive Approach to Strategic Change in Organizations: Some Theory, British Journal of Management 6 (1995) 59–76.

[26] J.A.A. Sillince, A Model of Social, Emotional and Symbolic Aspects of Computer-mediated Communication Within Organizations, Computer-Supported Cooperative Work 4, No. 2 (1995) (in press).

[27] P. Slater, The Principal Components of a Repertory Grid (Vincent Andrews, London, 1965).

![](/api/attachments/XU9X9JBM/fulltext/images/04fe780beb913fbbf19dbed8697b0268b48ccc94acd265efbbfecbfaf1249bbf.jpg)  
Dr. John A.A. Sillince has degrees in mathematics and computer science. He formerly taught Computer Science at Coventry University, and now teaches Management Information Systems at the Management School, University of Sheffield. His research focus is argumentation-based group decision support systems.
