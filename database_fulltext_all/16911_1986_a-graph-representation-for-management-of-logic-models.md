---
otero_id: 16911
otero_key: "ET6FCQHG"
title: "A graph representation for management of logic models"
authors: "Steven O Kimbrough"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90118-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Graph Representation for Management of Logic Models

Steven O. KIMBROUGH

University of Pennsylvania, Department of Decision Sciences, SH-DH/CC, Philadelphia, PA 19104, USA

This paper addresses the problem of managing logic models, which are characterized as formal representations, in logic, of particular systems of interest. The paper presents a new, graph-based representation scheme for logic models. The scheme produces logic graphs and these graphs are useful for management of logic models. Logic graphs not only provide the full deductive capabilities of logic, but they facilitate the gaining of insight into the structure of the logic model. As such, logic graphs are an attractive alternative to other automatic theorem-proving techniques in logic. The discussion is illustrated throughout with an example problem in policy analysis and planning that has appeared in the management literature.

Keywords: Logic; Graph; Automatic Deduction; Planning; Model Management; Decision Support Systems

![](/api/attachments/ET6FCQHG/fulltext/images/80146b9b3ba253d7c92f431aa44544a760a7029deb34165dc0177ec0190c92a9.jpg)

Steven Kimbrough is Atlantic Richfield Assistant Professor in information systems at the Department of Decision Sciences, The Wharton School, University of Pennsylvania. His main research interests are in the fields of telecommunications and decision support systems. His active research areas include: automatic theorem-proving in modal logic; DSS support for multicriteria evaluation and design problems; investigation of industrial organizational effects of new telecom-

munications technology; and principles of network management. Kimbrough received his MS and PhD degrees at the University of Wisconsin-Madison.

## 1. Introduction

Formal logic is being applied increasingly to problems in management. Applications in artificial intelligence and decision support systems have gained considerable acceptance and are becoming well known. One application of logic to management that is especially interesting is in planning and policy analysis [1-3], in which competing reasons for a particular policy judgment are symbolized into formal logic, producing what I will call a logic model of the situation. (I use the term logic model, rather than the familiar 'logical model', to avoid confusion. The former is exactly what the latter is not: a declarative, non-procedural representation of a system.) The logic model, being a formal representation, can then be studied using rigorous techniques [4] and (viz. Prolog) can be implemented on a computer. Thus, one might hope to avoid some of the confusion and obfuscation commonly associated with policy formation and planning.

This paper addresses the problem of managing logic models. The concept of a model management system (MMS) is that of a system which provides 'a structured milieu for storing, manipulating, and retrieving models' [5–8]. In what follows, I present a new, graph-based representation scheme for logic models. The representation scheme produces what I shall call logic graphs, which graphs are useful for management of logic models. Logic graphs not only provide the full deductive capabilities of logic (here, sentence logic), but they facilitate the gaining of insight into the structure of the logic model. As such, logic graphs are an attractive alternative to other automatic theorem-proving techniques in logic. These points are all illustrated with an example problem in policy analysis that has appeared in the management literature. Finally, I discuss issues for future research.

## 2. Logic and Policy Analysis

The following passage from [1] (p. 1392) nicely captures a primary motivation for constructing logic models for policy analysis.

The dialogue between two professionals in a given field may be construed as a complex argument that unfolds and changes over time. Most of the time, we rarely penetrate beneath the surface structure of an argument to examine the basic premises and assumptions upon which the credibility of the outcome of the argument rests, let alone the structure of the argument itself. And yet, it is precisely this more thorough examination of the entire chain of reasoning by which a decision-maker has arrived at certain decisions that is one of the most critical tasks in policy analysis.

As an example, an argument and a series of rebuttals to the argument are discussed in [1]. The policy issue at hand is the use by the Census Bureau of the straight head count method in determining population counts. Informally, their example argument is:

1. The Census Bureau has been perceived historically to be nonpolitical.

2. Nonpoliticization implies nonadjustment of raw census figures.

3. Nonadjustment of raw census figures implies using the straight head count method.

4. Nonpoliticization is fundamental to objectivity (or, nonpoliticization implies objectivity is required as a policy).

5. Therefore, the straight head count method is warranted or justified.

The symbolization scheme used for this argument in [1] is (essentially) the following:

(1) P: The Census Bureau has historically been perceived to be political.

(2) S: The straight head count method is warranted or justified.

(3) W: The straight head count method is adjusted.

(4) V: The Bureau is objective.

Given the symbolization scheme, the argument in [1] is formalized as follows.

(1) -P

(2) $-\mathbf{P} \rightarrow -\mathbf{W}$

(3) $-\mathbf{W} \rightarrow \mathbf{S}$

(4) $-\mathbf{P} \rightarrow \mathbf{V}$

(5) Therefore, S

Given this formulation, it is clear that the argument for S is valid and that the fourth premise is superfluous (although this is not mentioned in [1]). In attempting to simplify the argument and to determine its basic definition, the technique in [1] is applied to produce the following statement:

$(-V \& -P \& -W \& S)$

This, as Locks points out in [2], is incorrect. The statement should read:

(V & -P & -W & S)

The rebuttal is symbolized as a collection of assertions, which informally are as follows.

(1) A case can be made that some other method is justified.

(2) A case can be made for politicization of the bureau.

(3) It is not necessarily true that avoiding politicization implies using the straight head count method (taking slight, perhaps inconsequential, liberties with the formulation in [1]).

(4) It is not necessarily true that avoiding politicization leads to being objective.

In [1] the rebuttal was symbolized as such:

1. -S

2. P

3. $-( - P\to S)$

4. $-(-\mathbf{P} \rightarrow \mathbf{V})$

Using their earlier technique for reducing a collection of statements, the rebuttal was reduced in [1] to:

$(-V \& P \& -P \& -S)$

This reduction is correct in the sense that this statement can be derived from the conjunction of the four rebuttal statements, as symbolized. Note, however, that the reduction statement is inconsistent. It asserts both P and -P. In fact, the four rebuttal statements taken together are inconsistent. This is, I take it, not altogether obvious from the informal rebuttal statement and serves to demonstrate the value of formalization into logic.

The bulk of [1] is concerned with the analysis of the argument and the rebuttal(s) and relies mainly on the reduction method. There is much value in this (laying aside the logical error), but there is much more value to be extracted from the formalization and analysis of arguments. An important issue is raised in [1]:

How should we compare and analyze competing, inconsistent logic models for planning and policy making?

An example of a tool, or technique for helping to do this, would be one which asked a logical ‘what-if’ question, as in:

'What if we changed a particular assumption, being attacked by the rebuttal, would we need to change our conclusion?';

or 'What if we added a new assertion to shore up a particular assumption, would we get into trouble otherwise?';

or 'What are the consequences of agreeing to drop

a particular assertion in our model?" and so on. Both the methods in [1] and the standard proof methods for logic (mainly, resolution) do not easily support this sort of capability. In the next section, I shall present and discuss an alternative proof and analysis method that appears to support these logical 'what-if' questions.

## 3. Logic Graphs for Sentence Logic

Graph- or digraph-based knowledge representation schemes have a number of advantages, including conceptual clarity, ease of programming, and ease of manipulation. They are natural devices for encoding virtual knowledge. Usually, when digraphs are used in knowledge representation, nodes are interpreted as objects and directed arcs are interpreted as 'semantic' relations [9]. In this section, I present and discuss a digraph representation for sentence logic. The representation can be used, in combination with shortest-path algorithms (such as Floyd's algorithm [14]) to prove theorems. Under the intended interpretation of the digraphs, nodes correspond to sentences (or well-formed formulae) and directed arcs correspond to the relation of material implication. Thus, $[P] \rightarrow [Q]$ is a digraph representation of ‘P → Q’, using ‘→’ for material implication.

The three main results I shall present and discuss are:

(1) A digraph representation algorithm for translating a collection of statements (AXIOM) in sentence logic into a directed graph. I will refer to this algorithm as SLDRA (sentence logic digraph representation algorithm) and to its resulting digraph as DGR.

(2) A consistency criterion, CC, for judging whether AXIOM (as represented by DGR and produced by SLDRA) is logically consistent.

(3) Proofs as to the adequacy of (1) and (2).

These results are presented and discussed in detail in Appendices A and B. Briefly, the logic graph method employs an algorithm, SLDRA, to produce a representation of a collection of statements in sentence logic. The representation consists of a directed graph, DRG, and a list, LI. A consistency criterion, CC, can be applied to the (DRG, LI) pair for the purpose of doing proofs in sentence logic. The elements of LI are formulas (or sentences) in sentence logic. The directed graph, DRG, is to be interpreted so that nodes correspond to certain formulae in sentence logic and directed arcs stand for the logical concept of material implication, as mentioned above.

The logic graph method, described in Appendix A, is a full theorem-proving method for sentence logic. It has, in addition, a number of properties that are quite desirable from the point of view of managing logic models. To see this, consider again the example from MMB. The argument in MMB would be represented in Fig. 1, using the logic graph technique (i.e., using SLDRA).

![](/api/attachments/ET6FCQHG/fulltext/images/fbbe33f8e5b98b3d2c2bbee831290e53c75888a114a0c1df12304137ddbff5e0.jpg)  
Fig. 1.

LI consists of just the statement: -P. Notice that from -P we can reach -W, V, and S. So, under this representation we obtain immediately the four literals obtained by the corrected version of MMB, and we do this in a direct and easy manner. Now, if we want to ask if the conclusion, S, logically follows from the axioms, given above, we simply add -S (i.e., the denial of the conclusion) to the axiom set, perform SLDRA, and check for consistency. Doing this has the effect of merely adding -S to LI. Once we do this, P, -P, W, -W, S, -S, and V (but not -V!) are asserted and we clearly have a contradiction of literals, so the argument is indeed valid.

Now let us take a look at the rebuttal. It consists of four, possibly independent, statements, symbolized as follows.

$$
1. - S
$$

2. P

$$
3. (- (- \mathbf {P} \rightarrow \mathbf {S}))
$$

$$
4. (- (- \mathbf {P} \rightarrow \mathbf {V}))
$$

Using the above logic graph helps us to understand the process of rebuttal. On the first rebuttal, notice that formally the effect of it would be simply to deny the conclusion. This is hardly an effective rebuttal, for all it really does is to announce disagreement with the conclusion of a valid argument. It offers no reasons to deny the premises. Notice, however, the intended meaning of the original first rebuttal was that 'A case can be made that some other method is justified'. That, by itself, would not block the conclusion either. What is needed is an argument to show that some other method is justified (M) and the claim that if M and S are true (i.e., if the two methods are justified), then the M method is preferable to the S (straight head count) method.

If the logic graph does not help us much on the first rebuttal, it does help on the second. For the effect of the second rebuttal is simply to remove -P from LI. If this is accepted, then the conclusion is indeed blocked. Removing the assertion that -P makes the consequent argument invalid. -P is a key assertion in the argument and it is the logic graph that shows us this clearly. Notice, also, that nothing in the argument justifies or supports the claim that -P (and nothing in the rebuttal as given supports the assertion that P, either). So, in examining this argument, discussion of -P is crucial. If P is asserted, the only way for a proponent of the conclusion to get a valid argument with this structure is to assert -W. Notice that this fact can be read off of the logic graph directly.

What if it is granted that -P is correct? Is there then any way left to block the conclusion? Yes, for an opponent could claim either that the $(-P \rightarrow -W)$ conditional is incorrect or that the $(-W \rightarrow S)$ conditional is incorrect. This, too, we can read directly from the logic graph. To see that this is not otherwise an obvious fact, notice that none of the rebuttals recognize it.

The third rebuttal would have the effect of removing an arc from $[-P]$ to $[S]$ , but there is no such arc. Is the third rebuttal irrelevant? It is certainly not directly relevant and is mostly beside the point. Charitably interpreted (and this can be read off from the graph), the third rebuttal is saying that either the $[-P]$ to $[-W]$ arc should be blocked or the $[-W]$ to $[S]$ arc should be blocked, or both. This objection was recognized explicitly in the previous paragraph.

The fourth and last rebuttal amounts to the removal of the arcs from $[-P]$ to $[V]$ and from $[-V]$ to $[P]$ . These arcs are strictly irrelevant to the argument as it stands. A proponent could cheerfully grant this rebuttal without putting the conclusion in jeopardy. What is curious about this is why a supporter of the argument would not have added, as a form of backing, the claim that if you are going to be objective, then you have to use the straight head count method, i.e. $(V \rightarrow S)$ . Had this been done, there would have been two node and arc disjoint paths from -P to S, with consequent changes to the rhetorical dynamics of the policy question. I leave these to the reader to contemplate, with the aid of the above logic graph.

The rebuttals, thus, are of mixed value for their intended purpose. Had an opponent of this argument considered its logic graph, it would have been immediately apparent that (formally) there are but three lines of attack: deny that -P, block the material implication from -P to -W, and block the material implication from -W to S. Formally, there is nothing else to attack. Non-formally, of course, there may well be other issues, mainly having to do with the adequacy of the symbolization process. An opponent could maintain that the argument was improperly formalized ('That's not what we mean by...') or that the conclusion, however correct, is insufficient for the issue actually at hand (e.g., 'Sure the straight head count method is justified, to some degree, but that does not solve the problem because other methods are also justified'). Symbolic logic is concerned with the formal structure of the argument. Its only contribution to resolving the informal issues of symbolization is to show clearly the results and consequences of a given symbolization scheme.

To conclude this section, then, argument is a tricky business, one in which we are all prone to mistakes. The situation is exacerbated when groups, containing individuals with varying and competing interests, are involved in reasoning to a conclusion. Logic in general and symbolic logic in particular are proper tools that may support planning and policy formation through clarifying and focusing both arguments and their rebuttals. These tools, however, are themselves exposed to erroneous use. I have proposed the method of logic graphs as a way to make more effective use of symbolic logic as a tool for planning and policy formation. The primary value of logic graphs lies jointly in their ability to clarify the argument (and rebuttals) at hand and in their capacity (through the graph structure) to be implemented and manipulated on computers. In the next section I shall develop this idea further.

## 4. Model Management and Logic Models

From the point of view of model management, a logic model should be treated as an abstract data type, i.e., as a mathematical model with a group of operations defined on the model [15]. This is, at the very least, one way to implement the concept of models as data for the model management system [5]. Before discussing the appropriate mathematical model for logic models seen as abstract data types, let us first discuss what operations we might want to perform on a logic model. I propose the following list, using questions to indicate operations:

(1) Is the argument valid?

(2) Are the premises consistent?

(3) Is the rebuttal consistent?

(4) Is the rebuttal effective (i.e., does it imply the denial of the argument's conclusion or does it make the argument invalid)?

(5) How, exactly, does the rebuttal disagree with the argument?

(6) If a statement, B, were added to the premises of the argument (rebuttal) would the premises (rebuttal) be consistent? I call this the increment problem.

(7) Given a collection of assertions (or axioms) and the desire to remove a particular assertion, B, which, if any, other assertions must also be withdrawn? This is what I call the decrement problem. It arises when an axiom system is redundant and an attempt is made to remove a particular axiom.

(8) Given an inconsistent system of assertions, which assertions will, when withdrawn, make the remaining system consistent? I call this the revision problem.

For the purpose of answering these types of questions, logic graphs, I maintain, have a number of advantages as the underlying mathematical model for the abstract data type of logic model. I shall now illustrate this claim with a, by now familiar, example.

Suppose we are opponents to the straight head count method and we have made the rebuttal that was discussed above. It was then pointed out to us that the four rebuttal assertions are, taken together, mutually inconsistent. We must now consider what to do, so we begin by applying SLDRA to our collection of rebutting statements. The result (in part, leaving out a few nodes and arcs) is shown in Fig. 2. The numbers in curley brackets under LI refer to the number of the rebuttal statement, with $\{3\}$ and $\{4\}$ being logically equivalent transformations of the originals (after calling DISTNEG).

It is clear from LI that this collection of assertions is inconsistent, since both P and -P can be derived. What happens if we remove P from our list of rebuttals? This is, in effect, to ask a revision question. The answer can easily be read off of the graph and LI. If P is removed from LI, then so must every node reachable from [P], unless the reachable node can be asserted on some independent grounds. So, we see that [P v S] is reachable from [P], that [P v S] belongs to LI (i.e., is asserted), that [P v S] is reachable only by one other node, [S], and that [S] is not asserted. Using the OR rule from CC, we conclude (correctly) that [P v S] should be removed from LI. Similar reasoning has us remove [P v V] and nothing else. We see, too, that by removing P we have not had to retract any of the other rebutting statements and we have achieved consistency in the rebuttal, a minimal requirement, but a requirement nonetheless.

![](/api/attachments/ET6FCQHG/fulltext/images/9053b845e6869e19503fc9758cf4b83254640a37c778ba713650e94f5674fa9b.jpg)  
Fig. 2.

Should we remove P, then, and commit to the revised rebuttal (the original, without the second assertion)? That is an option, but recall our earlier discussion of the rebuttal. None of the other three rebutting statements are effective at defeating the argument. Moreover, the assertion of -P was shown to be critical to the argument. If -P could be removed from LI in the argument, the argument would fail to be valid. We should, then, like to consider the effect on the rebuttal of keeping P but somehow removing -P.

Again, the consequences of this move can be read from the graph and LI, more or less directly. If we remove -P from LI, then we must remove any asserted nodes from which -P is reachable. So, we need to remove [-P & -S] and [-P & -V]. In other words, if we are to keep rebuttal statement [2], we must give up both rebuttal statement {3} and {4}. Notice, too, from the graph, that were -S not asserted by an individual rebuttal statement we would have to remove it as well from LI. In other words, if P is our rebuttal we succeed in making the argument invalid, but we do not succeed in proving the denial of its conclusion.

The argument and rebuttal of MMB are both quite simple. Yet, as we have seen, there is much to be said about these collections of statements and much structure that does not lie on the surface. And there is in fact much more to be said than I have said. Enough has been said, however, to demonstrate some of the requirements for managing logic models and to demonstrate some of the advantages for model management of using logic graphs to represent the logic models.

## 5. Research Issues for Management of Logic Models

Work on logic models in management is still new and work on management of logic models has only just begun. Work on logic graphs is reported here for the first time. The following is a list of areas for further work, rather than specific topics.

1. Symbolization: This term refers to the process of representing in formal logic a collection of English statements, or, more generally, a system of interest. (The reverse process is called translation, although this latter term is sometimes used for both processes.) The issues are how to do it and how to support it. There is a good general literature on this topic, to be found in logic texts, among other places. Outside of Ron Lee's work [16], however, there is little systematic discussion of the symbolization problem as applied to management subjects. A reasonable hope for work in this area is that it would be cumulatively valuable. For example, once areas of budgeting or accounting were symbolized and accepted, their logic models could be brought into play in new situations, rather like subroutine libraries [3]. It is worth noting, in this context, that serious questions can be raised about the symbolization used by MMB. To say more, however, would be to take us beyond present purposes.

2. Applications of Logic Models: Logic models are like expert systems in that we are only beginning to understand where they can be used effectively and economically. A number of authors have proposed that DSs in general be built around logic models [5,17]. A good case can be made for this proposal, but much remains to be known. An important proposal is made in [1] that logic models can be used for planning and policy analysis, but little has been done in this area beyond that particular paper. Recent work in strategic planning has emphasized ‘assumption surfacing’, the making explicit of rules and facts assumed and critical for the planning process and the examining of these assumptions [18,19]. The logic graph method would seem to be worth serious exploration as a supporting technique for evaluating surfaced assumptions.

3. Extensions to Other Branches of Logic: Sentence logic was used in [1] and sentence logic is the logic captured by the logic graph method presented above. It is a general requirement for logic models that they be able to handle predicate logic. There may be value in extending to modal, deontic, and/or tense logic as well, but tradeoffs will have to be assessed. This is largely an untouched area in management research. The logic graph method, discussed above, can be extended to predicate logic and to modal (and deontic) logic.

4. Determination of Requirements for Management of Logic Models: I have made a few suggestions in section 5, above, but these are only suggestions. They need to be extended and clarified.

5. Theory: The computational complexity of logic graphs and of any other model management techniques for logic models needs to be studied. The logic graph technique I have given will consume lots of memory, but is (I believe) relatively efficient for model management tasks, when it comes to processing resources.

6. Implementation: Logic-based DSS and logic-based expert systems are research and development areas of fairly high activity. Much is being learned about the problem of implementing logic models. The main representation vehicle, however, is Prolog and logic graphs have not been implemented as a programming language. Little is known about implementation of model management systems for logic models.

7. Testing with Decision Makers: If little is known about management of logic models, even less is known about what decision makers want and will accept.

In sum, logic models are promising tools for DSS and expert systems in management, but much remains to be learned if the promise is to be realized. Part of what remains to be learned is how to build model management systems for logic models. Logic graphs are likely to be of great help on this issue.

## 6. Appendix A: The Logic Graph Method in Detail

The purpose of this appendix is to present in detail SLDRÅ (sentence logic digraph representation algorithm) and the test for consistency, used in performing proofs.

First, some remarks on notation and some definitions. Capital letters in the last half of the alphabet (N, O, ..., Z) will be used for sentences in the object language. Capital letters in the first part of the alphabet (A, B, ..., K) will be used in the metalanguage to refer to statements (or well-formed formulae) in the object language. In either case, indices may be used; P(2) and B(5) are legitimate expressions in the object and metalanguages respectively. Nodes in a graph will be assigned to formulae. The node, e.g., assigned to formula B will be called [B].

Definition: A statement, B, is a literal [20,21] if and only if one of the following conditions obtains:

1. It consists of only a single sentence letter, in which case it is said to be atomic.

2. It consists of only a single sentence letter preceded by a single negation sign.

Definition: A statement, B, is molecular or compound if and only if it is not literal.

Associated with SLDRA and the resulting DGR and QU and LI. QU is an initially empty queue of statements to be added to DGR, using SLDRA. These statements are produced by SLDRA when adding a single statement, B (possibly molecular), to DGR. QU has a first-in-first-out discipline, although this is not essential for any of what follows. LI is list of basic assertions, BAs, which I will explain presently. LI need not be empty when SLDRA is initiated for B.

In presenting SLDRA, it will be useful to define two procedures on well-formed formulae, DISTNEG(B), for 'distribute negations', and ADDQU(B), for 'add B to QU'. These are defined as follows, using ‘:=’ as an assignment operator (directed from right to left).

## DISTNEG(B)

1. If B has the form --D, then B := D.

2. If B has the form $-(D \& E)$ , then $B := (-D \lor -E)$ .

3. If B has the form $-(D \lor E)$ , then $B := (-D \& -E)$ .

4. If B has the form $-(D \rightarrow E)$ , then $B := (D \& -E)$ .

5. If B is a literal or does not have the form -C, then RETURN B; else DISTNEG(B).

## ADDQU(B)

1. B(1) := B.

2. If B(1) has the form (D → E), then B(1) := (-D v E).

3. DISTNEG(B(1)).

4. Add B(1) to QU, if B(1) is not a literal.

5. If any node in DGR is labeled B, then label that node B(1).

SLDRA is as follows: Statement B is to be added to DGR; B may be molecular and DGR may be empty; assume QU is empty, but if DGR is not empty, then LI need not be empty.

## SLDRA

1. Eliminate any biconditionals, $(\mathbf{C} \leftrightarrow \mathbf{D})$ , in $\mathbf{B}$ in favor of $((\mathbf{C} \rightarrow \mathbf{D})$ & $(\mathbf{D} \rightarrow \mathbf{C})$ . Call the resulting formula $\mathbf{B}$ .

2. DISTNEG(B).

3. If B has the form (C v D), let $B := (-C \rightarrow D)$ .

4. If B has the form $(C \rightarrow D)$ , then add $[C] \rightarrow [D]$ and $[-D] \rightarrow [-C]$ to DGR. Call DISTNEG() then ADDQU() on each of the four formulae added as nodes.

5. If B has the form (C & D), then add to DGR:

![](/api/attachments/ET6FCQHG/fulltext/images/b8c9795e0a967ab2587a9345b3ae391aeb6ebfac3596518060ecdf7e4e88ec2e.jpg)  
Fig. 3.

![](/api/attachments/ET6FCQHG/fulltext/images/78700ed600d163bd6499b68ff9bb61b9736677a091b001eee9d017c977acfe81.jpg)

after calling DISTNEG) then ADDQU() on each of $(-C \lor -D)$ , C, -C, D, and -D. If B was not drawn from QU, add B to LI.

6. If B has the form (C v D), and thus was drawn from QU, add to DGR:

![](/api/attachments/ET6FCQHG/fulltext/images/fa9aaa19ae48321d087acebe2e39d2e1874b3cdb4ad5ac61d8db6be68c5ecf09.jpg)  
Fig. 4.

Call DISTNEG() then ADDQU() on each of C, -C, D, and -D.

7. If B is a literal, and thus was not drawn from QU, add [B] and [-B] to DGR, after calling DISTNEG() on B and on -B, and add B to LI.

8. If QU is empty, stop; else draw the next customer from QU, call it B and go to step 5.

Before discussing SLDRA, we need CC, the consistency criterion.

## cc

Assume the SLDRA has been run and DGR and LI are present.

1. Apply the AND rule throughout DGR: if in DGR we have:

![](/api/attachments/ET6FCQHG/fulltext/images/c9ce3e06f1143e7e3e53e33764203349a8361f2c522c84fe1df3d6ef35eaedf4.jpg)  
Fig. 5.

and both C and D appear in LI, then add (C & D) to LI.

2. Apply the OR rule throughout DGR: if in DGR we have:

![](/api/attachments/ET6FCQHG/fulltext/images/d1a66c6e65af4943b3531fcad2078606bb5a1cefaea26bbfc5eb227e6758f1fc.jpg)

Fig. 6.

and either C or D appear in LI, or C = -D, then add (C v D) for LI.

3. For each pair of nodes in DGR, [C] and [D], determine whether there is a directed path from [C] to [D]. Floyd's algorithm might be used to perform this task.

4. Count (DGR, LI) as inconsistent if and only if there are directed paths from some basic assertion (i.e., member of LI) to both [C] and [-C], where C and -C are literals. LI can be augmented to include any assertion corresponding to a node that is reachable from the node corresponding to a member of LI. (In other words, if F belongs to LI, and [F] → [G] belongs to DGR, then add G to LI.)

As is shown in Appendix B, (DGR, LI) is inconsistent if and only if the collection of axioms represented by SLDRA is inconsistent. This logic graph method is, in other words, a full theorem-proving method for sentence logic.

## 7. Appendix B: Proofs of Correctness

The purpose of this appendix is to sketch a series of proofs, which establish the correctness of the logic graph method for sentence logic.

Notice, first of all, that SLDRA always terminates, assuming that the axiom set it is handling, AXIOM, is finite. Only molecules enter QU and the main connective of these molecules is either &/or v, so that the molecules are further broken down in steps 5 and 6. Second, notice that all molecules appearing in AXIOM are broken down into their constituent literals by SLDRA. If B is an atom appearing in AXIOM (whether or not B appears in atomic form), then both B and -B appear as nodes in DGR, after SLDRA has operated on AXIOM. The consistency criterion, CC, performs its crucial test on literals, which is something easy to implement on a computer.

Proposition 1: Under the intended interpretation, (DGR, LI) is logically equivalent to AXIOM.

The intended interpretation is that every entry in LI is to be asserted and that every node-arc combination, $[B] \rightarrow [C]$ , is to be asserted as $(B \rightarrow C)$ .

The proof of this proposition can be had by stepping through SLDRA and CC (AND and OR rules), and noting that every transformation produces a result that is logically equivalent to the input formula. For example, consider step 5 of SLDRA. The formula, (C & D) is transformed into a graph, whose intended interpretation is:

$$
\begin{array}{l}\left( \right.\left( \right.\mathbf {C} \&\mathbf {D}\left. \right)\rightarrow \mathbf {C}\left. \right) \&\left( \right.\left( \right.\mathbf {C} \&\mathbf {D}\left. \right)\rightarrow \mathbf {D}\left. \right) \&(- \mathbf {C} \rightarrow\\\left(- \mathbf {C} \vee - \mathbf {D}\right)) \&(- \mathbf {D} \rightarrow (- \mathbf {C} \vee - \mathbf {D}))\end{array}
$$

which is a tautology. If (C & D) is to be asserted, i.e., if it is the B we are adding or if it is reachable from some other asserted node, then (C & D) will appear in LI, and if not, not.

Proposition 2: If SLDRA and CC together indicate that AXIOM is inconsistent, then AXIOM is inconsistent.

Given Proposition 1, the proof is more or less immediate. AXIOM is logically equivalent to (DGR, LI). Moreover, the AND and OR rules in CC are truth-preserving or valid rules, so the augmentation of LI preserves equivalence. Finally, finding a path from a member of LI to any other formula, including a literal, is equivalent (under the interpretation) to concluding C from B and (B → C). This is just the rule of modus ponens and is quite valid.

Proposition 3: If AXIOM is inconsistent, then SLDRA and CC will together indicate that AXIOM is inconsistent.

Propositions 2 and 3 together imply that the logic graph method for sentence logic is entirely equivalent to sentence logic.

What needs to be shown to prove Proposition 3 is that if sentence logic can derive a formula, logic graphs can too. If this can be shown, then it would follow that if sentence logic can derive any literal, so can logic graphs. The proof method for logic graphs is a proof by contradiction, based on deriving inconsistent literals. Thus, showing that anything derivable by sentence logic is derivable by logic graphs is to prove this proposition.

I will argue, then, that any transformation of a set of axioms that is possible in sentence logic is also possible in logic graphs. Since proofs in sentence logic are just transformations of axioms, this suffices to show that sentence logic is equivalent to logic graphs, providing we account for the axioms of sentence logic and show how they are handled in logic graphs.

I will use a particular formulation of sentence logic, although this is not essential. The formulation I will use is called PM, for Principia Mathematica. It is the formulation of sentence logic made by Russell and Whitehead following the revision in [22]. PM has four axioms and two rules, as follows:

1. $(\mathbf{P} \vee \mathbf{P}) \to \mathbf{P}$

2. $\mathbf{Q}\rightarrow (\mathbf{P}\vee \mathbf{Q})$

3. (P v Q) → (Q v P)

4. $(\mathbf{Q}\to \mathbf{R})\rightarrow ((\mathbf{P}\lor \mathbf{Q})\rightarrow (\mathbf{P}\lor \mathbf{R}))$

TR1: The result of uniformly replacing any variable in a thesis by any well-formed formula is itself a thesis. (A thesis is either an axiom or a theorem. This is called the rule of uniform substitution.)

TR2: If B and $(B \rightarrow C)$ are theses, so is C. (This is called the rule of modus ponens.)

Under the intended interpretation, every member of LI (as augmented by CC) is a thesis and every node-arc combination, $[B] \rightarrow [C]$ , is the thesis $(B \rightarrow C)$ . CC tells us to follow the rule of modus ponens. So, it is immediate that TR2 is covered by the logic graph method.

To understand why TR1 is covered by the logic graph method, consider the following. We have a collection of axioms and a conclusion, B, that happens to follow from these axioms. We add -B to the axioms, run SLDRA and CC on the system, and find that it is inconsistent, thereby showing that B follows from the axioms. Now, we perform the uniform substitution on some atom (i.e., variable). Is the result provably a thesis by the logic graph method, i.e., is the result still inconsistent?

There are three cases. First, if the formula we substitute in is a literal, then clearly all we have done is to rename some variables and inconsistency at the literal level will remain.

Second, if the formula we substitute in, B, is not a literal and the atom that we replaced uniformly did not figure in the contradiction (i.e., if C was the atom, then we could not show both C and -C in the original run of SLDRA and CC), then again it is immediate that the result of the substitution will produce a contradiction at the literal level.

The third case is when the formula we substitute in, B, is molecular and the atom we replace figures in the determination of inconsistency. To see that the desired result obtains, imagine that we perform the substitution on DGR and LI, after SLDRA and CC have been run. (Recall that they produce a result logically equivalent to the original axioms.) At this point, by hypothesis, we can derive both B and -B. But, B is not a literal, so the algorithm is not completed. We call DISTNEG() and ADDQU() on B and -B, and we proceed to step 5 of SLDRA. When we complete the algorithm, B and -B will be fully analyzed down to their constituent literals and contradictions at the literal level will arise. To see this, assume that B has the form (E & F). The full logic graph for B would be as follows.

![](/api/attachments/ET6FCQHG/fulltext/images/d83ccc52a45e6a87077a4fe5471a20c74e3643dd9244fb5d89f7c2e740791e65.jpg)  
Fig. 7.

Using CC, and recalling that B (= (E & F)) and -B (= (-E v -F) = DISTNEG(-(E & F))) are derivable, we see that E, F, -E, and -F are derivable now. The story is similar when the main connective of B is v. If, then, either E or F are literals, we find a contradiction at the literal level. If not, we continue the algorithm and the story repeats itself until we do find a contradiction at the literal level. I conclude that TR1 is in fact implemented by the logic graph method.

Finally, we have to prove the four axioms of PM. That is easy and I leave it to the reader as an exercise. Simply take the axioms one at a time, negate them, apply the algorithms, and you will obtain a contradiction at the literal level. To illustrate, the second axiom is $(Q \rightarrow (P \lor Q))$ . Negated it is: $(Q \& -(P \lor Q))$ , after calling DISTNEG. The graph, in part, for this is:

![](/api/attachments/ET6FCQHG/fulltext/images/74f1985b56e123a58b509af617e9a44bbc62f499d8d0480ca844d8fcaa924fb7.jpg)  
Fig. 8.

LI contains (Q & -(P v Q)) and CC finds the contradiction.

It is safe to conclude that the logic graph method, as described above, is fully equivalent to sentence logic.

## Acknowledgements

I would like to thank several people for reading and commenting upon an earlier version of this paper: Richard Cartwright, John Henderson, Christopher Jones, Ronald M. Lee, Thomas Malone, and Jeff Meldman. The logic graph concept was originally presented at the KROT meetings in Portugal, September 1983, and benefitted from the discussions there. This research was supported in part by the Atlantic Richfield Foundation.

## References

[1] Mitroff, I.I., R.O. Mason and V.P. Barabba, Policy as Argument - A Logic for Ill-Structured Decision Problems, Management Sci. 28 (Dec. 1982) 1391-1404.

[2] Locks, M.O., The Logic of Policy as Argument, Management Sci. 31 (Jan. 1985) 109–114.

[3] Kimbrough, S.O., Text Symbolization Projects for Investigations of Logic Programming, University of Pennsylvania, Dept. Decision Sciences, working paper 85-06-01 (1985).

[4] Quine, W. Van Orman, Methods of Logic, 4th ed., p. 112, Harvard University Press, Cambridge MA (1982).

[5] Dolk, D.R., and Konsynski, B.R., Knowledge Representation for Model Management Systems, IEEE Trans. Soft. Eng. SE-10 (Nov. 1984) 619–628.

[6] Blanning, R.W., A Relational Framework for Model Management in Decision Support Systems, DSS-82: Transactions of the Second International Conference on Decision Support Systems, G.W. Dickson, ed. (1982).

[7] Elam, J.J., Henderson, J.C., and Miller, L.W., Model Management Systems: An Approach to Decision Support in Complex Organizations, University of Pennsylvania, Dept. Decision Sciences, working paper 80-08-04 (1980).

[8] Elam, J.J., Model Management Systems: A Framework for Development, University of Pennsylvania, Dept. Decision Sciences, working paper 79-2-04 (1979).

[9] Findler, N.V., Ed., Associative Networks – The Representation and Use of Knowledge in Computers, Academic Press, New York (1979).

[10] Nilsson, N.J., Principles of Artificial Intelligence, Tioga Publ. Co., Palo Alto, CA (1980).

[11] Winston, P.H., Artificial Intelligence, 2nd edn. Addison-Wesley, Reading, MA (1984).

[12] Aspvall, B., Plass, M.F., and Tarjan, R.E., A Linear-Time Algorithm for Testing the Truth of Certain Quantified Boolean Formulas, Informat. Proc. Lett. 8 (1979) 121–123.

[13] Hansen, P., Jaumard, B. and Minous, M., A Linear Expected-Time Algorithm for Deriving All Logical Conclusions Implied by a Set of Boolean Inequalities, mimeo (1984).

[14] Floyd, R.W., Algorithm 97: Shortest Path, Comm. ACM 5 (1962) 345.

[15] Aho, A.V., Hopcroft, J.E. and Ullman, J.D., Data Structures and Algorithms, Addison-Wesley, Reading, MA (1983).

[16] Lee, R.M., CANDID Description of Commercial and Financial Concepts: A Formal Semantics Approach to Knowledge Representation, International Institute for Applied Systems Analysis, Laxenburg, Austria, working paper (Dec. 1981).

[17] Bonczek, R.H., Holsapple, C.W. and Whinston, A.B., Foundations of Decision Support Systems, Academic Press, New York (1981).

[18] Henderson, J.C., Rockart, J.F. and Sifonis, J.G., A Planning Methodology for Integrating Management Support Systems, Massachusetts Institute of Technology, Center for Information Systems Research, working paper 116 (1984).

[19] Fisher, S.D., Gettys, C.F., Manning, C. Mehle, T. and Baca, S. Consistency Checking in Hypothesis Generation, Organizat. Behav. Human Perform. 31 (1983) 233–254.

[20] Quine, W. Van Orman, Elementary Logic, p. 56 Revised Edition, Harvard University Press, Cambridge MA (1980).

[21] Clocksin, W.F. and Mellish, C.S., Programming in Prolog, p. 238, Springer-Verlag, New York (1984).

[22] Hughes, G.E. and Cresswell, M.J., An Introduction to Modal Logic, Methuen, London (1972).
